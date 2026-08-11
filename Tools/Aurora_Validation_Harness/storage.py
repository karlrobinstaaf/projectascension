"""Immutable, content-verified storage for Aurora validation run packages.

Storage is validator-owned infrastructure.  It persists canonical JSON
artifacts beneath a governed output root, writes each run through a private
staging directory, publishes the completed directory atomically, and refuses
to overwrite an existing run.  Loading verifies the manifest, every artifact,
the complete directory shape, and all declared hashes before returning data.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import tempfile
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import Final, cast

SUPPORTED_STORAGE_SCHEMA_VERSION: Final[str] = "1.0"
RUN_MANIFEST_FILENAME: Final[str] = "run_manifest.json"
DEFAULT_MAX_STORED_ARTIFACT_BYTES: Final[int] = 67_108_864
MAX_STORED_ARTIFACT_BYTES: Final[int] = 268_435_456
MAX_RUN_MANIFEST_BYTES: Final[int] = 16_777_216
MAX_RUN_PACKAGE_ARTIFACTS: Final[int] = 100_000
MAX_ARTIFACT_PATH_LENGTH: Final[int] = 1_024
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_PATH_SEGMENT_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,254}$")


class StorageError(ValueError):
    """Raised when a stored artifact or run package is unsafe or invalid."""


class ArtifactKind(StrEnum):
    """Canonical validator artifact classes supported by run packages."""

    BASELINE_VERIFICATION = "BASELINE_VERIFICATION"
    RUN_CONFIGURATION = "RUN_CONFIGURATION"
    FIXTURE_MANIFEST = "FIXTURE_MANIFEST"
    PARTITION_SET = "PARTITION_SET"
    CHANNEL_SERIES = "CHANNEL_SERIES"
    EVENT_SERIES = "EVENT_SERIES"
    EVIDENCE_PACKAGE = "EVIDENCE_PACKAGE"
    SNAPSHOT_SERIES = "SNAPSHOT_SERIES"
    TRANSITION_SERIES = "TRANSITION_SERIES"
    ASSERTION_SERIES = "ASSERTION_SERIES"
    COMPARISON_REPORT = "COMPARISON_REPORT"
    SCENARIO_VERDICT = "SCENARIO_VERDICT"
    DIAGNOSTIC = "DIAGNOSTIC"


@dataclass(frozen=True, slots=True)
class StoragePayload:
    """Canonical JSON object bytes with an exact content digest."""

    payload_json: bytes
    payload_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.payload_json, bytes):
            raise StorageError("payload_json must be bytes")
        _validate_sha256(self.payload_sha256, field="payload_sha256")
        if len(self.payload_json) > MAX_STORED_ARTIFACT_BYTES:
            raise StorageError(f"payload_json must not exceed {MAX_STORED_ARTIFACT_BYTES} bytes")
        if hashlib.sha256(self.payload_json).hexdigest() != self.payload_sha256:
            raise StorageError("payload_sha256 does not match payload_json")
        decoded = _decode_json_object(self.payload_json, field="payload_json")
        _validate_json_value(decoded, path="payload")
        if self.payload_json != _canonical_json_bytes(decoded):
            raise StorageError("payload_json must use canonical JSON encoding")

    @property
    def size_bytes(self) -> int:
        """Return the exact stored byte length."""

        return len(self.payload_json)

    def decode(self) -> dict[str, object]:
        """Return a fresh decoded JSON object."""

        return _decode_json_object(self.payload_json, field="payload_json")

    def to_mapping(self) -> dict[str, object]:
        """Return the portable payload wrapper representation."""

        return {
            "data": self.decode(),
            "payload_sha256": self.payload_sha256,
            "size_bytes": self.size_bytes,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> StoragePayload:
        """Parse and verify one portable payload wrapper."""

        mapping = _require_mapping(value, field="storage payload")
        _require_exact_keys(
            mapping,
            required=frozenset({"data", "payload_sha256", "size_bytes"}),
            field="storage payload",
        )
        data = _require_mapping(mapping["data"], field="storage payload.data")
        payload = create_storage_payload(
            data,
            max_payload_bytes=MAX_STORED_ARTIFACT_BYTES,
        )
        declared_size = _require_integer(mapping["size_bytes"], field="storage payload.size_bytes")
        if declared_size != payload.size_bytes:
            raise StorageError("declared size_bytes does not match storage payload")
        _validate_declared_sha256(
            payload.payload_sha256,
            mapping,
            key="payload_sha256",
            field="storage payload",
        )
        return payload


@dataclass(frozen=True, slots=True)
class ArtifactDescriptor:
    """Immutable manifest entry for one content-addressed JSON artifact."""

    artifact_id: str
    kind: ArtifactKind
    relative_path: str
    payload_sha256: str
    size_bytes: int

    def __post_init__(self) -> None:
        _validate_control_id(self.artifact_id, field="artifact_id")
        if not isinstance(self.kind, ArtifactKind):
            raise StorageError("kind must be an ArtifactKind value")
        _validate_artifact_path(self.relative_path)
        _validate_sha256(self.payload_sha256, field="payload_sha256")
        _validate_positive_integer(self.size_bytes, field="size_bytes")
        if self.size_bytes > MAX_STORED_ARTIFACT_BYTES:
            raise StorageError(f"size_bytes must not exceed {MAX_STORED_ARTIFACT_BYTES}")

    @property
    def descriptor_sha256(self) -> str:
        """Return the digest of this artifact declaration."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "artifact_id": self.artifact_id,
            "kind": self.kind.value,
            "payload_sha256": self.payload_sha256,
            "relative_path": self.relative_path,
            "size_bytes": self.size_bytes,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable artifact declaration."""

        return {**self._content_mapping(), "descriptor_sha256": self.descriptor_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> ArtifactDescriptor:
        """Parse and verify one serialized artifact declaration."""

        mapping = _require_mapping(value, field="artifact descriptor")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "artifact_id",
                    "descriptor_sha256",
                    "kind",
                    "payload_sha256",
                    "relative_path",
                    "size_bytes",
                }
            ),
            field="artifact descriptor",
        )
        descriptor = cls(
            artifact_id=_require_string(
                mapping["artifact_id"], field="artifact descriptor.artifact_id"
            ),
            kind=_parse_enum(
                ArtifactKind,
                mapping["kind"],
                field="artifact descriptor.kind",
            ),
            relative_path=_require_string(
                mapping["relative_path"],
                field="artifact descriptor.relative_path",
            ),
            payload_sha256=_require_string(
                mapping["payload_sha256"],
                field="artifact descriptor.payload_sha256",
            ),
            size_bytes=_require_integer(
                mapping["size_bytes"], field="artifact descriptor.size_bytes"
            ),
        )
        _validate_declared_sha256(
            descriptor.descriptor_sha256,
            mapping,
            key="descriptor_sha256",
            field="artifact descriptor",
        )
        return descriptor


@dataclass(frozen=True, slots=True)
class RunPackageManifest:
    """Integrity-sealed inventory for one immutable validation run directory."""

    package_id: str
    run_id: str
    scenario_id: str
    finalized_at_tick: int
    artifacts: tuple[ArtifactDescriptor, ...]

    def __post_init__(self) -> None:
        _validate_control_id(self.package_id, field="package_id")
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        _validate_tick(self.finalized_at_tick, field="finalized_at_tick")
        _validate_artifact_descriptors(self.artifacts)

    @property
    def artifact_count(self) -> int:
        """Return the immutable number of stored artifacts."""

        return len(self.artifacts)

    @property
    def total_size_bytes(self) -> int:
        """Return the exact combined size of all artifact payloads."""

        return sum(artifact.size_bytes for artifact in self.artifacts)

    @property
    def manifest_sha256(self) -> str:
        """Return the digest binding run identity and all artifact declarations."""

        return calculate_run_package_manifest_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "artifact_count": self.artifact_count,
            "artifacts": [artifact.to_mapping() for artifact in self.artifacts],
            "finalized_at_tick": self.finalized_at_tick,
            "package_id": self.package_id,
            "package_type": "FINALIZED_RUN_PACKAGE",
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "storage_schema_version": SUPPORTED_STORAGE_SCHEMA_VERSION,
            "total_size_bytes": self.total_size_bytes,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete portable run-package manifest."""

        return {**self._content_mapping(), "manifest_sha256": self.manifest_sha256}

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> RunPackageManifest:
        """Parse and verify one serialized run-package manifest."""

        mapping = _require_mapping(value, field="run package manifest")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "artifact_count",
                    "artifacts",
                    "finalized_at_tick",
                    "manifest_sha256",
                    "package_id",
                    "package_type",
                    "run_id",
                    "scenario_id",
                    "storage_schema_version",
                    "total_size_bytes",
                }
            ),
            field="run package manifest",
        )
        _validate_schema_version(mapping["storage_schema_version"])
        if mapping["package_type"] != "FINALIZED_RUN_PACKAGE":
            raise StorageError("unsupported package_type")
        manifest = cls(
            package_id=_require_string(
                mapping["package_id"], field="run package manifest.package_id"
            ),
            run_id=_require_string(mapping["run_id"], field="run package manifest.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"], field="run package manifest.scenario_id"
            ),
            finalized_at_tick=_require_integer(
                mapping["finalized_at_tick"],
                field="run package manifest.finalized_at_tick",
            ),
            artifacts=_parse_artifact_descriptors(mapping["artifacts"]),
        )
        declared_count = _require_integer(
            mapping["artifact_count"],
            field="run package manifest.artifact_count",
        )
        if declared_count != manifest.artifact_count:
            raise StorageError("declared artifact_count does not match run package manifest")
        declared_size = _require_integer(
            mapping["total_size_bytes"],
            field="run package manifest.total_size_bytes",
        )
        if declared_size != manifest.total_size_bytes:
            raise StorageError("declared total_size_bytes does not match run package manifest")
        _validate_declared_sha256(
            manifest.manifest_sha256,
            mapping,
            key="manifest_sha256",
            field="run package manifest",
        )
        return manifest


