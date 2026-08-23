"""Frozen-baseline models, hashing, loading, and verification.

This module implements the first harness capability (HC-1). It verifies that a
run targets a known, active documentation baseline and that every controlled
file still matches its declared path, version, and content hashes.
"""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import Final, Mapping

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_MARKDOWN_VERSION_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^\|\s*Version\s*\|\s*([^|]+?)\s*\|\s*$", re.MULTILINE
)
_ACTIVE_BASELINE_STATES: Final[frozenset[BaselineState]]


class ManifestError(ValueError):
    """Raised when a baseline manifest is structurally invalid."""


class BaselineState(StrEnum):
    """Lifecycle state declared by the Foundation Freeze Record."""

    PRE_FREEZE = "PRE_FREEZE"
    DOCUMENTATION_BASELINE_FROZEN = "DOCUMENTATION_BASELINE_FROZEN"
    EXECUTION_BASELINE_READY = "EXECUTION_BASELINE_READY"
    FORMAL_EXECUTION_ACTIVE = "FORMAL_EXECUTION_ACTIVE"
    SUPERSEDED = "SUPERSEDED"


_ACTIVE_BASELINE_STATES = frozenset(
    {
        BaselineState.DOCUMENTATION_BASELINE_FROZEN,
        BaselineState.EXECUTION_BASELINE_READY,
        BaselineState.FORMAL_EXECUTION_ACTIVE,
    }
)


class VerificationStatus(StrEnum):
    """Overall baseline-verification result."""

    VERIFIED = "VERIFIED"
    BLOCKED = "BLOCKED"
    INVALID = "INVALID"


class FileVerificationStatus(StrEnum):
    """Verification result for one controlled file."""

    VERIFIED = "VERIFIED"
    MISSING = "MISSING"
    INVALID = "INVALID"


class IssueEffect(StrEnum):
    """How a verification issue affects the overall result."""

    OBSERVATION = "OBSERVATION"
    BLOCKED = "BLOCKED"
    INVALID = "INVALID"


@dataclass(frozen=True, slots=True)
class BaselineIssue:
    """One baseline-verification observation or failure."""

    code: str
    effect: IssueEffect
    message: str
    path: str | None = None


@dataclass(frozen=True, slots=True)
class ManifestFile:
    """Expected identity of one file in a frozen baseline."""

    path: str
    category: str
    raw_sha256: str
    normalized_text_sha256: str | None = None
    version: str | None = None
    verify_version: bool = True
    required: bool = True

    def __post_init__(self) -> None:
        _validate_relative_manifest_path(self.path)
        _validate_sha256(self.raw_sha256, field="raw_sha256")
        if self.normalized_text_sha256 is not None:
            _validate_sha256(
                self.normalized_text_sha256,
                field="normalized_text_sha256",
            )
        if self.verify_version and self.version is None:
            raise ManifestError("version is required when verify_version is true")

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> ManifestFile:
        """Create a manifest file from decoded JSON data."""

        return cls(
            path=_required_string(data, "path"),
            category=_required_string(data, "category"),
            raw_sha256=_required_string(data, "raw_sha256"),
            normalized_text_sha256=_optional_string(data, "normalized_text_sha256"),
            version=_optional_string(data, "version"),
            verify_version=_optional_boolean(data, "verify_version", default=True),
            required=_optional_boolean(data, "required", default=True),
        )

    def to_mapping(self) -> dict[str, object]:
        """Return the stable JSON representation used for manifest hashing."""

        return {
            "category": self.category,
            "normalized_text_sha256": self.normalized_text_sha256,
            "path": self.path,
            "raw_sha256": self.raw_sha256,
            "required": self.required,
            "verify_version": self.verify_version,
            "version": self.version,
        }


