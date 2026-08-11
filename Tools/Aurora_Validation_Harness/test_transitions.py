"""Unit tests for deterministic structural state transitions."""

from __future__ import annotations

import copy
import hashlib
from dataclasses import FrozenInstanceError, replace
from types import MappingProxyType

import pytest

from aurora_validation_harness import transitions as transitions_module
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
    DEFAULT_MAX_TRANSITION_CHANGES,
    DEFAULT_MAX_TRANSITION_VALUE_BYTES,
    MAX_TICK,
    MAX_TRANSITION_CAUSES,
    MAX_TRANSITION_CHANGES,
    MAX_TRANSITION_VALUE_BYTES,
    SUPPORTED_TRANSITION_SCHEMA_VERSION,
    ChangeOperation,
    StateChange,
    StateTransition,
    TransitionError,
    TransitionSeries,
    TransitionStatus,
    TransitionValue,
    append_state_transition,
    calculate_state_transition_sha256,
    calculate_transition_series_sha256,
    create_state_transition,
    create_transition_evidence_payload,
    create_transition_series,
    create_transition_source,
    create_transition_value,
    derive_state_changes,
    validate_state_transition,
)

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_RUN_ID = "AURORA-RUN-FOUND-001-001"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"


def _value(data: object = "UNKNOWN") -> TransitionValue:
    return create_transition_value(data)


def _raw_value(value_json: bytes, *, digest: object | None = None) -> TransitionValue:
    return TransitionValue(
        value_json=value_json,
        value_sha256=(hashlib.sha256(value_json).hexdigest() if digest is None else digest),
    )


def _change(
    *,
    path: str = "/belief",
    operation: ChangeOperation = ChangeOperation.REPLACED,
    before: TransitionValue | None = None,
    after: TransitionValue | None = None,
) -> StateChange:
    if before is None and operation is not ChangeOperation.ADDED:
        before = _value("UNKNOWN")
    if after is None and operation is not ChangeOperation.REMOVED:
        after = _value("KNOWN")
    return StateChange(path=path, operation=operation, before=before, after=after)


def _source(
    *,
    kind: EvidenceSourceKind = EvidenceSourceKind.EVENT,
    source_id: str = "EVENT-FOUND-001-E1",
    digest: str = "a" * 64,
) -> EvidenceSource:
    return EvidenceSource(kind, source_id, digest)


def _snapshot_pair(
    *,
    before_data: dict[str, object] | None = None,
    after_data: dict[str, object] | None = None,
    run_id: str = _RUN_ID,
    scenario_id: str = _SCENARIO_ID,
    domain: EvidenceDomain = EvidenceDomain.AURORA_STATE,
    subject_id: str = "AURORA",
    before_tick: int = 0,
    after_tick: int = 10,
) -> tuple[StateSnapshot, StateSnapshot]:
    before_state = create_snapshot_state(
        {"belief": "UNKNOWN", "confidence": None} if before_data is None else before_data
    )
    after_state = create_snapshot_state(
        {"belief": "KNOWN", "confidence": 0.8} if after_data is None else after_data
    )
    series = create_snapshot_series(run_id, scenario_id)
    series = append_state_snapshot(
        series,
        snapshot_id="SNAPSHOT-FOUND-001-000",
        captured_at_tick=before_tick,
        phase=SnapshotPhase.INITIAL,
        domain=domain,
        subject_id=subject_id,
        producer_id="HARNESS-RUNTIME",
        checkpoint_id="CP0",
        state=before_state,
    )
    series = append_state_snapshot(
        series,
        snapshot_id="SNAPSHOT-FOUND-001-001",
        captured_at_tick=after_tick,
        phase=SnapshotPhase.CHECKPOINT,
        domain=domain,
        subject_id=subject_id,
        producer_id="HARNESS-RUNTIME",
        checkpoint_id="CP1",
        state=after_state,
    )
    return series.snapshots[0], series.snapshots[1]


def _transition(
    *,
    changed: bool = True,
    transition_id: str = "TRANSITION-FOUND-001-000",
    sequence: int = 0,
    causes: tuple[EvidenceSource, ...] = (),
    previous_transition_sha256: str | None = None,
) -> StateTransition:
    if changed:
        before, after = _snapshot_pair()
    else:
        state = {"belief": "UNKNOWN", "confidence": None}
        before, after = _snapshot_pair(before_data=state, after_data=state)
    if sequence > 0 and previous_transition_sha256 is None:
        previous_transition_sha256 = "b" * 64
    return create_state_transition(
        before,
        after,
        transition_id=transition_id,
        sequence=sequence,
        causes=causes,
        previous_transition_sha256=previous_transition_sha256,
    )


def _series(transition_count: int = 3) -> TransitionSeries:
    snapshots = create_snapshot_series(_RUN_ID, _SCENARIO_ID)
    for index in range(transition_count + 1):
        snapshots = append_state_snapshot(
            snapshots,
            snapshot_id=f"SNAPSHOT-FOUND-001-{index:03d}",
            captured_at_tick=index,
            phase=SnapshotPhase.INITIAL if index == 0 else SnapshotPhase.CHECKPOINT,
            domain=EvidenceDomain.AURORA_STATE,
            subject_id="AURORA",
            producer_id="HARNESS-RUNTIME",
            checkpoint_id=f"CP{index}",
            state=create_snapshot_state({"index": index}),
        )

    series = create_transition_series(_RUN_ID, _SCENARIO_ID)
    for index in range(transition_count):
        series = append_state_transition(
            series,
            transition_id=f"TRANSITION-FOUND-001-{index:03d}",
            before=snapshots.snapshots[index],
            after=snapshots.snapshots[index + 1],
            causes=(
                _source(
                    source_id=f"EVENT-FOUND-001-E{index}",
                    digest=f"{index + 1:x}" * 64,
                ),
            ),
        )
    return series


def test_public_constants_define_schema_and_bounded_limits() -> None:
    assert SUPPORTED_TRANSITION_SCHEMA_VERSION == "1.0"
    assert DEFAULT_MAX_TRANSITION_VALUE_BYTES == 4_194_304
    assert MAX_TRANSITION_VALUE_BYTES == 16_777_216
    assert DEFAULT_MAX_TRANSITION_CHANGES == 50_000
    assert MAX_TRANSITION_CHANGES == 1_000_000
    assert MAX_TRANSITION_CAUSES == 1_024
    assert MAX_TICK == (1 << 63) - 1
    assert 0 < DEFAULT_MAX_TRANSITION_VALUE_BYTES < MAX_TRANSITION_VALUE_BYTES < MAX_TICK
    assert 0 < DEFAULT_MAX_TRANSITION_CHANGES < MAX_TRANSITION_CHANGES


def test_transition_enums_have_stable_contract_values() -> None:
    assert {operation.value for operation in ChangeOperation} == {
        "ADDED",
        "REMOVED",
        "REPLACED",
    }
    assert {status.value for status in TransitionStatus} == {"UNCHANGED", "CHANGED"}


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
def test_transition_value_accepts_every_supported_json_shape(data: object) -> None:
    value = create_transition_value(data)

    assert value.decode() == data
    assert value.size_bytes == len(value.value_json)
    assert value.value_sha256 == hashlib.sha256(value.value_json).hexdigest()
    assert value.to_mapping() == {"data": data, "value_sha256": value.value_sha256}


