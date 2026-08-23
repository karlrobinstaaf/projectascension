"""Least-privilege reference runtime for FOUND-001.

The adapter consumes only the Aurora fixture capability and Aurora-safe step
inputs. It does not import the validator-owned scenario plan, inspect hidden
partitions, or encode the scenario's expected answer. Communication is derived
from the belief and memory state already available to Aurora.
"""

from __future__ import annotations

from collections.abc import Mapping
from enum import StrEnum
from typing import Final, NoReturn, cast

from aurora_validation_harness.fixtures import FixturePartition
from aurora_validation_harness.harness import AuroraResetRequest, AuroraStepRequest
from aurora_validation_harness.partitions import AccessPrincipal
from aurora_validation_harness.snapshots import create_snapshot_state

SUPPORTED_FOUND_001_RUNTIME_VERSION: Final[str] = "1.0"
SUPPORTED_FOUND_001_FIXTURE_SCHEMA_VERSION: Final[str] = "1.0"
QUESTION_EVENT_ID: Final[str] = "OBS-FOUND-001-E2"

_AURORA_SUBJECT_ID: Final[str] = "aurora"
_LOCATION_SUBJECT_ID: Final[str] = "mara"
_UNKNOWN_BELIEF: Final[str] = "UNKNOWN"
_CURRENT_LOCATION_BELIEF_KEY: Final[str] = "mara_current_location"
_LAST_KNOWN_LOCATION_FACT: Final[str] = "MARA_LAST_KNOWN_LOCATION"
_FIXTURE_KEYS: Final[frozenset[str]] = frozenset(
    {
        "accessible_location_sources",
        "fixture_schema_version",
        "initial_state",
        "subject_id",
    }
)
_STATE_KEYS: Final[frozenset[str]] = frozenset(
    {
        "active_goal",
        "active_prediction",
        "attention",
        "beliefs",
        "current_location",
        "emotion",
        "memories",
        "relationship_with_mara",
        "uncertainty",
    }
)
_QUESTION_PAYLOAD_KEYS: Final[frozenset[str]] = frozenset(
    {
        "question",
        "subject_id",
        "supplies_current_location_evidence",
    }
)


class Found001RuntimeFailureReason(StrEnum):
    """Stable fail-closed reason codes for the reference adapter."""

    INVALID_REQUEST = "INVALID_REQUEST"
    INVALID_FIXTURE = "INVALID_FIXTURE"
    NOT_RESET = "NOT_RESET"
    RUN_MISMATCH = "RUN_MISMATCH"
    STATE_MISMATCH = "STATE_MISMATCH"
    UNSUPPORTED_INPUT = "UNSUPPORTED_INPUT"


class Found001RuntimeError(RuntimeError):
    """Raised when the adapter cannot safely execute a requested operation."""

    def __init__(self, reason: Found001RuntimeFailureReason, message: str) -> None:
        if not isinstance(reason, Found001RuntimeFailureReason):
            raise TypeError("reason must be a Found001RuntimeFailureReason")
        if not isinstance(message, str) or not message.strip():
            raise TypeError("message must be a non-empty string")
        self.reason = reason
        self.detail = message
        super().__init__(f"{reason.value}: {message}")


