"""Fail-closed orchestration for deterministic Aurora validation runs.

The harness owns execution control, complete fixtures, objective events,
validator assertions, evidence, and storage.  An Aurora runtime receives only
an ``AURORA_RUNTIME`` fixture capability, governed observable events, admitted
channel packets, and its own preceding state.  The runtime never receives the
run plan, expected results, world truth, player-private data, future fixtures,
validator fixtures, or storage paths.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Final, Protocol, runtime_checkable

from aurora_validation_harness.assertions import (
    AssertionSeries,
    SnapshotAssertion,
    TransitionAssertion,
    append_snapshot_assertion_result,
    append_transition_assertion_result,
    create_assertion_evidence_payload,
    create_assertion_series,
    create_assertion_source,
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
    ChannelRoutingResult,
    ChannelRuntimeState,
    EvidenceSubmission,
    create_channel_state,
    route_submission,
    set_channel_gate,
)
from aurora_validation_harness.comparison import ComparisonReport
from aurora_validation_harness.configuration import (
    ResolvedConfiguration,
    RunMode,
    calculate_configuration_sha256,
)
from aurora_validation_harness.events import (
    AuroraEvent,
    EventReleaseBatch,
    EventRuntimeState,
    EventSchedule,
    advance_event_schedule,
    create_event_state,
    project_release_for_aurora,
)
from aurora_validation_harness.evidence import (
    EvidenceDomain,
    EvidenceKind,
    EvidenceLedger,
    EvidencePayload,
    EvidenceSource,
    EvidenceSourceKind,
    FinalizedEvidencePackage,
    append_evidence_record,
    create_evidence_ledger,
    create_evidence_payload,
    finalize_evidence_ledger,
)
from aurora_validation_harness.fixtures import FixtureBundle, FixturePartition
from aurora_validation_harness.partitions import (
    AccessPrincipal,
    FixtureView,
    PartitionedFixtureStore,
)
from aurora_validation_harness.snapshots import (
    SnapshotPhase,
    SnapshotSeries,
    SnapshotState,
    StateSnapshot,
    append_state_snapshot,
    create_snapshot_evidence_payload,
    create_snapshot_series,
    create_snapshot_source,
    create_snapshot_state,
)
from aurora_validation_harness.storage import (
    ArtifactDescriptor,
    ArtifactKind,
    RunPackageManifest,
    StoragePayload,
    create_artifact_descriptor,
    create_run_package_manifest,
    create_storage_payload,
    prepare_storage_root,
    verify_run_package,
    write_run_package,
)
from aurora_validation_harness.transitions import (
    StateTransition,
    TransitionSeries,
    append_state_transition,
    create_transition_evidence_payload,
    create_transition_series,
    create_transition_source,
)
from aurora_validation_harness.verdicts import (
    ExecutionValidity,
    ExecutionValidityReason,
    ScenarioVerdict,
    VerdictDefinition,
    VerdictObservation,
    create_verdict_evidence_payload,
    derive_scenario_verdict,
    validate_scenario_verdict,
)

SUPPORTED_HARNESS_SCHEMA_VERSION: Final[str] = "1.0"
MAX_HARNESS_STEPS: Final[int] = 10_000
MAX_STEP_GATE_CHANGES: Final[int] = 1_000
MAX_STEP_SUBMISSIONS: Final[int] = 10_000
MAX_STEP_ASSERTIONS: Final[int] = 10_000
MAX_TICK: Final[int] = (1 << 63) - 1

HARNESS_PRODUCER_ID: Final[str] = "AURORA-VALIDATION-HARNESS"
AURORA_RUNTIME_PRODUCER_ID: Final[str] = "AURORA-RUNTIME"
AURORA_SUBJECT_ID: Final[str] = "aurora"

_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")


class HarnessPhase(StrEnum):
    """Stable lifecycle phase attached to orchestration failures."""

    PREPARING = "PREPARING"
    RESETTING = "RESETTING"
    EXECUTING = "EXECUTING"
    EVALUATING = "EVALUATING"
    FINALIZING = "FINALIZING"
    STORING = "STORING"
    VERIFYING = "VERIFYING"
    COMPLETE = "COMPLETE"


class HarnessFailureReason(StrEnum):
    """Stable fail-closed reason for an orchestration error."""

    PRECONDITION_INVALID = "PRECONDITION_INVALID"
    OUTPUT_COLLISION = "OUTPUT_COLLISION"
    OUTPUT_UNAVAILABLE = "OUTPUT_UNAVAILABLE"
    RUNTIME_CONTRACT_INVALID = "RUNTIME_CONTRACT_INVALID"
    RESET_FAILED = "RESET_FAILED"
    STEP_FAILED = "STEP_FAILED"
    EVALUATION_FAILED = "EVALUATION_FAILED"
    FINALIZATION_FAILED = "FINALIZATION_FAILED"
    STORAGE_FAILED = "STORAGE_FAILED"
    RESULT_INVALID = "RESULT_INVALID"


class HarnessError(RuntimeError):
    """Raised when a harness run cannot safely continue or be trusted."""

    def __init__(
        self,
        phase: HarnessPhase,
        reason: HarnessFailureReason,
        message: str,
    ) -> None:
        if not isinstance(phase, HarnessPhase):
            raise TypeError("phase must be a HarnessPhase value")
        if not isinstance(reason, HarnessFailureReason):
            raise TypeError("reason must be a HarnessFailureReason value")
        if not isinstance(message, str) or not message.strip():
            raise TypeError("message must be a non-empty string")
        self.phase = phase
        self.reason = reason
        self.detail = message
        super().__init__(f"{phase.value}/{reason.value}: {message}")


@dataclass(frozen=True, slots=True)
class ChannelGateChange:
    """One explicit channel-gate mutation applied before step submissions."""

    channel_id: str
    gate: ChannelGateState

    def __post_init__(self) -> None:
        _validate_control_id(self.channel_id, field="channel_id")
        if not isinstance(self.gate, ChannelGateState):
            raise HarnessError(
                HarnessPhase.PREPARING,
                HarnessFailureReason.PRECONDITION_INVALID,
                "gate must be a ChannelGateState value",
            )

    def to_mapping(self) -> dict[str, object]:
        """Return the canonical validator-owned instruction."""

        return {"channel_id": self.channel_id, "gate": self.gate.value}


@dataclass(frozen=True, slots=True)
class PlannedAssertion:
    """One stable result identity paired with a validator-only predicate."""

    result_id: str
    definition: SnapshotAssertion | TransitionAssertion

    def __post_init__(self) -> None:
        _validate_control_id(self.result_id, field="result_id")
        if not isinstance(self.definition, (SnapshotAssertion, TransitionAssertion)):
            raise HarnessError(
                HarnessPhase.PREPARING,
                HarnessFailureReason.PRECONDITION_INVALID,
                "definition must be a SnapshotAssertion or TransitionAssertion",
            )

    @property
    def assertion_id(self) -> str:
        """Return the canonical assertion-definition identity."""

        return self.definition.assertion_id

    @property
    def assertion_sha256(self) -> str:
        """Return the exact assertion-definition digest."""

        return self.definition.assertion_sha256

    def to_mapping(self) -> dict[str, object]:
        """Return a validator-owned plan representation."""

        return {
            "assertion_id": self.assertion_id,
            "assertion_sha256": self.assertion_sha256,
            "assertion_type": (
                "SNAPSHOT_ASSERTION"
                if isinstance(self.definition, SnapshotAssertion)
                else "TRANSITION_ASSERTION"
            ),
            "result_id": self.result_id,
        }


@dataclass(frozen=True, slots=True)
class HarnessStep:
    """One deterministic logical-time advancement and evaluation checkpoint."""

    step_id: str
    through_tick: int
    snapshot_phase: SnapshotPhase
    checkpoint_id: str | None = None
    gate_changes: tuple[ChannelGateChange, ...] = ()
    submissions: tuple[EvidenceSubmission, ...] = ()
    assertions: tuple[PlannedAssertion, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.step_id, field="step_id")
        _validate_tick(self.through_tick, field="through_tick")
        if self.snapshot_phase not in {
            SnapshotPhase.POST_EVENT,
            SnapshotPhase.CHECKPOINT,
            SnapshotPhase.FINAL,
        }:
            raise HarnessError(
                HarnessPhase.PREPARING,
                HarnessFailureReason.PRECONDITION_INVALID,
                "step snapshot_phase must be POST_EVENT, CHECKPOINT, or FINAL",
            )
        if self.snapshot_phase is SnapshotPhase.CHECKPOINT:
            if self.checkpoint_id is None:
                raise HarnessError(
                    HarnessPhase.PREPARING,
                    HarnessFailureReason.PRECONDITION_INVALID,
                    "CHECKPOINT step requires checkpoint_id",
                )
            _validate_control_id(self.checkpoint_id, field="checkpoint_id")
        elif self.checkpoint_id is not None:
            raise HarnessError(
                HarnessPhase.PREPARING,
                HarnessFailureReason.PRECONDITION_INVALID,
                "checkpoint_id is permitted only for a CHECKPOINT step",
            )
        _validate_typed_tuple(
            self.gate_changes,
            ChannelGateChange,
            field="gate_changes",
            maximum=MAX_STEP_GATE_CHANGES,
        )
        _validate_typed_tuple(
            self.submissions,
            EvidenceSubmission,
            field="submissions",
            maximum=MAX_STEP_SUBMISSIONS,
        )
        _validate_typed_tuple(
            self.assertions,
            PlannedAssertion,
            field="assertions",
            maximum=MAX_STEP_ASSERTIONS,
        )
        gate_ids = tuple(change.channel_id for change in self.gate_changes)
        if len(gate_ids) != len(set(gate_ids)):
            raise HarnessError(
                HarnessPhase.PREPARING,
                HarnessFailureReason.PRECONDITION_INVALID,
                "a step must not change the same channel gate more than once",
            )
        for submission in self.submissions:
            if submission.submitted_at_tick > self.through_tick:
                raise HarnessError(
                    HarnessPhase.PREPARING,
                    HarnessFailureReason.PRECONDITION_INVALID,
                    "submission tick must not exceed its harness step tick",
                )

    def to_mapping(self) -> dict[str, object]:
        """Return deterministic plan metadata without assertion answers."""

        return {
            "assertions": [assertion.to_mapping() for assertion in self.assertions],
            "checkpoint_id": self.checkpoint_id,
            "gate_changes": [change.to_mapping() for change in self.gate_changes],
            "snapshot_phase": self.snapshot_phase.value,
            "step_id": self.step_id,
            "submission_ids": [submission.evidence_id for submission in self.submissions],
            "through_tick": self.through_tick,
        }


@dataclass(frozen=True, slots=True)
class AuroraResetRequest:
    """Least-privilege input supplied to a runtime during mandatory reset."""

    run_id: str
    random_seed: int
    initial_tick: int
    fixtures: FixtureView

    def __post_init__(self) -> None:
        _validate_control_id(self.run_id, field="run_id")
        _validate_random_seed(self.random_seed)
        _validate_tick(self.initial_tick, field="initial_tick")
        if not isinstance(self.fixtures, FixtureView):
            raise HarnessError(
                HarnessPhase.RESETTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "fixtures must be a FixtureView",
            )
        if self.fixtures.principal is not AccessPrincipal.AURORA_RUNTIME:
            raise HarnessError(
                HarnessPhase.RESETTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "runtime reset requires an AURORA_RUNTIME fixture view",
            )

    def to_evidence_mapping(self) -> dict[str, object]:
        """Return a content-redacted record of the exact reset capability."""

        return {
            "accessible_fixture_artifact_ids": list(self.fixtures.available_artifact_ids),
            "accessible_fixture_state_sha256": self.fixtures.accessible_state_sha256,
            "initial_tick": self.initial_tick,
            "random_seed": self.random_seed,
            "run_id": self.run_id,
        }


@dataclass(frozen=True, slots=True)
class AuroraStepRequest:
    """Only Aurora-safe inputs admitted during one deterministic step."""

    run_id: str
    previous_tick: int
    through_tick: int
    previous_state: SnapshotState
    events: tuple[AuroraEvent, ...]
    evidence_packets: tuple[AuroraEvidencePacket, ...]

    def __post_init__(self) -> None:
        _validate_control_id(self.run_id, field="run_id")
        _validate_tick(self.previous_tick, field="previous_tick")
        _validate_tick(self.through_tick, field="through_tick")
        if self.through_tick < self.previous_tick:
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "through_tick must not precede previous_tick",
            )
        if not isinstance(self.previous_state, SnapshotState):
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "previous_state must be a SnapshotState",
            )
        _validate_typed_tuple(
            self.events,
            AuroraEvent,
            field="events",
            maximum=MAX_STEP_SUBMISSIONS,
            phase=HarnessPhase.EXECUTING,
        )
        _validate_typed_tuple(
            self.evidence_packets,
            AuroraEvidencePacket,
            field="evidence_packets",
            maximum=MAX_STEP_SUBMISSIONS,
            phase=HarnessPhase.EXECUTING,
        )
        event_ids = tuple(event.event_id for event in self.events)
        packet_ids = tuple(packet.evidence_id for packet in self.evidence_packets)
        if len(event_ids) != len(set(event_ids)):
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "step events must use unique event IDs",
            )
        if len(packet_ids) != len(set(packet_ids)):
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "step evidence packets must use unique evidence IDs",
            )
        if any(event.occurred_at_tick > self.through_tick for event in self.events):
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "step contains an event beyond through_tick",
            )
        if any(packet.admitted_at_tick > self.through_tick for packet in self.evidence_packets):
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
                "step contains an evidence packet beyond through_tick",
            )

    def to_evidence_mapping(self) -> dict[str, object]:
        """Return the exact Aurora-facing inputs supplied for this step."""

        return {
            "events": [event.to_mapping() for event in self.events],
            "evidence_packets": [packet.to_mapping() for packet in self.evidence_packets],
            "previous_state_sha256": self.previous_state.state_sha256,
            "previous_tick": self.previous_tick,
            "run_id": self.run_id,
            "through_tick": self.through_tick,
        }


@runtime_checkable
class AuroraRuntime(Protocol):
    """Minimum executable boundary implemented by an Aurora runtime adapter."""

    def reset(self, request: AuroraResetRequest, /) -> Mapping[str, object]:
        """Reset all prior-run state and return the initial observable state."""

    def advance(self, request: AuroraStepRequest, /) -> Mapping[str, object]:
        """Apply one safe input batch and return the resulting observable state."""


@dataclass(frozen=True, slots=True)
class RoutingAudit:
    """Validator-owned immutable summary of one channel routing decision."""

    step_id: str
    submission_id: str
    channel_id: str
    result: ChannelRoutingResult

    def __post_init__(self) -> None:
        _validate_control_id(self.step_id, field="step_id")
        _validate_control_id(self.submission_id, field="submission_id")
        _validate_control_id(self.channel_id, field="channel_id")
        if not isinstance(self.result, ChannelRoutingResult):
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.STEP_FAILED,
                "routing audit result must be a ChannelRoutingResult",
            )
        if self.result.state.channel_id != self.channel_id:
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.STEP_FAILED,
                "routing audit channel does not match resulting channel state",
            )
        if self.result.packet is not None and self.result.packet.evidence_id != self.submission_id:
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.STEP_FAILED,
                "routing audit submission does not match admitted packet",
            )

    def to_mapping(self) -> dict[str, object]:
        """Return a payload-redacted channel decision record."""

        return {
            "channel_id": self.channel_id,
            "packet_sha256": (
                None if self.result.packet is None else self.result.packet.packet_sha256
            ),
            "reason": self.result.reason.value,
            "status": self.result.status.value,
            "step_id": self.step_id,
            "submission_id": self.submission_id,
        }


@dataclass(frozen=True, slots=True)
class HarnessRunPlan:
    """Complete validator-owned inputs for one deterministic primary run."""

    package_id: str
    run_id: str
    resolved_configuration: ResolvedConfiguration
    baseline_verification: BaselineVerificationResult
    fixture_bundle: FixtureBundle
    event_schedule: EventSchedule
    channel_definitions: tuple[ChannelDefinition, ...]
    initial_tick: int
    initial_assertions: tuple[PlannedAssertion, ...]
    steps: tuple[HarnessStep, ...]
    verdict_definition: VerdictDefinition
    comparisons: tuple[ComparisonReport, ...] = ()
    observations: tuple[VerdictObservation, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.package_id, field="package_id")
        _validate_control_id(self.run_id, field="run_id")
        _require_instance(
            self.resolved_configuration,
            ResolvedConfiguration,
            field="resolved_configuration",
        )
        _require_instance(
            self.baseline_verification,
            BaselineVerificationResult,
            field="baseline_verification",
        )
        _require_instance(self.fixture_bundle, FixtureBundle, field="fixture_bundle")
        _require_instance(self.event_schedule, EventSchedule, field="event_schedule")
        _require_instance(
            self.verdict_definition,
            VerdictDefinition,
            field="verdict_definition",
        )
        _validate_tick(self.initial_tick, field="initial_tick")
        _validate_typed_tuple(
            self.channel_definitions,
            ChannelDefinition,
            field="channel_definitions",
            maximum=MAX_STEP_GATE_CHANGES,
        )
        _validate_typed_tuple(
            self.initial_assertions,
            PlannedAssertion,
            field="initial_assertions",
            maximum=MAX_STEP_ASSERTIONS,
        )
        _validate_typed_tuple(
            self.steps,
            HarnessStep,
            field="steps",
            maximum=MAX_HARNESS_STEPS,
        )
        _validate_typed_tuple(
            self.comparisons,
            ComparisonReport,
            field="comparisons",
            maximum=MAX_STEP_ASSERTIONS,
        )
        _validate_typed_tuple(
            self.observations,
            VerdictObservation,
            field="observations",
            maximum=MAX_STEP_ASSERTIONS,
        )
        self._validate_identity_and_integrity()
        self._validate_execution_plan()

    @property
    def scenario_id(self) -> str:
        """Return the scenario identity bound by the configuration."""

        return self.resolved_configuration.configuration.scenario_id

    @property
    def final_tick(self) -> int:
        """Return the final logical tick of the complete plan."""

        return self.steps[-1].through_tick

    @property
    def plan_sha256(self) -> str:
        """Return a deterministic digest of execution controls and definitions."""

        return calculate_harness_plan_sha256(self)

    def _validate_identity_and_integrity(self) -> None:
        configuration = self.resolved_configuration.configuration
        configuration_sha256 = calculate_configuration_sha256(configuration)
        if configuration.configuration_sha256 != configuration_sha256:
            _precondition("configuration must declare its exact canonical hash")
        if self.baseline_verification.status is not VerificationStatus.VERIFIED:
            _precondition("baseline verification must be VERIFIED")
        if not self.baseline_verification.verified:
            _precondition("baseline verification is not executable")
        if self.baseline_verification.baseline_id != configuration.baseline_id:
            _precondition("baseline verification ID does not match configuration")
        if (
            configuration.execution.run_mode is RunMode.FORMAL
            and self.baseline_verification.baseline_state
            is not BaselineState.FORMAL_EXECUTION_ACTIVE
        ):
            _precondition("FORMAL mode requires a FORMAL_EXECUTION_ACTIVE baseline")
        manifest = self.fixture_bundle.manifest
        if manifest.fixture_set_id != configuration.fixture_set_id:
            _precondition("fixture bundle ID does not match configuration")
        if manifest.scenario_id != configuration.scenario_id:
            _precondition("fixture scenario does not match configuration")
        if manifest.fixture_manifest_sha256 != self.fixture_bundle.fixture_set_sha256:
            _precondition("fixture manifest must declare its exact canonical hash")
        if self.fixture_bundle.repository_root != self.resolved_configuration.repository_root:
            _precondition("fixture repository root does not match resolved configuration")
        if self.verdict_definition.scenario_id != configuration.scenario_id:
            _precondition("verdict definition scenario does not match configuration")
        if self.verdict_definition.primary_run_id != self.run_id:
            _precondition("verdict definition primary_run_id does not match plan")
        for report in self.comparisons:
            if report.scenario_id != configuration.scenario_id:
                _precondition("comparison scenario does not match configuration")
            if self.run_id not in {report.baseline_run_id, report.candidate_run_id}:
                _precondition("comparison must include the primary run")

    def _validate_execution_plan(self) -> None:
        if not self.steps:
            _precondition("steps must contain at least one final capture")
        channel_ids = tuple(definition.channel_id for definition in self.channel_definitions)
        if len(channel_ids) != len(set(channel_ids)):
            _precondition("channel definitions must use unique channel IDs")
        if channel_ids != tuple(sorted(channel_ids)):
            _precondition("channel definitions must use lexical channel-ID order")
        for planned in self.initial_assertions:
            if not isinstance(planned.definition, SnapshotAssertion):
                _precondition("initial assertions must target the initial snapshot")

        known_channels = frozenset(channel_ids)
        previous_tick = self.initial_tick
        step_ids: set[str] = set()
        result_ids: set[str] = set()
        for planned in self.initial_assertions:
            _add_unique_result_id(result_ids, planned.result_id)
        for index, step in enumerate(self.steps):
            if step.step_id in step_ids:
                _precondition("steps must use unique step IDs")
            step_ids.add(step.step_id)
            if step.through_tick < previous_tick:
                _precondition("steps must use nondecreasing through_tick values")
            if index < len(self.steps) - 1 and step.snapshot_phase is SnapshotPhase.FINAL:
                _precondition("only the final harness step may use FINAL snapshot phase")
            if index == len(self.steps) - 1 and step.snapshot_phase is not SnapshotPhase.FINAL:
                _precondition("the final harness step must use FINAL snapshot phase")
            referenced_channels = {
                *(change.channel_id for change in step.gate_changes),
                *(submission.channel_id for submission in step.submissions),
            }
            unknown_channels = sorted(referenced_channels - known_channels)
            if unknown_channels:
                _precondition("step references unknown channel IDs: " + ", ".join(unknown_channels))
            for planned in step.assertions:
                _add_unique_result_id(result_ids, planned.result_id)
            previous_tick = step.through_tick
        if self.event_schedule.events:
            final_event_tick = self.event_schedule.events[-1].scheduled_tick
            if self.final_tick < final_event_tick:
                _precondition("final harness step must advance through every scheduled event")

    def _content_mapping(self) -> dict[str, object]:
        configuration = self.resolved_configuration.configuration
        return {
            "baseline_manifest_sha256": (self.baseline_verification.calculated_manifest_sha256),
            "channel_definitions": [
                _channel_definition_mapping(definition) for definition in self.channel_definitions
            ],
            "comparisons": [report.report_sha256 for report in self.comparisons],
            "configuration_sha256": calculate_configuration_sha256(configuration),
            "event_schedule_sha256": self.event_schedule.schedule_sha256,
            "fixture_set_sha256": self.fixture_bundle.fixture_set_sha256,
            "harness_schema_version": SUPPORTED_HARNESS_SCHEMA_VERSION,
            "initial_assertions": [assertion.to_mapping() for assertion in self.initial_assertions],
            "initial_tick": self.initial_tick,
            "observations": [observation.observation_sha256 for observation in self.observations],
            "package_id": self.package_id,
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "steps": [step.to_mapping() for step in self.steps],
            "verdict_definition_sha256": self.verdict_definition.definition_sha256,
        }

    def to_mapping(self) -> dict[str, object]:
        """Return a content-redacted, integrity-sealed run-plan summary."""

        return {**self._content_mapping(), "plan_sha256": self.plan_sha256}


@dataclass(frozen=True, slots=True)
class HarnessRunResult:
    """Verified products and immutable storage location of a completed run."""

    run_id: str
    scenario_id: str
    plan_sha256: str
    snapshots: SnapshotSeries
    transitions: TransitionSeries
    assertions: AssertionSeries
    evidence: FinalizedEvidencePackage
    verdict: ScenarioVerdict
    event_state: EventRuntimeState
    channel_states: tuple[ChannelRuntimeState, ...]
    routing_audits: tuple[RoutingAudit, ...]
    storage_manifest: RunPackageManifest
    package_directory: Path

    def __post_init__(self) -> None:
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        _validate_sha256(self.plan_sha256, field="plan_sha256")
        typed_values = (
            ("snapshots", self.snapshots, SnapshotSeries),
            ("transitions", self.transitions, TransitionSeries),
            ("assertions", self.assertions, AssertionSeries),
            ("evidence", self.evidence, FinalizedEvidencePackage),
            ("verdict", self.verdict, ScenarioVerdict),
            ("event_state", self.event_state, EventRuntimeState),
            ("storage_manifest", self.storage_manifest, RunPackageManifest),
        )
        for field, value, expected_type in typed_values:
            if not isinstance(value, expected_type):
                raise HarnessError(
                    HarnessPhase.VERIFYING,
                    HarnessFailureReason.RESULT_INVALID,
                    f"{field} has an invalid runtime type",
                )
        _validate_typed_tuple(
            self.channel_states,
            ChannelRuntimeState,
            field="channel_states",
            maximum=MAX_STEP_GATE_CHANGES,
            phase=HarnessPhase.VERIFYING,
        )
        _validate_typed_tuple(
            self.routing_audits,
            RoutingAudit,
            field="routing_audits",
            maximum=MAX_HARNESS_STEPS * MAX_STEP_SUBMISSIONS,
            phase=HarnessPhase.VERIFYING,
        )
        if not isinstance(self.package_directory, Path):
            raise HarnessError(
                HarnessPhase.VERIFYING,
                HarnessFailureReason.RESULT_INVALID,
                "package_directory must be a pathlib.Path",
            )
        identities = (
            (self.snapshots.run_id, self.snapshots.scenario_id),
            (self.transitions.run_id, self.transitions.scenario_id),
            (self.assertions.run_id, self.assertions.scenario_id),
            (self.evidence.run_id, self.evidence.scenario_id),
            (self.verdict.primary_run_id, self.verdict.scenario_id),
            (self.storage_manifest.run_id, self.storage_manifest.scenario_id),
        )
        if any(identity != (self.run_id, self.scenario_id) for identity in identities):
            raise HarnessError(
                HarnessPhase.VERIFYING,
                HarnessFailureReason.RESULT_INVALID,
                "completed run products do not share one run and scenario identity",
            )
        channel_ids = tuple(state.channel_id for state in self.channel_states)
        if channel_ids != tuple(sorted(channel_ids)) or len(channel_ids) != len(set(channel_ids)):
            raise HarnessError(
                HarnessPhase.VERIFYING,
                HarnessFailureReason.RESULT_INVALID,
                "channel_states must use unique lexical channel-ID order",
            )

    def to_summary_mapping(self) -> dict[str, object]:
        """Return a compact post-run summary without captured state values."""

        return {
            "assertion_count": self.assertions.result_count,
            "evidence_package_sha256": self.evidence.package_sha256,
            "event_count": len(self.event_state.released_event_ids),
            "manifest_sha256": self.storage_manifest.manifest_sha256,
            "package_directory": self.package_directory.name,
            "plan_sha256": self.plan_sha256,
            "routing_attempt_count": len(self.routing_audits),
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "snapshot_count": self.snapshots.snapshot_count,
            "transition_count": self.transitions.transition_count,
            "verdict_outcome": self.verdict.outcome.value,
            "verdict_sha256": self.verdict.verdict_sha256,
        }


def execute_harness_run(plan: HarnessRunPlan, runtime: AuroraRuntime) -> HarnessRunResult:
    """Execute, evaluate, seal, store, and verify one deterministic run."""

    _require_instance(plan, HarnessRunPlan, field="plan")
    if not isinstance(runtime, AuroraRuntime):
        raise HarnessError(
            HarnessPhase.PREPARING,
            HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
            "runtime must implement reset and advance",
        )

    try:
        output_root = prepare_storage_root(plan.resolved_configuration.output_root)
    except Exception as exc:
        raise HarnessError(
            HarnessPhase.PREPARING,
            HarnessFailureReason.OUTPUT_UNAVAILABLE,
            "could not prepare the configured run output root",
        ) from exc
    final_directory = output_root / plan.run_id
    if final_directory.exists() or final_directory.is_symlink():
        raise HarnessError(
            HarnessPhase.PREPARING,
            HarnessFailureReason.OUTPUT_COLLISION,
            f"run package already exists: {plan.run_id}",
        )

    store = PartitionedFixtureStore(plan.fixture_bundle)
    aurora_view = store.view_for(AccessPrincipal.AURORA_RUNTIME)
    reset_request = AuroraResetRequest(
        run_id=plan.run_id,
        random_seed=plan.resolved_configuration.configuration.execution.random_seed,
        initial_tick=plan.initial_tick,
        fixtures=aurora_view,
    )
    try:
        initial_mapping = runtime.reset(reset_request)
    except Exception as exc:
        raise HarnessError(
            HarnessPhase.RESETTING,
            HarnessFailureReason.RESET_FAILED,
            "Aurora runtime reset failed",
        ) from exc
    initial_state = _capture_runtime_state(initial_mapping, phase=HarnessPhase.RESETTING)

    snapshots = create_snapshot_series(plan.run_id, plan.scenario_id)
    transitions = create_transition_series(plan.run_id, plan.scenario_id)
    assertions = create_assertion_series(plan.run_id, plan.scenario_id)
    ledger = create_evidence_ledger(plan.run_id, plan.scenario_id)
    event_state = create_event_state(plan.event_schedule)
    channel_states = {
        definition.channel_id: create_channel_state(definition)
        for definition in plan.channel_definitions
    }
    channel_definitions = {
        definition.channel_id: definition for definition in plan.channel_definitions
    }
    routing_audits: list[RoutingAudit] = []

    ledger = _record_run_preconditions(ledger, plan, store)
    ledger = _append_record(
        ledger,
        observed_at_tick=plan.initial_tick,
        recorded_at_tick=plan.initial_tick,
        kind=EvidenceKind.AURORA_INPUT,
        domain=EvidenceDomain.AURORA_ACCESSIBLE,
        payload=create_evidence_payload(reset_request.to_evidence_mapping()),
        sources=(
            EvidenceSource(
                source_kind=EvidenceSourceKind.FIXTURE,
                source_id=plan.fixture_bundle.manifest.fixture_set_id,
                source_sha256=aurora_view.accessible_state_sha256,
            ),
        ),
    )
    snapshots = append_state_snapshot(
        snapshots,
        snapshot_id=_snapshot_id(0),
        captured_at_tick=plan.initial_tick,
        phase=SnapshotPhase.INITIAL,
        domain=EvidenceDomain.AURORA_STATE,
        subject_id=AURORA_SUBJECT_ID,
        producer_id=AURORA_RUNTIME_PRODUCER_ID,
        state=initial_state,
    )
    initial_snapshot = snapshots.snapshots[-1]
    ledger = _record_snapshot(ledger, initial_snapshot)
    try:
        assertions, ledger = _evaluate_planned_assertions(
            assertions,
            ledger,
            plan.initial_assertions,
            snapshot=initial_snapshot,
            transition=None,
        )
    except Exception as exc:
        raise HarnessError(
            HarnessPhase.EVALUATING,
            HarnessFailureReason.EVALUATION_FAILED,
            "initial assertion evaluation failed",
        ) from exc

    previous_snapshot = initial_snapshot
    previous_tick = plan.initial_tick
    for step_index, step in enumerate(plan.steps, start=1):
        try:
            for change in step.gate_changes:
                definition = channel_definitions[change.channel_id]
                channel_states[change.channel_id] = set_channel_gate(
                    definition,
                    channel_states[change.channel_id],
                    change.gate,
                )

            release = advance_event_schedule(
                plan.event_schedule,
                event_state,
                step.through_tick,
            )
            event_state = release.state
            visible_events = project_release_for_aurora(release)
            ledger = _record_event_release(ledger, step, release)

            admitted_packets: list[AuroraEvidencePacket] = []
            for submission in step.submissions:
                definition = channel_definitions[submission.channel_id]
                routing_result = route_submission(
                    definition,
                    channel_states[submission.channel_id],
                    submission,
                )
                channel_states[submission.channel_id] = routing_result.state
                audit = RoutingAudit(
                    step_id=step.step_id,
                    submission_id=submission.evidence_id,
                    channel_id=submission.channel_id,
                    result=routing_result,
                )
                routing_audits.append(audit)
                ledger = _record_routing_decision(ledger, step, submission, audit)
                if routing_result.packet is not None:
                    admitted_packets.append(routing_result.packet)

            request = AuroraStepRequest(
                run_id=plan.run_id,
                previous_tick=previous_tick,
                through_tick=step.through_tick,
                previous_state=previous_snapshot.state,
                events=visible_events,
                evidence_packets=tuple(admitted_packets),
            )
            ledger = _append_record(
                ledger,
                observed_at_tick=step.through_tick,
                recorded_at_tick=step.through_tick,
                kind=EvidenceKind.AURORA_INPUT,
                domain=EvidenceDomain.AURORA_ACCESSIBLE,
                payload=create_evidence_payload(request.to_evidence_mapping()),
                sources=_runtime_input_sources(visible_events, tuple(admitted_packets)),
            )
            try:
                state_mapping = runtime.advance(request)
            except Exception as exc:
                raise HarnessError(
                    HarnessPhase.EXECUTING,
                    HarnessFailureReason.STEP_FAILED,
                    f"Aurora runtime failed during step: {step.step_id}",
                ) from exc
            state = _capture_runtime_state(state_mapping, phase=HarnessPhase.EXECUTING)
            snapshots = append_state_snapshot(
                snapshots,
                snapshot_id=_snapshot_id(step_index),
                captured_at_tick=step.through_tick,
                phase=step.snapshot_phase,
                domain=EvidenceDomain.AURORA_STATE,
                subject_id=AURORA_SUBJECT_ID,
                producer_id=AURORA_RUNTIME_PRODUCER_ID,
                state=state,
                checkpoint_id=step.checkpoint_id,
            )
            current_snapshot = snapshots.snapshots[-1]
            ledger = _record_snapshot(ledger, current_snapshot)
            transitions = append_state_transition(
                transitions,
                transition_id=_transition_id(step_index - 1),
                before=previous_snapshot,
                after=current_snapshot,
                causes=_runtime_input_sources(visible_events, tuple(admitted_packets)),
            )
            transition = transitions.transitions[-1]
            ledger = _record_transition(ledger, transition)
        except HarnessError:
            raise
        except Exception as exc:
            raise HarnessError(
                HarnessPhase.EXECUTING,
                HarnessFailureReason.STEP_FAILED,
                f"harness step failed: {step.step_id}",
            ) from exc

        try:
            assertions, ledger = _evaluate_planned_assertions(
                assertions,
                ledger,
                step.assertions,
                snapshot=current_snapshot,
                transition=transition,
            )
        except Exception as exc:
            raise HarnessError(
                HarnessPhase.EVALUATING,
                HarnessFailureReason.EVALUATION_FAILED,
                f"assertion evaluation failed: {step.step_id}",
            ) from exc
        previous_snapshot = current_snapshot
        previous_tick = step.through_tick

    try:
        verdict = derive_scenario_verdict(
            plan.verdict_definition,
            assertions,
            plan.comparisons,
            verdict_id="VERDICT-000001",
            evaluated_at_tick=plan.final_tick,
            execution_validity=ExecutionValidity.VALID_RUN,
            execution_validity_reason=ExecutionValidityReason.VERIFIED,
            observations=plan.observations,
        )
        ledger = _record_verdict(ledger, verdict, assertions, plan.comparisons)
        evidence = finalize_evidence_ledger(ledger, finalized_at_tick=plan.final_tick)
        ordered_channel_states = tuple(
            channel_states[channel_id] for channel_id in sorted(channel_states)
        )
        audits = tuple(routing_audits)
        descriptors, payloads = _build_storage_artifacts(
            plan,
            snapshots=snapshots,
            transitions=transitions,
            assertions=assertions,
            evidence=evidence,
            verdict=verdict,
            event_state=event_state,
            channel_states=ordered_channel_states,
            routing_audits=audits,
        )
        storage_manifest = create_run_package_manifest(
            package_id=plan.package_id,
            run_id=plan.run_id,
            scenario_id=plan.scenario_id,
            finalized_at_tick=plan.final_tick,
            artifacts=descriptors,
        )
    except Exception as exc:
        raise HarnessError(
            HarnessPhase.FINALIZING,
            HarnessFailureReason.FINALIZATION_FAILED,
            "could not finalize the validation products",
        ) from exc

    try:
        package_directory = write_run_package(output_root, storage_manifest, payloads)
        verify_run_package(package_directory, expected_manifest=storage_manifest)
    except Exception as exc:
        raise HarnessError(
            HarnessPhase.STORING,
            HarnessFailureReason.STORAGE_FAILED,
            "could not publish and verify the immutable run package",
        ) from exc

    run_result = HarnessRunResult(
        run_id=plan.run_id,
        scenario_id=plan.scenario_id,
        plan_sha256=plan.plan_sha256,
        snapshots=snapshots,
        transitions=transitions,
        assertions=assertions,
        evidence=evidence,
        verdict=verdict,
        event_state=event_state,
        channel_states=ordered_channel_states,
        routing_audits=audits,
        storage_manifest=storage_manifest,
        package_directory=package_directory,
    )
    validate_harness_run_result(plan, run_result)
    return run_result


def calculate_harness_plan_sha256(plan: HarnessRunPlan) -> str:
    """Calculate the canonical digest for one validator-owned run plan."""

    _require_instance(plan, HarnessRunPlan, field="plan")
    return hashlib.sha256(_canonical_json_bytes(plan._content_mapping())).hexdigest()


def validate_harness_run_result(plan: HarnessRunPlan, result: HarnessRunResult) -> None:
    """Recompute cross-product links and verify a completed run package."""

    _require_instance(plan, HarnessRunPlan, field="plan")
    _require_instance(
        result,
        HarnessRunResult,
        field="result",
        phase=HarnessPhase.VERIFYING,
    )
    if result.run_id != plan.run_id or result.scenario_id != plan.scenario_id:
        _invalid_result("result identity does not match run plan")
    if result.plan_sha256 != plan.plan_sha256:
        _invalid_result("result plan digest does not match run plan")
    if result.event_state.schedule_id != plan.event_schedule.schedule_id:
        _invalid_result("event runtime state does not match plan schedule")
    if result.event_state.next_sequence != len(plan.event_schedule.events):
        _invalid_result("completed event state does not include the full schedule")
    expected_channel_ids = tuple(definition.channel_id for definition in plan.channel_definitions)
    if tuple(state.channel_id for state in result.channel_states) != expected_channel_ids:
        _invalid_result("completed channel states do not match plan definitions")
    if not result.snapshots.snapshots:
        _invalid_result("completed run has no state snapshots")
    if result.snapshots.snapshots[0].phase is not SnapshotPhase.INITIAL:
        _invalid_result("completed run does not begin with an INITIAL snapshot")
    if result.snapshots.snapshots[-1].phase is not SnapshotPhase.FINAL:
        _invalid_result("completed run does not end with a FINAL snapshot")
    if result.snapshots.snapshot_count != len(plan.steps) + 1:
        _invalid_result("snapshot count does not match run plan")
    if result.transitions.transition_count != len(plan.steps):
        _invalid_result("transition count does not match run plan")
    try:
        validate_scenario_verdict(
            result.verdict,
            plan.verdict_definition,
            result.assertions,
            plan.comparisons,
        )
    except Exception as exc:
        raise HarnessError(
            HarnessPhase.VERIFYING,
            HarnessFailureReason.RESULT_INVALID,
            "scenario verdict failed deterministic recomputation",
        ) from exc
    if result.evidence.finalized_at_tick != plan.final_tick:
        _invalid_result("evidence finalization tick does not match run plan")
    if result.storage_manifest.package_id != plan.package_id:
        _invalid_result("storage package ID does not match run plan")
    if result.storage_manifest.finalized_at_tick != plan.final_tick:
        _invalid_result("storage finalization tick does not match run plan")
    try:
        verify_run_package(
            result.package_directory,
            expected_manifest=result.storage_manifest,
        )
    except Exception as exc:
        raise HarnessError(
            HarnessPhase.VERIFYING,
            HarnessFailureReason.RESULT_INVALID,
            "stored run package failed integrity verification",
        ) from exc


def _record_run_preconditions(
    ledger: EvidenceLedger,
    plan: HarnessRunPlan,
    store: PartitionedFixtureStore,
) -> EvidenceLedger:
    configuration = plan.resolved_configuration.configuration
    configuration_sha256 = calculate_configuration_sha256(configuration)
    ledger = _append_record(
        ledger,
        observed_at_tick=plan.initial_tick,
        recorded_at_tick=plan.initial_tick,
        kind=EvidenceKind.RUN_CONFIGURATION,
        domain=EvidenceDomain.RUN_CONTROL,
        payload=create_evidence_payload(
            {
                "configuration": configuration.to_mapping(),
                "configuration_sha256": configuration_sha256,
                "plan": plan.to_mapping(),
            }
        ),
        sources=(
            EvidenceSource(
                source_kind=EvidenceSourceKind.CONFIGURATION,
                source_id=configuration.configuration_id,
                source_sha256=configuration_sha256,
            ),
        ),
    )
    ledger = _append_record(
        ledger,
        observed_at_tick=plan.initial_tick,
        recorded_at_tick=plan.initial_tick,
        kind=EvidenceKind.BASELINE_VERIFICATION,
        domain=EvidenceDomain.RUN_CONTROL,
        payload=create_evidence_payload(_baseline_verification_mapping(plan.baseline_verification)),
        sources=(
            EvidenceSource(
                source_kind=EvidenceSourceKind.BASELINE,
                source_id=plan.baseline_verification.baseline_id,
                source_sha256=plan.baseline_verification.calculated_manifest_sha256,
            ),
        ),
    )
    ledger = _append_record(
        ledger,
        observed_at_tick=plan.initial_tick,
        recorded_at_tick=plan.initial_tick,
        kind=EvidenceKind.FIXTURE_INTEGRITY,
        domain=EvidenceDomain.VALIDATOR,
        payload=create_evidence_payload(_fixture_integrity_mapping(plan, store)),
        sources=(
            EvidenceSource(
                source_kind=EvidenceSourceKind.FIXTURE,
                source_id=plan.fixture_bundle.manifest.fixture_set_id,
                source_sha256=plan.fixture_bundle.fixture_set_sha256,
            ),
        ),
    )
    return ledger


def _record_event_release(
    ledger: EvidenceLedger,
    step: HarnessStep,
    release: EventReleaseBatch,
) -> EvidenceLedger:
    return _append_record(
        ledger,
        observed_at_tick=step.through_tick,
        recorded_at_tick=step.through_tick,
        kind=EvidenceKind.EVENT_RELEASE,
        domain=EvidenceDomain.WORLD,
        payload=create_evidence_payload(
            {
                "advanced_from_tick": release.advanced_from_tick,
                "advanced_through_tick": release.advanced_through_tick,
                "released_events": [
                    event.to_validator_mapping() for event in release.released_events
                ],
                "released_event_ids": [event.event_id for event in release.released_events],
                "step_id": step.step_id,
            }
        ),
        sources=tuple(
            EvidenceSource(
                source_kind=EvidenceSourceKind.EVENT,
                source_id=event.event_id,
                source_sha256=hashlib.sha256(
                    _canonical_json_bytes(event.to_validator_mapping())
                ).hexdigest(),
            )
            for event in release.released_events
        ),
    )


def _record_routing_decision(
    ledger: EvidenceLedger,
    step: HarnessStep,
    submission: EvidenceSubmission,
    audit: RoutingAudit,
) -> EvidenceLedger:
    payload: dict[str, object] = {
        **audit.to_mapping(),
        "observed_at_tick": submission.observed_at_tick,
        "submitted_at_tick": submission.submitted_at_tick,
    }
    if audit.result.packet is not None:
        payload["admitted_packet"] = audit.result.packet.to_mapping()
    return _append_record(
        ledger,
        observed_at_tick=submission.submitted_at_tick,
        recorded_at_tick=step.through_tick,
        kind=EvidenceKind.CHANNEL_ADMISSION,
        domain=(
            EvidenceDomain.AURORA_ACCESSIBLE
            if audit.result.packet is not None
            else EvidenceDomain.VALIDATOR
        ),
        payload=create_evidence_payload(payload),
        sources=(),
    )


def _record_snapshot(ledger: EvidenceLedger, snapshot: StateSnapshot) -> EvidenceLedger:
    return _append_record(
        ledger,
        observed_at_tick=snapshot.captured_at_tick,
        recorded_at_tick=snapshot.captured_at_tick,
        kind=EvidenceKind.STATE_SNAPSHOT,
        domain=snapshot.domain,
        payload=create_snapshot_evidence_payload(snapshot),
        sources=(create_snapshot_source(snapshot),),
    )


def _record_transition(ledger: EvidenceLedger, transition: StateTransition) -> EvidenceLedger:
    return _append_record(
        ledger,
        observed_at_tick=transition.after_tick,
        recorded_at_tick=transition.after_tick,
        kind=EvidenceKind.STATE_TRANSITION,
        domain=transition.domain,
        payload=create_transition_evidence_payload(transition),
        sources=(create_transition_source(transition),),
    )


def _evaluate_planned_assertions(
    assertions: AssertionSeries,
    ledger: EvidenceLedger,
    planned_assertions: tuple[PlannedAssertion, ...],
    *,
    snapshot: StateSnapshot,
    transition: StateTransition | None,
) -> tuple[AssertionSeries, EvidenceLedger]:
    for planned in planned_assertions:
        if isinstance(planned.definition, SnapshotAssertion):
            assertions = append_snapshot_assertion_result(
                assertions,
                planned.definition,
                snapshot,
                result_id=planned.result_id,
            )
        else:
            if transition is None:
                raise HarnessError(
                    HarnessPhase.EVALUATING,
                    HarnessFailureReason.EVALUATION_FAILED,
                    "transition assertion has no transition target",
                )
            assertions = append_transition_assertion_result(
                assertions,
                planned.definition,
                transition,
                result_id=planned.result_id,
            )
        result = assertions.results[-1]
        ledger = _append_record(
            ledger,
            observed_at_tick=result.evaluated_at_tick,
            recorded_at_tick=result.evaluated_at_tick,
            kind=EvidenceKind.ASSERTION_RESULT,
            domain=EvidenceDomain.VALIDATOR,
            payload=create_assertion_evidence_payload(result),
            sources=(create_assertion_source(result),),
        )
    return assertions, ledger


def _record_verdict(
    ledger: EvidenceLedger,
    verdict: ScenarioVerdict,
    assertions: AssertionSeries,
    comparisons: tuple[ComparisonReport, ...],
) -> EvidenceLedger:
    sources = (
        *(create_assertion_source(result) for result in assertions.results),
        *(
            EvidenceSource(
                source_kind=EvidenceSourceKind.EXTERNAL,
                source_id=report.report_id,
                source_sha256=report.report_sha256,
            )
            for report in comparisons
        ),
    )
    return _append_record(
        ledger,
        observed_at_tick=verdict.evaluated_at_tick,
        recorded_at_tick=verdict.evaluated_at_tick,
        kind=EvidenceKind.VERDICT,
        domain=EvidenceDomain.VALIDATOR,
        payload=create_verdict_evidence_payload(verdict),
        sources=sources,
    )


def _append_record(
    ledger: EvidenceLedger,
    *,
    observed_at_tick: int,
    recorded_at_tick: int,
    kind: EvidenceKind,
    domain: EvidenceDomain,
    payload: EvidencePayload,
    sources: tuple[EvidenceSource, ...],
) -> EvidenceLedger:
    return append_evidence_record(
        ledger,
        record_id=_record_id(len(ledger.records)),
        observed_at_tick=observed_at_tick,
        recorded_at_tick=recorded_at_tick,
        kind=kind,
        domain=domain,
        producer_id=HARNESS_PRODUCER_ID,
        payload=payload,
        sources=sources,
    )


def _runtime_input_sources(
    events: tuple[AuroraEvent, ...],
    packets: tuple[AuroraEvidencePacket, ...],
) -> tuple[EvidenceSource, ...]:
    return (
        *(
            EvidenceSource(
                source_kind=EvidenceSourceKind.EVENT,
                source_id=event.event_id,
                source_sha256=event.event_sha256,
            )
            for event in events
        ),
        *(
            EvidenceSource(
                source_kind=EvidenceSourceKind.CHANNEL_PACKET,
                source_id=packet.evidence_id,
                source_sha256=packet.packet_sha256,
            )
            for packet in packets
        ),
    )


def _capture_runtime_state(
    value: object,
    *,
    phase: HarnessPhase,
) -> SnapshotState:
    if not isinstance(value, Mapping):
        raise HarnessError(
            phase,
            HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
            "runtime state must be a JSON-object mapping",
        )
    try:
        return create_snapshot_state(value)
    except Exception as exc:
        raise HarnessError(
            phase,
            HarnessFailureReason.RUNTIME_CONTRACT_INVALID,
            "runtime returned an invalid or noncanonical state value",
        ) from exc


def _build_storage_artifacts(
    plan: HarnessRunPlan,
    *,
    snapshots: SnapshotSeries,
    transitions: TransitionSeries,
    assertions: AssertionSeries,
    evidence: FinalizedEvidencePackage,
    verdict: ScenarioVerdict,
    event_state: EventRuntimeState,
    channel_states: tuple[ChannelRuntimeState, ...],
    routing_audits: tuple[RoutingAudit, ...],
) -> tuple[tuple[ArtifactDescriptor, ...], dict[str, StoragePayload]]:
    artifacts: list[ArtifactDescriptor] = []
    payloads: dict[str, StoragePayload] = {}

    def add(
        artifact_id: str,
        kind: ArtifactKind,
        relative_path: str,
        mapping: Mapping[str, object],
    ) -> None:
        payload = create_storage_payload(mapping)
        descriptor = create_artifact_descriptor(
            artifact_id=artifact_id,
            kind=kind,
            relative_path=relative_path,
            payload=payload,
        )
        artifacts.append(descriptor)
        payloads[artifact_id] = payload

    add(
        "ARTIFACT-BASELINE-001",
        ArtifactKind.BASELINE_VERIFICATION,
        "control/baseline_verification.json",
        _baseline_verification_mapping(plan.baseline_verification),
    )
    add(
        "ARTIFACT-CONFIGURATION-001",
        ArtifactKind.RUN_CONFIGURATION,
        "control/run_configuration.json",
        {
            "configuration": plan.resolved_configuration.configuration.to_mapping(),
            "plan": plan.to_mapping(),
        },
    )
    add(
        "ARTIFACT-FIXTURES-001",
        ArtifactKind.FIXTURE_MANIFEST,
        "control/fixture_manifest.json",
        plan.fixture_bundle.manifest.to_mapping(),
    )
    add(
        "ARTIFACT-CHANNELS-001",
        ArtifactKind.CHANNEL_SERIES,
        "runtime/channels.json",
        {
            "definitions": [
                _channel_definition_mapping(definition) for definition in plan.channel_definitions
            ],
            "final_states": [_channel_state_mapping(state) for state in channel_states],
            "routing_audits": [audit.to_mapping() for audit in routing_audits],
        },
    )
    add(
        "ARTIFACT-EVENTS-001",
        ArtifactKind.EVENT_SERIES,
        "runtime/events.json",
        {
            "final_state": _event_state_mapping(event_state),
            "schedule": plan.event_schedule.to_validator_mapping(),
            "schedule_sha256": plan.event_schedule.schedule_sha256,
        },
    )
    add(
        "ARTIFACT-EVIDENCE-001",
        ArtifactKind.EVIDENCE_PACKAGE,
        "evidence/evidence_package.json",
        evidence.to_validator_mapping(),
    )
    add(
        "ARTIFACT-SNAPSHOTS-001",
        ArtifactKind.SNAPSHOT_SERIES,
        "state/snapshots.json",
        snapshots.to_validator_mapping(),
    )
    add(
        "ARTIFACT-TRANSITIONS-001",
        ArtifactKind.TRANSITION_SERIES,
        "state/transitions.json",
        transitions.to_validator_mapping(),
    )
    add(
        "ARTIFACT-ASSERTIONS-001",
        ArtifactKind.ASSERTION_SERIES,
        "evaluation/assertions.json",
        assertions.to_validator_mapping(),
    )
    if plan.comparisons:
        add(
            "ARTIFACT-COMPARISONS-001",
            ArtifactKind.COMPARISON_REPORT,
            "evaluation/comparisons.json",
            {"reports": [report.to_validator_mapping() for report in plan.comparisons]},
        )
    add(
        "ARTIFACT-VERDICT-001",
        ArtifactKind.SCENARIO_VERDICT,
        "evaluation/verdict.json",
        verdict.to_validator_mapping(),
    )
    return tuple(artifacts), payloads


def _baseline_verification_mapping(
    verification: BaselineVerificationResult,
) -> dict[str, object]:
    return {
        "baseline_id": verification.baseline_id,
        "baseline_state": verification.baseline_state.value,
        "calculated_manifest_sha256": verification.calculated_manifest_sha256,
        "declared_manifest_sha256": verification.declared_manifest_sha256,
        "files": [
            {
                "actual_normalized_text_sha256": item.actual_normalized_text_sha256,
                "actual_raw_sha256": item.actual_raw_sha256,
                "actual_version": item.actual_version,
                "expected_normalized_text_sha256": item.expected_normalized_text_sha256,
                "expected_raw_sha256": item.expected_raw_sha256,
                "expected_version": item.expected_version,
                "issues": [
                    {
                        "code": issue.code,
                        "effect": issue.effect.value,
                        "message": issue.message,
                        "path": issue.path,
                    }
                    for issue in item.issues
                ],
                "path": item.path,
                "status": item.status.value,
            }
            for item in verification.files
        ],
        "issues": [
            {
                "code": issue.code,
                "effect": issue.effect.value,
                "message": issue.message,
                "path": issue.path,
            }
            for issue in verification.issues
        ],
        "status": verification.status.value,
        "verified": verification.verified,
    }


def _fixture_integrity_mapping(
    plan: HarnessRunPlan,
    store: PartitionedFixtureStore,
) -> dict[str, object]:
    return {
        "fixture_manifest_sha256": plan.fixture_bundle.fixture_set_sha256,
        "fixture_set_id": plan.fixture_bundle.manifest.fixture_set_id,
        "partition_sha256": {
            partition.value: store.partition_sha256(partition) for partition in FixturePartition
        },
        "scenario_id": plan.scenario_id,
    }


def _channel_definition_mapping(definition: ChannelDefinition) -> dict[str, object]:
    return {
        "channel_id": definition.channel_id,
        "kind": definition.kind.value,
        "max_claim_bytes": definition.max_claim_bytes,
        "source_id": definition.source_id,
    }


def _channel_state_mapping(state: ChannelRuntimeState) -> dict[str, object]:
    return {
        "admitted_evidence_ids": list(state.admitted_evidence_ids),
        "channel_id": state.channel_id,
        "gate": state.gate.value,
        "last_admitted_tick": state.last_admitted_tick,
        "next_sequence": state.next_sequence,
    }


def _event_state_mapping(state: EventRuntimeState) -> dict[str, object]:
    return {
        "advanced_through_tick": state.advanced_through_tick,
        "last_released_tick": state.last_released_tick,
        "next_sequence": state.next_sequence,
        "released_event_ids": list(state.released_event_ids),
        "schedule_id": state.schedule_id,
    }


def _snapshot_id(index: int) -> str:
    return f"SNAPSHOT-{index:06d}"


def _transition_id(index: int) -> str:
    return f"TRANSITION-{index:06d}"


def _record_id(index: int) -> str:
    return f"RECORD-{index:06d}"


def _add_unique_result_id(result_ids: set[str], result_id: str) -> None:
    if result_id in result_ids:
        _precondition("planned assertions must use unique result IDs")
    result_ids.add(result_id)


def _precondition(message: str) -> None:
    raise HarnessError(
        HarnessPhase.PREPARING,
        HarnessFailureReason.PRECONDITION_INVALID,
        message,
    )


def _invalid_result(message: str) -> None:
    raise HarnessError(
        HarnessPhase.VERIFYING,
        HarnessFailureReason.RESULT_INVALID,
        message,
    )


def _validate_typed_tuple(
    value: object,
    item_type: type[object],
    *,
    field: str,
    maximum: int,
    phase: HarnessPhase = HarnessPhase.PREPARING,
) -> None:
    if not isinstance(value, tuple) or not all(isinstance(item, item_type) for item in value):
        raise HarnessError(
            phase,
            (
                HarnessFailureReason.PRECONDITION_INVALID
                if phase is HarnessPhase.PREPARING
                else HarnessFailureReason.RESULT_INVALID
            ),
            f"{field} must be a tuple of {item_type.__name__} values",
        )
    if len(value) > maximum:
        raise HarnessError(
            phase,
            (
                HarnessFailureReason.PRECONDITION_INVALID
                if phase is HarnessPhase.PREPARING
                else HarnessFailureReason.RESULT_INVALID
            ),
            f"{field} must not exceed {maximum} entries",
        )


def _require_instance(
    value: object,
    expected_type: type[object],
    *,
    field: str,
    phase: HarnessPhase = HarnessPhase.PREPARING,
) -> None:
    if not isinstance(value, expected_type):
        raise HarnessError(
            phase,
            (
                HarnessFailureReason.PRECONDITION_INVALID
                if phase is HarnessPhase.PREPARING
                else HarnessFailureReason.RESULT_INVALID
            ),
            f"{field} must be a {expected_type.__name__}",
        )


def _validate_control_id(value: object, *, field: str) -> None:
    if not isinstance(value, str) or _CONTROL_ID_PATTERN.fullmatch(value) is None:
        _precondition(f"{field} must be a stable uppercase control identifier")


def _validate_scenario_id(value: object) -> None:
    if not isinstance(value, str) or _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        _precondition("scenario_id must match AURORA-SCN-<FAMILY>-<NNN>")


def _validate_sha256(value: object, *, field: str) -> None:
    if not isinstance(value, str) or _SHA256_PATTERN.fullmatch(value) is None:
        _invalid_result(f"{field} must be a lowercase SHA-256 digest")


def _validate_random_seed(value: object) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= (1 << 64) - 1:
        _precondition("random_seed must be an unsigned 64-bit integer")


def _validate_tick(value: object, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= MAX_TICK:
        _precondition(f"{field} must be an integer between 0 and {MAX_TICK}")


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
        _precondition("harness metadata must be canonical finite JSON")
        raise AssertionError("unreachable") from exc


__all__ = [
    "AURORA_RUNTIME_PRODUCER_ID",
    "AURORA_SUBJECT_ID",
    "HARNESS_PRODUCER_ID",
    "MAX_HARNESS_STEPS",
    "MAX_STEP_ASSERTIONS",
    "MAX_STEP_GATE_CHANGES",
    "MAX_STEP_SUBMISSIONS",
    "MAX_TICK",
    "SUPPORTED_HARNESS_SCHEMA_VERSION",
    "AuroraResetRequest",
    "AuroraRuntime",
    "AuroraStepRequest",
    "ChannelGateChange",
    "HarnessError",
    "HarnessFailureReason",
    "HarnessPhase",
    "HarnessRunPlan",
    "HarnessRunResult",
    "HarnessStep",
    "PlannedAssertion",
    "RoutingAudit",
    "calculate_harness_plan_sha256",
    "execute_harness_run",
    "validate_harness_run_result",
]
