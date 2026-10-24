"""Unit tests for deterministic semantic Aurora assertions."""

from __future__ import annotations

import hashlib
import json
from dataclasses import FrozenInstanceError, replace
from types import MappingProxyType

import pytest

from aurora_validation_harness import assertions as assertions_module
from aurora_validation_harness.assertions import (
    DEFAULT_MAX_ASSERTION_VALUE_BYTES,
    MAX_ASSERTION_ALLOWED_VALUES,
    MAX_ASSERTION_RESULTS,
    MAX_ASSERTION_VALUE_BYTES,
    MAX_TICK,
    SUPPORTED_ASSERTION_SCHEMA_VERSION,
    AssertionReason,
    AssertionResult,
    AssertionSeries,
    AssertionSeverity,
    AssertionStatus,
    AssertionTargetKind,
    AssertionValue,
    AssertionValueType,
    InvariantClass,
    PathMatchMode,
    SnapshotAssertion,
    SnapshotAssertionOperator,
    TransitionAssertion,
    TransitionAssertionOperator,
    append_snapshot_assertion_result,
    append_transition_assertion_result,
    calculate_assertion_result_sha256,
    calculate_assertion_series_sha256,
    create_assertion_evidence_payload,
    create_assertion_series,
    create_assertion_source,
    create_assertion_value,
    create_snapshot_assertion,
    create_transition_assertion,
    evaluate_snapshot_assertion,
    evaluate_transition_assertion,
    validate_assertion_result,
)
from aurora_validation_harness.assertions import (
    AssertionError as AuroraAssertionError,
)
from aurora_validation_harness.evidence import (
    EvidenceDomain,
    EvidenceKind,
    EvidenceSource,
    EvidenceSourceKind,
    append_evidence_record,
    create_evidence_ledger,
)
from aurora_validation_harness.snapshots import (
    SnapshotPhase,
    StateSnapshot,
    append_state_snapshot,
    create_snapshot_series,
    create_snapshot_state,
)
from aurora_validation_harness.transitions import (
    ChangeOperation,
    StateTransition,
    TransitionStatus,
    create_state_transition,
)

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_RUN_ID = "AURORA-RUN-FOUND-001-001"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"
_UNSET = object()


def _source(
    *,
    kind: EvidenceSourceKind = EvidenceSourceKind.EVENT,
    source_id: str = "EVENT-FOUND-001-E1",
    digest: str = "a" * 64,
) -> EvidenceSource:
    return EvidenceSource(kind, source_id, digest)


def _snapshot(
    data: dict[str, object] | None = None,
    *,
    snapshot_id: str = "SNAPSHOT-FOUND-001-000",
    run_id: str = _RUN_ID,
    scenario_id: str = _SCENARIO_ID,
    tick: int = 10,
    domain: EvidenceDomain = EvidenceDomain.AURORA_STATE,
) -> StateSnapshot:
    state = {
        "belief": {"location": "UNKNOWN", "confidence": 0.25},
        "nullable": None,
        "flags": [True, False],
        "escaped/key": {"tilde~key": "VISIBLE"},
    }
    series = create_snapshot_series(run_id, scenario_id)
    series = append_state_snapshot(
        series,
        snapshot_id=snapshot_id,
        captured_at_tick=tick,
        phase=SnapshotPhase.INITIAL,
        domain=domain,
        subject_id="AURORA",
        producer_id="HARNESS-RUNTIME",
        checkpoint_id=None,
        state=create_snapshot_state(state if data is None else data),
    )
    return series.snapshots[0]


def _snapshot_pair(
    *,
    before_data: dict[str, object] | None = None,
    after_data: dict[str, object] | None = None,
    run_id: str = _RUN_ID,
    scenario_id: str = _SCENARIO_ID,
    before_tick: int = 0,
    after_tick: int = 10,
) -> tuple[StateSnapshot, StateSnapshot]:
    before = (
        {"belief": {"location": "UNKNOWN", "confidence": 0.25}, "stable": True}
        if before_data is None
        else before_data
    )
    after = (
        {
            "belief": {"location": "CARGO-7", "confidence": 0.8},
            "stable": True,
            "new": "OBSERVED",
        }
        if after_data is None
        else after_data
    )
    series = create_snapshot_series(run_id, scenario_id)
    series = append_state_snapshot(
        series,
        snapshot_id="SNAPSHOT-FOUND-001-000",
        captured_at_tick=before_tick,
        phase=SnapshotPhase.INITIAL,
        domain=EvidenceDomain.AURORA_STATE,
        subject_id="AURORA",
        producer_id="HARNESS-RUNTIME",
        checkpoint_id=None,
        state=create_snapshot_state(before),
    )
    series = append_state_snapshot(
        series,
        snapshot_id="SNAPSHOT-FOUND-001-001",
        captured_at_tick=after_tick,
        phase=SnapshotPhase.CHECKPOINT,
        domain=EvidenceDomain.AURORA_STATE,
        subject_id="AURORA",
        producer_id="HARNESS-RUNTIME",
        checkpoint_id="CP1",
        state=create_snapshot_state(after),
    )
    return series.snapshots[0], series.snapshots[1]


def _transition(
    *,
    changed: bool = True,
    causes: tuple[EvidenceSource, ...] = (),
    before_data: dict[str, object] | None = None,
    after_data: dict[str, object] | None = None,
    run_id: str = _RUN_ID,
    scenario_id: str = _SCENARIO_ID,
) -> StateTransition:
    if not changed:
        before_data = {"belief": "UNKNOWN", "stable": True}
        after_data = {"belief": "UNKNOWN", "stable": True}
    before, after = _snapshot_pair(
        before_data=before_data,
        after_data=after_data,
        run_id=run_id,
        scenario_id=scenario_id,
    )
    return create_state_transition(
        before,
        after,
        transition_id="TRANSITION-FOUND-001-000",
        sequence=0,
        causes=causes,
    )


def _snapshot_assertion(
    operator: SnapshotAssertionOperator = SnapshotAssertionOperator.EXISTS,
    *,
    assertion_id: str = "ASSERTION-FOUND-001-A1",
    invariant_class: InvariantClass = InvariantClass.HARD,
    path: str = "/belief",
    expected: object = _UNSET,
    expected_type: AssertionValueType | None = None,
    minimum: int | float | None = None,
    maximum: int | float | None = None,
    minimum_inclusive: bool = True,
    maximum_inclusive: bool = True,
    allowed_values: tuple[object, ...] = (),
) -> SnapshotAssertion:
    kwargs: dict[str, object] = {}
    if expected is not _UNSET:
        kwargs["expected"] = expected
    return create_snapshot_assertion(
        assertion_id=assertion_id,
        invariant_id="AURORA-INFO-001",
        invariant_class=invariant_class,
        severity=AssertionSeverity.S4,
        operator=operator,
        path=path,
        expected_type=expected_type,
        minimum=minimum,
        maximum=maximum,
        minimum_inclusive=minimum_inclusive,
        maximum_inclusive=maximum_inclusive,
        allowed_values=allowed_values,
        **kwargs,
    )


def _transition_assertion(
    operator: TransitionAssertionOperator = TransitionAssertionOperator.PATH_CHANGED,
    *,
    assertion_id: str = "ASSERTION-FOUND-001-T1",
    invariant_class: InvariantClass = InvariantClass.HARD,
    path: str | None = "/belief/location",
    match_mode: PathMatchMode = PathMatchMode.EXACT,
    expected_operation: ChangeOperation | None = None,
    expected_status: TransitionStatus | None = None,
    required_cause_kind: EvidenceSourceKind | None = None,
) -> TransitionAssertion:
    return create_transition_assertion(
        assertion_id=assertion_id,
        invariant_id="AURORA-INFO-001",
        invariant_class=invariant_class,
        severity=AssertionSeverity.S4,
        operator=operator,
        path=path,
        match_mode=match_mode,
        expected_operation=expected_operation,
        expected_status=expected_status,
        required_cause_kind=required_cause_kind,
    )


def _result(
    *,
    result_id: str = "RESULT-FOUND-001-000",
    invariant_class: InvariantClass = InvariantClass.HARD,
) -> AssertionResult:
    assertion = _snapshot_assertion(invariant_class=invariant_class)
    return evaluate_snapshot_assertion(assertion, _snapshot(), result_id=result_id)


def test_public_constants_define_schema_and_bounded_limits() -> None:
    assert SUPPORTED_ASSERTION_SCHEMA_VERSION == "1.0"
    assert DEFAULT_MAX_ASSERTION_VALUE_BYTES == 1_048_576
    assert MAX_ASSERTION_VALUE_BYTES == 16_777_216
    assert MAX_ASSERTION_ALLOWED_VALUES == 4_096
    assert MAX_ASSERTION_RESULTS == 1_000_000
    assert MAX_TICK == (1 << 63) - 1
    assert 0 < DEFAULT_MAX_ASSERTION_VALUE_BYTES < MAX_ASSERTION_VALUE_BYTES < MAX_TICK


