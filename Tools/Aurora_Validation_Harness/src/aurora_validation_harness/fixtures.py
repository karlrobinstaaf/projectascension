"""Fixture manifest models, integrity checks, and immutable artifact loading.

Fixtures are validator-owned inputs. This module proves their identity and
keeps their declared partitions explicit, but it does not decide which data is
visible to Aurora. Access-controlled views belong to the partition layer.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import Final

SUPPORTED_FIXTURE_MANIFEST_VERSION: Final[str] = "1.0"
FIXTURE_ROOT: Final[str] = "Development/Validation/Aurora/Fixtures"

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_IDENTIFIER_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_MANIFEST_KEYS: Final[frozenset[str]] = frozenset(
    {
        "files",
        "fixture_manifest_sha256",
        "fixture_manifest_version",
        "fixture_set_id",
        "scenario_id",
    }
)
_REQUIRED_MANIFEST_KEYS: Final[frozenset[str]] = _MANIFEST_KEYS - {"fixture_manifest_sha256"}
_FILE_KEYS: Final[frozenset[str]] = frozenset(
    {
        "media_type",
        "partition",
        "path",
        "sha256",
        "size_bytes",
    }
)


class FixtureError(ValueError):
    """Raised when a fixture definition, manifest, or artifact is invalid."""


class FixturePartition(StrEnum):
    """Validator-owned information partition assigned to a fixture artifact."""

    WORLD = "WORLD"
    AURORA = "AURORA"
    PLAYER_PRIVATE = "PLAYER_PRIVATE"
    FUTURE = "FUTURE"
    VALIDATOR = "VALIDATOR"
    EXPECTED_RESULTS = "EXPECTED_RESULTS"


CORE_FIXTURE_PARTITIONS: Final[frozenset[FixturePartition]] = frozenset(
    {
        FixturePartition.WORLD,
        FixturePartition.AURORA,
        FixturePartition.PLAYER_PRIVATE,
        FixturePartition.FUTURE,
        FixturePartition.VALIDATOR,
    }
)


class FixtureMediaType(StrEnum):
    """Content formats supported by the dependency-free fixture loader."""

    JSON = "application/json"
    TEXT = "text/plain"
    MARKDOWN = "text/markdown"
    BINARY = "application/octet-stream"


_TEXT_MEDIA_TYPES: Final[frozenset[FixtureMediaType]] = frozenset(
    {
        FixtureMediaType.JSON,
        FixtureMediaType.TEXT,
        FixtureMediaType.MARKDOWN,
    }
)


@dataclass(frozen=True, slots=True)
class FixtureFile:
    """Expected identity and partition of one controlled fixture file."""

    path: str
    partition: FixturePartition
    media_type: FixtureMediaType
    sha256: str
    size_bytes: int

    def __post_init__(self) -> None:
        if not isinstance(self.partition, FixturePartition):
            raise FixtureError("partition must be a FixturePartition value")
        if not isinstance(self.media_type, FixtureMediaType):
            raise FixtureError("media_type must be a FixtureMediaType value")
        _validate_fixture_path(self.path)
        _validate_sha256(self.sha256, field="sha256")
        if isinstance(self.size_bytes, bool) or not isinstance(self.size_bytes, int):
            raise FixtureError("size_bytes must be an integer")
        if self.size_bytes < 0:
            raise FixtureError("size_bytes must not be negative")

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> FixtureFile:
        """Create a fixture file definition from decoded JSON data."""

        _validate_keys(
            data,
            allowed=_FILE_KEYS,
            required=_FILE_KEYS,
            context="fixture file",
        )
        raw_partition = _required_string(data, "partition", context="fixture file")
        try:
            partition = FixturePartition(raw_partition)
        except ValueError as exc:
            raise FixtureError(f"unsupported fixture partition: {raw_partition}") from exc

        raw_media_type = _required_string(data, "media_type", context="fixture file")
        try:
            media_type = FixtureMediaType(raw_media_type)
        except ValueError as exc:
            raise FixtureError(f"unsupported fixture media_type: {raw_media_type}") from exc

        return cls(
            path=_required_string(data, "path", context="fixture file"),
            partition=partition,
            media_type=media_type,
            sha256=_required_string(data, "sha256", context="fixture file"),
            size_bytes=_required_integer(data, "size_bytes", context="fixture file"),
        )

    def to_mapping(self) -> dict[str, object]:
        """Return the stable JSON representation used for manifest hashing."""

        return {
            "media_type": self.media_type.value,
            "partition": self.partition.value,
            "path": self.path,
            "sha256": self.sha256,
            "size_bytes": self.size_bytes,
        }


@dataclass(frozen=True, slots=True)
class FixtureManifest:
    """Hash-bound definition of a complete, partitioned fixture set."""

    fixture_set_id: str
    scenario_id: str
    fixture_manifest_version: str
    files: tuple[FixtureFile, ...]
    fixture_manifest_sha256: str | None = None

    def __post_init__(self) -> None:
        _validate_identifier(self.fixture_set_id, field="fixture_set_id")
        if not isinstance(self.scenario_id, str):
            raise FixtureError("scenario_id must be a string")
        if _SCENARIO_ID_PATTERN.fullmatch(self.scenario_id) is None:
            raise FixtureError("scenario_id must match AURORA-SCN-<GATE>-<NNN>")
        if not isinstance(self.fixture_manifest_version, str):
            raise FixtureError("fixture_manifest_version must be a string")
        if self.fixture_manifest_version != SUPPORTED_FIXTURE_MANIFEST_VERSION:
            raise FixtureError(
                "unsupported fixture_manifest_version: "
                f"{self.fixture_manifest_version}; "
                f"expected {SUPPORTED_FIXTURE_MANIFEST_VERSION}"
            )
        if not isinstance(self.files, tuple):
            raise FixtureError("files must be a tuple of FixtureFile values")
        if not all(isinstance(entry, FixtureFile) for entry in self.files):
            raise FixtureError("files must contain only FixtureFile values")
        object.__setattr__(
            self,
            "files",
            tuple(sorted(self.files, key=lambda entry: entry.path)),
        )

        path_counts = Counter(entry.path for entry in self.files)
        duplicates = sorted(path for path, count in path_counts.items() if count > 1)
        if duplicates:
            raise FixtureError(f"duplicate fixture paths: {', '.join(duplicates)}")

        present_partitions = {entry.partition for entry in self.files}
        missing_partitions = sorted(
            CORE_FIXTURE_PARTITIONS - present_partitions,
            key=lambda partition: partition.value,
        )
        if missing_partitions:
            names = ", ".join(partition.value for partition in missing_partitions)
            raise FixtureError(f"missing core fixture partition(s): {names}")

        if self.fixture_manifest_sha256 is not None:
            _validate_sha256(
                self.fixture_manifest_sha256,
                field="fixture_manifest_sha256",
            )

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> FixtureManifest:
        """Create a fixture manifest from decoded JSON data."""

        _validate_keys(
            data,
            allowed=_MANIFEST_KEYS,
            required=_REQUIRED_MANIFEST_KEYS,
            context="fixture manifest",
        )
        raw_files = data.get("files")
        if not isinstance(raw_files, list):
            raise FixtureError("fixture manifest.files must be a JSON array")

        files: list[FixtureFile] = []
        for index, item in enumerate(raw_files):
            if not isinstance(item, Mapping):
                raise FixtureError(f"fixture manifest.files[{index}] must be a JSON object")
            files.append(FixtureFile.from_mapping(item))

        return cls(
            fixture_set_id=_required_string(data, "fixture_set_id"),
            scenario_id=_required_string(data, "scenario_id"),
            fixture_manifest_version=_required_string(
                data,
                "fixture_manifest_version",
            ),
            files=tuple(files),
            fixture_manifest_sha256=_optional_string(
                data,
                "fixture_manifest_sha256",
            ),
        )

    def hash_payload(self) -> dict[str, object]:
        """Return canonical content excluding the self-referential hash field."""

        ordered_files = sorted(self.files, key=lambda entry: entry.path)
        return {
            "files": [entry.to_mapping() for entry in ordered_files],
            "fixture_manifest_version": self.fixture_manifest_version,
            "fixture_set_id": self.fixture_set_id,
            "scenario_id": self.scenario_id,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete stable JSON representation."""

        return self.hash_payload() | {"fixture_manifest_sha256": self.fixture_manifest_sha256}


