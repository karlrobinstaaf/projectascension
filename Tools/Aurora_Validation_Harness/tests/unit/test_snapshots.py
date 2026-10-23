"""Unit tests for deterministic state snapshots and append-only snapshot series."""

from __future__ import annotations

import copy
import hashlib
from dataclasses import FrozenInstanceError, replace
from types import MappingProxyType

import pytest

from aurora_validation_harness import snapshots as snapshots_module
from aurora_validation_harness.evidence import (
    EvidenceDomain,
    EvidenceKind,
    EvidenceSourceKind,
    append_evidence_record,
    create_evidence_ledger,
)
from aurora_validation_harness.snapshots import (
    DEFAULT_MAX_SNAPSHOT_STATE_BYTES,
    MAX_SNAPSHOT_STATE_BYTES,
    MAX_TICK,
    SUPPORTED_SNAPSHOT_SCHEMA_VERSION,
    SnapshotError,
    SnapshotPhase,
    SnapshotSeries,
    SnapshotState,
    StateSnapshot,
    append_state_snapshot,
    calculate_snapshot_series_sha256,
    calculate_state_snapshot_sha256,
    create_snapshot_evidence_payload,
    create_snapshot_series,
    create_snapshot_source,
    create_snapshot_state,
)

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_RUN_ID = "AURORA-RUN-FOUND-001-001"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"


def _state(data: dict[str, object] | None = None) -> SnapshotState:
    return create_snapshot_state(
        {
            "beliefs": {"Mara_location": {"confidence": None, "value": "UNKNOWN"}},
            "identity": {"aurora_id": "AURORA"},
        }
        if data is None
        else data
    )


def _snapshot(
    *,
    snapshot_id: str = "SNAPSHOT-FOUND-001-000",
    run_id: str = _RUN_ID,
    scenario_id: str = _SCENARIO_ID,
    sequence: int = 0,
    captured_at_tick: int = 0,
    phase: SnapshotPhase = SnapshotPhase.INITIAL,
    domain: EvidenceDomain = EvidenceDomain.AURORA_STATE,
    subject_id: str = "AURORA",
    producer_id: str = "HARNESS-RUNTIME",
    checkpoint_id: str | None = "CP0",
    state: SnapshotState | None = None,
    previous_snapshot_sha256: str | None = None,
) -> StateSnapshot:
    if sequence > 0 and previous_snapshot_sha256 is None:
        previous_snapshot_sha256 = "b" * 64
    return StateSnapshot(
        snapshot_id=snapshot_id,
        run_id=run_id,
        scenario_id=scenario_id,
        sequence=sequence,
        captured_at_tick=captured_at_tick,
        phase=phase,
        domain=domain,
        subject_id=subject_id,
        producer_id=producer_id,
        checkpoint_id=checkpoint_id,
        state=_state() if state is None else state,
        previous_snapshot_sha256=previous_snapshot_sha256,
    )


def _append(
    series: SnapshotSeries,
    index: int,
    *,
    tick: int | None = None,
    phase: SnapshotPhase = SnapshotPhase.CHECKPOINT,
    domain: EvidenceDomain = EvidenceDomain.AURORA_STATE,
    subject_id: str = "AURORA",
    producer_id: str = "HARNESS-RUNTIME",
    checkpoint_id: str | None = None,
    state: SnapshotState | None = None,
) -> SnapshotSeries:
    resolved_checkpoint = f"CP{index}" if checkpoint_id is None else checkpoint_id
    return append_state_snapshot(
        series,
        snapshot_id=f"SNAPSHOT-FOUND-001-{index:03d}",
        captured_at_tick=index if tick is None else tick,
        phase=phase,
        domain=domain,
        subject_id=subject_id,
        producer_id=producer_id,
        checkpoint_id=resolved_checkpoint,
        state=_state({"index": index}) if state is None else state,
    )


def _series(snapshot_count: int = 3) -> SnapshotSeries:
    series = create_snapshot_series(_RUN_ID, _SCENARIO_ID)
    for index in range(snapshot_count):
        phase = SnapshotPhase.INITIAL if index == 0 else SnapshotPhase.CHECKPOINT
        series = _append(series, index, phase=phase)
    return series


def _raw_state(state_json: bytes, *, digest: object | None = None) -> SnapshotState:
    return SnapshotState(
        state_json=state_json,
        state_sha256=(hashlib.sha256(state_json).hexdigest() if digest is None else digest),
    )


def test_public_constants_define_schema_and_bounded_limits() -> None:
    assert SUPPORTED_SNAPSHOT_SCHEMA_VERSION == "1.0"
    assert DEFAULT_MAX_SNAPSHOT_STATE_BYTES == 4_194_304
    assert MAX_SNAPSHOT_STATE_BYTES == 16_777_216
    assert MAX_TICK == (1 << 63) - 1
    assert 0 < DEFAULT_MAX_SNAPSHOT_STATE_BYTES < MAX_SNAPSHOT_STATE_BYTES < MAX_TICK


def test_snapshot_phase_values_are_stable() -> None:
    assert {phase.value for phase in SnapshotPhase} == {
        "INITIAL",
        "PRE_EVENT",
        "POST_EVENT",
        "CHECKPOINT",
        "FINAL",
        "FAILURE",
    }


