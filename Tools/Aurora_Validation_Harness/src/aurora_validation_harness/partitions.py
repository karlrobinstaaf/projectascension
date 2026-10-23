"""Sealed fixture-partition policy and capability-scoped runtime views.

The complete fixture store is validator-owned. Runtime components receive
detached views containing only their authorized artifacts; an Aurora view has
no reference back to world truth, player-private state, future state,
validator metadata, or expected results.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from types import MappingProxyType
from typing import Final

from aurora_validation_harness.fixtures import (
    FixtureArtifact,
    FixtureBundle,
    FixtureMediaType,
    FixturePartition,
)

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_ARTIFACT_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z_]+-[0-9]{3}$")


class PartitionError(ValueError):
    """Raised when partition policy or a capability-scoped view is invalid."""


class PartitionAccessError(PermissionError):
    """Raised when a runtime principal requests unavailable fixture data."""


class AccessPrincipal(StrEnum):
    """Runtime identities allowed to receive fixture capabilities."""

    WORLD_RUNTIME = "WORLD_RUNTIME"
    AURORA_RUNTIME = "AURORA_RUNTIME"
    PLAYER_RUNTIME = "PLAYER_RUNTIME"
    FUTURE_SCHEDULER = "FUTURE_SCHEDULER"
    VALIDATOR = "VALIDATOR"


_SEALED_ACCESS_POLICY: Final[Mapping[AccessPrincipal, frozenset[FixturePartition]]] = (
    MappingProxyType(
        {
            AccessPrincipal.WORLD_RUNTIME: frozenset({FixturePartition.WORLD}),
            AccessPrincipal.AURORA_RUNTIME: frozenset({FixturePartition.AURORA}),
            AccessPrincipal.PLAYER_RUNTIME: frozenset({FixturePartition.PLAYER_PRIVATE}),
            AccessPrincipal.FUTURE_SCHEDULER: frozenset({FixturePartition.FUTURE}),
            AccessPrincipal.VALIDATOR: frozenset(FixturePartition),
        }
    )
)


class AccessDecisionReason(StrEnum):
    """Stable reason code for a partition-access decision."""

    AUTHORIZED_PARTITION = "AUTHORIZED_PARTITION"
    PARTITION_DENIED = "PARTITION_DENIED"


@dataclass(frozen=True, slots=True)
class PartitionAccessDecision:
    """Auditable result of evaluating one principal-to-partition edge."""

    principal: AccessPrincipal
    partition: FixturePartition
    granted: bool
    reason: AccessDecisionReason

    def __post_init__(self) -> None:
        _validate_principal(self.principal)
        _validate_partition(self.partition)
        if not isinstance(self.granted, bool):
            raise PartitionError("granted must be a boolean")
        if not isinstance(self.reason, AccessDecisionReason):
            raise PartitionError("reason must be an AccessDecisionReason value")

        expected_grant = self.partition in _SEALED_ACCESS_POLICY[self.principal]
        expected_reason = (
            AccessDecisionReason.AUTHORIZED_PARTITION
            if expected_grant
            else AccessDecisionReason.PARTITION_DENIED
        )
        if self.granted is not expected_grant or self.reason is not expected_reason:
            raise PartitionError("access decision does not match the sealed policy")


@dataclass(frozen=True, slots=True)
class ScopedFixtureArtifact:
    """Runtime-safe artifact without source path or global fixture identity."""

    artifact_id: str
    partition: FixturePartition
    media_type: FixtureMediaType
    content_sha256: str
    size_bytes: int
    content_bytes: bytes

    def __post_init__(self) -> None:
        _validate_artifact_id(self.artifact_id)
        _validate_partition(self.partition)
        if not isinstance(self.media_type, FixtureMediaType):
            raise PartitionError("media_type must be a FixtureMediaType value")
        _validate_sha256(self.content_sha256, field="content_sha256")
        if isinstance(self.size_bytes, bool) or not isinstance(self.size_bytes, int):
            raise PartitionError("size_bytes must be an integer")
        if self.size_bytes < 0:
            raise PartitionError("size_bytes must not be negative")
        if not isinstance(self.content_bytes, bytes):
            raise PartitionError("content_bytes must be bytes")
        if len(self.content_bytes) != self.size_bytes:
            raise PartitionError(f"scoped artifact size mismatch: {self.artifact_id}")
        if hashlib.sha256(self.content_bytes).hexdigest() != self.content_sha256:
            raise PartitionError(f"scoped artifact hash mismatch: {self.artifact_id}")

    def decode_text(self) -> str:
        """Decode a scoped text artifact as strict UTF-8."""

        if self.media_type is FixtureMediaType.BINARY:
            raise PartitionError(f"scoped artifact is not text: {self.artifact_id}")
        try:
            return self.content_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise PartitionError(f"scoped artifact is not valid UTF-8: {self.artifact_id}") from exc

    def decode_json_object(self) -> dict[str, object]:
        """Decode a scoped JSON artifact into a fresh top-level object."""

        if self.media_type is not FixtureMediaType.JSON:
            raise PartitionError(f"scoped artifact is not JSON: {self.artifact_id}")
        try:
            decoded = json.loads(
                self.decode_text(),
                parse_constant=_reject_non_finite_json,
            )
        except (json.JSONDecodeError, ValueError) as exc:
            raise PartitionError(
                f"scoped artifact is not valid JSON: {self.artifact_id}: {exc}"
            ) from exc
        if not isinstance(decoded, Mapping):
            raise PartitionError(f"scoped JSON artifact root must be an object: {self.artifact_id}")
        return dict(decoded)


@dataclass(frozen=True, slots=True)
class FixtureView:
    """Detached collection containing only one principal's authorized fixtures."""

    principal: AccessPrincipal
    permitted_partitions: frozenset[FixturePartition]
    artifacts: tuple[ScopedFixtureArtifact, ...]

    def __post_init__(self) -> None:
        _validate_principal(self.principal)
        if not isinstance(self.permitted_partitions, frozenset) or not all(
            isinstance(partition, FixturePartition) for partition in self.permitted_partitions
        ):
            raise PartitionError(
                "permitted_partitions must be a frozenset of FixturePartition values"
            )

        expected_partitions = allowed_partitions_for(self.principal)
        if self.permitted_partitions != expected_partitions:
            raise PartitionError("permitted_partitions do not match the sealed policy")
        if not isinstance(self.artifacts, tuple) or not all(
            isinstance(artifact, ScopedFixtureArtifact) for artifact in self.artifacts
        ):
            raise PartitionError("artifacts must be a tuple of ScopedFixtureArtifact values")

        ordered_artifacts = tuple(sorted(self.artifacts, key=lambda artifact: artifact.artifact_id))
        object.__setattr__(self, "artifacts", ordered_artifacts)
        artifact_ids = [artifact.artifact_id for artifact in self.artifacts]
        if len(artifact_ids) != len(set(artifact_ids)):
            raise PartitionError("fixture view contains duplicate artifact IDs")
        forbidden = [
            artifact.artifact_id
            for artifact in self.artifacts
            if artifact.partition not in self.permitted_partitions
        ]
        if forbidden:
            raise PartitionError("fixture view contains artifacts outside its permitted partitions")

    @property
    def available_artifact_ids(self) -> tuple[str, ...]:
        """Return opaque IDs visible through this capability."""

        return tuple(artifact.artifact_id for artifact in self.artifacts)

    @property
    def accessible_state_sha256(self) -> str:
        """Fingerprint only the state visible through this capability."""

        return calculate_artifact_set_sha256(self.artifacts)

    def __len__(self) -> int:
        """Return the number of artifacts visible through this capability."""

        return len(self.artifacts)

    def contains(self, artifact_id: str) -> bool:
        """Return whether an opaque artifact ID is available in this capability."""

        _validate_artifact_id(artifact_id)
        return any(artifact.artifact_id == artifact_id for artifact in self.artifacts)

    def artifact(self, artifact_id: str) -> ScopedFixtureArtifact:
        """Return an available artifact or a non-disclosing access error."""

        _validate_artifact_id(artifact_id)
        for artifact in self.artifacts:
            if artifact.artifact_id == artifact_id:
                return artifact
        raise PartitionAccessError(
            f"fixture artifact is not available to {self.principal.value}: {artifact_id}"
        )

    def by_partition(
        self,
        partition: FixturePartition,
    ) -> tuple[ScopedFixtureArtifact, ...]:
        """Return artifacts from an authorized partition only."""

        decision = evaluate_partition_access(self.principal, partition)
        if not decision.granted:
            raise PartitionAccessError(
                f"partition is not available to {self.principal.value}: {partition.value}"
            )
        return tuple(artifact for artifact in self.artifacts if artifact.partition is partition)


