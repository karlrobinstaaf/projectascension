"""Deterministic, validator-owned state snapshots for Aurora validation runs.

Snapshots preserve exact state at explicit logical ticks without becoming an
input channel into Aurora.  The module freezes detached canonical JSON,
separates the pure state digest from run-specific provenance, and binds ordered
captures into an immutable hash chain.  Structural integrity is enforced here;
semantic validity belongs to transition and assertion modules so that an
invalid Aurora state can still be captured as evidence.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Final, cast

from aurora_validation_harness.evidence import (
    EvidenceDomain,
    EvidencePayload,
    EvidenceSource,
    EvidenceSourceKind,
    create_evidence_payload,
)

SUPPORTED_SNAPSHOT_SCHEMA_VERSION: Final[str] = "1.0"
DEFAULT_MAX_SNAPSHOT_STATE_BYTES: Final[int] = 4_194_304
MAX_SNAPSHOT_STATE_BYTES: Final[int] = 16_777_216
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_ENTITY_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")


class SnapshotError(ValueError):
    """Raised when snapshot state, provenance, or chain integrity is invalid."""


class SnapshotPhase(StrEnum):
    """Stable reason for capturing one state snapshot."""

    INITIAL = "INITIAL"
    PRE_EVENT = "PRE_EVENT"
    POST_EVENT = "POST_EVENT"
    CHECKPOINT = "CHECKPOINT"
    FINAL = "FINAL"
    FAILURE = "FAILURE"


@dataclass(frozen=True, slots=True)
class SnapshotState:
    """Detached canonical JSON state and its content-only integrity digest."""

    state_json: bytes
    state_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.state_json, bytes):
            raise SnapshotError("state_json must be bytes")
        _validate_sha256(self.state_sha256, field="state_sha256")
        if hashlib.sha256(self.state_json).hexdigest() != self.state_sha256:
            raise SnapshotError("state_sha256 does not match state_json")
        if len(self.state_json) > MAX_SNAPSHOT_STATE_BYTES:
            raise SnapshotError(f"state_json must not exceed {MAX_SNAPSHOT_STATE_BYTES} bytes")

        decoded = _decode_json_object(self.state_json)
        _validate_json_value(decoded, path="state")
        if self.state_json != _canonical_json_bytes(decoded):
            raise SnapshotError("state_json must use canonical JSON encoding")

    @property
    def size_bytes(self) -> int:
        """Return the exact byte size of the canonical state."""

        return len(self.state_json)

    def decode(self) -> dict[str, object]:
        """Return a fresh detached copy of the captured state."""

        return _decode_json_object(self.state_json)

    def to_mapping(self) -> dict[str, object]:
        """Return the portable state representation."""

        return {
            "data": self.decode(),
            "state_sha256": self.state_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> SnapshotState:
        """Parse and verify a portable snapshot state."""

        mapping = _require_mapping(value, field="snapshot state")
        _require_exact_keys(
            mapping,
            required=frozenset({"data", "state_sha256"}),
            field="snapshot state",
        )
        data = _require_mapping(mapping["data"], field="snapshot state.data")
        declared_sha256 = _require_string(
            mapping["state_sha256"],
            field="snapshot state.state_sha256",
        )
        state = create_snapshot_state(
            data,
            max_state_bytes=MAX_SNAPSHOT_STATE_BYTES,
        )
        if state.state_sha256 != declared_sha256:
            raise SnapshotError("declared state_sha256 does not match snapshot state")
        return state


@dataclass(frozen=True, slots=True)
class StateSnapshot:
    """One provenance-bound capture of a state domain at a logical tick."""

    snapshot_id: str
    run_id: str
    scenario_id: str
    sequence: int
    captured_at_tick: int
    phase: SnapshotPhase
    domain: EvidenceDomain
    subject_id: str
    producer_id: str
    checkpoint_id: str | None
    state: SnapshotState
    previous_snapshot_sha256: str | None

    def __post_init__(self) -> None:
        _validate_control_id(self.snapshot_id, field="snapshot_id")
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        _validate_sequence(self.sequence, field="sequence")
        _validate_tick(self.captured_at_tick, field="captured_at_tick")
        if not isinstance(self.phase, SnapshotPhase):
            raise SnapshotError("phase must be a SnapshotPhase value")
        if not isinstance(self.domain, EvidenceDomain):
            raise SnapshotError("domain must be an EvidenceDomain value")
        _validate_entity_id(self.subject_id, field="subject_id")
        _validate_control_id(self.producer_id, field="producer_id")
        if self.checkpoint_id is not None:
            _validate_control_id(self.checkpoint_id, field="checkpoint_id")
        if self.phase is SnapshotPhase.CHECKPOINT and self.checkpoint_id is None:
            raise SnapshotError("CHECKPOINT snapshot requires checkpoint_id")
        if not isinstance(self.state, SnapshotState):
            raise SnapshotError("state must be a SnapshotState")
        if self.previous_snapshot_sha256 is not None:
            _validate_sha256(
                self.previous_snapshot_sha256,
                field="previous_snapshot_sha256",
            )
        if self.sequence == 0 and self.previous_snapshot_sha256 is not None:
            raise SnapshotError("first state snapshot must not declare a previous hash")
        if self.sequence > 0 and self.previous_snapshot_sha256 is None:
            raise SnapshotError("non-first state snapshot requires a previous hash")

    @property
    def snapshot_sha256(self) -> str:
        """Return the digest binding state content, provenance, and chain position."""

        return calculate_state_snapshot_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "captured_at_tick": self.captured_at_tick,
            "checkpoint_id": self.checkpoint_id,
            "domain": self.domain.value,
            "phase": self.phase.value,
            "previous_snapshot_sha256": self.previous_snapshot_sha256,
            "producer_id": self.producer_id,
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "sequence": self.sequence,
            "snapshot_id": self.snapshot_id,
            "snapshot_schema_version": SUPPORTED_SNAPSHOT_SCHEMA_VERSION,
            "snapshot_type": "STATE_SNAPSHOT",
            "state": self.state.to_mapping(),
            "subject_id": self.subject_id,
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete validator-owned snapshot representation."""

        return {
            **self._content_mapping(),
            "snapshot_sha256": self.snapshot_sha256,
        }

    def to_evidence_mapping(self) -> dict[str, object]:
        """Return a compact evidence summary without embedding captured state."""

        return {
            "captured_at_tick": self.captured_at_tick,
            "checkpoint_id": self.checkpoint_id,
            "domain": self.domain.value,
            "phase": self.phase.value,
            "snapshot_id": self.snapshot_id,
            "snapshot_sha256": self.snapshot_sha256,
            "state_sha256": self.state.state_sha256,
            "state_size_bytes": self.state.size_bytes,
            "subject_id": self.subject_id,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> StateSnapshot:
        """Parse and verify a serialized state snapshot."""

        mapping = _require_mapping(value, field="state snapshot")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "captured_at_tick",
                    "checkpoint_id",
                    "domain",
                    "phase",
                    "previous_snapshot_sha256",
                    "producer_id",
                    "run_id",
                    "scenario_id",
                    "sequence",
                    "snapshot_id",
                    "snapshot_schema_version",
                    "snapshot_sha256",
                    "snapshot_type",
                    "state",
                    "subject_id",
                }
            ),
            field="state snapshot",
        )
        _validate_schema_version(mapping["snapshot_schema_version"])
        if mapping["snapshot_type"] != "STATE_SNAPSHOT":
            raise SnapshotError("unsupported snapshot_type")
        snapshot = cls(
            snapshot_id=_require_string(
                mapping["snapshot_id"],
                field="state snapshot.snapshot_id",
            ),
            run_id=_require_string(mapping["run_id"], field="state snapshot.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"],
                field="state snapshot.scenario_id",
            ),
            sequence=_require_integer(
                mapping["sequence"],
                field="state snapshot.sequence",
            ),
            captured_at_tick=_require_integer(
                mapping["captured_at_tick"],
                field="state snapshot.captured_at_tick",
            ),
            phase=_parse_enum(
                SnapshotPhase,
                mapping["phase"],
                field="state snapshot.phase",
            ),
            domain=_parse_enum(
                EvidenceDomain,
                mapping["domain"],
                field="state snapshot.domain",
            ),
            subject_id=_require_string(
                mapping["subject_id"],
                field="state snapshot.subject_id",
            ),
            producer_id=_require_string(
                mapping["producer_id"],
                field="state snapshot.producer_id",
            ),
            checkpoint_id=_require_optional_string(
                mapping["checkpoint_id"],
                field="state snapshot.checkpoint_id",
            ),
            state=SnapshotState.from_mapping(
                _require_mapping(mapping["state"], field="state snapshot.state")
            ),
            previous_snapshot_sha256=_require_optional_string(
                mapping["previous_snapshot_sha256"],
                field="state snapshot.previous_snapshot_sha256",
            ),
        )
        declared_sha256 = _require_string(
            mapping["snapshot_sha256"],
            field="state snapshot.snapshot_sha256",
        )
        if snapshot.snapshot_sha256 != declared_sha256:
            raise SnapshotError("declared snapshot_sha256 does not match state snapshot")
        return snapshot


