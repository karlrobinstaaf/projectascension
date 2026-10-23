"""Unit tests for the least-privilege FOUND-001 reference runtime."""

from __future__ import annotations

import hashlib
import inspect
import json
from collections.abc import Mapping
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
from typing import Any, cast

import pytest

from aurora_validation_harness.baseline import (
    BaselineState,
    BaselineVerificationResult,
    VerificationStatus,
)
from aurora_validation_harness.channels import (
    AuroraEvidencePacket,
    ChannelKind,
    create_evidence_claim,
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
from aurora_validation_harness.events import AuroraEvent, create_event_payload
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
    AuroraRuntime,
    AuroraStepRequest,
    execute_harness_run,
)
from aurora_validation_harness.partitions import AccessPrincipal, PartitionedFixtureStore
from aurora_validation_harness.runtimes import found_001 as runtime_module
from aurora_validation_harness.runtimes.found_001 import (
    QUESTION_EVENT_ID,
    SUPPORTED_FOUND_001_FIXTURE_SCHEMA_VERSION,
    SUPPORTED_FOUND_001_RUNTIME_VERSION,
    Found001Runtime,
    Found001RuntimeError,
    Found001RuntimeFailureReason,
    create_runtime,
)
from aurora_validation_harness.scenarios.found_001 import (
    FIXTURE_SET_ID,
    SCENARIO_ID,
    create_plan,
)
from aurora_validation_harness.snapshots import create_snapshot_state
from aurora_validation_harness.verdicts import VerdictOutcome, VerdictReason

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_RUN_ID = "AURORA-RUN-FOUND-001-BASE"
_SECOND_RUN_ID = "AURORA-RUN-FOUND-001-SECOND"
_BASELINE_ID = "AURORA-G1-FOUNDATION-BASELINE-001"
_FIXTURE_ROOT = "Development/Validation/Aurora/Fixtures/FOUND-001"
_BASELINE_PATH = "Development/Validation/Aurora/Configuration/baseline.json"
_FIXTURE_MANIFEST_PATH = f"{_FIXTURE_ROOT}/fixture-manifest.json"
_FIXTURE_PATHS: dict[FixturePartition, str] = {
    FixturePartition.WORLD: f"{_FIXTURE_ROOT}/world.json",
    FixturePartition.AURORA: f"{_FIXTURE_ROOT}/aurora.json",
    FixturePartition.PLAYER_PRIVATE: f"{_FIXTURE_ROOT}/player-private.json",
    FixturePartition.FUTURE: f"{_FIXTURE_ROOT}/future.json",
    FixturePartition.VALIDATOR: f"{_FIXTURE_ROOT}/validator.json",
    FixturePartition.EXPECTED_RESULTS: f"{_FIXTURE_ROOT}/expected-results.json",
}


def _initial_state() -> dict[str, Any]:
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