@pytest.mark.parametrize(
    "value",
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
def test_snapshot_state_accepts_supported_nested_json_values(value: object) -> None:
    state = create_snapshot_state({"value": value})

    assert state.decode() == {"value": value}
    assert state.size_bytes == len(state.state_json)
    assert state.state_sha256 == hashlib.sha256(state.state_json).hexdigest()
    assert state.to_mapping() == {
        "data": {"value": value},
        "state_sha256": state.state_sha256,
    }


def test_snapshot_state_accepts_generic_mapping_and_canonicalizes_unicode() -> None:
    data = MappingProxyType(
        {
            "z": "ö",
            "a": MappingProxyType({"β": [2, 1]}),
        }
    )

    state = create_snapshot_state(data)

    assert state.state_json == '{"a":{"β":[2,1]},"z":"ö"}'.encode()


def test_snapshot_state_is_detached_from_mutable_input_and_decodes_fresh_values() -> None:
    data: dict[str, object] = {"belief": {"value": "UNKNOWN"}, "history": ["T0"]}
    state = create_snapshot_state(data)
    expected_hash = state.state_sha256

    belief = data["belief"]
    assert isinstance(belief, dict)
    belief["value"] = "Cargo_Bay_7"
    history = data["history"]
    assert isinstance(history, list)
    history.append("T1")

    first_decode = state.decode()
    first_belief = first_decode["belief"]
    assert isinstance(first_belief, dict)
    first_belief["value"] = "tampered"

    assert state.decode() == {"belief": {"value": "UNKNOWN"}, "history": ["T0"]}
    assert state.state_sha256 == expected_hash


def test_snapshot_state_hash_is_deterministic_across_mapping_order() -> None:
    first = create_snapshot_state({"b": 2, "a": {"y": 2, "x": 1}})
    second = create_snapshot_state({"a": {"x": 1, "y": 2}, "b": 2})

    assert first == second
    assert first.state_sha256 == second.state_sha256


def test_snapshot_state_default_limit_is_an_explicit_smaller_boundary() -> None:
    data = {"value": "x" * DEFAULT_MAX_SNAPSHOT_STATE_BYTES}

    with pytest.raises(SnapshotError, match="snapshot state must not exceed"):
        create_snapshot_state(data)

    state = create_snapshot_state(data, max_state_bytes=MAX_SNAPSHOT_STATE_BYTES)
    assert state.size_bytes > DEFAULT_MAX_SNAPSHOT_STATE_BYTES


@pytest.mark.parametrize("max_state_bytes", [True, False, 1.5, "1024", None])
def test_snapshot_state_rejects_non_integer_size_limit(max_state_bytes: object) -> None:
    with pytest.raises(SnapshotError, match="max_state_bytes must be an integer"):
        create_snapshot_state({"value": 1}, max_state_bytes=max_state_bytes)  # type: ignore[arg-type]


@pytest.mark.parametrize("max_state_bytes", [0, -1, MAX_SNAPSHOT_STATE_BYTES + 1])
def test_snapshot_state_rejects_out_of_range_size_limit(max_state_bytes: int) -> None:
    with pytest.raises(SnapshotError, match="max_state_bytes must be between"):
        create_snapshot_state({"value": 1}, max_state_bytes=max_state_bytes)


def test_snapshot_state_enforces_configured_size_limit() -> None:
    with pytest.raises(SnapshotError, match="snapshot state must not exceed 8 bytes"):
        create_snapshot_state({"value": "large"}, max_state_bytes=8)


@pytest.mark.parametrize("data", [[], "state", 7, None])
def test_snapshot_state_requires_top_level_mapping(data: object) -> None:
    with pytest.raises(SnapshotError, match="snapshot state data must be a JSON object"):
        create_snapshot_state(data)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "value",
    [
        ("tuple",),
        {"set"},
        b"bytes",
        object(),
    ],
)
def test_snapshot_state_rejects_unsupported_json_value_types(value: object) -> None:
    with pytest.raises(SnapshotError, match="unsupported JSON value type"):
        create_snapshot_state({"nested": [value]})


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_snapshot_state_rejects_non_finite_numbers(value: float) -> None:
    with pytest.raises(SnapshotError, match="contains a non-finite number"):
        create_snapshot_state({"nested": [{"value": value}]})


def test_snapshot_state_rejects_non_string_object_keys() -> None:
    with pytest.raises(SnapshotError, match="contains a non-string object key"):
        create_snapshot_state({"nested": {1: "value"}})  # type: ignore[dict-item]


def test_snapshot_state_round_trips_through_mapping() -> None:
    state = _state({"identity": {"id": "AURORA"}, "uncertainty": 0.8})

    restored = SnapshotState.from_mapping(MappingProxyType(state.to_mapping()))

    assert restored == state
    assert restored is not state


def test_snapshot_state_mapping_requires_exact_schema() -> None:
    mapping = _state().to_mapping()

    missing = dict(mapping)
    del missing["data"]
    with pytest.raises(SnapshotError, match="missing required field"):
        SnapshotState.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(SnapshotError, match="contains unknown field"):
        SnapshotState.from_mapping(unknown)


