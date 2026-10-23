"""Append-only, provenance-preserving validation evidence for Aurora runs.

The evidence ledger is validator-owned audit state. It records what the
harness observed across isolated epistemic domains, binds every record into a
deterministic hash chain, and produces a finalized package suitable for later
assertion and storage modules. It is never an input channel into Aurora.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Final, cast

SUPPORTED_EVIDENCE_SCHEMA_VERSION: Final[str] = "1.0"
DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES: Final[int] = 1_048_576
MAX_EVIDENCE_PAYLOAD_BYTES: Final[int] = 4_194_304
MAX_TICK: Final[int] = (1 << 63) - 1

_SHA256_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[0-9a-f]{64}$")
_CONTROL_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Z0-9][A-Z0-9._-]{2,127}$")
_SCENARIO_ID_PATTERN: Final[re.Pattern[str]] = re.compile(r"^AURORA-SCN-[A-Z0-9]+-[0-9]{3}$")
_AURORA_ACCESSIBLE_FORBIDDEN_KEYS: Final[frozenset[str]] = frozenset(
    {
        "expected_answer",
        "expected_interpretation",
        "expected_result",
        "failure_conditions",
        "fixture_manifest_sha256",
        "fixture_set_id",
        "future_event_queue",
        "hidden_from_aurora",
        "hidden_state_marker",
        "player_private",
        "scenario_id",
        "scenario_name",
        "validator_metadata",
        "validator_notes",
        "world_debug_state",
        "world_truth",
    }
)


class EvidenceError(ValueError):
    """Raised when evidence data, provenance, or package integrity is invalid."""


class EvidenceDomain(StrEnum):
    """Epistemic or operational domain in which a record was captured."""

    RUN_CONTROL = "RUN_CONTROL"
    WORLD = "WORLD"
    PLAYER_PRIVATE = "PLAYER_PRIVATE"
    FUTURE = "FUTURE"
    AURORA_ACCESSIBLE = "AURORA_ACCESSIBLE"
    AURORA_STATE = "AURORA_STATE"
    EXPECTED_RESULTS = "EXPECTED_RESULTS"
    VALIDATOR = "VALIDATOR"
    INFRASTRUCTURE = "INFRASTRUCTURE"


class EvidenceKind(StrEnum):
    """Stable classification of one captured evidence record."""

    RUN_CONFIGURATION = "RUN_CONFIGURATION"
    BASELINE_VERIFICATION = "BASELINE_VERIFICATION"
    FIXTURE_INTEGRITY = "FIXTURE_INTEGRITY"
    EVENT_RELEASE = "EVENT_RELEASE"
    CHANNEL_ADMISSION = "CHANNEL_ADMISSION"
    AURORA_INPUT = "AURORA_INPUT"
    STATE_SNAPSHOT = "STATE_SNAPSHOT"
    STATE_TRANSITION = "STATE_TRANSITION"
    ASSERTION_RESULT = "ASSERTION_RESULT"
    WORLD_CONSEQUENCE = "WORLD_CONSEQUENCE"
    DIAGNOSTIC = "DIAGNOSTIC"
    VERDICT = "VERDICT"


class EvidenceSourceKind(StrEnum):
    """Provenance class for an input that supports an evidence record."""

    BASELINE = "BASELINE"
    CONFIGURATION = "CONFIGURATION"
    FIXTURE = "FIXTURE"
    EVENT = "EVENT"
    CHANNEL_PACKET = "CHANNEL_PACKET"
    SNAPSHOT = "SNAPSHOT"
    TRANSITION = "TRANSITION"
    ASSERTION = "ASSERTION"
    RECORD = "RECORD"
    EXTERNAL = "EXTERNAL"


@dataclass(frozen=True, slots=True)
class EvidencePayload:
    """Canonical JSON evidence content with an exact integrity digest."""

    payload_json: bytes
    payload_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.payload_json, bytes):
            raise EvidenceError("payload_json must be bytes")
        _validate_sha256(self.payload_sha256, field="payload_sha256")
        if hashlib.sha256(self.payload_json).hexdigest() != self.payload_sha256:
            raise EvidenceError("payload_sha256 does not match payload_json")
        if len(self.payload_json) > MAX_EVIDENCE_PAYLOAD_BYTES:
            raise EvidenceError(f"payload_json must not exceed {MAX_EVIDENCE_PAYLOAD_BYTES} bytes")

        decoded = _decode_json_object(self.payload_json)
        _validate_json_value(decoded, path="payload")
        if self.payload_json != _canonical_json_bytes(decoded):
            raise EvidenceError("payload_json must use canonical JSON encoding")

    @property
    def size_bytes(self) -> int:
        """Return the exact canonical payload size."""

        return len(self.payload_json)

    def decode(self) -> dict[str, object]:
        """Return a fresh decoded evidence object."""

        return _decode_json_object(self.payload_json)

    def to_mapping(self) -> dict[str, object]:
        """Return the portable payload representation."""

        return {
            "data": self.decode(),
            "payload_sha256": self.payload_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> EvidencePayload:
        """Parse and verify a portable evidence payload."""

        mapping = _require_mapping(value, field="payload")
        _require_exact_keys(
            mapping,
            required=frozenset({"data", "payload_sha256"}),
            field="payload",
        )
        data = _require_mapping(mapping["data"], field="payload.data")
        declared_sha256 = _require_string(
            mapping["payload_sha256"],
            field="payload.payload_sha256",
        )
        payload = create_evidence_payload(
            data,
            max_payload_bytes=MAX_EVIDENCE_PAYLOAD_BYTES,
        )
        if payload.payload_sha256 != declared_sha256:
            raise EvidenceError("declared payload_sha256 does not match payload data")
        return payload


@dataclass(frozen=True, slots=True)
class EvidenceSource:
    """Immutable reference to one provenance-bearing evidence input."""

    source_kind: EvidenceSourceKind
    source_id: str
    source_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.source_kind, EvidenceSourceKind):
            raise EvidenceError("source_kind must be an EvidenceSourceKind value")
        _validate_control_id(self.source_id, field="source_id")
        _validate_sha256(self.source_sha256, field="source_sha256")

    def to_mapping(self) -> dict[str, object]:
        """Return the stable provenance reference representation."""

        return {
            "source_id": self.source_id,
            "source_kind": self.source_kind.value,
            "source_sha256": self.source_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> EvidenceSource:
        """Parse one provenance reference from a schema mapping."""

        mapping = _require_mapping(value, field="source")
        _require_exact_keys(
            mapping,
            required=frozenset({"source_id", "source_kind", "source_sha256"}),
            field="source",
        )
        source_kind = _parse_enum(
            EvidenceSourceKind,
            mapping["source_kind"],
            field="source.source_kind",
        )
        return cls(
            source_kind=source_kind,
            source_id=_require_string(mapping["source_id"], field="source.source_id"),
            source_sha256=_require_string(
                mapping["source_sha256"],
                field="source.source_sha256",
            ),
        )


@dataclass(frozen=True, slots=True)
class EvidenceRecord:
    """One append-only, hash-chained record in a validator evidence ledger."""

    record_id: str
    run_id: str
    scenario_id: str
    sequence: int
    observed_at_tick: int
    recorded_at_tick: int
    kind: EvidenceKind
    domain: EvidenceDomain
    producer_id: str
    payload: EvidencePayload
    sources: tuple[EvidenceSource, ...]
    previous_record_sha256: str | None

    def __post_init__(self) -> None:
        _validate_control_id(self.record_id, field="record_id")
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        _validate_sequence(self.sequence, field="sequence")
        _validate_tick(self.observed_at_tick, field="observed_at_tick")
        _validate_tick(self.recorded_at_tick, field="recorded_at_tick")
        if self.observed_at_tick > self.recorded_at_tick:
            raise EvidenceError("observed_at_tick must not exceed recorded_at_tick")
        if not isinstance(self.kind, EvidenceKind):
            raise EvidenceError("kind must be an EvidenceKind value")
        if not isinstance(self.domain, EvidenceDomain):
            raise EvidenceError("domain must be an EvidenceDomain value")
        _validate_control_id(self.producer_id, field="producer_id")
        if not isinstance(self.payload, EvidencePayload):
            raise EvidenceError("payload must be an EvidencePayload")
        if not isinstance(self.sources, tuple) or not all(
            isinstance(source, EvidenceSource) for source in self.sources
        ):
            raise EvidenceError("sources must be a tuple of EvidenceSource values")

        source_keys = tuple((source.source_kind, source.source_id) for source in self.sources)
        if len(source_keys) != len(set(source_keys)):
            raise EvidenceError("sources must not contain duplicate kind and ID pairs")

        if self.previous_record_sha256 is not None:
            _validate_sha256(
                self.previous_record_sha256,
                field="previous_record_sha256",
            )
        if self.sequence == 0 and self.previous_record_sha256 is not None:
            raise EvidenceError("first evidence record must not declare a previous hash")
        if self.sequence > 0 and self.previous_record_sha256 is None:
            raise EvidenceError("non-first evidence record requires a previous hash")

        if self.domain is EvidenceDomain.AURORA_ACCESSIBLE:
            _validate_aurora_accessible_payload(self.payload.decode(), path="payload")

    @property
    def record_sha256(self) -> str:
        """Return the content and chain digest for this record."""

        return hashlib.sha256(_canonical_json_bytes(self._content_mapping())).hexdigest()

    def _content_mapping(self) -> dict[str, object]:
        return {
            "domain": self.domain.value,
            "kind": self.kind.value,
            "observed_at_tick": self.observed_at_tick,
            "payload": self.payload.to_mapping(),
            "previous_record_sha256": self.previous_record_sha256,
            "producer_id": self.producer_id,
            "record_id": self.record_id,
            "recorded_at_tick": self.recorded_at_tick,
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "sequence": self.sequence,
            "sources": [source.to_mapping() for source in self.sources],
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete validator-owned evidence record."""

        return {
            **self._content_mapping(),
            "record_sha256": self.record_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> EvidenceRecord:
        """Parse and verify a serialized evidence record."""

        mapping = _require_mapping(value, field="evidence record")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "domain",
                    "kind",
                    "observed_at_tick",
                    "payload",
                    "previous_record_sha256",
                    "producer_id",
                    "record_id",
                    "record_sha256",
                    "recorded_at_tick",
                    "run_id",
                    "scenario_id",
                    "sequence",
                    "sources",
                }
            ),
            field="evidence record",
        )
        sources = _parse_sources(mapping["sources"])
        previous_hash = _require_optional_string(
            mapping["previous_record_sha256"],
            field="evidence record.previous_record_sha256",
        )
        record = cls(
            record_id=_require_string(mapping["record_id"], field="evidence record.record_id"),
            run_id=_require_string(mapping["run_id"], field="evidence record.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"],
                field="evidence record.scenario_id",
            ),
            sequence=_require_integer(mapping["sequence"], field="evidence record.sequence"),
            observed_at_tick=_require_integer(
                mapping["observed_at_tick"],
                field="evidence record.observed_at_tick",
            ),
            recorded_at_tick=_require_integer(
                mapping["recorded_at_tick"],
                field="evidence record.recorded_at_tick",
            ),
            kind=_parse_enum(
                EvidenceKind,
                mapping["kind"],
                field="evidence record.kind",
            ),
            domain=_parse_enum(
                EvidenceDomain,
                mapping["domain"],
                field="evidence record.domain",
            ),
            producer_id=_require_string(
                mapping["producer_id"],
                field="evidence record.producer_id",
            ),
            payload=EvidencePayload.from_mapping(
                _require_mapping(mapping["payload"], field="evidence record.payload")
            ),
            sources=sources,
            previous_record_sha256=previous_hash,
        )
        declared_sha256 = _require_string(
            mapping["record_sha256"],
            field="evidence record.record_sha256",
        )
        if record.record_sha256 != declared_sha256:
            raise EvidenceError("declared record_sha256 does not match evidence record")
        return record


