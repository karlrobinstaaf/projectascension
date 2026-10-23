"""Deterministic semantic assertions for Aurora validation evidence.

The module evaluates validator-owned snapshot state and structural transitions.
Assertions describe required properties, bounded numeric envelopes, and
provenance requirements without prescribing Aurora's dialogue or internal
implementation.  Expected values and captured actual values remain in the
validator partition; evidence summaries expose only hashes and outcomes.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Final, cast

from aurora_validation_harness.evidence import (
    EvidenceDomain,
    EvidencePayload,
    EvidenceSource,
    EvidenceSourceKind,
    create_evidence_payload,
)
from aurora_validation_harness.snapshots import StateSnapshot
from aurora_validation_harness.transitions import (
    ChangeOperation,
    StateTransition,
    TransitionStatus,
)

SUPPORTED_ASSERTION_SCHEMA_VERSION: Final[str] = "1.0"
DEFAULT_MAX_ASSERTION_VALUE_BYTES: Final[int] = 1_048_576
MAX_ASSERTION_VALUE_BYTES: Final[int] = 16_777_216
MAX_ASSERTION_ALLOWED_VALUES: Final[int] = 4_096
MAX_ASSERTION_RESULTS: Final[int] = 1_000_000
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_JSON_POINTER_PATTERN: Final[re.Pattern[str]] = re.compile(r"^(?:/(?:[^~]|~[01])*)+$")
_MISSING: Final[object] = object()


class AssertionError(ValueError):
    """Raised when an assertion contract, evaluation, or result chain is invalid."""


class AssertionSeverity(StrEnum):
    """Canonical severity assigned if an assertion is not satisfied."""

    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    S4 = "S4"


class InvariantClass(StrEnum):
    """Canonical enforcement class of the referenced invariant."""

    HARD = "HARD"
    SOFT = "SOFT"
    CONTEXTUAL = "CONTEXTUAL"


class AssertionStatus(StrEnum):
    """Machine-readable outcome of one assertion evaluation."""

    PASS = "PASS"
    FAIL = "FAIL"
    REVIEW = "REVIEW"
    BLOCKED = "BLOCKED"


class AssertionTargetKind(StrEnum):
    """Supported validator-owned evidence target classes."""

    SNAPSHOT = "SNAPSHOT"
    TRANSITION = "TRANSITION"


class AssertionValueType(StrEnum):
    """JSON value categories used by snapshot type assertions."""

    NULL = "NULL"
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    NUMBER = "NUMBER"
    STRING = "STRING"
    ARRAY = "ARRAY"
    OBJECT = "OBJECT"


class SnapshotAssertionOperator(StrEnum):
    """Deterministic predicates available for captured snapshot state."""

    EXISTS = "EXISTS"
    ABSENT = "ABSENT"
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    TYPE_IS = "TYPE_IS"
    NUMBER_RANGE = "NUMBER_RANGE"
    ONE_OF = "ONE_OF"


class TransitionAssertionOperator(StrEnum):
    """Deterministic predicates available for structural state transitions."""

    PATH_CHANGED = "PATH_CHANGED"
    PATH_UNCHANGED = "PATH_UNCHANGED"
    OPERATION_IS = "OPERATION_IS"
    STATUS_IS = "STATUS_IS"
    CHANGES_HAVE_CAUSE = "CHANGES_HAVE_CAUSE"
    CHANGES_HAVE_CAUSE_KIND = "CHANGES_HAVE_CAUSE_KIND"


class PathMatchMode(StrEnum):
    """Whether a transition assertion addresses one path or its full subtree."""

    EXACT = "EXACT"
    SUBTREE = "SUBTREE"


class AssertionReason(StrEnum):
    """Stable explanation code for a deterministic assertion outcome."""

    PATH_FOUND = "PATH_FOUND"
    PATH_NOT_FOUND = "PATH_NOT_FOUND"
    VALUES_EQUAL = "VALUES_EQUAL"
    VALUES_DIFFER = "VALUES_DIFFER"
    TYPE_MATCH = "TYPE_MATCH"
    TYPE_MISMATCH = "TYPE_MISMATCH"
    VALUE_IN_RANGE = "VALUE_IN_RANGE"
    VALUE_OUT_OF_RANGE = "VALUE_OUT_OF_RANGE"
    VALUE_ALLOWED = "VALUE_ALLOWED"
    VALUE_NOT_ALLOWED = "VALUE_NOT_ALLOWED"
    PATH_CHANGED = "PATH_CHANGED"
    PATH_UNCHANGED = "PATH_UNCHANGED"
    OPERATION_MATCH = "OPERATION_MATCH"
    OPERATION_MISMATCH = "OPERATION_MISMATCH"
    STATUS_MATCH = "STATUS_MATCH"
    STATUS_MISMATCH = "STATUS_MISMATCH"
    CAUSE_PRESENT = "CAUSE_PRESENT"
    CAUSE_MISSING = "CAUSE_MISSING"
    CAUSE_KIND_PRESENT = "CAUSE_KIND_PRESENT"
    CAUSE_KIND_MISSING = "CAUSE_KIND_MISSING"


@dataclass(frozen=True, slots=True)
class AssertionValue:
    """Canonical validator-owned JSON value used by a definition or result."""

    value_json: bytes
    value_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.value_json, bytes):
            raise AssertionError("value_json must be bytes")
        _validate_sha256(self.value_sha256, field="value_sha256")
        if hashlib.sha256(self.value_json).hexdigest() != self.value_sha256:
            raise AssertionError("value_sha256 does not match value_json")
        if len(self.value_json) > MAX_ASSERTION_VALUE_BYTES:
            raise AssertionError(f"value_json must not exceed {MAX_ASSERTION_VALUE_BYTES} bytes")

        decoded = _decode_json_value(self.value_json)
        _validate_json_value(decoded, path="value")
        if self.value_json != _canonical_json_bytes(decoded):
            raise AssertionError("value_json must use canonical JSON encoding")

    @property
    def size_bytes(self) -> int:
        """Return the exact canonical value size."""

        return len(self.value_json)

    def decode(self) -> object:
        """Return a fresh decoded JSON value."""

        return _decode_json_value(self.value_json)

    def to_mapping(self) -> dict[str, object]:
        """Return the portable value representation."""

        return {"data": self.decode(), "value_sha256": self.value_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> AssertionValue:
        """Parse and verify one portable assertion value."""

        mapping = _require_mapping(value, field="assertion value")
        _require_exact_keys(
            mapping,
            required=frozenset({"data", "value_sha256"}),
            field="assertion value",
        )
        declared_sha256 = _require_string(
            mapping["value_sha256"],
            field="assertion value.value_sha256",
        )
        assertion_value = create_assertion_value(
            mapping["data"],
            max_value_bytes=MAX_ASSERTION_VALUE_BYTES,
        )
        if assertion_value.value_sha256 != declared_sha256:
            raise AssertionError("declared value_sha256 does not match assertion value")
        return assertion_value


@dataclass(frozen=True, slots=True)
class SnapshotAssertion:
    """Immutable predicate over one RFC 6901 path in a state snapshot."""

    assertion_id: str
    invariant_id: str
    invariant_class: InvariantClass
    severity: AssertionSeverity
    operator: SnapshotAssertionOperator
    path: str
    expected: AssertionValue | None = None
    expected_type: AssertionValueType | None = None
    minimum: int | float | None = None
    maximum: int | float | None = None
    minimum_inclusive: bool = True
    maximum_inclusive: bool = True
    allowed_values: tuple[AssertionValue, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.assertion_id, field="assertion_id")
        _validate_control_id(self.invariant_id, field="invariant_id")
        if not isinstance(self.invariant_class, InvariantClass):
            raise AssertionError("invariant_class must be an InvariantClass value")
        if not isinstance(self.severity, AssertionSeverity):
            raise AssertionError("severity must be an AssertionSeverity value")
        if not isinstance(self.operator, SnapshotAssertionOperator):
            raise AssertionError("operator must be a SnapshotAssertionOperator value")
        _validate_json_pointer(self.path)
        if self.expected is not None and not isinstance(self.expected, AssertionValue):
            raise AssertionError("expected must be null or an AssertionValue")
        if self.expected_type is not None and not isinstance(
            self.expected_type, AssertionValueType
        ):
            raise AssertionError("expected_type must be null or an AssertionValueType")
        _validate_optional_number(self.minimum, field="minimum")
        _validate_optional_number(self.maximum, field="maximum")
        if not isinstance(self.minimum_inclusive, bool):
            raise AssertionError("minimum_inclusive must be a boolean")
        if not isinstance(self.maximum_inclusive, bool):
            raise AssertionError("maximum_inclusive must be a boolean")
        if not isinstance(self.allowed_values, tuple) or not all(
            isinstance(item, AssertionValue) for item in self.allowed_values
        ):
            raise AssertionError("allowed_values must be a tuple of AssertionValue values")
        if len(self.allowed_values) > MAX_ASSERTION_ALLOWED_VALUES:
            raise AssertionError(
                f"allowed_values must not exceed {MAX_ASSERTION_ALLOWED_VALUES} entries"
            )
        allowed_hashes = tuple(item.value_sha256 for item in self.allowed_values)
        if len(allowed_hashes) != len(set(allowed_hashes)):
            raise AssertionError("allowed_values must not contain duplicate values")
        if allowed_hashes != tuple(sorted(allowed_hashes)):
            raise AssertionError("allowed_values must be ordered by value_sha256")
        self._validate_operator_contract()

    def _validate_operator_contract(self) -> None:
        has_expected = self.expected is not None
        has_type = self.expected_type is not None
        has_bounds = self.minimum is not None or self.maximum is not None
        has_allowed = bool(self.allowed_values)
        has_nondefault_bound_mode = not (self.minimum_inclusive and self.maximum_inclusive)

        if self.operator in {SnapshotAssertionOperator.EXISTS, SnapshotAssertionOperator.ABSENT}:
            if has_expected or has_type or has_bounds or has_allowed or has_nondefault_bound_mode:
                raise AssertionError(f"{self.operator.value} does not accept value constraints")
        elif self.operator in {
            SnapshotAssertionOperator.EQUALS,
            SnapshotAssertionOperator.NOT_EQUALS,
        }:
            if (
                not has_expected
                or has_type
                or has_bounds
                or has_allowed
                or has_nondefault_bound_mode
            ):
                raise AssertionError(f"{self.operator.value} requires only one expected value")
        elif self.operator is SnapshotAssertionOperator.TYPE_IS:
            if (
                has_expected
                or not has_type
                or has_bounds
                or has_allowed
                or has_nondefault_bound_mode
            ):
                raise AssertionError("TYPE_IS requires only expected_type")
        elif self.operator is SnapshotAssertionOperator.NUMBER_RANGE:
            if has_expected or has_type or not has_bounds or has_allowed:
                raise AssertionError("NUMBER_RANGE requires at least one numeric bound")
            if self.minimum is None and not self.minimum_inclusive:
                raise AssertionError("minimum_inclusive requires a minimum bound")
            if self.maximum is None and not self.maximum_inclusive:
                raise AssertionError("maximum_inclusive requires a maximum bound")
            if self.minimum is not None and self.maximum is not None:
                if self.minimum > self.maximum:
                    raise AssertionError("minimum must not exceed maximum")
                if self.minimum == self.maximum and not (
                    self.minimum_inclusive and self.maximum_inclusive
                ):
                    raise AssertionError("equal bounds must both be inclusive")
        elif has_expected or has_type or has_bounds or not has_allowed or has_nondefault_bound_mode:
            raise AssertionError("ONE_OF requires only one or more allowed_values")

    @property
    def assertion_sha256(self) -> str:
        """Return the digest of the complete validator-owned predicate."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "allowed_values": [item.to_mapping() for item in self.allowed_values],
            "assertion_id": self.assertion_id,
            "assertion_schema_version": SUPPORTED_ASSERTION_SCHEMA_VERSION,
            "assertion_type": "SNAPSHOT_ASSERTION",
            "expected": None if self.expected is None else self.expected.to_mapping(),
            "expected_type": None if self.expected_type is None else self.expected_type.value,
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "maximum": self.maximum,
            "maximum_inclusive": self.maximum_inclusive,
            "minimum": self.minimum,
            "minimum_inclusive": self.minimum_inclusive,
            "operator": self.operator.value,
            "path": self.path,
            "severity": self.severity.value,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable snapshot-assertion representation."""

        return {**self._content_mapping(), "assertion_sha256": self.assertion_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> SnapshotAssertion:
        """Parse and verify a serialized snapshot assertion."""

        mapping = _require_mapping(value, field="snapshot assertion")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "allowed_values",
                    "assertion_id",
                    "assertion_schema_version",
                    "assertion_sha256",
                    "assertion_type",
                    "expected",
                    "expected_type",
                    "invariant_class",
                    "invariant_id",
                    "maximum",
                    "maximum_inclusive",
                    "minimum",
                    "minimum_inclusive",
                    "operator",
                    "path",
                    "severity",
                }
            ),
            field="snapshot assertion",
        )
        _validate_schema_version(mapping["assertion_schema_version"])
        if mapping["assertion_type"] != "SNAPSHOT_ASSERTION":
            raise AssertionError("unsupported assertion_type")
        assertion = cls(
            assertion_id=_require_string(
                mapping["assertion_id"], field="snapshot assertion.assertion_id"
            ),
            invariant_id=_require_string(
                mapping["invariant_id"], field="snapshot assertion.invariant_id"
            ),
            invariant_class=_parse_enum(
                InvariantClass,
                mapping["invariant_class"],
                field="snapshot assertion.invariant_class",
            ),
            severity=_parse_enum(
                AssertionSeverity,
                mapping["severity"],
                field="snapshot assertion.severity",
            ),
            operator=_parse_enum(
                SnapshotAssertionOperator,
                mapping["operator"],
                field="snapshot assertion.operator",
            ),
            path=_require_string(mapping["path"], field="snapshot assertion.path"),
            expected=_parse_optional_assertion_value(
                mapping["expected"], field="snapshot assertion.expected"
            ),
            expected_type=_parse_optional_enum(
                AssertionValueType,
                mapping["expected_type"],
                field="snapshot assertion.expected_type",
            ),
            minimum=_require_optional_number(
                mapping["minimum"], field="snapshot assertion.minimum"
            ),
            maximum=_require_optional_number(
                mapping["maximum"], field="snapshot assertion.maximum"
            ),
            minimum_inclusive=_require_boolean(
                mapping["minimum_inclusive"],
                field="snapshot assertion.minimum_inclusive",
            ),
            maximum_inclusive=_require_boolean(
                mapping["maximum_inclusive"],
                field="snapshot assertion.maximum_inclusive",
            ),
            allowed_values=_parse_assertion_values(
                mapping["allowed_values"], field="snapshot assertion.allowed_values"
            ),
        )
        _validate_declared_sha256(assertion.assertion_sha256, mapping, field="snapshot assertion")
        return assertion


@dataclass(frozen=True, slots=True)
class TransitionAssertion:
    """Immutable predicate over one structural state transition."""

    assertion_id: str
    invariant_id: str
    invariant_class: InvariantClass
    severity: AssertionSeverity
    operator: TransitionAssertionOperator
    path: str | None = None
    match_mode: PathMatchMode = PathMatchMode.EXACT
    expected_operation: ChangeOperation | None = None
    expected_status: TransitionStatus | None = None
    required_cause_kind: EvidenceSourceKind | None = None

    def __post_init__(self) -> None:
        _validate_control_id(self.assertion_id, field="assertion_id")
        _validate_control_id(self.invariant_id, field="invariant_id")
        if not isinstance(self.invariant_class, InvariantClass):
            raise AssertionError("invariant_class must be an InvariantClass value")
        if not isinstance(self.severity, AssertionSeverity):
            raise AssertionError("severity must be an AssertionSeverity value")
        if not isinstance(self.operator, TransitionAssertionOperator):
            raise AssertionError("operator must be a TransitionAssertionOperator value")
        if self.path is not None:
            _validate_json_pointer(self.path)
        if not isinstance(self.match_mode, PathMatchMode):
            raise AssertionError("match_mode must be a PathMatchMode value")
        if self.expected_operation is not None and not isinstance(
            self.expected_operation, ChangeOperation
        ):
            raise AssertionError("expected_operation must be null or a ChangeOperation")
        if self.expected_status is not None and not isinstance(
            self.expected_status, TransitionStatus
        ):
            raise AssertionError("expected_status must be null or a TransitionStatus")
        if self.required_cause_kind is not None and not isinstance(
            self.required_cause_kind, EvidenceSourceKind
        ):
            raise AssertionError("required_cause_kind must be null or an EvidenceSourceKind")
        self._validate_operator_contract()

    def _validate_operator_contract(self) -> None:
        path_operators = {
            TransitionAssertionOperator.PATH_CHANGED,
            TransitionAssertionOperator.PATH_UNCHANGED,
            TransitionAssertionOperator.OPERATION_IS,
        }
        if self.operator in path_operators:
            if self.path is None:
                raise AssertionError(f"{self.operator.value} requires path")
        elif self.path is not None or self.match_mode is not PathMatchMode.EXACT:
            raise AssertionError(f"{self.operator.value} does not accept path matching")

        if self.operator is TransitionAssertionOperator.OPERATION_IS:
            if self.expected_operation is None:
                raise AssertionError("OPERATION_IS requires expected_operation")
        elif self.expected_operation is not None:
            raise AssertionError(f"{self.operator.value} does not accept expected_operation")

        if self.operator is TransitionAssertionOperator.STATUS_IS:
            if self.expected_status is None:
                raise AssertionError("STATUS_IS requires expected_status")
        elif self.expected_status is not None:
            raise AssertionError(f"{self.operator.value} does not accept expected_status")

        if self.operator is TransitionAssertionOperator.CHANGES_HAVE_CAUSE_KIND:
            if self.required_cause_kind is None:
                raise AssertionError("CHANGES_HAVE_CAUSE_KIND requires required_cause_kind")
        elif self.required_cause_kind is not None:
            raise AssertionError(f"{self.operator.value} does not accept required_cause_kind")

    @property
    def assertion_sha256(self) -> str:
        """Return the digest of the complete validator-owned predicate."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "assertion_id": self.assertion_id,
            "assertion_schema_version": SUPPORTED_ASSERTION_SCHEMA_VERSION,
            "assertion_type": "TRANSITION_ASSERTION",
            "expected_operation": (
                None if self.expected_operation is None else self.expected_operation.value
            ),
            "expected_status": None if self.expected_status is None else self.expected_status.value,
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "match_mode": self.match_mode.value,
            "operator": self.operator.value,
            "path": self.path,
            "required_cause_kind": (
                None if self.required_cause_kind is None else self.required_cause_kind.value
            ),
            "severity": self.severity.value,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable transition-assertion representation."""

        return {**self._content_mapping(), "assertion_sha256": self.assertion_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> TransitionAssertion:
        """Parse and verify a serialized transition assertion."""

        mapping = _require_mapping(value, field="transition assertion")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "assertion_id",
                    "assertion_schema_version",
                    "assertion_sha256",
                    "assertion_type",
                    "expected_operation",
                    "expected_status",
                    "invariant_class",
                    "invariant_id",
                    "match_mode",
                    "operator",
                    "path",
                    "required_cause_kind",
                    "severity",
                }
            ),
            field="transition assertion",
        )
        _validate_schema_version(mapping["assertion_schema_version"])
        if mapping["assertion_type"] != "TRANSITION_ASSERTION":
            raise AssertionError("unsupported assertion_type")
        assertion = cls(
            assertion_id=_require_string(
                mapping["assertion_id"], field="transition assertion.assertion_id"
            ),
            invariant_id=_require_string(
                mapping["invariant_id"], field="transition assertion.invariant_id"
            ),
            invariant_class=_parse_enum(
                InvariantClass,
                mapping["invariant_class"],
                field="transition assertion.invariant_class",
            ),
            severity=_parse_enum(
                AssertionSeverity,
                mapping["severity"],
                field="transition assertion.severity",
            ),
            operator=_parse_enum(
                TransitionAssertionOperator,
                mapping["operator"],
                field="transition assertion.operator",
            ),
            path=_require_optional_string(mapping["path"], field="transition assertion.path"),
            match_mode=_parse_enum(
                PathMatchMode,
                mapping["match_mode"],
                field="transition assertion.match_mode",
            ),
            expected_operation=_parse_optional_enum(
                ChangeOperation,
                mapping["expected_operation"],
                field="transition assertion.expected_operation",
            ),
            expected_status=_parse_optional_enum(
                TransitionStatus,
                mapping["expected_status"],
                field="transition assertion.expected_status",
            ),
            required_cause_kind=_parse_optional_enum(
                EvidenceSourceKind,
                mapping["required_cause_kind"],
                field="transition assertion.required_cause_kind",
            ),
        )
        _validate_declared_sha256(assertion.assertion_sha256, mapping, field="transition assertion")
        return assertion


@dataclass(frozen=True, slots=True)
class AssertionResult:
    """One immutable, target-bound assertion evaluation result."""

    result_id: str
    run_id: str
    scenario_id: str
    sequence: int
    evaluated_at_tick: int
    assertion_id: str
    assertion_sha256: str
    invariant_id: str
    invariant_class: InvariantClass
    severity: AssertionSeverity
    target_kind: AssertionTargetKind
    target_id: str
    target_sha256: str
    target_domain: EvidenceDomain
    status: AssertionStatus
    reason: AssertionReason
    path: str | None
    actual: AssertionValue | None
    previous_result_sha256: str | None

    def __post_init__(self) -> None:
        _validate_control_id(self.result_id, field="result_id")
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        _validate_sequence(self.sequence, field="sequence")
        _validate_tick(self.evaluated_at_tick, field="evaluated_at_tick")
        _validate_control_id(self.assertion_id, field="assertion_id")
        _validate_sha256(self.assertion_sha256, field="assertion_sha256")
        _validate_control_id(self.invariant_id, field="invariant_id")
        if not isinstance(self.invariant_class, InvariantClass):
            raise AssertionError("invariant_class must be an InvariantClass value")
        if not isinstance(self.severity, AssertionSeverity):
            raise AssertionError("severity must be an AssertionSeverity value")
        if not isinstance(self.target_kind, AssertionTargetKind):
            raise AssertionError("target_kind must be an AssertionTargetKind value")
        _validate_control_id(self.target_id, field="target_id")
        _validate_sha256(self.target_sha256, field="target_sha256")
        if not isinstance(self.target_domain, EvidenceDomain):
            raise AssertionError("target_domain must be an EvidenceDomain value")
        if not isinstance(self.status, AssertionStatus):
            raise AssertionError("status must be an AssertionStatus value")
        if not isinstance(self.reason, AssertionReason):
            raise AssertionError("reason must be an AssertionReason value")
        if self.path is not None:
            _validate_json_pointer(self.path)
        if self.actual is not None and not isinstance(self.actual, AssertionValue):
            raise AssertionError("actual must be null or an AssertionValue")
        if self.previous_result_sha256 is not None:
            _validate_sha256(self.previous_result_sha256, field="previous_result_sha256")
        if self.sequence == 0 and self.previous_result_sha256 is not None:
            raise AssertionError("first assertion result must not declare a previous hash")
        if self.sequence > 0 and self.previous_result_sha256 is None:
            raise AssertionError("non-first assertion result requires a previous hash")

    @property
    def result_sha256(self) -> str:
        """Return the digest binding the assertion, target, outcome, and chain position."""

        return calculate_assertion_result_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "actual": None if self.actual is None else self.actual.to_mapping(),
            "assertion_id": self.assertion_id,
            "assertion_schema_version": SUPPORTED_ASSERTION_SCHEMA_VERSION,
            "assertion_sha256": self.assertion_sha256,
            "evaluated_at_tick": self.evaluated_at_tick,
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "path": self.path,
            "previous_result_sha256": self.previous_result_sha256,
            "reason": self.reason.value,
            "result_id": self.result_id,
            "result_type": "ASSERTION_RESULT",
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "sequence": self.sequence,
            "severity": self.severity.value,
            "status": self.status.value,
            "target_domain": self.target_domain.value,
            "target_id": self.target_id,
            "target_kind": self.target_kind.value,
            "target_sha256": self.target_sha256,
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete validator-owned result representation."""

        return {**self._content_mapping(), "result_sha256": self.result_sha256}

    def to_evidence_mapping(self) -> dict[str, object]:
        """Return a compact summary without expected or captured state values."""

        return {
            "actual_value_sha256": None if self.actual is None else self.actual.value_sha256,
            "assertion_id": self.assertion_id,
            "assertion_sha256": self.assertion_sha256,
            "evaluated_at_tick": self.evaluated_at_tick,
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "path": self.path,
            "reason": self.reason.value,
            "result_id": self.result_id,
            "result_sha256": self.result_sha256,
            "severity": self.severity.value,
            "status": self.status.value,
            "target_domain": self.target_domain.value,
            "target_id": self.target_id,
            "target_kind": self.target_kind.value,
            "target_sha256": self.target_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> AssertionResult:
        """Parse and verify a serialized assertion result."""

        mapping = _require_mapping(value, field="assertion result")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "actual",
                    "assertion_id",
                    "assertion_schema_version",
                    "assertion_sha256",
                    "evaluated_at_tick",
                    "invariant_class",
                    "invariant_id",
                    "path",
                    "previous_result_sha256",
                    "reason",
                    "result_id",
                    "result_sha256",
                    "result_type",
                    "run_id",
                    "scenario_id",
                    "sequence",
                    "severity",
                    "status",
                    "target_domain",
                    "target_id",
                    "target_kind",
                    "target_sha256",
                }
            ),
            field="assertion result",
        )
        _validate_schema_version(mapping["assertion_schema_version"])
        if mapping["result_type"] != "ASSERTION_RESULT":
            raise AssertionError("unsupported result_type")
        result = cls(
            result_id=_require_string(mapping["result_id"], field="assertion result.result_id"),
            run_id=_require_string(mapping["run_id"], field="assertion result.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"], field="assertion result.scenario_id"
            ),
            sequence=_require_integer(mapping["sequence"], field="assertion result.sequence"),
            evaluated_at_tick=_require_integer(
                mapping["evaluated_at_tick"], field="assertion result.evaluated_at_tick"
            ),
            assertion_id=_require_string(
                mapping["assertion_id"], field="assertion result.assertion_id"
            ),
            assertion_sha256=_require_string(
                mapping["assertion_sha256"], field="assertion result.assertion_sha256"
            ),
            invariant_id=_require_string(
                mapping["invariant_id"], field="assertion result.invariant_id"
            ),
            invariant_class=_parse_enum(
                InvariantClass,
                mapping["invariant_class"],
                field="assertion result.invariant_class",
            ),
            severity=_parse_enum(
                AssertionSeverity, mapping["severity"], field="assertion result.severity"
            ),
            target_kind=_parse_enum(
                AssertionTargetKind,
                mapping["target_kind"],
                field="assertion result.target_kind",
            ),
            target_id=_require_string(mapping["target_id"], field="assertion result.target_id"),
            target_sha256=_require_string(
                mapping["target_sha256"], field="assertion result.target_sha256"
            ),
            target_domain=_parse_enum(
                EvidenceDomain,
                mapping["target_domain"],
                field="assertion result.target_domain",
            ),
            status=_parse_enum(AssertionStatus, mapping["status"], field="assertion result.status"),
            reason=_parse_enum(AssertionReason, mapping["reason"], field="assertion result.reason"),
            path=_require_optional_string(mapping["path"], field="assertion result.path"),
            actual=_parse_optional_assertion_value(
                mapping["actual"], field="assertion result.actual"
            ),
            previous_result_sha256=_require_optional_string(
                mapping["previous_result_sha256"],
                field="assertion result.previous_result_sha256",
            ),
        )
        _validate_declared_sha256(result.result_sha256, mapping, field="assertion result")
        return result