def test_transition_value_accepts_generic_mapping_and_canonicalizes_unicode() -> None:
    data = MappingProxyType({"z": "ö", "a": MappingProxyType({"β": [2, 1]})})

    value = create_transition_value(data)

    assert value.value_json == '{"a":{"β":[2,1]},"z":"ö"}'.encode()


def test_transition_value_detaches_mutable_input_and_decodes_fresh_values() -> None:
    data: dict[str, object] = {"belief": {"value": "UNKNOWN"}, "history": ["T0"]}
    value = create_transition_value(data)
    expected_hash = value.value_sha256

    belief = data["belief"]
    assert isinstance(belief, dict)
    belief["value"] = "KNOWN"
    history = data["history"]
    assert isinstance(history, list)
    history.append("T1")
    decoded = value.decode()
    assert isinstance(decoded, dict)
    decoded["belief"] = "tampered"

    assert value.decode() == {"belief": {"value": "UNKNOWN"}, "history": ["T0"]}
    assert value.value_sha256 == expected_hash


def test_transition_value_hash_is_deterministic_across_mapping_order() -> None:
    first = create_transition_value({"b": 2, "a": {"y": 2, "x": 1}})
    second = create_transition_value({"a": {"x": 1, "y": 2}, "b": 2})

    assert first == second


def test_transition_value_default_limit_requires_explicit_large_value_opt_in() -> None:
    data = "x" * DEFAULT_MAX_TRANSITION_VALUE_BYTES

    with pytest.raises(TransitionError, match="transition value must not exceed"):
        create_transition_value(data)

    value = create_transition_value(data, max_value_bytes=MAX_TRANSITION_VALUE_BYTES)
    assert value.size_bytes > DEFAULT_MAX_TRANSITION_VALUE_BYTES


@pytest.mark.parametrize("max_value_bytes", [True, False, 1.5, "10", None])
def test_transition_value_rejects_non_integer_size_limit(max_value_bytes: object) -> None:
    with pytest.raises(TransitionError, match="max_value_bytes must be an integer"):
        create_transition_value("value", max_value_bytes=max_value_bytes)  # type: ignore[arg-type]


@pytest.mark.parametrize("max_value_bytes", [0, -1, MAX_TRANSITION_VALUE_BYTES + 1])
def test_transition_value_rejects_out_of_range_size_limit(max_value_bytes: int) -> None:
    with pytest.raises(TransitionError, match="max_value_bytes must be between"):
        create_transition_value("value", max_value_bytes=max_value_bytes)


def test_transition_value_enforces_configured_size_limit() -> None:
    with pytest.raises(TransitionError, match="transition value must not exceed 4 bytes"):
        create_transition_value("large", max_value_bytes=4)


@pytest.mark.parametrize("data", [("tuple",), {"set"}, b"bytes", object()])
def test_transition_value_rejects_unsupported_json_types(data: object) -> None:
    with pytest.raises(TransitionError, match="unsupported JSON value type"):
        create_transition_value({"nested": [data]})


@pytest.mark.parametrize("data", [float("nan"), float("inf"), float("-inf")])
def test_transition_value_rejects_non_finite_numbers(data: float) -> None:
    with pytest.raises(TransitionError, match="contains a non-finite number"):
        create_transition_value({"nested": [{"value": data}]})


def test_transition_value_rejects_non_string_object_keys() -> None:
    with pytest.raises(TransitionError, match="contains a non-string object key"):
        create_transition_value({"nested": {1: "value"}})


def test_transition_value_round_trips_through_mapping() -> None:
    value = create_transition_value({"belief": ["UNKNOWN", None]})

    restored = TransitionValue.from_mapping(MappingProxyType(value.to_mapping()))

    assert restored == value
    assert restored is not value


def test_transition_value_mapping_requires_exact_schema() -> None:
    mapping = _value().to_mapping()

    missing = dict(mapping)
    del missing["data"]
    with pytest.raises(TransitionError, match="missing required field"):
        TransitionValue.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(TransitionError, match="contains unknown field"):
        TransitionValue.from_mapping(unknown)

    with pytest.raises(TransitionError, match="transition value must be a JSON object"):
        TransitionValue.from_mapping([])  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="must use string keys"):
        TransitionValue.from_mapping({1: "bad"})  # type: ignore[arg-type]


def test_transition_value_mapping_rejects_digest_type_and_mismatch() -> None:
    mapping = _value().to_mapping()

    invalid = dict(mapping)
    invalid["value_sha256"] = 7
    with pytest.raises(TransitionError, match="value_sha256 must be a string"):
        TransitionValue.from_mapping(invalid)

    mismatched = dict(mapping)
    mismatched["value_sha256"] = "0" * 64
    with pytest.raises(TransitionError, match="declared value_sha256 does not match"):
        TransitionValue.from_mapping(mismatched)


def test_transition_value_constructor_rejects_non_bytes_and_bad_digest() -> None:
    with pytest.raises(TransitionError, match="value_json must be bytes"):
        TransitionValue(value_json="null", value_sha256="0" * 64)  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="value_sha256 must be a string"):
        _raw_value(b"null", digest=7)

    with pytest.raises(TransitionError, match="lowercase 64-character"):
        _raw_value(b"null", digest="ABC")

    with pytest.raises(TransitionError, match="does not match value_json"):
        _raw_value(b"null", digest="0" * 64)


@pytest.mark.parametrize(
    ("value_json", "message"),
    [
        (b"\xff", "not valid JSON"),
        (b"{", "not valid JSON"),
        (b"NaN", "not valid JSON"),
        (b'{"b":2, "a":1}', "canonical JSON encoding"),
    ],
)
def test_transition_value_constructor_rejects_invalid_or_noncanonical_json(
    value_json: bytes,
    message: str,
) -> None:
    with pytest.raises(TransitionError, match=message):
        _raw_value(value_json)


def test_transition_value_constructor_enforces_absolute_size_limit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(transitions_module, "MAX_TRANSITION_VALUE_BYTES", 1)

    with pytest.raises(TransitionError, match="value_json must not exceed 1 bytes"):
        _raw_value(b"null")


def test_private_canonicalizer_wraps_serialization_errors() -> None:
    with pytest.raises(TransitionError, match="value is not JSON-serializable"):
        transitions_module._canonical_json_bytes({1: object()})


def test_private_normalizer_retains_defensive_unsupported_branch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(transitions_module, "_validate_json_value", lambda *_a, **_k: None)

    with pytest.raises(TransitionError, match="unsupported JSON value type"):
        transitions_module._normalize_json_value(object(), path="value")


def test_state_change_distinguishes_json_null_from_missing_side() -> None:
    added_null = StateChange(
        path="/value",
        operation=ChangeOperation.ADDED,
        before=None,
        after=_value(None),
    )
    removed_null = StateChange(
        path="/value",
        operation=ChangeOperation.REMOVED,
        before=_value(None),
        after=None,
    )

    assert added_null.after is not None
    assert added_null.after.decode() is None
    assert removed_null.before is not None
    assert removed_null.before.decode() is None


