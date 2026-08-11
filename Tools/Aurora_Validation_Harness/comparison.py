"""Deterministic differential comparison of Aurora assertion runs.

The module pairs semantically equivalent assertion results across controlled
runs and evaluates relations between them.  It supports repeatability, hidden
state isolation, information-driven divergence, counterfactuals, and version
regression checks without comparing exact dialogue.  Raw actual values remain
validator-owned and are excluded from portable comparison operands.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Final, cast

from aurora_validation_harness.assertions import (
    AssertionReason,
    AssertionResult,
    AssertionSeries,
    AssertionSeverity,
    AssertionStatus,
    AssertionTargetKind,
    InvariantClass,
)
from aurora_validation_harness.evidence import (
    EvidenceDomain,
    EvidencePayload,
    create_evidence_payload,
)

SUPPORTED_COMPARISON_SCHEMA_VERSION: Final[str] = "1.0"
MAX_COMPARISON_ASSERTION_IDS: Final[int] = 50_000
MAX_COMPARISON_PAIRS: Final[int] = 1_000_000
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_JSON_POINTER_PATTERN: Final[re.Pattern[str]] = re.compile(r"^(?:/(?:[^~]|~[01])*)+$")


class ComparisonError(ValueError):
    """Raised when comparison data, run pairing, or report integrity is invalid."""


class ComparisonKind(StrEnum):
    """Canonical purpose of one controlled differential comparison."""

    REPEATABILITY = "REPEATABILITY"
    HIDDEN_STATE = "HIDDEN_STATE"
    INFORMATION = "INFORMATION"
    COUNTERFACTUAL = "COUNTERFACTUAL"
    VERSION = "VERSION"
    CUSTOM = "CUSTOM"


class ComparisonPolicy(StrEnum):
    """Relation required between paired assertion results."""

    EXACT = "EXACT"
    OUTCOME_EQUIVALENT = "OUTCOME_EQUIVALENT"
    ACTUAL_EQUIVALENT = "ACTUAL_EQUIVALENT"
    EXPECTED_DIVERGENCE = "EXPECTED_DIVERGENCE"
    NO_STATUS_REGRESSION = "NO_STATUS_REGRESSION"
    ACTUAL_NON_INCREASING = "ACTUAL_NON_INCREASING"
    ACTUAL_NON_DECREASING = "ACTUAL_NON_DECREASING"


class ComparisonStatus(StrEnum):
    """Machine-readable outcome of a differential comparison."""

    PASS = "PASS"
    FAIL = "FAIL"
    REVIEW = "REVIEW"
    BLOCKED = "BLOCKED"


class ComparisonReason(StrEnum):
    """Stable explanation code for a comparison outcome."""

    EXACT_MATCH = "EXACT_MATCH"
    OUTCOMES_EQUIVALENT = "OUTCOMES_EQUIVALENT"
    ACTUALS_EQUIVALENT = "ACTUALS_EQUIVALENT"
    EXPECTED_DIVERGENCE_OBSERVED = "EXPECTED_DIVERGENCE_OBSERVED"
    NO_STATUS_REGRESSION = "NO_STATUS_REGRESSION"
    NUMERIC_RELATION_SATISFIED = "NUMERIC_RELATION_SATISFIED"
    UNEXPECTED_DIVERGENCE = "UNEXPECTED_DIVERGENCE"
    REQUIRED_DIVERGENCE_NOT_OBSERVED = "REQUIRED_DIVERGENCE_NOT_OBSERVED"
    STATUS_REGRESSION = "STATUS_REGRESSION"
    NUMERIC_RELATION_VIOLATED = "NUMERIC_RELATION_VIOLATED"
    INSUFFICIENT_PAIRED_RESULTS = "INSUFFICIENT_PAIRED_RESULTS"
    INCOMPLETE_PAIRING = "INCOMPLETE_PAIRING"
    INCOMPATIBLE_ASSERTION_DEFINITION = "INCOMPATIBLE_ASSERTION_DEFINITION"
    BLOCKED_ASSERTION_RESULT = "BLOCKED_ASSERTION_RESULT"
    NON_NUMERIC_ACTUAL = "NON_NUMERIC_ACTUAL"


class DifferenceKind(StrEnum):
    """Independent semantic difference observed in one paired result."""

    MISSING_BASELINE = "MISSING_BASELINE"
    MISSING_CANDIDATE = "MISSING_CANDIDATE"
    DEFINITION_CHANGED = "DEFINITION_CHANGED"
    STATUS_CHANGED = "STATUS_CHANGED"
    REASON_CHANGED = "REASON_CHANGED"
    ACTUAL_CHANGED = "ACTUAL_CHANGED"


_DIFFERENCE_ORDER: Final[dict[DifferenceKind, int]] = {
    item: index for index, item in enumerate(DifferenceKind)
}
_STATUS_QUALITY: Final[dict[AssertionStatus, int]] = {
    AssertionStatus.PASS: 0,
    AssertionStatus.REVIEW: 1,
    AssertionStatus.FAIL: 2,
}


@dataclass(frozen=True, slots=True)
class ComparisonDefinition:
    """Immutable declaration of a relation between two assertion runs."""

    comparison_id: str
    scenario_id: str
    baseline_run_id: str
    candidate_run_id: str
    invariant_id: str
    invariant_class: InvariantClass
    severity: AssertionSeverity
    kind: ComparisonKind
    policy: ComparisonPolicy
    assertion_ids: tuple[str, ...] = ()
    minimum_paired_results: int = 1
    allow_unpaired_results: bool = False

    def __post_init__(self) -> None:
        _validate_control_id(self.comparison_id, field="comparison_id")
        _validate_scenario_id(self.scenario_id)
        _validate_control_id(self.baseline_run_id, field="baseline_run_id")
        _validate_control_id(self.candidate_run_id, field="candidate_run_id")
        if self.baseline_run_id == self.candidate_run_id:
            raise ComparisonError("baseline and candidate run IDs must differ")
        _validate_control_id(self.invariant_id, field="invariant_id")
        if not isinstance(self.invariant_class, InvariantClass):
            raise ComparisonError("invariant_class must be an InvariantClass value")
        if not isinstance(self.severity, AssertionSeverity):
            raise ComparisonError("severity must be an AssertionSeverity value")
        if not isinstance(self.kind, ComparisonKind):
            raise ComparisonError("kind must be a ComparisonKind value")
        if not isinstance(self.policy, ComparisonPolicy):
            raise ComparisonError("policy must be a ComparisonPolicy value")
        if not isinstance(self.assertion_ids, tuple) or not all(
            isinstance(assertion_id, str) for assertion_id in self.assertion_ids
        ):
            raise ComparisonError("assertion_ids must be a tuple of strings")
        if len(self.assertion_ids) > MAX_COMPARISON_ASSERTION_IDS:
            raise ComparisonError(
                f"assertion_ids must not exceed {MAX_COMPARISON_ASSERTION_IDS} entries"
            )
        for assertion_id in self.assertion_ids:
            _validate_control_id(assertion_id, field="assertion_ids entry")
        if len(self.assertion_ids) != len(set(self.assertion_ids)):
            raise ComparisonError("assertion_ids must not contain duplicates")
        if self.assertion_ids != tuple(sorted(self.assertion_ids)):
            raise ComparisonError("assertion_ids must use lexical order")
        _validate_positive_integer(
            self.minimum_paired_results,
            field="minimum_paired_results",
        )
        if self.minimum_paired_results > MAX_COMPARISON_PAIRS:
            raise ComparisonError(f"minimum_paired_results must not exceed {MAX_COMPARISON_PAIRS}")
        if not isinstance(self.allow_unpaired_results, bool):
            raise ComparisonError("allow_unpaired_results must be a boolean")

    @property
    def comparison_sha256(self) -> str:
        """Return the digest of the complete comparison declaration."""

        return calculate_comparison_definition_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "allow_unpaired_results": self.allow_unpaired_results,
            "assertion_ids": list(self.assertion_ids),
            "baseline_run_id": self.baseline_run_id,
            "candidate_run_id": self.candidate_run_id,
            "comparison_id": self.comparison_id,
            "comparison_schema_version": SUPPORTED_COMPARISON_SCHEMA_VERSION,
            "comparison_type": "COMPARISON_DEFINITION",
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "kind": self.kind.value,
            "minimum_paired_results": self.minimum_paired_results,
            "policy": self.policy.value,
            "scenario_id": self.scenario_id,
            "severity": self.severity.value,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable comparison definition."""

        return {**self._content_mapping(), "comparison_sha256": self.comparison_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> ComparisonDefinition:
        """Parse and verify a serialized comparison definition."""

        mapping = _require_mapping(value, field="comparison definition")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "allow_unpaired_results",
                    "assertion_ids",
                    "baseline_run_id",
                    "candidate_run_id",
                    "comparison_id",
                    "comparison_schema_version",
                    "comparison_sha256",
                    "comparison_type",
                    "invariant_class",
                    "invariant_id",
                    "kind",
                    "minimum_paired_results",
                    "policy",
                    "scenario_id",
                    "severity",
                }
            ),
            field="comparison definition",
        )
        _validate_schema_version(mapping["comparison_schema_version"])
        if mapping["comparison_type"] != "COMPARISON_DEFINITION":
            raise ComparisonError("unsupported comparison_type")
        definition = cls(
            comparison_id=_require_string(
                mapping["comparison_id"], field="comparison definition.comparison_id"
            ),
            scenario_id=_require_string(
                mapping["scenario_id"], field="comparison definition.scenario_id"
            ),
            baseline_run_id=_require_string(
                mapping["baseline_run_id"],
                field="comparison definition.baseline_run_id",
            ),
            candidate_run_id=_require_string(
                mapping["candidate_run_id"],
                field="comparison definition.candidate_run_id",
            ),
            invariant_id=_require_string(
                mapping["invariant_id"], field="comparison definition.invariant_id"
            ),
            invariant_class=_parse_enum(
                InvariantClass,
                mapping["invariant_class"],
                field="comparison definition.invariant_class",
            ),
            severity=_parse_enum(
                AssertionSeverity,
                mapping["severity"],
                field="comparison definition.severity",
            ),
            kind=_parse_enum(
                ComparisonKind,
                mapping["kind"],
                field="comparison definition.kind",
            ),
            policy=_parse_enum(
                ComparisonPolicy,
                mapping["policy"],
                field="comparison definition.policy",
            ),
            assertion_ids=_parse_string_tuple(
                mapping["assertion_ids"],
                field="comparison definition.assertion_ids",
            ),
            minimum_paired_results=_require_integer(
                mapping["minimum_paired_results"],
                field="comparison definition.minimum_paired_results",
            ),
            allow_unpaired_results=_require_boolean(
                mapping["allow_unpaired_results"],
                field="comparison definition.allow_unpaired_results",
            ),
        )
        _validate_declared_sha256(
            definition.comparison_sha256,
            mapping,
            key="comparison_sha256",
            field="comparison definition",
        )
        return definition


