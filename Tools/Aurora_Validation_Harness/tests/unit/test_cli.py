"""Unit tests for the fail-closed Aurora validation command-line boundary."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import runpy
import sys
import warnings
from collections.abc import Mapping
from dataclasses import FrozenInstanceError, dataclass, replace
from pathlib import Path
from typing import Any

import pytest

from aurora_validation_harness import __version__
from aurora_validation_harness import cli as cli_module
from aurora_validation_harness.assertions import (
    AssertionSeverity,
    InvariantClass,
    SnapshotAssertionOperator,
    create_snapshot_assertion,
)
from aurora_validation_harness.baseline import (
    BaselineManifest,
    BaselineState,
    ManifestError,
    VerificationStatus,
    calculate_manifest_sha256,
)
from aurora_validation_harness.cli import (
    CLI_PROGRAM_NAME,
    SUPPORTED_CLI_SCHEMA_VERSION,
    CliError,
    CliExitCode,
    CliRunContext,
    create_argument_parser,
    main,
    run_cli,
)
from aurora_validation_harness.configuration import (
    RUN_OUTPUT_ROOT,
    SUPPORTED_CONFIGURATION_VERSION,
    ConfigurationError,
    ExecutionPolicy,
    HarnessConfiguration,
    RunMode,
    calculate_configuration_sha256,
)
from aurora_validation_harness.events import EventSchedule
from aurora_validation_harness.fixtures import (
    SUPPORTED_FIXTURE_MANIFEST_VERSION,
    FixtureArtifact,
    FixtureBundle,
    FixtureError,
    FixtureFile,
    FixtureManifest,
    FixtureMediaType,
    FixturePartition,
    calculate_fixture_manifest_sha256,
    create_fixture_file,
)
from aurora_validation_harness.harness import (
    AuroraResetRequest,
    AuroraStepRequest,
    HarnessError,
    HarnessFailureReason,
    HarnessPhase,
    HarnessRunPlan,
    HarnessStep,
    PlannedAssertion,
)
from aurora_validation_harness.snapshots import SnapshotPhase
from aurora_validation_harness.verdicts import create_verdict_definition

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_RUN_ID = "AURORA-RUN-FOUND-CLI-001"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"
_BASELINE_ID = "AURORA-FOUNDATION-BASELINE-001"
_FIXTURE_SET_ID = "AURORA-FIXTURE-FOUND-001-A"
_BASELINE_PATH = "Development/Validation/Aurora/Baseline/baseline.json"
_FIXTURE_MANIFEST_PATH = "Development/Validation/Aurora/Fixtures/FOUND-001/fixture-manifest.json"
_CONFIGURATION_PATH = "Development/Validation/Aurora/Configuration/FOUND-001.json"

_PARTITION_PAYLOADS: dict[FixturePartition, dict[str, object]] = {
    FixturePartition.WORLD: {"world_canary": "WORLD-SECRET-CANARY"},
    FixturePartition.AURORA: {"known_location": "UNKNOWN"},
    FixturePartition.PLAYER_PRIVATE: {"player_canary": "PLAYER-SECRET-CANARY"},
    FixturePartition.FUTURE: {"future_canary": "FUTURE-SECRET-CANARY"},
    FixturePartition.VALIDATOR: {"validator_canary": "VALIDATOR-SECRET-CANARY"},
}


@dataclass(frozen=True, slots=True)
class RepositoryCase:
    """Physical, hash-bound repository inputs for one CLI invocation."""

    root: Path
    configuration_path: Path
    baseline_path: Path
    fixture_manifest_path: Path


class RecordingRuntime:
    """Minimal deterministic runtime satisfying the executable interface."""

    reset_requests: list[AuroraResetRequest]
    step_requests: list[AuroraStepRequest]

    def __init__(self) -> None:
        self.reset_requests = []
        self.step_requests = []

    def reset(self, request: AuroraResetRequest, /) -> Mapping[str, object]:
        self.reset_requests.append(request)
        return {"ready": True, "tick": request.initial_tick}

    def advance(self, request: AuroraStepRequest, /) -> Mapping[str, object]:
        self.step_requests.append(request)
        return {"ready": True, "tick": request.through_tick}


class FactoryContainer:
    """Public nested attribute used to qualify dotted factory resolution."""

    @staticmethod
    def factory() -> RecordingRuntime:
        return RecordingRuntime()


NOT_CALLABLE_FACTORY = 17


def valid_plan_factory(context: CliRunContext) -> HarnessRunPlan:
    """Module-level factory resolved through the real dynamic-import boundary."""

    return _minimal_plan(context)


def failing_plan_factory(_context: CliRunContext) -> HarnessRunPlan:
    raise RuntimeError("plan factory exploded")


def invalid_plan_factory(_context: CliRunContext) -> object:
    return object()


def valid_runtime_factory() -> RecordingRuntime:
    return RecordingRuntime()


def failing_runtime_factory() -> RecordingRuntime:
    raise RuntimeError("runtime factory exploded")


def invalid_runtime_factory() -> object:
    return object()


def _module_spec(attribute: str) -> str:
    return f"{__name__}:{attribute}"


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def _baseline_mapping(manifest: BaselineManifest) -> dict[str, object]:
    return manifest.hash_payload() | {"manifest_sha256": manifest.manifest_sha256}


def _create_repository(
    tmp_path: Path,
    *,
    baseline_id: str = _BASELINE_ID,
    baseline_state: BaselineState = BaselineState.EXECUTION_BASELINE_READY,
    fixture_set_id: str = _FIXTURE_SET_ID,
    fixture_scenario_id: str = _SCENARIO_ID,
    run_mode: RunMode = RunMode.DRY_RUN,
) -> RepositoryCase:
    root = tmp_path / "repository"
    root.mkdir(parents=True)

    unsigned_baseline = BaselineManifest(
        baseline_id=baseline_id,
        baseline_state=baseline_state,
        manifest_version="1.0",
        files=(),
    )
    baseline = replace(
        unsigned_baseline,
        manifest_sha256=calculate_manifest_sha256(unsigned_baseline),
    )
    baseline_path = root / _BASELINE_PATH
    _write_json(baseline_path, _baseline_mapping(baseline))

    definitions: list[FixtureFile] = []
    fixture_directory = "Development/Validation/Aurora/Fixtures/FOUND-001"
    for partition, payload in _PARTITION_PAYLOADS.items():
        filename = partition.value.lower().replace("_", "-") + ".json"
        relative_path = f"{fixture_directory}/{filename}"
        _write_json(root / relative_path, payload)
        definitions.append(
            create_fixture_file(
                root,
                relative_path,
                partition=partition,
                media_type=FixtureMediaType.JSON,
            )
        )
    unsigned_fixture_manifest = FixtureManifest(
        fixture_set_id=fixture_set_id,
        scenario_id=fixture_scenario_id,
        fixture_manifest_version=SUPPORTED_FIXTURE_MANIFEST_VERSION,
        files=tuple(definitions),
    )
    fixture_manifest = replace(
        unsigned_fixture_manifest,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(unsigned_fixture_manifest),
    )
    fixture_manifest_path = root / _FIXTURE_MANIFEST_PATH
    _write_json(fixture_manifest_path, fixture_manifest.to_mapping())

    execution = ExecutionPolicy(
        run_mode=run_mode,
        random_seed=41001,
        deterministic=True,
        strict_isolation=True,
        reset_before_run=True,
        network_access_enabled=False,
        telemetry_feedback_enabled=False,
        allow_output_overwrite=False,
    )
    unsigned_configuration = HarnessConfiguration(
        configuration_id="AURORA-CONFIG-FOUND-001-CLI",
        configuration_version=SUPPORTED_CONFIGURATION_VERSION,
        scenario_id=_SCENARIO_ID,
        baseline_id=_BASELINE_ID,
        baseline_manifest_path=_BASELINE_PATH,
        fixture_set_id=_FIXTURE_SET_ID,
        fixture_manifest_path=_FIXTURE_MANIFEST_PATH,
        output_root=RUN_OUTPUT_ROOT,
        execution=execution,
    )
    configuration = replace(
        unsigned_configuration,
        configuration_sha256=calculate_configuration_sha256(unsigned_configuration),
    )
    configuration_path = root / _CONFIGURATION_PATH
    _write_json(configuration_path, configuration.to_mapping())
    return RepositoryCase(
        root=root,
        configuration_path=configuration_path,
        baseline_path=baseline_path,
        fixture_manifest_path=fixture_manifest_path,
    )


def _preflight_arguments(case: RepositoryCase) -> tuple[str, ...]:
    return (
        "preflight",
        "--repository-root",
        str(case.root),
        "--configuration",
        str(case.configuration_path),
    )


def _run_arguments(case: RepositoryCase) -> tuple[str, ...]:
    return (
        "run",
        "--repository-root",
        str(case.root),
        "--configuration",
        str(case.configuration_path),
        "--plan-factory",
        _module_spec("valid_plan_factory"),
        "--runtime-factory",
        _module_spec("valid_runtime_factory"),
    )


def _load_context(case: RepositoryCase) -> CliRunContext:
    return cli_module._load_run_context(
        repository_root=case.root,
        configuration_path=case.configuration_path,
    )


def _minimal_plan(context: CliRunContext) -> HarnessRunPlan:
    assertion = create_snapshot_assertion(
        assertion_id="ASSERTION-FOUND-CLI-001",
        invariant_id="AURORA-INFO-CLI-001",
        invariant_class=InvariantClass.HARD,
        severity=AssertionSeverity.S4,
        operator=SnapshotAssertionOperator.EXISTS,
        path="/ready",
    )
    planned = PlannedAssertion("RESULT-FOUND-CLI-001", assertion)
    verdict_definition = create_verdict_definition(
        verdict_definition_id="VERDICT-DEFINITION-FOUND-CLI-001",
        scenario_id=_SCENARIO_ID,
        primary_run_id=_RUN_ID,
        required_assertion_ids=(assertion.assertion_id,),
        minimum_finding_count=1,
    )
    return HarnessRunPlan(
        package_id="PACKAGE-FOUND-CLI-001",
        run_id=_RUN_ID,
        resolved_configuration=context.resolved_configuration,
        baseline_verification=context.baseline_verification,
        fixture_bundle=context.fixture_bundle,
        event_schedule=EventSchedule("AURORA-EVENTS-FOUND-CLI-001", ()),
        channel_definitions=(),
        initial_tick=0,
        initial_assertions=(planned,),
        steps=(HarnessStep("STEP-FOUND-CLI-FINAL", 0, SnapshotPhase.FINAL),),
        verdict_definition=verdict_definition,
    )


def _invoke(arguments: tuple[str, ...]) -> tuple[int, dict[str, object], str]:
    stdout = io.StringIO()
    stderr = io.StringIO()
    code = run_cli(arguments, stdout=stdout, stderr=stderr)
    selected = stdout.getvalue() if stdout.getvalue() else stderr.getvalue()
    decoded = json.loads(selected)
    assert isinstance(decoded, dict)
    return code, decoded, stderr.getvalue()


def _assert_error(
    result: dict[str, object],
    *,
    category: str,
    exit_code: CliExitCode,
) -> dict[str, object]:
    assert result["cli_schema_version"] == SUPPORTED_CLI_SCHEMA_VERSION
    assert result["status"] == "ERROR"
    error = result["error"]
    assert isinstance(error, dict)
    assert error["category"] == category
    assert error["exit_code"] == int(exit_code)
    return error


def _replace_plan(plan: HarnessRunPlan, **changes: object) -> HarnessRunPlan:
    return replace(plan, **changes)  # type: ignore[arg-type]


def _raising_context_loader(exception: Exception) -> Any:
    def loader(**_kwargs: object) -> CliRunContext:
        raise exception

    return loader


def test_public_constants_and_exit_codes_are_stable() -> None:
    assert SUPPORTED_CLI_SCHEMA_VERSION == "1.0"
    assert CLI_PROGRAM_NAME == "aurora-validation-harness"
    assert {item.name: int(item) for item in CliExitCode} == {
        "SUCCESS": 0,
        "USAGE": 2,
        "CONFIGURATION_INVALID": 10,
        "BASELINE_BLOCKED": 11,
        "BASELINE_INVALID": 12,
        "FIXTURE_INVALID": 13,
        "ADAPTER_INVALID": 14,
        "PLAN_INVALID": 15,
        "HARNESS_FAILED": 16,
        "INTERNAL_ERROR": 70,
    }


def test_cli_error_is_structured_detached_and_immutable() -> None:
    source_details: dict[str, object] = {"issue_codes": ["HASH-MISMATCH"]}
    error = CliError(
        CliExitCode.BASELINE_INVALID,
        "BASELINE_INVALID",
        "baseline rejected",
        details=source_details,
    )
    source_details["tampered"] = True

    assert str(error) == "BASELINE_INVALID: baseline rejected"
    assert error.exit_code is CliExitCode.BASELINE_INVALID
    assert error.category == "BASELINE_INVALID"
    assert error.detail == "baseline rejected"
    assert "tampered" not in error.details
    assert error.to_mapping() == {
        "category": "BASELINE_INVALID",
        "details": {"issue_codes": ["HASH-MISMATCH"]},
        "exit_code": 12,
        "message": "baseline rejected",
    }
    with pytest.raises(TypeError):
        error.details["tampered"] = True  # type: ignore[index]


@pytest.mark.parametrize(
    ("values", "message"),
    [
        ((CliExitCode.SUCCESS, "ERROR", "message"), "non-success"),
        ((17, "ERROR", "message"), "non-success"),
        ((CliExitCode.USAGE, "", "message"), "uppercase"),
        ((CliExitCode.USAGE, "lowercase", "message"), "uppercase"),
        ((CliExitCode.USAGE, 7, "message"), "uppercase"),
        ((CliExitCode.USAGE, "ERROR", " "), "non-empty"),
        ((CliExitCode.USAGE, "ERROR", 7), "non-empty"),
    ],
)
def test_cli_error_rejects_invalid_core_fields(
    values: tuple[object, object, object],
    message: str,
) -> None:
    with pytest.raises(TypeError, match=message):
        CliError(*values)  # type: ignore[arg-type]


@pytest.mark.parametrize("details", [[], {"bad": object()}, {"bad": float("nan")}])
def test_cli_error_rejects_invalid_or_noncanonical_details(details: object) -> None:
    with pytest.raises(TypeError):
        CliError(
            CliExitCode.INTERNAL_ERROR,
            "INTERNAL_ERROR",
            "invalid details",
            details=details,  # type: ignore[arg-type]
        )


def test_context_round_trips_only_redacted_preflight_data(tmp_path: Path) -> None:
    context = _load_context(_create_repository(tmp_path))
    mapping = context.to_mapping()
    serialized = json.dumps(mapping)

    assert mapping["scenario_id"] == _SCENARIO_ID
    assert mapping["output_root"] == RUN_OUTPUT_ROOT
    fixtures = mapping["fixtures"]
    assert isinstance(fixtures, dict)
    assert fixtures["artifact_count"] == 5
    assert len(str(fixtures["fixture_manifest_sha256"])) == 64
    assert "WORLD-SECRET-CANARY" not in serialized
    assert "VALIDATOR-SECRET-CANARY" not in serialized
    assert str(context.resolved_configuration.repository_root) not in serialized
    with pytest.raises(FrozenInstanceError):
        context.fixture_bundle = object()  # type: ignore[assignment,misc]


def test_context_rejects_invalid_runtime_types(tmp_path: Path) -> None:
    context = _load_context(_create_repository(tmp_path))
    cases: tuple[tuple[object, object, object], ...] = (
        (object(), context.baseline_verification, context.fixture_bundle),
        (context.resolved_configuration, object(), context.fixture_bundle),
        (context.resolved_configuration, context.baseline_verification, object()),
    )
    for values in cases:
        with pytest.raises(TypeError):
            CliRunContext(*values)  # type: ignore[arg-type]


def test_context_rejects_cross_identity_and_repository_mismatches(tmp_path: Path) -> None:
    context = _load_context(_create_repository(tmp_path))
    configuration = context.resolved_configuration.configuration
    wrong_id_manifest = replace(
        context.fixture_bundle.manifest,
        fixture_set_id="AURORA-FIXTURE-FOUND-001-B",
    )
    wrong_scenario_manifest = replace(
        context.fixture_bundle.manifest,
        scenario_id="AURORA-SCN-OTHER-001",
    )
    cases = (
        (
            context.resolved_configuration,
            replace(context.baseline_verification, status=VerificationStatus.BLOCKED),
            context.fixture_bundle,
            "VERIFIED",
        ),
        (
            context.resolved_configuration,
            replace(context.baseline_verification, baseline_id="BASELINE-OTHER-001"),
            context.fixture_bundle,
            "baseline verification",
        ),
        (
            context.resolved_configuration,
            context.baseline_verification,
            replace(context.fixture_bundle, manifest=wrong_id_manifest),
            "fixture bundle",
        ),
        (
            context.resolved_configuration,
            context.baseline_verification,
            replace(context.fixture_bundle, manifest=wrong_scenario_manifest),
            "fixture scenario",
        ),
        (
            context.resolved_configuration,
            context.baseline_verification,
            replace(context.fixture_bundle, repository_root=tmp_path / "other"),
            "repository root",
        ),
    )
    assert configuration.fixture_set_id == _FIXTURE_SET_ID
    for resolved, baseline, bundle, message in cases:
        with pytest.raises(ValueError, match=message):
            CliRunContext(resolved, baseline, bundle)


def test_argument_parser_defines_preflight_run_help_and_version(
    capsys: pytest.CaptureFixture[str],
) -> None:
    parser = create_argument_parser()
    preflight = parser.parse_args(["preflight", "--configuration", "config.json"])
    run = parser.parse_args(
        [
            "run",
            "--configuration",
            "config.json",
            "--plan-factory",
            "scenario:plan",
            "--runtime-factory",
            "runtime:create",
        ]
    )
    assert preflight.command == "preflight"
    assert preflight.repository_root == "."
    assert run.command == "run"
    assert run.plan_factory == "scenario:plan"
    assert run.runtime_factory == "runtime:create"

    with pytest.raises(SystemExit) as version:
        parser.parse_args(["--version"])
    assert version.value.code == 0
    assert capsys.readouterr().out == f"{CLI_PROGRAM_NAME} {__version__}\n"

    with pytest.raises(SystemExit) as help_exit:
        parser.parse_args(["--help"])
    assert help_exit.value.code == 0
    assert "preflight" in capsys.readouterr().out


def test_argument_errors_use_json_and_never_touch_stdout() -> None:
    code, result, stderr = _invoke(())
    error = _assert_error(result, category="CLI_USAGE", exit_code=CliExitCode.USAGE)
    assert code == int(CliExitCode.USAGE)
    assert "required" in str(error["message"])
    assert stderr


def test_preflight_command_verifies_real_repository_and_redacts_contents(tmp_path: Path) -> None:
    case = _create_repository(tmp_path)
    stdout = io.StringIO()
    stderr = io.StringIO()

    code = run_cli(_preflight_arguments(case), stdout=stdout, stderr=stderr)
    result = json.loads(stdout.getvalue())

    assert code == int(CliExitCode.SUCCESS)
    assert stderr.getvalue() == ""
    assert result["status"] == "VERIFIED"
    assert result["command"] == "preflight"
    assert stdout.getvalue().endswith("\n")
    assert stdout.getvalue().strip() == json.dumps(
        result,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    assert all(
        canary not in stdout.getvalue()
        for canary in (
            "WORLD-SECRET-CANARY",
            "PLAYER-SECRET-CANARY",
            "FUTURE-SECRET-CANARY",
            "VALIDATOR-SECRET-CANARY",
        )
    )


def test_preflight_uses_default_process_streams_and_main_reads_sys_argv(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    case = _create_repository(tmp_path)
    monkeypatch.setattr(sys, "argv", [CLI_PROGRAM_NAME, *_preflight_arguments(case)])

    assert main() == int(CliExitCode.SUCCESS)
    captured = capsys.readouterr()
    assert json.loads(captured.out)["status"] == "VERIFIED"
    assert captured.err == ""


def test_run_command_executes_real_factories_harness_and_storage(tmp_path: Path) -> None:
    case = _create_repository(tmp_path)
    code, result, stderr = _invoke(_run_arguments(case))

    assert code == int(CliExitCode.SUCCESS)
    assert stderr == ""
    assert result["status"] == "COMPLETE"
    assert result["command"] == "run"
    summary = result["result"]
    assert isinstance(summary, dict)
    assert summary["run_id"] == _RUN_ID
    assert summary["verdict_outcome"] == "PASS"
    assert summary["snapshot_count"] == 2
    assert (case.root / RUN_OUTPUT_ROOT / _RUN_ID).is_dir()
    serialized = json.dumps(result)
    assert "WORLD-SECRET-CANARY" not in serialized
    assert str(case.root) not in serialized


def test_module_execution_delegates_to_main_and_exits_successfully(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    case = _create_repository(tmp_path)
    monkeypatch.setattr(sys, "argv", [CLI_PROGRAM_NAME, *_preflight_arguments(case)])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        with pytest.raises(SystemExit) as exit_info:
            runpy.run_module("aurora_validation_harness.cli", run_name="__main__")
    assert exit_info.value.code == 0
    assert json.loads(capsys.readouterr().out)["status"] == "VERIFIED"


def test_main_delegates_explicit_arguments(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: list[object] = []

    def fake_run_cli(argv: object) -> int:
        captured.append(argv)
        return 27

    monkeypatch.setattr(cli_module, "run_cli", fake_run_cli)
    arguments = ("preflight", "--configuration", "config.json")
    assert main(arguments) == 27
    assert captured == [arguments]


def test_run_cli_rejects_unreachable_unsupported_command(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    context = _load_context(_create_repository(tmp_path))

    class FakeParser:
        def parse_args(self, _argv: object) -> argparse.Namespace:
            return argparse.Namespace(
                command="unsupported",
                repository_root=str(context.resolved_configuration.repository_root),
                configuration="ignored.json",
            )

    monkeypatch.setattr(cli_module, "create_argument_parser", FakeParser)
    monkeypatch.setattr(cli_module, "_load_run_context", lambda **_kwargs: context)
    stdout = io.StringIO()
    stderr = io.StringIO()
    code = run_cli((), stdout=stdout, stderr=stderr)
    result = json.loads(stderr.getvalue())
    _assert_error(result, category="CLI_USAGE", exit_code=CliExitCode.USAGE)
    assert code == int(CliExitCode.USAGE)
    assert stdout.getvalue() == ""


def test_configuration_manifest_and_fixture_exceptions_map_to_stable_exit_codes(
    tmp_path: Path,
) -> None:
    missing = tmp_path / "missing.json"
    code, result, _ = _invoke(
        (
            "preflight",
            "--repository-root",
            str(tmp_path),
            "--configuration",
            str(missing),
        )
    )
    _assert_error(
        result,
        category="CONFIGURATION_INVALID",
        exit_code=CliExitCode.CONFIGURATION_INVALID,
    )
    assert code == int(CliExitCode.CONFIGURATION_INVALID)

    malformed = _create_repository(tmp_path / "manifest")
    malformed.baseline_path.write_text("[]", encoding="utf-8")
    code, result, _ = _invoke(_preflight_arguments(malformed))
    _assert_error(
        result,
        category="BASELINE_INVALID",
        exit_code=CliExitCode.BASELINE_INVALID,
    )
    assert code == int(CliExitCode.BASELINE_INVALID)

    corrupt = _create_repository(tmp_path / "fixture")
    fixture_file = next(
        path
        for path in corrupt.fixture_manifest_path.parent.glob("*.json")
        if path != corrupt.fixture_manifest_path
    )
    fixture_file.write_text('{"tampered":true}', encoding="utf-8")
    code, result, _ = _invoke(_preflight_arguments(corrupt))
    _assert_error(
        result,
        category="FIXTURE_INVALID",
        exit_code=CliExitCode.FIXTURE_INVALID,
    )
    assert code == int(CliExitCode.FIXTURE_INVALID)


@pytest.mark.parametrize(
    ("baseline_state", "expected_code"),
    [
        (BaselineState.PRE_FREEZE, CliExitCode.BASELINE_BLOCKED),
        (BaselineState.SUPERSEDED, CliExitCode.BASELINE_BLOCKED),
    ],
)
def test_nonactive_baselines_are_blocked_with_issue_codes(
    tmp_path: Path,
    baseline_state: BaselineState,
    expected_code: CliExitCode,
) -> None:
    case = _create_repository(tmp_path, baseline_state=baseline_state)
    code, result, _ = _invoke(_preflight_arguments(case))
    error = _assert_error(result, category="BASELINE_BLOCKED", exit_code=expected_code)
    details = error["details"]
    assert isinstance(details, dict)
    assert details["status"] == "BLOCKED"
    assert "BASELINE_NOT_ACTIVE" in details["issue_codes"]
    assert code == int(expected_code)


def test_invalid_baseline_hash_uses_invalid_not_blocked(tmp_path: Path) -> None:
    case = _create_repository(tmp_path)
    mapping = json.loads(case.baseline_path.read_text(encoding="utf-8"))
    mapping["manifest_sha256"] = "f" * 64
    _write_json(case.baseline_path, mapping)

    code, result, _ = _invoke(_preflight_arguments(case))
    error = _assert_error(
        result,
        category="BASELINE_INVALID",
        exit_code=CliExitCode.BASELINE_INVALID,
    )
    details = error["details"]
    assert isinstance(details, dict)
    assert details["status"] == "INVALID"
    assert "MANIFEST_HASH_MISMATCH" in details["issue_codes"]
    assert code == int(CliExitCode.BASELINE_INVALID)


def test_baseline_identity_mismatch_is_invalid(tmp_path: Path) -> None:
    case = _create_repository(tmp_path, baseline_id="AURORA-BASELINE-OTHER-001")
    code, result, _ = _invoke(_preflight_arguments(case))
    error = _assert_error(
        result,
        category="BASELINE_INVALID",
        exit_code=CliExitCode.BASELINE_INVALID,
    )
    assert isinstance(error["message"], str)
    assert "does not match" in error["message"]
    assert code == int(CliExitCode.BASELINE_INVALID)


def test_formal_mode_requires_formal_active_baseline(tmp_path: Path) -> None:
    blocked = _create_repository(tmp_path / "blocked", run_mode=RunMode.FORMAL)
    code, result, _ = _invoke(_preflight_arguments(blocked))
    error = _assert_error(
        result,
        category="BASELINE_BLOCKED",
        exit_code=CliExitCode.BASELINE_BLOCKED,
    )
    assert isinstance(error["message"], str)
    assert "FORMAL_EXECUTION_ACTIVE" in error["message"]
    assert code == int(CliExitCode.BASELINE_BLOCKED)

    active = _create_repository(
        tmp_path / "active",
        run_mode=RunMode.FORMAL,
        baseline_state=BaselineState.FORMAL_EXECUTION_ACTIVE,
    )
    code, result, _ = _invoke(_preflight_arguments(active))
    assert code == 0
    assert result["status"] == "VERIFIED"


@pytest.mark.parametrize(
    ("repository_changes", "message"),
    [
        ({"fixture_set_id": "AURORA-FIXTURE-OTHER-001"}, "fixture bundle"),
        ({"fixture_scenario_id": "AURORA-SCN-OTHER-001"}, "fixture scenario"),
    ],
)
def test_fixture_identity_mismatches_are_invalid(
    tmp_path: Path,
    repository_changes: dict[str, object],
    message: str,
) -> None:
    case = _create_repository(tmp_path, **repository_changes)  # type: ignore[arg-type]
    code, result, _ = _invoke(_preflight_arguments(case))
    error = _assert_error(
        result,
        category="FIXTURE_INVALID",
        exit_code=CliExitCode.FIXTURE_INVALID,
    )
    assert isinstance(error["message"], str)
    assert message in error["message"]
    assert code == int(CliExitCode.FIXTURE_INVALID)


def test_factory_loader_resolves_public_nested_callable() -> None:
    factory = cli_module._load_factory(
        _module_spec("FactoryContainer.factory"),
        field="runtime_factory",
    )
    assert isinstance(factory(), RecordingRuntime)


@pytest.mark.parametrize(
    ("specification", "message"),
    [
        (17, "MODULE:ATTRIBUTE string"),
        ("not-a-factory", "canonical"),
        (_module_spec("_private_factory"), "private"),
        ("module_that_does_not_exist:create", "could not resolve"),
        (_module_spec("missing_factory"), "could not resolve"),
        (_module_spec("NOT_CALLABLE_FACTORY"), "callable"),
    ],
)
def test_factory_loader_rejects_invalid_or_unresolvable_targets(
    specification: object,
    message: str,
) -> None:
    with pytest.raises(CliError, match=message) as error:
        cli_module._load_factory(specification, field="runtime_factory")
    assert error.value.exit_code is CliExitCode.ADAPTER_INVALID


def test_execute_from_factories_wraps_plan_factory_failures(tmp_path: Path) -> None:
    context = _load_context(_create_repository(tmp_path))
    with pytest.raises(CliError, match="plan factory failed") as raised:
        cli_module._execute_from_factories(
            context,
            plan_factory_spec=_module_spec("failing_plan_factory"),
            runtime_factory_spec=_module_spec("valid_runtime_factory"),
        )
    assert raised.value.exit_code is CliExitCode.PLAN_INVALID

    with pytest.raises(CliError, match="must return a HarnessRunPlan"):
        cli_module._execute_from_factories(
            context,
            plan_factory_spec=_module_spec("invalid_plan_factory"),
            runtime_factory_spec=_module_spec("valid_runtime_factory"),
        )


def test_execute_from_factories_wraps_runtime_factory_failures(tmp_path: Path) -> None:
    context = _load_context(_create_repository(tmp_path))
    with pytest.raises(CliError, match="runtime factory failed") as raised:
        cli_module._execute_from_factories(
            context,
            plan_factory_spec=_module_spec("valid_plan_factory"),
            runtime_factory_spec=_module_spec("failing_runtime_factory"),
        )
    assert raised.value.exit_code is CliExitCode.ADAPTER_INVALID

    with pytest.raises(CliError, match="must return an AuroraRuntime"):
        cli_module._execute_from_factories(
            context,
            plan_factory_spec=_module_spec("valid_plan_factory"),
            runtime_factory_spec=_module_spec("invalid_runtime_factory"),
        )


def _different_fixture_bundle(context: CliRunContext) -> FixtureBundle:
    content = b'{"expected":"UNKNOWN"}'
    definition = FixtureFile(
        path=("Development/Validation/Aurora/Fixtures/FOUND-001/expected-results.json"),
        partition=FixturePartition.EXPECTED_RESULTS,
        media_type=FixtureMediaType.JSON,
        sha256=hashlib.sha256(content).hexdigest(),
        size_bytes=len(content),
    )
    artifact = FixtureArtifact(
        definition=definition,
        resolved_path=context.fixture_bundle.repository_root / definition.path,
        content_bytes=content,
    )
    unsigned_manifest = replace(
        context.fixture_bundle.manifest,
        files=(*context.fixture_bundle.manifest.files, definition),
        fixture_manifest_sha256=None,
    )
    manifest = replace(
        unsigned_manifest,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(unsigned_manifest),
    )
    return FixtureBundle(
        manifest,
        context.fixture_bundle.repository_root,
        (*context.fixture_bundle.artifacts, artifact),
    )


def test_plan_context_validation_rejects_each_unverified_product(tmp_path: Path) -> None:
    context = _load_context(_create_repository(tmp_path))
    plan = _minimal_plan(context)
    wrong_resolved = replace(
        context.resolved_configuration,
        output_root=context.resolved_configuration.output_root / "other",
    )
    wrong_baseline = replace(
        context.baseline_verification,
        declared_manifest_sha256="e" * 64,
    )
    wrong_fixture = _different_fixture_bundle(context)
    cases = (
        (_replace_plan(plan, resolved_configuration=wrong_resolved), "configuration"),
        (_replace_plan(plan, baseline_verification=wrong_baseline), "baseline"),
        (_replace_plan(plan, fixture_bundle=wrong_fixture), "fixture"),
    )
    for changed, message in cases:
        with pytest.raises(CliError, match=message) as error:
            cli_module._validate_plan_context(changed, context)
        assert error.value.exit_code is CliExitCode.PLAN_INVALID

    cli_module._validate_plan_context(plan, context)


def test_run_cli_reports_plan_and_adapter_errors_as_json(tmp_path: Path) -> None:
    plan_case = _create_repository(tmp_path / "plan")
    arguments = list(_run_arguments(plan_case))
    arguments[arguments.index(_module_spec("valid_plan_factory"))] = _module_spec(
        "invalid_plan_factory"
    )
    code, result, _ = _invoke(tuple(arguments))
    _assert_error(result, category="PLAN_INVALID", exit_code=CliExitCode.PLAN_INVALID)
    assert code == int(CliExitCode.PLAN_INVALID)

    runtime_case = _create_repository(tmp_path / "runtime")
    arguments = list(_run_arguments(runtime_case))
    arguments[arguments.index(_module_spec("valid_runtime_factory"))] = _module_spec(
        "invalid_runtime_factory"
    )
    code, result, _ = _invoke(tuple(arguments))
    _assert_error(
        result,
        category="ADAPTER_INVALID",
        exit_code=CliExitCode.ADAPTER_INVALID,
    )
    assert code == int(CliExitCode.ADAPTER_INVALID)


def test_run_cli_reports_harness_failures_with_phase_and_reason(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    case = _create_repository(tmp_path)

    def fail_harness(*_args: object) -> Any:
        raise HarnessError(
            HarnessPhase.STORING,
            HarnessFailureReason.STORAGE_FAILED,
            "storage unavailable",
        )

    monkeypatch.setattr(cli_module, "execute_harness_run", fail_harness)
    code, result, _ = _invoke(_run_arguments(case))
    error = _assert_error(
        result,
        category="HARNESS_FAILED",
        exit_code=CliExitCode.HARNESS_FAILED,
    )
    assert error["message"] == "storage unavailable"
    assert error["details"] == {"phase": "STORING", "reason": "STORAGE_FAILED"}
    assert code == int(CliExitCode.HARNESS_FAILED)


def test_run_cli_reports_unexpected_exceptions_without_traceback(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def explode(**_kwargs: object) -> CliRunContext:
        raise RuntimeError("unexpected boom")

    monkeypatch.setattr(cli_module, "_load_run_context", explode)
    stdout = io.StringIO()
    stderr = io.StringIO()
    code = run_cli(
        ("preflight", "--configuration", "ignored.json"),
        stdout=stdout,
        stderr=stderr,
    )
    result = json.loads(stderr.getvalue())
    error = _assert_error(
        result,
        category="INTERNAL_ERROR",
        exit_code=CliExitCode.INTERNAL_ERROR,
    )
    assert error["message"] == "unexpected RuntimeError: unexpected boom"
    assert "Traceback" not in stderr.getvalue()
    assert stdout.getvalue() == ""
    assert code == int(CliExitCode.INTERNAL_ERROR)


def test_direct_exception_handlers_cover_configuration_manifest_and_fixture(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exceptions = (
        (ConfigurationError("configuration bad"), CliExitCode.CONFIGURATION_INVALID),
        (ManifestError("baseline bad"), CliExitCode.BASELINE_INVALID),
        (FixtureError("fixture bad"), CliExitCode.FIXTURE_INVALID),
    )
    for exception, expected_code in exceptions:
        monkeypatch.setattr(
            cli_module,
            "_load_run_context",
            _raising_context_loader(exception),
        )
        stdout = io.StringIO()
        stderr = io.StringIO()
        code = run_cli(
            ("preflight", "--configuration", "ignored.json"),
            stdout=stdout,
            stderr=stderr,
        )
        assert code == int(expected_code)
        assert json.loads(stderr.getvalue())["error"]["exit_code"] == int(expected_code)
        assert stdout.getvalue() == ""


def test_report_emit_and_canonical_json_helpers_flush_and_reject_invalid_output() -> None:
    class FlushTrackingStream(io.StringIO):
        flushed: bool = False

        def flush(self) -> None:
            self.flushed = True
            super().flush()

    stream = FlushTrackingStream()
    error = CliError(CliExitCode.USAGE, "CLI_USAGE", "bad arguments")
    assert cli_module._report_error(stream, error) == int(CliExitCode.USAGE)
    assert stream.flushed is True
    assert json.loads(stream.getvalue())["error"] == error.to_mapping()
    assert cli_module._canonical_json_bytes({"b": 2, "a": "Café"}) == (
        '{"a":"Café","b":2}'.encode()
    )
    for value in (object(), {"value": float("inf")}):
        with pytest.raises(TypeError, match="canonical finite JSON"):
            cli_module._canonical_json_bytes(value)
