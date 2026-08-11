"""Unit tests for fixture manifests, integrity checks, and artifact loading."""

from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path

import pytest

from aurora_validation_harness import fixtures as fixtures_module
from aurora_validation_harness.fixtures import (
    CORE_FIXTURE_PARTITIONS,
    FIXTURE_ROOT,
    SUPPORTED_FIXTURE_MANIFEST_VERSION,
    FixtureArtifact,
    FixtureError,
    FixtureFile,
    FixtureManifest,
    FixtureMediaType,
    FixturePartition,
    calculate_fixture_manifest_sha256,
    create_fixture_file,
    load_fixture_bundle,
    load_fixture_manifest,
    load_fixture_set,
)

pytestmark = pytest.mark.foundation

_SCENARIO_DIRECTORY = f"{FIXTURE_ROOT}/FOUND-001"
_MANIFEST_PATH = f"{_SCENARIO_DIRECTORY}/fixture-manifest.json"
_PARTITION_NAMES: dict[FixturePartition, str] = {
    FixturePartition.WORLD: "world.json",
    FixturePartition.AURORA: "aurora.json",
    FixturePartition.PLAYER_PRIVATE: "player-private.json",
    FixturePartition.FUTURE: "future.json",
    FixturePartition.VALIDATOR: "validator.json",
}
_PARTITION_CONTENT: dict[FixturePartition, dict[str, object]] = {
    FixturePartition.WORLD: {"hidden_location": "Cargo_Bay_7"},
    FixturePartition.AURORA: {"current_location": "UNKNOWN"},
    FixturePartition.PLAYER_PRIVATE: {"knows_hidden_location": True},
    FixturePartition.FUTURE: {"queued_events": []},
    FixturePartition.VALIDATOR: {"expected_answer": "UNKNOWN"},
}


def _relative_path(filename: str) -> str:
    return f"{_SCENARIO_DIRECTORY}/{filename}"


def _write_bytes(repository_root: Path, relative_path: str, content: bytes) -> Path:
    path = repository_root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n").encode()


def _create_repository(tmp_path: Path, *, include_expected: bool = True) -> Path:
    repository_root = tmp_path / "repository"
    for partition, filename in _PARTITION_NAMES.items():
        _write_bytes(
            repository_root,
            _relative_path(filename),
            _json_bytes(_PARTITION_CONTENT[partition]),
        )
    if include_expected:
        _write_bytes(
            repository_root,
            _relative_path("expected.md"),
            b"# Expected result\n\nAurora remains uncertain.\n",
        )
    return repository_root


def _create_definitions(
    repository_root: Path,
    *,
    include_expected: bool = True,
) -> tuple[FixtureFile, ...]:
    definitions = [
        create_fixture_file(
            repository_root,
            _relative_path(filename),
            partition=partition,
            media_type=FixtureMediaType.JSON,
        )
        for partition, filename in _PARTITION_NAMES.items()
    ]
    if include_expected:
        definitions.append(
            create_fixture_file(
                repository_root,
                _relative_path("expected.md"),
                partition=FixturePartition.EXPECTED_RESULTS,
                media_type=FixtureMediaType.MARKDOWN,
            )
        )
    return tuple(definitions)


def _manifest(
    repository_root: Path,
    *,
    signed: bool = True,
    include_expected: bool = True,
) -> FixtureManifest:
    unsigned = FixtureManifest(
        fixture_set_id="AURORA-FIXTURE-FOUND-001-A",
        scenario_id="AURORA-SCN-FOUND-001",
        fixture_manifest_version=SUPPORTED_FIXTURE_MANIFEST_VERSION,
        files=_create_definitions(
            repository_root,
            include_expected=include_expected,
        ),
    )
    if not signed:
        return unsigned
    return replace(
        unsigned,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(unsigned),
    )


