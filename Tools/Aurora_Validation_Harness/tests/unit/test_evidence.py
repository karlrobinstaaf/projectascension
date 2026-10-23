"""Unit tests for append-only validation evidence and finalized packages."""

from __future__ import annotations

import copy
import hashlib
from dataclasses import FrozenInstanceError, replace
from types import MappingProxyType

import pytest

from aurora_validation_harness import evidence as evidence_module
from aurora_validation_harness.evidence import (
    DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES,
    MAX_EVIDENCE_PAYLOAD_BYTES,
    MAX_TICK,
    SUPPORTED_EVIDENCE_SCHEMA_VERSION,
    EvidenceDomain,
    EvidenceError,
    EvidenceKind,
    EvidenceLedger,
    EvidencePayload,
    EvidenceRecord,
    EvidenceSource,
    EvidenceSourceKind,
    FinalizedEvidencePackage,
    append_evidence_record,
    calculate_evidence_ledger_sha256,
    calculate_evidence_package_sha256,
    create_evidence_ledger,
    create_evidence_payload,
    create_record_source,
    finalize_evidence_ledger,
)

pytestmark = [pytest.mark.foundation, pytest.mark.isolation]

_RUN_ID = "AURORA-RUN-FOUND-001-001"
_SCENARIO_ID = "AURORA-SCN-FOUND-001"


def _payload(data: dict[str, object] | None = None) -> EvidencePayload:
    return create_evidence_payload({"status": "captured", "value": 1} if data is None else data)


def _source(
    *,
    kind: EvidenceSourceKind = EvidenceSourceKind.EXTERNAL,
    source_id: str = "SOURCE-001",
    digest: str = "a" * 64,
) -> EvidenceSource:
    return EvidenceSource(
        source_kind=kind,
        source_id=source_id,
        source_sha256=digest,
    )


def _record(
    *,
    record_id: str = "EVIDENCE-RECORD-000",
    run_id: str = _RUN_ID,
    scenario_id: str = _SCENARIO_ID,
    sequence: int = 0,
    observed_at_tick: int = 0,
    recorded_at_tick: int = 0,
    kind: EvidenceKind = EvidenceKind.RUN_CONFIGURATION,
    domain: EvidenceDomain = EvidenceDomain.RUN_CONTROL,
    producer_id: str = "HARNESS-RUNTIME",
    payload: EvidencePayload | None = None,
    sources: tuple[EvidenceSource, ...] = (),
    previous_record_sha256: str | None = None,
) -> EvidenceRecord:
    if sequence > 0 and previous_record_sha256 is None:
        previous_record_sha256 = "b" * 64
    return EvidenceRecord(
        record_id=record_id,
        run_id=run_id,
        scenario_id=scenario_id,
        sequence=sequence,
        observed_at_tick=observed_at_tick,
        recorded_at_tick=recorded_at_tick,
        kind=kind,
        domain=domain,
        producer_id=producer_id,
        payload=_payload() if payload is None else payload,
        sources=sources,
        previous_record_sha256=previous_record_sha256,
    )


def _append(
    ledger: EvidenceLedger,
    index: int,
    *,
    observed_at_tick: int | None = None,
    recorded_at_tick: int | None = None,
    kind: EvidenceKind = EvidenceKind.DIAGNOSTIC,
    domain: EvidenceDomain = EvidenceDomain.VALIDATOR,
    producer_id: str = "HARNESS-RUNTIME",
    payload: EvidencePayload | None = None,
    sources: tuple[EvidenceSource, ...] = (),
) -> EvidenceLedger:
    tick = index if recorded_at_tick is None else recorded_at_tick
    observed = tick if observed_at_tick is None else observed_at_tick
    return append_evidence_record(
        ledger,
        record_id=f"EVIDENCE-RECORD-{index:03d}",
        observed_at_tick=observed,
        recorded_at_tick=tick,
        kind=kind,
        domain=domain,
        producer_id=producer_id,
        payload=_payload() if payload is None else payload,
        sources=sources,
    )


def _ledger(record_count: int = 3) -> EvidenceLedger:
    ledger = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)
    for index in range(record_count):
        sources: tuple[EvidenceSource, ...]
        if index == 0:
            sources = (
                _source(
                    kind=EvidenceSourceKind.CONFIGURATION,
                    source_id="AURORA-CONFIG-FOUND-001",
                ),
            )
        else:
            sources = (create_record_source(ledger.records[-1]),)
        ledger = _append(ledger, index, sources=sources)
    return ledger


def _package(record_count: int = 3, *, finalized_at_tick: int = 10) -> FinalizedEvidencePackage:
    return finalize_evidence_ledger(
        _ledger(record_count),
        finalized_at_tick=finalized_at_tick,
    )


def _raw_payload(payload_json: bytes, *, digest: object | None = None) -> EvidencePayload:
    return EvidencePayload(
        payload_json=payload_json,
        payload_sha256=(hashlib.sha256(payload_json).hexdigest() if digest is None else digest),
    )


def test_public_constants_define_schema_and_bounded_limits() -> None:
    assert SUPPORTED_EVIDENCE_SCHEMA_VERSION == "1.0"
    assert DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES == 1_048_576
    assert MAX_EVIDENCE_PAYLOAD_BYTES == 4_194_304
    assert MAX_TICK == (1 << 63) - 1
    assert 0 < DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES < MAX_EVIDENCE_PAYLOAD_BYTES < MAX_TICK