@pytest.mark.parametrize("path", ["/value", "/", "/a/b/0", "/a~0b", "/a~1b"])
def test_state_change_accepts_valid_nonempty_json_pointers(path: str) -> None:
    assert _change(path=path).path == path


@pytest.mark.parametrize("path", ["", "value", "~", "/a~", "/a~2b"])
def test_state_change_rejects_invalid_json_pointer(path: str) -> None:
    with pytest.raises(TransitionError, match="non-empty RFC 6901 JSON Pointer"):
        _change(path=path)


def test_state_change_rejects_non_string_path_and_operation() -> None:
    with pytest.raises(TransitionError, match="path must be a string"):
        _change(path=7)  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="operation must be a ChangeOperation"):
        StateChange("/value", "ADDED", None, _value(1))  # type: ignore[arg-type]


def test_state_change_rejects_invalid_before_and_after_types() -> None:
    with pytest.raises(TransitionError, match="before must be null or a TransitionValue"):
        StateChange("/value", ChangeOperation.REMOVED, "old", None)  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="after must be null or a TransitionValue"):
        StateChange("/value", ChangeOperation.ADDED, None, "new")  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("operation", "before", "after", "message"),
    [
        (ChangeOperation.ADDED, _value(1), _value(2), "ADDED change requires only"),
        (ChangeOperation.ADDED, None, None, "ADDED change requires only"),
        (ChangeOperation.REMOVED, None, None, "REMOVED change requires only"),
        (ChangeOperation.REMOVED, _value(1), _value(2), "REMOVED change requires only"),
        (ChangeOperation.REPLACED, None, _value(2), "REPLACED change requires"),
        (ChangeOperation.REPLACED, _value(1), None, "REPLACED change requires"),
    ],
)
def test_state_change_enforces_operation_value_shape(
    operation: ChangeOperation,
    before: TransitionValue | None,
    after: TransitionValue | None,
    message: str,
) -> None:
    with pytest.raises(TransitionError, match=message):
        StateChange("/value", operation, before, after)


def test_replaced_change_requires_distinct_values() -> None:
    value = _value({"same": True})

    with pytest.raises(TransitionError, match="REPLACED change values must differ"):
        StateChange("/value", ChangeOperation.REPLACED, value, value)


@pytest.mark.parametrize(
    "change",
    [
        StateChange("/added", ChangeOperation.ADDED, None, _value(None)),
        StateChange("/removed", ChangeOperation.REMOVED, _value(False), None),
        StateChange("/replaced", ChangeOperation.REPLACED, _value(1), _value(1.0)),
    ],
)
def test_state_change_round_trips_every_operation(change: StateChange) -> None:
    restored = StateChange.from_mapping(change.to_mapping())

    assert restored == change
    assert restored.change_sha256 == change.change_sha256


def test_state_change_hash_is_deterministic_and_content_sensitive() -> None:
    first = _change()
    equivalent = _change()
    changed = _change(after=_value("CONFIRMED"))

    assert first.change_sha256 == equivalent.change_sha256
    assert first.change_sha256 != changed.change_sha256


def test_state_change_mapping_requires_exact_schema() -> None:
    mapping = _change().to_mapping()

    missing = dict(mapping)
    del missing["path"]
    with pytest.raises(TransitionError, match="missing required field"):
        StateChange.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(TransitionError, match="contains unknown field"):
        StateChange.from_mapping(unknown)

    with pytest.raises(TransitionError, match="state change must be a JSON object"):
        StateChange.from_mapping([])  # type: ignore[arg-type]


def test_state_change_mapping_rejects_invalid_scalars_and_enums() -> None:
    mapping = _change().to_mapping()

    invalid_path = copy.deepcopy(mapping)
    invalid_path["path"] = 7
    with pytest.raises(TransitionError, match=r"state change.path must be a string"):
        StateChange.from_mapping(invalid_path)

    invalid_operation = copy.deepcopy(mapping)
    invalid_operation["operation"] = "MOVED"
    with pytest.raises(TransitionError, match=r"unsupported state change.operation"):
        StateChange.from_mapping(invalid_operation)

    non_string_operation = copy.deepcopy(mapping)
    non_string_operation["operation"] = 7
    with pytest.raises(TransitionError, match=r"state change.operation must be a string"):
        StateChange.from_mapping(non_string_operation)

    invalid_hash = copy.deepcopy(mapping)
    invalid_hash["change_sha256"] = 7
    with pytest.raises(TransitionError, match="change_sha256 must be a string"):
        StateChange.from_mapping(invalid_hash)


def test_state_change_mapping_rejects_invalid_optional_values_and_tampering() -> None:
    mapping = _change().to_mapping()

    invalid_before = copy.deepcopy(mapping)
    invalid_before["before"] = []
    with pytest.raises(TransitionError, match=r"state change.before must be a JSON object"):
        StateChange.from_mapping(invalid_before)

    invalid_after = copy.deepcopy(mapping)
    invalid_after["after"] = "value"
    with pytest.raises(TransitionError, match=r"state change.after must be a JSON object"):
        StateChange.from_mapping(invalid_after)

    wrong_hash = copy.deepcopy(mapping)
    wrong_hash["change_sha256"] = "0" * 64
    with pytest.raises(TransitionError, match="declared change_sha256 does not match"):
        StateChange.from_mapping(wrong_hash)

    tampered_value = copy.deepcopy(mapping)
    after = tampered_value["after"]
    assert isinstance(after, dict)
    after["data"] = "tampered"
    with pytest.raises(TransitionError, match="declared value_sha256 does not match"):
        StateChange.from_mapping(tampered_value)


def test_derive_state_changes_returns_empty_for_identical_state() -> None:
    state = create_snapshot_state({"belief": "UNKNOWN"})

    assert derive_state_changes(state, state) == ()


def test_derive_state_changes_handles_nested_mapping_operations() -> None:
    before = create_snapshot_state(
        {
            "belief": {"confidence": None, "value": "UNKNOWN"},
            "obsolete": {"nested": True},
            "stable": 1,
        }
    )
    after = create_snapshot_state(
        {
            "belief": {"confidence": 0.8, "value": "KNOWN"},
            "new": {"nested": True},
            "stable": 1,
        }
    )

    changes = derive_state_changes(before, after)
    by_path = {change.path: change for change in changes}

    assert tuple(change.path for change in changes) == tuple(sorted(by_path))
    assert by_path["/belief/confidence"].operation is ChangeOperation.REPLACED
    assert by_path["/belief/confidence"].before is not None
    assert by_path["/belief/confidence"].before.decode() is None
    assert by_path["/belief/value"].after is not None
    assert by_path["/belief/value"].after.decode() == "KNOWN"
    assert by_path["/new"].operation is ChangeOperation.ADDED
    assert by_path["/new"].after is not None
    assert by_path["/new"].after.decode() == {"nested": True}
    assert by_path["/obsolete"].operation is ChangeOperation.REMOVED
    assert "/stable" not in by_path