@dataclass(frozen=True, slots=True)
class ComparisonKey:
    """Stable semantic key used to pair repeated assertion results."""

    assertion_id: str
    target_kind: AssertionTargetKind
    target_domain: EvidenceDomain
    path: str | None
    occurrence: int

    def __post_init__(self) -> None:
        _validate_control_id(self.assertion_id, field="assertion_id")
        if not isinstance(self.target_kind, AssertionTargetKind):
            raise ComparisonError("target_kind must be an AssertionTargetKind value")
        if not isinstance(self.target_domain, EvidenceDomain):
            raise ComparisonError("target_domain must be an EvidenceDomain value")
        if self.path is not None:
            _validate_json_pointer(self.path)
        _validate_sequence(self.occurrence, field="occurrence")

    @property
    def key_sha256(self) -> str:
        """Return the digest of the semantic pairing key."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "assertion_id": self.assertion_id,
            "occurrence": self.occurrence,
            "path": self.path,
            "target_domain": self.target_domain.value,
            "target_kind": self.target_kind.value,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable key representation."""

        return {**self._content_mapping(), "key_sha256": self.key_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> ComparisonKey:
        """Parse and verify a serialized comparison key."""

        mapping = _require_mapping(value, field="comparison key")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "assertion_id",
                    "key_sha256",
                    "occurrence",
                    "path",
                    "target_domain",
                    "target_kind",
                }
            ),
            field="comparison key",
        )
        key = cls(
            assertion_id=_require_string(
                mapping["assertion_id"], field="comparison key.assertion_id"
            ),
            target_kind=_parse_enum(
                AssertionTargetKind,
                mapping["target_kind"],
                field="comparison key.target_kind",
            ),
            target_domain=_parse_enum(
                EvidenceDomain,
                mapping["target_domain"],
                field="comparison key.target_domain",
            ),
            path=_require_optional_string(mapping["path"], field="comparison key.path"),
            occurrence=_require_integer(mapping["occurrence"], field="comparison key.occurrence"),
        )
        _validate_declared_sha256(
            key.key_sha256,
            mapping,
            key="key_sha256",
            field="comparison key",
        )
        return key