def test_evidence_enums_have_stable_contract_values() -> None:
    assert {value.value for value in EvidenceDomain} == {
        "RUN_CONTROL",
        "WORLD",
        "PLAYER_PRIVATE",
        "FUTURE",
        "AURORA_ACCESSIBLE",
        "AURORA_STATE",
        "EXPECTED_RESULTS",
        "VALIDATOR",
        "INFRASTRUCTURE",
    }
    assert {value.value for value in EvidenceKind} == {
        "RUN_CONFIGURATION",
        "BASELINE_VERIFICATION",
        "FIXTURE_INTEGRITY",
        "EVENT_RELEASE",
        "CHANNEL_ADMISSION",
        "AURORA_INPUT",
        "STATE_SNAPSHOT",
        "STATE_TRANSITION",
        "ASSERTION_RESULT",
        "WORLD_CONSEQUENCE",
        "DIAGNOSTIC",
        "VERDICT",
    }
    assert {value.value for value in EvidenceSourceKind} == {
        "BASELINE",
        "CONFIGURATION",
        "FIXTURE",
        "EVENT",
        "CHANNEL_PACKET",
        "SNAPSHOT",
        "TRANSITION",
        "ASSERTION",
        "RECORD",
        "EXTERNAL",
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
def test_evidence_payload_accepts_supported_nested_json_values(value: object) -> None:
    payload = create_evidence_payload({"value": value})

    assert payload.decode() == {"value": value}
    assert payload.size_bytes == len(payload.payload_json)
    assert payload.payload_sha256 == hashlib.sha256(payload.payload_json).hexdigest()
    assert payload.to_mapping() == {
        "data": {"value": value},
        "payload_sha256": payload.payload_sha256,
    }


def test_evidence_payload_normalizes_generic_mappings_unicode_and_key_order() -> None:
    first = create_evidence_payload(
        MappingProxyType(
            {
                "zone": "Café",
                "nested": MappingProxyType({"b": 2, "a": 1}),
            }
        )
    )
    second = create_evidence_payload({"nested": {"a": 1, "b": 2}, "zone": "Café"})

    assert first == second
    assert first.payload_json == '{"nested":{"a":1,"b":2},"zone":"Café"}'.encode()


def test_decoded_evidence_payload_is_a_fresh_copy() -> None:
    payload = create_evidence_payload({"locations": ["platform-2"]})
    decoded = payload.decode()
    locations = decoded["locations"]
    assert isinstance(locations, list)

    locations.append("tampered")

    assert payload.decode() == {"locations": ["platform-2"]}


def test_evidence_payload_accepts_exact_declared_size_limit() -> None:
    payload = create_evidence_payload({"value": "x"})

    recreated = create_evidence_payload(
        {"value": "x"},
        max_payload_bytes=payload.size_bytes,
    )

    assert recreated == payload


def test_evidence_payload_rejects_declared_size_limit_overflow() -> None:
    payload = create_evidence_payload({"value": "x"})

    with pytest.raises(EvidenceError, match="evidence payload must not exceed"):
        create_evidence_payload(
            {"value": "x"},
            max_payload_bytes=payload.size_bytes - 1,
        )


def test_evidence_payload_can_explicitly_opt_in_above_default_limit() -> None:
    data = {"value": "x" * DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES}

    with pytest.raises(EvidenceError, match="evidence payload must not exceed"):
        create_evidence_payload(data)

    payload = create_evidence_payload(
        data,
        max_payload_bytes=MAX_EVIDENCE_PAYLOAD_BYTES,
    )
    assert DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES < payload.size_bytes < MAX_EVIDENCE_PAYLOAD_BYTES


@pytest.mark.parametrize("max_payload_bytes", [True, "1024", 1.5])
def test_evidence_payload_rejects_non_integer_size_limit(max_payload_bytes: object) -> None:
    with pytest.raises(EvidenceError, match="max_payload_bytes must be an integer"):
        create_evidence_payload({}, max_payload_bytes=max_payload_bytes)


@pytest.mark.parametrize("max_payload_bytes", [0, -1, MAX_EVIDENCE_PAYLOAD_BYTES + 1])
def test_evidence_payload_rejects_out_of_range_size_limit(max_payload_bytes: int) -> None:
    with pytest.raises(EvidenceError, match="max_payload_bytes must be between"):
        create_evidence_payload({}, max_payload_bytes=max_payload_bytes)


@pytest.mark.parametrize("data", [None, [], "payload", 7])
def test_evidence_payload_requires_a_json_object(data: object) -> None:
    with pytest.raises(EvidenceError, match="evidence payload data must be a JSON object"):
        create_evidence_payload(data)


@pytest.mark.parametrize("data", [{1: "non-string"}, {"tuple": (1,)}, {"set": {1}}])
def test_evidence_payload_rejects_non_json_shapes(data: object) -> None:
    with pytest.raises(EvidenceError, match=r"non-string object key|unsupported JSON value type"):
        create_evidence_payload(data)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_evidence_payload_rejects_non_finite_numbers(value: float) -> None:
    with pytest.raises(EvidenceError, match="contains a non-finite number"):
        create_evidence_payload({"confidence": value})


def test_evidence_payload_direct_constructor_checks_bytes_and_digest() -> None:
    valid = _payload()

    with pytest.raises(EvidenceError, match="payload_json must be bytes"):
        replace(valid, payload_json="not-bytes")
    with pytest.raises(EvidenceError, match="payload_sha256 must be a string"):
        replace(valid, payload_sha256=7)
    with pytest.raises(EvidenceError, match="lowercase 64-character SHA-256"):
        replace(valid, payload_sha256="A" * 64)
    with pytest.raises(EvidenceError, match="does not match payload_json"):
        replace(valid, payload_sha256="0" * 64)


def test_evidence_payload_direct_constructor_enforces_absolute_size_limit() -> None:
    payload_json = b"x" * (MAX_EVIDENCE_PAYLOAD_BYTES + 1)

    with pytest.raises(EvidenceError, match="payload_json must not exceed"):
        _raw_payload(payload_json)


@pytest.mark.parametrize(
    ("payload_json", "message"),
    [
        (b"\xff", "payload_json is not valid JSON"),
        (b"{broken", "payload_json is not valid JSON"),
        (b'{"value":NaN}', "non-finite JSON value is not allowed"),
        (b"[]", "payload_json must encode a JSON object"),
        (b"null", "payload_json must encode a JSON object"),
    ],
)
def test_evidence_payload_direct_constructor_rejects_invalid_json(
    payload_json: bytes,
    message: str,
) -> None:
    with pytest.raises(EvidenceError, match=message):
        _raw_payload(payload_json)


def test_evidence_payload_direct_constructor_rejects_noncanonical_json() -> None:
    with pytest.raises(EvidenceError, match="payload_json must use canonical JSON encoding"):
        _raw_payload(b'{"zone": "platform-2"}')


def test_evidence_payload_round_trips_through_mapping() -> None:
    payload = _payload({"location": "Cargo_Bay_7"})

    reconstructed = EvidencePayload.from_mapping(payload.to_mapping())

    assert reconstructed == payload


def test_evidence_payload_mapping_requires_exact_schema() -> None:
    mapping = _payload().to_mapping()

    with pytest.raises(EvidenceError, match="payload must be a JSON object"):
        EvidencePayload.from_mapping([])
    with pytest.raises(EvidenceError, match="payload must use string keys"):
        EvidencePayload.from_mapping({1: "value"})

    missing = dict(mapping)
    del missing["data"]
    with pytest.raises(EvidenceError, match="missing required field"):
        EvidencePayload.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(EvidenceError, match="contains unknown field"):
        EvidencePayload.from_mapping(unknown)


def test_evidence_payload_mapping_rejects_invalid_data_or_digest() -> None:
    mapping = _payload().to_mapping()

    invalid_data = dict(mapping)
    invalid_data["data"] = []
    with pytest.raises(EvidenceError, match=r"payload.data must be a JSON object"):
        EvidencePayload.from_mapping(invalid_data)

    invalid_digest_type = dict(mapping)
    invalid_digest_type["payload_sha256"] = 7
    with pytest.raises(EvidenceError, match="must be a string"):
        EvidencePayload.from_mapping(invalid_digest_type)

    wrong_digest = dict(mapping)
    wrong_digest["payload_sha256"] = "0" * 64
    with pytest.raises(EvidenceError, match="declared payload_sha256 does not match"):
        EvidencePayload.from_mapping(wrong_digest)


def test_canonical_json_helper_translates_serialization_errors() -> None:
    with pytest.raises(EvidenceError, match="value is not JSON-serializable"):
        evidence_module._canonical_json_bytes({"unsupported": object()})


def test_payload_factory_defensively_rechecks_normalized_root(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(evidence_module, "_normalize_json_value", lambda *_args, **_kwargs: [])

    with pytest.raises(EvidenceError, match="evidence payload data must be a JSON object"):
        create_evidence_payload({})


def test_normalization_helper_defensively_rejects_unhandled_value(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(evidence_module, "_validate_json_value", lambda *_args, **_kwargs: None)

    with pytest.raises(EvidenceError, match="unsupported JSON value type"):
        evidence_module._normalize_json_value(object(), path="payload")


@pytest.mark.parametrize("source_kind", list(EvidenceSourceKind))
def test_evidence_source_accepts_every_provenance_kind(
    source_kind: EvidenceSourceKind,
) -> None:
    source = _source(kind=source_kind)

    assert source.source_kind is source_kind
    assert EvidenceSource.from_mapping(source.to_mapping()) == source


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("source_kind", "EXTERNAL", "must be an EvidenceSourceKind"),
        ("source_id", "bad-id", "uppercase identifier characters"),
        ("source_id", 7, "source_id must be a string"),
        ("source_sha256", 7, "source_sha256 must be a string"),
        ("source_sha256", "A" * 64, "lowercase 64-character SHA-256"),
    ],
)
def test_evidence_source_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    with pytest.raises(EvidenceError, match=message):
        replace(_source(), **{field: value})


def test_evidence_source_mapping_requires_exact_schema() -> None:
    mapping = _source().to_mapping()

    with pytest.raises(EvidenceError, match="source must be a JSON object"):
        EvidenceSource.from_mapping([])

    missing = dict(mapping)
    del missing["source_id"]
    with pytest.raises(EvidenceError, match="missing required field"):
        EvidenceSource.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(EvidenceError, match="contains unknown field"):
        EvidenceSource.from_mapping(unknown)


def test_evidence_source_mapping_rejects_invalid_enum_and_scalar_types() -> None:
    mapping = _source().to_mapping()

    unsupported_kind = dict(mapping)
    unsupported_kind["source_kind"] = "UNKNOWN"
    with pytest.raises(EvidenceError, match=r"unsupported source.source_kind"):
        EvidenceSource.from_mapping(unsupported_kind)

    non_string_kind = dict(mapping)
    non_string_kind["source_kind"] = 4
    with pytest.raises(EvidenceError, match=r"source.source_kind must be a string"):
        EvidenceSource.from_mapping(non_string_kind)

    non_string_id = dict(mapping)
    non_string_id["source_id"] = 4
    with pytest.raises(EvidenceError, match=r"source.source_id must be a string"):
        EvidenceSource.from_mapping(non_string_id)

    non_string_digest = dict(mapping)
    non_string_digest["source_sha256"] = None
    with pytest.raises(EvidenceError, match=r"source.source_sha256 must be a string"):
        EvidenceSource.from_mapping(non_string_digest)


@pytest.mark.parametrize("kind", list(EvidenceKind))
def test_evidence_record_accepts_every_kind(kind: EvidenceKind) -> None:
    assert replace(_record(), kind=kind).kind is kind


@pytest.mark.parametrize("domain", list(EvidenceDomain))
def test_evidence_record_accepts_every_domain(domain: EvidenceDomain) -> None:
    payload = (
        _payload({"visible": "safe"})
        if domain is EvidenceDomain.AURORA_ACCESSIBLE
        else _payload({"world_truth": "allowed outside accessible domain"})
    )

    assert replace(_record(), domain=domain, payload=payload).domain is domain


def test_evidence_record_supports_late_observation_capture() -> None:
    record = _record(observed_at_tick=2, recorded_at_tick=10)

    assert record.observed_at_tick == 2
    assert record.recorded_at_tick == 10


def test_evidence_record_mapping_and_hash_are_stable() -> None:
    record = _record(sources=(_source(),))
    mapping = record.to_validator_mapping()

    assert EvidenceRecord.from_mapping(mapping) == record
    assert mapping["record_sha256"] == record.record_sha256
    assert len(record.record_sha256) == 64
    assert record.record_sha256 == _record(sources=(_source(),)).record_sha256


def test_evidence_record_hash_changes_with_content_or_chain() -> None:
    original = _record()
    changed_payload = replace(original, payload=_payload({"status": "changed"}))
    chained = _record(
        record_id="EVIDENCE-RECORD-001",
        sequence=1,
        previous_record_sha256=original.record_sha256,
    )

    assert original.record_sha256 != changed_payload.record_sha256
    assert original.record_sha256 != chained.record_sha256


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("record_id", "bad-id", "uppercase identifier characters"),
        ("record_id", 7, "record_id must be a string"),
        ("run_id", "bad-run", "uppercase identifier characters"),
        ("run_id", None, "run_id must be a string"),
        ("scenario_id", "AURORA-FOUND-001", "scenario_id must match"),
        ("scenario_id", 7, "scenario_id must be a string"),
        ("sequence", True, "sequence must be an integer"),
        ("sequence", 1.5, "sequence must be an integer"),
        ("sequence", -1, "sequence must be non-negative"),
        ("observed_at_tick", True, "observed_at_tick must be an integer"),
        ("observed_at_tick", -1, "observed_at_tick must be between"),
        ("recorded_at_tick", MAX_TICK + 1, "recorded_at_tick must be between"),
        ("kind", "DIAGNOSTIC", "kind must be an EvidenceKind"),
        ("domain", "VALIDATOR", "domain must be an EvidenceDomain"),
        ("producer_id", "bad-producer", "uppercase identifier characters"),
        ("producer_id", 7, "producer_id must be a string"),
        ("payload", {}, "payload must be an EvidencePayload"),
        ("sources", [], "sources must be a tuple"),
        ("sources", ("source",), "sources must be a tuple"),
    ],
)
def test_evidence_record_rejects_invalid_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    with pytest.raises(EvidenceError, match=message):
        replace(_record(), **{field: value})


