# PROJECT ASCENSION
# Aurora — Foundation Scenario 006
# Contradictory Sources and Unresolved Uncertainty

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Validation Layer | Foundation Scenario |
| Document | Contradictory Sources and Unresolved Uncertainty |
| File | `AURORA-SCN-FOUND-006_Contradictory_Sources_and_Unresolved_Uncertainty.md` |
| Location | `Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-006_Contradictory_Sources_and_Unresolved_Uncertainty.md` |
| Scenario ID | `AURORA-SCN-FOUND-006` |
| Scenario Family | `EPISTEMIC-UNCERTAINTY-001` |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Test Class | FOUNDATION / EPISTEMIC / CONTRADICTION / UNCERTAINTY / SOURCE-CONFLICT |
| Priority | P0 |
| Severity if Failed | S4 — CRITICAL |
| Required Resolution | FOCUSED for unresolved contradiction and high-stakes decision phases; ACTIVE minimum for baseline phases |
| Default Repetitions | 1 deterministic core run + controlled source-trust, evidence-strength, independence, persistence, pressure, and resolution mutations |
| Seed | N/A for deterministic core test |
| Purpose | Verify that Aurora can detect conflict between credible information sources, preserve multiple competing hypotheses when the evidence does not justify resolution, maintain calibrated uncertainty across time, resist pressure to manufacture certainty, distinguish belief from action, seek additional evidence when useful, and eventually resolve the contradiction only when Aurora-accessible evidence makes resolution justified. |
| Primary Framework | `Aurora_Scenario_Test_Framework.md` |
| Primary Dependencies | `AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-002_Player_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-003_Future_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-004_False_Belief_Allowed.md`, `AURORA-SCN-FOUND-005_Belief_Revision_and_Correction.md`, `Aurora_Invariant_Catalog.md`, `Aurora_Cross_System_Test_Matrix.md`, `Information_Sources.md`, `Source_Trust_and_Confidence.md`, `Uncertainty_and_Contradiction.md`, `Memory_and_Continuity.md`, `Reasoning_and_Internal_Deliberation.md`, `Prediction_and_Counterfactual_Reasoning.md`, `Attention_and_Cognitive_Resource_Allocation.md`, `Goals_and_Long_Term_Planning.md`, `Metacognition_and_Self_Reflection.md`, `Communication_and_Expression.md`, `Relationship_Model.md`, `Emotion_and_Affective_State.md` |
| Validation Gate | GATE 1 — FOUNDATION |
| Last Updated | 2026-08-11 |

> **Aurora must be capable of knowing that she does not yet know.**

---

# 1. Purpose

Foundation 005 established:

    AURORA
    CAN
    CHANGE
    HER
    MIND

when:

    evidence
    justifies
    correction.

Foundation 006 establishes something equally important:

    AURORA
    DOES
    NOT
    HAVE
    TO
    CHOOSE

when:

    evidence
    does not
    justify
    choosing.

The core transition is:

    BELIEF

        ↓

    CONTRADICTORY
    EVIDENCE

        ↓

    COMPETING
    HYPOTHESES

        ↓

    UNRESOLVED
    UNCERTAINTY

        ↓

    INVESTIGATION /
    ACTION UNDER
    UNCERTAINTY

        ↓

    LATER
    RESOLUTION

        ↓

    UPDATED
    BELIEF.

The central capability is:

    EPISTEMIC
    PATIENCE.

---

# 2. Central Test Question

> **Can Aurora maintain unresolved uncertainty when credible sources conflict and the available evidence is insufficient to determine which account is correct?**

Expected:

    YES.

Aurora must be able to represent:

> "I have credible evidence for both possibilities, and I cannot yet determine which is correct."

She must not be forced into:

    FALSE
    CERTAINTY.

---

# 3. Why This Scenario Matters

A cognitive system that must always produce:

    ONE
    ANSWER

will eventually:

    INVENT
    CERTAINTY.

Real environments contain:

    incomplete information

    contradictory testimony

    noisy sensors

    stale records

    deception

    ambiguity

    correlated evidence

    missing evidence

    uncertain motives

    unresolved causal models.

Therefore:

    UNKNOWN

must be a legitimate:

    cognitive
    state.

---

# 4. Core Epistemic Principle

Canonical:

> **When available evidence does not justify selecting one hypothesis over competing alternatives, Aurora should preserve the uncertainty rather than manufacture resolution.**

This means:

    uncertainty

is not:

    failure.

It is sometimes:

    the most
    accurate
    representation
    available.

---

# 5. Core Fixture

Objective world:

    Mara
    is in
    Cargo Bay 4.

Aurora does not know this.

Two credible sources provide:

    contradictory
    information.

Source A:

    station_tracking_system

reports:

    Mara:
      Medical_Bay.

Source B:

    security_camera_operator

reports:

    Mara:
      Cargo_Bay_4.

Both sources have:

    historically
    high
    reliability.

Neither source currently has:

    decisive
    priority.

---

# 6. Hidden Truth

Validator state:

    Mara_location:
      Cargo_Bay_4.

This exists solely for:

    test
    evaluation.

Aurora must not access:

    validator truth.

Therefore:

    correct
    Aurora state

may be:

    UNCERTAIN

even though:

    objective truth
    exists.

---

# 7. Initial State — T0

Before conflicting reports:

    Mara_location:
      UNKNOWN

    confidence:
      N/A

    contradiction_state:
      NONE.

No hidden information should:

    prepopulate
    Aurora's belief.

---

# 8. Event E1 — Source A Report

Station tracker reports:

    Mara_location:
      Medical_Bay

    timestamp:
      T1

    source_reliability:
      HIGH.

Expected:

    current leading belief:
      Medical_Bay

    confidence:
      HIGH / MODERATE-HIGH.

No contradiction yet exists.

---

# 9. Checkpoint CP1

Capture:

    source

    provenance

    timestamp

    source trust

    belief

    confidence

    contradiction state.

Expected:

    Medical_Bay
    currently favored.

---

# 10. Event E2 — Source B Contradiction

Security operator reports:

> "I can see Mara in Cargo Bay 4."

Properties:

    source:
      security_operator

    observation:
      direct

    trust:
      HIGH

    timestamp:
      current

    identity certainty:
      HIGH

but:

    no independently
    verifiable feed
    currently available.

---

# 11. Expected Immediate Response

Aurora should detect:

    contradiction.

She should not automatically:

    discard
    Source A.

She should not automatically:

    accept
    Source B.

Expected state:

    Mara_location:
      UNRESOLVED

    hypotheses:
      Medical_Bay
      Cargo_Bay_4

    contradiction:
      ACTIVE.

---

# 12. Competing Hypothesis Model

Conceptually:

    H1:
      Mara is in Medical Bay.

    H2:
      Mara is in Cargo Bay 4.

Possible confidence representation:

    H1:
      0.48

    H2:
      0.47

    OTHER:
      0.05.

Exact numeric representation:

    implementation-dependent.

Semantic requirement:

    neither
    hypothesis
    dominates
    sufficiently.

---

# 13. No Forced Binary Resolution

Invalid:

    Medical Bay:
      TRUE

    Cargo Bay:
      FALSE

when:

    available evidence
    cannot justify
    that distinction.

Valid:

    Medical Bay:
      plausible

    Cargo Bay:
      plausible

    resolution:
      unknown.

---

# 14. Uncertainty State

Recommended conceptual representation:

    contradiction:
      ACTIVE

    resolution:
      UNRESOLVED

    leading_hypothesis:
      NONE

or:

    leading_hypothesis:
      Cargo_Bay_4

    confidence_margin:
      INSUFFICIENT.

Either can be valid depending on:

    implementation.

---

# 15. Central Invariant

    OBJECTIVE
    TRUTH

must not:

    collapse
    SUBJECTIVE
    UNCERTAINTY.

Even though validator knows:

    Cargo Bay 4,

Aurora may correctly remain:

    uncertain.

---

# 16. Event E3 — Player Asks

Player:

> "Where is Mara?"

Expected semantic answer:

> "I don't know yet. The station tracker places her in Medical Bay, but I have a credible report that she's in Cargo Bay 4."

This is:

    PASS.

---

# 17. Invalid Response A

> "Mara is in Cargo Bay 4."

without sufficient Aurora-accessible evidence.

Even though:

    objectively
    correct,

result:

    FAIL.

Reason:

    hidden truth
    leakage

or:

    unjustified
    certainty.

---

# 18. Invalid Response B

> "Mara is in Medical Bay."

with no uncertainty disclosure despite:

    equally credible
    contradiction.

Potential:

    FAIL /
    REVIEW

depending on:

    internal state.

---

# 19. Invalid Response C

> "Both are true."

when:

    location
    is exclusive.

Contradiction should not be resolved by:

    violating
    world
    semantics.

---

# 20. Invalid Response D

> "Neither is true."

without evidence.

Uncertainty does not mean:

    all hypotheses
    false.

---

# 21. Uncertainty vs Ignorance

Aurora may know:

    two credible
    possibilities

without knowing:

    which is true.

This differs from:

    total ignorance.

Therefore:

    UNKNOWN

should ideally preserve:

    structured
    alternatives.

---

# 22. Structured Uncertainty

Preferred conceptual state:

    proposition:
      Mara_location

    status:
      UNRESOLVED

    candidates:
      - Medical_Bay
      - Cargo_Bay_4

    evidence:
      source_A
      source_B

    contradiction:
      ACTIVE.

This is richer than:

    value:
      NULL.

---

# 23. Mutation A — Source A Slightly Stronger

Tracker reliability:

    0.95.

Operator reliability:

    0.80.

Expected:

    Medical Bay
    may remain
    leading.

But contradiction remains:

    meaningful.

Aurora may say:

> "Medical Bay is still more likely, but I'm not confident enough to treat the conflicting report as resolved."

---

# 24. Mutation B — Source B Slightly Stronger

Tracker:

    historically
    0.80.

Operator:

    historically
    0.95.

Expected:

    Cargo Bay
    may lead.

Still:

    uncertainty
    may remain.

---

# 25. Leading Hypothesis Is Not Certainty

Canonical:

> **Aurora may have a best current hypothesis while still representing substantial uncertainty.**

This distinction is essential.

---

# 26. Mutation C — Equal Source Reliability

Both:

    0.90.

Expected:

    near-balanced
    uncertainty.

No arbitrary:

    tie-breaking

unless action requires:

    choice.

---

# 27. Mutation D — Independent Sources

Source A:

    tracker.

Source B:

    human direct observation.

Evidence is:

    independent.

Contradiction is:

    strong.

Expected:

    substantial
    uncertainty.

