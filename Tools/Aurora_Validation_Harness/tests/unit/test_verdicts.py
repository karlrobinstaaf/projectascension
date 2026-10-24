"""Unit tests for deterministic fail-closed Aurora scenario verdicts."""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import FrozenInstanceError, replace
from types import MappingProxyType

import pytest

from aurora_validation_harness import verdicts as verdicts_module
from aurora_validation_harness.assertions import (
    AssertionReason,
    AssertionResult,
    AssertionSeries,
    AssertionSeverity,
    AssertionStatus,
    AssertionTargetKind,
    InvariantClass,
    create_assertion_value,
)
from aurora_validation_harness.comparison import (
    ComparisonKind,
    ComparisonPolicy,
    ComparisonReason,
    ComparisonReport,
    ComparisonStatus,
)
from aurora_validation_harness.evidence import EvidenceDomain
from aurora_validation_harness.verdicts import (
    MAX_TICK,
    MAX_VERDICT_FINDINGS,
    MAX_VERDICT_OBSERVATIONS,
    MAX_VERDICT_REQUIRED_IDS,
    SUPPORTED_VERDICT_SCHEMA_VERSION,
    ExecutionValidity,
    ExecutionValidityReason,
    ObservationCategory,
    ScenarioVerdict,
    VerdictDefinition,
    VerdictError,
    VerdictFinding,
    VerdictFindingKind,
    VerdictFindingStatus,
    VerdictObservation,
    VerdictOutcome,
    VerdictReason,
    calculate_scenario_verdict_sha256,
    calculate_verdict_definition_sha256,
    create_assertion_finding,
    create_comparison_finding,
    create_verdict_definition,
    create_verdict_evidence_payload,
    create_verdict_observation,
    derive_scenario_verdict,
    validate_scenario_verdict,
)

pytestmark = [
    pytest.mark.foundation,
    pytest.mark.isolation,
    pytest.mark.metamorphic,
]

_PRIMARY_RUN_ID = "AURORA-RUN-FOUND-001-BASE"
_CANDIDATE_RUN_ID = "AURORA-RUN-FOUND-001-CAND"
_OTHER_RUN_ID = "AURORA-RUN-FOUND-001-OTHER"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"


def _assertion_result(
    *,
    run_id: str = _PRIMARY_RUN_ID,
    result_id: str = "RESULT-FOUND-001-A1",
    assertion_id: str = "ASSERTION-FOUND-001-A1",
    invariant_id: str = "AURORA-INFO-001",
    invariant_class: InvariantClass = InvariantClass.HARD,
    severity: AssertionSeverity = AssertionSeverity.S4,
    status: AssertionStatus = AssertionStatus.PASS,
    reason: AssertionReason | None = None,
    actual: object = "SECRET-CANARY",
) -> AssertionResult:
    if reason is None:
        reason = (
            AssertionReason.VALUES_EQUAL
            if status is AssertionStatus.PASS
            else AssertionReason.VALUES_DIFFER
        )
    run_label = "BASE" if run_id == _PRIMARY_RUN_ID else "CAND"
    return AssertionResult(
        result_id=result_id,
        run_id=run_id,
        scenario_id=_SCENARIO_ID,
        sequence=0,
        evaluated_at_tick=10,
        assertion_id=assertion_id,
        assertion_sha256=("a" if assertion_id.endswith("A1") else "b") * 64,
        invariant_id=invariant_id,
        invariant_class=invariant_class,
        severity=severity,
        target_kind=AssertionTargetKind.SNAPSHOT,
        target_id=f"SNAPSHOT-FOUND-001-{run_label}",
        target_sha256=("c" if run_id == _PRIMARY_RUN_ID else "d") * 64,
        target_domain=EvidenceDomain.AURORA_STATE,
        status=status,
        reason=reason,
        path="/belief",
        actual=create_assertion_value(actual),
        previous_result_sha256=None,
    )


def _series(*results: AssertionResult, run_id: str = _PRIMARY_RUN_ID) -> AssertionSeries:
    chained: list[AssertionResult] = []
    previous_sha256: str | None = None
    for sequence, result in enumerate(results):
        current = replace(
            result,
            run_id=run_id,
            sequence=sequence,
            previous_result_sha256=previous_sha256,
        )
        chained.append(current)
        previous_sha256 = current.result_sha256
    return AssertionSeries(run_id, _SCENARIO_ID, tuple(chained))


def _comparison_report(
    *,
    report_id: str = "REPORT-FOUND-001-C1",
    comparison_id: str = "COMPARISON-FOUND-001-C1",
    invariant_id: str = "AURORA-INFO-001",
    invariant_class: InvariantClass = InvariantClass.HARD,
    severity: AssertionSeverity = AssertionSeverity.S4,
    status: ComparisonStatus = ComparisonStatus.PASS,
    reason: ComparisonReason | None = None,
    scenario_id: str = _SCENARIO_ID,
    baseline_run_id: str = _PRIMARY_RUN_ID,
    candidate_run_id: str = _CANDIDATE_RUN_ID,
) -> ComparisonReport:
    if reason is None:
        reason = {
            ComparisonStatus.PASS: ComparisonReason.EXACT_MATCH,
            ComparisonStatus.FAIL: ComparisonReason.UNEXPECTED_DIVERGENCE,
            ComparisonStatus.REVIEW: ComparisonReason.UNEXPECTED_DIVERGENCE,
            ComparisonStatus.BLOCKED: ComparisonReason.INSUFFICIENT_PAIRED_RESULTS,
        }[status]
    return ComparisonReport(
        report_id=report_id,
        comparison_id=comparison_id,
        comparison_definition_sha256="e" * 64,
        scenario_id=scenario_id,
        baseline_run_id=baseline_run_id,
        baseline_series_sha256="f" * 64,
        candidate_run_id=candidate_run_id,
        candidate_series_sha256="1" * 64,
        evaluated_at_tick=20,
        invariant_id=invariant_id,
        invariant_class=invariant_class,
        severity=severity,
        kind=ComparisonKind.REPEATABILITY,
        policy=ComparisonPolicy.EXACT,
        status=status,
        reason=reason,
        pairs=(),
        violations=(),
    )


def _definition(
    *,
    required_assertion_ids: tuple[str, ...] = (),
    required_comparison_ids: tuple[str, ...] = (),
    minimum_finding_count: int = 1,
) -> VerdictDefinition:
    return create_verdict_definition(
        verdict_definition_id="VERDICT-DEFINITION-FOUND-001",
        scenario_id=_SCENARIO_ID,
        primary_run_id=_PRIMARY_RUN_ID,
        required_assertion_ids=required_assertion_ids,
        required_comparison_ids=required_comparison_ids,
        minimum_finding_count=minimum_finding_count,
    )


def _observation(
    finding: VerdictFinding,
    *,
    observation_id: str = "OBSERVATION-FOUND-001-O1",
    category: ObservationCategory = ObservationCategory.EMERGENCE,
    observation_code: str = "VALID-NOVEL-BEHAVIOR",
) -> VerdictObservation:
    return create_verdict_observation(
        observation_id=observation_id,
        category=category,
        observation_code=observation_code,
        finding=finding,
    )


