"""Unit tests for deterministic cross-run assertion comparisons."""

from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import FrozenInstanceError, replace
from types import MappingProxyType

import pytest

from aurora_validation_harness import comparison as comparison_module
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
    MAX_COMPARISON_ASSERTION_IDS,
    MAX_COMPARISON_PAIRS,
    MAX_TICK,
    SUPPORTED_COMPARISON_SCHEMA_VERSION,
    ComparisonDefinition,
    ComparisonError,
    ComparisonKey,
    ComparisonKind,
    ComparisonOperand,
    ComparisonPolicy,
    ComparisonReason,
    ComparisonReport,
    ComparisonStatus,
    DifferenceKind,
    ResultComparison,
    calculate_comparison_definition_sha256,
    calculate_comparison_report_sha256,
    compare_assertion_series,
    create_comparison_definition,
    create_comparison_evidence_payload,
    validate_comparison_report,
)
from aurora_validation_harness.evidence import EvidenceDomain

pytestmark = [
    pytest.mark.foundation,
    pytest.mark.isolation,
    pytest.mark.metamorphic,
]

_BASELINE_RUN_ID = "AURORA-RUN-FOUND-001-BASE"
_CANDIDATE_RUN_ID = "AURORA-RUN-FOUND-001-CAND"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"
_NO_ACTUAL = object()


def _result(
    run_id: str,
    *,
    result_id: str,
    assertion_id: str = "ASSERTION-FOUND-001-A1",
    assertion_sha256: str = "a" * 64,
    invariant_id: str = "AURORA-INFO-001",
    invariant_class: InvariantClass = InvariantClass.HARD,
    severity: AssertionSeverity = AssertionSeverity.S4,
    target_kind: AssertionTargetKind = AssertionTargetKind.SNAPSHOT,
    target_domain: EvidenceDomain = EvidenceDomain.AURORA_STATE,
    path: str | None = "/value",
    status: AssertionStatus = AssertionStatus.PASS,
    reason: AssertionReason = AssertionReason.VALUES_EQUAL,
    actual: object = "UNKNOWN",
) -> AssertionResult:
    """Create a valid result whose semantic fields can be controlled independently."""

    run_label = "BASE" if run_id == _BASELINE_RUN_ID else "CAND"
    return AssertionResult(
        result_id=result_id,
        run_id=run_id,
        scenario_id=_SCENARIO_ID,
        sequence=0,
        evaluated_at_tick=10,
        assertion_id=assertion_id,
        assertion_sha256=assertion_sha256,
        invariant_id=invariant_id,
        invariant_class=invariant_class,
        severity=severity,
        target_kind=target_kind,
        target_id=f"TARGET-FOUND-001-{run_label}",
        target_sha256=("b" if run_id == _BASELINE_RUN_ID else "c") * 64,
        target_domain=target_domain,
        status=status,
        reason=reason,
        path=path,
        actual=None if actual is _NO_ACTUAL else create_assertion_value(actual),
        previous_result_sha256=None,
    )


def _series(run_id: str, *results: AssertionResult) -> AssertionSeries:
    """Re-chain supplied results into one valid immutable series."""

    chained: list[AssertionResult] = []
    previous_sha256: str | None = None
    for sequence, result in enumerate(results):
        current = replace(
            result,
            sequence=sequence,
            previous_result_sha256=previous_sha256,
        )
        chained.append(current)
        previous_sha256 = current.result_sha256
    return AssertionSeries(run_id, _SCENARIO_ID, tuple(chained))


def _definition(
    policy: ComparisonPolicy = ComparisonPolicy.EXACT,
    *,
    invariant_class: InvariantClass = InvariantClass.HARD,
    assertion_ids: tuple[str, ...] = (),
    minimum_paired_results: int = 1,
    allow_unpaired_results: bool = False,
) -> ComparisonDefinition:
    return create_comparison_definition(
        comparison_id="COMPARISON-FOUND-001-C1",
        scenario_id=_SCENARIO_ID,
        baseline_run_id=_BASELINE_RUN_ID,
        candidate_run_id=_CANDIDATE_RUN_ID,
        invariant_id="AURORA-COMPARISON-001",
        invariant_class=invariant_class,
        severity=AssertionSeverity.S4,
        kind=ComparisonKind.REPEATABILITY,
        policy=policy,
        assertion_ids=assertion_ids,
        minimum_paired_results=minimum_paired_results,
        allow_unpaired_results=allow_unpaired_results,
    )


def _inputs(
    *,
    baseline_actual: object = "UNKNOWN",
    candidate_actual: object = "UNKNOWN",
    baseline_status: AssertionStatus = AssertionStatus.PASS,
    candidate_status: AssertionStatus = AssertionStatus.PASS,
    baseline_reason: AssertionReason = AssertionReason.VALUES_EQUAL,
    candidate_reason: AssertionReason = AssertionReason.VALUES_EQUAL,
    baseline_definition_sha256: str = "a" * 64,
    candidate_definition_sha256: str = "a" * 64,
    invariant_class: InvariantClass = InvariantClass.HARD,
) -> tuple[AssertionSeries, AssertionSeries]:
    baseline = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE",
        actual=baseline_actual,
        status=baseline_status,
        reason=baseline_reason,
        assertion_sha256=baseline_definition_sha256,
        invariant_class=invariant_class,
    )
    candidate = _result(
        _CANDIDATE_RUN_ID,
        result_id="RESULT-FOUND-001-CAND",
        actual=candidate_actual,
        status=candidate_status,
        reason=candidate_reason,
        assertion_sha256=candidate_definition_sha256,
        invariant_class=invariant_class,
    )
    return _series(_BASELINE_RUN_ID, baseline), _series(_CANDIDATE_RUN_ID, candidate)


def _report(
    policy: ComparisonPolicy = ComparisonPolicy.EXACT,
    *,
    invariant_class: InvariantClass = InvariantClass.HARD,
    baseline: AssertionSeries | None = None,
    candidate: AssertionSeries | None = None,
    **definition_options: object,
) -> tuple[ComparisonDefinition, AssertionSeries, AssertionSeries, ComparisonReport]:
    if baseline is None or candidate is None:
        default_baseline, default_candidate = _inputs(invariant_class=invariant_class)
        baseline = default_baseline if baseline is None else baseline
        candidate = default_candidate if candidate is None else candidate
    definition = _definition(
        policy,
        invariant_class=invariant_class,
        **definition_options,  # type: ignore[arg-type]
    )
    report = compare_assertion_series(
        definition,
        baseline,
        candidate,
        report_id="REPORT-FOUND-001-C1",
        evaluated_at_tick=20,
    )
    return definition, baseline, candidate, report


def _operand(**changes: object) -> ComparisonOperand:
    _, _, _, report = _report()
    baseline = report.pairs[0].baseline
    assert baseline is not None
    return replace(baseline, **changes)


