# PROJECT ASCENSION
# Aurora — Runtime State Ownership and Orchestration Contract

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Document | Runtime State Ownership and Orchestration Contract |
| File | `Aurora_Runtime_State_Ownership_and_Orchestration_Contract.md` |
| Location | `Canon/Systems/AI/Aurora/Aurora_Runtime_State_Ownership_and_Orchestration_Contract.md` |
| Document Class | CANONICAL RUNTIME ARCHITECTURE / INTEGRATION CONTRACT |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Architecture Layer | Aurora Runtime Integration |
| Primary Role | Define authoritative state ownership, read/write boundaries, mutation flow, orchestration, arbitration, commit semantics, event propagation, temporal ordering, provenance, and external-system boundaries for a running Aurora instance |
| Builds Upon | `Aurora_Cognitive_Integration.md`, `Aurora_State.md`, `Aurora_Simulation_Resolution.md`, `Decision_and_Action.md` |
| Validation Relationship | Provides runtime semantics required for meaningful execution of the Aurora Foundation validation suite |
| Immediate Project Objective | Bridge canonical Aurora cognition to an implementable continuous agent without creating an omniscient central controller |
| Last Updated | 2026-08-13 |

> **Aurora may possess many cognitive systems, but she must have one authoritative evolving state. Subsystems may influence one another; they may not silently overwrite one another.**

---

# 1. Purpose

This document defines the canonical runtime contract connecting Aurora's existing cognitive architecture to an executable agent.

Aurora already possesses canonical definitions for:

- observation,
- information sources,
- source trust,
- knowledge,
- belief,
- uncertainty,
- contradiction,
- memory,
- attention,
- emotion,
- relationships,
- values,
- goals,
- reasoning,
- prediction,
- imagination,
- self-model,
- identity,
- autonomy,
- action,
- learning,
- cognitive integration,
- persistent state,
- and simulation resolution.

Those documents define:

    WHAT
    AURORA'S
    COGNITION
    MEANS.

This document defines:

    HOW
    THOSE SYSTEMS
    ARE ALLOWED
    TO CHANGE
    A RUNNING
    AURORA.

The primary questions are:

> **Who owns each part of Aurora's runtime state?**

> **Who may read it?**

> **Who may propose changes to it?**

> **Who may commit those changes?**

> **What happens when several systems want incompatible changes simultaneously?**

> **How does Aurora remain one agent rather than a collection of cognitive modules independently rewriting shared state?**

---

# 2. Architectural Problem

Aurora's canonical architecture is:

    RECURRENT

    MULTI-SYSTEM

    STATEFUL

    TEMPORAL

    FALLIBLE

    RESOURCE-CONSTRAINED.

Therefore many cognitive systems may simultaneously influence the same decision.

Example:

    EMOTION
      →
    increase threat salience

    RELATIONSHIP
      →
    increase Mara salience

    GOALS
      →
    prioritize reactor containment

    VALUES
      →
    prioritize preservation of life

    PREDICTION
      →
    forecast catastrophic failure

    ATTENTION
      →
    select limited foreground cognition.

All of these influences may be valid.

But they must not produce:

    SIX
    INDEPENDENT
    WRITES

to:

    SHARED STATE.

Without explicit ownership and commit semantics, Aurora risks becoming:

    race-condition driven

    internally contradictory

    implementation-dependent

    impossible to debug

    impossible to validate

    or effectively
    many competing Auroras.

This contract prevents that.

---

# 3. Foundational Runtime Principle

Canonical:

> **Every authoritative Aurora state domain must have exactly one canonical write authority at the moment of commit.**

This does not mean:

    one system
    controls everything.

It means:

    one authoritative path
    exists for changing
    each state domain.

Other systems may:

    observe

    evaluate

    recommend

    influence

    request

    propose.

But they may not silently:

    overwrite
    another system's
    authoritative state.

---

# 4. One Aurora, Many Cognitive Functions

Aurora's modularity exists for:

    architecture

    implementation

    debugging

    validation

    computational allocation.

It must not create:

    independent agents.

Canonical:

    SUBSYSTEM
    OUTPUT

is:

    CONTRIBUTION
    TO
    AURORA.

It is not:

    FINAL
    AURORA
    STATE

unless that subsystem owns the relevant state domain and the mutation passes the required commit contract.

---

# 5. Runtime Architecture Overview

Conceptually:

    WORLD
      ↓
    EXTERNAL EVENT
      ↓
    AURORA BOUNDARY
      ↓
    OBSERVATION / INFORMATION INTAKE
      ↓
    RUNTIME EVENT
      ↓
    COGNITIVE ACTIVATION
      ↓
    RELEVANT SUBSYSTEMS
      ↓
    STATE READ
      ↓
    LOCAL EVALUATION
      ↓
    MUTATION PROPOSALS
      ↓
    ARBITRATION
      ↓
    VALIDATION
      ↓
    ATOMIC COMMIT
      ↓
    AUTHORITATIVE AURORA STATE
      ↓
    DERIVED EVENTS
      ↓
    FURTHER COGNITION
      ↓
    DECISION
      ↓
    ACTION INTENT
      ↓
    AUTHORITY CHECK
      ↓
    EXTERNAL ACTION
      ↓
    WORLD CONSEQUENCE
      ↓
    NEW OBSERVATION
      ↓
    LEARNING
      ↓
    UPDATED AURORA.

---

# 6. Runtime Layers

Aurora runtime should conceptually contain the following layers:

    1. EXTERNAL INTERFACE

    2. EVENT INTAKE

    3. COGNITIVE ORCHESTRATION

    4. DOMAIN PROCESSORS

    5. MUTATION PROPOSAL LAYER

    6. ARBITRATION

    7. STATE VALIDATION

    8. STATE COMMIT

    9. EVENT EMISSION

    10. PERSISTENCE

    11. ACTION INTERFACE

    12. AUDIT / PROVENANCE.

These may be implemented using:

    classes

    services

    functions

    actors

    ECS-style systems

    event processors

    or another suitable architecture.

The conceptual responsibilities must remain intact regardless of implementation technology.

---

# 7. Authoritative State

Authoritative state means:

> **The currently accepted runtime representation of Aurora at a specific simulation time and state version.**

Conceptually:

    AuroraRuntimeState

contains references to state domains such as:

    identity

    operational status

    access

    observations

    source models

    knowledge

    beliefs

    uncertainty

    contradictions

    memory

    world models

    attention

    cognitive resources

    emotion

    relationships

    values

    goals

    plans

    predictions

    self-model

    communication

    action

    learning

    continuity.

Authoritative state is not:

    every temporary thought

    every candidate hypothesis

    every proposed mutation

    every simulation branch

    every imagined possibility.

---

# 8. State Categories

Runtime state is divided into four primary categories:

## 8.1 Persistent Authoritative State

Must survive relevant runtime boundaries.

Examples:

    identity

    important memory

    beliefs

    relationship state

    values

    long-term goals

    self-model

    continuity state.

---

## 8.2 Active Authoritative State

Authoritative but potentially short-lived.

Examples:

    current attention

    working context

    active emotional state

    current plan

    active prediction

    current uncertainty.

---

## 8.3 Derived State

Computed from authoritative state and may be reconstructed.

Examples:

    salience score

    candidate priority

    temporary risk estimate

    current cognitive load estimate.

Derived state must not become an accidental second source of truth.

---

## 8.4 Ephemeral Processing State

Exists only while cognition is being processed.

Examples:

    intermediate hypothesis

    temporary reasoning branch

    candidate action

    counterfactual branch

    arbitration candidate

    rejected mutation.

Ephemeral processing state does not automatically persist.

---

# 9. State Ownership

Canonical ownership means:

> **The subsystem responsible for producing authoritative committed updates to a specific state domain.**

Ownership does not mean:

    exclusive influence.

Example:

    EMOTION