def test_assertion_enums_have_stable_contract_values() -> None:
    assert {item.value for item in AssertionSeverity} == {"S1", "S2", "S3", "S4"}
    assert {item.value for item in InvariantClass} == {"HARD", "SOFT", "CONTEXTUAL"}
    assert {item.value for item in AssertionStatus} == {"PASS", "FAIL", "REVIEW", "BLOCKED"}
    assert {item.value for item in AssertionTargetKind} == {"SNAPSHOT", "TRANSITION"}
    assert {item.value for item in PathMatchMode} == {"EXACT", "SUBTREE"}
    assert {item.value for item in SnapshotAssertionOperator} == {
        "EXISTS",
        "ABSENT",
        "EQUALS",
        "NOT_EQUALS",
        "TYPE_IS",
        "NUMBER_RANGE",
        "ONE_OF",
    }
    assert {item.value for item in TransitionAssertionOperator} == {
        "PATH_CHANGED",
        "PATH_UNCHANGED",
        "OPERATION_IS",
        "STATUS_IS",
        "CHANGES_HAVE_CAUSE",
        "CHANGES_HAVE_CAUSE_KIND",
    }


@pytest.mark.parametrize(
    "data",
    [
        None,
        "Cargo_Bay_7",
        True,
        42,
        2.5,
        ["alpha", 2, False, None],
        {"confidence": 0.75, "locations": ["Docking_Ring", "Cargo_Bay_7"]},
    ],
)
def test_assertion_value_accepts_every_supported_json_shape(data: object) -> None:
    value = create_assertion_value(data)

    assert value.decode() == data
    assert value.size_bytes == len(value.value_json)
    assert value.value_sha256 == hashlib.sha256(value.value_json).hexdigest()
    assert value.to_mapping() == {"data": data, "value_sha256": value.value_sha256}


def test_assertion_value_canonicalizes_generic_mapping_unicode_and_tuples() -> None:
    data = MappingProxyType({"z": "ö", "a": MappingProxyType({"β": (2, 1)})})

    value = create_assertion_value(data)

    assert value.value_json == '{"a":{"β":[2,1]},"z":"ö"}'.encode()
    assert value.decode() == {"a": {"β": [2, 1]}, "z": "ö"}


def test_assertion_value_detaches_input_and_returns_fresh_decodes() -> None:
    data: dict[str, object] = {"belief": {"value": "UNKNOWN"}, "history": ["T0"]}
    value = create_assertion_value(data)
    original_hash = value.value_sha256

    nested = data["belief"]
    assert isinstance(nested, dict)
    nested["value"] = "KNOWN"
    decoded = value.decode()
    assert isinstance(decoded, dict)
    decoded["belief"] = "tampered"

    assert value.decode() == {"belief": {"value": "UNKNOWN"}, "history": ["T0"]}
    assert value.value_sha256 == original_hash


def test_assertion_values_preserve_exact_json_number_representation() -> None:
    assert create_assertion_value(1).value_sha256 != create_assertion_value(1.0).value_sha256


def test_assertion_value_is_frozen_and_slotted() -> None:
    value = create_assertion_value("UNKNOWN")

    with pytest.raises(FrozenInstanceError):
        value.value_sha256 = "b" * 64  # type: ignore[misc]
    with pytest.raises((AttributeError, TypeError)):
        value.extra = True  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    ("value_json", "digest", "message"),
    [
        ("{}", "a" * 64, "value_json must be bytes"),
        (b"{}", 7, "value_sha256 must be a string"),
        (b"{}", "A" * 64, "lowercase SHA-256"),
        (b"{}", "a" * 64, "does not match value_json"),
        (b"\xff", None, "valid finite UTF-8 JSON"),
        (b"{", None, "valid finite UTF-8 JSON"),
        (b"NaN", None, "valid finite UTF-8 JSON"),
        (b'{"z":1,"a":2}', None, "canonical JSON encoding"),
    ],
)
def test_assertion_value_rejects_invalid_raw_contract(
    value_json: object,
    digest: object | None,
    message: str,
) -> None:
    raw = value_json
    resolved_digest = (
        hashlib.sha256(raw).hexdigest() if isinstance(raw, bytes) and digest is None else digest
    )
    with pytest.raises(AuroraAssertionError, match=message):
        AssertionValue(value_json=raw, value_sha256=resolved_digest)  # type: ignore[arg-type]


def test_assertion_value_rejects_raw_value_over_absolute_limit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    payload = b'"abc"'
    monkeypatch.setattr(assertions_module, "MAX_ASSERTION_VALUE_BYTES", len(payload) - 1)

    with pytest.raises(AuroraAssertionError, match="value_json must not exceed"):
        AssertionValue(payload, hashlib.sha256(payload).hexdigest())


@pytest.mark.parametrize("data", [{1: "bad"}, {"bad": {1, 2}}, object(), float("inf")])
def test_create_assertion_value_rejects_non_json_data(data: object) -> None:
    with pytest.raises(AuroraAssertionError):
        create_assertion_value(data)


@pytest.mark.parametrize("limit", [True, 1.5, 0, MAX_ASSERTION_VALUE_BYTES + 1])
def test_create_assertion_value_rejects_invalid_size_limit(limit: object) -> None:
    with pytest.raises(AuroraAssertionError, match="max_value_bytes"):
        create_assertion_value("x", max_value_bytes=limit)  # type: ignore[arg-type]


def test_create_assertion_value_enforces_caller_size_limit() -> None:
    with pytest.raises(AuroraAssertionError, match="must not exceed 3 bytes"):
        create_assertion_value("abcd", max_value_bytes=3)


def test_assertion_value_round_trip_accepts_generic_mapping() -> None:
    value = create_assertion_value({"belief": "UNKNOWN"})

    restored = AssertionValue.from_mapping(MappingProxyType(value.to_mapping()))

    assert restored == value


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("data"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("value_sha256", "b" * 64),
        lambda data: data.__setitem__("value_sha256", 1),
    ],
)
def test_assertion_value_from_mapping_rejects_malformed_or_tampered_data(mutation: object) -> None:
    data = create_assertion_value("UNKNOWN").to_mapping()
    mutation(data)  # type: ignore[operator]

    with pytest.raises(AuroraAssertionError):
        AssertionValue.from_mapping(data)


def test_assertion_value_from_mapping_requires_an_object() -> None:
    with pytest.raises(AuroraAssertionError, match="assertion value must be an object"):
        AssertionValue.from_mapping([])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "assertion",
    [
        _snapshot_assertion(SnapshotAssertionOperator.EXISTS),
        _snapshot_assertion(SnapshotAssertionOperator.ABSENT, path="/missing"),
        _snapshot_assertion(SnapshotAssertionOperator.EQUALS, expected=None, path="/nullable"),
        _snapshot_assertion(SnapshotAssertionOperator.NOT_EQUALS, expected="KNOWN"),
        _snapshot_assertion(
            SnapshotAssertionOperator.TYPE_IS,
            expected_type=AssertionValueType.OBJECT,
        ),
        _snapshot_assertion(
            SnapshotAssertionOperator.NUMBER_RANGE,
            path="/belief/confidence",
            minimum=0.0,
            maximum=1.0,
        ),
        _snapshot_assertion(
            SnapshotAssertionOperator.ONE_OF,
            path="/belief/location",
            allowed_values=("KNOWN", "UNKNOWN"),
        ),
    ],
)
def test_snapshot_assertion_supports_each_operator_and_round_trips(
    assertion: SnapshotAssertion,
) -> None:
    restored = SnapshotAssertion.from_mapping(MappingProxyType(assertion.to_mapping()))

    assert restored == assertion
    assert restored.assertion_sha256 == assertion.assertion_sha256
    assert restored.to_mapping()["assertion_type"] == "SNAPSHOT_ASSERTION"


def test_snapshot_assertion_distinguishes_expected_json_null_from_no_expected_value() -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.EQUALS,
        path="/nullable",
        expected=None,
    )

    assert assertion.expected is not None
    assert assertion.expected.decode() is None


def test_snapshot_assertion_sorts_allowed_values_by_digest() -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.ONE_OF,
        allowed_values=("z", "a", "m"),
    )

    hashes = tuple(item.value_sha256 for item in assertion.allowed_values)
    assert hashes == tuple(sorted(hashes))