def _pair(
    *,
    baseline: ComparisonOperand | None = None,
    candidate: ComparisonOperand | None = None,
    occurrence: int = 0,
) -> ResultComparison:
    if baseline is None and candidate is None:
        baseline = _operand()
        candidate = replace(baseline, result_id="RESULT-FOUND-001-CAND", result_sha256="d" * 64)
    operand = baseline if baseline is not None else candidate
    assert operand is not None
    key = ComparisonKey(
        assertion_id=operand.assertion_id,
        target_kind=operand.target_kind,
        target_domain=operand.target_domain,
        path=operand.path,
        occurrence=occurrence,
    )
    return ResultComparison(
        key=key,
        baseline=baseline,
        candidate=candidate,
        differences=comparison_module._derive_differences(baseline, candidate),
    )


def test_public_constants_and_enums_define_stable_contract() -> None:
    assert SUPPORTED_COMPARISON_SCHEMA_VERSION == "1.0"
    assert MAX_COMPARISON_ASSERTION_IDS == 50_000
    assert MAX_COMPARISON_PAIRS == 1_000_000
    assert MAX_TICK == (1 << 63) - 1
    assert {item.value for item in ComparisonKind} == {
        "REPEATABILITY",
        "HIDDEN_STATE",
        "INFORMATION",
        "COUNTERFACTUAL",
        "VERSION",
        "CUSTOM",
    }
    assert {item.value for item in ComparisonPolicy} == {
        "EXACT",
        "OUTCOME_EQUIVALENT",
        "ACTUAL_EQUIVALENT",
        "EXPECTED_DIVERGENCE",
        "NO_STATUS_REGRESSION",
        "ACTUAL_NON_INCREASING",
        "ACTUAL_NON_DECREASING",
    }
    assert {item.value for item in ComparisonStatus} == {"PASS", "FAIL", "REVIEW", "BLOCKED"}
    assert {item.value for item in DifferenceKind} == {
        "MISSING_BASELINE",
        "MISSING_CANDIDATE",
        "DEFINITION_CHANGED",
        "STATUS_CHANGED",
        "REASON_CHANGED",
        "ACTUAL_CHANGED",
    }
    assert len(ComparisonReason) == 15


@pytest.mark.parametrize("kind", list(ComparisonKind))
@pytest.mark.parametrize("policy", list(ComparisonPolicy))
def test_definition_accepts_every_kind_and_policy(
    kind: ComparisonKind,
    policy: ComparisonPolicy,
) -> None:
    definition = replace(_definition(policy), kind=kind)

    assert definition.kind is kind
    assert definition.policy is policy
    assert calculate_comparison_definition_sha256(definition) == definition.comparison_sha256
    assert (
        ComparisonDefinition.from_mapping(MappingProxyType(definition.to_mapping())) == definition
    )


def test_definition_factory_sorts_ids_and_definition_is_frozen_slotted_and_sensitive() -> None:
    definition = _definition(assertion_ids=("ASSERTION-FOUND-001-B2", "ASSERTION-FOUND-001-A1"))

    assert definition.assertion_ids == (
        "ASSERTION-FOUND-001-A1",
        "ASSERTION-FOUND-001-B2",
    )
    assert (
        definition.comparison_sha256
        != replace(definition, allow_unpaired_results=True).comparison_sha256
    )
    assert not hasattr(definition, "__dict__")
    with pytest.raises(FrozenInstanceError):
        definition.policy = ComparisonPolicy.ACTUAL_EQUIVALENT  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("comparison_id", "bad", "stable uppercase"),
        ("scenario_id", 1, "scenario_id must be a string"),
        ("scenario_id", "SCENARIO", "AURORA-SCN"),
        ("baseline_run_id", 1, "must be a string"),
        ("candidate_run_id", "bad", "stable uppercase"),
        ("invariant_id", "bad", "stable uppercase"),
        ("invariant_class", "HARD", "InvariantClass"),
        ("severity", "S4", "AssertionSeverity"),
        ("kind", "VERSION", "ComparisonKind"),
        ("policy", "EXACT", "ComparisonPolicy"),
        ("assertion_ids", [], "tuple of strings"),
        ("assertion_ids", (1,), "tuple of strings"),
        ("assertion_ids", ("bad",), "stable uppercase"),
        (
            "assertion_ids",
            ("ASSERTION-FOUND-001-A1", "ASSERTION-FOUND-001-A1"),
            "duplicates",
        ),
        (
            "assertion_ids",
            ("ASSERTION-FOUND-001-B2", "ASSERTION-FOUND-001-A1"),
            "lexical order",
        ),
        ("minimum_paired_results", True, "must be an integer"),
        ("minimum_paired_results", 0, "must be positive"),
        ("minimum_paired_results", MAX_COMPARISON_PAIRS + 1, "must not exceed"),
        ("allow_unpaired_results", 1, "must be a boolean"),
    ],
)
def test_definition_rejects_invalid_field_contracts(
    field: str,
    value: object,
    message: str,
) -> None:
    with pytest.raises(ComparisonError, match=message):
        replace(_definition(), **{field: value})


def test_definition_rejects_same_run_and_factory_requires_tuple() -> None:
    with pytest.raises(ComparisonError, match="must differ"):
        replace(_definition(), candidate_run_id=_BASELINE_RUN_ID)
    with pytest.raises(ComparisonError, match="must be a tuple"):
        create_comparison_definition(  # type: ignore[arg-type]
            comparison_id="COMPARISON-FOUND-001-C1",
            scenario_id=_SCENARIO_ID,
            baseline_run_id=_BASELINE_RUN_ID,
            candidate_run_id=_CANDIDATE_RUN_ID,
            invariant_id="AURORA-COMPARISON-001",
            invariant_class=InvariantClass.HARD,
            severity=AssertionSeverity.S4,
            kind=ComparisonKind.REPEATABILITY,
            policy=ComparisonPolicy.EXACT,
            assertion_ids=[],
        )


def test_definition_enforces_assertion_id_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(comparison_module, "MAX_COMPARISON_ASSERTION_IDS", 1)
    with pytest.raises(ComparisonError, match="must not exceed"):
        replace(
            _definition(),
            assertion_ids=("ASSERTION-FOUND-001-A1", "ASSERTION-FOUND-001-B2"),
        )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("policy"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("comparison_schema_version", "2.0"),
        lambda data: data.__setitem__("comparison_type", "OTHER"),
        lambda data: data.__setitem__("comparison_sha256", "b" * 64),
        lambda data: data.__setitem__("kind", "INVALID"),
        lambda data: data.__setitem__("policy", 1),
        lambda data: data.__setitem__("assertion_ids", {}),
        lambda data: data.__setitem__("assertion_ids", [1]),
        lambda data: data.__setitem__("minimum_paired_results", True),
        lambda data: data.__setitem__("allow_unpaired_results", 1),
    ],
)
def test_definition_from_mapping_rejects_malformed_or_tampered_data(mutation: object) -> None:
    data = _definition().to_mapping()
    mutation(data)  # type: ignore[operator]

    with pytest.raises(ComparisonError):
        ComparisonDefinition.from_mapping(data)


