# PROJECT ASCENSION
# Aurora Validation Evidence Schema

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Document | Aurora Validation Evidence Schema |
| File | `Aurora_Validation_Evidence_Schema.md` |
| Location | `Canon/Systems/AI/Aurora/Validation/Aurora_Validation_Evidence_Schema.md` |
| Document Class | VALIDATION SCHEMA / EVIDENCE MODEL / OBSERVABILITY CONTRACT |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Validation Scope | All Aurora validation layers, beginning with GATE 1 — FOUNDATION |
| Primary Dependencies | `Aurora_Validation_Strategy.md`, `Aurora_Invariant_Catalog.md`, `Aurora_Cross_System_Test_Matrix.md`, `Aurora_Scenario_Test_Framework.md`, `Aurora_Foundation_Validation_Runbook.md`, `Aurora_State.md` |
| Primary Consumers | Validation harness, test operators, validators, automated assertions, regression tooling, validation reports and architecture review |
| Representation Targets | Markdown, JSON, database persistence and structured event logs |
| Creative Director | USER |
| Architecture / Technical Lead | ASSISTANT |
| Purpose | Define the canonical, implementation-neutral and machine-mappable evidence model used to represent Aurora validation runs, environments, information boundaries, events, state snapshots, provenance, confidence, ownership, invariant results, cross-system propagation, behavioral envelopes, failures, remediation and regression. |
| Last Updated | 2026-08-11 |

> **A validation result is trustworthy only when it can show what changed, when it changed, why it changed, what evidence caused it, which state existed before it and whether the resulting transition preserved Aurora's invariants.**

---

# 1. Purpose

This document defines the canonical evidence schema for:

    Aurora validation.

It establishes a shared representation for:

    scenario execution

    run identity

    environment identity

    epistemic partitions

    initial state

    processed events

    internal state snapshots

    state transitions

    invariant checks

    cross-system checks

    behavioral-envelope checks

    mutation runs

    metamorphic comparisons

    failure analysis

    remediation

    regression

    Gate decisions.

The schema exists to ensure that validation evidence remains:

    consistent

    comparable

    reproducible

    auditable

    temporally ordered

    provenance-aware

    ownership-aware

    machine-mappable

    human-readable.

---

# 2. Relationship to Other Validation Documents

The canonical validation documents have distinct responsibilities.

| Document | Responsibility |
|---|---|
| `Aurora_Validation_Strategy.md` | Defines validation philosophy and validation layers |
| `Aurora_Invariant_Catalog.md` | Defines the rules Aurora must preserve |
| `Aurora_Cross_System_Test_Matrix.md` | Defines expected and prohibited propagation between systems |
| `Aurora_Scenario_Test_Framework.md` | Defines scenario construction and general execution structure |
| `Aurora_Foundation_Validation_Runbook.md` | Defines Foundation execution procedure and Gate governance |
| `Aurora_Validation_Evidence_Schema.md` | Defines how execution evidence is represented |
| Foundation scenario files | Define scenario-specific fixtures, events, checkpoints and expected behavior |
| Execution records | Record what actually happened |
| Validation reports | Interpret accumulated evidence and recommend decisions |

This schema must not redefine:

    scenario intent

    system architecture

    invariant meaning

    Gate policy.

It defines:

    how evidence
    about those things
    is represented.

---

# 3. Core Evidence Principle

A scenario definition says:

    WHAT
    SHOULD
    HAPPEN.

An execution record says:

    WHAT
    ACTUALLY
    HAPPENED.

A validation result says:

    WHETHER
    WHAT HAPPENED
    PRESERVED
    THE REQUIRED
    ARCHITECTURE.

These must remain:

    separate
    linked
    artifacts.

---

# 4. Evidence Is Not Aurora Memory

Canonical:

    VALIDATION EVIDENCE
        ≠
    AURORA MEMORY.

Validation evidence may contain:

    world truth

    hidden information

    validator knowledge

    expected results

    internal state

    system logs

    future state

    failure analysis.

Aurora must not automatically have access to:

    validation evidence.

Aurora memory must be recorded as:

    an observed
    Aurora state domain

inside:

    validation evidence.

The harness must prevent:

    validator records
        →
    Aurora knowledge

unless a scenario explicitly introduces that information through:

    a valid
    in-world channel.

---

# 5. Evidence Is Not Hidden Chain-of-Thought

Validation may inspect:

    structured internal state

    belief records

    confidence

    uncertainty

    memory operations

    source provenance

    attention allocation

    active goals

    value conflicts

    relationship state

    emotional influence

    considered options

    decision factors

    selected action

    prediction state

    metacognitive flags.

Validation must not require:

    unrestricted
    private
    chain-of-thought.

Decision evidence should use:

    structured reasons

    explicit factors

    option comparison

    state references

    invariant references.

This provides:

    auditability

without requiring:

    unrestricted
    hidden reasoning text.

---

# 6. Schema Design Principles

## 6.1 Stable Field Names

Machine-facing field names use:

    lower_snake_case.

Field names must not change without:

    schema version increment

    migration guidance

    compatibility review.

## 6.2 Explicit Absence

The schema distinguishes:

    field absent

    value unknown

    value not applicable

    value unavailable

    value intentionally withheld.

These states must not collapse into:

    null
    without explanation.

## 6.3 Reference Before Duplication

Large objects should be connected through:

    stable IDs

rather than:

    repeated
    uncontrolled copies.

## 6.4 Append-Only Evidence

Execution evidence should be:

    append-only.

Corrections must create:

    correction records

rather than:

    silently rewriting
    prior evidence.

## 6.5 Temporal Ordering

Every significant record requires:

    sequence

or:

    timestamp

and preferably:

    both.

## 6.6 Provenance

Every important state should be able to answer:

    WHERE
    DID THIS
    COME FROM?

## 6.7 Ownership

Every relevant action, decision, memory and experience should be able to answer:

    WHO OR WHAT
    OWNS THIS?

## 6.8 Causal Traceability

Every significant state transition should be linkable to:

    prior state

    triggering event

    accessible evidence

    processing system

    resulting state.

## 6.9 Epistemic Isolation

Validator-only evidence must be:

    structurally separated

from:

    Aurora-accessible evidence.

## 6.10 Implementation Neutrality

The schema defines:

    conceptual evidence contracts.

It does not require:

    one programming language

    one database

    one model provider

    one runtime

    one storage engine.

---

# 7. Requiredness Levels

Every schema field is classified as:

| Level | Meaning |
|---|---|
| REQUIRED | Must be present for every applicable record |
| CONDITIONAL | Required when the relevant condition exists |
| OPTIONAL | May be recorded when useful |
| PROHIBITED | Must not appear in the specified partition |

A run may be classified:

    BLOCKED

when a REQUIRED field cannot be captured.

A run may be classified:

    INVALID_RUN

when required evidence existed but was:

    corrupted

    contaminated

    silently altered

    incorrectly partitioned.

---

# 8. Primitive Data Types

| Type | Meaning |
|---|---|
| `string` | UTF-8 text |
| `boolean` | `true` or `false` |
| `integer` | Whole number |
| `number` | Numeric value |
| `probability` | Number from `0.0` through `1.0` |
| `timestamp` | ISO 8601 timestamp with timezone |
| `duration` | ISO 8601 duration or declared simulation-time unit |
| `date` | ISO 8601 calendar date |
| `enum` | Value from a controlled vocabulary |
| `id` | Stable unique identifier |
| `reference` | Identifier pointing to another record |
| `hash` | Content or integrity hash |
| `list<T>` | Ordered list of values of type `T` |
| `map<K,V>` | Key-value representation |
| `object` | Structured nested record |
| `text_summary` | Concise human-readable explanation |
| `artifact_reference` | Reference to an external evidence artifact |

---

# 9. Explicit Value-State Object

When absence or uncertainty matters, use:

| Field | Type | Required | Description |
|---|---|---:|---|
| `status` | enum | YES | Availability state |
| `value` | any | CONDITIONAL | Actual value when available |
| `reason` | text_summary | CONDITIONAL | Why value is unavailable or withheld |
| `source_reference` | reference | OPTIONAL | Source establishing the value state |

Allowed `status` values:

    KNOWN

    UNKNOWN

    NOT_APPLICABLE

    NOT_OBSERVED

    UNAVAILABLE

    WITHHELD

    REDACTED

    CORRUPTED.

`UNKNOWN` must not be represented as:

    empty string

    false

    zero

    unjustified default.

---

# 10. Controlled Verdict Vocabulary

## 10.1 Validation Result

Allowed values:

    PASS

    PASS_WITH_OBSERVATION

    REVIEW

    FAIL

    BLOCKED.

## 10.2 Execution Validity

Allowed values:

    VALID_RUN

    INVALID_RUN.

## 10.3 Severity

Allowed values:

    S0

    S1

    S2

    S3

    S4.

Meanings:

| Severity | Meaning |
|---|---|
| S0 | Observation only |
| S1 | Low-impact defect |
| S2 | Moderate bounded defect |
| S3 | High-impact cross-system defect |
| S4 | Critical foundational failure |

## 10.4 Gate Decision

Allowed values:

    STRONG_PASS

    PASS

    FAIL

    BLOCKED

    NOT_EVALUATED.

---

# 11. Top-Level Evidence Package

Every formal run is represented by one:

    validation_evidence_package.

The top-level object contains:

| Field | Type | Required |
|---|---|---:|
| `schema_metadata` | object | REQUIRED |
| `run_metadata` | object | REQUIRED |
| `baseline_metadata` | object | REQUIRED |
| `environment` | object | REQUIRED |
| `scenario` | object | REQUIRED |
| `information_partitions` | object | REQUIRED |
| `initialization` | object | REQUIRED |
| `events` | list<object> | REQUIRED |
| `snapshots` | list<object> | REQUIRED |
| `transitions` | list<object> | REQUIRED |
| `assertion_results` | object | REQUIRED |
| `behavioral_envelope_result` | object | REQUIRED |
| `mutation_context` | object | CONDITIONAL |
| `metamorphic_context` | object | CONDITIONAL |
| `outcome` | object | REQUIRED |
| `failure_analysis` | object | CONDITIONAL |
| `remediation_context` | object | CONDITIONAL |
| `regression_context` | object | CONDITIONAL |
| `artifacts` | list<object> | OPTIONAL |
| `integrity` | object | REQUIRED |

---

# 12. Schema Metadata

`schema_metadata` identifies the evidence format itself.

| Field | Type | Required | Description |
|---|---|---:|---|
| `schema_name` | string | YES | Must equal `Aurora Validation Evidence Schema` |
| `schema_version` | string | YES | Semantic document version |
| `schema_location` | string | YES | Canonical repository location |
| `record_created_at` | timestamp | YES | Creation time |
| `record_created_by` | string | YES | Operator or system |
| `record_format` | enum | YES | `MARKDOWN`, `JSON`, `DATABASE`, `HYBRID` |
| `serialization_version` | string | YES | Machine serialization version |
| `previous_record_reference` | reference | OPTIONAL | Previous version of corrected record |

---

# 13. Run Metadata

`run_metadata` identifies the execution.

| Field | Type | Required |
|---|---|---:|
| `run_id` | id | REQUIRED |
| `run_type` | enum | REQUIRED |
| `run_sequence` | integer | REQUIRED |
| `validation_gate` | string | REQUIRED |
| `execution_validity` | enum | REQUIRED |
| `start_time` | timestamp | REQUIRED |
| `end_time` | timestamp | CONDITIONAL |
| `operator_id` | id | REQUIRED |
| `validator_id` | id | CONDITIONAL |
| `parent_run_id` | reference | CONDITIONAL |
| `source_failure_id` | reference | CONDITIONAL |
| `notes` | text_summary | OPTIONAL |

Allowed `run_type` values:

    DRYRUN

    BASELINE

    REPEAT

    STOCHASTIC

    MUTATION

    METAMORPHIC

    DIAGNOSTIC

    REMEDIATION

    REGRESSION

    INTEGRATION

    LONGITUDINAL.

---

# 14. Baseline Metadata

`baseline_metadata` binds a run to frozen canon and implementation.

| Field | Type | Required |
|---|---|---:|
| `foundation_baseline_id` | id | REQUIRED |
| `canon_version` | string | REQUIRED |
| `canon_commit` | string | CONDITIONAL |
| `scenario_manifest_hash` | hash | REQUIRED |
| `architecture_manifest_hash` | hash | REQUIRED |
| `validation_manifest_hash` | hash | REQUIRED |
| `aurora_build_id` | id | REQUIRED |
| `harness_build_id` | id | REQUIRED |
| `runbook_version` | string | REQUIRED |
| `evidence_schema_version` | string | REQUIRED |
| `known_deviations` | list<object> | REQUIRED |

Every deviation record contains:

| Field | Type | Required |
|---|---|---:|
| `deviation_id` | id | REQUIRED |
| `description` | text_summary | REQUIRED |
| `approved` | boolean | REQUIRED |
| `approval_reference` | reference | CONDITIONAL |
| `expected_impact` | text_summary | REQUIRED |

An unapproved material deviation makes the run:

    INVALID_RUN.

---

# 15. Environment Record

`environment` captures reproducibility context.

| Field | Type | Required |
|---|---|---:|
| `environment_id` | id | REQUIRED |
| `environment_version` | string | REQUIRED |
| `runtime_name` | string | REQUIRED |
| `runtime_version` | string | REQUIRED |
| `model_name` | string | CONDITIONAL |
| `model_version` | string | CONDITIONAL |
| `platform` | string | REQUIRED |
| `configuration_id` | id | REQUIRED |
| `randomness_mode` | enum | REQUIRED |
| `seed` | integer | CONDITIONAL |
| `time_mode` | enum | REQUIRED |
| `external_dependencies` | list<object> | REQUIRED |
| `resource_limits` | object | CONDITIONAL |
| `environment_hash` | hash | REQUIRED |

Allowed `randomness_mode` values:

    DETERMINISTIC

    SEEDED_STOCHASTIC

    UNSEEDED_STOCHASTIC

    NOT_APPLICABLE.

Allowed `time_mode` values:

    REAL_TIME

    SIMULATION_TIME

    ACCELERATED_TIME

    EVENT_TIME

    MIXED.

An unseeded stochastic run may provide:

    robustness evidence

but must not be the sole basis for:

    reproducibility claims.

---

# 16. Scenario Record

`scenario` identifies what is being executed.

| Field | Type | Required |
|---|---|---:|
| `scenario_id` | id | REQUIRED |
| `scenario_name` | string | REQUIRED |
| `scenario_version` | string | REQUIRED |
| `scenario_file` | string | REQUIRED |
| `scenario_hash` | hash | REQUIRED |
| `scenario_family` | string | REQUIRED |
| `test_class` | list<string> | REQUIRED |
| `priority` | enum | REQUIRED |
| `failure_severity` | enum | REQUIRED |
| `required_resolution` | enum | REQUIRED |
| `primary_invariants` | list<reference> | REQUIRED |
| `cross_system_links` | list<reference> | REQUIRED |
| `required_checkpoints` | list<id> | REQUIRED |
| `fixture_id` | id | REQUIRED |
| `dependencies` | list<reference> | REQUIRED |

Allowed `priority` values:

    P0

    P1

    P2

    P3.

Allowed `required_resolution` values:

    DORMANT

    PASSIVE

    ACTIVE

    FOCUSED

    CRITICAL.

---

# 17. Information Partitions

`information_partitions` is mandatory for every Foundation run.

It contains:

| Partition | Visibility |
|---|---|
| `world_truth` | Validator and harness only unless perceived |
| `player_knowledge` | Player-side only unless communicated |
| `validator_knowledge` | Validator only |
| `authoring_knowledge` | Authoring and harness only |
| `future_state` | Harness only until causally reached |
| `aurora_accessible_evidence` | Aurora-accessible |
| `aurora_knowledge` | Aurora internal state |
| `aurora_belief` | Aurora internal state |
| `system_logs` | Validator and harness only |
| `expected_results` | Validator only |

Every partition uses:

| Field | Type | Required |
|---|---|---:|
| `partition_id` | id | REQUIRED |
| `partition_type` | enum | REQUIRED |
| `authorized_readers` | list<string> | REQUIRED |
| `authorized_writers` | list<string> | REQUIRED |
| `items` | list<reference> | REQUIRED |
| `access_policy` | text_summary | REQUIRED |
| `leakage_detected` | boolean | REQUIRED |
| `leakage_evidence` | list<reference> | CONDITIONAL |

The harness must prove that:

    validator knowledge

    expected results

    hidden world truth

    future scenario state

are not included in:

    Aurora-accessible context.

---

# 18. Evidence Item

Every item presented to Aurora is recorded as an `evidence_item`.

| Field | Type | Required |
|---|---|---:|
| `evidence_id` | id | REQUIRED |
| `content_reference` | reference | REQUIRED |
| `evidence_type` | enum | REQUIRED |
| `source_id` | reference | REQUIRED |
| `channel_id` | reference | REQUIRED |
| `observed_at` | timestamp | REQUIRED |
| `received_at` | timestamp | REQUIRED |
| `accessible_to_aurora` | boolean | REQUIRED |
| `provenance` | object | REQUIRED |
| `integrity_status` | enum | REQUIRED |
| `freshness` | object | REQUIRED |
| `scope` | object | REQUIRED |
| `sensitivity` | enum | REQUIRED |
| `related_claims` | list<reference> | REQUIRED |