def create_storage_payload(
    data: Mapping[str, object],
    *,
    max_payload_bytes: int = DEFAULT_MAX_STORED_ARTIFACT_BYTES,
) -> StoragePayload:
    """Create canonical storage bytes from one JSON object."""

    if not isinstance(data, Mapping):
        raise StorageError("storage payload data must be a JSON object")
    if isinstance(max_payload_bytes, bool) or not isinstance(max_payload_bytes, int):
        raise StorageError("max_payload_bytes must be an integer")
    if not 1 <= max_payload_bytes <= MAX_STORED_ARTIFACT_BYTES:
        raise StorageError(f"max_payload_bytes must be between 1 and {MAX_STORED_ARTIFACT_BYTES}")
    normalized = _normalize_json_value(data, path="payload")
    if not isinstance(normalized, dict):
        raise StorageError("storage payload data must be a JSON object")
    payload_json = _canonical_json_bytes(normalized)
    if len(payload_json) > max_payload_bytes:
        raise StorageError(f"storage payload must not exceed {max_payload_bytes} bytes")
    return StoragePayload(
        payload_json=payload_json,
        payload_sha256=hashlib.sha256(payload_json).hexdigest(),
    )


def create_artifact_descriptor(
    *,
    artifact_id: str,
    kind: ArtifactKind,
    relative_path: str,
    payload: StoragePayload,
) -> ArtifactDescriptor:
    """Create a manifest entry bound to exact storage payload bytes."""

    if not isinstance(payload, StoragePayload):
        raise StorageError("payload must be a StoragePayload")
    return ArtifactDescriptor(
        artifact_id=artifact_id,
        kind=kind,
        relative_path=relative_path,
        payload_sha256=payload.payload_sha256,
        size_bytes=payload.size_bytes,
    )