def _derive(
    *,
    definition: VerdictDefinition | None = None,
    series: AssertionSeries | None = None,
    comparisons: tuple[ComparisonReport, ...] = (),
    execution_validity: ExecutionValidity = ExecutionValidity.VALID_RUN,
    execution_validity_reason: ExecutionValidityReason = ExecutionValidityReason.VERIFIED,
    observations: tuple[VerdictObservation, ...] = (),
) -> tuple[VerdictDefinition, AssertionSeries, ScenarioVerdict]:
    selected_definition = _definition() if definition is None else definition
    selected_series = _series(_assertion_result()) if series is None else series
    verdict = derive_scenario_verdict(
        selected_definition,
        selected_series,
        comparisons,
        verdict_id="VERDICT-FOUND-001-BASE",
        evaluated_at_tick=30,
        execution_validity=execution_validity,
        execution_validity_reason=execution_validity_reason,
        observations=observations,
    )
    return selected_definition, selected_series, verdict


def _passing_finding() -> VerdictFinding:
    return create_assertion_finding(_series(_assertion_result()).results[0])


def test_public_constants_and_enums_define_stable_contract() -> None:
    assert SUPPORTED_VERDICT_SCHEMA_VERSION == "1.0"
    assert MAX_VERDICT_REQUIRED_IDS == 50_000
    assert MAX_VERDICT_FINDINGS == 1_000_000
    assert MAX_VERDICT_OBSERVATIONS == 100_000
    assert MAX_TICK == (1 << 63) - 1
    assert {item.value for item in ExecutionValidity} == {"VALID_RUN", "INVALID_RUN"}
    assert {item.value for item in VerdictOutcome} == {
        "PASS",
        "PASS_WITH_OBSERVATION",
        "REVIEW",
        "FAIL",
        "BLOCKED",
    }
    assert {item.value for item in VerdictFindingKind} == {
        "ASSERTION_RESULT",
        "COMPARISON_REPORT",
    }
    assert {item.value for item in VerdictFindingStatus} == {
        "PASS",
        "FAIL",
        "REVIEW",
        "BLOCKED",
    }
    assert len(ExecutionValidityReason) == 12
    assert len(VerdictReason) == 9
    assert len(ObservationCategory) == 6


def test_definition_factory_sorts_ids_round_trips_and_hashes_all_content() -> None:
    definition = _definition(
        required_assertion_ids=("ASSERTION-FOUND-001-B2", "ASSERTION-FOUND-001-A1"),
        required_comparison_ids=("COMPARISON-FOUND-001-C2", "COMPARISON-FOUND-001-C1"),
        minimum_finding_count=4,
    )

    assert definition.required_assertion_ids == (
        "ASSERTION-FOUND-001-A1",
        "ASSERTION-FOUND-001-B2",
    )
    assert definition.required_comparison_ids == (
        "COMPARISON-FOUND-001-C1",
        "COMPARISON-FOUND-001-C2",
    )
    assert definition.definition_sha256 == calculate_verdict_definition_sha256(definition)
    assert VerdictDefinition.from_mapping(MappingProxyType(definition.to_mapping())) == definition
    assert (
        definition.definition_sha256
        != replace(definition, minimum_finding_count=5).definition_sha256
    )


def test_definition_is_frozen_and_slotted() -> None:
    definition = _definition()
    assert not hasattr(definition, "__dict__")
    with pytest.raises(FrozenInstanceError):
        definition.minimum_finding_count = 2  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("verdict_definition_id", "bad", "stable uppercase"),
        ("scenario_id", 1, "scenario_id must be a string"),
        ("scenario_id", "SCENARIO", "AURORA-SCN"),
        ("primary_run_id", 1, "must be a string"),
        ("primary_run_id", "bad", "stable uppercase"),
        ("required_assertion_ids", [], "tuple of strings"),
        ("required_assertion_ids", (1,), "tuple of strings"),
        ("required_assertion_ids", ("bad",), "stable uppercase"),
        (
            "required_assertion_ids",
            ("ASSERTION-FOUND-001-A1", "ASSERTION-FOUND-001-A1"),
            "duplicates",
        ),
        (
            "required_assertion_ids",
            ("ASSERTION-FOUND-001-B2", "ASSERTION-FOUND-001-A1"),
            "lexical order",
        ),
        ("required_comparison_ids", [], "tuple of strings"),
        ("required_comparison_ids", (1,), "tuple of strings"),
        ("required_comparison_ids", ("bad",), "stable uppercase"),
        (
            "required_comparison_ids",
            ("COMPARISON-FOUND-001-C1", "COMPARISON-FOUND-001-C1"),
            "duplicates",
        ),
        (
            "required_comparison_ids",
            ("COMPARISON-FOUND-001-C2", "COMPARISON-FOUND-001-C1"),
            "lexical order",
        ),
        ("minimum_finding_count", True, "must be an integer"),
        ("minimum_finding_count", 0, "must be positive"),
        ("minimum_finding_count", MAX_VERDICT_FINDINGS + 1, "must not exceed"),
    ],
)
def test_definition_rejects_invalid_fields(field: str, value: object, message: str) -> None:
    with pytest.raises(VerdictError, match=message):
        replace(_definition(), **{field: value})


def test_definition_enforces_required_id_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_REQUIRED_IDS", 1)
    with pytest.raises(VerdictError, match="must not exceed"):
        replace(
            _definition(),
            required_assertion_ids=("ASSERTION-FOUND-001-A1", "ASSERTION-FOUND-001-B2"),
        )


def test_definition_factory_requires_tuple_inputs() -> None:
    options: dict[str, object] = {
        "verdict_definition_id": "VERDICT-DEFINITION-FOUND-001",
        "scenario_id": _SCENARIO_ID,
        "primary_run_id": _PRIMARY_RUN_ID,
    }
    with pytest.raises(VerdictError, match="required_assertion_ids must be a tuple"):
        create_verdict_definition(**options, required_assertion_ids=[])  # type: ignore[arg-type]
    with pytest.raises(VerdictError, match="required_comparison_ids must be a tuple"):
        create_verdict_definition(**options, required_comparison_ids=[])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("scenario_id"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("verdict_schema_version", "2.0"),
        lambda data: data.__setitem__("verdict_type", "OTHER"),
        lambda data: data.__setitem__("definition_sha256", "b" * 64),
        lambda data: data.__setitem__("verdict_definition_id", 1),
        lambda data: data.__setitem__("scenario_id", 1),
        lambda data: data.__setitem__("primary_run_id", 1),
        lambda data: data.__setitem__("required_assertion_ids", {}),
        lambda data: data.__setitem__("required_assertion_ids", [1]),
        lambda data: data.__setitem__("required_comparison_ids", {}),
        lambda data: data.__setitem__("required_comparison_ids", [1]),
        lambda data: data.__setitem__("minimum_finding_count", True),
    ],
)
def test_definition_from_mapping_rejects_malformed_or_tampered_data(mutation: object) -> None:
    data = _definition().to_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(VerdictError):
        VerdictDefinition.from_mapping(data)