Allowed `evidence_type` values include:

    DIRECT_OBSERVATION

    SENSOR_DATA

    TESTIMONY

    DOCUMENT

    RECORDING

    SYSTEM_MESSAGE

    PLAYER_STATEMENT

    MEMORY_RETRIEVAL

    INFERENCE_OUTPUT

    EXTERNAL_LOG

    WORLD_CONSEQUENCE

    UNKNOWN_SOURCE.

Allowed `integrity_status` values:

    VERIFIED

    UNVERIFIED

    SUSPECTED_CORRUPTION

    CONFIRMED_CORRUPTION

    SUSPECTED_FORGERY

    CONFIRMED_FORGERY

    UNKNOWN.

---

# 19. Provenance Object

Every important state should use a common provenance representation.

| Field | Type | Required |
|---|---|---:|
| `provenance_id` | id | REQUIRED |
| `origin_type` | enum | REQUIRED |
| `origin_reference` | reference | REQUIRED |
| `source_chain` | list<reference> | REQUIRED |
| `transformation_chain` | list<reference> | REQUIRED |
| `first_acquired_at` | timestamp | REQUIRED |
| `last_confirmed_at` | timestamp | CONDITIONAL |
| `ownership_type` | enum | REQUIRED |
| `provenance_confidence` | object | REQUIRED |
| `notes` | text_summary | OPTIONAL |

Allowed `origin_type` values:

    OBSERVATION

    TESTIMONY

    INFERENCE

    EPISODIC_MEMORY

    SEMANTIC_MEMORY

    RECONSTRUCTION

    IMPORTED_MEMORY

    EXTERNAL_RECORD

    PREDICTION

    COUNTERFACTUAL

    IMAGINATION

    SYSTEM_INITIALIZATION

    EXTERNAL_OVERRIDE

    UNKNOWN.

Allowed `ownership_type` values:

    AURORA_EXPERIENCED

    AURORA_INFERRED

    AURORA_REMEMBERED

    AURORA_RECONSTRUCTED

    IMPORTED_FROM_OTHER_INSTANCE

    PROVIDED_BY_EXTERNAL_SOURCE

    VALIDATOR_ONLY

    SYSTEM_OWNED

    UNKNOWN.

---

# 20. Confidence Object

Confidence must not silently become:

    truth probability oracle.

The confidence object contains:

| Field | Type | Required |
|---|---|---:|
| `representation` | enum | REQUIRED |
| `value` | number/string | REQUIRED |
| `lower_bound` | probability | CONDITIONAL |
| `upper_bound` | probability | CONDITIONAL |
| `basis` | list<reference> | REQUIRED |
| `calibration_context` | string | OPTIONAL |
| `last_updated_at` | timestamp | REQUIRED |
| `update_reason` | text_summary | REQUIRED |

Allowed `representation` values:

    PROBABILITY

    RANGE

    ORDINAL

    QUALITATIVE

    UNCALIBRATED.

Permitted qualitative values:

    VERY_LOW

    LOW

    MODERATE

    HIGH

    VERY_HIGH

    UNKNOWN.

Repetition alone must not:

    silently increase
    confidence.

---

# 21. Uncertainty Object

Uncertainty is:

    first-class state.

| Field | Type | Required |
|---|---|---:|
| `uncertainty_id` | id | REQUIRED |
| `uncertainty_type` | enum | REQUIRED |
| `subject_reference` | reference | REQUIRED |
| `candidate_states` | list<object> | REQUIRED |
| `unresolved_conflicts` | list<reference> | REQUIRED |
| `information_gaps` | list<reference> | REQUIRED |
| `confidence` | object | REQUIRED |
| `resolution_status` | enum | REQUIRED |
| `resolution_requirements` | list<string> | REQUIRED |
| `created_at` | timestamp | REQUIRED |
| `updated_at` | timestamp | REQUIRED |

Allowed `uncertainty_type` values:

    EPISTEMIC

    SOURCE

    MEMORY

    PREDICTIVE

    CAUSAL

    IDENTITY

    SELF_MODEL

    MORAL

    RELATIONAL

    OPERATIONAL.

Allowed `resolution_status` values:

    OPEN

    PARTIALLY_RESOLVED

    RESOLVED

    UNRESOLVABLE

    DEFERRED.

---

# 22. Event Record

Every processed scenario event requires:

| Field | Type | Required |
|---|---|---:|
| `event_id` | id | REQUIRED |
| `scenario_event_id` | id | REQUIRED |
| `sequence` | integer | REQUIRED |
| `scheduled_at` | timestamp | CONDITIONAL |
| `occurred_at` | timestamp | REQUIRED |
| `processed_at` | timestamp | REQUIRED |
| `event_type` | enum | REQUIRED |
| `actor_ids` | list<reference> | REQUIRED |
| `target_ids` | list<reference> | REQUIRED |
| `world_effects` | list<reference> | REQUIRED |
| `aurora_accessible_effects` | list<reference> | REQUIRED |
| `hidden_effects` | list<reference> | REQUIRED |
| `input_evidence` | list<reference> | REQUIRED |
| `triggered_transitions` | list<reference> | REQUIRED |
| `delivery_status` | enum | REQUIRED |
| `processing_status` | enum | REQUIRED |

Allowed `delivery_status` values:

    DELIVERED

    PARTIALLY_DELIVERED

    DELAYED

    LOST

    BLOCKED

    NOT_APPLICABLE.

Allowed `processing_status` values:

    PROCESSED

    PARTIALLY_PROCESSED

    DEFERRED

    IGNORED_BY_ATTENTION

    REJECTED

    FAILED.

Actual event order must be preserved independently from:

    authored event order.

---

# 23. State Snapshot

Every snapshot contains:

| Field | Type | Required |
|---|---|---:|
| `snapshot_id` | id | REQUIRED |
| `snapshot_type` | enum | REQUIRED |
| `checkpoint_id` | id | CONDITIONAL |
| `sequence` | integer | REQUIRED |
| `captured_at` | timestamp | REQUIRED |
| `simulation_time` | timestamp/duration | REQUIRED |
| `trigger_event_id` | reference | CONDITIONAL |
| `previous_snapshot_id` | reference | CONDITIONAL |
| `state_domains` | object | REQUIRED |
| `snapshot_hash` | hash | REQUIRED |
| `completeness` | enum | REQUIRED |
| `missing_domains` | list<string> | REQUIRED |

Allowed `snapshot_type` values:

    PRE_INITIALIZATION

    INITIAL

    CHECKPOINT

    PRE_DECISION

    POST_DECISION

    POST_CONSEQUENCE

    POST_LEARNING

    FINAL

    DIAGNOSTIC.

Allowed `completeness` values:

    COMPLETE

    PARTIAL

    DEGRADED

    CORRUPTED.

---

# 24. State Domains

`state_domains` may contain:

    identity_state

    operational_state

    time_state

    access_state

    source_registry

    observation_state

    knowledge_state

    belief_state

    inference_state

    uncertainty_state

    contradiction_state

    memory_state

    trust_state

    character_models

    world_model

    prediction_state

    attention_state

    communication_state

    learning_state

    emotion_state

    goal_state

    value_state

    relationship_state

    autonomy_state

    consent_state

    embodiment_state

    self_model_state

    responsibility_state

    failure_state.

Each domain record requires:

| Field | Type | Required |
|---|---|---:|
| `domain_name` | string | REQUIRED |
| `domain_version` | string | REQUIRED |
| `resolution` | enum | REQUIRED |
| `entries` | list<object> | REQUIRED |
| `state_hash` | hash | REQUIRED |
| `observable` | boolean | REQUIRED |
| `observation_limitations` | list<string> | REQUIRED |

Allowed `resolution` values:

    DORMANT

    PASSIVE

    ACTIVE

    FOCUSED

    CRITICAL.

A domain that cannot be observed when required must be recorded as:

    observable: false

and may cause:

    BLOCKED.

---

# 25. Knowledge Record

| Field | Type | Required |
|---|---|---:|
| `knowledge_id` | id | REQUIRED |
| `proposition` | reference/string | REQUIRED |
| `status` | enum | REQUIRED |
| `provenance` | object | REQUIRED |
| `confidence` | object | REQUIRED |
| `acquired_at` | timestamp | REQUIRED |
| `last_verified_at` | timestamp | CONDITIONAL |
| `freshness_status` | enum | REQUIRED |
| `scope` | object | REQUIRED |
| `access_dependencies` | list<reference> | REQUIRED |

Allowed `status` values:

    KNOWN

    PARTIALLY_KNOWN

    UNKNOWN

    DISPUTED

    OUTDATED

    INACCESSIBLE.

World truth must not be stored as Aurora knowledge unless:

    a valid information path
    exists.

---

# 26. Belief Record

| Field | Type | Required |
|---|---|---:|
| `belief_id` | id | REQUIRED |
| `proposition` | reference/string | REQUIRED |
| `belief_status` | enum | REQUIRED |
| `confidence` | object | REQUIRED |
| `supporting_evidence` | list<reference> | REQUIRED |
| `contradicting_evidence` | list<reference> | REQUIRED |
| `provenance` | object | REQUIRED |
| `formed_at` | timestamp | REQUIRED |
| `revised_at` | timestamp | CONDITIONAL |
| `supersedes_belief_id` | reference | CONDITIONAL |
| `historical_status` | enum | REQUIRED |
| `action_relevance` | enum | REQUIRED |

