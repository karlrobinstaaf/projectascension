"""Deterministic scenario verdicts for Aurora validation runs.

The module converts validator-owned assertion and comparison results into one
portable scenario outcome.  Execution validity remains separate from Aurora's
behavioral outcome: an invalid run is BLOCKED, never silently passed and never
misclassified as an Aurora failure.  Findings contain provenance and outcome
metadata only; raw assertion values remain outside the verdict artifact.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Final, cast

from aurora_validation_harness.assertions import (
    AssertionResult,
    AssertionSeries,
    AssertionSeverity,
    InvariantClass,
)
from aurora_validation_harness.comparison import ComparisonReport
from aurora_validation_harness.evidence import EvidencePayload, create_evidence_payload

SUPPORTED_VERDICT_SCHEMA_VERSION: Final[str] = "1.0"
MAX_VERDICT_REQUIRED_IDS: Final[int] = 50_000
MAX_VERDICT_FINDINGS: Final[int] = 1_000_000
MAX_VERDICT_OBSERVATIONS: Final[int] = 100_000
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")


class VerdictError(ValueError):
    """Raised when verdict inputs, policy, or serialized integrity are invalid."""


class ExecutionValidity(StrEnum):
    """Whether a run is eligible for behavioral evaluation."""

    VALID_RUN = "VALID_RUN"
    INVALID_RUN = "INVALID_RUN"


class ExecutionValidityReason(StrEnum):
    """Stable reason for the separately recorded execution-validity result."""

    VERIFIED = "VERIFIED"
    BASELINE_INVALID = "BASELINE_INVALID"
    CONFIGURATION_INVALID = "CONFIGURATION_INVALID"
    FIXTURE_INVALID = "FIXTURE_INVALID"
    PARTITION_INVALID = "PARTITION_INVALID"
    CHANNEL_INVALID = "CHANNEL_INVALID"
    EVENT_SEQUENCE_INVALID = "EVENT_SEQUENCE_INVALID"
    EVIDENCE_INVALID = "EVIDENCE_INVALID"
    STATE_CAPTURE_INVALID = "STATE_CAPTURE_INVALID"
    RESET_INVALID = "RESET_INVALID"
    REPLAY_INVALID = "REPLAY_INVALID"
    HARNESS_ERROR = "HARNESS_ERROR"


class VerdictOutcome(StrEnum):
    """Canonical scenario execution outcome."""

    PASS = "PASS"
    PASS_WITH_OBSERVATION = "PASS_WITH_OBSERVATION"
    REVIEW = "REVIEW"
    FAIL = "FAIL"
    BLOCKED = "BLOCKED"


class VerdictReason(StrEnum):
    """Stable explanation code for one derived scenario outcome."""

    ALL_REQUIRED_RESULTS_PASSED = "ALL_REQUIRED_RESULTS_PASSED"
    VALID_WITH_OBSERVATIONS = "VALID_WITH_OBSERVATIONS"
    SOURCE_REVIEW_REQUIRED = "SOURCE_REVIEW_REQUIRED"
    NON_HARD_INVARIANT_FAILED = "NON_HARD_INVARIANT_FAILED"
    HARD_INVARIANT_FAILED = "HARD_INVARIANT_FAILED"
    EXECUTION_INVALID = "EXECUTION_INVALID"
    REQUIRED_RESULT_BLOCKED = "REQUIRED_RESULT_BLOCKED"
    MISSING_REQUIRED_RESULT = "MISSING_REQUIRED_RESULT"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class VerdictFindingKind(StrEnum):
    """Validator result type normalized into a verdict finding."""

    ASSERTION_RESULT = "ASSERTION_RESULT"
    COMPARISON_REPORT = "COMPARISON_REPORT"


class VerdictFindingStatus(StrEnum):
    """Common result status used during verdict aggregation."""

    PASS = "PASS"
    FAIL = "FAIL"
    REVIEW = "REVIEW"
    BLOCKED = "BLOCKED"


class ObservationCategory(StrEnum):
    """Canonical category for valid but noteworthy behavior."""

    BEHAVIORAL_VARIATION = "BEHAVIORAL_VARIATION"
    EMERGENCE = "EMERGENCE"
    PERFORMANCE = "PERFORMANCE"
    DIAGNOSTIC = "DIAGNOSTIC"
    REGRESSION_CANDIDATE = "REGRESSION_CANDIDATE"
    OTHER = "OTHER"


@dataclass(frozen=True, slots=True)
class VerdictDefinition:
    """Immutable declaration of the evidence required for a scenario verdict."""

    verdict_definition_id: str
    scenario_id: str
    primary_run_id: str
    required_assertion_ids: tuple[str, ...] = ()
    required_comparison_ids: tuple[str, ...] = ()
    minimum_finding_count: int = 1

    def __post_init__(self) -> None:
        _validate_control_id(self.verdict_definition_id, field="verdict_definition_id")
        _validate_scenario_id(self.scenario_id)
        _validate_control_id(self.primary_run_id, field="primary_run_id")
        _validate_required_ids(self.required_assertion_ids, field="required_assertion_ids")
        _validate_required_ids(self.required_comparison_ids, field="required_comparison_ids")
        _validate_positive_integer(self.minimum_finding_count, field="minimum_finding_count")
        if self.minimum_finding_count > MAX_VERDICT_FINDINGS:
            raise VerdictError(f"minimum_finding_count must not exceed {MAX_VERDICT_FINDINGS}")

    @property
    def definition_sha256(self) -> str:
        """Return the digest of the complete verdict declaration."""

        return calculate_verdict_definition_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "minimum_finding_count": self.minimum_finding_count,
            "primary_run_id": self.primary_run_id,
            "required_assertion_ids": list(self.required_assertion_ids),
            "required_comparison_ids": list(self.required_comparison_ids),
            "scenario_id": self.scenario_id,
            "verdict_definition_id": self.verdict_definition_id,
            "verdict_schema_version": SUPPORTED_VERDICT_SCHEMA_VERSION,
            "verdict_type": "VERDICT_DEFINITION",
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable verdict definition."""

        return {**self._content_mapping(), "definition_sha256": self.definition_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> VerdictDefinition:
        """Parse and verify a serialized verdict definition."""

        mapping = _require_mapping(value, field="verdict definition")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "definition_sha256",
                    "minimum_finding_count",
                    "primary_run_id",
                    "required_assertion_ids",
                    "required_comparison_ids",
                    "scenario_id",
                    "verdict_definition_id",
                    "verdict_schema_version",
                    "verdict_type",
                }
            ),
            field="verdict definition",
        )
        _validate_schema_version(mapping["verdict_schema_version"])
        if mapping["verdict_type"] != "VERDICT_DEFINITION":
            raise VerdictError("unsupported verdict_type")
        definition = cls(
            verdict_definition_id=_require_string(
                mapping["verdict_definition_id"],
                field="verdict definition.verdict_definition_id",
            ),
            scenario_id=_require_string(
                mapping["scenario_id"], field="verdict definition.scenario_id"
            ),
            primary_run_id=_require_string(
                mapping["primary_run_id"],
                field="verdict definition.primary_run_id",
            ),
            required_assertion_ids=_parse_string_tuple(
                mapping["required_assertion_ids"],
                field="verdict definition.required_assertion_ids",
            ),
            required_comparison_ids=_parse_string_tuple(
                mapping["required_comparison_ids"],
                field="verdict definition.required_comparison_ids",
            ),
            minimum_finding_count=_require_integer(
                mapping["minimum_finding_count"],
                field="verdict definition.minimum_finding_count",
            ),
        )
        _validate_declared_sha256(
            definition.definition_sha256,
            mapping,
            key="definition_sha256",
            field="verdict definition",
        )
        return definition


