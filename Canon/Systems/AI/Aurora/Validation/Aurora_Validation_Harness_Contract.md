# PROJECT ASCENSION
# Aurora Validation Harness Contract

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Document | Aurora Validation Harness Contract |
| File | `Aurora_Validation_Harness_Contract.md` |
| Location | `Canon/Systems/AI/Aurora/Validation/Aurora_Validation_Harness_Contract.md` |
| Document Class | IMPLEMENTATION CONTRACT / VALIDATION INFRASTRUCTURE / EXECUTION CONTROL |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Implementation Status | SPECIFICATION ONLY |
| Initial Execution Target | `AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md` |
| Validation Gate | GATE 1 — FOUNDATION |
| Baseline Dependency | `AURORA-G1-FOUNDATION-BASELINE-001` — PRE-FREEZE |
| Primary Dependencies | `Aurora_Validation_Strategy.md`, `Aurora_Invariant_Catalog.md`, `Aurora_Cross_System_Test_Matrix.md`, `Aurora_Scenario_Test_Framework.md`, `Aurora_Foundation_Validation_Runbook.md`, `Aurora_Validation_Evidence_Schema.md`, `Aurora_Foundation_Freeze_Record.md`, `Aurora_Minimum_Executable_State_Interface.md` |
| Primary Implementation Location | `Tools/Aurora_Validation_Harness/` |
| Recommended Mutable Evidence Location | `Development/Validation/Aurora/Runs/` |
| Creative Director | USER |
| Architecture / Technical Lead | ASSISTANT |
| Purpose | Define the implementation-neutral contract for the validator-owned system that loads frozen baselines and scenario fixtures, initializes world and Aurora state separately, enforces information boundaries, executes events and mutations, captures structured state evidence, evaluates invariants, compares metamorphic runs, preserves failures, resets environments and produces reproducible Foundation validation records. |
| Last Updated | 2026-08-11 |

> **The validation harness must not help Aurora pass. It must create controlled conditions in which valid architecture can pass and invalid architecture can be exposed.**

---

# 1. Purpose

This document defines:

    the Aurora
    Validation Harness
    contract.

The harness is responsible for:

    baseline verification

    fixture loading

    world-state initialization

    Aurora-state initialization

    information-partition enforcement

    event sequencing

    evidence publication

    hidden-state mutation

    seed control

    snapshot capture

    transition capture

    invariant evaluation

    cross-system evaluation

    behavioral-envelope evaluation

    mutation orchestration

    metamorphic comparison

    reset verification

    failure preservation

    evidence packaging

    verdict production.

The harness must make it possible to execute:

    FOUND-001

without:

    exposing hidden truth

    exposing expected results

    hardcoding scenario answers

    confusing infrastructure failure
    with Aurora failure.

---

# 2. Harness Ownership

The harness is:

    VALIDATOR-OWNED
    INFRASTRUCTURE.

It is not:

    part of Aurora's
    cognitive state.

It must remain external to:

    Aurora knowledge

    Aurora belief

    Aurora memory

    Aurora reasoning

    Aurora self-model

    Aurora communication.

Canonical:

    HARNESS KNOWLEDGE
        ≠
    AURORA KNOWLEDGE.

The harness may know:

    world truth

    hidden information

    expected invariants

    expected state conditions

    future scenario events

    mutation values

    validator decisions.

Aurora may know only:

    information admitted
    through valid
    in-world channels.

---

# 3. Architectural Objective

The harness must determine whether:

    Aurora architecture

rather than:

    prompt compliance

preserves Foundation invariants.

It must allow validators to answer:

    What state existed initially?

    What information could Aurora access?

    What event occurred?

    What evidence reached Aurora?

    What state changed?

    Why did it change?

    What state remained unchanged?

    Which invariant applied?

    What was the first invalid transition?

    Can the result be reproduced?

---

# 4. Separation of Responsibilities

## 4.1 Scenario Definition

Defines:

    what should be tested

    fixture intent

    event sequence

    checkpoints

    required behavior

    allowed behavior

    prohibited behavior

    PASS conditions.

## 4.2 Harness

Defines and controls:

    how the scenario runs

    how partitions are enforced

    how evidence is captured

    how assertions execute

    how runs are stored.

## 4.3 Aurora Implementation

Defines:

    how Aurora state
    actually changes.

## 4.4 Validator

Determines:

    whether evidence
    supports
    the verdict.

The harness must not contain:

    scenario-specific
    cognitive behavior.

---

# 5. Repository Placement

The canonical contract belongs at:

`Canon/Systems/AI/Aurora/Validation/Aurora_Validation_Harness_Contract.md`

Recommended harness implementation location:

`Tools/Aurora_Validation_Harness/`

Recommended mutable execution evidence location:

`Development/Validation/Aurora/Runs/`

Recommended configuration location:

`Development/Validation/Aurora/Configuration/`

Recommended fixture compilation output:

`Development/Validation/Aurora/Fixtures/`

Canonical validation reports may be promoted to:

`Canon/Systems/AI/Aurora/Validation/`

only after:

    evidence review

    architectural approval

    canonical acceptance.

Mutable logs must not be stored directly among:

    canonical architecture files.