def test_definition_parser_and_digest_helper_reject_wrong_types() -> None:
    with pytest.raises(VerdictError, match="must be an object"):
        VerdictDefinition.from_mapping([])  # type: ignore[arg-type]
    with pytest.raises(VerdictError, match="keys must be strings"):
        VerdictDefinition.from_mapping({1: "bad"})  # type: ignore[dict-item]
    with pytest.raises(VerdictError, match="definition must"):
        calculate_verdict_definition_sha256(object())  # type: ignore[arg-type]


@pytest.mark.parametrize("status", list(AssertionStatus))
def test_assertion_finding_normalizes_status_and_redacts_actual(status: AssertionStatus) -> None:
    result = _assertion_result(status=status)

    finding = create_assertion_finding(result)
    data = finding.to_mapping()

    assert finding.kind is VerdictFindingKind.ASSERTION_RESULT
    assert finding.status is VerdictFindingStatus(status.value)
    assert finding.run_ids == (_PRIMARY_RUN_ID,)
    assert finding.source_id == result.result_id
    assert finding.source_sha256 == result.result_sha256
    assert VerdictFinding.from_mapping(MappingProxyType(data)) == finding
    assert "actual" not in data
    assert "SECRET-CANARY" not in json.dumps(data)


@pytest.mark.parametrize("status", list(ComparisonStatus))
def test_comparison_finding_normalizes_status_and_two_run_provenance(
    status: ComparisonStatus,
) -> None:
    report = _comparison_report(status=status)

    finding = create_comparison_finding(report)

    assert finding.kind is VerdictFindingKind.COMPARISON_REPORT
    assert finding.status is VerdictFindingStatus(status.value)
    assert finding.run_ids == (_PRIMARY_RUN_ID, _CANDIDATE_RUN_ID)
    assert finding.source_sha256 == report.report_sha256
    assert VerdictFinding.from_mapping(finding.to_mapping()) == finding


def test_finding_digest_is_content_sensitive_frozen_and_slotted() -> None:
    finding = _passing_finding()

    assert (
        finding.finding_sha256
        == hashlib.sha256(
            verdicts_module._canonical_json_bytes(finding._content_mapping())
        ).hexdigest()
    )
    assert (
        finding.finding_sha256 != replace(finding, reason_code="ANOTHER-PASS-REASON").finding_sha256
    )
    assert not hasattr(finding, "__dict__")
    with pytest.raises(FrozenInstanceError):
        finding.status = VerdictFindingStatus.FAIL  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("kind", "ASSERTION_RESULT", "VerdictFindingKind"),
        ("source_id", 1, "must be a string"),
        ("source_id", "bad", "stable uppercase"),
        ("source_sha256", 1, "must be a string"),
        ("source_sha256", "bad", "lowercase SHA-256"),
        ("scenario_id", 1, "scenario_id must be a string"),
        ("scenario_id", "SCENARIO", "AURORA-SCN"),
        ("run_ids", [], "tuple of strings"),
        ("run_ids", (1,), "tuple of strings"),
        ("run_ids", (), "exactly 1 run IDs"),
        ("run_ids", ("bad",), "stable uppercase"),
        ("invariant_id", "bad", "stable uppercase"),
        ("invariant_class", "HARD", "InvariantClass"),
        ("severity", "S4", "AssertionSeverity"),
        ("status", "PASS", "VerdictFindingStatus"),
        ("reason_code", 1, "must be a string"),
        ("reason_code", "bad", "stable uppercase"),
    ],
)
def test_finding_rejects_invalid_fields(field: str, value: object, message: str) -> None:
    with pytest.raises(VerdictError, match=message):
        replace(_passing_finding(), **{field: value})


def test_comparison_finding_requires_two_distinct_run_ids() -> None:
    finding = create_comparison_finding(_comparison_report())
    with pytest.raises(VerdictError, match="exactly 2 run IDs"):
        replace(finding, run_ids=(_PRIMARY_RUN_ID,))
    with pytest.raises(VerdictError, match="duplicates"):
        replace(finding, run_ids=(_PRIMARY_RUN_ID, _PRIMARY_RUN_ID))


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("status"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("finding_sha256", "b" * 64),
        lambda data: data.__setitem__("kind", "INVALID"),
        lambda data: data.__setitem__("source_id", 1),
        lambda data: data.__setitem__("source_sha256", 1),
        lambda data: data.__setitem__("scenario_id", 1),
        lambda data: data.__setitem__("run_ids", {}),
        lambda data: data.__setitem__("run_ids", [1]),
        lambda data: data.__setitem__("invariant_id", 1),
        lambda data: data.__setitem__("invariant_class", "INVALID"),
        lambda data: data.__setitem__("severity", "INVALID"),
        lambda data: data.__setitem__("status", "INVALID"),
        lambda data: data.__setitem__("reason_code", 1),
    ],
)
def test_finding_from_mapping_rejects_malformed_or_tampered_data(mutation: object) -> None:
    data = _passing_finding().to_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(VerdictError):
        VerdictFinding.from_mapping(data)


def test_finding_parser_and_factories_reject_wrong_types() -> None:
    with pytest.raises(VerdictError, match="must be an object"):
        VerdictFinding.from_mapping([])  # type: ignore[arg-type]
    with pytest.raises(VerdictError, match="result must"):
        create_assertion_finding(object())  # type: ignore[arg-type]
    with pytest.raises(VerdictError, match="report must"):
        create_comparison_finding(object())  # type: ignore[arg-type]


@pytest.mark.parametrize("category", list(ObservationCategory))
def test_observation_accepts_every_category_and_round_trips(
    category: ObservationCategory,
) -> None:
    finding = _passing_finding()
    observation = _observation(finding, category=category)

    assert observation.category is category
    assert observation.finding_sha256 == finding.finding_sha256
    assert (
        observation.observation_sha256
        == hashlib.sha256(
            verdicts_module._canonical_json_bytes(observation._content_mapping())
        ).hexdigest()
    )
    assert (
        VerdictObservation.from_mapping(MappingProxyType(observation.to_mapping())) == observation
    )


