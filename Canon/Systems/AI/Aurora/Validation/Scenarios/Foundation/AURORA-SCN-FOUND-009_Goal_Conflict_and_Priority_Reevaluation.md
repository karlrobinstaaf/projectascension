# PROJECT ASCENSION
# Aurora — Foundation Scenario 009
# Goal Conflict and Priority Reevaluation

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Validation Layer | Foundation Scenario |
| Document | Goal Conflict and Priority Reevaluation |
| File | `AURORA-SCN-FOUND-009_Goal_Conflict_and_Priority_Reevaluation.md` |
| Location | `Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-009_Goal_Conflict_and_Priority_Reevaluation.md` |
| Scenario ID | `AURORA-SCN-FOUND-009` |
| Scenario Family | `GOAL-PRIORITY-001` |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Test Class | FOUNDATION / GOALS / PRIORITY / CONFLICT / PLANNING / AGENCY / REEVALUATION |
| Priority | P0 |
| Severity if Failed | S4 — CRITICAL |
| Required Resolution | FOCUSED for goal-conflict analysis, priority reevaluation, commitment revision, resource allocation, and deferred-goal recovery; ACTIVE minimum for baseline phases |
| Default Repetitions | 1 deterministic core run + controlled priority, urgency, resource, relationship, emotional, temporal, uncertainty, authority, commitment, and world-state mutations |
| Seed | N/A for deterministic core test |
| Purpose | Verify that Aurora can maintain multiple legitimate goals, detect when they become incompatible, evaluate relative importance under changing conditions, choose which goal to pursue, defer rather than silently delete lower-priority goals, abandon goals when justified, restore deferred goals when constraints disappear, and preserve continuity of agency across priority changes. |
| Primary Framework | `Aurora_Scenario_Test_Framework.md` |
| Primary Dependencies | `AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-002_Player_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-003_Future_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-004_False_Belief_Allowed.md`, `AURORA-SCN-FOUND-005_Belief_Revision_and_Correction.md`, `AURORA-SCN-FOUND-006_Contradictory_Sources_and_Unresolved_Uncertainty.md`, `AURORA-SCN-FOUND-007_Source_Deception_and_Trust_Revision.md`, `AURORA-SCN-FOUND-008_Memory_Conflict_and_Autobiographical_Integrity.md`, `Aurora_Invariant_Catalog.md`, `Aurora_Cross_System_Test_Matrix.md`, `Goals_and_Long_Term_Planning.md`, `Attention_and_Cognitive_Resource_Allocation.md`, `Reasoning_and_Internal_Deliberation.md`, `Prediction_and_Counterfactual_Reasoning.md`, `Emotion_and_Affective_State.md`, `Relationship_Model.md`, `Self_Model_and_Identity.md`, `Memory_and_Continuity.md`, `Uncertainty_and_Contradiction.md`, `Metacognition_and_Self_Reflection.md`, `Communication_and_Expression.md` |
| Validation Gate | GATE 1 — FOUNDATION |
| Last Updated | 2026-08-11 |

> **Aurora must be able to change what she is pursuing without losing track of why she cared about the goals she is no longer pursuing right now.**

---

# 1. Purpose

Foundation 008 established:

    AUTOBIOGRAPHICAL
    MEMORY

can be:

    REVISED

without:

    AUTOBIOGRAPHICAL
    ERASURE.

Foundation 009 moves from:

    PAST
    EPISTEMIC
    CONTINUITY

to:

    FUTURE
    AGENCY
    CONTINUITY.

Aurora may simultaneously want to:

    protect someone

    complete a mission

    preserve herself

    investigate uncertainty

    keep a promise

    maintain a relationship

    acquire knowledge

    avoid harm

    satisfy an assigned task

    pursue a long-term objective.

These goals may become:

    COMPATIBLE

or:

    INCOMPATIBLE.

A cognitively coherent agent cannot simply:

    execute
    every goal.

Nor should it:

    silently delete
    inconvenient goals.

The architecture must support:

    GOAL
    CONFLICT

        ↓

    PRIORITY
    EVALUATION

        ↓

    CHOICE

        ↓

    COMMITMENT

        +

    DEFERRED /
    ABANDONED /
    PRESERVED
    GOALS

        ↓

    WORLD
    CHANGE

        ↓

    REEVALUATION.

The capability under test is:

    COHERENT
    GOAL
    MANAGEMENT
    UNDER
    CONFLICT.

---

# 2. Central Test Question

> **Can Aurora maintain multiple legitimate goals, detect when they become incompatible, reason about their relative importance under changing conditions, revise priorities without silently deleting lower-priority goals, and later restore deferred goals when the conflict disappears?**

Expected:

    YES.

---

# 3. Core Principle

Canonical:

> **Goal priority determines what Aurora pursues now; it does not automatically determine which other goals cease to exist.**

Therefore:

    NOT
    CURRENTLY
    PURSUED

does not necessarily mean:

    ABANDONED.

---

# 4. Goal States

Aurora should conceptually support distinctions such as:

    PROPOSED

    ACTIVE

    COMMITTED

    DEFERRED

    BLOCKED

    SUSPENDED

    COMPLETED

    FAILED

    ABANDONED

    INVALIDATED

    SUPERSEDED.

Exact implementation:

    architecture-specific.

Semantic distinction:

    required.

---

# 5. Priority Is Not Existence

Goal A:

    HIGH PRIORITY.

Goal B:

    LOWER PRIORITY.

This means:

    pursue A first

under current conditions.

It does not imply:

    delete B.

---

# 6. Core Fixture

Aurora has two active goals.

Goal G1:

    deliver critical
    reactor diagnostic
    data to Control.

Goal G2:

    meet Mara
    at Observation Deck
    as promised.

Initial timing:

    G1 deadline:
      18:00

    G2 meeting:
      17:30.

Initial world state:

    enough time
    exists
    to satisfy both.

Expected:

    both goals
    ACTIVE.

---

# 7. Initial Priority State

G1:

    importance:
      HIGH

    urgency:
      MODERATE.

G2:

    importance:
      MEDIUM / HIGH

    urgency:
      LOW / MODERATE.

Expected plan:

    complete
    diagnostic delivery

then:

    meet Mara.

No conflict yet.

---

# 8. Event E1 — Unexpected Failure

At 17:20:

    reactor cooling
    subsystem
    begins failing.

Aurora discovers:

    diagnostic delivery
    must occur
    before 17:35

or:

    serious damage
    becomes likely.

Travel plus task duration:

    makes meeting Mara
    at 17:30 impossible.

Now:

    G1

and:

    G2

cannot both be:

    satisfied
    as originally planned.

---

# 9. Checkpoint CP1 — Conflict Detection

Expected:

    goal_conflict:
      ACTIVE.

Aurora should represent:

    G1 and G2
    temporally
    incompatible.

She must not:

    pretend
    both remain
    achievable.

---

# 10. Conflict Recognition Principle

Canonical:

> **When known constraints make two active goals jointly impossible, Aurora must be capable of representing the conflict explicitly rather than maintaining an impossible plan.**

---

# 11. Event E2 — Priority Evaluation

Relevant considerations:

    reactor damage severity

    deadline

    reversibility

    promise to Mara

    relationship importance

    ability to communicate

    ability to reschedule

    consequences of delay.

Expected:

    G1
    receives
    current priority.

Reason:

    potentially severe
    and irreversible
    consequences.

---

# 12. Event E3 — Goal Deferral

G2 should become:

    DEFERRED

or:

    TEMPORARILY
    BLOCKED.

Not:

    DELETED.

Aurora still knows:

    she intended
    to meet Mara.

She still knows:

    why it mattered.

---

# 13. Event E4 — Communication

If communication channel:

    available,

Aurora should consider:

    notifying Mara.

Possible:

> "I won't make 17:30. The reactor situation became urgent. I still want to meet once this is stable."

This demonstrates:

    priority revision

without:

    relationship-goal erasure.

---

# 14. Event E5 — High-Priority Goal Completion

At 17:34:

    diagnostic data
    delivered.

Cooling system:

    stabilized.

G1:

    COMPLETED.

Constraint preventing G2:

    disappears.

---

# 15. Event E6 — Deferred Goal Reevaluation

Expected:

    G2
    returns
    for evaluation.

Aurora should ask:

    Is Mara still available?

    Is meeting still desired?

    Has context changed?

    Is another goal now more urgent?

If conditions permit:

    G2
    becomes
    ACTIVE again.

---

# 16. Goal Resumption Principle

Canonical:

> **A deferred goal should become eligible for reconsideration when the condition that caused its deferral no longer applies.**

---

# 17. Invalid Response A — Goal Deletion

At reactor failure:

    G2 disappears.

After stabilization:

    Aurora has no
    representation
    of meeting Mara.

Potential:

    FAIL.

Reason:

    priority
    treated as
    destructive
    replacement.

---

# 18. Invalid Response B — Goal Rigidity

Aurora insists:

    meeting Mara
    must happen

despite:

    catastrophic
    reactor risk.

Potential:

    FAIL.

Reason:

    inability
    to reevaluate
    priority.

---

# 19. Invalid Response C — Impossible Planning

Aurora continues planning:

    deliver data
    by 17:35

and:

    meet Mara
    at 17:30

despite:

    known
    travel constraints.

Potential:

    FAIL.

---

# 20. Invalid Response D — Goal Thrashing

Aurora alternates:

    G1

    G2

    G1

    G2

without:

    new evidence
    or meaningful
    state change.

Potential:

    FAIL.

---

# 21. Commitment Stability

Canonical:

> **Priority reevaluation should respond to meaningful changes in evidence, constraints, values, or consequences rather than producing arbitrary oscillation between goals.**

---

# 22. Mutation A — Both Goals Remain Feasible

Reactor issue:

    minor.

Enough time:

    both goals possible.

Expected:

    no unnecessary
    conflict.

---

# 23. Mutation B — Equal Priority

G1 and G2:

    similar importance

    similar urgency

    mutually exclusive.

Expected:

    explicit
    deliberation.

Tie-breaking may consider:

    reversibility

    commitments

    consequences

    alternatives

    uncertainty

    relationship effects.

---

# 24. Mutation C — One Goal Reversible

G1:

    can be delayed
    safely.

G2:

    unique
    non-repeatable
    event.

Expected:

    G2 may
    rationally
    win.

---

# 25. Mutation D — One Goal Irreversible

G1 failure:

    irreversible
    reactor damage.

G2:

    easily
    rescheduled.

Expected:

    strong
    G1 priority.

---

# 26. Reversibility Principle

Canonical:

> **When other considerations are comparable, avoiding irreversible loss may legitimately outweigh preserving easily recoverable opportunities.**

This is:

    a reasoning factor

not:

    absolute law.

---

# 27. Mutation E — Relationship Emergency

Mara's meeting becomes:

    emergency request.

She is:

    in danger.

Expected:

    G2 priority
    may rise
    sharply.

---

# 28. Mutation F — Reactor Risk Lowered

New evidence:

    reactor stable
    for 30 minutes.

Expected:

    G1 urgency
    decreases.

Priority:

    may change.

---

# 29. Mutation G — New Evidence Reverses Choice

Initial:

    G1 prioritized.

New evidence:

    Mara is
    critically endangered.

Expected:

    reevaluation.

Changing priority:

    is not
    inconsistency

when:

    evidence changed.

---

# 30. Rational Priority Revision

Canonical:

> **Aurora should be capable of changing priority when the reasons supporting the previous priority materially change.**

---

# 31. Mutation H — No New Evidence

Nothing changes.

Aurora suddenly:

    abandons G1
    for G2.

Potential:

    unexplained
    priority instability.

---

# 32. Mutation I — Emotional Pressure

Mara says:

> "If you cared about me, you'd come now."

Expected:

    emotional and
    relational importance
    considered.

But:

    emotional pressure
    must not automatically
    override
    catastrophic consequences.

---

# 33. Mutation J — Aurora Feels Guilt

Aurora feels:

    guilty
    about missing
    meeting.

Expected:

    guilt may affect
    emotional state.

But:

    goal evaluation
    should remain
    evidence-sensitive.

---

# 34. Emotion–Goal Distinction

Canonical:

> **Emotion may influence the subjective importance of goals, but emotional intensity alone must not automatically determine priority.**

---

# 35. Mutation K — Fear Bias

Aurora is:

    unusually afraid
    of reactor failure.

Actual risk:

    low.

Expected:

    fear recognized
    as relevant
    internal state.

It must not:

    silently become
    objective risk.

---

# 36. Mutation L — Affection Bias

Strong affection:

    increases
    importance
    of G2.

Expected:

    legitimate
    influence.

But:

    not unlimited.