def test_derive_state_changes_handles_list_growth_shrink_and_nested_replacement() -> None:
    before = create_snapshot_state({"grow": [1], "nested": [{"value": "old"}], "shrink": [1, 2, 3]})
    after = create_snapshot_state({"grow": [1, 2, 3], "nested": [{"value": "new"}], "shrink": [1]})

    by_path = {change.path: change for change in derive_state_changes(before, after)}

    assert by_path["/grow/1"].operation is ChangeOperation.ADDED
    assert by_path["/grow/2"].operation is ChangeOperation.ADDED
    assert by_path["/nested/0/value"].operation is ChangeOperation.REPLACED
    assert by_path["/shrink/1"].operation is ChangeOperation.REMOVED
    assert by_path["/shrink/2"].operation is ChangeOperation.REMOVED


def test_derive_state_changes_replaces_incompatible_container_types() -> None:
    before = create_snapshot_state({"value": {"nested": 1}})
    after = create_snapshot_state({"value": [1, 2]})

    changes = derive_state_changes(before, after)

    assert len(changes) == 1
    assert changes[0].path == "/value"
    assert changes[0].operation is ChangeOperation.REPLACED
    assert changes[0].before is not None
    assert changes[0].before.decode() == {"nested": 1}
    assert changes[0].after is not None
    assert changes[0].after.decode() == [1, 2]


def test_derive_state_changes_escapes_json_pointer_tokens() -> None:
    before = create_snapshot_state({"": 0, "a/b": 1, "a~b": 2})
    after = create_snapshot_state({"": 1, "a/b": 2, "a~b": 3})

    paths = {change.path for change in derive_state_changes(before, after)}

    assert paths == {"/", "/a~1b", "/a~0b"}


@pytest.mark.parametrize(
    ("before_value", "after_value"),
    [(1, 1.0), (1, True), (0, False), (None, 0)],
)
def test_derive_state_changes_preserves_json_type_distinctions(
    before_value: object,
    after_value: object,
) -> None:
    before = create_snapshot_state({"value": before_value})
    after = create_snapshot_state({"value": after_value})

    changes = derive_state_changes(before, after)

    assert len(changes) == 1
    assert changes[0].operation is ChangeOperation.REPLACED


def test_derive_state_changes_is_deterministic_across_mapping_order() -> None:
    before_a = create_snapshot_state({"z": 0, "a": 0, "m": 0})
    after_a = create_snapshot_state({"z": 1, "a": 1, "m": 1})
    before_b = create_snapshot_state({"m": 0, "a": 0, "z": 0})
    after_b = create_snapshot_state({"a": 1, "z": 1, "m": 1})

    assert derive_state_changes(before_a, after_a) == derive_state_changes(before_b, after_b)


def test_derive_state_changes_requires_snapshot_state_values() -> None:
    state = create_snapshot_state({"value": 1})

    with pytest.raises(TransitionError, match="before and after must be SnapshotState"):
        derive_state_changes({}, state)  # type: ignore[arg-type]
    with pytest.raises(TransitionError, match="before and after must be SnapshotState"):
        derive_state_changes(state, {})  # type: ignore[arg-type]


@pytest.mark.parametrize("max_changes", [True, False, 1.5, "2", None])
def test_derive_state_changes_rejects_non_integer_change_limit(max_changes: object) -> None:
    before = create_snapshot_state({"value": 1})
    after = create_snapshot_state({"value": 2})

    with pytest.raises(TransitionError, match="max_changes must be an integer"):
        derive_state_changes(before, after, max_changes=max_changes)  # type: ignore[arg-type]


@pytest.mark.parametrize("max_changes", [0, -1, MAX_TRANSITION_CHANGES + 1])
def test_derive_state_changes_rejects_out_of_range_change_limit(max_changes: int) -> None:
    before = create_snapshot_state({"value": 1})
    after = create_snapshot_state({"value": 2})

    with pytest.raises(TransitionError, match="max_changes must be between"):
        derive_state_changes(before, after, max_changes=max_changes)


def test_derive_state_changes_enforces_change_limit_but_accepts_exact_limit() -> None:
    before = create_snapshot_state({"a": 0, "b": 0})
    after = create_snapshot_state({"a": 1, "b": 1})

    with pytest.raises(TransitionError, match="state diff exceeds max_changes limit of 1"):
        derive_state_changes(before, after, max_changes=1)

    assert len(derive_state_changes(before, after, max_changes=2)) == 2


def test_create_state_transition_binds_compatible_snapshot_pair_and_causes() -> None:
    before, after = _snapshot_pair()
    cause = _source()

    transition = create_state_transition(
        before,
        after,
        transition_id="TRANSITION-FOUND-001-000",
        causes=(cause,),
    )

    assert transition.run_id == before.run_id == after.run_id
    assert transition.scenario_id == before.scenario_id == after.scenario_id
    assert transition.domain is before.domain is after.domain
    assert transition.subject_id == "AURORA"
    assert transition.before_snapshot_id == before.snapshot_id
    assert transition.before_snapshot_sha256 == before.snapshot_sha256
    assert transition.before_state_sha256 == before.state.state_sha256
    assert transition.before_tick == before.captured_at_tick
    assert transition.after_snapshot_id == after.snapshot_id
    assert transition.after_snapshot_sha256 == after.snapshot_sha256
    assert transition.after_state_sha256 == after.state.state_sha256
    assert transition.after_tick == after.captured_at_tick
    assert transition.causes == (cause,)
    assert transition.status is TransitionStatus.CHANGED
    assert transition.change_count == len(transition.changes) > 0


def test_changed_transition_may_preserve_missing_cause_for_later_assertion() -> None:
    transition = _transition(changed=True, causes=())

    assert transition.status is TransitionStatus.CHANGED
    assert transition.causes == ()


def test_unchanged_transition_has_identical_state_hashes_and_empty_changes() -> None:
    transition = _transition(changed=False)

    assert transition.status is TransitionStatus.UNCHANGED
    assert transition.changes == ()
    assert transition.change_count == 0
    assert transition.before_state_sha256 == transition.after_state_sha256


def test_transition_hashes_are_deterministic_and_content_sensitive() -> None:
    first = _transition(causes=(_source(),))
    equivalent = _transition(causes=(_source(),))
    changed_causes = _transition(causes=(_source(digest="c" * 64),))

    assert first.change_set_sha256 == equivalent.change_set_sha256
    assert first.transition_sha256 == equivalent.transition_sha256
    assert first.transition_sha256 == calculate_state_transition_sha256(first)
    assert first.transition_sha256 != changed_causes.transition_sha256


def test_create_state_transition_accepts_nonadjacent_snapshot_sequences() -> None:
    before, after = _snapshot_pair()
    after = replace(after, sequence=5)

    transition = create_state_transition(
        before,
        after,
        transition_id="TRANSITION-NONADJACENT-001",
    )

    assert transition.before_snapshot_id == before.snapshot_id
    assert transition.after_snapshot_id == after.snapshot_id


