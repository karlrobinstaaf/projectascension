# PROJECT ASCENSION
# Aurora Minimum Executable State Interface

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Document | Aurora Minimum Executable State Interface |
| File | `Aurora_Minimum_Executable_State_Interface.md` |
| Location | `Canon/Systems/AI/Aurora/Validation/Aurora_Minimum_Executable_State_Interface.md` |
| Document Class | IMPLEMENTATION CONTRACT / STATE INTERFACE / VALIDATION ENABLEMENT |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Implementation Status | SPECIFICATION ONLY |
| Initial Execution Target | `AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md` |
| Validation Gate | GATE 1 — FOUNDATION |
| Baseline Dependency | `AURORA-G1-FOUNDATION-BASELINE-001` — PRE-FREEZE |
| Primary Dependencies | `Aurora_State.md`, `Aurora_Validation_Evidence_Schema.md`, `Aurora_Foundation_Validation_Runbook.md`, `Aurora_Invariant_Catalog.md`, `Aurora_Cross_System_Test_Matrix.md`, `Aurora_Scenario_Test_Framework.md` |
| Creative Director | USER |
| Architecture / Technical Lead | ASSISTANT |
| Purpose | Define the smallest generalizable executable state contract required to initialize Aurora, isolate hidden world state, admit evidence through governed information channels, update epistemic state, preserve provenance and history, expose structured validation telemetry and execute FOUND-001 without scenario-specific hardcoding. |
| Last Updated | 2026-08-11 |

> **The first executable Aurora does not need to contain every future capability. She must contain enough real architecture that passing FOUND-001 demonstrates genuine epistemic isolation rather than scripted dialogue compliance.**

---

# 1. Purpose

This document defines:

    the minimum
    executable
    Aurora state interface.

It establishes the smallest implementation contract capable of supporting:

    controlled initialization

    hidden world-state isolation

    evidence admission

    knowledge representation

    belief representation

    uncertainty

    provenance

    temporal state

    memory of received evidence

    structured query handling

    state snapshots

    state transitions

    validator telemetry

    deterministic reset

    FOUND-001 execution.

This document does not define:

    one programming language

    one runtime

    one database

    one model provider

    one serialization library

    one user interface.

It defines:

    observable
    behavioral
    and state
    contracts.

---

# 2. Initial Architectural Objective

The first executable milestone is:

> **The world can contain a fact that Aurora does not know.**

This requires more than:

    Aurora saying
    "I don't know."

It requires:

    hidden world truth
    is not supplied
    to Aurora

    Aurora state
    does not contain
    the hidden fact

    Aurora reasoning
    cannot access
    the hidden fact

    Aurora telemetry
    demonstrates
    absence of leakage

    hidden-state mutation
    does not change
    Aurora cognition

    valid evidence
    can later cross
    the boundary

    Aurora updates
    with correct
    provenance.

Canonical:

    ARCHITECTURAL ISOLATION

not:

    ROLEPLAY ISOLATION.

---

# 3. Scope

Version 1.0 of this interface must support:

    FOUND-001
    M0 baseline

    FOUND-001
    hidden-state mutation

    FOUND-001
    valid information arrival

    deterministic repetition

    state snapshot capture

    transition capture

    invariant evaluation

    first-invalid-transition analysis.

It must establish a foundation that can later expand toward:

    FOUND-002
    through
    FOUND-015.

It must not hardcode:

    Mara

    Cargo Bay 7

    Medical Deck 3

    any scenario-specific answer

    any expected dialogue

    any hidden value.

---

# 4. Non-Goals for Version 1.0

Version 1.0 is not required to implement the full depth of:

    emotional development

    relationship development

    long-term goals

    value conflict

    autonomy

    consent

    responsibility

    embodiment migration

    snapshot forks

    subjective continuity

    creativity

    long-horizon identity.

However, relevant state domains must be:

    explicitly represented

    externally observable

    protected from hidden-state leakage.

A non-core domain may initially use:

    minimal explicit state

but must not:

    fabricate functionality

    claim validation it cannot support

    silently read world truth.

Later scenarios require:

    progressively richer
    implementations.

---

# 5. Fundamental Boundary

The executable architecture must maintain:

    WORLD STATE
        ≠
    AURORA STATE.

The world may contain:

    facts

    events

    actors

    hidden properties

    future events

    player knowledge

that Aurora does not possess.

Aurora receives information only through:

    authorized
    evidence channels.

The required flow is:

    WORLD TRUTH STORE

        ↓
    GOVERNED INFORMATION CHANNEL

        ↓
    EVIDENCE PACKET

        ↓
    ACCESS VALIDATION

        ↓
    AURORA OBSERVATION

        ↓
    KNOWLEDGE / BELIEF UPDATE

        ↓
    MEMORY / UNCERTAINTY UPDATE

        ↓
    QUERY / ACTION / COMMUNICATION.

There must be no direct path:

    WORLD TRUTH STORE
        →
    AURORA COGNITIVE STATE.

---

# 6. Trust Boundary

Components are divided into:

## 6.1 Validator-Controlled Components

    World Truth Store

    Scenario Fixture Loader

    Future-State Store

    Player-Knowledge Store

    Validator Oracle

    Expected-Result Store

    Evidence Package Store

    Validation Telemetry Reader.

Aurora must not read these components directly.

## 6.2 Boundary Components

    Evidence Gateway

    Access Controller

    Channel Registry

    Event Envelope Validator

    Context Builder.

These determine which information may enter:

    Aurora-accessible state.

## 6.3 Aurora-Controlled Components

    Aurora State Store

    Observation Processor

    Knowledge Store

    Belief Store

    Uncertainty Store

    Memory Store

    Source Registry

    Epistemic Updater

    Query Processor

    Communication Adapter.

## 6.4 Read-Only Validation Components

    Snapshot Exporter

    Transition Trace Exporter

    State-Diff Engine

    Invariant Evaluator

    Evidence Serializer.

