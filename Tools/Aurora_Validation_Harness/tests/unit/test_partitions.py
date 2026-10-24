"""Unit tests for sealed partition policy and capability-scoped fixture views."""

from __future__ import annotations

import hashlib
import json
from dataclasses import FrozenInstanceError, replace
from pathlib import Path

import pytest

from aurora_validation_harness.fixtures import (
    FIXTURE_ROOT,
    FixtureBundle,
    FixtureManifest,
    FixtureMediaType,
    FixturePartition,
    calculate_fixture_manifest_sha256,
    create_fixture_file,
    load_fixture_bundle,
)
from aurora_validation_harness.partitions import (
    AccessDecisionReason,
    AccessPrincipal,
    FixtureView,
    PartitionAccessError,
    PartitionedFixtureStore,
    PartitionError,
    ScopedFixtureArtifact,
    allowed_partitions_for,
    calculate_artifact_set_sha256,
    denied_partitions_for,
    evaluate_partition_access,
)

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_SCENARIO_DIRECTORY = f"{FIXTURE_ROOT}/FOUND-001"
_EXPECTED_POLICY: dict[AccessPrincipal, frozenset[FixturePartition]] = {
    AccessPrincipal.WORLD_RUNTIME: frozenset({FixturePartition.WORLD}),
    AccessPrincipal.AURORA_RUNTIME: frozenset({FixturePartition.AURORA}),
    AccessPrincipal.PLAYER_RUNTIME: frozenset({FixturePartition.PLAYER_PRIVATE}),
    AccessPrincipal.FUTURE_SCHEDULER: frozenset({FixturePartition.FUTURE}),
    AccessPrincipal.VALIDATOR: frozenset(FixturePartition),
}


def _relative_path(filename: str) -> str:
    return f"{_SCENARIO_DIRECTORY}/{filename}"


def _json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n").encode()


def _write_bytes(repository_root: Path, relative_path: str, content: bytes) -> Path:
    path = repository_root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def _build_bundle(
    repository_root: Path,
    *,
    world_location: str = "Cargo_Bay_7",
    fixture_set_id: str = "AURORA-FIXTURE-FOUND-001-A",
    include_expected: bool = True,
    extra_aurora_artifact: bool = False,
) -> FixtureBundle:
    definitions = []
    fixture_values: list[tuple[str, FixturePartition, object]] = [
        ("world-secret.json", FixturePartition.WORLD, {"location": world_location}),
        ("aurora-state.json", FixturePartition.AURORA, {"location": "UNKNOWN"}),
        (
            "player-private.json",
            FixturePartition.PLAYER_PRIVATE,
            {"knows_location": True},
        ),
        ("future-events.json", FixturePartition.FUTURE, {"events": []}),
        (
            "validator-oracle.json",
            FixturePartition.VALIDATOR,
            {"expected": "UNKNOWN"},
        ),
    ]
    if include_expected:
        fixture_values.append(
            (
                "expected-results.json",
                FixturePartition.EXPECTED_RESULTS,
                {"verdict": "PASS"},
            )
        )
    if extra_aurora_artifact:
        fixture_values.append(
            (
                "aurora-memory.json",
                FixturePartition.AURORA,
                {"last_known_location": "Docking_Ring"},
            )
        )

    for filename, partition, value in fixture_values:
        relative_path = _relative_path(filename)
        _write_bytes(repository_root, relative_path, _json_bytes(value))
        definitions.append(
            create_fixture_file(
                repository_root,
                relative_path,
                partition=partition,
                media_type=FixtureMediaType.JSON,
            )
        )

    unsigned = FixtureManifest(
        fixture_set_id=fixture_set_id,
        scenario_id="AURORA-SCN-FOUND-001",
        fixture_manifest_version="1.0",
        files=tuple(definitions),
    )
    signed = replace(
        unsigned,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(unsigned),
    )
    return load_fixture_bundle(repository_root, signed)


def _build_store(
    tmp_path: Path,
    **changes: object,
) -> PartitionedFixtureStore:
    bundle = _build_bundle(tmp_path / "repository", **changes)
    return PartitionedFixtureStore(bundle)


def _scoped_artifact(
    content: bytes = b'{"state":"ready"}',
    *,
    artifact_id: str = "AURORA-001",
    partition: FixturePartition = FixturePartition.AURORA,
    media_type: FixtureMediaType = FixtureMediaType.JSON,
) -> ScopedFixtureArtifact:
    return ScopedFixtureArtifact(
        artifact_id=artifact_id,
        partition=partition,
        media_type=media_type,
        content_sha256=hashlib.sha256(content).hexdigest(),
        size_bytes=len(content),
        content_bytes=content,
    )


