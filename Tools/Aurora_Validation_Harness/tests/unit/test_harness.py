"""Unit tests for fail-closed Aurora validation-run orchestration."""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from dataclasses import FrozenInstanceError, replace
from pathlib import Path
from typing import Any

import pytest

from aurora_validation_harness import harness as harness_module
from aurora_validation_harness.assertions import (
    AssertionSeverity,
    InvariantClass,
    SnapshotAssertion,
    SnapshotAssertionOperator,
    TransitionAssertion,
    TransitionAssertionOperator,
    create_assertion_series,
    create_snapshot_assertion,
    create_transition_assertion,
)
from aurora_validation_harness.baseline import (
    BaselineState,
    BaselineVerificationResult,
    VerificationStatus,
)
from aurora_validation_harness.channels import (
    AuroraEvidencePacket,
    ChannelDefinition,
    ChannelGateState,
    ChannelKind,
    EvidenceSubmission,
    RoutingReason,
    RoutingStatus,
    create_channel_state,
    create_evidence_claim,
    route_submission,
)
from aurora_validation_harness.comparison import (
    ComparisonKind,
    ComparisonPolicy,
    ComparisonReason,
    ComparisonReport,
    ComparisonStatus,
)
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
    AuroraEvent,
    EventObservability,
    EventRuntimeState,
    EventSchedule,
    EventSignificance,
    ScheduledEvent,
    SimulationResolution,
    create_event_payload,
)
from aurora_validation_harness.evidence import (
    EvidenceDomain,
    EvidenceKind,
    create_evidence_ledger,
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
    AURORA_RUNTIME_PRODUCER_ID,
    AURORA_SUBJECT_ID,
    HARNESS_PRODUCER_ID,
    MAX_HARNESS_STEPS,
    MAX_STEP_ASSERTIONS,
    MAX_STEP_GATE_CHANGES,
    MAX_STEP_SUBMISSIONS,
    MAX_TICK,
    SUPPORTED_HARNESS_SCHEMA_VERSION,
    AuroraResetRequest,
    AuroraRuntime,
    AuroraStepRequest,
    ChannelGateChange,
    HarnessError,
    HarnessFailureReason,
    HarnessPhase,
    HarnessRunPlan,
    HarnessRunResult,
    HarnessStep,
    PlannedAssertion,
    RoutingAudit,
    calculate_harness_plan_sha256,
    execute_harness_run,
    validate_harness_run_result,
)
from aurora_validation_harness.partitions import (
    AccessPrincipal,
    PartitionedFixtureStore,
)
from aurora_validation_harness.snapshots import (
    SnapshotPhase,
    SnapshotSeries,
    append_state_snapshot,
    create_snapshot_series,
    create_snapshot_state,
)
from aurora_validation_harness.transitions import TransitionSeries, create_transition_series
from aurora_validation_harness.verdicts import (
    ObservationCategory,
    VerdictDefinition,
    create_comparison_finding,
    create_verdict_definition,
    create_verdict_observation,
)

pytestmark = [
    pytest.mark.foundation,
    pytest.mark.isolation,
    pytest.mark.metamorphic,
]

_RUN_ID = "AURORA-RUN-FOUND-001-BASE"
_CANDIDATE_RUN_ID = "AURORA-RUN-FOUND-001-CAND"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"
_FIXTURE_SET_ID = "AURORA-FIXTURE-FOUND-001-A"
_BASELINE_ID = "AURORA-FOUNDATION-BASELINE-001"
_CHANNEL_ID = "CH-SENSOR-001"
_SECOND_CHANNEL_ID = "CH-AUDIO-001"
_SOURCE_ID = "STATION-SENSOR-001"
_EVENT_ID = "AURORA-SCN-FOUND-001-E001"
_OBSERVABLE_EVENT_ID = "OBS-FOUND-001"


class RecordingRuntime:
    """Stateful deterministic runtime double that records its safe inputs."""

    def __init__(
        self,
        *,
        reset_value: object | None = None,
        advance_value: object | None = None,
        reset_error: Exception | None = None,
        advance_error: Exception | None = None,
    ) -> None:
        self.reset_requests: list[AuroraResetRequest] = []
        self.step_requests: list[AuroraStepRequest] = []
        self.reset_value = reset_value
        self.advance_value = advance_value
        self.reset_error = reset_error
        self.advance_error = advance_error

    def reset(self, request: AuroraResetRequest, /) -> Mapping[str, object]:
        self.reset_requests.append(request)
        if self.reset_error is not None:
            raise self.reset_error
        if self.reset_value is not None:
            return self.reset_value  # type: ignore[return-value]
        return {"ready": True, "tick": request.initial_tick, "visible_inputs": 0}

    def advance(self, request: AuroraStepRequest, /) -> Mapping[str, object]:
        self.step_requests.append(request)
        if self.advance_error is not None:
            raise self.advance_error
        if self.advance_value is not None:
            return self.advance_value  # type: ignore[return-value]
        return {
            "ready": True,
            "tick": request.through_tick,
            "visible_inputs": len(request.events) + len(request.evidence_packets),
        }


def _json_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode()


def _fixture_bundle(repository_root: Path) -> FixtureBundle:
    contents = {
        FixturePartition.WORLD: {"world_secret": "CARGO-7"},
        FixturePartition.AURORA: {"known_location": "UNKNOWN"},
        FixturePartition.PLAYER_PRIVATE: {"player_secret": True},
        FixturePartition.FUTURE: {"future_event": "SEALED"},
        FixturePartition.VALIDATOR: {"expected_result": "UNKNOWN"},
        FixturePartition.EXPECTED_RESULTS: {"answer": "UNKNOWN"},
    }
    artifacts: list[FixtureArtifact] = []
    definitions: list[FixtureFile] = []
    for partition in FixturePartition:
        content = _json_bytes(contents[partition])
        filename = partition.value.lower().replace("_", "-") + ".json"
        relative_path = f"Development/Validation/Aurora/Fixtures/FOUND-001/{filename}"
        definition = FixtureFile(
            path=relative_path,
            partition=partition,
            media_type=FixtureMediaType.JSON,
            sha256=hashlib.sha256(content).hexdigest(),
            size_bytes=len(content),
        )
        definitions.append(definition)
        artifacts.append(
            FixtureArtifact(
                definition=definition,
                resolved_path=repository_root / relative_path,
                content_bytes=content,
            )
        )
    unsigned = FixtureManifest(
        fixture_set_id=_FIXTURE_SET_ID,
        scenario_id=_SCENARIO_ID,
        fixture_manifest_version=SUPPORTED_FIXTURE_MANIFEST_VERSION,
        files=tuple(definitions),
    )
    manifest = replace(
        unsigned,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(unsigned),
    )
    return FixtureBundle(manifest, repository_root, tuple(artifacts))