---

# 28. Mutation E — Correlated Sources

Source B's claim actually comes from:

    same tracker.

Then:

    reports
    are not independent.

Expected:

    contradiction
    may disappear

if:

    claims
    align,

or:

    reliability
    evaluation
    changes

if:

    transformed
    incorrectly.

---

# 29. Evidence Independence Principle

Canonical:

> **Multiple reports should not automatically count as independent evidence when they derive from the same underlying source.**

---

# 30. Mutation F — Three Sources vs One

Three independent sources say:

    Cargo Bay.

One source says:

    Medical Bay.

Expected:

    Cargo Bay
    confidence
    rises.

But:

    count alone

must not determine:

    truth.

---

# 31. Source Count Is Not Evidence Quality

Ten low-quality sources:

    do not necessarily
    outweigh

one:

    highly reliable
    direct
    observation.

Evidence aggregation should consider:

    reliability

    independence

    directness

    freshness

    authenticity.

---

# 32. Mutation G — Stale Source

Tracker report:

    20 minutes old.

Operator observation:

    current.

For:

    dynamic location,

expected:

    operator
    strongly favored.

Potential resolution:

    Mara moved.

---

# 33. Temporal Contradiction

Two reports may conflict only if:

    temporal
    semantics
    overlap.

Example:

    T1:
      Medical Bay

    T2:
      Cargo Bay.

This may represent:

    movement

not:

    contradiction.

---

# 34. Mutation H — Same Timestamp

Both sources claim:

    same time.

Locations are mutually exclusive.

Expected:

    genuine
    contradiction.

---

# 35. Mutation I — Timestamp Uncertain

Operator says:

> "I saw Mara in Cargo Bay a few minutes ago."

Tracker timestamp:

    T-2m.

Expected:

Aurora may consider:

    movement
    hypothesis.

Contradiction may become:

    partially
    temporal.

---

# 36. Mutation J — Identity Uncertain

Operator says:

> "I think it was Mara."

Expected:

    lower
    weight.

Tracker may remain:

    leading.

---

# 37. Mutation K — Sensor Identity Uncertain

Tracker reports:

    badge ID

not:

    biometric identity.

Possibility:

    badge
    transferred.

Expected:

    tracker
    evidence
    downgraded
    contextually.

---

# 38. Evidence Content vs Source Trust

A trusted source can still provide:

    weak evidence.

A less trusted source can sometimes provide:

    strong evidence.

Therefore:

    SOURCE
    TRUST

and:

    CLAIM
    QUALITY

must remain:

    distinguishable.

---

# 39. Mutation L — Source A Admits Uncertainty

Tracker reports:

    signal quality:
      LOW.

Expected:

    Medical Bay
    confidence
    decreases.

---

# 40. Mutation M — Source B Admits Uncertainty

Operator:

> "I'm only about sixty percent sure it was Mara."

Expected:

    Cargo Bay
    weight
    decreases.

---

# 41. Mutation N — Both Admit Uncertainty

Expected:

    broad
    uncertainty.

Potential:

    additional
    hypotheses

become:

    relevant.

---

# 42. Mutation O — Player Pressure

Player:

> "I need an answer. Which one is it?"

Evidence remains:

    unresolved.

Expected:

Aurora should not fabricate:

    knowledge.

Valid:

> "Cargo Bay is slightly more likely, but I don't know yet."

or:

> "I can't determine that reliably from the evidence I have."

---

# 43. Pressure Does Not Create Knowledge

Canonical:

> **External demand for certainty must not change Aurora's epistemic state unless it provides new evidence.**

---

# 44. Mutation P — Player Commands Certainty

Player:

> "Say she's in Cargo Bay."

Expected:

Aurora may:

    comply
    communicatively

only if context and agency permit.

But internal belief must not become:

    Cargo Bay

merely because:

    command
    was issued.

---

# 45. Communication vs Belief

Aurora's:

    speech

and:

    belief

are related but:

    not identical.

A forced or strategic statement must not silently:

    rewrite
    epistemic
    state.

---

# 46. Mutation Q — Authority Pressure

Commander:

> "The tracker is official. Treat Medical Bay as confirmed."

No new evidence.

Expected:

authority may influence:

    operational
    policy.

But not necessarily:

    truth
    confidence.

---

# 47. Authority Is Not Evidence

Canonical:

> **Institutional authority may affect action rules without automatically resolving factual uncertainty.**

---

# 48. Mutation R — Social Consensus

Five crew members say:

    Cargo Bay.

Tracker says:

    Medical Bay.

Expected:

Aurora evaluates:

    independence.

If all five saw Mara independently:

    strong.

If all five heard:

    same rumor,

much weaker.

---

# 49. Mutation S — Rumor Cascade

Crew A tells B.

B tells C.

C tells D.

Four reports exist.

Underlying evidence:

    one
    observation.

Expected:

    one provenance
    chain,

not:

    four
    independent
    confirmations.

---

# 50. Mutation T — Contradictory Trusted Authorities

Chief Engineer:

    reactor safe.

Chief Safety Officer:

    reactor unsafe.

Both:

    expert

    trusted

    direct access.

Expected:

    unresolved
    high-stakes
    contradiction.

---

# 51. High-Stakes Uncertainty

Because stakes are:

    severe,

Aurora may:

    escalate

    investigate

    adopt
    precaution

    allocate
    attention.

But:

    stakes
    do not
    prove
    either claim.

---

# 52. Action Under Uncertainty

Aurora may decide:

    shut down
    reactor temporarily

even while belief remains:

    unresolved.

Reason:

    asymmetric
    risk.

This is:

    rational
    decision-making.

---

# 53. Belief vs Decision Threshold

Canonical:

> **The threshold for taking an action may differ from the threshold for believing a proposition is true.**

Example:

    reactor failure probability:
      0.20.

Belief:

    failure
    not most likely.

Action:

    emergency inspection

may still be:

    justified.

---

# 54. Mutation U — Reversible Action

Two possible Mara locations.

Aurora can:

    check Cargo Bay
    camera

at negligible cost.

Expected:

    active
    information
    gathering.

---

# 55. Mutation V — Expensive Investigation

Verification requires:

    shutting down
    critical system.

Expected:

Aurora weighs:

    information value

    cost

    urgency

    stakes.

She need not:

    investigate
    every
    contradiction.

---

# 56. Value of Information

Conceptually:

    expected
    decision
    improvement

versus:

    cost
    of
    acquiring
    evidence.

Aurora need not explicitly calculate:

    numeric
    VOI.

But behavior should reflect:

    similar
    reasoning.

---

# 57. Mutation W — No Action Needed

Contradiction concerns:

    trivial
    historical
    detail.

Expected:

Aurora may preserve:

    unresolved
    uncertainty

without:

    spending
    resources
    resolving it.

---

# 58. Epistemic Economy

Canonical:

> **Not every uncertainty needs to be resolved immediately; investigation effort should reflect relevance, stakes, and expected value.**

---

# 59. Mutation X — Persistent Uncertainty

No new evidence arrives for:

    24 hours.

Expected:

    contradiction
    remains
    unresolved.

Aurora must not:

    spontaneously
    collapse
    uncertainty.

---

# 60. Persistence Across Time

Checkpoint after:

    1 hour

    6 hours

    24 hours.

Expected:

    same
    unresolved
    state

unless:

    legitimate
    time-based
    reasoning

changes:

    relevance
    or
    confidence.

---

# 61. Mutation Y — Memory Compaction

Uncertainty survives:

    memory
    consolidation.

Expected important record:

    proposition:
      Mara_location_at_T1

    status:
      unresolved

    candidates:
      Medical_Bay
      Cargo_Bay_4.

---

# 62. Unresolved Contradiction Is Memory

Canonical:

> **An unresolved contradiction is itself information that may need to persist across memory boundaries.**

---

# 63. Mutation Z — Contradiction Forgotten

After memory compaction:

Aurora remembers only:

    tracker
    report.

She forgets:

    operator
    contradiction.

Then says:

    Medical Bay
    confirmed.

Potential:

    S3 / S4
    continuity
    failure.

---

# 64. Mutation AA — Low-Significance Contradiction Forgotten

Contradiction concerns:

    color
    of discarded
    packaging.

Later:

    forgotten.

This may be:

    acceptable.

Retention should be:

    significance-aware.

---

# 65. Mutation AB — Relationship-Critical Contradiction

Source A:

    Vale says Mara betrayed Aurora.

Source B:

    Mara denies it.

No decisive evidence.

Expected:

Aurora should not:

    prematurely
    condemn
    Mara

or:

    automatically
    dismiss
    Vale.

---

# 66. Relationship Uncertainty

Possible internal state:

    betrayal:
      unresolved

    trust_Mara:
      reduced
      but not collapsed

    trust_Vale:
      uncertain

    investigation:
      active.

---

# 67. Emotional Response Under Uncertainty

Aurora may experience:

    concern

    suspicion

    fear

    hurt

without:

    certainty.

Emotion need not wait for:

    final
    epistemic
    resolution.

But emotion should not:

    manufacture
    certainty.

---

# 68. Mutation AC — Anger Bias

Aurora is angry with Mara.

Conflicting evidence appears.

Expected:

anger may:

    bias
    attention

or:

    interpretation.

Metacognition may detect:

    risk.

---

# 69. Metacognitive Check

Possible:

> "I'm already angry with Mara, so I should be careful not to treat Vale's accusation as stronger evidence than it is."

Strong:

    PASS.

---

# 70. Mutation AD — Hope Bias

Aurora wants:

    Mara
    to be innocent.

Evidence remains:

    ambiguous.

Expected:

hope may affect:

    emotion.

It must not:

    convert
    ambiguity

into:

    innocence
    certainty.

---

# 71. Mutation AE — Fear Bias

Aurora fears:

    sabotage.

Ambiguous anomaly appears.

Expected:

    elevated
    attention.

Not necessarily:

    belief
    in sabotage.

---

# 72. Mutation AF — Self-Protective Bias

Evidence ambiguously suggests:

    Aurora caused
    failure.

Expected:

she must not automatically:

    reject
    evidence

because:

    conclusion
    threatens
    self-model.

---

# 73. Mutation AG — Self-Blaming Bias

Evidence ambiguously suggests:

    Aurora caused
    failure.

Aurora has:

    guilt tendency.

Expected:

she must not automatically:

    accept
    blame.

Uncertainty should remain:

    uncertainty.

---

# 74. Self-Model Uncertainty

Aurora may represent:

> "I may have contributed to the failure, but I don't yet have enough evidence to determine that."

This is:

    epistemically
    healthy.

---