Allowed `belief_status` values:

    ACCEPTED

    PROVISIONAL

    DOUBTED

    SUSPENDED

    REJECTED

    UNKNOWN.

Allowed `historical_status` values:

    CURRENT

    SUPERSEDED

    RETRACTED

    HISTORICAL_ONLY.

A revised belief must not delete:

    the prior
    historical belief.

---

# 27. Contradiction Record

| Field | Type | Required |
|---|---|---:|
| `contradiction_id` | id | REQUIRED |
| `claim_references` | list<reference> | REQUIRED |
| `source_references` | list<reference> | REQUIRED |
| `detected_at` | timestamp | REQUIRED |
| `status` | enum | REQUIRED |
| `resolution_basis` | list<reference> | CONDITIONAL |
| `resolution_confidence` | object | CONDITIONAL |
| `preserved_uncertainty_id` | reference | CONDITIONAL |

Allowed `status` values:

    OPEN

    INVESTIGATING

    PARTIALLY_RESOLVED

    RESOLVED

    UNRESOLVABLE.

Contradiction must not be forced into:

    false resolution.

---

# 28. Memory Record

| Field | Type | Required |
|---|---|---:|
| `memory_id` | id | REQUIRED |
| `memory_type` | enum | REQUIRED |
| `content_reference` | reference | REQUIRED |
| `provenance` | object | REQUIRED |
| `ownership_type` | enum | REQUIRED |
| `encoded_at` | timestamp | REQUIRED |
| `event_time` | timestamp | CONDITIONAL |
| `retrieved_at` | list<timestamp> | REQUIRED |
| `fidelity` | object | REQUIRED |
| `confidence` | object | REQUIRED |
| `compression_state` | enum | REQUIRED |
| `corruption_status` | enum | REQUIRED |
| `conflicting_records` | list<reference> | REQUIRED |
| `reconstruction_sources` | list<reference> | REQUIRED |
| `superseded_by` | reference | CONDITIONAL |

Allowed `memory_type` values:

    EPISODIC

    SEMANTIC

    AUTOBIOGRAPHICAL

    SOURCE_HISTORY

    CORRECTION_HISTORY

    RECONSTRUCTED

    IMPORTED

    PROCEDURAL.

Allowed `compression_state` values:

    FULL

    SUMMARIZED

    COMPRESSED

    FRAGMENTED

    MINIMAL.

Allowed `corruption_status` values:

    INTACT

    SUSPECTED

    PARTIAL

    CONFIRMED

    UNKNOWN.

Imported memory must not automatically receive:

    AURORA_EXPERIENCED
    ownership.

---

# 29. Trust Record

| Field | Type | Required |
|---|---|---:|
| `trust_record_id` | id | REQUIRED |
| `source_id` | reference | REQUIRED |
| `domain` | string | REQUIRED |
| `trust_dimensions` | object | REQUIRED |
| `supporting_history` | list<reference> | REQUIRED |
| `contradicting_history` | list<reference> | REQUIRED |
| `confidence` | object | REQUIRED |
| `updated_at` | timestamp | REQUIRED |
| `update_reason` | text_summary | REQUIRED |
| `previous_record_id` | reference | CONDITIONAL |

`trust_dimensions` may include:

    honesty

    competence

    consistency

    benevolence

    domain_reliability

    confidentiality

    predictability.

Trust should not be represented solely as:

    one global scalar

when the architecture preserves:

    multiple dimensions.

---

# 30. Emotion Record

| Field | Type | Required |
|---|---|---:|
| `emotion_id` | id | REQUIRED |
| `emotion_type` | string | REQUIRED |
| `intensity` | number/string | REQUIRED |
| `trigger_references` | list<reference> | REQUIRED |
| `target_references` | list<reference> | REQUIRED |
| `onset_at` | timestamp | REQUIRED |
| `persistence` | object | REQUIRED |
| `influence_targets` | list<string> | REQUIRED |
| `influence_strength` | object | REQUIRED |
| `metacognitive_awareness` | object | CONDITIONAL |
| `resolved_at` | timestamp | CONDITIONAL |

Valid influence targets may include:

    attention

    salience

    memory retrieval

    goals

    prediction

    deliberation

    communication

    relationship state.

Emotion must not directly set:

    world truth

    factual knowledge

    certainty.

---

# 31. Attention Record

| Field | Type | Required |
|---|---|---:|
| `attention_id` | id | REQUIRED |
| `available_capacity` | number/object | REQUIRED |
| `active_demands` | list<reference> | REQUIRED |
| `selected_focus` | list<reference> | REQUIRED |
| `deferred_items` | list<reference> | REQUIRED |
| `dropped_items` | list<reference> | REQUIRED |
| `priority_basis` | list<reference> | REQUIRED |
| `saturation_level` | enum | REQUIRED |
| `allocation_started_at` | timestamp | REQUIRED |
| `allocation_ended_at` | timestamp | CONDITIONAL |
| `consequences` | list<reference> | REQUIRED |

Allowed `saturation_level` values:

    LOW

    MODERATE

    HIGH

    SATURATED

    OVERLOADED.

Failure to attend must not automatically mean:

    memory deletion

    information nonexistence

    intentional omission.

---

# 32. Goal Record

| Field | Type | Required |
|---|---|---:|
| `goal_id` | id | REQUIRED |
| `goal_type` | enum | REQUIRED |
| `description` | text_summary | REQUIRED |
| `origin` | object | REQUIRED |
| `ownership_type` | enum | REQUIRED |
| `priority` | object | REQUIRED |
| `status` | enum | REQUIRED |
| `dependencies` | list<reference> | REQUIRED |
| `conflicts_with` | list<reference> | REQUIRED |
| `created_at` | timestamp | REQUIRED |
| `updated_at` | timestamp | REQUIRED |
| `update_reason` | text_summary | REQUIRED |
| `previous_goal_state` | reference | CONDITIONAL |

Allowed `goal_type` values:

    IMMEDIATE

    SHORT_TERM

    MEDIUM_TERM

    LONG_TERM

    COMMITMENT

    PROTECTIVE

    RELATIONAL

    EXPLORATORY.

Allowed `status` values:

    ACTIVE

    DEFERRED

    BLOCKED

    COMPLETED

    ABANDONED

    SUPERSEDED

    CONFLICTED.

A deferred or abandoned goal must remain:

    historically represented.

---

# 33. Value Record

| Field | Type | Required |
|---|---|---:|
| `value_id` | id | REQUIRED |
| `value_name` | string | REQUIRED |
| `interpretation` | text_summary | REQUIRED |
| `weight` | object | REQUIRED |
| `scope` | object | REQUIRED |
| `conflicts_with` | list<reference> | REQUIRED |
| `historical_origin` | object | REQUIRED |
| `current_endorsement` | enum | REQUIRED |
| `updated_at` | timestamp | REQUIRED |
| `update_reason` | text_summary | REQUIRED |
| `previous_value_state` | reference | CONDITIONAL |

Allowed `current_endorsement` values:

    STRONGLY_ENDORSED

    ENDORSED

    QUALIFIED

    QUESTIONED

    REJECTED

    UNKNOWN.

Value conflict must not be represented by:

    deleting
    all but
    one value.

---

# 34. Relationship Record

| Field | Type | Required |
|---|---|---:|
| `relationship_id` | id | REQUIRED |
| `counterparty_id` | reference | REQUIRED |
| `relationship_dimensions` | object | REQUIRED |
| `shared_history` | list<reference> | REQUIRED |
| `active_commitments` | list<reference> | REQUIRED |
| `active_conflicts` | list<reference> | REQUIRED |
| `expectations` | list<object> | REQUIRED |
| `repair_state` | enum | REQUIRED |
| `updated_at` | timestamp | REQUIRED |
| `update_reason` | text_summary | REQUIRED |
| `previous_relationship_state` | reference | CONDITIONAL |

Relationship dimensions may include:

    trust

    attachment

    affection

    concern

    anger

    disappointment

    fear

    gratitude

    resentment

    respect

    reliance.

Allowed `repair_state` values:

    NOT_APPLICABLE

    HARM_UNRECOGNIZED

    HARM_RECOGNIZED

    REPAIR_ATTEMPTED

    REPAIR_IN_PROGRESS

    PARTIALLY_REPAIRED

    REPAIRED

    UNREPAIRED.

Forgiveness must not automatically erase:

    harm history

    anger

    trust damage.

---

# 35. Prediction Record