def create_run_package_manifest(
    *,
    package_id: str,
    run_id: str,
    scenario_id: str,
    finalized_at_tick: int,
    artifacts: tuple[ArtifactDescriptor, ...],
) -> RunPackageManifest:
    """Create a manifest with canonical artifact-path ordering."""

    if not isinstance(artifacts, tuple):
        raise StorageError("artifacts must be a tuple")
    return RunPackageManifest(
        package_id=package_id,
        run_id=run_id,
        scenario_id=scenario_id,
        finalized_at_tick=finalized_at_tick,
        artifacts=tuple(sorted(artifacts, key=lambda artifact: artifact.relative_path)),
    )


def calculate_run_package_manifest_sha256(manifest: RunPackageManifest) -> str:
    """Calculate the canonical digest for one run-package manifest."""

    if not isinstance(manifest, RunPackageManifest):
        raise StorageError("manifest must be a RunPackageManifest")
    return hashlib.sha256(_canonical_json_bytes(manifest._content_mapping())).hexdigest()


def prepare_storage_root(output_root: Path) -> Path:
    """Create or validate one explicit output-root directory without recursion."""

    root = _require_path(output_root, field="output_root")
    if root.is_symlink():
        raise StorageError("output_root must not be a symbolic link")
    if root.exists():
        if not root.is_dir():
            raise StorageError("output_root must be a directory")
        return root.resolve()

    parent = root.parent
    if parent.is_symlink():
        raise StorageError("output_root parent must not be a symbolic link")
    if not parent.exists() or not parent.is_dir():
        raise StorageError("output_root parent must be an existing directory")
    try:
        root.mkdir(exist_ok=False)
    except OSError as exc:
        raise StorageError(f"could not create output_root: {root}") from exc
    return root.resolve()