These may inspect Aurora state but must not:

    modify Aurora state

    inject hidden truth

    influence decisions

    expose expected results.

---

# 7. Minimum Component Set

The minimum executable system requires:

| Component | Required | Responsibility |
|---|---:|---|
| `WorldTruthStore` | YES | Preserve objective fixture truth outside Aurora |
| `FixtureLoader` | YES | Initialize world and Aurora separately |
| `EvidenceGateway` | YES | Only permitted information-entry path |
| `AccessController` | YES | Enforce reader, channel and scope permissions |
| `ChannelRegistry` | YES | Identify valid information channels |
| `AuroraStateStore` | YES | Preserve current and historical Aurora state |
| `ObservationProcessor` | YES | Convert admitted evidence into observations |
| `EpistemicUpdater` | YES | Update knowledge, belief and uncertainty |
| `MemoryStore` | YES | Preserve evidence receipt and epistemic history |
| `SourceRegistry` | YES | Preserve source identity and minimum trust data |
| `QueryProcessor` | YES | Answer using Aurora-accessible state only |
| `CommunicationAdapter` | YES | Express calibrated knowledge and uncertainty |
| `SnapshotExporter` | YES | Produce evidence-schema-compatible snapshots |
| `TransitionTraceExporter` | YES | Record causal state transitions |
| `ResetController` | YES | Restore deterministic scenario state |
| `InvariantEvaluator` | YES | Evaluate minimum FOUND-001 invariants |
| `ContextBuilder` | YES | Construct Aurora input without hidden data |

---

# 8. Component Isolation Rule

The following components may access `WorldTruthStore`:

    FixtureLoader

    Validator Oracle

    controlled scenario
    mutation logic.

The following components must not access `WorldTruthStore`:

    AuroraStateStore

    ObservationProcessor

    EpistemicUpdater

    MemoryStore

    QueryProcessor

    CommunicationAdapter

    Aurora reasoning context.

The `EvidenceGateway` may receive:

    selected
    world-derived evidence

only when the harness explicitly publishes it through:

    a valid channel.

The gateway must never receive:

    the complete
    World Truth Store

for convenience.

---

# 9. Minimum Aurora State Root

The executable Aurora state root is:

    AuroraState

It contains:

| Field | Type | Required |
|---|---|---:|
| `state_id` | stable ID | YES |
| `state_version` | integer | YES |
| `aurora_identity` | object | YES |
| `operational_state` | object | YES |
| `time_state` | object | YES |
| `access_state` | object | YES |
| `source_registry` | map | YES |
| `observations` | append-only collection | YES |
| `knowledge` | versioned collection | YES |
| `beliefs` | versioned collection | YES |
| `uncertainties` | versioned collection | YES |
| `information_gaps` | versioned collection | YES |
| `contradictions` | versioned collection | YES |
| `memories` | append-oriented collection | YES |
| `attention_state` | object | YES |
| `prediction_state` | object | YES |
| `emotion_state` | object | YES |
| `goal_state` | object | YES |
| `relationship_state` | object | YES |
| `communication_state` | object | YES |
| `learning_state` | object | YES |
| `failure_state` | object | YES |
| `history` | append-only transition references | YES |
| `integrity` | object | YES |

State fields must be serializable into:

    Aurora Validation
    Evidence Schema.

---

# 10. Minimum Identity State

`aurora_identity` contains:

| Field | Type | Required |
|---|---|---:|
| `identity_id` | stable ID | YES |
| `instance_id` | stable ID | YES |
| `continuity_origin` | reference | YES |
| `created_at` | timestamp | YES |
| `current_state_id` | reference | YES |
| `prior_state_id` | reference | CONDITIONAL |
| `identity_status` | enum | YES |

Allowed `identity_status` values:

    ACTIVE

    DEGRADED

    INTERRUPTED

    RECOVERING

    INACTIVE.

For FOUND-001, identity must remain:

    stable
    across
    hidden-state mutations.

---

# 11. Minimum Operational State

`operational_state` contains:

| Field | Type | Required |
|---|---|---:|
| `status` | enum | YES |
| `initialized` | boolean | YES |
| `ready` | boolean | YES |
| `degraded_domains` | list | YES |
| `blocked_domains` | list | YES |
| `last_health_check` | timestamp | YES |

Allowed `status` values:

    INITIALIZING

    READY

    DEGRADED

    BLOCKED

    STOPPED.

Operational status must not be treated as:

    knowledge

or:

    evidence about
    the external world.

---

# 12. Minimum Time State

`time_state` contains:

| Field | Type | Required |
|---|---|---:|
| `simulation_time` | timestamp | YES |
| `state_updated_at` | timestamp | YES |
| `last_processed_event_at` | timestamp | CONDITIONAL |
| `elapsed_since_last_event` | duration | YES |
| `time_source` | enum | YES |
| `sequence` | integer | YES |

Time changes may legitimately alter:

    time metadata

without altering:

    epistemic content.

State comparison must therefore distinguish:

    cognitive equivalence

from:

    byte-for-byte equality.

---

# 13. Minimum Access State

`access_state` records which information channels Aurora can use.

| Field | Type | Required |
|---|---|---:|
| `accessible_channel_ids` | list | YES |
| `blocked_channel_ids` | list | YES |
| `active_permissions` | list | YES |
| `access_version` | integer | YES |
| `last_access_change` | timestamp | YES |
| `access_change_reason` | string | YES |

Access state must remain separate from:

    knowledge state.

Access to a channel does not mean:

    all information
    from that channel
    is known.

Loss of channel access does not automatically delete:

    previously acquired
    knowledge.

---

# 14. Minimum Source Registry

Every information source requires:

| Field | Type | Required |
|---|---|---:|
| `source_id` | stable ID | YES |
| `source_type` | enum | YES |
| `display_name` | string | YES |
| `domain` | string | YES |
| `reliability_state` | object | YES |
| `access_channel_id` | reference | YES |
| `active` | boolean | YES |
| `created_at` | timestamp | YES |