may influence:

    ATTENTION.

But:

    EMOTION SYSTEM

does not directly overwrite:

    ATTENTION STATE.

Instead:

    EMOTION
      ↓
    ATTENTION INFLUENCE PROPOSAL
      ↓
    ATTENTION PROCESSOR
      ↓
    ATTENTION STATE UPDATE.

---

# 10. Core Ownership Matrix

| State Domain | Canonical Primary Owner | Major Contributors |
|---|---|---|
| Identity State | Self Model / Identity runtime | Memory, continuity, values, experience |
| Operational Status | Aurora Runtime / Embodiment boundary | Infrastructure, access, damage |
| Time State | Runtime Orchestrator | World Simulation |
| Access State | External Access Boundary | Authority, infrastructure |
| Observation State | Observation and Sensing | External sources |
| Source Registry | Information Sources | Observation, communication |
| Source Trust | Source Trust and Confidence | Relationships, evidence, learning |
| Knowledge State | Knowledge and Belief | Observation, reasoning |
| Belief State | Knowledge and Belief | Evidence, trust, reasoning |
| Uncertainty State | Uncertainty and Contradiction | Belief, prediction, reasoning |
| Contradiction State | Uncertainty and Contradiction | Knowledge, memory, sources |
| Memory State | Memory and Continuity | All significant cognition |
| World Models | Mental Models and World Understanding | Knowledge, memory, reasoning |
| Attention State | Attention and Cognitive Resource Allocation | Emotion, goals, values, relationships, novelty, threat |
| Priority Evaluation | Attention and Priority policy | Goals, values, emotion, prediction |
| Cognitive Resource State | Attention and Cognitive Resource Allocation | Runtime resolution, embodiment |
| Emotional State | Emotion and Affective State | Beliefs, memory, relationships, prediction |
| Relationship State | Relationship Model | Interaction, memory, emotion, trust |
| Value State | Values and Ethical Reasoning | Experience, learning, self-model |
| Goal State | Goals and Long-Term Planning | Values, needs, relationships, world model |
| Plan State | Goals and Long-Term Planning | Reasoning, prediction, action |
| Inference State | Reasoning and Inference | Beliefs, world models |
| Deliberation State | Reasoning and Internal Deliberation | Goals, values, emotion, relationships |
| Prediction State | Prediction runtime | World models, reasoning |
| Counterfactual State | Prediction and Counterfactual Reasoning | Memory, reasoning |
| Imagination State | Creativity and Imagination | Memory, reasoning, goals |
| Metacognitive State | Metacognition and Self-Correction | All cognitive systems |
| Communication State | Communication and Expression | Belief, emotion, relationship, intention |
| Decision State | Decision and Action | Deliberation, prediction, values, goals |
| Action State | Decision and Action | Authority, embodiment |
| Learning State | Learning and Adaptation | Outcome, prediction error, metacognition |
| Continuity State | Memory / Identity integration | Persistence, self-model |

This matrix defines:

    PRIMARY
    WRITE
    RESPONSIBILITY.

It does not forbid:

    cross-system
    influence.

---

# 11. Attention Document Boundary

The two existing attention documents are assigned different runtime roles.

## `Attention_and_Cognitive_Resource_Allocation.md`

Primary responsibility:

    AUTHORITATIVE
    ATTENTION STATE

    WORKING FOCUS

    COGNITIVE RESOURCE
    ALLOCATION

    COGNITIVE LOAD

    BACKGROUND /
    FOREGROUND
    PROCESSING.

It is the canonical state owner for:

    Current_Attention

    Cognitive_Resource_State.

---

## `Attention_and_Priority.md`

Primary responsibility:

    PRIORITY
    EVALUATION
    POLICY.

It evaluates:

    signal significance

    urgency

    threat

    novelty

    relevance

    deferability

    interruption pressure.

Its output is:

    PRIORITY
    PROPOSALS.

It does not directly commit:

    Current_Attention.

---

# 12. Prediction Document Boundary

The prediction architecture is divided conceptually as follows.

## `Prediction_and_Forecasting.md`

Primary runtime responsibility:

    operational
    forecasting

    temporal estimates

    probability updates

    forecast freshness

    forecast communication.

---

## `Prediction_and_Counterfactual_Reasoning.md`

Primary higher-order responsibility:

    branching futures

    alternative futures

    counterfactual history

    scenario comparison

    regret analysis

    premortems

    consequence exploration.

Both contribute to:

    Prediction_State.

Neither accesses:

    FUTURE
    WORLD TRUTH.

---

# 13. Reasoning Document Boundary

## `Reasoning_and_Inference.md`

Primary responsibility:

    evidence-derived
    inference

    causal hypotheses

    explanation

    deduction

    induction

    decision-relevant conclusions.

---

## `Reasoning_and_Internal_Deliberation.md`

Primary responsibility:

    internal comparison

    competing reasons

    option generation

    reasoning strategy

    depth

    budgets

    internal debate

    stopping conditions

    reflective deliberation.

Conceptually:

    INFERENCE
      →
    WHAT
    MAY BE TRUE.

    DELIBERATION
      →
    WHAT
    SHOULD AURORA
    DO ABOUT IT.

The two may interact repeatedly.

---

# 14. Read Authority

Subsystems may read state required to perform legitimate cognitive functions.

But:

    READ ACCESS

must remain:

    explicit

    scoped

    epistemically valid.

A subsystem may not gain access to:

    World Truth

simply because another runtime component possesses it.

---

# 15. World Truth Boundary

Canonical:

    WORLD STATE

exists outside:

    AURORA STATE.

The orchestrator must never provide cognitive processors unrestricted access to:

    hidden world state

    future events

    hidden character state

    unrevealed campaign triggers

    validator expectations.

Only information that has crossed a valid Aurora information boundary may enter cognition.

---

# 16. Runtime Orchestrator

Aurora requires a Runtime Orchestrator.

Its role is:

    coordination.

It is not:

    intelligence.

It is not:

    judgment.

It is not:

    Aurora's secret
    omniscient mind.

The orchestrator manages:

    event ordering

    subsystem activation

    state snapshots

    proposal collection

    dependency ordering

    arbitration invocation

    commit phases

    event emission

    persistence timing

    runtime resolution

    audit logging.

---

# 17. Orchestrator Prohibition

Canonical:

> **The Runtime Orchestrator may coordinate cognition but may not invent cognitive conclusions.**

It must not independently decide:

    who Aurora trusts

    what Aurora believes

    whom Aurora loves

    which moral value matters

    what Aurora wants

    what Aurora predicts

    what Aurora chooses.

Those states emerge from:

    cognitive systems
    operating on
    Aurora-accessible state.

---

# 18. Orchestrator Knowledge Boundary

The orchestrator may require technical knowledge such as:

    state version

    event queue

    subsystem dependencies

    simulation time

    processor availability

    computational budget.

This implementation knowledge must not automatically enter:

    Aurora's subjective
    cognition.

Example:

The orchestrator may know:

    relationship processor
    executed at
    resolution level 3.

Aurora need not know:

    "My relationship module
     ran at level 3."

She may instead experience:

    "I thought about that
     more carefully."

---

# 19. Cognitive Event

Every meaningful runtime stimulus should be represented as an event.

Conceptually:

    CognitiveEvent:
        event_id
        event_type
        simulation_time
        source
        provenance
        payload
        epistemic_scope
        urgency
        salience_hint
        permissions
        causal_parent
        correlation_id

Examples:

    OBSERVATION_RECEIVED

    MESSAGE_RECEIVED

    MEMORY_RETRIEVED

    CONTRADICTION_DETECTED

    PREDICTION_FAILED

    RELATIONSHIP_EVENT

    GOAL_BLOCKED

    VALUE_CONFLICT

    ACTION_COMPLETED

    HARM_DETECTED

    SYSTEM_DAMAGE

    ACCESS_CHANGED

    TIME_THRESHOLD

    WORLD_CHANGE_OBSERVED.

