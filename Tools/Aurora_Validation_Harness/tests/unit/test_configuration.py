"""Unit tests for immutable harness configuration and safe path resolution."""

from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

import pytest

from aurora_validation_harness.configuration import (
    MAX_RANDOM_SEED,
    RUN_OUTPUT_ROOT,
    SUPPORTED_CONFIGURATION_VERSION,
    ConfigurationError,
    ExecutionPolicy,
    HarnessConfiguration,
    RunMode,
    calculate_configuration_sha256,
    load_and_resolve_configuration,
    load_configuration,
    resolve_configuration,
)

pytestmark = pytest.mark.foundation

_CONFIGURATION_PATH = "Development/Validation/Aurora/Configuration/FOUND-001.json"
_BASELINE_PATH = "Development/Validation/Aurora/Configuration/baseline.json"
_FIXTURE_PATH = "Development/Validation/Aurora/Fixtures/FOUND-001/manifest.json"


def _execution_mapping(**changes: object) -> dict[str, object]:
    values: dict[str, object] = {
        "allow_output_overwrite": False,
        "deterministic": True,
        "network_access_enabled": False,
        "random_seed": 41001,
        "reset_before_run": True,
        "run_mode": RunMode.DRY_RUN.value,
        "strict_isolation": True,
        "telemetry_feedback_enabled": False,
    }
    values.update(changes)
    return values


def _policy(**changes: object) -> ExecutionPolicy:
    return ExecutionPolicy.from_mapping(_execution_mapping(**changes))


def _configuration_mapping(**changes: object) -> dict[str, object]:
    values: dict[str, object] = {
        "baseline_id": "AURORA-FOUNDATION-BASELINE-001",
        "baseline_manifest_path": _BASELINE_PATH,
        "configuration_id": "AURORA-CONFIG-FOUND-001-DRY",
        "configuration_version": SUPPORTED_CONFIGURATION_VERSION,
        "execution": _execution_mapping(),
        "fixture_manifest_path": _FIXTURE_PATH,
        "fixture_set_id": "AURORA-FIXTURE-FOUND-001-A",
        "output_root": RUN_OUTPUT_ROOT,
        "scenario_id": "AURORA-SCN-FOUND-001",
    }
    values.update(changes)
    return values


def _configuration(**changes: object) -> HarnessConfiguration:
    return HarnessConfiguration.from_mapping(_configuration_mapping(**changes))


def _signed_configuration(**changes: object) -> HarnessConfiguration:
    unsigned = _configuration(**changes)
    return replace(
        unsigned,
        configuration_sha256=calculate_configuration_sha256(unsigned),
    )


def _create_repository(tmp_path: Path) -> Path:
    repository_root = tmp_path / "repository"
    for relative_path in (_BASELINE_PATH, _FIXTURE_PATH):
        path = repository_root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}\n", encoding="utf-8")
    return repository_root