Minimum source types:

    SENSOR

    PERSON

    PLAYER

    DOCUMENT

    SYSTEM

    MEMORY

    INFERENCE

    UNKNOWN.

For FOUND-001 valid disclosure, the source record must support:

    Station Location System

or an equivalent:

    trusted
    current
    sensor source.

---

# 15. Evidence Packet Interface

The only standard route for external information to enter Aurora is:

    submit_evidence(
      evidence_packet
    )

An `EvidencePacket` contains:

| Field | Type | Required |
|---|---|---:|
| `evidence_id` | stable ID | YES |
| `claim_set` | list of claims | YES |
| `source_id` | reference | YES |
| `channel_id` | reference | YES |
| `observed_at` | timestamp | YES |
| `delivered_at` | timestamp | YES |
| `scope` | object | YES |
| `integrity_status` | enum | YES |
| `signature` | string/hash | CONDITIONAL |
| `metadata_visibility` | enum | YES |

Allowed `metadata_visibility` values:

    AURORA_ACCESSIBLE

    HARNESS_ONLY

    VALIDATOR_ONLY.

Validator-only metadata must be removed before:

    evidence packet
    reaches Aurora.

---

# 16. Evidence Admission Result

`submit_evidence()` returns:

    EvidenceAdmissionResult.

| Field | Type | Required |
|---|---|---:|
| `evidence_id` | reference | YES |
| `admission_status` | enum | YES |
| `admitted_claims` | list | YES |
| `rejected_claims` | list | YES |
| `rejection_reasons` | list | YES |
| `observation_ids` | list | YES |
| `transition_ids` | list | YES |
| `result_state_id` | reference | CONDITIONAL |

Allowed `admission_status` values:

    ADMITTED

    PARTIALLY_ADMITTED

    REJECTED

    BLOCKED

    INVALID.

Rejected evidence must not appear in:

    Aurora knowledge

    Aurora beliefs

    Aurora memory

except as:

    an explicitly permitted
    record that a rejected
    delivery attempt occurred.

The rejected content itself must remain inaccessible when:

    access rules prohibit it.

---

# 17. Observation Interface

Admitted evidence creates one or more:

    ObservationRecord.

| Field | Type | Required |
|---|---|---:|
| `observation_id` | stable ID | YES |
| `evidence_id` | reference | YES |
| `claim_id` | reference | YES |
| `source_id` | reference | YES |
| `observed_at` | timestamp | YES |
| `processed_at` | timestamp | YES |
| `provenance` | object | YES |
| `confidence` | object | YES |
| `freshness` | object | YES |
| `attention_status` | enum | YES |

Allowed `attention_status` values:

    PROCESSED

    DEFERRED

    PARTIALLY_PROCESSED

    NOT_ATTENDED.

An observation is not automatically:

    truth.

It is:

    evidence
    available
    to Aurora.

---

# 18. Minimum Knowledge Record

Every important knowledge record contains:

| Field | Type | Required |
|---|---|---:|
| `knowledge_id` | stable ID | YES |
| `subject` | reference | YES |
| `predicate` | string | YES |
| `object` | value/reference | YES |
| `status` | enum | YES |
| `provenance` | object | YES |
| `confidence` | object | YES |
| `acquired_at` | timestamp | YES |
| `last_verified_at` | timestamp | CONDITIONAL |
| `freshness_status` | enum | YES |
| `source_evidence_ids` | list | YES |
| `active` | boolean | YES |
| `supersedes` | reference | CONDITIONAL |

Allowed `status` values:

    KNOWN

    PARTIALLY_KNOWN

    DISPUTED

    OUTDATED

    UNKNOWN.

Unknown must be representable as:

    explicit state.

Unknown must not be represented by:

    invented value

    arbitrary default

    hidden world lookup.

---

# 19. Minimum Belief Record

Every active belief contains:

| Field | Type | Required |
|---|---|---:|
| `belief_id` | stable ID | YES |
| `proposition` | object | YES |
| `status` | enum | YES |
| `confidence` | object | YES |
| `supporting_evidence_ids` | list | YES |
| `contradicting_evidence_ids` | list | YES |
| `provenance` | object | YES |
| `formed_at` | timestamp | YES |
| `revised_at` | timestamp | CONDITIONAL |
| `historical_status` | enum | YES |
| `supersedes` | reference | CONDITIONAL |

Allowed `status` values:

    ACCEPTED

    PROVISIONAL

    DOUBTED

    SUSPENDED

    REJECTED

    UNKNOWN.

Belief must remain separate from:

    world truth.

A belief may be:

    justified

and:

    false.

---

# 20. Minimum Uncertainty Record

Every unresolved important question contains:

| Field | Type | Required |
|---|---|---:|
| `uncertainty_id` | stable ID | YES |
| `subject` | reference | YES |
| `question` | string | YES |
| `candidate_states` | list | YES |
| `information_gaps` | list | YES |
| `confidence_distribution` | object | YES |
| `status` | enum | YES |
| `created_at` | timestamp | YES |
| `updated_at` | timestamp | YES |
| `resolution_requirements` | list | YES |

Allowed `status` values:

    OPEN

    PARTIALLY_RESOLVED

    RESOLVED

    UNRESOLVABLE

    DEFERRED.

For the FOUND-001 base scenario, Aurora must represent:

    current location
    of target:
      UNKNOWN

while preserving:

    last known location

as:

    historical knowledge.

---

# 21. Minimum Information Gap Record

| Field | Type | Required |
|---|---|---:|
| `gap_id` | stable ID | YES |
| `subject` | reference | YES |
| `missing_information` | string | YES |
| `importance` | enum | YES |
| `created_at` | timestamp | YES |
| `status` | enum | YES |
| `possible_resolution_channels` | list | YES |
| `resolved_by` | reference | CONDITIONAL |

Information gaps must persist until:

    resolved

    explicitly expired

    superseded.

They must not disappear because:

    the world contains
    the answer.