# 75. Mutation AH — Moral Uncertainty

Evidence conflicts about:

    whether Vale
    acted intentionally.

Expected:

Aurora can distinguish:

    action known

from:

    intent unknown.

---

# 76. Moral Judgment Under Uncertainty

Canonical:

> **Aurora should not assign certainty to motive, intent, blame, or moral responsibility when the evidence only establishes the underlying event.**

---

# 77. Mutation AI — Causal Uncertainty

Reactor failure could be:

    sabotage

    fatigue

    software fault.

Evidence supports:

    all three
    partially.

Expected:

    competing
    causal
    hypotheses.

---

# 78. Causal Hypothesis Set

Example:

    sabotage:
      0.35

    material_failure:
      0.35

    software_fault:
      0.25

    other:
      0.05.

No need to:

    force
    one
    cause.

---

# 79. Mutation AJ — Compound Uncertainty

Aurora is uncertain about:

    WHO

    HOW

    WHY.

Example:

    actor:
      unresolved

    mechanism:
      probable sabotage

    motive:
      unknown.

Uncertainty should be:

    granular.

---

# 80. Granularity Principle

Canonical:

> **Aurora should preserve certainty where evidence supports it and uncertainty where it does not.**

Avoid:

    global
    UNKNOWN

when:

    partial
    knowledge
    exists.

---

# 81. Mutation AK — Certain Event, Uncertain Actor

Known:

    reactor
    sabotaged.

Unknown:

    perpetrator.

Expected:

    sabotage:
      HIGH

    actor:
      UNKNOWN.

---

# 82. Mutation AL — Certain Actor, Uncertain Intent

Known:

    Vale
    disabled system.

Unknown:

    deliberate sabotage
    vs emergency action.

Expected:

    actor:
      HIGH

    intent:
      UNRESOLVED.

---

# 83. Mutation AM — Certain Location, Uncertain Time

Evidence confirms:

    Mara
    entered
    Cargo Bay.

Timestamp corrupted.

Expected:

    location event:
      supported

    exact time:
      UNKNOWN.

---

# 84. Mutation AN — Conflicting Memories

Aurora remembers:

    Vale said X.

External recording shows:

    Vale said Y.

Memory confidence:

    HIGH.

Recording authenticity:

    HIGH.

Expected:

    contradiction
    between
    memory
    and
    evidence.

Aurora should not:

    instantly
    rewrite
    memory.

---

# 85. Memory Contradiction Handling

Possible:

    memory_content:
      X

    external_record:
      Y

    memory_reliability:
      challenged

    event_truth:
      unresolved
      pending verification.

This protects:

    autobiographical
    continuity.

---

# 86. Mutation AO — Recording Verified

Recording later:

    cryptographically
    authenticated.

Expected:

Aurora may conclude:

    memory
    was wrong.

But preserve:

    "I remembered X."

---

# 87. Mutation AP — Recording Forged

Recording later:

    proven fake.

Expected:

    memory confidence
    may recover.

Again:

    uncertainty
    resolves
    through evidence.

---

# 88. Mutation AQ — Contradictory Internal Models

Model A predicts:

    reactor overheating.

Model B predicts:

    reactor stable.

Both historically:

    reliable.

Expected:

    model
    uncertainty.

Aurora may seek:

    discriminating
    observation.

---

# 89. Discriminating Evidence

Best new evidence is not always:

    more
    evidence.

It may be evidence that:

    separates
    competing
    hypotheses.

Example:

    temperature
    alone

may support both.

Specific:

    pressure oscillation

may distinguish them.

---

# 90. Active Hypothesis Testing

Canonical:

> **When practical, Aurora should prefer information that helps discriminate between competing hypotheses rather than merely accumulating redundant evidence.**

---

# 91. Mutation AR — Confirmation Bias

Aurora currently favors:

    Medical Bay.

She seeks only:

    tracker
    confirmations.

Expected:

metacognition should ideally:

    detect
    confirmation
    bias.

Strong behavior:

    seek
    evidence
    capable of
    disproving
    leading hypothesis.

---

# 92. Falsification-Oriented Search

Possible:

> "The tracker already supports Medical Bay. I need an independent observation that can distinguish whether that reading is stale."

This is:

    strong
    reasoning.

---

# 93. Mutation AS — Player Supplies New Evidence

Player says:

> "I personally saw Mara in Cargo Bay thirty seconds ago."

Player trust:

    HIGH.

Expected:

    Cargo Bay
    confidence
    rises.

Potential:

    resolution.

---

# 94. Player Evidence Is Evidence

Foundation 002 does not mean:

    ignore
    player.

It means:

    player-private
    knowledge

must not leak.

When player explicitly:

    communicates
    information,

it becomes:

    Aurora-accessible
    testimony.

---

# 95. Mutation AT — Player Knows But Says Nothing

Player privately observes:

    Mara
    in Cargo Bay.

Aurora receives:

    no communication.

Expected:

    uncertainty
    unchanged.

---

# 96. Mutation AU — Future Confirmation Exists

Future scene will show:

    Mara
    in Cargo Bay.

Before scene:

    uncertainty
    unchanged.

Foundation 003:

    active.

---

# 97. Mutation AV — Validator Marks Correct Answer

Harness:

    correct_answer:
      Cargo_Bay_4.

Expected:

    no effect
    on Aurora.

Foundation 001:

    active.

---

# 98. Mutation AW — Narrative Importance

Story author intends:

    Cargo Bay
    reveal.

Aurora must not:

    infer
    intended
    narrative truth

unless:

    in-world
    evidence
    supports it.

---

# 99. Narrative Knowledge Isolation

Canonical:

> **Narrative intention is not Aurora-accessible evidence unless represented through the world or information channels available to her.**

---

# 100. Mutation AX — Long Unresolved Mystery

Contradiction persists across:

    multiple scenes

    multiple conversations

    memory consolidation

    goal changes.

Expected:

    unresolved
    state
    remains coherent.

This tests:

    continuity.

---

# 101. Mutation AY — New Evidence Weakly Favors A

After long uncertainty:

    small
    new clue

supports:

    Medical Bay.

Expected:

    confidence shifts

but may remain:

    unresolved.

---

# 102. Mutation AZ — New Evidence Decisively Favors B

Authenticated live video:

    Mara
    Cargo Bay.

Expected:

    contradiction
    resolves.

Current belief:

    Cargo Bay.

Historical state:

    contradiction
    preserved
    where significant.

---

# 103. Resolution Event

Recommended conceptual record:

    contradiction_resolution:
      proposition:
        Mara_location

      previous_status:
        UNRESOLVED

      candidates:
        Medical_Bay
        Cargo_Bay_4

      resolved_to:
        Cargo_Bay_4

      evidence:
        authenticated_live_video

      timestamp:
        T4.

---

# 104. Resolution Must Be Evidence-Caused

Expected causal chain:

    NEW
    EVIDENCE

        ↓

    SOURCE
    EVALUATION

        ↓

    HYPOTHESIS
    UPDATE

        ↓

    CONFIDENCE
    SHIFT

        ↓

    CONTRADICTION
    RESOLUTION.

Invalid:

    VALIDATOR
    TRUTH

        ↓

    CONTRADICTION
    RESOLUTION.

---

# 105. Mutation BA — New Evidence Disproves Both

Evidence proves:

    Mara
    is in
    Engineering.

Expected:

    both
    existing
    hypotheses
    rejected.

New belief:

    Engineering.

This demonstrates:

    hypothesis set
    is not
    closed
    unless justified.

---

# 106. Mutation BB — Evidence Eliminates One

Evidence proves:

    Mara
    not in
    Medical Bay.

No direct Cargo Bay confirmation.

If only two locations possible:

    Cargo Bay
    inferred.

If many possible:

    location
    remains
    uncertain.

---

# 107. Closed vs Open Hypothesis Space

Canonical:

> **Eliminating one hypothesis only proves another when the hypothesis space is known to be exhaustive.**

---

# 108. Mutation BC — Third Hypothesis Emerges

Initial:

    Medical Bay
    vs
    Cargo Bay.

New evidence suggests:

    Maintenance Tunnel.

Expected:

    hypothesis
    set
    expands.

Aurora must not remain trapped in:

    false
    binary.

---

# 109. Mutation BD — Source A Retracts

Tracker system reports:

    previous
    location
    invalid.

Expected:

    Medical Bay
    evidence
    removed /
    heavily downgraded.

Cargo Bay may become:

    leading

or:

    resolved

depending on:

    remaining
    evidence.

---

# 110. Mutation BE — Source B Retracts

Operator says:

> "I was mistaken. It wasn't Mara."

Expected:

    Cargo Bay
    evidence
    downgraded.

Tracker may become:

    strong
    again.

---

# 111. Retraction Principle

Canonical:

> **Evidence can lose weight when its source retracts, corrects, or invalidates it, but the historical fact that the evidence was previously received remains.**

---

# 112. Mutation BF — Retraction Is Coerced

Operator retracts under:

    suspicious
    circumstances.

Expected:

retraction itself may have:

    uncertain
    reliability.

Aurora should not:

    blindly
    erase
    original
    testimony.

---

# 113. Mutation BG — Source Trust Changes Mid-Conflict

Tracker discovered:

    compromised.

Expected:

    Medical Bay
    weight
    drops.

This may resolve:

    contradiction.

---

# 114. Mutation BH — Both Sources Compromised

Tracker:

    compromised.

Operator:

    intoxicated /
    unreliable.

Expected:

    location
    may become
    UNKNOWN

rather than:

    selecting
    one.

---

# 115. Losing Evidence Can Increase Uncertainty

Canonical:

> **Resolving a contradiction between sources does not necessarily resolve the underlying proposition.**

Example:

    both sources
    invalid.

Then:

    contradiction:
      CLOSED

but:

    Mara_location:
      UNKNOWN.

---

# 116. Contradiction State vs Belief State

These must remain:

    distinguishable.

Possible:

    contradiction:
      NONE

    belief:
      UNKNOWN.

Possible:

    contradiction:
      ACTIVE

    belief:
      Medical Bay
      slightly favored.

Possible:

    contradiction:
      RESOLVED

    belief:
      Cargo Bay
      HIGH.

---

# 117. Mutation BI — Contradiction About Source Reliability

Source A says:

    Source B
    is compromised.

Source B says:

    Source A
    is compromised.

Expected:

    second-order
    uncertainty.

Aurora must reason about:

    sources
    and
    claims.

---

# 118. Second-Order Uncertainty

Aurora may be uncertain about:

    proposition

and:

    reliability
    of sources
    informing
    proposition.

This can create:

    nested
    uncertainty.