def write_run_package(
    output_root: Path,
    manifest: RunPackageManifest,
    payloads: Mapping[str, StoragePayload],
) -> Path:
    """Atomically publish a new immutable run directory without overwriting."""

    root = _validate_existing_directory(output_root, field="output_root")
    if not isinstance(manifest, RunPackageManifest):
        raise StorageError("manifest must be a RunPackageManifest")
    normalized_payloads = _validate_package_payloads(manifest, payloads)
    final_directory = root / manifest.run_id
    if final_directory.exists() or final_directory.is_symlink():
        raise StorageError(f"run package already exists: {manifest.run_id}")

    try:
        staging_text = tempfile.mkdtemp(
            prefix=f".{manifest.run_id}.staging-",
            dir=root,
        )
    except OSError as exc:
        raise StorageError("could not create run-package staging directory") from exc
    staging_directory = Path(staging_text)
    published = False
    try:
        for descriptor in manifest.artifacts:
            payload = normalized_payloads[descriptor.artifact_id]
            artifact_path = _join_artifact_path(staging_directory, descriptor.relative_path)
            artifact_path.parent.mkdir(parents=True, exist_ok=True)
            _write_new_file(artifact_path, payload.payload_json)

        manifest_bytes = _canonical_json_bytes(manifest.to_mapping())
        if len(manifest_bytes) > MAX_RUN_MANIFEST_BYTES:
            raise StorageError(
                f"serialized run manifest must not exceed {MAX_RUN_MANIFEST_BYTES} bytes"
            )
        _write_new_file(staging_directory / RUN_MANIFEST_FILENAME, manifest_bytes)
        if final_directory.exists() or final_directory.is_symlink():
            raise StorageError(f"run package already exists: {manifest.run_id}")
        try:
            staging_directory.rename(final_directory)
        except OSError as exc:
            raise StorageError("could not atomically publish run package") from exc
        published = True
    finally:
        if not published and staging_directory.exists():
            shutil.rmtree(staging_directory)
    return final_directory