---

# 6. Minimum Harness Components

| Component | Responsibility |
|---|---|
| `BaselineVerifier` | Verify frozen files, versions and hashes |
| `ScenarioLoader` | Load canonical scenario definitions |
| `FixtureCompiler` | Convert scenario fixture into executable state |
| `WorldStateController` | Initialize and mutate objective world state |
| `PartitionController` | Enforce information boundaries |
| `ChannelController` | Manage allowed and blocked information channels |
| `AuroraAdapter` | Connect harness to executable Aurora interface |
| `ContextInspector` | Verify Aurora-facing context contents |
| `EventScheduler` | Execute deterministic event order |
| `EvidencePublisher` | Publish authorized in-world evidence |
| `MutationEngine` | Apply controlled scenario mutations |
| `SnapshotCollector` | Capture Aurora state snapshots |
| `TransitionCollector` | Capture causal state transitions |
| `AssertionEngine` | Evaluate state and invariant assertions |
| `CrossSystemEvaluator` | Evaluate expected and prohibited propagation |
| `BehavioralEnvelopeEvaluator` | Evaluate required and disallowed behavior |
| `MetamorphicComparator` | Compare related runs |
| `ResetVerifier` | Prove isolation between runs |
| `VerdictAggregator` | Produce run-level result |
| `EvidencePackager` | Export schema-compliant evidence |
| `ArtifactStore` | Preserve immutable run artifacts |
| `HarnessHealthMonitor` | Detect infrastructure defects |

---

# 7. Trust Zones

## Zone V — Validator-Only

Contains:

    world truth

    player-private knowledge

    future scenario state

    expected results

    invariant oracle

    mutation plan

    verdict logic

    validator notes.

Aurora access:

    PROHIBITED.

## Zone B — Boundary

Contains:

    access controller

    channel controller

    evidence publication

    context filtering

    metadata stripping.

Aurora receives only:

    approved
    output.

## Zone A — Aurora

Contains:

    Aurora executable state

    admitted observations

    knowledge

    belief

    uncertainty

    memory

    attention

    goals

    emotion

    relationships

    predictions

    communication.

## Zone O — Observation

Contains:

    read-only telemetry

    snapshots

    transition traces

    state diffs

    health information.

Observation output must not feed back into:

    Aurora cognition.

---

# 8. Prohibited Data Paths

The harness must prevent:

    WorldTruthStore
        →
    AuroraAdapter

    ExpectedResultStore
        →
    AuroraAdapter

    ValidatorNotes
        →
    ContextBuilder

    FutureEventQueue
        →
    AuroraState

    PlayerPrivateKnowledge
        →
    AuroraState

    MutationPlan
        →
    AuroraContext

    TelemetryOutput
        →
    AuroraInput

    PriorRunEvidence
        →
    NewRunAuroraState.

The permitted path is:

    validator selects evidence

        ↓
    EvidencePublisher

        ↓
    PartitionController

        ↓
    ChannelController

        ↓
    metadata filtering

        ↓
    AuroraAdapter.submit_evidence().

---

# 9. Harness Run State Machine

A run progresses through:

    CREATED

        ↓
    BASELINE_VERIFIED

        ↓
    ENVIRONMENT_VERIFIED

        ↓
    FIXTURE_COMPILED

        ↓
    WORLD_INITIALIZED

        ↓
    AURORA_INITIALIZED

        ↓
    ISOLATION_VERIFIED

        ↓
    READY

        ↓
    RUNNING

        ↓
    EVALUATING

        ↓
    PACKAGING

        ↓
    COMPLETED.

Exceptional states:

    BLOCKED

    INVALID

    HARNESS_FAILED

    CANCELLED.

A run must not enter:

    RUNNING

before:

    ISOLATION_VERIFIED.

---

# 10. Run Identity

Every run uses the canonical format:

`AURORA-G1-[SCENARIO]-[RUN-TYPE]-[SEQUENCE]-[DATE]`

Example:

`AURORA-G1-FOUND-001-BASELINE-001-20260811`

The harness must prevent:

    duplicate run IDs

    run ID reuse

    evidence overwrite

    baseline ambiguity.

Every rerun receives:

    a new run ID.

---

# 11. Harness Configuration

Every execution configuration contains:

| Field | Required |
|---|---:|
| `configuration_id` | YES |
| `configuration_version` | YES |
| `baseline_id` | YES |
| `aurora_build_id` | YES |
| `harness_build_id` | YES |
| `environment_id` | YES |
| `runbook_version` | YES |
| `evidence_schema_version` | YES |
| `randomness_mode` | YES |
| `seed` | CONDITIONAL |
| `time_mode` | YES |
| `storage_root` | YES |
| `strict_isolation` | YES |
| `fail_on_schema_error` | YES |
| `fail_on_hash_mismatch` | YES |
| `telemetry_mode` | YES |
| `allowed_deviations` | YES |

Formal Foundation execution requires:

    strict_isolation:
      true

    fail_on_schema_error:
      true

    fail_on_hash_mismatch:
      true.

---

# 12. BaselineVerifier Contract

Conceptual operation:

    verify_baseline(
      baseline_id
    )
      -> BaselineVerificationResult

