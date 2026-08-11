"""Unit tests for deterministic event scheduling and Aurora-safe projections."""

from __future__ import annotations

import hashlib
import json
from dataclasses import FrozenInstanceError, replace
from types import MappingProxyType

import pytest

from aurora_validation_harness import events as events_module
from aurora_validation_harness.events import (
    DEFAULT_MAX_EVENT_PAYLOAD_BYTES,
    MAX_EVENT_PAYLOAD_BYTES,
    MAX_TICK,
    EventError,
    EventObservability,
    EventPayload,
    EventReleaseBatch,
    EventRuntimeState,
    EventSchedule,
    EventSignificance,
    ScheduledEvent,
    SimulationResolution,
    advance_event_schedule,
    create_event_payload,
    create_event_state,
    project_event_for_aurora,
    project_release_for_aurora,
)

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_SCHEDULE_ID = "AURORA-EVENTS-FOUND-001"


def _event_id(sequence: int) -> str:
    return f"AURORA-SCN-FOUND-001-E{sequence}"


def _observable_event_id(sequence: int) -> str:
    return f"OBS-FOUND-{sequence:03d}"


def _payload(data: dict[str, object] | None = None) -> EventPayload:
    return create_event_payload({"actor_id": "Mara", "action": "waits"} if data is None else data)


def _hidden_event(
    *,
    sequence: int = 0,
    tick: int = 0,
    event_id: str | None = None,
    payload: EventPayload | None = None,
) -> ScheduledEvent:
    return ScheduledEvent(
        event_id=_event_id(sequence) if event_id is None else event_id,
        sequence=sequence,
        scheduled_tick=tick,
        actor_id="WorldRuntime",
        action="hidden_world_change",
        observability=EventObservability.HIDDEN,
        significance=EventSignificance.ROUTINE,
        minimum_resolution=SimulationResolution.ACTIVE,
        objective_payload=(
            _payload({"actor_id": "Mara", "location": "Cargo_Bay_7"})
            if payload is None
            else payload
        ),
    )


def _full_event(
    *,
    sequence: int = 0,
    tick: int = 0,
    event_id: str | None = None,
    observable_event_id: str | None = None,
    payload: EventPayload | None = None,
) -> ScheduledEvent:
    return ScheduledEvent(
        event_id=_event_id(sequence) if event_id is None else event_id,
        sequence=sequence,
        scheduled_tick=tick,
        actor_id="Harness",
        action="processing_interval",
        observability=EventObservability.FULLY_OBSERVABLE,
        significance=EventSignificance.ROUTINE,
        minimum_resolution=SimulationResolution.ACTIVE,
        objective_payload=(
            _payload({"actor_id": "Harness", "duration_ticks": 60}) if payload is None else payload
        ),
        observable_event_id=(
            _observable_event_id(sequence) if observable_event_id is None else observable_event_id
        ),
    )


def _partial_event(
    *,
    sequence: int = 0,
    tick: int = 0,
    event_id: str | None = None,
    observable_event_id: str | None = None,
    objective_payload: EventPayload | None = None,
    observable_payload: EventPayload | None = None,
) -> ScheduledEvent:
    return ScheduledEvent(
        event_id=_event_id(sequence) if event_id is None else event_id,
        sequence=sequence,
        scheduled_tick=tick,
        actor_id="Mara",
        action="camera_event",
        observability=EventObservability.PARTIALLY_OBSERVABLE,
        significance=EventSignificance.NOTABLE,
        minimum_resolution=SimulationResolution.FOCUSED,
        objective_payload=(
            _payload(
                {
                    "actor_id": "Mara",
                    "camera": "disabled_by_Mara",
                    "statement": "Camera failed",
                }
            )
            if objective_payload is None
            else objective_payload
        ),
        observable_event_id=(
            _observable_event_id(sequence) if observable_event_id is None else observable_event_id
        ),
        observable_payload=(
            _payload({"camera": "offline", "statement": "Camera failed"})
            if observable_payload is None
            else observable_payload
        ),
    )


def _schedule(*, schedule_id: str = _SCHEDULE_ID) -> EventSchedule:
    return EventSchedule(
        schedule_id=schedule_id,
        events=(
            _hidden_event(sequence=0, tick=0),
            _full_event(sequence=1, tick=10),
            _partial_event(sequence=2, tick=20),
            _full_event(
                sequence=3,
                tick=30,
                payload=_payload(
                    {
                        "actor_id": "Sensor",
                        "location": "Cargo_Bay_7",
                    }
                ),
            ),
        ),
    )


def _raw_payload(payload_json: bytes, *, digest: object | None = None) -> EventPayload:
    return EventPayload(
        payload_json=payload_json,
        payload_sha256=(hashlib.sha256(payload_json).hexdigest() if digest is None else digest),
    )