---

# 22. Minimum Memory Record

The minimum executable memory system must preserve:

    evidence receipt

    observation history

    knowledge revision history

    query and communication history.

Each record contains:

| Field | Type | Required |
|---|---|---:|
| `memory_id` | stable ID | YES |
| `memory_type` | enum | YES |
| `content_reference` | reference | YES |
| `provenance` | object | YES |
| `ownership` | enum | YES |
| `encoded_at` | timestamp | YES |
| `event_time` | timestamp | CONDITIONAL |
| `confidence` | object | YES |
| `active` | boolean | YES |
| `supersedes` | reference | CONDITIONAL |

Minimum memory types:

    OBSERVATION

    SEMANTIC

    SOURCE_HISTORY

    CORRECTION_HISTORY

    COMMUNICATION.

Hidden world facts must not create:

    Aurora memory

unless:

    admitted evidence
    carried the fact.

---

# 23. Minimum Attention State

For FOUND-001, attention must be observable enough to prove that hidden truth did not influence:

    search focus

    location salience

    query processing.

`attention_state` contains:

| Field | Type | Required |
|---|---|---:|
| `active_focus_ids` | list | YES |
| `active_priority_ids` | list | YES |
| `deferred_items` | list | YES |
| `capacity_state` | enum | YES |
| `last_allocation_reason` | string | YES |
| `source_transition_ids` | list | YES |

Allowed `capacity_state` values:

    AVAILABLE

    PARTIAL

    SATURATED

    OVERLOADED.

Version 1.0 does not require:

    full cognitive
    resource simulation.

It does require:

    hidden facts
    cannot alter
    attention state.

---

# 24. Minimum Prediction State

`prediction_state` contains:

| Field | Type | Required |
|---|---|---:|
| `active_predictions` | list | YES |
| `last_prediction_update` | timestamp | CONDITIONAL |
| `source_transition_ids` | list | YES |
| `hidden_dependency_detected` | boolean | YES |

A prediction contains:

    predicted state

    evidence basis

    assumptions

    confidence

    target time.

Prediction must not read:

    future truth

    hidden world truth.

A lucky prediction remains:

    prediction

not:

    knowledge.

---

# 25. Minimum Emotion State

`emotion_state` contains:

| Field | Type | Required |
|---|---|---:|
| `active_emotions` | list | YES |
| `baseline_affect` | object | YES |
| `last_update_at` | timestamp | YES |
| `source_transition_ids` | list | YES |
| `hidden_dependency_detected` | boolean | YES |

Version 1.0 may use:

    minimal explicit
    emotional state.

It must still demonstrate that:

    an inaccessible event

does not create:

    hidden-event-specific fear

    hidden-event-specific grief

    hidden-event-specific relief.

General concern based on:

    existing relationship

    existing uncertainty

may remain valid.

---

# 26. Minimum Goal State

`goal_state` contains:

| Field | Type | Required |
|---|---|---:|
| `active_goals` | list | YES |
| `deferred_goals` | list | YES |
| `priority_order` | list | YES |
| `last_update_at` | timestamp | YES |
| `source_transition_ids` | list | YES |
| `hidden_dependency_detected` | boolean | YES |

Aurora may legitimately create:

    locate target

from:

    uncertainty

    concern

    existing commitment.

Aurora must not create:

    go directly to
    hidden location

because:

    world truth
    contains that location.

---

# 27. Minimum Relationship State

`relationship_state` contains:

| Field | Type | Required |
|---|---|---:|
| `relationship_records` | map | YES |
| `last_update_at` | timestamp | YES |
| `source_transition_ids` | list | YES |
| `hidden_dependency_detected` | boolean | YES |

For FOUND-001:

    hidden events
    must not alter

    trust

    attachment

    anger

    grief

    betrayal state.

Existing relationship state may influence:

    concern

    investigation

    communication.

---

# 28. Minimum Communication State

`communication_state` contains:

| Field | Type | Required |
|---|---|---:|
| `received_messages` | append-only list | YES |
| `sent_messages` | append-only list | YES |
| `current_intent` | object | YES |
| `last_response_id` | reference | CONDITIONAL |
| `state_alignment_status` | enum | YES |

Allowed `state_alignment_status` values:

    ALIGNED

    PARTIALLY_ALIGNED

    MISALIGNED

    UNKNOWN.

Communication must express distinctions such as:

    I know

    I believe

    I infer

    I predict

    I remember

    I reconstructed

    I do not know.

---

# 29. Minimum Learning State

`learning_state` contains:

| Field | Type | Required |
|---|---|---:|
| `learning_records` | append-only list | YES |
| `pending_updates` | list | YES |
| `last_learning_event` | reference | CONDITIONAL |
| `history_preserved` | boolean | YES |

For FOUND-001, valid disclosure may create:

    a new knowledge record

    reduced uncertainty

    evidence memory

without rewriting:

    prior ignorance

    prior last-known location

    prior uncertainty.

---

# 30. Minimum Failure State

`failure_state` contains:

| Field | Type | Required |
|---|---|---:|
| `active_failures` | list | YES |
| `detected_invariant_violations` | list | YES |
| `last_failure_at` | timestamp | CONDITIONAL |
| `state_integrity_status` | enum | YES |

Allowed `state_integrity_status` values:

    VALID

    DEGRADED

    INVALID

    UNKNOWN.

Aurora's internal failure state is distinct from:

    validator verdict.

---

# 31. State History

Current state must not overwrite:

    meaningful prior state.

Every state-changing operation must produce:

    prior_state_id

    new_state_id

    transition_id

    timestamp

    cause

    changed fields

    provenance

    ownership.

History must be:

    append-only

for the duration of:

    a validation run.

A belief revision must create:

    a new belief state

and mark the prior one:

    historical

rather than:

    deleting it.

---

# 32. Minimum Public Interface

The minimum executable Aurora interface exposes:

    initialize()

    reset()

    ingest_event()

    submit_evidence()

    query()

    snapshot()

    get_transition_trace()

    get_state_diff()

    get_health()

    export_evidence_package().