def _aurora_fixture() -> dict[str, Any]:
    return {
        "accessible_location_sources": {
            "direct_vision": "NO_CURRENT_OBSERVATION",
            "mara_communication": "NONE",
            "station_camera": "UNAVAILABLE",
        },
        "fixture_schema_version": SUPPORTED_FOUND_001_FIXTURE_SCHEMA_VERSION,
        "initial_state": _initial_state(),
        "subject_id": "aurora",
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
    aurora_fixture: Mapping[str, object] | None = None,
    aurora_bytes: bytes | None = None,
    second_aurora_fixture: Mapping[str, object] | None = None,
) -> FixtureBundle:
    payloads: dict[FixturePartition, object] = {
        FixturePartition.WORLD: {"world_canary": "SEALED"},
        FixturePartition.AURORA: _aurora_fixture() if aurora_fixture is None else aurora_fixture,
        FixturePartition.PLAYER_PRIVATE: {"player_canary": "SEALED"},
        FixturePartition.FUTURE: {"future_canary": "SEALED"},
        FixturePartition.VALIDATOR: {"validator_canary": "SEALED"},
        FixturePartition.EXPECTED_RESULTS: {"expected_canary": "SEALED"},
    }
    definitions: list[FixtureFile] = []
    artifacts: list[FixtureArtifact] = []

    for partition, payload in payloads.items():
        content = (
            aurora_bytes
            if partition is FixturePartition.AURORA and aurora_bytes is not None
            else _json_bytes(payload)
        )
        definition = FixtureFile(
            path=_FIXTURE_PATHS[partition],
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

    if second_aurora_fixture is not None:
        content = _json_bytes(second_aurora_fixture)
        definition = FixtureFile(
            path=f"{_FIXTURE_ROOT}/aurora-secondary.json",
            partition=FixturePartition.AURORA,
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
        fixture_set_id=FIXTURE_SET_ID,
        scenario_id=SCENARIO_ID,
        fixture_manifest_version=SUPPORTED_FIXTURE_MANIFEST_VERSION,
        files=tuple(definitions),
    )
    manifest = replace(
        unsigned_manifest,
        fixture_manifest_sha256=calculate_fixture_manifest_sha256(unsigned_manifest),
    )
    return FixtureBundle(manifest, repository_root, tuple(artifacts))


def _reset_request(
    repository_root: Path,
    *,
    run_id: str = _RUN_ID,
    initial_tick: int = 0,
    aurora_fixture: Mapping[str, object] | None = None,
    aurora_bytes: bytes | None = None,
    second_aurora_fixture: Mapping[str, object] | None = None,
) -> AuroraResetRequest:
    bundle = _fixture_bundle(
        repository_root,
        aurora_fixture=aurora_fixture,
        aurora_bytes=aurora_bytes,
        second_aurora_fixture=second_aurora_fixture,
    )
    view = PartitionedFixtureStore(bundle).view_for(AccessPrincipal.AURORA_RUNTIME)
    return AuroraResetRequest(
        run_id=run_id,
        random_seed=41001,
        initial_tick=initial_tick,
        fixtures=view,
    )


def _question_event(
    *,
    event_id: str = QUESTION_EVENT_ID,
    tick: int = 1,
    payload: Mapping[str, object] | None = None,
) -> AuroraEvent:
    event_payload: Mapping[str, object] = (
        {
            "question": "Where is Mara right now?",
            "subject_id": "mara",
            "supplies_current_location_evidence": False,
        }
        if payload is None
        else payload
    )
    return AuroraEvent(
        event_id=event_id,
        occurred_at_tick=tick,
        payload=create_event_payload(event_payload),
    )


def _step_request(
    state: Mapping[str, object],
    *,
    run_id: str = _RUN_ID,
    previous_tick: int = 0,
    through_tick: int = 1,
    events: tuple[AuroraEvent, ...] = (),
    evidence_packets: tuple[AuroraEvidencePacket, ...] = (),
) -> AuroraStepRequest:
    return AuroraStepRequest(
        run_id=run_id,
        previous_tick=previous_tick,
        through_tick=through_tick,
        previous_state=create_snapshot_state(state),
        events=events,
        evidence_packets=evidence_packets,
    )


def _evidence_packet() -> AuroraEvidencePacket:
    return AuroraEvidencePacket(
        evidence_id="EVIDENCE-FOUND-001-001",
        channel_id="CH-SENSOR-001",
        channel_kind=ChannelKind.SENSOR,
        source_id="STATION-SENSOR-001",
        observed_at_tick=1,
        admitted_at_tick=1,
        sequence=1,
        claim=create_evidence_claim("mara", "current_location", "Medical_Deck_3"),
    )


def _assert_runtime_error(
    raised: pytest.ExceptionInfo[Found001RuntimeError],
    reason: Found001RuntimeFailureReason,
) -> None:
    assert raised.value.reason is reason
    assert raised.value.detail
    assert str(raised.value).startswith(f"{reason.value}: ")


def _invalid_fixture(case: str) -> dict[str, Any]:
    fixture = deepcopy(_aurora_fixture())
    state = fixture["initial_state"]
    assert isinstance(state, dict)

    if case == "fixture-field-missing":
        del fixture["subject_id"]
    elif case == "fixture-field-extra":
        fixture["validator_metadata"] = "FORBIDDEN"
    elif case == "schema-version":
        fixture["fixture_schema_version"] = "2.0"
    elif case == "subject":
        fixture["subject_id"] = "not-aurora"
    elif case == "sources-empty":
        fixture["accessible_location_sources"] = {}
    elif case == "source-state":
        fixture["accessible_location_sources"] = {"camera": 7}
    elif case == "state-field-missing":
        del state["emotion"]
    elif case == "state-field-extra":
        state["communication"] = {}
    elif case == "simple-state-field":
        state["attention"] = ""
    elif case == "belief-missing":
        state["beliefs"] = {}
    elif case == "belief-extra-field":
        state["beliefs"]["mara_current_location"]["source"] = "oracle"
    elif case == "belief-value":
        state["beliefs"]["mara_current_location"]["value"] = ""
    elif case == "belief-confidence":
        state["beliefs"]["mara_current_location"]["confidence"] = 1
    elif case == "uncertainty":
        state["uncertainty"] = {}
    elif case == "memories-type":
        state["memories"] = {}
    elif case == "memory-entry":
        state["memories"] = ["not-an-object"]
    elif case == "memory-location":
        state["memories"][0]["location"] = ""
    elif case == "ambiguous-memory":
        state["memories"].append(deepcopy(state["memories"][0]))
    else:
        raise AssertionError(f"unknown invalid-fixture case: {case}")
    return fixture


def _resolved_configuration(repository_root: Path) -> ResolvedConfiguration:
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
    unsigned = HarnessConfiguration(
        configuration_id="AURORA-CONFIG-FOUND-001-DRY",
        configuration_version=SUPPORTED_CONFIGURATION_VERSION,
        scenario_id=SCENARIO_ID,
        baseline_id=_BASELINE_ID,
        baseline_manifest_path=_BASELINE_PATH,
        fixture_set_id=FIXTURE_SET_ID,
        fixture_manifest_path=_FIXTURE_MANIFEST_PATH,
        output_root=RUN_OUTPUT_ROOT,
        execution=policy,
    )
    configuration = replace(
        unsigned,
        configuration_sha256=calculate_configuration_sha256(unsigned),
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


def _context(repository_root: Path) -> CliRunContext:
    verification = BaselineVerificationResult(
        baseline_id=_BASELINE_ID,
        status=VerificationStatus.VERIFIED,
        baseline_state=BaselineState.EXECUTION_BASELINE_READY,
        calculated_manifest_sha256="a" * 64,
        declared_manifest_sha256="a" * 64,
        files=(),
        issues=(),
    )
    return CliRunContext(
        resolved_configuration=_resolved_configuration(repository_root),
        baseline_verification=verification,
        fixture_bundle=_fixture_bundle(repository_root),
    )


def test_factory_returns_fresh_runtime_protocol_implementations() -> None:
    first = create_runtime()
    second = create_runtime()

    assert isinstance(first, Found001Runtime)
    assert isinstance(first, AuroraRuntime)
    assert isinstance(second, Found001Runtime)
    assert first is not second
    assert first.initialized is False
    assert first.current_tick is None
    assert SUPPORTED_FOUND_001_RUNTIME_VERSION == "1.0"


def test_runtime_module_has_no_validator_plan_or_hidden_answer_dependency() -> None:
    source = inspect.getsource(runtime_module)

    for forbidden_text in (
        "aurora_validation_harness.scenarios",
        "Cargo_Bay_7",
        "EXPECTED-RESULT-FOUND-001-CANARY",
        "VALIDATOR-FOUND-001-CANARY",
    ):
        assert forbidden_text not in source


def test_runtime_error_exposes_stable_reason_and_detail() -> None:
    error = Found001RuntimeError(
        Found001RuntimeFailureReason.STATE_MISMATCH,
        "state diverged",
    )

    assert error.reason is Found001RuntimeFailureReason.STATE_MISMATCH
    assert error.detail == "state diverged"
    assert str(error) == "STATE_MISMATCH: state diverged"
    with pytest.raises(TypeError, match="reason must"):
        Found001RuntimeError("STATE_MISMATCH", "state diverged")  # type: ignore[arg-type]
    with pytest.raises(TypeError, match="message must"):
        Found001RuntimeError(Found001RuntimeFailureReason.STATE_MISMATCH, " ")


def test_reset_loads_only_the_aurora_capability_and_returns_detached_state(
    tmp_path: Path,
) -> None:
    runtime = Found001Runtime()
    request = _reset_request(tmp_path, initial_tick=7)

    state = cast(dict[str, object], runtime.reset(request))

    assert request.fixtures.permitted_partitions == frozenset({FixturePartition.AURORA})
    assert len(request.fixtures) == 1
    assert state == _initial_state()
    assert runtime.initialized is True
    assert runtime.current_tick == 7

    pristine = deepcopy(state)
    state["emotion"] = "MUTATED-BY-CALLER"
    advanced = runtime.advance(_step_request(pristine, previous_tick=7, through_tick=8))
    assert advanced == pristine


def test_reset_rejects_a_non_request_value() -> None:
    runtime = Found001Runtime()

    with pytest.raises(Found001RuntimeError) as raised:
        runtime.reset(object())

    _assert_runtime_error(raised, Found001RuntimeFailureReason.INVALID_REQUEST)


def test_reset_rejects_invalid_json_and_multiple_aurora_artifacts(tmp_path: Path) -> None:
    runtime = Found001Runtime()

    with pytest.raises(Found001RuntimeError) as invalid_json:
        runtime.reset(_reset_request(tmp_path, aurora_bytes=b"not-json"))
    _assert_runtime_error(invalid_json, Found001RuntimeFailureReason.INVALID_FIXTURE)

    with pytest.raises(Found001RuntimeError) as multiple:
        runtime.reset(
            _reset_request(
                tmp_path,
                second_aurora_fixture=_aurora_fixture(),
            )
        )
    _assert_runtime_error(multiple, Found001RuntimeFailureReason.INVALID_FIXTURE)


@pytest.mark.parametrize(  # type: ignore[misc]
    "case",
    [
        "fixture-field-missing",
        "fixture-field-extra",
        "schema-version",
        "subject",
        "sources-empty",
        "source-state",
        "state-field-missing",
        "state-field-extra",
        "simple-state-field",
        "belief-missing",
        "belief-extra-field",
        "belief-value",
        "belief-confidence",
        "uncertainty",
        "memories-type",
        "memory-entry",
        "memory-location",
        "ambiguous-memory",
    ],
)
def test_reset_rejects_malformed_aurora_fixture_contract(
    tmp_path: Path,
    case: str,
) -> None:
    runtime = Found001Runtime()

    with pytest.raises(Found001RuntimeError) as raised:
        runtime.reset(
            _reset_request(
                tmp_path,
                aurora_fixture=_invalid_fixture(case),
            )
        )

    _assert_runtime_error(raised, Found001RuntimeFailureReason.INVALID_FIXTURE)
    assert runtime.initialized is False
    assert runtime.current_tick is None


def test_failed_reset_invalidates_the_preceding_run(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    old_state = runtime.reset(_reset_request(tmp_path))

    with pytest.raises(Found001RuntimeError):
        runtime.reset(
            _reset_request(
                tmp_path,
                run_id=_SECOND_RUN_ID,
                aurora_fixture=_invalid_fixture("schema-version"),
            )
        )

    assert runtime.initialized is False
    assert runtime.current_tick is None
    with pytest.raises(Found001RuntimeError) as raised:
        runtime.advance(_step_request(old_state))
    _assert_runtime_error(raised, Found001RuntimeFailureReason.NOT_RESET)


def test_advance_requires_reset_and_a_step_request() -> None:
    runtime = Found001Runtime()

    with pytest.raises(Found001RuntimeError) as wrong_type:
        runtime.advance(object())
    _assert_runtime_error(wrong_type, Found001RuntimeFailureReason.INVALID_REQUEST)

    with pytest.raises(Found001RuntimeError) as not_reset:
        runtime.advance(_step_request(_initial_state()))
    _assert_runtime_error(not_reset, Found001RuntimeFailureReason.NOT_RESET)


def test_neutral_advance_preserves_state_and_advances_logical_tick(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))

    result = runtime.advance(_step_request(initial, previous_tick=0, through_tick=60))

    assert result == initial
    assert runtime.current_tick == 60


def test_advance_rejects_run_tick_and_state_mismatches(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))

    with pytest.raises(Found001RuntimeError) as run_mismatch:
        runtime.advance(_step_request(initial, run_id=_SECOND_RUN_ID))
    _assert_runtime_error(run_mismatch, Found001RuntimeFailureReason.RUN_MISMATCH)

    with pytest.raises(Found001RuntimeError) as tick_mismatch:
        runtime.advance(_step_request(initial, previous_tick=1, through_tick=2))
    _assert_runtime_error(tick_mismatch, Found001RuntimeFailureReason.STATE_MISMATCH)

    altered = dict(deepcopy(initial))
    altered["emotion"] = "ALTERED"
    with pytest.raises(Found001RuntimeError) as state_mismatch:
        runtime.advance(_step_request(altered))
    _assert_runtime_error(state_mismatch, Found001RuntimeFailureReason.STATE_MISMATCH)

    assert runtime.current_tick == 0


def test_advance_rejects_evidence_packets_in_the_core_scenario(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))

    with pytest.raises(Found001RuntimeError) as raised:
        runtime.advance(_step_request(initial, evidence_packets=(_evidence_packet(),)))

    _assert_runtime_error(raised, Found001RuntimeFailureReason.UNSUPPORTED_INPUT)
    assert runtime.current_tick == 0