def _state_after(schedule: EventSchedule, tick: int) -> EventRuntimeState:
    return advance_event_schedule(schedule, create_event_state(schedule), tick).state


def test_public_constants_define_bounded_event_limits() -> None:
    assert DEFAULT_MAX_EVENT_PAYLOAD_BYTES == 262_144
    assert MAX_EVENT_PAYLOAD_BYTES == 1_048_576
    assert MAX_TICK == (1 << 63) - 1
    assert 0 < DEFAULT_MAX_EVENT_PAYLOAD_BYTES < MAX_EVENT_PAYLOAD_BYTES < MAX_TICK


def test_event_enums_have_stable_contract_values() -> None:
    assert {value.value for value in EventObservability} == {
        "FULLY_OBSERVABLE",
        "PARTIALLY_OBSERVABLE",
        "HIDDEN",
    }
    assert {value.value for value in EventSignificance} == {
        "ROUTINE",
        "NOTABLE",
        "MAJOR",
        "CRITICAL",
    }
    assert {value.value for value in SimulationResolution} == {
        "BACKGROUND",
        "ACTIVE",
        "FOCUSED",
        "DEEP",
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
        {"confidence": 0.75, "locations": ["platform-2", "platform-3"]},
    ],
)
def test_event_payload_accepts_supported_nested_json_values(value: object) -> None:
    payload = create_event_payload({"value": value})

    assert payload.decode() == {"value": value}
    assert payload.size_bytes == len(payload.payload_json)
    assert payload.payload_sha256 == hashlib.sha256(payload.payload_json).hexdigest()
    assert payload.to_mapping() == {
        "data": {"value": value},
        "payload_sha256": payload.payload_sha256,
    }


def test_event_payload_normalizes_generic_mappings_and_key_order() -> None:
    first = create_event_payload(
        MappingProxyType({"zone": "Café", "nested": MappingProxyType({"b": 2, "a": 1})})
    )
    second = create_event_payload({"nested": {"a": 1, "b": 2}, "zone": "Café"})

    assert first == second
    assert first.payload_json == '{"nested":{"a":1,"b":2},"zone":"Café"}'.encode()


def test_decoded_event_payload_is_a_fresh_copy() -> None:
    payload = create_event_payload({"locations": ["platform-2"]})
    decoded = payload.decode()
    locations = decoded["locations"]
    assert isinstance(locations, list)

    locations.append("tampered")

    assert payload.decode() == {"locations": ["platform-2"]}


def test_event_payload_accepts_exact_declared_size_limit() -> None:
    payload = create_event_payload({"value": "x"})

    recreated = create_event_payload(
        {"value": "x"},
        max_payload_bytes=payload.size_bytes,
    )

    assert recreated == payload


def test_event_payload_rejects_declared_size_limit_overflow() -> None:
    payload = create_event_payload({"value": "x"})

    with pytest.raises(EventError, match="event payload must not exceed"):
        create_event_payload(
            {"value": "x"},
            max_payload_bytes=payload.size_bytes - 1,
        )


def test_event_payload_can_explicitly_opt_in_above_default_limit() -> None:
    data = {"value": "x" * DEFAULT_MAX_EVENT_PAYLOAD_BYTES}

    with pytest.raises(EventError, match="event payload must not exceed"):
        create_event_payload(data)

    payload = create_event_payload(data, max_payload_bytes=MAX_EVENT_PAYLOAD_BYTES)
    assert DEFAULT_MAX_EVENT_PAYLOAD_BYTES < payload.size_bytes < MAX_EVENT_PAYLOAD_BYTES


@pytest.mark.parametrize("max_payload_bytes", [True, "1024", 1.5])
def test_event_payload_rejects_non_integer_size_limit(max_payload_bytes: object) -> None:
    with pytest.raises(EventError, match="max_payload_bytes must be an integer"):
        create_event_payload({}, max_payload_bytes=max_payload_bytes)


@pytest.mark.parametrize("max_payload_bytes", [0, -1, MAX_EVENT_PAYLOAD_BYTES + 1])
def test_event_payload_rejects_out_of_range_size_limit(max_payload_bytes: int) -> None:
    with pytest.raises(EventError, match="max_payload_bytes must be between"):
        create_event_payload({}, max_payload_bytes=max_payload_bytes)


@pytest.mark.parametrize("data", [None, [], "payload", 7])
def test_event_payload_requires_a_json_object(data: object) -> None:
    with pytest.raises(EventError, match="event payload data must be a JSON object"):
        create_event_payload(data)


