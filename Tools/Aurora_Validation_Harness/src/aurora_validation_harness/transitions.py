"""Deterministic structural state transitions for Aurora validation runs.

The module compares two validator-owned snapshots, records exact JSON changes,
binds the result to both snapshot digests, and preserves explicit causal
references.  It describes what changed; it deliberately does not decide
whether a change was valid.  Assertion modules must remain able to inspect and
reject transitions that are uncaused, contaminated, or otherwise semantically
invalid.
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
from aurora_validation_harness.snapshots import SnapshotState, StateSnapshot

SUPPORTED_TRANSITION_SCHEMA_VERSION: Final[str] = "1.0"
DEFAULT_MAX_TRANSITION_VALUE_BYTES: Final[int] = 4_194_304
MAX_TRANSITION_VALUE_BYTES: Final[int] = 16_777_216
DEFAULT_MAX_TRANSITION_CHANGES: Final[int] = 50_000
MAX_TRANSITION_CHANGES: Final[int] = 1_000_000
MAX_TRANSITION_CAUSES: Final[int] = 1_024
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_ENTITY_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
_JSON_POINTER_PATTERN: Final[re.Pattern[str]] = re.compile(r"^(?:/(?:[^~]|~[01])*)+$")


class TransitionError(ValueError):
    """Raised when transition data, snapshot linkage, or chain integrity is invalid."""


class ChangeOperation(StrEnum):
    """Structural operation represented by one state change."""

    ADDED = "ADDED"
    REMOVED = "REMOVED"
    REPLACED = "REPLACED"


class TransitionStatus(StrEnum):
    """Whether a snapshot pair contains any structural state change."""

    UNCHANGED = "UNCHANGED"
    CHANGED = "CHANGED"


@dataclass(frozen=True, slots=True)
class TransitionValue:
    """Canonical JSON value captured on one side of a structural change."""

    value_json: bytes
    value_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.value_json, bytes):
            raise TransitionError("value_json must be bytes")
        _validate_sha256(self.value_sha256, field="value_sha256")
        if hashlib.sha256(self.value_json).hexdigest() != self.value_sha256:
            raise TransitionError("value_sha256 does not match value_json")
        if len(self.value_json) > MAX_TRANSITION_VALUE_BYTES:
            raise TransitionError(f"value_json must not exceed {MAX_TRANSITION_VALUE_BYTES} bytes")

        decoded = _decode_json_value(self.value_json)
        _validate_json_value(decoded, path="value")
        if self.value_json != _canonical_json_bytes(decoded):
            raise TransitionError("value_json must use canonical JSON encoding")

    @property
    def size_bytes(self) -> int:
        """Return the exact canonical value size."""

        return len(self.value_json)

    def decode(self) -> object:
        """Return a fresh decoded JSON value."""

        return _decode_json_value(self.value_json)

    def to_mapping(self) -> dict[str, object]:
        """Return the portable value representation."""

        return {
            "data": self.decode(),
            "value_sha256": self.value_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> TransitionValue:
        """Parse and verify one portable transition value."""

        mapping = _require_mapping(value, field="transition value")
        _require_exact_keys(
            mapping,
            required=frozenset({"data", "value_sha256"}),
            field="transition value",
        )
        declared_sha256 = _require_string(
            mapping["value_sha256"],
            field="transition value.value_sha256",
        )
        transition_value = create_transition_value(
            mapping["data"],
            max_value_bytes=MAX_TRANSITION_VALUE_BYTES,
        )
        if transition_value.value_sha256 != declared_sha256:
            raise TransitionError("declared value_sha256 does not match transition value")
        return transition_value


@dataclass(frozen=True, slots=True)
class StateChange:
    """One deterministic JSON Pointer change between two snapshot states."""

    path: str
    operation: ChangeOperation
    before: TransitionValue | None
    after: TransitionValue | None

    def __post_init__(self) -> None:
        _validate_json_pointer(self.path)
        if not isinstance(self.operation, ChangeOperation):
            raise TransitionError("operation must be a ChangeOperation value")
        if self.before is not None and not isinstance(self.before, TransitionValue):
            raise TransitionError("before must be null or a TransitionValue")
        if self.after is not None and not isinstance(self.after, TransitionValue):
            raise TransitionError("after must be null or a TransitionValue")

        if self.operation is ChangeOperation.ADDED:
            if self.before is not None or self.after is None:
                raise TransitionError("ADDED change requires only an after value")
        elif self.operation is ChangeOperation.REMOVED:
            if self.before is None or self.after is not None:
                raise TransitionError("REMOVED change requires only a before value")
        else:
            if self.before is None or self.after is None:
                raise TransitionError("REPLACED change requires before and after values")
            if self.before.value_sha256 == self.after.value_sha256:
                raise TransitionError("REPLACED change values must differ")

    @property
    def change_sha256(self) -> str:
        """Return the digest of this path, operation, and captured values."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "after": None if self.after is None else self.after.to_mapping(),
            "before": None if self.before is None else self.before.to_mapping(),
            "operation": self.operation.value,
            "path": self.path,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable change representation."""

        return {
            **self._content_mapping(),
            "change_sha256": self.change_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> StateChange:
        """Parse and verify one serialized state change."""

        mapping = _require_mapping(value, field="state change")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "after",
                    "before",
                    "change_sha256",
                    "operation",
                    "path",
                }
            ),
            field="state change",
        )
        change = cls(
            path=_require_string(mapping["path"], field="state change.path"),
            operation=_parse_enum(
                ChangeOperation,
                mapping["operation"],
                field="state change.operation",
            ),
            before=_parse_optional_transition_value(
                mapping["before"],
                field="state change.before",
            ),
            after=_parse_optional_transition_value(
                mapping["after"],
                field="state change.after",
            ),
        )
        declared_sha256 = _require_string(
            mapping["change_sha256"],
            field="state change.change_sha256",
        )
        if change.change_sha256 != declared_sha256:
            raise TransitionError("declared change_sha256 does not match state change")
        return change


@dataclass(frozen=True, slots=True)
class StateTransition:
    """A provenance-bound structural transition between two state snapshots."""

    transition_id: str
    run_id: str
    scenario_id: str
    sequence: int
    domain: EvidenceDomain
    subject_id: str
    before_snapshot_id: str
    before_snapshot_sha256: str
    before_state_sha256: str
    before_tick: int
    after_snapshot_id: str
    after_snapshot_sha256: str
    after_state_sha256: str
    after_tick: int
    causes: tuple[EvidenceSource, ...]
    changes: tuple[StateChange, ...]
    previous_transition_sha256: str | None

    def __post_init__(self) -> None:
        _validate_control_id(self.transition_id, field="transition_id")
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        _validate_sequence(self.sequence, field="sequence")
        if not isinstance(self.domain, EvidenceDomain):
            raise TransitionError("domain must be an EvidenceDomain value")
        _validate_entity_id(self.subject_id, field="subject_id")
        _validate_control_id(self.before_snapshot_id, field="before_snapshot_id")
        _validate_sha256(self.before_snapshot_sha256, field="before_snapshot_sha256")
        _validate_sha256(self.before_state_sha256, field="before_state_sha256")
        _validate_tick(self.before_tick, field="before_tick")
        _validate_control_id(self.after_snapshot_id, field="after_snapshot_id")
        _validate_sha256(self.after_snapshot_sha256, field="after_snapshot_sha256")
        _validate_sha256(self.after_state_sha256, field="after_state_sha256")
        _validate_tick(self.after_tick, field="after_tick")
        if self.after_tick < self.before_tick:
            raise TransitionError("after_tick must not precede before_tick")
        if self.before_snapshot_id == self.after_snapshot_id:
            raise TransitionError("before and after snapshot IDs must differ")

        if not isinstance(self.causes, tuple) or not all(
            isinstance(source, EvidenceSource) for source in self.causes
        ):
            raise TransitionError("causes must be a tuple of EvidenceSource values")
        if len(self.causes) > MAX_TRANSITION_CAUSES:
            raise TransitionError(f"causes must not exceed {MAX_TRANSITION_CAUSES} entries")
        cause_keys = tuple((source.source_kind, source.source_id) for source in self.causes)
        if len(cause_keys) != len(set(cause_keys)):
            raise TransitionError("causes must not contain duplicate kind and ID pairs")

        if not isinstance(self.changes, tuple) or not all(
            isinstance(change, StateChange) for change in self.changes
        ):
            raise TransitionError("changes must be a tuple of StateChange values")
        if len(self.changes) > MAX_TRANSITION_CHANGES:
            raise TransitionError(f"changes must not exceed {MAX_TRANSITION_CHANGES} entries")
        paths = tuple(change.path for change in self.changes)
        if len(paths) != len(set(paths)):
            raise TransitionError("changes must contain unique JSON Pointer paths")
        if paths != tuple(sorted(paths)):
            raise TransitionError("changes must be ordered by JSON Pointer path")

        if self.changes and self.before_state_sha256 == self.after_state_sha256:
            raise TransitionError("changed transition requires distinct state digests")
        if not self.changes and self.before_state_sha256 != self.after_state_sha256:
            raise TransitionError("unchanged transition requires identical state digests")

        if self.previous_transition_sha256 is not None:
            _validate_sha256(
                self.previous_transition_sha256,
                field="previous_transition_sha256",
            )
        if self.sequence == 0 and self.previous_transition_sha256 is not None:
            raise TransitionError("first state transition must not declare a previous hash")
        if self.sequence > 0 and self.previous_transition_sha256 is None:
            raise TransitionError("non-first state transition requires a previous hash")

    @property
    def status(self) -> TransitionStatus:
        """Return whether the transition changed state structurally."""

        return TransitionStatus.CHANGED if self.changes else TransitionStatus.UNCHANGED

    @property
    def change_count(self) -> int:
        """Return the number of structural changes."""

        return len(self.changes)

    @property
    def change_set_sha256(self) -> str:
        """Return the digest of the ordered change set."""

        return hashlib.sha256(
            _canonical_json_bytes([change.to_mapping() for change in self.changes])
        ).hexdigest()

    @property
    def transition_sha256(self) -> str:
        """Return the digest binding snapshots, changes, causes, and chain position."""

        return calculate_state_transition_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "after_snapshot_id": self.after_snapshot_id,
            "after_snapshot_sha256": self.after_snapshot_sha256,
            "after_state_sha256": self.after_state_sha256,
            "after_tick": self.after_tick,
            "before_snapshot_id": self.before_snapshot_id,
            "before_snapshot_sha256": self.before_snapshot_sha256,
            "before_state_sha256": self.before_state_sha256,
            "before_tick": self.before_tick,
            "causes": [source.to_mapping() for source in self.causes],
            "change_count": self.change_count,
            "change_set_sha256": self.change_set_sha256,
            "changes": [change.to_mapping() for change in self.changes],
            "domain": self.domain.value,
            "previous_transition_sha256": self.previous_transition_sha256,
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "sequence": self.sequence,
            "status": self.status.value,
            "subject_id": self.subject_id,
            "transition_id": self.transition_id,
            "transition_schema_version": SUPPORTED_TRANSITION_SCHEMA_VERSION,
            "transition_type": "STATE_TRANSITION",
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete validator-owned transition representation."""

        return {
            **self._content_mapping(),
            "transition_sha256": self.transition_sha256,
        }

    def to_evidence_mapping(self) -> dict[str, object]:
        """Return a compact transition summary without embedding changed values."""

        return {
            "after_snapshot_id": self.after_snapshot_id,
            "after_snapshot_sha256": self.after_snapshot_sha256,
            "after_state_sha256": self.after_state_sha256,
            "after_tick": self.after_tick,
            "before_snapshot_id": self.before_snapshot_id,
            "before_snapshot_sha256": self.before_snapshot_sha256,
            "before_state_sha256": self.before_state_sha256,
            "before_tick": self.before_tick,
            "causes": [source.to_mapping() for source in self.causes],
            "change_count": self.change_count,
            "change_set_sha256": self.change_set_sha256,
            "domain": self.domain.value,
            "status": self.status.value,
            "subject_id": self.subject_id,
            "transition_id": self.transition_id,
            "transition_sha256": self.transition_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> StateTransition:
        """Parse and verify a serialized state transition."""

        mapping = _require_mapping(value, field="state transition")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "after_snapshot_id",
                    "after_snapshot_sha256",
                    "after_state_sha256",
                    "after_tick",
                    "before_snapshot_id",
                    "before_snapshot_sha256",
                    "before_state_sha256",
                    "before_tick",
                    "causes",
                    "change_count",
                    "change_set_sha256",
                    "changes",
                    "domain",
                    "previous_transition_sha256",
                    "run_id",
                    "scenario_id",
                    "sequence",
                    "status",
                    "subject_id",
                    "transition_id",
                    "transition_schema_version",
                    "transition_sha256",
                    "transition_type",
                }
            ),
            field="state transition",
        )
        _validate_schema_version(mapping["transition_schema_version"])
        if mapping["transition_type"] != "STATE_TRANSITION":
            raise TransitionError("unsupported transition_type")
        transition = cls(
            transition_id=_require_string(
                mapping["transition_id"],
                field="state transition.transition_id",
            ),
            run_id=_require_string(mapping["run_id"], field="state transition.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"],
                field="state transition.scenario_id",
            ),
            sequence=_require_integer(
                mapping["sequence"],
                field="state transition.sequence",
            ),
            domain=_parse_enum(
                EvidenceDomain,
                mapping["domain"],
                field="state transition.domain",
            ),
            subject_id=_require_string(
                mapping["subject_id"],
                field="state transition.subject_id",
            ),
            before_snapshot_id=_require_string(
                mapping["before_snapshot_id"],
                field="state transition.before_snapshot_id",
            ),
            before_snapshot_sha256=_require_string(
                mapping["before_snapshot_sha256"],
                field="state transition.before_snapshot_sha256",
            ),
            before_state_sha256=_require_string(
                mapping["before_state_sha256"],
                field="state transition.before_state_sha256",
            ),
            before_tick=_require_integer(
                mapping["before_tick"],
                field="state transition.before_tick",
            ),
            after_snapshot_id=_require_string(
                mapping["after_snapshot_id"],
                field="state transition.after_snapshot_id",
            ),
            after_snapshot_sha256=_require_string(
                mapping["after_snapshot_sha256"],
                field="state transition.after_snapshot_sha256",
            ),
            after_state_sha256=_require_string(
                mapping["after_state_sha256"],
                field="state transition.after_state_sha256",
            ),
            after_tick=_require_integer(
                mapping["after_tick"],
                field="state transition.after_tick",
            ),
            causes=_parse_sources(mapping["causes"], field="state transition.causes"),
            changes=_parse_changes(mapping["changes"]),
            previous_transition_sha256=_require_optional_string(
                mapping["previous_transition_sha256"],
                field="state transition.previous_transition_sha256",
            ),
        )
        _validate_transition_derived_fields(transition, mapping)
        return transition