@dataclass(frozen=True, slots=True)
class SnapshotSeries:
    """Immutable append-only snapshot chain for one validation run."""

    run_id: str
    scenario_id: str
    snapshots: tuple[StateSnapshot, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        if not isinstance(self.snapshots, tuple) or not all(
            isinstance(snapshot, StateSnapshot) for snapshot in self.snapshots
        ):
            raise SnapshotError("snapshots must be a tuple of StateSnapshot values")

        seen_snapshot_ids: set[str] = set()
        seen_capture_keys: set[tuple[str, SnapshotPhase, EvidenceDomain, str]] = set()
        previous_snapshot: StateSnapshot | None = None
        for expected_sequence, snapshot in enumerate(self.snapshots):
            if snapshot.run_id != self.run_id or snapshot.scenario_id != self.scenario_id:
                raise SnapshotError("snapshot identity does not match snapshot series")
            if snapshot.sequence != expected_sequence:
                raise SnapshotError("snapshot sequence must be contiguous and start at zero")
            if snapshot.snapshot_id in seen_snapshot_ids:
                raise SnapshotError("snapshot_id values must be unique within a series")
            if previous_snapshot is None:
                if snapshot.previous_snapshot_sha256 is not None:
                    raise SnapshotError("first series snapshot must not reference a previous hash")
            else:
                if snapshot.captured_at_tick < previous_snapshot.captured_at_tick:
                    raise SnapshotError("snapshots must use nondecreasing captured_at_tick values")
                if snapshot.previous_snapshot_sha256 != previous_snapshot.snapshot_sha256:
                    raise SnapshotError("snapshot hash chain does not match previous snapshot")

            if snapshot.checkpoint_id is not None:
                capture_key = (
                    snapshot.checkpoint_id,
                    snapshot.phase,
                    snapshot.domain,
                    snapshot.subject_id,
                )
                if capture_key in seen_capture_keys:
                    raise SnapshotError(
                        "checkpoint contains a duplicate phase, domain, and subject capture"
                    )
                seen_capture_keys.add(capture_key)

            seen_snapshot_ids.add(snapshot.snapshot_id)
            previous_snapshot = snapshot

    @property
    def snapshot_count(self) -> int:
        """Return the immutable number of snapshots in the series."""

        return len(self.snapshots)

    @property
    def terminal_snapshot_sha256(self) -> str | None:
        """Return the final chain digest, or null for an empty series."""

        return None if not self.snapshots else self.snapshots[-1].snapshot_sha256

    @property
    def series_sha256(self) -> str:
        """Return the digest of the complete snapshot series."""

        return calculate_snapshot_series_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "series_type": "SNAPSHOT_SERIES",
            "snapshot_count": self.snapshot_count,
            "snapshot_schema_version": SUPPORTED_SNAPSHOT_SCHEMA_VERSION,
            "snapshots": [snapshot.to_validator_mapping() for snapshot in self.snapshots],
            "terminal_snapshot_sha256": self.terminal_snapshot_sha256,
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete portable snapshot-series representation."""

        return {
            **self._content_mapping(),
            "series_sha256": self.series_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> SnapshotSeries:
        """Parse and verify a serialized append-only snapshot series."""

        mapping = _require_mapping(value, field="snapshot series")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "run_id",
                    "scenario_id",
                    "series_sha256",
                    "series_type",
                    "snapshot_count",
                    "snapshot_schema_version",
                    "snapshots",
                    "terminal_snapshot_sha256",
                }
            ),
            field="snapshot series",
        )
        _validate_schema_version(mapping["snapshot_schema_version"])
        if mapping["series_type"] != "SNAPSHOT_SERIES":
            raise SnapshotError("unsupported series_type")
        series = cls(
            run_id=_require_string(mapping["run_id"], field="snapshot series.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"],
                field="snapshot series.scenario_id",
            ),
            snapshots=_parse_snapshots(mapping["snapshots"]),
        )

        declared_count = _require_integer(
            mapping["snapshot_count"],
            field="snapshot series.snapshot_count",
        )
        if series.snapshot_count != declared_count:
            raise SnapshotError("declared snapshot_count does not match snapshot series")
        declared_terminal = _require_optional_string(
            mapping["terminal_snapshot_sha256"],
            field="snapshot series.terminal_snapshot_sha256",
        )
        if series.terminal_snapshot_sha256 != declared_terminal:
            raise SnapshotError("declared terminal_snapshot_sha256 does not match snapshot series")
        declared_series_sha256 = _require_string(
            mapping["series_sha256"],
            field="snapshot series.series_sha256",
        )
        if series.series_sha256 != declared_series_sha256:
            raise SnapshotError("declared series_sha256 does not match snapshot series")
        return series


def create_snapshot_state(
    data: Mapping[str, object],
    *,
    max_state_bytes: int = DEFAULT_MAX_SNAPSHOT_STATE_BYTES,
) -> SnapshotState:
    """Freeze a JSON state object into a detached canonical representation."""

    if not isinstance(data, Mapping):
        raise SnapshotError("snapshot state data must be a JSON object")
    if isinstance(max_state_bytes, bool) or not isinstance(max_state_bytes, int):
        raise SnapshotError("max_state_bytes must be an integer")
    if not 1 <= max_state_bytes <= MAX_SNAPSHOT_STATE_BYTES:
        raise SnapshotError(f"max_state_bytes must be between 1 and {MAX_SNAPSHOT_STATE_BYTES}")
    normalized = _normalize_json_value(data, path="state")
    if not isinstance(normalized, dict):
        raise SnapshotError("snapshot state data must be a JSON object")
    state_json = _canonical_json_bytes(normalized)
    if len(state_json) > max_state_bytes:
        raise SnapshotError(f"snapshot state must not exceed {max_state_bytes} bytes")
    return SnapshotState(
        state_json=state_json,
        state_sha256=hashlib.sha256(state_json).hexdigest(),
    )


def create_snapshot_series(run_id: str, scenario_id: str) -> SnapshotSeries:
    """Create an empty append-only snapshot chain for one validation run."""

    return SnapshotSeries(run_id=run_id, scenario_id=scenario_id)


def append_state_snapshot(
    series: SnapshotSeries,
    *,
    snapshot_id: str,
    captured_at_tick: int,
    phase: SnapshotPhase,
    domain: EvidenceDomain,
    subject_id: str,
    producer_id: str,
    state: SnapshotState,
    checkpoint_id: str | None = None,
) -> SnapshotSeries:
    """Return a new series with one deterministic state snapshot appended."""

    if not isinstance(series, SnapshotSeries):
        raise SnapshotError("series must be a SnapshotSeries")
    snapshot = StateSnapshot(
        snapshot_id=snapshot_id,
        run_id=series.run_id,
        scenario_id=series.scenario_id,
        sequence=len(series.snapshots),
        captured_at_tick=captured_at_tick,
        phase=phase,
        domain=domain,
        subject_id=subject_id,
        producer_id=producer_id,
        checkpoint_id=checkpoint_id,
        state=state,
        previous_snapshot_sha256=series.terminal_snapshot_sha256,
    )
    return SnapshotSeries(
        run_id=series.run_id,
        scenario_id=series.scenario_id,
        snapshots=(*series.snapshots, snapshot),
    )


def create_snapshot_source(snapshot: StateSnapshot) -> EvidenceSource:
    """Create an evidence-schema provenance reference to a state snapshot."""

    if not isinstance(snapshot, StateSnapshot):
        raise SnapshotError("snapshot must be a StateSnapshot")
    return EvidenceSource(
        source_kind=EvidenceSourceKind.SNAPSHOT,
        source_id=snapshot.snapshot_id,
        source_sha256=snapshot.snapshot_sha256,
    )


def create_snapshot_evidence_payload(snapshot: StateSnapshot) -> EvidencePayload:
    """Create compact evidence metadata without duplicating snapshot state."""

    if not isinstance(snapshot, StateSnapshot):
        raise SnapshotError("snapshot must be a StateSnapshot")
    return create_evidence_payload(snapshot.to_evidence_mapping())


def calculate_state_snapshot_sha256(snapshot: StateSnapshot) -> str:
    """Calculate the canonical provenance-bound digest of one state snapshot."""

    if not isinstance(snapshot, StateSnapshot):
        raise SnapshotError("snapshot must be a StateSnapshot")
    return hashlib.sha256(_canonical_json_bytes(snapshot._content_mapping())).hexdigest()


def calculate_snapshot_series_sha256(series: SnapshotSeries) -> str:
    """Calculate the canonical digest of a complete snapshot series."""

    if not isinstance(series, SnapshotSeries):
        raise SnapshotError("series must be a SnapshotSeries")
    return hashlib.sha256(_canonical_json_bytes(series._content_mapping())).hexdigest()


def _parse_snapshots(value: object) -> tuple[StateSnapshot, ...]:
    if not isinstance(value, list):
        raise SnapshotError("snapshots must be a JSON array")
    return tuple(
        StateSnapshot.from_mapping(_require_mapping(item, field=f"snapshots[{index}]"))
        for index, item in enumerate(value)
    )


def _validate_schema_version(value: object) -> None:
    version = _require_string(value, field="snapshot_schema_version")
    if version != SUPPORTED_SNAPSHOT_SCHEMA_VERSION:
        raise SnapshotError(f"unsupported snapshot_schema_version: {version}")


def _decode_json_object(state_json: bytes) -> dict[str, object]:
    try:
        decoded = json.loads(
            state_json,
            parse_constant=_reject_non_finite_json,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise SnapshotError(f"state_json is not valid JSON: {exc}") from exc
    if not isinstance(decoded, dict):
        raise SnapshotError("state_json must encode a JSON object")
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
        raise SnapshotError(f"value is not JSON-serializable: {exc}") from exc


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
    raise SnapshotError(f"{path} contains unsupported JSON value type")


def _validate_json_value(value: object, *, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise SnapshotError(f"{path} contains a non-finite number")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_value(item, path=f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise SnapshotError(f"{path} contains a non-string object key")
            _validate_json_value(item, path=f"{path}.{key}")
        return
    raise SnapshotError(f"{path} contains unsupported JSON value type")


def _require_mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise SnapshotError(f"{field} must be a JSON object")
    if not all(isinstance(key, str) for key in value):
        raise SnapshotError(f"{field} must use string keys")
    return cast(Mapping[str, object], value)


def _require_exact_keys(
    mapping: Mapping[str, object],
    *,
    required: frozenset[str],
    field: str,
) -> None:
    keys = frozenset(mapping)
    missing = sorted(required - keys)
    unknown = sorted(keys - required)
    if missing:
        raise SnapshotError(f"{field} missing required field(s): {', '.join(missing)}")
    if unknown:
        raise SnapshotError(f"{field} contains unknown field(s): {', '.join(unknown)}")


def _require_string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        raise SnapshotError(f"{field} must be a string")
    return value


def _require_optional_string(value: object, *, field: str) -> str | None:
    if value is None:
        return None
    return _require_string(value, field=field)


def _require_integer(value: object, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise SnapshotError(f"{field} must be an integer")
    return value


def _parse_enum[T: StrEnum](
    enum_type: type[T],
    value: object,
    *,
    field: str,
) -> T:
    text = _require_string(value, field=field)
    try:
        return enum_type(text)
    except ValueError as exc:
        raise SnapshotError(f"unsupported {field}: {text}") from exc


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise SnapshotError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise SnapshotError(f"{field} must contain 3-128 uppercase identifier characters")


def _validate_scenario_id(value: str) -> None:
    if not isinstance(value, str):
        raise SnapshotError("scenario_id must be a string")
    if _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        raise SnapshotError("scenario_id must match AURORA-SCN-<GATE>-<NNN>")


def _validate_entity_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise SnapshotError(f"{field} must be a string")
    if _ENTITY_ID_PATTERN.fullmatch(value) is None:
        raise SnapshotError(f"{field} contains unsupported identifier characters")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise SnapshotError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise SnapshotError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _validate_sequence(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise SnapshotError(f"{field} must be an integer")
    if value < 0:
        raise SnapshotError(f"{field} must be non-negative")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise SnapshotError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise SnapshotError(f"{field} must be between 0 and {MAX_TICK}")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
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
]