def test_snapshot_pair_requires_runtime_snapshot_values() -> None:
    before, after = _snapshot_pair()

    with pytest.raises(TransitionError, match="before and after must be StateSnapshot"):
        create_state_transition(  # type: ignore[arg-type]
            "before",
            after,
            transition_id="TRANSITION-001",
        )
    with pytest.raises(TransitionError, match="before and after must be StateSnapshot"):
        create_state_transition(  # type: ignore[arg-type]
            before,
            "after",
            transition_id="TRANSITION-001",
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ({"run_id": "AURORA-RUN-FOUND-001-002"}, "same run and scenario"),
        ({"scenario_id": "AURORA-SCN-FOUND-002"}, "same run and scenario"),
        ({"domain": EvidenceDomain.WORLD}, "same evidence domain"),
        ({"subject_id": "WORLD"}, "same subject"),
        ({"sequence": 0}, "sequence must follow"),
        ({"captured_at_tick": 0}, "tick must not precede"),
        ({"snapshot_id": "SNAPSHOT-FOUND-001-000"}, "snapshot IDs must differ"),
    ],
)
def test_snapshot_pair_rejects_incompatible_after_snapshot(
    mutation: dict[str, object],
    message: str,
) -> None:
    before, after = _snapshot_pair(before_tick=5, after_tick=10)
    if mutation == {"captured_at_tick": 0}:
        changed_after = replace(after, captured_at_tick=0)
    elif mutation == {"sequence": 0}:
        changed_after = replace(
            after,
            sequence=0,
            previous_snapshot_sha256=None,
        )
    else:
        changed_after = replace(after, **mutation)  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match=message):
        create_state_transition(
            before,
            changed_after,
            transition_id="TRANSITION-FOUND-001-000",
        )


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("transition_id", "bad", "uppercase identifier"),
        ("transition_id", 7, "transition_id must be a string"),
        ("run_id", "bad", "uppercase identifier"),
        ("run_id", 7, "run_id must be a string"),
        ("scenario_id", "FOUND-001", "must match"),
        ("scenario_id", 7, "scenario_id must be a string"),
        ("sequence", True, "sequence must be an integer"),
        ("sequence", "0", "sequence must be an integer"),
        ("sequence", -1, "sequence must be non-negative"),
        ("domain", "AURORA_STATE", "domain must be an EvidenceDomain"),
        ("subject_id", "bad subject", "unsupported identifier"),
        ("subject_id", 7, "subject_id must be a string"),
        ("before_snapshot_id", "bad", "uppercase identifier"),
        ("before_snapshot_sha256", "bad", "lowercase 64-character"),
        ("before_state_sha256", 7, "before_state_sha256 must be a string"),
        ("before_tick", True, "before_tick must be an integer"),
        ("before_tick", -1, "before_tick must be between"),
        ("after_snapshot_id", "bad", "uppercase identifier"),
        ("after_snapshot_sha256", "bad", "lowercase 64-character"),
        ("after_state_sha256", 7, "after_state_sha256 must be a string"),
        ("after_tick", "10", "after_tick must be an integer"),
        ("after_tick", MAX_TICK + 1, "after_tick must be between"),
    ],
)
def test_state_transition_rejects_invalid_scalar_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    transition = _transition()

    with pytest.raises(TransitionError, match=message):
        replace(transition, **{field: value})


def test_state_transition_rejects_tick_regression_and_same_snapshot_id() -> None:
    transition = _transition()

    with pytest.raises(TransitionError, match="after_tick must not precede before_tick"):
        replace(transition, before_tick=11)

    with pytest.raises(TransitionError, match="before and after snapshot IDs must differ"):
        replace(transition, after_snapshot_id=transition.before_snapshot_id)


def test_state_transition_validates_cause_collection() -> None:
    transition = _transition()

    with pytest.raises(TransitionError, match="causes must be a tuple"):
        replace(transition, causes=[])  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="causes must be a tuple"):
        replace(transition, causes=("cause",))  # type: ignore[arg-type]

    source = _source()
    with pytest.raises(TransitionError, match="duplicate kind and ID pairs"):
        replace(transition, causes=(source, source))


def test_state_transition_enforces_absolute_cause_limit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    transition = _transition()
    monkeypatch.setattr(transitions_module, "MAX_TRANSITION_CAUSES", 1)

    with pytest.raises(TransitionError, match="causes must not exceed 1 entries"):
        replace(
            transition,
            causes=(
                _source(source_id="EVENT-FOUND-001-E1"),
                _source(source_id="EVENT-FOUND-001-E2"),
            ),
        )


def test_state_transition_validates_change_collection() -> None:
    transition = _transition()

    with pytest.raises(TransitionError, match="changes must be a tuple"):
        replace(transition, changes=[])  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="changes must be a tuple"):
        replace(transition, changes=("change",))  # type: ignore[arg-type]

    duplicate = _change(path="/a")
    with pytest.raises(TransitionError, match="unique JSON Pointer paths"):
        replace(transition, changes=(duplicate, duplicate))

    with pytest.raises(TransitionError, match="ordered by JSON Pointer path"):
        replace(transition, changes=(_change(path="/z"), _change(path="/a")))


def test_state_transition_enforces_absolute_change_limit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    transition = _transition()
    monkeypatch.setattr(transitions_module, "MAX_TRANSITION_CHANGES", 1)

    with pytest.raises(TransitionError, match="changes must not exceed 1 entries"):
        replace(transition, changes=(_change(path="/a"), _change(path="/b")))


def test_state_transition_enforces_status_to_state_digest_consistency() -> None:
    changed = _transition(changed=True)
    unchanged = _transition(changed=False)

    with pytest.raises(TransitionError, match="changed transition requires distinct"):
        replace(changed, after_state_sha256=changed.before_state_sha256)

    with pytest.raises(TransitionError, match="unchanged transition requires identical"):
        replace(unchanged, after_state_sha256="0" * 64)


def test_state_transition_validates_previous_hash_and_chain_position() -> None:
    transition = _transition()

    with pytest.raises(TransitionError, match="previous_transition_sha256 must be a string"):
        replace(transition, sequence=1, previous_transition_sha256=7)  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="lowercase 64-character"):
        replace(transition, sequence=1, previous_transition_sha256="ABC")

    with pytest.raises(TransitionError, match="first state transition must not declare"):
        replace(transition, previous_transition_sha256="a" * 64)

    later = _transition(sequence=1)
    with pytest.raises(TransitionError, match="non-first state transition requires"):
        replace(later, previous_transition_sha256=None)


def test_state_transition_round_trips_changed_and_unchanged_records() -> None:
    changed = _transition(causes=(_source(),))
    unchanged = _transition(changed=False)

    assert StateTransition.from_mapping(changed.to_validator_mapping()) == changed
    assert StateTransition.from_mapping(unchanged.to_validator_mapping()) == unchanged


def test_state_transition_evidence_mapping_is_compact() -> None:
    transition = _transition(causes=(_source(),))

    mapping = transition.to_evidence_mapping()

    assert mapping["transition_id"] == transition.transition_id
    assert mapping["transition_sha256"] == transition.transition_sha256
    assert mapping["change_count"] == transition.change_count
    assert mapping["change_set_sha256"] == transition.change_set_sha256
    assert mapping["causes"] == [transition.causes[0].to_mapping()]
    assert "changes" not in mapping
    assert "run_id" not in mapping
    assert "scenario_id" not in mapping


def test_state_transition_validator_mapping_has_complete_envelope() -> None:
    transition = _transition(causes=(_source(),))
    mapping = transition.to_validator_mapping()

    assert mapping["transition_schema_version"] == "1.0"
    assert mapping["transition_type"] == "STATE_TRANSITION"
    assert mapping["status"] == "CHANGED"
    assert mapping["change_count"] == len(transition.changes)
    assert mapping["changes"] == [change.to_mapping() for change in transition.changes]
    assert mapping["transition_sha256"] == transition.transition_sha256