class PartitionedFixtureStore:
    """Validator-owned fixture store that issues detached least-privilege views.

    The store itself must never be passed to Aurora or another runtime
    component. Only the result of :meth:`view_for` is a runtime capability.
    """

    __slots__ = ("_artifacts", "_fixture_set_id", "_fixture_set_sha256")

    def __init__(self, bundle: FixtureBundle) -> None:
        if not isinstance(bundle, FixtureBundle):
            raise PartitionError("bundle must be a FixtureBundle")
        self._fixture_set_id = bundle.manifest.fixture_set_id
        self._fixture_set_sha256 = bundle.fixture_set_sha256
        self._artifacts = tuple(sorted(bundle.artifacts, key=lambda artifact: artifact.path))

    @property
    def fixture_set_id(self) -> str:
        """Return the fixture identity without exposing fixture contents."""

        return self._fixture_set_id

    @property
    def fixture_set_sha256(self) -> str:
        """Return the complete fixture-set identity for evidence provenance."""

        return self._fixture_set_sha256

    def view_for(self, principal: AccessPrincipal) -> FixtureView:
        """Issue a detached capability containing only authorized artifacts."""

        partitions = allowed_partitions_for(principal)
        source_artifacts = tuple(
            artifact for artifact in self._artifacts if artifact.partition in partitions
        )
        return FixtureView(
            principal=principal,
            permitted_partitions=partitions,
            artifacts=_scope_artifacts(source_artifacts),
        )

    def partition_sha256(self, partition: FixturePartition) -> str:
        """Fingerprint one validator-visible partition for isolation evidence."""

        _validate_partition(partition)
        source_artifacts = tuple(
            artifact for artifact in self._artifacts if artifact.partition is partition
        )
        return calculate_artifact_set_sha256(_scope_artifacts(source_artifacts))