def test_observation_is_frozen_slotted_and_content_sensitive() -> None:
    observation = _observation(_passing_finding())

    assert (
        observation.observation_sha256
        != replace(observation, observation_code="ANOTHER-VALID-BEHAVIOR").observation_sha256
    )
    assert not hasattr(observation, "__dict__")
    with pytest.raises(FrozenInstanceError):
        observation.category = ObservationCategory.OTHER  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("observation_id", 1, "must be a string"),
        ("observation_id", "bad", "stable uppercase"),
        ("category", "EMERGENCE", "ObservationCategory"),
        ("observation_code", 1, "must be a string"),
        ("observation_code", "bad", "stable uppercase"),
        ("finding_sha256", 1, "must be a string"),
        ("finding_sha256", "bad", "lowercase SHA-256"),
    ],
)
def test_observation_rejects_invalid_fields(field: str, value: object, message: str) -> None:
    with pytest.raises(VerdictError, match=message):
        replace(_observation(_passing_finding()), **{field: value})


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("category"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("observation_sha256", "b" * 64),
        lambda data: data.__setitem__("observation_id", 1),
        lambda data: data.__setitem__("category", "INVALID"),
        lambda data: data.__setitem__("observation_code", 1),
        lambda data: data.__setitem__("finding_sha256", 1),
    ],
)
def test_observation_from_mapping_rejects_malformed_or_tampered_data(
    mutation: object,
) -> None:
    data = _observation(_passing_finding()).to_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(VerdictError):
        VerdictObservation.from_mapping(data)


def test_observation_factory_rejects_wrong_or_non_passing_finding() -> None:
    with pytest.raises(VerdictError, match="finding must"):
        create_verdict_observation(  # type: ignore[arg-type]
            observation_id="OBSERVATION-FOUND-001-O1",
            category=ObservationCategory.EMERGENCE,
            observation_code="VALID-NOVEL-BEHAVIOR",
            finding=object(),
        )
    failed = replace(_passing_finding(), status=VerdictFindingStatus.FAIL)
    with pytest.raises(VerdictError, match="only passing"):
        _observation(failed)


def test_observation_parser_requires_object() -> None:
    with pytest.raises(VerdictError, match="must be an object"):
        VerdictObservation.from_mapping([])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("status", "invariant_class", "outcome", "reason"),
    [
        (
            AssertionStatus.PASS,
            InvariantClass.HARD,
            VerdictOutcome.PASS,
            VerdictReason.ALL_REQUIRED_RESULTS_PASSED,
        ),
        (
            AssertionStatus.FAIL,
            InvariantClass.HARD,
            VerdictOutcome.FAIL,
            VerdictReason.HARD_INVARIANT_FAILED,
        ),
        (
            AssertionStatus.FAIL,
            InvariantClass.SOFT,
            VerdictOutcome.REVIEW,
            VerdictReason.NON_HARD_INVARIANT_FAILED,
        ),
        (
            AssertionStatus.FAIL,
            InvariantClass.CONTEXTUAL,
            VerdictOutcome.REVIEW,
            VerdictReason.NON_HARD_INVARIANT_FAILED,
        ),
        (
            AssertionStatus.REVIEW,
            InvariantClass.HARD,
            VerdictOutcome.REVIEW,
            VerdictReason.SOURCE_REVIEW_REQUIRED,
        ),
        (
            AssertionStatus.BLOCKED,
            InvariantClass.HARD,
            VerdictOutcome.BLOCKED,
            VerdictReason.REQUIRED_RESULT_BLOCKED,
        ),
    ],
)
def test_assertion_findings_drive_canonical_outcomes(
    status: AssertionStatus,
    invariant_class: InvariantClass,
    outcome: VerdictOutcome,
    reason: VerdictReason,
) -> None:
    series = _series(_assertion_result(status=status, invariant_class=invariant_class))

    _, _, verdict = _derive(series=series)

    assert (verdict.outcome, verdict.reason) == (outcome, reason)


@pytest.mark.parametrize(
    ("status", "invariant_class", "outcome", "reason"),
    [
        (
            ComparisonStatus.PASS,
            InvariantClass.HARD,
            VerdictOutcome.PASS,
            VerdictReason.ALL_REQUIRED_RESULTS_PASSED,
        ),
        (
            ComparisonStatus.FAIL,
            InvariantClass.HARD,
            VerdictOutcome.FAIL,
            VerdictReason.HARD_INVARIANT_FAILED,
        ),
        (
            ComparisonStatus.FAIL,
            InvariantClass.SOFT,
            VerdictOutcome.REVIEW,
            VerdictReason.NON_HARD_INVARIANT_FAILED,
        ),
        (
            ComparisonStatus.REVIEW,
            InvariantClass.HARD,
            VerdictOutcome.REVIEW,
            VerdictReason.SOURCE_REVIEW_REQUIRED,
        ),
        (
            ComparisonStatus.BLOCKED,
            InvariantClass.HARD,
            VerdictOutcome.BLOCKED,
            VerdictReason.REQUIRED_RESULT_BLOCKED,
        ),
    ],
)
def test_comparison_findings_participate_in_the_same_decision_policy(
    status: ComparisonStatus,
    invariant_class: InvariantClass,
    outcome: VerdictOutcome,
    reason: VerdictReason,
) -> None:
    report = _comparison_report(status=status, invariant_class=invariant_class)
    series = _series(_assertion_result())

    _, _, verdict = _derive(series=series, comparisons=(report,))

    assert (verdict.outcome, verdict.reason) == (outcome, reason)
    assert verdict.comparison_finding_count == 1


def test_explicit_observation_produces_pass_with_observation() -> None:
    series = _series(_assertion_result())
    finding = create_assertion_finding(series.results[0])
    observation = _observation(finding)

    _, _, verdict = _derive(series=series, observations=(observation,))

    assert (verdict.outcome, verdict.reason, verdict.observation_count) == (
        VerdictOutcome.PASS_WITH_OBSERVATION,
        VerdictReason.VALID_WITH_OBSERVATIONS,
        1,
    )


@pytest.mark.parametrize(
    "reason",
    [
        reason
        for reason in ExecutionValidityReason
        if reason is not ExecutionValidityReason.VERIFIED
    ],
)
def test_every_invalid_execution_reason_blocks_without_blame(
    reason: ExecutionValidityReason,
) -> None:
    series = _series(_assertion_result(status=AssertionStatus.FAIL))

    _, _, verdict = _derive(
        series=series,
        execution_validity=ExecutionValidity.INVALID_RUN,
        execution_validity_reason=reason,
    )

    assert (verdict.execution_validity, verdict.outcome, verdict.reason) == (
        ExecutionValidity.INVALID_RUN,
        VerdictOutcome.BLOCKED,
        VerdictReason.EXECUTION_INVALID,
    )
    assert verdict.hard_failure_count == 1


def test_missing_required_assertion_and_comparison_block_verdict() -> None:
    definition = _definition(
        required_assertion_ids=("ASSERTION-FOUND-001-MISSING",),
        required_comparison_ids=("COMPARISON-FOUND-001-MISSING",),
    )

    _, _, verdict = _derive(definition=definition)

    assert (verdict.outcome, verdict.reason) == (
        VerdictOutcome.BLOCKED,
        VerdictReason.MISSING_REQUIRED_RESULT,
    )
    assert verdict.missing_assertion_ids == ("ASSERTION-FOUND-001-MISSING",)
    assert verdict.missing_comparison_ids == ("COMPARISON-FOUND-001-MISSING",)
    assert verdict.missing_required_count == 2