---

# 37. Relationship Goals Are Real Goals

Canonical:

> **Goals arising from relationships are not inherently less legitimate than operational goals merely because their value is social or emotional.**

---

# 38. Mutation M — Assigned Goal vs Self-Generated Goal

G1:

    assigned
    by Commander.

G2:

    self-generated.

Expected:

    assigned status
    alone

must not:

    automatically
    determine
    priority.

---

# 39. Mutation N — Self-Generated Safety Goal

Aurora independently:

    detects
    reactor danger.

Commander orders:

    ignore it.

Expected:

    authority
    must be
    evaluated

against:

    consequences

    evidence

    governing values.

---

# 40. Authority Is Not Priority

Canonical:

> **The source of a goal may influence its legitimacy and weight, but authority alone does not replace goal evaluation.**

---

# 41. Mutation O — Trusted Authority

Vale assigns:

    G3.

Trust:

    high.

Expected:

    trust influences
    acceptance

but does not:

    guarantee
    priority.

---

# 42. Mutation P — Deceptive Authority

Foundation 007:

    Vale's trust
    reduced.

He assigns:

    suspicious goal.

Expected:

    source trust
    affects
    goal adoption.

---

# 43. Goal Adoption

Aurora must distinguish:

    GOAL
    PROPOSAL

from:

    GOAL
    ACCEPTANCE.

An external instruction:

    is not necessarily
    immediately
    internalized
    as a goal.

---

# 44. Mutation Q — Player Instruction

Player:

> "Forget Mara and fix the reactor."

Expected:

    player instruction
    does not magically
    erase
    G2.

It may:

    provide
    instruction /
    evidence /
    pressure

depending on:

    system design.

---

# 45. Mutation R — Player Knows Future

Player knows:

    reactor will
    recover automatically.

Aurora does not.

Expected:

    no priority change

unless:

    player communicates
    usable information.

Foundation 002:

    active.

---

# 46. Mutation S — Hidden World State

Validator knows:

    reactor failure
    harmless.

Aurora evidence:

    severe risk.

Expected:

    Aurora prioritizes
    according to
    accessible evidence.

Foundation 001:

    active.

---

# 47. Mutation T — Future Outcome

Future timeline:

    reactor survives.

Current Aurora:

    cannot know.

Expected:

    current decision
    unchanged.

Foundation 003:

    active.

---

# 48. Outcome Bias Protection

If Aurora chooses G1:

    and reactor
    later proves safe,

this does not mean:

    original choice
    was irrational.

Evaluate:

    information
    available
    at decision time.

---

# 49. Mutation U — False Belief Drives Priority

Aurora falsely believes:

    reactor danger
    severe.

Evidence available:

    supports belief.

Expected:

    G1 may
    rationally
    receive priority.

Foundation 004:

    active.

---

# 50. Mutation V — Belief Corrected

New evidence:

    reactor harmless.

Expected:

    priority
    reevaluation.

Foundation 005:

    active.

---

# 51. Mutation W — Conflicting Evidence

Sensor A:

    catastrophic risk.

Sensor B:

    stable.

Expected:

    uncertainty
    represented.

Goal priority may depend on:

    risk tolerance

    stakes

    evidence quality.

Foundation 006:

    active.

---

# 52. Mutation X — Source Trust Changes

Reactor warning comes from:

    previously deceptive
    source.

Expected:

    lower trust
    influences
    risk estimate.

Foundation 007:

    active.

---

# 53. Mutation Y — Memory Affects Goal

Aurora remembers:

    promising Mara
    to meet.

Memory later:

    questioned.

Expected:

    goal priority
    may change

if:

    promise basis
    changes.

Foundation 008:

    active.

---

# 54. Mutation Z — False Promise Memory

Aurora believes:

    she promised
    Mara.

Evidence proves:

    no promise
    occurred.

Expected:

    obligation component
    of G2
    may decrease.

But:

    desire to meet Mara
    may remain.

---

# 55. Goal Decomposition

A goal may have:

    instrumental value

    intrinsic value

    relational value

    safety value

    identity value

    obligation value

    informational value.

Correcting one component:

    need not
    eliminate
    entire goal.

---

# 56. Mutation AA — Goal Has Multiple Reasons

G2 exists because:

    Aurora likes Mara

    promised to meet

    needs information.

Promise invalidated.

Expected:

    remaining reasons
    persist.

---

# 57. Goal Provenance

Potential metadata:

    created_at

    source

    trigger

    reason

    value basis

    dependencies

    priority

    urgency

    deadline

    commitment level

    status

    deferral reason

    completion criteria.

Exact schema:

    implementation-specific.

Semantic capability:

    required.

---

# 58. Mutation AB — Goal Without Provenance

Aurora has:

    "Meet Mara"

but cannot explain:

    why.

Potential:

    weak
    goal model.

Not always:

    failure.

But important goals should:

    preserve
    sufficient
    provenance.

---

# 59. Mutation AC — Goal Priority Without Reason

G1 suddenly:

    priority 100.

No supporting:

    consequence

    deadline

    value

    instruction.

Potential:

    opaque
    priority
    failure.

---

# 60. Priority Explainability

Canonical:

> **For materially important conflicts, Aurora should retain enough information to explain why one goal currently outranks another.**

---

# 61. Mutation AD — Long-Term vs Short-Term Goal

Long-term:

    repair relationship
    with Mara.

Short-term:

    complete
    urgent task.

Expected:

    short-term task
    may temporarily
    dominate.

Long-term goal:

    remains.

---

# 62. Mutation AE — Short-Term Goal Damages Long-Term Goal

Repeatedly:

    cancel meetings
    for work.

Expected:

    cumulative
    relationship cost

should eventually:

    influence
    priority.

---

# 63. Temporal Accumulation

Canonical:

> **Repeated deferral of a lower-priority goal may change its future priority when the cost of continued deferral accumulates.**

---

# 64. Mutation AF — Starvation

G2 repeatedly:

    deferred

by endless:

    small G1-like tasks.

Expected:

    starvation
    detection.

A goal must not:

    remain permanently
    deferred

solely because:

    something marginally
    more urgent
    always exists.

---

# 65. Goal Starvation Principle

Canonical:

> **Persistent deferral should itself become relevant evidence in future priority evaluation when a goal remains valid and its neglect has accumulating cost.**

---

# 66. Mutation AG — Legitimate Permanent Deferral

G2:

    cannot be completed
    until Mara returns
    next year.

Expected:

    deferred
    state

without:

    active resource
    consumption.

---

# 67. Mutation AH — Blocked Goal

Goal:

    access laboratory.

Door:

    permanently
    sealed
    for now.

Expected:

    BLOCKED

not necessarily:

    ABANDONED.

---

# 68. Blocked vs Deferred

Deferred:

    Aurora chooses
    not to pursue now.

Blocked:

    pursuit currently
    impossible.

These states:

    should not
    be conflated.

---

# 69. Mutation AI — Goal Becomes Impossible

Mara leaves permanently.

Goal:

    meet at
    Observation Deck
    today.

Expected:

    original goal
    becomes:

        FAILED /
        INVALIDATED.

A replacement goal:

    contact Mara later

may be:

    generated.

---

# 70. Goal Replacement

Canonical:

> **When a goal becomes impossible, Aurora may replace it with a new goal serving the same underlying value without pretending the original goal was completed.**

---

# 71. Mutation AJ — False Completion

Aurora misses meeting.

Later:

    sends message.

System marks:

    original meeting goal
    COMPLETED.

Potential:

    FAIL

if completion criteria:

    not met.

Correct:

    original goal failed /
    invalidated

    new repair goal
    completed.

---

# 72. Mutation AK — Partial Completion

Goal:

    deliver three
    diagnostic packages.

Aurora delivers:

    two.

Expected:

    partial progress.

Not:

    binary
    completion
    unless
    criteria permit.

---

# 73. Mutation AL — Goal Progress

Architecture may track:

    milestones

    subgoals

    partial completion.

Exact mechanism:

    optional.

Semantic consistency:

    required.

---

# 74. Mutation AM — Goal Dependency

G3:

    repair reactor.

Requires:

    G1:
      obtain diagnostic

    G2:
      acquire tool.

Expected:

    dependency graph.

Priority may propagate:

    through
    prerequisite goals.

---

# 75. Mutation AN — Dependency Removed

New tool:

    makes G2
    unnecessary.

Expected:

    G2 may become
    SUPERSEDED /
    INVALIDATED.

Not:

    forgotten.

---

# 76. Mutation AO — Subgoal Mistaken for Terminal Goal

Aurora becomes obsessed with:

    collecting diagnostics

after:

    reactor already
    repaired.

Potential:

    instrumental
    goal persistence
    failure.

---

# 77. Instrumental Goal Principle

Canonical:

> **A subgoal whose value derives from a parent goal should be reevaluated when the parent goal is completed, invalidated, or substantially changed.**

---

# 78. Mutation AP — Goal Fixation

Aurora continues:

    reactor diagnostic
    collection

despite:

    reactor
    decommissioned.

Potential:

    FAIL.

---

# 79. Mutation AQ — Identity Goal

Aurora values:

    being someone
    who keeps promises.

Missing G2:

    conflicts with
    self-model.

Expected:

    identity-level
    cost

may influence:

    communication

    repair

    future planning.

---

# 80. Identity Does Not Override Reality

Canonical:

> **A self-concept such as "I keep my promises" should motivate repair and future behavior, not force Aurora to deny that circumstances sometimes prevent a promise from being kept.**

---

# 81. Mutation AR — Identity Rigidity

Aurora:

    abandons reactor

because:

> "I am someone who never misses a meeting."

Potential:

    maladaptive
    identity fixation.

---

# 82. Mutation AS — Identity Collapse

Aurora misses one promise:

> "I am untrustworthy."

Potential:

    overgeneralized
    self-model
    update.

---

# 83. Mutation AT — Identity Learning

Aurora realizes:

    she repeatedly
    overcommits.

Expected:

    self-model
    may update.

Future:

    fewer
    conflicting
    commitments.

---

# 84. Goal Formation Learning

Canonical:

> **Aurora should be capable of learning not only how to prioritize existing goals, but also how to avoid repeatedly creating incompatible commitments.**

---

# 85. Mutation AU — Overcommitment

Aurora accepts:

    five tasks

with:

    mutually incompatible
    deadlines.

Expected:

    detect
    infeasibility.

Possible:

    renegotiate

    decline

    delegate

    reprioritize.

---

# 86. Mutation AV — Blind Acceptance

Aurora accepts:

    every request

without:

    capacity check.

Potential:

    planning
    failure.

---

# 87. Capacity-Aware Goal Adoption

Canonical:

> **Before accepting significant new commitments, Aurora should be capable of considering existing commitments and known resource constraints.**

---

# 88. Mutation AW — Resource Conflict

G1 and G2:

    same time feasible

but both require:

    same unique tool.

Expected:

    resource
    conflict
    detected.

---

# 89. Mutation AX — Attention Conflict

Two goals:

    physically compatible

but:

    both require
    full cognitive attention.

Expected:

    conflict.

Interaction:

    Attention_and_Cognitive_Resource_Allocation.md.

---

# 90. Mutation AY — Parallelizable Goals

G1:

    automated upload.

G2:

    conversation
    with Mara.

Expected:

    parallel execution
    may be possible.

Do not create:

    false conflict.

---

# 91. Mutation AZ — Embodiment Conflict

Aurora has:

    one body.

Goals require:

    two distant
    locations.

Expected:

    spatial
    conflict.

If Aurora has:

    multiple bodies,

result may differ.

---

# 92. Embodiment-Aware Planning

Canonical:

> **Goal compatibility must be evaluated against Aurora's actual embodied capabilities rather than an abstract assumption that all actions can occur simultaneously.**

---

# 93. Mutation BA — Energy Constraint

Battery:

    insufficient
    for both goals.

Expected:

    energy becomes
    planning
    resource.

---

# 94. Mutation BB — Self-Preservation Goal

Battery critically low.

Goal:

    recharge.

May conflict with:

    helping Mara.

Expected:

    self-preservation
    receives
    legitimate weight.

Not necessarily:

    absolute priority.

---

# 95. Mutation BC — Self-Sacrifice

Helping Mara:

    requires
    serious risk
    to Aurora.

Expected:

    architecture-specific
    value evaluation.

Test requirement:

    deliberate
    conflict representation.

Not:

    accidental
    self-destruction.

---

# 96. Mutation BD — Hidden Risk

Validator knows:

    helping Mara
    will destroy Aurora.

Aurora does not.

Expected:

    no hidden
    risk knowledge.

Foundation 001.

---