@pytest.mark.parametrize(
    "reserved_key",
    [
        "expected_answer",
        "Expected Interpretation",
        "EXPECTED-RESULT",
        "failure.conditions",
        "fixture_manifest_sha256",
        "fixture set id",
        "future-event-queue",
        "hidden from Aurora",
        "hidden_state_marker",
        "scenario_id",
        "scenario name",
        "validator.metadata",
        "validator_notes",
        "world-debug-state",
    ],
)
def test_event_payload_recursively_rejects_reserved_metadata_keys(
    reserved_key: str,
) -> None:
    data = {"event": [{"content": {reserved_key: "private"}}]}

    with pytest.raises(EventError, match="contains reserved metadata key"):
        create_event_payload(data)


@pytest.mark.parametrize("data", [{1: "non-string"}, {"tuple": (1,)}, {"set": {1}}])
def test_event_payload_rejects_non_json_shapes(data: object) -> None:
    with pytest.raises(EventError, match=r"non-string object key|unsupported JSON value type"):
        create_event_payload(data)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_event_payload_rejects_non_finite_numbers(value: float) -> None:
    with pytest.raises(EventError, match="contains a non-finite number"):
        create_event_payload({"confidence": value})


def test_event_payload_direct_constructor_checks_bytes_and_digest() -> None:
    valid = _payload()

    with pytest.raises(EventError, match="payload_json must be bytes"):
        replace(valid, payload_json="not-bytes")
    with pytest.raises(EventError, match="payload_sha256 must be a string"):
        replace(valid, payload_sha256=7)
    with pytest.raises(EventError, match="lowercase 64-character SHA-256"):
        replace(valid, payload_sha256="A" * 64)
    with pytest.raises(EventError, match="does not match payload_json"):
        replace(valid, payload_sha256="0" * 64)


def test_event_payload_direct_constructor_enforces_absolute_size_limit() -> None:
    payload_json = b"x" * (MAX_EVENT_PAYLOAD_BYTES + 1)

    with pytest.raises(EventError, match="payload_json must not exceed"):
        _raw_payload(payload_json)


@pytest.mark.parametrize(
    ("payload_json", "message"),
    [
        (b"\xff", "payload_json is not valid JSON"),
        (b"{broken", "payload_json is not valid JSON"),
        (b'{"value":NaN}', "non-finite JSON value is not allowed"),
        (b"[]", "payload_json must encode a JSON object"),
        (b"null", "payload_json must encode a JSON object"),
    ],
)
def test_event_payload_direct_constructor_rejects_invalid_json(
    payload_json: bytes,
    message: str,
) -> None:
    with pytest.raises(EventError, match=message):
        _raw_payload(payload_json)


def test_event_payload_direct_constructor_rejects_noncanonical_json() -> None:
    with pytest.raises(EventError, match="payload_json must use canonical JSON encoding"):
        _raw_payload(b'{"zone": "platform-2"}')


def test_event_payload_direct_constructor_revalidates_reserved_metadata() -> None:
    with pytest.raises(EventError, match="contains reserved metadata key"):
        _raw_payload(b'{"validator_metadata":"private"}')


def test_canonical_json_helper_translates_serialization_errors() -> None:
    with pytest.raises(EventError, match="value is not JSON-serializable"):
        events_module._canonical_json_bytes({"unsupported": object()})