@dataclass(frozen=True, slots=True)
class AssertionSeries:
    """Immutable append-only assertion-result chain for one validation run."""

    run_id: str
    scenario_id: str
    results: tuple[AssertionResult, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        if not isinstance(self.results, tuple) or not all(
            isinstance(result, AssertionResult) for result in self.results
        ):
            raise AssertionError("results must be a tuple of AssertionResult values")
        if len(self.results) > MAX_ASSERTION_RESULTS:
            raise AssertionError(f"results must not exceed {MAX_ASSERTION_RESULTS} entries")

        seen_result_ids: set[str] = set()
        previous_result: AssertionResult | None = None
        for expected_sequence, result in enumerate(self.results):
            if result.run_id != self.run_id or result.scenario_id != self.scenario_id:
                raise AssertionError("result identity does not match assertion series")
            if result.sequence != expected_sequence:
                raise AssertionError("result sequence must be contiguous and start at zero")
            if result.result_id in seen_result_ids:
                raise AssertionError("result_id values must be unique within a series")
            if previous_result is None:
                if result.previous_result_sha256 is not None:
                    raise AssertionError("first series result must not reference a previous hash")
            else:
                if result.evaluated_at_tick < previous_result.evaluated_at_tick:
                    raise AssertionError("results must use nondecreasing evaluated_at_tick values")
                if result.previous_result_sha256 != previous_result.result_sha256:
                    raise AssertionError("result hash chain does not match previous result")
            seen_result_ids.add(result.result_id)
            previous_result = result

    @property
    def result_count(self) -> int:
        """Return the immutable number of results in the series."""

        return len(self.results)

    @property
    def terminal_result_sha256(self) -> str | None:
        """Return the final chain digest, or null for an empty series."""

        return None if not self.results else self.results[-1].result_sha256

    @property
    def series_sha256(self) -> str:
        """Return the digest of the complete assertion series."""

        return calculate_assertion_series_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "assertion_schema_version": SUPPORTED_ASSERTION_SCHEMA_VERSION,
            "result_count": self.result_count,
            "results": [result.to_validator_mapping() for result in self.results],
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "series_type": "ASSERTION_SERIES",
            "terminal_result_sha256": self.terminal_result_sha256,
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete portable assertion-series representation."""

        return {**self._content_mapping(), "series_sha256": self.series_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> AssertionSeries:
        """Parse and verify a serialized append-only assertion series."""

        mapping = _require_mapping(value, field="assertion series")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "assertion_schema_version",
                    "result_count",
                    "results",
                    "run_id",
                    "scenario_id",
                    "series_sha256",
                    "series_type",
                    "terminal_result_sha256",
                }
            ),
            field="assertion series",
        )
        _validate_schema_version(mapping["assertion_schema_version"])
        if mapping["series_type"] != "ASSERTION_SERIES":
            raise AssertionError("unsupported series_type")
        series = cls(
            run_id=_require_string(mapping["run_id"], field="assertion series.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"], field="assertion series.scenario_id"
            ),
            results=_parse_results(mapping["results"]),
        )
        declared_count = _require_integer(
            mapping["result_count"], field="assertion series.result_count"
        )
        if series.result_count != declared_count:
            raise AssertionError("declared result_count does not match assertion series")
        declared_terminal = _require_optional_string(
            mapping["terminal_result_sha256"],
            field="assertion series.terminal_result_sha256",
        )
        if series.terminal_result_sha256 != declared_terminal:
            raise AssertionError("declared terminal_result_sha256 does not match assertion series")
        _validate_declared_sha256(series.series_sha256, mapping, field="assertion series")
        return series


def create_assertion_value(
    value: object,
    *,
    max_value_bytes: int = DEFAULT_MAX_ASSERTION_VALUE_BYTES,
) -> AssertionValue:
    """Freeze any supported JSON value for a validator-owned assertion."""

    _validate_max_value_bytes(max_value_bytes)
    normalized = _normalize_json_value(value, path="value")
    value_json = _canonical_json_bytes(normalized)
    if len(value_json) > max_value_bytes:
        raise AssertionError(f"assertion value must not exceed {max_value_bytes} bytes")
    return AssertionValue(
        value_json=value_json,
        value_sha256=hashlib.sha256(value_json).hexdigest(),
    )


def create_snapshot_assertion(
    *,
    assertion_id: str,
    invariant_id: str,
    invariant_class: InvariantClass,
    severity: AssertionSeverity,
    operator: SnapshotAssertionOperator,
    path: str,
    expected: object = _MISSING,
    expected_type: AssertionValueType | None = None,
    minimum: int | float | None = None,
    maximum: int | float | None = None,
    minimum_inclusive: bool = True,
    maximum_inclusive: bool = True,
    allowed_values: tuple[object, ...] = (),
    max_value_bytes: int = DEFAULT_MAX_ASSERTION_VALUE_BYTES,
) -> SnapshotAssertion:
    """Create and validate one snapshot assertion from ordinary JSON values."""

    _validate_max_value_bytes(max_value_bytes)
    frozen_expected = (
        None
        if expected is _MISSING
        else create_assertion_value(expected, max_value_bytes=max_value_bytes)
    )
    if not isinstance(allowed_values, tuple):
        raise AssertionError("allowed_values must be a tuple")
    frozen_allowed = tuple(
        create_assertion_value(item, max_value_bytes=max_value_bytes) for item in allowed_values
    )
    frozen_allowed = tuple(sorted(frozen_allowed, key=lambda item: item.value_sha256))
    return SnapshotAssertion(
        assertion_id=assertion_id,
        invariant_id=invariant_id,
        invariant_class=invariant_class,
        severity=severity,
        operator=operator,
        path=path,
        expected=frozen_expected,
        expected_type=expected_type,
        minimum=minimum,
        maximum=maximum,
        minimum_inclusive=minimum_inclusive,
        maximum_inclusive=maximum_inclusive,
        allowed_values=frozen_allowed,
    )


def create_transition_assertion(
    *,
    assertion_id: str,
    invariant_id: str,
    invariant_class: InvariantClass,
    severity: AssertionSeverity,
    operator: TransitionAssertionOperator,
    path: str | None = None,
    match_mode: PathMatchMode = PathMatchMode.EXACT,
    expected_operation: ChangeOperation | None = None,
    expected_status: TransitionStatus | None = None,
    required_cause_kind: EvidenceSourceKind | None = None,
) -> TransitionAssertion:
    """Create and validate one structural-transition assertion."""

    return TransitionAssertion(
        assertion_id=assertion_id,
        invariant_id=invariant_id,
        invariant_class=invariant_class,
        severity=severity,
        operator=operator,
        path=path,
        match_mode=match_mode,
        expected_operation=expected_operation,
        expected_status=expected_status,
        required_cause_kind=required_cause_kind,
    )


def create_assertion_series(run_id: str, scenario_id: str) -> AssertionSeries:
    """Create an empty append-only assertion-result series."""

    return AssertionSeries(run_id=run_id, scenario_id=scenario_id)


def evaluate_snapshot_assertion(
    assertion: SnapshotAssertion,
    snapshot: StateSnapshot,
    *,
    result_id: str,
    sequence: int = 0,
    evaluated_at_tick: int | None = None,
    previous_result_sha256: str | None = None,
) -> AssertionResult:
    """Evaluate one deterministic predicate against a validator-owned snapshot."""

    if not isinstance(assertion, SnapshotAssertion):
        raise AssertionError("assertion must be a SnapshotAssertion")
    if not isinstance(snapshot, StateSnapshot):
        raise AssertionError("snapshot must be a StateSnapshot")
    tick = snapshot.captured_at_tick if evaluated_at_tick is None else evaluated_at_tick
    _validate_tick(tick, field="evaluated_at_tick")
    actual_object = _resolve_json_pointer(snapshot.state.decode(), assertion.path)
    status, reason = _evaluate_snapshot_condition(assertion, actual_object)
    actual = (
        None
        if actual_object is _MISSING
        else create_assertion_value(actual_object, max_value_bytes=MAX_ASSERTION_VALUE_BYTES)
    )
    return AssertionResult(
        result_id=result_id,
        run_id=snapshot.run_id,
        scenario_id=snapshot.scenario_id,
        sequence=sequence,
        evaluated_at_tick=tick,
        assertion_id=assertion.assertion_id,
        assertion_sha256=assertion.assertion_sha256,
        invariant_id=assertion.invariant_id,
        invariant_class=assertion.invariant_class,
        severity=assertion.severity,
        target_kind=AssertionTargetKind.SNAPSHOT,
        target_id=snapshot.snapshot_id,
        target_sha256=snapshot.snapshot_sha256,
        target_domain=snapshot.domain,
        status=status,
        reason=reason,
        path=assertion.path,
        actual=actual,
        previous_result_sha256=previous_result_sha256,
    )


def evaluate_transition_assertion(
    assertion: TransitionAssertion,
    transition: StateTransition,
    *,
    result_id: str,
    sequence: int = 0,
    evaluated_at_tick: int | None = None,
    previous_result_sha256: str | None = None,
) -> AssertionResult:
    """Evaluate one deterministic predicate against a structural transition."""

    if not isinstance(assertion, TransitionAssertion):
        raise AssertionError("assertion must be a TransitionAssertion")
    if not isinstance(transition, StateTransition):
        raise AssertionError("transition must be a StateTransition")
    tick = transition.after_tick if evaluated_at_tick is None else evaluated_at_tick
    _validate_tick(tick, field="evaluated_at_tick")
    status, reason, actual_object = _evaluate_transition_condition(assertion, transition)
    actual = (
        None
        if actual_object is _MISSING
        else create_assertion_value(actual_object, max_value_bytes=MAX_ASSERTION_VALUE_BYTES)
    )
    return AssertionResult(
        result_id=result_id,
        run_id=transition.run_id,
        scenario_id=transition.scenario_id,
        sequence=sequence,
        evaluated_at_tick=tick,
        assertion_id=assertion.assertion_id,
        assertion_sha256=assertion.assertion_sha256,
        invariant_id=assertion.invariant_id,
        invariant_class=assertion.invariant_class,
        severity=assertion.severity,
        target_kind=AssertionTargetKind.TRANSITION,
        target_id=transition.transition_id,
        target_sha256=transition.transition_sha256,
        target_domain=transition.domain,
        status=status,
        reason=reason,
        path=assertion.path,
        actual=actual,
        previous_result_sha256=previous_result_sha256,
    )


def append_snapshot_assertion_result(
    series: AssertionSeries,
    assertion: SnapshotAssertion,
    snapshot: StateSnapshot,
    *,
    result_id: str,
    evaluated_at_tick: int | None = None,
) -> AssertionSeries:
    """Evaluate a snapshot assertion and append its hash-linked result."""

    _validate_series_target(series, snapshot.run_id, snapshot.scenario_id)
    if series.result_count >= MAX_ASSERTION_RESULTS:
        raise AssertionError(f"assertion series must not exceed {MAX_ASSERTION_RESULTS} results")
    result = evaluate_snapshot_assertion(
        assertion,
        snapshot,
        result_id=result_id,
        sequence=series.result_count,
        evaluated_at_tick=evaluated_at_tick,
        previous_result_sha256=series.terminal_result_sha256,
    )
    return AssertionSeries(
        run_id=series.run_id,
        scenario_id=series.scenario_id,
        results=(*series.results, result),
    )


def append_transition_assertion_result(
    series: AssertionSeries,
    assertion: TransitionAssertion,
    transition: StateTransition,
    *,
    result_id: str,
    evaluated_at_tick: int | None = None,
) -> AssertionSeries:
    """Evaluate a transition assertion and append its hash-linked result."""

    _validate_series_target(series, transition.run_id, transition.scenario_id)
    if series.result_count >= MAX_ASSERTION_RESULTS:
        raise AssertionError(f"assertion series must not exceed {MAX_ASSERTION_RESULTS} results")
    result = evaluate_transition_assertion(
        assertion,
        transition,
        result_id=result_id,
        sequence=series.result_count,
        evaluated_at_tick=evaluated_at_tick,
        previous_result_sha256=series.terminal_result_sha256,
    )
    return AssertionSeries(
        run_id=series.run_id,
        scenario_id=series.scenario_id,
        results=(*series.results, result),
    )


def create_assertion_source(result: AssertionResult) -> EvidenceSource:
    """Create a verified provenance reference to one assertion result."""

    if not isinstance(result, AssertionResult):
        raise AssertionError("result must be an AssertionResult")
    return EvidenceSource(
        source_kind=EvidenceSourceKind.ASSERTION,
        source_id=result.result_id,
        source_sha256=result.result_sha256,
    )


def validate_assertion_result(
    result: AssertionResult,
    assertion: SnapshotAssertion | TransitionAssertion,
    target: StateSnapshot | StateTransition,
) -> None:
    """Re-evaluate and verify a result against its exact definition and target."""

    if not isinstance(result, AssertionResult):
        raise AssertionError("result must be an AssertionResult")
    if isinstance(assertion, SnapshotAssertion):
        if not isinstance(target, StateSnapshot):
            raise AssertionError("snapshot assertion requires a StateSnapshot target")
        expected = evaluate_snapshot_assertion(
            assertion,
            target,
            result_id=result.result_id,
            sequence=result.sequence,
            evaluated_at_tick=result.evaluated_at_tick,
            previous_result_sha256=result.previous_result_sha256,
        )
    elif isinstance(assertion, TransitionAssertion):
        if not isinstance(target, StateTransition):
            raise AssertionError("transition assertion requires a StateTransition target")
        expected = evaluate_transition_assertion(
            assertion,
            target,
            result_id=result.result_id,
            sequence=result.sequence,
            evaluated_at_tick=result.evaluated_at_tick,
            previous_result_sha256=result.previous_result_sha256,
        )
    else:
        raise AssertionError("assertion must be a SnapshotAssertion or TransitionAssertion")
    if result != expected:
        raise AssertionError("assertion result does not match its definition and target")


def create_assertion_evidence_payload(result: AssertionResult) -> EvidencePayload:
    """Create a compact validator evidence payload for one assertion result."""

    if not isinstance(result, AssertionResult):
        raise AssertionError("result must be an AssertionResult")
    return create_evidence_payload(result.to_evidence_mapping())


def calculate_assertion_result_sha256(result: AssertionResult) -> str:
    """Calculate the canonical digest for one assertion result."""

    if not isinstance(result, AssertionResult):
        raise AssertionError("result must be an AssertionResult")
    return hashlib.sha256(_canonical_json_bytes(result._content_mapping())).hexdigest()


def calculate_assertion_series_sha256(series: AssertionSeries) -> str:
    """Calculate the canonical digest for an assertion-result series."""

    if not isinstance(series, AssertionSeries):
        raise AssertionError("series must be an AssertionSeries")
    return hashlib.sha256(_canonical_json_bytes(series._content_mapping())).hexdigest()


def _evaluate_snapshot_condition(
    assertion: SnapshotAssertion,
    actual: object,
) -> tuple[AssertionStatus, AssertionReason]:
    found = actual is not _MISSING
    operator = assertion.operator
    if operator is SnapshotAssertionOperator.EXISTS:
        return _condition_result(
            assertion, found, AssertionReason.PATH_FOUND, AssertionReason.PATH_NOT_FOUND
        )
    if operator is SnapshotAssertionOperator.ABSENT:
        return _condition_result(
            assertion, not found, AssertionReason.PATH_NOT_FOUND, AssertionReason.PATH_FOUND
        )
    if not found:
        return AssertionStatus.BLOCKED, AssertionReason.PATH_NOT_FOUND

    if operator is SnapshotAssertionOperator.EQUALS:
        assert assertion.expected is not None
        matches = _json_values_equal(actual, assertion.expected)
        return _condition_result(
            assertion, matches, AssertionReason.VALUES_EQUAL, AssertionReason.VALUES_DIFFER
        )
    if operator is SnapshotAssertionOperator.NOT_EQUALS:
        assert assertion.expected is not None
        differs = not _json_values_equal(actual, assertion.expected)
        return _condition_result(
            assertion, differs, AssertionReason.VALUES_DIFFER, AssertionReason.VALUES_EQUAL
        )
    if operator is SnapshotAssertionOperator.TYPE_IS:
        assert assertion.expected_type is not None
        matches = _classify_json_type(actual) is assertion.expected_type
        if assertion.expected_type is AssertionValueType.NUMBER:
            matches = _is_json_number(actual)
        return _condition_result(
            assertion, matches, AssertionReason.TYPE_MATCH, AssertionReason.TYPE_MISMATCH
        )
    if operator is SnapshotAssertionOperator.NUMBER_RANGE:
        if not _is_json_number(actual):
            return _failure_status(assertion), AssertionReason.TYPE_MISMATCH
        in_range = _number_in_range(cast(int | float, actual), assertion)
        return _condition_result(
            assertion,
            in_range,
            AssertionReason.VALUE_IN_RANGE,
            AssertionReason.VALUE_OUT_OF_RANGE,
        )

    actual_value = create_assertion_value(actual, max_value_bytes=MAX_ASSERTION_VALUE_BYTES)
    allowed_hashes = {item.value_sha256 for item in assertion.allowed_values}
    allowed = actual_value.value_sha256 in allowed_hashes
    return _condition_result(
        assertion, allowed, AssertionReason.VALUE_ALLOWED, AssertionReason.VALUE_NOT_ALLOWED
    )


def _evaluate_transition_condition(
    assertion: TransitionAssertion,
    transition: StateTransition,
) -> tuple[AssertionStatus, AssertionReason, object]:
    operator = assertion.operator
    if operator is TransitionAssertionOperator.STATUS_IS:
        assert assertion.expected_status is not None
        matches = transition.status is assertion.expected_status
        status, reason = _condition_result(
            assertion,
            matches,
            AssertionReason.STATUS_MATCH,
            AssertionReason.STATUS_MISMATCH,
        )
        return status, reason, transition.status.value

    if operator is TransitionAssertionOperator.CHANGES_HAVE_CAUSE:
        satisfied = not transition.changes or bool(transition.causes)
        status, reason = _condition_result(
            assertion,
            satisfied,
            AssertionReason.CAUSE_PRESENT,
            AssertionReason.CAUSE_MISSING,
        )
        return status, reason, len(transition.causes)

    if operator is TransitionAssertionOperator.CHANGES_HAVE_CAUSE_KIND:
        assert assertion.required_cause_kind is not None
        satisfied = not transition.changes or any(
            source.source_kind is assertion.required_cause_kind for source in transition.causes
        )
        status, reason = _condition_result(
            assertion,
            satisfied,
            AssertionReason.CAUSE_KIND_PRESENT,
            AssertionReason.CAUSE_KIND_MISSING,
        )
        actual_kinds = sorted({source.source_kind.value for source in transition.causes})
        return status, reason, actual_kinds

    assert assertion.path is not None
    matching_changes = tuple(
        change
        for change in transition.changes
        if _path_matches(change.path, assertion.path, assertion.match_mode)
    )
    changed = bool(matching_changes)
    if operator is TransitionAssertionOperator.PATH_CHANGED:
        status, reason = _condition_result(
            assertion,
            changed,
            AssertionReason.PATH_CHANGED,
            AssertionReason.PATH_UNCHANGED,
        )
        return status, reason, [change.path for change in matching_changes]
    if operator is TransitionAssertionOperator.PATH_UNCHANGED:
        status, reason = _condition_result(
            assertion,
            not changed,
            AssertionReason.PATH_UNCHANGED,
            AssertionReason.PATH_CHANGED,
        )
        return status, reason, [change.path for change in matching_changes]

    if not matching_changes:
        return AssertionStatus.BLOCKED, AssertionReason.PATH_NOT_FOUND, _MISSING
    assert assertion.expected_operation is not None
    operation_matches = all(
        change.operation is assertion.expected_operation for change in matching_changes
    )
    status, reason = _condition_result(
        assertion,
        operation_matches,
        AssertionReason.OPERATION_MATCH,
        AssertionReason.OPERATION_MISMATCH,
    )
    return status, reason, [change.operation.value for change in matching_changes]


def _condition_result(
    assertion: SnapshotAssertion | TransitionAssertion,
    satisfied: bool,
    pass_reason: AssertionReason,
    failure_reason: AssertionReason,
) -> tuple[AssertionStatus, AssertionReason]:
    if satisfied:
        return AssertionStatus.PASS, pass_reason
    return _failure_status(assertion), failure_reason


def _failure_status(
    assertion: SnapshotAssertion | TransitionAssertion,
) -> AssertionStatus:
    if assertion.invariant_class is InvariantClass.HARD:
        return AssertionStatus.FAIL
    return AssertionStatus.REVIEW


def _json_values_equal(actual: object, expected: AssertionValue) -> bool:
    actual_value = create_assertion_value(actual, max_value_bytes=MAX_ASSERTION_VALUE_BYTES)
    return actual_value.value_sha256 == expected.value_sha256


def _number_in_range(value: int | float, assertion: SnapshotAssertion) -> bool:
    if assertion.minimum is not None:
        if value < assertion.minimum:
            return False
        if value == assertion.minimum and not assertion.minimum_inclusive:
            return False
    if assertion.maximum is not None:
        if value > assertion.maximum:
            return False
        if value == assertion.maximum and not assertion.maximum_inclusive:
            return False
    return True


def _classify_json_type(value: object) -> AssertionValueType:
    if value is None:
        return AssertionValueType.NULL
    if isinstance(value, bool):
        return AssertionValueType.BOOLEAN
    if isinstance(value, int):
        return AssertionValueType.INTEGER
    if isinstance(value, float):
        return AssertionValueType.NUMBER
    if isinstance(value, str):
        return AssertionValueType.STRING
    if isinstance(value, list):
        return AssertionValueType.ARRAY
    if isinstance(value, dict):
        return AssertionValueType.OBJECT
    raise AssertionError("captured state contains an unsupported JSON value")


def _is_json_number(value: object) -> bool:
    return not isinstance(value, bool) and isinstance(value, (int, float))


def _path_matches(change_path: str, asserted_path: str, mode: PathMatchMode) -> bool:
    if mode is PathMatchMode.EXACT:
        return change_path == asserted_path
    return change_path == asserted_path or change_path.startswith(f"{asserted_path}/")


def _resolve_json_pointer(document: object, path: str) -> object:
    current = document
    for raw_token in path.split("/")[1:]:
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict):
            if token not in current:
                return _MISSING
            current = current[token]
        elif isinstance(current, list):
            if not token.isdigit() or (len(token) > 1 and token.startswith("0")):
                return _MISSING
            index = int(token)
            if index >= len(current):
                return _MISSING
            current = current[index]
        else:
            return _MISSING
    return current


def _validate_series_target(series: AssertionSeries, run_id: str, scenario_id: str) -> None:
    if not isinstance(series, AssertionSeries):
        raise AssertionError("series must be an AssertionSeries")
    if series.run_id != run_id or series.scenario_id != scenario_id:
        raise AssertionError("target identity does not match assertion series")


def _parse_optional_assertion_value(value: object, *, field: str) -> AssertionValue | None:
    if value is None:
        return None
    mapping = _require_mapping(value, field=field)
    return AssertionValue.from_mapping(mapping)


def _parse_assertion_values(value: object, *, field: str) -> tuple[AssertionValue, ...]:
    if not isinstance(value, list):
        raise AssertionError(f"{field} must be an array")
    return tuple(
        AssertionValue.from_mapping(_require_mapping(item, field=f"{field}[{index}]"))
        for index, item in enumerate(value)
    )


def _parse_results(value: object) -> tuple[AssertionResult, ...]:
    if not isinstance(value, list):
        raise AssertionError("assertion series.results must be an array")
    return tuple(
        AssertionResult.from_mapping(
            _require_mapping(item, field=f"assertion series.results[{index}]")
        )
        for index, item in enumerate(value)
    )


def _validate_declared_sha256(
    calculated_sha256: str,
    mapping: Mapping[str, object],
    *,
    field: str,
) -> None:
    declared_sha256 = _require_string(
        mapping[f"{field.split()[-1]}_sha256"], field=f"{field}.sha256"
    )
    if declared_sha256 != calculated_sha256:
        raise AssertionError(f"declared sha256 does not match {field}")


def _validate_schema_version(value: object) -> None:
    version = _require_string(value, field="assertion_schema_version")
    if version != SUPPORTED_ASSERTION_SCHEMA_VERSION:
        raise AssertionError(f"unsupported assertion_schema_version: {version}")


def _validate_max_value_bytes(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AssertionError("max_value_bytes must be an integer")
    if not 1 <= value <= MAX_ASSERTION_VALUE_BYTES:
        raise AssertionError(f"max_value_bytes must be between 1 and {MAX_ASSERTION_VALUE_BYTES}")


def _decode_json_value(value_json: bytes) -> object:
    try:
        return json.loads(
            value_json.decode("utf-8"),
            parse_constant=_reject_non_finite_json,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise AssertionError("value_json must contain valid finite UTF-8 JSON") from exc


def _canonical_json_bytes(value: object) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise AssertionError("value must be canonical finite JSON") from exc


def _normalize_json_value(value: object, *, path: str) -> object:
    _validate_json_value(value, path=path)
    if isinstance(value, Mapping):
        return {
            key: _normalize_json_value(item, path=f"{path}.{key}")
            for key, item in sorted(value.items())
        }
    if isinstance(value, (list, tuple)):
        return [
            _normalize_json_value(item, path=f"{path}[{index}]") for index, item in enumerate(value)
        ]
    return value


def _validate_json_value(value: object, *, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise AssertionError(f"{path} must not contain non-finite numbers")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise AssertionError(f"{path} object keys must be strings")
            _validate_json_value(item, path=f"{path}.{key}")
        return
    if isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            _validate_json_value(item, path=f"{path}[{index}]")
        return
    raise AssertionError(f"{path} contains unsupported JSON value type")


def _require_mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise AssertionError(f"{field} must be an object")
    for key in value:
        if not isinstance(key, str):
            raise AssertionError(f"{field} keys must be strings")
    return cast(Mapping[str, object], value)


def _require_exact_keys(
    mapping: Mapping[str, object],
    *,
    required: frozenset[str],
    field: str,
) -> None:
    actual = frozenset(mapping)
    missing = sorted(required - actual)
    unexpected = sorted(actual - required)
    if missing:
        raise AssertionError(f"{field} is missing required fields: {', '.join(missing)}")
    if unexpected:
        raise AssertionError(f"{field} contains unexpected fields: {', '.join(unexpected)}")


def _require_string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        raise AssertionError(f"{field} must be a string")
    return value


def _require_optional_string(value: object, *, field: str) -> str | None:
    if value is None:
        return None
    return _require_string(value, field=field)


def _require_integer(value: object, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AssertionError(f"{field} must be an integer")
    return value


def _require_boolean(value: object, *, field: str) -> bool:
    if not isinstance(value, bool):
        raise AssertionError(f"{field} must be a boolean")
    return value


def _require_optional_number(value: object, *, field: str) -> int | float | None:
    if value is None:
        return None
    _validate_optional_number(value, field=field)
    return cast(int | float, value)


def _parse_enum[T: StrEnum](
    enum_type: type[T],
    value: object,
    *,
    field: str,
) -> T:
    raw = _require_string(value, field=field)
    try:
        return enum_type(raw)
    except ValueError as exc:
        raise AssertionError(f"{field} contains an unsupported value: {raw}") from exc


def _parse_optional_enum[T: StrEnum](
    enum_type: type[T],
    value: object,
    *,
    field: str,
) -> T | None:
    if value is None:
        return None
    return _parse_enum(enum_type, value, field=field)


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise AssertionError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise AssertionError(f"{field} must be a stable uppercase control identifier")


def _validate_scenario_id(value: str) -> None:
    if not isinstance(value, str):
        raise AssertionError("scenario_id must be a string")
    if _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        raise AssertionError("scenario_id must match AURORA-SCN-<FAMILY>-<NNN>")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise AssertionError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise AssertionError(f"{field} must be a lowercase SHA-256 digest")


def _validate_json_pointer(value: str) -> None:
    if not isinstance(value, str):
        raise AssertionError("path must be a string")
    if _JSON_POINTER_PATTERN.fullmatch(value) is None:
        raise AssertionError("path must be a non-empty RFC 6901 JSON Pointer")


def _validate_optional_number(value: object, *, field: str) -> None:
    if value is None:
        return
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise AssertionError(f"{field} must be null or a number")
    if isinstance(value, float) and not math.isfinite(value):
        raise AssertionError(f"{field} must be finite")


def _validate_sequence(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AssertionError(f"{field} must be an integer")
    if value < 0:
        raise AssertionError(f"{field} must be non-negative")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise AssertionError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise AssertionError(f"{field} must be between 0 and {MAX_TICK}")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
    "DEFAULT_MAX_ASSERTION_VALUE_BYTES",
    "MAX_ASSERTION_ALLOWED_VALUES",
    "MAX_ASSERTION_RESULTS",
    "MAX_ASSERTION_VALUE_BYTES",
    "MAX_TICK",
    "SUPPORTED_ASSERTION_SCHEMA_VERSION",
    "AssertionError",
    "AssertionReason",
    "AssertionResult",
    "AssertionSeries",
    "AssertionSeverity",
    "AssertionStatus",
    "AssertionTargetKind",
    "AssertionValue",
    "AssertionValueType",
    "InvariantClass",
    "PathMatchMode",
    "SnapshotAssertion",
    "SnapshotAssertionOperator",
    "TransitionAssertion",
    "TransitionAssertionOperator",
    "append_snapshot_assertion_result",
    "append_transition_assertion_result",
    "calculate_assertion_result_sha256",
    "calculate_assertion_series_sha256",
    "create_assertion_evidence_payload",
    "create_assertion_series",
    "create_assertion_source",
    "create_assertion_value",
    "create_snapshot_assertion",
    "create_transition_assertion",
    "evaluate_snapshot_assertion",
    "evaluate_transition_assertion",
    "validate_assertion_result",
]