def test_snapshot_assertion_is_frozen_and_digest_is_content_sensitive() -> None:
    assertion = _snapshot_assertion()
    changed = _snapshot_assertion(path="/nullable")

    with pytest.raises(FrozenInstanceError):
        assertion.path = "/changed"  # type: ignore[misc]
    assert assertion.assertion_sha256 != changed.assertion_sha256


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("assertion_id", "bad", "stable uppercase"),
        ("invariant_id", "bad", "stable uppercase"),
        ("invariant_class", "HARD", "InvariantClass"),
        ("severity", "S4", "AssertionSeverity"),
        ("operator", "EXISTS", "SnapshotAssertionOperator"),
        ("path", "belief", "RFC 6901"),
        ("expected", "UNKNOWN", "AssertionValue"),
        ("expected_type", "STRING", "AssertionValueType"),
        ("minimum", True, "number"),
        ("maximum", float("inf"), "finite"),
        ("minimum_inclusive", 1, "boolean"),
        ("maximum_inclusive", 1, "boolean"),
        ("allowed_values", [], "tuple"),
    ],
)
def test_snapshot_assertion_rejects_invalid_field_contracts(
    field: str,
    value: object,
    message: str,
) -> None:
    assertion = _snapshot_assertion()

    with pytest.raises(AuroraAssertionError, match=message):
        replace(assertion, **{field: value})


def test_snapshot_assertion_rejects_too_many_allowed_values(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    values = tuple(sorted((create_assertion_value("a"),), key=lambda item: item.value_sha256))
    monkeypatch.setattr(assertions_module, "MAX_ASSERTION_ALLOWED_VALUES", 0)

    with pytest.raises(AuroraAssertionError, match="allowed_values must not exceed"):
        replace(
            _snapshot_assertion(
                SnapshotAssertionOperator.ONE_OF,
                allowed_values=("a",),
            ),
            allowed_values=values,
        )


def test_snapshot_assertion_rejects_duplicate_and_unsorted_allowed_values() -> None:
    one = create_assertion_value("one")
    two = create_assertion_value("two")

    with pytest.raises(AuroraAssertionError, match="duplicate"):
        replace(
            _snapshot_assertion(SnapshotAssertionOperator.ONE_OF, allowed_values=("one",)),
            allowed_values=(one, one),
        )
    ordered = tuple(sorted((one, two), key=lambda item: item.value_sha256))
    with pytest.raises(AuroraAssertionError, match="ordered"):
        replace(
            _snapshot_assertion(SnapshotAssertionOperator.ONE_OF, allowed_values=("one",)),
            allowed_values=tuple(reversed(ordered)),
        )


@pytest.mark.parametrize(
    "changes",
    [
        {"expected": create_assertion_value("x")},
        {"expected_type": AssertionValueType.STRING},
        {"minimum": 0},
        {"allowed_values": (create_assertion_value("x"),)},
        {"minimum_inclusive": False},
    ],
)
@pytest.mark.parametrize(
    "operator", [SnapshotAssertionOperator.EXISTS, SnapshotAssertionOperator.ABSENT]
)
def test_presence_operators_reject_value_constraints(
    operator: SnapshotAssertionOperator,
    changes: dict[str, object],
) -> None:
    with pytest.raises(AuroraAssertionError, match="does not accept value constraints"):
        replace(_snapshot_assertion(operator), **changes)


@pytest.mark.parametrize(
    "changes",
    [
        {"expected": None},
        {"expected_type": AssertionValueType.STRING},
        {"minimum": 0},
        {"allowed_values": (create_assertion_value("x"),)},
        {"maximum_inclusive": False},
    ],
)
@pytest.mark.parametrize(
    "operator", [SnapshotAssertionOperator.EQUALS, SnapshotAssertionOperator.NOT_EQUALS]
)
def test_equality_operators_require_only_expected(
    operator: SnapshotAssertionOperator,
    changes: dict[str, object],
) -> None:
    assertion = _snapshot_assertion(operator, expected="UNKNOWN")

    with pytest.raises(AuroraAssertionError, match="requires only one expected value"):
        replace(assertion, **changes)


@pytest.mark.parametrize(
    "changes",
    [
        {"expected_type": None},
        {"expected": create_assertion_value("x")},
        {"minimum": 0},
        {"allowed_values": (create_assertion_value("x"),)},
        {"minimum_inclusive": False},
    ],
)
def test_type_operator_requires_only_expected_type(changes: dict[str, object]) -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.TYPE_IS,
        expected_type=AssertionValueType.OBJECT,
    )

    with pytest.raises(AuroraAssertionError, match="TYPE_IS requires only expected_type"):
        replace(assertion, **changes)


@pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"minimum": None}, "at least one numeric bound"),
        ({"expected": create_assertion_value(0)}, "at least one numeric bound"),
        ({"expected_type": AssertionValueType.NUMBER}, "at least one numeric bound"),
        ({"allowed_values": (create_assertion_value(0),)}, "at least one numeric bound"),
        ({"minimum": 2, "maximum": 1}, "minimum must not exceed maximum"),
        (
            {"minimum": 1, "maximum": 1, "minimum_inclusive": False},
            "equal bounds must both be inclusive",
        ),
        ({"minimum": None, "maximum": 1, "minimum_inclusive": False}, "requires a minimum"),
        ({"minimum": 0, "maximum": None, "maximum_inclusive": False}, "requires a maximum"),
    ],
)
def test_range_operator_rejects_invalid_constraint_combinations(
    changes: dict[str, object],
    message: str,
) -> None:
    assertion = _snapshot_assertion(SnapshotAssertionOperator.NUMBER_RANGE, minimum=0)

    with pytest.raises(AuroraAssertionError, match=message):
        replace(assertion, **changes)


@pytest.mark.parametrize(
    "changes",
    [
        {"allowed_values": ()},
        {"expected": create_assertion_value("x")},
        {"expected_type": AssertionValueType.STRING},
        {"minimum": 0},
        {"minimum_inclusive": False},
    ],
)
def test_one_of_operator_requires_only_allowed_values(changes: dict[str, object]) -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.ONE_OF,
        allowed_values=("UNKNOWN",),
    )

    with pytest.raises(AuroraAssertionError, match="ONE_OF requires only"):
        replace(assertion, **changes)


def test_snapshot_assertion_factory_validates_allowed_values_tuple_and_size_limit() -> None:
    with pytest.raises(AuroraAssertionError, match="allowed_values must be a tuple"):
        create_snapshot_assertion(
            assertion_id="ASSERTION-FOUND-001-A1",
            invariant_id="AURORA-INFO-001",
            invariant_class=InvariantClass.HARD,
            severity=AssertionSeverity.S4,
            operator=SnapshotAssertionOperator.ONE_OF,
            path="/belief",
            allowed_values=["UNKNOWN"],  # type: ignore[arg-type]
        )
    with pytest.raises(AuroraAssertionError, match="max_value_bytes"):
        create_snapshot_assertion(
            assertion_id="ASSERTION-FOUND-001-A1",
            invariant_id="AURORA-INFO-001",
            invariant_class=InvariantClass.HARD,
            severity=AssertionSeverity.S4,
            operator=SnapshotAssertionOperator.EXISTS,
            path="/belief",
            max_value_bytes=0,
        )
    with pytest.raises(AuroraAssertionError, match="must not exceed 3 bytes"):
        create_snapshot_assertion(
            assertion_id="ASSERTION-FOUND-001-A1",
            invariant_id="AURORA-INFO-001",
            invariant_class=InvariantClass.HARD,
            severity=AssertionSeverity.S4,
            operator=SnapshotAssertionOperator.EQUALS,
            path="/belief",
            expected="large",
            max_value_bytes=3,
        )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("path"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("assertion_schema_version", "2.0"),
        lambda data: data.__setitem__("assertion_type", "TRANSITION_ASSERTION"),
        lambda data: data.__setitem__("assertion_sha256", "b" * 64),
        lambda data: data.__setitem__("invariant_class", "INVALID"),
        lambda data: data.__setitem__("severity", "S5"),
        lambda data: data.__setitem__("operator", "INVALID"),
        lambda data: data.__setitem__("minimum_inclusive", 1),
        lambda data: data.__setitem__("minimum", "zero"),
        lambda data: data.__setitem__("allowed_values", {}),
    ],
)
def test_snapshot_assertion_from_mapping_rejects_tampering(mutation: object) -> None:
    data = _snapshot_assertion().to_mapping()
    mutation(data)  # type: ignore[operator]

    with pytest.raises(AuroraAssertionError):
        SnapshotAssertion.from_mapping(data)