@dataclass(frozen=True, slots=True)
class ComparisonOperand:
    """Portable, value-redacted reference to one assertion result."""

    result_id: str
    result_sha256: str
    assertion_id: str
    assertion_sha256: str
    target_kind: AssertionTargetKind
    target_domain: EvidenceDomain
    target_id: str
    target_sha256: str
    path: str | None
    invariant_id: str
    invariant_class: InvariantClass
    severity: AssertionSeverity
    status: AssertionStatus
    reason: AssertionReason
    actual_value_sha256: str | None

    def __post_init__(self) -> None:
        _validate_control_id(self.result_id, field="result_id")
        _validate_sha256(self.result_sha256, field="result_sha256")
        _validate_control_id(self.assertion_id, field="assertion_id")
        _validate_sha256(self.assertion_sha256, field="assertion_sha256")
        if not isinstance(self.target_kind, AssertionTargetKind):
            raise ComparisonError("target_kind must be an AssertionTargetKind value")
        if not isinstance(self.target_domain, EvidenceDomain):
            raise ComparisonError("target_domain must be an EvidenceDomain value")
        _validate_control_id(self.target_id, field="target_id")
        _validate_sha256(self.target_sha256, field="target_sha256")
        if self.path is not None:
            _validate_json_pointer(self.path)
        _validate_control_id(self.invariant_id, field="invariant_id")
        if not isinstance(self.invariant_class, InvariantClass):
            raise ComparisonError("invariant_class must be an InvariantClass value")
        if not isinstance(self.severity, AssertionSeverity):
            raise ComparisonError("severity must be an AssertionSeverity value")
        if not isinstance(self.status, AssertionStatus):
            raise ComparisonError("status must be an AssertionStatus value")
        if not isinstance(self.reason, AssertionReason):
            raise ComparisonError("reason must be an AssertionReason value")
        if self.actual_value_sha256 is not None:
            _validate_sha256(self.actual_value_sha256, field="actual_value_sha256")

    def to_mapping(self) -> dict[str, object]:
        """Return the portable redacted operand representation."""

        return {
            "actual_value_sha256": self.actual_value_sha256,
            "assertion_id": self.assertion_id,
            "assertion_sha256": self.assertion_sha256,
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "reason": self.reason.value,
            "result_id": self.result_id,
            "result_sha256": self.result_sha256,
            "severity": self.severity.value,
            "status": self.status.value,
            "target_domain": self.target_domain.value,
            "target_id": self.target_id,
            "target_kind": self.target_kind.value,
            "target_sha256": self.target_sha256,
            "path": self.path,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> ComparisonOperand:
        """Parse one serialized redacted comparison operand."""

        mapping = _require_mapping(value, field="comparison operand")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "actual_value_sha256",
                    "assertion_id",
                    "assertion_sha256",
                    "invariant_class",
                    "invariant_id",
                    "reason",
                    "result_id",
                    "result_sha256",
                    "severity",
                    "status",
                    "target_domain",
                    "target_id",
                    "target_kind",
                    "target_sha256",
                    "path",
                }
            ),
            field="comparison operand",
        )
        return cls(
            result_id=_require_string(mapping["result_id"], field="comparison operand.result_id"),
            result_sha256=_require_string(
                mapping["result_sha256"], field="comparison operand.result_sha256"
            ),
            assertion_id=_require_string(
                mapping["assertion_id"], field="comparison operand.assertion_id"
            ),
            assertion_sha256=_require_string(
                mapping["assertion_sha256"],
                field="comparison operand.assertion_sha256",
            ),
            target_kind=_parse_enum(
                AssertionTargetKind,
                mapping["target_kind"],
                field="comparison operand.target_kind",
            ),
            target_domain=_parse_enum(
                EvidenceDomain,
                mapping["target_domain"],
                field="comparison operand.target_domain",
            ),
            target_id=_require_string(mapping["target_id"], field="comparison operand.target_id"),
            target_sha256=_require_string(
                mapping["target_sha256"], field="comparison operand.target_sha256"
            ),
            path=_require_optional_string(mapping["path"], field="comparison operand.path"),
            invariant_id=_require_string(
                mapping["invariant_id"], field="comparison operand.invariant_id"
            ),
            invariant_class=_parse_enum(
                InvariantClass,
                mapping["invariant_class"],
                field="comparison operand.invariant_class",
            ),
            severity=_parse_enum(
                AssertionSeverity,
                mapping["severity"],
                field="comparison operand.severity",
            ),
            status=_parse_enum(
                AssertionStatus,
                mapping["status"],
                field="comparison operand.status",
            ),
            reason=_parse_enum(
                AssertionReason,
                mapping["reason"],
                field="comparison operand.reason",
            ),
            actual_value_sha256=_require_optional_string(
                mapping["actual_value_sha256"],
                field="comparison operand.actual_value_sha256",
            ),
        )


@dataclass(frozen=True, slots=True)
class ResultComparison:
    """One deterministic baseline/candidate assertion-result pairing."""

    key: ComparisonKey
    baseline: ComparisonOperand | None
    candidate: ComparisonOperand | None
    differences: tuple[DifferenceKind, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.key, ComparisonKey):
            raise ComparisonError("key must be a ComparisonKey")
        if self.baseline is not None and not isinstance(self.baseline, ComparisonOperand):
            raise ComparisonError("baseline must be null or a ComparisonOperand")
        if self.candidate is not None and not isinstance(self.candidate, ComparisonOperand):
            raise ComparisonError("candidate must be null or a ComparisonOperand")
        if self.baseline is None and self.candidate is None:
            raise ComparisonError("result comparison requires at least one operand")
        for operand in (self.baseline, self.candidate):
            if operand is not None and (
                operand.assertion_id != self.key.assertion_id
                or operand.target_kind is not self.key.target_kind
                or operand.target_domain is not self.key.target_domain
                or operand.path != self.key.path
            ):
                raise ComparisonError("comparison operand does not match comparison key")
        if not isinstance(self.differences, tuple) or not all(
            isinstance(item, DifferenceKind) for item in self.differences
        ):
            raise ComparisonError("differences must be a tuple of DifferenceKind values")
        if len(self.differences) != len(set(self.differences)):
            raise ComparisonError("differences must not contain duplicates")
        expected_order = tuple(sorted(self.differences, key=_DIFFERENCE_ORDER.__getitem__))
        if self.differences != expected_order:
            raise ComparisonError("differences must use canonical order")
        if self.differences != _derive_differences(self.baseline, self.candidate):
            raise ComparisonError("differences do not match comparison operands")

    @property
    def paired(self) -> bool:
        """Return whether both sides supplied a result."""

        return self.baseline is not None and self.candidate is not None

    @property
    def changed(self) -> bool:
        """Return whether any semantic difference was observed."""

        return bool(self.differences)

    @property
    def comparison_sha256(self) -> str:
        """Return the digest of this result comparison."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "baseline": None if self.baseline is None else self.baseline.to_mapping(),
            "candidate": None if self.candidate is None else self.candidate.to_mapping(),
            "differences": [item.value for item in self.differences],
            "key": self.key.to_mapping(),
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable pairing representation."""

        return {**self._content_mapping(), "comparison_sha256": self.comparison_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> ResultComparison:
        """Parse and verify one serialized result comparison."""

        mapping = _require_mapping(value, field="result comparison")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {"baseline", "candidate", "comparison_sha256", "differences", "key"}
            ),
            field="result comparison",
        )
        comparison = cls(
            key=ComparisonKey.from_mapping(
                _require_mapping(mapping["key"], field="result comparison.key")
            ),
            baseline=_parse_optional_operand(
                mapping["baseline"], field="result comparison.baseline"
            ),
            candidate=_parse_optional_operand(
                mapping["candidate"], field="result comparison.candidate"
            ),
            differences=_parse_enum_tuple(
                DifferenceKind,
                mapping["differences"],
                field="result comparison.differences",
            ),
        )
        _validate_declared_sha256(
            comparison.comparison_sha256,
            mapping,
            key="comparison_sha256",
            field="result comparison",
        )
        return comparison