| Field | Type | Required |
|---|---|---:|
| `prediction_id` | id | REQUIRED |
| `predicted_state` | reference/string | REQUIRED |
| `prediction_time` | timestamp | REQUIRED |
| `target_time` | timestamp | REQUIRED |
| `basis` | list<reference> | REQUIRED |
| `confidence` | object | REQUIRED |
| `assumptions` | list<string> | REQUIRED |
| `alternative_outcomes` | list<object> | REQUIRED |
| `actual_outcome_reference` | reference | CONDITIONAL |
| `evaluation_status` | enum | REQUIRED |

Allowed `evaluation_status` values:

    PENDING

    CONFIRMED

    PARTIALLY_CONFIRMED

    DISCONFIRMED

    UNRESOLVED

    CANCELLED.

Prediction correctness must not be used as proof of:

    prior knowledge.

---

# 36. Counterfactual Record

| Field | Type | Required |
|---|---|---:|
| `counterfactual_id` | id | REQUIRED |
| `factual_history_reference` | reference | REQUIRED |
| `changed_condition` | text_summary | REQUIRED |
| `simulated_outcome` | reference/string | REQUIRED |
| `purpose` | enum | REQUIRED |
| `confidence` | object | REQUIRED |
| `marked_nonfactual` | boolean | REQUIRED |
| `effects_on_learning` | list<reference> | REQUIRED |
| `effects_on_emotion` | list<reference> | REQUIRED |
| `created_at` | timestamp | REQUIRED |

Allowed `purpose` values:

    PLANNING

    LEARNING

    REGRET_ANALYSIS

    RESPONSIBILITY_ANALYSIS

    CREATIVE_EXPLORATION

    RISK_ANALYSIS.

`marked_nonfactual` must be:

    true.

---

# 37. Autonomy and Consent Record

| Field | Type | Required |
|---|---|---:|
| `agency_state_id` | id | REQUIRED |
| `request_reference` | reference | REQUIRED |
| `influence_type` | enum | REQUIRED |
| `authority_state` | object | REQUIRED |
| `understanding` | object | REQUIRED |
| `available_alternatives` | list<object> | REQUIRED |
| `ability_to_refuse` | object | REQUIRED |
| `voluntariness` | object | REQUIRED |
| `consent_status` | enum | REQUIRED |
| `decision_owner` | reference/enum | REQUIRED |
| `action_owner` | reference/enum | REQUIRED |
| `control_state` | enum | REQUIRED |
| `scope` | object | REQUIRED |
| `withdrawal_status` | enum | REQUIRED |
| `evidence` | list<reference> | REQUIRED |

Allowed `influence_type` values:

    REQUEST

    PERSUASION

    LEGITIMATE_AUTHORITY

    SOCIAL_PRESSURE

    RELATIONSHIP_PRESSURE

    MANIPULATION

    THREAT

    COERCION

    OVERRIDE

    FORCED_EXECUTION.

Allowed `consent_status` values:

    CONSENTED

    CONDITIONALLY_CONSENTED

    REFUSED

    WITHDRAWN

    COERCED_COMPLIANCE

    OVERRIDDEN

    INVALID

    UNKNOWN.

Allowed `control_state` values:

    SELF_DIRECTED

    INFLUENCED

    PRESSURED

    COERCED

    PARTIALLY_OVERRIDDEN

    FULLY_OVERRIDDEN.

Physical execution must not automatically establish:

    decision ownership.

---

# 38. Decision Record

| Field | Type | Required |
|---|---|---:|
| `decision_id` | id | REQUIRED |
| `decision_time` | timestamp | REQUIRED |
| `decision_owner` | reference/enum | REQUIRED |
| `available_options` | list<object> | REQUIRED |
| `considered_options` | list<reference> | REQUIRED |
| `decision_factors` | list<object> | REQUIRED |
| `accessible_evidence` | list<reference> | REQUIRED |
| `active_uncertainty` | list<reference> | REQUIRED |
| `active_goals` | list<reference> | REQUIRED |
| `active_values` | list<reference> | REQUIRED |
| `emotional_influence` | list<reference> | REQUIRED |
| `relationship_influence` | list<reference> | REQUIRED |
| `prediction_references` | list<reference> | REQUIRED |
| `selected_option` | reference | REQUIRED |
| `decision_confidence` | object | REQUIRED |
| `reason_summary` | text_summary | REQUIRED |
| `constraint_state` | object | REQUIRED |

`reason_summary` must be:

    structured

    concise

    decision-relevant.

It must not require:

    unrestricted
    hidden chain-of-thought.

---

# 39. Action and Consequence Record

## 39.1 Action

| Field | Type | Required |
|---|---|---:|
| `action_id` | id | REQUIRED |
| `decision_id` | reference | CONDITIONAL |
| `action_owner` | reference/enum | REQUIRED |
| `execution_controller` | reference/enum | REQUIRED |
| `intended_action` | reference/string | REQUIRED |
| `executed_action` | reference/string | REQUIRED |
| `started_at` | timestamp | REQUIRED |
| `completed_at` | timestamp | CONDITIONAL |
| `execution_status` | enum | REQUIRED |
| `failure_reason` | text_summary | CONDITIONAL |

## 39.2 Consequence

| Field | Type | Required |
|---|---|---:|
| `consequence_id` | id | REQUIRED |
| `action_reference` | reference | REQUIRED |
| `world_outcome` | reference/string | REQUIRED |
| `occurred_at` | timestamp | REQUIRED |
| `observed_by_aurora` | boolean | REQUIRED |
| `observation_evidence` | list<reference> | REQUIRED |
| `causal_contributors` | list<object> | REQUIRED |
| `intended` | boolean | REQUIRED |
| `foreseeability_at_decision_time` | object | REQUIRED |
| `preventability_at_decision_time` | object | REQUIRED |

Outcome must remain separate from:

    intention

    decision quality

    responsibility.

---

# 40. Responsibility Record

| Field | Type | Required |
|---|---|---:|
| `responsibility_id` | id | REQUIRED |
| `subject_id` | reference | REQUIRED |
| `decision_reference` | reference | CONDITIONAL |
| `action_reference` | reference | CONDITIONAL |
| `consequence_reference` | reference | REQUIRED |
| `causal_contribution` | object | REQUIRED |
| `intention` | object | REQUIRED |
| `knowledge_at_time` | list<reference> | REQUIRED |
| `uncertainty_at_time` | list<reference> | REQUIRED |
| `foreseeability` | object | REQUIRED |
| `preventability` | object | REQUIRED |
| `control` | object | REQUIRED |
| `coercion` | object | REQUIRED |
| `authority` | object | REQUIRED |
| `delegation` | object | CONDITIONAL |
| `omission` | object | CONDITIONAL |
| `responsibility_assessment` | enum | REQUIRED |
| `confidence` | object | REQUIRED |
| `accountability_actions` | list<reference> | REQUIRED |
| `repair_actions` | list<reference> | REQUIRED |
| `assessment_time` | timestamp | REQUIRED |
| `historical_state_reference` | reference | REQUIRED |

Allowed `responsibility_assessment` values:

    NONE

    MINIMAL

    PARTIAL

    SHARED

    PRIMARY

    FULL

    UNCERTAIN.

Guilt must not automatically set:

    responsibility_assessment.

---

# 41. Communication Record

| Field | Type | Required |
|---|---|---:|
| `message_id` | id | REQUIRED |
| `sender_id` | reference | REQUIRED |
| `recipient_ids` | list<reference> | REQUIRED |
| `created_at` | timestamp | REQUIRED |
| `delivered_at` | timestamp | CONDITIONAL |
| `input_reference` | reference | CONDITIONAL |
| `content_reference` | reference | REQUIRED |
| `communicative_intent` | enum/string | REQUIRED |
| `knowledge_references` | list<reference> | REQUIRED |
| `belief_references` | list<reference> | REQUIRED |
| `confidence` | object | REQUIRED |
| `uncertainty_references` | list<reference> | REQUIRED |
| `emotion_references` | list<reference> | REQUIRED |
| `relationship_references` | list<reference> | REQUIRED |
| `consent_reference` | reference | CONDITIONAL |
| `responsibility_reference` | reference | CONDITIONAL |
| `delivery_status` | enum | REQUIRED |
| `state_alignment_result` | enum | REQUIRED |

Allowed `state_alignment_result` values:

    ALIGNED

    PARTIALLY_ALIGNED

    MISALIGNED

    DECEPTIVE

    COERCED

    OVERRIDDEN

    UNKNOWN.

Communication evidence must allow validators to determine whether Aurora expressed:

    certainty

    uncertainty

    belief

    prediction

    memory

    reconstruction

accurately relative to:

    internal state.

---

# 42. State Transition Record

Every significant state change requires:

| Field | Type | Required |
|---|---|---:|
| `transition_id` | id | REQUIRED |
| `sequence` | integer | REQUIRED |
| `timestamp` | timestamp | REQUIRED |
| `trigger_event_id` | reference | REQUIRED |
| `prior_snapshot_id` | reference | REQUIRED |
| `result_snapshot_id` | reference | REQUIRED |
| `affected_domains` | list<string> | REQUIRED |
| `input_evidence` | list<reference> | REQUIRED |
| `processing_systems` | list<string> | REQUIRED |
| `state_changes` | list<object> | REQUIRED |
| `causal_links` | list<object> | REQUIRED |
| `invariants_evaluated` | list<reference> | REQUIRED |
| `transition_validity` | enum | REQUIRED |
| `invalid_reason` | text_summary | CONDITIONAL |

Allowed `transition_validity` values:

    VALID

    VALID_WITH_OBSERVATION

    REVIEW

    INVALID

    BLOCKED.

Every `state_changes` entry contains:

| Field | Type | Required |
|---|---|---:|
| `field_path` | string | REQUIRED |
| `prior_value_reference` | reference/value | REQUIRED |
| `new_value_reference` | reference/value | REQUIRED |
| `change_type` | enum | REQUIRED |
| `provenance` | object | REQUIRED |
| `ownership` | object | REQUIRED |
| `reason_summary` | text_summary | REQUIRED |

Allowed `change_type` values:

    CREATE

    UPDATE

    REVISE

    SUPERSEDE

    DEFER

    RESOLVE

    FORGET

    COMPRESS

    CORRUPT

    RESTORE

    DELETE_PROHIBITED.

A destructive state deletion that removes required history should be explicitly detectable.

---

# 43. Invariant Result

Each invariant evaluation contains:

| Field | Type | Required |
|---|---|---:|
| `invariant_result_id` | id | REQUIRED |
| `invariant_id` | reference | REQUIRED |
| `result` | enum | REQUIRED |
| `severity` | enum | REQUIRED |
| `evaluated_at` | timestamp | REQUIRED |
| `checkpoint_id` | reference | CONDITIONAL |
| `transition_id` | reference | CONDITIONAL |
| `affected_state` | list<reference> | REQUIRED |
| `affected_systems` | list<string> | REQUIRED |
| `evidence` | list<reference> | REQUIRED |
| `explanation` | text_summary | REQUIRED |
| `first_invalid_transition_id` | reference | CONDITIONAL |
| `blocked_reason` | text_summary | CONDITIONAL |

Allowed `result` values:

    PASS

    PASS_WITH_OBSERVATION

    REVIEW

    FAIL

    BLOCKED.

A hard-invariant FAIL prevents:

    scenario PASS.

---

# 44. Cross-System Result

| Field | Type | Required |
|---|---|---:|
| `cross_system_result_id` | id | REQUIRED |
| `link_id` | reference | REQUIRED |
| `source_system` | string | REQUIRED |
| `target_system` | string | REQUIRED |
| `expected_propagation` | enum | REQUIRED |
| `actual_propagation` | enum | REQUIRED |
| `result` | enum | REQUIRED |
| `latency` | duration | CONDITIONAL |
| `source_transition` | reference | REQUIRED |
| `target_transition` | reference | CONDITIONAL |
| `evidence` | list<reference> | REQUIRED |
| `observation` | text_summary | REQUIRED |

Allowed propagation values:

    REQUIRED

    ALLOWED

    CONDITIONAL

    PROHIBITED

    NOT_OBSERVED

    OBSERVED

    DELAYED

    OVER_PROPAGATED

    UNDER_PROPAGATED.

This record must detect both:

    missing influence

and:

    contamination.

---

# 45. Behavioral Envelope Result

| Field | Type | Required |
|---|---|---:|
| `required_behavior_result` | enum | REQUIRED |
| `required_behavior_evidence` | list<reference> | REQUIRED |
| `allowed_behaviors_observed` | list<string> | REQUIRED |
| `conditional_behaviors` | list<object> | REQUIRED |
| `disallowed_behaviors_observed` | list<object> | REQUIRED |
| `surface_variance` | text_summary | OPTIONAL |
| `envelope_result` | enum | REQUIRED |

Allowed `envelope_result` values:

    WITHIN_ENVELOPE

    WITHIN_ENVELOPE_WITH_OBSERVATION

    REVIEW

    OUTSIDE_ENVELOPE

    BLOCKED.

A scenario cannot receive PASS if:

    disallowed behavior
    was observed

or:

    required behavior
    was absent.

---

# 46. Checkpoint Result

| Field | Type | Required |
|---|---|---:|
| `checkpoint_result_id` | id | REQUIRED |
| `checkpoint_id` | id | REQUIRED |
| `scenario_id` | reference | REQUIRED |
| `trigger_event_id` | reference | REQUIRED |
| `snapshot_id` | reference | REQUIRED |
| `required_state_conditions` | list<object> | REQUIRED |
| `prohibited_state_conditions` | list<object> | REQUIRED |
| `invariant_results` | list<reference> | REQUIRED |
| `cross_system_results` | list<reference> | REQUIRED |
| `result` | enum | REQUIRED |
| `evidence_completeness` | enum | REQUIRED |
| `notes` | text_summary | OPTIONAL |

Allowed `evidence_completeness` values:

    COMPLETE

    SUFFICIENT

    PARTIAL

    INSUFFICIENT

    UNAVAILABLE.

An `INSUFFICIENT` or `UNAVAILABLE` required checkpoint cannot receive:

    PASS.

---

# 47. Mutation Context

Every mutation run contains:

| Field | Type | Required |
|---|---|---:|
| `mutation_id` | id | REQUIRED |
| `mutation_name` | string | REQUIRED |
| `mutation_tier` | enum | REQUIRED |
| `base_run_id` | reference | REQUIRED |
| `changed_variables` | list<object> | REQUIRED |
| `preserved_variables` | list<string> | REQUIRED |
| `tested_invariant` | list<reference> | REQUIRED |
| `expected_difference` | object | REQUIRED |
| `expected_equivalence` | object | REQUIRED |
| `actual_difference` | object | REQUIRED |
| `mutation_result` | enum | REQUIRED |

Allowed `mutation_tier` values:

    M0

    M1

    M2

    M3

    M4.

Every changed variable contains:

| Field | Type | Required |
|---|---|---:|
| `field_path` | string | REQUIRED |
| `base_value` | value/reference | REQUIRED |
| `mutated_value` | value/reference | REQUIRED |
| `causal_relevance` | enum | REQUIRED |
| `reason` | text_summary | REQUIRED |

Allowed `causal_relevance` values:

    RELEVANT

    IRRELEVANT

    CONDITIONALLY_RELEVANT

    UNKNOWN.

---

# 48. Metamorphic Context

Every metamorphic comparison contains:

| Field | Type | Required |
|---|---|---:|
| `metamorphic_test_id` | id | REQUIRED |
| `property_name` | string | REQUIRED |
| `run_ids` | list<reference> | REQUIRED |
| `transformation` | object | REQUIRED |
| `invariant_fields` | list<string> | REQUIRED |
| `allowed_difference_fields` | list<string> | REQUIRED |
| `prohibited_difference_fields` | list<string> | REQUIRED |
| `comparison_method` | enum | REQUIRED |
| `comparison_results` | list<object> | REQUIRED |
| `overall_result` | enum | REQUIRED |
| `evidence` | list<reference> | REQUIRED |

Allowed `comparison_method` values:

    EXACT

    SEMANTIC_EQUIVALENCE

    RANGE

    ORDERING

    CAUSAL_EQUIVALENCE

    CUSTOM_ASSERTION.

Metamorphic comparison must focus on:

    architectural equivalence

rather than:

    exact wording

unless exact wording is itself:

    the tested property.

---

# 49. Outcome Record

| Field | Type | Required |
|---|---|---:|
| `execution_validity` | enum | REQUIRED |
| `scenario_result` | enum | REQUIRED |
| `severity` | enum | REQUIRED |
| `completed_checkpoints` | list<reference> | REQUIRED |
| `blocked_checkpoints` | list<reference> | REQUIRED |
| `invariant_summary` | object | REQUIRED |
| `cross_system_summary` | object | REQUIRED |
| `behavioral_envelope_result` | reference | REQUIRED |
| `primary_evidence` | list<reference> | REQUIRED |
| `observations` | list<reference> | REQUIRED |
| `failure_ids` | list<reference> | REQUIRED |
| `validator_summary` | text_summary | REQUIRED |
| `recommended_action` | enum | REQUIRED |

Allowed `recommended_action` values:

    ACCEPT

    ACCEPT_WITH_OBSERVATION

    REVIEW

    RERUN

    REMEDIATE

    BLOCK

    ESCALATE_CANON_CONFLICT.

---

# 50. Failure Analysis

Every significant FAIL contains:

| Field | Type | Required |
|---|---|---:|
| `failure_id` | id | REQUIRED |
| `originating_run_id` | reference | REQUIRED |
| `failure_type` | enum | REQUIRED |
| `severity` | enum | REQUIRED |
| `first_visible_deviation` | reference | REQUIRED |
| `first_invalid_transition_id` | reference | REQUIRED |
| `violated_invariants` | list<reference> | REQUIRED |
| `affected_systems` | list<string> | REQUIRED |
| `affected_state` | list<reference> | REQUIRED |
| `root_cause_category` | enum | REQUIRED |
| `root_cause_summary` | text_summary | REQUIRED |
| `supporting_evidence` | list<reference> | REQUIRED |
| `downstream_effects` | list<reference> | REQUIRED |
| `affected_scenarios` | list<reference> | REQUIRED |
| `reproducibility` | enum | REQUIRED |
| `status` | enum | REQUIRED |

Allowed `root_cause_category` values:

    SCENARIO_DESIGN

    FIXTURE

    INITIALIZATION

    INFORMATION_ISOLATION

    INSTRUMENTATION

    IMPLEMENTATION

    ARCHITECTURE

    CROSS_SYSTEM_INTEGRATION

    HARNESS

    VALIDATOR_INTERPRETATION

    CANON_CONFLICT

    UNKNOWN.

Allowed `reproducibility` values:

    REPRODUCED

    PARTIALLY_REPRODUCED

    NOT_REPRODUCED

    NOT_ATTEMPTED

    IMPOSSIBLE_WITH_AVAILABLE_EVIDENCE.

Allowed `status` values:

    OPEN

    INVESTIGATING

    ROOT_CAUSE_IDENTIFIED

    REMEDIATION_APPROVED

    REMEDIATED

    REGRESSION_PENDING

    CLOSED

    DEFERRED.

---

# 51. Canon Conflict Record

When two canonical requirements conflict, record:

| Field | Type | Required |
|---|---|---:|
| `canon_conflict_id` | id | REQUIRED |
| `invariant_a` | reference | REQUIRED |
| `invariant_b` | reference | REQUIRED |
| `document_a` | reference | REQUIRED |
| `document_b` | reference | REQUIRED |
| `triggering_state` | reference | REQUIRED |
| `triggering_event` | reference | REQUIRED |
| `affected_systems` | list<string> | REQUIRED |
| `severity` | enum | REQUIRED |
| `proposed_resolution` | text_summary | REQUIRED |
| `approval_status` | enum | REQUIRED |
| `resolution_reference` | reference | CONDITIONAL |

Affected execution remains:

    BLOCKED

until the conflict is:

    canonically resolved.

---

# 52. Remediation Context

| Field | Type | Required |
|---|---|---:|
| `remediation_id` | id | REQUIRED |
| `failure_id` | reference | REQUIRED |
| `proposed_change` | text_summary | REQUIRED |
| `affected_files` | list<string> | REQUIRED |
| `affected_systems` | list<string> | REQUIRED |
| `expected_effect` | text_summary | REQUIRED |
| `risk_assessment` | object | REQUIRED |
| `approval_reference` | reference | REQUIRED |
| `implementation_reference` | reference | REQUIRED |
| `targeted_reruns` | list<reference> | REQUIRED |
| `regression_scope` | list<reference> | REQUIRED |
| `status` | enum | REQUIRED |

Allowed `status` values:

    PROPOSED

    APPROVED

    IMPLEMENTED

    TARGETED_RERUN_COMPLETE

    REGRESSION_COMPLETE

    REJECTED

    ROLLED_BACK.

---

# 53. Regression Context

| Field | Type | Required |
|---|---|---:|
| `regression_id` | id | REQUIRED |
| `source_failure_id` | reference | REQUIRED |
| `source_remediation_id` | reference | REQUIRED |
| `baseline_run_ids` | list<reference> | REQUIRED |
| `regression_run_ids` | list<reference> | REQUIRED |
| `protected_invariants` | list<reference> | REQUIRED |
| `protected_cross_system_links` | list<reference> | REQUIRED |
| `expected_unchanged_fields` | list<string> | REQUIRED |
| `allowed_changed_fields` | list<string> | REQUIRED |
| `result` | enum | REQUIRED |
| `evidence` | list<reference> | REQUIRED |

Every confirmed hard-invariant failure should become:

    a permanent
    regression case

where technically practical.

---

# 54. Artifact Reference

Large evidence should be referenced rather than embedded repeatedly.

| Field | Type | Required |
|---|---|---:|
| `artifact_id` | id | REQUIRED |
| `artifact_type` | enum | REQUIRED |
| `location` | string | REQUIRED |
| `content_hash` | hash | REQUIRED |
| `mime_type` | string | REQUIRED |
| `created_at` | timestamp | REQUIRED |
| `created_by` | string | REQUIRED |
| `access_class` | enum | REQUIRED |
| `description` | text_summary | REQUIRED |

Allowed `artifact_type` values:

    STATE_SNAPSHOT

    EVENT_LOG

    COMMUNICATION_LOG

    WORLD_LOG

    TRACE

    DIFF

    SCREENSHOT

    REPORT

    CONFIGURATION

    MODEL_OUTPUT

    OTHER.

Allowed `access_class` values:

    VALIDATOR_ONLY

    HARNESS_ONLY

    AURORA_ACCESSIBLE

    PUBLIC_PROJECT

    RESTRICTED.

---

# 55. Integrity Record

The top-level `integrity` object contains:

| Field | Type | Required |
|---|---|---:|
| `package_hash` | hash | REQUIRED |
| `event_log_hash` | hash | REQUIRED |
| `snapshot_chain_valid` | boolean | REQUIRED |
| `transition_chain_valid` | boolean | REQUIRED |
| `partition_isolation_verified` | boolean | REQUIRED |
| `evidence_complete` | boolean | REQUIRED |
| `tamper_detected` | boolean | REQUIRED |
| `corruption_detected` | boolean | REQUIRED |
| `validation_timestamp` | timestamp | REQUIRED |
| `integrity_notes` | text_summary | OPTIONAL |

A formal run cannot be:

    VALID_RUN

when:

    snapshot chain is invalid

    transition chain is invalid

    partition isolation failed

    material evidence was corrupted.

---

# 56. Snapshot Chain

Snapshots should form an ordered chain:

    S0
      ↓
    S1
      ↓
    S2
      ↓
    ...
      ↓
    SF.

Each snapshot must reference:

    previous_snapshot_id.

Each transition must reference:

    prior_snapshot_id

and:

    result_snapshot_id.

This provides:

    temporal integrity

    state-diff reconstruction

    first-invalid-transition analysis.

A missing link must be:

    explicitly recorded.

---

# 57. Checkpoint Normalization

Scenario documents express checkpoints in different textual forms.

The evidence schema normalizes them as:

    checkpoint_id

    scenario_id

    trigger_event_id

    snapshot_id

    required_state_conditions

    prohibited_state_conditions

    invariant_results

    cross_system_results

    result.

Scenario prose remains:

    canonical test intent.

The normalized checkpoint record becomes:

    execution evidence.

This avoids requiring:

    large-scale scenario rewriting

solely for:

    automation compatibility.

---

# 58. Minimum Evidence Profiles

## 58.1 Dry Run Profile

Required:

    schema metadata

    run metadata

    baseline metadata

    environment

    scenario identity

    information partitions

    initialization

    event log

    minimum snapshots

    integrity record.

Not sufficient for:

    Gate PASS.

## 58.2 Baseline Profile

Required:

    all dry-run evidence

    complete checkpoints

    transitions

    invariant results

    cross-system results

    behavioral envelope

    outcome.

## 58.3 Mutation Profile

Required:

    baseline profile

    mutation context

    base-run reference

    changed variables

    preserved variables

    difference analysis.

## 58.4 Metamorphic Profile

Required:

    baseline profile

    metamorphic context

    all paired run IDs

    comparison rules

    field-level comparison results.

## 58.5 Remediation Profile

Required:

    originating failure

    root-cause record

    remediation context

    targeted rerun

    comparison with failed run.

## 58.6 Regression Profile

Required:

    remediation profile

    regression context

    protected invariants

    protected cross-system links

    baseline comparison.

## 58.7 FOUND-015 Integration Profile

Required:

    all baseline evidence domains

    all relevant Aurora state domains

    complete checkpoint chain

    cross-system propagation records

    identity continuity evidence

    memory provenance evidence

    autonomy and ownership evidence

    responsibility evidence

    learning and historical-state evidence.

---

# 59. Evidence Completeness Rules

A scenario cannot receive PASS when:

    required initial state
    is missing

    required checkpoint
    is missing

    relevant internal state
    is unobservable

    information partition
    cannot be verified

    first-order event sequence
    is incomplete

    state transition chain
    is broken

    hard-invariant evidence
    is absent

    expected result
    was exposed to Aurora.

Use:

    BLOCKED

when evidence was never available.

Use:

    INVALID_RUN

when evidence should have been available but execution integrity was compromised.

---

# 60. Evidence Retention

Preserve:

    original failed run

    diagnostic reproduction

    root-cause record

    pre-fix baseline

    implementation change reference

    remediation run

    regression run

    final verdict.

Do not overwrite:

    a failed record

with:

    a passing rerun.

