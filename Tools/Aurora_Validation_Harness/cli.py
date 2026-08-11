"""Fail-closed command-line boundary for the Aurora validation harness.

The CLI verifies repository-controlled inputs before importing scenario or
runtime adapters.  It emits deterministic, content-redacted JSON suitable for
automation and delegates all execution semantics to :mod:`harness`.
"""

from __future__ import annotations

import argparse
import importlib
import json
import re
import sys
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path
from types import MappingProxyType
from typing import Final, NoReturn, Protocol, TextIO, cast

from aurora_validation_harness import __version__
from aurora_validation_harness.baseline import (
    BaselineState,
    BaselineVerificationResult,
    ManifestError,
    VerificationStatus,
    load_manifest,
    verify_baseline,
)
from aurora_validation_harness.configuration import (
    ConfigurationError,
    ResolvedConfiguration,
    RunMode,
    load_and_resolve_configuration,
)
from aurora_validation_harness.fixtures import (
    FixtureBundle,
    FixtureError,
    load_fixture_set,
)
from aurora_validation_harness.harness import (
    AuroraRuntime,
    HarnessError,
    HarnessRunPlan,
    HarnessRunResult,
    execute_harness_run,
)

SUPPORTED_CLI_SCHEMA_VERSION: Final[str] = "1.0"
CLI_PROGRAM_NAME: Final[str] = "aurora-validation-harness"

_FACTORY_SPEC_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^(?P<module>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*):"
    r"(?P<attribute>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)$"
)


class CliExitCode(IntEnum):
    """Stable process exit codes for automation and operator diagnosis."""

    SUCCESS = 0
    USAGE = 2
    CONFIGURATION_INVALID = 10
    BASELINE_BLOCKED = 11
    BASELINE_INVALID = 12
    FIXTURE_INVALID = 13
    ADAPTER_INVALID = 14
    PLAN_INVALID = 15
    HARNESS_FAILED = 16
    INTERNAL_ERROR = 70


class CliError(RuntimeError):
    """Structured operator-safe failure raised inside the CLI boundary."""

    def __init__(
        self,
        exit_code: CliExitCode,
        category: str,
        message: str,
        *,
        details: Mapping[str, object] | None = None,
    ) -> None:
        if not isinstance(exit_code, CliExitCode) or exit_code is CliExitCode.SUCCESS:
            raise TypeError("exit_code must be a non-success CliExitCode value")
        if not isinstance(category, str) or not category or category != category.upper():
            raise TypeError("category must be a non-empty uppercase string")
        if not isinstance(message, str) or not message.strip():
            raise TypeError("message must be a non-empty string")
        if details is not None and not isinstance(details, Mapping):
            raise TypeError("details must be null or a mapping")
        normalized_details = {} if details is None else dict(details)
        _canonical_json_bytes(normalized_details)
        self.exit_code = exit_code
        self.category = category
        self.detail = message
        self.details = MappingProxyType(normalized_details)
        super().__init__(f"{category}: {message}")

    def to_mapping(self) -> dict[str, object]:
        """Return the stable error fields used by the JSON envelope."""

        return {
            "category": self.category,
            "details": dict(self.details),
            "exit_code": int(self.exit_code),
            "message": self.detail,
        }


class PlanFactory(Protocol):
    """Scenario-owned callable that compiles validated inputs into a run plan."""

    def __call__(self, context: CliRunContext, /) -> HarnessRunPlan:
        """Return one complete plan bound to the supplied validated context."""


class RuntimeFactory(Protocol):
    """Callable that constructs a fresh Aurora runtime adapter."""

    def __call__(self) -> AuroraRuntime:
        """Return a runtime implementing the minimum executable interface."""