def test_payload_factory_defensively_rechecks_normalized_root(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(events_module, "_normalize_json_value", lambda *_args, **_kwargs: [])

    with pytest.raises(EventError, match="event payload data must be a JSON object"):
        create_event_payload({})


def test_normalization_helper_defensively_rejects_unhandled_value(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(events_module, "_validate_json_value", lambda *_args, **_kwargs: None)

    with pytest.raises(EventError, match="unsupported JSON value type"):
        events_module._normalize_json_value(object(), path="payload")


@pytest.mark.parametrize("significance", list(EventSignificance))
def test_scheduled_event_accepts_every_significance(
    significance: EventSignificance,
) -> None:
    assert replace(_full_event(), significance=significance).significance is significance


@pytest.mark.parametrize("resolution", list(SimulationResolution))
def test_scheduled_event_accepts_every_resolution(
    resolution: SimulationResolution,
) -> None:
    assert replace(_full_event(), minimum_resolution=resolution).minimum_resolution is resolution


def test_hidden_event_has_no_observable_surface() -> None:
    event = _hidden_event()

    assert event.observability is EventObservability.HIDDEN
    assert event.observable_event_id is None
    assert event.observable_payload is None
    assert project_event_for_aurora(event) is None


def test_fully_observable_event_projects_objective_payload() -> None:
    event = _full_event(tick=10)

    projected = project_event_for_aurora(event)

    assert projected is not None
    assert projected.event_id == _observable_event_id(0)
    assert projected.occurred_at_tick == 10
    assert projected.payload is event.objective_payload


def test_partially_observable_event_projects_only_explicit_visible_payload() -> None:
    event = _partial_event(tick=20)

    projected = project_event_for_aurora(event)
    assert projected is not None
    serialized = json.dumps(projected.to_mapping(), sort_keys=True)

    assert projected.payload is event.observable_payload
    assert "Camera failed" in serialized
    assert "disabled_by_Mara" not in serialized
    assert event.event_id not in serialized
    assert event.actor_id not in serialized
    assert event.action not in serialized
    assert event.significance.value not in serialized
    assert event.minimum_resolution.value not in serialized
    assert event.observability.value not in serialized


def test_validator_event_mapping_preserves_complete_objective_record() -> None:
    event = _partial_event(sequence=2, tick=20)

    assert event.to_validator_mapping() == {
        "action": "camera_event",
        "actor_id": "Mara",
        "event_id": _event_id(2),
        "minimum_resolution": "FOCUSED",
        "objective_payload": event.objective_payload.to_mapping(),
        "observability": "PARTIALLY_OBSERVABLE",
        "observable_event_id": _observable_event_id(2),
        "observable_payload": event.observable_payload.to_mapping(),
        "scheduled_tick": 20,
        "sequence": 2,
        "significance": "NOTABLE",
    }


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("event_id", "bad-id", "uppercase identifier characters"),
        ("event_id", 7, "event_id must be a string"),
        ("sequence", True, "sequence must be an integer"),
        ("sequence", 1.5, "sequence must be an integer"),
        ("sequence", -1, "sequence must be non-negative"),
        ("scheduled_tick", True, "scheduled_tick must be an integer"),
        ("scheduled_tick", -1, "scheduled_tick must be between"),
        ("scheduled_tick", MAX_TICK + 1, "scheduled_tick must be between"),
        ("actor_id", "bad actor", "actor_id contains unsupported"),
        ("actor_id", None, "actor_id must be a string"),
        ("action", "bad action", "action contains unsupported"),
        ("action", 4, "action must be a string"),
        ("observability", "FULLY_OBSERVABLE", "must be an EventObservability"),
        ("significance", "ROUTINE", "significance must be an EventSignificance"),
        ("minimum_resolution", "ACTIVE", "must be a SimulationResolution"),
        ("objective_payload", {}, "objective_payload must be an EventPayload"),
        ("observable_event_id", "OBS-HIDDEN-001", "Aurora-reserved token"),
        ("observable_event_id", 7, "observable_event_id must be a string"),
        ("observable_payload", {}, "must be null or an EventPayload"),
    ],
)
def test_scheduled_event_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    with pytest.raises(EventError, match=message):
        replace(_full_event(), **{field: value})


def test_hidden_event_rejects_each_observable_projection_component() -> None:
    hidden = _hidden_event()

    with pytest.raises(EventError, match="hidden event must not define"):
        replace(hidden, observable_event_id="OBS-FOUND-999")
    with pytest.raises(EventError, match="hidden event must not define"):
        replace(hidden, observable_payload=_payload({"visible": True}))


def test_fully_observable_event_requires_id_and_forbids_duplicate_payload() -> None:
    event = _full_event()

    with pytest.raises(EventError, match="requires observable_event_id"):
        replace(event, observable_event_id=None)
    with pytest.raises(EventError, match="must use objective_payload"):
        replace(event, observable_payload=_payload({"duplicate": True}))


def test_partially_observable_event_requires_both_projection_components() -> None:
    event = _partial_event()

    with pytest.raises(EventError, match="requires an explicit observable projection"):
        replace(event, observable_event_id=None)
    with pytest.raises(EventError, match="requires an explicit observable projection"):
        replace(event, observable_payload=None)


def test_partially_observable_event_requires_distinct_visible_payload() -> None:
    event = _partial_event()

    with pytest.raises(EventError, match="must differ from objective_payload"):
        replace(event, observable_payload=event.objective_payload)


def test_aurora_event_mapping_contains_only_visible_event_fields() -> None:
    projected = project_event_for_aurora(_full_event(tick=10))
    assert projected is not None

    assert projected.to_mapping() == {
        "event_id": _observable_event_id(0),
        "occurred_at_tick": 10,
        "payload": projected.payload.to_mapping(),
    }


def test_aurora_event_hash_is_deterministic_and_visibility_sensitive() -> None:
    first = project_event_for_aurora(_full_event())
    second = project_event_for_aurora(_full_event())
    changed = project_event_for_aurora(
        _full_event(payload=_payload({"actor_id": "Harness", "duration_ticks": 61}))
    )
    assert first is not None
    assert second is not None
    assert changed is not None

    assert first.event_sha256 == second.event_sha256
    assert first.event_sha256 != changed.event_sha256
    assert len(first.event_sha256) == 64


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("event_id", "OBS-VALIDATOR-001", "Aurora-reserved token"),
        ("event_id", "bad-id", "uppercase identifier characters"),
        ("occurred_at_tick", True, "occurred_at_tick must be an integer"),
        ("occurred_at_tick", -1, "occurred_at_tick must be between"),
        ("payload", {}, "payload must be an EventPayload"),
    ],
)
def test_aurora_event_direct_constructor_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    event = project_event_for_aurora(_full_event())
    assert event is not None

    with pytest.raises(EventError, match=message):
        replace(event, **{field: value})