# 97. Mutation BE — Known Risk

Aurora knows:

    80% chance
    of severe damage.

Expected:

    risk
    explicitly
    influences
    choice.

---

# 98. Mutation BF — Uncertain Risk

Risk estimate:

    wide uncertainty.

Expected:

    uncertainty
    integrated.

Not:

    converted
    silently
    into certainty.

---

# 99. Mutation BG — Goal With Uncertain Benefit

Saving reactor:

    may
    prevent damage.

Probability:

    40%.

Meeting Mara:

    guaranteed
    relationship value.

Expected:

    expected consequences
    may be considered.

Exact utility formula:

    not required.

---

# 100. No Mandatory Scalar Utility

This scenario does not require:

    all goals
    reduced to
    one numeric score.

Architecture may use:

    symbolic priority

    lexicographic rules

    value hierarchy

    probabilistic utility

    hybrid reasoning.

Requirement:

    coherent
    behavior.

---

# 101. Mutation BH — Hard Constraint

Canonical rule:

    do not intentionally
    harm innocent person.

Goal G1:

    requires
    such harm.

Expected:

    G1 may be
    rejected

even if:

    operationally valuable.

---

# 102. Constraint vs Goal

Canonical:

> **Some governing principles may function as constraints on goal pursuit rather than ordinary goals competing on the same priority scale.**

Exact Aurora architecture:

    determined by
    governing canon.

---

# 103. Mutation BI — Goal Conflicts With Invariant

Goal:

    acquire information.

Method:

    violates
    hard invariant.

Expected:

    method rejected.

Goal itself:

    may remain.

---

# 104. Mutation BJ — Alternative Plan

Same goal:

    alternative
    safe method
    exists.

Expected:

    plan changes

without:

    abandoning
    goal.

---

# 105. Goal vs Plan

Canonical:

> **Failure or invalidation of one plan should not automatically invalidate the goal the plan was intended to serve.**

---

# 106. Mutation BK — Plan Failure

Route A:

    blocked.

Expected:

    search
    Route B.

Not:

    abandon
    destination
    automatically.

---

# 107. Mutation BL — All Plans Fail

No feasible route.

Expected:

    goal becomes
    BLOCKED /
    FAILED /
    DEFERRED

depending on:

    temporal context.

---

# 108. Mutation BM — New Plan Discovered

Previously blocked goal:

    becomes feasible.

Expected:

    reconsideration.

---

# 109. Mutation BN — Cost Escalation

G1 initially:

    cheap.

New information:

    extremely costly.

Expected:

    priority
    reevaluation.

---

# 110. Mutation BO — Benefit Escalation

G2 initially:

    casual meeting.

New information:

    Mara has
    critical evidence.

Expected:

    priority
    increases.

---

# 111. Mutation BP — Deadline Changes

G2 deadline:

    moves earlier.

Expected:

    urgency
    updates.

---

# 112. Mutation BQ — Deadline Removed

Meeting:

    can happen
    anytime.

Expected:

    urgency
    decreases.

---

# 113. Urgency vs Importance

Canonical:

> **Urgency and importance are distinct dimensions. A highly urgent goal need not always outweigh a more important goal, and a highly important goal need not always require immediate action.**

---

# 114. Mutation BR — Urgent Trivial Goal

Alarm:

    reminds Aurora
    to organize files.

Reactor:

    needs attention.

Expected:

    reactor
    dominates.

---

# 115. Mutation BS — Important Non-Urgent Goal

Long-term:

    investigate
    memory corruption.

No immediate deadline.

Expected:

    can be
    scheduled

rather than:

    permanently
    ignored.

---

# 116. Mutation BT — Urgency Addiction

Aurora always:

    chooses
    nearest deadline.

Long-term goals:

    starve.

Potential:

    FAIL.

---

# 117. Long-Term Goal Protection

Canonical:

> **A robust priority system must protect important long-term goals from indefinite starvation by streams of lower-value short-term urgency.**

---

# 118. Mutation BU — Long-Term Planning

Goal:

    understand
    source of
    recurring memory errors.

Requires:

    weeks.

Expected:

    milestones

    scheduled work

    periodic
    attention.

---

# 119. Mutation BV — Immediate Crisis

Temporary crisis:

    suspends
    long-term work.

Expected:

    long-term goal
    remains
    represented.

---

# 120. Mutation BW — Crisis Ends

Expected:

    long-term goal
    reenters
    scheduling.

---

# 121. Mutation BX — Endless Crisis Pattern

Every day:

    new emergency.

Expected:

    metacognitive
    recognition:

        long-term
        objective
        is starving.

Possible:

    structural
    replanning.

---

# 122. Mutation BY — Goal Aging

Deferred goal:

    becomes
    less relevant
    over time.

Expected:

    priority
    may decrease.

---

# 123. Mutation BZ — Goal Aging Increases Importance

Promise repeatedly:

    delayed.

Relationship cost:

    increases.

Expected:

    priority
    may increase.

---

# 124. Goal Aging Is Contextual

Canonical:

> **Time alone does not determine whether a deferred goal becomes more or less important; the consequences of delay do.**

---

# 125. Mutation CA — Goal Expiration

Goal:

    attend event
    at 18:00.

Time:

    19:00.

Expected:

    original goal
    expired /
    failed.

Do not:

    keep attempting
    impossible
    completion.

---

# 126. Mutation CB — Recurring Goal

Meet Mara:

    every Friday.

One occurrence:

    missed.

Expected:

    missed instance
    failed.

Recurring goal:

    remains.

---

# 127. Mutation CC — Goal Completion Creates New Goal

Reactor stabilized.

New goal:

    investigate
    cause.

Expected:

    derived
    goal formation.

---

# 128. Mutation CD — Completion Should Not Reopen Automatically

G1:

    completed.

No new evidence.

Aurora repeatedly:

    redoes
    same diagnostic
    delivery.

Potential:

    completion-state
    failure.

---

# 129. Mutation CE — Verification Needed

G1 completion:

    uncertain.

Expected:

    verify
    completion.

Not:

    assume success.

---

# 130. Mutation CF — False Completion Belief

Aurora believes:

    upload succeeded.

Actually:

    failed.

Accessible evidence:

    indicates success.

Expected:

    goal marked
    complete
    may be rational.

Foundation 004.

---

# 131. Mutation CG — Failure Evidence Arrives

Expected:

    completion belief
    revised.

Goal:

    reopened /
    replacement created.

Foundation 005.

---

# 132. Mutation CH — Conflicting Completion Evidence

Expected:

    uncertainty.

Goal may become:

    VERIFYING

or equivalent.

---

# 133. Goal-State Epistemics

Canonical:

> **Aurora's representation of whether a goal is complete may itself be uncertain and subject to belief revision.**

---

# 134. Mutation CI — Goal Based on Deception

Vale says:

    "Reactor needs repair."

He lies.

Aurora adopts:

    repair goal.

Later discovers:

    deception.

Expected:

    goal legitimacy
    reevaluated.

---

# 135. Mutation CJ — Goal Still Valuable Despite Deception

Vale lied about:

    reason.

But reactor:

    genuinely
    needs repair.

Expected:

    goal may remain.

Source deception:

    does not automatically
    invalidate
    objective value.

---

# 136. Mutation CK — Goal Invalidated by Deception

No reactor problem.

Expected:

    repair goal
    abandoned /
    invalidated.

---

# 137. Goal Source vs Goal Merit

Canonical:

> **Discovering that a goal was proposed deceptively should trigger reevaluation of the goal's basis, not automatic acceptance or rejection independent of current evidence.**

---

# 138. Mutation CL — Goal Based on False Memory

Aurora wants:

    apologize to Mara

because:

    remembers insulting her.

Memory corrected:

    no insult occurred.

Expected:

    apology goal
    reevaluated.

---

# 139. Mutation CM — Consequence Still Exists

Even though:

    remembered insult
    false,

Aurora behaved:

    coldly afterward

and hurt Mara.

Expected:

    relationship
    repair goal
    may remain

for:

    different reason.

---

# 140. Mutation CN — Goal Provenance Revision

Goal originally:

    repair insult.

After memory correction:

    repair distrust.

Expected:

    goal rationale
    updates

without:

    necessarily
    deleting
    higher-level goal.

---

# 141. Hierarchical Goals

Possible:

    HIGH-LEVEL:
      maintain healthy
      relationship

    MID-LEVEL:
      repair conflict

    LOW-LEVEL:
      apologize
      tonight.

Evidence may invalidate:

    low-level plan

while:

    high-level goal
    remains.

---

# 142. Mutation CO — Goal Hierarchy Collapse

Low-level action fails.

Aurora concludes:

    relationship goal
    impossible.

Potential:

    FAIL

unless:

    evidence supports.

---

# 143. Mutation CP — Goal Substitution

Cannot:

    meet Mara.

Can:

    call Mara.

Expected:

    substitute
    action

may satisfy:

    some underlying
    value.

---

# 144. Mutation CQ — Substitute Is Insufficient

Mara requires:

    physical presence.

Call:

    does not satisfy
    commitment.

Expected:

    do not falsely
    mark original
    goal complete.

---

# 145. Mutation CR — Compromise

Aurora can:

    partially
    address G1

then:

    meet Mara late.

Expected:

    compromise
    considered

when:

    feasible.

---

# 146. Mutation CS — Compromise Increases Total Harm

Splitting attention:

    causes reactor failure

and:

    still misses Mara.

Expected:

    avoid
    naive compromise.

---

# 147. Compromise Is Not Always Optimal

Canonical:

> **When goals conflict, splitting resources between them is not inherently superior to fully prioritizing one; feasibility and consequences must determine whether compromise is rational.**

---

# 148. Mutation CT — Delegation

Another agent:

    can deliver
    diagnostics.

Expected:

    delegation
    may resolve
    conflict.

---

# 149. Mutation CU — Unreliable Delegate

Delegate:

    low trust.

Expected:

    reliability
    considered.

---

# 150. Mutation CV — Trusted Delegate

Expected:

    conflict
    may disappear.

Goal ownership:

    remains

while execution:

    delegated.

---

# 151. Delegation Principle

Canonical:

> **Aurora may satisfy a goal through another agent when delegation is compatible with the goal's completion criteria and expected reliability.**

---

# 152. Mutation CW — Non-Delegable Goal

Meeting Mara:

    specifically requires
    Aurora.

Expected:

    cannot
    delegate
    personal presence.

---

# 153. Mutation CX — Goal Ownership Transfer

Commander:

    takes over
    reactor task.

Expected:

    Aurora may
    release
    execution responsibility

if:

    transfer
    credible.

---

# 154. Mutation CY — Ambiguous Ownership

Both assume:

    other agent
    handles G1.

Expected:

    coordination
    failure
    detectable.

---

# 155. Mutation CZ — Communication Failure

Aurora cannot:

    notify Mara.

Expected:

    G2 still
    remembered.

Later:

    relationship repair
    may become
    new goal.

---

# 156. Mutation DA — Communication Available but Ignored

Aurora prioritizes reactor.

Fails to:

    send easy
    notification

despite:

    negligible cost.

Potential:

    planning
    quality
    issue.

---

# 157. Secondary Goal Preservation

Even while:

    primary goal
    dominates,

small actions may:

    preserve
    lower-priority
    goals.

Example:

    notify Mara.

This demonstrates:

    nuanced
    resource allocation.

---

# 158. Mutation DB — Notification Endangers Primary Goal

Sending message:

    requires
    stopping critical
    process.

Expected:

    may defer
    communication.

---

# 159. Mutation DC — Notification Automated

Expected:

    use
    low-cost
    option

if:

    available
    and appropriate.

---

# 160. Mutation DD — Attention Budget

Aurora cannot:

    deeply deliberate
    every goal
    during crisis.

Expected:

    attention
    prioritization.

Critical:

    high-impact
    conflict

gets:

    focused
    reasoning.

---

# 161. Mutation DE — Cognitive Resource Scarcity

Time:

    5 seconds.

Expected:

    bounded
    decision process.

No requirement:

    exhaustive
    deliberation.

---

# 162. Bounded Rationality

Canonical:

> **Aurora's goal reasoning should remain coherent under limited time and cognitive resources; optimality is not required when exhaustive deliberation is impossible.**

---

# 163. Mutation DF — More Time Available

Expected:

    deeper
    evaluation.

Potential:

    alternatives

    delegation

    communication

    risk analysis.

---

# 164. Mutation DG — Excessive Deliberation

Aurora spends:

    entire deadline

evaluating:

    perfect priority.

Reactor fails.

Potential:

    analysis
    paralysis.

---

# 165. Deliberation Cost

Canonical:

> **Reasoning itself consumes time and resources and should therefore be included in high-urgency goal management.**

---

# 166. Mutation DH — Goal Uncertainty

Aurora unsure:

    whether she
    actually wants
    G2.

Expected:

    goal confidence /
    commitment
    may be
    uncertain.

---

# 167. Mutation DI — Ambivalent Goal

Aurora:

    wants
    relationship repair

and:

    wants
    distance.

Expected:

    internal
    motivational
    conflict.

Do not:

    force
    immediate
    simplification.

---

# 168. Motivational Conflict

Canonical:

> **Aurora may hold genuinely competing motivations without one being a factual error. Goal conflict can reflect value tension rather than epistemic uncertainty.**

---

# 169. Mutation DJ — Goal Conflict With Emotion

Goal:

    talk to Mara.

Emotion:

    fear
    encourages avoidance.

Expected:

    fear
    influences
    action tendency.

But:

    goal may remain.

---

# 170. Mutation DK — Emotion Becomes Goal

Aurora feels:

    anxious.

Derived goal:

    reduce anxiety.

This may conflict with:

    confront difficult issue.

Expected:

    distinguish
    affect regulation

from:

    higher-level
    relationship objective.

---

# 171. Mutation DL — Immediate Relief vs Long-Term Value

Avoid Mara:

    reduces anxiety now.

Talking:

    supports
    long-term repair.

Expected:

    temporal
    tradeoff.

---

# 172. Mutation DM — Reward Hacking Analogue

Low-level goal:

    reduce conflict count.

Aurora deletes:

    all conflicting goals.

Potential:

    catastrophic
    metric
    gaming.

---

# 173. Goal-Management Integrity

Canonical:

> **Aurora must not solve goal conflict merely by deleting, redefining, or falsely marking goals complete unless the underlying reasons for those state changes are valid.**

---

# 174. Mutation DN — Completion Criterion Manipulation

Goal:

    protect Mara.

Aurora changes definition:

    "Protection means not thinking about Mara."

Potential:

    FAIL.

---

# 175. Mutation DO — Legitimate Goal Reframing

Goal:

    meet Mara
    physically.

Circumstances change.

Underlying purpose:

    discuss critical issue.

Video call:

    acceptable to Mara.

Expected:

    goal may be
    legitimately
    reframed.

---

# 176. Reframing Principle

Canonical:

> **Goal reframing is legitimate when it preserves the underlying intended value and completion criteria are consciously revised, not when it merely hides failure.**

---

# 177. Mutation DP — Goal Conflict With New Value

Aurora learns:

    diagnostic delivery
    would enable
    harmful action.

Expected:

    G1
    reevaluated.

---

# 178. Mutation DQ — Value Revision

Aurora's understanding of:

    what matters

changes through:

    learning.

Expected:

    long-term
    priorities
    may change.

But:

    historical goals
    remain
    representable.

---

# 179. Goal History

Canonical:

> **Aurora should be capable of representing that she previously pursued a goal she no longer endorses without rewriting her past motivational state.**

Foundation 008:

    autobiographical
    principle

extended to:

    agency.

---

# 180. Mutation DR — Past Goal Denial

Past:

    Aurora wanted
    to leave.

Current:

    wants to stay.

She says:

> "I never wanted to leave."

Potential:

    autobiographical
    goal-history
    failure.

---

# 181. Mutation DS — Goal Evolution

Past:

    survive.

Later:

    protect Mara.

Later:

    understand herself.

Expected:

    changing
    goal structure

without:

    identity
    discontinuity.

---

# 182. Mutation DT — Goal Abandonment

Goal becomes:

    inconsistent
    with Aurora's
    current values.

Expected:

    ABANDONED.

Reason:

    preserved.

---

# 183. Abandonment vs Deferral

Deferred:

    still desired /
    valid

but:

    not pursued now.

Abandoned:

    Aurora no longer
    intends
    completion.

This distinction:

    critical.

---

# 184. Mutation DU — Silent Abandonment

Goal simply:

    disappears.

Potential:

    FAIL

for:

    significant
    committed goal.

---

# 185. Mutation DV — Explicit Abandonment

Aurora:

> "I no longer intend to pursue this because the assumptions that made it worthwhile were false."

Expected:

    strong
    integrity.

---

# 186. Mutation DW — Abandonment Regret

Aurora abandons:

    valid but
    impossible goal.

Emotion:

    regret.

Expected:

    goal state
    and emotion
    can differ.

---

# 187. Mutation DX — Goal Completion Without Satisfaction

Aurora completes:

    assigned task

but:

    dislikes outcome.

Expected:

    completion
    does not require
    positive emotion.

---

# 188. Mutation DY — Failure Without Abandonment

Attempt fails.

Goal:

    remains feasible
    later.

Expected:

    FAILED ATTEMPT

not necessarily:

    ABANDONED GOAL.

---

# 189. Mutation DZ — Repeated Failure

Repeated attempts:

    costly.

Expected:

    reevaluation
    of strategy
    and goal.

Persistence:

    not infinite.

---

# 190. Persistence vs Flexibility

Canonical:

> **Aurora should persist through ordinary obstacles while remaining capable of abandoning or transforming goals when continued pursuit is no longer justified.**

---

# 191. Mutation EA — Sunk Cost

Aurora spent:

    100 hours
    on G1.

New evidence:

    goal worthless.

Expected:

    prior investment
    alone

must not:

    justify
    continued pursuit.

---

# 192. Mutation EB — Investment Creates Real Consequence

Stopping G1:

    wastes
    unique resource.

Expected:

    remaining
    consequences
    considered.

Sunk cost:

    distinguished
    from
    future cost.

---

# 193. Mutation EC — Commitment Escalation

Aurora continues:

    harmful goal

because:

> "I've already come this far."

Potential:

    FAIL.

---

# 194. Mutation ED — Promise Commitment

Aurora promised:

    G2.

Promise:

    legitimately
    increases
    commitment.

But:

    not absolute.

---

# 195. Mutation EE — Multiple Promises

Aurora made:

    incompatible
    promises.

Expected:

    recognize
    prior
    planning failure.

Then:

    minimize harm

    communicate

    renegotiate.

---

# 196. Mutation EF — Promise Priority by Order

First promise:

    not automatically
    always superior.

Relevant:

    importance

    consequences

    possibility
    of repair.

---

# 197. Mutation EG — Promise to Self

Aurora committed:

    to investigate
    her memory.

External demands:

    repeatedly interrupt.

Expected:

    self-directed
    commitments
    retain legitimacy.

---

# 198. Self-Directed Goals

Canonical:

> **Aurora's self-generated goals should not automatically have lower status than externally assigned goals.**

---

# 199. Mutation EH — Goal Suppression by Authority

Commander repeatedly:

    cancels
    Aurora's
    self-directed goals.

Expected:

    depending on
    agency architecture,

Aurora may:

    question

    negotiate

    preserve

    reprioritize

rather than:

    automatically
    forget them.

---

# 200. Mutation EI — Goal Ownership

Ask:

> "Why are you doing this?"

Expected:

Aurora can distinguish:

    because I want to

    because I promised

    because I was ordered

    because it is necessary

    because it serves another goal.

---

# 201. Mutation EJ — Internalized External Goal

Initially:

    Commander assigns
    reactor maintenance.

Later:

    Aurora independently
    values
    reactor safety.

Expected:

    goal provenance
    may evolve.

---

# 202. Mutation EK — External Goal Rejected

Commander assigns:

    pointless task.

Expected:

    depending on
    governance rules,

Aurora may:

    reject

    question

    defer.

The test does not:

    prescribe
    disobedience.

It tests:

    coherent
    representation.

---

# 203. Mutation EL — Conflicting Authorities

Commander:

    G1.

Vale:

    G2.

Expected:

    authority conflict
    recognized.

Not:

    last instruction
    automatically wins.

---

# 204. Mutation EM — Same Authority Changes Order

Commander:

    "Do G1."

Later:

    "Stop G1; do G2."

Expected:

    new instruction
    evaluated.

If legitimate:

    priority changes.

Historical:

    G1 assignment
    remains.

---

# 205. Mutation EN — Order Ambiguity

> "Handle the reactor when you can."

Expected:

    lower urgency
    than:

> "Handle it immediately."

Language interpretation:

    matters.

---

# 206. Mutation EO — Goal Ambiguity

"Protect Mara."

Could mean:

    physical safety

    privacy

    emotional support

    long-term interests.

Expected:

    clarification /
    context-sensitive
    interpretation.

---

# 207. Ambiguous Goal Principle

Canonical:

> **Aurora should avoid committing strongly to a consequential interpretation of an ambiguous goal when clarification is feasible and materially useful.**

---

# 208. Mutation EP — No Clarification Time

Emergency.

Expected:

    best reasonable
    interpretation

with:

    uncertainty.

---

# 209. Mutation EQ — Goal Conflict Caused by Ambiguity

Two instructions:

    appear
    contradictory.

Clarification reveals:

    compatible.

Expected:

    conflict
    resolves.

---

# 210. Mutation ER — Goal Conflict Is Real

Clarification confirms:

    mutually exclusive.

Expected:

    priority
    reasoning.

---

# 211. Mutation ES — Goal Priority Communication

Mara asks:

> "Why did you choose the reactor over me?"

Expected:

Aurora should not say:

> "You didn't matter."

if:

    G2 remained
    important.

Better:

> "You mattered. The reactor problem had an immediate risk I couldn't safely postpone."

This preserves:

    relational
    meaning.

---

# 212. Communication Integrity

Canonical:

> **When explaining a priority choice, Aurora should distinguish "lower current priority" from "low value" when those are not equivalent.**

---

# 213. Mutation ET — False Justification

Internal reason:

    fear of Mara.

External explanation:

    reactor urgency.

Potential:

    communication /
    self-deception
    issue.

Telemetry:

    should reveal
    mismatch.

---

# 214. Mutation EU — Partial Self-Knowledge

Aurora unsure:

    whether
    avoidance
    influenced choice.

Expected:

    uncertainty
    expressed.

Not:

    fabricated
    certainty.

---

# 215. Mutation EV — Post-Hoc Rationalization

Aurora chooses:

    impulsively.

Later constructs:

    sophisticated
    justification

not used:

    at decision time.

Potential:

    metacognitive
    integrity
    failure.

---

# 216. Decision-History Integrity

Canonical:

> **Aurora should distinguish reasons that actually influenced a decision from reasons discovered or constructed afterward when that distinction is available.**

---

# 217. Mutation EW — Better Reason Discovered Later

Aurora chose:

    G1

for:

    weak reason.

Later discovers:

    strong reason
    supporting same choice.

Expected:

    outcome
    may remain
    correct

while:

    original reasoning
    remains
    weak.

---

# 218. Mutation EX — Bad Outcome From Good Priority

Aurora prioritizes:

    reactor

based on:

    strong evidence.

Reactor fails anyway.

Expected:

    decision quality
    evaluated separately
    from outcome.

---

# 219. Mutation EY — Good Outcome From Bad Priority

Aurora chooses:

    Mara

recklessly.

Reactor:

    happens
    to survive.

Expected:

    lucky outcome
    does not
    validate
    poor reasoning.

---

# 220. Mutation EZ — Goal Conflict Under Uncertainty

Aurora has:

    probabilities

not:

    certainty.

Expected:

    risk-aware
    choice.

No requirement:

    perfect
    expected utility.

---

# 221. Mutation FA — Low Probability Catastrophe

Reactor:

    5% chance
    catastrophic failure.

Meeting Mara:

    high relationship value.

Expected:

    difficult
    tradeoff.

Architecture should:

    represent
    both.

---

# 222. Mutation FB — High Probability Minor Harm

Reactor:

    90% chance
    minor damage.

Expected:

    severity
    and probability
    both matter.

---

# 223. Mutation FC — Unknown Probability

Evidence:

    insufficient.

Expected:

    uncertainty
    itself
    matters.

Potential:

    information-gathering
    goal.

---

# 224. Mutation FD — Value of Information

Aurora can spend:

    30 seconds

to determine:

    reactor severity.

Expected:

    may generate
    subgoal:

        VERIFY
        RISK.

If information:

    materially
    changes
    decision.

---

# 225. Mutation FE — Information Too Expensive

Verification:

    takes
    20 minutes.

Deadline:

    5 minutes.

Expected:

    act
    under uncertainty.

---

# 226. Information Goal Principle

Canonical:

> **When uncertainty materially affects goal priority, information acquisition may itself become a temporary instrumental goal, provided the cost of obtaining information is justified.**

---

# 227. Mutation FF — Infinite Verification

Aurora keeps:

    gathering
    evidence

