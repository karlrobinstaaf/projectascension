"""Unit tests for frozen-baseline loading, hashing, and verification."""

from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

import pytest

from aurora_validation_harness.baseline import (
    BaselineManifest,
    BaselineState,
    BaselineVerificationResult,
    FileVerification,
    FileVerificationStatus,
    IssueEffect,
    ManifestError,
    ManifestFile,
    VerificationStatus,
    calculate_manifest_sha256,
    create_manifest_file,
    extract_markdown_version,
    load_manifest,
    normalize_markdown_text,
    sha256_bytes,
    sha256_normalized_markdown,
    verify_baseline,
)

pytestmark = pytest.mark.foundation

_DEFAULT_PATH = "Canon/Systems/Example.md"


def _markdown(version: str = "1.0", *, body: str = "Canonical content.") -> str:
    return f"# Example\n\n| Field | Value |\n|---|---|\n| Version | {version} |\n\n{body}\n"


def _write_markdown(
    repository_root: Path,
    *,
    relative_path: str = _DEFAULT_PATH,
    version: str = "1.0",
    body: str = "Canonical content.",
) -> Path:
    path = repository_root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_markdown(version, body=body), encoding="utf-8", newline="")
    return path


def _entry(
    repository_root: Path,
    *,
    relative_path: str = _DEFAULT_PATH,
    version: str | None = "1.0",
    verify_version: bool = True,
    required: bool = True,
) -> ManifestFile:
    return create_manifest_file(
        repository_root,
        relative_path,
        category="CANON_SYSTEM",
        version=version,
        verify_version=verify_version,
        required=required,
    )


def _signed_manifest(
    *files: ManifestFile,
    state: BaselineState = BaselineState.DOCUMENTATION_BASELINE_FROZEN,
) -> BaselineManifest:
    unsigned = BaselineManifest(
        baseline_id="AURORA-FOUNDATION-BASELINE-001",
        baseline_state=state,
        manifest_version="1.0",
        files=files,
    )
    return replace(unsigned, manifest_sha256=calculate_manifest_sha256(unsigned))


def _issue_codes(result: BaselineVerificationResult | FileVerification) -> set[str]:
    return {issue.code for issue in result.issues}


def test_normalize_markdown_text_canonicalizes_line_endings_unicode_and_eof() -> None:
    source = "Cafe\u0301\r\nSecond line\r\n\r\n"

    assert normalize_markdown_text(source) == "Café\nSecond line\n"


def test_normalized_hash_is_independent_of_supported_line_endings() -> None:
    lf_text = "# Record\n\nStable text.\n"
    crlf_text = lf_text.replace("\n", "\r\n")

    assert sha256_normalized_markdown(lf_text) == sha256_normalized_markdown(crlf_text)
    assert sha256_bytes(lf_text.encode()) != sha256_bytes(crlf_text.encode())


@pytest.mark.parametrize(
    ("metadata", "expected"),
    [
        ("| Version | 1.4 |", "1.4"),
        ("| Version | `2.0-draft` |", "2.0-draft"),
        ("| Status | Draft |", None),
    ],
)
def test_extract_markdown_version(metadata: str, expected: str | None) -> None:
    assert extract_markdown_version(metadata) == expected