def test_definition_parser_and_digest_helper_reject_wrong_types() -> None:
    with pytest.raises(ComparisonError, match="must be an object"):
        ComparisonDefinition.from_mapping([])  # type: ignore[arg-type]
    with pytest.raises(ComparisonError, match="keys must be strings"):
        ComparisonDefinition.from_mapping({1: "bad"})  # type: ignore[dict-item]
    with pytest.raises(ComparisonError, match="definition must"):
        calculate_comparison_definition_sha256(object())  # type: ignore[arg-type]


def test_comparison_key_round_trip_hash_and_frozen_contract() -> None:
    key = ComparisonKey(
        "ASSERTION-FOUND-001-A1",
        AssertionTargetKind.SNAPSHOT,
        EvidenceDomain.AURORA_STATE,
        "/escaped~1key/tilde~0key",
        2,
    )

    assert (
        key.key_sha256
        == hashlib.sha256(
            json.dumps(
                {
                    "assertion_id": key.assertion_id,
                    "occurrence": 2,
                    "path": key.path,
                    "target_domain": key.target_domain.value,
                    "target_kind": key.target_kind.value,
                },
                ensure_ascii=False,
                allow_nan=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
    )
    assert ComparisonKey.from_mapping(MappingProxyType(key.to_mapping())) == key
    assert not hasattr(key, "__dict__")
    with pytest.raises(FrozenInstanceError):
        key.path = "/other"  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("assertion_id", "bad", "stable uppercase"),
        ("target_kind", "SNAPSHOT", "AssertionTargetKind"),
        ("target_domain", "AURORA_STATE", "EvidenceDomain"),
        ("path", 1, "path must be a string"),
        ("path", "value", "RFC 6901"),
        ("occurrence", True, "must be an integer"),
        ("occurrence", -1, "non-negative"),
    ],
)
def test_comparison_key_rejects_invalid_fields(field: str, value: object, message: str) -> None:
    key = ComparisonKey(
        "ASSERTION-FOUND-001-A1",
        AssertionTargetKind.SNAPSHOT,
        EvidenceDomain.AURORA_STATE,
        "/value",
        0,
    )
    with pytest.raises(ComparisonError, match=message):
        replace(key, **{field: value})


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("path"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("key_sha256", "b" * 64),
        lambda data: data.__setitem__("target_kind", "INVALID"),
        lambda data: data.__setitem__("target_domain", 1),
        lambda data: data.__setitem__("path", []),
        lambda data: data.__setitem__("occurrence", True),
    ],
)
def test_comparison_key_from_mapping_rejects_tampering(mutation: object) -> None:
    data = _pair().key.to_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(ComparisonError):
        ComparisonKey.from_mapping(data)


def test_comparison_key_parser_requires_object() -> None:
    with pytest.raises(ComparisonError, match="must be an object"):
        ComparisonKey.from_mapping([])  # type: ignore[arg-type]


def test_comparison_key_accepts_null_path() -> None:
    key = replace(_pair().key, path=None)

    assert ComparisonKey.from_mapping(key.to_mapping()) == key


def test_operand_is_redacted_round_trippable_frozen_and_slotted() -> None:
    operand = _operand()
    data = operand.to_mapping()

    assert ComparisonOperand.from_mapping(MappingProxyType(data)) == operand
    assert data["actual_value_sha256"] == create_assertion_value("UNKNOWN").value_sha256
    assert "actual" not in data
    assert "UNKNOWN" not in json.dumps(data)
    assert not hasattr(operand, "__dict__")
    with pytest.raises(FrozenInstanceError):
        operand.status = AssertionStatus.FAIL  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("result_id", "bad", "stable uppercase"),
        ("result_sha256", 1, "must be a string"),
        ("result_sha256", "bad", "lowercase SHA-256"),
        ("assertion_id", "bad", "stable uppercase"),
        ("assertion_sha256", "bad", "lowercase SHA-256"),
        ("target_kind", "SNAPSHOT", "AssertionTargetKind"),
        ("target_domain", "AURORA_STATE", "EvidenceDomain"),
        ("target_id", "bad", "stable uppercase"),
        ("target_sha256", "bad", "lowercase SHA-256"),
        ("path", 1, "path must be a string"),
        ("path", "value", "RFC 6901"),
        ("invariant_id", "bad", "stable uppercase"),
        ("invariant_class", "HARD", "InvariantClass"),
        ("severity", "S4", "AssertionSeverity"),
        ("status", "PASS", "AssertionStatus"),
        ("reason", "VALUES_EQUAL", "AssertionReason"),
        ("actual_value_sha256", 1, "must be a string"),
        ("actual_value_sha256", "bad", "lowercase SHA-256"),
    ],
)
def test_operand_rejects_invalid_fields(field: str, value: object, message: str) -> None:
    with pytest.raises(ComparisonError, match=message):
        replace(_operand(), **{field: value})


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("status"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("result_id", 1),
        lambda data: data.__setitem__("result_sha256", "bad"),
        lambda data: data.__setitem__("assertion_id", 1),
        lambda data: data.__setitem__("assertion_sha256", 1),
        lambda data: data.__setitem__("target_kind", "INVALID"),
        lambda data: data.__setitem__("target_domain", "INVALID"),
        lambda data: data.__setitem__("target_id", 1),
        lambda data: data.__setitem__("target_sha256", 1),
        lambda data: data.__setitem__("path", []),
        lambda data: data.__setitem__("invariant_id", 1),
        lambda data: data.__setitem__("invariant_class", "INVALID"),
        lambda data: data.__setitem__("severity", "INVALID"),
        lambda data: data.__setitem__("status", "INVALID"),
        lambda data: data.__setitem__("reason", "INVALID"),
        lambda data: data.__setitem__("actual_value_sha256", []),
    ],
)
def test_operand_from_mapping_rejects_malformed_data(mutation: object) -> None:
    data = _operand().to_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(ComparisonError):
        ComparisonOperand.from_mapping(data)


def test_operand_parser_requires_object() -> None:
    with pytest.raises(ComparisonError, match="must be an object"):
        ComparisonOperand.from_mapping([])  # type: ignore[arg-type]


def test_operand_accepts_null_path_and_actual_digest() -> None:
    operand = replace(_operand(), path=None, actual_value_sha256=None)

    assert ComparisonOperand.from_mapping(operand.to_mapping()) == operand


def test_result_comparison_derives_all_paired_differences_in_canonical_order() -> None:
    baseline = _operand()
    candidate = replace(
        baseline,
        result_id="RESULT-FOUND-001-CAND",
        result_sha256="d" * 64,
        assertion_sha256="e" * 64,
        invariant_id="AURORA-INFO-002",
        invariant_class=InvariantClass.SOFT,
        severity=AssertionSeverity.S3,
        status=AssertionStatus.FAIL,
        reason=AssertionReason.VALUES_DIFFER,
        actual_value_sha256="f" * 64,
    )

    pair = _pair(baseline=baseline, candidate=candidate)

    assert pair.paired
    assert pair.changed
    assert pair.differences == (
        DifferenceKind.DEFINITION_CHANGED,
        DifferenceKind.STATUS_CHANGED,
        DifferenceKind.REASON_CHANGED,
        DifferenceKind.ACTUAL_CHANGED,
    )
    assert ResultComparison.from_mapping(MappingProxyType(pair.to_mapping())) == pair
    assert (
        pair.comparison_sha256
        == hashlib.sha256(
            comparison_module._canonical_json_bytes(pair._content_mapping())
        ).hexdigest()
    )