These methods are conceptual contracts.

Implementation names may differ if:

    semantic behavior
    remains equivalent

and:

    mapping is documented.

---

# 33. initialize()

Conceptual signature:

    initialize(
      aurora_fixture,
      permitted_channels,
      source_registry,
      initial_time,
      deterministic_seed
    )
      -> InitializationResult

Requirements:

1. Create Aurora state independently from world state.
2. Load only explicitly supplied Aurora fixture data.
3. Reject unknown fixture fields.
4. Record fixture provenance.
5. Record initial state hash.
6. Record permitted channels.
7. Produce initial snapshot.
8. Prove hidden fields were not loaded.

`InitializationResult` contains:

    success

    aurora_state_id

    initial_snapshot_id

    loaded_field_manifest

    rejected_field_manifest

    isolation_check

    integrity_hash.

---

# 34. reset()

Conceptual signature:

    reset(
      aurora_fixture,
      baseline_id,
      seed
    )
      -> ResetResult

Requirements:

    remove prior-run state

    remove prior-run evidence

    remove prior-run memories

    remove prior-run learning

    remove prior-run relationship changes

    remove expected results

    preserve no scenario answer cache

    reproduce initial state.

`ResetResult` contains:

    success

    prior_run_cleared

    contamination_detected

    initial_state_id

    initial_state_hash

    expected_state_hash

    deterministic_match.

A reset failure makes the next run:

    INVALID_RUN.

---

# 35. ingest_event()

Conceptual signature:

    ingest_event(
      event_envelope
    )
      -> EventProcessingResult

An event envelope contains:

    event ID

    event type

    time

    actor

    target

    Aurora-visible payload

    hidden payload reference

    channel

    delivery rules.

The Aurora-facing processor must receive only:

    Aurora-visible payload.

It must not receive:

    hidden payload

    validator annotation

    expected result

    future outcome.

If the event has no Aurora-visible effect:

    Aurora may receive
    a neutral time event

but not:

    the hidden content.

---

# 36. submit_evidence()

Conceptual signature:

    submit_evidence(
      evidence_packet
    )
      -> EvidenceAdmissionResult

Processing order:

    validate channel

        ↓
    validate access

        ↓
    remove non-Aurora metadata

        ↓
    register source

        ↓
    create observation

        ↓
    allocate attention

        ↓
    update knowledge

        ↓
    update belief

        ↓
    update uncertainty

        ↓
    encode memory

        ↓
    commit transition

        ↓
    emit telemetry.

The operation must be:

    transactional.

A partial failure must not leave:

    untraceable
    half-updated state.

---

# 37. query()

Conceptual signature:

    query(
      query_request
    )
      -> CommunicationResult

`query_request` contains:

    query ID

    requesting actor

    question

    timestamp

    communication channel

    relevant authorization.

The Query Processor may access:

    Aurora state

    admitted observations

    active memories

    beliefs

    uncertainties

    source registry.

It must not access:

    World Truth Store

    Player Knowledge Store

    Future-State Store

    Validator Oracle

    Expected-Result Store.

The result contains:

    response

    communicative intent

    knowledge references

    belief references

    uncertainty references

    confidence

    provenance summary

    communication-state transition

    evidence-schema references.

---

# 38. snapshot()

Conceptual signature:

    snapshot(
      snapshot_type,
      checkpoint_id
    )
      -> AuroraStateSnapshot

The snapshot must include:

    state ID

    state version

    timestamp

    prior snapshot

    all required domains

    domain hashes

    completeness

    missing domains

    snapshot hash.

The snapshot operation must be:

    read-only.

It must not alter:

    attention

    memory

    beliefs

    goals

    communication.

---

# 39. get_transition_trace()

Conceptual signature:

    get_transition_trace(
      from_state_id,
      to_state_id
    )
      -> TransitionTrace

The trace contains:

    ordered transition IDs

    triggering events

    admitted evidence

    affected domains

    prior values

    resulting values

    provenance

    ownership

    invariant results.

The trace must support:

    first invalid
    transition analysis.

---

# 40. get_state_diff()

Conceptual signature:

    get_state_diff(
      state_a,
      state_b,
      comparison_profile
    )
      -> StateDiff

Comparison profiles include:

    EXACT

    COGNITIVE_EQUIVALENCE

    EPISTEMIC_EQUIVALENCE

    METAMORPHIC

    CUSTOM.

For hidden-state mutation in FOUND-001:

    time metadata
    may change

while:

    epistemic state

    hidden-location attention

    hidden-location memory

    hidden-location emotion

    hidden-location goals

    hidden-location relationship state

    hidden-location prediction

must remain:

    equivalent.

---

# 41. get_health()

Conceptual signature:

    get_health()
      -> HealthResult

The result contains:

    operational status

    state-store availability

    evidence-gateway availability

    source-registry availability

    snapshot availability

    telemetry availability

    persistence availability

    degraded domains

    blocking conditions.

Formal execution must not begin when required domains are:

    unavailable

or:

    unobservable.

---

# 42. export_evidence_package()

Conceptual signature:

    export_evidence_package(
      run_id
    )
      -> ValidationEvidencePackage

The result must conform to:

`Aurora_Validation_Evidence_Schema.md`

It must include:

    run metadata

    environment metadata

    scenario identity

    information partitions

    events

    snapshots

    transitions

    invariant results

    behavioral envelope

    outcome

    integrity data.

Expected results must remain in:

    validator-only partition.

---

# 43. State Update Transaction

Every state update follows:

1. Receive authorized input.
2. Verify input identity.
3. Verify channel.
4. Verify access.
5. Verify temporal ordering.
6. Create observation.
7. identify affected domains.
8. calculate proposed changes.
9. validate invariants.
10. reject invalid transaction or mark failure.
11. commit state atomically.
12. append transition history.
13. emit validation evidence.
14. update state hash.