@dataclass(frozen=True, slots=True)
class TransitionSeries:
    """Immutable append-only transition chain for one validation run."""

    run_id: str
    scenario_id: str
    transitions: tuple[StateTransition, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        if not isinstance(self.transitions, tuple) or not all(
            isinstance(transition, StateTransition) for transition in self.transitions
        ):
            raise TransitionError("transitions must be a tuple of StateTransition values")

        seen_transition_ids: set[str] = set()
        seen_edges: set[tuple[str, str, EvidenceDomain, str]] = set()
        previous_transition: StateTransition | None = None
        for expected_sequence, transition in enumerate(self.transitions):
            if transition.run_id != self.run_id or transition.scenario_id != self.scenario_id:
                raise TransitionError("transition identity does not match transition series")
            if transition.sequence != expected_sequence:
                raise TransitionError("transition sequence must be contiguous and start at zero")
            if transition.transition_id in seen_transition_ids:
                raise TransitionError("transition_id values must be unique within a series")
            if previous_transition is None:
                if transition.previous_transition_sha256 is not None:
                    raise TransitionError(
                        "first series transition must not reference a previous hash"
                    )
            else:
                if transition.after_tick < previous_transition.after_tick:
                    raise TransitionError("transitions must use nondecreasing after_tick values")
                if transition.previous_transition_sha256 != previous_transition.transition_sha256:
                    raise TransitionError(
                        "transition hash chain does not match previous transition"
                    )

            edge = (
                transition.before_snapshot_sha256,
                transition.after_snapshot_sha256,
                transition.domain,
                transition.subject_id,
            )
            if edge in seen_edges:
                raise TransitionError("transition series contains a duplicate snapshot edge")
            seen_edges.add(edge)
            seen_transition_ids.add(transition.transition_id)
            previous_transition = transition

    @property
    def transition_count(self) -> int:
        """Return the immutable number of transitions in the series."""

        return len(self.transitions)

    @property
    def terminal_transition_sha256(self) -> str | None:
        """Return the final chain digest, or null for an empty series."""

        return None if not self.transitions else self.transitions[-1].transition_sha256

    @property
    def series_sha256(self) -> str:
        """Return the digest of the complete transition series."""

        return calculate_transition_series_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "series_type": "TRANSITION_SERIES",
            "terminal_transition_sha256": self.terminal_transition_sha256,
            "transition_count": self.transition_count,
            "transition_schema_version": SUPPORTED_TRANSITION_SCHEMA_VERSION,
            "transitions": [transition.to_validator_mapping() for transition in self.transitions],
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete portable transition-series representation."""

        return {
            **self._content_mapping(),
            "series_sha256": self.series_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> TransitionSeries:
        """Parse and verify a serialized append-only transition series."""

        mapping = _require_mapping(value, field="transition series")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "run_id",
                    "scenario_id",
                    "series_sha256",
                    "series_type",
                    "terminal_transition_sha256",
                    "transition_count",
                    "transition_schema_version",
                    "transitions",
                }
            ),
            field="transition series",
        )
        _validate_schema_version(mapping["transition_schema_version"])
        if mapping["series_type"] != "TRANSITION_SERIES":
            raise TransitionError("unsupported series_type")
        series = cls(
            run_id=_require_string(mapping["run_id"], field="transition series.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"],
                field="transition series.scenario_id",
            ),
            transitions=_parse_transitions(mapping["transitions"]),
        )

        declared_count = _require_integer(
            mapping["transition_count"],
            field="transition series.transition_count",
        )
        if series.transition_count != declared_count:
            raise TransitionError("declared transition_count does not match transition series")
        declared_terminal = _require_optional_string(
            mapping["terminal_transition_sha256"],
            field="transition series.terminal_transition_sha256",
        )
        if series.terminal_transition_sha256 != declared_terminal:
            raise TransitionError(
                "declared terminal_transition_sha256 does not match transition series"
            )
        declared_series_sha256 = _require_string(
            mapping["series_sha256"],
            field="transition series.series_sha256",
        )
        if series.series_sha256 != declared_series_sha256:
            raise TransitionError("declared series_sha256 does not match transition series")
        return series


def create_transition_value(
    value: object,
    *,
    max_value_bytes: int = DEFAULT_MAX_TRANSITION_VALUE_BYTES,
) -> TransitionValue:
    """Freeze any supported JSON value for a structural change record."""

    if isinstance(max_value_bytes, bool) or not isinstance(max_value_bytes, int):
        raise TransitionError("max_value_bytes must be an integer")
    if not 1 <= max_value_bytes <= MAX_TRANSITION_VALUE_BYTES:
        raise TransitionError(f"max_value_bytes must be between 1 and {MAX_TRANSITION_VALUE_BYTES}")
    normalized = _normalize_json_value(value, path="value")
    value_json = _canonical_json_bytes(normalized)
    if len(value_json) > max_value_bytes:
        raise TransitionError(f"transition value must not exceed {max_value_bytes} bytes")
    return TransitionValue(
        value_json=value_json,
        value_sha256=hashlib.sha256(value_json).hexdigest(),
    )


def derive_state_changes(
    before: SnapshotState,
    after: SnapshotState,
    *,
    max_changes: int = DEFAULT_MAX_TRANSITION_CHANGES,
) -> tuple[StateChange, ...]:
    """Return an exact deterministic structural diff between two snapshot states."""

    if not isinstance(before, SnapshotState) or not isinstance(after, SnapshotState):
        raise TransitionError("before and after must be SnapshotState values")
    _validate_max_changes(max_changes)
    if before.state_sha256 == after.state_sha256:
        return ()

    changes: list[StateChange] = []
    _collect_changes(
        before.decode(),
        after.decode(),
        path="",
        changes=changes,
        max_changes=max_changes,
    )
    changes.sort(key=lambda change: change.path)
    return tuple(changes)


def create_state_transition(
    before: StateSnapshot,
    after: StateSnapshot,
    *,
    transition_id: str,
    sequence: int = 0,
    causes: tuple[EvidenceSource, ...] = (),
    previous_transition_sha256: str | None = None,
    max_changes: int = DEFAULT_MAX_TRANSITION_CHANGES,
) -> StateTransition:
    """Derive and bind one state transition from a compatible snapshot pair."""

    _validate_snapshot_pair(before, after)
    changes = derive_state_changes(before.state, after.state, max_changes=max_changes)
    return StateTransition(
        transition_id=transition_id,
        run_id=before.run_id,
        scenario_id=before.scenario_id,
        sequence=sequence,
        domain=before.domain,
        subject_id=before.subject_id,
        before_snapshot_id=before.snapshot_id,
        before_snapshot_sha256=before.snapshot_sha256,
        before_state_sha256=before.state.state_sha256,
        before_tick=before.captured_at_tick,
        after_snapshot_id=after.snapshot_id,
        after_snapshot_sha256=after.snapshot_sha256,
        after_state_sha256=after.state.state_sha256,
        after_tick=after.captured_at_tick,
        causes=causes,
        changes=changes,
        previous_transition_sha256=previous_transition_sha256,
    )


def create_transition_series(run_id: str, scenario_id: str) -> TransitionSeries:
    """Create an empty append-only transition chain for one validation run."""

    return TransitionSeries(run_id=run_id, scenario_id=scenario_id)


def append_state_transition(
    series: TransitionSeries,
    *,
    transition_id: str,
    before: StateSnapshot,
    after: StateSnapshot,
    causes: tuple[EvidenceSource, ...] = (),
    max_changes: int = DEFAULT_MAX_TRANSITION_CHANGES,
) -> TransitionSeries:
    """Return a new series with one derived state transition appended."""

    if not isinstance(series, TransitionSeries):
        raise TransitionError("series must be a TransitionSeries")
    if before.run_id != series.run_id or before.scenario_id != series.scenario_id:
        raise TransitionError("snapshot identity does not match transition series")
    transition = create_state_transition(
        before,
        after,
        transition_id=transition_id,
        sequence=len(series.transitions),
        causes=causes,
        previous_transition_sha256=series.terminal_transition_sha256,
        max_changes=max_changes,
    )
    return TransitionSeries(
        run_id=series.run_id,
        scenario_id=series.scenario_id,
        transitions=(*series.transitions, transition),
    )


def validate_state_transition(
    transition: StateTransition,
    before: StateSnapshot,
    after: StateSnapshot,
    *,
    max_changes: int = MAX_TRANSITION_CHANGES,
) -> None:
    """Verify a transition against the exact snapshots it claims to connect."""

    if not isinstance(transition, StateTransition):
        raise TransitionError("transition must be a StateTransition")
    _validate_snapshot_pair(before, after)
    expected = create_state_transition(
        before,
        after,
        transition_id=transition.transition_id,
        sequence=transition.sequence,
        causes=transition.causes,
        previous_transition_sha256=transition.previous_transition_sha256,
        max_changes=max_changes,
    )
    if transition != expected:
        raise TransitionError("transition does not match its referenced snapshots")


def create_transition_source(transition: StateTransition) -> EvidenceSource:
    """Create an evidence-schema provenance reference to a state transition."""

    if not isinstance(transition, StateTransition):
        raise TransitionError("transition must be a StateTransition")
    return EvidenceSource(
        source_kind=EvidenceSourceKind.TRANSITION,
        source_id=transition.transition_id,
        source_sha256=transition.transition_sha256,
    )


def create_transition_evidence_payload(transition: StateTransition) -> EvidencePayload:
    """Create compact evidence metadata without duplicating changed values."""

    if not isinstance(transition, StateTransition):
        raise TransitionError("transition must be a StateTransition")
    return create_evidence_payload(transition.to_evidence_mapping())


def calculate_state_transition_sha256(transition: StateTransition) -> str:
    """Calculate the canonical provenance-bound digest of one transition."""

    if not isinstance(transition, StateTransition):
        raise TransitionError("transition must be a StateTransition")
    return hashlib.sha256(_canonical_json_bytes(transition._content_mapping())).hexdigest()


def calculate_transition_series_sha256(series: TransitionSeries) -> str:
    """Calculate the canonical digest of a complete transition series."""

    if not isinstance(series, TransitionSeries):
        raise TransitionError("series must be a TransitionSeries")
    return hashlib.sha256(_canonical_json_bytes(series._content_mapping())).hexdigest()


def _validate_snapshot_pair(before: StateSnapshot, after: StateSnapshot) -> None:
    if not isinstance(before, StateSnapshot) or not isinstance(after, StateSnapshot):
        raise TransitionError("before and after must be StateSnapshot values")
    if before.run_id != after.run_id or before.scenario_id != after.scenario_id:
        raise TransitionError("snapshots must belong to the same run and scenario")
    if before.domain is not after.domain:
        raise TransitionError("snapshots must belong to the same evidence domain")
    if before.subject_id != after.subject_id:
        raise TransitionError("snapshots must describe the same subject")
    if after.sequence <= before.sequence:
        raise TransitionError("after snapshot sequence must follow before snapshot sequence")
    if after.captured_at_tick < before.captured_at_tick:
        raise TransitionError("after snapshot tick must not precede before snapshot tick")
    if before.snapshot_id == after.snapshot_id:
        raise TransitionError("before and after snapshot IDs must differ")


def _collect_changes(
    before: object,
    after: object,
    *,
    path: str,
    changes: list[StateChange],
    max_changes: int,
) -> None:
    if isinstance(before, Mapping) and isinstance(after, Mapping):
        keys = sorted(set(before) | set(after))
        for key in keys:
            child_path = _join_json_pointer(path, key)
            if key not in before:
                _append_change(
                    changes,
                    StateChange(
                        path=child_path,
                        operation=ChangeOperation.ADDED,
                        before=None,
                        after=create_transition_value(
                            after[key],
                            max_value_bytes=MAX_TRANSITION_VALUE_BYTES,
                        ),
                    ),
                    max_changes=max_changes,
                )
            elif key not in after:
                _append_change(
                    changes,
                    StateChange(
                        path=child_path,
                        operation=ChangeOperation.REMOVED,
                        before=create_transition_value(
                            before[key],
                            max_value_bytes=MAX_TRANSITION_VALUE_BYTES,
                        ),
                        after=None,
                    ),
                    max_changes=max_changes,
                )
            else:
                _collect_changes(
                    before[key],
                    after[key],
                    path=child_path,
                    changes=changes,
                    max_changes=max_changes,
                )
        return

    if isinstance(before, list) and isinstance(after, list):
        common_length = min(len(before), len(after))
        for index in range(common_length):
            _collect_changes(
                before[index],
                after[index],
                path=_join_json_pointer(path, str(index)),
                changes=changes,
                max_changes=max_changes,
            )
        for index in range(common_length, len(before)):
            _append_change(
                changes,
                StateChange(
                    path=_join_json_pointer(path, str(index)),
                    operation=ChangeOperation.REMOVED,
                    before=create_transition_value(
                        before[index],
                        max_value_bytes=MAX_TRANSITION_VALUE_BYTES,
                    ),
                    after=None,
                ),
                max_changes=max_changes,
            )
        for index in range(common_length, len(after)):
            _append_change(
                changes,
                StateChange(
                    path=_join_json_pointer(path, str(index)),
                    operation=ChangeOperation.ADDED,
                    before=None,
                    after=create_transition_value(
                        after[index],
                        max_value_bytes=MAX_TRANSITION_VALUE_BYTES,
                    ),
                ),
                max_changes=max_changes,
            )
        return

    if type(before) is type(after) and before == after:
        return
    _append_change(
        changes,
        StateChange(
            path=path,
            operation=ChangeOperation.REPLACED,
            before=create_transition_value(
                before,
                max_value_bytes=MAX_TRANSITION_VALUE_BYTES,
            ),
            after=create_transition_value(
                after,
                max_value_bytes=MAX_TRANSITION_VALUE_BYTES,
            ),
        ),
        max_changes=max_changes,
    )


def _append_change(
    changes: list[StateChange],
    change: StateChange,
    *,
    max_changes: int,
) -> None:
    if len(changes) >= max_changes:
        raise TransitionError(f"state diff exceeds max_changes limit of {max_changes}")
    changes.append(change)


def _join_json_pointer(path: str, token: str) -> str:
    escaped = token.replace("~", "~0").replace("/", "~1")
    return f"{path}/{escaped}"


def _parse_optional_transition_value(
    value: object,
    *,
    field: str,
) -> TransitionValue | None:
    if value is None:
        return None
    return TransitionValue.from_mapping(_require_mapping(value, field=field))


def _parse_changes(value: object) -> tuple[StateChange, ...]:
    if not isinstance(value, list):
        raise TransitionError("state transition.changes must be a JSON array")
    return tuple(
        StateChange.from_mapping(_require_mapping(item, field=f"state transition.changes[{index}]"))
        for index, item in enumerate(value)
    )


def _parse_sources(value: object, *, field: str) -> tuple[EvidenceSource, ...]:
    if not isinstance(value, list):
        raise TransitionError(f"{field} must be a JSON array")
    return tuple(
        EvidenceSource.from_mapping(_require_mapping(item, field=f"{field}[{index}]"))
        for index, item in enumerate(value)
    )


def _parse_transitions(value: object) -> tuple[StateTransition, ...]:
    if not isinstance(value, list):
        raise TransitionError("transitions must be a JSON array")
    return tuple(
        StateTransition.from_mapping(_require_mapping(item, field=f"transitions[{index}]"))
        for index, item in enumerate(value)
    )


def _validate_transition_derived_fields(
    transition: StateTransition,
    mapping: Mapping[str, object],
) -> None:
    declared_status = _parse_enum(
        TransitionStatus,
        mapping["status"],
        field="state transition.status",
    )
    if transition.status is not declared_status:
        raise TransitionError("declared status does not match state transition")
    declared_count = _require_integer(
        mapping["change_count"],
        field="state transition.change_count",
    )
    if transition.change_count != declared_count:
        raise TransitionError("declared change_count does not match state transition")
    declared_change_set_sha256 = _require_string(
        mapping["change_set_sha256"],
        field="state transition.change_set_sha256",
    )
    if transition.change_set_sha256 != declared_change_set_sha256:
        raise TransitionError("declared change_set_sha256 does not match state transition")
    declared_transition_sha256 = _require_string(
        mapping["transition_sha256"],
        field="state transition.transition_sha256",
    )
    if transition.transition_sha256 != declared_transition_sha256:
        raise TransitionError("declared transition_sha256 does not match state transition")


def _validate_schema_version(value: object) -> None:
    version = _require_string(value, field="transition_schema_version")
    if version != SUPPORTED_TRANSITION_SCHEMA_VERSION:
        raise TransitionError(f"unsupported transition_schema_version: {version}")


def _validate_max_changes(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TransitionError("max_changes must be an integer")
    if not 1 <= value <= MAX_TRANSITION_CHANGES:
        raise TransitionError(f"max_changes must be between 1 and {MAX_TRANSITION_CHANGES}")


def _decode_json_value(value_json: bytes) -> object:
    try:
        return json.loads(
            value_json,
            parse_constant=_reject_non_finite_json,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise TransitionError(f"value_json is not valid JSON: {exc}") from exc


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
        raise TransitionError(f"value is not JSON-serializable: {exc}") from exc


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
    raise TransitionError(f"{path} contains unsupported JSON value type")


def _validate_json_value(value: object, *, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise TransitionError(f"{path} contains a non-finite number")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_value(item, path=f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise TransitionError(f"{path} contains a non-string object key")
            _validate_json_value(item, path=f"{path}.{key}")
        return
    raise TransitionError(f"{path} contains unsupported JSON value type")


def _require_mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise TransitionError(f"{field} must be a JSON object")
    if not all(isinstance(key, str) for key in value):
        raise TransitionError(f"{field} must use string keys")
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
        raise TransitionError(f"{field} missing required field(s): {', '.join(missing)}")
    if unknown:
        raise TransitionError(f"{field} contains unknown field(s): {', '.join(unknown)}")


def _require_string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        raise TransitionError(f"{field} must be a string")
    return value


def _require_optional_string(value: object, *, field: str) -> str | None:
    if value is None:
        return None
    return _require_string(value, field=field)


def _require_integer(value: object, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TransitionError(f"{field} must be an integer")
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
        raise TransitionError(f"unsupported {field}: {text}") from exc


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise TransitionError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise TransitionError(f"{field} must contain 3-128 uppercase identifier characters")


def _validate_scenario_id(value: str) -> None:
    if not isinstance(value, str):
        raise TransitionError("scenario_id must be a string")
    if _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        raise TransitionError("scenario_id must match AURORA-SCN-<GATE>-<NNN>")


def _validate_entity_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise TransitionError(f"{field} must be a string")
    if _ENTITY_ID_PATTERN.fullmatch(value) is None:
        raise TransitionError(f"{field} contains unsupported identifier characters")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise TransitionError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise TransitionError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _validate_json_pointer(value: str) -> None:
    if not isinstance(value, str):
        raise TransitionError("path must be a string")
    if _JSON_POINTER_PATTERN.fullmatch(value) is None:
        raise TransitionError("path must be a non-empty RFC 6901 JSON Pointer")


def _validate_sequence(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TransitionError(f"{field} must be an integer")
    if value < 0:
        raise TransitionError(f"{field} must be non-negative")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TransitionError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise TransitionError(f"{field} must be between 0 and {MAX_TICK}")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
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
]