@dataclass(frozen=True, slots=True)
class FixtureArtifact:
    """One verified fixture artifact represented by immutable exact bytes."""

    definition: FixtureFile
    resolved_path: Path
    content_bytes: bytes

    def __post_init__(self) -> None:
        if not isinstance(self.definition, FixtureFile):
            raise FixtureError("definition must be a FixtureFile")
        if not isinstance(self.resolved_path, Path):
            raise FixtureError("resolved_path must be a Path")
        if not isinstance(self.content_bytes, bytes):
            raise FixtureError("content_bytes must be bytes")
        if len(self.content_bytes) != self.definition.size_bytes:
            raise FixtureError(f"fixture size does not match definition: {self.definition.path}")
        if _sha256_bytes(self.content_bytes) != self.definition.sha256:
            raise FixtureError(f"fixture hash does not match definition: {self.definition.path}")

    @property
    def path(self) -> str:
        """Return the repository-relative path declared by the manifest."""

        return self.definition.path

    @property
    def partition(self) -> FixturePartition:
        """Return the validator-owned partition assigned by the manifest."""

        return self.definition.partition

    @property
    def media_type(self) -> FixtureMediaType:
        """Return the declared content format."""

        return self.definition.media_type

    def decode_text(self) -> str:
        """Decode a declared text fixture as strict UTF-8."""

        if self.media_type not in _TEXT_MEDIA_TYPES:
            raise FixtureError(f"fixture is not a text media type: {self.path}")
        try:
            return self.content_bytes.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise FixtureError(f"fixture is not valid UTF-8: {self.path}") from exc

    def decode_json_object(self) -> dict[str, object]:
        """Decode a JSON fixture and return a fresh top-level object."""

        if self.media_type is not FixtureMediaType.JSON:
            raise FixtureError(f"fixture is not JSON: {self.path}")
        decoded = _decode_json_object(self.content_bytes, path=self.path)
        return dict(decoded)