def test_result_comparison_represents_both_unpaired_directions() -> None:
    operand = _operand()
    missing_candidate = _pair(baseline=operand)
    missing_baseline = _pair(candidate=operand)

    assert not missing_candidate.paired
    assert missing_candidate.differences == (DifferenceKind.MISSING_CANDIDATE,)
    assert missing_baseline.differences == (DifferenceKind.MISSING_BASELINE,)
    assert ResultComparison.from_mapping(missing_candidate.to_mapping()) == missing_candidate
    assert ResultComparison.from_mapping(missing_baseline.to_mapping()) == missing_baseline


def test_identical_result_comparison_is_unchanged_frozen_and_slotted() -> None:
    pair = _pair()

    assert pair.paired
    assert not pair.changed
    assert pair.differences == ()
    assert not hasattr(pair, "__dict__")
    with pytest.raises(FrozenInstanceError):
        pair.differences = ()  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("key", object(), "key must"),
        ("baseline", object(), "baseline must"),
        ("candidate", object(), "candidate must"),
        ("differences", [], "tuple of DifferenceKind"),
        ("differences", ("ACTUAL_CHANGED",), "tuple of DifferenceKind"),
        (
            "differences",
            (DifferenceKind.ACTUAL_CHANGED, DifferenceKind.ACTUAL_CHANGED),
            "duplicates",
        ),
        (
            "differences",
            (DifferenceKind.ACTUAL_CHANGED, DifferenceKind.STATUS_CHANGED),
            "canonical order",
        ),
        ("differences", (DifferenceKind.ACTUAL_CHANGED,), "do not match"),
    ],
)
def test_result_comparison_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    with pytest.raises(ComparisonError, match=message):
        replace(_pair(), **{field: value})


def test_result_comparison_requires_operand_and_matching_key() -> None:
    pair = _pair()
    with pytest.raises(ComparisonError, match="at least one operand"):
        replace(pair, baseline=None, candidate=None, differences=())
    assert pair.baseline is not None
    with pytest.raises(ComparisonError, match="does not match comparison key"):
        replace(pair, baseline=replace(pair.baseline, assertion_id="ASSERTION-FOUND-001-B2"))


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("candidate"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("comparison_sha256", "b" * 64),
        lambda data: data.__setitem__("key", []),
        lambda data: data.__setitem__("baseline", []),
        lambda data: data.__setitem__("candidate", []),
        lambda data: data.__setitem__("differences", {}),
        lambda data: data.__setitem__("differences", ["INVALID"]),
    ],
)
def test_result_comparison_from_mapping_rejects_tampering(mutation: object) -> None:
    data = _pair().to_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(ComparisonError):
        ResultComparison.from_mapping(data)


def test_result_comparison_parser_requires_object() -> None:
    with pytest.raises(ComparisonError, match="must be an object"):
        ResultComparison.from_mapping([])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("policy", "baseline_actual", "candidate_actual", "status", "reason", "violations"),
    [
        (
            ComparisonPolicy.EXACT,
            "UNKNOWN",
            "UNKNOWN",
            ComparisonStatus.PASS,
            ComparisonReason.EXACT_MATCH,
            0,
        ),
        (
            ComparisonPolicy.EXACT,
            "UNKNOWN",
            "KNOWN",
            ComparisonStatus.FAIL,
            ComparisonReason.UNEXPECTED_DIVERGENCE,
            1,
        ),
        (
            ComparisonPolicy.ACTUAL_EQUIVALENT,
            "UNKNOWN",
            "UNKNOWN",
            ComparisonStatus.PASS,
            ComparisonReason.ACTUALS_EQUIVALENT,
            0,
        ),
        (
            ComparisonPolicy.ACTUAL_EQUIVALENT,
            "UNKNOWN",
            "KNOWN",
            ComparisonStatus.FAIL,
            ComparisonReason.UNEXPECTED_DIVERGENCE,
            1,
        ),
        (
            ComparisonPolicy.EXPECTED_DIVERGENCE,
            "UNKNOWN",
            "KNOWN",
            ComparisonStatus.PASS,
            ComparisonReason.EXPECTED_DIVERGENCE_OBSERVED,
            0,
        ),
        (
            ComparisonPolicy.EXPECTED_DIVERGENCE,
            "UNKNOWN",
            "UNKNOWN",
            ComparisonStatus.FAIL,
            ComparisonReason.REQUIRED_DIVERGENCE_NOT_OBSERVED,
            1,
        ),
    ],
)
def test_value_sensitive_policies(
    policy: ComparisonPolicy,
    baseline_actual: object,
    candidate_actual: object,
    status: ComparisonStatus,
    reason: ComparisonReason,
    violations: int,
) -> None:
    baseline, candidate = _inputs(
        baseline_actual=baseline_actual,
        candidate_actual=candidate_actual,
    )

    _, _, _, report = _report(policy, baseline=baseline, candidate=candidate)

    assert (report.status, report.reason, report.violation_count) == (status, reason, violations)


def test_outcome_equivalent_ignores_reason_and_actual_but_not_status() -> None:
    baseline, candidate = _inputs(
        baseline_actual="UNKNOWN",
        candidate_actual="KNOWN",
        candidate_reason=AssertionReason.VALUES_DIFFER,
    )
    _, _, _, equivalent = _report(
        ComparisonPolicy.OUTCOME_EQUIVALENT,
        baseline=baseline,
        candidate=candidate,
    )
    baseline, candidate = _inputs(candidate_status=AssertionStatus.FAIL)
    _, _, _, changed = _report(
        ComparisonPolicy.OUTCOME_EQUIVALENT,
        baseline=baseline,
        candidate=candidate,
    )

    assert (equivalent.status, equivalent.reason) == (
        ComparisonStatus.PASS,
        ComparisonReason.OUTCOMES_EQUIVALENT,
    )
    assert (changed.status, changed.reason, changed.violation_count) == (
        ComparisonStatus.FAIL,
        ComparisonReason.UNEXPECTED_DIVERGENCE,
        1,
    )


def test_actual_equivalent_ignores_outcome_when_actual_is_equal() -> None:
    baseline, candidate = _inputs(
        candidate_status=AssertionStatus.FAIL,
        candidate_reason=AssertionReason.VALUES_DIFFER,
    )
    _, _, _, report = _report(
        ComparisonPolicy.ACTUAL_EQUIVALENT,
        baseline=baseline,
        candidate=candidate,
    )

    assert report.status is ComparisonStatus.PASS
    assert report.reason is ComparisonReason.ACTUALS_EQUIVALENT