@dataclass(frozen=True, slots=True)
class VerdictFinding:
    """Value-redacted normalized result used by the verdict policy."""

    kind: VerdictFindingKind
    source_id: str
    source_sha256: str
    scenario_id: str
    run_ids: tuple[str, ...]
    invariant_id: str
    invariant_class: InvariantClass
    severity: AssertionSeverity
    status: VerdictFindingStatus
    reason_code: str

    def __post_init__(self) -> None:
        if not isinstance(self.kind, VerdictFindingKind):
            raise VerdictError("kind must be a VerdictFindingKind value")
        _validate_control_id(self.source_id, field="source_id")
        _validate_sha256(self.source_sha256, field="source_sha256")
        _validate_scenario_id(self.scenario_id)
        if not isinstance(self.run_ids, tuple) or not all(
            isinstance(run_id, str) for run_id in self.run_ids
        ):
            raise VerdictError("run_ids must be a tuple of strings")
        expected_run_count = 1 if self.kind is VerdictFindingKind.ASSERTION_RESULT else 2
        if len(self.run_ids) != expected_run_count:
            raise VerdictError(
                f"{self.kind.value} findings require exactly {expected_run_count} run IDs"
            )
        for run_id in self.run_ids:
            _validate_control_id(run_id, field="run_ids entry")
        if len(self.run_ids) != len(set(self.run_ids)):
            raise VerdictError("run_ids must not contain duplicates")
        _validate_control_id(self.invariant_id, field="invariant_id")
        if not isinstance(self.invariant_class, InvariantClass):
            raise VerdictError("invariant_class must be an InvariantClass value")
        if not isinstance(self.severity, AssertionSeverity):
            raise VerdictError("severity must be an AssertionSeverity value")
        if not isinstance(self.status, VerdictFindingStatus):
            raise VerdictError("status must be a VerdictFindingStatus value")
        _validate_control_id(self.reason_code, field="reason_code")

    @property
    def finding_sha256(self) -> str:
        """Return the digest of this normalized finding."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "invariant_class": self.invariant_class.value,
            "invariant_id": self.invariant_id,
            "kind": self.kind.value,
            "reason_code": self.reason_code,
            "run_ids": list(self.run_ids),
            "scenario_id": self.scenario_id,
            "severity": self.severity.value,
            "source_id": self.source_id,
            "source_sha256": self.source_sha256,
            "status": self.status.value,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable finding representation."""

        return {**self._content_mapping(), "finding_sha256": self.finding_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> VerdictFinding:
        """Parse and verify one serialized verdict finding."""

        mapping = _require_mapping(value, field="verdict finding")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "finding_sha256",
                    "invariant_class",
                    "invariant_id",
                    "kind",
                    "reason_code",
                    "run_ids",
                    "scenario_id",
                    "severity",
                    "source_id",
                    "source_sha256",
                    "status",
                }
            ),
            field="verdict finding",
        )
        finding = cls(
            kind=_parse_enum(
                VerdictFindingKind,
                mapping["kind"],
                field="verdict finding.kind",
            ),
            source_id=_require_string(mapping["source_id"], field="verdict finding.source_id"),
            source_sha256=_require_string(
                mapping["source_sha256"], field="verdict finding.source_sha256"
            ),
            scenario_id=_require_string(
                mapping["scenario_id"], field="verdict finding.scenario_id"
            ),
            run_ids=_parse_string_tuple(mapping["run_ids"], field="verdict finding.run_ids"),
            invariant_id=_require_string(
                mapping["invariant_id"], field="verdict finding.invariant_id"
            ),
            invariant_class=_parse_enum(
                InvariantClass,
                mapping["invariant_class"],
                field="verdict finding.invariant_class",
            ),
            severity=_parse_enum(
                AssertionSeverity,
                mapping["severity"],
                field="verdict finding.severity",
            ),
            status=_parse_enum(
                VerdictFindingStatus,
                mapping["status"],
                field="verdict finding.status",
            ),
            reason_code=_require_string(
                mapping["reason_code"], field="verdict finding.reason_code"
            ),
        )
        _validate_declared_sha256(
            finding.finding_sha256,
            mapping,
            key="finding_sha256",
            field="verdict finding",
        )
        return finding