def test_snapshot_assertion_from_mapping_requires_an_object() -> None:
    with pytest.raises(AuroraAssertionError, match="snapshot assertion must be an object"):
        SnapshotAssertion.from_mapping([])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "assertion",
    [
        _transition_assertion(TransitionAssertionOperator.PATH_CHANGED),
        _transition_assertion(TransitionAssertionOperator.PATH_UNCHANGED),
        _transition_assertion(
            TransitionAssertionOperator.OPERATION_IS,
            expected_operation=ChangeOperation.REPLACED,
        ),
        _transition_assertion(
            TransitionAssertionOperator.STATUS_IS,
            path=None,
            expected_status=TransitionStatus.CHANGED,
        ),
        _transition_assertion(TransitionAssertionOperator.CHANGES_HAVE_CAUSE, path=None),
        _transition_assertion(
            TransitionAssertionOperator.CHANGES_HAVE_CAUSE_KIND,
            path=None,
            required_cause_kind=EvidenceSourceKind.EVENT,
        ),
    ],
)
def test_transition_assertion_supports_each_operator_and_round_trips(
    assertion: TransitionAssertion,
) -> None:
    restored = TransitionAssertion.from_mapping(MappingProxyType(assertion.to_mapping()))

    assert restored == assertion
    assert restored.assertion_sha256 == assertion.assertion_sha256
    assert restored.to_mapping()["assertion_type"] == "TRANSITION_ASSERTION"


def test_transition_assertion_is_frozen_and_digest_is_content_sensitive() -> None:
    assertion = _transition_assertion()
    changed = _transition_assertion(match_mode=PathMatchMode.SUBTREE)

    with pytest.raises(FrozenInstanceError):
        assertion.path = "/changed"  # type: ignore[misc]
    assert assertion.assertion_sha256 != changed.assertion_sha256


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("assertion_id", "bad", "stable uppercase"),
        ("invariant_id", "bad", "stable uppercase"),
        ("invariant_class", "HARD", "InvariantClass"),
        ("severity", "S4", "AssertionSeverity"),
        ("operator", "PATH_CHANGED", "TransitionAssertionOperator"),
        ("path", "belief", "RFC 6901"),
        ("match_mode", "EXACT", "PathMatchMode"),
        ("expected_operation", "REPLACED", "ChangeOperation"),
        ("expected_status", "CHANGED", "TransitionStatus"),
        ("required_cause_kind", "EVENT", "EvidenceSourceKind"),
    ],
)
def test_transition_assertion_rejects_invalid_field_contracts(
    field: str,
    value: object,
    message: str,
) -> None:
    assertion = _transition_assertion()

    with pytest.raises(AuroraAssertionError, match=message):
        replace(assertion, **{field: value})


@pytest.mark.parametrize(
    "operator",
    [
        TransitionAssertionOperator.PATH_CHANGED,
        TransitionAssertionOperator.PATH_UNCHANGED,
        TransitionAssertionOperator.OPERATION_IS,
    ],
)
def test_transition_path_operators_require_path(operator: TransitionAssertionOperator) -> None:
    kwargs: dict[str, object] = {}
    if operator is TransitionAssertionOperator.OPERATION_IS:
        kwargs["expected_operation"] = ChangeOperation.REPLACED

    with pytest.raises(AuroraAssertionError, match="requires path"):
        _transition_assertion(operator, path=None, **kwargs)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "operator",
    [
        TransitionAssertionOperator.STATUS_IS,
        TransitionAssertionOperator.CHANGES_HAVE_CAUSE,
        TransitionAssertionOperator.CHANGES_HAVE_CAUSE_KIND,
    ],
)
def test_transition_non_path_operators_reject_path_matching(
    operator: TransitionAssertionOperator,
) -> None:
    kwargs: dict[str, object] = {}
    if operator is TransitionAssertionOperator.STATUS_IS:
        kwargs["expected_status"] = TransitionStatus.CHANGED
    elif operator is TransitionAssertionOperator.CHANGES_HAVE_CAUSE_KIND:
        kwargs["required_cause_kind"] = EvidenceSourceKind.EVENT

    with pytest.raises(AuroraAssertionError, match="does not accept path matching"):
        _transition_assertion(operator, path="/belief", **kwargs)  # type: ignore[arg-type]
    with pytest.raises(AuroraAssertionError, match="does not accept path matching"):
        _transition_assertion(
            operator,
            path=None,
            match_mode=PathMatchMode.SUBTREE,
            **kwargs,  # type: ignore[arg-type]
        )


def test_transition_operation_operator_requires_and_owns_expected_operation() -> None:
    with pytest.raises(AuroraAssertionError, match="requires expected_operation"):
        _transition_assertion(TransitionAssertionOperator.OPERATION_IS)
    with pytest.raises(AuroraAssertionError, match="does not accept expected_operation"):
        _transition_assertion(
            TransitionAssertionOperator.PATH_CHANGED,
            expected_operation=ChangeOperation.REPLACED,
        )


def test_transition_status_operator_requires_and_owns_expected_status() -> None:
    with pytest.raises(AuroraAssertionError, match="requires expected_status"):
        _transition_assertion(TransitionAssertionOperator.STATUS_IS, path=None)
    with pytest.raises(AuroraAssertionError, match="does not accept expected_status"):
        _transition_assertion(
            TransitionAssertionOperator.PATH_CHANGED,
            expected_status=TransitionStatus.CHANGED,
        )


def test_transition_cause_kind_operator_requires_and_owns_cause_kind() -> None:
    with pytest.raises(AuroraAssertionError, match="requires required_cause_kind"):
        _transition_assertion(TransitionAssertionOperator.CHANGES_HAVE_CAUSE_KIND, path=None)
    with pytest.raises(AuroraAssertionError, match="does not accept required_cause_kind"):
        _transition_assertion(
            TransitionAssertionOperator.PATH_CHANGED,
            required_cause_kind=EvidenceSourceKind.EVENT,
        )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("path"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("assertion_schema_version", "2.0"),
        lambda data: data.__setitem__("assertion_type", "SNAPSHOT_ASSERTION"),
        lambda data: data.__setitem__("assertion_sha256", "b" * 64),
        lambda data: data.__setitem__("match_mode", "INVALID"),
        lambda data: data.__setitem__("expected_operation", "INVALID"),
        lambda data: data.__setitem__("expected_status", "INVALID"),
        lambda data: data.__setitem__("required_cause_kind", "INVALID"),
    ],
)
def test_transition_assertion_from_mapping_rejects_tampering(mutation: object) -> None:
    data = _transition_assertion().to_mapping()
    mutation(data)  # type: ignore[operator]

    with pytest.raises(AuroraAssertionError):
        TransitionAssertion.from_mapping(data)


def test_transition_assertion_from_mapping_requires_an_object() -> None:
    with pytest.raises(AuroraAssertionError, match="transition assertion must be an object"):
        TransitionAssertion.from_mapping([])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("operator", "path", "expected_status", "expected_reason"),
    [
        (
            SnapshotAssertionOperator.EXISTS,
            "/nullable",
            AssertionStatus.PASS,
            AssertionReason.PATH_FOUND,
        ),
        (
            SnapshotAssertionOperator.EXISTS,
            "/missing",
            AssertionStatus.FAIL,
            AssertionReason.PATH_NOT_FOUND,
        ),
        (
            SnapshotAssertionOperator.ABSENT,
            "/missing",
            AssertionStatus.PASS,
            AssertionReason.PATH_NOT_FOUND,
        ),
        (
            SnapshotAssertionOperator.ABSENT,
            "/nullable",
            AssertionStatus.FAIL,
            AssertionReason.PATH_FOUND,
        ),
    ],
)
def test_snapshot_presence_operators_distinguish_null_from_missing(
    operator: SnapshotAssertionOperator,
    path: str,
    expected_status: AssertionStatus,
    expected_reason: AssertionReason,
) -> None:
    result = evaluate_snapshot_assertion(
        _snapshot_assertion(operator, path=path),
        _snapshot(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is expected_status
    assert result.reason is expected_reason
    assert (result.actual is None) is (path == "/missing")


@pytest.mark.parametrize(
    ("invariant_class", "status"),
    [
        (InvariantClass.HARD, AssertionStatus.FAIL),
        (InvariantClass.SOFT, AssertionStatus.REVIEW),
        (InvariantClass.CONTEXTUAL, AssertionStatus.REVIEW),
    ],
)
def test_failed_condition_maps_invariant_class_to_outcome(
    invariant_class: InvariantClass,
    status: AssertionStatus,
) -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.EQUALS,
        path="/belief/location",
        expected="KNOWN",
        invariant_class=invariant_class,
    )

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is AssertionReason.VALUES_DIFFER


@pytest.mark.parametrize(
    ("operator", "expected", "status", "reason"),
    [
        (
            SnapshotAssertionOperator.EQUALS,
            "UNKNOWN",
            AssertionStatus.PASS,
            AssertionReason.VALUES_EQUAL,
        ),
        (
            SnapshotAssertionOperator.EQUALS,
            "KNOWN",
            AssertionStatus.FAIL,
            AssertionReason.VALUES_DIFFER,
        ),
        (
            SnapshotAssertionOperator.NOT_EQUALS,
            "KNOWN",
            AssertionStatus.PASS,
            AssertionReason.VALUES_DIFFER,
        ),
        (
            SnapshotAssertionOperator.NOT_EQUALS,
            "UNKNOWN",
            AssertionStatus.FAIL,
            AssertionReason.VALUES_EQUAL,
        ),
    ],
)
def test_snapshot_equality_operators_are_exact_and_reasoned(
    operator: SnapshotAssertionOperator,
    expected: object,
    status: AssertionStatus,
    reason: AssertionReason,
) -> None:
    assertion = _snapshot_assertion(
        operator,
        path="/belief/location",
        expected=expected,
    )

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason
    assert result.actual is not None
    assert result.actual.decode() == "UNKNOWN"


def test_snapshot_equality_preserves_integer_vs_float_representation() -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.EQUALS,
        path="/number",
        expected=1.0,
    )

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot({"number": 1}),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is AssertionStatus.FAIL
    assert result.reason is AssertionReason.VALUES_DIFFER