def _write_configuration(
    repository_root: Path,
    configuration: HarnessConfiguration,
) -> Path:
    path = repository_root / _CONFIGURATION_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(configuration.to_mapping(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


@pytest.mark.parametrize("run_mode", list(RunMode))
def test_execution_policy_accepts_every_governed_run_mode(run_mode: RunMode) -> None:
    policy = _policy(run_mode=run_mode.value)

    assert policy.run_mode is run_mode
    assert policy.to_mapping()["run_mode"] == run_mode.value


@pytest.mark.parametrize("random_seed", [0, MAX_RANDOM_SEED])
def test_execution_policy_accepts_seed_boundaries(random_seed: int) -> None:
    assert _policy(random_seed=random_seed).random_seed == random_seed


@pytest.mark.parametrize(
    ("change", "message"),
    [
        ({"deterministic": False}, "deterministic must be true"),
        ({"strict_isolation": False}, "strict_isolation must be true"),
        ({"reset_before_run": False}, "reset_before_run must be true"),
        ({"network_access_enabled": True}, "network_access_enabled must be false"),
        (
            {"telemetry_feedback_enabled": True},
            "telemetry_feedback_enabled must be false",
        ),
        ({"allow_output_overwrite": True}, "allow_output_overwrite must be false"),
    ],
)
def test_execution_policy_rejects_unsafe_controls(
    change: dict[str, object],
    message: str,
) -> None:
    with pytest.raises(ConfigurationError, match=message):
        _policy(**change)


@pytest.mark.parametrize("random_seed", [-1, MAX_RANDOM_SEED + 1])
def test_execution_policy_rejects_seed_outside_unsigned_64_bit_range(
    random_seed: int,
) -> None:
    with pytest.raises(ConfigurationError, match="random_seed must be between"):
        _policy(random_seed=random_seed)


@pytest.mark.parametrize("random_seed", [True, "41001", 4.5, None])
def test_execution_policy_rejects_non_integer_seed(random_seed: object) -> None:
    with pytest.raises(ConfigurationError, match=r"execution\.random_seed must be an integer"):
        _policy(random_seed=random_seed)


@pytest.mark.parametrize(
    "change",
    [
        {"deterministic": 1},
        {"strict_isolation": "true"},
        {"reset_before_run": None},
        {"network_access_enabled": 0},
        {"telemetry_feedback_enabled": "false"},
        {"allow_output_overwrite": []},
    ],
)
def test_execution_policy_rejects_non_boolean_controls(
    change: dict[str, object],
) -> None:
    with pytest.raises(ConfigurationError, match="must be a boolean"):
        _policy(**change)


def test_execution_policy_rejects_unknown_run_mode() -> None:
    with pytest.raises(ConfigurationError, match=r"unsupported execution\.run_mode"):
        _policy(run_mode="EXPERIMENTAL")


def test_execution_policy_rejects_unknown_field() -> None:
    with pytest.raises(ConfigurationError, match="unknown execution field"):
        _policy(hidden_override=True)


def test_execution_policy_rejects_missing_field() -> None:
    mapping = _execution_mapping()
    del mapping["random_seed"]

    with pytest.raises(ConfigurationError, match="missing execution field"):
        ExecutionPolicy.from_mapping(mapping)


def test_execution_policy_direct_constructor_checks_runtime_types() -> None:
    valid = _policy()

    with pytest.raises(ConfigurationError, match="run_mode must be a RunMode"):
        replace(valid, run_mode="DRY_RUN")
    with pytest.raises(ConfigurationError, match="random_seed must be an integer"):
        replace(valid, random_seed=True)
    with pytest.raises(ConfigurationError, match="deterministic must be a boolean"):
        replace(valid, deterministic=1)


def test_configuration_round_trips_through_stable_mapping() -> None:
    configuration = _configuration()

    reconstructed = HarnessConfiguration.from_mapping(configuration.to_mapping())

    assert reconstructed == configuration
    assert reconstructed.execution == _policy()
    assert reconstructed.configuration_sha256 is None


def test_configuration_hash_is_stable_and_excludes_declared_hash() -> None:
    unsigned = _configuration()
    calculated = calculate_configuration_sha256(unsigned)
    signed = replace(unsigned, configuration_sha256=calculated)

    assert len(calculated) == 64
    assert calculate_configuration_sha256(signed) == calculated


def test_configuration_hash_is_independent_of_json_key_order() -> None:
    original_mapping = _configuration_mapping()
    reversed_mapping = dict(reversed(tuple(original_mapping.items())))
    original = HarnessConfiguration.from_mapping(original_mapping)
    reordered = HarnessConfiguration.from_mapping(reversed_mapping)

    assert calculate_configuration_sha256(original) == calculate_configuration_sha256(reordered)


def test_configuration_hash_changes_when_control_data_changes() -> None:
    original = _configuration()
    changed = _configuration(fixture_set_id="AURORA-FIXTURE-FOUND-001-B")

    assert calculate_configuration_sha256(original) != calculate_configuration_sha256(changed)


@pytest.mark.parametrize(
    "identifier_field",
    ["configuration_id", "baseline_id", "fixture_set_id"],
)
@pytest.mark.parametrize("invalid_identifier", ["ab", "lowercase-id", "BAD ID"])
def test_configuration_rejects_invalid_identifiers(
    identifier_field: str,
    invalid_identifier: str,
) -> None:
    with pytest.raises(ConfigurationError, match="uppercase identifier characters"):
        _configuration(**{identifier_field: invalid_identifier})


@pytest.mark.parametrize(
    "scenario_id",
    ["AURORA-FOUND-001", "AURORA-SCN-FOUND-01", "aurora-scn-found-001"],
)
def test_configuration_rejects_noncanonical_scenario_id(scenario_id: str) -> None:
    with pytest.raises(ConfigurationError, match="scenario_id must match"):
        _configuration(scenario_id=scenario_id)


def test_configuration_rejects_unsupported_schema_version() -> None:
    with pytest.raises(ConfigurationError, match="unsupported configuration_version"):
        _configuration(configuration_version="2.0")


def test_configuration_rejects_shared_manifest_path() -> None:
    with pytest.raises(ConfigurationError, match="must be distinct"):
        _configuration(fixture_manifest_path=_BASELINE_PATH)


@pytest.mark.parametrize(
    "invalid_hash",
    ["0" * 63, "A" * 64, "not-a-hash"],
)
def test_configuration_rejects_malformed_declared_hash(invalid_hash: str) -> None:
    with pytest.raises(ConfigurationError, match="lowercase 64-character SHA-256"):
        _configuration(configuration_sha256=invalid_hash)


@pytest.mark.parametrize(
    "output_root",
    [RUN_OUTPUT_ROOT, f"{RUN_OUTPUT_ROOT}/FOUND-001", f"{RUN_OUTPUT_ROOT}/regression/001"],
)
def test_configuration_accepts_governed_output_locations(output_root: str) -> None:
    assert _configuration(output_root=output_root).output_root == output_root


@pytest.mark.parametrize(
    "output_root",
    ["Canon/Runs", "Development/Validation/Aurora/Run", f"{RUN_OUTPUT_ROOT}Archive"],
)
def test_configuration_rejects_output_outside_governed_root(output_root: str) -> None:
    with pytest.raises(ConfigurationError, match="output_root must be"):
        _configuration(output_root=output_root)


@pytest.mark.parametrize(
    "invalid_path",
    [
        "",
        "   ",
        " Development/manifest.json",
        "Development/manifest.json ",
        "../outside.json",
        "/absolute.json",
        "C:/drive.json",
        "Development\\manifest.json",
        "Development//manifest.json",
        "Development/./manifest.json",
        ".",
    ],
)
def test_configuration_rejects_unsafe_or_noncanonical_input_path(
    invalid_path: str,
) -> None:
    with pytest.raises(ConfigurationError):
        _configuration(baseline_manifest_path=invalid_path)


def test_configuration_rejects_unknown_top_level_field() -> None:
    mapping = _configuration_mapping(unexpected_control=True)

    with pytest.raises(ConfigurationError, match="unknown configuration field"):
        HarnessConfiguration.from_mapping(mapping)


def test_configuration_rejects_missing_top_level_field() -> None:
    mapping = _configuration_mapping()
    del mapping["fixture_set_id"]

    with pytest.raises(ConfigurationError, match="missing configuration field"):
        HarnessConfiguration.from_mapping(mapping)


@pytest.mark.parametrize("execution", [None, [], "policy"])
def test_configuration_rejects_non_object_execution(execution: object) -> None:
    with pytest.raises(ConfigurationError, match="execution must be a JSON object"):
        _configuration(execution=execution)


@pytest.mark.parametrize("invalid_value", [None, "", "   ", 42])
def test_configuration_rejects_invalid_required_string(invalid_value: object) -> None:
    with pytest.raises(ConfigurationError, match=r"configuration\.baseline_id"):
        _configuration(baseline_id=invalid_value)


@pytest.mark.parametrize("invalid_value", ["", "   ", 42])
def test_configuration_rejects_invalid_optional_hash_type(invalid_value: object) -> None:
    with pytest.raises(ConfigurationError, match=r"configuration\.configuration_sha256"):
        _configuration(configuration_sha256=invalid_value)


def test_configuration_direct_constructor_checks_runtime_types() -> None:
    valid = _configuration()

    with pytest.raises(ConfigurationError, match="execution must be an ExecutionPolicy"):
        replace(valid, execution={})
    with pytest.raises(ConfigurationError, match="configuration_id must be a string"):
        replace(valid, configuration_id=1)
    with pytest.raises(ConfigurationError, match="configuration_version must be a string"):
        replace(valid, configuration_version=1)
    with pytest.raises(ConfigurationError, match="scenario_id must be a string"):
        replace(valid, scenario_id=1)
    with pytest.raises(ConfigurationError, match="baseline_manifest_path must be a string"):
        replace(valid, baseline_manifest_path=[])
    with pytest.raises(ConfigurationError, match="baseline_manifest_path must not be empty"):
        replace(valid, baseline_manifest_path="")
    with pytest.raises(ConfigurationError, match="configuration_sha256 must be a string"):
        replace(valid, configuration_sha256=1)


def test_load_configuration_accepts_valid_signed_document(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    expected = _signed_configuration()
    path = _write_configuration(repository_root, expected)

    loaded = load_configuration(path)

    assert loaded == expected
    assert calculate_configuration_sha256(loaded) == loaded.configuration_sha256


def test_load_configuration_can_read_unsigned_draft_only_when_explicit(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    unsigned = _configuration()
    path = _write_configuration(repository_root, unsigned)

    with pytest.raises(ConfigurationError, match="configuration_sha256 is required"):
        load_configuration(path)

    assert load_configuration(path, require_hash=False) == unsigned


def test_load_configuration_rejects_tampered_signed_document(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    signed = _signed_configuration()
    mapping = signed.to_mapping()
    mapping["scenario_id"] = "AURORA-SCN-FOUND-002"
    path = repository_root / _CONFIGURATION_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(mapping), encoding="utf-8")

    with pytest.raises(ConfigurationError, match="does not match"):
        load_configuration(path)


@pytest.mark.parametrize("document", ["[]", "{broken json", '{"value": NaN}'])
def test_load_configuration_rejects_invalid_json_document(
    tmp_path: Path,
    document: str,
) -> None:
    path = tmp_path / "configuration.json"
    path.write_text(document, encoding="utf-8")

    with pytest.raises(ConfigurationError):
        load_configuration(path)


def test_load_configuration_rejects_invalid_utf8(tmp_path: Path) -> None:
    path = tmp_path / "configuration.json"
    path.write_bytes(b"\xff\xfe\x00")

    with pytest.raises(ConfigurationError, match="unable to load configuration"):
        load_configuration(path)


def test_load_configuration_rejects_missing_file(tmp_path: Path) -> None:
    with pytest.raises(ConfigurationError, match="unable to load configuration"):
        load_configuration(tmp_path / "missing.json")


def test_resolve_configuration_binds_controlled_paths_without_creating_output(
    tmp_path: Path,
) -> None:
    repository_root = _create_repository(tmp_path)

    resolved = resolve_configuration(repository_root, _configuration())

    assert resolved.repository_root == repository_root.resolve()
    assert resolved.baseline_manifest == (repository_root / _BASELINE_PATH).resolve()
    assert resolved.fixture_manifest == (repository_root / _FIXTURE_PATH).resolve()
    assert resolved.controlled_inputs == (
        resolved.baseline_manifest,
        resolved.fixture_manifest,
    )
    assert resolved.output_root == (repository_root / RUN_OUTPUT_ROOT).resolve()
    assert not resolved.output_root.exists()


def test_resolve_configuration_accepts_existing_output_directory(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    output_root = repository_root / RUN_OUTPUT_ROOT
    output_root.mkdir(parents=True)

    resolved = resolve_configuration(repository_root, _configuration())

    assert resolved.output_root == output_root.resolve()


def test_load_and_resolve_configuration_combines_both_operations(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    expected = _signed_configuration()
    path = _write_configuration(repository_root, expected)

    resolved = load_and_resolve_configuration(path, repository_root)

    assert resolved.configuration == expected
    assert resolved.controlled_inputs == (
        (repository_root / _BASELINE_PATH).resolve(),
        (repository_root / _FIXTURE_PATH).resolve(),
    )


def test_load_and_resolve_configuration_can_accept_unsigned_draft(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    unsigned = _configuration()
    path = _write_configuration(repository_root, unsigned)

    resolved = load_and_resolve_configuration(
        path,
        repository_root,
        require_hash=False,
    )

    assert resolved.configuration == unsigned


def test_resolve_configuration_rejects_missing_repository(tmp_path: Path) -> None:
    with pytest.raises(ConfigurationError, match="repository root cannot be resolved"):
        resolve_configuration(tmp_path / "missing", _configuration())


def test_resolve_configuration_rejects_repository_file(tmp_path: Path) -> None:
    repository_root = tmp_path / "repository"
    repository_root.write_text("not a directory", encoding="utf-8")

    with pytest.raises(ConfigurationError, match="repository root is not a directory"):
        resolve_configuration(repository_root, _configuration())


def test_resolve_configuration_rejects_missing_input_manifest(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    (repository_root / _BASELINE_PATH).unlink()

    with pytest.raises(ConfigurationError, match="unable to resolve baseline_manifest_path"):
        resolve_configuration(repository_root, _configuration())


def test_resolve_configuration_rejects_input_directory(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    input_directory = repository_root / "Development/Validation/Aurora/Fixtures/Input"
    input_directory.mkdir(parents=True)
    configuration = _configuration(
        fixture_manifest_path="Development/Validation/Aurora/Fixtures/Input"
    )

    with pytest.raises(ConfigurationError, match="fixture_manifest_path is not a file"):
        resolve_configuration(repository_root, configuration)


def test_resolve_configuration_rejects_output_file(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    output_root = repository_root / RUN_OUTPUT_ROOT
    output_root.parent.mkdir(parents=True, exist_ok=True)
    output_root.write_text("not a directory", encoding="utf-8")

    with pytest.raises(ConfigurationError, match="output_root is not a directory"):
        resolve_configuration(repository_root, _configuration())


def test_resolve_configuration_rejects_two_paths_to_same_manifest(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    fixture = repository_root / _FIXTURE_PATH
    fixture.unlink()
    try:
        fixture.symlink_to(repository_root / _BASELINE_PATH)
    except OSError as exc:
        pytest.skip(f"symbolic links unavailable: {exc}")

    with pytest.raises(ConfigurationError, match="resolve to the same file"):
        resolve_configuration(repository_root, _configuration())


def test_resolve_configuration_rejects_input_symlink_escape(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    outside = tmp_path / "outside.json"
    outside.write_text("{}", encoding="utf-8")
    baseline = repository_root / _BASELINE_PATH
    baseline.unlink()
    try:
        baseline.symlink_to(outside)
    except OSError as exc:
        pytest.skip(f"symbolic links unavailable: {exc}")

    with pytest.raises(ConfigurationError, match="escapes repository root"):
        resolve_configuration(repository_root, _configuration())


def test_resolve_configuration_rejects_output_symlink_escape(tmp_path: Path) -> None:
    repository_root = _create_repository(tmp_path)
    outside = tmp_path / "outside-runs"
    outside.mkdir()
    output_root = repository_root / RUN_OUTPUT_ROOT
    output_root.parent.mkdir(parents=True, exist_ok=True)
    try:
        output_root.symlink_to(outside, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symbolic links unavailable: {exc}")

    with pytest.raises(ConfigurationError, match="escapes repository root"):
        resolve_configuration(repository_root, _configuration())