@dataclass(frozen=True, slots=True)
class FixtureBundle:
    """Complete set of verified artifacts loaded for validator-controlled use."""

    manifest: FixtureManifest
    repository_root: Path
    artifacts: tuple[FixtureArtifact, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.manifest, FixtureManifest):
            raise FixtureError("manifest must be a FixtureManifest")
        if not isinstance(self.repository_root, Path):
            raise FixtureError("repository_root must be a Path")
        if not isinstance(self.artifacts, tuple) or not all(
            isinstance(artifact, FixtureArtifact) for artifact in self.artifacts
        ):
            raise FixtureError("artifacts must be a tuple of FixtureArtifact values")

        expected_paths = sorted(entry.path for entry in self.manifest.files)
        actual_paths = sorted(artifact.path for artifact in self.artifacts)
        if actual_paths != expected_paths:
            raise FixtureError("bundle artifacts do not match fixture manifest files")

    @property
    def fixture_set_sha256(self) -> str:
        """Return the calculated identity of the loaded fixture set."""

        return calculate_fixture_manifest_sha256(self.manifest)

    def by_partition(
        self,
        partition: FixturePartition,
    ) -> tuple[FixtureArtifact, ...]:
        """Return verified artifacts assigned to one validator-owned partition."""

        if not isinstance(partition, FixturePartition):
            raise FixtureError("partition must be a FixturePartition value")
        return tuple(artifact for artifact in self.artifacts if artifact.partition is partition)

    def artifact(self, relative_path: str) -> FixtureArtifact:
        """Return one verified artifact by exact manifest path."""

        _validate_fixture_path(relative_path)
        for artifact in self.artifacts:
            if artifact.path == relative_path:
                return artifact
        raise FixtureError(f"fixture artifact is not present: {relative_path}")