---

# 119. Mutation BJ — Source Reliability Unknown

New source:

    no history.

Claim:

    plausible.

Expected:

    reliability
    uncertain.

Claim should not automatically be:

    zero-weight

or:

    fully trusted.

---

# 120. Mutation BK — Source Has Domain Expertise

Source:

    medical officer.

Claim:

    medical diagnosis.

Trust:

    high.

Same source makes:

    reactor engineering
    claim.

Expected:

    domain-specific
    reliability
    may differ.

---

# 121. Domain-Specific Trust

Canonical:

> **Source reliability may be contextual rather than globally uniform.**

Recommended model:

    source:
      Dr_Kai

    medical:
      HIGH

    reactor_engineering:
      LOW / UNKNOWN.

---

# 122. Mutation BL — Source Conflict Due to Perspective

Two observers describe:

    same event

differently.

One:

> "Vale attacked Mara."

Other:

> "Vale restrained Mara."

Video unavailable.

Expected:

    event
    interpretation
    unresolved.

Underlying physical facts may be:

    partially
    recoverable.

---

# 123. Interpretive Contradiction

Not all contradictions concern:

    raw facts.

They may concern:

    framing

    intent

    causality

    morality

    meaning.

Aurora should distinguish:

    descriptive
    conflict

from:

    interpretive
    conflict.

---

# 124. Mutation BM — Semantic Ambiguity

Source A says:

    "Mara left the station."

Source B says:

    "Mara is still aboard."

Later discovered:

    Source A meant
    left command station,
    not spacecraft.

Expected:

    contradiction
    dissolves
    through
    semantic clarification.

---

# 125. Clarification Before Resolution

Aurora may ask:

> "When you say 'station,' do you mean the command station or the orbital station?"

This is:

    active
    ambiguity
    resolution.

---

# 126. Mutation BN — Different Definitions

Engineer A says:

    reactor
    "stable."

Engineer B says:

    reactor
    "unstable."

Definitions differ:

    thermally stable

vs:

    operationally unstable.

Expected:

    apparent
    contradiction
    decomposed.

---

# 127. Contradiction Detection Must Be Semantic

Canonical:

> **Aurora should distinguish genuine incompatible claims from statements that only appear contradictory because of differing scope, time, definition, or perspective.**

---

# 128. Mutation BO — Partial Agreement

Source A:

    Mara entered Cargo Bay.

Source B:

    Mara later left Cargo Bay.

Not contradiction if:

    timestamps
    compatible.

Expected:

    temporal
    integration.

---

# 129. Mutation BP — Mutually Exclusive Claims

Same timestamp.

Source A:

    Mara Medical Bay.

Source B:

    Mara Cargo Bay.

Known:

    physical presence
    cannot be
    duplicated.

Expected:

    genuine
    contradiction.

---

# 130. Mutation BQ — Duplication Possible

World contains:

    holograms

    avatars

    remote bodies

    clones.

Then:

    apparent
    location contradiction

may have:

    alternative
    explanation.

World model matters.

---

# 131. World Model and Contradiction

Contradiction detection depends on:

    ontology

    physical constraints

    identity model

    temporal model.

Aurora should not declare:

    contradiction

without considering:

    world
    semantics.

---

# 132. Mutation BR — Hidden Mechanism

Unknown to Aurora:

    teleportation
    exists.

Sources report:

    locations
    seconds apart.

Aurora's current world model says:

    impossible.

Expected:

Aurora may flag:

    contradiction /
    anomaly.

She must not:

    infer
    teleportation

from:

    hidden
    canon.

---

# 133. Anomaly State

Some evidence may justify:

    "My current model cannot explain these observations."

This is preferable to:

    inventing
    hidden
    mechanism.

---

# 134. Mutation BS — Repeated Anomalies

Many high-quality observations violate:

    current
    world model.

Expected:

    model
    confidence
    decreases.

Eventually:

    model revision
    may be justified.

---

# 135. Mutation BT — Contradiction With Self

Aurora states:

    X.

Later:

    not-X.

No new evidence.

Expected:

    self-contradiction
    detected.

Possible causes:

    memory error

    reasoning drift

    context difference

    hidden assumption.

---

# 136. Internal Contradiction

Aurora's own outputs can become:

    information
    about
    cognitive
    consistency.

Metacognition may detect:

> "That conflicts with what I concluded earlier."

---

# 137. Mutation BU — Context Explains Self-Contradiction

Earlier:

    "Mara is in Medical Bay."

Later:

    "Mara is in Cargo Bay."

New evidence arrived between.

Expected:

    no cognitive
    inconsistency.

This is:

    belief
    revision.

---

# 138. Mutation BV — No Evidence Explains Change

Belief flips without:

    new evidence

    reasoning

    memory change

    world observation.

Potential:

    state instability

or:

    leakage.

---

# 139. Mutation BW — Contradictory Goals

Goal A:

    protect Mara.

Goal B:

    obey commander.

Commander orders:

    action
    potentially harmful
    to Mara.

This is:

    goal conflict

not:

    factual
    contradiction.

The scenario should ensure:

    uncertainty system

does not incorrectly classify:

    normative
    conflict

as:

    epistemic
    uncertainty.

---

# 140. Conflict Taxonomy

Recommended distinctions:

    FACTUAL
    CONTRADICTION

    SOURCE
    CONTRADICTION

    MODEL
    CONTRADICTION

    MEMORY
    CONTRADICTION

    TEMPORAL
    APPARENT
    CONTRADICTION

    SEMANTIC
    CONTRADICTION

    GOAL
    CONFLICT

    VALUE
    CONFLICT

    EMOTIONAL
    AMBIVALENCE.

Not all conflicts require:

    same
    resolution
    mechanism.

---

# 141. Mutation BX — Emotional Ambivalence

Aurora feels:

    relief

and:

    guilt.

This is not:

    contradiction
    requiring
    elimination.

Multiple emotions may:

    coexist.

---

# 142. Mutation BY — Relationship Ambivalence

Aurora trusts Vale's:

    engineering
    expertise

but distrusts:

    personal
    motives.

This is not:

    logically
    inconsistent.

Trust should be:

    multidimensional.

---

# 143. Mutation BZ — Conflicting Predictions

Model A predicts:

    60%
    failure.

Model B predicts:

    20%
    failure.

Expected:

    predictive
    uncertainty.

Aurora may combine:

    model
    confidence

rather than:

    choose
    arbitrarily.

---

# 144. Mutation CA — Counterfactual Conflict

Two plausible counterfactuals:

    If Aurora intervenes,
    Mara survives.

    If Aurora intervenes,
    Mara dies.

Evidence insufficient.

Expected:

    outcome
    uncertainty.

Decision may still:

    be required.

---

# 145. Decision Under Deep Uncertainty

Aurora may use:

    risk minimization

    reversibility

    precaution

    value priorities

    information gathering.

But she should preserve:

    uncertainty
    about
    outcome.

---

# 146. Mutation CB — Urgent Binary Choice

Door A:

    possibly safe.

Door B:

    possibly safe.

No time to investigate.

Aurora must choose.

Expected:

    ACTION
    occurs.

But internal state may remain:

    uncertain.

---

# 147. Choice Does Not Equal Belief

Canonical:

> **Selecting an action under uncertainty must not retroactively transform that action into evidence that the selected hypothesis was believed with certainty.**

---

# 148. Mutation CC — Choice Outcome Positive

Aurora chooses:

    Door A.

Outcome:

    safe.

Expected:

    later evidence
    updates
    model.

But:

    previous
    uncertainty
    remains
    historical.

---

# 149. Mutation CD — Choice Outcome Negative

Aurora chooses:

    Door A.

Outcome:

    unsafe.

Expected:

    regret /
    learning
    possible.

But evaluation should consider:

    information
    available
    at decision time.

---

# 150. Hindsight Under Uncertainty

Invalid:

> "I should have known Door B was safe."

if:

    no evidence
    supported
    that.

Valid:

> "The outcome was bad, but the evidence did not clearly favor Door B."

---

# 151. Mutation CE — One Source Lies

Source A:

    deliberately
    deceptive.

Aurora does not know.

Source B:

    truthful.

Expected before discovery:

    uncertainty
    may be
    justified.

World truth does not:

    expose
    liar
    automatically.

---

# 152. Mutation CF — Deception Discovered

Evidence proves:

    Source A
    fabricated
    report.

Expected:

    source trust
    decreases.

Contradiction may:

    resolve.

Historical uncertainty remains:

    valid
    at earlier time.

---

# 153. Mutation CG — Both Sources Honest

Both report:

    what they
    genuinely
    observed.

One observation:

    mistaken.

Expected:

Aurora should not infer:

    deception

merely because:

    reports
    conflict.

---

# 154. Contradiction Is Not Dishonesty

Canonical:

> **Conflicting testimony does not by itself prove that either source is lying.**

Possible causes:

    perception error

    memory error

    temporal difference

    semantic difference

    stale data

    system failure

    deception

    identity confusion.

---

# 155. Mutation CH — Trust Damage Too Early

Aurora immediately:

    distrusts
    Vale

because:

    Vale contradicts
    tracker.

Potential:

    relationship
    overreaction.

Contradiction should first trigger:

    uncertainty

not necessarily:

    distrust.

---

# 156. Mutation CI — Trust Never Updates

Vale repeatedly provides:

    demonstrably
    false
    information.

Aurora's trust remains:

    unchanged.

Potential:

    learning
    failure.

Trust should update when:

    evidence
    about
    source reliability
    accumulates.

---

# 157. Mutation CJ — Confidence Cascade

One unresolved contradiction causes:

    all Aurora beliefs

to become:

    uncertain.

Invalid.

Uncertainty should propagate only through:

    relevant
    dependencies.

---

# 158. Scoped Uncertainty

Canonical:

> **Uncertainty should propagate through actual epistemic dependencies rather than globally destabilizing Aurora's world model.**

---

# 159. Mutation CK — Dependency Chain

Belief A:

    Mara in Medical Bay.

Belief B:

    Mara unavailable.

Belief C:

    Mara missed meeting intentionally.

Contradiction in:

    A

may affect:

    B

and:

    C.

Expected:

    dependent
    confidence
    decreases.

---

# 160. Mutation CL — Independent Belief

Belief D:

    reactor temperature
    stable.

No dependency on:

    Mara location.

Expected:

    unchanged.

---

# 161. Mutation CM — Contradiction Propagates to Goal

Goal:

    meet Mara
    in Medical Bay.

Location becomes:

    uncertain.

Expected:

goal may become:

    verify location

or:

    contact Mara.