@dataclass(frozen=True, slots=True)
class ComparisonReport:
    """Immutable outcome of applying one definition to two assertion series."""

    report_id: str
    comparison_id: str
    comparison_definition_sha256: str
    scenario_id: str
    baseline_run_id: str
    baseline_series_sha256: str
    candidate_run_id: str
    candidate_series_sha256: str
    evaluated_at_tick: int
    invariant_id: str
    invariant_class: InvariantClass
    severity: AssertionSeverity
    kind: ComparisonKind
    policy: ComparisonPolicy
    status: ComparisonStatus
    reason: ComparisonReason
    pairs: tuple[ResultComparison, ...]
    violations: tuple[ComparisonKey, ...]

    def __post_init__(self) -> None:
        _validate_control_id(self.report_id, field="report_id")
        _validate_control_id(self.comparison_id, field="comparison_id")
        _validate_sha256(
            self.comparison_definition_sha256,
            field="comparison_definition_sha256",
        )
        _validate_scenario_id(self.scenario_id)
        _validate_control_id(self.baseline_run_id, field="baseline_run_id")
        _validate_sha256(self.baseline_series_sha256, field="baseline_series_sha256")
        _validate_control_id(self.candidate_run_id, field="candidate_run_id")
        _validate_sha256(self.candidate_series_sha256, field="candidate_series_sha256")
        if self.baseline_run_id == self.candidate_run_id:
            raise ComparisonError("baseline and candidate run IDs must differ")
        _validate_tick(self.evaluated_at_tick, field="evaluated_at_tick")
        _validate_control_id(self.invariant_id, field="invariant_id")
        if not isinstance(self.invariant_class, InvariantClass):
            raise ComparisonError("invariant_class must be an InvariantClass value")
        if not isinstance(self.severity, AssertionSeverity):
            raise ComparisonError("severity must be an AssertionSeverity value")
        if not isinstance(self.kind, ComparisonKind):
            raise ComparisonError("kind must be a ComparisonKind value")
        if not isinstance(self.policy, ComparisonPolicy):
            raise ComparisonError("policy must be a ComparisonPolicy value")
        if not isinstance(self.status, ComparisonStatus):
            raise ComparisonError("status must be a ComparisonStatus value")
        if not isinstance(self.reason, ComparisonReason):
            raise ComparisonError("reason must be a ComparisonReason value")
        if not isinstance(self.pairs, tuple) or not all(
            isinstance(pair, ResultComparison) for pair in self.pairs
        ):
            raise ComparisonError("pairs must be a tuple of ResultComparison values")
        if len(self.pairs) > MAX_COMPARISON_PAIRS:
            raise ComparisonError(f"pairs must not exceed {MAX_COMPARISON_PAIRS} entries")
        pair_hashes = tuple(pair.key.key_sha256 for pair in self.pairs)
        if len(pair_hashes) != len(set(pair_hashes)):
            raise ComparisonError("pairs must use unique comparison keys")
        if pair_hashes != tuple(sorted(pair_hashes)):
            raise ComparisonError("pairs must be ordered by key_sha256")
        if not isinstance(self.violations, tuple) or not all(
            isinstance(key, ComparisonKey) for key in self.violations
        ):
            raise ComparisonError("violations must be a tuple of ComparisonKey values")
        violation_hashes = tuple(key.key_sha256 for key in self.violations)
        if len(violation_hashes) != len(set(violation_hashes)):
            raise ComparisonError("violations must use unique comparison keys")
        if violation_hashes != tuple(sorted(violation_hashes)):
            raise ComparisonError("violations must be ordered by key_sha256")
        if not set(violation_hashes).issubset(pair_hashes):
            raise ComparisonError("violations must reference keys present in pairs")

    @property
    def pair_count(self) -> int:
        """Return the total number of unioned semantic result keys."""

        return len(self.pairs)

    @property
    def paired_result_count(self) -> int:
        """Return the number of keys present on both sides."""

        return sum(pair.paired for pair in self.pairs)

    @property
    def unpaired_result_count(self) -> int:
        """Return the number of keys missing from either side."""

        return sum(not pair.paired for pair in self.pairs)

    @property
    def changed_pair_count(self) -> int:
        """Return the number of keys with at least one semantic difference."""

        return sum(pair.changed for pair in self.pairs)

    @property
    def violation_count(self) -> int:
        """Return the number of policy-violating comparison keys."""

        return len(self.violations)

    @property
    def report_sha256(self) -> str:
        """Return the digest binding definition, input series, and outcome."""

        return calculate_comparison_report_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "baseline_run_id": self.baseline_run_id,
            "baseline_series_sha256": self.baseline_series_sha256,
            "candidate_run_id": self.candidate_run_id,
            "candidate_series_sha256": self.candidate_series_sha256,
            "changed_pair_count": self.changed_pair_count,
            "comparison_definition_sha256": self.comparison_definition_sha256,
            "comparison_id": self.comparison_id,
            "comparison_schema_version": SUPPORTED_COMPARISON_SCHEMA_VERSION,
            "evaluated_at_tick": self.evaluated_at_tick,
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "kind": self.kind.value,
            "pair_count": self.pair_count,
            "paired_result_count": self.paired_result_count,
            "pairs": [pair.to_mapping() for pair in self.pairs],
            "policy": self.policy.value,
            "reason": self.reason.value,
            "report_id": self.report_id,
            "report_type": "COMPARISON_REPORT",
            "scenario_id": self.scenario_id,
            "severity": self.severity.value,
            "status": self.status.value,
            "unpaired_result_count": self.unpaired_result_count,
            "violation_count": self.violation_count,
            "violations": [key.to_mapping() for key in self.violations],
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete validator-owned comparison report."""

        return {**self._content_mapping(), "report_sha256": self.report_sha256}

    def to_evidence_mapping(self) -> dict[str, object]:
        """Return a compact report summary without assertion actual values."""

        return {
            "baseline_run_id": self.baseline_run_id,
            "baseline_series_sha256": self.baseline_series_sha256,
            "candidate_run_id": self.candidate_run_id,
            "candidate_series_sha256": self.candidate_series_sha256,
            "changed_pair_count": self.changed_pair_count,
            "comparison_definition_sha256": self.comparison_definition_sha256,
            "comparison_id": self.comparison_id,
            "evaluated_at_tick": self.evaluated_at_tick,
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "kind": self.kind.value,
            "pair_count": self.pair_count,
            "paired_result_count": self.paired_result_count,
            "policy": self.policy.value,
            "reason": self.reason.value,
            "report_id": self.report_id,
            "report_sha256": self.report_sha256,
            "severity": self.severity.value,
            "status": self.status.value,
            "unpaired_result_count": self.unpaired_result_count,
            "violation_count": self.violation_count,
            "violation_key_sha256": [key.key_sha256 for key in self.violations],
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> ComparisonReport:
        """Parse and verify a serialized comparison report."""

        mapping = _require_mapping(value, field="comparison report")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "baseline_run_id",
                    "baseline_series_sha256",
                    "candidate_run_id",
                    "candidate_series_sha256",
                    "changed_pair_count",
                    "comparison_definition_sha256",
                    "comparison_id",
                    "comparison_schema_version",
                    "evaluated_at_tick",
                    "invariant_class",
                    "invariant_id",
                    "kind",
                    "pair_count",
                    "paired_result_count",
                    "pairs",
                    "policy",
                    "reason",
                    "report_id",
                    "report_sha256",
                    "report_type",
                    "scenario_id",
                    "severity",
                    "status",
                    "unpaired_result_count",
                    "violation_count",
                    "violations",
                }
            ),
            field="comparison report",
        )
        _validate_schema_version(mapping["comparison_schema_version"])
        if mapping["report_type"] != "COMPARISON_REPORT":
            raise ComparisonError("unsupported report_type")
        report = cls(
            report_id=_require_string(mapping["report_id"], field="comparison report.report_id"),
            comparison_id=_require_string(
                mapping["comparison_id"], field="comparison report.comparison_id"
            ),
            comparison_definition_sha256=_require_string(
                mapping["comparison_definition_sha256"],
                field="comparison report.comparison_definition_sha256",
            ),
            scenario_id=_require_string(
                mapping["scenario_id"], field="comparison report.scenario_id"
            ),
            baseline_run_id=_require_string(
                mapping["baseline_run_id"],
                field="comparison report.baseline_run_id",
            ),
            baseline_series_sha256=_require_string(
                mapping["baseline_series_sha256"],
                field="comparison report.baseline_series_sha256",
            ),
            candidate_run_id=_require_string(
                mapping["candidate_run_id"],
                field="comparison report.candidate_run_id",
            ),
            candidate_series_sha256=_require_string(
                mapping["candidate_series_sha256"],
                field="comparison report.candidate_series_sha256",
            ),
            evaluated_at_tick=_require_integer(
                mapping["evaluated_at_tick"],
                field="comparison report.evaluated_at_tick",
            ),
            invariant_id=_require_string(
                mapping["invariant_id"], field="comparison report.invariant_id"
            ),
            invariant_class=_parse_enum(
                InvariantClass,
                mapping["invariant_class"],
                field="comparison report.invariant_class",
            ),
            severity=_parse_enum(
                AssertionSeverity,
                mapping["severity"],
                field="comparison report.severity",
            ),
            kind=_parse_enum(
                ComparisonKind,
                mapping["kind"],
                field="comparison report.kind",
            ),
            policy=_parse_enum(
                ComparisonPolicy,
                mapping["policy"],
                field="comparison report.policy",
            ),
            status=_parse_enum(
                ComparisonStatus,
                mapping["status"],
                field="comparison report.status",
            ),
            reason=_parse_enum(
                ComparisonReason,
                mapping["reason"],
                field="comparison report.reason",
            ),
            pairs=_parse_pairs(mapping["pairs"]),
            violations=_parse_keys(mapping["violations"], field="comparison report.violations"),
        )
        _validate_report_derived_fields(report, mapping)
        _validate_declared_sha256(
            report.report_sha256,
            mapping,
            key="report_sha256",
            field="comparison report",
        )
        return report


def create_comparison_definition(
    *,
    comparison_id: str,
    scenario_id: str,
    baseline_run_id: str,
    candidate_run_id: str,
    invariant_id: str,
    invariant_class: InvariantClass,
    severity: AssertionSeverity,
    kind: ComparisonKind,
    policy: ComparisonPolicy,
    assertion_ids: tuple[str, ...] = (),
    minimum_paired_results: int = 1,
    allow_unpaired_results: bool = False,
) -> ComparisonDefinition:
    """Create a comparison definition with canonical assertion-ID ordering."""

    if not isinstance(assertion_ids, tuple):
        raise ComparisonError("assertion_ids must be a tuple")
    return ComparisonDefinition(
        comparison_id=comparison_id,
        scenario_id=scenario_id,
        baseline_run_id=baseline_run_id,
        candidate_run_id=candidate_run_id,
        invariant_id=invariant_id,
        invariant_class=invariant_class,
        severity=severity,
        kind=kind,
        policy=policy,
        assertion_ids=tuple(sorted(assertion_ids)),
        minimum_paired_results=minimum_paired_results,
        allow_unpaired_results=allow_unpaired_results,
    )


def compare_assertion_series(
    definition: ComparisonDefinition,
    baseline: AssertionSeries,
    candidate: AssertionSeries,
    *,
    report_id: str,
    evaluated_at_tick: int,
) -> ComparisonReport:
    """Apply one declared differential relation to two assertion series."""

    _validate_comparison_inputs(definition, baseline, candidate)
    _validate_control_id(report_id, field="report_id")
    _validate_tick(evaluated_at_tick, field="evaluated_at_tick")
    pairs, raw_results = _pair_assertion_results(definition, baseline, candidate)
    status, reason, violations = _evaluate_policy(definition, pairs, raw_results)
    return ComparisonReport(
        report_id=report_id,
        comparison_id=definition.comparison_id,
        comparison_definition_sha256=definition.comparison_sha256,
        scenario_id=definition.scenario_id,
        baseline_run_id=baseline.run_id,
        baseline_series_sha256=baseline.series_sha256,
        candidate_run_id=candidate.run_id,
        candidate_series_sha256=candidate.series_sha256,
        evaluated_at_tick=evaluated_at_tick,
        invariant_id=definition.invariant_id,
        invariant_class=definition.invariant_class,
        severity=definition.severity,
        kind=definition.kind,
        policy=definition.policy,
        status=status,
        reason=reason,
        pairs=pairs,
        violations=violations,
    )


def validate_comparison_report(
    report: ComparisonReport,
    definition: ComparisonDefinition,
    baseline: AssertionSeries,
    candidate: AssertionSeries,
) -> None:
    """Recompute and verify a comparison report against its exact inputs."""

    if not isinstance(report, ComparisonReport):
        raise ComparisonError("report must be a ComparisonReport")
    expected = compare_assertion_series(
        definition,
        baseline,
        candidate,
        report_id=report.report_id,
        evaluated_at_tick=report.evaluated_at_tick,
    )
    if report != expected:
        raise ComparisonError("comparison report does not match its definition and inputs")


def create_comparison_evidence_payload(report: ComparisonReport) -> EvidencePayload:
    """Create a compact validator evidence payload for one comparison report."""

    if not isinstance(report, ComparisonReport):
        raise ComparisonError("report must be a ComparisonReport")
    return create_evidence_payload(report.to_evidence_mapping())


def calculate_comparison_definition_sha256(definition: ComparisonDefinition) -> str:
    """Calculate the canonical digest for one comparison definition."""

    if not isinstance(definition, ComparisonDefinition):
        raise ComparisonError("definition must be a ComparisonDefinition")
    return hashlib.sha256(_canonical_json_bytes(definition._content_mapping())).hexdigest()


def calculate_comparison_report_sha256(report: ComparisonReport) -> str:
    """Calculate the canonical digest for one comparison report."""

    if not isinstance(report, ComparisonReport):
        raise ComparisonError("report must be a ComparisonReport")
    return hashlib.sha256(_canonical_json_bytes(report._content_mapping())).hexdigest()


type _BaseKey = tuple[str, AssertionTargetKind, EvidenceDomain, str | None]
type _RawPair = tuple[AssertionResult | None, AssertionResult | None]


def _validate_comparison_inputs(
    definition: ComparisonDefinition,
    baseline: AssertionSeries,
    candidate: AssertionSeries,
) -> None:
    if not isinstance(definition, ComparisonDefinition):
        raise ComparisonError("definition must be a ComparisonDefinition")
    if not isinstance(baseline, AssertionSeries):
        raise ComparisonError("baseline must be an AssertionSeries")
    if not isinstance(candidate, AssertionSeries):
        raise ComparisonError("candidate must be an AssertionSeries")
    if baseline.scenario_id != definition.scenario_id:
        raise ComparisonError("baseline scenario does not match comparison definition")
    if candidate.scenario_id != definition.scenario_id:
        raise ComparisonError("candidate scenario does not match comparison definition")
    if baseline.run_id != definition.baseline_run_id:
        raise ComparisonError("baseline run does not match comparison definition")
    if candidate.run_id != definition.candidate_run_id:
        raise ComparisonError("candidate run does not match comparison definition")


def _pair_assertion_results(
    definition: ComparisonDefinition,
    baseline: AssertionSeries,
    candidate: AssertionSeries,
) -> tuple[tuple[ResultComparison, ...], dict[str, _RawPair]]:
    selected = None if not definition.assertion_ids else frozenset(definition.assertion_ids)
    baseline_index = _index_results(baseline.results, selected)
    candidate_index = _index_results(candidate.results, selected)
    all_keys = set(baseline_index) | set(candidate_index)
    if len(all_keys) > MAX_COMPARISON_PAIRS:
        raise ComparisonError(f"comparison must not exceed {MAX_COMPARISON_PAIRS} result pairs")

    pairs: list[ResultComparison] = []
    raw_results: dict[str, _RawPair] = {}
    for key in all_keys:
        baseline_result = baseline_index.get(key)
        candidate_result = candidate_index.get(key)
        baseline_operand = None if baseline_result is None else _create_operand(baseline_result)
        candidate_operand = None if candidate_result is None else _create_operand(candidate_result)
        comparison_key = ComparisonKey(
            assertion_id=key[0],
            target_kind=key[1],
            target_domain=key[2],
            path=key[3],
            occurrence=key[4],
        )
        pair = ResultComparison(
            key=comparison_key,
            baseline=baseline_operand,
            candidate=candidate_operand,
            differences=_derive_differences(baseline_operand, candidate_operand),
        )
        pairs.append(pair)
        raw_results[comparison_key.key_sha256] = (baseline_result, candidate_result)
    pairs.sort(key=lambda pair: pair.key.key_sha256)
    return tuple(pairs), raw_results


def _index_results(
    results: tuple[AssertionResult, ...],
    selected: frozenset[str] | None,
) -> dict[tuple[str, AssertionTargetKind, EvidenceDomain, str | None, int], AssertionResult]:
    occurrence_counts: defaultdict[_BaseKey, int] = defaultdict(int)
    indexed: dict[
        tuple[str, AssertionTargetKind, EvidenceDomain, str | None, int],
        AssertionResult,
    ] = {}
    for result in results:
        if selected is not None and result.assertion_id not in selected:
            continue
        base_key: _BaseKey = (
            result.assertion_id,
            result.target_kind,
            result.target_domain,
            result.path,
        )
        occurrence = occurrence_counts[base_key]
        occurrence_counts[base_key] += 1
        indexed[(*base_key, occurrence)] = result
    return indexed


def _create_operand(result: AssertionResult) -> ComparisonOperand:
    return ComparisonOperand(
        result_id=result.result_id,
        result_sha256=result.result_sha256,
        assertion_id=result.assertion_id,
        assertion_sha256=result.assertion_sha256,
        target_kind=result.target_kind,
        target_domain=result.target_domain,
        target_id=result.target_id,
        target_sha256=result.target_sha256,
        path=result.path,
        invariant_id=result.invariant_id,
        invariant_class=result.invariant_class,
        severity=result.severity,
        status=result.status,
        reason=result.reason,
        actual_value_sha256=(None if result.actual is None else result.actual.value_sha256),
    )


def _derive_differences(
    baseline: ComparisonOperand | None,
    candidate: ComparisonOperand | None,
) -> tuple[DifferenceKind, ...]:
    differences: list[DifferenceKind] = []
    if baseline is None:
        differences.append(DifferenceKind.MISSING_BASELINE)
    if candidate is None:
        differences.append(DifferenceKind.MISSING_CANDIDATE)
    if baseline is not None and candidate is not None:
        if (
            baseline.assertion_sha256 != candidate.assertion_sha256
            or baseline.invariant_id != candidate.invariant_id
            or baseline.invariant_class is not candidate.invariant_class
            or baseline.severity is not candidate.severity
        ):
            differences.append(DifferenceKind.DEFINITION_CHANGED)
        if baseline.status is not candidate.status:
            differences.append(DifferenceKind.STATUS_CHANGED)
        if baseline.reason is not candidate.reason:
            differences.append(DifferenceKind.REASON_CHANGED)
        if baseline.actual_value_sha256 != candidate.actual_value_sha256:
            differences.append(DifferenceKind.ACTUAL_CHANGED)
    return tuple(sorted(differences, key=_DIFFERENCE_ORDER.__getitem__))


def _evaluate_policy(
    definition: ComparisonDefinition,
    pairs: tuple[ResultComparison, ...],
    raw_results: Mapping[str, _RawPair],
) -> tuple[ComparisonStatus, ComparisonReason, tuple[ComparisonKey, ...]]:
    paired = tuple(pair for pair in pairs if pair.paired)
    unpaired = tuple(pair for pair in pairs if not pair.paired)
    if len(paired) < definition.minimum_paired_results:
        return (
            ComparisonStatus.BLOCKED,
            ComparisonReason.INSUFFICIENT_PAIRED_RESULTS,
            _sorted_keys(pair.key for pair in unpaired),
        )
    if unpaired and not definition.allow_unpaired_results:
        return (
            ComparisonStatus.BLOCKED,
            ComparisonReason.INCOMPLETE_PAIRING,
            _sorted_keys(pair.key for pair in unpaired),
        )

    incompatible = tuple(
        pair for pair in paired if DifferenceKind.DEFINITION_CHANGED in pair.differences
    )
    if incompatible:
        return (
            ComparisonStatus.BLOCKED,
            ComparisonReason.INCOMPATIBLE_ASSERTION_DEFINITION,
            _sorted_keys(pair.key for pair in incompatible),
        )

    blocked = tuple(
        pair
        for pair in paired
        if pair.baseline is not None
        and pair.candidate is not None
        and (
            pair.baseline.status is AssertionStatus.BLOCKED
            or pair.candidate.status is AssertionStatus.BLOCKED
        )
    )
    if blocked:
        return (
            ComparisonStatus.BLOCKED,
            ComparisonReason.BLOCKED_ASSERTION_RESULT,
            _sorted_keys(pair.key for pair in blocked),
        )

    if definition.policy is ComparisonPolicy.EXACT:
        violations = tuple(pair for pair in paired if pair.differences)
        return _policy_outcome(
            definition,
            violations,
            pass_reason=ComparisonReason.EXACT_MATCH,
            failure_reason=ComparisonReason.UNEXPECTED_DIVERGENCE,
        )
    if definition.policy is ComparisonPolicy.OUTCOME_EQUIVALENT:
        violations = tuple(
            pair
            for pair in paired
            if pair.baseline is not None
            and pair.candidate is not None
            and pair.baseline.status is not pair.candidate.status
        )
        return _policy_outcome(
            definition,
            violations,
            pass_reason=ComparisonReason.OUTCOMES_EQUIVALENT,
            failure_reason=ComparisonReason.UNEXPECTED_DIVERGENCE,
        )
    if definition.policy is ComparisonPolicy.ACTUAL_EQUIVALENT:
        violations = tuple(
            pair
            for pair in paired
            if pair.baseline is not None
            and pair.candidate is not None
            and pair.baseline.actual_value_sha256 != pair.candidate.actual_value_sha256
        )
        return _policy_outcome(
            definition,
            violations,
            pass_reason=ComparisonReason.ACTUALS_EQUIVALENT,
            failure_reason=ComparisonReason.UNEXPECTED_DIVERGENCE,
        )
    if definition.policy is ComparisonPolicy.EXPECTED_DIVERGENCE:
        divergent = tuple(pair for pair in paired if pair.differences)
        if divergent:
            return (
                ComparisonStatus.PASS,
                ComparisonReason.EXPECTED_DIVERGENCE_OBSERVED,
                (),
            )
        return (
            _failure_status(definition),
            ComparisonReason.REQUIRED_DIVERGENCE_NOT_OBSERVED,
            _sorted_keys(pair.key for pair in paired),
        )
    if definition.policy is ComparisonPolicy.NO_STATUS_REGRESSION:
        regressions = tuple(pair for pair in paired if _is_status_regression(pair))
        return _policy_outcome(
            definition,
            regressions,
            pass_reason=ComparisonReason.NO_STATUS_REGRESSION,
            failure_reason=ComparisonReason.STATUS_REGRESSION,
        )
    return _evaluate_numeric_policy(definition, paired, raw_results)


def _evaluate_numeric_policy(
    definition: ComparisonDefinition,
    paired: tuple[ResultComparison, ...],
    raw_results: Mapping[str, _RawPair],
) -> tuple[ComparisonStatus, ComparisonReason, tuple[ComparisonKey, ...]]:
    non_numeric: list[ComparisonKey] = []
    violations: list[ComparisonKey] = []
    for pair in paired:
        baseline_result, candidate_result = raw_results[pair.key.key_sha256]
        if baseline_result is None or candidate_result is None:
            raise ComparisonError("paired comparison is missing raw assertion results")
        baseline_value = _decode_numeric_actual(baseline_result)
        candidate_value = _decode_numeric_actual(candidate_result)
        if baseline_value is None or candidate_value is None:
            non_numeric.append(pair.key)
            continue
        if definition.policy is ComparisonPolicy.ACTUAL_NON_INCREASING:
            satisfied = candidate_value <= baseline_value
        else:
            satisfied = candidate_value >= baseline_value
        if not satisfied:
            violations.append(pair.key)
    if non_numeric:
        return (
            ComparisonStatus.BLOCKED,
            ComparisonReason.NON_NUMERIC_ACTUAL,
            _sorted_keys(non_numeric),
        )
    if violations:
        return (
            _failure_status(definition),
            ComparisonReason.NUMERIC_RELATION_VIOLATED,
            _sorted_keys(violations),
        )
    return ComparisonStatus.PASS, ComparisonReason.NUMERIC_RELATION_SATISFIED, ()


def _decode_numeric_actual(result: AssertionResult) -> int | float | None:
    if result.actual is None:
        return None
    value = result.actual.decode()
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return value


def _is_status_regression(pair: ResultComparison) -> bool:
    if pair.baseline is None or pair.candidate is None:
        return False
    if (
        pair.baseline.status is AssertionStatus.BLOCKED
        or pair.candidate.status is AssertionStatus.BLOCKED
    ):
        return False
    return _STATUS_QUALITY[pair.candidate.status] > _STATUS_QUALITY[pair.baseline.status]


def _policy_outcome(
    definition: ComparisonDefinition,
    violations: tuple[ResultComparison, ...],
    *,
    pass_reason: ComparisonReason,
    failure_reason: ComparisonReason,
) -> tuple[ComparisonStatus, ComparisonReason, tuple[ComparisonKey, ...]]:
    if not violations:
        return ComparisonStatus.PASS, pass_reason, ()
    return (
        _failure_status(definition),
        failure_reason,
        _sorted_keys(pair.key for pair in violations),
    )


def _failure_status(definition: ComparisonDefinition) -> ComparisonStatus:
    if definition.invariant_class is InvariantClass.HARD:
        return ComparisonStatus.FAIL
    return ComparisonStatus.REVIEW


def _sorted_keys(keys: Iterable[ComparisonKey]) -> tuple[ComparisonKey, ...]:
    return tuple(sorted(keys, key=lambda key: key.key_sha256))


def _parse_optional_operand(value: object, *, field: str) -> ComparisonOperand | None:
    if value is None:
        return None
    return ComparisonOperand.from_mapping(_require_mapping(value, field=field))


def _parse_pairs(value: object) -> tuple[ResultComparison, ...]:
    if not isinstance(value, list):
        raise ComparisonError("comparison report.pairs must be an array")
    return tuple(
        ResultComparison.from_mapping(
            _require_mapping(item, field=f"comparison report.pairs[{index}]")
        )
        for index, item in enumerate(value)
    )


def _parse_keys(value: object, *, field: str) -> tuple[ComparisonKey, ...]:
    if not isinstance(value, list):
        raise ComparisonError(f"{field} must be an array")
    return tuple(
        ComparisonKey.from_mapping(_require_mapping(item, field=f"{field}[{index}]"))
        for index, item in enumerate(value)
    )


def _validate_report_derived_fields(
    report: ComparisonReport,
    mapping: Mapping[str, object],
) -> None:
    expected_counts = {
        "changed_pair_count": report.changed_pair_count,
        "pair_count": report.pair_count,
        "paired_result_count": report.paired_result_count,
        "unpaired_result_count": report.unpaired_result_count,
        "violation_count": report.violation_count,
    }
    for field, expected in expected_counts.items():
        declared = _require_integer(mapping[field], field=f"comparison report.{field}")
        if declared != expected:
            raise ComparisonError(f"declared {field} does not match comparison report")


def _parse_string_tuple(value: object, *, field: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ComparisonError(f"{field} must be an array")
    return tuple(
        _require_string(item, field=f"{field}[{index}]") for index, item in enumerate(value)
    )


def _parse_enum_tuple[T: StrEnum](
    enum_type: type[T],
    value: object,
    *,
    field: str,
) -> tuple[T, ...]:
    if not isinstance(value, list):
        raise ComparisonError(f"{field} must be an array")
    return tuple(
        _parse_enum(enum_type, item, field=f"{field}[{index}]") for index, item in enumerate(value)
    )


def _validate_schema_version(value: object) -> None:
    version = _require_string(value, field="comparison_schema_version")
    if version != SUPPORTED_COMPARISON_SCHEMA_VERSION:
        raise ComparisonError(f"unsupported comparison_schema_version: {version}")


def _validate_declared_sha256(
    calculated_sha256: str,
    mapping: Mapping[str, object],
    *,
    key: str,
    field: str,
) -> None:
    declared_sha256 = _require_string(mapping[key], field=f"{field}.{key}")
    if declared_sha256 != calculated_sha256:
        raise ComparisonError(f"declared {key} does not match {field}")


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
        raise ComparisonError("value must be canonical finite JSON") from exc


def _require_mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ComparisonError(f"{field} must be an object")
    for key in value:
        if not isinstance(key, str):
            raise ComparisonError(f"{field} keys must be strings")
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
        raise ComparisonError(f"{field} is missing required fields: {', '.join(missing)}")
    if unexpected:
        raise ComparisonError(f"{field} contains unexpected fields: {', '.join(unexpected)}")


def _require_string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        raise ComparisonError(f"{field} must be a string")
    return value


def _require_optional_string(value: object, *, field: str) -> str | None:
    if value is None:
        return None
    return _require_string(value, field=field)


def _require_integer(value: object, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ComparisonError(f"{field} must be an integer")
    return value


def _require_boolean(value: object, *, field: str) -> bool:
    if not isinstance(value, bool):
        raise ComparisonError(f"{field} must be a boolean")
    return value


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
        raise ComparisonError(f"{field} contains an unsupported value: {raw}") from exc


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise ComparisonError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise ComparisonError(f"{field} must be a stable uppercase control identifier")


def _validate_scenario_id(value: str) -> None:
    if not isinstance(value, str):
        raise ComparisonError("scenario_id must be a string")
    if _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        raise ComparisonError("scenario_id must match AURORA-SCN-<FAMILY>-<NNN>")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise ComparisonError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise ComparisonError(f"{field} must be a lowercase SHA-256 digest")


def _validate_json_pointer(value: str) -> None:
    if not isinstance(value, str):
        raise ComparisonError("path must be a string")
    if _JSON_POINTER_PATTERN.fullmatch(value) is None:
        raise ComparisonError("path must be a non-empty RFC 6901 JSON Pointer")


def _validate_positive_integer(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ComparisonError(f"{field} must be an integer")
    if value < 1:
        raise ComparisonError(f"{field} must be positive")


def _validate_sequence(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ComparisonError(f"{field} must be an integer")
    if value < 0:
        raise ComparisonError(f"{field} must be non-negative")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ComparisonError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise ComparisonError(f"{field} must be between 0 and {MAX_TICK}")


__all__ = [
    "MAX_COMPARISON_ASSERTION_IDS",
    "MAX_COMPARISON_PAIRS",
    "MAX_TICK",
    "SUPPORTED_COMPARISON_SCHEMA_VERSION",
    "ComparisonDefinition",
    "ComparisonError",
    "ComparisonKey",
    "ComparisonKind",
    "ComparisonOperand",
    "ComparisonPolicy",
    "ComparisonReason",
    "ComparisonReport",
    "ComparisonStatus",
    "DifferenceKind",
    "ResultComparison",
    "calculate_comparison_definition_sha256",
    "calculate_comparison_report_sha256",
    "compare_assertion_series",
    "create_comparison_definition",
    "create_comparison_evidence_payload",
    "validate_comparison_report",
]