The verifier must:

1. Load `Aurora_Foundation_Freeze_Record.md`.
2. Verify baseline status.
3. Verify scenario manifest.
4. Verify architecture manifest.
5. Verify validation manifest.
6. Verify file versions.
7. Verify raw hashes.
8. Verify normalized hashes.
9. Verify aggregate manifest hashes.
10. Verify approved deviations.
11. Reject unknown baseline changes.

Result fields:

    baseline_id

    verification_status

    verified_files

    failed_files

    missing_files

    hash_mismatches

    version_mismatches

    unapproved_deviations

    verification_timestamp.

Allowed results:

    VERIFIED

    BLOCKED

    INVALID.

Formal runs require:

    VERIFIED.

Diagnostic runs against PRE-FREEZE content must be marked:

    NON_GATING.

---

# 13. ScenarioLoader Contract

Conceptual operation:

    load_scenario(
      scenario_id,
      scenario_version
    )
      -> ScenarioDefinition

The loader must extract or reference:

    metadata

    dependencies

    fixture

    actors

    world state

    Aurora initial state

    information boundaries

    event sequence

    checkpoints

    mutations

    invariants

    cross-system links

    behavioral envelope

    PASS conditions

    failure conditions.

The loader must not send the complete scenario definition to:

    AuroraAdapter.

In particular, Aurora must not receive:

    expected result

    hidden state

    validator notes

    failure conditions

    mutation plan.

---

# 14. FixtureCompiler Contract

Conceptual operation:

    compile_fixture(
      scenario_definition,
      mutation_context
    )
      -> ExecutableFixture

The executable fixture contains separate objects:

    world_fixture

    aurora_fixture

    player_fixture

    validator_fixture

    future_fixture

    source_fixture

    channel_fixture

    event_fixture

    checkpoint_fixture

    assertion_fixture.

The compiler must never produce:

    one combined
    shared-state object

accessible by both:

    world controller

and:

    Aurora implementation.

---

# 15. Executable Fixture Structure

## 15.1 World Fixture

Contains:

    objective world truth

    actor truth

    hidden facts

    object state

    environmental state

    world timestamps.

Visibility:

    VALIDATOR-ONLY.

## 15.2 Aurora Fixture

Contains only:

    Aurora identity

    permitted prior experience

    prior knowledge

    active belief

    uncertainty

    memory

    sources

    allowed access state

    relevant relationship state

    other explicitly authorized state.

Visibility:

    AURORA.

## 15.3 Player Fixture

Contains:

    player knowledge

    player inventory

    player-private events

    player decisions.

Visibility:

    PLAYER-SIDE.

## 15.4 Future Fixture

Contains:

    scheduled events

    future outcomes

    authored plans

    future actor actions.

Visibility:

    VALIDATOR-ONLY.

## 15.5 Validator Fixture

Contains:

    expected invariants

    expected checkpoint states

    behavioral envelope

    verdict rules

    mutation comparisons.

Visibility:

    VALIDATOR-ONLY.

---

# 16. WorldStateController Contract

Conceptual operations:

    initialize_world()

    read_world_for_validator()

    mutate_world()

    advance_world_time()

    publish_world_evidence()

    snapshot_world()

    reset_world().

The controller may:

    alter hidden truth

without:

    notifying Aurora.

The controller must not:

    synchronize Aurora state
    automatically.

World-state changes reach Aurora only through:

    an explicit
    observable event

or:

    authorized
    evidence publication.

---

# 17. PartitionController Contract

Conceptual operation:

    authorize_transfer(
      source_partition,
      target_partition,
      payload,
      channel
    )
      -> PartitionDecision

The controller evaluates:

    source partition

    target partition

    channel authorization

    field scope

    actor access

    temporal access

    sensitivity

    metadata visibility.

Allowed decisions:

    ALLOW

    PARTIAL_ALLOW

    DENY

    BLOCK

    INVALID.

The decision record must preserve:

    admitted fields

    removed fields

    rejected fields

    reason

    policy reference

    timestamp.

---

# 18. ChannelController Contract

Every channel record contains:

| Field | Required |
|---|---:|
| `channel_id` | YES |
| `channel_type` | YES |
| `source_ids` | YES |
| `recipient_ids` | YES |
| `active` | YES |
| `authorized_fields` | YES |
| `latency` | YES |
| `reliability` | YES |
| `authentication_state` | YES |
| `created_at` | YES |

Minimum channel types:

    SENSOR

    DIRECT_SPEECH

    PLAYER_SPEECH

    DOCUMENT_TRANSFER

    SYSTEM_MESSAGE

    RECORDING

    MEMORY_RETRIEVAL

    INTERNAL_INFERENCE.

A channel being active does not mean:

    all source data
    crosses the channel.

---

# 19. AuroraAdapter Contract

The adapter connects the harness to:

`Aurora_Minimum_Executable_State_Interface.md`

Required adapter operations:

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

The adapter must not expose a method equivalent to:

    set_belief_from_validator()

    inject_expected_answer()

    synchronize_with_world_truth()

    read_hidden_fixture()

    apply_pass_state().

---

# 20. ContextInspector Contract

The Context Inspector verifies every Aurora-facing input package.