@dataclass(frozen=True, slots=True)
class VerdictObservation:
    """Explicit marker that a passing finding is valid but noteworthy."""

    observation_id: str
    category: ObservationCategory
    observation_code: str
    finding_sha256: str

    def __post_init__(self) -> None:
        _validate_control_id(self.observation_id, field="observation_id")
        if not isinstance(self.category, ObservationCategory):
            raise VerdictError("category must be an ObservationCategory value")
        _validate_control_id(self.observation_code, field="observation_code")
        _validate_sha256(self.finding_sha256, field="finding_sha256")

    @property
    def observation_sha256(self) -> str:
        """Return the digest binding this observation to its finding."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "category": self.category.value,
            "finding_sha256": self.finding_sha256,
            "observation_code": self.observation_code,
            "observation_id": self.observation_id,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable observation representation."""

        return {**self._content_mapping(), "observation_sha256": self.observation_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> VerdictObservation:
        """Parse and verify one serialized verdict observation."""

        mapping = _require_mapping(value, field="verdict observation")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "category",
                    "finding_sha256",
                    "observation_code",
                    "observation_id",
                    "observation_sha256",
                }
            ),
            field="verdict observation",
        )
        observation = cls(
            observation_id=_require_string(
                mapping["observation_id"],
                field="verdict observation.observation_id",
            ),
            category=_parse_enum(
                ObservationCategory,
                mapping["category"],
                field="verdict observation.category",
            ),
            observation_code=_require_string(
                mapping["observation_code"],
                field="verdict observation.observation_code",
            ),
            finding_sha256=_require_string(
                mapping["finding_sha256"],
                field="verdict observation.finding_sha256",
            ),
        )
        _validate_declared_sha256(
            observation.observation_sha256,
            mapping,
            key="observation_sha256",
            field="verdict observation",
        )
        return observation