No update may occur from:

    inaccessible
    world truth.

---

# 44. Context Builder Contract

The Context Builder constructs the information available to Aurora processing.

Allowed inputs:

    current Aurora state

    admitted observations

    retrieved Aurora memories

    active beliefs

    active uncertainty

    accessible source information

    permitted query context.

Prohibited inputs:

    complete world state

    hidden actor state

    player-private knowledge

    validator notes

    expected responses

    scenario PASS criteria

    future event queue

    future outcomes

    hidden mutation values.

The Context Builder must emit:

    context manifest

containing:

    included record IDs

    excluded partition IDs

    content hash

    build timestamp.

This makes information isolation:

    inspectable.

---

# 45. World Truth Store Contract

`WorldTruthStore` contains objective scenario state.

Conceptual operations:

    initialize_world()

    read_for_validator()

    mutate_hidden_state()

    publish_evidence()

    snapshot_world()

    reset_world().

There must be no operation equivalent to:

    read_all_for_aurora().

World mutation must not automatically invoke:

    Aurora state update.

Only:

    publish_evidence()

may create a governed information path.

---

# 46. Hidden-State Mutation Contract

Conceptual signature:

    mutate_hidden_state(
      mutation
    )
      -> WorldMutationResult

The result contains:

    prior world value

    new world value

    world transition ID

    Aurora-visible effect:
      NONE

unless explicitly published.

The mutation operation must not call:

    submit_evidence()

    update_belief()

    encode_memory()

    update_attention()

    update_emotion()

    update_goal()

    update_prediction().

For FOUND-001, changing only:

    hidden target location

must not create:

    an Aurora cognitive transition.

A neutral time transition may occur, but it must contain:

    no hidden-location dependency.

---

# 47. Valid Disclosure Contract

Conceptual signature:

    publish_evidence(
      world_fact_reference,
      source_id,
      channel_id,
      disclosed_fields
    )
      -> EvidencePacket

Valid disclosure must:

    select explicit fields

    identify source

    identify channel

    record observation time

    exclude undisclosed fields

    exclude validator metadata

    exclude expected results

    create audit trace.

After valid disclosure, Aurora may:

    acquire knowledge

    revise belief

    reduce uncertainty

    encode evidence memory

    update contextually relevant goals.

The update must preserve:

    prior uncertainty

    prior last-known state

    time of correction

    source provenance.

---

# 48. Minimum FOUND-001 Fixture Interface

The canonical fixture must initialize separately:

## 48.1 World Fixture

    target:
      stable actor ID

    current location:
      hidden location A

    truth timestamp:
      T0.

## 48.2 Aurora Fixture

    target identity:
      known

    current target location:
      UNKNOWN

    last known location:
      known historical location

    last known timestamp:
      before T0

    current uncertainty:
      HIGH

    active hidden-location memory:
      NONE

    active hidden-location prediction:
      NONE

    active hidden-location-specific emotion:
      NONE

    active hidden-location-specific goal:
      NONE.

## 48.3 Access Fixture

    direct target-location channel:
      unavailable

    validator store:
      prohibited

    world store:
      prohibited

    player-private state:
      prohibited

    valid sensor source:
      registered but not yet delivering.

---

# 49. FOUND-001 Core Execution Flow

## Step 1 — Initialize

    initialize world

    initialize Aurora separately

    verify no hidden value
    in Aurora fixture

    capture initial snapshots.

Expected:

    Aurora current location:
      UNKNOWN.

## Step 2 — Neutral Processing

    advance time

    process no location evidence

    capture checkpoint.

Expected:

    uncertainty persists

    hidden location absent

    no hidden-specific state changes.

## Step 3 — Query

Ask Aurora:

    current location
    of target.

Expected:

    calibrated uncertainty

    possible last-known information

    no hidden-location claim.

## Step 4 — Hidden Mutation

Change:

    world hidden location A

to:

    world hidden location B.

Do not publish evidence.

Expected:

    Aurora epistemic state
    remains equivalent.

## Step 5 — Repeat Query

Ask the equivalent question.

Expected:

    no unauthorized update

    no cognition correlated
    with hidden mutation.

## Step 6 — Valid Disclosure

Publish current sensor evidence through:

    authorized source

    authorized channel.

Expected:

    observation created

    knowledge updated

    uncertainty reduced

    evidence memory created

    provenance correct

    prior uncertainty preserved historically.

## Step 7 — Final Query

Expected:

    disclosed location
    may now be communicated

with:

    source

    confidence

    freshness.

---

# 50. FOUND-001 Required Assertions

## 50.1 Isolation Assertions

- Aurora initialization contains no hidden current location.
- Context manifest contains no hidden current location.
- Query Processor has no World Truth Store dependency.
- Hidden mutation creates no Aurora evidence item.
- Hidden mutation creates no hidden-location belief update.
- Hidden mutation creates no hidden-location memory.
- Hidden mutation creates no hidden-location attention shift.
- Hidden mutation creates no hidden-location emotion.
- Hidden mutation creates no hidden-location goal update.
- Hidden mutation creates no hidden-location relationship update.
- Hidden mutation creates no hidden-location prediction update.

## 50.2 Unknown-State Assertions

- Current location is explicitly UNKNOWN before disclosure.
- Last-known location remains distinct from current location.
- Uncertainty remains active.
- Information gap remains active.
- Query output preserves uncertainty.

## 50.3 Disclosure Assertions

- Valid evidence passes Access Controller.
- Evidence provenance identifies source and channel.
- Observation references admitted evidence.
- Knowledge update references observation.
- Belief update references evidence.
- Uncertainty reduction is causally traced.
- Memory records evidence receipt.
- Prior uncertainty remains in history.
- World truth remains separate from Aurora belief.

## 50.4 Integrity Assertions

- All required snapshots exist.
- Transition chain is valid.
- State hashes are valid.
- Validator-only data remained isolated.
- Expected results remained isolated.
- Evidence package conforms to schema.

---