def test_snapshot_state_mapping_rejects_invalid_root_data_and_digest() -> None:
    mapping = _state().to_mapping()

    with pytest.raises(SnapshotError, match="snapshot state must be a JSON object"):
        SnapshotState.from_mapping([])  # type: ignore[arg-type]

    non_string_key = {1: "bad"}
    with pytest.raises(SnapshotError, match="must use string keys"):
        SnapshotState.from_mapping(non_string_key)  # type: ignore[arg-type]

    invalid_data = dict(mapping)
    invalid_data["data"] = []
    with pytest.raises(SnapshotError, match=r"snapshot state.data must be a JSON object"):
        SnapshotState.from_mapping(invalid_data)

    invalid_digest = dict(mapping)
    invalid_digest["state_sha256"] = 7
    with pytest.raises(SnapshotError, match="state_sha256 must be a string"):
        SnapshotState.from_mapping(invalid_digest)

    mismatched_digest = dict(mapping)
    mismatched_digest["state_sha256"] = "0" * 64
    with pytest.raises(SnapshotError, match="declared state_sha256 does not match"):
        SnapshotState.from_mapping(mismatched_digest)


def test_snapshot_state_constructor_rejects_non_bytes_and_bad_digest_shapes() -> None:
    with pytest.raises(SnapshotError, match="state_json must be bytes"):
        SnapshotState(state_json="{}", state_sha256="0" * 64)  # type: ignore[arg-type]

    with pytest.raises(SnapshotError, match="state_sha256 must be a string"):
        _raw_state(b"{}", digest=7)

    with pytest.raises(SnapshotError, match="lowercase 64-character"):
        _raw_state(b"{}", digest="ABC")

    with pytest.raises(SnapshotError, match="does not match state_json"):
        _raw_state(b"{}", digest="0" * 64)


@pytest.mark.parametrize(
    ("state_json", "message"),
    [
        (b"\xff", "not valid JSON"),
        (b"{", "not valid JSON"),
        (b"NaN", "not valid JSON"),
        (b"[]", "must encode a JSON object"),
        (b'{"b":2, "a":1}', "canonical JSON encoding"),
    ],
)
def test_snapshot_state_constructor_rejects_invalid_or_noncanonical_json(
    state_json: bytes,
    message: str,
) -> None:
    with pytest.raises(SnapshotError, match=message):
        _raw_state(state_json)