@dataclass(frozen=True, slots=True)
class CliRunContext:
    """Verified repository inputs made available to a scenario plan factory."""

    resolved_configuration: ResolvedConfiguration
    baseline_verification: BaselineVerificationResult
    fixture_bundle: FixtureBundle

    def __post_init__(self) -> None:
        if not isinstance(self.resolved_configuration, ResolvedConfiguration):
            raise TypeError("resolved_configuration must be a ResolvedConfiguration")
        if not isinstance(self.baseline_verification, BaselineVerificationResult):
            raise TypeError("baseline_verification must be a BaselineVerificationResult")
        if not isinstance(self.fixture_bundle, FixtureBundle):
            raise TypeError("fixture_bundle must be a FixtureBundle")
        configuration = self.resolved_configuration.configuration
        if self.baseline_verification.status is not VerificationStatus.VERIFIED:
            raise ValueError("baseline verification must be VERIFIED")
        if self.baseline_verification.baseline_id != configuration.baseline_id:
            raise ValueError("baseline verification does not match configuration")
        if self.fixture_bundle.manifest.fixture_set_id != configuration.fixture_set_id:
            raise ValueError("fixture bundle does not match configuration")
        if self.fixture_bundle.manifest.scenario_id != configuration.scenario_id:
            raise ValueError("fixture scenario does not match configuration")
        if self.fixture_bundle.repository_root != self.resolved_configuration.repository_root:
            raise ValueError("fixture repository root does not match configuration")

    def to_mapping(self) -> dict[str, object]:
        """Return content-redacted preflight evidence for operators."""

        configuration = self.resolved_configuration.configuration
        manifest = self.fixture_bundle.manifest
        return {
            "baseline": {
                "baseline_id": self.baseline_verification.baseline_id,
                "baseline_state": self.baseline_verification.baseline_state.value,
                "calculated_manifest_sha256": (
                    self.baseline_verification.calculated_manifest_sha256
                ),
                "status": self.baseline_verification.status.value,
            },
            "configuration": {
                "configuration_id": configuration.configuration_id,
                "configuration_sha256": configuration.configuration_sha256,
                "run_mode": configuration.execution.run_mode.value,
            },
            "fixtures": {
                "artifact_count": len(self.fixture_bundle.artifacts),
                "fixture_manifest_sha256": self.fixture_bundle.fixture_set_sha256,
                "fixture_set_id": manifest.fixture_set_id,
            },
            "output_root": configuration.output_root,
            "scenario_id": configuration.scenario_id,
        }


class _CliArgumentParser(argparse.ArgumentParser):
    """Argument parser that reports usage failures through the JSON boundary."""

    def error(self, message: str) -> NoReturn:
        raise CliError(CliExitCode.USAGE, "CLI_USAGE", message)