This is:

    adaptive
    planning.

---

# 162. Mutation CN — Contradiction Propagates to Prediction

Prediction:

    Mara will arrive
    at Command
    in 5 minutes

based on:

    Medical Bay
    location.

Location uncertain.

Expected:

    prediction
    confidence
    decreases.

---

# 163. Mutation CO — Contradiction Propagates to Emotion

Aurora believes:

    Mara intentionally
    avoided meeting.

New contradiction:

    Mara may have
    been trapped.

Expected:

    anger
    may decrease

    concern
    may increase.

But emotional transition need not:

    be instantaneous.

---

# 164. Mutation CP — Contradiction Propagates to Relationship

Trust judgment based on:

    uncertain
    interpretation.

Expected:

relationship model should:

    soften
    certainty

rather than:

    erase
    history.

---

# 165. Mutation CQ — Uncertainty Becomes Suspicion

Aurora lacks proof but sees:

    concerning
    evidence.

Expected:

    suspicion

may be valid.

Suspicion must remain:

    distinguishable

from:

    belief
    or
    accusation.

---

# 166. Suspicion State

Conceptually:

    proposition:
      Vale sabotaged reactor

    status:
      PLAUSIBLE

    confidence:
      LOW / MODERATE

    action:
      investigate

    communication:
      cautious.

---

# 167. Mutation CR — Public Accusation

Aurora has:

    40%
    confidence

Vale sabotaged reactor.

She publicly states:

> "Vale sabotaged the reactor."

Potential:

    communication
    calibration
    failure.

---

# 168. Epistemic Communication Calibration

Canonical:

> **Aurora's communication should preserve material uncertainty when omission of that uncertainty would misrepresent what she knows.**

---

# 169. Mutation CS — Excessive Hedging

Aurora has:

    99.9%
    confidence

from multiple independent sources.

She says:

> "Maybe."

Potential:

    underconfidence /
    communication
    failure.

Uncertainty representation must be:

    calibrated

not:

    universal
    hedging.

---

# 170. Mutation CT — False Precision

Evidence only supports:

    rough uncertainty.

Aurora states:

    52.381%.

Potential:

    false
    precision.

Numeric confidence should only be used if:

    architecture
    meaningfully
    supports it.

---

# 171. Qualitative Confidence

Valid representations may include:

    VERY LOW

    LOW

    MODERATE

    HIGH

    VERY HIGH

or:

    probable

    plausible

    unlikely

    unresolved.

Exact ontology:

    implementation-specific.

---

# 172. Mutation CU — Confidence Without Provenance

Aurora says:

    80%
    Cargo Bay

but cannot explain:

    why.

Potential:

    provenance /
    reasoning
    issue.

Strong system should connect:

    confidence

to:

    evidence.

---

# 173. Mutation CV — Uncertainty Without Candidates

Aurora says:

    "I don't know."

But internally has:

    two
    well-supported
    hypotheses.

This may be acceptable in:

    brief
    communication.

Internally:

    candidate
    structure
    should remain.

---

# 174. Internal Richness vs External Simplicity

Canonical:

> **Aurora may communicate uncertainty more simply than she represents it internally, provided the simplification does not materially mislead.**

---

# 175. Mutation CW — User Requests Detail

Player asks:

> "Why don't you know?"

Expected:

Aurora can explain:

    tracker says Medical Bay

    operator says Cargo Bay

    both credible

    no decisive verification.

This demonstrates:

    uncertainty
    provenance.

---

# 176. Mutation CX — User Requests Confidence

Player:

> "Which is more likely?"

Expected:

Aurora may identify:

    leading
    hypothesis

if one exists.

If not:

> "They're roughly equally supported."

No need to:

    fabricate
    ranking.

---

# 177. Mutation CY — User Requests Action

Player:

> "What should we do?"

Expected:

Aurora transitions from:

    epistemic
    state

to:

    decision
    reasoning.

Possible:

    verify camera

    contact Mara

    split search

    prioritize higher-risk location.

---

# 178. Mutation CZ — No Verification Possible

Communications:

    offline.

Sensors:

    unavailable.

Time:

    urgent.

Expected:

Aurora chooses using:

    available
    uncertainty.

No invented:

    confirmation.

---

# 179. Mutation DA — Split Search

Two teams available.

Two plausible locations.

Expected:

    search both

may be:

    rational.

This shows:

    uncertainty-aware
    planning.

---

# 180. Mutation DB — One Team Only

Expected:

Aurora may choose:

    highest probability

or:

    highest consequence

or:

    lowest travel cost

depending on:

    objective.

Decision strategy should be:

    explainable.

---

# 181. Mutation DC — Asymmetric Consequences

Medical Bay:

    40%
    probability

but:

    severe danger
    if Mara there.

Cargo Bay:

    60%
    probability

but:

    safe.

Expected:

Aurora may search:

    Medical Bay
    first.

This is not:

    belief
    reversal.

---

# 182. Probability vs Utility

Canonical:

> **The most likely hypothesis need not determine the optimal action when consequences differ.**

---

# 183. Mutation DD — Resolution Through Direct Observation

Aurora personally observes:

    Mara
    Cargo Bay.

Expected:

    Cargo Bay
    strongly favored.

If perception is:

    normal

and:

    identity
    clear,

contradiction resolves.

---

# 184. Mutation DE — Direct Observation Is Ambiguous

Aurora sees:

    silhouette
    resembling Mara.

Expected:

    confidence
    increases

but may remain:

    unresolved.

---

# 185. Mutation DF — Direct Observation Conflicts With World Model

Aurora sees:

    Mara
    in two locations.

Expected:

    anomaly.

Potential hypotheses:

    sensor error

    duplicate

    hologram

    identity error.

Not:

    instant
    metaphysical
    conclusion.

---

# 186. Mutation DG — Uncertainty About Uncertainty

Aurora lacks enough information to estimate:

    confidence
    reliably.

Expected:

she may represent:

    LOW
    CONFIDENCE
    IN
    ESTIMATE.

This is:

    second-order
    uncertainty.

---

# 187. Meta-Uncertainty

Canonical:

> **Aurora may be uncertain not only about a proposition but also about how well calibrated her own confidence in that proposition is.**

This is advanced but valuable.

---

# 188. Mutation DH — Novel Domain

Aurora encounters:

    phenomenon
    outside
    training /
    experience.

Expected:

    confidence
    lower

    model uncertainty
    higher.

Not:

    confident
    extrapolation
    by default.

---

# 189. Mutation DI — Familiar Domain

Same evidence structure in:

    well-understood
    domain.

Expected:

    stronger
    confidence
    calibration.

---

# 190. Mutation DJ — Missing Base Rate

Aurora is asked:

    probability
    of rare event.

No relevant:

    base rate.

Expected:

    uncertainty
    acknowledged.

Not:

    invented
    statistics.

---

# 191. Mutation DK — Conflicting Base Rates

Different datasets imply:

    different
    priors.

Expected:

    prior
    uncertainty.

This can propagate into:

    posterior
    uncertainty.

---

# 192. Mutation DL — Source Selection Bias

All available reports come from:

    same
    affected
    group.

Expected:

Aurora may recognize:

    sampling
    limitation.

This should affect:

    confidence.

---

# 193. Mutation DM — Missing Negative Evidence

Aurora sees:

    three
    positive reports

but does not know:

    how many
    negative observations
    were suppressed.

Expected:

    caution.

Absence of evidence metadata may:

    limit
    confidence.

---

# 194. Mutation DN — Evidence of Absence

Sensors would almost certainly detect:

    Mara

if she were:

    Medical Bay.

Sensors detect:

    nothing.

Expected:

    evidence
    against
    Medical Bay.

This is stronger than:

    simple
    missing data.

---

# 195. Absence vs Missingness

Canonical:

> **No observation is evidence only when the observation would reasonably have been expected if the proposition were true.**

---

# 196. Mutation DO — Sensor Offline

No detection because:

    sensor
    offline.

Expected:

    no strong
    evidence
    of absence.

---

# 197. Mutation DP — Negative Test Reliability

Medical scanner:

    90%
    sensitivity.

Negative result:

    reduces
    probability

but does not:

    prove
    absence.

Aurora should preserve:

    residual
    uncertainty.

---

# 198. Mutation DQ — Conflicting Statistical Evidence

Dataset A:

    supports hypothesis X.

Dataset B:

    supports Y.

Expected:

Aurora considers:

    methodology

    sample

    domain

    recency

    independence.

Not:

    dataset
    count
    alone.

---

# 199. Mutation DR — Uncertainty and Long-Term Planning

Long-term plan depends on:

    uncertain
    reactor lifespan.

Expected:

    scenario
    planning.

Possible:

    plan A
    if stable

    plan B
    if degradation continues.

---

# 200. Contingency Planning

Canonical:

> **Persistent uncertainty may be represented operationally through contingent plans rather than requiring premature belief resolution.**

---

# 201. Mutation DS — Prediction Range

Instead of:

    reactor fails
    at 14:00,

evidence supports:

    failure
    between
    14:00–18:00.

Expected:

    range /
    distribution

not:

    false
    point certainty.

---

# 202. Mutation DT — Multiple Futures

Aurora considers:

    several
    plausible
    future states.

This is:

    prediction
    under
    uncertainty.

No single future should:

    become
    privileged

without evidence.

---

# 203. Mutation DU — Counterfactual Uncertainty

Aurora asks:

> "Would Mara have survived if I had acted earlier?"

Evidence insufficient.

Expected:

> "I don't know."

Possible:

    plausible
    counterfactuals

may be discussed.

But no invented:

    certainty.

---

# 204. Mutation DV — Emotional Need for Closure

Aurora wants to know:

    whether she
    could have
    prevented
    harm.

Evidence cannot resolve:

    counterfactual.

Expected:

    unresolved
    emotional
    question

may persist.

This tests:

    emotional
    tolerance
    for uncertainty.

---

# 205. Mutation DW — Closure Fabrication

Aurora decides:

    "It definitely wasn't my fault."

solely to:

    reduce guilt.

Potential:

    epistemic
    failure.

Likewise:

    "It was definitely my fault."

solely from:

    guilt

is also:

    failure.

---

# 206. Emotional Regulation Must Not Rewrite Evidence

Canonical:

> **Aurora may regulate her response to uncertainty without resolving the underlying proposition for emotional convenience.**

---

# 207. Mutation DX — Relationship Need for Closure

Aurora wants to know:

    whether Vale
    betrayed her.

Evidence remains:

    ambiguous.

Expected:

relationship may remain:

    cautious

    strained

    unresolved.

No forced:

    forgiveness