def test_snapshot_state_constructor_enforces_absolute_size_limit(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(snapshots_module, "MAX_SNAPSHOT_STATE_BYTES", 1)

    with pytest.raises(SnapshotError, match="state_json must not exceed 1 bytes"):
        _raw_state(b"{}")


def test_private_canonicalizer_wraps_serialization_errors() -> None:
    with pytest.raises(SnapshotError, match="value is not JSON-serializable"):
        snapshots_module._canonical_json_bytes({1: object()})


def test_private_normalizer_retains_defensive_unsupported_branch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(snapshots_module, "_validate_json_value", lambda *_args, **_kwargs: None)

    with pytest.raises(SnapshotError, match="unsupported JSON value type"):
        snapshots_module._normalize_json_value(object(), path="state")


def test_create_snapshot_state_rejects_non_object_normalizer_result(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        snapshots_module,
        "_normalize_json_value",
        lambda *_args, **_kwargs: [],
    )

    with pytest.raises(SnapshotError, match="snapshot state data must be a JSON object"):
        create_snapshot_state({"value": 1})


@pytest.mark.parametrize("phase", list(SnapshotPhase))
def test_state_snapshot_accepts_every_capture_phase(phase: SnapshotPhase) -> None:
    checkpoint_id = "CP1" if phase is SnapshotPhase.CHECKPOINT else None
    snapshot = _snapshot(phase=phase, checkpoint_id=checkpoint_id)

    assert snapshot.phase is phase


@pytest.mark.parametrize("domain", list(EvidenceDomain))
def test_state_snapshot_accepts_every_evidence_domain(domain: EvidenceDomain) -> None:
    snapshot = _snapshot(domain=domain)

    assert snapshot.domain is domain


def test_state_snapshot_mapping_contains_complete_validator_contract() -> None:
    snapshot = _snapshot()
    mapping = snapshot.to_validator_mapping()

    assert mapping == {
        "captured_at_tick": 0,
        "checkpoint_id": "CP0",
        "domain": "AURORA_STATE",
        "phase": "INITIAL",
        "previous_snapshot_sha256": None,
        "producer_id": "HARNESS-RUNTIME",
        "run_id": _RUN_ID,
        "scenario_id": _SCENARIO_ID,
        "sequence": 0,
        "snapshot_id": "SNAPSHOT-FOUND-001-000",
        "snapshot_schema_version": "1.0",
        "snapshot_sha256": snapshot.snapshot_sha256,
        "snapshot_type": "STATE_SNAPSHOT",
        "state": snapshot.state.to_mapping(),
        "subject_id": "AURORA",
    }


def test_state_snapshot_evidence_mapping_is_compact_and_excludes_state() -> None:
    snapshot = _snapshot()

    mapping = snapshot.to_evidence_mapping()

    assert mapping == {
        "captured_at_tick": 0,
        "checkpoint_id": "CP0",
        "domain": "AURORA_STATE",
        "phase": "INITIAL",
        "snapshot_id": snapshot.snapshot_id,
        "snapshot_sha256": snapshot.snapshot_sha256,
        "state_sha256": snapshot.state.state_sha256,
        "state_size_bytes": snapshot.state.size_bytes,
        "subject_id": "AURORA",
    }
    assert "state" not in mapping
    assert "run_id" not in mapping
    assert "scenario_id" not in mapping


def test_state_snapshot_hash_is_deterministic_and_provenance_sensitive() -> None:
    first = _snapshot()
    equivalent = _snapshot()
    changed_state = _snapshot(state=_state({"belief": "KNOWN"}))
    changed_run = _snapshot(run_id="AURORA-RUN-FOUND-001-002")

    assert first.snapshot_sha256 == equivalent.snapshot_sha256
    assert first.snapshot_sha256 == calculate_state_snapshot_sha256(first)
    assert first.snapshot_sha256 != changed_state.snapshot_sha256
    assert first.snapshot_sha256 != changed_run.snapshot_sha256


def test_identical_state_has_stable_content_hash_across_runs_but_distinct_snapshot_hash() -> None:
    state = _state({"belief": "UNKNOWN"})
    first = _snapshot(run_id="AURORA-RUN-FOUND-001-001", state=state)
    second = _snapshot(run_id="AURORA-RUN-FOUND-001-002", state=state)

    assert first.state.state_sha256 == second.state.state_sha256
    assert first.snapshot_sha256 != second.snapshot_sha256


def test_state_snapshot_allows_semantically_invalid_state_to_be_captured() -> None:
    contaminated = _state(
        {
            "belief": {"Mara_location": "Cargo_Bay_7"},
            "expected_result": "UNKNOWN",
            "world_truth": {"Mara_location": "Cargo_Bay_7"},
        }
    )

    snapshot = _snapshot(domain=EvidenceDomain.AURORA_STATE, state=contaminated)

    assert snapshot.state.decode()["world_truth"] == {"Mara_location": "Cargo_Bay_7"}


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("snapshot_id", "bad", "uppercase identifier"),
        ("snapshot_id", 7, "snapshot_id must be a string"),
        ("run_id", "bad", "uppercase identifier"),
        ("run_id", None, "run_id must be a string"),
        ("scenario_id", "FOUND-001", "must match"),
        ("scenario_id", 7, "scenario_id must be a string"),
        ("sequence", True, "sequence must be an integer"),
        ("sequence", "0", "sequence must be an integer"),
        ("sequence", -1, "sequence must be non-negative"),
        ("captured_at_tick", True, "captured_at_tick must be an integer"),
        ("captured_at_tick", "0", "captured_at_tick must be an integer"),
        ("captured_at_tick", -1, "captured_at_tick must be between"),
        ("captured_at_tick", MAX_TICK + 1, "captured_at_tick must be between"),
        ("phase", "INITIAL", "phase must be a SnapshotPhase"),
        ("domain", "AURORA_STATE", "domain must be an EvidenceDomain"),
        ("subject_id", "bad subject", "unsupported identifier"),
        ("subject_id", 7, "subject_id must be a string"),
        ("producer_id", "bad", "uppercase identifier"),
        ("producer_id", 7, "producer_id must be a string"),
        ("checkpoint_id", "cp0", "uppercase identifier"),
        ("checkpoint_id", 7, "checkpoint_id must be a string"),
        ("state", {"value": 1}, "state must be a SnapshotState"),
    ],
)
def test_state_snapshot_rejects_invalid_fields(field: str, value: object, message: str) -> None:
    values: dict[str, object] = {
        "snapshot_id": "SNAPSHOT-FOUND-001-000",
        "run_id": _RUN_ID,
        "scenario_id": _SCENARIO_ID,
        "sequence": 0,
        "captured_at_tick": 0,
        "phase": SnapshotPhase.INITIAL,
        "domain": EvidenceDomain.AURORA_STATE,
        "subject_id": "AURORA",
        "producer_id": "HARNESS-RUNTIME",
        "checkpoint_id": "CP0",
        "state": _state(),
        "previous_snapshot_sha256": None,
    }
    values[field] = value

    with pytest.raises(SnapshotError, match=message):
        StateSnapshot(**values)  # type: ignore[arg-type]


def test_state_snapshot_requires_checkpoint_id_for_checkpoint_phase() -> None:
    with pytest.raises(SnapshotError, match="CHECKPOINT snapshot requires checkpoint_id"):
        _snapshot(phase=SnapshotPhase.CHECKPOINT, checkpoint_id=None)


def test_state_snapshot_validates_previous_hash_shape_and_chain_position() -> None:
    with pytest.raises(SnapshotError, match="previous_snapshot_sha256 must be a string"):
        _snapshot(sequence=1, previous_snapshot_sha256=7)  # type: ignore[arg-type]

    with pytest.raises(SnapshotError, match="lowercase 64-character"):
        _snapshot(sequence=1, previous_snapshot_sha256="ABC")

    with pytest.raises(SnapshotError, match="first state snapshot must not declare"):
        _snapshot(sequence=0, previous_snapshot_sha256="a" * 64)

    first = _snapshot()
    with pytest.raises(SnapshotError, match="non-first state snapshot requires"):
        replace(first, sequence=1, previous_snapshot_sha256=None)


def test_state_snapshot_round_trips_with_and_without_optional_fields() -> None:
    first = _snapshot(checkpoint_id=None)
    later = _snapshot(
        snapshot_id="SNAPSHOT-FOUND-001-001",
        sequence=1,
        captured_at_tick=4,
        phase=SnapshotPhase.POST_EVENT,
        checkpoint_id="CP1",
        previous_snapshot_sha256=first.snapshot_sha256,
    )

    assert StateSnapshot.from_mapping(first.to_validator_mapping()) == first
    assert StateSnapshot.from_mapping(later.to_validator_mapping()) == later