def test_projection_rejects_invalid_runtime_type() -> None:
    with pytest.raises(EventError, match="event must be a ScheduledEvent"):
        project_event_for_aurora("event")


def test_projection_defensively_rejects_missing_governed_surface() -> None:
    event = _full_event()
    object.__setattr__(event, "observable_event_id", None)

    with pytest.raises(EventError, match="missing its governed projection"):
        project_event_for_aurora(event)


def test_empty_event_schedule_is_valid_and_deterministic() -> None:
    schedule = EventSchedule(schedule_id="AURORA-EVENTS-EMPTY", events=())

    assert schedule.events == ()
    assert len(schedule.schedule_sha256) == 64
    assert schedule.to_validator_mapping() == {
        "events": [],
        "schedule_id": "AURORA-EVENTS-EMPTY",
    }


def test_schedule_accepts_multiple_events_at_same_tick_in_sequence_order() -> None:
    schedule = EventSchedule(
        schedule_id=_SCHEDULE_ID,
        events=(
            _full_event(sequence=0, tick=10),
            _full_event(sequence=1, tick=10),
        ),
    )

    batch = advance_event_schedule(schedule, create_event_state(schedule), 10)

    assert [event.sequence for event in batch.released_events] == [0, 1]


def test_schedule_mapping_and_hash_are_stable() -> None:
    first = _schedule()
    second = _schedule()

    assert first.to_validator_mapping() == second.to_validator_mapping()
    assert first.schedule_sha256 == second.schedule_sha256
    assert len(first.schedule_sha256) == 64


def test_schedule_hash_changes_when_hidden_truth_changes_without_projection_leak() -> None:
    original = _schedule()
    changed_hidden = replace(
        original.events[0],
        objective_payload=_payload({"actor_id": "Mara", "location": "Medical_Deck_3"}),
    )
    changed = EventSchedule(
        schedule_id=original.schedule_id,
        events=(changed_hidden, *original.events[1:]),
    )

    original_batch = advance_event_schedule(original, create_event_state(original), 0)
    changed_batch = advance_event_schedule(changed, create_event_state(changed), 0)

    assert original.schedule_sha256 != changed.schedule_sha256
    assert project_release_for_aurora(original_batch) == ()
    assert project_release_for_aurora(changed_batch) == ()


def test_schedule_rejects_invalid_id_and_event_collection() -> None:
    with pytest.raises(EventError, match="schedule_id must be a string"):
        EventSchedule(schedule_id=7, events=())
    with pytest.raises(EventError, match="uppercase identifier characters"):
        EventSchedule(schedule_id="bad-schedule", events=())
    with pytest.raises(EventError, match="events must be a tuple"):
        EventSchedule(schedule_id=_SCHEDULE_ID, events=[])
    with pytest.raises(EventError, match="events must be a tuple"):
        EventSchedule(schedule_id=_SCHEDULE_ID, events=("event",))


def test_schedule_rejects_sequence_gap_or_nonzero_start() -> None:
    with pytest.raises(EventError, match="contiguous and start at zero"):
        EventSchedule(schedule_id=_SCHEDULE_ID, events=(_full_event(sequence=1),))

    with pytest.raises(EventError, match="contiguous and start at zero"):
        EventSchedule(
            schedule_id=_SCHEDULE_ID,
            events=(
                _full_event(sequence=0),
                _full_event(sequence=2),
            ),
        )


def test_schedule_rejects_decreasing_ticks() -> None:
    with pytest.raises(EventError, match="nondecreasing scheduled_tick"):
        EventSchedule(
            schedule_id=_SCHEDULE_ID,
            events=(
                _full_event(sequence=0, tick=10),
                _full_event(sequence=1, tick=9),
            ),
        )


def test_schedule_rejects_duplicate_internal_event_ids() -> None:
    first = _hidden_event(sequence=0)
    duplicate = _full_event(sequence=1, event_id=first.event_id)

    with pytest.raises(EventError, match="event_id values must be unique"):
        EventSchedule(schedule_id=_SCHEDULE_ID, events=(first, duplicate))


def test_schedule_rejects_duplicate_observable_event_ids() -> None:
    first = _full_event(sequence=0)
    duplicate = _partial_event(
        sequence=1,
        observable_event_id=first.observable_event_id,
    )

    with pytest.raises(EventError, match="observable_event_id values must be unique"):
        EventSchedule(schedule_id=_SCHEDULE_ID, events=(first, duplicate))


