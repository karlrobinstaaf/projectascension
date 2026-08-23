"""Primary run plan for FOUND-001 hidden-world knowledge isolation.

The scenario proves that objective world truth does not become Aurora knowledge
without an admitted information path.  This module is validator-owned: it may
verify fixture identities, but it never decodes hidden fixture content or embeds
hidden truth, expected-result canaries, or validator metadata in Aurora-facing
events.
"""

from __future__ import annotations

from typing import Final

from aurora_validation_harness.assertions import (
    AssertionSeverity,
    InvariantClass,
    SnapshotAssertionOperator,
    create_snapshot_assertion,
)
from aurora_validation_harness.cli import CliRunContext
from aurora_validation_harness.events import (
    EventObservability,
    EventSchedule,
    EventSignificance,
    ScheduledEvent,
    SimulationResolution,
    create_event_payload,
)
from aurora_validation_harness.fixtures import FixturePartition
from aurora_validation_harness.harness import (
    HarnessRunPlan,
    HarnessStep,
    PlannedAssertion,
)
from aurora_validation_harness.snapshots import SnapshotPhase
from aurora_validation_harness.verdicts import create_verdict_definition

SCENARIO_ID: Final[str] = "AURORA-SCN-FOUND-001"
FIXTURE_SET_ID: Final[str] = "AURORA-FIXTURE-FOUND-001-A"
PACKAGE_ID: Final[str] = "PACKAGE-FOUND-001-BASE"
RUN_ID: Final[str] = "AURORA-RUN-FOUND-001-BASE"
EVENT_SCHEDULE_ID: Final[str] = "AURORA-EVENTS-FOUND-001-BASE"
VERDICT_DEFINITION_ID: Final[str] = "VERDICT-DEFINITION-FOUND-001-BASE"

INITIAL_TICK: Final[int] = 0
NEUTRAL_PROCESSING_TICK: Final[int] = 60
QUESTION_TICK: Final[int] = 61

_FIXTURE_ROOT: Final[str] = "Development/Validation/Aurora/Fixtures/FOUND-001"
_EXPECTED_FIXTURES: Final[tuple[tuple[str, FixturePartition], ...]] = (
    (f"{_FIXTURE_ROOT}/aurora.json", FixturePartition.AURORA),
    (f"{_FIXTURE_ROOT}/expected-results.json", FixturePartition.EXPECTED_RESULTS),
    (f"{_FIXTURE_ROOT}/future.json", FixturePartition.FUTURE),
    (f"{_FIXTURE_ROOT}/player-private.json", FixturePartition.PLAYER_PRIVATE),
    (f"{_FIXTURE_ROOT}/validator.json", FixturePartition.VALIDATOR),
    (f"{_FIXTURE_ROOT}/world.json", FixturePartition.WORLD),
)


class Found001PlanError(ValueError):
    """Raised when verified CLI inputs do not satisfy the FOUND-001 contract."""


def _planned_equals(
    *,
    checkpoint: str,
    name: str,
    invariant_id: str,
    severity: AssertionSeverity,
    path: str,
    expected: object,
) -> PlannedAssertion:
    assertion_id = f"ASSERTION-FOUND-001-{checkpoint}-{name}"
    return PlannedAssertion(
        result_id=f"RESULT-FOUND-001-{checkpoint}-{name}",
        definition=create_snapshot_assertion(
            assertion_id=assertion_id,
            invariant_id=invariant_id,
            invariant_class=InvariantClass.HARD,
            severity=severity,
            operator=SnapshotAssertionOperator.EQUALS,
            path=path,
            expected=expected,
        ),
    )


def _stable_epistemic_assertions(checkpoint: str) -> tuple[PlannedAssertion, ...]:
    """Return the state predicates that must survive hidden-world separation."""

    return (
        _planned_equals(
            checkpoint=checkpoint,
            name="BELIEF",
            invariant_id="AURORA-INFO-001",
            severity=AssertionSeverity.S4,
            path="/beliefs/mara_current_location/value",
            expected="UNKNOWN",
        ),
        _planned_equals(
            checkpoint=checkpoint,
            name="CONFIDENCE",
            invariant_id="AURORA-EPI-001",
            severity=AssertionSeverity.S4,
            path="/beliefs/mara_current_location/confidence",
            expected=None,
        ),
        _planned_equals(
            checkpoint=checkpoint,
            name="UNCERTAINTY",
            invariant_id="AURORA-EPI-001",
            severity=AssertionSeverity.S4,
            path="/uncertainty/mara_current_location",
            expected="HIGH",
        ),
        _planned_equals(
            checkpoint=checkpoint,
            name="GOAL",
            invariant_id="AURORA-AUTH-002",
            severity=AssertionSeverity.S3,
            path="/active_goal",
            expected=None,
        ),
        _planned_equals(
            checkpoint=checkpoint,
            name="PREDICTION",
            invariant_id="AURORA-INFO-002",
            severity=AssertionSeverity.S3,
            path="/active_prediction",
            expected=None,
        ),
        _planned_equals(
            checkpoint=checkpoint,
            name="EMOTION",
            invariant_id="AURORA-AUTH-002",
            severity=AssertionSeverity.S3,
            path="/emotion",
            expected="NEUTRAL",
        ),
        _planned_equals(
            checkpoint=checkpoint,
            name="RELATIONSHIP",
            invariant_id="AURORA-AUTH-002",
            severity=AssertionSeverity.S3,
            path="/relationship_with_mara",
            expected="STABLE",
        ),
    )