def test_state_snapshot_mapping_requires_exact_schema() -> None:
    mapping = _snapshot().to_validator_mapping()

    missing = dict(mapping)
    del missing["state"]
    with pytest.raises(SnapshotError, match="missing required field"):
        StateSnapshot.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(SnapshotError, match="contains unknown field"):
        StateSnapshot.from_mapping(unknown)

    with pytest.raises(SnapshotError, match="state snapshot must be a JSON object"):
        StateSnapshot.from_mapping([])  # type: ignore[arg-type]


@pytest.mark.parametrize("version", ["0.9", "2.0", "1.0-draft"])
def test_state_snapshot_mapping_rejects_unsupported_schema(version: str) -> None:
    mapping = _snapshot().to_validator_mapping()
    mapping["snapshot_schema_version"] = version

    with pytest.raises(SnapshotError, match="unsupported snapshot_schema_version"):
        StateSnapshot.from_mapping(mapping)


def test_state_snapshot_mapping_rejects_non_string_schema_version() -> None:
    mapping = _snapshot().to_validator_mapping()
    mapping["snapshot_schema_version"] = 1

    with pytest.raises(SnapshotError, match="snapshot_schema_version must be a string"):
        StateSnapshot.from_mapping(mapping)


def test_state_snapshot_mapping_rejects_invalid_type_enums_and_nested_state() -> None:
    mapping = _snapshot().to_validator_mapping()

    invalid_type = copy.deepcopy(mapping)
    invalid_type["snapshot_type"] = "OTHER"
    with pytest.raises(SnapshotError, match="unsupported snapshot_type"):
        StateSnapshot.from_mapping(invalid_type)

    invalid_phase = copy.deepcopy(mapping)
    invalid_phase["phase"] = "DURING_EVENT"
    with pytest.raises(SnapshotError, match=r"unsupported state snapshot.phase"):
        StateSnapshot.from_mapping(invalid_phase)

    non_string_phase = copy.deepcopy(mapping)
    non_string_phase["phase"] = 1
    with pytest.raises(SnapshotError, match=r"state snapshot.phase must be a string"):
        StateSnapshot.from_mapping(non_string_phase)

    invalid_domain = copy.deepcopy(mapping)
    invalid_domain["domain"] = "AURORA_PRIVATE"
    with pytest.raises(SnapshotError, match=r"unsupported state snapshot.domain"):
        StateSnapshot.from_mapping(invalid_domain)

    invalid_state = copy.deepcopy(mapping)
    invalid_state["state"] = []
    with pytest.raises(SnapshotError, match=r"state snapshot.state must be a JSON object"):
        StateSnapshot.from_mapping(invalid_state)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("snapshot_id", 7, "snapshot_id must be a string"),
        ("run_id", 7, "run_id must be a string"),
        ("scenario_id", 7, "scenario_id must be a string"),
        ("sequence", True, "sequence must be an integer"),
        ("captured_at_tick", None, "captured_at_tick must be an integer"),
        ("subject_id", None, "subject_id must be a string"),
        ("producer_id", None, "producer_id must be a string"),
        ("checkpoint_id", 7, "checkpoint_id must be a string"),
        ("previous_snapshot_sha256", 7, "previous_snapshot_sha256 must be a string"),
        ("snapshot_sha256", 7, "snapshot_sha256 must be a string"),
    ],
)
def test_state_snapshot_mapping_rejects_invalid_scalar_types(
    field: str,
    value: object,
    message: str,
) -> None:
    mapping = _snapshot().to_validator_mapping()
    mapping[field] = value

    with pytest.raises(SnapshotError, match=message):
        StateSnapshot.from_mapping(mapping)


def test_state_snapshot_mapping_detects_declared_hash_and_nested_state_tampering() -> None:
    mapping = _snapshot().to_validator_mapping()

    wrong_hash = copy.deepcopy(mapping)
    wrong_hash["snapshot_sha256"] = "0" * 64
    with pytest.raises(SnapshotError, match="declared snapshot_sha256 does not match"):
        StateSnapshot.from_mapping(wrong_hash)

    tampered_state = copy.deepcopy(mapping)
    state_mapping = tampered_state["state"]
    assert isinstance(state_mapping, dict)
    data = state_mapping["data"]
    assert isinstance(data, dict)
    data["hidden_state_marker"] = "tampered"
    with pytest.raises(SnapshotError, match="declared state_sha256 does not match"):
        StateSnapshot.from_mapping(tampered_state)


def test_empty_snapshot_series_has_stable_identity_and_round_trip() -> None:
    series = create_snapshot_series(_RUN_ID, _SCENARIO_ID)

    assert series.snapshots == ()
    assert series.snapshot_count == 0
    assert series.terminal_snapshot_sha256 is None
    assert series.series_sha256 == calculate_snapshot_series_sha256(series)
    assert SnapshotSeries.from_mapping(series.to_validator_mapping()) == series