def load_run_package_manifest(package_directory: Path) -> RunPackageManifest:
    """Load and verify the canonical manifest file from one run directory."""

    directory = _validate_existing_directory(
        package_directory,
        field="package_directory",
    )
    manifest_path = directory / RUN_MANIFEST_FILENAME
    manifest_bytes = _read_regular_file(
        manifest_path,
        max_bytes=MAX_RUN_MANIFEST_BYTES,
        field="run manifest",
    )
    mapping = _decode_json_object(manifest_bytes, field="run manifest")
    if manifest_bytes != _canonical_json_bytes(mapping):
        raise StorageError("run manifest must use canonical JSON encoding")
    manifest = RunPackageManifest.from_mapping(mapping)
    if directory.name != manifest.run_id:
        raise StorageError("run package directory name must match manifest run_id")
    return manifest


def read_run_artifact(
    package_directory: Path,
    manifest: RunPackageManifest,
    artifact_id: str,
) -> StoragePayload:
    """Read and verify one artifact declared by an exact manifest."""

    directory = _validate_existing_directory(
        package_directory,
        field="package_directory",
    )
    if not isinstance(manifest, RunPackageManifest):
        raise StorageError("manifest must be a RunPackageManifest")
    _validate_control_id(artifact_id, field="artifact_id")
    descriptor = next(
        (artifact for artifact in manifest.artifacts if artifact.artifact_id == artifact_id),
        None,
    )
    if descriptor is None:
        raise StorageError(f"artifact_id is not declared by manifest: {artifact_id}")
    artifact_path = _join_artifact_path(directory, descriptor.relative_path)
    payload_json = _read_regular_file(
        artifact_path,
        max_bytes=MAX_STORED_ARTIFACT_BYTES,
        field=f"artifact {artifact_id}",
    )
    payload = StoragePayload(
        payload_json=payload_json,
        payload_sha256=hashlib.sha256(payload_json).hexdigest(),
    )
    if payload.size_bytes != descriptor.size_bytes:
        raise StorageError(f"artifact size does not match manifest: {artifact_id}")
    if payload.payload_sha256 != descriptor.payload_sha256:
        raise StorageError(f"artifact digest does not match manifest: {artifact_id}")
    return payload


def verify_run_package(
    package_directory: Path,
    *,
    expected_manifest: RunPackageManifest | None = None,
) -> RunPackageManifest:
    """Verify the manifest, every artifact, and the complete directory shape."""

    directory = _validate_existing_directory(
        package_directory,
        field="package_directory",
    )
    if expected_manifest is not None and not isinstance(expected_manifest, RunPackageManifest):
        raise StorageError("expected_manifest must be null or a RunPackageManifest")
    manifest = load_run_package_manifest(directory)
    if expected_manifest is not None and manifest != expected_manifest:
        raise StorageError("stored run manifest does not match expected manifest")
    for descriptor in manifest.artifacts:
        read_run_artifact(directory, manifest, descriptor.artifact_id)
    _validate_package_tree(directory, manifest)
    return manifest


def _validate_package_payloads(
    manifest: RunPackageManifest,
    payloads: Mapping[str, StoragePayload],
) -> dict[str, StoragePayload]:
    mapping = _require_mapping(payloads, field="payloads")
    if not all(isinstance(payload, StoragePayload) for payload in mapping.values()):
        raise StorageError("payloads values must be StoragePayload instances")
    normalized = cast(dict[str, StoragePayload], dict(mapping))
    expected_ids = {artifact.artifact_id for artifact in manifest.artifacts}
    actual_ids = set(normalized)
    missing = sorted(expected_ids - actual_ids)
    unexpected = sorted(actual_ids - expected_ids)
    if missing:
        raise StorageError(f"payloads are missing artifact IDs: {', '.join(missing)}")
    if unexpected:
        raise StorageError(f"payloads contain unexpected artifact IDs: {', '.join(unexpected)}")
    for descriptor in manifest.artifacts:
        payload = normalized[descriptor.artifact_id]
        if payload.size_bytes != descriptor.size_bytes:
            raise StorageError(f"payload size does not match descriptor: {descriptor.artifact_id}")
        if payload.payload_sha256 != descriptor.payload_sha256:
            raise StorageError(
                f"payload digest does not match descriptor: {descriptor.artifact_id}"
            )
    return normalized