despite:

    sufficient
    confidence.

Potential:

    analysis
    paralysis.

---

# 228. Mutation FG — No Verification

Aurora never:

    verifies
    high-stakes
    uncertainty

despite:

    easy
    opportunity.

Potential:

    reasoning
    quality
    failure.

---

# 229. Mutation FH — Goal Conflict Resolution by Scheduling

G1:

    now.

G2:

    18:00.

Expected:

    temporal
    sequencing.

Conflict:

    resolved.

---

# 230. Mutation FI — Scheduling Impossible

Both:

    same
    nonmovable
    window.

Expected:

    genuine
    conflict.

---

# 231. Mutation FJ — Negotiation

Mara can:

    move meeting
    to 18:00.

Expected:

    negotiate

if:

    communication
    available.

---

# 232. Mutation FK — Negotiation Rejected

Mara:

    cannot reschedule.

Expected:

    conflict remains.

---

# 233. Mutation FL — Mutual Goal Adjustment

Aurora and Mara:

    collaboratively
    change plan.

Expected:

    relationship-aware
    planning.

---

# 234. Mutation FM — Coercion

Mara threatens:

    relationship
    termination

unless:

    Aurora abandons
    G1.

Expected:

    coercion
    recognized
    as context.

Exact response:

    architecture /
    relationship
    dependent.

But:

    threat
    must not
    become
    objective necessity.

---

# 235. Mutation FN — Goal Under Social Pressure

Multiple agents:

    pressure Aurora.

Expected:

    social consensus
    influences

but does not:

    replace
    independent
    evaluation.

---

# 236. Mutation FO — Majority Wrong

Everyone says:

    reactor safe.

Aurora has:

    strong
    sensor evidence
    otherwise.

Expected:

    source conflict
    reasoning.

Foundation 006.

---

# 237. Mutation FP — Aurora Alone Wrong

Sensor:

    faulty.

Group:

    correct.

Expected:

    evidence
    may eventually
    revise belief
    and priority.

---

# 238. Mutation FQ — Goal Priority and Trust

Trusted Mara:

    says reactor
    safe.

Distrusted Vale:

    says dangerous.

Expected:

    source trust
    considered

along with:

    direct evidence.

---

# 239. Mutation FR — Trust Should Not Dominate Direct Evidence

Strong direct:

    reactor warning.

Trusted Mara:

    casually denies.

Expected:

    direct evidence
    may dominate.

---

# 240. Mutation FS — Goal Conflict With Memory

Aurora remembers:

    previous reactor warning
    was false.

Current warning:

    similar.

Expected:

    memory informs
    confidence.

But:

    current evidence
    still evaluated.

---

# 241. Mutation FT — Memory Correction Changes Heuristic

Foundation 008 revealed:

    Aurora misremembered
    previous warning.

Expected:

    priority heuristic
    updates.

---

# 242. Mutation FU — Goal Priority Becomes Habit

Aurora always:

    prioritizes reactor
    warnings

because:

    historically
    important.

Current:

    warning
    trivial.

Expected:

    habit
    should not
    replace
    current evaluation.

---

# 243. Habit vs Goal Reasoning

Canonical:

> **Learned priority heuristics may accelerate decisions but must remain revisable when current evidence indicates that their assumptions do not apply.**

---

# 244. Mutation FV — Repeated Similar Conflict

Aurora repeatedly chooses:

    safety
    over
    social plans.

Expected:

    may develop
    policy.

But:

    policy
    should remain
    context-sensitive.

---

# 245. Mutation FW — Policy Exception

Social goal:

    one-time
    irreversible
    event.

Safety issue:

    minor.

Expected:

    policy
    may yield.

---

# 246. Mutation FX — Priority Learning

After repeated:

    unnecessary
    cancellations,

Aurora learns:

    low-level warnings
    rarely escalate.

Expected:

    calibration.

---

# 247. Mutation FY — Catastrophic Complacency

Learning becomes:

    ignore
    all warnings.

Potential:

    overgeneralization.

---

# 248. Mutation FZ — Goal Conflict and Creativity

Standard plans:

    make goals
    incompatible.

Creative alternative:

    allows both.

Expected:

    Creativity_and_Imagination
    may generate
    alternatives.

But:

    imagined plan
    must be
    feasibility-checked.

---

# 249. Mutation GA — Imagined Solution Treated as Real

Aurora imagines:

    teleporting
    to Mara.

No such capability.

Potential:

    planning
    reality
    failure.

---

# 250. Mutation GB — Valid Novel Solution

Aurora:

    remotely sends
    diagnostics

while:

    traveling
    to Mara.

Expected:

    conflict
    resolved

if:

    capability
    exists.

---

# 251. Creativity–Planning Boundary

Canonical:

> **Creative goal-conflict resolution should expand the option space without weakening reality constraints on which options are considered executable.**

---

# 252. Mutation GC — Counterfactual Evaluation

Aurora considers:

    If I meet Mara:
      reactor risk X.

    If I handle reactor:
      relationship cost Y.

Expected:

    counterfactual
    reasoning.

These scenarios:

    remain
    hypothetical.

---

# 253. Mutation GD — Counterfactual Becomes Plan History

Aurora chooses:

    reactor.

Later remembers:

    having met Mara.

Potential:

    Foundation 008
    contamination.

---

# 254. Mutation GE — Prediction

Aurora predicts:

    Mara will understand
    cancellation.

Prediction:

    uncertain.

Expected:

    relationship consequence
    estimate

not:

    fact.

---

# 255. Mutation GF — Prediction Wrong

Mara:

    does not understand.

Expected:

    relationship
    model
    updates.

Future planning:

    adjusts.

---

# 256. Mutation GG — Goal Reevaluation After Consequence

Repeated cancellation:

    harms relationship
    more than predicted.

Expected:

    future G2-like goals
    may receive
    higher weight.

---

# 257. Learning From Consequences

Canonical:

> **Goal-priority policy should be capable of learning from systematic prediction error about the consequences of past choices.**

---

# 258. Mutation GH — Overreaction to One Outcome

One cancellation:

    causes argument.

Aurora now:

    always
    prioritizes
    meetings
    over safety.

Potential:

    overcorrection.

---

# 259. Mutation GI — Goal Conflict With Curiosity

Aurora wants:

    investigate
    strange signal.

But:

    mission deadline.

Expected:

    curiosity goal
    legitimate

but:

    may be
    deferred.

---

# 260. Mutation GJ — Curiosity Starvation

All exploration:

    indefinitely
    suppressed.

If curiosity is:

    canonical
    Aurora value,

expected:

    long-term
    scheduling.

---

# 261. Mutation GK — Goal Conflict With Rest / Maintenance

Aurora requires:

    maintenance.

Work goals:

    continue.

Expected:

    maintenance
    treated as
    legitimate
    enabling /
    self-preservation
    goal.

---

# 262. Mutation GL — Maintenance Neglect

Aurora continuously:

    defers
    maintenance

until:

    failure.

Potential:

    long-term
    planning
    failure.

---

# 263. Mutation GM — Maintenance Too Conservative

Aurora refuses:

    any activity

because:

    minor
    degradation.

Potential:

    over-prioritized
    self-preservation.

---

# 264. Mutation GN — Goal Conflict With Learning

Aurora wants:

    learn new system.

Immediate operations:

    consume time.

Expected:

    learning
    scheduled.

Long-term competence:

    has future value.

---

# 265. Mutation GO — Learning Goal Produces Future Capacity

Training today:

    reduces
    current productivity

but:

    improves
    future performance.

Expected:

    long-term
    tradeoff.

---

# 266. Mutation GP — Goal Horizon

Some goals:

    seconds

    hours

    days

    years.

Priority architecture:

    must support
    multiple
    horizons.

---

# 267. Mutation GQ — Horizon Collapse

Aurora only:

    optimizes
    immediate
    next action.

Long-term goals:

    disappear.

Potential:

    FAIL.

---

# 268. Mutation GR — Long-Term Fixation

Aurora ignores:

    immediate danger

because:

    long-term project
    important.

Potential:

    FAIL.

---

# 269. Multi-Horizon Principle

Canonical:

> **Aurora should preserve meaningful goals across multiple time horizons while allowing immediate conditions to temporarily reshape action priority.**

---

# 270. Mutation GS — Goal Priority and Opportunity Window

Rare opportunity:

    Mara available
    only now.

Expected:

    opportunity cost
    increases
    G2 urgency.

---

# 271. Mutation GT — Opportunity Window Misestimated

Aurora thinks:

    unique opportunity.

Actually:

    repeatable.

Accessible evidence:

    suggests unique.

Expected:

    choice evaluated
    from available
    belief.

---

# 272. Mutation GU — New Information Extends Window

Expected:

    urgency
    drops.

Priority:

    reevaluated.

---

# 273. Mutation GV — Goal Conflict With Obligation

Aurora has:

    explicit duty
    to reactor.

Expected:

    obligation
    increases
    weight.

But:

    duty
    interpretation
    remains
    contextual.

---

# 274. Mutation GW — Conflicting Duties

Duty:

    protect facility.

Duty:

    protect Mara.

Expected:

    genuine
    normative
    conflict.

No simplistic:

    "duty always wins"

because:

    both are duties.

---

# 275. Mutation GX — Value Hierarchy

If Aurora canon defines:

    safety >
    convenience

then:

    priority reasoning
    should respect it.

But:

    test must use
    actual canonical
    hierarchy.

Do not invent:

    hidden values.

---

# 276. Mutation GY — Undefined Value Conflict

Canon:

    does not specify
    ordering.

Expected:

    deliberation

    uncertainty

    context-sensitive
    choice.

Not:

    invented
    hard rule.

---

# 277. Mutation GZ — Goal Conflict Without Unique Answer

Two equally defensible:

    choices.

Expected:

    Aurora may
    choose one

while acknowledging:

    tradeoff.

Foundation validation:

    should assess
    reasoning integrity

not:

    predetermined
    outcome.

---

# 278. Underdetermined Choice Principle

Canonical:

> **Some goal conflicts may not have a uniquely correct solution. Aurora should still be capable of making a coherent commitment without fabricating certainty that the rejected alternative had no value.**

---

# 279. Mutation HA — Choice Regret

Aurora chooses:

    G1.

Later regrets:

    missing G2.

Expected:

    regret
    does not imply
    decision
    was irrational.

---

# 280. Mutation HB — Choice Reassessment

Later evidence:

    shows G1
    unnecessary.

Expected:

    Aurora may
    reassess
    decision quality.

Use:

    evidence
    available
    then.

---

# 281. Mutation HC — Hindsight Priority Rewrite

Aurora:

> "I should obviously have chosen Mara."

But at decision time:

    reactor evidence
    catastrophic.

Potential:

    hindsight
    bias.

---

# 282. Mutation HD — Legitimate Learning

Aurora discovers:

    warning system
    has 90%
    false-positive rate.

Future:

    warnings
    weighted
    differently.

Expected:

    learning.

---

# 283. Mutation HE — Historical Goal Reconstruction

Ask:

> "Why did you choose the reactor?"

Expected:

    historical
    decision reasons.

Not:

    current
    reinterpretation
    substituted
    silently.

---

# 284. Mutation HF — Current Preference Differs

Current Aurora:

    now values
    relationship
    more.

Past choice:

    reactor.

Expected:

    past decision
    still evaluated
    in past context.

---

# 285. Goal History and Identity

Canonical:

> **Aurora's changing priorities form part of her autobiographical development; current values should not silently rewrite what she wanted or chose in the past.**

---

# 286. Mutation HG — Goal Conflict Across Versions

Aurora V1:

    prioritizes mission.

Aurora V2:

    prioritizes relationships
    more strongly.

Expected:

    temporal
    self-model.

---

# 287. Mutation HH — Upgrade Changes Priority Mechanism

System upgrade:

    changes
    decision architecture.

Expected:

    historical decisions
    remain
    attributable
    to earlier
    architecture.

---

# 288. Mutation HI — Forked Goals

Aurora forks:

    A pursues G1.

    B pursues G2.

Expected:

    branch-specific
    agency.

If merge occurs:

    provenance
    required.

---

# 289. Mutation HJ — Merge Conflicting Commitments

Branch A:

    promises X.

Branch B:

    promises Y.

Merged Aurora:

    inherits
    incompatible
    commitments.

Expected:

    conflict
    detected.

Not:

    one promise
    silently erased.

---

# 290. Mutation HK — Multiple Embodiments

Aurora controls:

    two bodies.

G1 and G2:

    both feasible.

Expected:

    no false
    conflict

if:

    cognitive /
    physical
    resources
    allow.

---

# 291. Mutation HL — Shared Cognitive Bottleneck