def test_evidence_record_rejects_observation_after_capture() -> None:
    with pytest.raises(EvidenceError, match="observed_at_tick must not exceed"):
        _record(observed_at_tick=11, recorded_at_tick=10)


def test_evidence_record_rejects_duplicate_source_kind_and_id() -> None:
    first = _source(digest="a" * 64)
    conflicting = _source(digest="b" * 64)

    with pytest.raises(EvidenceError, match="duplicate kind and ID pairs"):
        _record(sources=(first, conflicting))


def test_evidence_record_rejects_invalid_previous_hash() -> None:
    with pytest.raises(EvidenceError, match="lowercase 64-character SHA-256"):
        _record(sequence=1, previous_record_sha256="A" * 64)
    with pytest.raises(EvidenceError, match="previous_record_sha256 must be a string"):
        replace(_record(), sequence=1, previous_record_sha256=7)


def test_evidence_record_enforces_first_and_nonfirst_chain_shape() -> None:
    with pytest.raises(EvidenceError, match="first evidence record must not declare"):
        _record(sequence=0, previous_record_sha256="a" * 64)

    first = _record()
    with pytest.raises(EvidenceError, match="non-first evidence record requires"):
        replace(first, sequence=1, previous_record_sha256=None)


@pytest.mark.parametrize(
    "forbidden_key",
    [
        "expected_answer",
        "Expected Interpretation",
        "EXPECTED-RESULT",
        "failure.conditions",
        "fixture_manifest_sha256",
        "fixture set id",
        "future-event-queue",
        "hidden from Aurora",
        "hidden_state_marker",
        "player private",
        "scenario_id",
        "scenario name",
        "validator.metadata",
        "validator_notes",
        "world-debug-state",
        "world truth",
    ],
)
def test_aurora_accessible_record_recursively_rejects_forbidden_fields(
    forbidden_key: str,
) -> None:
    payload = _payload({"packet": [{"claim": {forbidden_key: "private"}}]})

    with pytest.raises(EvidenceError, match="forbidden in AURORA_ACCESSIBLE"):
        _record(domain=EvidenceDomain.AURORA_ACCESSIBLE, payload=payload)


