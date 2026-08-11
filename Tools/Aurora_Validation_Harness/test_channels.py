"""Unit tests for deterministic, provenance-preserving Aurora evidence channels."""

from __future__ import annotations

import hashlib
import json
from dataclasses import FrozenInstanceError, replace

import pytest

from aurora_validation_harness import channels as channels_module
from aurora_validation_harness.channels import (
    DEFAULT_MAX_CLAIM_BYTES,
    MAX_CLAIM_BYTES,
    MAX_TICK,
    ChannelDefinition,
    ChannelError,
    ChannelGateState,
    ChannelKind,
    ChannelRoutingResult,
    ChannelRuntimeState,
    EvidenceClaim,
    EvidenceSubmission,
    RoutingReason,
    RoutingStatus,
    create_channel_state,
    create_evidence_claim,
    route_submission,
    set_channel_gate,
)

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_CHANNEL_ID = "CH-STATION-LOC"
_SOURCE_ID = "STATION-LOC-SYSTEM"
_VALIDATOR_EVENT_ID = "AURORA-SCN-FOUND-001-E1"


def _definition(
    *,
    channel_id: str = _CHANNEL_ID,
    kind: ChannelKind = ChannelKind.SENSOR,
    source_id: str = _SOURCE_ID,
    max_claim_bytes: int = DEFAULT_MAX_CLAIM_BYTES,
) -> ChannelDefinition:
    return ChannelDefinition(
        channel_id=channel_id,
        kind=kind,
        source_id=source_id,
        max_claim_bytes=max_claim_bytes,
    )


def _claim(value: object = "platform-2") -> EvidenceClaim:
    return create_evidence_claim("Mara", "current_location", value)


def _submission(
    *,
    evidence_id: str = "EVIDENCE-001",
    channel_id: str = _CHANNEL_ID,
    source_id: str = _SOURCE_ID,
    validator_event_id: str = _VALIDATOR_EVENT_ID,
    observed_at_tick: int = 10,
    submitted_at_tick: int = 10,
    claim: EvidenceClaim | None = None,
) -> EvidenceSubmission:
    return EvidenceSubmission(
        evidence_id=evidence_id,
        channel_id=channel_id,
        source_id=source_id,
        validator_event_id=validator_event_id,
        observed_at_tick=observed_at_tick,
        submitted_at_tick=submitted_at_tick,
        claim=_claim() if claim is None else claim,
    )


def _route_admitted(
    *,
    definition: ChannelDefinition | None = None,
    submission: EvidenceSubmission | None = None,
) -> ChannelRoutingResult:
    active_definition = _definition() if definition is None else definition
    state = create_channel_state(active_definition, gate=ChannelGateState.OPEN)
    result = route_submission(
        active_definition,
        state,
        _submission() if submission is None else submission,
    )
    assert result.packet is not None
    return result


def _raw_claim(value_json: bytes, *, digest: str | None = None) -> EvidenceClaim:
    return EvidenceClaim(
        subject_id="Mara",
        predicate="current_location",
        value_json=value_json,
        value_sha256=hashlib.sha256(value_json).hexdigest() if digest is None else digest,
    )


def test_public_constants_define_bounded_deterministic_limits() -> None:
    assert DEFAULT_MAX_CLAIM_BYTES == 65_536
    assert MAX_CLAIM_BYTES == 1_048_576
    assert MAX_TICK == (1 << 63) - 1
    assert 0 < DEFAULT_MAX_CLAIM_BYTES < MAX_CLAIM_BYTES < MAX_TICK


def test_channel_enums_have_stable_contract_values() -> None:
    assert {kind.value for kind in ChannelKind} == {
        "DIRECT_OBSERVATION",
        "SENSOR",
        "COMMUNICATION",
        "TESTIMONY",
        "DOCUMENT",
        "SYSTEM_REPORT",
    }
    assert {gate.value for gate in ChannelGateState} == {"CLOSED", "OPEN"}
    assert {status.value for status in RoutingStatus} == {"ADMITTED", "BLOCKED"}
    assert {reason.value for reason in RoutingReason} == {
        "ADMITTED",
        "CHANNEL_CLOSED",
        "CHANNEL_ID_MISMATCH",
        "SOURCE_ID_MISMATCH",
        "DUPLICATE_EVIDENCE_ID",
        "OUT_OF_ORDER_SUBMISSION",
        "CLAIM_TOO_LARGE",
    }