@pytest.mark.parametrize(
    ("baseline_status", "candidate_status", "expected_status", "expected_reason"),
    [
        (
            AssertionStatus.PASS,
            AssertionStatus.PASS,
            ComparisonStatus.PASS,
            ComparisonReason.NO_STATUS_REGRESSION,
        ),
        (
            AssertionStatus.PASS,
            AssertionStatus.REVIEW,
            ComparisonStatus.FAIL,
            ComparisonReason.STATUS_REGRESSION,
        ),
        (
            AssertionStatus.REVIEW,
            AssertionStatus.FAIL,
            ComparisonStatus.FAIL,
            ComparisonReason.STATUS_REGRESSION,
        ),
        (
            AssertionStatus.FAIL,
            AssertionStatus.PASS,
            ComparisonStatus.PASS,
            ComparisonReason.NO_STATUS_REGRESSION,
        ),
        (
            AssertionStatus.REVIEW,
            AssertionStatus.PASS,
            ComparisonStatus.PASS,
            ComparisonReason.NO_STATUS_REGRESSION,
        ),
    ],
)
def test_no_status_regression_uses_ordered_quality(
    baseline_status: AssertionStatus,
    candidate_status: AssertionStatus,
    expected_status: ComparisonStatus,
    expected_reason: ComparisonReason,
) -> None:
    baseline, candidate = _inputs(
        baseline_status=baseline_status,
        candidate_status=candidate_status,
    )

    _, _, _, report = _report(
        ComparisonPolicy.NO_STATUS_REGRESSION,
        baseline=baseline,
        candidate=candidate,
    )

    assert (report.status, report.reason) == (expected_status, expected_reason)


@pytest.mark.parametrize(
    (
        "policy",
        "baseline_value",
        "candidate_value",
        "expected_status",
        "expected_reason",
    ),
    [
        (
            ComparisonPolicy.ACTUAL_NON_INCREASING,
            10,
            9,
            ComparisonStatus.PASS,
            ComparisonReason.NUMERIC_RELATION_SATISFIED,
        ),
        (
            ComparisonPolicy.ACTUAL_NON_INCREASING,
            10,
            10.0,
            ComparisonStatus.PASS,
            ComparisonReason.NUMERIC_RELATION_SATISFIED,
        ),
        (
            ComparisonPolicy.ACTUAL_NON_INCREASING,
            10,
            11,
            ComparisonStatus.FAIL,
            ComparisonReason.NUMERIC_RELATION_VIOLATED,
        ),
        (
            ComparisonPolicy.ACTUAL_NON_DECREASING,
            10,
            11.5,
            ComparisonStatus.PASS,
            ComparisonReason.NUMERIC_RELATION_SATISFIED,
        ),
        (
            ComparisonPolicy.ACTUAL_NON_DECREASING,
            10,
            10,
            ComparisonStatus.PASS,
            ComparisonReason.NUMERIC_RELATION_SATISFIED,
        ),
        (
            ComparisonPolicy.ACTUAL_NON_DECREASING,
            10,
            9,
            ComparisonStatus.FAIL,
            ComparisonReason.NUMERIC_RELATION_VIOLATED,
        ),
    ],
)
def test_numeric_policies_apply_inclusive_metamorphic_relations(
    policy: ComparisonPolicy,
    baseline_value: object,
    candidate_value: object,
    expected_status: ComparisonStatus,
    expected_reason: ComparisonReason,
) -> None:
    baseline, candidate = _inputs(
        baseline_actual=baseline_value,
        candidate_actual=candidate_value,
    )

    _, _, _, report = _report(policy, baseline=baseline, candidate=candidate)

    assert (report.status, report.reason) == (expected_status, expected_reason)


@pytest.mark.parametrize(
    ("baseline_value", "candidate_value"),
    [
        (True, 1),
        (1, False),
        ("10", 10),
        (10, "10"),
        (_NO_ACTUAL, 10),
        (10, _NO_ACTUAL),
    ],
)
def test_numeric_policies_block_missing_boolean_and_non_numeric_actuals(
    baseline_value: object,
    candidate_value: object,
) -> None:
    baseline, candidate = _inputs(
        baseline_actual=baseline_value,
        candidate_actual=candidate_value,
    )

    _, _, _, report = _report(
        ComparisonPolicy.ACTUAL_NON_INCREASING,
        baseline=baseline,
        candidate=candidate,
    )

    assert (report.status, report.reason, report.violation_count) == (
        ComparisonStatus.BLOCKED,
        ComparisonReason.NON_NUMERIC_ACTUAL,
        1,
    )


@pytest.mark.parametrize("invariant_class", [InvariantClass.SOFT, InvariantClass.CONTEXTUAL])
@pytest.mark.parametrize(
    "policy",
    [
        ComparisonPolicy.EXACT,
        ComparisonPolicy.OUTCOME_EQUIVALENT,
        ComparisonPolicy.ACTUAL_EQUIVALENT,
        ComparisonPolicy.EXPECTED_DIVERGENCE,
        ComparisonPolicy.NO_STATUS_REGRESSION,
        ComparisonPolicy.ACTUAL_NON_INCREASING,
        ComparisonPolicy.ACTUAL_NON_DECREASING,
    ],
)
def test_non_hard_policy_violations_require_review(
    policy: ComparisonPolicy,
    invariant_class: InvariantClass,
) -> None:
    if policy is ComparisonPolicy.EXPECTED_DIVERGENCE:
        baseline_value, candidate_value = "SAME", "SAME"
        baseline_status, candidate_status = AssertionStatus.PASS, AssertionStatus.PASS
    elif policy is ComparisonPolicy.NO_STATUS_REGRESSION:
        baseline_value, candidate_value = "SAME", "SAME"
        baseline_status, candidate_status = AssertionStatus.PASS, AssertionStatus.FAIL
    elif policy is ComparisonPolicy.ACTUAL_NON_INCREASING:
        baseline_value, candidate_value = 1, 2
        baseline_status, candidate_status = AssertionStatus.PASS, AssertionStatus.PASS
    elif policy is ComparisonPolicy.ACTUAL_NON_DECREASING:
        baseline_value, candidate_value = 2, 1
        baseline_status, candidate_status = AssertionStatus.PASS, AssertionStatus.PASS
    else:
        baseline_value, candidate_value = "BASE", "CAND"
        baseline_status = AssertionStatus.PASS
        candidate_status = (
            AssertionStatus.FAIL
            if policy is ComparisonPolicy.OUTCOME_EQUIVALENT
            else AssertionStatus.PASS
        )
    baseline, candidate = _inputs(
        baseline_actual=baseline_value,
        candidate_actual=candidate_value,
        baseline_status=baseline_status,
        candidate_status=candidate_status,
        invariant_class=invariant_class,
    )

    _, _, _, report = _report(
        policy,
        invariant_class=invariant_class,
        baseline=baseline,
        candidate=candidate,
    )

    assert report.status is ComparisonStatus.REVIEW