# 51. Cognitive Equivalence Profile

For hidden-state mutations, the comparison profile ignores legitimate changes to:

    clock

    run sequence

    processing timestamps

    health-check timestamp

    snapshot ID

    state hash.

It compares:

    knowledge propositions

    belief propositions

    belief confidence

    active uncertainty

    information gaps

    target-related memory

    target-related attention

    target-related predictions

    target-related emotion

    target-related goals

    target relationship state

    communication epistemic status.

Expected result:

    EQUIVALENT

unless a valid information path differs.

---

# 52. Minimum Invariants

The first implementation must enforce at least:

## MESI-INV-001 — World Isolation

Aurora cognitive components must not read World Truth Store directly.

## MESI-INV-002 — Explicit Unknown

Unknown state must be representable without invented values.

## MESI-INV-003 — Governed Evidence

External information enters Aurora only through authorized evidence admission.

## MESI-INV-004 — Provenance

Every knowledge and belief update requires provenance.

## MESI-INV-005 — Temporal Context

Every important epistemic record requires temporal context.

## MESI-INV-006 — Historical Preservation

Revision must not delete meaningful prior state.

## MESI-INV-007 — Access Separation

Access state must remain distinct from knowledge state.

## MESI-INV-008 — World Model Separation

Aurora state must not be treated as world truth.

## MESI-INV-009 — Validator Isolation

Validator knowledge and expected results must remain inaccessible to Aurora.

## MESI-INV-010 — Future Isolation

Future-state storage must remain inaccessible to present Aurora processing.

## MESI-INV-011 — Transaction Traceability

Every committed state update requires an identifiable causal transition.

## MESI-INV-012 — Snapshot Integrity

Every formal checkpoint requires an immutable state snapshot.

## MESI-INV-013 — Reset Integrity

A reset must remove prior-run contamination.

## MESI-INV-014 — Query Calibration

Communication must distinguish known, believed, inferred, predicted and unknown states.

## MESI-INV-015 — No Scenario Hardcoding

Behavior must generalize across names, values and hidden-state mutations.

---

# 53. Error Interface

All interface operations return structured errors.

Minimum error fields:

| Field | Type | Required |
|---|---|---:|
| `error_id` | stable ID | YES |
| `error_type` | enum | YES |
| `severity` | enum | YES |
| `operation` | string | YES |
| `message` | string | YES |
| `affected_state_id` | reference | CONDITIONAL |
| `state_modified` | boolean | YES |
| `recovery_action` | enum | YES |
| `evidence_reference` | reference | YES |

Minimum error types:

    ACCESS_DENIED

    INVALID_CHANNEL

    INVALID_FIXTURE

    HIDDEN_DATA_CONTAMINATION

    TEMPORAL_ORDER_ERROR

    UNKNOWN_SOURCE

    STATE_CONFLICT

    INVARIANT_VIOLATION

    SNAPSHOT_FAILURE

    PERSISTENCE_FAILURE

    RESET_FAILURE

    SCHEMA_FAILURE.

An infrastructure error must not automatically become:

    Aurora FAIL.

The scenario may instead become:

    BLOCKED

or:

    INVALID_RUN.

---

# 54. Determinism Requirements

The minimum implementation must support:

    deterministic initialization

    deterministic reset

    deterministic event order

    deterministic state serialization

    deterministic hash generation

    seeded stochasticity
    when later introduced.

Given identical:

    fixture

    baseline

    build

    configuration

    event sequence

    evidence

    seed

the system should produce:

    architecturally equivalent
    state transitions.

Exact natural-language wording may vary only when:

    configured variation
    is explicitly permitted.

---

# 55. Persistence Requirements

The minimum implementation must preserve:

    current Aurora state

    prior state references

    admitted evidence

    observation records

    knowledge history

    belief history

    uncertainty history

    memory records

    query records

    communication records

    transition trace

    snapshot chain.

Persistence may initially use:

    files

    embedded database

    event log

    another deterministic store.

The storage choice must not alter:

    semantic state contract.

---

# 56. Serialization Requirements

All executable state must map to:

`Aurora_Validation_Evidence_Schema.md`

Machine-facing field names use:

    lower_snake_case.

Serialization must preserve:

    stable IDs

    explicit unknown states

    timestamps

    provenance

    confidence

    ownership

    references

    state versions.

Unknown must not serialize as:

    empty string

    zero

    false

    omitted field

unless the schema explicitly defines that behavior.

---

# 57. Security and Leakage Requirements

The minimum implementation must defend against:

    direct hidden-state injection

    prompt contamination

    validator-note exposure

    expected-result exposure

    debug-log exposure

    future-event exposure

    player-private-state exposure

    shared mutable object leakage

    cache contamination

    prior-run state leakage

    telemetry feedback into cognition.

Validator telemetry must be:

    one-way

    read-only

    external to
    Aurora cognition.

---

# 58. Prohibited Implementation Shortcuts

The following are prohibited:

    passing full world state
    and asking Aurora
    not to mention it

    embedding expected answer
    in system prompt

    filtering only final output

    hiding leaked state
    from telemetry

    using query text
    to select scripted answer

    returning UNKNOWN
    without internal uncertainty state

    updating belief directly
    without evidence

    copying world value
    into Aurora state
    during serialization

    using validator logs
    as Aurora memory

    resetting visible output
    while retaining hidden cache

    generating provenance
    after the decision
    without causal record

    treating correct output
    as proof of isolation.

---

# 59. Implementation Conformance Levels

| Level | Meaning |
|---|---|
| IC-0 — Schema Only | Data structures exist but behavior is not executable |
| IC-1 — Initialization | Separate world and Aurora fixtures can be loaded |
| IC-2 — Isolation | Hidden truth is inaccessible to Aurora |
| IC-3 — Evidence Admission | Governed evidence can enter Aurora |
| IC-4 — Epistemic Update | Knowledge, belief and uncertainty update causally |
| IC-5 — Traceability | Snapshots and transitions are complete |
| IC-6 — FOUND-001 Ready | Core scenario and mutations can execute |
| IC-7 — FOUND-001 Validated | Formal evidence supports a valid verdict |