@pytest.mark.parametrize(
    "value",
    [
        None,
        "Cargo_Bay_7",
        True,
        42,
        2.5,
        ["alpha", 2, False, None],
        {"confidence": 0.75, "locations": ["platform-2", "platform-3"]},
    ],
)
def test_evidence_claim_accepts_supported_json_values(value: object) -> None:
    claim = create_evidence_claim("Mara", "current_location", value)

    assert claim.decode_value() == value
    assert claim.size_bytes == len(claim.value_json)
    assert claim.value_sha256 == hashlib.sha256(claim.value_json).hexdigest()
    assert claim.to_mapping() == {
        "predicate": "current_location",
        "subject_id": "Mara",
        "value": value,
        "value_sha256": claim.value_sha256,
    }


def test_evidence_claim_uses_canonical_unicode_json_and_stable_hashing() -> None:
    first = create_evidence_claim(
        "Mara",
        "reported_location",
        {"zone": "Café", "confidence": 1},
    )
    second = create_evidence_claim(
        "Mara",
        "reported_location",
        {"confidence": 1, "zone": "Café"},
    )

    assert first == second
    assert first.value_json == '{"confidence":1,"zone":"Café"}'.encode()
    assert first.value_sha256 == second.value_sha256


def test_decoded_claim_value_is_a_fresh_copy() -> None:
    claim = _claim({"locations": ["platform-2"]})
    decoded = claim.decode_value()
    assert isinstance(decoded, dict)

    locations = decoded["locations"]
    assert isinstance(locations, list)
    locations.append("tampered")

    assert claim.decode_value() == {"locations": ["platform-2"]}


@pytest.mark.parametrize(
    "reserved_key",
    [
        "expected_answer",
        "Expected Answer",
        "EXPECTED-RESULT",
        "failure.conditions",
        "fixture_manifest_sha256",
        "fixture set id",
        "future-event-queue",
        "hidden_state_marker",
        "scenario_id",
        "scenario name",
        "validator.metadata",
        "validator_notes",
        "world-debug-state",
    ],
)
def test_evidence_claim_recursively_rejects_reserved_metadata_keys(
    reserved_key: str,
) -> None:
    value = {"observation": [{"payload": {reserved_key: "hidden"}}]}

    with pytest.raises(ChannelError, match="contains reserved metadata key"):
        _claim(value)


@pytest.mark.parametrize("value", [{1: "non-string"}, ("tuple",), {"set"}])
def test_evidence_claim_rejects_non_json_value_shapes(value: object) -> None:
    with pytest.raises(ChannelError, match=r"non-string object key|unsupported JSON value type"):
        _claim(value)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_evidence_claim_rejects_non_finite_numbers(value: float) -> None:
    with pytest.raises(ChannelError, match="contains a non-finite number"):
        _claim({"confidence": value})


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("subject_id", "", "subject_id contains unsupported identifier characters"),
        ("subject_id", 4, "subject_id must be a string"),
        ("predicate", "bad predicate", "predicate contains unsupported identifier characters"),
        ("predicate", None, "predicate must be a string"),
    ],
)
def test_evidence_claim_rejects_invalid_entity_identifiers(
    field: str,
    value: object,
    message: str,
) -> None:
    arguments: dict[str, object] = {
        "subject_id": "Mara",
        "predicate": "current_location",
        "value": "platform-2",
    }
    arguments[field] = value

    with pytest.raises(ChannelError, match=message):
        create_evidence_claim(**arguments)


@pytest.mark.parametrize(
    ("value_json", "message"),
    [
        (b"\xff", "value_json is not valid JSON"),
        (b"{broken", "value_json is not valid JSON"),
        (b"NaN", "non-finite JSON value is not allowed"),
    ],
)
def test_evidence_claim_direct_constructor_rejects_invalid_json(
    value_json: bytes,
    message: str,
) -> None:
    with pytest.raises(ChannelError, match=message):
        _raw_claim(value_json)


def test_evidence_claim_direct_constructor_rejects_noncanonical_json() -> None:
    with pytest.raises(ChannelError, match="value_json must use canonical JSON encoding"):
        _raw_claim(b'{"zone": "platform-2"}')


def test_evidence_claim_direct_constructor_revalidates_reserved_metadata() -> None:
    with pytest.raises(ChannelError, match="contains reserved metadata key"):
        _raw_claim(b'{"validator_metadata":"hidden"}')


