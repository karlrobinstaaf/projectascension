"""Deterministic, provenance-preserving evidence channels into Aurora.

Channels cannot read fixture stores or world state. They admit only explicit
evidence submissions through an open gate, remove validator-only routing
metadata, assign deterministic sequence numbers, and emit immutable packets
safe for Aurora-facing adapters.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass, replace
from enum import StrEnum
from typing import Final

DEFAULT_MAX_CLAIM_BYTES: Final[int] = 65_536
MAX_CLAIM_BYTES: Final[int] = 1_048_576
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_ENTITY_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
_RESERVED_CLAIM_KEYS: Final[frozenset[str]] = frozenset(
    {
        "expected_answer",
        "expected_result",
        "failure_conditions",
        "fixture_manifest_sha256",
        "fixture_set_id",
        "future_event_queue",
        "hidden_state_marker",
        "scenario_id",
        "scenario_name",
        "validator_metadata",
        "validator_notes",
        "world_debug_state",
    }
)
_RUNTIME_ID_FORBIDDEN_TOKENS: Final[frozenset[str]] = frozenset(
    {
        "EXPECTED",
        "FIXTURE",
        "HIDDEN",
        "SCENARIO",
        "VALIDATOR",
    }
)


class ChannelError(ValueError):
    """Raised when channel data or deterministic runtime state is invalid."""


class ChannelKind(StrEnum):
    """Provenance class carried with admitted evidence."""

    DIRECT_OBSERVATION = "DIRECT_OBSERVATION"
    SENSOR = "SENSOR"
    COMMUNICATION = "COMMUNICATION"
    TESTIMONY = "TESTIMONY"
    DOCUMENT = "DOCUMENT"
    SYSTEM_REPORT = "SYSTEM_REPORT"


class ChannelGateState(StrEnum):
    """Whether a channel may currently admit evidence."""

    CLOSED = "CLOSED"
    OPEN = "OPEN"


class RoutingStatus(StrEnum):
    """High-level result of routing one submission."""

    ADMITTED = "ADMITTED"
    BLOCKED = "BLOCKED"


class RoutingReason(StrEnum):
    """Stable reason code for an evidence-routing decision."""

    ADMITTED = "ADMITTED"
    CHANNEL_CLOSED = "CHANNEL_CLOSED"
    CHANNEL_ID_MISMATCH = "CHANNEL_ID_MISMATCH"
    SOURCE_ID_MISMATCH = "SOURCE_ID_MISMATCH"
    DUPLICATE_EVIDENCE_ID = "DUPLICATE_EVIDENCE_ID"
    OUT_OF_ORDER_SUBMISSION = "OUT_OF_ORDER_SUBMISSION"
    CLAIM_TOO_LARGE = "CLAIM_TOO_LARGE"


@dataclass(frozen=True, slots=True)
class EvidenceClaim:
    """Canonical claim content with no validator-owned routing metadata."""

    subject_id: str
    predicate: str
    value_json: bytes
    value_sha256: str

    def __post_init__(self) -> None:
        _validate_entity_id(self.subject_id, field="subject_id")
        _validate_entity_id(self.predicate, field="predicate")
        if not isinstance(self.value_json, bytes):
            raise ChannelError("value_json must be bytes")
        _validate_sha256(self.value_sha256, field="value_sha256")
        if hashlib.sha256(self.value_json).hexdigest() != self.value_sha256:
            raise ChannelError("value_sha256 does not match value_json")

        decoded = _decode_json_value(self.value_json)
        _validate_json_value(decoded, path="value")
        canonical = _canonical_json_bytes(decoded)
        if self.value_json != canonical:
            raise ChannelError("value_json must use canonical JSON encoding")

    @property
    def size_bytes(self) -> int:
        """Return the exact canonical claim-value size."""

        return len(self.value_json)

    def decode_value(self) -> object:
        """Return a fresh decoded value for Aurora-facing serialization."""

        return _decode_json_value(self.value_json)

    def to_mapping(self) -> dict[str, object]:
        """Return the Aurora-safe claim representation."""

        return {
            "predicate": self.predicate,
            "subject_id": self.subject_id,
            "value": self.decode_value(),
            "value_sha256": self.value_sha256,
        }


@dataclass(frozen=True, slots=True)
class ChannelDefinition:
    """Immutable definition of one evidence source and provenance channel."""

    channel_id: str
    kind: ChannelKind
    source_id: str
    max_claim_bytes: int = DEFAULT_MAX_CLAIM_BYTES

    def __post_init__(self) -> None:
        _validate_runtime_control_id(self.channel_id, field="channel_id")
        if not isinstance(self.kind, ChannelKind):
            raise ChannelError("kind must be a ChannelKind value")
        _validate_runtime_control_id(self.source_id, field="source_id")
        if isinstance(self.max_claim_bytes, bool) or not isinstance(
            self.max_claim_bytes,
            int,
        ):
            raise ChannelError("max_claim_bytes must be an integer")
        if not 1 <= self.max_claim_bytes <= MAX_CLAIM_BYTES:
            raise ChannelError(f"max_claim_bytes must be between 1 and {MAX_CLAIM_BYTES}")


@dataclass(frozen=True, slots=True)
class ChannelRuntimeState:
    """Immutable deterministic state of one channel during a harness run."""

    channel_id: str
    gate: ChannelGateState
    next_sequence: int = 1
    last_admitted_tick: int | None = None
    admitted_evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _validate_runtime_control_id(self.channel_id, field="channel_id")
        if not isinstance(self.gate, ChannelGateState):
            raise ChannelError("gate must be a ChannelGateState value")
        if isinstance(self.next_sequence, bool) or not isinstance(
            self.next_sequence,
            int,
        ):
            raise ChannelError("next_sequence must be an integer")
        if self.next_sequence < 1:
            raise ChannelError("next_sequence must be positive")
        if self.last_admitted_tick is not None:
            _validate_tick(self.last_admitted_tick, field="last_admitted_tick")
        if not isinstance(self.admitted_evidence_ids, tuple) or not all(
            isinstance(evidence_id, str) for evidence_id in self.admitted_evidence_ids
        ):
            raise ChannelError("admitted_evidence_ids must be a tuple of strings")
        for evidence_id in self.admitted_evidence_ids:
            _validate_runtime_control_id(evidence_id, field="admitted evidence ID")
        if len(self.admitted_evidence_ids) != len(set(self.admitted_evidence_ids)):
            raise ChannelError("admitted_evidence_ids must not contain duplicates")
        if self.next_sequence != len(self.admitted_evidence_ids) + 1:
            raise ChannelError("next_sequence must equal admitted evidence count plus one")
        if self.admitted_evidence_ids and self.last_admitted_tick is None:
            raise ChannelError("last_admitted_tick is required after evidence admission")
        if not self.admitted_evidence_ids and self.last_admitted_tick is not None:
            raise ChannelError("last_admitted_tick must be null before evidence admission")


@dataclass(frozen=True, slots=True)
class EvidenceSubmission:
    """Validator-side request to admit one explicit claim through a channel."""

    evidence_id: str
    channel_id: str
    source_id: str
    validator_event_id: str
    observed_at_tick: int
    submitted_at_tick: int
    claim: EvidenceClaim

    def __post_init__(self) -> None:
        _validate_runtime_control_id(self.evidence_id, field="evidence_id")
        _validate_runtime_control_id(self.channel_id, field="channel_id")
        _validate_runtime_control_id(self.source_id, field="source_id")
        _validate_control_id(self.validator_event_id, field="validator_event_id")
        _validate_tick(self.observed_at_tick, field="observed_at_tick")
        _validate_tick(self.submitted_at_tick, field="submitted_at_tick")
        if self.observed_at_tick > self.submitted_at_tick:
            raise ChannelError("observed_at_tick must not exceed submitted_at_tick")
        if not isinstance(self.claim, EvidenceClaim):
            raise ChannelError("claim must be an EvidenceClaim")


@dataclass(frozen=True, slots=True)
class AuroraEvidencePacket:
    """Immutable admitted packet containing only Aurora-safe evidence fields."""

    evidence_id: str
    channel_id: str
    channel_kind: ChannelKind
    source_id: str
    observed_at_tick: int
    admitted_at_tick: int
    sequence: int
    claim: EvidenceClaim

    def __post_init__(self) -> None:
        _validate_runtime_control_id(self.evidence_id, field="evidence_id")
        _validate_runtime_control_id(self.channel_id, field="channel_id")
        if not isinstance(self.channel_kind, ChannelKind):
            raise ChannelError("channel_kind must be a ChannelKind value")
        _validate_runtime_control_id(self.source_id, field="source_id")
        _validate_tick(self.observed_at_tick, field="observed_at_tick")
        _validate_tick(self.admitted_at_tick, field="admitted_at_tick")
        if self.observed_at_tick > self.admitted_at_tick:
            raise ChannelError("observed_at_tick must not exceed admitted_at_tick")
        if isinstance(self.sequence, bool) or not isinstance(self.sequence, int):
            raise ChannelError("sequence must be an integer")
        if self.sequence < 1:
            raise ChannelError("sequence must be positive")
        if not isinstance(self.claim, EvidenceClaim):
            raise ChannelError("claim must be an EvidenceClaim")

    @property
    def packet_sha256(self) -> str:
        """Return a deterministic fingerprint of Aurora-visible packet data."""

        payload = json.dumps(
            self.to_mapping(),
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
        return hashlib.sha256(payload).hexdigest()

    def to_mapping(self) -> dict[str, object]:
        """Return the complete Aurora-facing representation."""

        return {
            "admitted_at_tick": self.admitted_at_tick,
            "channel_id": self.channel_id,
            "channel_kind": self.channel_kind.value,
            "claim": self.claim.to_mapping(),
            "evidence_id": self.evidence_id,
            "observed_at_tick": self.observed_at_tick,
            "sequence": self.sequence,
            "source_id": self.source_id,
        }


@dataclass(frozen=True, slots=True)
class ChannelRoutingResult:
    """Result and resulting immutable state after one routing attempt."""

    status: RoutingStatus
    reason: RoutingReason
    state: ChannelRuntimeState
    packet: AuroraEvidencePacket | None

    def __post_init__(self) -> None:
        if not isinstance(self.status, RoutingStatus):
            raise ChannelError("status must be a RoutingStatus value")
        if not isinstance(self.reason, RoutingReason):
            raise ChannelError("reason must be a RoutingReason value")
        if not isinstance(self.state, ChannelRuntimeState):
            raise ChannelError("state must be a ChannelRuntimeState")
        if self.packet is not None and not isinstance(
            self.packet,
            AuroraEvidencePacket,
        ):
            raise ChannelError("packet must be null or an AuroraEvidencePacket")

        if self.status is RoutingStatus.ADMITTED:
            if self.reason is not RoutingReason.ADMITTED or self.packet is None:
                raise ChannelError("admitted result requires admitted reason and packet")
            if self.packet.channel_id != self.state.channel_id:
                raise ChannelError("admitted packet channel does not match resulting state")
            if self.state.next_sequence != self.packet.sequence + 1:
                raise ChannelError("admitted packet sequence does not match resulting state")
            if (
                not self.state.admitted_evidence_ids
                or self.state.admitted_evidence_ids[-1] != self.packet.evidence_id
            ):
                raise ChannelError("admitted packet is not recorded in resulting state")
            if self.state.last_admitted_tick != self.packet.admitted_at_tick:
                raise ChannelError("admitted packet tick does not match resulting state")
        elif self.reason is RoutingReason.ADMITTED or self.packet is not None:
            raise ChannelError("blocked result requires blocked reason and no packet")

    @property
    def admitted(self) -> bool:
        """Return true only when an Aurora evidence packet was emitted."""

        return self.status is RoutingStatus.ADMITTED


def create_evidence_claim(
    subject_id: str,
    predicate: str,
    value: object,
) -> EvidenceClaim:
    """Create a canonical evidence claim after recursive metadata validation."""

    _validate_entity_id(subject_id, field="subject_id")
    _validate_entity_id(predicate, field="predicate")
    _validate_json_value(value, path="value")
    value_json = _canonical_json_bytes(value)
    return EvidenceClaim(
        subject_id=subject_id,
        predicate=predicate,
        value_json=value_json,
        value_sha256=hashlib.sha256(value_json).hexdigest(),
    )


def create_channel_state(
    definition: ChannelDefinition,
    *,
    gate: ChannelGateState = ChannelGateState.CLOSED,
) -> ChannelRuntimeState:
    """Create pristine deterministic state for a channel definition."""

    if not isinstance(definition, ChannelDefinition):
        raise ChannelError("definition must be a ChannelDefinition")
    if not isinstance(gate, ChannelGateState):
        raise ChannelError("gate must be a ChannelGateState value")
    return ChannelRuntimeState(channel_id=definition.channel_id, gate=gate)


def set_channel_gate(
    definition: ChannelDefinition,
    state: ChannelRuntimeState,
    gate: ChannelGateState,
) -> ChannelRuntimeState:
    """Return state with an explicitly changed gate and no other mutation."""

    _validate_definition_and_state(definition, state)
    if not isinstance(gate, ChannelGateState):
        raise ChannelError("gate must be a ChannelGateState value")
    return replace(state, gate=gate)


def route_submission(
    definition: ChannelDefinition,
    state: ChannelRuntimeState,
    submission: EvidenceSubmission,
) -> ChannelRoutingResult:
    """Route one explicit submission without consulting hidden system state."""

    _validate_definition_and_state(definition, state)
    if not isinstance(submission, EvidenceSubmission):
        raise ChannelError("submission must be an EvidenceSubmission")

    if submission.channel_id != definition.channel_id:
        return _blocked(state, RoutingReason.CHANNEL_ID_MISMATCH)
    if submission.source_id != definition.source_id:
        return _blocked(state, RoutingReason.SOURCE_ID_MISMATCH)
    if state.gate is ChannelGateState.CLOSED:
        return _blocked(state, RoutingReason.CHANNEL_CLOSED)
    if submission.evidence_id in state.admitted_evidence_ids:
        return _blocked(state, RoutingReason.DUPLICATE_EVIDENCE_ID)
    if (
        state.last_admitted_tick is not None
        and submission.submitted_at_tick < state.last_admitted_tick
    ):
        return _blocked(state, RoutingReason.OUT_OF_ORDER_SUBMISSION)
    if submission.claim.size_bytes > definition.max_claim_bytes:
        return _blocked(state, RoutingReason.CLAIM_TOO_LARGE)

    packet = AuroraEvidencePacket(
        evidence_id=submission.evidence_id,
        channel_id=definition.channel_id,
        channel_kind=definition.kind,
        source_id=definition.source_id,
        observed_at_tick=submission.observed_at_tick,
        admitted_at_tick=submission.submitted_at_tick,
        sequence=state.next_sequence,
        claim=submission.claim,
    )
    updated_state = replace(
        state,
        next_sequence=state.next_sequence + 1,
        last_admitted_tick=submission.submitted_at_tick,
        admitted_evidence_ids=(
            *state.admitted_evidence_ids,
            submission.evidence_id,
        ),
    )
    return ChannelRoutingResult(
        status=RoutingStatus.ADMITTED,
        reason=RoutingReason.ADMITTED,
        state=updated_state,
        packet=packet,
    )


def _blocked(
    state: ChannelRuntimeState,
    reason: RoutingReason,
) -> ChannelRoutingResult:
    return ChannelRoutingResult(
        status=RoutingStatus.BLOCKED,
        reason=reason,
        state=state,
        packet=None,
    )


def _validate_definition_and_state(
    definition: ChannelDefinition,
    state: ChannelRuntimeState,
) -> None:
    if not isinstance(definition, ChannelDefinition):
        raise ChannelError("definition must be a ChannelDefinition")
    if not isinstance(state, ChannelRuntimeState):
        raise ChannelError("state must be a ChannelRuntimeState")
    if state.channel_id != definition.channel_id:
        raise ChannelError("state channel_id does not match channel definition")


def _decode_json_value(value_json: bytes) -> object:
    try:
        text = value_json.decode("utf-8")
        return json.loads(text, parse_constant=_reject_non_finite_json)
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise ChannelError(f"value_json is not valid JSON: {exc}") from exc


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
        raise ChannelError(f"value is not JSON-serializable: {exc}") from exc


def _validate_json_value(value: object, *, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ChannelError(f"{path} contains a non-finite number")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_value(item, path=f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ChannelError(f"{path} contains a non-string object key")
            normalized_key = _normalize_metadata_key(key)
            if normalized_key in _RESERVED_CLAIM_KEYS:
                raise ChannelError(f"{path} contains reserved metadata key: {key}")
            _validate_json_value(item, path=f"{path}.{key}")
        return
    raise ChannelError(f"{path} contains unsupported JSON value type")


def _normalize_metadata_key(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", key.casefold()).strip("_")


def _validate_runtime_control_id(value: str, *, field: str) -> None:
    _validate_control_id(value, field=field)
    tokens = frozenset(re.split(r"[._-]+", value.upper()))
    forbidden = sorted(tokens & _RUNTIME_ID_FORBIDDEN_TOKENS)
    if forbidden:
        raise ChannelError(f"{field} contains validator-reserved token(s): {', '.join(forbidden)}")


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise ChannelError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise ChannelError(f"{field} must contain 3-128 uppercase identifier characters")


def _validate_entity_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise ChannelError(f"{field} must be a string")
    if _ENTITY_ID_PATTERN.fullmatch(value) is None:
        raise ChannelError(f"{field} contains unsupported identifier characters")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise ChannelError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise ChannelError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ChannelError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise ChannelError(f"{field} must be between 0 and {MAX_TICK}")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
    "DEFAULT_MAX_CLAIM_BYTES",
    "MAX_CLAIM_BYTES",
    "MAX_TICK",
    "AuroraEvidencePacket",
    "ChannelDefinition",
    "ChannelError",
    "ChannelGateState",
    "ChannelKind",
    "ChannelRoutingResult",
    "ChannelRuntimeState",
    "EvidenceClaim",
    "EvidenceSubmission",
    "RoutingReason",
    "RoutingStatus",
    "create_channel_state",
    "create_evidence_claim",
    "route_submission",
    "set_channel_gate",
]