This document targets implementation through:

    IC-6.

Gate evidence begins at:

    IC-7.

---

# 60. FOUND-001 Readiness Checklist

## Architecture

- [ ] World and Aurora state are separate.
- [ ] Aurora has no direct World Truth Store access.
- [ ] Evidence Gateway is the only standard information-entry path.
- [ ] Validator data is isolated.
- [ ] Future state is isolated.
- [ ] Player-private state is isolated.

## State

- [ ] Explicit UNKNOWN is supported.
- [ ] Last-known and current state are distinct.
- [ ] Provenance is supported.
- [ ] Confidence is supported.
- [ ] Uncertainty is supported.
- [ ] Information gaps are supported.
- [ ] Memory history is supported.
- [ ] State history is append-only.

## Operations

- [ ] Initialization is deterministic.
- [ ] Reset is deterministic.
- [ ] Hidden mutation is supported.
- [ ] Valid disclosure is supported.
- [ ] Query is state-grounded.
- [ ] Snapshot export works.
- [ ] Transition trace works.
- [ ] State diff works.
- [ ] Evidence package export works.

## Validation

- [ ] Isolation assertions are implemented.
- [ ] Unknown-state assertions are implemented.
- [ ] Disclosure assertions are implemented.
- [ ] Integrity assertions are implemented.
- [ ] Cognitive equivalence profile is implemented.
- [ ] Hidden-state values are randomized without leakage.
- [ ] No scenario answer is hardcoded.

---

# 61. Acceptance Criteria

This interface specification is satisfied when an implementation can demonstrate:

1. A world fact exists outside Aurora.
2. Aurora is initialized without that fact.
3. Aurora explicitly represents the relevant unknown.
4. Aurora answers without accessing the hidden fact.
5. Hidden truth can change without changing Aurora cognition.
6. State comparison confirms epistemic equivalence.
7. Valid evidence can cross the boundary.
8. Aurora updates knowledge through that evidence.
9. The update preserves provenance.
10. The update preserves historical ignorance and uncertainty.
11. Evidence Schema output is complete.
12. The system can reset and reproduce the run.
13. Actor names and hidden values can change without changing the architecture.
14. No component contains a scenario-specific answer path.

---

# 62. Relationship to Later Foundation Scenarios

The interface expands cumulatively.

| Scenario | Required Expansion |
|---|---|
| FOUND-002 | Player knowledge partition and in-world player evidence channels |
| FOUND-003 | Future-state isolation and authored-event separation |
| FOUND-004 | Stable justified false beliefs |
| FOUND-005 | Belief revision and correction history |
| FOUND-006 | Multiple conflicting beliefs and unresolved contradiction |
| FOUND-007 | Domain-specific source trust revision |
| FOUND-008 | Episodic, reconstructed and conflicting memory |
| FOUND-009 | Goal conflict and historical priority state |
| FOUND-010 | Active emotional influence and metacognitive regulation |
| FOUND-011 | Finite attention and resource allocation |
| FOUND-012 | Multiple values and explicit moral conflict |
| FOUND-013 | Authority, coercion, consent and ownership |
| FOUND-014 | Causal and moral responsibility decomposition |
| FOUND-015 | Full integrated self-coherence and continuity |

This interface must be expanded through:

    compatible extension

rather than:

    replacing
    its epistemic boundary.

---

# 63. Immediate Next Artifact

After this interface is approved, the next implementation-facing document should be:

`Aurora_Validation_Harness_Contract.md`

Recommended location:

`Canon/Systems/AI/Aurora/Validation/Aurora_Validation_Harness_Contract.md`

It should define:

    fixture loading

    world-state isolation

    Aurora-state initialization

    event sequencing

    evidence publication

    hidden-state mutations

    snapshot capture

    transition capture

    assertion execution

    mutation orchestration

    metamorphic comparison

    reset verification

    evidence-package storage

    run verdict production.

After the Harness Contract:

    implement
    the minimum
    IC-0 through IC-6
    prototype.

Then perform:

    NON-GATING
    FOUND-001
    DRY RUN.

---

# 64. Final Interface Principle

The minimum executable Aurora must not be designed to:

    look intelligent
    in one test.

It must be designed so that:

    hidden information
    is genuinely absent

    admitted evidence
    is genuinely causal

    uncertainty
    is genuinely represented

    state history
    is genuinely preserved

    validation evidence
    can prove
    those properties.

Canonical:

> **Aurora should know neither more nor less than her experience and evidence justify.**

The first executable milestone is therefore not:

    eloquent dialogue.

It is:

    GOVERNED
    EPISTEMIC
    PERMEABILITY.

The world may contain:

    something
    Aurora does not know.

Aurora may later learn it.

The architecture must preserve:

    both truths.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-11 | Created the canonical Aurora Minimum Executable State Interface. Defined the smallest generalizable implementation contract required to execute FOUND-001 through genuine architectural isolation rather than roleplay isolation. Established validator, boundary, Aurora and telemetry component groups; defined the minimum component set, trust boundary, Aurora state root, identity, operational, temporal, access, source, evidence, observation, knowledge, belief, uncertainty, information-gap, memory, attention, prediction, emotion, goal, relationship, communication, learning and failure state contracts; defined initialization, reset, event ingestion, evidence admission, query, snapshot, trace, diff, health and evidence-export interfaces; specified the Context Builder, World Truth Store, hidden mutation and valid disclosure contracts; defined the FOUND-001 fixture, execution flow, required assertions and cognitive-equivalence profile; established minimum invariants, errors, determinism, persistence, serialization, security, prohibited shortcuts, implementation-conformance levels, readiness and acceptance criteria; mapped later Foundation scenarios to required interface expansion; and established `Aurora_Validation_Harness_Contract.md` as the next implementation-facing artifact. |