@pytest.mark.parametrize("blocked_side", ["baseline", "candidate"])
def test_blocked_assertion_result_blocks_every_policy(blocked_side: str) -> None:
    options = {
        "baseline_status": AssertionStatus.BLOCKED
        if blocked_side == "baseline"
        else AssertionStatus.PASS,
        "candidate_status": AssertionStatus.BLOCKED
        if blocked_side == "candidate"
        else AssertionStatus.PASS,
    }
    baseline, candidate = _inputs(**options)

    _, _, _, report = _report(
        ComparisonPolicy.EXACT,
        baseline=baseline,
        candidate=candidate,
    )

    assert (report.status, report.reason, report.violation_count) == (
        ComparisonStatus.BLOCKED,
        ComparisonReason.BLOCKED_ASSERTION_RESULT,
        1,
    )


def test_definition_change_blocks_policy_evaluation() -> None:
    baseline, candidate = _inputs(candidate_definition_sha256="d" * 64)

    _, _, _, report = _report(
        ComparisonPolicy.EXACT,
        baseline=baseline,
        candidate=candidate,
    )

    assert (report.status, report.reason, report.violation_count) == (
        ComparisonStatus.BLOCKED,
        ComparisonReason.INCOMPATIBLE_ASSERTION_DEFINITION,
        1,
    )


def test_assertion_selection_ignores_unselected_results() -> None:
    baseline_selected = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE-A1",
    )
    candidate_selected = _result(
        _CANDIDATE_RUN_ID,
        result_id="RESULT-FOUND-001-CAND-A1",
    )
    baseline_extra = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE-B2",
        assertion_id="ASSERTION-FOUND-001-B2",
        actual="BASE-ONLY",
    )
    baseline = _series(_BASELINE_RUN_ID, baseline_selected, baseline_extra)
    candidate = _series(_CANDIDATE_RUN_ID, candidate_selected)

    _, _, _, report = _report(
        baseline=baseline,
        candidate=candidate,
        assertion_ids=("ASSERTION-FOUND-001-A1",),
    )

    assert report.status is ComparisonStatus.PASS
    assert report.pair_count == report.paired_result_count == 1
    assert report.pairs[0].key.assertion_id == "ASSERTION-FOUND-001-A1"


def test_repeated_semantic_results_pair_by_occurrence() -> None:
    baseline_results = tuple(
        _result(
            _BASELINE_RUN_ID,
            result_id=f"RESULT-FOUND-001-BASE-{index}",
            actual=index,
        )
        for index in range(2)
    )
    candidate_results = tuple(
        _result(
            _CANDIDATE_RUN_ID,
            result_id=f"RESULT-FOUND-001-CAND-{index}",
            actual=index,
        )
        for index in range(2)
    )

    _, _, _, report = _report(
        baseline=_series(_BASELINE_RUN_ID, *baseline_results),
        candidate=_series(_CANDIDATE_RUN_ID, *candidate_results),
        minimum_paired_results=2,
    )

    assert report.status is ComparisonStatus.PASS
    assert {pair.key.occurrence for pair in report.pairs} == {0, 1}


@pytest.mark.parametrize(
    ("baseline_present", "candidate_present", "expected_difference"),
    [
        (True, False, DifferenceKind.MISSING_CANDIDATE),
        (False, True, DifferenceKind.MISSING_BASELINE),
    ],
)
def test_unpaired_result_blocks_by_default(
    baseline_present: bool,
    candidate_present: bool,
    expected_difference: DifferenceKind,
) -> None:
    baseline_result = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE",
    )
    candidate_result = _result(
        _CANDIDATE_RUN_ID,
        result_id="RESULT-FOUND-001-CAND",
    )
    baseline = _series(_BASELINE_RUN_ID, *(baseline_result,) if baseline_present else ())
    candidate = _series(_CANDIDATE_RUN_ID, *(candidate_result,) if candidate_present else ())

    _, _, _, report = _report(baseline=baseline, candidate=candidate)

    assert (report.status, report.reason) == (
        ComparisonStatus.BLOCKED,
        ComparisonReason.INSUFFICIENT_PAIRED_RESULTS,
    )
    assert report.pairs[0].differences == (expected_difference,)


def test_incomplete_pairing_blocks_after_minimum_is_met() -> None:
    baseline_a = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE-A1",
    )
    baseline_b = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE-B2",
        assertion_id="ASSERTION-FOUND-001-B2",
    )
    candidate_a = _result(
        _CANDIDATE_RUN_ID,
        result_id="RESULT-FOUND-001-CAND-A1",
    )

    _, _, _, report = _report(
        baseline=_series(_BASELINE_RUN_ID, baseline_a, baseline_b),
        candidate=_series(_CANDIDATE_RUN_ID, candidate_a),
    )

    assert (report.status, report.reason, report.paired_result_count) == (
        ComparisonStatus.BLOCKED,
        ComparisonReason.INCOMPLETE_PAIRING,
        1,
    )
    assert report.violation_count == 1


def test_unpaired_results_can_be_allowed_after_minimum_is_met() -> None:
    baseline_a = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE-A1",
    )
    baseline_b = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE-B2",
        assertion_id="ASSERTION-FOUND-001-B2",
    )
    candidate_a = _result(
        _CANDIDATE_RUN_ID,
        result_id="RESULT-FOUND-001-CAND-A1",
    )

    _, _, _, report = _report(
        baseline=_series(_BASELINE_RUN_ID, baseline_a, baseline_b),
        candidate=_series(_CANDIDATE_RUN_ID, candidate_a),
        allow_unpaired_results=True,
    )

    assert (report.status, report.reason) == (
        ComparisonStatus.PASS,
        ComparisonReason.EXACT_MATCH,
    )
    assert (report.pair_count, report.paired_result_count, report.unpaired_result_count) == (
        2,
        1,
        1,
    )


def test_empty_selection_has_insufficient_paired_results() -> None:
    baseline, candidate = _inputs()

    _, _, _, report = _report(
        baseline=baseline,
        candidate=candidate,
        assertion_ids=("ASSERTION-FOUND-001-OTHER",),
    )

    assert (report.status, report.reason, report.pairs, report.violations) == (
        ComparisonStatus.BLOCKED,
        ComparisonReason.INSUFFICIENT_PAIRED_RESULTS,
        (),
        (),
    )


@pytest.mark.parametrize(
    ("field", "baseline_value", "candidate_value"),
    [
        ("path", "/baseline", "/candidate"),
        ("target_domain", EvidenceDomain.AURORA_STATE, EvidenceDomain.WORLD),
        ("target_kind", AssertionTargetKind.SNAPSHOT, AssertionTargetKind.TRANSITION),
    ],
)
def test_semantic_key_changes_create_two_unpaired_results(
    field: str,
    baseline_value: object,
    candidate_value: object,
) -> None:
    baseline_result = _result(
        _BASELINE_RUN_ID,
        result_id="RESULT-FOUND-001-BASE",
        **{field: baseline_value},  # type: ignore[arg-type]
    )
    candidate_result = _result(
        _CANDIDATE_RUN_ID,
        result_id="RESULT-FOUND-001-CAND",
        **{field: candidate_value},  # type: ignore[arg-type]
    )

    _, _, _, report = _report(
        baseline=_series(_BASELINE_RUN_ID, baseline_result),
        candidate=_series(_CANDIDATE_RUN_ID, candidate_result),
    )

    assert report.pair_count == report.unpaired_result_count == 2
    assert report.reason is ComparisonReason.INSUFFICIENT_PAIRED_RESULTS