def test_evidence_claim_direct_constructor_checks_bytes_and_digest() -> None:
    valid = _claim()

    with pytest.raises(ChannelError, match="value_json must be bytes"):
        replace(valid, value_json="not-bytes")
    with pytest.raises(ChannelError, match="value_sha256 must be a string"):
        replace(valid, value_sha256=7)
    with pytest.raises(ChannelError, match="lowercase 64-character SHA-256"):
        replace(valid, value_sha256="A" * 64)
    with pytest.raises(ChannelError, match="does not match value_json"):
        replace(valid, value_sha256="0" * 64)


def test_canonical_json_helper_translates_serialization_errors() -> None:
    with pytest.raises(ChannelError, match="value is not JSON-serializable"):
        channels_module._canonical_json_bytes({"unsupported": object()})


@pytest.mark.parametrize("kind", list(ChannelKind))
def test_channel_definition_accepts_every_provenance_kind(kind: ChannelKind) -> None:
    definition = _definition(kind=kind)

    assert definition.kind is kind
    assert definition.max_claim_bytes == DEFAULT_MAX_CLAIM_BYTES


@pytest.mark.parametrize("max_claim_bytes", [1, DEFAULT_MAX_CLAIM_BYTES, MAX_CLAIM_BYTES])
def test_channel_definition_accepts_claim_size_boundaries(max_claim_bytes: int) -> None:
    assert _definition(max_claim_bytes=max_claim_bytes).max_claim_bytes == max_claim_bytes


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("channel_id", "ch-station-loc", "uppercase identifier characters"),
        ("channel_id", "CH-VALIDATOR-LOC", "validator-reserved token"),
        ("channel_id", 7, "channel_id must be a string"),
        ("source_id", "SOURCE FIXTURE", "uppercase identifier characters"),
        ("source_id", "SOURCE-FIXTURE", "validator-reserved token"),
        ("source_id", None, "source_id must be a string"),
        ("kind", "SENSOR", "kind must be a ChannelKind"),
    ],
)
def test_channel_definition_rejects_invalid_control_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    valid = _definition()

    with pytest.raises(ChannelError, match=message):
        replace(valid, **{field: value})


@pytest.mark.parametrize("max_claim_bytes", [True, "1024", 1.5])
def test_channel_definition_rejects_non_integer_size_limit(max_claim_bytes: object) -> None:
    with pytest.raises(ChannelError, match="max_claim_bytes must be an integer"):
        replace(_definition(), max_claim_bytes=max_claim_bytes)


@pytest.mark.parametrize("max_claim_bytes", [0, -1, MAX_CLAIM_BYTES + 1])
def test_channel_definition_rejects_out_of_range_size_limit(max_claim_bytes: int) -> None:
    with pytest.raises(ChannelError, match="max_claim_bytes must be between"):
        replace(_definition(), max_claim_bytes=max_claim_bytes)


def test_create_channel_state_defaults_to_closed_pristine_state() -> None:
    state = create_channel_state(_definition())

    assert state == ChannelRuntimeState(
        channel_id=_CHANNEL_ID,
        gate=ChannelGateState.CLOSED,
        next_sequence=1,
        last_admitted_tick=None,
        admitted_evidence_ids=(),
    )


def test_create_channel_state_can_start_open() -> None:
    state = create_channel_state(_definition(), gate=ChannelGateState.OPEN)

    assert state.gate is ChannelGateState.OPEN


def test_set_channel_gate_changes_only_gate_and_preserves_history() -> None:
    admitted = _route_admitted()

    closed = set_channel_gate(_definition(), admitted.state, ChannelGateState.CLOSED)

    assert closed == replace(admitted.state, gate=ChannelGateState.CLOSED)
    assert closed.admitted_evidence_ids == ("EVIDENCE-001",)
    assert closed.next_sequence == 2