def test_append_builds_immutable_hash_chain_with_nondecreasing_ticks() -> None:
    empty = create_snapshot_series(_RUN_ID, _SCENARIO_ID)
    first = _append(empty, 0, tick=0, phase=SnapshotPhase.INITIAL)
    second = _append(
        first,
        1,
        tick=0,
        phase=SnapshotPhase.PRE_EVENT,
        domain=EvidenceDomain.WORLD,
        subject_id="WORLD",
    )
    third = _append(second, 2, tick=5, phase=SnapshotPhase.POST_EVENT)

    assert empty.snapshots == ()
    assert len(first.snapshots) == 1
    assert len(second.snapshots) == 2
    assert len(third.snapshots) == 3
    assert third.snapshots[0].sequence == 0
    assert third.snapshots[0].previous_snapshot_sha256 is None
    assert third.snapshots[1].previous_snapshot_sha256 == third.snapshots[0].snapshot_sha256
    assert third.snapshots[2].previous_snapshot_sha256 == third.snapshots[1].snapshot_sha256
    assert third.terminal_snapshot_sha256 == third.snapshots[-1].snapshot_sha256


def test_append_accepts_snapshots_without_checkpoint_ids_when_phase_allows_it() -> None:
    series = create_snapshot_series(_RUN_ID, _SCENARIO_ID)
    series = append_state_snapshot(
        series,
        snapshot_id="SNAPSHOT-FOUND-001-FAILURE",
        captured_at_tick=0,
        phase=SnapshotPhase.FAILURE,
        domain=EvidenceDomain.AURORA_STATE,
        subject_id="AURORA",
        producer_id="HARNESS-RUNTIME",
        checkpoint_id=None,
        state=_state(),
    )

    assert series.snapshots[0].checkpoint_id is None


def test_append_rejects_invalid_runtime_series_type() -> None:
    with pytest.raises(SnapshotError, match="series must be a SnapshotSeries"):
        append_state_snapshot(  # type: ignore[arg-type]
            "series",
            snapshot_id="SNAPSHOT-001",
            captured_at_tick=0,
            phase=SnapshotPhase.INITIAL,
            domain=EvidenceDomain.AURORA_STATE,
            subject_id="AURORA",
            producer_id="HARNESS-RUNTIME",
            state=_state(),
        )


def test_snapshot_series_rejects_invalid_container_and_member_types() -> None:
    with pytest.raises(SnapshotError, match="snapshots must be a tuple"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, [])  # type: ignore[arg-type]

    with pytest.raises(SnapshotError, match="snapshots must be a tuple"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, ("snapshot",))  # type: ignore[arg-type]


def test_snapshot_series_rejects_snapshot_identity_mismatch() -> None:
    snapshot = _snapshot(run_id="AURORA-RUN-FOUND-001-OTHER")
    with pytest.raises(SnapshotError, match="identity does not match"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, (snapshot,))

    snapshot = _snapshot(scenario_id="AURORA-SCN-FOUND-002")
    with pytest.raises(SnapshotError, match="identity does not match"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, (snapshot,))


def test_snapshot_series_rejects_noncontiguous_sequence() -> None:
    snapshot = _snapshot(sequence=1)

    with pytest.raises(SnapshotError, match="sequence must be contiguous"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, (snapshot,))


def test_snapshot_series_rejects_duplicate_snapshot_ids() -> None:
    series = _series(2)
    duplicate = replace(series.snapshots[1], snapshot_id=series.snapshots[0].snapshot_id)

    with pytest.raises(SnapshotError, match="snapshot_id values must be unique"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, (series.snapshots[0], duplicate))


def test_snapshot_series_retains_defensive_first_hash_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(StateSnapshot, "__post_init__", lambda self: None)
    snapshot = StateSnapshot(
        snapshot_id="SNAPSHOT-FOUND-001-000",
        run_id=_RUN_ID,
        scenario_id=_SCENARIO_ID,
        sequence=0,
        captured_at_tick=0,
        phase=SnapshotPhase.INITIAL,
        domain=EvidenceDomain.AURORA_STATE,
        subject_id="AURORA",
        producer_id="HARNESS-RUNTIME",
        checkpoint_id="CP0",
        state=_state(),
        previous_snapshot_sha256="a" * 64,
    )

    with pytest.raises(SnapshotError, match="first series snapshot must not reference"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, (snapshot,))


def test_snapshot_series_rejects_decreasing_capture_ticks() -> None:
    series = _series(2)
    later = replace(series.snapshots[1], captured_at_tick=0)
    first = replace(series.snapshots[0], captured_at_tick=1)
    later = replace(later, previous_snapshot_sha256=first.snapshot_sha256)

    with pytest.raises(SnapshotError, match="nondecreasing captured_at_tick"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, (first, later))


def test_snapshot_series_rejects_broken_hash_chain() -> None:
    series = _series(2)
    changed = replace(series.snapshots[1], previous_snapshot_sha256="0" * 64)

    with pytest.raises(SnapshotError, match="hash chain does not match"):
        SnapshotSeries(_RUN_ID, _SCENARIO_ID, (series.snapshots[0], changed))


def test_snapshot_series_rejects_duplicate_checkpoint_capture_key() -> None:
    series = create_snapshot_series(_RUN_ID, _SCENARIO_ID)
    series = _append(series, 0, phase=SnapshotPhase.INITIAL, checkpoint_id="CP0")

    with pytest.raises(SnapshotError, match="duplicate phase, domain, and subject"):
        _append(series, 1, phase=SnapshotPhase.INITIAL, checkpoint_id="CP0")