@dataclass(frozen=True, slots=True)
class BaselineManifest:
    """Machine-readable representation of a Foundation freeze manifest."""

    baseline_id: str
    baseline_state: BaselineState
    manifest_version: str
    files: tuple[ManifestFile, ...]
    manifest_sha256: str | None = None

    def __post_init__(self) -> None:
        if not self.baseline_id.strip():
            raise ManifestError("baseline_id must not be empty")
        if not self.manifest_version.strip():
            raise ManifestError("manifest_version must not be empty")
        paths = [entry.path for entry in self.files]
        duplicates = sorted({path for path in paths if paths.count(path) > 1})
        if duplicates:
            raise ManifestError(f"duplicate manifest paths: {', '.join(duplicates)}")
        if self.manifest_sha256 is not None:
            _validate_sha256(self.manifest_sha256, field="manifest_sha256")

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> BaselineManifest:
        """Create a baseline manifest from decoded JSON data."""

        raw_files = data.get("files")
        if not isinstance(raw_files, list):
            raise ManifestError("files must be a JSON array")

        files: list[ManifestFile] = []
        for index, item in enumerate(raw_files):
            if not isinstance(item, Mapping):
                raise ManifestError(f"files[{index}] must be a JSON object")
            files.append(ManifestFile.from_mapping(item))

        raw_state = _required_string(data, "baseline_state")
        try:
            state = BaselineState(raw_state)
        except ValueError as exc:
            raise ManifestError(f"unsupported baseline_state: {raw_state}") from exc

        return cls(
            baseline_id=_required_string(data, "baseline_id"),
            baseline_state=state,
            manifest_version=_required_string(data, "manifest_version"),
            files=tuple(files),
            manifest_sha256=_optional_string(data, "manifest_sha256"),
        )

    def hash_payload(self) -> dict[str, object]:
        """Return the canonical payload used to calculate the manifest hash."""

        ordered_files = sorted(self.files, key=lambda entry: entry.path)
        return {
            "baseline_id": self.baseline_id,
            "baseline_state": self.baseline_state.value,
            "files": [entry.to_mapping() for entry in ordered_files],
            "manifest_version": self.manifest_version,
        }


@dataclass(frozen=True, slots=True)
class FileVerification:
    """Observed identity and result for one manifest file."""

    path: str
    status: FileVerificationStatus
    expected_raw_sha256: str
    actual_raw_sha256: str | None
    expected_normalized_text_sha256: str | None
    actual_normalized_text_sha256: str | None
    expected_version: str | None
    actual_version: str | None
    issues: tuple[BaselineIssue, ...]


@dataclass(frozen=True, slots=True)
class BaselineVerificationResult:
    """Complete result of verifying one baseline against a repository."""

    baseline_id: str
    status: VerificationStatus
    baseline_state: BaselineState
    calculated_manifest_sha256: str
    declared_manifest_sha256: str | None
    files: tuple[FileVerification, ...]
    issues: tuple[BaselineIssue, ...]

    @property
    def verified(self) -> bool:
        """Return true only when the complete baseline is verified."""

        return self.status is VerificationStatus.VERIFIED


def normalize_markdown_text(text: str) -> str:
    """Apply the canonical Markdown normalization defined by the Freeze Record."""

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = unicodedata.normalize("NFC", normalized)
    return normalized.rstrip("\n") + "\n"


def sha256_bytes(content: bytes) -> str:
    """Return the lowercase SHA-256 digest for exact bytes."""

    return hashlib.sha256(content).hexdigest()


def sha256_normalized_markdown(text: str) -> str:
    """Return the SHA-256 digest for canonically normalized Markdown."""

    return sha256_bytes(normalize_markdown_text(text).encode("utf-8"))