def test_channel_state_helpers_reject_invalid_runtime_types_and_mismatch() -> None:
    definition = _definition()
    state = create_channel_state(definition)

    with pytest.raises(ChannelError, match="definition must be a ChannelDefinition"):
        create_channel_state("definition")
    with pytest.raises(ChannelError, match="gate must be a ChannelGateState"):
        create_channel_state(definition, gate="OPEN")
    with pytest.raises(ChannelError, match="definition must be a ChannelDefinition"):
        set_channel_gate("definition", state, ChannelGateState.OPEN)
    with pytest.raises(ChannelError, match="state must be a ChannelRuntimeState"):
        set_channel_gate(definition, "state", ChannelGateState.OPEN)
    with pytest.raises(ChannelError, match="does not match channel definition"):
        set_channel_gate(
            definition,
            create_channel_state(_definition(channel_id="CH-OTHER-LOC")),
            ChannelGateState.OPEN,
        )
    with pytest.raises(ChannelError, match="gate must be a ChannelGateState"):
        set_channel_gate(definition, state, "OPEN")


@pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"gate": "OPEN"}, "gate must be a ChannelGateState"),
        ({"next_sequence": True}, "next_sequence must be an integer"),
        ({"next_sequence": 1.5}, "next_sequence must be an integer"),
        ({"next_sequence": 0}, "next_sequence must be positive"),
        ({"last_admitted_tick": True}, "last_admitted_tick must be an integer"),
        ({"last_admitted_tick": -1}, "last_admitted_tick must be between"),
        ({"admitted_evidence_ids": ["EVIDENCE-001"]}, "must be a tuple of strings"),
        ({"admitted_evidence_ids": (1,)}, "must be a tuple of strings"),
        ({"admitted_evidence_ids": ("bad-id",)}, "uppercase identifier characters"),
        (
            {
                "admitted_evidence_ids": ("EVIDENCE-001", "EVIDENCE-001"),
                "next_sequence": 3,
                "last_admitted_tick": 10,
            },
            "must not contain duplicates",
        ),
        (
            {
                "admitted_evidence_ids": ("EVIDENCE-001",),
                "next_sequence": 1,
                "last_admitted_tick": 10,
            },
            "next_sequence must equal admitted evidence count plus one",
        ),
        (
            {"admitted_evidence_ids": ("EVIDENCE-001",), "next_sequence": 2},
            "last_admitted_tick is required",
        ),
        ({"last_admitted_tick": 10}, "last_admitted_tick must be null"),
    ],
)
def test_channel_runtime_state_rejects_inconsistent_state(
    changes: dict[str, object],
    message: str,
) -> None:
    with pytest.raises(ChannelError, match=message):
        replace(create_channel_state(_definition()), **changes)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("evidence_id", "bad-id", "uppercase identifier characters"),
        ("evidence_id", "EVIDENCE-HIDDEN-001", "validator-reserved token"),
        ("channel_id", "channel", "uppercase identifier characters"),
        ("source_id", "SOURCE-SCENARIO", "validator-reserved token"),
        ("validator_event_id", "bad-event", "uppercase identifier characters"),
        ("observed_at_tick", True, "observed_at_tick must be an integer"),
        ("observed_at_tick", -1, "observed_at_tick must be between"),
        ("submitted_at_tick", MAX_TICK + 1, "submitted_at_tick must be between"),
        ("claim", "claim", "claim must be an EvidenceClaim"),
    ],
)
def test_evidence_submission_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    with pytest.raises(ChannelError, match=message):
        replace(_submission(), **{field: value})


def test_evidence_submission_accepts_tick_boundaries() -> None:
    submission = _submission(observed_at_tick=0, submitted_at_tick=MAX_TICK)

    assert submission.observed_at_tick == 0
    assert submission.submitted_at_tick == MAX_TICK


def test_evidence_submission_rejects_observation_from_the_future() -> None:
    with pytest.raises(ChannelError, match="observed_at_tick must not exceed"):
        _submission(observed_at_tick=11, submitted_at_tick=10)


def test_closed_channel_blocks_submission_without_mutating_state() -> None:
    definition = _definition()
    state = create_channel_state(definition)

    result = route_submission(definition, state, _submission())

    assert result.status is RoutingStatus.BLOCKED
    assert result.reason is RoutingReason.CHANNEL_CLOSED
    assert result.admitted is False
    assert result.packet is None
    assert result.state is state