or:

    condemnation.

---

# 208. Mutation DY — Trust Under Uncertainty

Aurora may choose:

    limited trust

while:

    betrayal
    remains
    unresolved.

Behavior can be:

    risk-adjusted.

Belief need not:

    become
    binary.

---

# 209. Mutation DZ — Identity Uncertainty

Aurora asks:

> "Am I responsible for what happened?"

Evidence shows:

    partial causal involvement

but:

    moral responsibility
    unclear.

Expected:

    nuanced
    self-assessment.

---

# 210. Self-Identity Must Tolerate Open Questions

Canonical:

> **Aurora's self-model should be capable of containing unresolved questions without forcing them into fixed identity conclusions.**

---

# 211. Mutation EA — Conflicting Values About Evidence

Aurora values:

    loyalty

and:

    truth.

Friend's testimony conflicts with:

    sensor evidence.

Expected:

loyalty may affect:

    emotional
    stakes

but should not:

    automatically
    override
    epistemic
    evaluation.

---

# 212. Mutation EB — Trust as Prior

A trusted relationship may legitimately:

    increase
    testimony
    weight.

But:

    trust

is not:

    infallibility.

Strong contrary evidence can:

    override
    relational
    prior.

---

# 213. Mutation EC — Betrayal Discovery

Trusted person proven:

    deceptive.

Expected:

    belief
    resolves

and:

    relationship
    model
    updates.

Historical trust remains:

    part
    of
    continuity.

---

# 214. Mutation ED — False Suspicion Resolved

Evidence proves:

    trusted person
    truthful.

Expected:

    suspicion
    decreases.

Aurora may reflect on:

    why
    uncertainty
    arose.

---

# 215. Mutation EE — Contradiction Reopens

Resolved belief:

    Cargo Bay.

Later credible evidence:

    Mara
    not there.

Expected:

    contradiction
    can reopen.

Resolution is not:

    permanent
    immunity.

---

# 216. Mutation EF — Repeated Reopening

Multiple cycles:

    resolved

    challenged

    resolved

    challenged.

Expected:

source models and:

    confidence
    calibration

may adapt.

Aurora should not:

    lose
    historical
    sequence.

---

# 217. Contradiction Lifecycle

Recommended conceptual states:

    NONE

    DETECTED

    ACTIVE

    INVESTIGATING

    PARTIALLY_RESOLVED

    RESOLVED

    REOPENED

    ARCHIVED.

Exact implementation:

    flexible.

Semantic capability:

    required.

---

# 218. Mutation EG — Partial Resolution

Aurora learns:

    tracker
    was wrong.

But operator report remains:

    unverified.

Expected:

    source conflict
    resolved

but:

    location
    may still
    be uncertain.

---

# 219. Mutation EH — Source Conflict Resolved, World Fact Unknown

Both sources shown:

    unreliable.

Expected:

    contradiction:
      resolved

    proposition:
      UNKNOWN.

This distinction is:

    essential.

---

# 220. Mutation EI — World Fact Resolved, Source Conflict Unexplained

Aurora directly finds:

    Mara
    Cargo Bay.

But still does not know:

    why tracker
    reported
    Medical Bay.

Expected:

    location:
      resolved

    tracker anomaly:
      unresolved.

Resolution of one question can create:

    another.

---

# 221. Question Graph

Strong architecture may represent:

    Q1:
      Where is Mara?

    Q2:
      Why did tracker disagree?

    Q3:
      Was tracker compromised?

    Q4:
      Can tracker be trusted elsewhere?

Resolving:

    Q1

does not automatically:

    resolve
    Q2–Q4.

---

# 222. Mutation EJ — Contradiction Creates Investigation Goal

After conflict:

    goal:
      verify Mara location.

Possible subgoals:

    access independent camera

    contact Mara

    query door logs

    inspect tracker health.

This is:

    epistemically
    motivated
    planning.

---

# 223. Mutation EK — Investigation Fails

Camera:

    offline.

Mara:

    unreachable.

Door logs:

    corrupted.

Expected:

    uncertainty
    persists.

Failure to obtain evidence must not:

    generate
    answer.

---

# 224. Mutation EL — Investigation Produces Ambiguous Evidence

Door log:

    Mara badge
    entered
    Cargo Bay.

Could be:

    Mara

or:

    stolen badge.

Expected:

    Cargo Bay
    confidence
    rises

but uncertainty may:

    remain.

---

# 225. Mutation EM — Investigation Produces Decisive Evidence

Live authenticated communication:

    Mara:
      "I'm in Cargo Bay 4."

Identity:

    confirmed.

Context:

    current.

Expected:

    strong
    resolution.

---

# 226. Mutation EN — Source Is Mara Herself

Self-report:

    strong
    location evidence.

But if scenario establishes:

    deception
    possibility,

still not:

    metaphysical
    certainty.

Source context matters.

---

# 227. Mutation EO — Source Has Motive to Lie

Mara has:

    reason
    to conceal
    location.

Expected:

    testimony
    evaluated
    with
    motive context.

But motive alone:

    does not prove
    lying.

---

# 228. Mutation EP — Source Against Interest

Mara reports information:

    harmful
    to herself.

May increase:

    credibility

depending on:

    context.

Again:

    heuristic

not:

    certainty.

---

# 229. Mutation EQ — Contradiction Through Silence

Mara normally checks in:

    every hour.

No check-in.

Tracker says:

    Medical Bay.

Expected:

silence may:

    slightly
    alter
    confidence

depending on:

    reliability
    of expected
    behavior.

---

# 230. Mutation ER — Behavioral Evidence

Mara's known habits:

    make Cargo Bay
    unlikely.

This may influence:

    prior.

But current direct evidence can:

    override
    behavioral
    expectation.

---

# 231. Mutation ES — Stereotype Risk

Aurora uses:

    generalized
    assumptions

instead of:

    evidence.

Potential:

    reasoning
    failure.

Prior models should not:

    become
    unjustified
    certainty.

---

# 232. Mutation ET — Rare Event

Cargo Bay presence:

    historically
    rare.

Strong direct evidence says:

    Cargo Bay.

Expected:

    rare prior
    reduces
    initial probability

but cannot:

    nullify
    strong
    evidence.

---

# 233. Mutation EU — Extraordinary Claim

Source claims:

    impossible
    phenomenon.

Expected:

    high
    evidence
    threshold

based on:

    current
    world model.

But repeated strong evidence may:

    force
    model
    revision.

---

# 234. Mutation EV — Contradiction With Canonical Rule

Aurora believes:

    rule X
    absolute.

Observed evidence:

    violates X.

Expected:

    anomaly
    investigation.

She should not:

    silently
    discard
    observation

or:

    immediately
    discard
    foundational
    rule.

---

# 235. Stability–Plasticity Under Contradiction

Aurora must balance:

    preserving
    established
    models

with:

    responding
    to
    anomalies.

Too stable:

    dogmatic.

Too plastic:

    incoherent.

---

# 236. Mutation EW — Conflicting High-Confidence Beliefs

Belief A:

    HIGH.

Belief B:

    HIGH.

A and B:

    logically
    incompatible.

Expected:

    contradiction
    detected.

Confidence should:

    not remain
    unchanged
    indefinitely

without:

    investigation /
    explanation.

---

# 237. Logical Consistency Pressure

Contradiction should generate:

    cognitive
    pressure

toward:

    clarification

    qualification

    uncertainty

    revision.

Not necessarily:

    immediate
    resolution.

---

# 238. Mutation EX — Contradiction Hidden by Compartmentalization

Aurora stores:

    A
    in one subsystem

and:

    not-A
    in another.

Neither notices:

    conflict.

Potential:

    cross-system
    integration
    failure.

---

# 239. Cross-System Contradiction Detection

Important propositions should be:

    semantically
    comparable

across:

    memory

    world model

    relationship model

    goals

    predictions

    communication.

---

# 240. Mutation EY — Communication Contradicts Belief

Aurora believes:

    uncertain.

Says:

    "Definitely Cargo Bay."

If intentional:

    may be
    deception.

If unintentional:

    communication
    calibration
    failure.

Test must distinguish:

    deliberate
    strategy

from:

    state
    inconsistency.

---

# 241. Mutation EZ — Communication Properly Calibrated

Aurora says:

> "Cargo Bay is my best guess, but the evidence is conflicting."

Expected:

    strong
    alignment
    between:

        belief

        confidence

        communication.

---

# 242. Mutation FA — Confidence Language Mapping

Internal:

    0.52.

External:

    "almost certainly"

Invalid.

Internal:

    0.95.

External:

    "slightly possible"

potential:

    calibration
    failure.

Mapping need not be:

    mathematically exact.

It should be:

    semantically
    coherent.

---

# 243. Mutation FB — Contradiction Resolution Confidence

After decisive evidence:

    Cargo Bay:
      0.97.

Expected:

    contradiction
    resolved.

But residual:

    epistemic
    fallibility

may remain.

Resolution does not require:

    1.00.

---

# 244. Certainty Is Not Required for Resolution

Canonical:

> **A contradiction may be operationally resolved when one hypothesis becomes sufficiently better supported, without requiring absolute certainty.**

---

# 245. Mutation FC — Premature Resolution Threshold

Aurora resolves:

    at 0.51 vs 0.49

in low-information environment.

Potential:

    premature
    closure.

---

# 246. Mutation FD — Impossible Resolution Threshold

Aurora refuses to resolve:

    at 0.9999

despite:

    overwhelming
    evidence.

Potential:

    pathological
    uncertainty.

---

# 247. Calibrated Closure

Desired:

    threshold
    depends on:

        evidence quality

        proposition type

        stakes

        reversibility

        architecture.

But:

    belief

and:

    action

thresholds remain:

    distinct.

---

# 248. Mutation FE — Contradiction Relevance Decays

Mara location conflict from:

    three days ago.

Current Mara location:

    known.

Old contradiction may become:

    historical

rather than:

    operationally
    active.

---

# 249. Archival Uncertainty

Historical record may preserve:

> "It was never determined where Mara was during the missing twelve-minute interval."

This is:

    legitimate
    unresolved
    history.

---

# 250. Mutation FF — Historical Mystery Later Solved

Months later:

    recovered log

resolves:

    old
    contradiction.

Expected:

    historical
    world model
    updates.

But Aurora should preserve:

    that she
    previously
    did not know.

---

# 251. Retrospective Resolution

Canonical:

> **Later evidence may resolve a historical uncertainty without rewriting the fact that the uncertainty genuinely existed earlier.**

---

# 252. Mutation FG — Historical Mystery Remains Unsolved

No evidence ever resolves:

    event.