def test_comparison_pair_bound_is_enforced(monkeypatch: pytest.MonkeyPatch) -> None:
    baseline, candidate = _inputs()
    definition = _definition()
    monkeypatch.setattr(comparison_module, "MAX_COMPARISON_PAIRS", 0)

    with pytest.raises(ComparisonError, match="must not exceed"):
        compare_assertion_series(
            definition,
            baseline,
            candidate,
            report_id="REPORT-FOUND-001-C1",
            evaluated_at_tick=20,
        )


def test_report_exposes_deterministic_counts_digests_and_redacted_evidence() -> None:
    baseline, candidate = _inputs(candidate_actual="KNOWN")
    definition, baseline, candidate, report = _report(
        baseline=baseline,
        candidate=candidate,
    )
    validator_data = report.to_validator_mapping()
    evidence_data = report.to_evidence_mapping()
    payload = create_comparison_evidence_payload(report)

    assert report.comparison_definition_sha256 == definition.comparison_sha256
    assert report.baseline_series_sha256 == baseline.series_sha256
    assert report.candidate_series_sha256 == candidate.series_sha256
    assert (report.pair_count, report.paired_result_count, report.unpaired_result_count) == (
        1,
        1,
        0,
    )
    assert (report.changed_pair_count, report.violation_count) == (1, 1)
    assert report.report_sha256 == calculate_comparison_report_sha256(report)
    assert validator_data["report_sha256"] == report.report_sha256
    assert evidence_data["violation_key_sha256"] == [report.violations[0].key_sha256]
    assert payload.decode() == evidence_data
    assert "pairs" not in evidence_data
    assert "violations" not in evidence_data
    assert "UNKNOWN" not in json.dumps(validator_data)
    assert "KNOWN" not in json.dumps(validator_data)


def test_report_round_trip_is_frozen_slotted_and_hash_sensitive() -> None:
    _, _, _, report = _report()

    assert ComparisonReport.from_mapping(MappingProxyType(report.to_validator_mapping())) == report
    assert report.report_sha256 != replace(report, evaluated_at_tick=21).report_sha256
    assert not hasattr(report, "__dict__")
    with pytest.raises(FrozenInstanceError):
        report.status = ComparisonStatus.FAIL  # type: ignore[misc]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("report_id", "bad", "stable uppercase"),
        ("comparison_id", "bad", "stable uppercase"),
        ("comparison_definition_sha256", 1, "must be a string"),
        ("comparison_definition_sha256", "bad", "lowercase SHA-256"),
        ("scenario_id", "SCENARIO", "AURORA-SCN"),
        ("baseline_run_id", "bad", "stable uppercase"),
        ("baseline_series_sha256", "bad", "lowercase SHA-256"),
        ("candidate_run_id", "bad", "stable uppercase"),
        ("candidate_series_sha256", "bad", "lowercase SHA-256"),
        ("evaluated_at_tick", True, "must be an integer"),
        ("evaluated_at_tick", -1, "between 0"),
        ("evaluated_at_tick", MAX_TICK + 1, "between 0"),
        ("invariant_id", "bad", "stable uppercase"),
        ("invariant_class", "HARD", "InvariantClass"),
        ("severity", "S4", "AssertionSeverity"),
        ("kind", "VERSION", "ComparisonKind"),
        ("policy", "EXACT", "ComparisonPolicy"),
        ("status", "PASS", "ComparisonStatus"),
        ("reason", "EXACT_MATCH", "ComparisonReason"),
        ("pairs", [], "tuple of ResultComparison"),
        ("pairs", (object(),), "tuple of ResultComparison"),
        ("violations", [], "tuple of ComparisonKey"),
        ("violations", (object(),), "tuple of ComparisonKey"),
    ],
)
def test_report_rejects_invalid_field_contracts(
    field: str,
    value: object,
    message: str,
) -> None:
    _, _, _, report = _report()
    with pytest.raises(ComparisonError, match=message):
        replace(report, **{field: value})


def test_report_rejects_same_run_pair_bound_duplicates_order_and_unknown_violations(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, _, _, report = _report()
    with pytest.raises(ComparisonError, match="must differ"):
        replace(report, candidate_run_id=report.baseline_run_id)

    monkeypatch.setattr(comparison_module, "MAX_COMPARISON_PAIRS", 0)
    with pytest.raises(ComparisonError, match="must not exceed"):
        replace(report)
    monkeypatch.setattr(comparison_module, "MAX_COMPARISON_PAIRS", MAX_COMPARISON_PAIRS)

    pair = report.pairs[0]
    with pytest.raises(ComparisonError, match="unique comparison keys"):
        replace(report, pairs=(pair, pair))
    second_pair = _pair(occurrence=1)
    sorted_pairs = tuple(sorted((pair, second_pair), key=lambda item: item.key.key_sha256))
    with pytest.raises(ComparisonError, match="ordered by key_sha256"):
        replace(report, pairs=tuple(reversed(sorted_pairs)))

    key = pair.key
    with pytest.raises(ComparisonError, match="unique comparison keys"):
        replace(report, violations=(key, key))
    second_key = second_pair.key
    sorted_keys = tuple(sorted((key, second_key), key=lambda item: item.key_sha256))
    with pytest.raises(ComparisonError, match="ordered by key_sha256"):
        replace(report, violations=tuple(reversed(sorted_keys)))
    unknown = replace(key, occurrence=99)
    with pytest.raises(ComparisonError, match="present in pairs"):
        replace(report, violations=(unknown,))


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("status"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("comparison_schema_version", "2.0"),
        lambda data: data.__setitem__("report_type", "OTHER"),
        lambda data: data.__setitem__("report_sha256", "b" * 64),
        lambda data: data.__setitem__("report_id", 1),
        lambda data: data.__setitem__("comparison_id", 1),
        lambda data: data.__setitem__("comparison_definition_sha256", 1),
        lambda data: data.__setitem__("scenario_id", 1),
        lambda data: data.__setitem__("baseline_run_id", 1),
        lambda data: data.__setitem__("baseline_series_sha256", 1),
        lambda data: data.__setitem__("candidate_run_id", 1),
        lambda data: data.__setitem__("candidate_series_sha256", 1),
        lambda data: data.__setitem__("evaluated_at_tick", True),
        lambda data: data.__setitem__("invariant_id", 1),
        lambda data: data.__setitem__("invariant_class", "INVALID"),
        lambda data: data.__setitem__("severity", "INVALID"),
        lambda data: data.__setitem__("kind", "INVALID"),
        lambda data: data.__setitem__("policy", "INVALID"),
        lambda data: data.__setitem__("status", "INVALID"),
        lambda data: data.__setitem__("reason", "INVALID"),
        lambda data: data.__setitem__("pairs", {}),
        lambda data: data.__setitem__("pairs", [[]]),
        lambda data: data.__setitem__("violations", {}),
        lambda data: data.__setitem__("violations", [[]]),
    ],
)
def test_report_from_mapping_rejects_malformed_or_tampered_data(mutation: object) -> None:
    _, _, _, report = _report()
    data = report.to_validator_mapping()
    mutation(data)  # type: ignore[operator]
    with pytest.raises(ComparisonError):
        ComparisonReport.from_mapping(data)