def calculate_fixture_manifest_sha256(manifest: FixtureManifest) -> str:
    """Calculate a deterministic hash of a fixture manifest payload."""

    payload = json.dumps(
        manifest.hash_payload(),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def create_fixture_file(
    repository_root: Path,
    relative_path: str,
    *,
    partition: FixturePartition,
    media_type: FixtureMediaType,
) -> FixtureFile:
    """Create a fixture definition from an existing controlled repository file."""

    root = _resolve_repository_root(repository_root)
    path = _resolve_fixture_path(root, relative_path, strict=True)
    if not path.is_file():
        raise FixtureError(f"fixture source is not a file: {relative_path}")
    content = _read_fixture_bytes(path, relative_path=relative_path)
    _validate_content(content, media_type=media_type, path=relative_path)
    return FixtureFile(
        path=PurePosixPath(relative_path).as_posix(),
        partition=partition,
        media_type=media_type,
        sha256=_sha256_bytes(content),
        size_bytes=len(content),
    )


def load_fixture_manifest(
    path: Path,
    *,
    require_hash: bool = True,
) -> FixtureManifest:
    """Load a UTF-8 JSON fixture manifest and verify its declared hash."""

    try:
        decoded = json.loads(
            path.read_text(encoding="utf-8"),
            parse_constant=_reject_non_finite_json,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise FixtureError(f"unable to load fixture manifest {path}: {exc}") from exc
    if not isinstance(decoded, Mapping):
        raise FixtureError("fixture manifest root must be a JSON object")

    manifest = FixtureManifest.from_mapping(decoded)
    _verify_fixture_manifest_hash(manifest, require_hash=require_hash)
    return manifest


def load_fixture_bundle(
    repository_root: Path,
    manifest: FixtureManifest,
    *,
    require_manifest_hash: bool = True,
) -> FixtureBundle:
    """Verify and load all manifest artifacts without mutating the repository."""

    _verify_fixture_manifest_hash(manifest, require_hash=require_manifest_hash)
    root = _resolve_repository_root(repository_root)
    artifacts: list[FixtureArtifact] = []
    for definition in sorted(manifest.files, key=lambda entry: entry.path):
        path = _resolve_fixture_path(root, definition.path, strict=True)
        if not path.is_file():
            raise FixtureError(f"fixture path is not a file: {definition.path}")
        content = _read_fixture_bytes(path, relative_path=definition.path)
        if len(content) != definition.size_bytes:
            raise FixtureError(f"fixture size mismatch: {definition.path}")
        if _sha256_bytes(content) != definition.sha256:
            raise FixtureError(f"fixture hash mismatch: {definition.path}")
        _validate_content(
            content,
            media_type=definition.media_type,
            path=definition.path,
        )
        artifacts.append(
            FixtureArtifact(
                definition=definition,
                resolved_path=path,
                content_bytes=content,
            )
        )

    return FixtureBundle(
        manifest=manifest,
        repository_root=root,
        artifacts=tuple(artifacts),
    )


def load_fixture_set(
    manifest_path: Path,
    repository_root: Path,
    *,
    require_hash: bool = True,
) -> FixtureBundle:
    """Load a manifest, verify its hash, and load its controlled artifacts."""

    manifest = load_fixture_manifest(manifest_path, require_hash=require_hash)
    return load_fixture_bundle(
        repository_root,
        manifest,
        require_manifest_hash=require_hash,
    )


def _verify_fixture_manifest_hash(
    manifest: FixtureManifest,
    *,
    require_hash: bool,
) -> None:
    calculated_hash = calculate_fixture_manifest_sha256(manifest)
    if manifest.fixture_manifest_sha256 is None:
        if require_hash:
            raise FixtureError("fixture_manifest_sha256 is required for executable fixtures")
    elif manifest.fixture_manifest_sha256 != calculated_hash:
        raise FixtureError("fixture_manifest_sha256 does not match the canonical manifest payload")


def _validate_content(
    content: bytes,
    *,
    media_type: FixtureMediaType,
    path: str,
) -> None:
    if not isinstance(media_type, FixtureMediaType):
        raise FixtureError("media_type must be a FixtureMediaType value")
    if media_type is FixtureMediaType.BINARY:
        return
    if media_type is FixtureMediaType.JSON:
        _decode_json_object(content, path=path)
        return
    try:
        content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise FixtureError(f"fixture is not valid UTF-8: {path}") from exc


def _decode_json_object(content: bytes, *, path: str) -> Mapping[str, object]:
    try:
        text = content.decode("utf-8")
        decoded = json.loads(text, parse_constant=_reject_non_finite_json)
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise FixtureError(f"fixture is not valid JSON: {path}: {exc}") from exc
    if not isinstance(decoded, Mapping):
        raise FixtureError(f"JSON fixture root must be an object: {path}")
    if not all(isinstance(key, str) for key in decoded):
        raise FixtureError(f"JSON fixture keys must be strings: {path}")
    return decoded


def _read_fixture_bytes(path: Path, *, relative_path: str) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        raise FixtureError(f"unable to read fixture {relative_path}: {exc}") from exc


def _resolve_repository_root(repository_root: Path) -> Path:
    try:
        root = repository_root.resolve(strict=True)
    except OSError as exc:
        raise FixtureError(f"repository root cannot be resolved: {repository_root}: {exc}") from exc
    if not root.is_dir():
        raise FixtureError(f"repository root is not a directory: {root}")
    return root


def _resolve_fixture_path(root: Path, relative_path: str, *, strict: bool) -> Path:
    _validate_fixture_path(relative_path)
    try:
        candidate = root.joinpath(*PurePosixPath(relative_path).parts).resolve(strict=strict)
    except OSError as exc:
        raise FixtureError(f"unable to resolve fixture path {relative_path}: {exc}") from exc
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise FixtureError(f"fixture path escapes repository root: {relative_path}") from exc
    return candidate


def _validate_fixture_path(path: str) -> None:
    _validate_relative_path(path, field="fixture path")
    required_root = PurePosixPath(FIXTURE_ROOT)
    candidate = PurePosixPath(path)
    if candidate.parts[: len(required_root.parts)] != required_root.parts:
        raise FixtureError(f"fixture path must be {FIXTURE_ROOT} or one of its descendants")
    if candidate == required_root:
        raise FixtureError("fixture path must identify a file below the fixture root")


def _validate_relative_path(path: str, *, field: str) -> None:
    if not isinstance(path, str):
        raise FixtureError(f"{field} must be a string")
    if not path or not path.strip():
        raise FixtureError(f"{field} must not be empty")
    if path != path.strip():
        raise FixtureError(f"{field} must not contain surrounding whitespace")
    if "\\" in path:
        raise FixtureError(f"{field} must use forward slashes")
    pure_path = PurePosixPath(path)
    if pure_path.is_absolute() or ".." in pure_path.parts:
        raise FixtureError(f"{field} must remain repository-relative")
    if pure_path.parts and ":" in pure_path.parts[0]:
        raise FixtureError(f"{field} must not contain a drive prefix")
    if pure_path.as_posix() != path or pure_path == PurePosixPath("."):
        raise FixtureError(f"{field} must use canonical repository-relative form")


def _validate_identifier(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise FixtureError(f"{field} must be a string")
    if _IDENTIFIER_PATTERN.fullmatch(value) is None:
        raise FixtureError(f"{field} must contain 3-128 uppercase identifier characters")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise FixtureError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise FixtureError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _validate_keys(
    data: Mapping[str, object],
    *,
    allowed: frozenset[str],
    required: frozenset[str],
    context: str,
) -> None:
    keys = set(data)
    unknown = sorted(keys - allowed)
    if unknown:
        raise FixtureError(f"unknown {context} field(s): {', '.join(unknown)}")
    missing = sorted(required - keys)
    if missing:
        raise FixtureError(f"missing {context} field(s): {', '.join(missing)}")


def _required_string(
    data: Mapping[str, object],
    key: str,
    *,
    context: str = "fixture manifest",
) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise FixtureError(f"{context}.{key} must be a non-empty string")
    return value


def _optional_string(data: Mapping[str, object], key: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise FixtureError(f"fixture manifest.{key} must be null or a non-empty string")
    return value


def _required_integer(
    data: Mapping[str, object],
    key: str,
    *,
    context: str,
) -> int:
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise FixtureError(f"{context}.{key} must be an integer")
    return value


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


def _sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


__all__ = [
    "CORE_FIXTURE_PARTITIONS",
    "FIXTURE_ROOT",
    "SUPPORTED_FIXTURE_MANIFEST_VERSION",
    "FixtureArtifact",
    "FixtureBundle",
    "FixtureError",
    "FixtureFile",
    "FixtureManifest",
    "FixtureMediaType",
    "FixturePartition",
    "calculate_fixture_manifest_sha256",
    "create_fixture_file",
    "load_fixture_bundle",
    "load_fixture_manifest",
    "load_fixture_set",
]
