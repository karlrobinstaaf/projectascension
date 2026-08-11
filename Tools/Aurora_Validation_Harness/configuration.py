"""Immutable harness configuration loading, hashing, and path resolution.

Configuration is validator-owned control data. This module validates execution
identity and policy, verifies the configuration hash, and resolves controlled
repository paths without creating directories or loading fixture contents.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import Final

SUPPORTED_CONFIGURATION_VERSION: Final[str] = "1.0"
RUN_OUTPUT_ROOT: Final[str] = "Development/Validation/Aurora/Runs"
MAX_RANDOM_SEED: Final[int] = (1 << 64) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_IDENTIFIER_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_TOP_LEVEL_KEYS: Final[frozenset[str]] = frozenset(
    {
        "baseline_id",
        "baseline_manifest_path",
        "configuration_id",
        "configuration_sha256",
        "configuration_version",
        "execution",
        "fixture_manifest_path",
        "fixture_set_id",
        "output_root",
        "scenario_id",
    }
)
_REQUIRED_TOP_LEVEL_KEYS: Final[frozenset[str]] = _TOP_LEVEL_KEYS - {"configuration_sha256"}
_EXECUTION_KEYS: Final[frozenset[str]] = frozenset(
    {
        "allow_output_overwrite",
        "deterministic",
        "network_access_enabled",
        "random_seed",
        "reset_before_run",
        "run_mode",
        "strict_isolation",
        "telemetry_feedback_enabled",
    }
)


class ConfigurationError(ValueError):
    """Raised when harness configuration is invalid or cannot be resolved."""


class RunMode(StrEnum):
    """Governed execution mode for a validation run."""

    DRY_RUN = "DRY_RUN"
    FORMAL = "FORMAL"
    REGRESSION = "REGRESSION"


@dataclass(frozen=True, slots=True)
class ExecutionPolicy:
    """Safety and repeatability controls applied to one run configuration."""

    run_mode: RunMode
    random_seed: int
    deterministic: bool
    strict_isolation: bool
    reset_before_run: bool
    network_access_enabled: bool
    telemetry_feedback_enabled: bool
    allow_output_overwrite: bool

    def __post_init__(self) -> None:
        if not isinstance(self.run_mode, RunMode):
            raise ConfigurationError("run_mode must be a RunMode value")
        if isinstance(self.random_seed, bool) or not isinstance(self.random_seed, int):
            raise ConfigurationError("random_seed must be an integer")
        if not 0 <= self.random_seed <= MAX_RANDOM_SEED:
            raise ConfigurationError(f"random_seed must be between 0 and {MAX_RANDOM_SEED}")
        boolean_fields = (
            ("deterministic", self.deterministic),
            ("strict_isolation", self.strict_isolation),
            ("reset_before_run", self.reset_before_run),
            ("network_access_enabled", self.network_access_enabled),
            ("telemetry_feedback_enabled", self.telemetry_feedback_enabled),
            ("allow_output_overwrite", self.allow_output_overwrite),
        )
        for field, value in boolean_fields:
            if not isinstance(value, bool):
                raise ConfigurationError(f"{field} must be a boolean")
        if not self.deterministic:
            raise ConfigurationError("deterministic must be true")
        if not self.strict_isolation:
            raise ConfigurationError("strict_isolation must be true")
        if not self.reset_before_run:
            raise ConfigurationError("reset_before_run must be true")
        if self.network_access_enabled:
            raise ConfigurationError("network_access_enabled must be false")
        if self.telemetry_feedback_enabled:
            raise ConfigurationError("telemetry_feedback_enabled must be false")
        if self.allow_output_overwrite:
            raise ConfigurationError("allow_output_overwrite must be false")

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> ExecutionPolicy:
        """Create an execution policy from decoded JSON data."""

        _validate_keys(
            data,
            allowed=_EXECUTION_KEYS,
            required=_EXECUTION_KEYS,
            context="execution",
        )
        raw_mode = _required_string(data, "run_mode", context="execution")
        try:
            run_mode = RunMode(raw_mode)
        except ValueError as exc:
            raise ConfigurationError(f"unsupported execution.run_mode: {raw_mode}") from exc

        return cls(
            run_mode=run_mode,
            random_seed=_required_integer(data, "random_seed", context="execution"),
            deterministic=_required_boolean(data, "deterministic", context="execution"),
            strict_isolation=_required_boolean(
                data,
                "strict_isolation",
                context="execution",
            ),
            reset_before_run=_required_boolean(
                data,
                "reset_before_run",
                context="execution",
            ),
            network_access_enabled=_required_boolean(
                data,
                "network_access_enabled",
                context="execution",
            ),
            telemetry_feedback_enabled=_required_boolean(
                data,
                "telemetry_feedback_enabled",
                context="execution",
            ),
            allow_output_overwrite=_required_boolean(
                data,
                "allow_output_overwrite",
                context="execution",
            ),
        )

    def to_mapping(self) -> dict[str, object]:
        """Return the stable JSON representation used for configuration hashing."""

        return {
            "allow_output_overwrite": self.allow_output_overwrite,
            "deterministic": self.deterministic,
            "network_access_enabled": self.network_access_enabled,
            "random_seed": self.random_seed,
            "reset_before_run": self.reset_before_run,
            "run_mode": self.run_mode.value,
            "strict_isolation": self.strict_isolation,
            "telemetry_feedback_enabled": self.telemetry_feedback_enabled,
        }


@dataclass(frozen=True, slots=True)
class HarnessConfiguration:
    """Validated, immutable description of one harness execution setup."""

    configuration_id: str
    configuration_version: str
    scenario_id: str
    baseline_id: str
    baseline_manifest_path: str
    fixture_set_id: str
    fixture_manifest_path: str
    output_root: str
    execution: ExecutionPolicy
    configuration_sha256: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.execution, ExecutionPolicy):
            raise ConfigurationError("execution must be an ExecutionPolicy")
        _validate_identifier(self.configuration_id, field="configuration_id")
        _validate_identifier(self.baseline_id, field="baseline_id")
        _validate_identifier(self.fixture_set_id, field="fixture_set_id")
        if not isinstance(self.configuration_version, str):
            raise ConfigurationError("configuration_version must be a string")
        if self.configuration_version != SUPPORTED_CONFIGURATION_VERSION:
            raise ConfigurationError(
                "unsupported configuration_version: "
                f"{self.configuration_version}; expected {SUPPORTED_CONFIGURATION_VERSION}"
            )
        if not isinstance(self.scenario_id, str):
            raise ConfigurationError("scenario_id must be a string")
        if _SCENARIO_ID_PATTERN.fullmatch(self.scenario_id) is None:
            raise ConfigurationError("scenario_id must match AURORA-SCN-<GATE>-<NNN>")

        _validate_relative_path(
            self.baseline_manifest_path,
            field="baseline_manifest_path",
        )
        _validate_relative_path(
            self.fixture_manifest_path,
            field="fixture_manifest_path",
        )
        _validate_relative_path(self.output_root, field="output_root")
        _validate_output_root(self.output_root)

        if self.baseline_manifest_path == self.fixture_manifest_path:
            raise ConfigurationError(
                "baseline_manifest_path and fixture_manifest_path must be distinct"
            )
        if self.configuration_sha256 is not None:
            _validate_sha256(self.configuration_sha256, field="configuration_sha256")

    @classmethod
    def from_mapping(cls, data: Mapping[str, object]) -> HarnessConfiguration:
        """Create a harness configuration from decoded JSON data."""

        _validate_keys(
            data,
            allowed=_TOP_LEVEL_KEYS,
            required=_REQUIRED_TOP_LEVEL_KEYS,
            context="configuration",
        )
        raw_execution = data.get("execution")
        if not isinstance(raw_execution, Mapping):
            raise ConfigurationError("configuration.execution must be a JSON object")

        return cls(
            configuration_id=_required_string(data, "configuration_id"),
            configuration_version=_required_string(data, "configuration_version"),
            scenario_id=_required_string(data, "scenario_id"),
            baseline_id=_required_string(data, "baseline_id"),
            baseline_manifest_path=_required_string(data, "baseline_manifest_path"),
            fixture_set_id=_required_string(data, "fixture_set_id"),
            fixture_manifest_path=_required_string(data, "fixture_manifest_path"),
            output_root=_required_string(data, "output_root"),
            execution=ExecutionPolicy.from_mapping(raw_execution),
            configuration_sha256=_optional_string(data, "configuration_sha256"),
        )

    def hash_payload(self) -> dict[str, object]:
        """Return canonical content excluding the self-referential hash field."""

        return {
            "baseline_id": self.baseline_id,
            "baseline_manifest_path": self.baseline_manifest_path,
            "configuration_id": self.configuration_id,
            "configuration_version": self.configuration_version,
            "execution": self.execution.to_mapping(),
            "fixture_manifest_path": self.fixture_manifest_path,
            "fixture_set_id": self.fixture_set_id,
            "output_root": self.output_root,
            "scenario_id": self.scenario_id,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return the complete stable JSON representation."""

        return self.hash_payload() | {"configuration_sha256": self.configuration_sha256}