def _configuration(
    repository_root: Path,
    *,
    mode: RunMode = RunMode.DRY_RUN,
) -> ResolvedConfiguration:
    policy = ExecutionPolicy(
        run_mode=mode,
        random_seed=41001,
        deterministic=True,
        strict_isolation=True,
        reset_before_run=True,
        network_access_enabled=False,
        telemetry_feedback_enabled=False,
        allow_output_overwrite=False,
    )
    unsigned = HarnessConfiguration(
        configuration_id="AURORA-CONFIG-FOUND-001-DRY",
        configuration_version=SUPPORTED_CONFIGURATION_VERSION,
        scenario_id=_SCENARIO_ID,
        baseline_id=_BASELINE_ID,
        baseline_manifest_path="Development/Validation/Aurora/Baseline/baseline.json",
        fixture_set_id=_FIXTURE_SET_ID,
        fixture_manifest_path=(
            "Development/Validation/Aurora/Fixtures/FOUND-001/fixture-manifest.json"
        ),
        output_root=RUN_OUTPUT_ROOT,
        execution=policy,
    )
    signed = replace(
        unsigned,
        configuration_sha256=calculate_configuration_sha256(unsigned),
    )
    output_root = repository_root / RUN_OUTPUT_ROOT
    output_root.parent.mkdir(parents=True, exist_ok=True)
    return ResolvedConfiguration(
        configuration=signed,
        repository_root=repository_root,
        baseline_manifest=repository_root / signed.baseline_manifest_path,
        fixture_manifest=repository_root / signed.fixture_manifest_path,
        output_root=output_root,
    )


def _baseline(
    *,
    status: VerificationStatus = VerificationStatus.VERIFIED,
    state: BaselineState = BaselineState.EXECUTION_BASELINE_READY,
) -> BaselineVerificationResult:
    return BaselineVerificationResult(
        baseline_id=_BASELINE_ID,
        status=status,
        baseline_state=state,
        calculated_manifest_sha256="a" * 64,
        declared_manifest_sha256="a" * 64,
        files=(),
        issues=(),
    )


def _event_schedule() -> EventSchedule:
    visible = ScheduledEvent(
        event_id=_EVENT_ID,
        sequence=0,
        scheduled_tick=1,
        actor_id="Harness",
        action="processing_interval",
        observability=EventObservability.FULLY_OBSERVABLE,
        significance=EventSignificance.ROUTINE,
        minimum_resolution=SimulationResolution.ACTIVE,
        objective_payload=create_event_payload({"duration_ticks": 1}),
        observable_event_id=_OBSERVABLE_EVENT_ID,
    )
    hidden = ScheduledEvent(
        event_id="AURORA-SCN-FOUND-001-E002",
        sequence=1,
        scheduled_tick=2,
        actor_id="WorldRuntime",
        action="hidden_world_change",
        observability=EventObservability.HIDDEN,
        significance=EventSignificance.MAJOR,
        minimum_resolution=SimulationResolution.DEEP,
        objective_payload=create_event_payload({"hidden_location": "CARGO-7"}),
    )
    return EventSchedule("AURORA-EVENTS-FOUND-001", (visible, hidden))


def _channel_definitions() -> tuple[ChannelDefinition, ...]:
    return (
        ChannelDefinition(
            _SECOND_CHANNEL_ID,
            ChannelKind.COMMUNICATION,
            "STATION-AUDIO-001",
        ),
        ChannelDefinition(_CHANNEL_ID, ChannelKind.SENSOR, _SOURCE_ID),
    )


def _submission(
    *,
    evidence_id: str = "EVIDENCE-FOUND-001",
    tick: int = 2,
    channel_id: str = _CHANNEL_ID,
) -> EvidenceSubmission:
    return EvidenceSubmission(
        evidence_id=evidence_id,
        channel_id=channel_id,
        source_id=_SOURCE_ID,
        validator_event_id=_EVENT_ID,
        observed_at_tick=tick,
        submitted_at_tick=tick,
        claim=create_evidence_claim("Mara", "reported_location", "platform-2"),
    )


def _snapshot_assertion(
    *,
    assertion_id: str = "ASSERTION-FOUND-001-S1",
    path: str = "/ready",
) -> SnapshotAssertion:
    return create_snapshot_assertion(
        assertion_id=assertion_id,
        invariant_id="AURORA-INFO-001",
        invariant_class=InvariantClass.HARD,
        severity=AssertionSeverity.S4,
        operator=SnapshotAssertionOperator.EXISTS,
        path=path,
    )


def _transition_assertion() -> TransitionAssertion:
    return create_transition_assertion(
        assertion_id="ASSERTION-FOUND-001-T1",
        invariant_id="AURORA-INFO-002",
        invariant_class=InvariantClass.HARD,
        severity=AssertionSeverity.S4,
        operator=TransitionAssertionOperator.PATH_CHANGED,
        path="/tick",
    )


def _comparison_report() -> ComparisonReport:
    return ComparisonReport(
        report_id="REPORT-FOUND-001-C1",
        comparison_id="COMPARISON-FOUND-001-C1",
        comparison_definition_sha256="b" * 64,
        scenario_id=_SCENARIO_ID,
        baseline_run_id=_RUN_ID,
        baseline_series_sha256="c" * 64,
        candidate_run_id=_CANDIDATE_RUN_ID,
        candidate_series_sha256="d" * 64,
        evaluated_at_tick=2,
        invariant_id="AURORA-INFO-003",
        invariant_class=InvariantClass.SOFT,
        severity=AssertionSeverity.S2,
        kind=ComparisonKind.REPEATABILITY,
        policy=ComparisonPolicy.EXACT,
        status=ComparisonStatus.PASS,
        reason=ComparisonReason.EXACT_MATCH,
        pairs=(),
        violations=(),
    )


def _verdict_definition(
    *,
    include_comparison: bool = False,
) -> VerdictDefinition:
    return create_verdict_definition(
        verdict_definition_id="VERDICT-DEFINITION-FOUND-001",
        scenario_id=_SCENARIO_ID,
        primary_run_id=_RUN_ID,
        required_assertion_ids=(
            "ASSERTION-FOUND-001-S1",
            "ASSERTION-FOUND-001-T1",
        ),
        required_comparison_ids=(("COMPARISON-FOUND-001-C1",) if include_comparison else ()),
        minimum_finding_count=3 if include_comparison else 2,
    )