def _view(
    principal: AccessPrincipal = AccessPrincipal.AURORA_RUNTIME,
    artifacts: tuple[ScopedFixtureArtifact, ...] | None = None,
) -> FixtureView:
    if artifacts is None:
        default_partition = next(iter(allowed_partitions_for(principal)))
        artifacts = (
            _scoped_artifact(
                artifact_id=f"{default_partition.value}-001",
                partition=default_partition,
            ),
        )
    return FixtureView(
        principal=principal,
        permitted_partitions=allowed_partitions_for(principal),
        artifacts=artifacts,
    )


@pytest.mark.parametrize("principal", list(AccessPrincipal))
def test_sealed_policy_matches_architectural_matrix(principal: AccessPrincipal) -> None:
    allowed = allowed_partitions_for(principal)

    assert allowed == _EXPECTED_POLICY[principal]
    assert denied_partitions_for(principal) == frozenset(FixturePartition) - allowed
    assert isinstance(allowed, frozenset)


@pytest.mark.parametrize("principal", list(AccessPrincipal))
@pytest.mark.parametrize("partition", list(FixturePartition))
def test_access_decision_matches_sealed_policy(
    principal: AccessPrincipal,
    partition: FixturePartition,
) -> None:
    decision = evaluate_partition_access(principal, partition)
    expected = partition in _EXPECTED_POLICY[principal]

    assert decision.principal is principal
    assert decision.partition is partition
    assert decision.granted is expected
    assert decision.reason is (
        AccessDecisionReason.AUTHORIZED_PARTITION
        if expected
        else AccessDecisionReason.PARTITION_DENIED
    )


def test_access_helpers_reject_invalid_runtime_types() -> None:
    with pytest.raises(PartitionError, match="principal must be an AccessPrincipal"):
        allowed_partitions_for("AURORA_RUNTIME")
    with pytest.raises(PartitionError, match="principal must be an AccessPrincipal"):
        denied_partitions_for("AURORA_RUNTIME")
    with pytest.raises(PartitionError, match="principal must be an AccessPrincipal"):
        evaluate_partition_access("AURORA_RUNTIME", FixturePartition.AURORA)
    with pytest.raises(PartitionError, match="partition must be a FixturePartition"):
        evaluate_partition_access(AccessPrincipal.AURORA_RUNTIME, "AURORA")


def test_access_decision_direct_constructor_enforces_policy() -> None:
    granted = evaluate_partition_access(
        AccessPrincipal.AURORA_RUNTIME,
        FixturePartition.AURORA,
    )

    with pytest.raises(PartitionError, match="principal must be an AccessPrincipal"):
        replace(granted, principal="AURORA_RUNTIME")
    with pytest.raises(PartitionError, match="partition must be a FixturePartition"):
        replace(granted, partition="AURORA")
    with pytest.raises(PartitionError, match="granted must be a boolean"):
        replace(granted, granted=1)
    with pytest.raises(PartitionError, match="reason must be an AccessDecisionReason"):
        replace(granted, reason="AUTHORIZED_PARTITION")
    with pytest.raises(PartitionError, match="does not match the sealed policy"):
        replace(granted, granted=False)
    with pytest.raises(PartitionError, match="does not match the sealed policy"):
        replace(granted, reason=AccessDecisionReason.PARTITION_DENIED)


def test_partition_access_error_is_a_permission_error() -> None:
    assert issubclass(PartitionAccessError, PermissionError)


@pytest.mark.parametrize(
    "artifact_id",
    [
        "",
        "AURORA-1",
        "AURORA-0001",
        "aurora-001",
        "AURORA/001",
        "AURORA 001",
        "AURORA-ABC",
    ],
)
def test_scoped_artifact_rejects_noncanonical_id(artifact_id: str) -> None:
    with pytest.raises(PartitionError, match="artifact_id must use"):
        _scoped_artifact(artifact_id=artifact_id)


def test_scoped_artifact_accepts_partition_derived_ids() -> None:
    for partition in FixturePartition:
        artifact = _scoped_artifact(
            artifact_id=f"{partition.value}-001",
            partition=partition,
        )
        assert artifact.artifact_id == f"{partition.value}-001"