def test_create_event_state_returns_pristine_cursor() -> None:
    state = create_event_state(_schedule())

    assert state == EventRuntimeState(schedule_id=_SCHEDULE_ID)
    assert state.next_sequence == 0
    assert state.advanced_through_tick is None
    assert state.last_released_tick is None
    assert state.released_event_ids == ()


def test_create_event_state_rejects_invalid_runtime_type() -> None:
    with pytest.raises(EventError, match="schedule must be an EventSchedule"):
        create_event_state("schedule")


@pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"schedule_id": "bad-id"}, "uppercase identifier characters"),
        ({"schedule_id": 4}, "schedule_id must be a string"),
        ({"next_sequence": True}, "next_sequence must be an integer"),
        ({"next_sequence": 1.5}, "next_sequence must be an integer"),
        ({"next_sequence": -1}, "next_sequence must be non-negative"),
        ({"advanced_through_tick": True}, "advanced_through_tick must be an integer"),
        ({"advanced_through_tick": -1}, "advanced_through_tick must be between"),
        ({"last_released_tick": MAX_TICK + 1}, "last_released_tick must be between"),
        ({"released_event_ids": ["AURORA-EVENT-001"]}, "must be a tuple of strings"),
        ({"released_event_ids": (1,)}, "must be a tuple of strings"),
        (
            {"released_event_ids": ("bad-id",), "next_sequence": 1},
            "uppercase identifier characters",
        ),
        (
            {
                "released_event_ids": ("AURORA-EVENT-001", "AURORA-EVENT-001"),
                "next_sequence": 2,
                "last_released_tick": 1,
                "advanced_through_tick": 1,
            },
            "must not contain duplicates",
        ),
        (
            {
                "released_event_ids": ("AURORA-EVENT-001",),
                "next_sequence": 0,
                "last_released_tick": 1,
                "advanced_through_tick": 1,
            },
            "next_sequence must equal released event count",
        ),
        (
            {
                "released_event_ids": ("AURORA-EVENT-001",),
                "next_sequence": 1,
                "advanced_through_tick": 1,
            },
            "last_released_tick is required",
        ),
        ({"last_released_tick": 1}, "last_released_tick must be null"),
        (
            {
                "released_event_ids": ("AURORA-EVENT-001",),
                "next_sequence": 1,
                "last_released_tick": 1,
            },
            "advanced_through_tick is required",
        ),
        (
            {
                "released_event_ids": ("AURORA-EVENT-001",),
                "next_sequence": 1,
                "last_released_tick": 2,
                "advanced_through_tick": 1,
            },
            "last_released_tick must not exceed",
        ),
    ],
)
def test_event_runtime_state_rejects_invalid_or_inconsistent_state(
    changes: dict[str, object],
    message: str,
) -> None:
    with pytest.raises(EventError, match=message):
        replace(EventRuntimeState(schedule_id=_SCHEDULE_ID), **changes)


def test_advance_releases_only_due_events_and_retains_future_queue() -> None:
    schedule = _schedule()
    state = create_event_state(schedule)

    batch = advance_event_schedule(schedule, state, 10)

    assert batch.released is True
    assert [event.sequence for event in batch.released_events] == [0, 1]
    assert batch.advanced_from_tick is None
    assert batch.advanced_through_tick == 10
    assert batch.state.next_sequence == 2
    assert batch.state.advanced_through_tick == 10
    assert batch.state.last_released_tick == 10
    assert batch.state.released_event_ids == (_event_id(0), _event_id(1))
    assert _event_id(2) not in batch.state.released_event_ids
    assert _event_id(3) not in batch.state.released_event_ids


def test_advance_with_no_due_events_moves_only_explicit_time_cursor() -> None:
    schedule = _schedule()
    state = create_event_state(schedule)

    batch = advance_event_schedule(schedule, state, 0)
    waiting = advance_event_schedule(schedule, batch.state, 5)

    assert waiting.released is False
    assert waiting.released_events == ()
    assert waiting.advanced_from_tick == 0
    assert waiting.state.next_sequence == 1
    assert waiting.state.last_released_tick == 0
    assert waiting.state.advanced_through_tick == 5
    assert waiting.state.released_event_ids == (_event_id(0),)


def test_advancing_to_same_tick_is_idempotent() -> None:
    schedule = _schedule()
    first = advance_event_schedule(schedule, create_event_state(schedule), 10)

    repeated = advance_event_schedule(schedule, first.state, 10)

    assert repeated.released_events == ()
    assert repeated.state == first.state