def calculate_manifest_sha256(manifest: BaselineManifest) -> str:
    """Calculate a deterministic hash without recursively hashing the hash field."""

    payload = json.dumps(
        manifest.hash_payload(),
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return sha256_bytes(payload)


def extract_markdown_version(text: str) -> str | None:
    """Extract the top-level Field/Value metadata version from Markdown."""

    match = _MARKDOWN_VERSION_PATTERN.search(text)
    if match is None:
        return None
    return match.group(1).strip().strip("`")


def load_manifest(path: Path) -> BaselineManifest:
    """Load and validate a UTF-8 JSON baseline manifest."""

    try:
        decoded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ManifestError(f"unable to load manifest {path}: {exc}") from exc
    if not isinstance(decoded, Mapping):
        raise ManifestError("manifest root must be a JSON object")
    return BaselineManifest.from_mapping(decoded)


def create_manifest_file(
    repository_root: Path,
    relative_path: str,
    *,
    category: str,
    version: str | None,
    verify_version: bool = True,
    required: bool = True,
) -> ManifestFile:
    """Create a manifest entry from a repository file after safe path resolution."""

    resolved = _resolve_repository_path(repository_root, relative_path)
    if not resolved.is_file():
        raise ManifestError(f"manifest source is not a file: {relative_path}")
    try:
        raw = resolved.read_bytes()
    except OSError as exc:
        raise ManifestError(f"unable to read {relative_path}: {exc}") from exc

    normalized_hash: str | None = None
    if resolved.suffix.casefold() == ".md":
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ManifestError(f"Markdown is not valid UTF-8: {relative_path}") from exc
        normalized_hash = sha256_normalized_markdown(text)

    return ManifestFile(
        path=PurePosixPath(relative_path).as_posix(),
        category=category,
        raw_sha256=sha256_bytes(raw),
        normalized_text_sha256=normalized_hash,
        version=version,
        verify_version=verify_version,
        required=required,
    )


def verify_baseline(
    repository_root: Path,
    manifest: BaselineManifest,
) -> BaselineVerificationResult:
    """Verify a baseline manifest against repository files without mutating them."""

    issues: list[BaselineIssue] = []
    file_results: list[FileVerification] = []

    try:
        root = repository_root.resolve(strict=True)
    except OSError as exc:
        issue = BaselineIssue(
            code="REPOSITORY_ROOT_UNAVAILABLE",
            effect=IssueEffect.BLOCKED,
            message=f"repository root cannot be resolved: {exc}",
            path=str(repository_root),
        )
        return BaselineVerificationResult(
            baseline_id=manifest.baseline_id,
            status=VerificationStatus.BLOCKED,
            baseline_state=manifest.baseline_state,
            calculated_manifest_sha256=calculate_manifest_sha256(manifest),
            declared_manifest_sha256=manifest.manifest_sha256,
            files=(),
            issues=(issue,),
        )

    if not root.is_dir():
        issues.append(
            BaselineIssue(
                code="REPOSITORY_ROOT_NOT_DIRECTORY",
                effect=IssueEffect.BLOCKED,
                message="repository root is not a directory",
                path=str(root),
            )
        )

    if manifest.baseline_state not in _ACTIVE_BASELINE_STATES:
        issues.append(
            BaselineIssue(
                code="BASELINE_NOT_ACTIVE",
                effect=IssueEffect.BLOCKED,
                message=f"baseline state is {manifest.baseline_state.value}",
            )
        )

    calculated_manifest_hash = calculate_manifest_sha256(manifest)
    if manifest.manifest_sha256 is None:
        issues.append(
            BaselineIssue(
                code="MANIFEST_HASH_MISSING",
                effect=IssueEffect.BLOCKED,
                message="manifest_sha256 is required for a verified baseline",
            )
        )
    elif manifest.manifest_sha256 != calculated_manifest_hash:
        issues.append(
            BaselineIssue(
                code="MANIFEST_HASH_MISMATCH",
                effect=IssueEffect.INVALID,
                message="declared manifest hash does not match canonical manifest payload",
            )
        )

    for entry in manifest.files:
        file_result = _verify_manifest_file(root, entry)
        file_results.append(file_result)
        issues.extend(file_result.issues)

    status = _overall_status(issues)
    return BaselineVerificationResult(
        baseline_id=manifest.baseline_id,
        status=status,
        baseline_state=manifest.baseline_state,
        calculated_manifest_sha256=calculated_manifest_hash,
        declared_manifest_sha256=manifest.manifest_sha256,
        files=tuple(file_results),
        issues=tuple(issues),
    )


def _verify_manifest_file(root: Path, entry: ManifestFile) -> FileVerification:
    issues: list[BaselineIssue] = []
    try:
        path = _resolve_repository_path(root, entry.path)
    except ManifestError as exc:
        issue = BaselineIssue(
            code="UNSAFE_MANIFEST_PATH",
            effect=IssueEffect.INVALID,
            message=str(exc),
            path=entry.path,
        )
        return _file_result(entry, FileVerificationStatus.INVALID, (issue,))

    if not path.is_file():
        effect = IssueEffect.BLOCKED if entry.required else IssueEffect.OBSERVATION
        issue = BaselineIssue(
            code="FILE_MISSING",
            effect=effect,
            message=(
                "required baseline file is missing"
                if entry.required
                else "optional file is missing"
            ),
            path=entry.path,
        )
        return _file_result(entry, FileVerificationStatus.MISSING, (issue,))

    try:
        raw = path.read_bytes()
    except OSError as exc:
        issue = BaselineIssue(
            code="FILE_READ_FAILED",
            effect=IssueEffect.BLOCKED,
            message=f"unable to read baseline file: {exc}",
            path=entry.path,
        )
        return _file_result(entry, FileVerificationStatus.INVALID, (issue,))

    actual_raw_hash = sha256_bytes(raw)
    if actual_raw_hash != entry.raw_sha256:
        issues.append(
            BaselineIssue(
                code="RAW_HASH_MISMATCH",
                effect=IssueEffect.INVALID,
                message="file bytes differ from the frozen baseline",
                path=entry.path,
            )
        )

    text: str | None = None
    actual_normalized_hash: str | None = None
    if entry.normalized_text_sha256 is not None or entry.verify_version:
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            issues.append(
                BaselineIssue(
                    code="INVALID_UTF8",
                    effect=IssueEffect.INVALID,
                    message="text baseline file is not valid UTF-8",
                    path=entry.path,
                )
            )

    if entry.normalized_text_sha256 is not None and text is not None:
        actual_normalized_hash = sha256_normalized_markdown(text)
        if actual_normalized_hash != entry.normalized_text_sha256:
            issues.append(
                BaselineIssue(
                    code="NORMALIZED_HASH_MISMATCH",
                    effect=IssueEffect.INVALID,
                    message="normalized text differs from the frozen baseline",
                    path=entry.path,
                )
            )

    actual_version: str | None = None
    if entry.verify_version and text is not None:
        actual_version = extract_markdown_version(text)
        if actual_version is None:
            issues.append(
                BaselineIssue(
                    code="VERSION_MISSING",
                    effect=IssueEffect.INVALID,
                    message="Markdown Field/Value metadata does not contain Version",
                    path=entry.path,
                )
            )
        elif actual_version != entry.version:
            issues.append(
                BaselineIssue(
                    code="VERSION_MISMATCH",
                    effect=IssueEffect.INVALID,
                    message=f"expected version {entry.version}, found {actual_version}",
                    path=entry.path,
                )
            )

    status = (
        FileVerificationStatus.VERIFIED
        if not any(issue.effect is IssueEffect.INVALID for issue in issues)
        else FileVerificationStatus.INVALID
    )
    return FileVerification(
        path=entry.path,
        status=status,
        expected_raw_sha256=entry.raw_sha256,
        actual_raw_sha256=actual_raw_hash,
        expected_normalized_text_sha256=entry.normalized_text_sha256,
        actual_normalized_text_sha256=actual_normalized_hash,
        expected_version=entry.version,
        actual_version=actual_version,
        issues=tuple(issues),
    )


def _file_result(
    entry: ManifestFile,
    status: FileVerificationStatus,
    issues: tuple[BaselineIssue, ...],
) -> FileVerification:
    return FileVerification(
        path=entry.path,
        status=status,
        expected_raw_sha256=entry.raw_sha256,
        actual_raw_sha256=None,
        expected_normalized_text_sha256=entry.normalized_text_sha256,
        actual_normalized_text_sha256=None,
        expected_version=entry.version,
        actual_version=None,
        issues=issues,
    )


def _overall_status(issues: list[BaselineIssue]) -> VerificationStatus:
    if any(issue.effect is IssueEffect.INVALID for issue in issues):
        return VerificationStatus.INVALID
    if any(issue.effect is IssueEffect.BLOCKED for issue in issues):
        return VerificationStatus.BLOCKED
    return VerificationStatus.VERIFIED


def _resolve_repository_path(repository_root: Path, relative_path: str) -> Path:
    _validate_relative_manifest_path(relative_path)
    try:
        root = repository_root.resolve(strict=True)
    except OSError as exc:
        raise ManifestError(f"repository root cannot be resolved: {exc}") from exc
    pure_path = PurePosixPath(relative_path)
    candidate = root.joinpath(*pure_path.parts).resolve(strict=False)
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ManifestError(f"path escapes repository root: {relative_path}") from exc
    return candidate


def _validate_relative_manifest_path(path: str) -> None:
    if not path or not path.strip():
        raise ManifestError("manifest path must not be empty")
    if "\\" in path:
        raise ManifestError(f"manifest path must use forward slashes: {path}")
    pure_path = PurePosixPath(path)
    if pure_path.is_absolute() or ".." in pure_path.parts:
        raise ManifestError(f"manifest path must remain repository-relative: {path}")
    if pure_path.parts and ":" in pure_path.parts[0]:
        raise ManifestError(f"manifest path must not contain a drive prefix: {path}")


def _validate_sha256(value: str, *, field: str) -> None:
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise ManifestError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _required_string(data: Mapping[str, object], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{key} must be a non-empty string")
    return value


def _optional_string(data: Mapping[str, object], key: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{key} must be null or a non-empty string")
    return value


def _optional_boolean(data: Mapping[str, object], key: str, *, default: bool) -> bool:
    value = data.get(key, default)
    if not isinstance(value, bool):
        raise ManifestError(f"{key} must be a boolean")
    return value


__all__ = [
    "BaselineIssue",
    "BaselineManifest",
    "BaselineState",
    "BaselineVerificationResult",
    "FileVerification",
    "FileVerificationStatus",
    "IssueEffect",
    "ManifestError",
    "ManifestFile",
    "VerificationStatus",
    "calculate_manifest_sha256",
    "create_manifest_file",
    "extract_markdown_version",
    "load_manifest",
    "normalize_markdown_text",
    "sha256_bytes",
    "sha256_normalized_markdown",
    "verify_baseline",
]