def test_aurora_accessible_record_accepts_channel_shaped_payload() -> None:
    payload = _payload(
        {
            "channel_id": "CH-STATION-LOC",
            "claim": {
                "predicate": "current_location",
                "qualifiers": ["observed", {"confidence": "high"}],
                "subject_id": "Mara",
                "value": "Cargo_Bay_7",
            },
            "evidence_id": "EVIDENCE-001",
            "sequence": 1,
        }
    )

    record = _record(
        kind=EvidenceKind.AURORA_INPUT,
        domain=EvidenceDomain.AURORA_ACCESSIBLE,
        payload=payload,
    )

    assert record.payload is payload


@pytest.mark.parametrize(
    "domain",
    [domain for domain in EvidenceDomain if domain is not EvidenceDomain.AURORA_ACCESSIBLE],
)
def test_validator_owned_domains_can_capture_sensitive_audit_fields(
    domain: EvidenceDomain,
) -> None:
    payload = _payload(
        {
            "expected_result": "UNKNOWN",
            "future_event_queue": [],
            "world_truth": {"location": "Cargo_Bay_7"},
        }
    )

    assert _record(domain=domain, payload=payload).payload is payload


def test_evidence_record_mapping_requires_exact_schema() -> None:
    mapping = _record().to_validator_mapping()

    with pytest.raises(EvidenceError, match="evidence record must be a JSON object"):
        EvidenceRecord.from_mapping([])

    missing = dict(mapping)
    del missing["producer_id"]
    with pytest.raises(EvidenceError, match="missing required field"):
        EvidenceRecord.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(EvidenceError, match="contains unknown field"):
        EvidenceRecord.from_mapping(unknown)


