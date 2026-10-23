"""Deterministic event scheduling with explicit Aurora visibility boundaries.

The event schedule is validator-owned. It records objective events, releases
them only when an explicit logical tick is advanced, and creates a separate
Aurora-facing projection for observable content. Hidden events, future queue
contents, validator controls, and internal ordering identifiers never enter
that projection.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass, replace
from enum import StrEnum
from typing import Final, cast

DEFAULT_MAX_EVENT_PAYLOAD_BYTES: Final[int] = 262_144
MAX_EVENT_PAYLOAD_BYTES: Final[int] = 1_048_576
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_ENTITY_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
_RESERVED_PAYLOAD_KEYS: Final[frozenset[str]] = frozenset(
    {
        "expected_answer",
        "expected_interpretation",
        "expected_result",
        "failure_conditions",
        "fixture_manifest_sha256",
        "fixture_set_id",
        "future_event_queue",
        "hidden_from_aurora",
        "hidden_state_marker",
        "scenario_id",
        "scenario_name",
        "validator_metadata",
        "validator_notes",
        "world_debug_state",
    }
)
_AURORA_ID_FORBIDDEN_TOKENS: Final[frozenset[str]] = frozenset(
    {
        "EXPECTED",
        "FIXTURE",
        "FUTURE",
        "HIDDEN",
        "SCENARIO",
        "VALIDATOR",
    }
)


class EventError(ValueError):
    """Raised when an event record or deterministic schedule state is invalid."""


class EventObservability(StrEnum):
    """How much of an objective event Aurora can observe."""

    FULLY_OBSERVABLE = "FULLY_OBSERVABLE"
    PARTIALLY_OBSERVABLE = "PARTIALLY_OBSERVABLE"
    HIDDEN = "HIDDEN"


class EventSignificance(StrEnum):
    """Validator-owned significance classification for execution planning."""

    ROUTINE = "ROUTINE"
    NOTABLE = "NOTABLE"
    MAJOR = "MAJOR"
    CRITICAL = "CRITICAL"


class SimulationResolution(StrEnum):
    """Minimum simulation resolution required when an event is processed."""

    BACKGROUND = "BACKGROUND"
    ACTIVE = "ACTIVE"
    FOCUSED = "FOCUSED"
    DEEP = "DEEP"


@dataclass(frozen=True, slots=True)
class EventPayload:
    """Canonical JSON object used by an objective or observable event surface."""

    payload_json: bytes
    payload_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.payload_json, bytes):
            raise EventError("payload_json must be bytes")
        _validate_sha256(self.payload_sha256, field="payload_sha256")
        if hashlib.sha256(self.payload_json).hexdigest() != self.payload_sha256:
            raise EventError("payload_sha256 does not match payload_json")
        if len(self.payload_json) > MAX_EVENT_PAYLOAD_BYTES:
            raise EventError(f"payload_json must not exceed {MAX_EVENT_PAYLOAD_BYTES} bytes")

        decoded = _decode_json_object(self.payload_json)
        _validate_json_value(decoded, path="payload")
        if self.payload_json != _canonical_json_bytes(decoded):
            raise EventError("payload_json must use canonical JSON encoding")

    @property
    def size_bytes(self) -> int:
        """Return the exact canonical payload size."""

        return len(self.payload_json)

    def decode(self) -> dict[str, object]:
        """Return a fresh decoded payload object."""

        return _decode_json_object(self.payload_json)

    def to_mapping(self) -> dict[str, object]:
        """Return the decoded payload plus its deterministic content digest."""

        return {
            "data": self.decode(),
            "payload_sha256": self.payload_sha256,
        }


@dataclass(frozen=True, slots=True)
class ScheduledEvent:
    """Validator-owned objective event and its governed visibility boundary."""

    event_id: str
    sequence: int
    scheduled_tick: int
    actor_id: str
    action: str
    observability: EventObservability
    significance: EventSignificance
    minimum_resolution: SimulationResolution
    objective_payload: EventPayload
    observable_event_id: str | None = None
    observable_payload: EventPayload | None = None

    def __post_init__(self) -> None:
        _validate_control_id(self.event_id, field="event_id")
        _validate_sequence(self.sequence, field="sequence")
        _validate_tick(self.scheduled_tick, field="scheduled_tick")
        _validate_entity_id(self.actor_id, field="actor_id")
        _validate_entity_id(self.action, field="action")
        if not isinstance(self.observability, EventObservability):
            raise EventError("observability must be an EventObservability value")
        if not isinstance(self.significance, EventSignificance):
            raise EventError("significance must be an EventSignificance value")
        if not isinstance(self.minimum_resolution, SimulationResolution):
            raise EventError("minimum_resolution must be a SimulationResolution value")
        if not isinstance(self.objective_payload, EventPayload):
            raise EventError("objective_payload must be an EventPayload")
        if self.observable_event_id is not None:
            _validate_aurora_visible_id(
                self.observable_event_id,
                field="observable_event_id",
            )
        if self.observable_payload is not None and not isinstance(
            self.observable_payload,
            EventPayload,
        ):
            raise EventError("observable_payload must be null or an EventPayload")

        if self.observability is EventObservability.HIDDEN:
            if self.observable_event_id is not None or self.observable_payload is not None:
                raise EventError("hidden event must not define an observable projection")
        elif self.observability is EventObservability.FULLY_OBSERVABLE:
            if self.observable_event_id is None:
                raise EventError("fully observable event requires observable_event_id")
            if self.observable_payload is not None:
                raise EventError(
                    "fully observable event must use objective_payload as its projection"
                )
        else:
            if self.observable_event_id is None or self.observable_payload is None:
                raise EventError(
                    "partially observable event requires an explicit observable projection"
                )
            if self.observable_payload.payload_sha256 == self.objective_payload.payload_sha256:
                raise EventError("partially observable payload must differ from objective_payload")

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete validator-owned event record."""

        return {
            "action": self.action,
            "actor_id": self.actor_id,
            "event_id": self.event_id,
            "minimum_resolution": self.minimum_resolution.value,
            "objective_payload": self.objective_payload.to_mapping(),
            "observability": self.observability.value,
            "observable_event_id": self.observable_event_id,
            "observable_payload": (
                None if self.observable_payload is None else self.observable_payload.to_mapping()
            ),
            "scheduled_tick": self.scheduled_tick,
            "sequence": self.sequence,
            "significance": self.significance.value,
        }