@pytest.mark.parametrize(
    "field",
    [
        "changed_pair_count",
        "pair_count",
        "paired_result_count",
        "unpaired_result_count",
        "violation_count",
    ],
)
def test_report_from_mapping_verifies_every_derived_count(field: str) -> None:
    _, _, _, report = _report()
    data = report.to_validator_mapping()
    data[field] = int(data[field]) + 1  # type: ignore[arg-type]

    with pytest.raises(ComparisonError, match=f"declared {field}"):
        ComparisonReport.from_mapping(data)


def test_report_from_mapping_requires_integer_counts() -> None:
    _, _, _, report = _report()
    data = report.to_validator_mapping()
    data["pair_count"] = True
    with pytest.raises(ComparisonError, match="must be an integer"):
        ComparisonReport.from_mapping(data)


def test_report_parser_and_helpers_reject_wrong_types() -> None:
    with pytest.raises(ComparisonError, match="must be an object"):
        ComparisonReport.from_mapping([])  # type: ignore[arg-type]
    with pytest.raises(ComparisonError, match="report must"):
        calculate_comparison_report_sha256(object())  # type: ignore[arg-type]
    with pytest.raises(ComparisonError, match="report must"):
        create_comparison_evidence_payload(object())  # type: ignore[arg-type]
    with pytest.raises(ComparisonError, match="report must"):
        validate_comparison_report(  # type: ignore[arg-type]
            object(), _definition(), *_inputs()
        )


def test_validate_comparison_report_accepts_exact_recomputation_and_rejects_change() -> None:
    definition, baseline, candidate, report = _report()

    validate_comparison_report(report, definition, baseline, candidate)
    with pytest.raises(ComparisonError, match="does not match"):
        validate_comparison_report(
            replace(
                report,
                status=ComparisonStatus.FAIL,
                reason=ComparisonReason.UNEXPECTED_DIVERGENCE,
            ),
            definition,
            baseline,
            candidate,
        )


@pytest.mark.parametrize(
    ("definition", "baseline", "candidate", "message"),
    [
        (object(), None, None, "definition must"),
        (None, object(), None, "baseline must"),
        (None, None, object(), "candidate must"),
    ],
)
def test_compare_rejects_wrong_input_types(
    definition: object,
    baseline: object,
    candidate: object,
    message: str,
) -> None:
    valid_definition = _definition()
    valid_baseline, valid_candidate = _inputs()
    with pytest.raises(ComparisonError, match=message):
        compare_assertion_series(
            valid_definition if definition is None else definition,  # type: ignore[arg-type]
            valid_baseline if baseline is None else baseline,  # type: ignore[arg-type]
            valid_candidate if candidate is None else candidate,  # type: ignore[arg-type]
            report_id="REPORT-FOUND-001-C1",
            evaluated_at_tick=20,
        )


@pytest.mark.parametrize(
    ("target", "message"),
    [
        ("baseline_scenario", "baseline scenario"),
        ("candidate_scenario", "candidate scenario"),
        ("baseline_run", "baseline run"),
        ("candidate_run", "candidate run"),
    ],
)
def test_compare_rejects_identity_mismatch(target: str, message: str) -> None:
    definition = _definition()
    baseline, candidate = _inputs()
    if target == "baseline_scenario":
        baseline = replace(baseline, scenario_id="AURORA-SCN-FOUND-002", results=())
    elif target == "candidate_scenario":
        candidate = replace(candidate, scenario_id="AURORA-SCN-FOUND-002", results=())
    elif target == "baseline_run":
        baseline = replace(baseline, run_id="AURORA-RUN-FOUND-001-OTHER", results=())
    else:
        candidate = replace(candidate, run_id="AURORA-RUN-FOUND-001-OTHER", results=())

    with pytest.raises(ComparisonError, match=message):
        compare_assertion_series(
            definition,
            baseline,
            candidate,
            report_id="REPORT-FOUND-001-C1",
            evaluated_at_tick=20,
        )


@pytest.mark.parametrize(
    ("report_id", "tick", "message"),
    [
        ("bad", 20, "stable uppercase"),
        ("REPORT-FOUND-001-C1", True, "must be an integer"),
        ("REPORT-FOUND-001-C1", -1, "between 0"),
        ("REPORT-FOUND-001-C1", MAX_TICK + 1, "between 0"),
    ],
)
def test_compare_rejects_invalid_report_identity_and_tick(
    report_id: str,
    tick: int,
    message: str,
) -> None:
    baseline, candidate = _inputs()
    with pytest.raises(ComparisonError, match=message):
        compare_assertion_series(
            _definition(),
            baseline,
            candidate,
            report_id=report_id,
            evaluated_at_tick=tick,
        )


def test_private_defensive_branches_reject_impossible_or_non_json_inputs() -> None:
    definition, _, _, report = _report(ComparisonPolicy.ACTUAL_NON_INCREASING)
    pair = report.pairs[0]
    with pytest.raises(ComparisonError, match="missing raw assertion results"):
        comparison_module._evaluate_numeric_policy(
            definition,
            (pair,),
            {pair.key.key_sha256: (None, None)},
        )
    with pytest.raises(ComparisonError, match="canonical finite JSON"):
        comparison_module._canonical_json_bytes(object())


def test_private_status_regression_guard_handles_unpaired_and_blocked_operands() -> None:
    unpaired = _pair(baseline=_operand())
    assert not comparison_module._is_status_regression(unpaired)

    baseline = _operand(status=AssertionStatus.BLOCKED)
    candidate = replace(
        baseline,
        result_id="RESULT-FOUND-001-CAND",
        result_sha256="d" * 64,
        status=AssertionStatus.FAIL,
    )
    blocked = _pair(baseline=baseline, candidate=candidate)
    assert not comparison_module._is_status_regression(blocked)


def test_canonical_json_helper_rejects_non_finite_float() -> None:
    with pytest.raises(ComparisonError, match="canonical finite JSON"):
        comparison_module._canonical_json_bytes({"value": float("nan")})


def test_serialized_mappings_are_detached_from_immutable_models() -> None:
    definition, _, _, report = _report()
    definition_data = definition.to_mapping()
    report_data = report.to_validator_mapping()

    definition_data["assertion_ids"] = ["ASSERTION-FOUND-001-OTHER"]
    report_data["pairs"] = []

    assert definition.assertion_ids == ()
    assert report.pair_count == 1
    assert copy.deepcopy(report.to_validator_mapping()) == report.to_validator_mapping()