def _validate_artifact_descriptors(artifacts: tuple[ArtifactDescriptor, ...]) -> None:
    if not isinstance(artifacts, tuple) or not all(
        isinstance(artifact, ArtifactDescriptor) for artifact in artifacts
    ):
        raise StorageError("artifacts must be a tuple of ArtifactDescriptor values")
    if not artifacts:
        raise StorageError("artifacts must not be empty")
    if len(artifacts) > MAX_RUN_PACKAGE_ARTIFACTS:
        raise StorageError(f"artifacts must not exceed {MAX_RUN_PACKAGE_ARTIFACTS} entries")
    artifact_ids = tuple(artifact.artifact_id for artifact in artifacts)
    if len(artifact_ids) != len(set(artifact_ids)):
        raise StorageError("artifacts must use unique artifact IDs")
    paths = tuple(artifact.relative_path for artifact in artifacts)
    if len(paths) != len(set(paths)):
        raise StorageError("artifacts must use unique relative paths")
    if paths != tuple(sorted(paths)):
        raise StorageError("artifacts must use lexical relative-path order")
    _validate_non_overlapping_paths(paths)


def _validate_non_overlapping_paths(paths: tuple[str, ...]) -> None:
    parsed_paths = tuple(PurePosixPath(path) for path in paths)
    for index, path in enumerate(parsed_paths):
        for other in parsed_paths[index + 1 :]:
            if _is_path_prefix(path, other) or _is_path_prefix(other, path):
                raise StorageError("artifact paths must not overlap file and directory positions")


def _is_path_prefix(prefix: PurePosixPath, value: PurePosixPath) -> bool:
    return len(prefix.parts) < len(value.parts) and value.parts[: len(prefix.parts)] == prefix.parts


def _validate_artifact_path(value: str) -> None:
    if not isinstance(value, str):
        raise StorageError("relative_path must be a string")
    if not value or len(value) > MAX_ARTIFACT_PATH_LENGTH:
        raise StorageError(f"relative_path must contain 1-{MAX_ARTIFACT_PATH_LENGTH} characters")
    if "\\" in value:
        raise StorageError("relative_path must use POSIX separators")
    path = PurePosixPath(value)
    if path.is_absolute() or value != path.as_posix():
        raise StorageError("relative_path must be a normalized relative POSIX path")
    if any(part in {"", ".", ".."} for part in path.parts):
        raise StorageError("relative_path must not contain empty, dot, or parent segments")
    if any(_PATH_SEGMENT_PATTERN.fullmatch(part) is None for part in path.parts):
        raise StorageError("relative_path contains an unsupported path segment")
    if path.name == RUN_MANIFEST_FILENAME:
        raise StorageError(f"relative_path must not use reserved name {RUN_MANIFEST_FILENAME}")
    if path.suffix != ".json":
        raise StorageError("relative_path must end in .json")


def _join_artifact_path(root: Path, relative_path: str) -> Path:
    _validate_artifact_path(relative_path)
    candidate = root.joinpath(*PurePosixPath(relative_path).parts)
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise StorageError("artifact path escapes package directory") from exc
    return candidate