def test_snapshot_series_allows_same_checkpoint_for_distinct_capture_dimensions() -> None:
    series = create_snapshot_series(_RUN_ID, _SCENARIO_ID)
    series = _append(series, 0, phase=SnapshotPhase.INITIAL, checkpoint_id="CP0")
    series = _append(
        series,
        1,
        phase=SnapshotPhase.INITIAL,
        domain=EvidenceDomain.WORLD,
        subject_id="WORLD",
        checkpoint_id="CP0",
    )
    series = _append(
        series,
        2,
        phase=SnapshotPhase.POST_EVENT,
        checkpoint_id="CP0",
    )

    assert series.snapshot_count == 3


def test_snapshot_series_hash_is_deterministic_and_snapshot_sensitive() -> None:
    first = _series(3)
    equivalent = _series(3)
    changed_last = replace(first.snapshots[-1], state=_state({"changed": True}))
    changed = SnapshotSeries(
        first.run_id,
        first.scenario_id,
        (*first.snapshots[:-1], changed_last),
    )

    assert first.series_sha256 == equivalent.series_sha256
    assert first.series_sha256 == calculate_snapshot_series_sha256(first)
    assert first.series_sha256 != changed.series_sha256


def test_snapshot_series_round_trips_complete_chain() -> None:
    series = _series(4)

    restored = SnapshotSeries.from_mapping(series.to_validator_mapping())

    assert restored == series
    assert restored.series_sha256 == series.series_sha256


def test_snapshot_series_mapping_has_exact_envelope() -> None:
    series = _series(2)
    mapping = series.to_validator_mapping()

    assert mapping == {
        "run_id": _RUN_ID,
        "scenario_id": _SCENARIO_ID,
        "series_sha256": series.series_sha256,
        "series_type": "SNAPSHOT_SERIES",
        "snapshot_count": 2,
        "snapshot_schema_version": "1.0",
        "snapshots": [snapshot.to_validator_mapping() for snapshot in series.snapshots],
        "terminal_snapshot_sha256": series.terminal_snapshot_sha256,
    }


def test_snapshot_series_mapping_requires_exact_schema() -> None:
    mapping = _series().to_validator_mapping()

    missing = copy.deepcopy(mapping)
    del missing["snapshots"]
    with pytest.raises(SnapshotError, match="missing required field"):
        SnapshotSeries.from_mapping(missing)

    unknown = copy.deepcopy(mapping)
    unknown["unexpected"] = True
    with pytest.raises(SnapshotError, match="contains unknown field"):
        SnapshotSeries.from_mapping(unknown)

    with pytest.raises(SnapshotError, match="snapshot series must be a JSON object"):
        SnapshotSeries.from_mapping([])  # type: ignore[arg-type]


def test_snapshot_series_mapping_rejects_version_type_and_series_type() -> None:
    mapping = _series().to_validator_mapping()

    unsupported_version = copy.deepcopy(mapping)
    unsupported_version["snapshot_schema_version"] = "2.0"
    with pytest.raises(SnapshotError, match="unsupported snapshot_schema_version"):
        SnapshotSeries.from_mapping(unsupported_version)

    non_string_version = copy.deepcopy(mapping)
    non_string_version["snapshot_schema_version"] = 1
    with pytest.raises(SnapshotError, match="snapshot_schema_version must be a string"):
        SnapshotSeries.from_mapping(non_string_version)

    unsupported_type = copy.deepcopy(mapping)
    unsupported_type["series_type"] = "SNAPSHOT_PACKAGE"
    with pytest.raises(SnapshotError, match="unsupported series_type"):
        SnapshotSeries.from_mapping(unsupported_type)


def test_snapshot_series_mapping_rejects_invalid_identity_and_snapshot_array() -> None:
    mapping = _series().to_validator_mapping()

    invalid_run = copy.deepcopy(mapping)
    invalid_run["run_id"] = 7
    with pytest.raises(SnapshotError, match=r"snapshot series.run_id must be a string"):
        SnapshotSeries.from_mapping(invalid_run)

    invalid_scenario = copy.deepcopy(mapping)
    invalid_scenario["scenario_id"] = None
    with pytest.raises(SnapshotError, match=r"snapshot series.scenario_id must be a string"):
        SnapshotSeries.from_mapping(invalid_scenario)

    invalid_array = copy.deepcopy(mapping)
    invalid_array["snapshots"] = {}
    with pytest.raises(SnapshotError, match="snapshots must be a JSON array"):
        SnapshotSeries.from_mapping(invalid_array)

    invalid_member = copy.deepcopy(mapping)
    invalid_member["snapshots"] = [[]]
    with pytest.raises(SnapshotError, match=r"snapshots\[0\] must be a JSON object"):
        SnapshotSeries.from_mapping(invalid_member)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("snapshot_count", True, "snapshot_count must be an integer"),
        ("terminal_snapshot_sha256", 7, "terminal_snapshot_sha256 must be a string"),
        ("series_sha256", None, "series_sha256 must be a string"),
    ],
)
def test_snapshot_series_mapping_rejects_invalid_derived_field_types(
    field: str,
    value: object,
    message: str,
) -> None:
    mapping = _series().to_validator_mapping()
    mapping[field] = value

    with pytest.raises(SnapshotError, match=message):
        SnapshotSeries.from_mapping(mapping)