def test_create_manifest_file_captures_raw_and_normalized_hashes(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    path = _write_markdown(repository_root)

    entry = _entry(repository_root)

    raw = path.read_bytes()
    assert entry.path == _DEFAULT_PATH
    assert entry.raw_sha256 == sha256_bytes(raw)
    assert entry.normalized_text_sha256 == sha256_normalized_markdown(raw.decode())
    assert entry.version == "1.0"


def test_create_manifest_file_omits_normalized_hash_for_binary_file(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    path = repository_root / "Fixtures/state.bin"
    path.parent.mkdir(parents=True)
    path.write_bytes(b"\x00\x01\x02")

    entry = create_manifest_file(
        repository_root,
        "Fixtures/state.bin",
        category="FIXTURE",
        version=None,
        verify_version=False,
    )

    assert entry.raw_sha256 == sha256_bytes(b"\x00\x01\x02")
    assert entry.normalized_text_sha256 is None
    assert entry.verify_version is False


def test_create_manifest_file_rejects_missing_source(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    repository_root.mkdir()

    with pytest.raises(ManifestError, match="manifest source is not a file"):
        _entry(repository_root)


def test_verify_baseline_accepts_active_frozen_manifest(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    _write_markdown(repository_root)
    manifest = _signed_manifest(_entry(repository_root))

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.VERIFIED
    assert result.verified is True
    assert result.issues == ()
    assert result.calculated_manifest_sha256 == result.declared_manifest_sha256
    assert len(result.files) == 1
    assert result.files[0].status is FileVerificationStatus.VERIFIED


def test_pre_freeze_manifest_is_blocked(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    _write_markdown(repository_root)
    manifest = _signed_manifest(
        _entry(repository_root),
        state=BaselineState.PRE_FREEZE,
    )

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.BLOCKED
    assert result.verified is False
    assert "BASELINE_NOT_ACTIVE" in _issue_codes(result)


def test_missing_manifest_hash_is_blocked(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    _write_markdown(repository_root)
    manifest = replace(_signed_manifest(_entry(repository_root)), manifest_sha256=None)

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.BLOCKED
    assert "MANIFEST_HASH_MISSING" in _issue_codes(result)


def test_incorrect_manifest_hash_is_invalid(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    _write_markdown(repository_root)
    manifest = replace(
        _signed_manifest(_entry(repository_root)),
        manifest_sha256="0" * 64,
    )

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.INVALID
    assert "MANIFEST_HASH_MISMATCH" in _issue_codes(result)


def test_modified_file_invalidates_frozen_baseline(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    path = _write_markdown(repository_root)
    manifest = _signed_manifest(_entry(repository_root))
    path.write_text(_markdown(body="Modified after freeze."), encoding="utf-8")

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.INVALID
    assert result.files[0].status is FileVerificationStatus.INVALID
    assert _issue_codes(result.files[0]) == {
        "NORMALIZED_HASH_MISMATCH",
        "RAW_HASH_MISMATCH",
    }


def test_required_missing_file_blocks_verification(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    path = _write_markdown(repository_root)
    manifest = _signed_manifest(_entry(repository_root))
    path.unlink()

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.BLOCKED
    assert result.files[0].status is FileVerificationStatus.MISSING
    assert result.files[0].issues[0].effect is IssueEffect.BLOCKED
    assert _issue_codes(result) == {"FILE_MISSING"}


def test_optional_missing_file_is_observed_without_blocking(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    path = _write_markdown(repository_root)
    manifest = _signed_manifest(_entry(repository_root, required=False))
    path.unlink()

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.VERIFIED
    assert result.files[0].status is FileVerificationStatus.MISSING
    assert result.files[0].issues[0].effect is IssueEffect.OBSERVATION
    assert _issue_codes(result) == {"FILE_MISSING"}


def test_version_mismatch_invalidates_file_even_when_hashes_match(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    _write_markdown(repository_root, version="1.1")
    entry = _entry(repository_root, version="1.0")
    manifest = _signed_manifest(entry)

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.INVALID
    assert result.files[0].actual_version == "1.1"
    assert _issue_codes(result.files[0]) == {"VERSION_MISMATCH"}


def test_missing_version_metadata_invalidates_file(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    path = repository_root / _DEFAULT_PATH
    path.parent.mkdir(parents=True)
    path.write_text("# Example\n\nNo metadata table.\n", encoding="utf-8")
    manifest = _signed_manifest(_entry(repository_root, version="1.0"))

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.INVALID
    assert result.files[0].actual_version is None
    assert _issue_codes(result.files[0]) == {"VERSION_MISSING"}


def test_invalid_utf8_text_is_reported_without_decoding_hashes(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    path = repository_root / _DEFAULT_PATH
    path.parent.mkdir(parents=True)
    raw = b"\xff\xfe\x00"
    path.write_bytes(raw)
    entry = ManifestFile(
        path=_DEFAULT_PATH,
        category="CANON_SYSTEM",
        raw_sha256=sha256_bytes(raw),
        normalized_text_sha256="0" * 64,
        version="1.0",
    )

    result = verify_baseline(repository_root, _signed_manifest(entry))

    assert result.status is VerificationStatus.INVALID
    assert result.files[0].actual_normalized_text_sha256 is None
    assert result.files[0].actual_version is None
    assert _issue_codes(result.files[0]) == {"INVALID_UTF8"}


def test_missing_repository_root_blocks_before_file_verification(tmp_path: Path) -> None:
    repository_root = tmp_path / "missing-repository"
    manifest = _signed_manifest()

    result = verify_baseline(repository_root, manifest)

    assert result.status is VerificationStatus.BLOCKED
    assert result.files == ()
    assert _issue_codes(result) == {"REPOSITORY_ROOT_UNAVAILABLE"}


def test_repository_root_that_is_a_file_is_blocked(tmp_path: Path) -> None:
    repository_root = tmp_path / "not-a-directory"
    repository_root.write_text("not a repository", encoding="utf-8")

    result = verify_baseline(repository_root, _signed_manifest())

    assert result.status is VerificationStatus.BLOCKED
    assert _issue_codes(result) == {"REPOSITORY_ROOT_NOT_DIRECTORY"}


@pytest.mark.parametrize(
    "unsafe_path",
    [
        "../outside.md",
        "/absolute.md",
        "Canon\\WindowsStyle.md",
        "C:/drive-prefixed.md",
    ],
)
def test_manifest_file_rejects_unsafe_paths(unsafe_path: str) -> None:
    with pytest.raises(ManifestError):
        ManifestFile(
            path=unsafe_path,
            category="CANON_SYSTEM",
            raw_sha256="0" * 64,
            version="1.0",
        )


def test_symlink_escape_is_invalidated_during_verification(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    controlled_directory = repository_root / "Canon"
    controlled_directory.mkdir(parents=True)
    outside = tmp_path / "outside.md"
    outside.write_text(_markdown(), encoding="utf-8")
    link = controlled_directory / "Escaped.md"
    try:
        link.symlink_to(outside)
    except OSError as exc:
        pytest.skip(f"symbolic links unavailable: {exc}")

    raw = outside.read_bytes()
    entry = ManifestFile(
        path="Canon/Escaped.md",
        category="CANON_SYSTEM",
        raw_sha256=sha256_bytes(raw),
        normalized_text_sha256=sha256_normalized_markdown(raw.decode()),
        version="1.0",
    )

    result = verify_baseline(repository_root, _signed_manifest(entry))

    assert result.status is VerificationStatus.INVALID
    assert _issue_codes(result.files[0]) == {"UNSAFE_MANIFEST_PATH"}


def test_manifest_rejects_duplicate_file_paths() -> None:
    entry = ManifestFile(
        path=_DEFAULT_PATH,
        category="CANON_SYSTEM",
        raw_sha256="0" * 64,
        version="1.0",
    )

    with pytest.raises(ManifestError, match="duplicate manifest paths"):
        BaselineManifest(
            baseline_id="AURORA-FOUNDATION-BASELINE-001",
            baseline_state=BaselineState.DOCUMENTATION_BASELINE_FROZEN,
            manifest_version="1.0",
            files=(entry, entry),
        )


def test_load_manifest_round_trip(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    _write_markdown(repository_root)
    expected = _signed_manifest(_entry(repository_root))
    manifest_path = tmp_path / "baseline-manifest.json"
    payload = expected.hash_payload() | {"manifest_sha256": expected.manifest_sha256}
    manifest_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    loaded = load_manifest(manifest_path)

    assert loaded == expected
    assert calculate_manifest_sha256(loaded) == loaded.manifest_sha256


@pytest.mark.parametrize("invalid_json", ["[]", "{broken json"])
def test_load_manifest_rejects_invalid_document(tmp_path: Path, invalid_json: str) -> None:
    manifest_path = tmp_path / "invalid-manifest.json"
    manifest_path.write_text(invalid_json, encoding="utf-8")

    with pytest.raises(ManifestError):
        load_manifest(manifest_path)