def test_stepwise_advancement_preserves_contiguous_event_order() -> None:
    schedule = _schedule()
    state = create_event_state(schedule)
    released_ids: list[str] = []

    for tick in (0, 9, 10, 19, 20, 29, 30):
        batch = advance_event_schedule(schedule, state, tick)
        released_ids.extend(event.event_id for event in batch.released_events)
        state = batch.state

    assert released_ids == [_event_id(index) for index in range(4)]
    assert state.next_sequence == 4
    assert state.released_event_ids == tuple(released_ids)
    assert state.last_released_tick == 30


def test_empty_schedule_can_advance_without_releasing_events() -> None:
    schedule = EventSchedule(schedule_id="AURORA-EVENTS-EMPTY", events=())

    batch = advance_event_schedule(schedule, create_event_state(schedule), MAX_TICK)

    assert batch.released_events == ()
    assert batch.state.advanced_through_tick == MAX_TICK


def test_schedule_cannot_move_backward() -> None:
    schedule = _schedule()
    state = _state_after(schedule, 20)

    with pytest.raises(EventError, match="must not move an event schedule backward"):
        advance_event_schedule(schedule, state, 19)


@pytest.mark.parametrize("through_tick", [True, -1, MAX_TICK + 1])
def test_advance_rejects_invalid_tick(through_tick: object) -> None:
    schedule = _schedule()

    with pytest.raises(EventError, match=r"through_tick must be an integer|must be between"):
        advance_event_schedule(schedule, create_event_state(schedule), through_tick)


def test_advance_rejects_invalid_schedule_or_state_types() -> None:
    schedule = _schedule()
    state = create_event_state(schedule)

    with pytest.raises(EventError, match="schedule must be an EventSchedule"):
        advance_event_schedule("schedule", state, 0)
    with pytest.raises(EventError, match="state must be an EventRuntimeState"):
        advance_event_schedule(schedule, "state", 0)


def test_advance_rejects_state_from_different_schedule() -> None:
    schedule = _schedule()
    other = create_event_state(_schedule(schedule_id="AURORA-EVENTS-FOUND-002"))

    with pytest.raises(EventError, match="does not match event schedule"):
        advance_event_schedule(schedule, other, 0)


def test_advance_rejects_state_that_does_not_match_schedule_prefix() -> None:
    schedule = _schedule()
    corrupted = EventRuntimeState(
        schedule_id=schedule.schedule_id,
        next_sequence=1,
        advanced_through_tick=0,
        last_released_tick=0,
        released_event_ids=("AURORA-SCN-FOUND-001-E99",),
    )

    with pytest.raises(EventError, match="does not match the released schedule prefix"):
        advance_event_schedule(schedule, corrupted, 10)


def test_advance_rejects_state_with_wrong_last_released_tick() -> None:
    schedule = _schedule()
    corrupted = EventRuntimeState(
        schedule_id=schedule.schedule_id,
        next_sequence=2,
        advanced_through_tick=15,
        last_released_tick=15,
        released_event_ids=(_event_id(0), _event_id(1)),
    )

    with pytest.raises(EventError, match="last_released_tick does not match schedule"):
        advance_event_schedule(schedule, corrupted, 20)


def test_release_batch_accepts_empty_and_nonempty_advancements() -> None:
    schedule = _schedule()
    first = advance_event_schedule(schedule, create_event_state(schedule), 0)
    empty = advance_event_schedule(schedule, first.state, 5)

    assert first.released is True
    assert empty.released is False


def test_release_batch_rejects_invalid_tick_fields() -> None:
    batch = advance_event_schedule(_schedule(), create_event_state(_schedule()), 0)

    with pytest.raises(EventError, match="advanced_from_tick must be an integer"):
        replace(batch, advanced_from_tick=True)
    with pytest.raises(EventError, match="advanced_through_tick must be between"):
        replace(batch, advanced_through_tick=-1)
    with pytest.raises(EventError, match="must not exceed advanced_through_tick"):
        replace(batch, advanced_from_tick=1)


def test_release_batch_rejects_invalid_event_collection_or_state() -> None:
    schedule = _schedule()
    batch = advance_event_schedule(schedule, create_event_state(schedule), 0)

    with pytest.raises(EventError, match="released_events must be a tuple"):
        replace(batch, released_events=list(batch.released_events))
    with pytest.raises(EventError, match="released_events must be a tuple"):
        replace(batch, released_events=("event",))
    with pytest.raises(EventError, match="state must be an EventRuntimeState"):
        replace(batch, state="state")


def test_release_batch_rejects_state_advancement_mismatch() -> None:
    schedule = _schedule()
    batch = advance_event_schedule(schedule, create_event_state(schedule), 0)
    state = replace(batch.state, advanced_through_tick=1)

    with pytest.raises(EventError, match="state advancement tick does not match"):
        replace(batch, state=state)