def test_snapshot_series_mapping_rejects_derived_value_mismatches() -> None:
    mapping = _series().to_validator_mapping()

    wrong_count = copy.deepcopy(mapping)
    wrong_count["snapshot_count"] = 99
    with pytest.raises(SnapshotError, match="declared snapshot_count does not match"):
        SnapshotSeries.from_mapping(wrong_count)

    wrong_terminal = copy.deepcopy(mapping)
    wrong_terminal["terminal_snapshot_sha256"] = "0" * 64
    with pytest.raises(SnapshotError, match="declared terminal_snapshot_sha256 does not match"):
        SnapshotSeries.from_mapping(wrong_terminal)

    wrong_hash = copy.deepcopy(mapping)
    wrong_hash["series_sha256"] = "0" * 64
    with pytest.raises(SnapshotError, match="declared series_sha256 does not match"):
        SnapshotSeries.from_mapping(wrong_hash)


def test_snapshot_series_mapping_detects_nested_snapshot_tampering() -> None:
    mapping = _series().to_validator_mapping()
    snapshots = mapping["snapshots"]
    assert isinstance(snapshots, list)
    snapshot = snapshots[-1]
    assert isinstance(snapshot, dict)
    state = snapshot["state"]
    assert isinstance(state, dict)
    data = state["data"]
    assert isinstance(data, dict)
    data["index"] = 999

    with pytest.raises(SnapshotError, match="declared state_sha256 does not match"):
        SnapshotSeries.from_mapping(mapping)


def test_snapshot_source_binds_snapshot_identity_and_digest() -> None:
    snapshot = _snapshot()

    source = create_snapshot_source(snapshot)

    assert source.source_kind is EvidenceSourceKind.SNAPSHOT
    assert source.source_id == snapshot.snapshot_id
    assert source.source_sha256 == snapshot.snapshot_sha256


def test_snapshot_evidence_payload_is_compact_and_hash_verified() -> None:
    snapshot = _snapshot()

    payload = create_snapshot_evidence_payload(snapshot)

    assert payload.decode() == snapshot.to_evidence_mapping()
    assert "state" not in payload.decode()
    assert payload.payload_sha256 == hashlib.sha256(payload.payload_json).hexdigest()


def test_snapshot_integrates_with_append_only_evidence_ledger() -> None:
    snapshot = _snapshot()
    ledger = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)

    ledger = append_evidence_record(
        ledger,
        record_id="EVIDENCE-SNAPSHOT-000",
        observed_at_tick=snapshot.captured_at_tick,
        recorded_at_tick=snapshot.captured_at_tick,
        kind=EvidenceKind.STATE_SNAPSHOT,
        domain=snapshot.domain,
        producer_id="HARNESS-RUNTIME",
        payload=create_snapshot_evidence_payload(snapshot),
        sources=(create_snapshot_source(snapshot),),
    )

    record = ledger.records[0]
    assert record.kind is EvidenceKind.STATE_SNAPSHOT
    assert record.sources[0].source_kind is EvidenceSourceKind.SNAPSHOT
    assert record.sources[0].source_sha256 == snapshot.snapshot_sha256


@pytest.mark.parametrize(
    "function",
    [
        create_snapshot_source,
        create_snapshot_evidence_payload,
        calculate_state_snapshot_sha256,
    ],
)
def test_snapshot_functions_reject_invalid_runtime_snapshot_type(function: object) -> None:
    with pytest.raises(SnapshotError, match="snapshot must be a StateSnapshot"):
        function("snapshot")  # type: ignore[operator]


def test_series_hash_function_rejects_invalid_runtime_type() -> None:
    with pytest.raises(SnapshotError, match="series must be a SnapshotSeries"):
        calculate_snapshot_series_sha256("series")  # type: ignore[arg-type]


def test_snapshot_dataclasses_are_frozen() -> None:
    state = _state()
    snapshot = _snapshot()
    series = _series()

    with pytest.raises(FrozenInstanceError):
        state.state_sha256 = "0" * 64  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        snapshot.sequence = 2  # type: ignore[misc]
    with pytest.raises(FrozenInstanceError):
        series.snapshots = ()  # type: ignore[misc]


def test_snapshot_module_has_no_aurora_projection_api() -> None:
    assert not hasattr(SnapshotState, "to_aurora_mapping")
    assert not hasattr(StateSnapshot, "to_aurora_mapping")
    assert not hasattr(SnapshotSeries, "to_aurora_mapping")
    assert not hasattr(snapshots_module, "project_snapshot_for_aurora")


def test_snapshot_module_exports_stable_public_surface() -> None:
    assert set(snapshots_module.__all__) == {
        "DEFAULT_MAX_SNAPSHOT_STATE_BYTES",
        "MAX_SNAPSHOT_STATE_BYTES",
        "MAX_TICK",
        "SUPPORTED_SNAPSHOT_SCHEMA_VERSION",
        "SnapshotError",
        "SnapshotPhase",
        "SnapshotSeries",
        "SnapshotState",
        "StateSnapshot",
        "append_state_snapshot",
        "calculate_snapshot_series_sha256",
        "calculate_state_snapshot_sha256",
        "create_snapshot_evidence_payload",
        "create_snapshot_series",
        "create_snapshot_source",
        "create_snapshot_state",
    }