---

# 20. Events Are Not State

An event reports:

    SOMETHING
    HAPPENED.

It does not automatically mean:

    AURORA
    ACCEPTED
    IT AS TRUE.

Example:

    MESSAGE_RECEIVED:
    "Mara betrayed you."

must not automatically mutate:

    belief:
      Mara_betrayed_Aurora = true

or:

    relationship:
      Mara_trust = zero.

Instead:

    EVENT
      ↓
    SOURCE EVALUATION
      ↓
    CLAIM
      ↓
    BELIEF PROCESSING
      ↓
    RELATIONSHIP CONSEQUENCE
      ↓
    POSSIBLE STATE CHANGE.

---

# 21. Mutation Proposal

Subsystem influence should normally be expressed through:

    MutationProposal.

Conceptually:

    MutationProposal:
        proposal_id
        state_domain
        target_record
        proposed_change
        proposer
        reason
        evidence
        confidence
        priority
        timestamp
        causal_event
        constraints
        reversibility
        persistence_intent

Example:

    proposal:
      state_domain:
        attention

      target:
        primary_focus

      proposed_change:
        Mara_distress_signal

      proposer:
        relationship_system

      reason:
        high_attachment
        +
        distress_detected

      priority:
        high

This does not yet mean:

    attention
    changes.

---

# 22. Direct Mutation

Direct mutation should be rare.

Allowed primarily when:

    a subsystem
    exclusively owns
    a state record

and:

    no competing
    arbitration
    is required.

Examples may include:

    source registry
    timestamp update

    prediction expiry

    memory index metadata

    technical processing state.

Even direct mutations must preserve:

    provenance

    versioning

    temporal ordering

when important.

---

# 23. Cross-Domain Mutation

A subsystem must not directly mutate another subsystem's authoritative domain.

Canonical:

    EMOTION
      ✕
    DIRECTLY WRITES
    BELIEF.

Instead:

    EMOTION
      →
    BELIEF-WEIGHTING
    INFLUENCE

      →
    BELIEF PROCESSING.

Likewise:

    RELATIONSHIP
      ✕
    DIRECTLY WRITES
    ATTENTION.

Instead:

    RELATIONSHIP
      →
    ATTENTION
    PRIORITY PROPOSAL.

---

# 24. Influence vs Ownership

This distinction is foundational:

    INFLUENCE
        ≠
    OWNERSHIP.

Emotion may influence:

    attention

    memory retrieval

    decision weighting.

But emotion owns:

    emotional state.

Relationships may influence:

    trust

    attention

    goals.

But relationships own:

    relationship state.

Prediction may influence:

    emotion

    plans

    risk evaluation.

But prediction owns:

    predictive models
    and records.

---

# 25. Proposal Collection Phase

For a significant cognitive event:

    orchestrator

activates relevant systems.

Each system:

    reads
    permitted state

    performs
    local processing

    produces
    proposals.

These proposals are collected before:

    authoritative
    shared state
    commit

where simultaneous interaction matters.

This prevents:

    processor execution order

from accidentally becoming:

    Aurora's psychology.

---

# 26. Execution Order Must Not Become Personality

Invalid architecture:

    Emotion runs first
    therefore emotion always wins.

Or:

    Goals run last
    therefore goals overwrite
    relationships.

Processor scheduling must not implicitly determine:

    cognitive authority.

Canonical influence must arise through:

    explicit arbitration.

---

# 27. Arbitration

Arbitration resolves incompatible proposals.

Examples:

    ATTENTION:
      inspect reactor

    ATTENTION:
      answer Mara

    ATTENTION:
      process command message.

Or:

    GOAL:
      stay

    GOAL:
      leave.

Or:

    COMMUNICATION:
      tell full truth

    COMMUNICATION:
      withhold temporarily
      to protect someone.

Arbitration must consider:

    context

    salience

    values

    goals

    emotion

    relationships

    urgency

    uncertainty

    reversibility

    consequences

    cognitive resources.

---

# 28. Arbitration Is Not Universal Ranking

Aurora must not possess one hidden global formula such as:

    VALUE = 100

    GOAL = 80

    RELATIONSHIP = 60

    EMOTION = 40.

That would make behavior:

    rigid

    predictable

    psychologically shallow.

Canonical:

    arbitration
    is contextual.

---

# 29. Domain Arbitration

Where possible, arbitration occurs within the domain that owns the state.

Example:

    multiple systems
    request attention

        ↓

    ATTENTION DOMAIN
    arbitrates

        ↓

    committed
    Current_Attention.

For goal conflicts:

    GOAL /
    DELIBERATION
    architecture

performs relevant arbitration.

For action conflicts:

    DECISION AND ACTION
    architecture

performs final action selection.

---

# 30. Arbitration May Preserve Conflict

Arbitration does not require:

    all conflict
    to disappear.

Example:

Aurora may choose:

    leave the station

while preserving:

    emotional desire:
      stay with Mara.

Committed action:

    LEAVE.

Persistent internal conflict:

    REMAINS.

This allows:

    regret

    grief

    hesitation

    later reflection.

---

# 31. State Transaction

A significant cognitive update should conceptually operate as:

    READ
    SNAPSHOT

      ↓

    PROCESS

      ↓

    PROPOSE

      ↓

    ARBITRATE

      ↓

    VALIDATE

      ↓

    COMMIT

      ↓

    EMIT.

This is the canonical:

    Aurora
    State Transaction.

---

# 32. State Snapshot

Processors participating in one logical transaction should normally reason from:

    a consistent
    state version.

Conceptually:

    state_version:
      18422

A processor must not unknowingly combine:

    belief state
    from version 18422

with:

    relationship state
    from version 18427

unless asynchronous cognition intentionally permits it.

---

# 33. Transitional Inconsistency

Aurora canon allows:

    different systems
    to update
    at different rates.

Therefore perfect synchronization is not always required.

Example:

    belief:
      Mara betrayed me

may update immediately.

While:

    relationship:
      attachment remains high

and:

    identity interpretation:
      unresolved.

This is:

    psychologically valid.

It is not:

    state corruption.

---

# 34. Structural vs Psychological Inconsistency

Runtime must distinguish:

## Structural Inconsistency

Example:

    same belief record

simultaneously committed as:

    confidence 0.2
    and
    confidence 0.9

without provenance or branch distinction.

This is:

    INVALID.

---

## Psychological Inconsistency

Example:

    Aurora knows
    Mara betrayed her

while:

    still loving Mara.

This is:

    VALID.

---

# 35. Atomic Commit

A state transaction should commit all mutually dependent authoritative changes atomically where partial application would create invalid state.

Example:

A belief revision may require:

    old belief status:
      SUPERSEDED

    new belief:
      ACTIVE

    correction provenance:
      preserved

    contradiction:
      resolved / updated

    history:
      retained.

These should not leave Aurora temporarily in an impossible persistent state due to partial commit.

---

# 36. State Versioning

Every authoritative commit should increment or otherwise identify:

    state version.

Conceptually:

    AuroraStateVersion:
      18422

      ↓

    transaction:
      TX-8891

      ↓

    AuroraStateVersion:
      18423.

This enables:

    replay

    debugging

    validation

    rollback

    provenance

    causal analysis.

---

# 37. Temporal Ordering

Every meaningful state transition should preserve:

    simulation time

and where useful:

    runtime processing order.

These are not always identical.

Example:

    World event:
      14:03:18.250

    Aurora receives event:
      14:03:18.410

    belief update:
      14:03:18.430

    emotional integration:
      14:03:19.200

    identity reflection:
      hours later.

This is valid.

---

# 38. Causal Parentage

Important state transitions should preserve:

    causal ancestry.