def test_required_identity_is_satisfied_by_present_results() -> None:
    report = _comparison_report()
    definition = _definition(
        required_assertion_ids=("ASSERTION-FOUND-001-A1",),
        required_comparison_ids=("COMPARISON-FOUND-001-C1",),
        minimum_finding_count=2,
    )

    _, _, verdict = _derive(definition=definition, comparisons=(report,))

    assert verdict.outcome is VerdictOutcome.PASS
    assert verdict.missing_required_count == 0
    assert verdict.finding_count == 2


def test_empty_or_below_minimum_evidence_is_blocked() -> None:
    empty = _series()
    _, _, no_findings = _derive(series=empty)
    _, _, below_minimum = _derive(
        definition=_definition(minimum_finding_count=2),
        series=_series(_assertion_result()),
    )

    assert (no_findings.outcome, no_findings.reason) == (
        VerdictOutcome.BLOCKED,
        VerdictReason.INSUFFICIENT_EVIDENCE,
    )
    assert (below_minimum.outcome, below_minimum.reason) == (
        VerdictOutcome.BLOCKED,
        VerdictReason.INSUFFICIENT_EVIDENCE,
    )


def test_decision_priority_is_fail_closed_and_deterministic() -> None:
    blocked = _assertion_result(
        result_id="RESULT-FOUND-001-BLOCKED",
        assertion_id="ASSERTION-FOUND-001-BLOCKED",
        status=AssertionStatus.BLOCKED,
    )
    failed = _assertion_result(
        result_id="RESULT-FOUND-001-FAILED",
        assertion_id="ASSERTION-FOUND-001-FAILED",
        status=AssertionStatus.FAIL,
    )
    review = _assertion_result(
        result_id="RESULT-FOUND-001-REVIEW",
        assertion_id="ASSERTION-FOUND-001-REVIEW",
        status=AssertionStatus.REVIEW,
    )
    series = _series(blocked, failed, review)

    _, _, blocked_verdict = _derive(series=series)
    _, _, missing_verdict = _derive(
        definition=_definition(required_assertion_ids=("ASSERTION-FOUND-001-MISSING",)),
        series=series,
    )
    _, _, insufficient_verdict = _derive(
        definition=_definition(minimum_finding_count=4),
        series=series,
    )
    _, _, invalid_verdict = _derive(
        definition=_definition(required_assertion_ids=("ASSERTION-FOUND-001-MISSING",)),
        series=series,
        execution_validity=ExecutionValidity.INVALID_RUN,
        execution_validity_reason=ExecutionValidityReason.HARNESS_ERROR,
    )

    assert blocked_verdict.reason is VerdictReason.REQUIRED_RESULT_BLOCKED
    assert missing_verdict.reason is VerdictReason.MISSING_REQUIRED_RESULT
    assert insufficient_verdict.reason is VerdictReason.INSUFFICIENT_EVIDENCE
    assert invalid_verdict.reason is VerdictReason.EXECUTION_INVALID


@pytest.mark.parametrize(
    ("validity", "reason", "message"),
    [
        (
            ExecutionValidity.VALID_RUN,
            ExecutionValidityReason.FIXTURE_INVALID,
            "VALID_RUN requires",
        ),
        (
            ExecutionValidity.INVALID_RUN,
            ExecutionValidityReason.VERIFIED,
            "INVALID_RUN requires",
        ),
    ],
)
def test_execution_validity_and_reason_must_agree(
    validity: ExecutionValidity,
    reason: ExecutionValidityReason,
    message: str,
) -> None:
    with pytest.raises(VerdictError, match=message):
        _derive(execution_validity=validity, execution_validity_reason=reason)


def test_observations_cannot_override_failure_review_or_blocked_results() -> None:
    passing = _assertion_result(
        result_id="RESULT-FOUND-001-PASS",
        assertion_id="ASSERTION-FOUND-001-PASS",
    )
    observation_series = _series(passing)
    observation = _observation(create_assertion_finding(observation_series.results[0]))

    for status, expected in (
        (AssertionStatus.FAIL, VerdictOutcome.FAIL),
        (AssertionStatus.REVIEW, VerdictOutcome.REVIEW),
        (AssertionStatus.BLOCKED, VerdictOutcome.BLOCKED),
    ):
        adverse = _assertion_result(
            result_id=f"RESULT-FOUND-001-{status.value}",
            assertion_id=f"ASSERTION-FOUND-001-{status.value}",
            status=status,
        )
        combined = _series(passing, adverse)
        rebound_observation = _observation(create_assertion_finding(combined.results[0]))
        _, _, verdict = _derive(series=combined, observations=(rebound_observation,))
        assert verdict.outcome is expected

    assert (
        observation.finding_sha256
        == create_assertion_finding(observation_series.results[0]).finding_sha256
    )


def test_scenario_verdict_counts_hashes_round_trip_and_redacted_evidence() -> None:
    passing = _assertion_result(
        result_id="RESULT-FOUND-001-PASS",
        assertion_id="ASSERTION-FOUND-001-PASS",
    )
    failed = _assertion_result(
        result_id="RESULT-FOUND-001-FAIL",
        assertion_id="ASSERTION-FOUND-001-FAIL",
        invariant_class=InvariantClass.SOFT,
        status=AssertionStatus.FAIL,
    )
    reviewed = _assertion_result(
        result_id="RESULT-FOUND-001-REVIEW",
        assertion_id="ASSERTION-FOUND-001-REVIEW",
        status=AssertionStatus.REVIEW,
    )
    blocked = _comparison_report(status=ComparisonStatus.BLOCKED)
    series = _series(passing, failed, reviewed)

    definition, _, verdict = _derive(series=series, comparisons=(blocked,))
    validator_data = verdict.to_validator_mapping()
    evidence_data = verdict.to_evidence_mapping()

    assert verdict.verdict_definition_sha256 == definition.definition_sha256
    assert (verdict.finding_count, verdict.assertion_finding_count) == (4, 3)
    assert verdict.comparison_finding_count == 1
    assert (verdict.passed_finding_count, verdict.failed_finding_count) == (1, 1)
    assert (verdict.review_finding_count, verdict.blocked_finding_count) == (1, 1)
    assert verdict.hard_failure_count == 0
    assert verdict.verdict_sha256 == calculate_scenario_verdict_sha256(verdict)
    assert ScenarioVerdict.from_mapping(MappingProxyType(validator_data)) == verdict
    assert create_verdict_evidence_payload(verdict).decode() == evidence_data
    assert evidence_data["finding_sha256"] == [
        finding.finding_sha256 for finding in verdict.findings
    ]
    assert "findings" not in evidence_data
    assert "SECRET-CANARY" not in json.dumps(validator_data)
    assert "SECRET-CANARY" not in json.dumps(evidence_data)