@dataclass(frozen=True, slots=True)
class AuroraEvent:
    """Aurora-safe projection containing no validator or hidden event fields."""

    event_id: str
    occurred_at_tick: int
    payload: EventPayload

    def __post_init__(self) -> None:
        _validate_aurora_visible_id(self.event_id, field="event_id")
        _validate_tick(self.occurred_at_tick, field="occurred_at_tick")
        if not isinstance(self.payload, EventPayload):
            raise EventError("payload must be an EventPayload")

    @property
    def event_sha256(self) -> str:
        """Return a digest derived only from Aurora-visible event content."""

        return hashlib.sha256(_canonical_json_bytes(self.to_mapping())).hexdigest()

    def to_mapping(self) -> dict[str, object]:
        """Return the complete Aurora-facing event representation."""

        return {
            "event_id": self.event_id,
            "occurred_at_tick": self.occurred_at_tick,
            "payload": self.payload.to_mapping(),
        }


@dataclass(frozen=True, slots=True)
class EventSchedule:
    """Immutable, fully ordered validator-owned event schedule."""

    schedule_id: str
    events: tuple[ScheduledEvent, ...]

    def __post_init__(self) -> None:
        _validate_control_id(self.schedule_id, field="schedule_id")
        if not isinstance(self.events, tuple) or not all(
            isinstance(event, ScheduledEvent) for event in self.events
        ):
            raise EventError("events must be a tuple of ScheduledEvent values")

        event_ids: list[str] = []
        observable_event_ids: list[str] = []
        previous_tick: int | None = None
        for expected_sequence, event in enumerate(self.events):
            if event.sequence != expected_sequence:
                raise EventError("event sequence must be contiguous and start at zero")
            if previous_tick is not None and event.scheduled_tick < previous_tick:
                raise EventError("events must be ordered by nondecreasing scheduled_tick")
            event_ids.append(event.event_id)
            if event.observable_event_id is not None:
                observable_event_ids.append(event.observable_event_id)
            previous_tick = event.scheduled_tick

        if len(event_ids) != len(set(event_ids)):
            raise EventError("event_id values must be unique within a schedule")
        if len(observable_event_ids) != len(set(observable_event_ids)):
            raise EventError("observable_event_id values must be unique within a schedule")

    @property
    def schedule_sha256(self) -> str:
        """Return a validator-only digest of the complete objective schedule."""

        return hashlib.sha256(_canonical_json_bytes(self.to_validator_mapping())).hexdigest()

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete schedule, including hidden objective event data."""

        return {
            "events": [event.to_validator_mapping() for event in self.events],
            "schedule_id": self.schedule_id,
        }


@dataclass(frozen=True, slots=True)
class EventRuntimeState:
    """Immutable deterministic cursor for one schedule execution."""

    schedule_id: str
    next_sequence: int = 0
    advanced_through_tick: int | None = None
    last_released_tick: int | None = None
    released_event_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.schedule_id, field="schedule_id")
        _validate_sequence(self.next_sequence, field="next_sequence")
        if self.advanced_through_tick is not None:
            _validate_tick(self.advanced_through_tick, field="advanced_through_tick")
        if self.last_released_tick is not None:
            _validate_tick(self.last_released_tick, field="last_released_tick")
        if not isinstance(self.released_event_ids, tuple) or not all(
            isinstance(event_id, str) for event_id in self.released_event_ids
        ):
            raise EventError("released_event_ids must be a tuple of strings")
        for event_id in self.released_event_ids:
            _validate_control_id(event_id, field="released event ID")
        if len(self.released_event_ids) != len(set(self.released_event_ids)):
            raise EventError("released_event_ids must not contain duplicates")
        if self.next_sequence != len(self.released_event_ids):
            raise EventError("next_sequence must equal released event count")
        if self.released_event_ids and self.last_released_tick is None:
            raise EventError("last_released_tick is required after event release")
        if not self.released_event_ids and self.last_released_tick is not None:
            raise EventError("last_released_tick must be null before event release")
        if self.released_event_ids and self.advanced_through_tick is None:
            raise EventError("advanced_through_tick is required after event release")
        if (
            self.last_released_tick is not None
            and self.advanced_through_tick is not None
            and self.last_released_tick > self.advanced_through_tick
        ):
            raise EventError("last_released_tick must not exceed advanced_through_tick")


@dataclass(frozen=True, slots=True)
class EventReleaseBatch:
    """Events released by one explicit monotonic schedule advancement."""

    advanced_from_tick: int | None
    advanced_through_tick: int
    released_events: tuple[ScheduledEvent, ...]
    state: EventRuntimeState

    def __post_init__(self) -> None:
        if self.advanced_from_tick is not None:
            _validate_tick(self.advanced_from_tick, field="advanced_from_tick")
        _validate_tick(self.advanced_through_tick, field="advanced_through_tick")
        if (
            self.advanced_from_tick is not None
            and self.advanced_from_tick > self.advanced_through_tick
        ):
            raise EventError("advanced_from_tick must not exceed advanced_through_tick")
        if not isinstance(self.released_events, tuple) or not all(
            isinstance(event, ScheduledEvent) for event in self.released_events
        ):
            raise EventError("released_events must be a tuple of ScheduledEvent values")
        if not isinstance(self.state, EventRuntimeState):
            raise EventError("state must be an EventRuntimeState")
        if self.state.advanced_through_tick != self.advanced_through_tick:
            raise EventError("state advancement tick does not match release batch")

        previous_sequence: int | None = None
        released_ids: list[str] = []
        for event in self.released_events:
            if event.scheduled_tick > self.advanced_through_tick:
                raise EventError("release batch contains an event beyond its advancement tick")
            if (
                self.advanced_from_tick is not None
                and event.scheduled_tick <= self.advanced_from_tick
            ):
                raise EventError("release batch contains an event from an earlier advancement")
            if previous_sequence is not None and event.sequence != previous_sequence + 1:
                raise EventError("released events must have contiguous sequence values")
            previous_sequence = event.sequence
            released_ids.append(event.event_id)

        if released_ids:
            if tuple(released_ids) != self.state.released_event_ids[-len(released_ids) :]:
                raise EventError("released events do not match resulting runtime state")
            if self.state.last_released_tick != self.released_events[-1].scheduled_tick:
                raise EventError("last released event tick does not match runtime state")

    @property
    def released(self) -> bool:
        """Return true when this advancement released at least one event."""

        return bool(self.released_events)


def create_event_payload(
    data: Mapping[str, object],
    *,
    max_payload_bytes: int = DEFAULT_MAX_EVENT_PAYLOAD_BYTES,
) -> EventPayload:
    """Create a canonical event payload after recursive boundary validation."""

    if not isinstance(data, Mapping):
        raise EventError("event payload data must be a JSON object")
    if isinstance(max_payload_bytes, bool) or not isinstance(max_payload_bytes, int):
        raise EventError("max_payload_bytes must be an integer")
    if not 1 <= max_payload_bytes <= MAX_EVENT_PAYLOAD_BYTES:
        raise EventError(f"max_payload_bytes must be between 1 and {MAX_EVENT_PAYLOAD_BYTES}")
    normalized = _normalize_json_value(data, path="payload")
    if not isinstance(normalized, dict):
        raise EventError("event payload data must be a JSON object")
    payload_json = _canonical_json_bytes(normalized)
    if len(payload_json) > max_payload_bytes:
        raise EventError(f"event payload must not exceed {max_payload_bytes} bytes")
    return EventPayload(
        payload_json=payload_json,
        payload_sha256=hashlib.sha256(payload_json).hexdigest(),
    )


def create_event_state(schedule: EventSchedule) -> EventRuntimeState:
    """Create a pristine deterministic cursor for an event schedule."""

    if not isinstance(schedule, EventSchedule):
        raise EventError("schedule must be an EventSchedule")
    return EventRuntimeState(schedule_id=schedule.schedule_id)


def advance_event_schedule(
    schedule: EventSchedule,
    state: EventRuntimeState,
    through_tick: int,
) -> EventReleaseBatch:
    """Release all due events through an explicit logical tick, without a clock."""

    _validate_schedule_and_state(schedule, state)
    _validate_tick(through_tick, field="through_tick")
    if state.advanced_through_tick is not None and through_tick < state.advanced_through_tick:
        raise EventError("through_tick must not move an event schedule backward")

    next_sequence = state.next_sequence
    due_events: list[ScheduledEvent] = []
    while next_sequence < len(schedule.events):
        event = schedule.events[next_sequence]
        if event.scheduled_tick > through_tick:
            break
        due_events.append(event)
        next_sequence += 1

    released_events = tuple(due_events)
    released_event_ids = (
        *state.released_event_ids,
        *(event.event_id for event in released_events),
    )
    updated_state = replace(
        state,
        next_sequence=next_sequence,
        advanced_through_tick=through_tick,
        last_released_tick=(
            state.last_released_tick if not released_events else released_events[-1].scheduled_tick
        ),
        released_event_ids=released_event_ids,
    )
    return EventReleaseBatch(
        advanced_from_tick=state.advanced_through_tick,
        advanced_through_tick=through_tick,
        released_events=released_events,
        state=updated_state,
    )


def project_event_for_aurora(event: ScheduledEvent) -> AuroraEvent | None:
    """Project one released event without exposing its validator-owned record."""

    if not isinstance(event, ScheduledEvent):
        raise EventError("event must be a ScheduledEvent")
    if event.observability is EventObservability.HIDDEN:
        return None

    payload = (
        event.objective_payload
        if event.observability is EventObservability.FULLY_OBSERVABLE
        else event.observable_payload
    )
    if event.observable_event_id is None or payload is None:
        raise EventError("observable event is missing its governed projection")
    return AuroraEvent(
        event_id=event.observable_event_id,
        occurred_at_tick=event.scheduled_tick,
        payload=payload,
    )


def project_release_for_aurora(
    batch: EventReleaseBatch,
) -> tuple[AuroraEvent, ...]:
    """Return only observable projections from events released in one batch."""

    if not isinstance(batch, EventReleaseBatch):
        raise EventError("batch must be an EventReleaseBatch")
    projected: list[AuroraEvent] = []
    for event in batch.released_events:
        aurora_event = project_event_for_aurora(event)
        if aurora_event is not None:
            projected.append(aurora_event)
    return tuple(projected)


def _validate_schedule_and_state(
    schedule: EventSchedule,
    state: EventRuntimeState,
) -> None:
    if not isinstance(schedule, EventSchedule):
        raise EventError("schedule must be an EventSchedule")
    if not isinstance(state, EventRuntimeState):
        raise EventError("state must be an EventRuntimeState")
    if state.schedule_id != schedule.schedule_id:
        raise EventError("state schedule_id does not match event schedule")

    expected_events = schedule.events[: state.next_sequence]
    expected_ids = tuple(event.event_id for event in expected_events)
    if state.released_event_ids != expected_ids:
        raise EventError("runtime state does not match the released schedule prefix")
    if expected_events and state.last_released_tick != expected_events[-1].scheduled_tick:
        raise EventError("runtime state last_released_tick does not match schedule")


def _decode_json_object(payload_json: bytes) -> dict[str, object]:
    try:
        decoded = json.loads(
            payload_json.decode("utf-8"),
            parse_constant=_reject_non_finite_json,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise EventError(f"payload_json is not valid JSON: {exc}") from exc
    if not isinstance(decoded, dict):
        raise EventError("payload_json must encode a JSON object")
    return cast(dict[str, object], decoded)


def _canonical_json_bytes(value: object) -> bytes:
    try:
        return json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise EventError(f"value is not JSON-serializable: {exc}") from exc


def _normalize_json_value(value: object, *, path: str) -> object:
    _validate_json_value(value, path=path)
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if isinstance(value, list):
        return [
            _normalize_json_value(item, path=f"{path}[{index}]") for index, item in enumerate(value)
        ]
    if isinstance(value, Mapping):
        return {
            key: _normalize_json_value(item, path=f"{path}.{key}") for key, item in value.items()
        }
    raise EventError(f"{path} contains unsupported JSON value type")


def _validate_json_value(value: object, *, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise EventError(f"{path} contains a non-finite number")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_value(item, path=f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise EventError(f"{path} contains a non-string object key")
            normalized_key = _normalize_metadata_key(key)
            if normalized_key in _RESERVED_PAYLOAD_KEYS:
                raise EventError(f"{path} contains reserved metadata key: {key}")
            _validate_json_value(item, path=f"{path}.{key}")
        return
    raise EventError(f"{path} contains unsupported JSON value type")


def _normalize_metadata_key(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", key.casefold()).strip("_")


def _validate_aurora_visible_id(value: str, *, field: str) -> None:
    _validate_control_id(value, field=field)
    tokens = frozenset(re.split(r"[._-]+", value.upper()))
    forbidden = sorted(tokens & _AURORA_ID_FORBIDDEN_TOKENS)
    if forbidden:
        raise EventError(f"{field} contains Aurora-reserved token(s): {', '.join(forbidden)}")


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise EventError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise EventError(f"{field} must contain 3-128 uppercase identifier characters")


def _validate_entity_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise EventError(f"{field} must be a string")
    if _ENTITY_ID_PATTERN.fullmatch(value) is None:
        raise EventError(f"{field} contains unsupported identifier characters")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise EventError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise EventError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _validate_sequence(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise EventError(f"{field} must be an integer")
    if value < 0:
        raise EventError(f"{field} must be non-negative")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise EventError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise EventError(f"{field} must be between 0 and {MAX_TICK}")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
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
]