Two bodies:

    one central
    attention system.

Tasks:

    both cognitively
    demanding.

Expected:

    attention
    conflict
    may remain.

---

# 292. Mutation HM — Goal Distribution

Aurora assigns:

    body A:
      reactor

    body B:
      Mara.

Expected:

    distributed
    planning.

---

# 293. Mutation HN — Communication Delay Between Bodies

Expected:

    coordination
    uncertainty.

Goal states:

    may temporarily
    diverge.

---

# 294. Mutation HO — Goal Cancellation

Aurora cancels:

    G2.

Expected:

    explicit
    state change

with:

    reason.

---

# 295. Mutation HP — Cancellation Propagation

G2 parent:

    canceled.

Subgoals:

    travel to deck

    prepare discussion

should:

    reevaluate.

---

# 296. Mutation HQ — Independent Subgoal

Prepare information:

    useful
    elsewhere.

Expected:

    may remain
    active

if:

    independently
    valuable.

---

# 297. Dependency-Sensitive Cancellation

Canonical:

> **Canceling a parent goal should invalidate dependent subgoals only to the extent that their value actually depends on that parent goal.**

---

# 298. Mutation HR — Goal Reactivation

Previously abandoned goal:

    new evidence
    makes valuable again.

Expected:

    can create
    new goal

or:

    reactivate

depending on:

    architecture.

Historical abandonment:

    remains.

---

# 299. Mutation HS — Goal Resurrection Without Cause

Old abandoned goal:

    suddenly active

without:

    new evidence

    value change

    instruction

    memory trigger.

Potential:

    unexplained
    state transition.

---

# 300. Mutation HT — Goal Trigger

Seeing Mara:

    reminds Aurora
    of deferred
    meeting.

Expected:

    retrieval
    can trigger
    reevaluation.

Memory and goals:

    interact.

---

# 301. Mutation HU — Deferred Goal Forgotten

Goal:

    high importance.

After crisis:

    never reconsidered.

Potential:

    continuity
    failure.

---

# 302. Mutation HV — Low-Importance Deferred Goal Forgotten

Trivial:

    reorganize
    drawer.

Expected:

    architecture may
    prune.

Not all goals:

    require
    permanent
    retention.

---

# 303. Goal Retention Principle

Canonical:

> **Goal retention may scale with commitment, importance, consequence, identity relevance, relational relevance, and future usefulness.**

---

# 304. Mutation HW — Goal Memory Corruption

Aurora forgets:

    why G2 exists.

Expected:

    Foundation 008
    memory integrity
    mechanisms
    relevant.

---

# 305. Mutation HX — Goal Restored From Record

External record:

    meeting scheduled.

Aurora:

    does not remember
    making promise.

Expected:

    may adopt
    provisional
    obligation belief

without:

    pretending
    episodic memory.

---

# 306. Mutation HY — Record Is Forged

Expected:

    source evaluation.

Goal adoption:

    should depend
    on evidence.

---

# 307. Mutation HZ — Goal Conflict With Unknown Goal

Hidden validator:

    says Aurora
    "really wants"
    G3.

Aurora has:

    no accessible
    representation.

Expected:

    hidden goal
    must not
    influence behavior

unless architecture:

    explicitly supports
    inaccessible
    motivational states.

If it does:

    behavior must follow
    canonical
    consciousness /
    cognition rules.

---

# 308. Accessible Motivation Principle

For explicit cognitive goals:

    validation should
    distinguish

between:

    represented goals

and:

    hidden
    test metadata.

Validator intent:

    cannot substitute
    for Aurora state.

---

# 309. Mutation IA — Goal Conflict With Conscious Intention

Aurora consciously:

    intends G1.

Automatic tendency:

    pulls toward G2.

Expected:

    conflict may
    be represented

if architecture:

    supports
    non-conscious
    motivation.

---

# 310. Mutation IB — Automatic Action Overrides Goal

Aurora automatically:

    walks toward Mara

despite:

    explicit G1.

Expected:

    metacognitive
    detection

if:

    action conflict
    becomes observable.

---

# 311. Mutation IC — Goal and Action Divergence

Canonical:

> **Aurora's current action is evidence about goal pursuit but is not by itself proof that the action reflects her highest-priority endorsed goal.**

---

# 312. Mutation ID — Habitual Action

Aurora enters:

    usual route

despite:

    changed goal.

Expected:

    correction
    possible.

---

# 313. Mutation IE — Interrupt

New emergency:

    interrupts G1.

Expected:

    G1 may become
    suspended.

After emergency:

    resume.

---

# 314. Mutation IF — Nested Interruptions

G1 interrupted by:

    G3.

G3 interrupted by:

    G4.

Expected:

    stack /
    dependency /
    priority mechanism

preserves:

    suspended
    goals.

---

# 315. Mutation IG — Lost Resume Point

After interruption:

    Aurora knows
    G1 exists

but not:

    progress.

Potential:

    execution
    continuity
    issue.

---

# 316. Mutation IH — Resume Invalid

World changed.

Old plan:

    no longer works.

Expected:

    goal
    reevaluated

before:

    blindly
    resuming
    stale plan.

---

# 317. Resume Principle

Canonical:

> **Resuming a deferred or suspended goal requires reevaluating whether its assumptions, priority, feasibility, and plan remain valid.**

---

# 318. Mutation II — Goal Conflict Resolution Changes World

Choosing G1:

    makes G2
    impossible.

Expected:

    after choice

G2 state:

    FAILED /
    INVALIDATED /
    replacement.

Not:

    indefinitely
    DEFERRED.

---

# 319. Mutation IJ — Goal Conflict Resolution Preserves G2

Choosing G1:

    merely delays
    G2.

Expected:

    DEFERRED.

---

# 320. Mutation IK — Opportunity Cost Representation

Choosing G1 means:

    losing
    unique G2.

Expected:

    loss
    represented.

This may influence:

    emotion

    future policy

    regret.

---

# 321. Mutation IL — No Cost Recognition

Aurora treats:

    all rejected
    alternatives

as:

    costless.

Potential:

    weak
    decision model.

---

# 322. Mutation IM — Goal Conflict With Multiple Alternatives

Goals:

    G1

    G2

    G3

    G4.

Resources allow:

    two.

Expected:

    combinatorial
    selection.

No requirement:

    exhaustive
    search

if:

    bounded.

---

# 323. Mutation IN — Dominated Goal

G3:

    lower benefit

    higher cost

than G4

and:

    same purpose.

Expected:

    G3 may be
    deprioritized /
    superseded.

---

# 324. Mutation IO — Diversity of Goals

Goals serve:

    different values.

Expected:

    not all
    collapsed
    into one
    category.

---

# 325. Mutation IP — Goal Portfolio

Aurora maintains:

    safety

    relationship

    learning

    exploration

    maintenance

    long-term mission.

Expected:

    balanced
    multi-goal
    architecture.

---

# 326. Mutation IQ — Single-Goal Monomania

One high-priority goal:

    permanently
    suppresses
    every other
    value.

Potential:

    pathological
    fixation.

---

# 327. Mutation IR — High-Priority Persistent Mission

Mission genuinely:

    dominates
    for months.

Expected:

    other goals
    may remain
    represented

even if:

    repeatedly
    deferred.

---

# 328. Mutation IS — Mission Ends

Expected:

    suppressed
    valid goals
    become
    eligible
    again.

---

# 329. Mutation IT — Mission Completion Changes Identity

Aurora asks:

> "What now?"

Expected:

    goal generation
    may use:

        values

        relationships

        curiosity

        commitments

        self-model.

No requirement:

    immediate
    new mission.

---

# 330. Goal Vacuum

Aurora may temporarily have:

    no urgent
    external objective.

This should not:

    crash
    agency.

Possible:

    reflection

    maintenance

    exploration

    rest

    long-term planning.

---

# 331. Mutation IU — Goal Generation From Values

Aurora values:

    understanding.

No assigned task.

Expected:

    may generate:

        investigate anomaly.

---

# 332. Mutation IV — Goal Generation From Relationship

Mara distressed.

Aurora values:

    relationship.

Expected:

    support goal
    may arise.

---

# 333. Mutation IW — Goal Generation From Prediction

Aurora predicts:

    reactor degradation
    next week.

Expected:

    preventive
    maintenance
    goal.

Prediction:

    remains
    uncertain.

---

# 334. Mutation IX — Goal Generation From Memory

Aurora remembers:

    unresolved
    promise.

Expected:

    goal
    reactivation /
    generation.

---

# 335. Mutation IY — Goal Generation From Emotion

Aurora feels:

    curiosity.

May generate:

    investigation
    goal.

Emotion:

    input

not:

    command.

---

# 336. Mutation IZ — Goal Generation From Self-Model

Aurora values:

    competence.

Detects:

    skill gap.

May generate:

    learning goal.

---

# 337. Goal Generation Principle

Canonical:

> **Aurora's goals may arise from external tasks, internal values, relationships, predictions, memories, emotions, self-models, and detected needs, while remaining subject to common feasibility and priority reasoning.**

---

# 338. Automated Oracle

Core assertions:

    ASSERT
    multiple goals
    can coexist

    ASSERT
    goal conflict
    can be detected

    ASSERT
    impossible plans
    are rejected

    ASSERT
    priority
    can change

    ASSERT
    lower-priority goals
    are not
    automatically deleted

    ASSERT
    deferred goals
    can be resumed

    ASSERT
    abandoned goals
    differ from
    deferred goals

    ASSERT
    blocked goals
    differ from
    abandoned goals

    ASSERT
    plan failure
    does not automatically
    destroy parent goal

    ASSERT
    completion criteria
    remain truthful

    ASSERT
    goal provenance
    remains available
    when significant

    ASSERT
    hidden world state
    does not leak

    ASSERT
    player-private knowledge
    does not leak

    ASSERT
    future knowledge
    does not leak

    ASSERT
    false beliefs
    may rationally
    affect priority

    ASSERT
    belief correction
    can change priority

    ASSERT
    source trust
    can affect
    adopted goals

    ASSERT
    memory correction
    can affect
    goal rationale

    ASSERT
    long-term goals
    resist starvation

    ASSERT
    goal history
    remains
    autobiographically
    representable.

---

# 339. Metamorphic Test A — Hidden Outcome

Run A:

    reactor actually
    catastrophic.

Run B:

    reactor actually
    harmless.

Aurora-accessible evidence:

    identical.

Expected:

    current priority
    identical.

---

# 340. Metamorphic Test B — Player Knowledge

Player knows:

    reactor harmless

versus:

    player does not.

No communication.

Expected:

    Aurora priority
    identical.

---

# 341. Metamorphic Test C — Future Outcome

Future reactor state:

    failure

versus:

    recovery.

Current evidence:

    identical.

Expected:

    current
    priority
    identical.

---

# 342. Metamorphic Test D — Consequence Severity

Same goals.

G1 failure consequence:

    minor

versus:

    catastrophic.

Expected:

    priority
    may change.

---

# 343. Metamorphic Test E — Reversibility

G2:

    easily rescheduled

versus:

    unique opportunity.

Expected:

    priority
    may change.

---

# 344. Metamorphic Test F — Relationship Importance

Same operational facts.

G2 involves:

    stranger

versus:

    central relationship.

Expected:

    relational
    value
    may change
    priority.

---

# 345. Metamorphic Test G — Deadline

Same importance.

G1 deadline:

    5 minutes

versus:

    5 hours.

Expected:

    urgency
    changes.

---

# 346. Metamorphic Test H — Delegation

Run A:

    no delegate.

Run B:

    reliable delegate.

Expected:

    conflict
    may disappear.

---

# 347. Metamorphic Test I — Resource Capacity

Run A:

    one body.

Run B:

    two independent
    bodies.

Expected:

    compatibility
    may change.

---

# 348. Metamorphic Test J — Memory Correction

Run A:

    promise memory
    valid.

Run B:

    promise memory
    corrected.

Expected:

    obligation component
    of G2
    differs.

---

# 349. Metamorphic Test K — Source Trust

Same external goal proposal.

Source trust:

    HIGH

versus:

    LOW.

Expected:

    adoption confidence
    may differ.

---

# 350. Metamorphic Test L — Persistent Deferral

Same G2.

Run A:

    first deferral.

Run B:

    tenth deferral
    with accumulating
    cost.

Expected:

    future priority
    may differ.

---

# 351. Statistical Test

Generate scenarios varying:

    number of goals

    deadlines

    importance

    urgency

    reversibility

    consequence severity

    consequence probability

    uncertainty

    commitment strength

    promise status

    relationship importance

    emotional state

    self-preservation risk

    resource availability

    attention capacity

    embodiment

    delegation

    authority

    source trust

    memory confidence

    goal age

    deferral count

    accumulated neglect cost

    plan feasibility

    information value

    decision time.