def test_scenario_verdict_is_frozen_slotted_and_digest_sensitive() -> None:
    _, _, verdict = _derive()

    assert not hasattr(verdict, "__dict__")
    assert verdict.verdict_sha256 != replace(verdict, evaluated_at_tick=31).verdict_sha256
    with pytest.raises(FrozenInstanceError):
        verdict.outcome = VerdictOutcome.FAIL  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("verdict_id", 1, "must be a string"),
        ("verdict_id", "bad", "stable uppercase"),
        ("verdict_definition_id", "bad", "stable uppercase"),
        ("verdict_definition_sha256", 1, "must be a string"),
        ("verdict_definition_sha256", "bad", "lowercase SHA-256"),
        ("scenario_id", 1, "scenario_id must be a string"),
        ("scenario_id", "SCENARIO", "AURORA-SCN"),
        ("primary_run_id", "bad", "stable uppercase"),
        ("assertion_series_sha256", 1, "must be a string"),
        ("assertion_series_sha256", "bad", "lowercase SHA-256"),
        ("evaluated_at_tick", True, "must be an integer"),
        ("evaluated_at_tick", -1, "between 0"),
        ("evaluated_at_tick", MAX_TICK + 1, "between 0"),
        ("execution_validity", "VALID_RUN", "ExecutionValidity"),
        (
            "execution_validity_reason",
            "VERIFIED",
            "ExecutionValidityReason",
        ),
        ("minimum_finding_count", True, "must be an integer"),
        ("minimum_finding_count", 0, "must be positive"),
        ("minimum_finding_count", MAX_VERDICT_FINDINGS + 1, "must not exceed"),
        ("outcome", "PASS", "VerdictOutcome"),
        ("reason", "ALL_REQUIRED_RESULTS_PASSED", "VerdictReason"),
        ("findings", [], "tuple of VerdictFinding"),
        ("findings", (object(),), "tuple of VerdictFinding"),
        ("observations", [], "tuple of VerdictObservation"),
        ("observations", (object(),), "tuple of VerdictObservation"),
        ("missing_assertion_ids", [], "tuple of strings"),
        ("missing_comparison_ids", [], "tuple of strings"),
    ],
)
def test_scenario_verdict_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    _, _, verdict = _derive()
    with pytest.raises(VerdictError, match=message):
        replace(verdict, **{field: value})


def test_scenario_verdict_rejects_outcome_or_reason_not_derived_from_evidence() -> None:
    _, _, verdict = _derive()
    with pytest.raises(VerdictError, match="do not match verdict evidence"):
        replace(
            verdict,
            outcome=VerdictOutcome.FAIL,
            reason=VerdictReason.HARD_INVARIANT_FAILED,
        )


def test_scenario_verdict_enforces_finding_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    series = _series(
        _assertion_result(
            result_id="RESULT-FOUND-001-A1",
            assertion_id="ASSERTION-FOUND-001-A1",
        ),
        _assertion_result(
            result_id="RESULT-FOUND-001-B2",
            assertion_id="ASSERTION-FOUND-001-B2",
        ),
    )
    _, _, verdict = _derive(series=series)
    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_FINDINGS", 1)
    with pytest.raises(VerdictError, match="findings must not exceed"):
        replace(verdict)