def create_argument_parser() -> argparse.ArgumentParser:
    """Create the complete public command-line grammar."""

    parser = _CliArgumentParser(
        prog=CLI_PROGRAM_NAME,
        description=("Verify controlled Aurora validation inputs and execute one fail-closed run."),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    preflight = commands.add_parser(
        "preflight",
        help="verify configuration, baseline, and fixtures without loading adapters",
    )
    _add_controlled_input_arguments(preflight)

    run = commands.add_parser(
        "run",
        help="verify controlled inputs, construct adapters, and execute one run",
    )
    _add_controlled_input_arguments(run)
    run.add_argument(
        "--plan-factory",
        required=True,
        metavar="MODULE:ATTRIBUTE",
        help="scenario plan factory accepting one CliRunContext",
    )
    run.add_argument(
        "--runtime-factory",
        required=True,
        metavar="MODULE:ATTRIBUTE",
        help="zero-argument factory returning a fresh Aurora runtime adapter",
    )
    return parser


def run_cli(
    argv: Sequence[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
) -> int:
    """Run the CLI without terminating the interpreter and return an exit code."""

    output_stream = sys.stdout if stdout is None else stdout
    error_stream = sys.stderr if stderr is None else stderr
    parser = create_argument_parser()
    try:
        arguments = parser.parse_args(argv)
        context = _load_run_context(
            repository_root=Path(arguments.repository_root),
            configuration_path=Path(arguments.configuration),
        )
        if arguments.command == "preflight":
            _emit_json(
                output_stream,
                {
                    "cli_schema_version": SUPPORTED_CLI_SCHEMA_VERSION,
                    "command": "preflight",
                    "preflight": context.to_mapping(),
                    "status": "VERIFIED",
                },
            )
            return int(CliExitCode.SUCCESS)
        if arguments.command == "run":
            result = _execute_from_factories(
                context,
                plan_factory_spec=arguments.plan_factory,
                runtime_factory_spec=arguments.runtime_factory,
            )
            _emit_json(
                output_stream,
                {
                    "cli_schema_version": SUPPORTED_CLI_SCHEMA_VERSION,
                    "command": "run",
                    "preflight": context.to_mapping(),
                    "result": result.to_summary_mapping(),
                    "status": "COMPLETE",
                },
            )
            return int(CliExitCode.SUCCESS)
        raise CliError(
            CliExitCode.USAGE,
            "CLI_USAGE",
            "a supported command is required",
        )
    except CliError as exc:
        return _report_error(error_stream, exc)
    except ConfigurationError as exc:
        return _report_error(
            error_stream,
            CliError(
                CliExitCode.CONFIGURATION_INVALID,
                "CONFIGURATION_INVALID",
                str(exc),
            ),
        )
    except ManifestError as exc:
        return _report_error(
            error_stream,
            CliError(CliExitCode.BASELINE_INVALID, "BASELINE_INVALID", str(exc)),
        )
    except FixtureError as exc:
        return _report_error(
            error_stream,
            CliError(CliExitCode.FIXTURE_INVALID, "FIXTURE_INVALID", str(exc)),
        )
    except HarnessError as exc:
        return _report_error(
            error_stream,
            CliError(
                CliExitCode.HARNESS_FAILED,
                "HARNESS_FAILED",
                exc.detail,
                details={"phase": exc.phase.value, "reason": exc.reason.value},
            ),
        )
    except Exception as exc:
        return _report_error(
            error_stream,
            CliError(
                CliExitCode.INTERNAL_ERROR,
                "INTERNAL_ERROR",
                f"unexpected {type(exc).__name__}: {exc}",
            ),
        )


def main(argv: Sequence[str] | None = None) -> int:
    """Console-script entry point."""

    return run_cli(argv)


def _add_controlled_input_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--repository-root",
        default=".",
        metavar="PATH",
        help="Project Ascension repository root; defaults to the current directory",
    )
    parser.add_argument(
        "--configuration",
        required=True,
        metavar="PATH",
        help="hash-bound Aurora harness configuration JSON file",
    )


def _load_run_context(
    *,
    repository_root: Path,
    configuration_path: Path,
) -> CliRunContext:
    resolved = load_and_resolve_configuration(
        configuration_path,
        repository_root,
        require_hash=True,
    )
    configuration = resolved.configuration
    baseline_manifest = load_manifest(resolved.baseline_manifest)
    if baseline_manifest.baseline_id != configuration.baseline_id:
        raise CliError(
            CliExitCode.BASELINE_INVALID,
            "BASELINE_INVALID",
            "baseline manifest ID does not match configuration",
        )
    verification = verify_baseline(resolved.repository_root, baseline_manifest)
    if verification.status is not VerificationStatus.VERIFIED:
        exit_code = (
            CliExitCode.BASELINE_INVALID
            if verification.status is VerificationStatus.INVALID
            else CliExitCode.BASELINE_BLOCKED
        )
        category = (
            "BASELINE_INVALID"
            if verification.status is VerificationStatus.INVALID
            else "BASELINE_BLOCKED"
        )
        raise CliError(
            exit_code,
            category,
            "baseline verification did not produce an executable VERIFIED result",
            details={
                "baseline_id": verification.baseline_id,
                "baseline_state": verification.baseline_state.value,
                "issue_codes": [issue.code for issue in verification.issues],
                "status": verification.status.value,
            },
        )
    if (
        configuration.execution.run_mode is RunMode.FORMAL
        and verification.baseline_state is not BaselineState.FORMAL_EXECUTION_ACTIVE
    ):
        raise CliError(
            CliExitCode.BASELINE_BLOCKED,
            "BASELINE_BLOCKED",
            "FORMAL mode requires a FORMAL_EXECUTION_ACTIVE baseline",
            details={
                "baseline_id": verification.baseline_id,
                "baseline_state": verification.baseline_state.value,
                "status": verification.status.value,
            },
        )
    fixture_bundle = load_fixture_set(
        resolved.fixture_manifest,
        resolved.repository_root,
        require_hash=True,
    )
    try:
        return CliRunContext(resolved, verification, fixture_bundle)
    except (TypeError, ValueError) as exc:
        raise CliError(
            CliExitCode.FIXTURE_INVALID,
            "FIXTURE_INVALID",
            str(exc),
        ) from exc


def _execute_from_factories(
    context: CliRunContext,
    *,
    plan_factory_spec: str,
    runtime_factory_spec: str,
) -> HarnessRunResult:
    plan_factory = cast(
        PlanFactory,
        _load_factory(plan_factory_spec, field="plan_factory"),
    )
    try:
        plan = plan_factory(context)
    except Exception as exc:
        raise CliError(
            CliExitCode.PLAN_INVALID,
            "PLAN_INVALID",
            f"plan factory failed: {exc}",
        ) from exc
    if not isinstance(plan, HarnessRunPlan):
        raise CliError(
            CliExitCode.PLAN_INVALID,
            "PLAN_INVALID",
            "plan factory must return a HarnessRunPlan",
        )
    _validate_plan_context(plan, context)

    runtime_factory = cast(
        RuntimeFactory,
        _load_factory(runtime_factory_spec, field="runtime_factory"),
    )
    try:
        runtime = runtime_factory()
    except Exception as exc:
        raise CliError(
            CliExitCode.ADAPTER_INVALID,
            "ADAPTER_INVALID",
            f"runtime factory failed: {exc}",
        ) from exc
    if not isinstance(runtime, AuroraRuntime):
        raise CliError(
            CliExitCode.ADAPTER_INVALID,
            "ADAPTER_INVALID",
            "runtime factory must return an AuroraRuntime adapter",
        )
    return execute_harness_run(plan, runtime)


def _load_factory(specification: object, *, field: str) -> Callable[..., object]:
    if not isinstance(specification, str):
        raise CliError(
            CliExitCode.ADAPTER_INVALID,
            "ADAPTER_INVALID",
            f"{field} must be a MODULE:ATTRIBUTE string",
        )
    match = _FACTORY_SPEC_PATTERN.fullmatch(specification)
    if match is None:
        raise CliError(
            CliExitCode.ADAPTER_INVALID,
            "ADAPTER_INVALID",
            f"{field} must use canonical MODULE:ATTRIBUTE syntax",
        )
    module_name = match.group("module")
    attribute_path = match.group("attribute")
    if any(component.startswith("_") for component in attribute_path.split(".")):
        raise CliError(
            CliExitCode.ADAPTER_INVALID,
            "ADAPTER_INVALID",
            f"{field} must not reference private attributes",
        )
    try:
        value: object = importlib.import_module(module_name)
        for component in attribute_path.split("."):
            value = getattr(value, component)
    except (ImportError, AttributeError) as exc:
        raise CliError(
            CliExitCode.ADAPTER_INVALID,
            "ADAPTER_INVALID",
            f"could not resolve {field}: {specification}",
        ) from exc
    if not callable(value):
        raise CliError(
            CliExitCode.ADAPTER_INVALID,
            "ADAPTER_INVALID",
            f"{field} must resolve to a callable",
        )
    return cast(Callable[..., object], value)


def _validate_plan_context(plan: HarnessRunPlan, context: CliRunContext) -> None:
    if plan.resolved_configuration != context.resolved_configuration:
        raise CliError(
            CliExitCode.PLAN_INVALID,
            "PLAN_INVALID",
            "run plan does not use the CLI-verified configuration",
        )
    if plan.baseline_verification != context.baseline_verification:
        raise CliError(
            CliExitCode.PLAN_INVALID,
            "PLAN_INVALID",
            "run plan does not use the CLI-verified baseline result",
        )
    if plan.fixture_bundle != context.fixture_bundle:
        raise CliError(
            CliExitCode.PLAN_INVALID,
            "PLAN_INVALID",
            "run plan does not use the CLI-verified fixture bundle",
        )


def _report_error(stream: TextIO, error: CliError) -> int:
    _emit_json(
        stream,
        {
            "cli_schema_version": SUPPORTED_CLI_SCHEMA_VERSION,
            "error": error.to_mapping(),
            "status": "ERROR",
        },
    )
    return int(error.exit_code)


def _emit_json(stream: TextIO, value: Mapping[str, object]) -> None:
    stream.write(_canonical_json_bytes(value).decode("utf-8"))
    stream.write("\n")
    stream.flush()


def _canonical_json_bytes(value: object) -> bytes:
    try:
        return json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise TypeError("CLI output must be canonical finite JSON") from exc


__all__ = [
    "CLI_PROGRAM_NAME",
    "SUPPORTED_CLI_SCHEMA_VERSION",
    "CliError",
    "CliExitCode",
    "CliRunContext",
    "PlanFactory",
    "RuntimeFactory",
    "create_argument_parser",
    "main",
    "run_cli",
]


if __name__ == "__main__":
    raise SystemExit(main())