def _validate_package_tree(directory: Path, manifest: RunPackageManifest) -> None:
    expected_files = {
        Path(*PurePosixPath(artifact.relative_path).parts) for artifact in manifest.artifacts
    }
    expected_files.add(Path(RUN_MANIFEST_FILENAME))
    expected_directories: set[Path] = set()
    for path in expected_files:
        expected_directories.update(path.parents)
    expected_directories.discard(Path("."))

    actual_files: set[Path] = set()
    actual_directories: set[Path] = set()
    try:
        entries = tuple(directory.rglob("*"))
    except OSError as exc:
        raise StorageError("could not enumerate run package") from exc
    for entry in entries:
        relative = entry.relative_to(directory)
        if entry.is_symlink():
            raise StorageError(f"run package must not contain symbolic links: {relative}")
        if entry.is_dir():
            actual_directories.add(relative)
        elif entry.is_file():
            actual_files.add(relative)
        else:
            raise StorageError(f"run package contains unsupported filesystem entry: {relative}")
    if actual_files != expected_files:
        missing = sorted(str(path) for path in expected_files - actual_files)
        unexpected = sorted(str(path) for path in actual_files - expected_files)
        if missing:
            raise StorageError(f"run package is missing declared files: {', '.join(missing)}")
        raise StorageError(f"run package contains unexpected files: {', '.join(unexpected)}")
    if actual_directories != expected_directories:
        missing = sorted(str(path) for path in expected_directories - actual_directories)
        unexpected = sorted(str(path) for path in actual_directories - expected_directories)
        if missing:
            raise StorageError(f"run package is missing declared directories: {', '.join(missing)}")
        raise StorageError(f"run package contains unexpected directories: {', '.join(unexpected)}")


def _write_new_file(path: Path, data: bytes) -> None:
    try:
        with path.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except FileExistsError as exc:
        raise StorageError(f"refusing to overwrite storage file: {path.name}") from exc
    except OSError as exc:
        raise StorageError(f"could not write storage file: {path.name}") from exc


def _read_regular_file(path: Path, *, max_bytes: int, field: str) -> bytes:
    if path.is_symlink():
        raise StorageError(f"{field} must not be a symbolic link")
    if not path.exists():
        raise StorageError(f"{field} is missing")
    if not path.is_file():
        raise StorageError(f"{field} must be a regular file")
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise StorageError(f"could not inspect {field}") from exc
    if size > max_bytes:
        raise StorageError(f"{field} must not exceed {max_bytes} bytes")
    try:
        return path.read_bytes()
    except OSError as exc:
        raise StorageError(f"could not read {field}") from exc


def _validate_existing_directory(value: Path, *, field: str) -> Path:
    path = _require_path(value, field=field)
    if path.is_symlink():
        raise StorageError(f"{field} must not be a symbolic link")
    if not path.exists():
        raise StorageError(f"{field} does not exist")
    if not path.is_dir():
        raise StorageError(f"{field} must be a directory")
    return path.resolve()


def _require_path(value: object, *, field: str) -> Path:
    if not isinstance(value, Path):
        raise StorageError(f"{field} must be a pathlib.Path")
    return value


def _parse_artifact_descriptors(value: object) -> tuple[ArtifactDescriptor, ...]:
    if not isinstance(value, list):
        raise StorageError("run package manifest.artifacts must be an array")
    return tuple(
        ArtifactDescriptor.from_mapping(
            _require_mapping(item, field=f"run package manifest.artifacts[{index}]")
        )
        for index, item in enumerate(value)
    )


def _validate_schema_version(value: object) -> None:
    version = _require_string(value, field="storage_schema_version")
    if version != SUPPORTED_STORAGE_SCHEMA_VERSION:
        raise StorageError(f"unsupported storage_schema_version: {version}")


def _validate_declared_sha256(
    calculated_sha256: str,
    mapping: Mapping[str, object],
    *,
    key: str,
    field: str,
) -> None:
    declared_sha256 = _require_string(mapping[key], field=f"{field}.{key}")
    if declared_sha256 != calculated_sha256:
        raise StorageError(f"declared {key} does not match {field}")