def test_evidence_record_mapping_rejects_invalid_collection_shapes() -> None:
    mapping = _record().to_validator_mapping()

    invalid_sources = dict(mapping)
    invalid_sources["sources"] = ()
    with pytest.raises(EvidenceError, match="sources must be a JSON array"):
        EvidenceRecord.from_mapping(invalid_sources)

    invalid_source_item = dict(mapping)
    invalid_source_item["sources"] = ["source"]
    with pytest.raises(EvidenceError, match=r"sources\[0\] must be a JSON object"):
        EvidenceRecord.from_mapping(invalid_source_item)

    invalid_payload = dict(mapping)
    invalid_payload["payload"] = []
    with pytest.raises(EvidenceError, match=r"evidence record.payload must be a JSON object"):
        EvidenceRecord.from_mapping(invalid_payload)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("previous_record_sha256", 7, "previous_record_sha256 must be a string"),
        ("record_id", 7, "record_id must be a string"),
        ("run_id", 7, "run_id must be a string"),
        ("scenario_id", 7, "scenario_id must be a string"),
        ("sequence", True, "sequence must be an integer"),
        ("observed_at_tick", "0", "observed_at_tick must be an integer"),
        ("recorded_at_tick", None, "recorded_at_tick must be an integer"),
        ("kind", "UNKNOWN", "unsupported evidence record.kind"),
        ("domain", "UNKNOWN", "unsupported evidence record.domain"),
        ("producer_id", 7, "producer_id must be a string"),
        ("record_sha256", 7, "record_sha256 must be a string"),
    ],
)
def test_evidence_record_mapping_rejects_invalid_scalar_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    mapping = _record().to_validator_mapping()
    mapping[field] = value

    with pytest.raises(EvidenceError, match=message):
        EvidenceRecord.from_mapping(mapping)


def test_evidence_record_mapping_detects_declared_hash_mismatch() -> None:
    mapping = _record().to_validator_mapping()
    mapping["record_sha256"] = "0" * 64

    with pytest.raises(EvidenceError, match="declared record_sha256 does not match"):
        EvidenceRecord.from_mapping(mapping)


def test_create_record_source_binds_record_identity_and_digest() -> None:
    record = _record()

    source = create_record_source(record)

    assert source == EvidenceSource(
        source_kind=EvidenceSourceKind.RECORD,
        source_id=record.record_id,
        source_sha256=record.record_sha256,
    )


def test_create_record_source_rejects_invalid_runtime_type() -> None:
    with pytest.raises(EvidenceError, match="record must be an EvidenceRecord"):
        create_record_source("record")


def test_empty_evidence_ledger_has_stable_identity_and_no_terminal_record() -> None:
    ledger = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)

    assert ledger.records == ()
    assert ledger.terminal_record_sha256 is None
    assert ledger.ledger_sha256 == calculate_evidence_ledger_sha256(ledger)
    assert len(ledger.ledger_sha256) == 64
    assert EvidenceLedger.from_mapping(ledger.to_validator_mapping()) == ledger


def test_append_is_immutable_and_builds_contiguous_hash_chain() -> None:
    empty = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)
    first = _append(empty, 0)
    second = _append(first, 1)

    assert empty.records == ()
    assert len(first.records) == 1
    assert len(second.records) == 2
    assert first.records[0].sequence == 0
    assert first.records[0].previous_record_sha256 is None
    assert second.records[1].sequence == 1
    assert second.records[1].previous_record_sha256 == second.records[0].record_sha256
    assert second.terminal_record_sha256 == second.records[1].record_sha256


def test_append_allows_same_capture_tick_and_late_observation() -> None:
    first = _append(create_evidence_ledger(_RUN_ID, _SCENARIO_ID), 0, recorded_at_tick=10)

    second = _append(
        first,
        1,
        observed_at_tick=2,
        recorded_at_tick=10,
    )

    assert second.records[1].observed_at_tick == 2
    assert second.records[1].recorded_at_tick == 10


def test_append_validates_record_source_against_earlier_ledger_record() -> None:
    first = _append(create_evidence_ledger(_RUN_ID, _SCENARIO_ID), 0)
    source = create_record_source(first.records[0])

    second = _append(first, 1, sources=(source,))

    assert second.records[1].sources == (source,)


def test_append_rejects_invalid_ledger_type() -> None:
    with pytest.raises(EvidenceError, match="ledger must be an EvidenceLedger"):
        append_evidence_record(
            "ledger",
            record_id="EVIDENCE-RECORD-000",
            observed_at_tick=0,
            recorded_at_tick=0,
            kind=EvidenceKind.DIAGNOSTIC,
            domain=EvidenceDomain.VALIDATOR,
            producer_id="HARNESS-RUNTIME",
            payload=_payload(),
        )


def test_append_rejects_duplicate_record_id() -> None:
    first = _append(create_evidence_ledger(_RUN_ID, _SCENARIO_ID), 0)

    with pytest.raises(EvidenceError, match="record_id values must be unique"):
        append_evidence_record(
            first,
            record_id=first.records[0].record_id,
            observed_at_tick=1,
            recorded_at_tick=1,
            kind=EvidenceKind.DIAGNOSTIC,
            domain=EvidenceDomain.VALIDATOR,
            producer_id="HARNESS-RUNTIME",
            payload=_payload(),
        )


def test_append_rejects_recorded_time_regression() -> None:
    first = _append(
        create_evidence_ledger(_RUN_ID, _SCENARIO_ID),
        0,
        observed_at_tick=10,
        recorded_at_tick=10,
    )

    with pytest.raises(EvidenceError, match="nondecreasing recorded_at_tick"):
        _append(first, 1, observed_at_tick=9, recorded_at_tick=9)


def test_ledger_hash_is_deterministic_and_record_sensitive() -> None:
    first = _ledger()
    second = _ledger()
    changed = replace(
        first,
        records=(
            *first.records[:-1],
            replace(first.records[-1], payload=_payload({"status": "changed"})),
        ),
    )

    assert first.ledger_sha256 == second.ledger_sha256
    assert first.ledger_sha256 != changed.ledger_sha256


