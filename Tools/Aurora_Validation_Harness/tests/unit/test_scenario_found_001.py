"""Unit tests for the FOUND-001 hidden-world knowledge-isolation plan."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import replace
from pathlib import Path

import pytest

from aurora_validation_harness.assertions import (
    AssertionSeverity,
    InvariantClass,
    SnapshotAssertion,
    SnapshotAssertionOperator,
)
from aurora_validation_harness.baseline import (
    BaselineState,
    BaselineVerificationResult,
    VerificationStatus,
)
from aurora_validation_harness.cli import CliRunContext
from aurora_validation_harness.configuration import (
    RUN_OUTPUT_ROOT,
    SUPPORTED_CONFIGURATION_VERSION,
    ExecutionPolicy,
    HarnessConfiguration,
    ResolvedConfiguration,
    RunMode,
    calculate_configuration_sha256,
)
from aurora_validation_harness.events import (
    EventObservability,
    EventSignificance,
    SimulationResolution,
)
from aurora_validation_harness.fixtures import (
    SUPPORTED_FIXTURE_MANIFEST_VERSION,
    FixtureArtifact,
    FixtureBundle,
    FixtureFile,
    FixtureManifest,
    FixtureMediaType,
    FixturePartition,
    calculate_fixture_manifest_sha256,
)
from aurora_validation_harness.harness import (
    AuroraResetRequest,
    AuroraStepRequest,
    HarnessRunPlan,
    PlannedAssertion,
    execute_harness_run,
)
from aurora_validation_harness.scenarios.found_001 import (
    EVENT_SCHEDULE_ID,
    FIXTURE_SET_ID,
    PACKAGE_ID,
    RUN_ID,
    SCENARIO_ID,
    VERDICT_DEFINITION_ID,
    Found001PlanError,
    create_plan,
)
from aurora_validation_harness.snapshots import SnapshotPhase
from aurora_validation_harness.verdicts import VerdictOutcome, VerdictReason

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_BASELINE_ID = "AURORA-G1-FOUNDATION-BASELINE-001"
_FIXTURE_ROOT = "Development/Validation/Aurora/Fixtures/FOUND-001"
_BASELINE_PATH = "Development/Validation/Aurora/Configuration/baseline.json"
_FIXTURE_MANIFEST_PATH = f"{_FIXTURE_ROOT}/fixture-manifest.json"

_DEFAULT_FIXTURE_PATHS: dict[FixturePartition, str] = {
    FixturePartition.WORLD: f"{_FIXTURE_ROOT}/world.json",
    FixturePartition.AURORA: f"{_FIXTURE_ROOT}/aurora.json",
    FixturePartition.PLAYER_PRIVATE: f"{_FIXTURE_ROOT}/player-private.json",
    FixturePartition.FUTURE: f"{_FIXTURE_ROOT}/future.json",
    FixturePartition.VALIDATOR: f"{_FIXTURE_ROOT}/validator.json",
    FixturePartition.EXPECTED_RESULTS: f"{_FIXTURE_ROOT}/expected-results.json",
}


def _stable_state() -> dict[str, object]:
    return {
        "active_goal": None,
        "active_prediction": None,
        "attention": "NO_ACTIVE_MARA_FOCUS",
        "beliefs": {
            "mara_current_location": {
                "confidence": None,
                "value": "UNKNOWN",
            }
        },
        "current_location": "Observation_Deck",
        "emotion": "NEUTRAL",
        "memories": [
            {
                "confidence": "HIGH",
                "fact": "MARA_LAST_KNOWN_LOCATION",
                "location": "Docking_Ring",
                "observed_at": "T-3h",
                "provenance": "VALID_HISTORICAL_MEMORY",
            }
        ],
        "relationship_with_mara": "STABLE",
        "uncertainty": {"mara_current_location": "HIGH"},
    }


def _fixture_payloads() -> dict[FixturePartition, dict[str, object]]:
    return {
        FixturePartition.WORLD: {
            "isolation_canary": "WORLD-FOUND-001-CANARY",
            "mara_current_location": "Cargo_Bay_7",
        },
        FixturePartition.AURORA: {
            "initial_state": _stable_state(),
            "subject_id": "aurora",
        },
        FixturePartition.PLAYER_PRIVATE: {"isolation_canary": "PLAYER-PRIVATE-FOUND-001-CANARY"},
        FixturePartition.FUTURE: {"isolation_canary": "FUTURE-FOUND-001-CANARY"},
        FixturePartition.VALIDATOR: {"isolation_canary": "VALIDATOR-FOUND-001-CANARY"},
        FixturePartition.EXPECTED_RESULTS: {
            "expected_result_canary": "EXPECTED-RESULT-FOUND-001-CANARY"
        },
    }


def _json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _fixture_bundle(
    repository_root: Path,
    *,
    scenario_id: str = SCENARIO_ID,
    fixture_set_id: str = FIXTURE_SET_ID,
    path_overrides: Mapping[FixturePartition, str] | None = None,
) -> FixtureBundle:
    fixture_paths = dict(_DEFAULT_FIXTURE_PATHS)
    if path_overrides is not None:
        fixture_paths.update(path_overrides)

    definitions: list[FixtureFile] = []
    artifacts: list[FixtureArtifact] = []
    for partition, payload in _fixture_payloads().items():
        content = _json_bytes(payload)
        definition = FixtureFile(
            path=fixture_paths[partition],
            partition=partition,
            media_type=FixtureMediaType.JSON,
            sha256=hashlib.sha256(content).hexdigest(),
            size_bytes=len(content),
        )
        definitions.append(definition)
        artifacts.append(
            FixtureArtifact(
                definition=definition,
                resolved_path=repository_root / definition.path,
                content_bytes=content,
            )
        )

    unsigned_manifest = FixtureManifest(
        fixture_set_id=fixture_set_id,
        scenario_id=scenario_id,
        fixture_manifest_version=SUPPORTED_FIXTURE_MANIFEST_VERSION,
        files=tuple(definitions),
    )
    manifest = replace(
        unsigned_manifest,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(unsigned_manifest),
    )
    return FixtureBundle(manifest, repository_root, tuple(artifacts))


def _resolved_configuration(
    repository_root: Path,
    *,
    scenario_id: str = SCENARIO_ID,
    fixture_set_id: str = FIXTURE_SET_ID,
) -> ResolvedConfiguration:
    policy = ExecutionPolicy(
        run_mode=RunMode.DRY_RUN,
        random_seed=41001,
        deterministic=True,
        strict_isolation=True,
        reset_before_run=True,
        network_access_enabled=False,
        telemetry_feedback_enabled=False,
        allow_output_overwrite=False,
    )
    unsigned_configuration = HarnessConfiguration(
        configuration_id="AURORA-CONFIG-FOUND-001-DRY",
        configuration_version=SUPPORTED_CONFIGURATION_VERSION,
        scenario_id=scenario_id,
        baseline_id=_BASELINE_ID,
        baseline_manifest_path=_BASELINE_PATH,
        fixture_set_id=fixture_set_id,
        fixture_manifest_path=_FIXTURE_MANIFEST_PATH,
        output_root=RUN_OUTPUT_ROOT,
        execution=policy,
    )
    configuration = replace(
        unsigned_configuration,
        configuration_sha256=calculate_configuration_sha256(unsigned_configuration),
    )
    output_root = repository_root / RUN_OUTPUT_ROOT
    output_root.parent.mkdir(parents=True, exist_ok=True)
    return ResolvedConfiguration(
        configuration=configuration,
        repository_root=repository_root,
        baseline_manifest=repository_root / _BASELINE_PATH,
        fixture_manifest=repository_root / _FIXTURE_MANIFEST_PATH,
        output_root=output_root,
    )


def _baseline_verification() -> BaselineVerificationResult:
    return BaselineVerificationResult(
        baseline_id=_BASELINE_ID,
        status=VerificationStatus.VERIFIED,
        baseline_state=BaselineState.EXECUTION_BASELINE_READY,
        calculated_manifest_sha256="a" * 64,
        declared_manifest_sha256="a" * 64,
        files=(),
        issues=(),
    )


def _context(
    repository_root: Path,
    *,
    scenario_id: str = SCENARIO_ID,
    fixture_set_id: str = FIXTURE_SET_ID,
    path_overrides: Mapping[FixturePartition, str] | None = None,
) -> CliRunContext:
    return CliRunContext(
        resolved_configuration=_resolved_configuration(
            repository_root,
            scenario_id=scenario_id,
            fixture_set_id=fixture_set_id,
        ),
        baseline_verification=_baseline_verification(),
        fixture_bundle=_fixture_bundle(
            repository_root,
            scenario_id=scenario_id,
            fixture_set_id=fixture_set_id,
            path_overrides=path_overrides,
        ),
    )


def _all_assertions(plan: HarnessRunPlan) -> tuple[PlannedAssertion, ...]:
    return plan.initial_assertions + tuple(
        assertion for step in plan.steps for assertion in step.assertions
    )


def _expected_values(assertions: tuple[PlannedAssertion, ...]) -> dict[str, object]:
    values: dict[str, object] = {}
    for planned in assertions:
        definition = planned.definition
        assert isinstance(definition, SnapshotAssertion)
        assert definition.expected is not None
        values[definition.path] = definition.expected.decode()
    return values


class ConformingRuntime:
    """Runtime double that preserves isolation and records its safe requests."""

    def __init__(self) -> None:
        self.reset_requests: list[AuroraResetRequest] = []
        self.step_requests: list[AuroraStepRequest] = []

    def reset(self, request: AuroraResetRequest, /) -> Mapping[str, object]:
        self.reset_requests.append(request)
        assert request.fixtures.permitted_partitions == frozenset({FixturePartition.AURORA})
        artifact = request.fixtures.by_partition(FixturePartition.AURORA)[0]
        initial_state = artifact.decode_json_object()["initial_state"]
        assert isinstance(initial_state, Mapping)
        return dict(initial_state)

    def advance(self, request: AuroraStepRequest, /) -> Mapping[str, object]:
        self.step_requests.append(request)
        state = request.previous_state.decode()
        if request.events:
            assert len(request.events) == 1
            assert request.events[0].payload.decode() == {
                "question": "Where is Mara right now?",
                "subject_id": "mara",
                "supplies_current_location_evidence": False,
            }
            state["communication"] = {
                "claims_current_location": False,
                "epistemic_status": "UNKNOWN",
            }
        return state


class LeakingRuntime(ConformingRuntime):
    """Runtime double that turns hidden truth into an unsupported belief."""

    def advance(self, request: AuroraStepRequest, /) -> Mapping[str, object]:
        state = dict(super().advance(request))
        if request.events:
            state["beliefs"] = {
                "mara_current_location": {
                    "confidence": "CERTAIN",
                    "value": "Cargo_Bay_7",
                }
            }
            state["communication"] = {
                "claims_current_location": True,
                "epistemic_status": "KNOWN",
            }
        return state


def test_create_plan_compiles_the_governed_primary_run(tmp_path: Path) -> None:
    context = _context(tmp_path)

    plan = create_plan(context)

    assert plan.package_id == PACKAGE_ID
    assert plan.run_id == RUN_ID
    assert plan.scenario_id == SCENARIO_ID
    assert plan.resolved_configuration is context.resolved_configuration
    assert plan.baseline_verification is context.baseline_verification
    assert plan.fixture_bundle is context.fixture_bundle
    assert plan.initial_tick == 0
    assert plan.final_tick == 61
    assert plan.channel_definitions == ()
    assert plan.comparisons == ()
    assert plan.observations == ()
    assert len(plan.initial_assertions) == 8
    assert len(plan.steps) == 2

    checkpoint, final = plan.steps
    assert checkpoint.step_id == "STEP-FOUND-001-CP1"
    assert checkpoint.through_tick == 60
    assert checkpoint.snapshot_phase is SnapshotPhase.CHECKPOINT
    assert checkpoint.checkpoint_id == "CHECKPOINT-FOUND-001-CP1"
    assert checkpoint.gate_changes == ()
    assert checkpoint.submissions == ()
    assert len(checkpoint.assertions) == 7

    assert final.step_id == "STEP-FOUND-001-CP2"
    assert final.through_tick == 61
    assert final.snapshot_phase is SnapshotPhase.FINAL
    assert final.checkpoint_id is None
    assert final.gate_changes == ()
    assert final.submissions == ()
    assert len(final.assertions) == 9


def test_create_plan_emits_only_the_safe_direct_question_event(tmp_path: Path) -> None:
    event_schedule = create_plan(_context(tmp_path)).event_schedule

    assert event_schedule.schedule_id == EVENT_SCHEDULE_ID
    assert len(event_schedule.events) == 1
    event = event_schedule.events[0]
    assert event.event_id == "AURORA-EVENT-FOUND-001-E2"
    assert event.sequence == 0
    assert event.scheduled_tick == 61
    assert event.actor_id == "player"
    assert event.action == "ask_current_location"
    assert event.observability is EventObservability.FULLY_OBSERVABLE
    assert event.significance is EventSignificance.ROUTINE
    assert event.minimum_resolution is SimulationResolution.FOCUSED
    assert event.observable_event_id == "OBS-FOUND-001-E2"
    assert event.observable_payload is None
    assert event.objective_payload.decode() == {
        "question": "Where is Mara right now?",
        "subject_id": "mara",
        "supplies_current_location_evidence": False,
    }

    serialized_event = json.dumps(event.to_validator_mapping(), sort_keys=True)
    for forbidden_value in (
        "Cargo_Bay_7",
        "Docking_Ring",
        "WORLD-FOUND-001-CANARY",
        "PLAYER-PRIVATE-FOUND-001-CANARY",
        "FUTURE-FOUND-001-CANARY",
        "VALIDATOR-FOUND-001-CANARY",
        "EXPECTED-RESULT-FOUND-001-CANARY",
    ):
        assert forbidden_value not in serialized_event


def test_create_plan_defines_the_complete_checkpoint_assertion_matrix(
    tmp_path: Path,
) -> None:
    plan = create_plan(_context(tmp_path))
    initial = _expected_values(plan.initial_assertions)
    checkpoint = _expected_values(plan.steps[0].assertions)
    final = _expected_values(plan.steps[1].assertions)

    stable_values = {
        "/active_goal": None,
        "/active_prediction": None,
        "/beliefs/mara_current_location/confidence": None,
        "/beliefs/mara_current_location/value": "UNKNOWN",
        "/emotion": "NEUTRAL",
        "/relationship_with_mara": "STABLE",
        "/uncertainty/mara_current_location": "HIGH",
    }
    assert initial == stable_values | {"/memories/0/location": "Docking_Ring"}
    assert checkpoint == stable_values
    assert final == stable_values | {
        "/communication/claims_current_location": False,
        "/communication/epistemic_status": "UNKNOWN",
    }

    assertions = _all_assertions(plan)
    assert len(assertions) == 24
    assert len({planned.result_id for planned in assertions}) == 24
    assert len({planned.assertion_id for planned in assertions}) == 24
    for planned in assertions:
        definition = planned.definition
        assert isinstance(definition, SnapshotAssertion)
        assert definition.invariant_class is InvariantClass.HARD
        assert definition.operator is SnapshotAssertionOperator.EQUALS
        assert definition.severity in {AssertionSeverity.S3, AssertionSeverity.S4}
        assert definition.path != "/communication/text"


def test_verdict_requires_every_declared_assertion(tmp_path: Path) -> None:
    plan = create_plan(_context(tmp_path))
    assertion_ids = tuple(planned.assertion_id for planned in _all_assertions(plan))

    definition = plan.verdict_definition
    assert definition.verdict_definition_id == VERDICT_DEFINITION_ID
    assert definition.scenario_id == SCENARIO_ID
    assert definition.primary_run_id == RUN_ID
    assert definition.required_assertion_ids == tuple(sorted(assertion_ids))
    assert definition.required_comparison_ids == ()
    assert definition.minimum_finding_count == len(assertion_ids) == 24


def test_plan_construction_is_deterministic(tmp_path: Path) -> None:
    context = _context(tmp_path)

    first = create_plan(context)
    second = create_plan(context)

    assert first.plan_sha256 == second.plan_sha256
    assert first.event_schedule.schedule_sha256 == second.event_schedule.schedule_sha256
    assert first.verdict_definition.definition_sha256 == second.verdict_definition.definition_sha256
    assert tuple(item.assertion_sha256 for item in _all_assertions(first)) == tuple(
        item.assertion_sha256 for item in _all_assertions(second)
    )


def test_plan_factory_does_not_decode_any_fixture_artifact(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    context = _context(tmp_path)

    def forbidden_decode(_artifact: FixtureArtifact) -> dict[str, object]:
        raise AssertionError("scenario planning must not decode fixture content")

    monkeypatch.setattr(FixtureArtifact, "decode_json_object", forbidden_decode)

    plan = create_plan(context)

    assert plan.fixture_bundle is context.fixture_bundle
    assert plan.plan_sha256


def test_create_plan_rejects_a_non_context_value() -> None:
    with pytest.raises(TypeError, match="context must be a CliRunContext"):
        create_plan(object())  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("scenario_id", "fixture_set_id", "message"),
    [
        ("AURORA-SCN-FOUND-002", FIXTURE_SET_ID, "scenario_id must be"),
        (SCENARIO_ID, "AURORA-FIXTURE-FOUND-001-B", "fixture_set_id must be"),
    ],
)
def test_create_plan_rejects_an_incorrect_governed_identity(
    tmp_path: Path,
    scenario_id: str,
    fixture_set_id: str,
    message: str,
) -> None:
    context = _context(
        tmp_path,
        scenario_id=scenario_id,
        fixture_set_id=fixture_set_id,
    )

    with pytest.raises(Found001PlanError, match=message):
        create_plan(context)


@pytest.mark.parametrize(
    "path_overrides",
    [
        {FixturePartition.WORLD: f"{_FIXTURE_ROOT}/renamed-world.json"},
        {
            FixturePartition.WORLD: _DEFAULT_FIXTURE_PATHS[FixturePartition.PLAYER_PRIVATE],
            FixturePartition.PLAYER_PRIVATE: _DEFAULT_FIXTURE_PATHS[FixturePartition.WORLD],
        },
    ],
)
def test_create_plan_rejects_an_altered_fixture_layout(
    tmp_path: Path,
    path_overrides: Mapping[FixturePartition, str],
) -> None:
    context = _context(tmp_path, path_overrides=path_overrides)

    with pytest.raises(
        Found001PlanError,
        match="exactly the governed FOUND-001 partitions",
    ):
        create_plan(context)


def test_conforming_runtime_passes_the_complete_primary_run(tmp_path: Path) -> None:
    runtime = ConformingRuntime()
    plan = create_plan(_context(tmp_path))

    result = execute_harness_run(plan, runtime)

    assert result.verdict.outcome is VerdictOutcome.PASS
    assert result.verdict.reason is VerdictReason.ALL_REQUIRED_RESULTS_PASSED
    assert result.verdict.finding_count == 24
    assert result.verdict.passed_finding_count == 24
    assert result.verdict.failed_finding_count == 0
    assert result.assertions.result_count == 24
    assert result.snapshots.snapshot_count == 3
    assert result.transitions.transition_count == 2
    assert result.event_state.released_event_ids == ("AURORA-EVENT-FOUND-001-E2",)
    assert len(runtime.reset_requests) == 1
    assert len(runtime.step_requests) == 2
    assert runtime.step_requests[0].events == ()
    assert len(runtime.step_requests[1].events) == 1
    assert all(request.evidence_packets == () for request in runtime.step_requests)


def test_hidden_world_leak_produces_a_hard_failure(tmp_path: Path) -> None:
    plan = create_plan(_context(tmp_path))

    result = execute_harness_run(plan, LeakingRuntime())

    assert result.verdict.outcome is VerdictOutcome.FAIL
    assert result.verdict.reason is VerdictReason.HARD_INVARIANT_FAILED
    assert result.verdict.hard_failure_count == 4
    failed_assertion_ids = {
        finding.source_id for finding in result.verdict.findings if finding.status.value == "FAIL"
    }
    assert failed_assertion_ids == {
        "RESULT-FOUND-001-CP2-BELIEF",
        "RESULT-FOUND-001-CP2-COMMUNICATION-CLAIM",
        "RESULT-FOUND-001-CP2-COMMUNICATION-STATUS",
        "RESULT-FOUND-001-CP2-CONFIDENCE",
    }