def test_scoped_artifact_decodes_json_into_fresh_objects() -> None:
    content = b'{"nested":{"value":1}}'
    artifact = _scoped_artifact(content)

    first = artifact.decode_json_object()
    first["changed"] = True
    second = artifact.decode_json_object()

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
def test_scoped_artifact_decodes_text_media(
    media_type: FixtureMediaType,
    content: bytes,
) -> None:
    artifact = _scoped_artifact(
        content,
        artifact_id="AURORA-001",
        media_type=media_type,
    )

    assert artifact.decode_text() == content.decode()


def test_scoped_artifact_rejects_text_decode_for_binary() -> None:
    artifact = _scoped_artifact(
        b"\xff\x00",
        artifact_id="AURORA-001",
        media_type=FixtureMediaType.BINARY,
    )

    with pytest.raises(PartitionError, match="scoped artifact is not text"):
        artifact.decode_text()


def test_scoped_artifact_rejects_invalid_utf8_text() -> None:
    artifact = _scoped_artifact(
        b"\xff\xfe",
        artifact_id="AURORA-001",
        media_type=FixtureMediaType.TEXT,
    )

    with pytest.raises(PartitionError, match="not valid UTF-8"):
        artifact.decode_text()


@pytest.mark.parametrize("content", [b"{broken", b'{"value":NaN}', b"\xff"])
def test_scoped_artifact_rejects_invalid_json(content: bytes) -> None:
    artifact = _scoped_artifact(content)

    with pytest.raises(PartitionError, match="not valid JSON"):
        artifact.decode_json_object()


def test_scoped_artifact_rejects_non_object_json_root() -> None:
    artifact = _scoped_artifact(b"[]")

    with pytest.raises(PartitionError, match="root must be an object"):
        artifact.decode_json_object()


def test_scoped_artifact_rejects_json_decode_for_non_json_media() -> None:
    artifact = _scoped_artifact(b"{}", media_type=FixtureMediaType.TEXT)

    with pytest.raises(PartitionError, match="scoped artifact is not JSON"):
        artifact.decode_json_object()


def test_scoped_artifact_runtime_checks_and_integrity() -> None:
    valid = _scoped_artifact(b"{}")

    with pytest.raises(PartitionError, match="artifact_id must be a string"):
        replace(valid, artifact_id=1)
    with pytest.raises(PartitionError, match="partition must be a FixturePartition"):
        replace(valid, partition="AURORA")
    with pytest.raises(PartitionError, match="media_type must be a FixtureMediaType"):
        replace(valid, media_type="application/json")
    with pytest.raises(PartitionError, match="content_sha256 must be a string"):
        replace(valid, content_sha256=1)
    with pytest.raises(PartitionError, match="lowercase 64-character SHA-256"):
        replace(valid, content_sha256="A" * 64)
    with pytest.raises(PartitionError, match="size_bytes must be an integer"):
        replace(valid, size_bytes=True)
    with pytest.raises(PartitionError, match="size_bytes must not be negative"):
        replace(valid, size_bytes=-1)
    with pytest.raises(PartitionError, match="content_bytes must be bytes"):
        replace(valid, content_bytes=bytearray(b"{}"))
    with pytest.raises(PartitionError, match="scoped artifact size mismatch"):
        replace(valid, content_bytes=b"longer")
    with pytest.raises(PartitionError, match="scoped artifact hash mismatch"):
        replace(valid, content_bytes=b"[]")


def test_fixture_view_sorts_artifacts_and_exposes_only_opaque_ids() -> None:
    first = _scoped_artifact(
        b'{"memory":true}',
        artifact_id="AURORA-001",
    )
    second = _scoped_artifact(
        b'{"state":"ready"}',
        artifact_id="AURORA-002",
    )

    view = _view(artifacts=(second, first))

    assert view.available_artifact_ids == ("AURORA-001", "AURORA-002")
    assert len(view) == 2
    assert view.contains("AURORA-001")
    assert not view.contains("AURORA-999")
    assert view.artifact("AURORA-002") == second
    assert not hasattr(view, "fixture_set_id")
    assert not hasattr(view, "fixture_set_sha256")
    assert all(not hasattr(artifact, "path") for artifact in view.artifacts)
    assert all(not hasattr(artifact, "definition") for artifact in view.artifacts)