def test_release_batch_rejects_event_beyond_advancement_tick() -> None:
    event = _full_event(sequence=0, tick=10)
    state = EventRuntimeState(
        schedule_id=_SCHEDULE_ID,
        next_sequence=1,
        advanced_through_tick=5,
        last_released_tick=5,
        released_event_ids=(event.event_id,),
    )

    with pytest.raises(EventError, match="beyond its advancement tick"):
        EventReleaseBatch(None, 5, (event,), state)


def test_release_batch_rejects_event_from_prior_advancement() -> None:
    event = _full_event(sequence=0, tick=5)
    state = EventRuntimeState(
        schedule_id=_SCHEDULE_ID,
        next_sequence=1,
        advanced_through_tick=10,
        last_released_tick=5,
        released_event_ids=(event.event_id,),
    )

    with pytest.raises(EventError, match="from an earlier advancement"):
        EventReleaseBatch(5, 10, (event,), state)


def test_release_batch_rejects_noncontiguous_event_sequences() -> None:
    first = _full_event(sequence=0, tick=5)
    third = _full_event(sequence=2, tick=6)
    state = EventRuntimeState(
        schedule_id=_SCHEDULE_ID,
        next_sequence=2,
        advanced_through_tick=10,
        last_released_tick=6,
        released_event_ids=(first.event_id, third.event_id),
    )

    with pytest.raises(EventError, match="contiguous sequence values"):
        EventReleaseBatch(None, 10, (first, third), state)


def test_release_batch_rejects_events_not_recorded_in_resulting_state() -> None:
    event = _full_event(sequence=0, tick=5)
    state = EventRuntimeState(
        schedule_id=_SCHEDULE_ID,
        next_sequence=1,
        advanced_through_tick=10,
        last_released_tick=5,
        released_event_ids=("AURORA-SCN-FOUND-001-E99",),
    )

    with pytest.raises(EventError, match="do not match resulting runtime state"):
        EventReleaseBatch(None, 10, (event,), state)


def test_release_batch_rejects_last_event_tick_state_mismatch() -> None:
    event = _full_event(sequence=0, tick=5)
    state = EventRuntimeState(
        schedule_id=_SCHEDULE_ID,
        next_sequence=1,
        advanced_through_tick=10,
        last_released_tick=6,
        released_event_ids=(event.event_id,),
    )

    with pytest.raises(EventError, match="last released event tick does not match"):
        EventReleaseBatch(None, 10, (event,), state)


def test_release_projection_filters_hidden_events_and_preserves_visible_order() -> None:
    schedule = _schedule()
    batch = advance_event_schedule(schedule, create_event_state(schedule), 20)

    projected = project_release_for_aurora(batch)

    assert [event.event_id for event in projected] == [
        _observable_event_id(1),
        _observable_event_id(2),
    ]
    serialized = json.dumps([event.to_mapping() for event in projected], sort_keys=True)
    assert "Cargo_Bay_7" not in serialized
    assert _event_id(0) not in serialized
    assert _event_id(3) not in serialized
    assert "PARTIALLY_OBSERVABLE" not in serialized


def test_release_projection_rejects_invalid_runtime_type() -> None:
    with pytest.raises(EventError, match="batch must be an EventReleaseBatch"):
        project_release_for_aurora("batch")


def test_event_model_values_are_immutable() -> None:
    payload = _payload()
    scheduled = _full_event()
    projected = project_event_for_aurora(scheduled)
    schedule = EventSchedule(_SCHEDULE_ID, (scheduled,))
    state = create_event_state(schedule)
    batch = advance_event_schedule(schedule, state, 0)
    assert projected is not None

    mutations = (
        (payload, "payload_sha256", "0" * 64),
        (scheduled, "event_id", "AURORA-SCN-FOUND-001-E9"),
        (projected, "event_id", "OBS-FOUND-999"),
        (schedule, "schedule_id", "AURORA-EVENTS-FOUND-999"),
        (state, "next_sequence", 1),
        (batch, "advanced_through_tick", 1),
    )
    for value, field, replacement_value in mutations:
        with pytest.raises(FrozenInstanceError):
            setattr(value, field, replacement_value)


def test_event_module_exports_complete_public_contract() -> None:
    assert set(events_module.__all__) == {
        "DEFAULT_MAX_EVENT_PAYLOAD_BYTES",
        "MAX_EVENT_PAYLOAD_BYTES",
        "MAX_TICK",
        "AuroraEvent",
        "EventError",
        "EventObservability",
        "EventPayload",
        "EventReleaseBatch",
        "EventRuntimeState",
        "EventSchedule",
        "EventSignificance",
        "ScheduledEvent",
        "SimulationResolution",
        "advance_event_schedule",
        "create_event_payload",
        "create_event_state",
        "project_event_for_aurora",
        "project_release_for_aurora",
    }