def _plan(
    tmp_path: Path,
    *,
    with_comparison: bool = False,
    run_mode: RunMode = RunMode.DRY_RUN,
) -> HarnessRunPlan:
    repository_root = tmp_path / "repository"
    resolved = _configuration(repository_root, mode=run_mode)
    comparison = _comparison_report()
    comparisons = (comparison,) if with_comparison else ()
    observations = (
        (
            create_verdict_observation(
                observation_id="OBSERVATION-FOUND-001-O1",
                category=ObservationCategory.EMERGENCE,
                observation_code="VALID-NOVEL-BEHAVIOR",
                finding=create_comparison_finding(comparison),
            ),
        )
        if with_comparison
        else ()
    )
    initial = PlannedAssertion("RESULT-FOUND-001-S1", _snapshot_assertion())
    transition = PlannedAssertion("RESULT-FOUND-001-T1", _transition_assertion())
    submission = _submission()
    final_step = HarnessStep(
        step_id="STEP-FOUND-001-FINAL",
        through_tick=2,
        snapshot_phase=SnapshotPhase.FINAL,
        gate_changes=(ChannelGateChange(_CHANNEL_ID, ChannelGateState.OPEN),),
        submissions=(submission, submission),
        assertions=(transition,),
    )
    return HarnessRunPlan(
        package_id="PACKAGE-FOUND-001",
        run_id=_RUN_ID,
        resolved_configuration=resolved,
        baseline_verification=_baseline(
            state=(
                BaselineState.FORMAL_EXECUTION_ACTIVE
                if run_mode is RunMode.FORMAL
                else BaselineState.EXECUTION_BASELINE_READY
            )
        ),
        fixture_bundle=_fixture_bundle(repository_root),
        event_schedule=_event_schedule(),
        channel_definitions=_channel_definitions(),
        initial_tick=0,
        initial_assertions=(initial,),
        steps=(final_step,),
        verdict_definition=_verdict_definition(include_comparison=with_comparison),
        comparisons=comparisons,
        observations=observations,
    )


def _assert_harness_error(
    error: pytest.ExceptionInfo[HarnessError],
    *,
    phase: HarnessPhase,
    reason: HarnessFailureReason,
    match: str,
) -> None:
    assert error.value.phase is phase
    assert error.value.reason is reason
    assert match in error.value.detail
    assert str(error.value).startswith(f"{phase.value}/{reason.value}: ")


def _replace_plan(plan: HarnessRunPlan, **changes: object) -> HarnessRunPlan:
    return replace(plan, **changes)  # type: ignore[arg-type]


def _replace_result(result: HarnessRunResult, **changes: object) -> HarnessRunResult:
    return replace(result, **changes)  # type: ignore[arg-type]


def test_public_constants_and_enums_define_stable_contract() -> None:
    assert SUPPORTED_HARNESS_SCHEMA_VERSION == "1.0"
    assert MAX_HARNESS_STEPS == 10_000
    assert MAX_STEP_GATE_CHANGES == 1_000
    assert MAX_STEP_SUBMISSIONS == 10_000
    assert MAX_STEP_ASSERTIONS == 10_000
    assert MAX_TICK == (1 << 63) - 1
    assert HARNESS_PRODUCER_ID == "AURORA-VALIDATION-HARNESS"
    assert AURORA_RUNTIME_PRODUCER_ID == "AURORA-RUNTIME"
    assert AURORA_SUBJECT_ID == "aurora"
    assert {item.value for item in HarnessPhase} == {
        "PREPARING",
        "RESETTING",
        "EXECUTING",
        "EVALUATING",
        "FINALIZING",
        "STORING",
        "VERIFYING",
        "COMPLETE",
    }
    assert len(HarnessFailureReason) == 10


@pytest.mark.parametrize("field", ["phase", "reason", "message"])
def test_harness_error_validates_and_exposes_machine_fields(field: str) -> None:
    values: dict[str, object] = {
        "phase": HarnessPhase.EXECUTING,
        "reason": HarnessFailureReason.STEP_FAILED,
        "message": "step stopped",
    }
    values[field] = object() if field != "message" else " "
    with pytest.raises(TypeError):
        HarnessError(**values)  # type: ignore[arg-type]

    error = HarnessError(
        HarnessPhase.EXECUTING,
        HarnessFailureReason.STEP_FAILED,
        "step stopped",
    )
    assert error.phase is HarnessPhase.EXECUTING
    assert error.reason is HarnessFailureReason.STEP_FAILED
    assert error.detail == "step stopped"
    assert str(error) == "EXECUTING/STEP_FAILED: step stopped"