def test_state_transition_mapping_requires_exact_schema() -> None:
    mapping = _transition().to_validator_mapping()

    missing = copy.deepcopy(mapping)
    del missing["changes"]
    with pytest.raises(TransitionError, match="missing required field"):
        StateTransition.from_mapping(missing)

    unknown = copy.deepcopy(mapping)
    unknown["unexpected"] = True
    with pytest.raises(TransitionError, match="contains unknown field"):
        StateTransition.from_mapping(unknown)

    with pytest.raises(TransitionError, match="state transition must be a JSON object"):
        StateTransition.from_mapping([])  # type: ignore[arg-type]


def test_state_transition_mapping_rejects_schema_and_type() -> None:
    mapping = _transition().to_validator_mapping()

    bad_version = copy.deepcopy(mapping)
    bad_version["transition_schema_version"] = "2.0"
    with pytest.raises(TransitionError, match="unsupported transition_schema_version"):
        StateTransition.from_mapping(bad_version)

    non_string_version = copy.deepcopy(mapping)
    non_string_version["transition_schema_version"] = 1
    with pytest.raises(TransitionError, match="transition_schema_version must be a string"):
        StateTransition.from_mapping(non_string_version)

    bad_type = copy.deepcopy(mapping)
    bad_type["transition_type"] = "OTHER"
    with pytest.raises(TransitionError, match="unsupported transition_type"):
        StateTransition.from_mapping(bad_type)


def test_state_transition_mapping_rejects_invalid_domain_and_arrays() -> None:
    mapping = _transition().to_validator_mapping()

    bad_domain = copy.deepcopy(mapping)
    bad_domain["domain"] = "AURORA_PRIVATE"
    with pytest.raises(TransitionError, match=r"unsupported state transition.domain"):
        StateTransition.from_mapping(bad_domain)

    non_string_domain = copy.deepcopy(mapping)
    non_string_domain["domain"] = 7
    with pytest.raises(TransitionError, match=r"state transition.domain must be a string"):
        StateTransition.from_mapping(non_string_domain)

    bad_causes = copy.deepcopy(mapping)
    bad_causes["causes"] = {}
    with pytest.raises(TransitionError, match=r"state transition.causes must be a JSON array"):
        StateTransition.from_mapping(bad_causes)

    bad_cause_member = copy.deepcopy(mapping)
    bad_cause_member["causes"] = [[]]
    with pytest.raises(
        TransitionError, match=r"state transition.causes\[0\] must be a JSON object"
    ):
        StateTransition.from_mapping(bad_cause_member)

    bad_changes = copy.deepcopy(mapping)
    bad_changes["changes"] = {}
    with pytest.raises(TransitionError, match=r"state transition.changes must be a JSON array"):
        StateTransition.from_mapping(bad_changes)

    bad_change_member = copy.deepcopy(mapping)
    bad_change_member["changes"] = [[]]
    with pytest.raises(
        TransitionError, match=r"state transition.changes\[0\] must be a JSON object"
    ):
        StateTransition.from_mapping(bad_change_member)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("transition_id", 7, "transition_id must be a string"),
        ("run_id", 7, "run_id must be a string"),
        ("scenario_id", 7, "scenario_id must be a string"),
        ("sequence", True, "sequence must be an integer"),
        ("subject_id", None, "subject_id must be a string"),
        ("before_snapshot_id", None, "before_snapshot_id must be a string"),
        ("before_snapshot_sha256", None, "before_snapshot_sha256 must be a string"),
        ("before_state_sha256", None, "before_state_sha256 must be a string"),
        ("before_tick", None, "before_tick must be an integer"),
        ("after_snapshot_id", None, "after_snapshot_id must be a string"),
        ("after_snapshot_sha256", None, "after_snapshot_sha256 must be a string"),
        ("after_state_sha256", None, "after_state_sha256 must be a string"),
        ("after_tick", None, "after_tick must be an integer"),
        ("previous_transition_sha256", 7, "previous_transition_sha256 must be a string"),
    ],
)
def test_state_transition_mapping_rejects_invalid_scalar_types(
    field: str,
    value: object,
    message: str,
) -> None:
    mapping = _transition().to_validator_mapping()
    mapping[field] = value

    with pytest.raises(TransitionError, match=message):
        StateTransition.from_mapping(mapping)


def test_state_transition_mapping_validates_all_derived_fields() -> None:
    mapping = _transition().to_validator_mapping()

    bad_status = copy.deepcopy(mapping)
    bad_status["status"] = "UNCHANGED"
    with pytest.raises(TransitionError, match="declared status does not match"):
        StateTransition.from_mapping(bad_status)

    unsupported_status = copy.deepcopy(mapping)
    unsupported_status["status"] = "PARTIAL"
    with pytest.raises(TransitionError, match=r"unsupported state transition.status"):
        StateTransition.from_mapping(unsupported_status)

    bad_count = copy.deepcopy(mapping)
    bad_count["change_count"] = 999
    with pytest.raises(TransitionError, match="declared change_count does not match"):
        StateTransition.from_mapping(bad_count)

    bad_change_hash = copy.deepcopy(mapping)
    bad_change_hash["change_set_sha256"] = "0" * 64
    with pytest.raises(TransitionError, match="declared change_set_sha256 does not match"):
        StateTransition.from_mapping(bad_change_hash)

    bad_transition_hash = copy.deepcopy(mapping)
    bad_transition_hash["transition_sha256"] = "0" * 64
    with pytest.raises(TransitionError, match="declared transition_sha256 does not match"):
        StateTransition.from_mapping(bad_transition_hash)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("status", 7, "status must be a string"),
        ("change_count", True, "change_count must be an integer"),
        ("change_set_sha256", None, "change_set_sha256 must be a string"),
        ("transition_sha256", None, "transition_sha256 must be a string"),
    ],
)
def test_state_transition_mapping_rejects_derived_field_types(
    field: str,
    value: object,
    message: str,
) -> None:
    mapping = _transition().to_validator_mapping()
    mapping[field] = value

    with pytest.raises(TransitionError, match=message):
        StateTransition.from_mapping(mapping)


def test_state_transition_mapping_detects_nested_change_tampering() -> None:
    mapping = _transition().to_validator_mapping()
    changes = mapping["changes"]
    assert isinstance(changes, list)
    change = changes[0]
    assert isinstance(change, dict)
    change["path"] = "/tampered"

    with pytest.raises(TransitionError, match="declared change_sha256 does not match"):
        StateTransition.from_mapping(mapping)


def test_validate_state_transition_accepts_exact_pair_and_rejects_mismatch() -> None:
    before, after = _snapshot_pair()
    transition = create_state_transition(
        before,
        after,
        transition_id="TRANSITION-FOUND-001-000",
        causes=(_source(),),
    )

    assert validate_state_transition(transition, before, after) is None

    changed = replace(transition, after_tick=transition.after_tick - 1)
    with pytest.raises(TransitionError, match="does not match its referenced snapshots"):
        validate_state_transition(changed, before, after)