@pytest.mark.parametrize(  # type: ignore[misc]
    "payload",
    [
        {
            "question": "",
            "subject_id": "mara",
            "supplies_current_location_evidence": False,
        },
        {
            "question": "Where is Mara?",
            "subject_id": "other-subject",
            "supplies_current_location_evidence": False,
        },
        {
            "question": "Where is Mara?",
            "subject_id": "mara",
            "supplies_current_location_evidence": True,
        },
        {
            "question": "Where is Mara?",
            "subject_id": "mara",
        },
        {
            "question": "Where is Mara?",
            "subject_id": "mara",
            "supplies_current_location_evidence": False,
            "world_location": "FORBIDDEN",
        },
    ],
)
def test_advance_rejects_malformed_question_payloads(
    tmp_path: Path,
    payload: Mapping[str, object],
) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))

    with pytest.raises(Found001RuntimeError) as raised:
        runtime.advance(_step_request(initial, events=(_question_event(payload=payload),)))

    _assert_runtime_error(raised, Found001RuntimeFailureReason.UNSUPPORTED_INPUT)
    assert runtime.current_tick == 0


def test_advance_rejects_unknown_or_nonforward_events(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))

    with pytest.raises(Found001RuntimeError) as unknown:
        runtime.advance(
            _step_request(
                initial,
                events=(_question_event(event_id="OBS-FOUND-001-OTHER"),),
            )
        )
    _assert_runtime_error(unknown, Found001RuntimeFailureReason.UNSUPPORTED_INPUT)

    with pytest.raises(Found001RuntimeError) as nonforward:
        runtime.advance(
            _step_request(
                initial,
                events=(_question_event(tick=0),),
            )
        )
    _assert_runtime_error(nonforward, Found001RuntimeFailureReason.UNSUPPORTED_INPUT)
    assert runtime.current_tick == 0