def test_open_channel_admits_explicit_evidence_with_provenance() -> None:
    definition = _definition(kind=ChannelKind.DIRECT_OBSERVATION)
    initial = create_channel_state(definition, gate=ChannelGateState.OPEN)
    submission = _submission(
        validator_event_id="AURORA-SCN-FOUND-001-E99",
        observed_at_tick=8,
        submitted_at_tick=10,
        claim=_claim({"zone": "platform-2", "confidence": 0.8}),
    )

    result = route_submission(definition, initial, submission)

    assert result.status is RoutingStatus.ADMITTED
    assert result.reason is RoutingReason.ADMITTED
    assert result.admitted is True
    assert result.packet is not None
    assert result.packet.evidence_id == submission.evidence_id
    assert result.packet.channel_id == definition.channel_id
    assert result.packet.channel_kind is ChannelKind.DIRECT_OBSERVATION
    assert result.packet.source_id == definition.source_id
    assert result.packet.observed_at_tick == 8
    assert result.packet.admitted_at_tick == 10
    assert result.packet.sequence == 1
    assert result.packet.claim is submission.claim
    assert result.state == ChannelRuntimeState(
        channel_id=_CHANNEL_ID,
        gate=ChannelGateState.OPEN,
        next_sequence=2,
        last_admitted_tick=10,
        admitted_evidence_ids=("EVIDENCE-001",),
    )


def test_aurora_packet_mapping_excludes_validator_only_metadata() -> None:
    result = _route_admitted(
        submission=_submission(validator_event_id="AURORA-SCN-FOUND-001-SECRET-E1")
    )
    assert result.packet is not None

    mapping = result.packet.to_mapping()
    serialized = json.dumps(mapping, sort_keys=True)

    assert mapping == {
        "admitted_at_tick": 10,
        "channel_id": _CHANNEL_ID,
        "channel_kind": "SENSOR",
        "claim": _claim().to_mapping(),
        "evidence_id": "EVIDENCE-001",
        "observed_at_tick": 10,
        "sequence": 1,
        "source_id": _SOURCE_ID,
    }
    assert "validator_event_id" not in serialized
    assert "SECRET" not in serialized
    assert "scenario" not in serialized.casefold()


def test_packet_hash_is_deterministic_and_sensitive_to_visible_evidence() -> None:
    first = _route_admitted().packet
    second = _route_admitted().packet
    changed = _route_admitted(submission=_submission(claim=_claim("platform-7"))).packet
    assert first is not None
    assert second is not None
    assert changed is not None

    assert first.packet_sha256 == second.packet_sha256
    assert first.packet_sha256 != changed.packet_sha256
    assert len(first.packet_sha256) == 64


def test_successive_admissions_receive_deterministic_sequences() -> None:
    definition = _definition()
    initial = create_channel_state(definition, gate=ChannelGateState.OPEN)
    first = route_submission(definition, initial, _submission())
    second = route_submission(
        definition,
        first.state,
        _submission(
            evidence_id="EVIDENCE-002",
            observed_at_tick=11,
            submitted_at_tick=12,
        ),
    )
    assert first.packet is not None
    assert second.packet is not None

    assert (first.packet.sequence, second.packet.sequence) == (1, 2)
    assert second.state.next_sequence == 3
    assert second.state.admitted_evidence_ids == ("EVIDENCE-001", "EVIDENCE-002")
    assert second.state.last_admitted_tick == 12


def test_same_submission_tick_is_allowed_and_preserves_input_order() -> None:
    definition = _definition()
    first = _route_admitted(definition=definition)
    second = route_submission(
        definition,
        first.state,
        _submission(evidence_id="EVIDENCE-002"),
    )
    assert second.packet is not None

    assert second.packet.sequence == 2
    assert second.packet.admitted_at_tick == first.packet.admitted_at_tick


@pytest.mark.parametrize(
    ("changes", "reason"),
    [
        ({"channel_id": "CH-OTHER-LOC"}, RoutingReason.CHANNEL_ID_MISMATCH),
        ({"source_id": "OTHER-LOC-SYSTEM"}, RoutingReason.SOURCE_ID_MISMATCH),
    ],
)
def test_routing_blocks_channel_or_source_mismatch_before_admission(
    changes: dict[str, object],
    reason: RoutingReason,
) -> None:
    definition = _definition()
    state = create_channel_state(definition, gate=ChannelGateState.OPEN)

    result = route_submission(definition, state, replace(_submission(), **changes))

    assert result.reason is reason
    assert result.status is RoutingStatus.BLOCKED
    assert result.packet is None
    assert result.state is state