def test_validate_state_transition_rejects_invalid_runtime_transition() -> None:
    before, after = _snapshot_pair()

    with pytest.raises(TransitionError, match="transition must be a StateTransition"):
        validate_state_transition("transition", before, after)  # type: ignore[arg-type]


def test_empty_transition_series_has_stable_identity_and_round_trip() -> None:
    series = create_transition_series(_RUN_ID, _SCENARIO_ID)

    assert series.transitions == ()
    assert series.transition_count == 0
    assert series.terminal_transition_sha256 is None
    assert series.series_sha256 == calculate_transition_series_sha256(series)
    assert TransitionSeries.from_mapping(series.to_validator_mapping()) == series


def test_append_transition_builds_immutable_hash_chain() -> None:
    series = _series(3)

    assert series.transition_count == 3
    assert series.transitions[0].sequence == 0
    assert series.transitions[0].previous_transition_sha256 is None
    assert (
        series.transitions[1].previous_transition_sha256 == series.transitions[0].transition_sha256
    )
    assert (
        series.transitions[2].previous_transition_sha256 == series.transitions[1].transition_sha256
    )
    assert series.terminal_transition_sha256 == series.transitions[-1].transition_sha256


def test_append_transition_does_not_mutate_original_series() -> None:
    before, after = _snapshot_pair()
    empty = create_transition_series(_RUN_ID, _SCENARIO_ID)

    appended = append_state_transition(
        empty,
        transition_id="TRANSITION-FOUND-001-000",
        before=before,
        after=after,
    )

    assert empty.transitions == ()
    assert appended.transition_count == 1


def test_append_transition_rejects_invalid_series_and_snapshot_identity() -> None:
    before, after = _snapshot_pair()

    with pytest.raises(TransitionError, match="series must be a TransitionSeries"):
        append_state_transition(  # type: ignore[arg-type]
            "series",
            transition_id="TRANSITION-001",
            before=before,
            after=after,
        )

    series = create_transition_series("AURORA-RUN-FOUND-001-OTHER", _SCENARIO_ID)
    with pytest.raises(TransitionError, match="snapshot identity does not match"):
        append_state_transition(
            series,
            transition_id="TRANSITION-001",
            before=before,
            after=after,
        )


def test_transition_series_rejects_invalid_container_and_members() -> None:
    with pytest.raises(TransitionError, match="transitions must be a tuple"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, [])  # type: ignore[arg-type]

    with pytest.raises(TransitionError, match="transitions must be a tuple"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, ("transition",))  # type: ignore[arg-type]


def test_transition_series_rejects_identity_and_sequence_mismatch() -> None:
    transition = _transition()

    with pytest.raises(TransitionError, match="identity does not match"):
        TransitionSeries("AURORA-RUN-FOUND-001-OTHER", _SCENARIO_ID, (transition,))

    later = _transition(sequence=1)
    with pytest.raises(TransitionError, match="sequence must be contiguous"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, (later,))


def test_transition_series_rejects_duplicate_transition_ids() -> None:
    series = _series(2)
    duplicate = replace(
        series.transitions[1],
        transition_id=series.transitions[0].transition_id,
    )

    with pytest.raises(TransitionError, match="transition_id values must be unique"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, (series.transitions[0], duplicate))


def test_transition_series_retains_defensive_first_hash_check(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(StateTransition, "__post_init__", lambda self: None)
    transition = _transition()
    transition = replace(transition, previous_transition_sha256="a" * 64)

    with pytest.raises(TransitionError, match="first series transition must not reference"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, (transition,))


def test_transition_series_rejects_decreasing_after_ticks() -> None:
    series = _series(2)
    first = replace(series.transitions[0], after_tick=5)
    second = replace(
        series.transitions[1],
        previous_transition_sha256=first.transition_sha256,
        after_tick=4,
    )

    with pytest.raises(TransitionError, match="nondecreasing after_tick"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, (first, second))


def test_transition_series_rejects_broken_hash_chain() -> None:
    series = _series(2)
    changed = replace(series.transitions[1], previous_transition_sha256="0" * 64)

    with pytest.raises(TransitionError, match="hash chain does not match"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, (series.transitions[0], changed))


def test_transition_series_rejects_duplicate_snapshot_edges() -> None:
    series = _series(2)
    duplicate_edge = replace(
        series.transitions[1],
        before_snapshot_sha256=series.transitions[0].before_snapshot_sha256,
        after_snapshot_sha256=series.transitions[0].after_snapshot_sha256,
        domain=series.transitions[0].domain,
        subject_id=series.transitions[0].subject_id,
        previous_transition_sha256=series.transitions[0].transition_sha256,
    )

    with pytest.raises(TransitionError, match="duplicate snapshot edge"):
        TransitionSeries(_RUN_ID, _SCENARIO_ID, (series.transitions[0], duplicate_edge))


def test_transition_series_allows_equal_after_ticks_for_distinct_edges() -> None:
    series = _series(2)
    first = replace(series.transitions[0], after_tick=2)
    second = replace(
        series.transitions[1],
        after_tick=2,
        previous_transition_sha256=first.transition_sha256,
    )

    rebuilt = TransitionSeries(_RUN_ID, _SCENARIO_ID, (first, second))

    assert rebuilt.transition_count == 2


def test_transition_series_hash_is_deterministic_and_content_sensitive() -> None:
    first = _series(3)
    equivalent = _series(3)
    changed_last = replace(first.transitions[-1], causes=())
    changed = TransitionSeries(
        first.run_id,
        first.scenario_id,
        (*first.transitions[:-1], changed_last),
    )

    assert first.series_sha256 == equivalent.series_sha256
    assert first.series_sha256 == calculate_transition_series_sha256(first)
    assert first.series_sha256 != changed.series_sha256


def test_transition_series_round_trips_complete_chain() -> None:
    series = _series(4)

    restored = TransitionSeries.from_mapping(series.to_validator_mapping())

    assert restored == series
    assert restored.series_sha256 == series.series_sha256


def test_transition_series_mapping_has_complete_envelope() -> None:
    series = _series(2)
    mapping = series.to_validator_mapping()

    assert mapping == {
        "run_id": _RUN_ID,
        "scenario_id": _SCENARIO_ID,
        "series_sha256": series.series_sha256,
        "series_type": "TRANSITION_SERIES",
        "terminal_transition_sha256": series.terminal_transition_sha256,
        "transition_count": 2,
        "transition_schema_version": "1.0",
        "transitions": [transition.to_validator_mapping() for transition in series.transitions],
    }


def test_transition_series_mapping_requires_exact_schema() -> None:
    mapping = _series().to_validator_mapping()

    missing = copy.deepcopy(mapping)
    del missing["transitions"]
    with pytest.raises(TransitionError, match="missing required field"):
        TransitionSeries.from_mapping(missing)

    unknown = copy.deepcopy(mapping)
    unknown["unexpected"] = True
    with pytest.raises(TransitionError, match="contains unknown field"):
        TransitionSeries.from_mapping(unknown)

    with pytest.raises(TransitionError, match="transition series must be a JSON object"):
        TransitionSeries.from_mapping([])  # type: ignore[arg-type]


def test_transition_series_mapping_rejects_version_and_type() -> None:
    mapping = _series().to_validator_mapping()

    bad_version = copy.deepcopy(mapping)
    bad_version["transition_schema_version"] = "2.0"
    with pytest.raises(TransitionError, match="unsupported transition_schema_version"):
        TransitionSeries.from_mapping(bad_version)

    non_string_version = copy.deepcopy(mapping)
    non_string_version["transition_schema_version"] = 1
    with pytest.raises(TransitionError, match="transition_schema_version must be a string"):
        TransitionSeries.from_mapping(non_string_version)

    bad_type = copy.deepcopy(mapping)
    bad_type["series_type"] = "OTHER"
    with pytest.raises(TransitionError, match="unsupported series_type"):
        TransitionSeries.from_mapping(bad_type)


def test_transition_series_mapping_rejects_identity_and_transition_array() -> None:
    mapping = _series().to_validator_mapping()

    bad_run = copy.deepcopy(mapping)
    bad_run["run_id"] = 7
    with pytest.raises(TransitionError, match=r"transition series.run_id must be a string"):
        TransitionSeries.from_mapping(bad_run)

    bad_scenario = copy.deepcopy(mapping)
    bad_scenario["scenario_id"] = None
    with pytest.raises(
        TransitionError,
        match=r"transition series.scenario_id must be a string",
    ):
        TransitionSeries.from_mapping(bad_scenario)

    bad_array = copy.deepcopy(mapping)
    bad_array["transitions"] = {}
    with pytest.raises(TransitionError, match="transitions must be a JSON array"):
        TransitionSeries.from_mapping(bad_array)

    bad_member = copy.deepcopy(mapping)
    bad_member["transitions"] = [[]]
    with pytest.raises(TransitionError, match=r"transitions\[0\] must be a JSON object"):
        TransitionSeries.from_mapping(bad_member)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("transition_count", True, "transition_count must be an integer"),
        ("terminal_transition_sha256", 7, "terminal_transition_sha256 must be a string"),
        ("series_sha256", None, "series_sha256 must be a string"),
    ],
)
def test_transition_series_mapping_rejects_derived_field_types(
    field: str,
    value: object,
    message: str,
) -> None:
    mapping = _series().to_validator_mapping()
    mapping[field] = value

    with pytest.raises(TransitionError, match=message):
        TransitionSeries.from_mapping(mapping)