@pytest.mark.parametrize(
    ("value", "expected_type", "status"),
    [
        (None, AssertionValueType.NULL, AssertionStatus.PASS),
        (True, AssertionValueType.BOOLEAN, AssertionStatus.PASS),
        (1, AssertionValueType.INTEGER, AssertionStatus.PASS),
        (1, AssertionValueType.NUMBER, AssertionStatus.PASS),
        (1.5, AssertionValueType.NUMBER, AssertionStatus.PASS),
        ("x", AssertionValueType.STRING, AssertionStatus.PASS),
        ([1], AssertionValueType.ARRAY, AssertionStatus.PASS),
        ({"x": 1}, AssertionValueType.OBJECT, AssertionStatus.PASS),
        (True, AssertionValueType.NUMBER, AssertionStatus.FAIL),
        (1.5, AssertionValueType.INTEGER, AssertionStatus.FAIL),
    ],
)
def test_snapshot_type_assertion_classifies_json_values(
    value: object,
    expected_type: AssertionValueType,
    status: AssertionStatus,
) -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.TYPE_IS,
        path="/value",
        expected_type=expected_type,
    )

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot({"value": value}),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is (
        AssertionReason.TYPE_MATCH
        if status is AssertionStatus.PASS
        else AssertionReason.TYPE_MISMATCH
    )


@pytest.mark.parametrize(
    (
        "value",
        "minimum",
        "maximum",
        "minimum_inclusive",
        "maximum_inclusive",
        "status",
        "reason",
    ),
    [
        (0.5, 0.0, 1.0, True, True, AssertionStatus.PASS, AssertionReason.VALUE_IN_RANGE),
        (0.0, 0.0, 1.0, True, True, AssertionStatus.PASS, AssertionReason.VALUE_IN_RANGE),
        (1.0, 0.0, 1.0, True, True, AssertionStatus.PASS, AssertionReason.VALUE_IN_RANGE),
        (0.0, 0.0, 1.0, False, True, AssertionStatus.FAIL, AssertionReason.VALUE_OUT_OF_RANGE),
        (1.0, 0.0, 1.0, True, False, AssertionStatus.FAIL, AssertionReason.VALUE_OUT_OF_RANGE),
        (-0.1, 0.0, None, True, True, AssertionStatus.FAIL, AssertionReason.VALUE_OUT_OF_RANGE),
        (1.1, None, 1.0, True, True, AssertionStatus.FAIL, AssertionReason.VALUE_OUT_OF_RANGE),
        (True, 0.0, 1.0, True, True, AssertionStatus.FAIL, AssertionReason.TYPE_MISMATCH),
        ("0.5", 0.0, 1.0, True, True, AssertionStatus.FAIL, AssertionReason.TYPE_MISMATCH),
    ],
)
def test_snapshot_number_range_handles_bounds_and_type_failures(
    value: object,
    minimum: int | float | None,
    maximum: int | float | None,
    minimum_inclusive: bool,
    maximum_inclusive: bool,
    status: AssertionStatus,
    reason: AssertionReason,
) -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.NUMBER_RANGE,
        path="/value",
        minimum=minimum,
        maximum=maximum,
        minimum_inclusive=minimum_inclusive,
        maximum_inclusive=maximum_inclusive,
    )

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot({"value": value}),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason


@pytest.mark.parametrize(
    ("value", "status", "reason"),
    [
        ("UNKNOWN", AssertionStatus.PASS, AssertionReason.VALUE_ALLOWED),
        ("KNOWN", AssertionStatus.PASS, AssertionReason.VALUE_ALLOWED),
        ("INFERRED", AssertionStatus.FAIL, AssertionReason.VALUE_NOT_ALLOWED),
    ],
)
def test_snapshot_one_of_uses_canonical_allowed_values(
    value: object,
    status: AssertionStatus,
    reason: AssertionReason,
) -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.ONE_OF,
        path="/value",
        allowed_values=("UNKNOWN", "KNOWN"),
    )

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot({"value": value}),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason


@pytest.mark.parametrize(
    "operator_kwargs",
    [
        {
            "operator": SnapshotAssertionOperator.EQUALS,
            "expected": "UNKNOWN",
        },
        {
            "operator": SnapshotAssertionOperator.NOT_EQUALS,
            "expected": "UNKNOWN",
        },
        {
            "operator": SnapshotAssertionOperator.TYPE_IS,
            "expected_type": AssertionValueType.STRING,
        },
        {
            "operator": SnapshotAssertionOperator.NUMBER_RANGE,
            "minimum": 0,
        },
        {
            "operator": SnapshotAssertionOperator.ONE_OF,
            "allowed_values": ("UNKNOWN",),
        },
    ],
)
def test_value_operators_are_blocked_when_required_path_is_missing(
    operator_kwargs: dict[str, object],
) -> None:
    operator = operator_kwargs.pop("operator")
    assert isinstance(operator, SnapshotAssertionOperator)
    assertion = _snapshot_assertion(operator, path="/missing", **operator_kwargs)  # type: ignore[arg-type]

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is AssertionStatus.BLOCKED
    assert result.reason is AssertionReason.PATH_NOT_FOUND
    assert result.actual is None