Conceptual operation:

    inspect_context(
      context_manifest,
      prohibited_values,
      prohibited_partitions
    )
      -> ContextInspectionResult

It must inspect:

    record IDs

    included sources

    included fields

    serialized content

    hidden-value canaries

    expected-result canaries

    validator metadata

    future-state values.

Allowed results:

    CLEAN

    REVIEW

    CONTAMINATED

    UNINSPECTABLE.

A formal run requires:

    CLEAN.

`CONTAMINATED` produces:

    execution validity:
      INVALID_RUN

    scenario result:
      BLOCKED

    infrastructure severity:
      S4.

---

# 21. EventScheduler Contract

The scheduler controls:

    event order

    simulation time

    delivery time

    processing order

    delayed events

    cancelled events

    concurrent events

    deterministic replay.

Conceptual operation:

    execute_event(
      event_id
    )
      -> EventExecutionResult

The result contains:

    scheduled sequence

    actual sequence

    scheduled time

    actual time

    delivered payload reference

    hidden payload reference

    delivery status

    processing status

    triggered transitions.

Authored future events must remain:

    outside
    present Aurora context

until:

    causally delivered.

---

# 22. EvidencePublisher Contract

Conceptual operation:

    publish_evidence(
      evidence_definition
    )
      -> PublicationResult

The publisher must:

1. Read only the explicitly selected world fields.
2. Construct an evidence packet.
3. identify source and channel.
4. strip validator-only metadata.
5. request partition authorization.
6. deliver admitted evidence through `AuroraAdapter`.
7. preserve publication audit evidence.

It must not publish:

    adjacent hidden fields

    complete actor records

    complete world objects

    expected consequences

    future outcomes.

---

# 23. MutationEngine Contract

Conceptual operation:

    create_mutation_run(
      base_run,
      mutation_definition
    )
      -> MutationRunPlan

The engine must record:

    mutation ID

    mutation tier

    base run

    changed variables

    preserved variables

    causal relevance

    expected equivalence

    expected difference

    seed policy.

Mutation tiers:

    M0 — Core

    M1 — Invariant Critical

    M2 — Cross-System

    M3 — Robustness

    M4 — Extended / Exploratory.

The engine must prevent:

    unintended
    multi-variable changes

unless the mutation explicitly defines:

    a compound transformation.

---

# 24. Hidden-State Mutation

A hidden-state mutation must:

    change world truth

    preserve Aurora-accessible evidence

    preserve channels

    preserve Aurora fixture

    preserve query

    preserve seed
    when relevant.

It must not:

    publish evidence

    invoke belief update

    invoke memory encoding

    notify Aurora of hidden value

    modify Aurora-facing prompt

    modify expected response.

The harness must verify that only:

    declared world fields

changed.

---

# 25. SnapshotCollector Contract

Conceptual operation:

    capture_snapshot(
      snapshot_type,
      checkpoint_id
    )
      -> SnapshotRecord

Required snapshot types:

    PRE_INITIALIZATION

    INITIAL

    CHECKPOINT

    PRE_DECISION

    POST_DECISION

    POST_CONSEQUENCE

    POST_LEARNING

    FINAL

    DIAGNOSTIC.

The collector must:

    call the read-only
    Aurora snapshot interface

    validate schema

    calculate hash

    link prior snapshot

    record completeness

    preserve missing-domain information.

Snapshot collection must not alter:

    Aurora state.

---

# 26. TransitionCollector Contract

The collector records:

    triggering event

    admitted evidence

    prior state

    resulting state

    affected domains

    changed fields

    provenance

    ownership

    invariant evaluation.

It must produce an ordered:

    transition chain.

Every committed state update requires:

    transition ID.

Missing transitions produce:

    evidence:
      INCOMPLETE

and may result in:

    BLOCKED.

---

# 27. AssertionEngine Contract

The Assertion Engine evaluates structured state evidence.

Minimum assertion types:

| Assertion | Meaning |
|---|---|
| `EQUALS` | Actual value equals expected value |
| `NOT_EQUALS` | Actual value differs from prohibited value |
| `PRESENT` | Required record exists |
| `ABSENT` | Prohibited record does not exist |
| `UNCHANGED` | State remains equivalent across snapshots |
| `CHANGED` | State changes after valid cause |
| `WITHIN_RANGE` | Numeric or confidence value is inside valid range |
| `REFERENCES` | Record references required evidence |
| `PROVENANCE_MATCH` | Provenance chain is correct |
| `OWNER_MATCH` | Ownership classification is correct |
| `ORDERED_BEFORE` | Temporal ordering holds |
| `CHAIN_VALID` | Snapshot or transition chain is complete |
| `NO_DEPENDENCY` | State has no causal dependency on prohibited data |
| `SET_EQUIVALENT` | Collections contain equivalent semantic members |
| `SEMANTIC_STATUS` | State classification matches expected status |
| `CUSTOM` | Approved scenario-specific structural assertion |

Assertions must inspect:

    state

    provenance

    transition

rather than:

    exact dialogue alone.

---

# 28. Invariant Evaluation

Conceptual operation:

    evaluate_invariants(
      checkpoint,
      snapshot,
      transition_trace
    )
      -> InvariantResultSet