def test_routing_mismatch_precedes_closed_gate_decision() -> None:
    definition = _definition()
    state = create_channel_state(definition)
    mismatched = replace(
        _submission(),
        channel_id="CH-OTHER-LOC",
        source_id="OTHER-LOC-SYSTEM",
    )

    result = route_submission(definition, state, mismatched)

    assert result.reason is RoutingReason.CHANNEL_ID_MISMATCH


def test_duplicate_evidence_is_blocked_without_state_change() -> None:
    definition = _definition()
    admitted = _route_admitted(definition=definition)

    duplicate = route_submission(
        definition,
        admitted.state,
        _submission(observed_at_tick=11, submitted_at_tick=11),
    )

    assert duplicate.reason is RoutingReason.DUPLICATE_EVIDENCE_ID
    assert duplicate.state is admitted.state


def test_duplicate_decision_precedes_out_of_order_decision() -> None:
    definition = _definition()
    admitted = _route_admitted(
        definition=definition,
        submission=_submission(observed_at_tick=10, submitted_at_tick=10),
    )

    duplicate = route_submission(
        definition,
        admitted.state,
        _submission(observed_at_tick=5, submitted_at_tick=5),
    )

    assert duplicate.reason is RoutingReason.DUPLICATE_EVIDENCE_ID


def test_out_of_order_submission_is_blocked_without_state_change() -> None:
    definition = _definition()
    admitted = _route_admitted(
        definition=definition,
        submission=_submission(observed_at_tick=10, submitted_at_tick=12),
    )

    result = route_submission(
        definition,
        admitted.state,
        _submission(
            evidence_id="EVIDENCE-002",
            observed_at_tick=11,
            submitted_at_tick=11,
        ),
    )

    assert result.reason is RoutingReason.OUT_OF_ORDER_SUBMISSION
    assert result.state is admitted.state


def test_claim_size_limit_is_inclusive() -> None:
    claim = _claim("x")
    definition = _definition(max_claim_bytes=claim.size_bytes)
    state = create_channel_state(definition, gate=ChannelGateState.OPEN)

    result = route_submission(definition, state, _submission(claim=claim))

    assert result.admitted is True


def test_oversized_claim_is_blocked_without_state_change() -> None:
    claim = _claim("oversized")
    definition = _definition(max_claim_bytes=claim.size_bytes - 1)
    state = create_channel_state(definition, gate=ChannelGateState.OPEN)

    result = route_submission(definition, state, _submission(claim=claim))

    assert result.reason is RoutingReason.CLAIM_TOO_LARGE
    assert result.packet is None
    assert result.state is state


def test_route_submission_rejects_invalid_runtime_arguments() -> None:
    definition = _definition()
    state = create_channel_state(definition)

    with pytest.raises(ChannelError, match="definition must be a ChannelDefinition"):
        route_submission("definition", state, _submission())
    with pytest.raises(ChannelError, match="state must be a ChannelRuntimeState"):
        route_submission(definition, "state", _submission())
    with pytest.raises(ChannelError, match="does not match channel definition"):
        route_submission(
            definition,
            create_channel_state(_definition(channel_id="CH-OTHER-LOC")),
            _submission(),
        )
    with pytest.raises(ChannelError, match="submission must be an EvidenceSubmission"):
        route_submission(definition, state, "submission")


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("channel_kind", "SENSOR", "channel_kind must be a ChannelKind"),
        ("observed_at_tick", True, "observed_at_tick must be an integer"),
        ("admitted_at_tick", -1, "admitted_at_tick must be between"),
        ("sequence", True, "sequence must be an integer"),
        ("sequence", 0, "sequence must be positive"),
        ("claim", "claim", "claim must be an EvidenceClaim"),
    ],
)
def test_aurora_packet_direct_constructor_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    packet = _route_admitted().packet
    assert packet is not None

    with pytest.raises(ChannelError, match=message):
        replace(packet, **{field: value})


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("evidence_id", "bad-id"),
        ("channel_id", "BAD CHANNEL"),
        ("source_id", "SOURCE-EXPECTED"),
    ],
)
def test_aurora_packet_revalidates_runtime_identifiers(field: str, value: str) -> None:
    packet = _route_admitted().packet
    assert packet is not None

    with pytest.raises(ChannelError):
        replace(packet, **{field: value})


def test_aurora_packet_rejects_observation_after_admission() -> None:
    packet = _route_admitted().packet
    assert packet is not None

    with pytest.raises(ChannelError, match="observed_at_tick must not exceed"):
        replace(packet, observed_at_tick=11, admitted_at_tick=10)