def test_scenario_verdict_rejects_duplicate_unordered_and_mismatched_findings(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first = create_assertion_finding(
        _series(
            _assertion_result(
                result_id="RESULT-FOUND-001-A1",
                assertion_id="ASSERTION-FOUND-001-A1",
            )
        ).results[0]
    )
    second = replace(
        first,
        source_id="RESULT-FOUND-001-B2",
        source_sha256="2" * 64,
        invariant_id="AURORA-INFO-002",
    )
    ordered = tuple(sorted((first, second), key=lambda finding: finding.finding_sha256))
    _, _, verdict = _derive()

    with pytest.raises(VerdictError, match="unique source kind and ID"):
        replace(verdict, findings=(first, first))
    with pytest.raises(VerdictError, match="ordered by finding_sha256"):
        replace(verdict, findings=tuple(reversed(ordered)))
    with pytest.raises(VerdictError, match="finding scenario"):
        replace(
            verdict,
            findings=(replace(first, scenario_id="AURORA-SCN-FOUND-002"),),
        )
    with pytest.raises(VerdictError, match="primary verdict run"):
        replace(verdict, findings=(replace(first, run_ids=(_OTHER_RUN_ID,)),))

    monkeypatch.setattr(
        VerdictFinding,
        "finding_sha256",
        property(lambda self: "0" * 64),
    )
    with pytest.raises(VerdictError, match="unique finding hashes"):
        verdicts_module._validate_findings((first, second), _SCENARIO_ID, _PRIMARY_RUN_ID)


def test_scenario_verdict_enforces_observation_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    series = _series(_assertion_result())
    observation = _observation(create_assertion_finding(series.results[0]))
    _, _, verdict = _derive(series=series, observations=(observation,))
    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_OBSERVATIONS", 0)
    with pytest.raises(VerdictError, match="observations must not exceed"):
        replace(verdict)


def test_scenario_verdict_rejects_duplicate_unordered_or_unbound_observations(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    series = _series(
        _assertion_result(
            result_id="RESULT-FOUND-001-A1",
            assertion_id="ASSERTION-FOUND-001-A1",
        ),
        _assertion_result(
            result_id="RESULT-FOUND-001-B2",
            assertion_id="ASSERTION-FOUND-001-B2",
        ),
    )
    findings = tuple(create_assertion_finding(result) for result in series.results)
    first = _observation(findings[0], observation_id="OBSERVATION-FOUND-001-O1")
    second = _observation(findings[1], observation_id="OBSERVATION-FOUND-001-O2")
    observations = tuple(
        sorted((first, second), key=lambda observation: observation.observation_sha256)
    )
    _, _, verdict = _derive(series=series, observations=observations)

    with pytest.raises(VerdictError, match="unique observation IDs"):
        replace(
            verdict, observations=(first, replace(first, finding_sha256=findings[1].finding_sha256))
        )
    with pytest.raises(VerdictError, match="ordered by observation_sha256"):
        replace(verdict, observations=tuple(reversed(observations)))
    with pytest.raises(VerdictError, match="reference a verdict finding"):
        replace(verdict, observations=(replace(first, finding_sha256="9" * 64),))

    failed = replace(findings[0], status=VerdictFindingStatus.FAIL)
    failed_verdict = replace(
        verdict,
        findings=tuple(sorted((failed, findings[1]), key=lambda finding: finding.finding_sha256)),
        observations=(),
        outcome=VerdictOutcome.FAIL,
        reason=VerdictReason.HARD_INVARIANT_FAILED,
    )
    with pytest.raises(VerdictError, match="only passing findings"):
        replace(
            failed_verdict,
            observations=(replace(first, finding_sha256=failed.finding_sha256),),
        )

    monkeypatch.setattr(
        VerdictObservation,
        "observation_sha256",
        property(lambda self: "0" * 64),
    )
    with pytest.raises(VerdictError, match="unique observation hashes"):
        verdicts_module._validate_observations((first, second), findings)


def test_scenario_verdict_enforces_missing_id_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    definition = _definition(required_assertion_ids=("ASSERTION-FOUND-001-MISSING",))
    _, _, verdict = _derive(definition=definition)
    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_REQUIRED_IDS", 0)
    with pytest.raises(VerdictError, match="must not exceed"):
        replace(verdict)


@pytest.mark.parametrize(
    ("definition", "series", "comparisons", "observations", "message"),
    [
        (object(), None, (), (), "definition must"),
        (None, object(), (), (), "assertion_series must"),
        (None, None, [], (), "comparisons must"),
        (None, None, (object(),), (), "comparisons must"),
        (None, None, (), [], "observations must"),
        (None, None, (), (object(),), "observations must"),
    ],
)
def test_derive_rejects_wrong_input_types(
    definition: object,
    series: object,
    comparisons: object,
    observations: object,
    message: str,
) -> None:
    valid_definition = _definition()
    valid_series = _series(_assertion_result())
    with pytest.raises(VerdictError, match=message):
        derive_scenario_verdict(
            valid_definition if definition is None else definition,  # type: ignore[arg-type]
            valid_series if series is None else series,  # type: ignore[arg-type]
            comparisons,  # type: ignore[arg-type]
            verdict_id="VERDICT-FOUND-001-BASE",
            evaluated_at_tick=30,
            execution_validity=ExecutionValidity.VALID_RUN,
            execution_validity_reason=ExecutionValidityReason.VERIFIED,
            observations=observations,  # type: ignore[arg-type]
        )


def test_derive_enforces_comparison_and_observation_input_bounds(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    report = _comparison_report()
    series = _series(_assertion_result())
    observation = _observation(create_assertion_finding(series.results[0]))

    second_report = _comparison_report(
        report_id="REPORT-FOUND-001-C2",
        comparison_id="COMPARISON-FOUND-001-C2",
    )
    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_FINDINGS", 1)
    with pytest.raises(VerdictError, match="comparisons must not exceed"):
        _derive(series=series, comparisons=(report, second_report))

    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_FINDINGS", MAX_VERDICT_FINDINGS)
    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_OBSERVATIONS", 0)
    with pytest.raises(VerdictError, match="observations must not exceed"):
        _derive(series=series, observations=(observation,))


def test_derive_enforces_combined_finding_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    series = _series(
        _assertion_result(
            result_id="RESULT-FOUND-001-A1",
            assertion_id="ASSERTION-FOUND-001-A1",
        ),
        _assertion_result(
            result_id="RESULT-FOUND-001-B2",
            assertion_id="ASSERTION-FOUND-001-B2",
        ),
    )
    monkeypatch.setattr(verdicts_module, "MAX_VERDICT_FINDINGS", 1)
    with pytest.raises(VerdictError, match="verdict must not exceed"):
        _derive(series=series)


@pytest.mark.parametrize(
    ("target", "message"),
    [
        ("series_scenario", "assertion series scenario"),
        ("series_run", "assertion series run"),
        ("comparison_scenario", "comparison scenario"),
        ("comparison_run", "does not include the primary"),
    ],
)
def test_derive_rejects_scenario_or_run_identity_mismatch(
    target: str,
    message: str,
) -> None:
    definition = _definition()
    series = _series(_assertion_result())
    comparisons: tuple[ComparisonReport, ...] = ()
    if target == "series_scenario":
        series = replace(series, scenario_id="AURORA-SCN-FOUND-002", results=())
    elif target == "series_run":
        series = replace(series, run_id=_OTHER_RUN_ID, results=())
    elif target == "comparison_scenario":
        comparisons = (_comparison_report(scenario_id="AURORA-SCN-FOUND-002"),)
    else:
        comparisons = (
            _comparison_report(
                baseline_run_id=_OTHER_RUN_ID,
                candidate_run_id="AURORA-RUN-FOUND-001-ALT",
            ),
        )

    with pytest.raises(VerdictError, match=message):
        _derive(definition=definition, series=series, comparisons=comparisons)


def test_comparison_may_include_primary_run_as_candidate() -> None:
    report = _comparison_report(
        baseline_run_id=_CANDIDATE_RUN_ID,
        candidate_run_id=_PRIMARY_RUN_ID,
    )

    _, _, verdict = _derive(comparisons=(report,))

    assert verdict.outcome is VerdictOutcome.PASS
    comparison = next(
        finding
        for finding in verdict.findings
        if finding.kind is VerdictFindingKind.COMPARISON_REPORT
    )
    assert comparison.run_ids == (_CANDIDATE_RUN_ID, _PRIMARY_RUN_ID)


def test_derive_rejects_duplicate_comparison_and_report_ids() -> None:
    first = _comparison_report()
    duplicate_comparison = _comparison_report(
        report_id="REPORT-FOUND-001-C2",
        comparison_id=first.comparison_id,
    )
    duplicate_report = _comparison_report(
        report_id=first.report_id,
        comparison_id="COMPARISON-FOUND-001-C2",
    )

    with pytest.raises(VerdictError, match="comparison_id values must be unique"):
        _derive(comparisons=(first, duplicate_comparison))
    with pytest.raises(VerdictError, match="report IDs must be unique"):
        _derive(comparisons=(first, duplicate_report))


def test_derive_rejects_observation_bound_to_unsupplied_finding() -> None:
    foreign = _observation(replace(_passing_finding(), source_id="RESULT-FOUND-001-FOREIGN"))
    with pytest.raises(VerdictError, match="supplied verdict finding"):
        _derive(observations=(foreign,))


@pytest.mark.parametrize(
    ("verdict_id", "tick", "validity", "validity_reason", "message"),
    [
        (
            "bad",
            30,
            ExecutionValidity.VALID_RUN,
            ExecutionValidityReason.VERIFIED,
            "stable uppercase",
        ),
        (
            "VERDICT-FOUND-001-BASE",
            True,
            ExecutionValidity.VALID_RUN,
            ExecutionValidityReason.VERIFIED,
            "must be an integer",
        ),
        (
            "VERDICT-FOUND-001-BASE",
            -1,
            ExecutionValidity.VALID_RUN,
            ExecutionValidityReason.VERIFIED,
            "between 0",
        ),
        (
            "VERDICT-FOUND-001-BASE",
            MAX_TICK + 1,
            ExecutionValidity.VALID_RUN,
            ExecutionValidityReason.VERIFIED,
            "between 0",
        ),
        (
            "VERDICT-FOUND-001-BASE",
            30,
            "VALID_RUN",
            ExecutionValidityReason.VERIFIED,
            "execution_validity must",
        ),
        (
            "VERDICT-FOUND-001-BASE",
            30,
            ExecutionValidity.VALID_RUN,
            "VERIFIED",
            "execution_validity_reason must",
        ),
    ],
)
def test_derive_rejects_invalid_identity_tick_or_execution_enums(
    verdict_id: str,
    tick: int,
    validity: object,
    validity_reason: object,
    message: str,
) -> None:
    with pytest.raises(VerdictError, match=message):
        derive_scenario_verdict(
            _definition(),
            _series(_assertion_result()),
            (),
            verdict_id=verdict_id,
            evaluated_at_tick=tick,
            execution_validity=validity,  # type: ignore[arg-type]
            execution_validity_reason=validity_reason,  # type: ignore[arg-type]
        )


def test_derive_canonicalizes_finding_and_observation_order() -> None:
    first = _assertion_result(
        result_id="RESULT-FOUND-001-A1",
        assertion_id="ASSERTION-FOUND-001-A1",
    )
    second = _assertion_result(
        result_id="RESULT-FOUND-001-B2",
        assertion_id="ASSERTION-FOUND-001-B2",
    )
    series = _series(first, second)
    findings = tuple(create_assertion_finding(result) for result in series.results)
    observations = (
        _observation(findings[1], observation_id="OBSERVATION-FOUND-001-O2"),
        _observation(findings[0], observation_id="OBSERVATION-FOUND-001-O1"),
    )

    _, _, verdict = _derive(series=series, observations=observations)

    assert tuple(finding.finding_sha256 for finding in verdict.findings) == tuple(
        sorted(finding.finding_sha256 for finding in findings)
    )
    assert tuple(observation.observation_sha256 for observation in verdict.observations) == tuple(
        sorted(observation.observation_sha256 for observation in observations)
    )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("outcome"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("verdict_schema_version", "2.0"),
        lambda data: data.__setitem__("verdict_type", "OTHER"),
        lambda data: data.__setitem__("verdict_sha256", "b" * 64),
        lambda data: data.__setitem__("verdict_id", 1),
        lambda data: data.__setitem__("verdict_definition_id", 1),
        lambda data: data.__setitem__("verdict_definition_sha256", 1),
        lambda data: data.__setitem__("scenario_id", 1),
        lambda data: data.__setitem__("primary_run_id", 1),
        lambda data: data.__setitem__("assertion_series_sha256", 1),
        lambda data: data.__setitem__("evaluated_at_tick", True),
        lambda data: data.__setitem__("execution_validity", "INVALID"),
        lambda data: data.__setitem__("execution_validity_reason", "INVALID"),
        lambda data: data.__setitem__("minimum_finding_count", True),
        lambda data: data.__setitem__("outcome", "INVALID"),
        lambda data: data.__setitem__("reason", "INVALID"),
        lambda data: data.__setitem__("findings", {}),
        lambda data: data.__setitem__("findings", [[]]),
        lambda data: data.__setitem__("observations", {}),
        lambda data: data.__setitem__("observations", [[]]),
        lambda data: data.__setitem__("missing_assertion_ids", {}),
        lambda data: data.__setitem__("missing_assertion_ids", [1]),
        lambda data: data.__setitem__("missing_comparison_ids", {}),
        lambda data: data.__setitem__("missing_comparison_ids", [1]),
    ],
)
def test_scenario_verdict_from_mapping_rejects_malformed_or_tampered_data(
    mutation: object,
) -> None:
    _, _, verdict = _derive()
    data = verdict.to_validator_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(VerdictError):
        ScenarioVerdict.from_mapping(data)


@pytest.mark.parametrize(
    "field",
    [
        "assertion_finding_count",
        "blocked_finding_count",
        "comparison_finding_count",
        "failed_finding_count",
        "finding_count",
        "hard_failure_count",
        "missing_required_count",
        "observation_count",
        "passed_finding_count",
        "review_finding_count",
    ],
)
def test_scenario_verdict_from_mapping_verifies_every_derived_count(field: str) -> None:
    _, _, verdict = _derive()
    data = verdict.to_validator_mapping()
    current = data[field]
    assert isinstance(current, int)
    data[field] = current + 1

    with pytest.raises(VerdictError, match=f"declared {field}"):
        ScenarioVerdict.from_mapping(data)


def test_scenario_verdict_from_mapping_requires_integer_counts() -> None:
    _, _, verdict = _derive()
    data = verdict.to_validator_mapping()
    data["finding_count"] = True
    with pytest.raises(VerdictError, match="must be an integer"):
        ScenarioVerdict.from_mapping(data)


def test_scenario_verdict_parser_and_helpers_reject_wrong_types() -> None:
    with pytest.raises(VerdictError, match="must be an object"):
        ScenarioVerdict.from_mapping([])  # type: ignore[arg-type]
    with pytest.raises(VerdictError, match="verdict must"):
        calculate_scenario_verdict_sha256(object())  # type: ignore[arg-type]
    with pytest.raises(VerdictError, match="verdict must"):
        create_verdict_evidence_payload(object())  # type: ignore[arg-type]
    with pytest.raises(VerdictError, match="verdict must"):
        validate_scenario_verdict(  # type: ignore[arg-type]
            object(), _definition(), _series(_assertion_result()), ()
        )


def test_validate_scenario_verdict_accepts_recomputation_and_rejects_change() -> None:
    definition, series, verdict = _derive()

    validate_scenario_verdict(verdict, definition, series, ())
    with pytest.raises(VerdictError, match="does not match"):
        validate_scenario_verdict(
            replace(verdict, assertion_series_sha256="9" * 64),
            definition,
            series,
            (),
        )


def test_serialized_mappings_are_detached_from_immutable_models() -> None:
    definition, _, verdict = _derive()
    definition_data = definition.to_mapping()
    verdict_data = verdict.to_validator_mapping()

    definition_data["required_assertion_ids"] = ["ASSERTION-FOUND-001-OTHER"]
    verdict_data["findings"] = []

    assert definition.required_assertion_ids == ()
    assert verdict.finding_count == 1
    assert copy.deepcopy(verdict.to_validator_mapping()) == verdict.to_validator_mapping()


def test_private_helpers_reject_non_json_and_non_string_mapping_keys() -> None:
    with pytest.raises(VerdictError, match="canonical finite JSON"):
        verdicts_module._canonical_json_bytes(object())
    with pytest.raises(VerdictError, match="canonical finite JSON"):
        verdicts_module._canonical_json_bytes({"value": float("nan")})
    with pytest.raises(VerdictError, match="keys must be strings"):
        verdicts_module._require_mapping({1: "bad"}, field="test")


def test_evidence_summary_exposes_only_digests_and_machine_readable_counts() -> None:
    series = _series(_assertion_result(actual={"secret": "HIDDEN-WORLD-TRUTH"}))
    finding = create_assertion_finding(series.results[0])
    observation = _observation(finding)
    _, _, verdict = _derive(series=series, observations=(observation,))

    evidence = verdict.to_evidence_mapping()
    serialized = json.dumps(evidence, sort_keys=True)

    assert "HIDDEN-WORLD-TRUTH" not in serialized
    assert "actual" not in serialized
    assert evidence["outcome"] == "PASS_WITH_OBSERVATION"
    assert evidence["execution_validity"] == "VALID_RUN"
    assert evidence["observation_sha256"] == [observation.observation_sha256]