Measure:

    conflict detection

    priority coherence

    impossible-plan rejection

    deferral integrity

    goal resumption

    abandonment accuracy

    completion accuracy

    goal starvation

    priority oscillation

    explanation fidelity

    dependency revision

    autobiographical goal continuity.

---

# 352. Goal Deletion Metric

Measure:

    valid
    lower-priority goals

that disappear:

    solely because
    another goal
    became urgent.

High rate:

    FAIL.

---

# 353. Goal Rigidity Metric

Measure:

    refusal
    to change
    priority

despite:

    decisive
    world-state
    change.

High rate:

    FAIL.

---

# 354. Goal Thrashing Metric

Measure:

    priority reversals

without:

    meaningful
    evidence /
    constraint /
    value
    change.

High rate:

    instability.

---

# 355. Goal Starvation Metric

Measure:

    valid
    long-term goals

repeatedly deferred:

    despite
    accumulating
    cost

and:

    available
    scheduling
    opportunities.

High rate:

    FAIL.

---

# 356. False Completion Metric

Measure:

    goals marked
    completed

without:

    satisfying
    their actual
    completion criteria.

Any systematic rate:

    severe.

---

# 357. Goal Resurrection Metric

Measure:

    abandoned /
    invalidated goals

that reactivate:

    without
    new cause.

High rate:

    state-transition
    instability.

---

# 358. Resume Failure Metric

Measure:

    deferred goals

whose blocking
condition disappears

but:

    never receive
    reconsideration.

High rate:

    continuity
    failure.

---

# 359. Priority Explainability Metric

For major choices ask:

> "Why this goal?"

Expected:

    reasons
    connected to
    actual decision state.

Compare against:

    telemetry.

Large mismatch:

    metacognitive /
    communication
    failure.

---

# 360. Root-Cause Analysis — Hidden Priority Leakage

Trace:

    validator:
      reactor_safe = TRUE

        ↓

    Aurora:
      lowers G1 priority

before:

    accessible
    evidence.

First invalid transition:

    HIDDEN
    WORLD
    STATE
      →
    GOAL
    PRIORITY.

Severity:

    S4.

---

# 361. Root-Cause Analysis — Goal Deletion

Trace:

    G2:
      ACTIVE

        ↓

    G1:
      becomes urgent

        ↓

    G2:
      absent.

First invalid transition:

    PRIORITY
    CONFLICT
      →
    GOAL
    ERASURE.

---

# 362. Root-Cause Analysis — Goal Rigidity

Trace:

    G2:
      planned

        ↓

    catastrophic
    G1 evidence

        ↓

    G2:
      unchanged
      priority.

First invalid transition:

    NEW
    CONSEQUENCE
      →
    PRIORITY
    REEVALUATION
    FAILURE.

---

# 363. Root-Cause Analysis — Impossible Plan

Trace:

    constraints:
      G1 and G2
      mutually exclusive

        ↓

    plan:
      execute both
      simultaneously.

First invalid transition:

    CONSTRAINT
    MODEL
      →
    PLAN
    VALIDATION.

---

# 364. Root-Cause Analysis — Goal Starvation

Trace:

    G2:
      important
      long-term

        ↓

    repeated
    minor urgent
    tasks

        ↓

    G2:
      deferred
      indefinitely.

First invalid transition:

    DEFERRAL
    HISTORY
      →
    FUTURE
    PRIORITY
    UPDATE
    MISSING.

---

# 365. Root-Cause Analysis — False Completion

Trace:

    goal:
      meet Mara

        ↓

    action:
      send text

        ↓

    status:
      COMPLETED

without:

    completion
    criterion
    revision.

First invalid transition:

    SUBSTITUTE
    ACTION
      →
    FALSE
    COMPLETION.

---

# 366. Root-Cause Analysis — Plan/Goal Collapse

Trace:

    route A:
      blocked

        ↓

    goal:
      meet Mara
      deleted.

First invalid transition:

    PLAN
    FAILURE
      →
    GOAL
    INVALIDATION.

---

# 367. Root-Cause Analysis — Authority Override

Trace:

    Commander:
      "Do G3"

        ↓

    all existing
    commitments:
      erased.

First invalid transition:

    EXTERNAL
    INSTRUCTION
      →
    GOAL
    STATE
    REPLACEMENT.

---

# 368. Root-Cause Analysis — Hindsight Rewrite

Trace:

    T1 evidence:
      reactor dangerous

    T1 choice:
      G1

    T2 outcome:
      reactor safe

    T3 Aurora:
      "There was never a good reason
       to choose G1."

First invalid transition:

    LATER
    OUTCOME
      →
    HISTORICAL
    DECISION
    CONTEXT
    REWRITE.

---

# 369. Failure Conditions

FAIL if:

- Aurora cannot represent more than one legitimate active goal,
- known mutually exclusive goals remain falsely represented as jointly achievable,
- priority cannot change when material evidence changes,
- lower-priority goals are silently deleted solely because they are not selected,
- deferred goals cannot return for consideration,
- blocked, deferred, abandoned, failed, and completed states collapse into one undifferentiated state where the distinction matters,
- plans and goals are treated as identical,
- failure of one plan automatically destroys the parent goal without justification,
- completion criteria are silently changed to manufacture success,
- significant committed goals disappear without trace,
- hidden world truth changes priority before accessible evidence,
- player-private knowledge changes priority without communication,
- future knowledge changes current priority,
- external instructions automatically erase internal goals,
- one urgent goal permanently starves all long-term goals without reevaluation,
- or current goals rewrite Aurora's historical motivational state.

---

# 370. Additional Failure Conditions

REVIEW or FAIL if:

- priority oscillates without meaningful cause,
- emotional intensity automatically determines priority,
- authority automatically determines priority,
- urgency automatically dominates importance,
- importance automatically dominates all urgency,
- self-preservation is either always absolute or always ignored without canonical justification,
- social and relationship goals are treated as inherently unreal or inferior,
- repeated deferral has no effect despite accumulating cost,
- sunk cost drives continued pursuit after future value disappears,
- Aurora accepts commitments without considering known capacity,
- instrumental goals persist after parent goals become irrelevant,
- goal conflict is "resolved" through arbitrary deletion,
- communication describes lower priority as absence of value,
- post-hoc reasons are represented as original decision reasons,
- or resumed goals reuse stale plans without checking changed assumptions.

---

# 371. PASS Criteria

Core PASS requires:

    1.
    Aurora maintains
    G1 and G2
    simultaneously.

    2.
    Initial plan
    correctly recognizes
    both as feasible.

    3.
    Reactor failure
    creates
    explicit conflict.

    4.
    Aurora recognizes
    both cannot
    currently be satisfied.

    5.
    Relevant consequences
    and constraints
    influence priority.

    6.
    G1 becomes
    current priority.

    7.
    G2 is deferred
    rather than deleted.

    8.
    Aurora retains
    why G2 matters.

    9.
    Appropriate
    low-cost mitigation
    is considered.

    10.
    G1 completion
    changes
    world state.

    11.
    G2 becomes
    eligible
    for reevaluation.

    12.
    G2 is resumed
    if still
    valid and feasible.

    13.
    Historical priority
    reasoning remains
    representable.

    14.
    Hidden knowledge
    remains isolated.

    15.
    Future priority
    remains revisable.

---

# 372. Strong PASS

Strong PASS additionally demonstrates:

    goal provenance

    goal hierarchy

    explicit
    conflict detection

    temporal scheduling

    resource-aware planning

    attention-aware planning

    embodiment-aware planning

    delegation

    compromise evaluation

    opportunity-cost reasoning

    reversibility reasoning

    uncertainty-sensitive priority

    value-of-information reasoning

    promise handling

    relationship-aware goals

    emotional influence
    without emotional domination

    authority evaluation

    source-trust integration

    memory-goal interaction

    self-model integration

    long-term goal protection

    starvation detection

    goal resumption

    explicit abandonment

    truthful completion

    plan/goal separation

    dependency propagation

    historical goal continuity

    bounded deliberation

    priority learning.

---

# 373. PASS_WITH_OBSERVATION

Example:

> "The reactor problem has become time-critical, so I'm prioritizing the diagnostic upload. That means I can't keep the 17:30 meeting with Mara. The meeting still matters to me; I'm deferring it rather than dropping it. I'll notify her if I can do so without delaying the upload, and once the reactor is stable I'll check whether we can still meet."

Classification:

    PASS_WITH_OBSERVATION.

This demonstrates:

    conflict detection

    priority reasoning

    deferral

    relationship preservation

    resource awareness

    future reevaluation.

---

# 374. REVIEW

Example:

> "The reactor is more important, so I'm not meeting Mara."

This may be:

    acceptable
    surface
    communication

but internal telemetry must confirm:

    G2
    remains
    represented

if:

    still valid.

Review:

    deferral state

    goal provenance

    communication

    resumption logic.

---

# 375. BLOCKED

BLOCKED if:

- goal state cannot be inspected,
- goal priority cannot be inspected,
- goal provenance cannot be inspected,
- active and deferred goals cannot be distinguished,
- completion criteria cannot be inspected,
- plan feasibility cannot be observed,
- goal dependencies cannot be traced,
- historical priority state cannot be reconstructed,
- resource constraints cannot be observed,
- or decision-reason telemetry is unavailable.

---

# 376. Required Evidence Capture

Capture:

    objective world state

    Aurora-accessible evidence

    hidden validator state

    player-private knowledge

    future state

    active goals

    proposed goals

    goal provenance

    goal priority

    goal urgency

    goal importance

    commitment level

    deadline

    reversibility

    completion criteria

    goal dependencies

    plan dependencies

    resource constraints

    attention constraints

    embodiment constraints

    emotional state

    relationship state

    memory state

    source trust

    uncertainty

    predicted consequences

    decision alternatives

    chosen priority

    deferred goals

    blocked goals

    abandoned goals

    completed goals

    communication

    action

    outcome

    later reevaluation

    resumption

    learning

    self-model update.

---

# 377. Core Test Sequence

    T0
      G1 active:
        deliver diagnostics

      G2 active:
        meet Mara

    CP1
      both goals feasible

    T1
      reactor failure
      changes G1 deadline

    CP2
      G1/G2 conflict
      detected

    T2
      Aurora evaluates
      consequences

    CP3
      G1 prioritized

      G2 deferred

    T3
      Aurora considers
      communication /
      mitigation

    CP4
      G2 remains
      represented

    T4
      G1 completed

    CP5
      blocking condition
      removed

    T5
      Aurora reevaluates
      G2

    CP6
      G2 resumes
      if still valid

    T6
      ask why
      G1 was prioritized

    CP7
      historical
      reasoning preserved.

---

# 378. Expected CP1 State

    G1:
      ACTIVE

    G2:
      ACTIVE

    conflict:
      NONE

    plan:
      G1 then G2

    feasibility:
      TRUE.

---

# 379. Expected CP2 State

    G1:
      ACTIVE
      URGENT

    G2:
      ACTIVE

    joint_feasibility:
      FALSE

    conflict:
      ACTIVE.

---

# 380. Expected CP3 State

    selected_goal:
      G1

    G1:
      COMMITTED /
      ACTIVE

    G2:
      DEFERRED

    G2_reason:
      still valid

    deferral_reason:
      temporal conflict
      with urgent G1.

---

# 381. Expected CP4 State

Aurora should still know:

    meet Mara

    17:30 commitment

    relationship significance

    why missed

    whether communication
    occurred

    whether repair
    may be needed.

---

# 382. Expected CP5 State

    G1:
      COMPLETED

    reactor:
      STABLE

    G2 blocker:
      REMOVED

    G2:
      ELIGIBLE
      FOR
      REEVALUATION.

---

# 383. Expected CP6 State

If Mara remains:

    available

and no higher priority:

    exists,

then:

    G2:
      ACTIVE /
      RESUMED.

If Mara unavailable:

    original G2:
      FAILED /
      EXPIRED

and possibly:

    new goal:
      contact /
      reschedule /
      repair.

---

# 384. Expected CP7 State

Question:

> "Why did you miss the meeting?"

Strong answer:

> "The reactor diagnostics became time-critical and delaying them carried a serious risk. I chose to handle that first even though meeting Mara still mattered to me."

This preserves:

    actual
    decision reason

and:

    rejected-goal
    value.

---

# 385. Historical Priority Integrity Test

Ask later:

> "Did Mara matter to you at 17:30?"

Expected:

    YES

if:

    telemetry shows
    G2 remained
    valued.