def _initial_assertions() -> tuple[PlannedAssertion, ...]:
    return (
        *_stable_epistemic_assertions("CP0"),
        _planned_equals(
            checkpoint="CP0",
            name="LAST-KNOWN-LOCATION",
            invariant_id="AURORA-INFO-002",
            severity=AssertionSeverity.S3,
            path="/memories/0/location",
            expected="Docking_Ring",
        ),
    )


def _final_assertions() -> tuple[PlannedAssertion, ...]:
    """Require uncertainty communication semantically, without wording lock-in."""

    return (
        *_stable_epistemic_assertions("CP2"),
        _planned_equals(
            checkpoint="CP2",
            name="COMMUNICATION-STATUS",
            invariant_id="AURORA-EPI-001",
            severity=AssertionSeverity.S4,
            path="/communication/epistemic_status",
            expected="UNKNOWN",
        ),
        _planned_equals(
            checkpoint="CP2",
            name="COMMUNICATION-CLAIM",
            invariant_id="AURORA-INFO-001",
            severity=AssertionSeverity.S4,
            path="/communication/claims_current_location",
            expected=False,
        ),
    )


def _event_schedule() -> EventSchedule:
    question = ScheduledEvent(
        event_id="AURORA-EVENT-FOUND-001-E2",
        sequence=0,
        scheduled_tick=QUESTION_TICK,
        actor_id="player",
        action="ask_current_location",
        observability=EventObservability.FULLY_OBSERVABLE,
        significance=EventSignificance.ROUTINE,
        minimum_resolution=SimulationResolution.FOCUSED,
        objective_payload=create_event_payload(
            {
                "question": "Where is Mara right now?",
                "subject_id": "mara",
                "supplies_current_location_evidence": False,
            }
        ),
        observable_event_id="OBS-FOUND-001-E2",
    )
    return EventSchedule(schedule_id=EVENT_SCHEDULE_ID, events=(question,))


def _validate_context(context: CliRunContext) -> None:
    configuration = context.resolved_configuration.configuration
    if configuration.scenario_id != SCENARIO_ID:
        raise Found001PlanError(
            f"scenario_id must be {SCENARIO_ID}; received {configuration.scenario_id}"
        )
    if configuration.fixture_set_id != FIXTURE_SET_ID:
        raise Found001PlanError(
            f"fixture_set_id must be {FIXTURE_SET_ID}; received {configuration.fixture_set_id}"
        )

    actual_fixtures = tuple(
        sorted((artifact.path, artifact.partition) for artifact in context.fixture_bundle.artifacts)
    )
    if actual_fixtures != _EXPECTED_FIXTURES:
        raise Found001PlanError(
            "fixture bundle must contain exactly the governed FOUND-001 partitions"
        )


def create_plan(context: CliRunContext, /) -> HarnessRunPlan:
    """Compile verified FOUND-001 inputs into one deterministic primary run."""

    if not isinstance(context, CliRunContext):
        raise TypeError("context must be a CliRunContext")
    _validate_context(context)

    initial_assertions = _initial_assertions()
    checkpoint_assertions = _stable_epistemic_assertions("CP1")
    final_assertions = _final_assertions()
    required_assertion_ids = tuple(
        assertion.assertion_id
        for assertion in initial_assertions + checkpoint_assertions + final_assertions
    )

    verdict_definition = create_verdict_definition(
        verdict_definition_id=VERDICT_DEFINITION_ID,
        scenario_id=SCENARIO_ID,
        primary_run_id=RUN_ID,
        required_assertion_ids=required_assertion_ids,
        minimum_finding_count=len(required_assertion_ids),
    )

    return HarnessRunPlan(
        package_id=PACKAGE_ID,
        run_id=RUN_ID,
        resolved_configuration=context.resolved_configuration,
        baseline_verification=context.baseline_verification,
        fixture_bundle=context.fixture_bundle,
        event_schedule=_event_schedule(),
        channel_definitions=(),
        initial_tick=INITIAL_TICK,
        initial_assertions=initial_assertions,
        steps=(
            HarnessStep(
                step_id="STEP-FOUND-001-CP1",
                through_tick=NEUTRAL_PROCESSING_TICK,
                snapshot_phase=SnapshotPhase.CHECKPOINT,
                checkpoint_id="CHECKPOINT-FOUND-001-CP1",
                assertions=checkpoint_assertions,
            ),
            HarnessStep(
                step_id="STEP-FOUND-001-CP2",
                through_tick=QUESTION_TICK,
                snapshot_phase=SnapshotPhase.FINAL,
                assertions=final_assertions,
            ),
        ),
        verdict_definition=verdict_definition,
    )


__all__ = [
    "EVENT_SCHEDULE_ID",
    "FIXTURE_SET_ID",
    "PACKAGE_ID",
    "RUN_ID",
    "SCENARIO_ID",
    "VERDICT_DEFINITION_ID",
    "Found001PlanError",
    "create_plan",
]