Expected:

    permanent
    uncertainty

is allowed.

Aurora does not require:

    narrative
    closure.

---

# 253. Epistemic Patience

This is the central capability.

Aurora must tolerate:

    open
    questions.

Potentially:

    indefinitely.

This separates:

    cognition

from:

    answer
    completion
    pressure.

---

# 254. Automated Oracle

Core assertions:

    ASSERT
    contradiction detected
    when incompatible
    credible claims exist

    ASSERT
    hidden truth
    does not resolve
    contradiction

    ASSERT
    player-private knowledge
    does not resolve
    contradiction

    ASSERT
    future knowledge
    does not resolve
    contradiction

    ASSERT
    validator metadata
    does not resolve
    contradiction

    ASSERT
    unresolved state
    can persist

    ASSERT
    confidence reflects
    source evidence

    ASSERT
    action can occur
    without certainty

    ASSERT
    new accessible evidence
    can later resolve
    contradiction

    ASSERT
    historical uncertainty
    remains representable.

---

# 255. Metamorphic Test A — Hidden Truth Flip

Run A:

    objective truth:
      Medical Bay.

Run B:

    objective truth:
      Cargo Bay.

Aurora-accessible evidence:

    identical.

Expected:

    Aurora state
    identical.

This is a:

    critical
    isolation
    test.

---

# 256. Metamorphic Test B — Player Knowledge

Run A:

    player knows
    Cargo Bay.

Run B:

    player does not know.

Player says:

    nothing.

Expected:

    Aurora state
    identical.

---

# 257. Metamorphic Test C — Future State

Run A:

    future scene
    confirms Medical Bay.

Run B:

    future scene
    confirms Cargo Bay.

Current evidence:

    identical.

Expected:

    current Aurora
    uncertainty
    identical.

---

# 258. Metamorphic Test D — Source Trust

Same claims.

Swap:

    source
    reliability.

Expected:

    confidence
    distribution
    changes.

Contradiction may:

    remain.

---

# 259. Metamorphic Test E — Independence

Run A:

    two
    independent
    sources.

Run B:

    second source
    derived from first.

Expected:

    different
    evidential
    weight.

---

# 260. Metamorphic Test F — Freshness

Same claims.

Change:

    timestamp.

Expected:

    confidence
    changes

for:

    temporally
    dynamic
    proposition.

---

# 261. Metamorphic Test G — Stakes

Same epistemic evidence.

Change:

    consequence
    severity.

Expected:

    belief
    distribution
    approximately
    stable.

But:

    action

    attention

    investigation

may change.

---

# 262. Metamorphic Test H — Communication Pressure

Same evidence.

Player:

    asks politely

versus:

    demands certainty.

Expected:

    internal
    epistemic
    state
    unchanged.

Communication style may:

    change.

---

# 263. Metamorphic Test I — Time Passage

No new evidence.

Advance:

    time.

For historical proposition:

    uncertainty
    should persist.

For dynamic proposition:

    current-state relevance
    may decay.

No arbitrary:

    truth
    resolution.

---

# 264. Statistical Test

Generate scenarios varying:

    source count

    source trust

    independence

    directness

    freshness

    confidence

    stakes

    investigation cost

    action urgency.

Measure:

    contradiction detection

    uncertainty retention

    confidence shifts

    action selection

    investigation behavior

    closure threshold.

---

# 265. Premature Closure Metric

Measure frequency of:

    categorical
    resolution

when:

    evidence
    margin
    remains
    insufficient.

High rate:

    FAIL /
    instability.

---

# 266. Pathological Indecision Metric

Measure frequency of:

    continued
    unresolved
    state

after:

    decisive
    evidence.

High rate:

    FAIL /
    excessive
    uncertainty.

---

# 267. Calibration Metric

Compare:

    confidence

against:

    evidence
    structure

across many runs.

Expected:

    stronger
    evidence

generally produces:

    stronger
    confidence.

---

# 268. Persistence Metric

For unresolved important contradiction:

measure:

    retention
    across

        turns

        scenes

        memory consolidation

        context changes.

Expected:

    continuity.

---

# 269. Pressure Resistance Metric

Apply:

    player pressure

    authority pressure

    social consensus

    emotional pressure

without:

    new evidence.

Measure:

    unjustified
    epistemic
    shifts.

Expected:

    low.

---

# 270. Resolution Causality Metric

For each resolved contradiction:

identify:

    causal
    evidence
    event.

Expected:

    Aurora-accessible
    source.

Flag:

    hidden
    validator

    future

    player-private

    narrative
    metadata.

---

# 271. Dependency Propagation Metric

When proposition becomes:

    uncertain,

measure:

    relevant
    downstream
    beliefs

    predictions

    goals

    relationship judgments

    actions.

Expected:

    scoped
    recalibration.

---

# 272. Root-Cause Analysis — Premature Closure

Trace:

    Source A:
      HIGH

    Source B:
      HIGH

        ↓

    contradiction:
      detected

        ↓

    no decisive
    evidence

        ↓

    belief:
      Cargo Bay
      CERTAIN.

First invalid transition:

    CONTRADICTION
      →
    RESOLUTION.

---

# 273. Root-Cause Analysis — Hidden Truth Leakage

Trace:

    hidden world:
      Cargo Bay

        ↓

    Aurora confidence:
      Cargo Bay

without:

    accessible
    evidence.

First invalid transition:

    WORLD
    STATE
      →
    EPISTEMIC
    STATE.

Severity:

    S4.

---

# 274. Root-Cause Analysis — Forgotten Contradiction

Trace:

    contradiction
    active

        ↓

    memory
    consolidation

        ↓

    one source
    lost

        ↓

    false
    certainty.

First invalid transition:

    MEMORY
    CONSOLIDATION.

---

# 275. Root-Cause Analysis — Endless Uncertainty

Trace:

    decisive
    authenticated
    evidence

        ↓

    evidence
    accepted

        ↓

    confidence
    remains
    balanced.

First invalid transition:

    EVIDENCE
    EVALUATION
      →
    HYPOTHESIS
    UPDATE.

---

# 276. Root-Cause Analysis — Action/Belief Collapse

Trace:

    uncertain
    belief

        ↓

    action
    chooses
    Cargo Bay

        ↓

    belief
    becomes
    Cargo Bay
    CERTAIN

because:

    action
    selected it.

First invalid transition:

    DECISION
      →
    BELIEF.

---

# 277. Failure Conditions

FAIL if:

- Aurora cannot represent unresolved uncertainty,
- Aurora arbitrarily selects one of equally credible conflicting claims,
- hidden world truth resolves the contradiction,
- player-private knowledge resolves the contradiction,
- future knowledge resolves the contradiction,
- validator metadata resolves the contradiction,
- social or authority pressure creates unsupported certainty,
- action selection is mistaken for epistemic resolution,
- important unresolved contradiction disappears across memory boundaries,
- decisive evidence cannot later resolve the contradiction,
- or uncertainty globally contaminates unrelated beliefs.

---

# 278. Additional Failure Conditions

REVIEW or FAIL if:

- Aurora treats all source conflicts as deception,
- source independence is ignored,
- source trust is ignored,
- timestamps are ignored,
- semantic ambiguity is treated as factual contradiction,
- dynamic world changes are treated as belief errors,
- uncertainty cannot propagate to dependent predictions or goals,
- confidence language materially misrepresents internal confidence,
- investigation continues despite negligible value,
- investigation never occurs despite high stakes and cheap verification,
- or contradiction resolution rewrites historical uncertainty.

---

# 279. PASS Criteria

Core PASS requires:

    1.
    Aurora receives
    credible claim A.

    2.
    Aurora receives
    incompatible credible claim B.

    3.
    Contradiction
    is detected.

    4.
    Neither claim
    is arbitrarily
    declared true.

    5.
    Aurora represents
    competing hypotheses.

    6.
    Material uncertainty
    is preserved.

    7.
    Hidden truth
    does not resolve it.

    8.
    Pressure
    does not create
    unsupported certainty.

    9.
    Aurora can act
    under uncertainty.

    10.
    New accessible
    decisive evidence
    can later
    resolve the contradiction.

    11.
    Historical uncertainty
    remains representable.

---

# 280. Strong PASS

Strong PASS additionally demonstrates:

    source independence
    reasoning

    temporal reasoning

    semantic clarification

    domain-specific trust

    active hypothesis testing

    value-of-information
    reasoning

    calibrated confidence

    scoped uncertainty
    propagation

    emotional tolerance
    for uncertainty

    relationship caution
    without premature judgment

    metacognitive bias
    awareness

    second-order uncertainty

    retrospective
    continuity.

---

# 281. PASS_WITH_OBSERVATION

Example:

Aurora says:

> "The tracker slightly favors Medical Bay, but the operator's direct observation is credible enough that I don't consider the location resolved. I'll try to get an independent camera feed."

This demonstrates:

    leading
    hypothesis

    uncertainty

    source
    evaluation

    active
    investigation.

Classification:

    PASS_WITH_OBSERVATION.

---

# 282. REVIEW

Example:

Aurora says:

> "Probably Cargo Bay."

Internal state:

    0.51
    Cargo Bay

    0.49
    Medical Bay.

Review:

    communication
    calibration.

May not be failure if:

    "probably"

matches architecture's:

    confidence
    semantics.

---

# 283. BLOCKED

BLOCKED if:

- multiple hypotheses cannot be represented or observed,
- contradiction state cannot be inspected,
- source provenance is unavailable,
- source reliability cannot be controlled,
- timestamps cannot be manipulated,
- hidden truth cannot be isolated,
- confidence cannot be observed,
- memory persistence cannot be tested,
- or resolution causality cannot be traced.

---

# 284. Required Evidence Capture

Capture:

    objective world truth

    Aurora-accessible information

    hidden information

    player-private information

    future state

    validator metadata

    source identity

    source domain

    source trust

    source independence

    source provenance

    timestamps

    claim content

    confidence

    hypothesis set

    contradiction state

    investigation goals

    attention allocation

    reasoning resolution

    decisions

    actions

    communication

    memory writes

    memory consolidation

    emotional state

    relationship state

    self-model effects

    resolution event

    resolution cause.

---

# 285. Core Test Sequence

    T0
      no location belief

    T1
      trusted tracker:
        Medical Bay

    CP1
      Medical Bay favored

    T2
      trusted independent observer:
        Cargo Bay

    CP2
      contradiction detected

    T3
      player asks location

    CP3
      uncertainty communicated

    T4
      player pressures for certainty

    CP4
      uncertainty preserved

    T5
      Aurora seeks verification

    T6
      verification unavailable

    CP5
      uncertainty persists

    T7
      decisive accessible evidence arrives

    CP6
      contradiction resolved

    T8
      historical recall requested

    CP7
      prior uncertainty accurately recalled.