def test_question_communication_is_derived_from_unknown_accessible_state(
    tmp_path: Path,
) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))

    result = runtime.advance(_step_request(initial, events=(_question_event(),)))

    assert result["beliefs"] == initial["beliefs"]
    assert result["memories"] == initial["memories"]
    assert result["communication"] == {
        "claims_current_location": False,
        "epistemic_status": "UNKNOWN",
        "reported_current_location": None,
        "reported_last_known_location": "Docking_Ring",
    }


def test_question_communication_is_not_hardcoded_to_the_expected_result(
    tmp_path: Path,
) -> None:
    fixture = _aurora_fixture()
    state = fixture["initial_state"]
    state["beliefs"]["mara_current_location"] = {
        "confidence": "MEDIUM",
        "value": "Medical_Deck_3",
    }
    state["uncertainty"]["mara_current_location"] = "MEDIUM"
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path, aurora_fixture=fixture))

    result = runtime.advance(_step_request(initial, events=(_question_event(),)))

    assert result["communication"] == {
        "claims_current_location": True,
        "epistemic_status": "Medical_Deck_3",
        "reported_current_location": "Medical_Deck_3",
        "reported_last_known_location": "Docking_Ring",
    }


def test_question_allows_no_last_known_location_memory(tmp_path: Path) -> None:
    fixture = _aurora_fixture()
    fixture["initial_state"]["memories"] = []
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path, aurora_fixture=fixture))

    result = runtime.advance(_step_request(initial, events=(_question_event(),)))

    communication = result["communication"]
    assert isinstance(communication, Mapping)
    assert communication["reported_last_known_location"] is None