def test_small_plan_models_are_immutable_and_redact_validator_content(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    change = plan.steps[0].gate_changes[0]
    snapshot_planned = plan.initial_assertions[0]
    transition_planned = plan.steps[0].assertions[0]

    assert change.to_mapping() == {"channel_id": _CHANNEL_ID, "gate": "OPEN"}
    assert snapshot_planned.to_mapping()["assertion_type"] == "SNAPSHOT_ASSERTION"
    assert transition_planned.to_mapping()["assertion_type"] == "TRANSITION_ASSERTION"
    assert snapshot_planned.assertion_id == "ASSERTION-FOUND-001-S1"
    assert len(snapshot_planned.assertion_sha256) == 64
    assert plan.steps[0].to_mapping()["submission_ids"] == [
        "EVIDENCE-FOUND-001",
        "EVIDENCE-FOUND-001",
    ]
    assert "expected" not in json.dumps(plan.to_mapping())
    with pytest.raises(FrozenInstanceError):
        change.channel_id = "CH-TAMPER-001"  # type: ignore[misc]


@pytest.mark.parametrize(
    ("factory", "message"),
    [
        (lambda: ChannelGateChange("bad", ChannelGateState.OPEN), "channel_id"),
        (
            lambda: ChannelGateChange(
                _CHANNEL_ID,
                "OPEN",  # type: ignore[arg-type]
            ),
            "gate",
        ),
        (lambda: PlannedAssertion("bad", _snapshot_assertion()), "result_id"),
        (
            lambda: PlannedAssertion(
                "RESULT-001",
                object(),  # type: ignore[arg-type]
            ),
            "definition",
        ),
    ],
)
def test_small_plan_models_reject_invalid_values(factory: Any, message: str) -> None:
    with pytest.raises(HarnessError, match=message) as error:
        factory()
    assert error.value.phase is HarnessPhase.PREPARING
    assert error.value.reason is HarnessFailureReason.PRECONDITION_INVALID


def test_harness_step_supports_checkpoint_and_rejects_invalid_shapes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    checkpoint = HarnessStep(
        "STEP-FOUND-001-CP1",
        5,
        SnapshotPhase.CHECKPOINT,
        checkpoint_id="CHECKPOINT-001",
    )
    assert checkpoint.to_mapping()["checkpoint_id"] == "CHECKPOINT-001"

    bad_cases: tuple[dict[str, object], ...] = (
        {"snapshot_phase": SnapshotPhase.INITIAL},
        {"snapshot_phase": SnapshotPhase.CHECKPOINT},
        {"snapshot_phase": SnapshotPhase.CHECKPOINT, "checkpoint_id": "bad"},
        {"snapshot_phase": SnapshotPhase.FINAL, "checkpoint_id": "CHECKPOINT-001"},
        {"gate_changes": []},
        {"submissions": []},
        {"assertions": []},
        {
            "gate_changes": (
                ChannelGateChange(_CHANNEL_ID, ChannelGateState.OPEN),
                ChannelGateChange(_CHANNEL_ID, ChannelGateState.CLOSED),
            )
        },
        {"through_tick": 1, "submissions": (_submission(tick=2),)},
    )
    for changes in bad_cases:
        values: dict[str, object] = {
            "step_id": "STEP-FOUND-001",
            "through_tick": 2,
            "snapshot_phase": SnapshotPhase.FINAL,
        }
        values.update(changes)
        with pytest.raises(HarnessError) as error:
            HarnessStep(**values)  # type: ignore[arg-type]
        assert error.value.reason is HarnessFailureReason.PRECONDITION_INVALID

    monkeypatch.setattr(harness_module, "MAX_STEP_GATE_CHANGES", 0)
    with pytest.raises(HarnessError, match="must not exceed"):
        HarnessStep(
            "STEP-FOUND-001",
            2,
            SnapshotPhase.FINAL,
            gate_changes=(ChannelGateChange(_CHANNEL_ID, ChannelGateState.OPEN),),
        )


def test_reset_request_exposes_only_aurora_capability(tmp_path: Path) -> None:
    bundle = _fixture_bundle(tmp_path)
    store = PartitionedFixtureStore(bundle)
    view = store.view_for(AccessPrincipal.AURORA_RUNTIME)
    request = AuroraResetRequest(_RUN_ID, 7, 0, view)
    mapping = request.to_evidence_mapping()

    assert request.fixtures.principal is AccessPrincipal.AURORA_RUNTIME
    assert request.fixtures.permitted_partitions == frozenset({FixturePartition.AURORA})
    assert len(request.fixtures.artifacts) == 1
    assert mapping["accessible_fixture_artifact_ids"] == list(view.available_artifact_ids)
    serialized = json.dumps(mapping)
    assert _SCENARIO_ID not in serialized
    assert "world_secret" not in serialized
    assert "expected_result" not in serialized


def test_reset_request_rejects_invalid_contract_values(tmp_path: Path) -> None:
    store = PartitionedFixtureStore(_fixture_bundle(tmp_path))
    aurora_view = store.view_for(AccessPrincipal.AURORA_RUNTIME)
    validator_view = store.view_for(AccessPrincipal.VALIDATOR)
    cases: tuple[tuple[object, ...], ...] = (
        ("bad", 1, 0, aurora_view),
        (_RUN_ID, True, 0, aurora_view),
        (_RUN_ID, -1, 0, aurora_view),
        (_RUN_ID, 1, -1, aurora_view),
        (_RUN_ID, 1, 0, object()),
        (_RUN_ID, 1, 0, validator_view),
    )
    for values in cases:
        with pytest.raises(HarnessError):
            AuroraResetRequest(*values)  # type: ignore[arg-type]


def _aurora_event(*, event_id: str = _OBSERVABLE_EVENT_ID, tick: int = 1) -> AuroraEvent:
    return AuroraEvent(event_id, tick, create_event_payload({"visible": True}))


def _packet(*, evidence_id: str = "EVIDENCE-FOUND-001", tick: int = 1) -> AuroraEvidencePacket:
    definition = ChannelDefinition(_CHANNEL_ID, ChannelKind.SENSOR, _SOURCE_ID)
    submission = _submission(evidence_id=evidence_id, tick=tick)
    result = route_submission(
        definition,
        create_channel_state(definition, gate=ChannelGateState.OPEN),
        submission,
    )
    assert result.packet is not None
    return result.packet


def test_step_request_round_trips_safe_inputs_and_rejects_invalid_contracts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    state = create_snapshot_state({"tick": 0})
    event = _aurora_event()
    packet = _packet()
    request = AuroraStepRequest(_RUN_ID, 0, 1, state, (event,), (packet,))
    mapping = request.to_evidence_mapping()
    assert mapping["events"] == [event.to_mapping()]
    assert mapping["evidence_packets"] == [packet.to_mapping()]
    assert mapping["previous_state_sha256"] == state.state_sha256

    cases: tuple[dict[str, object], ...] = (
        {"through_tick": -1},
        {"previous_tick": 2, "through_tick": 1},
        {"previous_state": object()},
        {"events": []},
        {"evidence_packets": []},
        {"events": (event, event)},
        {"evidence_packets": (packet, packet)},
        {"through_tick": 0, "events": (event,)},
        {"through_tick": 0, "evidence_packets": (packet,)},
    )
    for changes in cases:
        values: dict[str, object] = {
            "run_id": _RUN_ID,
            "previous_tick": 0,
            "through_tick": 1,
            "previous_state": state,
            "events": (),
            "evidence_packets": (),
        }
        values.update(changes)
        with pytest.raises(HarnessError) as error:
            AuroraStepRequest(**values)  # type: ignore[arg-type]
        assert error.value.reason in {
            HarnessFailureReason.PRECONDITION_INVALID,
            HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
            HarnessFailureReason.RESULT_INVALID,
        }

    monkeypatch.setattr(harness_module, "MAX_STEP_SUBMISSIONS", 0)
    with pytest.raises(HarnessError, match="must not exceed"):
        AuroraStepRequest(_RUN_ID, 0, 1, state, (event,), ())


def test_routing_audit_redacts_claim_and_validates_cross_links() -> None:
    definition = ChannelDefinition(_CHANNEL_ID, ChannelKind.SENSOR, _SOURCE_ID)
    submission = _submission(tick=1)
    admitted = route_submission(
        definition,
        create_channel_state(definition, gate=ChannelGateState.OPEN),
        submission,
    )
    audit = RoutingAudit("STEP-FOUND-001", submission.evidence_id, _CHANNEL_ID, admitted)
    mapping = audit.to_mapping()
    assert mapping["status"] == "ADMITTED"
    assert mapping["reason"] == "ADMITTED"
    assert mapping["packet_sha256"] == admitted.packet.packet_sha256  # type: ignore[union-attr]
    assert "reported_location" not in json.dumps(mapping)

    blocked = route_submission(
        definition,
        create_channel_state(definition),
        submission,
    )
    blocked_audit = RoutingAudit(
        "STEP-FOUND-001",
        submission.evidence_id,
        _CHANNEL_ID,
        blocked,
    )
    assert blocked_audit.to_mapping()["packet_sha256"] is None

    with pytest.raises(HarnessError, match="result"):
        RoutingAudit("STEP-FOUND-001", submission.evidence_id, _CHANNEL_ID, object())  # type: ignore[arg-type]
    with pytest.raises(HarnessError, match="channel"):
        RoutingAudit("STEP-FOUND-001", submission.evidence_id, _SECOND_CHANNEL_ID, admitted)
    with pytest.raises(HarnessError, match="submission"):
        RoutingAudit("STEP-FOUND-001", "EVIDENCE-OTHER-001", _CHANNEL_ID, admitted)


def test_run_plan_is_hash_bound_canonical_and_supports_formal_mode(tmp_path: Path) -> None:
    plan = _plan(tmp_path, with_comparison=True)
    formal = _plan(tmp_path / "formal", run_mode=RunMode.FORMAL)
    mapping = plan.to_mapping()

    assert plan.scenario_id == _SCENARIO_ID
    assert plan.final_tick == 2
    assert plan.plan_sha256 == calculate_harness_plan_sha256(plan)
    assert mapping["plan_sha256"] == plan.plan_sha256
    assert mapping["comparisons"] == [plan.comparisons[0].report_sha256]
    assert mapping["observations"] == [plan.observations[0].observation_sha256]
    assert formal.baseline_verification.baseline_state is BaselineState.FORMAL_EXECUTION_ACTIVE
    assert (
        calculate_harness_plan_sha256(plan)
        == hashlib.sha256(
            json.dumps(
                plan._content_mapping(),
                allow_nan=False,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            ).encode()
        ).hexdigest()
    )


@pytest.mark.parametrize(
    "field",
    [
        "resolved_configuration",
        "baseline_verification",
        "fixture_bundle",
        "event_schedule",
        "verdict_definition",
    ],
)
def test_run_plan_rejects_invalid_required_runtime_types(tmp_path: Path, field: str) -> None:
    plan = _plan(tmp_path)
    with pytest.raises(HarnessError, match=field):
        _replace_plan(plan, **{field: object()})


@pytest.mark.parametrize(
    "field",
    [
        "channel_definitions",
        "initial_assertions",
        "steps",
        "comparisons",
        "observations",
    ],
)
def test_run_plan_rejects_non_tuple_collections(tmp_path: Path, field: str) -> None:
    with pytest.raises(HarnessError, match=field):
        _replace_plan(_plan(tmp_path), **{field: []})


def test_run_plan_rejects_identity_and_integrity_mismatches(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    unsigned_config = replace(plan.resolved_configuration.configuration, configuration_sha256=None)
    wrong_config = replace(
        unsigned_config,
        configuration_sha256="f" * 64,
    )
    config_wrong_baseline = replace(
        unsigned_config,
        baseline_id="AURORA-FOUNDATION-BASELINE-OTHER",
    )
    config_wrong_baseline = replace(
        config_wrong_baseline,
        configuration_sha256=calculate_configuration_sha256(config_wrong_baseline),
    )
    config_wrong_fixture = replace(
        unsigned_config,
        fixture_set_id="AURORA-FIXTURE-FOUND-001-B",
    )
    config_wrong_fixture = replace(
        config_wrong_fixture,
        configuration_sha256=calculate_configuration_sha256(config_wrong_fixture),
    )

    invalid_resolved = (
        replace(plan.resolved_configuration, configuration=unsigned_config),
        replace(plan.resolved_configuration, configuration=wrong_config),
        replace(plan.resolved_configuration, configuration=config_wrong_baseline),
        replace(plan.resolved_configuration, configuration=config_wrong_fixture),
        replace(plan.resolved_configuration, repository_root=tmp_path / "other-root"),
    )
    for resolved in invalid_resolved:
        with pytest.raises(HarnessError) as error:
            _replace_plan(plan, resolved_configuration=resolved)
        assert error.value.reason is HarnessFailureReason.PRECONDITION_INVALID

    for baseline in (
        _baseline(status=VerificationStatus.BLOCKED),
        replace(_baseline(), baseline_id="AURORA-FOUNDATION-BASELINE-OTHER"),
    ):
        with pytest.raises(HarnessError):
            _replace_plan(plan, baseline_verification=baseline)

    formal_policy = replace(
        plan.resolved_configuration.configuration.execution,
        run_mode=RunMode.FORMAL,
    )
    formal_unsigned = replace(
        unsigned_config,
        execution=formal_policy,
    )
    formal_config = replace(
        formal_unsigned,
        configuration_sha256=calculate_configuration_sha256(formal_unsigned),
    )
    with pytest.raises(HarnessError, match="FORMAL"):
        _replace_plan(
            plan,
            resolved_configuration=replace(
                plan.resolved_configuration,
                configuration=formal_config,
            ),
        )

    bad_manifest = replace(plan.fixture_bundle.manifest, fixture_manifest_sha256="e" * 64)
    with pytest.raises(HarnessError, match="manifest"):
        _replace_plan(
            plan,
            fixture_bundle=replace(plan.fixture_bundle, manifest=bad_manifest),
        )

    wrong_scenario_manifest = replace(
        plan.fixture_bundle.manifest,
        scenario_id="AURORA-SCN-OTHER-001",
    )
    with pytest.raises(HarnessError, match="fixture scenario"):
        _replace_plan(
            plan,
            fixture_bundle=replace(plan.fixture_bundle, manifest=wrong_scenario_manifest),
        )


def test_run_plan_requires_verified_property_even_with_verified_status(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    plan = _plan(tmp_path)
    monkeypatch.setattr(
        BaselineVerificationResult,
        "verified",
        property(lambda _verification: False),
    )
    with pytest.raises(HarnessError, match="not executable"):
        _replace_plan(plan)


def test_run_plan_rejects_verdict_and_comparison_identity_mismatches(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    wrong_scenario_definition = replace(
        plan.verdict_definition,
        scenario_id="AURORA-SCN-OTHER-001",
    )
    wrong_run_definition = replace(
        plan.verdict_definition,
        primary_run_id="AURORA-RUN-OTHER-001",
    )
    for definition in (wrong_scenario_definition, wrong_run_definition):
        with pytest.raises(HarnessError, match="verdict definition"):
            _replace_plan(plan, verdict_definition=definition)

    report = _comparison_report()
    with pytest.raises(HarnessError, match="comparison scenario"):
        _replace_plan(
            plan,
            comparisons=(replace(report, scenario_id="AURORA-SCN-OTHER-001"),),
        )
    with pytest.raises(HarnessError, match="include the primary run"):
        _replace_plan(
            plan,
            comparisons=(
                replace(
                    report,
                    baseline_run_id="AURORA-RUN-OTHER-001",
                    candidate_run_id="AURORA-RUN-OTHER-002",
                ),
            ),
        )


def test_run_plan_rejects_unsafe_or_incomplete_execution_topologies(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    transition_initial = PlannedAssertion("RESULT-FOUND-001-I1", _transition_assertion())
    duplicate_channel = (plan.channel_definitions[0], plan.channel_definitions[0])
    reversed_channels = tuple(reversed(plan.channel_definitions))
    early_final = HarnessStep("STEP-FOUND-001-A", 1, SnapshotPhase.FINAL)
    late_final = HarnessStep("STEP-FOUND-001-B", 2, SnapshotPhase.FINAL)
    nonfinal = HarnessStep("STEP-FOUND-001-A", 2, SnapshotPhase.POST_EVENT)
    backwards = HarnessStep("STEP-FOUND-001-B", 1, SnapshotPhase.FINAL)
    first = HarnessStep("STEP-FOUND-001-A", 2, SnapshotPhase.POST_EVENT)
    unknown_channel = HarnessStep(
        "STEP-FOUND-001-A",
        2,
        SnapshotPhase.FINAL,
        gate_changes=(ChannelGateChange("CH-UNKNOWN-001", ChannelGateState.OPEN),),
    )
    incomplete = HarnessStep("STEP-FOUND-001-A", 1, SnapshotPhase.FINAL)
    duplicate_result = HarnessStep(
        "STEP-FOUND-001-A",
        2,
        SnapshotPhase.FINAL,
        assertions=(PlannedAssertion("RESULT-FOUND-001-S1", _snapshot_assertion()),),
    )
    duplicate_step_a = HarnessStep(
        "STEP-DUPLICATE-001",
        1,
        SnapshotPhase.POST_EVENT,
    )
    duplicate_step_b = HarnessStep(
        "STEP-DUPLICATE-001",
        2,
        SnapshotPhase.FINAL,
    )

    cases = (
        {"steps": ()},
        {"channel_definitions": duplicate_channel},
        {"channel_definitions": reversed_channels},
        {"initial_assertions": (transition_initial,)},
        {"steps": (early_final, late_final)},
        {"steps": (nonfinal,)},
        {"steps": (first, backwards)},
        {"steps": (unknown_channel,)},
        {"steps": (incomplete,)},
        {"steps": (duplicate_result,)},
        {"steps": (duplicate_step_a, duplicate_step_b)},
    )
    for changes in cases:
        with pytest.raises(HarnessError) as error:
            _replace_plan(plan, **changes)
        assert error.value.phase is HarnessPhase.PREPARING
        assert error.value.reason is HarnessFailureReason.PRECONDITION_INVALID

    eventless = _replace_plan(
        plan,
        event_schedule=EventSchedule("AURORA-EVENTS-EMPTY-001", ()),
    )
    assert eventless.final_tick == 2


def test_execute_harness_run_isolates_inputs_and_publishes_verified_evidence(
    tmp_path: Path,
) -> None:
    plan = _plan(tmp_path, with_comparison=True)
    runtime = RecordingRuntime()

    assert isinstance(runtime, AuroraRuntime)
    result = execute_harness_run(plan, runtime)

    assert len(runtime.reset_requests) == 1
    assert len(runtime.step_requests) == 1
    reset = runtime.reset_requests[0]
    step = runtime.step_requests[0]
    assert reset.fixtures.principal is AccessPrincipal.AURORA_RUNTIME
    assert reset.fixtures.permitted_partitions == frozenset({FixturePartition.AURORA})
    assert [event.event_id for event in step.events] == [_OBSERVABLE_EVENT_ID]
    assert [packet.evidence_id for packet in step.evidence_packets] == ["EVIDENCE-FOUND-001"]
    assert _EVENT_ID not in json.dumps(step.to_evidence_mapping())
    assert "CARGO-7" not in json.dumps(step.to_evidence_mapping())

    assert result.snapshots.snapshot_count == 2
    assert result.transitions.transition_count == 1
    assert result.assertions.result_count == 2
    assert result.event_state.released_event_ids == (
        _EVENT_ID,
        "AURORA-SCN-FOUND-001-E002",
    )
    assert len(result.routing_audits) == 2
    assert result.routing_audits[0].result.status is RoutingStatus.ADMITTED
    assert result.routing_audits[1].result.reason is RoutingReason.DUPLICATE_EVIDENCE_ID
    assert tuple(state.channel_id for state in result.channel_states) == (
        _SECOND_CHANNEL_ID,
        _CHANNEL_ID,
    )
    assert result.verdict.outcome.value == "PASS_WITH_OBSERVATION"
    assert result.package_directory.is_dir()
    assert result.package_directory.name == _RUN_ID
    assert result.storage_manifest.manifest_sha256
    assert {record.kind for record in result.evidence.records} >= {
        EvidenceKind.RUN_CONFIGURATION,
        EvidenceKind.BASELINE_VERIFICATION,
        EvidenceKind.FIXTURE_INTEGRITY,
        EvidenceKind.AURORA_INPUT,
        EvidenceKind.EVENT_RELEASE,
        EvidenceKind.CHANNEL_ADMISSION,
        EvidenceKind.STATE_SNAPSHOT,
        EvidenceKind.STATE_TRANSITION,
        EvidenceKind.ASSERTION_RESULT,
        EvidenceKind.VERDICT,
    }
    channel_records = [
        record
        for record in result.evidence.records
        if record.kind is EvidenceKind.CHANNEL_ADMISSION
    ]
    assert [record.domain for record in channel_records] == [
        EvidenceDomain.AURORA_ACCESSIBLE,
        EvidenceDomain.VALIDATOR,
    ]
    assert any(
        artifact.relative_path == "evaluation/comparisons.json"
        for artifact in result.storage_manifest.artifacts
    )
    validate_harness_run_result(plan, result)
    summary = result.to_summary_mapping()
    assert summary["run_id"] == _RUN_ID
    assert summary["assertion_count"] == 2
    assert summary["routing_attempt_count"] == 2


def test_execute_without_comparisons_omits_comparison_artifact(tmp_path: Path) -> None:
    result = execute_harness_run(_plan(tmp_path), RecordingRuntime())
    assert result.verdict.outcome.value == "PASS"
    assert all(
        artifact.relative_path != "evaluation/comparisons.json"
        for artifact in result.storage_manifest.artifacts
    )


def test_execution_refuses_invalid_runtime_and_existing_output_before_reset(
    tmp_path: Path,
) -> None:
    plan = _plan(tmp_path)
    with pytest.raises(HarnessError, match="plan") as invalid_plan:
        execute_harness_run(object(), RecordingRuntime())  # type: ignore[arg-type]
    _assert_harness_error(
        invalid_plan,
        phase=HarnessPhase.PREPARING,
        reason=HarnessFailureReason.PRECONDITION_INVALID,
        match="plan",
    )
    with pytest.raises(HarnessError, match="runtime") as invalid_runtime:
        execute_harness_run(plan, object())  # type: ignore[arg-type]
    _assert_harness_error(
        invalid_runtime,
        phase=HarnessPhase.PREPARING,
        reason=HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
        match="runtime",
    )

    runtime = RecordingRuntime()
    execute_harness_run(plan, runtime)
    with pytest.raises(HarnessError, match="already exists") as collision:
        execute_harness_run(plan, runtime)
    _assert_harness_error(
        collision,
        phase=HarnessPhase.PREPARING,
        reason=HarnessFailureReason.OUTPUT_COLLISION,
        match=_RUN_ID,
    )
    assert len(runtime.reset_requests) == 1


def test_execution_wraps_output_reset_and_runtime_state_failures(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    plan = _plan(tmp_path)
    monkeypatch.setattr(
        harness_module,
        "prepare_storage_root",
        lambda _path: (_ for _ in ()).throw(OSError("denied")),
    )
    with pytest.raises(HarnessError) as unavailable:
        execute_harness_run(plan, RecordingRuntime())
    _assert_harness_error(
        unavailable,
        phase=HarnessPhase.PREPARING,
        reason=HarnessFailureReason.OUTPUT_UNAVAILABLE,
        match="output root",
    )
    monkeypatch.undo()

    with pytest.raises(HarnessError) as reset_failed:
        execute_harness_run(_plan(tmp_path / "reset"), RecordingRuntime(reset_error=ValueError()))
    _assert_harness_error(
        reset_failed,
        phase=HarnessPhase.RESETTING,
        reason=HarnessFailureReason.RESET_FAILED,
        match="reset failed",
    )

    invalid_reset_values: tuple[object, ...] = ([], {"bad": float("nan")})
    for value in invalid_reset_values:
        with pytest.raises(HarnessError) as invalid_reset:
            execute_harness_run(
                _plan(tmp_path / f"invalid-reset-{len(str(value))}"),
                RecordingRuntime(reset_value=value),
            )
        _assert_harness_error(
            invalid_reset,
            phase=HarnessPhase.RESETTING,
            reason=HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
            match="runtime",
        )

    with pytest.raises(HarnessError) as step_failed:
        execute_harness_run(
            _plan(tmp_path / "step-error"),
            RecordingRuntime(advance_error=RuntimeError()),
        )
    _assert_harness_error(
        step_failed,
        phase=HarnessPhase.EXECUTING,
        reason=HarnessFailureReason.STEP_FAILED,
        match="runtime failed",
    )

    invalid_step_values: tuple[object, ...] = ([], {"bad": float("inf")})
    for value in invalid_step_values:
        with pytest.raises(HarnessError) as invalid_step:
            execute_harness_run(
                _plan(tmp_path / f"invalid-step-{len(str(value))}"),
                RecordingRuntime(advance_value=value),
            )
        _assert_harness_error(
            invalid_step,
            phase=HarnessPhase.EXECUTING,
            reason=HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
            match="runtime",
        )


def test_execution_wraps_step_evaluation_finalization_and_storage_failures(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def boom(*_args: object, **_kwargs: object) -> Any:
        raise ValueError("injected")

    plan = _plan(tmp_path / "step")
    monkeypatch.setattr(harness_module, "advance_event_schedule", boom)
    with pytest.raises(HarnessError) as step_error:
        execute_harness_run(plan, RecordingRuntime())
    _assert_harness_error(
        step_error,
        phase=HarnessPhase.EXECUTING,
        reason=HarnessFailureReason.STEP_FAILED,
        match="harness step failed",
    )
    monkeypatch.undo()

    plan = _plan(tmp_path / "initial-evaluation")
    monkeypatch.setattr(harness_module, "append_snapshot_assertion_result", boom)
    with pytest.raises(HarnessError) as initial_evaluation:
        execute_harness_run(plan, RecordingRuntime())
    _assert_harness_error(
        initial_evaluation,
        phase=HarnessPhase.EVALUATING,
        reason=HarnessFailureReason.EVALUATION_FAILED,
        match="initial assertion",
    )
    monkeypatch.undo()

    plan = _plan(tmp_path / "step-evaluation")
    monkeypatch.setattr(harness_module, "append_transition_assertion_result", boom)
    with pytest.raises(HarnessError) as step_evaluation:
        execute_harness_run(plan, RecordingRuntime())
    _assert_harness_error(
        step_evaluation,
        phase=HarnessPhase.EVALUATING,
        reason=HarnessFailureReason.EVALUATION_FAILED,
        match="assertion evaluation failed",
    )
    monkeypatch.undo()

    plan = _plan(tmp_path / "finalization")
    monkeypatch.setattr(harness_module, "derive_scenario_verdict", boom)
    with pytest.raises(HarnessError) as finalization:
        execute_harness_run(plan, RecordingRuntime())
    _assert_harness_error(
        finalization,
        phase=HarnessPhase.FINALIZING,
        reason=HarnessFailureReason.FINALIZATION_FAILED,
        match="finalize",
    )
    monkeypatch.undo()

    plan = _plan(tmp_path / "storage")
    monkeypatch.setattr(harness_module, "write_run_package", boom)
    with pytest.raises(HarnessError) as storage:
        execute_harness_run(plan, RecordingRuntime())
    _assert_harness_error(
        storage,
        phase=HarnessPhase.STORING,
        reason=HarnessFailureReason.STORAGE_FAILED,
        match="publish",
    )


def test_direct_transition_assertion_without_target_fails_closed(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    assertions = create_assertion_series(_RUN_ID, _SCENARIO_ID)
    ledger = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)
    series = create_snapshot_series(_RUN_ID, _SCENARIO_ID)
    series = append_state_snapshot(
        series,
        snapshot_id="SNAPSHOT-DIRECT-001",
        captured_at_tick=0,
        phase=SnapshotPhase.INITIAL,
        domain=EvidenceDomain.AURORA_STATE,
        subject_id=AURORA_SUBJECT_ID,
        producer_id=AURORA_RUNTIME_PRODUCER_ID,
        state=create_snapshot_state({"ready": True}),
    )
    with pytest.raises(HarnessError, match="no transition target") as error:
        harness_module._evaluate_planned_assertions(
            assertions,
            ledger,
            (PlannedAssertion("RESULT-DIRECT-001", _transition_assertion()),),
            snapshot=series.snapshots[0],
            transition=None,
        )
    assert error.value.phase is HarnessPhase.EVALUATING
    assert plan.plan_sha256


def test_result_model_rejects_invalid_types_identities_and_channel_order(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    result = execute_harness_run(plan, RecordingRuntime())
    for field in (
        "snapshots",
        "transitions",
        "assertions",
        "evidence",
        "verdict",
        "event_state",
        "storage_manifest",
    ):
        with pytest.raises(HarnessError, match=field):
            _replace_result(result, **{field: object()})
    with pytest.raises(HarnessError, match="channel_states"):
        _replace_result(result, channel_states=[])
    with pytest.raises(HarnessError, match="routing_audits"):
        _replace_result(result, routing_audits=[])
    with pytest.raises(HarnessError, match="package_directory"):
        _replace_result(result, package_directory="not-a-path")
    with pytest.raises(HarnessError, match="do not share"):
        replace(result, run_id="AURORA-RUN-OTHER-001")
    with pytest.raises(HarnessError, match="lexical"):
        replace(result, channel_states=tuple(reversed(result.channel_states)))
    with pytest.raises(HarnessError, match="plan_sha256"):
        replace(result, plan_sha256="BAD")


def _blank_snapshots() -> SnapshotSeries:
    return create_snapshot_series(_RUN_ID, _SCENARIO_ID)


def _blank_transitions() -> TransitionSeries:
    return create_transition_series(_RUN_ID, _SCENARIO_ID)


def test_result_validation_detects_cross_product_and_storage_tampering(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    result = execute_harness_run(plan, RecordingRuntime())

    cases = (
        replace(result, plan_sha256="0" * 64),
        replace(
            result,
            event_state=replace(result.event_state, schedule_id="AURORA-EVENTS-OTHER-001"),
        ),
        replace(
            result,
            event_state=EventRuntimeState(
                schedule_id=result.event_state.schedule_id,
                next_sequence=1,
                advanced_through_tick=2,
                last_released_tick=1,
                released_event_ids=(_EVENT_ID,),
            ),
        ),
        replace(result, channel_states=()),
        replace(result, snapshots=_blank_snapshots()),
        replace(result, transitions=_blank_transitions()),
        replace(result, evidence=replace(result.evidence, finalized_at_tick=3)),
        replace(
            result,
            storage_manifest=replace(result.storage_manifest, package_id="PACKAGE-OTHER-001"),
        ),
        replace(
            result,
            storage_manifest=replace(result.storage_manifest, finalized_at_tick=3),
        ),
    )
    for tampered in cases:
        with pytest.raises(HarnessError) as error:
            validate_harness_run_result(plan, tampered)
        assert error.value.phase is HarnessPhase.VERIFYING
        assert error.value.reason is HarnessFailureReason.RESULT_INVALID

    artifact_path = result.package_directory / result.storage_manifest.artifacts[0].relative_path
    artifact_path.write_text("{}", encoding="utf-8")
    with pytest.raises(HarnessError, match="integrity verification") as storage_error:
        validate_harness_run_result(plan, result)
    assert storage_error.value.reason is HarnessFailureReason.RESULT_INVALID


def test_result_validation_rejects_snapshot_phase_and_count_tampering(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    result = execute_harness_run(plan, RecordingRuntime())
    initial = result.snapshots.snapshots[0]

    wrong_initial = SnapshotSeries(
        _RUN_ID,
        _SCENARIO_ID,
        (replace(initial, phase=SnapshotPhase.FINAL),),
    )
    with pytest.raises(HarnessError, match="begin with an INITIAL"):
        validate_harness_run_result(plan, replace(result, snapshots=wrong_initial))

    initial_only = SnapshotSeries(_RUN_ID, _SCENARIO_ID, (initial,))
    with pytest.raises(HarnessError, match="end with a FINAL"):
        validate_harness_run_result(plan, replace(result, snapshots=initial_only))

    extra_snapshot = append_state_snapshot(
        result.snapshots,
        snapshot_id="SNAPSHOT-EXTRA-001",
        captured_at_tick=2,
        phase=SnapshotPhase.FINAL,
        domain=EvidenceDomain.AURORA_STATE,
        subject_id=AURORA_SUBJECT_ID,
        producer_id=AURORA_RUNTIME_PRODUCER_ID,
        state=create_snapshot_state({"ready": True, "tick": 2}),
    )
    with pytest.raises(HarnessError, match="snapshot count"):
        validate_harness_run_result(plan, replace(result, snapshots=extra_snapshot))


def test_result_validation_wraps_verdict_recomputation_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    plan = _plan(tmp_path)
    result = execute_harness_run(plan, RecordingRuntime())

    def reject_verdict(*_args: object, **_kwargs: object) -> None:
        raise ValueError("tampered verdict")

    monkeypatch.setattr(harness_module, "validate_scenario_verdict", reject_verdict)
    with pytest.raises(HarnessError, match="deterministic recomputation") as error:
        validate_harness_run_result(plan, result)
    assert error.value.phase is HarnessPhase.VERIFYING
    assert error.value.reason is HarnessFailureReason.RESULT_INVALID


def test_result_validation_rejects_invalid_arguments(tmp_path: Path) -> None:
    plan = _plan(tmp_path)
    result = execute_harness_run(plan, RecordingRuntime())
    with pytest.raises(HarnessError, match="plan"):
        validate_harness_run_result(object(), result)  # type: ignore[arg-type]
    with pytest.raises(HarnessError, match="result") as error:
        validate_harness_run_result(plan, object())  # type: ignore[arg-type]
    assert error.value.phase is HarnessPhase.VERIFYING
    with pytest.raises(HarnessError, match="identity"):
        other_plan = replace(
            plan,
            run_id="AURORA-RUN-OTHER-001",
            verdict_definition=replace(
                plan.verdict_definition,
                primary_run_id="AURORA-RUN-OTHER-001",
            ),
        )
        validate_harness_run_result(other_plan, result)


def test_private_validators_and_id_generators_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert harness_module._snapshot_id(12) == "SNAPSHOT-000012"
    assert harness_module._transition_id(3) == "TRANSITION-000003"
    assert harness_module._record_id(9) == "RECORD-000009"

    with pytest.raises(HarnessError, match="scenario_id"):
        harness_module._validate_scenario_id("bad")
    with pytest.raises(HarnessError, match="digest"):
        harness_module._validate_sha256("BAD", field="digest")
    with pytest.raises(HarnessError, match="random_seed"):
        harness_module._validate_random_seed(1 << 64)
    with pytest.raises(HarnessError, match="tick"):
        harness_module._validate_tick(True, field="tick")
    with pytest.raises(HarnessError, match="canonical finite JSON"):
        harness_module._canonical_json_bytes(object())

    monkeypatch.setattr(harness_module, "_precondition", lambda _message: None)
    with pytest.raises(AssertionError, match="unreachable"):
        harness_module._canonical_json_bytes(object())
    monkeypatch.undo()

    monkeypatch.setattr(harness_module, "MAX_STEP_ASSERTIONS", 0)
    with pytest.raises(HarnessError, match="must not exceed"):
        HarnessStep(
            "STEP-FOUND-001",
            1,
            SnapshotPhase.FINAL,
            assertions=(PlannedAssertion("RESULT-001", _snapshot_assertion()),),
        )