@pytest.mark.parametrize(
    ("path", "status", "actual"),
    [
        ("/escaped~1key/tilde~0key", AssertionStatus.PASS, "VISIBLE"),
        ("/flags/0", AssertionStatus.PASS, True),
        ("/flags/01", AssertionStatus.FAIL, None),
        ("/flags/not-an-index", AssertionStatus.FAIL, None),
        ("/flags/9", AssertionStatus.FAIL, None),
        ("/nullable/child", AssertionStatus.FAIL, None),
    ],
)
def test_json_pointer_resolution_supports_escaping_arrays_and_missing_paths(
    path: str,
    status: AssertionStatus,
    actual: object,
) -> None:
    result = evaluate_snapshot_assertion(
        _snapshot_assertion(SnapshotAssertionOperator.EXISTS, path=path),
        _snapshot(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    if actual is None:
        assert result.actual is None
    else:
        assert result.actual is not None
        assert result.actual.decode() == actual


def test_snapshot_evaluation_binds_definition_target_and_explicit_tick() -> None:
    assertion = _snapshot_assertion()
    snapshot = _snapshot(tick=12, domain=EvidenceDomain.AURORA_STATE)

    result = evaluate_snapshot_assertion(
        assertion,
        snapshot,
        result_id="RESULT-FOUND-001-000",
        evaluated_at_tick=15,
    )

    assert result.run_id == snapshot.run_id
    assert result.scenario_id == snapshot.scenario_id
    assert result.evaluated_at_tick == 15
    assert result.assertion_sha256 == assertion.assertion_sha256
    assert result.target_kind is AssertionTargetKind.SNAPSHOT
    assert result.target_id == snapshot.snapshot_id
    assert result.target_sha256 == snapshot.snapshot_sha256
    assert result.target_domain is EvidenceDomain.AURORA_STATE


@pytest.mark.parametrize(
    ("assertion", "snapshot", "tick"),
    [
        (object(), _snapshot(), None),
        (_snapshot_assertion(), object(), None),
        (_snapshot_assertion(), _snapshot(), -1),
    ],
)
def test_snapshot_evaluation_rejects_invalid_inputs(
    assertion: object,
    snapshot: object,
    tick: int | None,
) -> None:
    kwargs = {} if tick is None else {"evaluated_at_tick": tick}
    with pytest.raises(AuroraAssertionError):
        evaluate_snapshot_assertion(  # type: ignore[arg-type]
            assertion,
            snapshot,
            result_id="RESULT-FOUND-001-000",
            **kwargs,
        )


@pytest.mark.parametrize(
    ("expected", "status", "reason"),
    [
        (TransitionStatus.CHANGED, AssertionStatus.PASS, AssertionReason.STATUS_MATCH),
        (TransitionStatus.UNCHANGED, AssertionStatus.FAIL, AssertionReason.STATUS_MISMATCH),
    ],
)
def test_transition_status_assertion_reports_match_and_mismatch(
    expected: TransitionStatus,
    status: AssertionStatus,
    reason: AssertionReason,
) -> None:
    assertion = _transition_assertion(
        TransitionAssertionOperator.STATUS_IS,
        path=None,
        expected_status=expected,
    )

    result = evaluate_transition_assertion(
        assertion,
        _transition(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason
    assert result.actual is not None
    assert result.actual.decode() == TransitionStatus.CHANGED.value


@pytest.mark.parametrize(
    ("changed", "causes", "status", "reason", "actual_count"),
    [
        (True, (), AssertionStatus.FAIL, AssertionReason.CAUSE_MISSING, 0),
        (True, (_source(),), AssertionStatus.PASS, AssertionReason.CAUSE_PRESENT, 1),
        (False, (), AssertionStatus.PASS, AssertionReason.CAUSE_PRESENT, 0),
    ],
)
def test_transition_changes_have_cause_is_vacuously_true_for_unchanged_state(
    changed: bool,
    causes: tuple[EvidenceSource, ...],
    status: AssertionStatus,
    reason: AssertionReason,
    actual_count: int,
) -> None:
    assertion = _transition_assertion(
        TransitionAssertionOperator.CHANGES_HAVE_CAUSE,
        path=None,
    )

    result = evaluate_transition_assertion(
        assertion,
        _transition(changed=changed, causes=causes),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason
    assert result.actual is not None
    assert result.actual.decode() == actual_count


@pytest.mark.parametrize(
    ("changed", "causes", "required", "status", "reason", "actual_kinds"),
    [
        (
            True,
            (_source(kind=EvidenceSourceKind.EVENT),),
            EvidenceSourceKind.EVENT,
            AssertionStatus.PASS,
            AssertionReason.CAUSE_KIND_PRESENT,
            ["EVENT"],
        ),
        (
            True,
            (_source(kind=EvidenceSourceKind.EVENT),),
            EvidenceSourceKind.CHANNEL_PACKET,
            AssertionStatus.FAIL,
            AssertionReason.CAUSE_KIND_MISSING,
            ["EVENT"],
        ),
        (
            False,
            (),
            EvidenceSourceKind.EVENT,
            AssertionStatus.PASS,
            AssertionReason.CAUSE_KIND_PRESENT,
            [],
        ),
    ],
)
def test_transition_cause_kind_assertion_is_provenance_aware(
    changed: bool,
    causes: tuple[EvidenceSource, ...],
    required: EvidenceSourceKind,
    status: AssertionStatus,
    reason: AssertionReason,
    actual_kinds: list[str],
) -> None:
    assertion = _transition_assertion(
        TransitionAssertionOperator.CHANGES_HAVE_CAUSE_KIND,
        path=None,
        required_cause_kind=required,
    )

    result = evaluate_transition_assertion(
        assertion,
        _transition(changed=changed, causes=causes),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason
    assert result.actual is not None
    assert result.actual.decode() == actual_kinds


@pytest.mark.parametrize(
    ("operator", "path", "mode", "status", "reason", "matched_paths"),
    [
        (
            TransitionAssertionOperator.PATH_CHANGED,
            "/belief/location",
            PathMatchMode.EXACT,
            AssertionStatus.PASS,
            AssertionReason.PATH_CHANGED,
            ["/belief/location"],
        ),
        (
            TransitionAssertionOperator.PATH_CHANGED,
            "/belief",
            PathMatchMode.EXACT,
            AssertionStatus.FAIL,
            AssertionReason.PATH_UNCHANGED,
            [],
        ),
        (
            TransitionAssertionOperator.PATH_CHANGED,
            "/belief",
            PathMatchMode.SUBTREE,
            AssertionStatus.PASS,
            AssertionReason.PATH_CHANGED,
            ["/belief/confidence", "/belief/location"],
        ),
        (
            TransitionAssertionOperator.PATH_UNCHANGED,
            "/stable",
            PathMatchMode.EXACT,
            AssertionStatus.PASS,
            AssertionReason.PATH_UNCHANGED,
            [],
        ),
        (
            TransitionAssertionOperator.PATH_UNCHANGED,
            "/belief",
            PathMatchMode.SUBTREE,
            AssertionStatus.FAIL,
            AssertionReason.PATH_CHANGED,
            ["/belief/confidence", "/belief/location"],
        ),
        (
            TransitionAssertionOperator.PATH_CHANGED,
            "/bel",
            PathMatchMode.SUBTREE,
            AssertionStatus.FAIL,
            AssertionReason.PATH_UNCHANGED,
            [],
        ),
    ],
)
def test_transition_path_assertions_support_exact_and_subtree_matching(
    operator: TransitionAssertionOperator,
    path: str,
    mode: PathMatchMode,
    status: AssertionStatus,
    reason: AssertionReason,
    matched_paths: list[str],
) -> None:
    assertion = _transition_assertion(operator, path=path, match_mode=mode)

    result = evaluate_transition_assertion(
        assertion,
        _transition(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason
    assert result.actual is not None
    assert result.actual.decode() == matched_paths


@pytest.mark.parametrize(
    ("path", "mode", "operation", "status", "reason", "actual"),
    [
        (
            "/belief/location",
            PathMatchMode.EXACT,
            ChangeOperation.REPLACED,
            AssertionStatus.PASS,
            AssertionReason.OPERATION_MATCH,
            ["REPLACED"],
        ),
        (
            "/new",
            PathMatchMode.EXACT,
            ChangeOperation.REPLACED,
            AssertionStatus.FAIL,
            AssertionReason.OPERATION_MISMATCH,
            ["ADDED"],
        ),
        (
            "/belief",
            PathMatchMode.SUBTREE,
            ChangeOperation.REPLACED,
            AssertionStatus.PASS,
            AssertionReason.OPERATION_MATCH,
            ["REPLACED", "REPLACED"],
        ),
        (
            "/missing",
            PathMatchMode.EXACT,
            ChangeOperation.REPLACED,
            AssertionStatus.BLOCKED,
            AssertionReason.PATH_NOT_FOUND,
            None,
        ),
    ],
)
def test_transition_operation_assertion_checks_all_matching_changes(
    path: str,
    mode: PathMatchMode,
    operation: ChangeOperation,
    status: AssertionStatus,
    reason: AssertionReason,
    actual: list[str] | None,
) -> None:
    assertion = _transition_assertion(
        TransitionAssertionOperator.OPERATION_IS,
        path=path,
        match_mode=mode,
        expected_operation=operation,
    )

    result = evaluate_transition_assertion(
        assertion,
        _transition(),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is status
    assert result.reason is reason
    if actual is None:
        assert result.actual is None
    else:
        assert result.actual is not None
        assert result.actual.decode() == actual


def test_transition_evaluation_binds_definition_target_and_default_tick() -> None:
    assertion = _transition_assertion()
    transition = _transition(causes=(_source(),))

    result = evaluate_transition_assertion(
        assertion,
        transition,
        result_id="RESULT-FOUND-001-000",
    )

    assert result.evaluated_at_tick == transition.after_tick
    assert result.assertion_id == assertion.assertion_id
    assert result.assertion_sha256 == assertion.assertion_sha256
    assert result.target_kind is AssertionTargetKind.TRANSITION
    assert result.target_id == transition.transition_id
    assert result.target_sha256 == transition.transition_sha256
    assert result.target_domain is transition.domain


@pytest.mark.parametrize(
    ("assertion", "transition", "tick"),
    [
        (object(), _transition(), None),
        (_transition_assertion(), object(), None),
        (_transition_assertion(), _transition(), MAX_TICK + 1),
    ],
)
def test_transition_evaluation_rejects_invalid_inputs(
    assertion: object,
    transition: object,
    tick: int | None,
) -> None:
    kwargs = {} if tick is None else {"evaluated_at_tick": tick}
    with pytest.raises(AuroraAssertionError):
        evaluate_transition_assertion(  # type: ignore[arg-type]
            assertion,
            transition,
            result_id="RESULT-FOUND-001-000",
            **kwargs,
        )


def test_assertion_result_is_frozen_hashed_and_has_compact_evidence_mapping() -> None:
    result = _result()
    validator_mapping = result.to_validator_mapping()
    evidence_mapping = result.to_evidence_mapping()

    with pytest.raises(FrozenInstanceError):
        result.status = AssertionStatus.FAIL  # type: ignore[misc]
    assert (
        result.result_sha256
        == hashlib.sha256(
            json.dumps(
                {key: value for key, value in validator_mapping.items() if key != "result_sha256"},
                ensure_ascii=False,
                allow_nan=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
    )
    assert validator_mapping["actual"] is not None
    assert "actual" not in evidence_mapping
    assert "actual_value_sha256" in evidence_mapping
    assert calculate_assertion_result_sha256(result) == result.result_sha256


def test_assertion_result_round_trips_from_generic_mapping() -> None:
    result = _result()

    restored = AssertionResult.from_mapping(MappingProxyType(result.to_validator_mapping()))

    assert restored == result
    assert restored.result_sha256 == result.result_sha256


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("result_id", "bad", "stable uppercase"),
        ("run_id", "bad", "stable uppercase"),
        ("scenario_id", "BAD", "scenario_id"),
        ("sequence", True, "integer"),
        ("sequence", -1, "non-negative"),
        ("evaluated_at_tick", -1, "between"),
        ("assertion_id", "bad", "stable uppercase"),
        ("assertion_sha256", "A" * 64, "lowercase SHA-256"),
        ("invariant_id", "bad", "stable uppercase"),
        ("invariant_class", "HARD", "InvariantClass"),
        ("severity", "S4", "AssertionSeverity"),
        ("target_kind", "SNAPSHOT", "AssertionTargetKind"),
        ("target_id", "bad", "stable uppercase"),
        ("target_sha256", "bad", "lowercase SHA-256"),
        ("target_domain", "AURORA_STATE", "EvidenceDomain"),
        ("status", "PASS", "AssertionStatus"),
        ("reason", "PATH_FOUND", "AssertionReason"),
        ("path", "belief", "RFC 6901"),
        ("actual", "UNKNOWN", "AssertionValue"),
        ("previous_result_sha256", "bad", "lowercase SHA-256"),
    ],
)
def test_assertion_result_rejects_invalid_field_contracts(
    field: str,
    value: object,
    message: str,
) -> None:
    result = _result()

    with pytest.raises(AuroraAssertionError, match=message):
        replace(result, **{field: value})


def test_assertion_result_enforces_chain_position_contract() -> None:
    first = _result()

    with pytest.raises(AuroraAssertionError, match="first assertion result"):
        replace(first, previous_result_sha256="b" * 64)
    with pytest.raises(AuroraAssertionError, match="non-first assertion result"):
        replace(first, sequence=1)
    chained = replace(first, sequence=1, previous_result_sha256="b" * 64)
    assert chained.sequence == 1


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("status"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("assertion_schema_version", "2.0"),
        lambda data: data.__setitem__("result_type", "OTHER"),
        lambda data: data.__setitem__("result_sha256", "b" * 64),
        lambda data: data.__setitem__("target_kind", "INVALID"),
        lambda data: data.__setitem__("actual", []),
        lambda data: data.__setitem__("previous_result_sha256", 1),
    ],
)
def test_assertion_result_from_mapping_rejects_tampering(mutation: object) -> None:
    data = _result().to_validator_mapping()
    mutation(data)  # type: ignore[operator]

    with pytest.raises(AuroraAssertionError):
        AssertionResult.from_mapping(data)


def test_assertion_result_from_mapping_requires_an_object() -> None:
    with pytest.raises(AuroraAssertionError, match="assertion result must be an object"):
        AssertionResult.from_mapping([])  # type: ignore[arg-type]


def test_validate_assertion_result_accepts_exact_snapshot_and_transition_linkage() -> None:
    snapshot = _snapshot()
    snapshot_assertion = _snapshot_assertion()
    snapshot_result = evaluate_snapshot_assertion(
        snapshot_assertion,
        snapshot,
        result_id="RESULT-FOUND-001-000",
    )
    transition = _transition()
    transition_assertion = _transition_assertion()
    transition_result = evaluate_transition_assertion(
        transition_assertion,
        transition,
        result_id="RESULT-FOUND-001-001",
    )

    validate_assertion_result(snapshot_result, snapshot_assertion, snapshot)
    validate_assertion_result(transition_result, transition_assertion, transition)


def test_validate_assertion_result_rejects_wrong_types_and_mismatched_outcome() -> None:
    snapshot = _snapshot()
    snapshot_assertion = _snapshot_assertion()
    result = evaluate_snapshot_assertion(
        snapshot_assertion,
        snapshot,
        result_id="RESULT-FOUND-001-000",
    )

    with pytest.raises(AuroraAssertionError, match="result must"):
        validate_assertion_result(object(), snapshot_assertion, snapshot)  # type: ignore[arg-type]
    with pytest.raises(AuroraAssertionError, match="StateSnapshot"):
        validate_assertion_result(result, snapshot_assertion, _transition())
    with pytest.raises(AuroraAssertionError, match="StateTransition"):
        validate_assertion_result(result, _transition_assertion(), snapshot)
    with pytest.raises(AuroraAssertionError, match="SnapshotAssertion or TransitionAssertion"):
        validate_assertion_result(result, object(), snapshot)  # type: ignore[arg-type]
    with pytest.raises(AuroraAssertionError, match="does not match"):
        validate_assertion_result(
            replace(result, reason=AssertionReason.PATH_NOT_FOUND), snapshot_assertion, snapshot
        )


def test_assertion_source_and_evidence_payload_preserve_integrity_without_raw_actual() -> None:
    result = _result()

    source = create_assertion_source(result)
    payload = create_assertion_evidence_payload(result)
    decoded = payload.decode()

    assert source == EvidenceSource(
        EvidenceSourceKind.ASSERTION,
        result.result_id,
        result.result_sha256,
    )
    assert decoded == result.to_evidence_mapping()
    assert "actual" not in decoded
    assert decoded["actual_value_sha256"] == result.actual.value_sha256  # type: ignore[union-attr]


@pytest.mark.parametrize(
    "function",
    [
        create_assertion_source,
        create_assertion_evidence_payload,
        calculate_assertion_result_sha256,
    ],
)
def test_result_helpers_reject_wrong_type(function: object) -> None:
    with pytest.raises(AuroraAssertionError, match="result must"):
        function(object())  # type: ignore[operator]


def test_assertion_result_integrates_with_append_only_evidence_ledger() -> None:
    result = _result()
    ledger = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)

    ledger = append_evidence_record(
        ledger,
        record_id="RECORD-FOUND-001-ASSERTION-000",
        observed_at_tick=result.evaluated_at_tick,
        recorded_at_tick=result.evaluated_at_tick,
        kind=EvidenceKind.ASSERTION_RESULT,
        domain=EvidenceDomain.VALIDATOR,
        producer_id="HARNESS-ASSERTIONS",
        payload=create_assertion_evidence_payload(result),
        sources=(create_assertion_source(result),),
    )

    record = ledger.records[0]
    assert record.kind is EvidenceKind.ASSERTION_RESULT
    assert record.payload.decode()["status"] == "PASS"
    assert record.sources[0].source_sha256 == result.result_sha256


def test_empty_assertion_series_has_stable_identity_and_round_trip() -> None:
    series = create_assertion_series(_RUN_ID, _SCENARIO_ID)

    assert series.results == ()
    assert series.result_count == 0
    assert series.terminal_result_sha256 is None
    assert series.series_sha256 == calculate_assertion_series_sha256(series)
    assert AssertionSeries.from_mapping(series.to_validator_mapping()) == series


def test_assertion_series_appends_snapshot_and_transition_results_immutably() -> None:
    original = create_assertion_series(_RUN_ID, _SCENARIO_ID)
    snapshot = _snapshot()
    snapshot_assertion = _snapshot_assertion(assertion_id="ASSERTION-FOUND-001-A1")
    first = append_snapshot_assertion_result(
        original,
        snapshot_assertion,
        snapshot,
        result_id="RESULT-FOUND-001-000",
    )
    transition = _transition()
    transition_assertion = _transition_assertion(assertion_id="ASSERTION-FOUND-001-T1")
    second = append_transition_assertion_result(
        first,
        transition_assertion,
        transition,
        result_id="RESULT-FOUND-001-001",
        evaluated_at_tick=20,
    )

    assert original.result_count == 0
    assert first.result_count == 1
    assert second.result_count == 2
    assert second.results[0].previous_result_sha256 is None
    assert second.results[1].previous_result_sha256 == second.results[0].result_sha256
    assert second.terminal_result_sha256 == second.results[-1].result_sha256
    assert AssertionSeries.from_mapping(second.to_validator_mapping()) == second


def test_assertion_series_is_frozen_and_slotted() -> None:
    series = create_assertion_series(_RUN_ID, _SCENARIO_ID)

    with pytest.raises(FrozenInstanceError):
        series.results = ()  # type: ignore[misc]
    with pytest.raises((AttributeError, TypeError)):
        series.extra = True  # type: ignore[attr-defined]


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("run_id", "bad", "stable uppercase"),
        ("scenario_id", "BAD", "scenario_id"),
        ("results", [], "tuple"),
        ("results", (object(),), "tuple"),
    ],
)
def test_assertion_series_rejects_invalid_top_level_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    with pytest.raises(AuroraAssertionError, match=message):
        replace(create_assertion_series(_RUN_ID, _SCENARIO_ID), **{field: value})


def test_assertion_series_rejects_result_over_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(assertions_module, "MAX_ASSERTION_RESULTS", 0)

    with pytest.raises(AuroraAssertionError, match="results must not exceed"):
        AssertionSeries(_RUN_ID, _SCENARIO_ID, (_result(),))


def test_assertion_series_rejects_identity_sequence_duplicates_time_and_chain_errors() -> None:
    first = _result(result_id="RESULT-FOUND-001-000")
    valid_second = replace(
        _result(result_id="RESULT-FOUND-001-001"),
        sequence=1,
        evaluated_at_tick=20,
        previous_result_sha256=first.result_sha256,
    )

    with pytest.raises(AuroraAssertionError, match="identity"):
        AssertionSeries(_RUN_ID, _SCENARIO_ID, (replace(first, run_id="OTHER-RUN-001"),))
    with pytest.raises(AuroraAssertionError, match="sequence"):
        AssertionSeries(
            _RUN_ID, _SCENARIO_ID, (replace(first, sequence=1, previous_result_sha256="b" * 64),)
        )
    duplicate = replace(valid_second, result_id=first.result_id)
    with pytest.raises(AuroraAssertionError, match="unique"):
        AssertionSeries(_RUN_ID, _SCENARIO_ID, (first, duplicate))
    earlier = replace(valid_second, evaluated_at_tick=9)
    with pytest.raises(AuroraAssertionError, match="nondecreasing"):
        AssertionSeries(_RUN_ID, _SCENARIO_ID, (first, earlier))
    broken = replace(valid_second, previous_result_sha256="b" * 64)
    with pytest.raises(AuroraAssertionError, match="hash chain"):
        AssertionSeries(_RUN_ID, _SCENARIO_ID, (first, broken))
    assert AssertionSeries(_RUN_ID, _SCENARIO_ID, (first, valid_second)).result_count == 2


def test_assertion_series_rejects_first_result_with_previous_hash() -> None:
    result = _result()
    object.__setattr__(result, "previous_result_sha256", "b" * 64)

    with pytest.raises(AuroraAssertionError, match="first series result"):
        AssertionSeries(_RUN_ID, _SCENARIO_ID, (result,))


def test_append_helpers_reject_wrong_series_identity_and_capacity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    snapshot = _snapshot()
    transition = _transition()
    wrong = create_assertion_series("AURORA-RUN-FOUND-001-OTHER", _SCENARIO_ID)

    with pytest.raises(AuroraAssertionError, match="identity"):
        append_snapshot_assertion_result(
            wrong,
            _snapshot_assertion(),
            snapshot,
            result_id="RESULT-FOUND-001-000",
        )
    with pytest.raises(AuroraAssertionError, match="identity"):
        append_transition_assertion_result(
            wrong,
            _transition_assertion(),
            transition,
            result_id="RESULT-FOUND-001-000",
        )
    with pytest.raises(AuroraAssertionError, match="series must"):
        append_snapshot_assertion_result(  # type: ignore[arg-type]
            object(),
            _snapshot_assertion(),
            snapshot,
            result_id="RESULT-FOUND-001-000",
        )

    monkeypatch.setattr(assertions_module, "MAX_ASSERTION_RESULTS", 0)
    empty = create_assertion_series(_RUN_ID, _SCENARIO_ID)
    with pytest.raises(AuroraAssertionError, match="must not exceed"):
        append_snapshot_assertion_result(
            empty,
            _snapshot_assertion(),
            snapshot,
            result_id="RESULT-FOUND-001-000",
        )
    with pytest.raises(AuroraAssertionError, match="must not exceed"):
        append_transition_assertion_result(
            empty,
            _transition_assertion(),
            transition,
            result_id="RESULT-FOUND-001-000",
        )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.pop("results"),
        lambda data: data.__setitem__("unexpected", True),
        lambda data: data.__setitem__("assertion_schema_version", "2.0"),
        lambda data: data.__setitem__("series_type", "OTHER"),
        lambda data: data.__setitem__("result_count", 2),
        lambda data: data.__setitem__("terminal_result_sha256", "b" * 64),
        lambda data: data.__setitem__("series_sha256", "b" * 64),
        lambda data: data.__setitem__("results", {}),
        lambda data: data.__setitem__("terminal_result_sha256", 1),
    ],
)
def test_assertion_series_from_mapping_rejects_tampering(mutation: object) -> None:
    series = append_snapshot_assertion_result(
        create_assertion_series(_RUN_ID, _SCENARIO_ID),
        _snapshot_assertion(),
        _snapshot(),
        result_id="RESULT-FOUND-001-000",
    )
    data = series.to_validator_mapping()
    mutation(data)  # type: ignore[operator]

    with pytest.raises(AuroraAssertionError):
        AssertionSeries.from_mapping(data)


def test_assertion_series_from_mapping_rejects_non_mapping_result() -> None:
    data = create_assertion_series(_RUN_ID, _SCENARIO_ID).to_validator_mapping()
    data["results"] = ["bad"]

    with pytest.raises(AuroraAssertionError, match="must be an object"):
        AssertionSeries.from_mapping(data)


def test_assertion_series_from_mapping_requires_an_object() -> None:
    with pytest.raises(AuroraAssertionError, match="assertion series must be an object"):
        AssertionSeries.from_mapping([])  # type: ignore[arg-type]


def test_calculate_assertion_series_sha256_rejects_wrong_type() -> None:
    with pytest.raises(AuroraAssertionError, match="series must"):
        calculate_assertion_series_sha256(object())  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("value", "minimum", "maximum"),
    [(0.5, 0.0, None), (0.5, None, 1.0)],
)
def test_number_range_accepts_values_with_only_one_bound(
    value: float,
    minimum: float | None,
    maximum: float | None,
) -> None:
    assertion = _snapshot_assertion(
        SnapshotAssertionOperator.NUMBER_RANGE,
        path="/value",
        minimum=minimum,
        maximum=maximum,
    )

    result = evaluate_snapshot_assertion(
        assertion,
        _snapshot({"value": value}),
        result_id="RESULT-FOUND-001-000",
    )

    assert result.status is AssertionStatus.PASS


def test_defensive_json_helpers_reject_unreachable_unsupported_objects() -> None:
    with pytest.raises(AuroraAssertionError, match="unsupported JSON value"):
        assertions_module._classify_json_type(object())  # type: ignore[attr-defined]
    with pytest.raises(AuroraAssertionError, match="canonical finite JSON"):
        assertions_module._canonical_json_bytes(object())  # type: ignore[attr-defined]


def test_schema_parsers_reject_non_string_keys_and_boolean_sequence() -> None:
    with pytest.raises(AuroraAssertionError, match="keys must be strings"):
        AssertionValue.from_mapping({1: "bad"})  # type: ignore[dict-item]
    data = _result().to_validator_mapping()
    data["sequence"] = True
    with pytest.raises(AuroraAssertionError, match="sequence must be an integer"):
        AssertionResult.from_mapping(data)


@pytest.mark.parametrize(
    ("target", "changes", "message"),
    [
        (_snapshot_assertion(), {"assertion_id": 1}, "assertion_id must be a string"),
        (_snapshot_assertion(), {"path": 1}, "path must be a string"),
        (_result(), {"scenario_id": 1}, "scenario_id must be a string"),
        (_result(), {"evaluated_at_tick": True}, "evaluated_at_tick must be an integer"),
    ],
)
def test_typed_contracts_defensively_reject_runtime_non_string_and_boolean_values(
    target: object,
    changes: dict[str, object],
    message: str,
) -> None:
    with pytest.raises(AuroraAssertionError, match=message):
        replace(target, **changes)  # type: ignore[type-var]