@dataclass(frozen=True, slots=True)
class ResolvedConfiguration:
    """Repository-bound configuration paths verified without filesystem mutation."""

    configuration: HarnessConfiguration
    repository_root: Path
    baseline_manifest: Path
    fixture_manifest: Path
    output_root: Path

    @property
    def controlled_inputs(self) -> tuple[Path, Path]:
        """Return source manifests whose bytes must remain read-only during a run."""

        return (self.baseline_manifest, self.fixture_manifest)


def calculate_configuration_sha256(configuration: HarnessConfiguration) -> str:
    """Calculate the deterministic hash of a configuration's canonical payload."""

    payload = json.dumps(
        configuration.hash_payload(),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_configuration(
    path: Path,
    *,
    require_hash: bool = True,
) -> HarnessConfiguration:
    """Load UTF-8 JSON configuration and verify its declared content hash."""

    try:
        decoded = json.loads(
            path.read_text(encoding="utf-8"),
            parse_constant=_reject_non_finite_json,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ConfigurationError(f"unable to load configuration {path}: {exc}") from exc
    if not isinstance(decoded, Mapping):
        raise ConfigurationError("configuration root must be a JSON object")

    configuration = HarnessConfiguration.from_mapping(decoded)
    calculated_hash = calculate_configuration_sha256(configuration)
    if configuration.configuration_sha256 is None:
        if require_hash:
            raise ConfigurationError(
                "configuration_sha256 is required for executable configuration"
            )
    elif configuration.configuration_sha256 != calculated_hash:
        raise ConfigurationError(
            "configuration_sha256 does not match the canonical configuration payload"
        )
    return configuration


def resolve_configuration(
    repository_root: Path,
    configuration: HarnessConfiguration,
) -> ResolvedConfiguration:
    """Resolve configuration paths beneath a repository without creating output."""

    try:
        root = repository_root.resolve(strict=True)
    except OSError as exc:
        raise ConfigurationError(
            f"repository root cannot be resolved: {repository_root}: {exc}"
        ) from exc
    if not root.is_dir():
        raise ConfigurationError(f"repository root is not a directory: {root}")

    baseline_manifest = _resolve_input_file(
        root,
        configuration.baseline_manifest_path,
        field="baseline_manifest_path",
    )
    fixture_manifest = _resolve_input_file(
        root,
        configuration.fixture_manifest_path,
        field="fixture_manifest_path",
    )
    if baseline_manifest == fixture_manifest:
        raise ConfigurationError("baseline and fixture manifests resolve to the same file")

    output_root = _resolve_repository_path(
        root,
        configuration.output_root,
        field="output_root",
        strict=False,
    )
    if output_root.exists() and not output_root.is_dir():
        raise ConfigurationError(f"output_root is not a directory: {output_root}")

    return ResolvedConfiguration(
        configuration=configuration,
        repository_root=root,
        baseline_manifest=baseline_manifest,
        fixture_manifest=fixture_manifest,
        output_root=output_root,
    )


def load_and_resolve_configuration(
    configuration_path: Path,
    repository_root: Path,
    *,
    require_hash: bool = True,
) -> ResolvedConfiguration:
    """Load, hash-verify, and repository-bind one configuration."""

    configuration = load_configuration(
        configuration_path,
        require_hash=require_hash,
    )
    return resolve_configuration(repository_root, configuration)


def _resolve_input_file(root: Path, relative_path: str, *, field: str) -> Path:
    path = _resolve_repository_path(root, relative_path, field=field, strict=True)
    if not path.is_file():
        raise ConfigurationError(f"{field} is not a file: {relative_path}")
    return path


def _resolve_repository_path(
    root: Path,
    relative_path: str,
    *,
    field: str,
    strict: bool,
) -> Path:
    _validate_relative_path(relative_path, field=field)
    try:
        candidate = root.joinpath(*PurePosixPath(relative_path).parts).resolve(strict=strict)
    except OSError as exc:
        raise ConfigurationError(f"unable to resolve {field}: {relative_path}: {exc}") from exc
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ConfigurationError(f"{field} escapes repository root: {relative_path}") from exc
    return candidate


def _validate_output_root(path: str) -> None:
    required_root = PurePosixPath(RUN_OUTPUT_ROOT)
    candidate = PurePosixPath(path)
    if candidate.parts[: len(required_root.parts)] != required_root.parts:
        raise ConfigurationError(f"output_root must be {RUN_OUTPUT_ROOT} or one of its descendants")


def _validate_relative_path(path: str, *, field: str) -> None:
    if not isinstance(path, str):
        raise ConfigurationError(f"{field} must be a string")
    if not path or not path.strip():
        raise ConfigurationError(f"{field} must not be empty")
    if path != path.strip():
        raise ConfigurationError(f"{field} must not contain surrounding whitespace")
    if "\\" in path:
        raise ConfigurationError(f"{field} must use forward slashes")
    pure_path = PurePosixPath(path)
    if pure_path.is_absolute() or ".." in pure_path.parts:
        raise ConfigurationError(f"{field} must remain repository-relative")
    if pure_path.parts and ":" in pure_path.parts[0]:
        raise ConfigurationError(f"{field} must not contain a drive prefix")
    if pure_path.as_posix() != path or pure_path == PurePosixPath("."):
        raise ConfigurationError(f"{field} must use canonical repository-relative form")


def _validate_identifier(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise ConfigurationError(f"{field} must be a string")
    if _IDENTIFIER_PATTERN.fullmatch(value) is None:
        raise ConfigurationError(f"{field} must contain 3-128 uppercase identifier characters")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise ConfigurationError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise ConfigurationError(f"{field} must be a lowercase 64-character SHA-256 digest")


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
        raise ConfigurationError(f"unknown {context} field(s): {', '.join(unknown)}")
    missing = sorted(required - keys)
    if missing:
        raise ConfigurationError(f"missing {context} field(s): {', '.join(missing)}")


def _required_string(
    data: Mapping[str, object],
    key: str,
    *,
    context: str = "configuration",
) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ConfigurationError(f"{context}.{key} must be a non-empty string")
    return value


def _optional_string(data: Mapping[str, object], key: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ConfigurationError(f"configuration.{key} must be null or a non-empty string")
    return value


def _required_boolean(
    data: Mapping[str, object],
    key: str,
    *,
    context: str,
) -> bool:
    value = data.get(key)
    if not isinstance(value, bool):
        raise ConfigurationError(f"{context}.{key} must be a boolean")
    return value


def _required_integer(
    data: Mapping[str, object],
    key: str,
    *,
    context: str,
) -> int:
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ConfigurationError(f"{context}.{key} must be an integer")
    return value


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
    "MAX_RANDOM_SEED",
    "RUN_OUTPUT_ROOT",
    "SUPPORTED_CONFIGURATION_VERSION",
    "ConfigurationError",
    "ExecutionPolicy",
    "HarnessConfiguration",
    "ResolvedConfiguration",
    "RunMode",
    "calculate_configuration_sha256",
    "load_and_resolve_configuration",
    "load_configuration",
    "resolve_configuration",
]