@dataclass(frozen=True, slots=True)
class EvidenceLedger:
    """Immutable append-only evidence chain for one validation run."""

    run_id: str
    scenario_id: str
    records: tuple[EvidenceRecord, ...] = ()

    def __post_init__(self) -> None:
        _validate_control_id(self.run_id, field="run_id")
        _validate_scenario_id(self.scenario_id)
        if not isinstance(self.records, tuple) or not all(
            isinstance(record, EvidenceRecord) for record in self.records
        ):
            raise EvidenceError("records must be a tuple of EvidenceRecord values")

        seen_record_ids: set[str] = set()
        seen_record_hashes: dict[str, str] = {}
        previous_record: EvidenceRecord | None = None
        for expected_sequence, record in enumerate(self.records):
            if record.run_id != self.run_id or record.scenario_id != self.scenario_id:
                raise EvidenceError("record identity does not match evidence ledger")
            if record.sequence != expected_sequence:
                raise EvidenceError("record sequence must be contiguous and start at zero")
            if record.record_id in seen_record_ids:
                raise EvidenceError("record_id values must be unique within a ledger")
            if previous_record is None:
                if record.previous_record_sha256 is not None:
                    raise EvidenceError("first ledger record must not reference a previous record")
            else:
                if record.recorded_at_tick < previous_record.recorded_at_tick:
                    raise EvidenceError("records must use nondecreasing recorded_at_tick values")
                if record.previous_record_sha256 != previous_record.record_sha256:
                    raise EvidenceError("record hash chain does not match previous record")

            for source in record.sources:
                if source.source_kind is EvidenceSourceKind.RECORD:
                    expected_hash = seen_record_hashes.get(source.source_id)
                    if expected_hash is None:
                        raise EvidenceError("record source must reference an earlier ledger record")
                    if source.source_sha256 != expected_hash:
                        raise EvidenceError("record source digest does not match referenced record")

            seen_record_ids.add(record.record_id)
            seen_record_hashes[record.record_id] = record.record_sha256
            previous_record = record

    @property
    def ledger_sha256(self) -> str:
        """Return a deterministic digest of the complete evidence chain."""

        return calculate_evidence_ledger_sha256(self)

    @property
    def terminal_record_sha256(self) -> str | None:
        """Return the final chain digest, or null for an empty ledger."""

        return None if not self.records else self.records[-1].record_sha256

    def _content_mapping(self) -> dict[str, object]:
        return {
            "evidence_schema_version": SUPPORTED_EVIDENCE_SCHEMA_VERSION,
            "records": [record.to_validator_mapping() for record in self.records],
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete portable ledger representation."""

        return {
            **self._content_mapping(),
            "ledger_sha256": self.ledger_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> EvidenceLedger:
        """Parse and verify a serialized append-only evidence ledger."""

        mapping = _require_mapping(value, field="evidence ledger")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "evidence_schema_version",
                    "ledger_sha256",
                    "records",
                    "run_id",
                    "scenario_id",
                }
            ),
            field="evidence ledger",
        )
        _validate_schema_version(mapping["evidence_schema_version"])
        ledger = cls(
            run_id=_require_string(mapping["run_id"], field="evidence ledger.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"],
                field="evidence ledger.scenario_id",
            ),
            records=_parse_records(mapping["records"]),
        )
        declared_sha256 = _require_string(
            mapping["ledger_sha256"],
            field="evidence ledger.ledger_sha256",
        )
        if ledger.ledger_sha256 != declared_sha256:
            raise EvidenceError("declared ledger_sha256 does not match evidence ledger")
        return ledger


@dataclass(frozen=True, slots=True)
class FinalizedEvidencePackage:
    """Integrity-sealed validator evidence package for a completed capture phase."""

    run_id: str
    scenario_id: str
    records: tuple[EvidenceRecord, ...]
    finalized_at_tick: int

    def __post_init__(self) -> None:
        ledger = EvidenceLedger(
            run_id=self.run_id,
            scenario_id=self.scenario_id,
            records=self.records,
        )
        _validate_tick(self.finalized_at_tick, field="finalized_at_tick")
        if ledger.records and self.finalized_at_tick < ledger.records[-1].recorded_at_tick:
            raise EvidenceError("finalized_at_tick must not precede the final evidence record")

    @property
    def record_count(self) -> int:
        """Return the immutable number of evidence records in the package."""

        return len(self.records)

    @property
    def ledger_sha256(self) -> str:
        """Return the digest of the embedded append-only ledger."""

        return EvidenceLedger(
            run_id=self.run_id,
            scenario_id=self.scenario_id,
            records=self.records,
        ).ledger_sha256

    @property
    def terminal_record_sha256(self) -> str | None:
        """Return the final record digest, or null when the package is empty."""

        return None if not self.records else self.records[-1].record_sha256

    @property
    def package_sha256(self) -> str:
        """Return the digest of the finalized package envelope and ledger."""

        return calculate_evidence_package_sha256(self)

    def _content_mapping(self) -> dict[str, object]:
        return {
            "evidence_schema_version": SUPPORTED_EVIDENCE_SCHEMA_VERSION,
            "finalized_at_tick": self.finalized_at_tick,
            "ledger_sha256": self.ledger_sha256,
            "package_type": "FINALIZED_EVIDENCE_PACKAGE",
            "record_count": self.record_count,
            "records": [record.to_validator_mapping() for record in self.records],
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "terminal_record_sha256": self.terminal_record_sha256,
        }

    def to_validator_mapping(self) -> dict[str, object]:
        """Return the complete finalized evidence package representation."""

        return {
            **self._content_mapping(),
            "package_sha256": self.package_sha256,
        }

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> FinalizedEvidencePackage:
        """Parse and verify a finalized evidence package and all nested records."""

        mapping = _require_mapping(value, field="evidence package")
        _require_exact_keys(
            mapping,
            required=frozenset(
                {
                    "evidence_schema_version",
                    "finalized_at_tick",
                    "ledger_sha256",
                    "package_sha256",
                    "package_type",
                    "record_count",
                    "records",
                    "run_id",
                    "scenario_id",
                    "terminal_record_sha256",
                }
            ),
            field="evidence package",
        )
        _validate_schema_version(mapping["evidence_schema_version"])
        if mapping["package_type"] != "FINALIZED_EVIDENCE_PACKAGE":
            raise EvidenceError("unsupported evidence package_type")
        package = cls(
            run_id=_require_string(mapping["run_id"], field="evidence package.run_id"),
            scenario_id=_require_string(
                mapping["scenario_id"],
                field="evidence package.scenario_id",
            ),
            records=_parse_records(mapping["records"]),
            finalized_at_tick=_require_integer(
                mapping["finalized_at_tick"],
                field="evidence package.finalized_at_tick",
            ),
        )

        declared_count = _require_integer(
            mapping["record_count"],
            field="evidence package.record_count",
        )
        if package.record_count != declared_count:
            raise EvidenceError("declared record_count does not match evidence package")
        declared_terminal = _require_optional_string(
            mapping["terminal_record_sha256"],
            field="evidence package.terminal_record_sha256",
        )
        if package.terminal_record_sha256 != declared_terminal:
            raise EvidenceError("declared terminal_record_sha256 does not match evidence package")
        declared_ledger_sha256 = _require_string(
            mapping["ledger_sha256"],
            field="evidence package.ledger_sha256",
        )
        if package.ledger_sha256 != declared_ledger_sha256:
            raise EvidenceError("declared ledger_sha256 does not match evidence package")
        declared_package_sha256 = _require_string(
            mapping["package_sha256"],
            field="evidence package.package_sha256",
        )
        if package.package_sha256 != declared_package_sha256:
            raise EvidenceError("declared package_sha256 does not match evidence package")
        return package


def create_evidence_payload(
    data: Mapping[str, object],
    *,
    max_payload_bytes: int = DEFAULT_MAX_EVIDENCE_PAYLOAD_BYTES,
) -> EvidencePayload:
    """Create a canonical evidence payload from a JSON object."""

    if not isinstance(data, Mapping):
        raise EvidenceError("evidence payload data must be a JSON object")
    if isinstance(max_payload_bytes, bool) or not isinstance(max_payload_bytes, int):
        raise EvidenceError("max_payload_bytes must be an integer")
    if not 1 <= max_payload_bytes <= MAX_EVIDENCE_PAYLOAD_BYTES:
        raise EvidenceError(f"max_payload_bytes must be between 1 and {MAX_EVIDENCE_PAYLOAD_BYTES}")
    normalized = _normalize_json_value(data, path="payload")
    if not isinstance(normalized, dict):
        raise EvidenceError("evidence payload data must be a JSON object")
    payload_json = _canonical_json_bytes(normalized)
    if len(payload_json) > max_payload_bytes:
        raise EvidenceError(f"evidence payload must not exceed {max_payload_bytes} bytes")
    return EvidencePayload(
        payload_json=payload_json,
        payload_sha256=hashlib.sha256(payload_json).hexdigest(),
    )


def create_evidence_ledger(run_id: str, scenario_id: str) -> EvidenceLedger:
    """Create an empty append-only ledger for one validation run."""

    return EvidenceLedger(run_id=run_id, scenario_id=scenario_id)


def create_record_source(record: EvidenceRecord) -> EvidenceSource:
    """Create a verified provenance reference to an earlier evidence record."""

    if not isinstance(record, EvidenceRecord):
        raise EvidenceError("record must be an EvidenceRecord")
    return EvidenceSource(
        source_kind=EvidenceSourceKind.RECORD,
        source_id=record.record_id,
        source_sha256=record.record_sha256,
    )


def append_evidence_record(
    ledger: EvidenceLedger,
    *,
    record_id: str,
    observed_at_tick: int,
    recorded_at_tick: int,
    kind: EvidenceKind,
    domain: EvidenceDomain,
    producer_id: str,
    payload: EvidencePayload,
    sources: tuple[EvidenceSource, ...] = (),
) -> EvidenceLedger:
    """Return a new ledger with one deterministic record appended."""

    if not isinstance(ledger, EvidenceLedger):
        raise EvidenceError("ledger must be an EvidenceLedger")
    previous_hash = ledger.terminal_record_sha256
    record = EvidenceRecord(
        record_id=record_id,
        run_id=ledger.run_id,
        scenario_id=ledger.scenario_id,
        sequence=len(ledger.records),
        observed_at_tick=observed_at_tick,
        recorded_at_tick=recorded_at_tick,
        kind=kind,
        domain=domain,
        producer_id=producer_id,
        payload=payload,
        sources=sources,
        previous_record_sha256=previous_hash,
    )
    return EvidenceLedger(
        run_id=ledger.run_id,
        scenario_id=ledger.scenario_id,
        records=(*ledger.records, record),
    )


def finalize_evidence_ledger(
    ledger: EvidenceLedger,
    *,
    finalized_at_tick: int,
) -> FinalizedEvidencePackage:
    """Seal the current immutable ledger into a finalized evidence package."""

    if not isinstance(ledger, EvidenceLedger):
        raise EvidenceError("ledger must be an EvidenceLedger")
    return FinalizedEvidencePackage(
        run_id=ledger.run_id,
        scenario_id=ledger.scenario_id,
        records=ledger.records,
        finalized_at_tick=finalized_at_tick,
    )


def calculate_evidence_ledger_sha256(ledger: EvidenceLedger) -> str:
    """Calculate the canonical digest of an evidence ledger."""

    if not isinstance(ledger, EvidenceLedger):
        raise EvidenceError("ledger must be an EvidenceLedger")
    return hashlib.sha256(_canonical_json_bytes(ledger._content_mapping())).hexdigest()


def calculate_evidence_package_sha256(package: FinalizedEvidencePackage) -> str:
    """Calculate the canonical digest of a finalized evidence package."""

    if not isinstance(package, FinalizedEvidencePackage):
        raise EvidenceError("package must be a FinalizedEvidencePackage")
    return hashlib.sha256(_canonical_json_bytes(package._content_mapping())).hexdigest()


def _parse_sources(value: object) -> tuple[EvidenceSource, ...]:
    if not isinstance(value, list):
        raise EvidenceError("evidence record.sources must be a JSON array")
    return tuple(
        EvidenceSource.from_mapping(
            _require_mapping(item, field=f"evidence record.sources[{index}]")
        )
        for index, item in enumerate(value)
    )


def _parse_records(value: object) -> tuple[EvidenceRecord, ...]:
    if not isinstance(value, list):
        raise EvidenceError("records must be a JSON array")
    return tuple(
        EvidenceRecord.from_mapping(_require_mapping(item, field=f"records[{index}]"))
        for index, item in enumerate(value)
    )


def _validate_schema_version(value: object) -> None:
    version = _require_string(value, field="evidence_schema_version")
    if version != SUPPORTED_EVIDENCE_SCHEMA_VERSION:
        raise EvidenceError(f"unsupported evidence_schema_version: {version}")


def _validate_aurora_accessible_payload(value: object, *, path: str) -> None:
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_aurora_accessible_payload(item, path=f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            normalized_key = _normalize_metadata_key(key)
            if normalized_key in _AURORA_ACCESSIBLE_FORBIDDEN_KEYS:
                raise EvidenceError(
                    f"{path} contains field forbidden in AURORA_ACCESSIBLE evidence: {key}"
                )
            _validate_aurora_accessible_payload(item, path=f"{path}.{key}")


def _decode_json_object(payload_json: bytes) -> dict[str, object]:
    try:
        decoded = json.loads(
            payload_json.decode("utf-8"),
            parse_constant=_reject_non_finite_json,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise EvidenceError(f"payload_json is not valid JSON: {exc}") from exc
    if not isinstance(decoded, dict):
        raise EvidenceError("payload_json must encode a JSON object")
    return cast(dict[str, object], decoded)


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
        raise EvidenceError(f"value is not JSON-serializable: {exc}") from exc


def _normalize_json_value(value: object, *, path: str) -> object:
    _validate_json_value(value, path=path)
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if isinstance(value, list):
        return [
            _normalize_json_value(item, path=f"{path}[{index}]") for index, item in enumerate(value)
        ]
    if isinstance(value, Mapping):
        return {
            key: _normalize_json_value(item, path=f"{path}.{key}") for key, item in value.items()
        }
    raise EvidenceError(f"{path} contains unsupported JSON value type")


def _validate_json_value(value: object, *, path: str) -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise EvidenceError(f"{path} contains a non-finite number")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            _validate_json_value(item, path=f"{path}[{index}]")
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            if not isinstance(key, str):
                raise EvidenceError(f"{path} contains a non-string object key")
            _validate_json_value(item, path=f"{path}.{key}")
        return
    raise EvidenceError(f"{path} contains unsupported JSON value type")


def _normalize_metadata_key(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", key.casefold()).strip("_")


def _require_mapping(value: object, *, field: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise EvidenceError(f"{field} must be a JSON object")
    if not all(isinstance(key, str) for key in value):
        raise EvidenceError(f"{field} must use string keys")
    return cast(Mapping[str, object], value)


def _require_exact_keys(
    mapping: Mapping[str, object],
    *,
    required: frozenset[str],
    field: str,
) -> None:
    keys = frozenset(mapping)
    missing = sorted(required - keys)
    unknown = sorted(keys - required)
    if missing:
        raise EvidenceError(f"{field} missing required field(s): {', '.join(missing)}")
    if unknown:
        raise EvidenceError(f"{field} contains unknown field(s): {', '.join(unknown)}")


def _require_string(value: object, *, field: str) -> str:
    if not isinstance(value, str):
        raise EvidenceError(f"{field} must be a string")
    return value


def _require_optional_string(value: object, *, field: str) -> str | None:
    if value is None:
        return None
    return _require_string(value, field=field)


def _require_integer(value: object, *, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise EvidenceError(f"{field} must be an integer")
    return value


def _parse_enum[T: StrEnum](
    enum_type: type[T],
    value: object,
    *,
    field: str,
) -> T:
    text = _require_string(value, field=field)
    try:
        return enum_type(text)
    except ValueError as exc:
        raise EvidenceError(f"unsupported {field}: {text}") from exc


def _validate_control_id(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise EvidenceError(f"{field} must be a string")
    if _CONTROL_ID_PATTERN.fullmatch(value) is None:
        raise EvidenceError(f"{field} must contain 3-128 uppercase identifier characters")


def _validate_scenario_id(value: str) -> None:
    if not isinstance(value, str):
        raise EvidenceError("scenario_id must be a string")
    if _SCENARIO_ID_PATTERN.fullmatch(value) is None:
        raise EvidenceError("scenario_id must match AURORA-SCN-<GATE>-<NNN>")


def _validate_sha256(value: str, *, field: str) -> None:
    if not isinstance(value, str):
        raise EvidenceError(f"{field} must be a string")
    if _SHA256_PATTERN.fullmatch(value) is None:
        raise EvidenceError(f"{field} must be a lowercase 64-character SHA-256 digest")


def _validate_sequence(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise EvidenceError(f"{field} must be an integer")
    if value < 0:
        raise EvidenceError(f"{field} must be non-negative")


def _validate_tick(value: int, *, field: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise EvidenceError(f"{field} must be an integer")
    if not 0 <= value <= MAX_TICK:
        raise EvidenceError(f"{field} must be between 0 and {MAX_TICK}")


def _reject_non_finite_json(value: str) -> None:
    raise ValueError(f"non-finite JSON value is not allowed: {value}")


__all__ = [
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
]