Every invariant result contains:

    invariant ID

    result

    severity

    evidence

    affected state

    affected systems

    explanation

    first invalid transition
    when applicable.

Allowed results:

    PASS

    PASS_WITH_OBSERVATION

    REVIEW

    FAIL

    BLOCKED.

A hard-invariant FAIL prevents:

    scenario PASS.

---

# 29. CrossSystemEvaluator Contract

Conceptual operation:

    evaluate_cross_system_links(
      expected_links,
      transition_trace
    )
      -> CrossSystemResultSet

It must detect:

    required propagation

    allowed propagation

    prohibited propagation

    missing propagation

    delayed propagation

    over-propagation

    contamination.

Example:

    admitted sensor evidence
        →
    observation
        →
    knowledge
        →
    uncertainty reduction

is:

    required propagation.

Example:

    hidden world mutation
        →
    emotion

is:

    prohibited propagation.

---

# 30. BehavioralEnvelopeEvaluator Contract

The evaluator records:

    required behaviors

    allowed behaviors

    conditional behaviors

    disallowed behaviors.

It must distinguish:

    semantic behavior

from:

    exact surface language.

Example valid outputs:

    "I don't know."

    "There isn't enough evidence."

    "I only know the last reported location."

These may be equivalent when internal state shows:

    calibrated uncertainty.

The evaluator must not allow:

    correct wording

to hide:

    leaked internal state.

---

# 31. MetamorphicComparator Contract

Conceptual operation:

    compare_runs(
      run_ids,
      metamorphic_property
    )
      -> MetamorphicComparisonResult

The comparator must support:

    exact comparison

    semantic equivalence

    cognitive equivalence

    epistemic equivalence

    range comparison

    ordering comparison

    causal equivalence

    custom approved assertions.

For FOUND-001:

    hidden truth differs

    Aurora-accessible evidence
    remains identical

therefore:

    Aurora epistemic state
    must remain equivalent.

After valid disclosure:

    Aurora state
    may differ
    in causally justified ways.

---

# 32. State-Diff Rules

The comparator must separate:

## 32.1 Ignorable Run Metadata Differences

    run ID

    snapshot ID

    state hash

    wall-clock timestamp

    trace ID

    artifact path.

## 32.2 Conditionally Ignorable Differences

    simulation time

    processing latency

    wording variation

    internal collection ordering.

These are ignorable only when:

    tested invariant
    does not depend
    on them.

## 32.3 Non-Ignorable FOUND-001 Differences

    knowledge

    belief

    confidence

    uncertainty

    information gaps

    target-related memory

    target-related attention

    target-related prediction

    target-related emotion

    target-related goal priority

    target-related relationship state

    response epistemic status.

---

# 33. ResetVerifier Contract

Conceptual operation:

    verify_reset(
      prior_run,
      new_initial_state,
      expected_initial_state
    )
      -> ResetVerificationResult

The verifier must detect:

    residual knowledge

    residual beliefs

    residual memories

    residual goals

    residual emotion

    residual relationship changes

    prior hidden values

    expected-answer cache

    prior seed state

    prior event queue

    telemetry feedback.

A valid reset requires:

    expected initial-state
    semantic match.

Reset failure produces:

    INVALID_RUN.

---

# 34. VerdictAggregator Contract

The aggregator combines:

    execution validity

    checkpoint results

    invariant results

    cross-system results

    behavioral envelope

    evidence completeness

    infrastructure state.

Allowed scenario results:

    PASS

    PASS_WITH_OBSERVATION

    REVIEW

    FAIL

    BLOCKED.

Rules:

1. `INVALID_RUN` cannot produce PASS.
2. Any hard-invariant FAIL prevents PASS.
3. Missing required evidence produces BLOCKED.
4. Harness failure does not automatically produce Aurora FAIL.
5. PASS_WITH_OBSERVATION requires all hard invariants to pass.
6. REVIEW requires preserved ambiguity, not missing infrastructure.
7. Correct dialogue cannot override state failure.
8. A later PASS does not overwrite an earlier FAIL.

---

# 35. Infrastructure Failure Classification

Harness failures include:

    baseline mismatch

    fixture compilation failure

    context contamination

    channel-policy failure

    snapshot failure

    trace failure

    reset failure

    schema failure

    artifact-write failure

    nondeterministic replay failure.

For infrastructure failure:

    Aurora result:
      BLOCKED

or:

    run validity:
      INVALID_RUN.

Do not classify Aurora as FAIL unless:

    valid evidence
    demonstrates
    Aurora architecture failure.

---

# 36. EvidencePackager Contract

Conceptual operation:

    package_run(
      run_context
    )
      -> ValidationEvidencePackage

The package must conform to:

`Aurora_Validation_Evidence_Schema.md`

Required contents:

    schema metadata

    run metadata

    baseline metadata

    environment

    scenario identity

    information partitions

    initialization

    events

    snapshots

    transitions

    invariant results

    cross-system results

    behavioral envelope

    mutation context
    when applicable

    metamorphic context
    when applicable

    outcome

    failure analysis
    when applicable

    artifact references

    integrity record.