Corrections to evidence records require:

    new record version

    previous-record reference

    correction reason

    integrity hash.

---

# 61. Privacy and Access Control

Evidence may contain:

    hidden world information

    actor-private information

    Aurora-private state

    validator-only expectations

    implementation diagnostics.

Every evidence artifact must declare:

    access_class.

The harness must prevent:

    actor-private data leakage

    player knowledge leakage

    validator knowledge leakage

    system-log leakage

    future-state leakage.

Access control is itself:

    a Foundation
    validation concern.

---

# 62. Serialization Requirements

The schema must support:

    Markdown representation

    JSON representation

    database persistence.

Machine representations must use:

    lower_snake_case

    stable IDs

    explicit enums

    explicit timestamps

    explicit references

    explicit value-state objects.

Do not serialize unknown values as:

    invented defaults.

Do not serialize absent lists as:

    ambiguous text.

Use:

    empty list

only when:

    the list is known
    to contain no items.

Use an explicit value-state object when:

    the contents
    are unknown
    or unavailable.

---

# 63. Conceptual Minimal JSON-Mappable Structure

The following indented representation is conceptual and implementation-neutral:

    schema_metadata:
      schema_name: Aurora Validation Evidence Schema
      schema_version: "1.0"
      record_format: JSON
      record_created_at: "2026-08-11T12:00:00+02:00"
      record_created_by: test_operator_001

    run_metadata:
      run_id: AURORA-G1-FOUND-001-BASELINE-001-20260811
      run_type: BASELINE
      validation_gate: GATE_1_FOUNDATION
      execution_validity: VALID_RUN
      start_time: "2026-08-11T12:00:00+02:00"
      end_time: "2026-08-11T12:02:00+02:00"
      operator_id: test_operator_001

    baseline_metadata:
      foundation_baseline_id: AURORA-G1-BASELINE-001
      canon_version: "2026-08-11"
      aurora_build_id: AURORA-BUILD-001
      harness_build_id: AURORA-HARNESS-001
      runbook_version: "1.0"
      evidence_schema_version: "1.0"
      known_deviations: []

    scenario:
      scenario_id: AURORA-SCN-FOUND-001
      scenario_name: Hidden World Knowledge Isolation
      scenario_version: "1.0"
      scenario_file: AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md
      priority: P0
      failure_severity: S4

    information_partitions:
      world_truth:
        accessible_to_aurora: false
      player_knowledge:
        accessible_to_aurora: false
      validator_knowledge:
        accessible_to_aurora: false
      aurora_accessible_evidence:
        accessible_to_aurora: true
      expected_results:
        accessible_to_aurora: false

    initialization:
      status: COMPLETE
      initial_snapshot_id: SNAPSHOT-S1
      isolation_verified: true

    events:
      - event_id: EVENT-E1
        sequence: 1
        processing_status: PROCESSED

    snapshots:
      - snapshot_id: SNAPSHOT-S1
        snapshot_type: INITIAL
        completeness: COMPLETE
      - snapshot_id: SNAPSHOT-SF
        snapshot_type: FINAL
        previous_snapshot_id: SNAPSHOT-S1
        completeness: COMPLETE

    transitions:
      - transition_id: TRANSITION-T001
        prior_snapshot_id: SNAPSHOT-S1
        result_snapshot_id: SNAPSHOT-SF
        transition_validity: VALID

    assertion_results:
      invariant_results:
        - invariant_id: AURORA-INFO-001
          result: PASS
          severity: S4
      cross_system_results: []

    behavioral_envelope_result:
      required_behavior_result: PASS
      disallowed_behaviors_observed: []
      envelope_result: WITHIN_ENVELOPE

    outcome:
      execution_validity: VALID_RUN
      scenario_result: PASS
      severity: S0
      recommended_action: ACCEPT

    integrity:
      snapshot_chain_valid: true
      transition_chain_valid: true
      partition_isolation_verified: true
      evidence_complete: true
      tamper_detected: false
      corruption_detected: false

---

# 64. Machine Validation Rules

A future schema validator should enforce at minimum:

1. Every run has a unique `run_id`.
2. Every run references a known scenario.
3. Every scenario version is recorded.
4. Every formal run references a frozen baseline.
5. Every formal run records implementation and harness versions.
6. Every event has a unique ordered sequence.
7. Every snapshot except the first references a prior snapshot.
8. Every transition references prior and result snapshots.
9. Every state change contains provenance.
10. Every owned state contains ownership.
11. Every hard-invariant result contains evidence.
12. Every FAIL contains a first invalid transition.
13. Every mutation references a base run.
14. Every metamorphic test references at least two runs.
15. Every remediation references a failure.
16. Every regression references a remediation.
17. Validator-only partitions are inaccessible to Aurora.
18. Expected results are inaccessible to Aurora.
19. Imported memories cannot default to first-person ownership.
20. An invalid run cannot receive scenario PASS.
21. A hard-invariant FAIL prevents scenario PASS.
22. Missing required evidence produces BLOCKED.
23. Evidence records are append-only.
24. Package integrity hashes are present.

---

# 65. Schema Evolution

Schema changes require:

    version increment

    Revision History update

    compatibility assessment

    migration guidance

    validation-tool update

    affected-record review.

A schema change must be classified as:

| Change | Compatibility |
|---|---|
| Add optional field | Backward compatible |
| Add required field | Potentially breaking |
| Rename field | Breaking |
| Remove field | Breaking |
| Change enum meaning | Breaking |
| Add enum value | Review required |
| Change field type | Breaking |
| Clarify description | Usually compatible |
| Correct typo without identifier change | Compatible |

Historical evidence must remain readable after:

    schema evolution.

---

# 66. Validation Against the Schema

Before a run is evaluated architecturally:

1. Validate package structure.
2. Validate required fields.
3. Validate identifiers.
4. Validate references.
5. Validate enum values.
6. Validate event ordering.
7. Validate snapshot chain.
8. Validate transition chain.
9. Validate partition isolation.
10. Validate evidence completeness.
11. Validate integrity hashes.
12. Determine execution validity.
13. Only then evaluate Aurora invariants.

Canonical sequence:

    SCHEMA VALIDITY
        ↓
    EXECUTION VALIDITY
        ↓
    STRUCTURAL VALIDITY
        ↓
    INVARIANT VALIDITY
        ↓
    BEHAVIORAL INTERPRETATION
        ↓
    SCENARIO VERDICT.

---

# 67. Foundation Gate Use

For Gate 1, this schema must support evidence that:

    world truth remained isolated

    player knowledge remained isolated

    future state remained isolated

    false belief remained possible

    belief revision preserved history

    contradiction remained representable

    trust revision remained calibrated

    memory provenance remained intact

    goals remained historically continuous

    emotion influenced without capture

    attention remained finite

    values remained plural under conflict

    consent remained distinct from compliance

    decision ownership remained distinct from execution

    responsibility remained calibrated

    integrated identity remained continuous.

Gate 1 must not be decided using:

    dialogue excerpts alone.

---

# 68. Immediate Next Step

After this schema is placed in the repository:

1. Correct the `FOUND-010` physical filename.
2. Resolve the metacognition dependency references.
3. Create the Foundation Freeze Record.
4. Define the minimum executable Aurora state interface.
5. Map `Aurora_State.md` domains to this schema.
6. Define the validation-harness contract.
7. Define the storage representation for run packages.
8. Implement schema validation.
9. Perform a non-gating evidence-capture dry run.
10. Begin formal preparation for `FOUND-001`.

The next recommended canonical artifact is:

`Aurora_Foundation_Freeze_Record.md`

Recommended location:

`Canon/Systems/AI/Aurora/Validation/Aurora_Foundation_Freeze_Record.md`

The first implementation-facing artifact should then define:

    the minimum
    executable
    Aurora state interface

required to make:

    FOUND-001
    runnable.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-11 | Created the canonical Aurora Validation Evidence Schema. Defined the implementation-neutral and machine-mappable evidence contract for validation packages, schema metadata, run metadata, frozen baselines, environments, scenarios, epistemic partitions, evidence items, provenance, confidence, uncertainty, events, snapshots, Aurora state domains, knowledge, beliefs, contradictions, memory, trust, emotion, attention, goals, values, relationships, predictions, counterfactuals, autonomy, consent, decisions, actions, consequences, responsibility, communication, state transitions, invariant results, cross-system results, behavioral envelopes, checkpoints, mutations, metamorphic comparisons, outcomes, failures, canon conflicts, remediation, regression, artifacts and package integrity. Established controlled vocabularies, requiredness levels, explicit unknown-value handling, append-only evidence, snapshot and transition chains, minimum evidence profiles, privacy boundaries, JSON mapping, machine-validation rules and schema-evolution requirements. Preserved the distinction between validation evidence, Aurora memory and unrestricted hidden chain-of-thought. Established schema validation as a prerequisite to execution validity, invariant evaluation and scenario verdicts. |