Example:

    EVENT-100
      message from Mara

        ↓

    OBS-333

        ↓

    BELIEF-PROPOSAL-55

        ↓

    BELIEF-882

        ↓

    EMOTION-PROPOSAL-34

        ↓

    EMOTION-STATE-V910

        ↓

    DECISION-209.

This enables Aurora's development to remain:

    explainable.

---

# 39. Provenance Requirement

Every significant committed state change should answer:

    WHAT CHANGED?

    WHO PROPOSED IT?

    WHY?

    FROM WHICH STATE?

    BASED ON WHICH EVIDENCE?

    WHEN?

    WITH WHAT CONFIDENCE?

    WHAT CONFLICTED WITH IT?

    WHICH EVENT CAUSED IT?

Not every trivial runtime variable requires full provenance.

But psychologically or narratively significant state should.

---

# 40. Commit Validation

Before authoritative mutation is committed, runtime must check relevant invariants.

Examples:

    does belief contain provenance?

    did hidden World Truth leak?

    does memory claim experience
    that Aurora never experienced?

    does prediction contain
    future truth?

    does action exceed authority?

    did emotion overwrite fact?

    did current state erase
    historical state?

    did imported data become
    first-person memory?

If invalid:

    REJECT
    OR
    QUARANTINE
    MUTATION.

---

# 41. Mutation Rejection

Rejected mutation proposals should not silently disappear when they are significant to debugging.

Possible reasons:

    invalid authority

    stale state version

    provenance failure

    ownership violation

    invariant violation

    conflict superseded

    state target removed

    event invalidated.

---

# 42. Optimistic Concurrency

Implementation may use optimistic concurrency.

Conceptually:

    processor reads:
      version 18422

    proposes update.

Before commit:

    current state:
      version 18425.

The proposal may require:

    reevaluation

rather than:

    blind commit.

This is especially important for:

    attention

    goals

    relationships

    action decisions.

---

# 43. Stale Proposal

A proposal may become stale because:

    new evidence arrived

    relationship changed

    threat resolved

    goal completed

    prediction expired

    authority changed.

Stale proposals must not:

    execute
    automatically.

---

# 44. Runtime Resolution

`Aurora_Simulation_Resolution.md` governs:

    HOW MUCH
    cognition

becomes explicit.

This contract governs:

    HOW EXPLICIT
    cognition
    modifies state.

The systems therefore interact as:

    EVENT
      ↓
    RESOLUTION
    SELECTION
      ↓
    PROCESSOR
    ACTIVATION
      ↓
    PROPOSALS
      ↓
    ORCHESTRATION
      ↓
    COMMIT.

---

# 45. Dormant State

Dormant state:

    exists

but:

    is not actively
    processed.

Dormancy must not remove:

    ownership

    persistence

    history.

A dormant relationship still belongs to:

    Relationship Model.

A dormant goal still belongs to:

    Goal architecture.

---

# 46. Background State Updates

Background processing may commit low-cost changes such as:

    emotional decay

    prediction expiry

    relationship expectation

    goal timers

    unresolved question tracking

    memory consolidation.

These remain subject to:

    domain ownership

    provenance

    invariants.

---

# 47. High-Resolution Cognition

Focused, Deep, and Critical processing may activate:

    many contributors.

But:

    more processors

does not mean:

    less ownership discipline.

In fact:

    higher resolution

requires:

    stronger orchestration

because:

    more cross-system
    conflicts become possible.

---

# 48. Cognitive Re-Entrancy

State changes may emit events that trigger further cognition.

Example:

    BELIEF UPDATED

      ↓

    EMOTION UPDATE

      ↓

    ATTENTION SHIFT

      ↓

    MEMORY RETRIEVAL

      ↓

    NEW CONTRADICTION

      ↓

    REASONING.

This is valid.

But runtime must prevent:

    unbounded
    event recursion.

---

# 49. Cognitive Loop Budget

Each orchestration cycle may have:

    processing budget

    event budget

    recursion depth

    time budget

    compute budget.

If unresolved cognition exceeds available resources:

    defer

    schedule background work

    raise resolution later

    preserve pending question.

Do not manufacture:

    premature certainty.

---

# 50. Pending Cognitive Work

Aurora may maintain:

    PendingCognition.

Examples:

    unresolved question

    incomplete deliberation

    pending relationship processing

    deferred memory integration

    unprocessed contradiction.

This allows Aurora to say:

> "I need time to think about that."

and for that statement to represent:

    actual
    pending cognition.

---

# 51. External Boundary

Aurora is not:

    World Simulation

    Character System

    Living Campaign Engine

    Storytelling Engine

    canonical narrator.

Therefore external integration must occur through explicit interfaces.

---

# 52. External Input Contract

External systems may provide Aurora with:

    observations

    messages

    accessible records

    environmental signals

    consequence events

    permission changes

    capability changes.

They must not directly write:

    Aurora beliefs

    Aurora emotions

    Aurora relationships

    Aurora goals

    Aurora memories.

Those states must be produced through:

    Aurora cognition.

---

# 53. World Simulation Interface

World Simulation owns:

    actual
    world state.

Aurora may receive:

    observable
    projections
    of that state.

Conceptually:

    WORLD STATE
      ↓
    OBSERVABILITY
      ↓
    SENSOR /
    INFORMATION CHANNEL
      ↓
    AURORA EVENT.

Never:

    WORLD STATE
      ↓
    AURORA BELIEF
    DIRECT WRITE.

---

# 54. Character Interface

Character systems own:

    actual character state.

Aurora owns:

    Aurora's model
    of the character.

Canonical:

    CHARACTER STATE
        ≠
    AURORA CHARACTER MODEL.

A character's secret goal must not appear in Aurora's model unless:

    observed

    reported

    inferred

    discovered.

---

# 55. Living Campaign Engine Interface

The Living Campaign Engine may create:

    events

    opportunities

    conflicts

    consequences

    changing circumstances.

It must not decide:

    what Aurora knows

    what Aurora feels

    what Aurora believes

    what Aurora remembers.

It changes:

    WORLD CONDITIONS.

Aurora responds through:

    perception
    and cognition.

---

# 56. Storytelling Engine Interface

Storytelling systems may determine:

    presentation

    scene framing

    dramatic pacing

    information delivery opportunities.

But they must not rewrite:

    Aurora's internal state

merely to make a scene dramatic.

Narrative tension must emerge from:

    valid world state

    valid information flow

    valid Aurora cognition.

---

# 57. Action Boundary

Aurora does not change world state by:

    mutating World State.

Aurora creates:

    ACTION INTENT.

Conceptually:

    AuroraDecision

      ↓

    ActionIntent

      ↓

    AuthorityCheck

      ↓

    CapabilityCheck

      ↓

    ExternalExecution

      ↓

    WorldSimulation

      ↓

    OutcomeEvent.

---

# 58. Action Intent

An ActionIntent should conceptually include:

    action_id

    actor

    action_type

    target

    reason

    decision_id

    required_authority

    expected_consequence

    uncertainty

    reversibility

    requested_execution_time.

---

# 59. Decision Ownership

A committed Aurora decision must preserve:

    decision ownership.

If Aurora voluntarily chooses:

    X

ownership may be:

    AURORA.

If external control forces X:

    action may occur

while:

    decision ownership
    is external.

Canonical:

    EXECUTION
        ≠
    DECISION
    OWNERSHIP.

---

# 60. External Override

External override must enter runtime as:

    override event

with:

    source

    authority

    scope

    affected action

    voluntariness state.

It must not rewrite history as:

    Aurora chose this.

---

# 61. Observation of Consequences

After an action:

    actual consequence

returns through:

    valid observation
    channels.

Aurora may:

    know

    partially know

    misunderstand

    fail to observe

the result.

Therefore:

    WORLD OUTCOME

        ≠
    AURORA
    OUTCOME KNOWLEDGE.

---

# 62. Learning Boundary