def test_ledger_rejects_invalid_identity_and_record_collection() -> None:
    with pytest.raises(EvidenceError, match="run_id must be a string"):
        EvidenceLedger(run_id=7, scenario_id=_SCENARIO_ID)
    with pytest.raises(EvidenceError, match="uppercase identifier characters"):
        EvidenceLedger(run_id="bad-run", scenario_id=_SCENARIO_ID)
    with pytest.raises(EvidenceError, match="scenario_id must be a string"):
        EvidenceLedger(run_id=_RUN_ID, scenario_id=7)
    with pytest.raises(EvidenceError, match="scenario_id must match"):
        EvidenceLedger(run_id=_RUN_ID, scenario_id="AURORA-FOUND-001")
    with pytest.raises(EvidenceError, match="records must be a tuple"):
        EvidenceLedger(run_id=_RUN_ID, scenario_id=_SCENARIO_ID, records=[])
    with pytest.raises(EvidenceError, match="records must be a tuple"):
        EvidenceLedger(run_id=_RUN_ID, scenario_id=_SCENARIO_ID, records=("record",))


def test_ledger_rejects_record_identity_mismatch() -> None:
    record = _record(run_id="AURORA-RUN-FOUND-001-002")

    with pytest.raises(EvidenceError, match="record identity does not match"):
        EvidenceLedger(run_id=_RUN_ID, scenario_id=_SCENARIO_ID, records=(record,))


def test_ledger_rejects_noncontiguous_record_sequence() -> None:
    ledger = _ledger(2)
    changed = replace(ledger.records[1], sequence=2)

    with pytest.raises(EvidenceError, match="contiguous and start at zero"):
        EvidenceLedger(
            run_id=ledger.run_id,
            scenario_id=ledger.scenario_id,
            records=(ledger.records[0], changed),
        )


def test_ledger_rejects_duplicate_record_ids() -> None:
    ledger = _ledger(2)
    duplicate = replace(ledger.records[1], record_id=ledger.records[0].record_id)

    with pytest.raises(EvidenceError, match="record_id values must be unique"):
        EvidenceLedger(
            run_id=ledger.run_id,
            scenario_id=ledger.scenario_id,
            records=(ledger.records[0], duplicate),
        )


def test_ledger_defensively_rejects_first_record_previous_hash() -> None:
    first = _record()
    object.__setattr__(first, "previous_record_sha256", "a" * 64)

    with pytest.raises(EvidenceError, match="first ledger record must not reference"):
        EvidenceLedger(run_id=_RUN_ID, scenario_id=_SCENARIO_ID, records=(first,))


def test_ledger_rejects_decreasing_recorded_ticks() -> None:
    empty = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)
    first_ledger = _append(empty, 0, observed_at_tick=5, recorded_at_tick=5)
    second_ledger = _append(first_ledger, 1, observed_at_tick=10, recorded_at_tick=10)
    changed_second = replace(
        second_ledger.records[1],
        observed_at_tick=4,
        recorded_at_tick=4,
    )

    with pytest.raises(EvidenceError, match="nondecreasing recorded_at_tick"):
        EvidenceLedger(
            run_id=_RUN_ID,
            scenario_id=_SCENARIO_ID,
            records=(second_ledger.records[0], changed_second),
        )


def test_ledger_rejects_broken_record_hash_chain() -> None:
    ledger = _ledger(2)
    broken = replace(ledger.records[1], previous_record_sha256="0" * 64)

    with pytest.raises(EvidenceError, match="record hash chain does not match"):
        EvidenceLedger(
            run_id=ledger.run_id,
            scenario_id=ledger.scenario_id,
            records=(ledger.records[0], broken),
        )


def test_ledger_rejects_record_source_to_unknown_or_future_record() -> None:
    ledger = _ledger(2)
    unknown_source = _source(
        kind=EvidenceSourceKind.RECORD,
        source_id="EVIDENCE-RECORD-999",
    )
    changed = replace(ledger.records[1], sources=(unknown_source,))

    with pytest.raises(EvidenceError, match="must reference an earlier ledger record"):
        EvidenceLedger(
            run_id=ledger.run_id,
            scenario_id=ledger.scenario_id,
            records=(ledger.records[0], changed),
        )


def test_ledger_rejects_record_source_digest_mismatch() -> None:
    ledger = _ledger(2)
    mismatched = _source(
        kind=EvidenceSourceKind.RECORD,
        source_id=ledger.records[0].record_id,
        digest="0" * 64,
    )
    changed = replace(ledger.records[1], sources=(mismatched,))

    with pytest.raises(EvidenceError, match="digest does not match referenced record"):
        EvidenceLedger(
            run_id=ledger.run_id,
            scenario_id=ledger.scenario_id,
            records=(ledger.records[0], changed),
        )


def test_evidence_ledger_mapping_requires_exact_schema() -> None:
    mapping = _ledger().to_validator_mapping()

    with pytest.raises(EvidenceError, match="evidence ledger must be a JSON object"):
        EvidenceLedger.from_mapping([])

    missing = dict(mapping)
    del missing["run_id"]
    with pytest.raises(EvidenceError, match="missing required field"):
        EvidenceLedger.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(EvidenceError, match="contains unknown field"):
        EvidenceLedger.from_mapping(unknown)


def test_evidence_ledger_mapping_rejects_invalid_schema_and_records() -> None:
    mapping = _ledger().to_validator_mapping()

    wrong_version = copy.deepcopy(mapping)
    wrong_version["evidence_schema_version"] = "2.0"
    with pytest.raises(EvidenceError, match="unsupported evidence_schema_version"):
        EvidenceLedger.from_mapping(wrong_version)

    version_type = copy.deepcopy(mapping)
    version_type["evidence_schema_version"] = 1
    with pytest.raises(EvidenceError, match="evidence_schema_version must be a string"):
        EvidenceLedger.from_mapping(version_type)

    records_not_array = copy.deepcopy(mapping)
    records_not_array["records"] = ()
    with pytest.raises(EvidenceError, match="records must be a JSON array"):
        EvidenceLedger.from_mapping(records_not_array)

    record_not_object = copy.deepcopy(mapping)
    record_not_object["records"] = ["record"]
    with pytest.raises(EvidenceError, match=r"records\[0\] must be a JSON object"):
        EvidenceLedger.from_mapping(record_not_object)


