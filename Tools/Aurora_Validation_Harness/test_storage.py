"""Unit tests for immutable, content-verified Aurora run-package storage."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
from collections.abc import Iterator, Mapping
from dataclasses import FrozenInstanceError, replace
from pathlib import Path
from types import MappingProxyType
from typing import NoReturn, cast

import pytest

from aurora_validation_harness import storage as storage_module
from aurora_validation_harness.storage import (
    DEFAULT_MAX_STORED_ARTIFACT_BYTES,
    MAX_ARTIFACT_PATH_LENGTH,
    MAX_RUN_MANIFEST_BYTES,
    MAX_RUN_PACKAGE_ARTIFACTS,
    MAX_STORED_ARTIFACT_BYTES,
    MAX_TICK,
    RUN_MANIFEST_FILENAME,
    SUPPORTED_STORAGE_SCHEMA_VERSION,
    ArtifactDescriptor,
    ArtifactKind,
    RunPackageManifest,
    StorageError,
    StoragePayload,
    calculate_run_package_manifest_sha256,
    create_artifact_descriptor,
    create_run_package_manifest,
    create_storage_payload,
    load_run_package_manifest,
    prepare_storage_root,
    read_run_artifact,
    verify_run_package,
    write_run_package,
)

pytestmark = [
    pytest.mark.foundation,
    pytest.mark.isolation,
    pytest.mark.metamorphic,
]

_PACKAGE_ID = "PACKAGE-FOUND-001-BASE"
_RUN_ID = "AURORA-RUN-FOUND-001-BASE"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"


def _payload(data: Mapping[str, object] | None = None) -> StoragePayload:
    selected = {"belief": "bounded", "tick": 7} if data is None else data
    return create_storage_payload(selected)


def _descriptor(
    *,
    artifact_id: str = "ARTIFACT-FOUND-001-A1",
    kind: ArtifactKind = ArtifactKind.DIAGNOSTIC,
    relative_path: str = "diagnostics/alpha.json",
    payload: StoragePayload | None = None,
) -> ArtifactDescriptor:
    return create_artifact_descriptor(
        artifact_id=artifact_id,
        kind=kind,
        relative_path=relative_path,
        payload=_payload() if payload is None else payload,
    )


def _manifest(*artifacts: ArtifactDescriptor) -> RunPackageManifest:
    selected = artifacts if artifacts else (_descriptor(),)
    return create_run_package_manifest(
        package_id=_PACKAGE_ID,
        run_id=_RUN_ID,
        scenario_id=_SCENARIO_ID,
        finalized_at_tick=42,
        artifacts=tuple(selected),
    )


def _package_components() -> tuple[
    RunPackageManifest,
    dict[str, StoragePayload],
]:
    diagnostic = _payload({"diagnostic": "nominal", "tick": 7})
    verdict = _payload({"outcome": "PASS", "valid": True})
    descriptors = (
        _descriptor(
            artifact_id="ARTIFACT-FOUND-001-A1",
            relative_path="diagnostics/alpha.json",
            payload=diagnostic,
        ),
        _descriptor(
            artifact_id="ARTIFACT-FOUND-001-V1",
            kind=ArtifactKind.SCENARIO_VERDICT,
            relative_path="verdicts/final.json",
            payload=verdict,
        ),
    )
    return _manifest(*descriptors), {
        descriptors[0].artifact_id: diagnostic,
        descriptors[1].artifact_id: verdict,
    }


def _write_package(
    tmp_path: Path,
) -> tuple[Path, Path, RunPackageManifest, dict[str, StoragePayload]]:
    root = prepare_storage_root(tmp_path / "runs")
    manifest, payloads = _package_components()
    package_directory = write_run_package(root, manifest, payloads)
    return root, package_directory, manifest, payloads


def _write_manifest_mapping(package_directory: Path, mapping: Mapping[str, object]) -> None:
    (package_directory / RUN_MANIFEST_FILENAME).write_bytes(
        json.dumps(
            mapping,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )


def _mutated_mapping(
    value: Mapping[str, object],
    key: str,
    replacement: object,
) -> dict[str, object]:
    result = copy.deepcopy(dict(value))
    result[key] = replacement
    return result


def test_storage_constants_define_bounded_versioned_contract() -> None:
    assert SUPPORTED_STORAGE_SCHEMA_VERSION == "1.0"
    assert RUN_MANIFEST_FILENAME == "run_manifest.json"
    assert 0 < DEFAULT_MAX_STORED_ARTIFACT_BYTES <= MAX_STORED_ARTIFACT_BYTES
    assert 0 < MAX_RUN_MANIFEST_BYTES < MAX_STORED_ARTIFACT_BYTES
    assert MAX_RUN_PACKAGE_ARTIFACTS == 100_000
    assert MAX_ARTIFACT_PATH_LENGTH == 1_024
    assert MAX_TICK == (1 << 63) - 1


def test_artifact_kind_values_are_stable_and_complete() -> None:
    assert tuple(kind.value for kind in ArtifactKind) == (
        "BASELINE_VERIFICATION",
        "RUN_CONFIGURATION",
        "FIXTURE_MANIFEST",
        "PARTITION_SET",
        "CHANNEL_SERIES",
        "EVENT_SERIES",
        "EVIDENCE_PACKAGE",
        "SNAPSHOT_SERIES",
        "TRANSITION_SERIES",
        "ASSERTION_SERIES",
        "COMPARISON_REPORT",
        "SCENARIO_VERDICT",
        "DIAGNOSTIC",
    )


def test_payload_is_canonical_content_addressed_and_detached() -> None:
    source: dict[str, object] = {
        "z": (None, True, 3, 1.25, "å"),
        "a": MappingProxyType({"nested": ["value"]}),
    }
    payload = create_storage_payload(source)

    assert payload.payload_json == (
        '{"a":{"nested":["value"]},"z":[null,true,3,1.25,"å"]}'.encode()
    )
    assert payload.payload_sha256 == hashlib.sha256(payload.payload_json).hexdigest()
    assert payload.size_bytes == len(payload.payload_json)
    decoded = payload.decode()
    cast(list[object], cast(dict[str, object], decoded["a"])["nested"]).append("changed")
    assert payload.decode() == {
        "a": {"nested": ["value"]},
        "z": [None, True, 3, 1.25, "å"],
    }


def test_payload_mapping_round_trip_is_exact_and_immutable() -> None:
    payload = _payload()
    assert StoragePayload.from_mapping(payload.to_mapping()) == payload
    assert not hasattr(payload, "__dict__")
    with pytest.raises(FrozenInstanceError):
        payload.payload_json = b"{}"  # type: ignore[misc]


@pytest.mark.parametrize(
    ("payload_json", "payload_sha256", "message"),
    [
        ("{}", "0" * 64, "payload_json must be bytes"),
        (b"{}", 7, "payload_sha256 must be a string"),
        (b"{}", "A" * 64, "lowercase SHA-256"),
        (b"{}", "0" * 64, "does not match"),
    ],
)
def test_payload_constructor_rejects_invalid_bytes_or_digest(
    payload_json: object,
    payload_sha256: object,
    message: str,
) -> None:
    with pytest.raises(StorageError, match=message):
        StoragePayload(payload_json, payload_sha256)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "payload_json",
    [
        b"\xff",
        b"{",
        b'{"value":NaN}',
        b"[]",
        b'{"z":1, "a":2}',
    ],
)
def test_payload_constructor_rejects_invalid_or_noncanonical_json(payload_json: bytes) -> None:
    with pytest.raises(StorageError):
        StoragePayload(payload_json, hashlib.sha256(payload_json).hexdigest())


def test_payload_constructor_enforces_global_byte_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(storage_module, "MAX_STORED_ARTIFACT_BYTES", 1)
    with pytest.raises(StorageError, match="must not exceed 1 bytes"):
        StoragePayload(b"{}", hashlib.sha256(b"{}").hexdigest())


@pytest.mark.parametrize("data", [None, [], "object"])
def test_create_payload_requires_mapping(data: object) -> None:
    with pytest.raises(StorageError, match="must be a JSON object"):
        create_storage_payload(data)  # type: ignore[arg-type]


@pytest.mark.parametrize("maximum", [True, 1.5, "10"])
def test_create_payload_requires_integer_byte_bound(maximum: object) -> None:
    with pytest.raises(StorageError, match="must be an integer"):
        create_storage_payload({}, max_payload_bytes=maximum)  # type: ignore[arg-type]


@pytest.mark.parametrize("maximum", [0, MAX_STORED_ARTIFACT_BYTES + 1])
def test_create_payload_requires_supported_byte_bound(maximum: int) -> None:
    with pytest.raises(StorageError, match="must be between"):
        create_storage_payload({}, max_payload_bytes=maximum)


@pytest.mark.parametrize(
    "data",
    [
        {"value": float("nan")},
        {"value": float("inf")},
        {"value": object()},
        {1: "non-string"},
    ],
)
def test_create_payload_rejects_non_json_values(data: Mapping[object, object]) -> None:
    with pytest.raises(StorageError):
        create_storage_payload(data)  # type: ignore[arg-type]


def test_create_payload_enforces_requested_byte_bound() -> None:
    with pytest.raises(StorageError, match="must not exceed 1 bytes"):
        create_storage_payload({"value": "large"}, max_payload_bytes=1)


def test_create_payload_defensively_rejects_non_object_normalization(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(storage_module, "_normalize_json_value", lambda *_a, **_k: [])
    with pytest.raises(StorageError, match="must be a JSON object"):
        create_storage_payload({})


def test_canonical_encoder_converts_serialization_failures() -> None:
    with pytest.raises(StorageError, match="canonical finite JSON"):
        storage_module._canonical_json_bytes(object())


@pytest.mark.parametrize(
    ("mapping", "message"),
    [
        ([], "must be an object"),
        ({"data": {}, "payload_sha256": "0" * 64}, "missing required fields"),
        (
            {"data": {}, "payload_sha256": "0" * 64, "size_bytes": 2, "extra": 1},
            "unexpected fields",
        ),
        (
            {"data": [], "payload_sha256": "0" * 64, "size_bytes": 2},
            "data must be an object",
        ),
        (
            {"data": {}, "payload_sha256": hashlib.sha256(b"{}").hexdigest(), "size_bytes": True},
            "size_bytes must be an integer",
        ),
        (
            {"data": {}, "payload_sha256": hashlib.sha256(b"{}").hexdigest(), "size_bytes": 3},
            "size_bytes does not match",
        ),
        ({"data": {}, "payload_sha256": "0" * 64, "size_bytes": 2}, "does not match"),
    ],
)
def test_payload_mapping_parser_fails_closed(mapping: object, message: str) -> None:
    with pytest.raises(StorageError, match=message):
        StoragePayload.from_mapping(mapping)  # type: ignore[arg-type]


@pytest.mark.parametrize("kind", list(ArtifactKind))
def test_descriptor_supports_every_governed_artifact_kind(kind: ArtifactKind) -> None:
    descriptor = _descriptor(kind=kind)
    assert descriptor.kind is kind
    assert ArtifactDescriptor.from_mapping(descriptor.to_mapping()) == descriptor


def test_descriptor_is_content_addressed_slotted_and_frozen() -> None:
    descriptor = _descriptor()
    content = {
        key: value for key, value in descriptor.to_mapping().items() if key != "descriptor_sha256"
    }
    expected = hashlib.sha256(
        json.dumps(content, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert descriptor.descriptor_sha256 == expected
    assert not hasattr(descriptor, "__dict__")
    with pytest.raises(FrozenInstanceError):
        descriptor.artifact_id = "ARTIFACT-FOUND-001-X1"  # type: ignore[misc]


@pytest.mark.parametrize("artifact_id", [7, "ab", "lower-case", " SPACE "])
def test_descriptor_requires_stable_artifact_id(artifact_id: object) -> None:
    with pytest.raises(StorageError, match="artifact_id must"):
        ArtifactDescriptor(
            artifact_id,  # type: ignore[arg-type]
            ArtifactKind.DIAGNOSTIC,
            "diagnostic.json",
            "0" * 64,
            2,
        )


def test_descriptor_requires_enum_kind() -> None:
    with pytest.raises(StorageError, match="kind must be"):
        ArtifactDescriptor("ARTIFACT-001", "DIAGNOSTIC", "a.json", "0" * 64, 2)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    "relative_path",
    [
        7,
        "",
        "a" * (MAX_ARTIFACT_PATH_LENGTH + 1),
        r"folder\a.json",
        "/a.json",
        "./a.json",
        "folder//a.json",
        "../a.json",
        "folder/../a.json",
        "_private/a.json",
        "folder/a space.json",
        f"{'a' * 256}.json",
        RUN_MANIFEST_FILENAME,
        f"nested/{RUN_MANIFEST_FILENAME}",
        "folder/a.txt",
    ],
)
def test_descriptor_rejects_unsafe_artifact_paths(relative_path: object) -> None:
    with pytest.raises(StorageError):
        ArtifactDescriptor(
            "ARTIFACT-001",
            ArtifactKind.DIAGNOSTIC,
            relative_path,  # type: ignore[arg-type]
            "0" * 64,
            2,
        )


@pytest.mark.parametrize("digest", [7, "A" * 64, "0" * 63])
def test_descriptor_rejects_invalid_payload_digest(digest: object) -> None:
    with pytest.raises(StorageError, match="payload_sha256 must"):
        ArtifactDescriptor(
            "ARTIFACT-001",
            ArtifactKind.DIAGNOSTIC,
            "a.json",
            digest,  # type: ignore[arg-type]
            2,
        )


@pytest.mark.parametrize("size", [True, 1.5, 0, -1])
def test_descriptor_requires_positive_integer_size(size: object) -> None:
    with pytest.raises(StorageError, match="size_bytes must"):
        ArtifactDescriptor(
            "ARTIFACT-001",
            ArtifactKind.DIAGNOSTIC,
            "a.json",
            "0" * 64,
            size,  # type: ignore[arg-type]
        )


def test_descriptor_enforces_global_size_bound() -> None:
    with pytest.raises(StorageError, match="must not exceed"):
        ArtifactDescriptor(
            "ARTIFACT-001",
            ArtifactKind.DIAGNOSTIC,
            "a.json",
            "0" * 64,
            MAX_STORED_ARTIFACT_BYTES + 1,
        )


def test_descriptor_factory_requires_storage_payload() -> None:
    with pytest.raises(StorageError, match="payload must be"):
        create_artifact_descriptor(
            artifact_id="ARTIFACT-001",
            kind=ArtifactKind.DIAGNOSTIC,
            relative_path="a.json",
            payload={},  # type: ignore[arg-type]
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ({"remove": "size_bytes"}, "missing required fields"),
        ({"extra": 1}, "unexpected fields"),
        ({"kind": "UNKNOWN"}, "unsupported value"),
        ({"kind": 7}, "must be a string"),
        ({"relative_path": 7}, "must be a string"),
        ({"size_bytes": True}, "must be an integer"),
        ({"descriptor_sha256": "0" * 64}, "does not match"),
    ],
)
def test_descriptor_mapping_parser_fails_closed(
    mutation: Mapping[str, object],
    message: str,
) -> None:
    mapping = _descriptor().to_mapping()
    remove = mutation.get("remove")
    if isinstance(remove, str):
        del mapping[remove]
    else:
        mapping.update(mutation)
    with pytest.raises(StorageError, match=message):
        ArtifactDescriptor.from_mapping(mapping)


def test_descriptor_mapping_requires_an_object() -> None:
    with pytest.raises(StorageError, match="must be an object"):
        ArtifactDescriptor.from_mapping([])  # type: ignore[arg-type]


def test_manifest_factory_sorts_artifacts_and_seals_inventory() -> None:
    first_payload = _payload({"first": 1})
    second_payload = _payload({"second": 2})
    zulu = _descriptor(
        artifact_id="ARTIFACT-FOUND-001-Z1",
        relative_path="zulu.json",
        payload=second_payload,
    )
    alpha = _descriptor(
        artifact_id="ARTIFACT-FOUND-001-A1",
        relative_path="alpha.json",
        payload=first_payload,
    )
    manifest = _manifest(zulu, alpha)

    assert manifest.artifacts == (alpha, zulu)
    assert manifest.artifact_count == 2
    assert manifest.total_size_bytes == first_payload.size_bytes + second_payload.size_bytes
    assert calculate_run_package_manifest_sha256(manifest) == manifest.manifest_sha256
    assert RunPackageManifest.from_mapping(manifest.to_mapping()) == manifest
    assert not hasattr(manifest, "__dict__")
    with pytest.raises(FrozenInstanceError):
        manifest.run_id = "AURORA-RUN-FOUND-001-X"  # type: ignore[misc]


@pytest.mark.parametrize("field", ["package_id", "run_id"])
@pytest.mark.parametrize("value", [7, "ab", "lower-case"])
def test_manifest_requires_stable_control_ids(field: str, value: object) -> None:
    values: dict[str, object] = {
        "package_id": _PACKAGE_ID,
        "run_id": _RUN_ID,
        "scenario_id": _SCENARIO_ID,
        "finalized_at_tick": 1,
        "artifacts": (_descriptor(),),
    }
    values[field] = value
    with pytest.raises(StorageError):
        RunPackageManifest(**values)  # type: ignore[arg-type]


@pytest.mark.parametrize("scenario_id", [7, "AURORA-SCN-bad-001", "SCN-FOUND-001"])
def test_manifest_requires_canonical_scenario_id(scenario_id: object) -> None:
    with pytest.raises(StorageError, match="scenario_id"):
        RunPackageManifest(
            _PACKAGE_ID,
            _RUN_ID,
            scenario_id,  # type: ignore[arg-type]
            1,
            (_descriptor(),),
        )


@pytest.mark.parametrize("tick", [True, 1.5, -1, MAX_TICK + 1])
def test_manifest_requires_bounded_integer_tick(tick: object) -> None:
    with pytest.raises(StorageError, match="finalized_at_tick must"):
        RunPackageManifest(
            _PACKAGE_ID,
            _RUN_ID,
            _SCENARIO_ID,
            tick,  # type: ignore[arg-type]
            (_descriptor(),),
        )


@pytest.mark.parametrize("artifacts", [[], (), ("not-a-descriptor",)])
def test_manifest_requires_nonempty_descriptor_tuple(artifacts: object) -> None:
    with pytest.raises(StorageError, match="artifacts must"):
        RunPackageManifest(
            _PACKAGE_ID,
            _RUN_ID,
            _SCENARIO_ID,
            1,
            artifacts,  # type: ignore[arg-type]
        )


def test_manifest_enforces_artifact_count_bound(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(storage_module, "MAX_RUN_PACKAGE_ARTIFACTS", 1)
    with pytest.raises(StorageError, match="must not exceed 1"):
        _manifest(
            _descriptor(artifact_id="ARTIFACT-001", relative_path="a.json"),
            _descriptor(artifact_id="ARTIFACT-002", relative_path="b.json"),
        )


def test_manifest_rejects_duplicate_artifact_ids() -> None:
    with pytest.raises(StorageError, match="unique artifact IDs"):
        RunPackageManifest(
            _PACKAGE_ID,
            _RUN_ID,
            _SCENARIO_ID,
            1,
            (
                _descriptor(artifact_id="ARTIFACT-001", relative_path="a.json"),
                _descriptor(artifact_id="ARTIFACT-001", relative_path="b.json"),
            ),
        )


def test_manifest_rejects_duplicate_artifact_paths() -> None:
    with pytest.raises(StorageError, match="unique relative paths"):
        RunPackageManifest(
            _PACKAGE_ID,
            _RUN_ID,
            _SCENARIO_ID,
            1,
            (
                _descriptor(artifact_id="ARTIFACT-001", relative_path="a.json"),
                _descriptor(artifact_id="ARTIFACT-002", relative_path="a.json"),
            ),
        )


def test_manifest_constructor_rejects_noncanonical_path_order() -> None:
    with pytest.raises(StorageError, match="lexical relative-path order"):
        RunPackageManifest(
            _PACKAGE_ID,
            _RUN_ID,
            _SCENARIO_ID,
            1,
            (
                _descriptor(artifact_id="ARTIFACT-002", relative_path="b.json"),
                _descriptor(artifact_id="ARTIFACT-001", relative_path="a.json"),
            ),
        )


def test_manifest_rejects_file_directory_path_overlap() -> None:
    with pytest.raises(StorageError, match="must not overlap"):
        RunPackageManifest(
            _PACKAGE_ID,
            _RUN_ID,
            _SCENARIO_ID,
            1,
            (
                _descriptor(artifact_id="ARTIFACT-001", relative_path="nested.json"),
                _descriptor(
                    artifact_id="ARTIFACT-002",
                    relative_path="nested.json/child.json",
                ),
            ),
        )


def test_manifest_factory_requires_tuple() -> None:
    with pytest.raises(StorageError, match="artifacts must be a tuple"):
        create_run_package_manifest(
            package_id=_PACKAGE_ID,
            run_id=_RUN_ID,
            scenario_id=_SCENARIO_ID,
            finalized_at_tick=1,
            artifacts=[_descriptor()],  # type: ignore[arg-type]
        )


def test_manifest_digest_calculator_requires_manifest() -> None:
    with pytest.raises(StorageError, match="manifest must be"):
        calculate_run_package_manifest_sha256({})  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("key", "replacement", "message"),
    [
        ("storage_schema_version", "2.0", "unsupported storage_schema_version"),
        ("storage_schema_version", 1, "must be a string"),
        ("package_type", "DRAFT", "unsupported package_type"),
        ("artifacts", {}, "artifacts must be an array"),
        ("artifacts", ["bad"], "artifacts\\[0\\] must be an object"),
        ("artifact_count", True, "artifact_count must be an integer"),
        ("artifact_count", 2, "artifact_count does not match"),
        ("total_size_bytes", True, "total_size_bytes must be an integer"),
        ("total_size_bytes", 1, "total_size_bytes does not match"),
        ("manifest_sha256", "0" * 64, "manifest_sha256 does not match"),
    ],
)
def test_manifest_mapping_parser_rejects_invalid_declarations(
    key: str,
    replacement: object,
    message: str,
) -> None:
    mapping = _mutated_mapping(_manifest().to_mapping(), key, replacement)
    with pytest.raises(StorageError, match=message):
        RunPackageManifest.from_mapping(mapping)


def test_manifest_mapping_requires_exact_object_shape() -> None:
    with pytest.raises(StorageError, match="must be an object"):
        RunPackageManifest.from_mapping([])  # type: ignore[arg-type]
    mapping = _manifest().to_mapping()
    del mapping["run_id"]
    with pytest.raises(StorageError, match="missing required fields"):
        RunPackageManifest.from_mapping(mapping)
    mapping = _manifest().to_mapping()
    mapping["extra"] = 1
    with pytest.raises(StorageError, match="unexpected fields"):
        RunPackageManifest.from_mapping(mapping)


def test_prepare_storage_root_creates_leaf_and_reuses_existing_directory(tmp_path: Path) -> None:
    root = tmp_path / "runs"
    assert prepare_storage_root(root) == root.resolve()
    assert prepare_storage_root(root) == root.resolve()


def test_prepare_storage_root_requires_path(tmp_path: Path) -> None:
    with pytest.raises(StorageError, match=r"pathlib\.Path"):
        prepare_storage_root(str(tmp_path))  # type: ignore[arg-type]


def test_prepare_storage_root_rejects_symlink(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()
    link = tmp_path / "link"
    link.symlink_to(target, target_is_directory=True)
    with pytest.raises(StorageError, match="must not be a symbolic link"):
        prepare_storage_root(link)


def test_prepare_storage_root_rejects_existing_file(tmp_path: Path) -> None:
    root = tmp_path / "file"
    root.write_text("not a directory")
    with pytest.raises(StorageError, match="must be a directory"):
        prepare_storage_root(root)


def test_prepare_storage_root_requires_existing_directory_parent(tmp_path: Path) -> None:
    with pytest.raises(StorageError, match="parent must be an existing directory"):
        prepare_storage_root(tmp_path / "missing" / "runs")
    parent_file = tmp_path / "parent-file"
    parent_file.write_text("file")
    with pytest.raises(StorageError, match="parent must be an existing directory"):
        prepare_storage_root(parent_file / "runs")


def test_prepare_storage_root_rejects_symlink_parent(tmp_path: Path) -> None:
    target = tmp_path / "target"
    target.mkdir()
    parent = tmp_path / "parent"
    parent.symlink_to(target, target_is_directory=True)
    with pytest.raises(StorageError, match="parent must not be a symbolic link"):
        prepare_storage_root(parent / "runs")


def test_prepare_storage_root_converts_creation_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail_mkdir(_path: Path, *, exist_ok: bool = False) -> NoReturn:
        del exist_ok
        raise OSError("denied")

    monkeypatch.setattr(Path, "mkdir", fail_mkdir)
    with pytest.raises(StorageError, match="could not create output_root"):
        prepare_storage_root(tmp_path / "runs")


def test_write_load_read_and_verify_run_package_round_trip(tmp_path: Path) -> None:
    root, package, manifest, payloads = _write_package(tmp_path)

    assert package == root / _RUN_ID
    assert load_run_package_manifest(package) == manifest
    assert verify_run_package(package, expected_manifest=manifest) == manifest
    for artifact_id, payload in payloads.items():
        assert read_run_artifact(package, manifest, artifact_id) == payload
    manifest_bytes = (package / RUN_MANIFEST_FILENAME).read_bytes()
    assert manifest_bytes == storage_module._canonical_json_bytes(manifest.to_mapping())


def test_write_accepts_read_only_payload_mapping(tmp_path: Path) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    manifest, payloads = _package_components()
    package = write_run_package(root, manifest, MappingProxyType(payloads))
    assert verify_run_package(package) == manifest


def test_write_refuses_to_overwrite_existing_run(tmp_path: Path) -> None:
    root, package, manifest, payloads = _write_package(tmp_path)
    original_manifest = (package / RUN_MANIFEST_FILENAME).read_bytes()
    with pytest.raises(StorageError, match="already exists"):
        write_run_package(root, manifest, payloads)
    assert (package / RUN_MANIFEST_FILENAME).read_bytes() == original_manifest


@pytest.mark.parametrize("payloads", [[], {1: _payload()}, {"ARTIFACT-FOUND-001-A1": {}}])
def test_write_requires_string_keyed_storage_payload_mapping(
    tmp_path: Path,
    payloads: object,
) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    manifest = _manifest()
    with pytest.raises(StorageError):
        write_run_package(root, manifest, payloads)  # type: ignore[arg-type]


def test_write_rejects_missing_and_unexpected_payload_ids(tmp_path: Path) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    manifest = _manifest()
    with pytest.raises(StorageError, match="missing artifact IDs"):
        write_run_package(root, manifest, {})
    with pytest.raises(StorageError, match="unexpected artifact IDs"):
        write_run_package(
            root,
            manifest,
            {
                manifest.artifacts[0].artifact_id: _payload(),
                "ARTIFACT-FOUND-001-X1": _payload(),
            },
        )


def test_write_rejects_payload_size_and_digest_mismatch(tmp_path: Path) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    payload = _payload()
    descriptor = _descriptor(payload=payload)
    size_manifest = _manifest(replace(descriptor, size_bytes=payload.size_bytes + 1))
    with pytest.raises(StorageError, match="payload size does not match"):
        write_run_package(root, size_manifest, {descriptor.artifact_id: payload})
    digest_manifest = _manifest(replace(descriptor, payload_sha256="0" * 64))
    with pytest.raises(StorageError, match="payload digest does not match"):
        write_run_package(root, digest_manifest, {descriptor.artifact_id: payload})


def test_write_requires_existing_safe_root_and_manifest(tmp_path: Path) -> None:
    manifest, payloads = _package_components()
    with pytest.raises(StorageError, match=r"pathlib\.Path"):
        write_run_package(str(tmp_path), manifest, payloads)  # type: ignore[arg-type]
    with pytest.raises(StorageError, match="does not exist"):
        write_run_package(tmp_path / "missing", manifest, payloads)
    file_root = tmp_path / "file"
    file_root.write_text("file")
    with pytest.raises(StorageError, match="must be a directory"):
        write_run_package(file_root, manifest, payloads)
    real_root = tmp_path / "real"
    real_root.mkdir()
    link_root = tmp_path / "link"
    link_root.symlink_to(real_root, target_is_directory=True)
    with pytest.raises(StorageError, match="symbolic link"):
        write_run_package(link_root, manifest, payloads)
    with pytest.raises(StorageError, match="manifest must be"):
        write_run_package(real_root, {}, payloads)  # type: ignore[arg-type]


def test_write_converts_staging_creation_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    manifest, payloads = _package_components()

    def fail_mkdtemp(*, prefix: str, dir: Path) -> NoReturn:
        del prefix, dir
        raise OSError("denied")

    monkeypatch.setattr(tempfile, "mkdtemp", fail_mkdtemp)
    with pytest.raises(StorageError, match="could not create run-package staging"):
        write_run_package(root, manifest, payloads)


def test_write_rejects_oversized_serialized_manifest_and_cleans_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    manifest, payloads = _package_components()
    monkeypatch.setattr(storage_module, "MAX_RUN_MANIFEST_BYTES", 1)
    with pytest.raises(StorageError, match="serialized run manifest"):
        write_run_package(root, manifest, payloads)
    assert tuple(root.iterdir()) == ()


def test_write_converts_publish_failure_and_cleans_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    manifest, payloads = _package_components()

    def fail_rename(_source: Path, _target: Path) -> NoReturn:
        raise OSError("denied")

    monkeypatch.setattr(Path, "rename", fail_rename)
    with pytest.raises(StorageError, match="could not atomically publish"):
        write_run_package(root, manifest, payloads)
    assert tuple(root.iterdir()) == ()


def test_write_detects_racing_final_directory_and_cleans_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root = prepare_storage_root(tmp_path / "runs")
    manifest, payloads = _package_components()
    original_write = storage_module._write_new_file

    def create_racing_directory(path: Path, data: bytes) -> None:
        original_write(path, data)
        if path.name == RUN_MANIFEST_FILENAME:
            (root / manifest.run_id).mkdir()

    monkeypatch.setattr(storage_module, "_write_new_file", create_racing_directory)
    with pytest.raises(StorageError, match="already exists"):
        write_run_package(root, manifest, payloads)
    assert tuple(path.name for path in root.iterdir()) == (manifest.run_id,)


def test_write_new_file_is_exclusive_and_converts_io_failure(tmp_path: Path) -> None:
    existing = tmp_path / "existing.json"
    existing.write_bytes(b"{}")
    with pytest.raises(StorageError, match="refusing to overwrite"):
        storage_module._write_new_file(existing, b"new")
    with pytest.raises(StorageError, match="could not write storage file"):
        storage_module._write_new_file(tmp_path / "missing" / "a.json", b"{}")


@pytest.mark.parametrize("kind", ["missing", "file", "symlink"])
def test_load_requires_existing_safe_package_directory(tmp_path: Path, kind: str) -> None:
    path = tmp_path / "package"
    if kind == "file":
        path.write_text("file")
    elif kind == "symlink":
        target = tmp_path / "target"
        target.mkdir()
        path.symlink_to(target, target_is_directory=True)
    with pytest.raises(StorageError):
        load_run_package_manifest(path)


@pytest.mark.parametrize("kind", ["missing", "directory", "symlink"])
def test_load_requires_regular_non_symlink_manifest(tmp_path: Path, kind: str) -> None:
    package = tmp_path / _RUN_ID
    package.mkdir()
    manifest_path = package / RUN_MANIFEST_FILENAME
    if kind == "directory":
        manifest_path.mkdir()
    elif kind == "symlink":
        target = tmp_path / "manifest-target"
        target.write_bytes(b"{}")
        manifest_path.symlink_to(target)
    with pytest.raises(StorageError):
        load_run_package_manifest(package)


def test_load_enforces_manifest_size_bound(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, package, _, _ = _write_package(tmp_path)
    monkeypatch.setattr(storage_module, "MAX_RUN_MANIFEST_BYTES", 1)
    with pytest.raises(StorageError, match="must not exceed 1 bytes"):
        load_run_package_manifest(package)


@pytest.mark.parametrize("manifest_bytes", [b"\xff", b"{", b'{"value":NaN}', b"[]"])
def test_load_rejects_invalid_manifest_json(tmp_path: Path, manifest_bytes: bytes) -> None:
    package = tmp_path / _RUN_ID
    package.mkdir()
    (package / RUN_MANIFEST_FILENAME).write_bytes(manifest_bytes)
    with pytest.raises(StorageError):
        load_run_package_manifest(package)


def test_load_rejects_noncanonical_manifest_encoding(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    (package / RUN_MANIFEST_FILENAME).write_text(
        json.dumps(manifest.to_mapping(), indent=2),
        encoding="utf-8",
    )
    with pytest.raises(StorageError, match="canonical JSON"):
        load_run_package_manifest(package)


def test_load_rejects_directory_name_manifest_mismatch(tmp_path: Path) -> None:
    _, package, _, _ = _write_package(tmp_path)
    renamed = package.with_name("AURORA-RUN-FOUND-001-OTHER")
    package.rename(renamed)
    with pytest.raises(StorageError, match="directory name must match"):
        load_run_package_manifest(renamed)


def test_load_rejects_tampered_manifest_declaration(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    _write_manifest_mapping(package, _mutated_mapping(manifest.to_mapping(), "artifact_count", 99))
    with pytest.raises(StorageError, match="artifact_count does not match"):
        load_run_package_manifest(package)


def test_read_artifact_validates_manifest_and_declared_id(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    with pytest.raises(StorageError, match="manifest must be"):
        read_run_artifact(package, {}, "ARTIFACT-FOUND-001-A1")  # type: ignore[arg-type]
    with pytest.raises(StorageError, match="artifact_id must"):
        read_run_artifact(package, manifest, "bad")
    with pytest.raises(StorageError, match="not declared"):
        read_run_artifact(package, manifest, "ARTIFACT-FOUND-001-X1")


@pytest.mark.parametrize("kind", ["missing", "directory", "symlink"])
def test_read_artifact_requires_regular_non_symlink_file(tmp_path: Path, kind: str) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    descriptor = manifest.artifacts[0]
    path = package / descriptor.relative_path
    path.unlink()
    if kind == "directory":
        path.mkdir()
    elif kind == "symlink":
        target = tmp_path / "artifact-target"
        target.write_bytes(b"{}")
        path.symlink_to(target)
    with pytest.raises(StorageError):
        read_run_artifact(package, manifest, descriptor.artifact_id)


def test_read_artifact_enforces_global_size_bound(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    monkeypatch.setattr(storage_module, "MAX_STORED_ARTIFACT_BYTES", 1)
    with pytest.raises(StorageError, match="must not exceed 1 bytes"):
        read_run_artifact(package, manifest, manifest.artifacts[0].artifact_id)


def test_read_artifact_rejects_noncanonical_or_tampered_payload(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    descriptor = manifest.artifacts[0]
    path = package / descriptor.relative_path
    path.write_bytes(b'{"tick":7, "diagnostic":"nominal"}')
    with pytest.raises(StorageError, match="canonical JSON"):
        read_run_artifact(package, manifest, descriptor.artifact_id)


def test_read_artifact_rejects_manifest_size_mismatch(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    descriptor = manifest.artifacts[0]
    altered = replace(descriptor, size_bytes=descriptor.size_bytes + 1)
    altered_manifest = replace(manifest, artifacts=(altered, *manifest.artifacts[1:]))
    with pytest.raises(StorageError, match="artifact size does not match"):
        read_run_artifact(package, altered_manifest, descriptor.artifact_id)


def test_read_artifact_rejects_manifest_digest_mismatch(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    descriptor = manifest.artifacts[0]
    altered = replace(descriptor, payload_sha256="0" * 64)
    altered_manifest = replace(manifest, artifacts=(altered, *manifest.artifacts[1:]))
    with pytest.raises(StorageError, match="artifact digest does not match"):
        read_run_artifact(package, altered_manifest, descriptor.artifact_id)


def test_verify_rejects_invalid_or_different_expected_manifest(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    with pytest.raises(StorageError, match="expected_manifest must"):
        verify_run_package(package, expected_manifest={})  # type: ignore[arg-type]
    other = replace(manifest, finalized_at_tick=manifest.finalized_at_tick + 1)
    with pytest.raises(StorageError, match="does not match expected"):
        verify_run_package(package, expected_manifest=other)


def test_verify_rejects_unexpected_file(tmp_path: Path) -> None:
    _, package, _, _ = _write_package(tmp_path)
    (package / "unexpected.json").write_bytes(b"{}")
    with pytest.raises(StorageError, match="unexpected files"):
        verify_run_package(package)


def test_verify_rejects_unexpected_directory(tmp_path: Path) -> None:
    _, package, _, _ = _write_package(tmp_path)
    (package / "unexpected").mkdir()
    with pytest.raises(StorageError, match="unexpected directories"):
        verify_run_package(package)


def test_verify_rejects_symbolic_link(tmp_path: Path) -> None:
    _, package, _, _ = _write_package(tmp_path)
    target = tmp_path / "target.json"
    target.write_bytes(b"{}")
    (package / "link.json").symlink_to(target)
    with pytest.raises(StorageError, match="symbolic links"):
        verify_run_package(package)


def test_validate_tree_rejects_missing_declared_file(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    (package / manifest.artifacts[0].relative_path).unlink()
    with pytest.raises(StorageError, match="missing declared files"):
        storage_module._validate_package_tree(package, manifest)


def test_validate_tree_rejects_missing_declared_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    real_entries = tuple(package.rglob("*"))
    files_only = tuple(path for path in real_entries if path.is_file())
    monkeypatch.setattr(Path, "rglob", lambda _path, _pattern: iter(files_only))
    with pytest.raises(StorageError, match="missing declared directories"):
        storage_module._validate_package_tree(package, manifest)


def test_validate_tree_converts_enumeration_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, package, manifest, _ = _write_package(tmp_path)

    def fail_rglob(_path: Path, _pattern: str) -> Iterator[Path]:
        raise OSError("denied")

    monkeypatch.setattr(Path, "rglob", fail_rglob)
    with pytest.raises(StorageError, match="could not enumerate"):
        storage_module._validate_package_tree(package, manifest)


@pytest.mark.skipif(not hasattr(os, "mkfifo"), reason="FIFO support is required")
def test_validate_tree_rejects_special_filesystem_entry(tmp_path: Path) -> None:
    _, package, manifest, _ = _write_package(tmp_path)
    fifo = package / "diagnostic.pipe"
    os.mkfifo(fifo)
    with pytest.raises(StorageError, match="unsupported filesystem entry"):
        storage_module._validate_package_tree(package, manifest)


def test_join_artifact_path_defensively_rejects_escape(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(storage_module, "_validate_artifact_path", lambda _value: None)
    with pytest.raises(StorageError, match="escapes package directory"):
        storage_module._join_artifact_path(tmp_path, "/escape.json")


class _InspectionFailurePath:
    def is_symlink(self) -> bool:
        return False

    def exists(self) -> bool:
        return True

    def is_file(self) -> bool:
        return True

    def stat(self) -> NoReturn:
        raise OSError("denied")


class _ReadFailurePath:
    def is_symlink(self) -> bool:
        return False

    def exists(self) -> bool:
        return True

    def is_file(self) -> bool:
        return True

    def stat(self) -> os.stat_result:
        return os.stat_result((0, 0, 0, 0, 0, 0, 2, 0, 0, 0))

    def read_bytes(self) -> NoReturn:
        raise OSError("denied")


def test_regular_file_reader_converts_inspection_and_read_failures() -> None:
    with pytest.raises(StorageError, match="could not inspect artifact"):
        storage_module._read_regular_file(
            _InspectionFailurePath(),  # type: ignore[arg-type]
            max_bytes=10,
            field="artifact",
        )
    with pytest.raises(StorageError, match="could not read artifact"):
        storage_module._read_regular_file(
            _ReadFailurePath(),  # type: ignore[arg-type]
            max_bytes=10,
            field="artifact",
        )


def test_mapping_validator_rejects_non_string_keys() -> None:
    with pytest.raises(StorageError, match="keys must be strings"):
        storage_module._require_mapping({1: "value"}, field="mapping")


def test_exact_key_validator_reports_missing_before_unexpected() -> None:
    with pytest.raises(StorageError, match="missing required fields: required"):
        storage_module._require_exact_keys(
            {"unexpected": 1},
            required=frozenset({"required"}),
            field="mapping",
        )