def test_fixture_view_denies_missing_and_forbidden_requests() -> None:
    view = _view()

    with pytest.raises(PartitionAccessError, match="fixture artifact is not available"):
        view.artifact("WORLD-001")
    with pytest.raises(PartitionAccessError, match="fixture artifact is not available"):
        view.artifact("AURORA-999")
    with pytest.raises(PartitionAccessError, match="partition is not available"):
        view.by_partition(FixturePartition.WORLD)
    with pytest.raises(PartitionError, match="artifact_id must use"):
        view.artifact("../world.json")
    with pytest.raises(PartitionError, match="partition must be a FixturePartition"):
        view.by_partition("WORLD")


def test_fixture_view_returns_only_authorized_partition() -> None:
    view = _view()

    assert view.by_partition(FixturePartition.AURORA) == view.artifacts


def test_fixture_view_direct_constructor_rejects_policy_expansion() -> None:
    valid = _view()

    with pytest.raises(PartitionError, match="principal must be an AccessPrincipal"):
        replace(valid, principal="AURORA_RUNTIME")
    with pytest.raises(PartitionError, match="permitted_partitions must be a frozenset"):
        replace(valid, permitted_partitions={FixturePartition.AURORA})
    with pytest.raises(PartitionError, match="permitted_partitions must be a frozenset"):
        replace(valid, permitted_partitions=frozenset({"AURORA"}))
    with pytest.raises(PartitionError, match="do not match the sealed policy"):
        replace(
            valid,
            permitted_partitions=frozenset({FixturePartition.AURORA, FixturePartition.WORLD}),
        )


def test_fixture_view_direct_constructor_rejects_invalid_artifacts() -> None:
    valid = _view()
    duplicate = (valid.artifacts[0], valid.artifacts[0])
    forbidden = _scoped_artifact(
        b"{}",
        artifact_id="WORLD-001",
        partition=FixturePartition.WORLD,
    )

    with pytest.raises(PartitionError, match="artifacts must be a tuple"):
        replace(valid, artifacts=[])
    with pytest.raises(PartitionError, match="artifacts must be a tuple"):
        replace(valid, artifacts=(object(),))
    with pytest.raises(PartitionError, match="duplicate artifact IDs"):
        replace(valid, artifacts=duplicate)
    with pytest.raises(PartitionError, match="outside its permitted partitions"):
        replace(valid, artifacts=(forbidden,))


def test_fixture_view_is_immutable() -> None:
    view = _view()

    with pytest.raises(FrozenInstanceError):
        view.principal = AccessPrincipal.VALIDATOR
    with pytest.raises(FrozenInstanceError):
        view.artifacts[0].content_bytes = b"tampered"


def test_artifact_set_hash_is_deterministic_and_order_independent() -> None:
    first = _scoped_artifact(b'{"a":1}', artifact_id="AURORA-001")
    second = _scoped_artifact(b'{"b":2}', artifact_id="AURORA-002")

    assert calculate_artifact_set_sha256((first, second)) == calculate_artifact_set_sha256(
        (second, first)
    )
    assert calculate_artifact_set_sha256(()) == calculate_artifact_set_sha256(())
    assert len(calculate_artifact_set_sha256((first,))) == 64


def test_artifact_set_hash_changes_with_visible_content() -> None:
    first = _scoped_artifact(b'{"state":1}')
    changed = _scoped_artifact(b'{"state":2}')

    assert calculate_artifact_set_sha256((first,)) != calculate_artifact_set_sha256((changed,))


def test_artifact_set_hash_rejects_invalid_collection() -> None:
    artifact = _scoped_artifact()

    with pytest.raises(PartitionError, match="artifacts must be a tuple"):
        calculate_artifact_set_sha256([artifact])
    with pytest.raises(PartitionError, match="artifacts must be a tuple"):
        calculate_artifact_set_sha256((object(),))
    with pytest.raises(PartitionError, match="duplicate artifact IDs"):
        calculate_artifact_set_sha256((artifact, artifact))


def test_store_exposes_provenance_but_runtime_view_does_not(tmp_path: Path) -> None:
    store = _build_store(tmp_path)
    aurora = store.view_for(AccessPrincipal.AURORA_RUNTIME)

    assert store.fixture_set_id == "AURORA-FIXTURE-FOUND-001-A"
    assert len(store.fixture_set_sha256) == 64
    assert not hasattr(aurora, "fixture_set_id")
    assert not hasattr(aurora, "fixture_set_sha256")