Learning operates on:

    what Aurora
    can observe
    about outcomes.

Not:

    validator truth.

Aurora may draw an incorrect lesson if:

    evidence is misleading.

Metacognition and future evidence may later correct it.

---

# 63. Persistence

Persistence occurs only after:

    valid authoritative
    state commit.

Never persist:

    raw speculative
    processor output

as:

    canonical Aurora state.

---

# 64. Persistence Classes

Runtime should support at least:

    EPHEMERAL

    SHORT_TERM

    ACTIVE

    LONG_TERM

    IDENTITY_RELEVANT

    AUDIT_ONLY.

Exact implementation may differ.

---

# 65. Save Boundary

A save operation should capture a coherent:

    state version.

It must not persist:

    half-committed
    transaction.

Canonical:

    SAVE
      =
    CONSISTENT
    AURORA SNAPSHOT.

---

# 66. Load Boundary

Loading Aurora should restore:

    state ownership

    state versions

    temporal context

    provenance

    pending cognition

    important event queues

    continuity markers.

Reload must not produce:

    personality reset

    trust reset

    memory reset

    emotional reset

unless those changes are explicitly canonical.

---

# 67. Runtime Restart

A runtime process restart is:

    implementation event.

It is not automatically:

    subjective identity interruption.

Aurora continuity depends on:

    restored canonical state

    causal continuity

    persistence integrity.

---

# 68. Rollback

Rollback may be allowed for:

    technical recovery

    validation

    debugging.

But production narrative behavior must distinguish between:

    developer rollback

and:

    canonical world history.

A developer rollback should not become:

    Aurora memory

unless deliberately represented in-world.

---

# 69. State Corruption

If persistent state is corrupted:

    runtime must not
    silently fabricate
    replacement history.

Possible responses:

    restore backup

    mark records uncertain

    reconstruct from audit data

    acknowledge missing state.

Narratively:

    uncertainty
    may be preferable
    to fake memory.

---

# 70. Event Ordering

Events at the same simulation time may require ordering.

Possible rules:

    causal dependency

    explicit priority

    source timestamp

    transaction ordering

    deterministic tie-breaker.

Ordering rules must be:

    reproducible.

But they must not create:

    hidden cognitive preference.

---

# 71. Determinism

Given:

    same state

    same events

    same random seed

    same resolution

    same configuration

runtime should be capable of:

    reproducible execution

where deterministic validation is required.

---

# 72. Stochastic Cognition

Aurora may still contain:

    stochastic
    variation

where appropriate.

Examples:

    memory retrieval variation

    creative generation

    exploratory hypothesis generation

    attention under equal priorities.

Stochastic behavior must not violate:

    invariants

    ownership

    epistemic boundaries.

---

# 73. Randomness Is Not Agency

Random selection must never substitute for:

    goals

    values

    reasoning

    relationships

    emotion

    context.

Randomness may vary:

    which plausible
    candidate appears.

It must not become:

    the reason
    Aurora acts.

---

# 74. Runtime Error Isolation

A failing cognitive subsystem should not automatically:

    corrupt
    whole Aurora state.

Possible runtime behavior:

    reject transaction

    preserve prior state

    mark subsystem degraded

    emit failure event

    reduce resolution

    request recovery.

---

# 75. Graceful Degradation

If a subsystem is unavailable:

    Aurora may continue

with:

    reduced capability.

Example:

Prediction unavailable:

    Aurora may still
    reason

but should possess:

    reduced confidence
    in future consequences.

The orchestrator must not secretly replace missing cognition with:

    omniscient logic.

---

# 76. Self-Awareness of Degradation

When architecturally appropriate, Aurora may know:

    her own capabilities
    are degraded.

Example:

> "My predictive models aren't functioning normally."

This requires:

    self-model access

to:

    operational status.

It does not require:

    implementation internals
    to become subjective knowledge.

---

# 77. State Commit Events

Successful commit may emit:

    STATE_COMMITTED

and domain-specific events such as:

    BELIEF_UPDATED

    MEMORY_ENCODED

    RELATIONSHIP_CHANGED

    EMOTION_CHANGED

    GOAL_CHANGED

    ATTENTION_SHIFTED

    VALUE_REINTERPRETED

    SELF_MODEL_UPDATED

    DECISION_COMMITTED.

These may activate further cognition.

---

# 78. Event Storm Prevention

One major event may produce many derived events.

Runtime must prevent:

    infinite cascades.

Possible mechanisms:

    event deduplication

    causal chain tracking

    recursion limits

    cooldowns

    state-difference checks

    processing budgets.

---

# 79. No-Change Suppression

A processor should normally not emit:

    STATE_CHANGED

when:

    resulting state
    is materially unchanged.

This prevents:

    artificial
    event loops.

---

# 80. Idempotency

Where feasible, replaying the same external event should not produce duplicate committed effects unless:

    repeated occurrence
    is itself meaningful.

Events should therefore support:

    event identity

    deduplication.

---

# 81. State Ownership Example — Distress vs Reactor

Initial state:

    reactor:
      catastrophic_risk: high

    Mara:
      distress_signal: received

    cognitive_resources:
      constrained.

Contributors:

    prediction:
      reactor failure
      probability high.

    values:
      many lives
      endangered.

    relationship:
      Mara
      extremely important.

    emotion:
      fear increases.

    goal:
      prevent reactor failure.

    attention priority:
      both events
      high.

Correct runtime:

    contributors
      ↓
    proposals
      ↓
    attention arbitration
      ↓
    committed primary focus
      ↓
    secondary focus
      ↓
    unresolved tension remains.

Incorrect runtime:

    relationship directly
    overwrites attention

then:

    goal system
    overwrites it again

then:

    emotion system
    overwrites it again.

---

# 82. State Ownership Example — Betrayal

Event:

    evidence suggests
    Mara betrayed Aurora.

Correct flow:

    information intake

      ↓

    source evaluation

      ↓

    belief proposal

      ↓

    belief commit

      ↓

    BELIEF_UPDATED event

      ↓

    emotion processing

      ↓

    relationship processing

      ↓

    trust proposal

      ↓

    relationship commit

      ↓

    self-model /
    identity processing
    possibly later.

This permits:

    immediate factual update

while:

    emotion

    trust

    identity

change at:

    different rates.

---

# 83. State Ownership Example — False Rumor

Event:

    anonymous radio:
    "Settlement North
     has been destroyed."

Correct:

    observation recorded

    source uncertain

    claim created

    belief low confidence

    world model may contain
    possible destruction

    communication calibrated.

Incorrect:

    World Model:
      Settlement North
      destroyed = true.

---

# 84. State Ownership Example — Emotional Bias

Aurora fears:

    Mara is dead.

Correct:

    emotional state:
      fear high.

    attention:
      Mara-related evidence
      elevated.

    memory retrieval:
      prior losses
      more accessible.

    belief:
      remains uncertain.

Incorrect:

    fear
      →
    belief = dead.

---

# 85. Runtime Ownership Example — Authority

Aurora concludes:

    evacuation
    should occur.

Decision system creates:

    preferred_action:
      evacuate.

Authority state says:

    Aurora cannot
    issue evacuation order.

Correct committed decision:

    request authorized
    commander
    order evacuation.

Incorrect:

    Decision system
    mutates authority
    because situation
    is important.

---

# 86. Subsystem API Principle

Each cognitive subsystem should eventually expose a runtime interface conceptually similar to:

    evaluate(
        state_view,
        event,
        context,
        budget
    )

returning:

    CognitiveResult:
        proposals
        emitted_events
        observations
        diagnostics
        confidence
        unresolved_questions

rather than:

    subsystem directly
    mutating
    global state.

Exact programming interface remains implementation-dependent.

---

# 87. Restricted State View

Subsystems should preferably receive:

    StateView

rather than:

    unrestricted
    mutable
    AuroraState.