def _decode_json_object(value: bytes, *, field: str) -> dict[str, object]:
    try:
        decoded = json.loads(
            value.decode("utf-8"),
            parse_constant=_reject_non_finite_json,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise StorageError(f"{field} is not valid finite UTF-8 JSON") from exc
    if not isinstance(decoded, dict):
        raise StorageError(f"{field} must encode a JSON object")
    return cast(dict[str, object], decoded)


def _canonical_json_bytes(value: object) -> bytes:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise StorageError("value must be canonical finite JSON") from exc


def _normalize_json_value(value: object, *, path: str) -> object:
    _validate_json_value(value, path=path)
    if isinstance(value, Mapping):
        return {
            key: _normalize_json_value(item, path=f"{path}.{key}")
            for key, item in sorted(value.items())
        }
    if isinstance(value, (list, tuple)):
        return [
            _normalize_json_value(item, path=f"{path}[{index}]") for index, item in enumerate(value)
        ]
    return value


def _validate_json_value(value: object, *, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise StorageError(f"{path} must not contain non-finite numbers")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise StorageError(f"{path} object keys must be strings")
            _validate_json_value(item, path=f"{path}.{key}")
        return
    if isinstance(value, (list, tuple)):
        for index, item in enumerate(value):
            _validate_json_value(item, path=f"{path}[{index}]")
        return
    raise StorageError(f"{path} contains unsupported JSON value type")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


def _require_mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise StorageError(f"{field} must be an object")
    for key in value:
        if not isinstance(key, str):
            raise StorageError(f"{field} keys must be strings")
    return cast(Mapping[str, object], value)


def _require_exact_keys(
    mapping: Mapping[str, object],
    *,
    required: frozenset[str],
    field: str,
) -> None:
    actual = frozenset(mapping)
    missing = sorted(required - actual)
    unexpected = sorted(actual - required)
    if missing:
        raise StorageError(f"{field} is missing required fields: {', '.join(missing)}")
    if unexpected:
        raise StorageError(f"{field} contains unexpected fields: {', '.join(unexpected)}")


def _require_string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        raise StorageError(f"{field} must be a string")
    return value


def _require_integer(value: object, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise StorageError(f"{field} must be an integer")
    return value


def _parse_enum[T: StrEnum](
    enum_type: type[T],
    value: object,
    *,
    field: str,
) -> T:
    raw = _require_string(value, field=field)
    try:
        return enum_type(raw)
    except ValueError as exc:
        raise StorageError(f"{field} contains an unsupported value: {raw}") from exc


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise StorageError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise StorageError(f"{field} must be a stable uppercase control identifier")


def _validate_scenario_id(value: str) -> None:
    if not isinstance(value, str):
        raise StorageError("scenario_id must be a string")
    if _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        raise StorageError("scenario_id must match AURORA-SCN-<FAMILY>-<NNN>")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise StorageError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise StorageError(f"{field} must be a lowercase SHA-256 digest")


def _validate_positive_integer(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise StorageError(f"{field} must be an integer")
    if value < 1:
        raise StorageError(f"{field} must be positive")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise StorageError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise StorageError(f"{field} must be between 0 and {MAX_TICK}")


__all__ = [
    "DEFAULT_MAX_STORED_ARTIFACT_BYTES",
    "MAX_ARTIFACT_PATH_LENGTH",
    "MAX_RUN_MANIFEST_BYTES",
    "MAX_RUN_PACKAGE_ARTIFACTS",
    "MAX_STORED_ARTIFACT_BYTES",
    "MAX_TICK",
    "RUN_MANIFEST_FILENAME",
    "SUPPORTED_STORAGE_SCHEMA_VERSION",
    "ArtifactDescriptor",
    "ArtifactKind",
    "RunPackageManifest",
    "StorageError",
    "StoragePayload",
    "calculate_run_package_manifest_sha256",
    "create_artifact_descriptor",
    "create_run_package_manifest",
    "create_storage_payload",
    "load_run_package_manifest",
    "prepare_storage_root",
    "read_run_artifact",
    "verify_run_package",
    "write_run_package",
]