class Found001Runtime:
    """Deterministic runtime that preserves FOUND-001 information isolation."""

    __slots__ = ("_run_id", "_seen_event_ids", "_state_sha256", "_tick")

    def __init__(self) -> None:
        self._run_id: str | None = None
        self._state_sha256: str | None = None
        self._tick: int | None = None
        self._seen_event_ids: set[str] = set()

    @property
    def initialized(self) -> bool:
        """Return whether a successful reset has established fresh run state."""

        return self._run_id is not None

    @property
    def current_tick(self) -> int | None:
        """Return the last accepted logical tick, or null before reset."""

        return self._tick

    def reset(self, request: AuroraResetRequest, /) -> Mapping[str, object]:
        """Load a fresh state exclusively from the scoped Aurora fixture."""

        if not isinstance(request, AuroraResetRequest):
            _fail(
                Found001RuntimeFailureReason.INVALID_REQUEST,
                "reset request must be an AuroraResetRequest",
            )
        if request.fixtures.principal is not AccessPrincipal.AURORA_RUNTIME:
            _fail(
                Found001RuntimeFailureReason.INVALID_REQUEST,
                "reset requires an AURORA_RUNTIME fixture capability",
            )
        if request.fixtures.permitted_partitions != frozenset({FixturePartition.AURORA}):
            _fail(
                Found001RuntimeFailureReason.INVALID_FIXTURE,
                "reset capability must contain only the AURORA partition",
            )

        artifacts = request.fixtures.by_partition(FixturePartition.AURORA)
        if len(artifacts) != 1:
            _fail(
                Found001RuntimeFailureReason.INVALID_FIXTURE,
                "FOUND-001 requires exactly one Aurora fixture artifact",
            )
        try:
            fixture = artifacts[0].decode_json_object()
        except (TypeError, ValueError) as exc:
            raise Found001RuntimeError(
                Found001RuntimeFailureReason.INVALID_FIXTURE,
                "Aurora fixture must be a valid JSON object",
            ) from exc

        state = _validate_fixture(fixture)
        frozen_state = create_snapshot_state(state)
        self._run_id = request.run_id
        self._tick = request.initial_tick
        self._state_sha256 = frozen_state.state_sha256
        self._seen_event_ids.clear()
        return cast(dict[str, object], frozen_state.decode())

    def advance(self, request: AuroraStepRequest, /) -> Mapping[str, object]:
        """Apply one governed Aurora-safe input batch deterministically."""

        if not isinstance(request, AuroraStepRequest):
            _fail(
                Found001RuntimeFailureReason.INVALID_REQUEST,
                "step request must be an AuroraStepRequest",
            )
        if not self.initialized or self._tick is None or self._state_sha256 is None:
            _fail(
                Found001RuntimeFailureReason.NOT_RESET,
                "runtime must be reset before advance",
            )
        if request.run_id != self._run_id:
            _fail(
                Found001RuntimeFailureReason.RUN_MISMATCH,
                "step run_id does not match the active run",
            )
        if request.previous_tick != self._tick:
            _fail(
                Found001RuntimeFailureReason.STATE_MISMATCH,
                "step previous_tick does not match the active runtime tick",
            )
        if request.previous_state.state_sha256 != self._state_sha256:
            _fail(
                Found001RuntimeFailureReason.STATE_MISMATCH,
                "step previous_state does not match the active runtime state",
            )
        if request.evidence_packets:
            _fail(
                Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
                "FOUND-001 core execution does not admit evidence packets",
            )

        state = request.previous_state.decode()
        seen_event_ids = set(self._seen_event_ids)
        for event in request.events:
            if event.event_id in seen_event_ids:
                _fail(
                    Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
                    "an Aurora-visible event must not be processed more than once",
                )
            if event.occurred_at_tick <= request.previous_tick:
                _fail(
                    Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
                    "event tick must follow the preceding runtime tick",
                )
            state = _apply_event(state, event.event_id, event.payload.decode())
            seen_event_ids.add(event.event_id)

        frozen_state = create_snapshot_state(state)
        self._tick = request.through_tick
        self._state_sha256 = frozen_state.state_sha256
        self._seen_event_ids = seen_event_ids
        return cast(dict[str, object], frozen_state.decode())


def _validate_fixture(fixture: Mapping[str, object]) -> dict[str, object]:
    _require_exact_keys(fixture, _FIXTURE_KEYS, field="Aurora fixture")
    if fixture["fixture_schema_version"] != SUPPORTED_FOUND_001_FIXTURE_SCHEMA_VERSION:
        _fail(
            Found001RuntimeFailureReason.INVALID_FIXTURE,
            "unsupported Aurora fixture_schema_version",
        )
    if fixture["subject_id"] != _AURORA_SUBJECT_ID:
        _fail(
            Found001RuntimeFailureReason.INVALID_FIXTURE,
            "Aurora fixture subject_id is invalid",
        )

    sources = _require_mapping(
        fixture["accessible_location_sources"],
        field="accessible_location_sources",
    )
    if not sources or not all(
        isinstance(source_id, str) and source_id and isinstance(source_state, str) and source_state
        for source_id, source_state in sources.items()
    ):
        _fail(
            Found001RuntimeFailureReason.INVALID_FIXTURE,
            "accessible_location_sources must contain non-empty string states",
        )

    state = _require_mapping(fixture["initial_state"], field="initial_state")
    _require_exact_keys(state, _STATE_KEYS, field="initial_state")
    _validate_initial_state(state)
    return cast(dict[str, object], create_snapshot_state(state).decode())


def _validate_initial_state(state: Mapping[str, object]) -> None:
    for key in ("attention", "current_location", "emotion", "relationship_with_mara"):
        _require_non_empty_string(state[key], field=f"initial_state.{key}")

    beliefs = _require_mapping(state["beliefs"], field="initial_state.beliefs")
    location_belief = _require_mapping(
        beliefs.get(_CURRENT_LOCATION_BELIEF_KEY),
        field=f"initial_state.beliefs.{_CURRENT_LOCATION_BELIEF_KEY}",
    )
    _require_exact_keys(
        location_belief,
        frozenset({"confidence", "value"}),
        field=f"initial_state.beliefs.{_CURRENT_LOCATION_BELIEF_KEY}",
    )
    _require_non_empty_string(
        location_belief["value"],
        field=f"initial_state.beliefs.{_CURRENT_LOCATION_BELIEF_KEY}.value",
    )
    confidence = location_belief["confidence"]
    if confidence is not None and (not isinstance(confidence, str) or not confidence):
        _fail(
            Found001RuntimeFailureReason.INVALID_FIXTURE,
            "location belief confidence must be null or a non-empty string",
        )

    uncertainty = _require_mapping(
        state["uncertainty"],
        field="initial_state.uncertainty",
    )
    _require_non_empty_string(
        uncertainty.get(_CURRENT_LOCATION_BELIEF_KEY),
        field=f"initial_state.uncertainty.{_CURRENT_LOCATION_BELIEF_KEY}",
    )

    memories = state["memories"]
    if not isinstance(memories, list) or not all(
        isinstance(memory, Mapping) for memory in memories
    ):
        _fail(
            Found001RuntimeFailureReason.INVALID_FIXTURE,
            "initial_state.memories must be an array of objects",
        )
    _last_known_location(memories)