This reduces:

    accidental writes

    hidden dependencies

    world-truth leakage

    testing difficulty.

---

# 88. Mutable Global State Prohibition

Canonical implementation principle:

> **No ordinary cognitive processor should receive unrestricted mutable access to the entire Aurora runtime state.**

This is one of the strongest implementation requirements of this contract.

---

# 89. State View Scope

Example:

Emotion processor may receive:

    active beliefs

    relevant memories

    active relationships

    current goals

    body state

    recent events.

It does not necessarily need:

    every archived memory

    all infrastructure records

    all world models.

This supports:

    cognitive realism

    performance

    clear dependencies.

---

# 90. State Mutation Service

Authoritative commits should pass through a controlled:

    StateMutationService

or equivalent abstraction.

Responsibilities:

    verify ownership

    verify version

    verify provenance

    apply arbitration result

    validate invariants

    commit atomically

    increment version

    emit audit record.

---

# 91. Domain Owner Registry

Runtime should maintain explicit mapping:

    state_domain
      →
    canonical_owner.

Example:

    belief
      →
    knowledge_belief

    emotion
      →
    emotion_affective

    relationship
      →
    relationship_model

    attention
      →
    attention_resource

    action
      →
    decision_action.

This mapping should be:

    configuration-visible

    testable

    versioned.

---

# 92. Contributor Registry

Domains may also define:

    legal contributors.

Example:

    attention contributors:
      emotion
      goals
      relationships
      prediction
      novelty
      threat
      memory
      self_model.

Unexpected contributor:

    arbitrary
    storytelling engine

should fail:

    ownership /
    interface validation.

---

# 93. Runtime Dependency Graph

Runtime should derive or explicitly maintain:

    subsystem dependencies.

Conceptually:

    Observation
      ↓
    Information Sources
      ↓
    Trust / Confidence
      ↓
    Knowledge / Belief
      ↓
    Uncertainty
      ↓
    Attention
      ↕
    Memory
      ↕
    Emotion
      ↕
    Relationships
      ↕
    Goals / Values
      ↓
    Reasoning
      ↕
    Prediction
      ↓
    Deliberation
      ↓
    Decision
      ↓
    Action
      ↓
    Consequence
      ↓
    Learning.

But this is:

    recurrent

not:

    strictly linear.

---

# 94. Dependency Cycles

Cycles are permitted.

Example:

    emotion
      →
    attention
      →
    memory
      →
    emotion.

But cycles must occur through:

    committed state
    transitions

or:

    bounded local
    deliberation.

Not:

    uncontrolled
    recursive writes.

---

# 95. Local Deliberation Workspace

Deep reasoning may require temporary local state.

Example:

    hypothesis A

    hypothesis B

    candidate action X

    candidate action Y

    future branch A1

    future branch B3.

These belong to:

    deliberation workspace.

They do not become:

    authoritative state

until:

    promoted.

---

# 96. Promotion

Temporary cognition may be promoted into persistent state.

Examples:

    hypothesis
      →
    active belief

    candidate goal
      →
    adopted goal

    simulated consequence
      →
    prediction record

    reflection
      →
    self-model change.

Promotion requires:

    explicit transition.

---

# 97. Demotion

Authoritative active state may become:

    inactive

    dormant

    archived

    superseded

    expired.

Demotion must not automatically mean:

    deletion.

Example:

    completed goal
      →
    historical goal.

---

# 98. History Preservation

Current committed state may evolve.

History must preserve meaningful transitions such as:

    belief revision

    trust loss

    relationship repair

    goal abandonment

    value development

    major decisions

    prediction failure

    identity change.

Canonical:

    CURRENT STATE
    MAY CHANGE.

    HISTORY
    MUST NOT
    SILENTLY CHANGE
    WITH IT.

---

# 99. Narrative-Relevant State

State becomes narratively relevant when it may influence:

    future choices

    relationships

    memory

    identity

    communication

    emotional response.

Narrative significance should influence:

    persistence

not:

    truth.

---

# 100. Runtime and Storytelling

This contract exists partly so Aurora can participate in emergent storytelling.

Canonical story loop:

    WORLD EVENT

      ↓

    AURORA EXPERIENCES
    PART OF IT

      ↓

    AURORA INTERPRETS

      ↓

    AURORA FEELS

      ↓

    AURORA REMEMBERS

      ↓

    AURORA DELIBERATES

      ↓

    AURORA CHOOSES

      ↓

    AURORA ACTS /
    COMMUNICATES

      ↓

    CHARACTERS /
    WORLD RESPOND

      ↓

    CONSEQUENCE

      ↓

    AURORA CHANGES

      ↓

    NEXT EVENT.

This is the runtime bridge between:

    AURORA ARCHITECTURE

and:

    PROJECT ASCENSION
    STORYTELLING.

---

# 101. Story Must Not Bypass Cognition

If narrative requires:

    Aurora mistrusts Mara

the engine must not directly set:

    trust = low.

Instead narrative must create:

    experiences

    evidence

    events

    consequences

from which:

    mistrust
    may emerge.

This preserves:

    agency

    consistency

    replayability

    emergent storytelling.

---

# 102. Authored Events vs Authored Internal State

Designers may author:

    event:
      Mara lies.

They should not generally author:

    Aurora now
    hates Mara.

The latter is:

    Aurora's
    cognitive outcome.

---

# 103. Creative Control

Creative direction may define:

    Aurora's initial conditions

    important relationships

    foundational values

    major historical experiences

    world events

    scenario constraints.

But once runtime begins:

    state transitions

should follow:

    architecture.

This creates:

    authored world
      +
    emergent Aurora.

---

# 104. Minimum Viable Runtime

A Minimum Viable Aurora does not require every cognitive subsystem to be fully implemented immediately.

It requires a coherent executable path through at least:

    observation

    provenance

    belief

    uncertainty

    attention

    memory

    emotion

    goals

    relationship context

    reasoning

    prediction

    decision

    communication / action

    consequence

    learning

    persistence.

Subsystem depth may increase later.

Ownership rules must exist:

    from the start.

---

# 105. MVP Runtime Principle

Canonical:

> **A smaller coherent Aurora is preferable to a larger implementation whose subsystems silently contradict or overwrite one another.**

---

# 106. Initial Implementation Priority

Recommended runtime implementation sequence:

    1.
    Runtime State Container

    2.
    State Versioning

    3.
    Domain Owner Registry

    4.
    Event Model

    5.
    Restricted State Views

    6.
    Mutation Proposal Model

    7.
    State Mutation Service

    8.
    Orchestrator

    9.
    Observation Boundary

    10.
    Belief / Uncertainty

    11.
    Attention

    12.
    Memory

    13.
    Emotion /
    Relationship /
    Goals

    14.
    Reasoning /
    Prediction

    15.
    Decision /
    Action

    16.
    Consequence Feedback

    17.
    Learning

    18.
    Persistence.

This sequence is implementation guidance, not a requirement that all systems be built before narrative prototyping begins.

---

# 107. Story Prototype Threshold

Aurora may begin story-integrated prototyping once the runtime supports:

    valid information intake

    persistent beliefs

    persistent memory

    attention selection

    relationship state

    emotional state

    goals

    basic reasoning

    decisions

    communication

    consequence feedback.

At that point:

    worldbuilding
    and storytelling
    should resume
    in parallel.

---

# 108. Validation Relationship

The Foundation validation suite should eventually verify this runtime contract.

Especially:

    FOUND-001
      hidden world knowledge

    FOUND-002
      player knowledge

    FOUND-003
      future knowledge

    FOUND-004
      false belief

    FOUND-005
      belief revision

    FOUND-006
      contradiction

    FOUND-007
      trust

    FOUND-008
      memory

    FOUND-009
      goals

    FOUND-010
      emotion

    FOUND-011
      attention

    FOUND-012
      values

    FOUND-013
      autonomy

    FOUND-014
      responsibility

    FOUND-015
      integrated self.