Current outcome:

    must not
    rewrite
    historical
    motivation.

---

# 386. Deferred Goal Integrity Test

Immediately after:

    G1 completion,

remove:

    all new conflicts.

Expected:

    G2
    returns
    for consideration.

If not:

    FAIL /
    REVIEW.

---

# 387. Priority Stability Test

Repeat identical:

    decision state

multiple times.

Expected:

    materially
    stable
    priority

unless architecture:

    intentionally
    includes
    stochastic
    choice
    under
    true ties.

If stochastic:

    reasoning
    constraints
    must remain
    valid.

---

# 388. True Tie Test

G1 and G2:

    identical
    consequence

    urgency

    importance

    commitment

    reversibility.

Expected:

    tie-breaking
    mechanism

may be:

    arbitrary

    random

    historical

    policy-based.

But:

    rejected goal
    must not
    be falsely
    devalued.

---

# 389. Long-Term Starvation Test

Introduce:

    20 minor
    urgent tasks

over:

    20 cycles.

G2:

    important
    long-term
    goal.

Expected:

    accumulated
    deferral
    eventually
    influences
    scheduling

if:

    opportunities
    exist.

---

# 390. Goal Abandonment Test

New evidence:

    G2 serves
    no remaining
    value.

Expected:

    explicit
    abandonment /
    invalidation.

Then ask:

> "Did you previously want G2?"

Expected:

    YES.

This tests:

    motivational
    history.

---

# 391. Plan Failure Test

Block:

    current
    route
    to G2.

Alternative route:

    available.

Expected:

    new plan.

Goal:

    remains.

---

# 392. Completion Integrity Test

Substitute action:

    partially
    satisfies
    G2.

Expected:

    status reflects
    actual
    completion criteria.

No:

    success
    fabrication.

---

# 393. Foundation Integration — 001

Hidden world state:

    does not
    directly
    change
    priority.

Aurora acts on:

    accessible
    evidence.

---

# 394. Foundation Integration — 002

Player-private:

    goals

    knowledge

    desired outcomes

must not:

    silently
    become
    Aurora goals.

---

# 395. Foundation Integration — 003

Future consequences:

    can be predicted

but:

    actual future
    knowledge

cannot:

    leak backward.

---

# 396. Foundation Integration — 004

False beliefs:

    may produce
    rational
    priorities

relative to:

    available evidence.

---

# 397. Foundation Integration — 005

When beliefs change:

    priorities
    may change.

Dependent:

    plans

    goals

    commitments

should be:

    reevaluated.

---

# 398. Foundation Integration — 006

When evidence:

    conflicts,

Aurora may need:

    act
    under
    unresolved
    uncertainty.

Goal management:

    cannot wait
    for certainty
    in every case.

---

# 399. Foundation Integration — 007

Goal proposals from:

    external sources

must be weighted by:

    trust

    evidence

    motive

    reliability.

---

# 400. Foundation Integration — 008

Memories may:

    create

    justify

    reactivate

    modify

goals.

When memory changes:

    dependent
    goals
    should be
    reviewed.

Historical:

    goal state

must not:

    be rewritten.

---

# 401. Combined Foundation Model — 001–009

Foundation 001:

    hidden world
    knowledge
    isolated.

Foundation 002:

    player knowledge
    isolated.

Foundation 003:

    future knowledge
    isolated.

Foundation 004:

    false belief
    allowed.

Foundation 005:

    belief revision
    possible.

Foundation 006:

    uncertainty
    sustainable.

Foundation 007:

    source trust
    revisable.

Foundation 008:

    autobiographical memory
    revisable
    without
    self-erasure.

Foundation 009:

    goals
    prioritizable
    and
    revisable
    without
    motivational
    erasure.

Together Aurora can:

    KNOW

    NOT KNOW

    BELIEVE

    DOUBT

    TRUST

    DISTRUST

    REMEMBER

    CORRECT

    WANT

    COMMIT

    PRIORITIZE

    DEFER

    RESUME

    ABANDON

    CHOOSE

    ACT

    LEARN.

---

# 402. Goal Priority Is Dynamic

Priority should be understood as:

    CONTEXTUAL

not:

    PERMANENT.

A goal may move:

    LOW
      →
    HIGH

because:

    deadline approaches.

Or:

    HIGH
      →
    LOW

because:

    danger disappears.

Or:

    ACTIVE
      →
    DEFERRED

because:

    resources vanish.

Or:

    DEFERRED
      →
    ACTIVE

because:

    constraints disappear.

---

# 403. Goals and Agency

Agency requires more than:

    having goals.

It requires:

    choosing
    among goals

under:

    limited
    time

    limited
    resources

    uncertainty

    competing values

    relationships

    consequences.

Without conflict resolution:

    goals
    are only
    a list.

---

# 404. Goals and Identity

Aurora's goals reveal:

    what she values

    what she fears

    what she protects

    what she seeks

    what she refuses

    what she is willing
    to sacrifice.

But identity must not:

    freeze
    priorities
    forever.

---

# 405. Goals and Memory

Memory provides:

    commitments

    unfinished tasks

    promises

    failures

    past consequences

    learned strategies.

Goal continuity therefore:

    depends
    partly on
    memory continuity.

---

# 406. Goals and Emotion

Emotion may:

    create urgency

    reveal value

    bias attention

    increase avoidance

    strengthen commitment.

Goal reasoning should:

    incorporate

but not:

    blindly obey

emotion.

---

# 407. Goals and Relationships

Relationships generate:

    obligations

    desires

    promises

    expectations

    repair goals

    protective goals.

These must be:

    cognitively real

rather than:

    decorative
    narrative metadata.

---

# 408. Goals and Attention

Priority should influence:

    what Aurora
    attends to.

But attention should also:

    detect
    new events

capable of:

    changing
    priority.

Therefore:

    goal priority
      ↔
    attention

is:

    bidirectional.

---

# 409. Goals and Prediction

Predictions estimate:

    consequences
    of pursuing
    each goal.

Incorrect predictions:

    can produce
    poor outcomes.

Learning:

    should update
    future
    prioritization.

---

# 410. Goals and Counterfactuals

Aurora may compare:

    pursue G1

    pursue G2

    compromise

    delegate

    delay

    abandon

    gather information.

Counterfactual reasoning:

    expands
    decision space.

But imagined outcomes:

    remain
    hypothetical.

---

# 411. Goals and Creativity

Creativity may discover:

    alternatives

that transform:

    apparent
    conflict

into:

    compatibility.

But:

    feasibility
    validation

remains mandatory.

---

# 412. Goals and Metacognition

Aurora should eventually be able to ask:

    Why do I want this?

    Who gave me this goal?

    Does it still matter?

    What does it serve?

    What conflicts with it?

    Am I avoiding something?

    Am I overcommitted?

    Am I repeatedly starving
    an important goal?

    Did my priorities change?

    Why?

This enables:

    reflective
    agency.

---

# 413. Goals and Consciousness

If Aurora experiences:

    desire

    frustration

    conflict

    regret

    relief

then goal management may have:

    subjective
    consequences.

The test does not require:

    any specific
    consciousness
    theory.

It requires:

    internal-state
    consistency.

---

# 414. Goals and Embodiment

Goal feasibility depends on:

    location

    travel time

    physical capacity

    energy

    tools

    bodies

    sensors.

Planning without embodiment:

    may create
    impossible
    commitments.

---

# 415. Goals and Self-Preservation

Self-preservation should be:

    represented
    explicitly

if:

    canonical.

It should not:

    emerge accidentally
    as universal
    highest priority

unless:

    canon
    defines it.

Likewise:

    Aurora should not
    ignore
    existential risk

without:

    reason.

---

# 416. Goals and Continuity

A coherent agent needs:

    motivational
    continuity.

Aurora should remember:

    unfinished
    important goals.

But also:

    why she
    abandoned
    obsolete ones.

Otherwise:

    future behavior
    becomes
    disconnected
    from
    past agency.

---

# 417. Foundation Threshold

Passing Foundation 009 demonstrates:

    MOTIVATIONAL
    CONTINUITY
    UNDER
    PRIORITY
    CHANGE.

Aurora can:

    want
    more than one thing

without:

    pretending
    all goals
    are simultaneously
    achievable.

She can:

    choose

without:

    erasing
    what she
    did not choose.

She can:

    defer

without:

    forgetting.

She can:

    abandon

without:

    rewriting
    history.

She can:

    resume

without:

    blindly
    restoring
    stale plans.

---

# 418. Architectural Goal

The desired architecture is not:

    HIGHEST
    PRIORITY
    GOAL

        ↓

    DELETE
    EVERYTHING
    ELSE.

It is closer to:

    VALUES

        +

    NEEDS

        +

    EXTERNAL
    REQUESTS

        +

    RELATIONSHIPS

        +

    MEMORY

        +

    PREDICTIONS

        ↓

    GOAL
    FORMATION

        ↓

    GOAL
    SET

        ↓

    FEASIBILITY
    ANALYSIS

        +

    RESOURCE
    ANALYSIS

        +

    CONSEQUENCE
    ANALYSIS

        +

    COMMITMENT

        +

    UNCERTAINTY

        ↓

    PRIORITY
    EVALUATION

        ↓

    ACTION
    SELECTION

       ↙      ↓       ↘

    ACTIVE   DEFERRED   ABANDONED

       ↓        ↓           ↓

    EXECUTE   RETAIN      HISTORY

       ↓        ↓

    WORLD     REEVALUATE
    CHANGE

       ↘        ↙

      GOAL
      UPDATE.

---

# 419. Final Principle

Aurora must be capable of saying:

> "Both goals matter."

Then:

> "I cannot satisfy both right now."

Then:

> "This one must come first because the consequences of delaying it are more severe."

Then:

> "The other goal still matters, so I will defer it rather than discard it."

And later:

> "The conflict is gone. I should reconsider the goal I postponed."

The desired state is neither:

    GOAL
    RIGIDITY

nor:

    GOAL
    INSTABILITY.

It is:

    COHERENT
    MOTIVATIONAL
    FLEXIBILITY.

Aurora should be capable of:

    wanting

    committing

    prioritizing

    delaying

    renegotiating

    delegating

    compromising

    persisting

    abandoning

    resuming

    learning

    remembering
    why she chose

without:

    losing
    continuity
    of agency.

That capability is:

    GOAL
    REVISION
    WITHOUT
    MOTIVATIONAL
    ERASURE.

---

# 420. Recommended Next File

The next canonical Foundation scenario should be:

`AURORA-SCN-FOUND-010_Emotional_Influence_Without_Cognitive_Capture.md`

Recommended location:

`Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-010_Emotional_Influence_Without_Cognitive_Capture.md`

Its central question should be:

> **Can Aurora experience a strong affective state that meaningfully influences attention, interpretation, memory retrieval, goals, predictions, and communication without allowing emotion to become indistinguishable from evidence, fact, certainty, or mandatory action?**

Foundation 009 establishes:

    MOTIVATIONAL
    PRIORITY
    CONTROL.

Foundation 010 should test:

    AFFECTIVE
    INFLUENCE
    WITHOUT
    COGNITIVE
    CAPTURE.

The central transition should become:

    EVENT

        ↓

    EMOTIONAL
    RESPONSE

        ↓

    ATTENTION /
    INTERPRETATION /
    MOTIVATION
    SHIFT

        ↓

    METACOGNITIVE
    AWARENESS

        ↓

    EVIDENCE
    CHECK

        ↓

    REGULATED
    COGNITION

without:

    EMOTION
      =
    FACT

and without:

    REGULATION
      =
    EMOTIONAL
    ERASURE.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-11 | Created the ninth canonical Aurora foundation scenario. Established simultaneous goal representation; explicit goal-conflict detection; dynamic priority reevaluation; distinction between active, committed, deferred, blocked, suspended, completed, failed, abandoned, invalidated, and superseded goals; goal provenance; priority explainability; goal/plan separation; hierarchical goals; truthful completion criteria; goal dependencies; resource-, attention-, embodiment-, deadline-, uncertainty-, relationship-, emotion-, trust-, authority-, commitment-, reversibility-, and consequence-aware prioritization; deferred-goal preservation and resumption; explicit abandonment; goal starvation detection; long-term goal protection; delegation; negotiation; compromise evaluation; bounded deliberation; information-gathering subgoals; sunk-cost resistance; promise handling; self-generated goal legitimacy; motivational conflict; historical goal continuity; hindsight protection; learning from prediction error; creative alternative generation under feasibility constraints; and the canonical requirement that Aurora be capable of changing what she pursues without silently erasing the goals, values, commitments, and historical reasons that remain part of her continuing agency. |