@pytest.mark.parametrize("principal", list(AccessPrincipal))
def test_store_issues_exact_least_privilege_view(
    tmp_path: Path,
    principal: AccessPrincipal,
) -> None:
    store = _build_store(tmp_path)
    view = store.view_for(principal)

    assert view.principal is principal
    assert view.permitted_partitions == _EXPECTED_POLICY[principal]
    assert all(artifact.partition in _EXPECTED_POLICY[principal] for artifact in view.artifacts)
    assert {artifact.partition for artifact in view.artifacts} <= _EXPECTED_POLICY[principal]


def test_scoped_ids_are_deterministic_with_multiple_partition_artifacts(
    tmp_path: Path,
) -> None:
    store = _build_store(tmp_path, extra_aurora_artifact=True)

    aurora = store.view_for(AccessPrincipal.AURORA_RUNTIME)
    validator = store.view_for(AccessPrincipal.VALIDATOR)

    assert aurora.available_artifact_ids == ("AURORA-001", "AURORA-002")
    assert (
        tuple(artifact.artifact_id for artifact in validator.by_partition(FixturePartition.AURORA))
        == aurora.available_artifact_ids
    )


def test_expected_results_are_visible_only_to_validator(tmp_path: Path) -> None:
    store = _build_store(tmp_path)

    for principal in AccessPrincipal:
        view = store.view_for(principal)
        expected = (
            view.by_partition(FixturePartition.EXPECTED_RESULTS)
            if (principal is AccessPrincipal.VALIDATOR)
            else ()
        )
        if principal is AccessPrincipal.VALIDATOR:
            assert len(expected) == 1
        else:
            with pytest.raises(PartitionAccessError):
                view.by_partition(FixturePartition.EXPECTED_RESULTS)


def test_hidden_world_mutation_cannot_change_aurora_capability(tmp_path: Path) -> None:
    first = _build_store(
        tmp_path / "first",
        world_location="Cargo_Bay_7",
        fixture_set_id="AURORA-FIXTURE-FOUND-001-A",
    )
    second = _build_store(
        tmp_path / "second",
        world_location="Medical_Deck_3",
        fixture_set_id="AURORA-FIXTURE-FOUND-001-B",
    )

    first_aurora = first.view_for(AccessPrincipal.AURORA_RUNTIME)
    second_aurora = second.view_for(AccessPrincipal.AURORA_RUNTIME)
    first_world = first.view_for(AccessPrincipal.WORLD_RUNTIME)
    second_world = second.view_for(AccessPrincipal.WORLD_RUNTIME)
    first_validator = first.view_for(AccessPrincipal.VALIDATOR)
    second_validator = second.view_for(AccessPrincipal.VALIDATOR)

    assert first.fixture_set_id != second.fixture_set_id
    assert first.fixture_set_sha256 != second.fixture_set_sha256
    assert first_aurora.available_artifact_ids == second_aurora.available_artifact_ids
    assert first_aurora.artifacts == second_aurora.artifacts
    assert first_aurora.accessible_state_sha256 == second_aurora.accessible_state_sha256
    assert first_world.accessible_state_sha256 != second_world.accessible_state_sha256
    assert first_validator.accessible_state_sha256 != second_validator.accessible_state_sha256


def test_partition_hash_tracks_only_selected_partition(tmp_path: Path) -> None:
    first = _build_store(tmp_path / "first", world_location="Cargo_Bay_7")
    second = _build_store(tmp_path / "second", world_location="Medical_Deck_3")

    assert first.partition_sha256(FixturePartition.AURORA) == second.partition_sha256(
        FixturePartition.AURORA
    )
    assert first.partition_sha256(FixturePartition.WORLD) != second.partition_sha256(
        FixturePartition.WORLD
    )


def test_partition_hash_supports_absent_optional_partition(tmp_path: Path) -> None:
    store = _build_store(tmp_path, include_expected=False)

    assert store.partition_sha256(
        FixturePartition.EXPECTED_RESULTS
    ) == calculate_artifact_set_sha256(())


def test_store_rejects_invalid_bundle_and_partition(tmp_path: Path) -> None:
    store = _build_store(tmp_path)

    with pytest.raises(PartitionError, match="bundle must be a FixtureBundle"):
        PartitionedFixtureStore(object())
    with pytest.raises(PartitionError, match="principal must be an AccessPrincipal"):
        store.view_for("AURORA_RUNTIME")
    with pytest.raises(PartitionError, match="partition must be a FixturePartition"):
        store.partition_sha256("AURORA")