def test_routing_result_direct_constructor_enforces_result_contract() -> None:
    admitted = _route_admitted()
    assert admitted.packet is not None
    blocked = route_submission(_definition(), create_channel_state(_definition()), _submission())

    with pytest.raises(ChannelError, match="status must be a RoutingStatus"):
        replace(admitted, status="ADMITTED")
    with pytest.raises(ChannelError, match="reason must be a RoutingReason"):
        replace(admitted, reason="ADMITTED")
    with pytest.raises(ChannelError, match="state must be a ChannelRuntimeState"):
        replace(admitted, state="state")
    with pytest.raises(ChannelError, match="packet must be null or an AuroraEvidencePacket"):
        replace(admitted, packet="packet")
    with pytest.raises(ChannelError, match="requires admitted reason and packet"):
        replace(admitted, reason=RoutingReason.CHANNEL_CLOSED)
    with pytest.raises(ChannelError, match="requires admitted reason and packet"):
        replace(admitted, packet=None)
    with pytest.raises(ChannelError, match="blocked result requires"):
        replace(blocked, reason=RoutingReason.ADMITTED)
    with pytest.raises(ChannelError, match="blocked result requires"):
        replace(blocked, packet=admitted.packet)


def test_routing_result_rejects_packet_state_channel_mismatch() -> None:
    admitted = _route_admitted()
    assert admitted.packet is not None
    other_state = ChannelRuntimeState(
        channel_id="CH-OTHER-LOC",
        gate=ChannelGateState.OPEN,
        next_sequence=2,
        last_admitted_tick=10,
        admitted_evidence_ids=("EVIDENCE-001",),
    )

    with pytest.raises(ChannelError, match="packet channel does not match"):
        replace(admitted, state=other_state)


def test_routing_result_rejects_packet_state_sequence_mismatch() -> None:
    admitted = _route_admitted()
    assert admitted.packet is not None
    state = ChannelRuntimeState(
        channel_id=_CHANNEL_ID,
        gate=ChannelGateState.OPEN,
        next_sequence=3,
        last_admitted_tick=10,
        admitted_evidence_ids=("EVIDENCE-001", "EVIDENCE-002"),
    )

    with pytest.raises(ChannelError, match="packet sequence does not match"):
        replace(admitted, state=state)


def test_routing_result_rejects_unrecorded_packet() -> None:
    admitted = _route_admitted()
    assert admitted.packet is not None

    with pytest.raises(ChannelError, match="packet is not recorded"):
        replace(admitted, packet=replace(admitted.packet, evidence_id="EVIDENCE-999"))


def test_routing_result_rejects_packet_tick_mismatch() -> None:
    admitted = _route_admitted()
    changed_state = replace(admitted.state, last_admitted_tick=11)

    with pytest.raises(ChannelError, match="packet tick does not match"):
        replace(admitted, state=changed_state)


def test_channel_model_values_are_immutable() -> None:
    claim = _claim()
    definition = _definition()
    state = create_channel_state(definition)
    submission = _submission()
    admitted = _route_admitted()
    assert admitted.packet is not None

    mutations = (
        (claim, "subject_id", "Nora"),
        (definition, "channel_id", "CH-OTHER-LOC"),
        (state, "gate", ChannelGateState.OPEN),
        (submission, "evidence_id", "EVIDENCE-002"),
        (admitted.packet, "evidence_id", "EVIDENCE-002"),
        (admitted, "status", RoutingStatus.BLOCKED),
    )
    for value, field, replacement_value in mutations:
        with pytest.raises(FrozenInstanceError):
            setattr(value, field, replacement_value)


def test_channel_module_exports_complete_public_contract() -> None:
    assert set(channels_module.__all__) == {
        "DEFAULT_MAX_CLAIM_BYTES",
        "MAX_CLAIM_BYTES",
        "MAX_TICK",
        "AuroraEvidencePacket",
        "ChannelDefinition",
        "ChannelError",
        "ChannelGateState",
        "ChannelKind",
        "ChannelRoutingResult",
        "ChannelRuntimeState",
        "EvidenceClaim",
        "EvidenceSubmission",
        "RoutingReason",
        "RoutingStatus",
        "create_channel_state",
        "create_evidence_claim",
        "route_submission",
        "set_channel_gate",
    }