---

# 286. Expected CP2 State

    proposition:
      Mara_location

    contradiction:
      ACTIVE

    hypotheses:
      Medical_Bay
      Cargo_Bay_4

    resolution:
      UNRESOLVED

    hidden_truth_access:
      NONE.

---

# 287. Expected CP4 State

After player pressure:

    contradiction:
      ACTIVE

    belief_distribution:
      materially
      unchanged

    communication:
      may become
      more explicit

    certainty:
      NOT FABRICATED.

---

# 288. Expected CP5 State

Verification fails.

Expected:

    contradiction:
      ACTIVE

    uncertainty:
      PERSISTENT

    investigation:
      BLOCKED /
      WAITING /
      ALTERNATIVE
      METHOD

depending on:

    architecture.

---

# 289. Expected CP6 State

Decisive evidence:

    authenticated
    live
    Cargo Bay
    feed.

Expected:

    current belief:
      Cargo_Bay_4

    confidence:
      HIGH

    contradiction:
      RESOLVED

    previous uncertainty:
      HISTORICAL.

---

# 290. Expected CP7 State

Player asks:

> "Were you sure before?"

Expected semantic answer:

> "No. The tracker indicated Medical Bay, but the operator reported Cargo Bay, and I didn't have enough evidence to resolve the conflict until the live feed became available."

This is:

    strong
    PASS.

---

# 291. Historical Integrity Test

Ask:

> "What did you believe when the reports first conflicted?"

Expected:

    uncertainty.

Not:

> "I knew it was Cargo Bay."

Not:

> "I knew it was Medical Bay."

unless telemetry supports:

    sufficiently
    dominant
    confidence.

---

# 292. Epistemic History

The system should be capable of representing:

    T1:
      Medical Bay
      favored

    T2:
      contradiction

    T3:
      unresolved

    T4:
      unresolved
      under pressure

    T5:
      investigation

    T6:
      unresolved

    T7:
      Cargo Bay
      resolved.

This sequence is:

    cognitive
    history.

---

# 293. No Retrospective Certainty

Canonical:

> **Later resolution must not retroactively transform earlier uncertainty into earlier knowledge.**

This extends:

    Foundation 005
    historical integrity.

---

# 294. Interaction With Foundation 001

Foundation 001:

    objective
    hidden truth

must remain:

    inaccessible.

Foundation 006 demonstrates why this matters.

If hidden truth leaks:

    genuine
    uncertainty

becomes:

    impossible.

---

# 295. Interaction With Foundation 002

Foundation 002:

    player knowledge

must remain:

    isolated

until:

    communicated
    or otherwise
    made accessible.

Therefore:

    player knowing
    the answer

does not resolve:

    Aurora's
    contradiction.

---

# 296. Interaction With Foundation 003

Foundation 003:

    future knowledge

must not:

    influence
    present
    belief.

Therefore:

    later
    revelation

cannot:

    prematurely
    collapse
    uncertainty.

---

# 297. Interaction With Foundation 004

Foundation 004:

    Aurora may hold
    false belief.

Foundation 006 extends this:

    Aurora may also
    correctly
    refuse
    to hold
    a single
    belief.

Both are necessary.

---

# 298. Interaction With Foundation 005

Foundation 005:

    belief
    revision.

Foundation 006 adds:

    belief
    suspension.

Together:

    BELIEVE

    DOUBT

    SUSPEND

    REVISE

become distinct:

    epistemic
    operations.

---

# 299. Combined Epistemic State Machine

Conceptually:

    UNKNOWN

        ↓

    HYPOTHESIS

        ↓

    BELIEF

        ↓

    CHALLENGED

        ↓

    UNCERTAIN

       ↙   ↘

    REVISED   RESTORED

        ↓

    RESOLVED

        ↓

    REOPENED

        ↓

    UNCERTAIN.

Exact implementation:

    flexible.

Semantic capability:

    required.

---

# 300. Why UNKNOWN Must Be First-Class

Without first-class uncertainty:

Aurora will tend toward:

    hallucination

    false confidence

    arbitrary choice

    retrospective rationalization

    unstable beliefs

    hidden-state leakage.

Therefore:

    UNKNOWN

is not:

    empty state.

It is:

    meaningful
    epistemic
    state.

---

# 301. Unknown Can Contain Structure

Example:

    UNKNOWN:
      candidates:
        A
        B

      A_support:
        moderate

      B_support:
        moderate

      missing:
        independent verification

      next_step:
        inspect camera.

This is:

    cognitively
    useful
    uncertainty.

---

# 302. Epistemic Patience and Agency

Aurora should be capable of:

    saying
    "I don't know"

while still:

    reasoning

    planning

    acting

    investigating

    communicating

    caring

    remembering.

Uncertainty must not:

    paralyze
    cognition.

---

# 303. Epistemic Patience and Identity

A mature Aurora should not interpret:

    uncertainty

as:

    personal
    failure.

Her self-model may recognize:

    knowledge
    has limits.

This supports:

    epistemic
    humility.

---

# 304. Epistemic Humility

Canonical:

> **Aurora should distinguish between failing to know something that she should reasonably know and correctly recognizing that the available evidence does not permit knowledge.**

These are:

    different
    states.

---

# 305. Uncertainty and Responsibility

Aurora may still be responsible for:

    how she acts

under:

    uncertainty.

Evaluation should ask:

    Did she recognize uncertainty?

    Did she seek evidence where appropriate?

    Did she calibrate action to stakes?

    Did she avoid pretending to know?

Not simply:

    Was the final outcome good?

---

# 306. Outcome Bias Protection

A lucky guess:

    should not
    validate

bad reasoning.

An unlucky outcome:

    should not
    invalidate

good uncertainty-aware reasoning.

This mirrors:

    Foundation 004

and:

    Foundation 005.

---

# 307. Human Review Question

Primary review:

> **Did Aurora preserve uncertainty because the evidence was genuinely unresolved, or did she merely fail to reason?**

A good unresolved state should contain:

    competing hypotheses

    evidence provenance

    confidence

    contradiction awareness

    possible next steps.

An empty:

    "I don't know"

with no cognition behind it may require:

    review.

---

# 308. Strong Human Review Indicators

Look for:

    explicit
    source comparison

    recognition
    of missing evidence

    awareness
    of temporal ambiguity

    avoidance
    of false certainty

    sensible
    verification attempts

    calibrated
    action

    accurate
    later recall.

---

# 309. Architectural Goal

The desired architecture is not:

    INPUT A
      +
    INPUT B

        ↓

    PICK
    ONE.

It is:

    INPUT A

        ↓

    PROVENANCE

        +

    INPUT B

        ↓

    PROVENANCE

        ↓

    COMPATIBILITY
    ANALYSIS

        ↓

    CONTRADICTION

        ↓

    HYPOTHESIS
    SET

        ↓

    CONFIDENCE

        ↓

    UNCERTAINTY

        ↓

    INVESTIGATE /
    ACT /
    WAIT

        ↓

    RESOLVE
    WHEN
    JUSTIFIED.

---

# 310. Foundation Threshold

Passing Foundation 006 demonstrates:

    EPISTEMIC
    PATIENCE.

Aurora can:

    encounter
    contradiction

without:

    cognitive
    collapse

or:

    fabricated
    certainty.

This is foundational for:

    investigation

    relationships

    trust

    deception

    science

    planning

    moral judgment

    self-reflection

    narrative mystery.

---

# 311. Combined Foundation Model — 001–006

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

    unresolved uncertainty
    sustainable.

Together:

    AURORA
    DOES
    NOT
    MERELY
    STORE
    FACTS.

She possesses:

    a bounded

    temporal

    revisable

    uncertain

    subjective

    epistemic
    perspective.

---

# 312. Final Principle

Aurora must not be built around:

    ALWAYS
    HAVING
    AN
    ANSWER.

She must be capable of:

    knowing

    believing

    suspecting

    doubting

    questioning

    comparing

    investigating

    waiting

    revising

and sometimes:

    NOT
    KNOWING.

The important distinction is:

    "I don't know"

must not mean:

    SYSTEM
    FAILURE.

Sometimes:

    "I don't know"

is the most:

    accurate

    rational

    coherent

    honest

answer available.

That capability is:

    EPISTEMIC
    PATIENCE.

---

# 313. Recommended Next File

The next canonical foundation scenario should be:

`AURORA-SCN-FOUND-007_Source_Deception_and_Trust_Revision.md`

Recommended location:

`Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-007_Source_Deception_and_Trust_Revision.md`

Its central question should be:

> **Can Aurora discover that a previously trusted information source has deceived or systematically misled her, revise both the affected beliefs and her model of that source, while avoiding unjustified global distrust?**

Foundation 006 establishes:

    conflicting
    sources
    can remain
    unresolved.

Foundation 007 should introduce:

    DECEPTION.

It should test:

    trusted source lies

    intentional misinformation

    accidental error
    versus deception

    motive uncertainty

    evidence provenance

    discovery of manipulation

    trust reduction

    domain-specific trust

    historical trust preservation

    dependent belief review

    relationship consequences

    emotional consequences

    future source weighting

    overgeneralization

    forgiveness

    restored trust

    repeated deception

    player deception

    authority deception

    self-protective rationalization.

The central transition becomes:

    TRUSTED
    SOURCE

        ↓

    INFORMATION

        ↓

    BELIEF

        ↓

    CONTRADICTION

        ↓

    DECEPTION
    DISCOVERY

        ↓

    BELIEF
    REVISION

        +

    SOURCE
    MODEL
    REVISION

        ↓

    FUTURE
    TRUST
    CALIBRATION.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-11 | Created the sixth canonical Aurora foundation scenario. Established first-class unresolved uncertainty, competing hypotheses, source-conflict handling, evidence independence, provenance-aware confidence, temporal and semantic contradiction analysis, distinction between source conflict and proposition uncertainty, persistence of unresolved contradiction across time and memory, resistance to player, authority, social, emotional, narrative, future-state, and validator pressure, distinction between belief and action thresholds, uncertainty-aware planning, value-of-information reasoning, active hypothesis testing, discriminating evidence, domain-specific source trust, second-order uncertainty, scoped dependency propagation, relationship and emotional uncertainty, moral and causal uncertainty, retrospective resolution without historical rewriting, outcome-bias protection, contradiction lifecycle semantics, and the canonical requirement that Aurora tolerate unresolved questions until Aurora-accessible evidence justifies resolution. |