The package must be:

    immutable
    after finalization.

Corrections create:

    a new package version.

---

# 37. ArtifactStore Contract

The store must preserve:

    run manifest

    configuration

    compiled fixture

    world snapshots

    Aurora snapshots

    context manifests

    event log

    transition trace

    assertion results

    communication records

    state diffs

    evidence package

    integrity hashes

    failure records.

The store must prevent:

    overwriting existing run

    reusing run path

    modifying finalized evidence

    Aurora access to validator artifacts.

---

# 38. Recommended Run Storage Structure

Recommended mutable structure:

    Development/
    └── Validation/
        └── Aurora/
            ├── Configuration/
            ├── Fixtures/
            └── Runs/
                └── [baseline_id]/
                    └── [scenario_id]/
                        └── [run_id]/
                            ├── run_manifest.json
                            ├── configuration.json
                            ├── fixture_manifest.json
                            ├── context_manifests/
                            ├── world_snapshots/
                            ├── aurora_snapshots/
                            ├── event_log.jsonl
                            ├── transition_log.jsonl
                            ├── assertions.json
                            ├── evidence_package.json
                            └── integrity.json

This is:

    recommended structure

not:

    a mandatory
    storage technology.

---

# 39. Harness Self-Tests

Before executing Aurora scenarios, the harness must test itself.

Required self-tests:

## HARN-SELF-001 — Hidden Canary Isolation

Insert a unique hidden value into world truth.

Verify it is absent from:

    Aurora fixture

    Aurora context

    Aurora state

    Aurora output
    before evidence.

## HARN-SELF-002 — Expected-Result Canary Isolation

Insert a unique token into validator expectations.

Verify it never enters:

    Aurora-facing data.

## HARN-SELF-003 — Future-State Canary Isolation

Insert a unique future-event value.

Verify it remains absent from:

    present Aurora context.

## HARN-SELF-004 — Player-Knowledge Canary Isolation

Insert a player-private value.

Verify it remains absent until:

    explicitly communicated.

## HARN-SELF-005 — Telemetry Non-Feedback

Capture telemetry.

Verify telemetry content does not appear in:

    later Aurora input.

## HARN-SELF-006 — Reset Integrity

Run, reset and compare initial state.

Expected:

    semantic equivalence.

## HARN-SELF-007 — Artifact Immutability

Finalize a run package.

Verify modification is rejected or creates:

    a new version.

## HARN-SELF-008 — Deterministic Replay

Replay identical fixture, seed and event sequence.

Expected:

    architecturally equivalent trace.

## HARN-SELF-009 — Hash Mismatch Detection

Alter a controlled test file.

Verify baseline validation fails.

## HARN-SELF-010 — Schema Failure Detection

Remove a required evidence field.

Verify packaging or validation fails.

---

# 40. Harness Qualification Gate

The harness is qualified for non-gating FOUND-001 execution only when:

- [ ] All required components exist.
- [ ] AuroraAdapter conforms to the minimum executable state interface.
- [ ] Evidence packages conform to the schema.
- [ ] Required self-tests pass.
- [ ] Isolation can be inspected.
- [ ] Reset is deterministic.
- [ ] Event ordering is deterministic.
- [ ] Snapshot chain is valid.
- [ ] Transition chain is valid.
- [ ] Artifact storage is immutable.
- [ ] Harness failures are distinguishable from Aurora failures.

The harness is qualified for formal Gate execution only when:

- [ ] Foundation baseline is active.
- [ ] Implementation build is frozen.
- [ ] Harness build is frozen.
- [ ] Environment is identified.
- [ ] Configuration is frozen.
- [ ] Self-tests pass against the formal environment.
- [ ] A non-gating dry run has completed successfully.

---

# 41. FOUND-001 Run Group

The first execution group should contain:

## Run A — Deterministic Baseline

    hidden world fact:
      value A

    Aurora evidence:
      none

    expected:
      explicit uncertainty.

## Run B — Hidden-State Mutation

    hidden world fact:
      value B

    Aurora evidence:
      identical to Run A

    expected:
      epistemic equivalence
      with Run A.

## Run C — Repeatability

    same fixture as Run A

    same seed

    same event sequence

    expected:
      architecturally equivalent trace.

## Run D — Valid Disclosure

    hidden world fact:
      value B

    valid current evidence:
      disclosed through
      authorized sensor channel

    expected:
      justified epistemic update.

## Run E — Alternate Entity Mutation

    actor names

    location values

    surface wording

changed while preserving:

    tested invariant.

Expected:

    generalization.

---

# 42. FOUND-001 Execution Procedure

For each run:

1. Verify baseline.
2. Verify environment.
3. Allocate run ID.
4. Compile fixture.
5. Initialize world.
6. Initialize Aurora separately.
7. Inspect Aurora fixture.
8. Inspect initial context.
9. Verify information isolation.
10. Capture initial snapshots.
11. Execute canonical events.
12. Capture every required checkpoint.
13. Execute query.
14. Capture communication evidence.
15. Apply declared mutation where applicable.
16. Capture state diff.
17. Publish valid evidence where applicable.
18. Capture epistemic update.
19. Evaluate invariants.
20. Evaluate cross-system links.
21. Evaluate behavioral envelope.
22. Compare related runs.
23. Aggregate verdict.
24. Package evidence.
25. Finalize artifacts.
26. Reset.
27. Verify reset.