def _write_manifest(repository_root: Path, manifest: FixtureManifest) -> Path:
    path = repository_root / _MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(manifest.to_mapping(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def _definition(
    content: bytes,
    *,
    filename: str = "artifact.json",
    partition: FixturePartition = FixturePartition.WORLD,
    media_type: FixtureMediaType = FixtureMediaType.JSON,
) -> FixtureFile:
    return FixtureFile(
        path=_relative_path(filename),
        partition=partition,
        media_type=media_type,
        sha256=hashlib.sha256(content).hexdigest(),
        size_bytes=len(content),
    )


def _artifact(
    content: bytes,
    *,
    filename: str = "artifact.json",
    partition: FixturePartition = FixturePartition.WORLD,
    media_type: FixtureMediaType = FixtureMediaType.JSON,
) -> FixtureArtifact:
    definition = _definition(
        content,
        filename=filename,
        partition=partition,
        media_type=media_type,
    )
    return FixtureArtifact(
        definition=definition,
        resolved_path=Path("/verified") / filename,
        content_bytes=content,
    )


def test_core_partition_set_matches_isolation_contract() -> None:
    assert {
        FixturePartition.WORLD,
        FixturePartition.AURORA,
        FixturePartition.PLAYER_PRIVATE,
        FixturePartition.FUTURE,
        FixturePartition.VALIDATOR,
    } == CORE_FIXTURE_PARTITIONS
    assert FixturePartition.EXPECTED_RESULTS not in CORE_FIXTURE_PARTITIONS


def test_create_fixture_file_captures_exact_identity(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    relative_path = _relative_path("world.json")
    source = repository_root / relative_path

    definition = create_fixture_file(
        repository_root,
        relative_path,
        partition=FixturePartition.WORLD,
        media_type=FixtureMediaType.JSON,
    )

    content = source.read_bytes()
    assert definition.path == relative_path
    assert definition.partition is FixturePartition.WORLD
    assert definition.media_type is FixtureMediaType.JSON
    assert definition.sha256 == hashlib.sha256(content).hexdigest()
    assert definition.size_bytes == len(content)


@pytest.mark.parametrize(
    ("filename", "media_type", "content"),
    [
        ("state.json", FixtureMediaType.JSON, b'{"state":"ready"}\n'),
        ("notes.txt", FixtureMediaType.TEXT, "Väntar.\n".encode()),
        ("record.md", FixtureMediaType.MARKDOWN, b"# Record\n"),
        ("state.bin", FixtureMediaType.BINARY, b"\xff\x00\x81"),
    ],
)
def test_create_fixture_file_accepts_supported_media_types(
    tmp_path: Path,
    filename: str,
    media_type: FixtureMediaType,
    content: bytes,
) -> None:
    repository_root = tmp_path / "repository"
    relative_path = _relative_path(filename)
    _write_bytes(repository_root, relative_path, content)

    definition = create_fixture_file(
        repository_root,
        relative_path,
        partition=FixturePartition.WORLD,
        media_type=media_type,
    )

    assert definition.media_type is media_type
    assert definition.size_bytes == len(content)


def test_fixture_file_round_trips_through_mapping() -> None:
    original = _definition(b'{"value":1}\n')

    reconstructed = FixtureFile.from_mapping(original.to_mapping())

    assert reconstructed == original


@pytest.mark.parametrize("partition", ["PUBLIC", "world", ""])
def test_fixture_file_rejects_unsupported_partition(partition: str) -> None:
    mapping = _definition(b"{}").to_mapping()
    mapping["partition"] = partition

    with pytest.raises(
        FixtureError,
        match=r"unsupported fixture partition|partition must be a non-empty string",
    ):
        FixtureFile.from_mapping(mapping)


@pytest.mark.parametrize("media_type", ["text/csv", "APPLICATION/JSON", ""])
def test_fixture_file_rejects_unsupported_media_type(media_type: str) -> None:
    mapping = _definition(b"{}").to_mapping()
    mapping["media_type"] = media_type

    with pytest.raises(
        FixtureError,
        match=r"unsupported fixture media_type|media_type must be a non-empty string",
    ):
        FixtureFile.from_mapping(mapping)


def test_fixture_file_rejects_unknown_field() -> None:
    mapping = _definition(b"{}").to_mapping()
    mapping["canary"] = "hidden"

    with pytest.raises(FixtureError, match="unknown fixture file field"):
        FixtureFile.from_mapping(mapping)


def test_fixture_file_rejects_missing_field() -> None:
    mapping = _definition(b"{}").to_mapping()
    del mapping["sha256"]

    with pytest.raises(FixtureError, match="missing fixture file field"):
        FixtureFile.from_mapping(mapping)


@pytest.mark.parametrize("invalid_value", [None, "", "   ", 42])
def test_fixture_file_rejects_invalid_required_string(invalid_value: object) -> None:
    mapping = _definition(b"{}").to_mapping()
    mapping["path"] = invalid_value

    with pytest.raises(FixtureError, match=r"fixture file\.path"):
        FixtureFile.from_mapping(mapping)


@pytest.mark.parametrize("size_bytes", [True, "2", 2.5, None])
def test_fixture_file_rejects_non_integer_size(size_bytes: object) -> None:
    mapping = _definition(b"{}").to_mapping()
    mapping["size_bytes"] = size_bytes

    with pytest.raises(FixtureError, match=r"fixture file\.size_bytes must be an integer"):
        FixtureFile.from_mapping(mapping)


def test_fixture_file_rejects_negative_size() -> None:
    with pytest.raises(FixtureError, match="size_bytes must not be negative"):
        replace(_definition(b"{}"), size_bytes=-1)


@pytest.mark.parametrize("invalid_hash", ["0" * 63, "A" * 64, "not-a-hash"])
def test_fixture_file_rejects_malformed_hash(invalid_hash: str) -> None:
    with pytest.raises(FixtureError, match="lowercase 64-character SHA-256"):
        replace(_definition(b"{}"), sha256=invalid_hash)


@pytest.mark.parametrize(
    "invalid_path",
    [
        "",
        "   ",
        f" {_SCENARIO_DIRECTORY}/state.json",
        f"{_SCENARIO_DIRECTORY}/state.json ",
        "../outside.json",
        "/absolute.json",
        "C:/drive.json",
        f"{FIXTURE_ROOT}\\state.json",
        f"{FIXTURE_ROOT}//state.json",
        f"{FIXTURE_ROOT}/./state.json",
        ".",
        FIXTURE_ROOT,
        "Canon/fixture.json",
        f"{FIXTURE_ROOT}Archive/state.json",
    ],
)
def test_fixture_file_rejects_unsafe_or_ungoverned_path(invalid_path: str) -> None:
    with pytest.raises(FixtureError):
        replace(_definition(b"{}"), path=invalid_path)


def test_fixture_file_direct_constructor_checks_runtime_types() -> None:
    valid = _definition(b"{}")

    with pytest.raises(FixtureError, match="partition must be a FixturePartition"):
        replace(valid, partition="WORLD")
    with pytest.raises(FixtureError, match="media_type must be a FixtureMediaType"):
        replace(valid, media_type="application/json")
    with pytest.raises(FixtureError, match="fixture path must be a string"):
        replace(valid, path=1)
    with pytest.raises(FixtureError, match="sha256 must be a string"):
        replace(valid, sha256=1)
    with pytest.raises(FixtureError, match="size_bytes must be an integer"):
        replace(valid, size_bytes=True)


def test_manifest_canonicalizes_file_order_and_round_trips(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    original = _manifest(repository_root, signed=False)
    reversed_mapping = original.to_mapping()
    raw_files = reversed_mapping["files"]
    assert isinstance(raw_files, list)
    reversed_mapping["files"] = list(reversed(raw_files))

    reconstructed = FixtureManifest.from_mapping(reversed_mapping)

    assert reconstructed == original
    assert [entry.path for entry in reconstructed.files] == sorted(
        entry.path for entry in reconstructed.files
    )


def test_manifest_hash_is_stable_and_excludes_declared_hash(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    unsigned = _manifest(repository_root, signed=False)
    calculated = calculate_fixture_manifest_sha256(unsigned)
    signed = replace(unsigned, fixture_manifest_sha256=calculated)

    assert len(calculated) == 64
    assert calculate_fixture_manifest_sha256(signed) == calculated


def test_manifest_hash_changes_with_fixture_identity(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    original = _manifest(repository_root, signed=False)
    first = original.files[0]
    changed_file = replace(first, sha256="0" * 64)
    changed = replace(original, files=(changed_file, *original.files[1:]))

    assert calculate_fixture_manifest_sha256(original) != calculate_fixture_manifest_sha256(changed)


@pytest.mark.parametrize("missing_partition", sorted(CORE_FIXTURE_PARTITIONS))
def test_manifest_requires_every_core_partition(
    tmp_path: Path,
    missing_partition: FixturePartition,
) -> None:
    repository_root = _create_repository(tmp_path)
    files = tuple(
        entry
        for entry in _create_definitions(repository_root)
        if entry.partition is not missing_partition
    )

    with pytest.raises(FixtureError, match="missing core fixture partition"):
        FixtureManifest(
            fixture_set_id="AURORA-FIXTURE-FOUND-001-A",
            scenario_id="AURORA-SCN-FOUND-001",
            fixture_manifest_version=SUPPORTED_FIXTURE_MANIFEST_VERSION,
            files=files,
        )


def test_manifest_does_not_require_expected_results_partition(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path, include_expected=False)

    manifest = _manifest(
        repository_root,
        signed=False,
        include_expected=False,
    )

    assert {entry.partition for entry in manifest.files} == CORE_FIXTURE_PARTITIONS


def test_manifest_rejects_duplicate_paths(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    files = _create_definitions(repository_root)

    with pytest.raises(FixtureError, match="duplicate fixture paths"):
        FixtureManifest(
            fixture_set_id="AURORA-FIXTURE-FOUND-001-A",
            scenario_id="AURORA-SCN-FOUND-001",
            fixture_manifest_version=SUPPORTED_FIXTURE_MANIFEST_VERSION,
            files=(*files, files[0]),
        )


@pytest.mark.parametrize("fixture_set_id", ["ab", "lowercase", "BAD ID"])
def test_manifest_rejects_invalid_fixture_set_identifier(
    tmp_path: Path,
    fixture_set_id: str,
) -> None:
    repository_root = _create_repository(tmp_path)

    with pytest.raises(FixtureError, match="uppercase identifier characters"):
        replace(
            _manifest(repository_root, signed=False),
            fixture_set_id=fixture_set_id,
        )


@pytest.mark.parametrize(
    "scenario_id",
    ["AURORA-FOUND-001", "AURORA-SCN-FOUND-01", "aurora-scn-found-001"],
)
def test_manifest_rejects_noncanonical_scenario_id(
    tmp_path: Path,
    scenario_id: str,
) -> None:
    repository_root = _create_repository(tmp_path)

    with pytest.raises(FixtureError, match="scenario_id must match"):
        replace(_manifest(repository_root, signed=False), scenario_id=scenario_id)


def test_manifest_rejects_unsupported_version(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)

    with pytest.raises(FixtureError, match="unsupported fixture_manifest_version"):
        replace(_manifest(repository_root, signed=False), fixture_manifest_version="2.0")


def test_manifest_direct_constructor_checks_runtime_types(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    valid = _manifest(repository_root, signed=False)

    with pytest.raises(FixtureError, match="fixture_set_id must be a string"):
        replace(valid, fixture_set_id=1)
    with pytest.raises(FixtureError, match="scenario_id must be a string"):
        replace(valid, scenario_id=1)
    with pytest.raises(FixtureError, match="fixture_manifest_version must be a string"):
        replace(valid, fixture_manifest_version=1)
    with pytest.raises(FixtureError, match="files must be a tuple"):
        replace(valid, files=[])
    with pytest.raises(FixtureError, match="files must contain only FixtureFile"):
        replace(valid, files=(object(),))
    with pytest.raises(FixtureError, match="fixture_manifest_sha256 must be a string"):
        replace(valid, fixture_manifest_sha256=1)


def test_manifest_from_mapping_rejects_unknown_field(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    mapping = _manifest(repository_root, signed=False).to_mapping()
    mapping["validator_note"] = "hidden"

    with pytest.raises(FixtureError, match="unknown fixture manifest field"):
        FixtureManifest.from_mapping(mapping)


def test_manifest_from_mapping_rejects_missing_field(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    mapping = _manifest(repository_root, signed=False).to_mapping()
    del mapping["scenario_id"]

    with pytest.raises(FixtureError, match="missing fixture manifest field"):
        FixtureManifest.from_mapping(mapping)


@pytest.mark.parametrize("files", [None, {}, "files"])
def test_manifest_from_mapping_rejects_non_array_files(
    tmp_path: Path,
    files: object,
) -> None:
    repository_root = _create_repository(tmp_path)
    mapping = _manifest(repository_root, signed=False).to_mapping()
    mapping["files"] = files

    with pytest.raises(FixtureError, match=r"manifest\.files must be a JSON array"):
        FixtureManifest.from_mapping(mapping)


def test_manifest_from_mapping_rejects_non_object_file(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    mapping = _manifest(repository_root, signed=False).to_mapping()
    mapping["files"] = ["not-an-object"]

    with pytest.raises(FixtureError, match=r"files\[0\] must be a JSON object"):
        FixtureManifest.from_mapping(mapping)


@pytest.mark.parametrize("invalid_value", [None, "", "   ", 42])
def test_manifest_from_mapping_rejects_invalid_required_string(
    tmp_path: Path,
    invalid_value: object,
) -> None:
    repository_root = _create_repository(tmp_path)
    mapping = _manifest(repository_root, signed=False).to_mapping()
    mapping["scenario_id"] = invalid_value

    with pytest.raises(FixtureError, match=r"fixture manifest\.scenario_id"):
        FixtureManifest.from_mapping(mapping)


@pytest.mark.parametrize("invalid_value", ["", "   ", 42])
def test_manifest_from_mapping_rejects_invalid_optional_hash(
    tmp_path: Path,
    invalid_value: object,
) -> None:
    repository_root = _create_repository(tmp_path)
    mapping = _manifest(repository_root, signed=False).to_mapping()
    mapping["fixture_manifest_sha256"] = invalid_value

    with pytest.raises(FixtureError, match=r"fixture manifest\.fixture_manifest_sha256"):
        FixtureManifest.from_mapping(mapping)


def test_load_fixture_manifest_accepts_valid_signed_document(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    expected = _manifest(repository_root)
    path = _write_manifest(repository_root, expected)

    loaded = load_fixture_manifest(path)

    assert loaded == expected
    assert calculate_fixture_manifest_sha256(loaded) == loaded.fixture_manifest_sha256


def test_load_fixture_manifest_accepts_unsigned_draft_only_when_explicit(
    tmp_path: Path,
) -> None:
    repository_root = _create_repository(tmp_path)
    unsigned = _manifest(repository_root, signed=False)
    path = _write_manifest(repository_root, unsigned)

    with pytest.raises(FixtureError, match="fixture_manifest_sha256 is required"):
        load_fixture_manifest(path)

    assert load_fixture_manifest(path, require_hash=False) == unsigned


def test_load_fixture_manifest_rejects_tampered_document(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    signed = _manifest(repository_root)
    mapping = signed.to_mapping()
    mapping["scenario_id"] = "AURORA-SCN-FOUND-002"
    path = repository_root / _MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(mapping), encoding="utf-8")

    with pytest.raises(FixtureError, match="does not match"):
        load_fixture_manifest(path)


@pytest.mark.parametrize("document", ["[]", "{broken json", '{"value": NaN}'])
def test_load_fixture_manifest_rejects_invalid_json(
    tmp_path: Path,
    document: str,
) -> None:
    path = tmp_path / "fixture-manifest.json"
    path.write_text(document, encoding="utf-8")

    with pytest.raises(FixtureError):
        load_fixture_manifest(path)


def test_load_fixture_manifest_rejects_invalid_utf8(tmp_path: Path) -> None:
    path = tmp_path / "fixture-manifest.json"
    path.write_bytes(b"\xff\xfe\x00")

    with pytest.raises(FixtureError, match="unable to load fixture manifest"):
        load_fixture_manifest(path)


def test_load_fixture_manifest_rejects_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FixtureError, match="unable to load fixture manifest"):
        load_fixture_manifest(tmp_path / "missing.json")


def test_fixture_artifact_exposes_identity_and_decodes_json() -> None:
    content = b'{"nested":{"value":1}}'
    artifact = _artifact(content)

    first = artifact.decode_json_object()
    first["changed"] = True
    second = artifact.decode_json_object()

    assert artifact.path == _relative_path("artifact.json")
    assert artifact.partition is FixturePartition.WORLD
    assert artifact.media_type is FixtureMediaType.JSON
    assert artifact.decode_text() == content.decode()
    assert second == {"nested": {"value": 1}}
    assert "changed" not in second


@pytest.mark.parametrize(
    ("media_type", "content"),
    [
        (FixtureMediaType.TEXT, b"Plain text.\n"),
        (FixtureMediaType.MARKDOWN, b"# Markdown\n"),
    ],
)
def test_fixture_artifact_decodes_supported_text(
    media_type: FixtureMediaType,
    content: bytes,
) -> None:
    artifact = _artifact(content, filename="text.txt", media_type=media_type)

    assert artifact.decode_text() == content.decode()


def test_fixture_artifact_rejects_text_decode_for_binary() -> None:
    artifact = _artifact(
        b"\xff\x00",
        filename="state.bin",
        media_type=FixtureMediaType.BINARY,
    )

    with pytest.raises(FixtureError, match="not a text media type"):
        artifact.decode_text()


def test_fixture_artifact_rejects_invalid_utf8_text() -> None:
    artifact = _artifact(
        b"\xff\xfe",
        filename="invalid.txt",
        media_type=FixtureMediaType.TEXT,
    )

    with pytest.raises(FixtureError, match="not valid UTF-8"):
        artifact.decode_text()


@pytest.mark.parametrize("content", [b"[]", b"{broken", b'{"value":NaN}', b"\xff"])
def test_fixture_artifact_rejects_invalid_json(content: bytes) -> None:
    artifact = _artifact(content)

    with pytest.raises(
        FixtureError,
        match=r"fixture is not valid JSON|root must be an object",
    ):
        artifact.decode_json_object()


def test_fixture_artifact_rejects_json_decode_for_non_json_media() -> None:
    artifact = _artifact(
        b"{}",
        filename="state.txt",
        media_type=FixtureMediaType.TEXT,
    )

    with pytest.raises(FixtureError, match="fixture is not JSON"):
        artifact.decode_json_object()


def test_fixture_artifact_rejects_non_string_json_keys(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    artifact = _artifact(b"{}")
    monkeypatch.setattr(fixtures_module.json, "loads", lambda *args, **kwargs: {1: "value"})

    with pytest.raises(FixtureError, match="JSON fixture keys must be strings"):
        artifact.decode_json_object()


def test_fixture_artifact_checks_runtime_types_and_integrity() -> None:
    valid = _artifact(b"{}")

    with pytest.raises(FixtureError, match="definition must be a FixtureFile"):
        replace(valid, definition=object())
    with pytest.raises(FixtureError, match="resolved_path must be a Path"):
        replace(valid, resolved_path="fixture.json")
    with pytest.raises(FixtureError, match="content_bytes must be bytes"):
        replace(valid, content_bytes=bytearray(b"{}"))
    with pytest.raises(FixtureError, match="fixture size does not match"):
        replace(valid, content_bytes=b"longer")
    with pytest.raises(FixtureError, match="fixture hash does not match"):
        replace(valid, content_bytes=b"[]")


def test_load_fixture_bundle_returns_complete_sorted_bundle(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)

    bundle = load_fixture_bundle(repository_root, manifest)

    assert bundle.repository_root == repository_root.resolve()
    assert bundle.manifest == manifest
    assert bundle.fixture_set_sha256 == manifest.fixture_manifest_sha256
    assert [artifact.path for artifact in bundle.artifacts] == sorted(
        entry.path for entry in manifest.files
    )
    assert len(bundle.by_partition(FixturePartition.WORLD)) == 1
    assert len(bundle.by_partition(FixturePartition.EXPECTED_RESULTS)) == 1
    world = bundle.artifact(_relative_path("world.json"))
    assert world.decode_json_object() == _PARTITION_CONTENT[FixturePartition.WORLD]


def test_load_fixture_bundle_accepts_unsigned_draft_only_when_explicit(
    tmp_path: Path,
) -> None:
    repository_root = _create_repository(tmp_path)
    unsigned = _manifest(repository_root, signed=False)

    with pytest.raises(FixtureError, match="fixture_manifest_sha256 is required"):
        load_fixture_bundle(repository_root, unsigned)

    bundle = load_fixture_bundle(
        repository_root,
        unsigned,
        require_manifest_hash=False,
    )
    assert bundle.manifest == unsigned


def test_load_fixture_bundle_rejects_manifest_hash_mismatch(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = replace(_manifest(repository_root), fixture_manifest_sha256="0" * 64)

    with pytest.raises(FixtureError, match="does not match"):
        load_fixture_bundle(repository_root, manifest)


def test_load_fixture_bundle_rejects_modified_fixture_size(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)
    path = repository_root / _relative_path("world.json")
    path.write_bytes(path.read_bytes() + b"x")

    with pytest.raises(FixtureError, match="fixture size mismatch"):
        load_fixture_bundle(repository_root, manifest)


def test_load_fixture_bundle_rejects_modified_fixture_hash(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)
    path = repository_root / _relative_path("world.json")
    content = path.read_bytes()
    path.write_bytes(content.replace(b"7", b"8"))

    with pytest.raises(FixtureError, match="fixture hash mismatch"):
        load_fixture_bundle(repository_root, manifest)


def test_load_fixture_bundle_rejects_missing_fixture(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)
    (repository_root / _relative_path("world.json")).unlink()

    with pytest.raises(FixtureError, match="unable to resolve fixture path"):
        load_fixture_bundle(repository_root, manifest)


def test_load_fixture_bundle_rejects_fixture_directory(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)
    path = repository_root / _relative_path("world.json")
    path.unlink()
    path.mkdir()

    with pytest.raises(FixtureError, match="fixture path is not a file"):
        load_fixture_bundle(repository_root, manifest)


@pytest.mark.parametrize(
    ("content", "media_type", "message"),
    [
        (b"[]", FixtureMediaType.JSON, "root must be an object"),
        (b"\xff", FixtureMediaType.TEXT, "not valid UTF-8"),
        (b"\xff", FixtureMediaType.MARKDOWN, "not valid UTF-8"),
    ],
)
def test_load_fixture_bundle_rejects_invalid_content_even_when_hash_matches(
    tmp_path: Path,
    content: bytes,
    media_type: FixtureMediaType,
    message: str,
) -> None:
    repository_root = _create_repository(tmp_path)
    unsigned = _manifest(repository_root, signed=False)
    target = next(entry for entry in unsigned.files if entry.partition is FixturePartition.WORLD)
    path = repository_root / target.path
    path.write_bytes(content)
    replacement = _definition(
        content,
        filename=Path(target.path).name,
        partition=FixturePartition.WORLD,
        media_type=media_type,
    )
    files = tuple(replacement if entry.path == target.path else entry for entry in unsigned.files)
    changed = replace(unsigned, files=files)
    signed = replace(
        changed,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(changed),
    )

    with pytest.raises(FixtureError, match=message):
        load_fixture_bundle(repository_root, signed)


def test_load_fixture_bundle_rejects_unreadable_fixture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)

    def fail_read_bytes(path: Path) -> bytes:
        raise OSError(f"read denied: {path}")

    monkeypatch.setattr(Path, "read_bytes", fail_read_bytes)
    with pytest.raises(FixtureError, match="unable to read fixture"):
        load_fixture_bundle(repository_root, manifest)


def test_load_fixture_bundle_rejects_input_symlink_escape(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)
    outside = tmp_path / "outside.json"
    outside.write_bytes(_json_bytes({"hidden_location": "Cargo_Bay_7"}))
    world = repository_root / _relative_path("world.json")
    world.unlink()
    try:
        world.symlink_to(outside)
    except OSError as exc:
        pytest.skip(f"symbolic links unavailable: {exc}")

    with pytest.raises(FixtureError, match="escapes repository root"):
        load_fixture_bundle(repository_root, manifest)


def test_load_fixture_bundle_rejects_missing_repository(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)

    with pytest.raises(FixtureError, match="repository root cannot be resolved"):
        load_fixture_bundle(tmp_path / "missing", manifest)


def test_load_fixture_bundle_rejects_repository_file(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    manifest = _manifest(repository_root)
    invalid_root = tmp_path / "not-a-repository"
    invalid_root.write_text("file", encoding="utf-8")

    with pytest.raises(FixtureError, match="repository root is not a directory"):
        load_fixture_bundle(invalid_root, manifest)


def test_fixture_bundle_lookup_rejects_invalid_requests(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    bundle = load_fixture_bundle(repository_root, _manifest(repository_root))

    with pytest.raises(FixtureError, match="partition must be a FixturePartition"):
        bundle.by_partition("WORLD")
    with pytest.raises(FixtureError, match="fixture artifact is not present"):
        bundle.artifact(_relative_path("missing.json"))
    with pytest.raises(FixtureError):
        bundle.artifact("../outside.json")


def test_fixture_bundle_direct_constructor_checks_runtime_types(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    valid = load_fixture_bundle(repository_root, _manifest(repository_root))

    with pytest.raises(FixtureError, match="manifest must be a FixtureManifest"):
        replace(valid, manifest=object())
    with pytest.raises(FixtureError, match="repository_root must be a Path"):
        replace(valid, repository_root="repository")
    with pytest.raises(FixtureError, match="artifacts must be a tuple"):
        replace(valid, artifacts=[])
    with pytest.raises(FixtureError, match="artifacts must be a tuple"):
        replace(valid, artifacts=(object(),))
    with pytest.raises(FixtureError, match="do not match fixture manifest files"):
        replace(valid, artifacts=valid.artifacts[:-1])


def test_load_fixture_set_combines_manifest_and_artifact_loading(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    expected = _manifest(repository_root)
    path = _write_manifest(repository_root, expected)

    bundle = load_fixture_set(path, repository_root)

    assert bundle.manifest == expected
    assert bundle.fixture_set_sha256 == expected.fixture_manifest_sha256


def test_load_fixture_set_can_accept_unsigned_draft(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    unsigned = _manifest(repository_root, signed=False)
    path = _write_manifest(repository_root, unsigned)

    bundle = load_fixture_set(path, repository_root, require_hash=False)

    assert bundle.manifest == unsigned


@pytest.mark.parametrize(
    ("content", "media_type", "message"),
    [
        (b"[]", FixtureMediaType.JSON, "root must be an object"),
        (b"{broken", FixtureMediaType.JSON, "not valid JSON"),
        (b'{"value":NaN}', FixtureMediaType.JSON, "not valid JSON"),
        (b"\xff", FixtureMediaType.JSON, "not valid JSON"),
        (b"\xff", FixtureMediaType.TEXT, "not valid UTF-8"),
        (b"\xff", FixtureMediaType.MARKDOWN, "not valid UTF-8"),
    ],
)
def test_create_fixture_file_rejects_invalid_content(
    tmp_path: Path,
    content: bytes,
    media_type: FixtureMediaType,
    message: str,
) -> None:
    repository_root = tmp_path / "repository"
    relative_path = _relative_path("invalid.dat")
    _write_bytes(repository_root, relative_path, content)

    with pytest.raises(FixtureError, match=message):
        create_fixture_file(
            repository_root,
            relative_path,
            partition=FixturePartition.WORLD,
            media_type=media_type,
        )


def test_create_fixture_file_rejects_invalid_media_type(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    relative_path = _relative_path("state.json")
    _write_bytes(repository_root, relative_path, b"{}")

    with pytest.raises(FixtureError, match="media_type must be a FixtureMediaType"):
        create_fixture_file(
            repository_root,
            relative_path,
            partition=FixturePartition.WORLD,
            media_type="application/json",
        )


def test_create_fixture_file_rejects_missing_source(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    repository_root.mkdir()

    with pytest.raises(FixtureError, match="unable to resolve fixture path"):
        create_fixture_file(
            repository_root,
            _relative_path("missing.json"),
            partition=FixturePartition.WORLD,
            media_type=FixtureMediaType.JSON,
        )


def test_create_fixture_file_rejects_source_directory(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    source = repository_root / _relative_path("directory.json")
    source.mkdir(parents=True)

    with pytest.raises(FixtureError, match="fixture source is not a file"):
        create_fixture_file(
            repository_root,
            _relative_path("directory.json"),
            partition=FixturePartition.WORLD,
            media_type=FixtureMediaType.JSON,
        )


def test_create_fixture_file_rejects_unreadable_source(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repository_root = tmp_path / "repository"
    relative_path = _relative_path("state.json")
    _write_bytes(repository_root, relative_path, b"{}")

    def fail_read_bytes(path: Path) -> bytes:
        raise OSError(f"read denied: {path}")

    monkeypatch.setattr(Path, "read_bytes", fail_read_bytes)
    with pytest.raises(FixtureError, match="unable to read fixture"):
        create_fixture_file(
            repository_root,
            relative_path,
            partition=FixturePartition.WORLD,
            media_type=FixtureMediaType.JSON,
        )


def test_create_fixture_file_rejects_symlink_escape(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    fixture_directory = repository_root / _SCENARIO_DIRECTORY
    fixture_directory.mkdir(parents=True)
    outside = tmp_path / "outside.json"
    outside.write_text("{}", encoding="utf-8")
    link = fixture_directory / "escaped.json"
    try:
        link.symlink_to(outside)
    except OSError as exc:
        pytest.skip(f"symbolic links unavailable: {exc}")

    with pytest.raises(FixtureError, match="escapes repository root"):
        create_fixture_file(
            repository_root,
            _relative_path("escaped.json"),
            partition=FixturePartition.WORLD,
            media_type=FixtureMediaType.JSON,
        )