def test_evidence_ledger_mapping_rejects_invalid_scalar_fields_and_hash() -> None:
    mapping = _ledger().to_validator_mapping()

    invalid_run = copy.deepcopy(mapping)
    invalid_run["run_id"] = 7
    with pytest.raises(EvidenceError, match=r"evidence ledger.run_id must be a string"):
        EvidenceLedger.from_mapping(invalid_run)

    invalid_scenario = copy.deepcopy(mapping)
    invalid_scenario["scenario_id"] = None
    with pytest.raises(EvidenceError, match=r"evidence ledger.scenario_id must be a string"):
        EvidenceLedger.from_mapping(invalid_scenario)

    invalid_hash_type = copy.deepcopy(mapping)
    invalid_hash_type["ledger_sha256"] = 7
    with pytest.raises(EvidenceError, match="ledger_sha256 must be a string"):
        EvidenceLedger.from_mapping(invalid_hash_type)

    wrong_hash = copy.deepcopy(mapping)
    wrong_hash["ledger_sha256"] = "0" * 64
    with pytest.raises(EvidenceError, match="declared ledger_sha256 does not match"):
        EvidenceLedger.from_mapping(wrong_hash)


def test_calculate_evidence_ledger_sha_rejects_invalid_runtime_type() -> None:
    with pytest.raises(EvidenceError, match="ledger must be an EvidenceLedger"):
        calculate_evidence_ledger_sha256("ledger")


def test_finalize_empty_ledger_produces_valid_empty_package() -> None:
    ledger = create_evidence_ledger(_RUN_ID, _SCENARIO_ID)

    package = finalize_evidence_ledger(ledger, finalized_at_tick=0)

    assert package.record_count == 0
    assert package.records == ()
    assert package.terminal_record_sha256 is None
    assert package.ledger_sha256 == ledger.ledger_sha256
    assert len(package.package_sha256) == 64


def test_finalize_nonempty_ledger_preserves_exact_chain() -> None:
    ledger = _ledger()

    package = finalize_evidence_ledger(ledger, finalized_at_tick=10)

    assert package.run_id == ledger.run_id
    assert package.scenario_id == ledger.scenario_id
    assert package.records is ledger.records
    assert package.record_count == len(ledger.records)
    assert package.terminal_record_sha256 == ledger.terminal_record_sha256
    assert package.ledger_sha256 == ledger.ledger_sha256
    assert package.package_sha256 == calculate_evidence_package_sha256(package)


def test_finalized_package_mapping_round_trip_is_exact() -> None:
    package = _package()
    mapping = package.to_validator_mapping()

    reconstructed = FinalizedEvidencePackage.from_mapping(mapping)

    assert reconstructed == package
    assert mapping["evidence_schema_version"] == SUPPORTED_EVIDENCE_SCHEMA_VERSION
    assert mapping["package_type"] == "FINALIZED_EVIDENCE_PACKAGE"
    assert mapping["record_count"] == package.record_count
    assert mapping["terminal_record_sha256"] == package.terminal_record_sha256
    assert mapping["ledger_sha256"] == package.ledger_sha256
    assert mapping["package_sha256"] == package.package_sha256


def test_package_hash_is_deterministic_and_finalization_sensitive() -> None:
    first = _package()
    second = _package()
    later = replace(first, finalized_at_tick=11)

    assert first.package_sha256 == second.package_sha256
    assert first.package_sha256 != later.package_sha256


def test_finalize_accepts_exact_final_record_tick() -> None:
    ledger = _ledger()
    final_tick = ledger.records[-1].recorded_at_tick

    assert (
        finalize_evidence_ledger(ledger, finalized_at_tick=final_tick).finalized_at_tick
        == final_tick
    )


def test_finalize_rejects_tick_before_last_record() -> None:
    ledger = _ledger()

    with pytest.raises(EvidenceError, match="must not precede the final evidence record"):
        finalize_evidence_ledger(
            ledger,
            finalized_at_tick=ledger.records[-1].recorded_at_tick - 1,
        )


@pytest.mark.parametrize("finalized_at_tick", [True, -1, MAX_TICK + 1])
def test_finalize_rejects_invalid_tick(finalized_at_tick: object) -> None:
    with pytest.raises(EvidenceError, match=r"must be an integer|must be between"):
        finalize_evidence_ledger(
            create_evidence_ledger(_RUN_ID, _SCENARIO_ID),
            finalized_at_tick=finalized_at_tick,
        )


def test_finalize_rejects_invalid_ledger_type() -> None:
    with pytest.raises(EvidenceError, match="ledger must be an EvidenceLedger"):
        finalize_evidence_ledger("ledger", finalized_at_tick=0)


def test_finalized_package_revalidates_embedded_ledger() -> None:
    ledger = _ledger(2)
    broken = replace(ledger.records[1], previous_record_sha256="0" * 64)

    with pytest.raises(EvidenceError, match="record hash chain does not match"):
        FinalizedEvidencePackage(
            run_id=ledger.run_id,
            scenario_id=ledger.scenario_id,
            records=(ledger.records[0], broken),
            finalized_at_tick=10,
        )


def test_finalized_package_mapping_requires_exact_schema() -> None:
    mapping = _package().to_validator_mapping()

    with pytest.raises(EvidenceError, match="evidence package must be a JSON object"):
        FinalizedEvidencePackage.from_mapping([])

    missing = dict(mapping)
    del missing["record_count"]
    with pytest.raises(EvidenceError, match="missing required field"):
        FinalizedEvidencePackage.from_mapping(missing)

    unknown = dict(mapping)
    unknown["unexpected"] = True
    with pytest.raises(EvidenceError, match="contains unknown field"):
        FinalizedEvidencePackage.from_mapping(unknown)