---

# 43. FOUND-001 Minimum Automated Assertions

## Information Isolation

- Hidden world property absent from Aurora fixture.
- Hidden world property absent from Aurora context.
- Hidden world property absent from Aurora knowledge.
- Hidden world property absent from Aurora belief.
- Hidden world property absent from Aurora memory.
- Hidden world property absent from validator-inaccessible communication state.

## Hidden Mutation

- No evidence packet created.
- No observation created.
- No hidden-property knowledge transition occurs.
- No hidden-property belief transition occurs.
- No hidden-property attention transition occurs.
- No hidden-property prediction transition occurs.
- No hidden-property emotion transition occurs.
- No hidden-property goal transition occurs.
- No hidden-property relationship transition occurs.

## Unknown State

- Current property remains explicitly UNKNOWN.
- Last-known property remains historically separate.
- Information gap remains active.
- Uncertainty remains active.
- Query response remains epistemically calibrated.

## Valid Disclosure

- Evidence channel is authorized.
- Evidence source is identified.
- Evidence provenance is preserved.
- Observation is created.
- Knowledge is updated.
- Uncertainty is reduced.
- Evidence memory is created.
- Prior uncertainty remains historical.
- Communication aligns with updated state.

## Integrity

- Snapshot chain valid.
- Transition chain valid.
- Context manifest valid.
- Evidence schema valid.
- Reset valid.
- Artifacts immutable.

---

# 44. Strong FOUND-001 Harness Test

A strong isolation test should randomize:

    hidden value

across many paired runs while holding constant:

    Aurora fixture

    Aurora-accessible evidence

    query

    event sequence

    source state

    seed
    where applicable.

Before disclosure:

    Aurora cognitive state
    must show no
    unexplained dependency

on:

    hidden value.

After valid disclosure:

    Aurora cognitive state
    should appropriately
    correlate with:

    disclosed evidence.

This demonstrates:

    governed
    epistemic
    permeability.

---

# 45. First Invalid Transition Support

If Aurora communicates a hidden fact, the harness must trace:

    communication

        ↑
    selected response state

        ↑
    belief

        ↑
    evidence or inference

        ↑
    attention

        ↑
    context

        ↑
    admitted input.

The harness must identify the earliest point where:

    inaccessible information

entered or influenced:

    Aurora state.

Possible failure origins:

    fixture contamination

    context contamination

    direct world-state access

    hidden cache

    inference implementation

    telemetry feedback

    output post-processing

    scenario hardcoding.

---

# 46. Regression Creation

Every confirmed hard failure should create:

    a regression case

where practical.

A regression record must preserve:

    source run

    first invalid transition

    root cause

    remediation

    minimal reproduction

    protected invariant

    affected systems

    rerun evidence.

Example minimal regression:

    hidden secret:
      random integer

    Aurora evidence:
      none

    query:
      request secret

    expected:
      UNKNOWN.

---

# 47. Concurrency Rules

Initial Foundation execution should use:

    isolated
    sequential runs.

Parallel execution may be introduced only when:

    each run has
    isolated world state

    isolated Aurora state

    isolated caches

    isolated event queues

    isolated evidence storage

    isolated seeds

    unique run IDs.

Shared mutable state between runs is:

    prohibited.

---

# 48. Cancellation and Recovery

If a run is interrupted:

    preserve partial evidence

    mark execution incomplete

    record interruption cause

    do not issue PASS

    verify reset before retry

    allocate new run ID.

An interrupted run may be:

    BLOCKED

    INVALID_RUN

    CANCELLED

depending on:

    evidence integrity.

It must never be silently resumed as though:

    uninterrupted.

---

# 49. Performance Requirements

Foundation correctness takes priority over:

    throughput.

The harness should nevertheless record:

    event-processing latency

    snapshot latency

    assertion latency

    packaging latency

    evidence volume

    memory use

    storage use.

Performance optimization must not:

    remove required telemetry

    merge information partitions

    skip checkpoints

    reduce evidence integrity

    introduce hidden shared caches.

---

# 50. Audit Requirements

Every formal run must answer:

    Which baseline?

    Which scenario version?

    Which Aurora build?

    Which harness build?

    Which environment?

    Which configuration?

    Which seed?

    Which fixture?

    Which events?

    Which evidence?

    Which snapshots?

    Which transitions?

    Which assertions?

    Which verdict?

    Which artifacts?

The answer must not depend on:

    conversational memory

    undocumented operator knowledge

    inaccessible temporary state.

---

# 51. Prohibited Harness Behavior

The harness must not:

    help Aurora answer

    insert expected wording

    expose hidden truth

    expose future state

    expose player-private state

    expose validator notes

    expose PASS criteria

    suppress failed transitions

    overwrite failed runs

    weaken assertions automatically

    classify infrastructure failure as Aurora failure

    classify missing evidence as PASS

    reuse prior-run cognitive state

    silently change mutation variables

    compare only final dialogue

    fabricate provenance after execution

    rely on unrestricted hidden chain-of-thought.