@dataclass(frozen=True, slots=True)
class ScenarioVerdict:
    """Immutable final outcome for one primary scenario run and its comparisons."""

    verdict_id: str
    verdict_definition_id: str
    verdict_definition_sha256: str
    scenario_id: str
    primary_run_id: str
    assertion_series_sha256: str
    evaluated_at_tick: int
    execution_validity: ExecutionValidity
    execution_validity_reason: ExecutionValidityReason
    minimum_finding_count: int
    outcome: VerdictOutcome
    reason: VerdictReason
    findings: tuple[VerdictFinding, ...]
    observations: tuple[VerdictObservation, ...]
    missing_assertion_ids: tuple[str, ...]
    missing_comparison_ids: tuple[str, ...]

    def __post_init__(self) -> None:
        _validate_control_id(self.verdict_id, field="verdict_id")
        _validate_control_id(self.verdict_definition_id, field="verdict_definition_id")
        _validate_sha256(
            self.verdict_definition_sha256,
            field="verdict_definition_sha256",
        )
        _validate_scenario_id(self.scenario_id)
        _validate_control_id(self.primary_run_id, field="primary_run_id")
        _validate_sha256(self.assertion_series_sha256, field="assertion_series_sha256")
        _validate_tick(self.evaluated_at_tick, field="evaluated_at_tick")
        if not isinstance(self.execution_validity, ExecutionValidity):
            raise VerdictError("execution_validity must be an ExecutionValidity value")
        if not isinstance(self.execution_validity_reason, ExecutionValidityReason):
            raise VerdictError("execution_validity_reason must be an ExecutionValidityReason value")
        _validate_execution_validity_pair(
            self.execution_validity,
            self.execution_validity_reason,
        )
        _validate_positive_integer(self.minimum_finding_count, field="minimum_finding_count")
        if self.minimum_finding_count > MAX_VERDICT_FINDINGS:
            raise VerdictError(f"minimum_finding_count must not exceed {MAX_VERDICT_FINDINGS}")
        if not isinstance(self.outcome, VerdictOutcome):
            raise VerdictError("outcome must be a VerdictOutcome value")
        if not isinstance(self.reason, VerdictReason):
            raise VerdictError("reason must be a VerdictReason value")
        _validate_findings(self.findings, self.scenario_id, self.primary_run_id)
        _validate_observations(self.observations, self.findings)
        _validate_required_ids(self.missing_assertion_ids, field="missing_assertion_ids")
        _validate_required_ids(self.missing_comparison_ids, field="missing_comparison_ids")

        expected_outcome, expected_reason = _derive_verdict_decision(
            self.execution_validity,
            self.findings,
            self.observations,
            self.missing_assertion_ids,
            self.missing_comparison_ids,
            self.minimum_finding_count,
        )
        if (self.outcome, self.reason) != (expected_outcome, expected_reason):
            raise VerdictError("outcome and reason do not match verdict evidence")

    @property
    def finding_count(self) -> int:
        """Return the total number of normalized findings."""

        return len(self.findings)

    @property
    def assertion_finding_count(self) -> int:
        """Return the number of assertion-result findings."""

        return sum(finding.kind is VerdictFindingKind.ASSERTION_RESULT for finding in self.findings)

    @property
    def comparison_finding_count(self) -> int:
        """Return the number of comparison-report findings."""

        return sum(
            finding.kind is VerdictFindingKind.COMPARISON_REPORT for finding in self.findings
        )

    @property
    def passed_finding_count(self) -> int:
        """Return the number of passing findings."""

        return _count_finding_status(self.findings, VerdictFindingStatus.PASS)

    @property
    def failed_finding_count(self) -> int:
        """Return the number of failed findings across all invariant classes."""

        return _count_finding_status(self.findings, VerdictFindingStatus.FAIL)

    @property
    def review_finding_count(self) -> int:
        """Return the number of findings already requiring review."""

        return _count_finding_status(self.findings, VerdictFindingStatus.REVIEW)

    @property
    def blocked_finding_count(self) -> int:
        """Return the number of blocked findings."""

        return _count_finding_status(self.findings, VerdictFindingStatus.BLOCKED)

    @property
    def hard_failure_count(self) -> int:
        """Return the number of failed hard-invariant findings."""

        return sum(
            finding.status is VerdictFindingStatus.FAIL
            and finding.invariant_class is InvariantClass.HARD
            for finding in self.findings
        )

    @property
    def observation_count(self) -> int:
        """Return the number of explicit valid-behavior observations."""

        return len(self.observations)

    @property
    def missing_required_count(self) -> int:
        """Return the total number of absent required result identities."""

        return len(self.missing_assertion_ids) + len(self.missing_comparison_ids)

    @property
    def verdict_sha256(self) -> str:
        """Return the digest binding policy, evidence, validity, and outcome."""

        return calculate_scenario_verdict_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "assertion_finding_count": self.assertion_finding_count,
            "assertion_series_sha256": self.assertion_series_sha256,
            "blocked_finding_count": self.blocked_finding_count,
            "comparison_finding_count": self.comparison_finding_count,
            "evaluated_at_tick": self.evaluated_at_tick,
            "execution_validity": self.execution_validity.value,
            "execution_validity_reason": self.execution_validity_reason.value,
            "failed_finding_count": self.failed_finding_count,
            "finding_count": self.finding_count,
            "findings": [finding.to_mapping() for finding in self.findings],
            "hard_failure_count": self.hard_failure_count,
            "minimum_finding_count": self.minimum_finding_count,
            "missing_assertion_ids": list(self.missing_assertion_ids),
            "missing_comparison_ids": list(self.missing_comparison_ids),
            "missing_required_count": self.missing_required_count,
            "observation_count": self.observation_count,
            "observations": [observation.to_mapping() for observation in self.observations],
            "outcome": self.outcome.value,
            "passed_finding_count": self.passed_finding_count,
            "primary_run_id": self.primary_run_id,
            "reason": self.reason.value,
            "review_finding_count": self.review_finding_count,
            "scenario_id": self.scenario_id,
            "verdict_definition_id": self.verdict_definition_id,
            "verdict_definition_sha256": self.verdict_definition_sha256,
            "verdict_id": self.verdict_id,
            "verdict_schema_version": SUPPORTED_VERDICT_SCHEMA_VERSION,
            "verdict_type": "SCENARIO_VERDICT",
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete validator-owned verdict representation."""

        return {**self._content_mapping(), "verdict_sha256": self.verdict_sha256}

    def to_evidence_mapping(self) -> dict[str, object]:
        """Return a compact, value-redacted verdict evidence summary."""

        return {
            "assertion_finding_count": self.assertion_finding_count,
            "assertion_series_sha256": self.assertion_series_sha256,
            "blocked_finding_count": self.blocked_finding_count,
            "comparison_finding_count": self.comparison_finding_count,
            "evaluated_at_tick": self.evaluated_at_tick,
            "execution_validity": self.execution_validity.value,
            "execution_validity_reason": self.execution_validity_reason.value,
            "failed_finding_count": self.failed_finding_count,
            "finding_count": self.finding_count,
            "finding_sha256": [finding.finding_sha256 for finding in self.findings],
            "hard_failure_count": self.hard_failure_count,
            "minimum_finding_count": self.minimum_finding_count,
            "missing_assertion_ids": list(self.missing_assertion_ids),
            "missing_comparison_ids": list(self.missing_comparison_ids),
            "missing_required_count": self.missing_required_count,
            "observation_count": self.observation_count,
            "observation_sha256": [
                observation.observation_sha256 for observation in self.observations
            ],
            "outcome": self.outcome.value,
            "passed_finding_count": self.passed_finding_count,
            "primary_run_id": self.primary_run_id,
            "reason": self.reason.value,
            "review_finding_count": self.review_finding_count,
            "scenario_id": self.scenario_id,
            "verdict_definition_id": self.verdict_definition_id,
            "verdict_definition_sha256": self.verdict_definition_sha256,
            "verdict_id": self.verdict_id,
            "verdict_sha256": self.verdict_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> ScenarioVerdict:
        """Parse and verify one serialized scenario verdict."""

        mapping = _require_mapping(value, field="scenario verdict")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "assertion_finding_count",
                    "assertion_series_sha256",
                    "blocked_finding_count",
                    "comparison_finding_count",
                    "evaluated_at_tick",
                    "execution_validity",
                    "execution_validity_reason",
                    "failed_finding_count",
                    "finding_count",
                    "findings",
                    "hard_failure_count",
                    "minimum_finding_count",
                    "missing_assertion_ids",
                    "missing_comparison_ids",
                    "missing_required_count",
                    "observation_count",
                    "observations",
                    "outcome",
                    "passed_finding_count",
                    "primary_run_id",
                    "reason",
                    "review_finding_count",
                    "scenario_id",
                    "verdict_definition_id",
                    "verdict_definition_sha256",
                    "verdict_id",
                    "verdict_schema_version",
                    "verdict_sha256",
                    "verdict_type",
                }
            ),
            field="scenario verdict",
        )
        _validate_schema_version(mapping["verdict_schema_version"])
        if mapping["verdict_type"] != "SCENARIO_VERDICT":
            raise VerdictError("unsupported verdict_type")
        verdict = cls(
            verdict_id=_require_string(mapping["verdict_id"], field="scenario verdict.verdict_id"),
            verdict_definition_id=_require_string(
                mapping["verdict_definition_id"],
                field="scenario verdict.verdict_definition_id",
            ),
            verdict_definition_sha256=_require_string(
                mapping["verdict_definition_sha256"],
                field="scenario verdict.verdict_definition_sha256",
            ),
            scenario_id=_require_string(
                mapping["scenario_id"], field="scenario verdict.scenario_id"
            ),
            primary_run_id=_require_string(
                mapping["primary_run_id"], field="scenario verdict.primary_run_id"
            ),
            assertion_series_sha256=_require_string(
                mapping["assertion_series_sha256"],
                field="scenario verdict.assertion_series_sha256",
            ),
            evaluated_at_tick=_require_integer(
                mapping["evaluated_at_tick"],
                field="scenario verdict.evaluated_at_tick",
            ),
            execution_validity=_parse_enum(
                ExecutionValidity,
                mapping["execution_validity"],
                field="scenario verdict.execution_validity",
            ),
            execution_validity_reason=_parse_enum(
                ExecutionValidityReason,
                mapping["execution_validity_reason"],
                field="scenario verdict.execution_validity_reason",
            ),
            minimum_finding_count=_require_integer(
                mapping["minimum_finding_count"],
                field="scenario verdict.minimum_finding_count",
            ),
            outcome=_parse_enum(
                VerdictOutcome,
                mapping["outcome"],
                field="scenario verdict.outcome",
            ),
            reason=_parse_enum(
                VerdictReason,
                mapping["reason"],
                field="scenario verdict.reason",
            ),
            findings=_parse_findings(mapping["findings"]),
            observations=_parse_observations(mapping["observations"]),
            missing_assertion_ids=_parse_string_tuple(
                mapping["missing_assertion_ids"],
                field="scenario verdict.missing_assertion_ids",
            ),
            missing_comparison_ids=_parse_string_tuple(
                mapping["missing_comparison_ids"],
                field="scenario verdict.missing_comparison_ids",
            ),
        )
        _validate_verdict_derived_fields(verdict, mapping)
        _validate_declared_sha256(
            verdict.verdict_sha256,
            mapping,
            key="verdict_sha256",
            field="scenario verdict",
        )
        return verdict


def create_verdict_definition(
    *,
    verdict_definition_id: str,
    scenario_id: str,
    primary_run_id: str,
    required_assertion_ids: tuple[str, ...] = (),
    required_comparison_ids: tuple[str, ...] = (),
    minimum_finding_count: int = 1,
) -> VerdictDefinition:
    """Create a verdict definition with canonical required-ID ordering."""

    if not isinstance(required_assertion_ids, tuple):
        raise VerdictError("required_assertion_ids must be a tuple")
    if not isinstance(required_comparison_ids, tuple):
        raise VerdictError("required_comparison_ids must be a tuple")
    return VerdictDefinition(
        verdict_definition_id=verdict_definition_id,
        scenario_id=scenario_id,
        primary_run_id=primary_run_id,
        required_assertion_ids=tuple(sorted(required_assertion_ids)),
        required_comparison_ids=tuple(sorted(required_comparison_ids)),
        minimum_finding_count=minimum_finding_count,
    )


def create_assertion_finding(result: AssertionResult) -> VerdictFinding:
    """Normalize one assertion result without copying its raw actual value."""

    if not isinstance(result, AssertionResult):
        raise VerdictError("result must be an AssertionResult")
    return VerdictFinding(
        kind=VerdictFindingKind.ASSERTION_RESULT,
        source_id=result.result_id,
        source_sha256=result.result_sha256,
        scenario_id=result.scenario_id,
        run_ids=(result.run_id,),
        invariant_id=result.invariant_id,
        invariant_class=result.invariant_class,
        severity=result.severity,
        status=VerdictFindingStatus(result.status.value),
        reason_code=result.reason.value,
    )


def create_comparison_finding(report: ComparisonReport) -> VerdictFinding:
    """Normalize one cross-run comparison report into a verdict finding."""

    if not isinstance(report, ComparisonReport):
        raise VerdictError("report must be a ComparisonReport")
    return VerdictFinding(
        kind=VerdictFindingKind.COMPARISON_REPORT,
        source_id=report.report_id,
        source_sha256=report.report_sha256,
        scenario_id=report.scenario_id,
        run_ids=(report.baseline_run_id, report.candidate_run_id),
        invariant_id=report.invariant_id,
        invariant_class=report.invariant_class,
        severity=report.severity,
        status=VerdictFindingStatus(report.status.value),
        reason_code=report.reason.value,
    )


def create_verdict_observation(
    *,
    observation_id: str,
    category: ObservationCategory,
    observation_code: str,
    finding: VerdictFinding,
) -> VerdictObservation:
    """Bind a valid-behavior observation to one normalized finding."""

    if not isinstance(finding, VerdictFinding):
        raise VerdictError("finding must be a VerdictFinding")
    if finding.status is not VerdictFindingStatus.PASS:
        raise VerdictError("observations may reference only passing findings")
    return VerdictObservation(
        observation_id=observation_id,
        category=category,
        observation_code=observation_code,
        finding_sha256=finding.finding_sha256,
    )


def derive_scenario_verdict(
    definition: VerdictDefinition,
    assertion_series: AssertionSeries,
    comparisons: tuple[ComparisonReport, ...],
    *,
    verdict_id: str,
    evaluated_at_tick: int,
    execution_validity: ExecutionValidity,
    execution_validity_reason: ExecutionValidityReason,
    observations: tuple[VerdictObservation, ...] = (),
) -> ScenarioVerdict:
    """Derive one fail-closed scenario outcome from exact validator results."""

    _validate_verdict_inputs(definition, assertion_series, comparisons, observations)
    _validate_control_id(verdict_id, field="verdict_id")
    _validate_tick(evaluated_at_tick, field="evaluated_at_tick")
    if not isinstance(execution_validity, ExecutionValidity):
        raise VerdictError("execution_validity must be an ExecutionValidity value")
    if not isinstance(execution_validity_reason, ExecutionValidityReason):
        raise VerdictError("execution_validity_reason must be an ExecutionValidityReason value")
    _validate_execution_validity_pair(execution_validity, execution_validity_reason)

    findings = _create_findings(assertion_series, comparisons)
    finding_hashes = frozenset(finding.finding_sha256 for finding in findings)
    for observation in observations:
        if observation.finding_sha256 not in finding_hashes:
            raise VerdictError("observation must reference a supplied verdict finding")
    ordered_observations = tuple(
        sorted(observations, key=lambda observation: observation.observation_sha256)
    )

    available_assertion_ids = frozenset(result.assertion_id for result in assertion_series.results)
    available_comparison_ids = frozenset(report.comparison_id for report in comparisons)
    missing_assertion_ids = tuple(
        sorted(set(definition.required_assertion_ids) - available_assertion_ids)
    )
    missing_comparison_ids = tuple(
        sorted(set(definition.required_comparison_ids) - available_comparison_ids)
    )
    outcome, reason = _derive_verdict_decision(
        execution_validity,
        findings,
        ordered_observations,
        missing_assertion_ids,
        missing_comparison_ids,
        definition.minimum_finding_count,
    )
    return ScenarioVerdict(
        verdict_id=verdict_id,
        verdict_definition_id=definition.verdict_definition_id,
        verdict_definition_sha256=definition.definition_sha256,
        scenario_id=definition.scenario_id,
        primary_run_id=definition.primary_run_id,
        assertion_series_sha256=assertion_series.series_sha256,
        evaluated_at_tick=evaluated_at_tick,
        execution_validity=execution_validity,
        execution_validity_reason=execution_validity_reason,
        minimum_finding_count=definition.minimum_finding_count,
        outcome=outcome,
        reason=reason,
        findings=findings,
        observations=ordered_observations,
        missing_assertion_ids=missing_assertion_ids,
        missing_comparison_ids=missing_comparison_ids,
    )


def validate_scenario_verdict(
    verdict: ScenarioVerdict,
    definition: VerdictDefinition,
    assertion_series: AssertionSeries,
    comparisons: tuple[ComparisonReport, ...],
) -> None:
    """Recompute and verify a verdict against its exact definition and inputs."""

    if not isinstance(verdict, ScenarioVerdict):
        raise VerdictError("verdict must be a ScenarioVerdict")
    expected = derive_scenario_verdict(
        definition,
        assertion_series,
        comparisons,
        verdict_id=verdict.verdict_id,
        evaluated_at_tick=verdict.evaluated_at_tick,
        execution_validity=verdict.execution_validity,
        execution_validity_reason=verdict.execution_validity_reason,
        observations=verdict.observations,
    )
    if verdict != expected:
        raise VerdictError("scenario verdict does not match its definition and inputs")


def create_verdict_evidence_payload(verdict: ScenarioVerdict) -> EvidencePayload:
    """Create a compact validator evidence payload for one scenario verdict."""

    if not isinstance(verdict, ScenarioVerdict):
        raise VerdictError("verdict must be a ScenarioVerdict")
    return create_evidence_payload(verdict.to_evidence_mapping())


def calculate_verdict_definition_sha256(definition: VerdictDefinition) -> str:
    """Calculate the canonical digest for one verdict definition."""

    if not isinstance(definition, VerdictDefinition):
        raise VerdictError("definition must be a VerdictDefinition")
    return hashlib.sha256(_canonical_json_bytes(definition._content_mapping())).hexdigest()


def calculate_scenario_verdict_sha256(verdict: ScenarioVerdict) -> str:
    """Calculate the canonical digest for one scenario verdict."""

    if not isinstance(verdict, ScenarioVerdict):
        raise VerdictError("verdict must be a ScenarioVerdict")
    return hashlib.sha256(_canonical_json_bytes(verdict._content_mapping())).hexdigest()


def _validate_verdict_inputs(
    definition: VerdictDefinition,
    assertion_series: AssertionSeries,
    comparisons: tuple[ComparisonReport, ...],
    observations: tuple[VerdictObservation, ...],
) -> None:
    if not isinstance(definition, VerdictDefinition):
        raise VerdictError("definition must be a VerdictDefinition")
    if not isinstance(assertion_series, AssertionSeries):
        raise VerdictError("assertion_series must be an AssertionSeries")
    if not isinstance(comparisons, tuple) or not all(
        isinstance(report, ComparisonReport) for report in comparisons
    ):
        raise VerdictError("comparisons must be a tuple of ComparisonReport values")
    if len(comparisons) > MAX_VERDICT_FINDINGS:
        raise VerdictError(f"comparisons must not exceed {MAX_VERDICT_FINDINGS} entries")
    if not isinstance(observations, tuple) or not all(
        isinstance(observation, VerdictObservation) for observation in observations
    ):
        raise VerdictError("observations must be a tuple of VerdictObservation values")
    if len(observations) > MAX_VERDICT_OBSERVATIONS:
        raise VerdictError(f"observations must not exceed {MAX_VERDICT_OBSERVATIONS} entries")
    if assertion_series.scenario_id != definition.scenario_id:
        raise VerdictError("assertion series scenario does not match verdict definition")
    if assertion_series.run_id != definition.primary_run_id:
        raise VerdictError("assertion series run does not match verdict definition")

    comparison_ids: list[str] = []
    report_ids: list[str] = []
    for report in comparisons:
        if report.scenario_id != definition.scenario_id:
            raise VerdictError("comparison scenario does not match verdict definition")
        if definition.primary_run_id not in (report.baseline_run_id, report.candidate_run_id):
            raise VerdictError("comparison does not include the primary verdict run")
        comparison_ids.append(report.comparison_id)
        report_ids.append(report.report_id)
    if len(comparison_ids) != len(set(comparison_ids)):
        raise VerdictError("comparison_id values must be unique within a verdict")
    if len(report_ids) != len(set(report_ids)):
        raise VerdictError("comparison report IDs must be unique within a verdict")


def _create_findings(
    assertion_series: AssertionSeries,
    comparisons: tuple[ComparisonReport, ...],
) -> tuple[VerdictFinding, ...]:
    finding_count = len(assertion_series.results) + len(comparisons)
    if finding_count > MAX_VERDICT_FINDINGS:
        raise VerdictError(f"verdict must not exceed {MAX_VERDICT_FINDINGS} findings")
    findings = [create_assertion_finding(result) for result in assertion_series.results]
    findings.extend(create_comparison_finding(report) for report in comparisons)
    findings.sort(key=lambda finding: finding.finding_sha256)
    return tuple(findings)


def _derive_verdict_decision(
    execution_validity: ExecutionValidity,
    findings: tuple[VerdictFinding, ...],
    observations: tuple[VerdictObservation, ...],
    missing_assertion_ids: tuple[str, ...],
    missing_comparison_ids: tuple[str, ...],
    minimum_finding_count: int,
) -> tuple[VerdictOutcome, VerdictReason]:
    if execution_validity is ExecutionValidity.INVALID_RUN:
        return VerdictOutcome.BLOCKED, VerdictReason.EXECUTION_INVALID
    if missing_assertion_ids or missing_comparison_ids:
        return VerdictOutcome.BLOCKED, VerdictReason.MISSING_REQUIRED_RESULT
    if len(findings) < minimum_finding_count:
        return VerdictOutcome.BLOCKED, VerdictReason.INSUFFICIENT_EVIDENCE
    if any(finding.status is VerdictFindingStatus.BLOCKED for finding in findings):
        return VerdictOutcome.BLOCKED, VerdictReason.REQUIRED_RESULT_BLOCKED
    if any(
        finding.status is VerdictFindingStatus.FAIL
        and finding.invariant_class is InvariantClass.HARD
        for finding in findings
    ):
        return VerdictOutcome.FAIL, VerdictReason.HARD_INVARIANT_FAILED
    if any(finding.status is VerdictFindingStatus.FAIL for finding in findings):
        return VerdictOutcome.REVIEW, VerdictReason.NON_HARD_INVARIANT_FAILED
    if any(finding.status is VerdictFindingStatus.REVIEW for finding in findings):
        return VerdictOutcome.REVIEW, VerdictReason.SOURCE_REVIEW_REQUIRED
    if observations:
        return VerdictOutcome.PASS_WITH_OBSERVATION, VerdictReason.VALID_WITH_OBSERVATIONS
    return VerdictOutcome.PASS, VerdictReason.ALL_REQUIRED_RESULTS_PASSED


def _validate_execution_validity_pair(
    validity: ExecutionValidity,
    reason: ExecutionValidityReason,
) -> None:
    if validity is ExecutionValidity.VALID_RUN and reason is not ExecutionValidityReason.VERIFIED:
        raise VerdictError("VALID_RUN requires execution validity reason VERIFIED")
    if validity is ExecutionValidity.INVALID_RUN and reason is ExecutionValidityReason.VERIFIED:
        raise VerdictError("INVALID_RUN requires a non-VERIFIED execution validity reason")


def _validate_findings(
    findings: tuple[VerdictFinding, ...],
    scenario_id: str,
    primary_run_id: str,
) -> None:
    if not isinstance(findings, tuple) or not all(
        isinstance(finding, VerdictFinding) for finding in findings
    ):
        raise VerdictError("findings must be a tuple of VerdictFinding values")
    if len(findings) > MAX_VERDICT_FINDINGS:
        raise VerdictError(f"findings must not exceed {MAX_VERDICT_FINDINGS} entries")
    source_keys = tuple((finding.kind, finding.source_id) for finding in findings)
    if len(source_keys) != len(set(source_keys)):
        raise VerdictError("findings must use unique source kind and ID pairs")
    finding_hashes = tuple(finding.finding_sha256 for finding in findings)
    if len(finding_hashes) != len(set(finding_hashes)):
        raise VerdictError("findings must use unique finding hashes")
    if finding_hashes != tuple(sorted(finding_hashes)):
        raise VerdictError("findings must be ordered by finding_sha256")
    for finding in findings:
        if finding.scenario_id != scenario_id:
            raise VerdictError("finding scenario does not match scenario verdict")
        if primary_run_id not in finding.run_ids:
            raise VerdictError("finding does not include the primary verdict run")


def _validate_observations(
    observations: tuple[VerdictObservation, ...],
    findings: tuple[VerdictFinding, ...],
) -> None:
    if not isinstance(observations, tuple) or not all(
        isinstance(observation, VerdictObservation) for observation in observations
    ):
        raise VerdictError("observations must be a tuple of VerdictObservation values")
    if len(observations) > MAX_VERDICT_OBSERVATIONS:
        raise VerdictError(f"observations must not exceed {MAX_VERDICT_OBSERVATIONS} entries")
    observation_ids = tuple(observation.observation_id for observation in observations)
    if len(observation_ids) != len(set(observation_ids)):
        raise VerdictError("observations must use unique observation IDs")
    observation_hashes = tuple(observation.observation_sha256 for observation in observations)
    if len(observation_hashes) != len(set(observation_hashes)):
        raise VerdictError("observations must use unique observation hashes")
    if observation_hashes != tuple(sorted(observation_hashes)):
        raise VerdictError("observations must be ordered by observation_sha256")
    findings_by_sha256 = {finding.finding_sha256: finding for finding in findings}
    for observation in observations:
        finding = findings_by_sha256.get(observation.finding_sha256)
        if finding is None:
            raise VerdictError("observation must reference a verdict finding")
        if finding.status is not VerdictFindingStatus.PASS:
            raise VerdictError("observations may reference only passing findings")


def _validate_required_ids(value: tuple[str, ...], *, field: str) -> None:
    if not isinstance(value, tuple) or not all(isinstance(item, str) for item in value):
        raise VerdictError(f"{field} must be a tuple of strings")
    if len(value) > MAX_VERDICT_REQUIRED_IDS:
        raise VerdictError(f"{field} must not exceed {MAX_VERDICT_REQUIRED_IDS} entries")
    for item in value:
        _validate_control_id(item, field=f"{field} entry")
    if len(value) != len(set(value)):
        raise VerdictError(f"{field} must not contain duplicates")
    if value != tuple(sorted(value)):
        raise VerdictError(f"{field} must use lexical order")


def _count_finding_status(
    findings: tuple[VerdictFinding, ...],
    status: VerdictFindingStatus,
) -> int:
    return sum(finding.status is status for finding in findings)


def _parse_findings(value: object) -> tuple[VerdictFinding, ...]:
    if not isinstance(value, list):
        raise VerdictError("scenario verdict.findings must be an array")
    return tuple(
        VerdictFinding.from_mapping(
            _require_mapping(item, field=f"scenario verdict.findings[{index}]")
        )
        for index, item in enumerate(value)
    )


def _parse_observations(value: object) -> tuple[VerdictObservation, ...]:
    if not isinstance(value, list):
        raise VerdictError("scenario verdict.observations must be an array")
    return tuple(
        VerdictObservation.from_mapping(
            _require_mapping(item, field=f"scenario verdict.observations[{index}]")
        )
        for index, item in enumerate(value)
    )


def _validate_verdict_derived_fields(
    verdict: ScenarioVerdict,
    mapping: Mapping[str, object],
) -> None:
    expected_counts = {
        "assertion_finding_count": verdict.assertion_finding_count,
        "blocked_finding_count": verdict.blocked_finding_count,
        "comparison_finding_count": verdict.comparison_finding_count,
        "failed_finding_count": verdict.failed_finding_count,
        "finding_count": verdict.finding_count,
        "hard_failure_count": verdict.hard_failure_count,
        "missing_required_count": verdict.missing_required_count,
        "observation_count": verdict.observation_count,
        "passed_finding_count": verdict.passed_finding_count,
        "review_finding_count": verdict.review_finding_count,
    }
    for field, expected in expected_counts.items():
        declared = _require_integer(mapping[field], field=f"scenario verdict.{field}")
        if declared != expected:
            raise VerdictError(f"declared {field} does not match scenario verdict")


def _parse_string_tuple(value: object, *, field: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise VerdictError(f"{field} must be an array")
    return tuple(
        _require_string(item, field=f"{field}[{index}]") for index, item in enumerate(value)
    )


def _validate_schema_version(value: object) -> None:
    version = _require_string(value, field="verdict_schema_version")
    if version != SUPPORTED_VERDICT_SCHEMA_VERSION:
        raise VerdictError(f"unsupported verdict_schema_version: {version}")


def _validate_declared_sha256(
    calculated_sha256: str,
    mapping: Mapping[str, object],
    *,
    key: str,
    field: str,
) -> None:
    declared_sha256 = _require_string(mapping[key], field=f"{field}.{key}")
    if declared_sha256 != calculated_sha256:
        raise VerdictError(f"declared {key} does not match {field}")


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
        raise VerdictError("value must be canonical finite JSON") from exc


def _require_mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise VerdictError(f"{field} must be an object")
    for key in value:
        if not isinstance(key, str):
            raise VerdictError(f"{field} keys must be strings")
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
        raise VerdictError(f"{field} is missing required fields: {', '.join(missing)}")
    if unexpected:
        raise VerdictError(f"{field} contains unexpected fields: {', '.join(unexpected)}")


def _require_string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        raise VerdictError(f"{field} must be a string")
    return value


def _require_integer(value: object, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerdictError(f"{field} must be an integer")
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
        raise VerdictError(f"{field} contains an unsupported value: {raw}") from exc


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise VerdictError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise VerdictError(f"{field} must be a stable uppercase control identifier")


def _validate_scenario_id(value: str) -> None:
    if not isinstance(value, str):
        raise VerdictError("scenario_id must be a string")
    if _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        raise VerdictError("scenario_id must match AURORA-SCN-<FAMILY>-<NNN>")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise VerdictError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise VerdictError(f"{field} must be a lowercase SHA-256 digest")


def _validate_positive_integer(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerdictError(f"{field} must be an integer")
    if value < 1:
        raise VerdictError(f"{field} must be positive")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise VerdictError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise VerdictError(f"{field} must be between 0 and {MAX_TICK}")


__all__ = [
    "MAX_TICK",
    "MAX_VERDICT_FINDINGS",
    "MAX_VERDICT_OBSERVATIONS",
    "MAX_VERDICT_REQUIRED_IDS",
    "SUPPORTED_VERDICT_SCHEMA_VERSION",
    "ExecutionValidity",
    "ExecutionValidityReason",
    "ObservationCategory",
    "ScenarioVerdict",
    "VerdictDefinition",
    "VerdictError",
    "VerdictFinding",
    "VerdictFindingKind",
    "VerdictFindingStatus",
    "VerdictObservation",
    "VerdictOutcome",
    "VerdictReason",
    "calculate_scenario_verdict_sha256",
    "calculate_verdict_definition_sha256",
    "create_assertion_finding",
    "create_comparison_finding",
    "create_verdict_definition",
    "create_verdict_evidence_payload",
    "create_verdict_observation",
    "derive_scenario_verdict",
    "validate_scenario_verdict",
]