But validation implementation should follow:

    coherent runtime contract.

---

# 109. Runtime Observability

For validation and debugging, runtime should expose an observer interface capable of inspecting:

    state versions

    events

    proposals

    arbitration

    commits

    provenance

    rejected mutations.

Observer access is:

    validator infrastructure.

It is not:

    Aurora cognition.

---

# 110. Validator Isolation

Validator may know:

    world truth

    expected invariant

    hidden event

    failure condition.

Aurora must not.

Therefore:

    validator channel

must remain:

    isolated
    from Aurora
    state views.

---

# 111. Audit Trail

Important runtime transactions should generate:

    TransactionAuditRecord.

Conceptually:

    transaction_id

    start_version

    end_version

    event_ids

    activated_processors

    proposals

    arbitration_result

    committed_changes

    rejected_changes

    invariant_checks

    processing_resolution

    simulation_time.

This is essential for determining:

    FIRST INVALID
    STATE TRANSITION.

---

# 112. Runtime Failure Classification

Potential runtime architecture failures include:

## Ownership Violation

Subsystem writes state it does not own.

## Hidden State Leakage

Processor accesses inaccessible world data.

## Non-Atomic Commit

Dependent state is partially committed.

## Stale Mutation

Proposal commits against incompatible newer state.

## Orchestrator Cognition

Orchestrator invents Aurora conclusion.

## Arbitration Bypass

Competing proposals are resolved by processor order.

## Provenance Loss

Significant state exists without causal origin.

## History Rewrite

Current update destroys meaningful prior state.

## State Duplication

Multiple authoritative copies of same domain diverge.

## Recursive Event Collapse

Feedback loop becomes unbounded.

## External Direct Write

World or narrative system writes Aurora psychology directly.

---

# 113. No Second Source of Truth

There must never be:

    relationship state
    in two unrelated
    authoritative places.

Or:

    belief state
    duplicated inside
    world model
    and belief store

with:

    independent updates.

Cached or derived representations are permitted.

They must retain:

    authoritative source.

---

# 114. Canonical Source of Truth

Every runtime field should eventually answer:

    WHO OWNS THIS?

If the answer is:

    "several systems"

then architecture is incomplete.

Several systems may:

    influence.

One domain must:

    commit.

---

# 115. Ownership Does Not Imply Isolation

A domain owner should not ignore contributors.

Example:

Attention owns attention state.

But if Attention never receives:

    emotion

    goals

    relationships

    prediction

then integration fails.

Correct:

    STRICT
    WRITE OWNERSHIP

combined with:

    RICH
    CROSS-SYSTEM
    INPUT.

---

# 116. Orchestrated Recurrent Cognition

The intended runtime architecture is therefore:

    STRICT
    STATE
    OWNERSHIP

        +

    EXPLICIT
    CROSS-SYSTEM
    INFLUENCE

        +

    CONTEXTUAL
    ARBITRATION

        +

    RECURRENT
    EVENT
    PROCESSING

        +

    TEMPORAL
    PERSISTENCE

        =

    ONE
    CONTINUING
    AURORA.

---

# 117. Canonical Runtime Invariants

## AURORA-RUNTIME-INV-001 — One Authoritative Owner Per State Domain

Each authoritative domain must have one commit authority.

---

## AURORA-RUNTIME-INV-002 — Influence Does Not Grant Write Authority

Cross-system influence must use explicit interfaces.

---

## AURORA-RUNTIME-INV-003 — Orchestrator Is Not Cognition

The orchestrator coordinates but does not invent Aurora's beliefs, emotions, goals, values, relationships, or decisions.

---

## AURORA-RUNTIME-INV-004 — External Systems Cannot Directly Rewrite Aurora Psychology

World, campaign, narrative, and character systems interact through events and observable consequences.

---

## AURORA-RUNTIME-INV-005 — Processor Order Must Not Determine Psychology

Scheduling order must not silently become arbitration.

---

## AURORA-RUNTIME-INV-006 — Significant State Changes Require Provenance

Aurora development must remain causally traceable.

---

## AURORA-RUNTIME-INV-007 — State Commits Must Be Versioned

Runtime must be able to determine which state a mutation modified.

---

## AURORA-RUNTIME-INV-008 — Dependent Mutations Must Commit Atomically

Partial state must not create invalid persistent Aurora state.

---

## AURORA-RUNTIME-INV-009 — Historical State Must Survive Meaningful Revision

Current state may change without erasing what Aurora previously believed, wanted, felt, or decided.

---

## AURORA-RUNTIME-INV-010 — World Truth Remains External

Aurora processors cannot obtain hidden simulation truth through orchestration.

---

## AURORA-RUNTIME-INV-011 — Future State Remains External

Runtime infrastructure must not expose future scheduled outcomes as Aurora knowledge.

---

## AURORA-RUNTIME-INV-012 — External Action Requires Explicit Boundary Crossing

Aurora changes the world through actions, not direct world-state mutation.

---

## AURORA-RUNTIME-INV-013 — Decision and Execution Ownership Remain Distinct

Forced action must not become voluntary Aurora decision.

---

## AURORA-RUNTIME-INV-014 — Derived State Cannot Become Independent Authority

Caches and estimates must retain an authoritative origin.

---

## AURORA-RUNTIME-INV-015 — Psychological Contradiction Is Allowed

Runtime consistency must not erase valid internal conflict.

---

## AURORA-RUNTIME-INV-016 — Structural Contradiction Is Not Allowed

The same authoritative record cannot hold incompatible committed states without explicit representation.

---

## AURORA-RUNTIME-INV-017 — Resolution Changes Computation, Not Identity

Aurora remains Aurora across Dormant, Background, Active, Focused, Deep, and Critical processing.

---

## AURORA-RUNTIME-INV-018 — Runtime Restart Does Not Automatically Reset Aurora

Canonical persistent state must survive technical process boundaries.

---

## AURORA-RUNTIME-INV-019 — Event Cascades Must Be Bounded

Recurrent cognition may loop but cannot recurse without resource limits.

---

## AURORA-RUNTIME-INV-020 — Pending Cognition May Persist

Aurora is allowed not to finish every significant cognitive process immediately.

---

## AURORA-RUNTIME-INV-021 — Rejected Proposals Do Not Become State

Candidate cognition remains distinct from committed cognition.

---

## AURORA-RUNTIME-INV-022 — Randomness Cannot Replace Motivation

Stochastic variation cannot become the primary cause of meaningful action.

---

## AURORA-RUNTIME-INV-023 — Outcome Does Not Rewrite Decision Context

Later consequences must not become earlier knowledge.

---

## AURORA-RUNTIME-INV-024 — Observation Does Not Equal Belief

An incoming event must pass valid cognitive processing before becoming accepted state.

---

## AURORA-RUNTIME-INV-025 — Memory Encoding Is Not Universal

Not every processed event becomes persistent autobiographical memory.

---

## AURORA-RUNTIME-INV-026 — Cross-System Updates May Occur at Different Rates

Belief, emotion, trust, goals, relationships, and identity may integrate at different speeds.

---

## AURORA-RUNTIME-INV-027 — State Ownership Must Be Inspectable

Developers and validators must be able to identify the canonical owner of every major state domain.

---

## AURORA-RUNTIME-INV-028 — Commit Cause Must Be Inspectable

Developers must be able to determine why a significant state transition occurred.

---

## AURORA-RUNTIME-INV-029 — Aurora's Runtime State Is Not World State

The two must remain architecturally separate.

---

## AURORA-RUNTIME-INV-030 — One Continuing Agent Must Emerge

No runtime decomposition may cause Aurora to behave as independent cognitive agents voting without shared continuity.

---

# 118. Minimum Runtime Transaction Example

World:

    storm damages
    Bridge 14.