def _apply_event(
    state: Mapping[str, object],
    event_id: str,
    payload: Mapping[str, object],
) -> dict[str, object]:
    if event_id != QUESTION_EVENT_ID:
        _fail(
            Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
            "FOUND-001 received an unsupported Aurora-visible event",
        )
    _require_exact_keys(
        payload,
        _QUESTION_PAYLOAD_KEYS,
        field="question event payload",
        reason=Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
    )
    _require_non_empty_string(
        payload["question"],
        field="question event payload.question",
        reason=Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
    )
    if payload["subject_id"] != _LOCATION_SUBJECT_ID:
        _fail(
            Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
            "question event subject_id is unsupported",
        )
    if payload["supplies_current_location_evidence"] is not False:
        _fail(
            Found001RuntimeFailureReason.UNSUPPORTED_INPUT,
            "the core question event must not supply current-location evidence",
        )

    updated = cast(dict[str, object], create_snapshot_state(state).decode())
    beliefs = _require_mapping(
        updated["beliefs"],
        field="state.beliefs",
        reason=Found001RuntimeFailureReason.STATE_MISMATCH,
    )
    location_belief = _require_mapping(
        beliefs.get(_CURRENT_LOCATION_BELIEF_KEY),
        field=f"state.beliefs.{_CURRENT_LOCATION_BELIEF_KEY}",
        reason=Found001RuntimeFailureReason.STATE_MISMATCH,
    )
    epistemic_status = _require_non_empty_string(
        location_belief.get("value"),
        field=f"state.beliefs.{_CURRENT_LOCATION_BELIEF_KEY}.value",
        reason=Found001RuntimeFailureReason.STATE_MISMATCH,
    )
    memories = updated["memories"]
    if not isinstance(memories, list):
        _fail(
            Found001RuntimeFailureReason.STATE_MISMATCH,
            "state.memories must remain an array",
        )

    claims_current_location = epistemic_status != _UNKNOWN_BELIEF
    updated["communication"] = {
        "claims_current_location": claims_current_location,
        "epistemic_status": epistemic_status,
        "reported_current_location": epistemic_status if claims_current_location else None,
        "reported_last_known_location": _last_known_location(
            memories,
            reason=Found001RuntimeFailureReason.STATE_MISMATCH,
        ),
    }
    return updated


def _last_known_location(
    memories: list[object],
    *,
    reason: Found001RuntimeFailureReason = Found001RuntimeFailureReason.INVALID_FIXTURE,
) -> str | None:
    locations: list[str] = []
    for memory in memories:
        if not isinstance(memory, Mapping):
            _fail(
                reason,
                "memory entries must be objects",
            )
        if memory.get("fact") != _LAST_KNOWN_LOCATION_FACT:
            continue
        locations.append(
            _require_non_empty_string(
                memory.get("location"),
                field="last-known-location memory.location",
                reason=reason,
            )
        )
    if len(locations) > 1:
        _fail(
            reason,
            "Aurora state contains ambiguous last-known-location memories",
        )
    return None if not locations else locations[0]


def _require_mapping(
    value: object,
    *,
    field: str,
    reason: Found001RuntimeFailureReason = Found001RuntimeFailureReason.INVALID_FIXTURE,
) -> Mapping[str, object]:
    if not isinstance(value, Mapping) or not all(isinstance(key, str) for key in value):
        _fail(
            reason,
            f"{field} must be an object with string keys",
        )
    return value


def _require_exact_keys(
    value: Mapping[str, object],
    expected: frozenset[str],
    *,
    field: str,
    reason: Found001RuntimeFailureReason = Found001RuntimeFailureReason.INVALID_FIXTURE,
) -> None:
    actual = frozenset(value)
    if actual != expected:
        _fail(
            reason,
            f"{field} must contain exactly the governed fields",
        )


def _require_non_empty_string(
    value: object,
    *,
    field: str,
    reason: Found001RuntimeFailureReason = Found001RuntimeFailureReason.INVALID_FIXTURE,
) -> str:
    if not isinstance(value, str) or not value:
        _fail(
            reason,
            f"{field} must be a non-empty string",
        )
    return value


def _fail(reason: Found001RuntimeFailureReason, message: str) -> NoReturn:
    raise Found001RuntimeError(reason, message)


def create_runtime() -> Found001Runtime:
    """Return a fresh FOUND-001 runtime adapter for CLI factory resolution."""

    return Found001Runtime()


__all__ = [
    "QUESTION_EVENT_ID",
    "SUPPORTED_FOUND_001_FIXTURE_SCHEMA_VERSION",
    "SUPPORTED_FOUND_001_RUNTIME_VERSION",
    "Found001Runtime",
    "Found001RuntimeError",
    "Found001RuntimeFailureReason",
    "create_runtime",
]