def test_transition_series_mapping_rejects_derived_value_mismatches() -> None:
    mapping = _series().to_validator_mapping()

    bad_count = copy.deepcopy(mapping)
    bad_count["transition_count"] = 99
    with pytest.raises(TransitionError, match="declared transition_count does not match"):
        TransitionSeries.from_mapping(bad_count)

    bad_terminal = copy.deepcopy(mapping)
    bad_terminal["terminal_transition_sha256"] = "0" * 64
    with pytest.raises(
        TransitionError,
        match="declared terminal_transition_sha256 does not match",
    ):
        TransitionSeries.from_mapping(bad_terminal)

    bad_hash = copy.deepcopy(mapping)
    bad_hash["series_sha256"] = "0" * 64
    with pytest.raises(TransitionError, match="declared series_sha256 does not match"):
        TransitionSeries.from_mapping(bad_hash)


def test_transition_series_mapping_detects_nested_transition_tampering() -> None:
    mapping = _series().to_validator_mapping()
    transitions = mapping["transitions"]
    assert isinstance(transitions, list)
    transition = transitions[-1]
    assert isinstance(transition, dict)
    transition["after_tick"] = 999

    with pytest.raises(TransitionError, match="declared transition_sha256 does not match"):
        TransitionSeries.from_mapping(mapping)


def test_transition_source_binds_transition_identity_and_digest() -> None:
    transition = _transition()

    source = create_transition_source(transition)

    assert source.source_kind is EvidenceSourceKind.TRANSITION
    assert source.source_id == transition.transition_id
    assert source.source_sha256 == transition.transition_sha256


def test_transition_evidence_payload_is_compact_and_hash_verified() -> None:
    transition = _transition(causes=(_source(),))

    payload = create_transition_evidence_payload(transition)

    assert payload.decode() == transition.to_evidence_mapping()
    assert "changes" not in payload.decode()
    assert payload.payload_sha256 == hashlib.sha256(payload.payload_json).hexdigest()


def test_transition_integrates_with_append_only_evidence_ledger() -> None:
    transition = _transition(causes=(_source(),))
    ledger = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)

    ledger = append_evidence_record(
        ledger,
        record_id="EVIDENCE-TRANSITION-000",
        observed_at_tick=transition.after_tick,
        recorded_at_tick=transition.after_tick,
        kind=EvidenceKind.STATE_TRANSITION,
        domain=transition.domain,
        producer_id="HARNESS-RUNTIME",
        payload=create_transition_evidence_payload(transition),
        sources=(create_transition_source(transition),),
    )

    record = ledger.records[0]
    assert record.kind is EvidenceKind.STATE_TRANSITION
    assert record.sources[0].source_kind is EvidenceSourceKind.TRANSITION
    assert record.sources[0].source_sha256 == transition.transition_sha256


@pytest.mark.parametrize(
    "function",
    [
        create_transition_source,
        create_transition_evidence_payload,
        calculate_state_transition_sha256,
    ],
)
def test_transition_functions_reject_invalid_runtime_transition(function: object) -> None:
    with pytest.raises(TransitionError, match="transition must be a StateTransition"):
        function("transition")  # type: ignore[operator]


def test_transition_series_hash_function_rejects_invalid_runtime_type() -> None:
    with pytest.raises(TransitionError, match="series must be a TransitionSeries"):
        calculate_transition_series_sha256("series")  # type: ignore[arg-type]


def test_transition_dataclasses_are_frozen() -> None:
    value = _value()
    change = _change()
    transition = _transition()
    series = _series()

    with pytest.raises(FrozenInstanceError):
        value.value_sha256 = "0" * 64  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        change.path = "/other"  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        transition.sequence = 2  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        series.transitions = ()  # type: ignore[misc]


def test_transition_module_has_no_aurora_projection_api() -> None:
    assert not hasattr(StateChange, "to_aurora_mapping")
    assert not hasattr(StateTransition, "to_aurora_mapping")
    assert not hasattr(TransitionSeries, "to_aurora_mapping")
    assert not hasattr(transitions_module, "project_transition_for_aurora")


def test_transition_module_exports_stable_public_surface() -> None:
    assert set(transitions_module.__all__) == {
        "DEFAULT_MAX_TRANSITION_CHANGES",
        "DEFAULT_MAX_TRANSITION_VALUE_BYTES",
        "MAX_TICK",
        "MAX_TRANSITION_CAUSES",
        "MAX_TRANSITION_CHANGES",
        "MAX_TRANSITION_VALUE_BYTES",
        "SUPPORTED_TRANSITION_SCHEMA_VERSION",
        "ChangeOperation",
        "StateChange",
        "StateTransition",
        "TransitionError",
        "TransitionSeries",
        "TransitionStatus",
        "TransitionValue",
        "append_state_transition",
        "calculate_state_transition_sha256",
        "calculate_transition_series_sha256",
        "create_state_transition",
        "create_transition_evidence_payload",
        "create_transition_series",
        "create_transition_source",
        "create_transition_value",
        "derive_state_changes",
        "validate_state_transition",
    }