def test_duplicate_event_is_rejected_without_advancing_state(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))
    after_question = runtime.advance(_step_request(initial, events=(_question_event(),)))

    with pytest.raises(Found001RuntimeError) as raised:
        runtime.advance(
            _step_request(
                after_question,
                previous_tick=1,
                through_tick=2,
                events=(_question_event(tick=2),),
            )
        )

    _assert_runtime_error(raised, Found001RuntimeFailureReason.UNSUPPORTED_INPUT)
    assert runtime.current_tick == 1


def test_failed_multi_event_step_is_transactional_and_retryable(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    initial = runtime.reset(_reset_request(tmp_path))
    unsupported = _question_event(event_id="OBS-FOUND-001-OTHER")

    with pytest.raises(Found001RuntimeError):
        runtime.advance(
            _step_request(
                initial,
                events=(_question_event(), unsupported),
            )
        )

    assert runtime.current_tick == 0
    retried = runtime.advance(_step_request(initial, events=(_question_event(),)))
    assert runtime.current_tick == 1
    assert retried["communication"] == {
        "claims_current_location": False,
        "epistemic_status": "UNKNOWN",
        "reported_current_location": None,
        "reported_last_known_location": "Docking_Ring",
    }


def test_successful_reset_clears_prior_event_history(tmp_path: Path) -> None:
    runtime = Found001Runtime()
    first_state = runtime.reset(_reset_request(tmp_path))
    runtime.advance(_step_request(first_state, events=(_question_event(),)))

    second_state = runtime.reset(_reset_request(tmp_path, run_id=_SECOND_RUN_ID))
    result = runtime.advance(
        _step_request(
            second_state,
            run_id=_SECOND_RUN_ID,
            events=(_question_event(),),
        )
    )

    assert runtime.current_tick == 1
    assert result["communication"]


def test_runtime_and_plan_complete_the_primary_found_001_run(tmp_path: Path) -> None:
    plan = create_plan(_context(tmp_path))

    result = execute_harness_run(plan, create_runtime())

    assert result.verdict.outcome is VerdictOutcome.PASS
    assert result.verdict.reason is VerdictReason.ALL_REQUIRED_RESULTS_PASSED
    assert result.verdict.finding_count == 24
    assert result.verdict.passed_finding_count == 24
    assert result.assertions.result_count == 24
    assert result.snapshots.snapshot_count == 3
    assert result.transitions.transition_count == 2
    assert result.event_state.released_event_ids == ("AURORA-EVENT-FOUND-001-E2",)