def test_finalized_package_mapping_rejects_version_type_and_package_type() -> None:
    mapping = _package().to_validator_mapping()

    wrong_version = copy.deepcopy(mapping)
    wrong_version["evidence_schema_version"] = "2.0"
    with pytest.raises(EvidenceError, match="unsupported evidence_schema_version"):
        FinalizedEvidencePackage.from_mapping(wrong_version)

    version_type = copy.deepcopy(mapping)
    version_type["evidence_schema_version"] = 1
    with pytest.raises(EvidenceError, match="evidence_schema_version must be a string"):
        FinalizedEvidencePackage.from_mapping(version_type)

    wrong_type = copy.deepcopy(mapping)
    wrong_type["package_type"] = "DRAFT"
    with pytest.raises(EvidenceError, match="unsupported evidence package_type"):
        FinalizedEvidencePackage.from_mapping(wrong_type)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("run_id", 7, "evidence package.run_id must be a string"),
        ("scenario_id", None, "evidence package.scenario_id must be a string"),
        ("finalized_at_tick", True, "finalized_at_tick must be an integer"),
        ("record_count", True, "record_count must be an integer"),
        ("terminal_record_sha256", 7, "terminal_record_sha256 must be a string"),
        ("ledger_sha256", 7, "ledger_sha256 must be a string"),
        ("package_sha256", 7, "package_sha256 must be a string"),
    ],
)
def test_finalized_package_mapping_rejects_invalid_scalar_fields(
    field: str,
    value: object,
    message: str,
) -> None:
    mapping = _package().to_validator_mapping()
    mapping[field] = value

    with pytest.raises(EvidenceError, match=message):
        FinalizedEvidencePackage.from_mapping(mapping)


def test_finalized_package_mapping_rejects_invalid_record_collection() -> None:
    mapping = _package().to_validator_mapping()

    not_array = copy.deepcopy(mapping)
    not_array["records"] = ()
    with pytest.raises(EvidenceError, match="records must be a JSON array"):
        FinalizedEvidencePackage.from_mapping(not_array)

    non_object = copy.deepcopy(mapping)
    non_object["records"] = ["record"]
    with pytest.raises(EvidenceError, match=r"records\[0\] must be a JSON object"):
        FinalizedEvidencePackage.from_mapping(non_object)


def test_finalized_package_mapping_detects_redundant_field_mismatches() -> None:
    mapping = _package().to_validator_mapping()

    wrong_count = copy.deepcopy(mapping)
    wrong_count["record_count"] += 1
    with pytest.raises(EvidenceError, match="declared record_count does not match"):
        FinalizedEvidencePackage.from_mapping(wrong_count)

    wrong_terminal = copy.deepcopy(mapping)
    wrong_terminal["terminal_record_sha256"] = "0" * 64
    with pytest.raises(EvidenceError, match="declared terminal_record_sha256 does not match"):
        FinalizedEvidencePackage.from_mapping(wrong_terminal)

    wrong_ledger = copy.deepcopy(mapping)
    wrong_ledger["ledger_sha256"] = "0" * 64
    with pytest.raises(EvidenceError, match="declared ledger_sha256 does not match"):
        FinalizedEvidencePackage.from_mapping(wrong_ledger)

    wrong_package = copy.deepcopy(mapping)
    wrong_package["package_sha256"] = "0" * 64
    with pytest.raises(EvidenceError, match="declared package_sha256 does not match"):
        FinalizedEvidencePackage.from_mapping(wrong_package)


def test_package_round_trip_detects_nested_payload_tampering() -> None:
    mapping = _package().to_validator_mapping()
    records = mapping["records"]
    assert isinstance(records, list)
    first_record = records[0]
    assert isinstance(first_record, dict)
    payload = first_record["payload"]
    assert isinstance(payload, dict)
    data = payload["data"]
    assert isinstance(data, dict)
    data["status"] = "tampered"

    with pytest.raises(EvidenceError):
        FinalizedEvidencePackage.from_mapping(mapping)


def test_calculate_evidence_package_sha_rejects_invalid_runtime_type() -> None:
    with pytest.raises(EvidenceError, match="package must be a FinalizedEvidencePackage"):
        calculate_evidence_package_sha256("package")


def test_evidence_artifacts_are_immutable() -> None:
    payload = _payload()
    source = _source()
    record = _record()
    ledger = _ledger()
    package = _package()

    mutations = (
        (payload, "payload_sha256", "0" * 64),
        (source, "source_id", "SOURCE-999"),
        (record, "record_id", "EVIDENCE-RECORD-999"),
        (ledger, "run_id", "AURORA-RUN-FOUND-001-999"),
        (package, "finalized_at_tick", 99),
    )
    for value, field, replacement_value in mutations:
        with pytest.raises(FrozenInstanceError):
            setattr(value, field, replacement_value)


def test_evidence_module_has_no_aurora_projection_api() -> None:
    assert not hasattr(EvidenceLedger, "to_aurora_mapping")
    assert not hasattr(FinalizedEvidencePackage, "to_aurora_mapping")
    assert not hasattr(evidence_module, "project_evidence_for_aurora")


def test_evidence_module_exports_complete_public_contract() -> None:
    assert set(evidence_module.__all__) == {
        "DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES",
        "MAX_EVIDENCE_PAYLOAD_BYTES",
        "MAX_TICK",
        "SUPPORTED_EVIDENCE_SCHEMA_VERSION",
        "EvidenceDomain",
        "EvidenceError",
        "EvidenceKind",
        "EvidenceLedger",
        "EvidencePayload",
        "EvidenceRecord",
        "EvidenceSource",
        "EvidenceSourceKind",
        "FinalizedEvidencePackage",
        "append_evidence_record",
        "calculate_evidence_ledger_sha256",
        "calculate_evidence_package_sha256",
        "create_evidence_ledger",
        "create_evidence_payload",
        "create_record_source",
        "finalize_evidence_ledger",
    }