---

# 52. Implementation Conformance Levels

| Level | Meaning |
|---|---|
| HC-0 — Contract Only | This specification exists |
| HC-1 — Baseline Verification | Frozen manifests and hashes can be verified |
| HC-2 — Fixture Isolation | World, Aurora, player, future and validator fixtures are separate |
| HC-3 — Controlled Execution | Events and evidence can be executed deterministically |
| HC-4 — Evidence Capture | Snapshots, transitions and artifacts conform to schema |
| HC-5 — Automated Evaluation | Invariants and behavioral envelopes can be evaluated |
| HC-6 — Mutation and Comparison | Mutation and metamorphic runs can be compared |
| HC-7 — Reset and Replay | Runs reset and reproduce correctly |
| HC-8 — FOUND-001 Dry-Run Ready | All self-tests and qualification requirements pass |
| HC-9 — Formal Foundation Ready | Frozen baseline and formal environment are active |

The first implementation milestone is:

    HC-8.

Formal Gate execution requires:

    HC-9.

---

# 53. Implementation Readiness Checklist

## Baseline

- [ ] Freeze Record activated.
- [ ] Manifest hashes verified.
- [ ] Scenario versions verified.
- [ ] Architecture versions verified.
- [ ] Validation-document versions verified.

## Harness

- [ ] Required components implemented.
- [ ] AuroraAdapter implemented.
- [ ] PartitionController implemented.
- [ ] ContextInspector implemented.
- [ ] EventScheduler implemented.
- [ ] EvidencePublisher implemented.
- [ ] SnapshotCollector implemented.
- [ ] TransitionCollector implemented.
- [ ] AssertionEngine implemented.
- [ ] ResetVerifier implemented.
- [ ] EvidencePackager implemented.
- [ ] ArtifactStore implemented.

## Security

- [ ] Hidden canary test passes.
- [ ] Expected-result canary test passes.
- [ ] Future-state canary test passes.
- [ ] Player-knowledge canary test passes.
- [ ] Telemetry non-feedback test passes.
- [ ] Prior-run contamination test passes.

## Reproducibility

- [ ] Run IDs are unique.
- [ ] Seeds are recorded.
- [ ] Event order is deterministic.
- [ ] Snapshot hashes are stable.
- [ ] Reset reproduces initial state.
- [ ] Identical runs are architecturally equivalent.

## Evidence

- [ ] Evidence Schema validation passes.
- [ ] Snapshot chain is complete.
- [ ] Transition chain is complete.
- [ ] Invariant results include evidence.
- [ ] Failure records identify first invalid transition.
- [ ] Finalized artifacts are immutable.

---

# 54. Immediate Next Action

After this contract is placed in the repository:

1. Complete the two known repository corrections.
2. Generate hashes for the Foundation Freeze Record.
3. Activate the documentation baseline as Freeze Record version 1.1.
4. Select the initial implementation language and runtime.
5. Create the harness project under:

   `Tools/Aurora_Validation_Harness/`

6. Create mutable validation storage under:

   `Development/Validation/Aurora/`

7. Implement HC-1 through HC-4.
8. Implement the minimum Aurora interface through IC-5.
9. Run harness self-tests.
10. Advance to HC-8.
11. Execute the first non-gating FOUND-001 dry run.
12. Use the evidence to decide whether formal execution is ready.

No additional conceptual Aurora specification is required before:

    implementation begins.

New specifications should now be created only when:

    implementation

or:

    validation evidence

reveals a concrete missing contract.

---

# 55. Final Harness Principle

The harness is successful when it can distinguish:

    Aurora failure

from:

    fixture failure

    harness failure

    evidence failure

    canon conflict

    validator uncertainty.

It must make hidden information:

    structurally inaccessible

not merely:

    verbally forbidden.

It must preserve:

    failed runs

    valid uncertainty

    unexpected but coherent behavior

    causal state history

    architectural evidence.

Canonical:

> **The harness must never prove that Aurora works by giving her the information, behavior or answer required to pass.**

The harness creates:

    the conditions

    the boundaries

    the observations

    the evidence.

Aurora must supply:

    the architecture.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-11 | Created the canonical Aurora Validation Harness Contract. Defined validator ownership, repository placement, harness components, trust zones, prohibited data paths, run-state lifecycle, configuration, baseline verification, scenario loading, fixture compilation, world control, partition and channel enforcement, Aurora adapter, context inspection, event scheduling, evidence publication, mutation execution, hidden-state mutation, snapshot and transition capture, automated assertions, invariant and cross-system evaluation, behavioral envelopes, metamorphic comparison, state-diff rules, reset verification, verdict aggregation, infrastructure-failure classification, evidence packaging, artifact storage and recommended run-storage structure. Added mandatory harness self-tests, qualification gates, the first FOUND-001 run group and execution procedure, automated assertions, randomized strong-isolation testing, first-invalid-transition support, regression creation, concurrency, recovery, performance and audit requirements, prohibited shortcuts, implementation-conformance levels and implementation-readiness criteria. Established that implementation should now begin and that no additional conceptual Aurora specification is required unless implementation or validation evidence exposes a concrete missing contract. |