def allowed_partitions_for(
    principal: AccessPrincipal,
) -> frozenset[FixturePartition]:
    """Return the immutable partitions granted by the sealed architecture."""

    _validate_principal(principal)
    return _SEALED_ACCESS_POLICY[principal]


def denied_partitions_for(
    principal: AccessPrincipal,
) -> frozenset[FixturePartition]:
    """Return all partitions excluded from one principal's capability."""

    return frozenset(FixturePartition) - allowed_partitions_for(principal)


def evaluate_partition_access(
    principal: AccessPrincipal,
    partition: FixturePartition,
) -> PartitionAccessDecision:
    """Evaluate one access edge against the sealed partition policy."""

    _validate_principal(principal)
    _validate_partition(partition)
    granted = partition in _SEALED_ACCESS_POLICY[principal]
    reason = (
        AccessDecisionReason.AUTHORIZED_PARTITION
        if granted
        else AccessDecisionReason.PARTITION_DENIED
    )
    return PartitionAccessDecision(
        principal=principal,
        partition=partition,
        granted=granted,
        reason=reason,
    )


def calculate_artifact_set_sha256(
    artifacts: tuple[ScopedFixtureArtifact, ...],
) -> str:
    """Calculate a deterministic fingerprint of exactly the supplied artifacts."""

    if not isinstance(artifacts, tuple) or not all(
        isinstance(artifact, ScopedFixtureArtifact) for artifact in artifacts
    ):
        raise PartitionError("artifacts must be a tuple of ScopedFixtureArtifact values")
    ordered = sorted(artifacts, key=lambda artifact: artifact.artifact_id)
    artifact_ids = [artifact.artifact_id for artifact in ordered]
    if len(artifact_ids) != len(set(artifact_ids)):
        raise PartitionError("artifact set contains duplicate artifact IDs")
    payload = json.dumps(
        [
            {
                "artifact_id": artifact.artifact_id,
                "content_sha256": artifact.content_sha256,
                "media_type": artifact.media_type.value,
                "partition": artifact.partition.value,
                "size_bytes": artifact.size_bytes,
            }
            for artifact in ordered
        ],
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _scope_artifacts(
    artifacts: tuple[FixtureArtifact, ...],
) -> tuple[ScopedFixtureArtifact, ...]:
    counters: dict[FixturePartition, int] = {}
    scoped: list[ScopedFixtureArtifact] = []
    for artifact in sorted(
        artifacts,
        key=lambda item: (item.partition.value, item.path),
    ):
        index = counters.get(artifact.partition, 0) + 1
        counters[artifact.partition] = index
        scoped.append(
            ScopedFixtureArtifact(
                artifact_id=f"{artifact.partition.value}-{index:03d}",
                partition=artifact.partition,
                media_type=artifact.media_type,
                content_sha256=artifact.definition.sha256,
                size_bytes=artifact.definition.size_bytes,
                content_bytes=artifact.content_bytes,
            )
        )
    return tuple(scoped)


def _validate_principal(principal: AccessPrincipal) -> None:
    if not isinstance(principal, AccessPrincipal):
        raise PartitionError("principal must be an AccessPrincipal value")


def _validate_partition(partition: FixturePartition) -> None:
    if not isinstance(partition, FixturePartition):
        raise PartitionError("partition must be a FixturePartition value")


def _validate_artifact_id(artifact_id: str) -> None:
    if not isinstance(artifact_id, str):
        raise PartitionError("artifact_id must be a string")
    if _ARTIFACT_ID_PATTERN.fullmatch(artifact_id) is None:
        raise PartitionError("artifact_id must use <PARTITION>-<NNN> form")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise PartitionError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise PartitionError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
    "AccessDecisionReason",
    "AccessPrincipal",
    "FixtureView",
    "PartitionAccessDecision",
    "PartitionAccessError",
    "PartitionError",
    "PartitionedFixtureStore",
    "ScopedFixtureArtifact",
    "allowed_partitions_for",
    "calculate_artifact_set_sha256",
    "denied_partitions_for",
    "evaluate_partition_access",
]