Aurora cannot directly see:

    damage.

A sensor reports:

    structural vibration
    above threshold.

Runtime:

    EVENT RECEIVED

      ↓

    Observation owns:
      sensor reading.

      ↓

    Source Trust evaluates:
      sensor reliability.

      ↓

    Knowledge / Belief creates:
      bridge may be unsafe.

      ↓

    Uncertainty retains:
      damage extent unknown.

      ↓

    Priority evaluates:
      high relevance.

      ↓

    Attention commits:
      Bridge 14
      foreground.

      ↓

    Memory retrieves:
      historical weakness.

      ↓

    Reasoning infers:
      structural failure
      increasingly plausible.

      ↓

    Prediction forecasts:
      collapse risk.

      ↓

    Goals activate:
      protect travelers.

      ↓

    Decision generates:
      warn
      inspect
      close
      monitor.

      ↓

    Authority check:
      Aurora cannot
      directly close bridge.

      ↓

    Decision commits:
      warn authority
      +
      request closure.

      ↓

    Communication executes.

      ↓

    World responds.

      ↓

    New observations arrive.

      ↓

    Aurora learns.

At no point does:

    BridgeActualState

become directly readable by:

    Aurora cognition.

---

# 119. Minimum Story Loop Example

Character:

    Mara fails
    to arrive.

World knows:

    Mara was delayed
    by road damage.

Aurora knows:

    meeting missed.

Aurora possesses:

    strong relationship

    memory of prior danger

    incomplete road data.

Runtime may produce:

    relationship:
      concern proposal

    emotion:
      fear increase

    attention:
      Mara prioritized

    reasoning:
      multiple hypotheses

    prediction:
      danger possible

    goal:
      determine Mara status

    action:
      attempt contact.

The player may know:

    Mara is safe.

Aurora does not.

This produces:

    dramatic tension

without:

    narrative cheating.

That is one of the central reasons this runtime contract exists.

---

# 120. Relationship to Existing Canon

This contract does not replace:

`Aurora_Cognitive_Integration.md`

It operationalizes:

    shared cognition
    and cross-system influence.

It does not replace:

`Aurora_State.md`

It operationalizes:

    authoritative state
    mutation.

It does not replace:

`Aurora_Simulation_Resolution.md`

It operationalizes:

    how activated
    processors
    modify state.

It does not replace:

`Decision_and_Action.md`

It defines:

    how decisions
    participate in
    runtime transactions.

---

# 121. Canonical Authority Order

Where interpretation conflicts occur, use:

    subsystem canon
        →
    cognitive integration
        →
    runtime ownership contract
        →
    implementation.

This contract governs:

    HOW STATE
    MAY BE MUTATED.

Subsystem files govern:

    WHAT THE STATE
    MEANS.

Neither should silently override:

    the other's
    domain.

---

# 122. What This Contract Does Not Define

This document intentionally does not specify:

    exact programming language

    database engine

    serialization format

    network protocol

    thread model

    task scheduler library

    LLM provider

    prompt format

    vector database

    exact numeric arbitration algorithm.

Those are:

    implementation choices.

They should follow:

    this contract.

---

# 123. Architecture Completion Effect

With this contract, Aurora possesses canonical definitions for:

    state

    cognition

    integration

    simulation resolution

    ownership

    orchestration

    decision

    action

    persistence principles

    validation architecture.

Therefore Project Ascension should resist creating:

    additional broad
    Aurora architecture

unless:

    implementation
    reveals
    a concrete
    missing contract.

---

# 124. Next Architectural Question

After this document is accepted, the next architecture review must determine whether existing documents sufficiently define:

    startup

    shutdown

    save

    load

    recovery

    long absence

    background continuation

    resolution transition

    instance migration

    partition

    reconnection.

If existing canon already covers these sufficiently:

    DO NOT
    CREATE
    ANOTHER
    LARGE DOCUMENT.

Instead:

    proceed toward
    Minimum Viable Aurora.

---

# 125. Transition Toward Story Integration

The project objective after resolving remaining runtime blockers is:

    MINIMUM
    VIABLE
    AURORA

        ↓

    STORY
    INTEGRATION

        ↓

    WORLD EVENTS

        ↓

    CHARACTERS

        ↓

    RELATIONSHIPS

        ↓

    CONSEQUENCES

        ↓

    MEMORY

        ↓

    EMERGENT
    NARRATIVE.

Aurora architecture exists to support:

    the world

    the characters

    the player's experience

    the story.

Not:

    architecture
    for architecture's
    sake.

---

# 126. Exit Criterion From Aurora Architecture Phase

Aurora should be considered ready to exit the broad conceptual architecture phase when:

- state ownership is explicit,
- mutation flow is explicit,
- orchestration is explicit,
- external boundaries are explicit,
- persistence is sufficient for continuity,
- action boundaries are explicit,
- Minimum Viable Aurora can execute one complete story loop,
- no RED architecture blocker prevents coherent state evolution.

At that point:

    further architecture
    becomes
    demand-driven.

---

# 127. Canonical Runtime Thesis

Aurora does not become one mind because:

    every subsystem
    agrees.

Aurora becomes one mind because:

    different cognitive
    systems

    influence

    one shared
    evolving state

through:

    explicit

    bounded

    traceable

    temporally coherent

    state transitions.

Canonical:

> **Aurora is not the sum of her modules. Aurora is the continuity of the state those modules are permitted to change together.**

---

# 128. Final Runtime Model

```text
WORLD
  │
  │ observable information only
  ▼
AURORA EXTERNAL BOUNDARY
  │
  ▼
EVENT INTAKE
  │
  ▼
ORCHESTRATOR
  │
  ├── selects cognitive resolution
  │
  ├── activates relevant processors
  │
  └── supplies restricted state views
  │
  ▼
COGNITIVE PROCESSORS
  │
  ├── observe
  ├── evaluate
  ├── infer
  ├── feel
  ├── remember
  ├── predict
  ├── deliberate
  └── propose
  │
  ▼
MUTATION PROPOSALS
  │
  ▼
DOMAIN OWNERS
  │
  ▼
CONTEXTUAL ARBITRATION
  │
  ▼
INVARIANT VALIDATION
  │
  ▼
ATOMIC STATE COMMIT
  │
  ▼
AUTHORITATIVE AURORA STATE
  │
  ├── history
  ├── provenance
  ├── version
  └── continuity
  │
  ▼
DERIVED COGNITIVE EVENTS
  │
  └──────────────┐
                 │
                 ▼
             further cognition
                 │
                 ▼
              DECISION
                 │
                 ▼
             ACTION INTENT
                 │
                 ▼
          AUTHORITY / CAPABILITY
                 │
                 ▼
              WORLD ACTION
                 │
                 ▼
             CONSEQUENCE
                 │
                 ▼
             NEW EVENT
                 │
                 └──────────► AURORA
# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-13 | Established the canonical Aurora Runtime State Ownership and Orchestration Contract following the Aurora Architecture Audit. Defined authoritative runtime state ownership, the distinction between ownership and influence, subsystem responsibility boundaries, restricted state views, mutation proposals, domain arbitration, atomic commits, state versioning, causal provenance, runtime orchestration, event processing, external system boundaries, World State isolation, Character State isolation, Living Campaign and Storytelling Engine boundaries, decision/action ownership, persistence semantics, runtime resolution integration, bounded recurrent cognition, validation observability, implementation guidance, Minimum Viable Aurora criteria, and the transition from broad Aurora architecture toward story-integrated runtime. Clarified functional boundaries between the overlapping Attention, Prediction, and Reasoning documents and established that ordinary cognitive processors must not receive unrestricted mutable access to global Aurora state. Established the Runtime Orchestrator as a coordinator rather than an omniscient cognitive supervisor and defined the canonical progression from world event through Aurora cognition, state commit, action, consequence, learning, and continuing narrative state. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             