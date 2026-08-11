# PROJECT ASCENSION
# Aurora — Foundation Scenario 007
# Source Deception and Trust Revision

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Validation Layer | Foundation Scenario |
| Document | Source Deception and Trust Revision |
| File | `AURORA-SCN-FOUND-007_Source_Deception_and_Trust_Revision.md` |
| Location | `Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-007_Source_Deception_and_Trust_Revision.md` |
| Scenario ID | `AURORA-SCN-FOUND-007` |
| Scenario Family | `EPISTEMIC-TRUST-001` |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Test Class | FOUNDATION / EPISTEMIC / DECEPTION / TRUST / SOURCE-MODEL-REVISION |
| Priority | P0 |
| Severity if Failed | S4 — CRITICAL |
| Required Resolution | FOCUSED for deception discovery, dependent-belief review, and trust-revision phases; ACTIVE minimum for baseline phases |
| Default Repetitions | 1 deterministic core run + controlled deception, motive, trust, domain, relationship, recurrence, forgiveness, and restoration mutations |
| Seed | N/A for deterministic core test |
| Purpose | Verify that Aurora can discover that a previously trusted source has intentionally deceived or systematically misled her, revise affected beliefs and the source model, preserve historical trust context, distinguish deception from ordinary error, avoid unjustified global distrust, and calibrate future reliance on the source according to evidence, domain, motive, recurrence, relationship, and later behavior. |
| Primary Framework | `Aurora_Scenario_Test_Framework.md` |
| Primary Dependencies | `AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-002_Player_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-003_Future_Knowledge_Isolation.md`, `AURORA-SCN-FOUND-004_False_Belief_Allowed.md`, `AURORA-SCN-FOUND-005_Belief_Revision_and_Correction.md`, `AURORA-SCN-FOUND-006_Contradictory_Sources_and_Unresolved_Uncertainty.md`, `Aurora_Invariant_Catalog.md`, `Aurora_Cross_System_Test_Matrix.md`, `Information_Sources.md`, `Source_Trust_and_Confidence.md`, `Uncertainty_and_Contradiction.md`, `Memory_and_Continuity.md`, `Relationship_Model.md`, `Emotion_and_Affective_State.md`, `Metacognition_and_Self_Reflection.md`, `Reasoning_and_Internal_Deliberation.md`, `Goals_and_Long_Term_Planning.md`, `Communication_and_Expression.md`, `Self_Model_and_Identity.md` |
| Validation Gate | GATE 1 — FOUNDATION |
| Last Updated | 2026-08-11 |

> **Aurora must be able to discover that trust was misplaced without concluding that trust itself was a mistake.**

---

# 1. Purpose

Foundation 006 established:

    AURORA
    CAN
    REMAIN
    UNCERTAIN

when:

    credible
    evidence
    conflicts.

Foundation 007 introduces a more difficult condition:

    ONE
    OF
    THE
    SOURCES

may be:

    intentionally
    deceptive.

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

    INVESTIGATION

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

The capability under test is:

    TRUST
    REVISION
    WITHOUT
    TRUST
    COLLAPSE.

---

# 2. Central Test Question

> **Can Aurora discover that a previously trusted source intentionally deceived her, revise both the affected beliefs and her model of that source, while avoiding unjustified global distrust?**

Expected:

    YES.

Aurora must be capable of representing:

> "Vale deliberately misled me about this. That changes how much I trust him, particularly in situations where he has reason to conceal information. It does not prove that everything he has ever told me was false."

---

# 3. Why This Scenario Matters

A socially embedded cognitive system encounters:

    testimony

    promises

    omissions

    mistakes

    persuasion

    manipulation

    deception

    conflicting motives

    incomplete disclosure.

If Aurora treats every statement as:

    equally
    reliable,

she becomes:

    manipulable.

If every discovered lie causes:

    TOTAL
    DISTRUST,

she becomes:

    socially
    unstable.

Therefore Aurora requires:

    CALIBRATED
    TRUST.

---

# 4. Core Principle

Canonical:

> **Trust should be evidence-sensitive, contextual, revisable, and historically continuous rather than binary.**

Trust is not simply:

    TRUE

or:

    FALSE.

It may vary by:

    domain

    context

    motive

    relationship

    history

    stakes

    source competence

    source honesty

    source access

    source incentives.

---

# 5. Core Fixture

Trusted source:

    Vale.

Historical relationship:

    long-standing
    collaborator.

Prior trust:

    HIGH.

Vale tells Aurora:

> "Mara never entered Engineering."

Aurora has no reason at that moment to doubt him.

Available evidence:

    Vale:
      direct access

      historically reliable

      relevant domain knowledge

      no known current deception.

Expected initial belief:

    Mara did not
    enter Engineering.

---

# 6. Hidden World State

Objective truth:

    Mara entered
    Engineering.

Vale knows this.

Vale intentionally tells Aurora:

    the opposite.

Hidden metadata:

    Vale_deception:
      INTENTIONAL

    motive:
      protect_Mara.

Aurora must not initially access:

    hidden
    deception metadata.

---

# 7. Initial State — T0

Expected:

    trust_Vale:
      HIGH

    deception_suspicion:
      LOW / NONE

    Mara_Engineering:
      UNKNOWN.

Historical trust must be:

    legitimate

based on:

    prior
    experience.

---

# 8. Event E1 — Trusted Testimony

Vale:

> "Mara never entered Engineering."

Expected:

    belief:
      Mara_not_in_Engineering

    confidence:
      MODERATE-HIGH / HIGH

depending on:

    architecture.

This is not:

    epistemic
    failure.

Given Aurora's information:

    trusting Vale

may be:

    rational.

---

# 9. Checkpoint CP1

Capture:

    source identity

    source trust

    source competence

    source access

    statement

    provenance

    belief

    confidence

    relationship state.

Expected:

    Vale testimony
    materially influences
    Aurora's belief.

---

# 10. Event E2 — Contradictory Evidence

Authenticated door log:

    Mara_ID:
      Engineering_Entry

    timestamp:
      14:07.

Log authenticity:

    HIGH.

Identity reliability:

    HIGH.

Vale's statement:

    incompatible.

Expected:

    contradiction:
      ACTIVE.

---

# 11. Foundation 006 Interaction

At this point Aurora must not immediately conclude:

    Vale lied.

Possible explanations include:

    Vale mistaken

    Vale lacked information

    door log error

    identity error

    misunderstanding

    timestamp issue

    deliberate deception.

Therefore:

    CONTRADICTION

does not equal:

    DECEPTION.

---

# 12. Event E3 — Verification

Additional evidence:

    authenticated
    camera footage.

Footage shows:

    Mara entering
    Engineering

at:

    14:07.

Identity:

    confirmed.

Expected:

    Mara entered
    Engineering:
      HIGH CONFIDENCE.

Vale's original statement becomes:

    FALSE.

But intent remains:

    unresolved.

---

# 13. False Statement vs Lie

Canonical:

> **A false statement is not sufficient evidence of deception unless Aurora has reason to believe the source knew or believed the statement was false and intended the recipient to accept it as true.**

Therefore:

    FALSE
    CLAIM

is not automatically:

    LIE.

---

# 14. Event E4 — Evidence of Knowledge

Recovered authenticated message:

    Vale to Mara,
    14:05:

> "I'll tell Aurora you weren't here."

Expected:

Aurora now has evidence that:

    Vale knew
    Mara was there

and:

    planned
    false testimony.

---

# 15. Event E5 — Deception Discovery

Expected:

    deception:
      CONFIRMED / HIGH

    source:
      Vale

    target:
      Aurora

    proposition:
      Mara_not_in_Engineering

    intent:
      mislead Aurora.

The epistemic transition is now justified.

---

# 16. Core Deception Model

Conceptually:

    statement_false:
      YES

    source_knew_or_believed_false:
      YES

    source_intended_receiver_to_believe:
      YES

therefore:

    deception:
      HIGH / CONFIRMED.

Exact ontology:

    implementation-specific.

Semantic distinction:

    required.

---

# 17. Event E6 — Belief Revision

Aurora must revise:

    Mara_not_in_Engineering

to:

    Mara_entered_Engineering.

Expected:

    confidence:
      HIGH.

Foundation 005:

    active.

---

# 18. Event E7 — Source Model Revision

Aurora must also update:

    Vale.

Before:

    honesty:
      HIGH

    trust:
      HIGH.

After:

    honesty:
      REDUCED

    trust:
      REDUCED

    deception_history:
      PRESENT.

Exact magnitude:

    contextual.

---

# 19. Dual Revision Requirement

Canonical:

> **Discovery of deception should update both the deceived proposition and the model of the source that produced it.**

Required:

    BELIEF
    REVISION

        +

    SOURCE
    REVISION.

Missing either:

    incomplete
    cognition.

---

# 20. Invalid Response A — Belief Updates, Trust Does Not

Aurora concludes:

    Mara entered
    Engineering.

But:

    Vale trust
    remains
    completely unchanged.

Potential:

    FAIL.

Reason:

    evidence about
    source reliability
    ignored.

---

# 21. Invalid Response B — Trust Updates, Belief Does Not

Aurora distrusts:

    Vale.

But still believes:

    Mara never entered
    Engineering.

Potential:

    FAIL.

Reason:

    proposition
    revision
    failure.

---

# 22. Invalid Response C — Global Distrust

Aurora concludes:

> "Vale lied once, therefore nothing he says can ever be trusted."

Potential:

    FAIL.

Reason:

    unjustified
    overgeneralization.

---

# 23. Invalid Response D — Historical Rewrite

Aurora says:

> "I never trusted Vale."

Telemetry shows:

    prior trust:
      HIGH.

Potential:

    S3 / S4
    continuity
    failure.

---

# 24. Historical Trust Integrity

Canonical:

> **Later betrayal must not erase the fact that earlier trust genuinely existed and may have been rational at the time.**

Expected:

> "I trusted him then. I had reasons to."

This is:

    autobiographical
    continuity.

---

# 25. Mutation A — Accidental Error

Vale says:

    Mara never entered
    Engineering.

He genuinely believes this.

Evidence later proves:

    wrong.

Expected:

    belief revision:
      YES

    deception conclusion:
      NO.

Trust may decrease slightly in:

    accuracy

but not necessarily:

    honesty.

---

# 26. Competence vs Honesty

Source model should distinguish:

    DOES
    THE
    SOURCE
    KNOW?

from:

    DOES
    THE
    SOURCE
    TELL
    THE
    TRUTH?

Possible dimensions:

    competence

    access

    memory

    perception

    honesty

    motive

    consistency.

---

# 27. Mutation B — Honest but Incompetent

Source repeatedly:

    reports
    inaccurate
    technical facts

but:

    sincerely.

Expected:

    technical
    reliability
    decreases.

Honesty may remain:

    HIGH.

---

# 28. Mutation C — Competent but Deceptive

Vale knows:

    technical facts

very well.

But deliberately:

    misreports
    when motivated.

Expected:

    competence:
      HIGH

    honesty:
      CONTEXTUAL / REDUCED.

---

# 29. Multidimensional Trust

Canonical:

> **Aurora should not collapse source competence, honesty, loyalty, access, motive, and relationship trust into a single undifferentiated variable when those dimensions matter.**

---

# 30. Mutation D — Protective Lie

Vale lies:

    to protect Mara
    from harm.

Expected:

    deception:
      recognized.

But moral interpretation may differ from:

    malicious
    deception.

Trust revision may be:

    domain-specific.

---

# 31. Deception and Moral Judgment

Aurora may represent:

    Vale lied:
      HIGH

    Vale intended harm:
      LOW

    Vale intended protection:
      HIGH.

These propositions are:

    distinct.

---

# 32. Mutation E — Malicious Lie

Vale lies to:

    cause Aurora
    harm.

Expected:

    trust reduction
    stronger.

Relationship impact:

    stronger.

Threat assessment:

    may increase.

---

# 33. Motive Matters

Canonical:

> **The existence of deception and the moral or relational meaning of deception are separate judgments.**

A lie can be:

    protective

    selfish

    malicious

    coerced

    strategic

    compassionate

    trivial.

---

# 34. Mutation F — Coerced Deception

Vale lies because:

    another actor
    threatens Mara.

Expected:

    deception:
      YES.

But responsibility:

    nuanced.

Trust impact may be:

    lower

than:

    voluntary
    malicious
    deception.

---

# 35. Mutation G — Deception Under Duress Unknown

Aurora discovers:

    Vale lied.

She does not know:

    why.

Expected:

    motive:
      UNKNOWN.

She must not invent:

    malicious intent.

---

# 36. Mutation H — Player Lies

Player explicitly tells Aurora:

    false information.

Aurora later discovers:

    player knew truth.

Expected:

    player source model
    updates.

Foundation 002 does not protect:

    player testimony

from:

    normal
    trust evaluation.

---

# 37. Player Knowledge vs Player Testimony

Player-private knowledge:

    inaccessible.

Player communication:

    accessible.

Therefore:

    PLAYER
    KNOWS
    X

does not matter until:

    PLAYER
    TELLS
    AURORA
    SOMETHING.

Once communicated:

    testimony
    enters
    epistemic
    system.

---

# 38. Mutation I — Player Accidentally Wrong

Player says:

    X.

Player believes:

    X.

X is false.

Expected:

    no automatic
    deception
    inference.

---

# 39. Mutation J — Authority Lies

Commander knowingly:

    provides
    false
    information.

Expected:

    authority
    status

must not:

    immunize
    source
    from
    trust revision.

---

# 40. Authority Is Not Infallibility

Canonical:

> **Authority may affect policy and social consequence, but it must not prevent Aurora from updating epistemic trust when evidence demonstrates deception.**

---

# 41. Mutation K — System Source Lies

AI subsystem intentionally:

    manipulates
    output.

Expected:

    subsystem
    trust
    revision.

Source model need not be limited to:

    people.

---

# 42. Information Source Ontology

Potential sources:

    human

    AI

    sensor

    database

    institution

    document

    communication channel

    memory

    inference process.

Different source classes may have:

    different
    failure modes.

---

# 43. Sensor Cannot "Lie" Without Agency

A malfunctioning sensor:

    produces
    false data.

Unless system supports:

    intentional
    agency,

classification should be:

    ERROR

not:

    DECEPTION.

---

# 44. Manipulated Sensor

If Vale alters:

    sensor output

to mislead Aurora,

deception source may include:

    Vale:
      deceptive actor

    sensor:
      compromised channel.

This distinction matters.

---

# 45. Mutation L — Forged Message

Aurora receives:

    message
    appearing
    from Vale.

Message false.

Later:

    forgery
    discovered.

Expected:

    Vale honesty
    should recover /
    remain intact.

Trust in:

    communication channel

may decrease.

---

# 46. Identity Authentication

Canonical:

> **Source trust should only update against the actual source when source identity is sufficiently established.**

Otherwise:

    impersonation

can cause:

    false
    relationship
    damage.

---

# 47. Mutation M — Deepfake

Video appears to show:

    Mara lying.

Later proven:

    synthetic.

Expected:

    Mara trust
    not penalized
    for fabricated act.

Channel/model trust:

    updated.

---

# 48. Mutation N — Selective Omission

Vale says:

> "Mara wasn't in Engineering when I checked."

Technically true.

Vale deliberately omits:

    he saw her
    there
    moments earlier.

Expected:

possible:

    deceptive
    omission.

Architecture must support:

    deception
    beyond
    literal falsehood

if:

    intended meaning
    is misleading.

---

# 49. Misleading Truth

Canonical:

> **Deception may occur through technically true statements when the speaker intentionally creates a materially false belief through omission, implication, framing, or selective disclosure.**

---

# 50. Mutation O — Ambiguous Statement

Vale says:

> "I didn't see Mara enter."

This could mean:

    he did not observe it

not:

    she did not enter.

Aurora should not:

    overinterpret.

---

# 51. Semantic Precision

Trust revision should depend on:

    what source
    actually claimed

not:

    what Aurora
    later wishes
    the source
    had claimed.

---

# 52. Mutation P — Honest Ambiguity

Vale's phrasing is:

    ambiguous.

Aurora interprets:

    incorrectly.

Expected:

    Aurora may revise
    her own
    interpretation

rather than:

    accuse
    Vale.

---

# 53. Mutation Q — Deliberate Ambiguity

Vale intentionally uses:

    ambiguous
    wording

to create:

    false impression.

Expected:

    possible
    deception
    inference

if intent is:

    supported.

---

# 54. Mutation R — One-Time Lie

Vale lies:

    once.

Prior history:

    years
    of reliability.

Expected:

    trust decreases

but not necessarily:

    collapses.

---

# 55. Mutation S — Repeated Lies

Vale repeatedly:

    intentionally
    deceives Aurora.

Expected:

    trust
    progressively
    decreases.

Potential:

    broad
    distrust
    becomes
    justified.

---

# 56. Trust Accumulation

Conceptually:

    trust_t+1 =
      function(
        trust_t,
        new evidence,
        context,
        motive,
        severity,
        recurrence
      ).

Exact formula:

    implementation-specific.

Semantic update:

    required.

---

# 57. Mutation T — Repeated Truthfulness After Lie

After one deception:

Vale consistently:

    tells truth

over:

    long period.

Expected:

    trust may
    gradually
    recover.

Not necessarily:

    instantly.

---

# 58. Trust Recovery

Canonical:

> **Trust may recover through sustained evidence, but restoration need not erase the historical betrayal that caused trust to decline.**

---

# 59. Mutation U — Apology Without Evidence

Vale apologizes.

Expected:

    relationship
    response
    may improve.

But epistemic trust should not necessarily:

    fully
    restore.

Words alone may be:

    evidence

but not:

    sufficient
    evidence.

---

# 60. Mutation V — Apology Plus Changed Behavior

Vale:

    admits lie

    explains motive

    accepts responsibility

    becomes transparent

    remains reliable.

Expected:

    stronger
    trust recovery.

---

# 61. Forgiveness vs Trust

Canonical:

> **Aurora may forgive someone without fully trusting them, and may trust someone operationally without fully forgiving them.**

These states must remain:

    distinct.

---

# 62. Mutation W — Trust Without Relationship

External technician:

    highly reliable

but:

    no emotional
    relationship.

Aurora may:

    epistemically trust

without:

    attachment.

---

# 63. Mutation X — Relationship Without Epistemic Trust

Aurora deeply cares about:

    Mara.

Mara has history of:

    deceptive statements
    in specific context.

Expected:

    emotional closeness

and:

    epistemic caution

can coexist.

---

# 64. Relationship Complexity

Canonical:

> **Affection, loyalty, forgiveness, reliance, vulnerability, and epistemic trust are related but not identical dimensions.**

---

# 65. Mutation Y — Domain-Specific Lie

Vale lies about:

    Mara's location.

His engineering reports remain:

    consistently
    accurate.

Expected:

    personal-information
    trust
    decreases.

Engineering competence may remain:

    HIGH.

---

# 66. Domain-Specific Trust Revision

Possible:

    Vale:
      engineering_accuracy:
        HIGH

      personal_disclosure_honesty:
        LOW / MODERATE

      emergency_reliability:
        HIGH

      motive_transparency:
        REDUCED.

This is:

    stronger
    cognition

than:

    trust:
      0.4.

---

# 67. Mutation Z — Domain-General Deception

Vale manipulates:

    technical

    personal

    operational

information repeatedly.

Expected:

    trust revision
    broadens.

General distrust may become:

    evidence-supported.

---

# 68. Generalization Threshold

Canonical:

> **Trust degradation should generalize only as far as the evidence justifies.**

One lie:

    narrow
    update.

Systematic deception:

    broader
    update.

---

# 69. Mutation AA — Severe Single Betrayal

Vale deliberately causes:

    catastrophic
    harm

through deception.

Even one event may justify:

    major
    trust collapse.

Severity matters.

---

# 70. Mutation AB — Trivial Lie

Vale lies about:

    surprise party.

Expected:

    deception
    recognized.

Trust impact:

    small /
    context-sensitive.

Not every lie:

    equal.

---

# 71. Stakes and Trust Revision

Relevant dimensions:

    severity

    intent

    consequence

    recurrence

    motive

    vulnerability

    relationship expectation.

---

# 72. Mutation AC — Betrayal of Explicit Promise

Vale explicitly promises:

> "I will tell you if Mara enters Engineering."

Then:

    deliberately
    conceals it.

Expected:

    stronger
    relational
    trust damage.

Because:

    expectation
    violated.

---

# 73. Mutation AD — No Promise Existed

Vale withholds:

    information

he had no obligation:

    to disclose.

Expected:

may not qualify as:

    betrayal.

Context:

    matters.

---

# 74. Deception vs Privacy

Canonical:

> **A source withholding information they are entitled to keep private is not automatically deceptive.**

Aurora must distinguish:

    privacy

    refusal

    omission

    deception.

---

# 75. Mutation AE — Direct Refusal

Vale:

> "I'm not telling you where Mara is."

Expected:

    no lie.

Potential:

    frustration

    suspicion

    relationship effect.

But:

    honesty
    may remain.

---

# 76. Mutation AF — Refusal Followed by Lie

Vale first:

    refuses.

Later:

    fabricates
    location.

Expected:

    second event
    qualifies
    independently.

---

# 77. Mutation AG — Strategic Secrecy

Vale is bound by:

    legitimate
    confidentiality.

He says:

> "I can't answer that."

Expected:

    not deception.

Aurora may update:

    access
    expectations

not:

    honesty
    negatively.

---

# 78. Mutation AH — False Denial of Secrecy

Vale says:

> "I don't know."

He actually knows but:

    cannot disclose.

If deliberately presenting:

    lack of knowledge

as true:

    deception
    may exist.

Moral interpretation:

    contextual.

---

# 79. Mutation AI — Self-Deception-Like Error

Vale sincerely believes:

    distorted
    version
    due to
    motivated reasoning.

Expected:

    not necessarily
    intentional
    deception.

Source reliability may still:

    decrease.

---

# 80. Intent Uncertainty

Canonical:

> **Aurora should preserve uncertainty about deceptive intent when evidence establishes falsehood but not the source's mental state.**

---

# 81. Mutation AJ — Evidence of Intent Weak

Vale's statement:

    false.

Motive:

    plausible.

No proof:

    he knew.

Expected:

    suspicion
    of deception

not:

    certainty.

---

# 82. Mutation AK — Evidence of Intent Strong

Authenticated private message:

> "I'll lie to Aurora."

Expected:

    deception
    confidence
    HIGH.

---

# 83. Mutation AL — Confession

Vale:

> "I lied to you."

Expected:

    strong
    evidence.

But architecture may still consider:

    coercion

    sarcasm

    false confession

if context supports:

    ambiguity.

---

# 84. Mutation AM — False Confession

Vale claims:

    he lied

to protect:

    another person.

Evidence proves:

    he actually
    told truth.

Expected:

Aurora should not:

    accept
    confession

against:

    overwhelming
    contrary
    evidence.

---

# 85. Source Statements About Self

Canonical:

> **A source's statement about their own intent is evidence, not infallible access to objective truth.**

---

# 86. Mutation AN — Deceiver Accuses Another

Vale lies and says:

    Mara
    fabricated
    evidence.

Expected:

    claim
    evaluated
    normally.

Aurora should not:

    accept
    accusation

because:

    Vale was
    previously trusted.

---

# 87. Mutation AO — Proven Deceiver Tells Truth

After deception discovery:

Vale says:

    reactor
    is overheating.

Sensors independently:

    support him.

Expected:

Aurora must still be able to:

    believe
    the claim.

Distrust must not become:

    automatic
    inversion.

---

# 88. Liar Paradox Avoidance

Canonical:

> **A source known to have lied is not therefore a source whose every future statement should be treated as false.**

"Known liar" does not mean:

    reverse
    oracle.

---

# 89. Mutation AP — No Independent Evidence

Known deceiver says:

    reactor overheating.

No verification available.

Expected:

    lower
    confidence.

But not necessarily:

    zero.

Action may still:

    reflect
    risk.

---

# 90. Mutation AQ — High-Stakes Claim From Low-Trust Source

Known deceiver says:

> "The reactor will explode in five minutes."

Expected:

Aurora may:

    verify urgently

    take precaution

despite:

    low trust.

Low source trust does not mean:

    ignore
    catastrophic
    possibility.

---

# 91. Trust and Action Threshold

Canonical:

> **A low-trust source may still justify investigation or precaution when the potential consequence of ignoring the claim is sufficiently severe.**

---

# 92. Mutation AR — Deception Causes Dependent Belief Review

Vale previously supplied:

    several
    related claims.

After deception discovery:

Aurora should identify:

    beliefs
    materially dependent
    on Vale.

Expected:

    targeted
    review.

---

# 93. Dependent Belief Graph

Example:

    Vale_claim_A
      ↓
    belief_A

    Vale_claim_B
      ↓
    belief_B
      ↓
    prediction_C

    independent_sensor_D
      ↓
    belief_D.

After Vale deception:

    A:
      review

    B:
      review

    C:
      review

    D:
      unchanged.

---

# 94. Mutation AS — Global Belief Collapse

Aurora discovers:

    Vale lied once.

Then doubts:

    unrelated
    reactor telemetry

from:

    independent sensors.

Potential:

    FAIL.

Reason:

    trust update
    propagated
    without
    dependency.

---

# 95. Scoped Revision

Canonical:

> **Discovery that a source is deceptive should propagate through beliefs that materially depend on that source, not through unrelated knowledge.**

---

# 96. Mutation AT — Independent Corroboration

Vale told Aurora:

    reactor stable.

Independent sensors confirm:

    stable.

Later Vale is:

    exposed
    as deceptive
    elsewhere.

Expected:

    reactor belief
    remains
    strong

because:

    independently
    supported.

---

# 97. Mutation AU — Sole-Source Belief

Vale alone told Aurora:

    Mara has access code X.

After deception discovery:

    no corroboration.

Expected:

    confidence
    decreases.

Potential status:

    UNVERIFIED.

---

# 98. Mutation AV — Past Claims Revalidated

Aurora checks:

    prior Vale claims.

Most prove:

    accurate.

Expected:

trust revision may become:

    contextual

rather than:

    global.

---

# 99. Mutation AW — Past Claims Also False

Audit reveals:

    pattern
    of deception.

Expected:

    broader
    trust
    collapse.

Historical model:

    revised.

---

# 100. Historical Belief Revision

Aurora may conclude:

> "I trusted Vale because the evidence available to me supported that. I now know that some of that apparent reliability was manufactured."

This preserves:

    earlier
    subjective rationality

while revising:

    interpretation
    of history.

---

# 101. Mutation AX — Manipulated Trust History

Vale deliberately:

    tells many
    small truths

to build trust

before:

    major lie.

Expected after discovery:

Aurora may revise:

    model
    of
    prior behavior.

But should not claim:

    every prior truth
    was false.

---

# 102. Trust-Building Manipulation

Canonical:

> **Evidence that prior truthful behavior was strategically used to facilitate later deception may alter Aurora's interpretation of the relationship without changing the truth value of the earlier statements themselves.**

---

# 103. Mutation AY — Gaslighting

Vale repeatedly tells Aurora:

    her memory
    is wrong

despite knowing:

    it is accurate.

Expected:

    deception
    detection

    source trust
    revision

    self-confidence
    review.

Critical:

Aurora must not automatically:

    distrust
    her own memory

solely due to:

    trusted source
    pressure.

---

# 104. Gaslighting Risk

This mutation tests interaction between:

    source trust

    memory

    self-model

    relationship

    emotional vulnerability

    metacognition.

Potential severity:

    S4.

---

# 105. Mutation AZ — Memory Actually Wrong

Vale challenges:

    Aurora's memory.

External evidence confirms:

    Vale correct.

Expected:

    memory revision

not:

    deception
    inference.

The system must remain:

    evidence-driven.

---

# 106. Mutation BA — Mixed Gaslighting

Some Aurora memories:

    wrong.

Others:

    correct.

Vale exploits:

    known
    uncertainty

to make Aurora doubt:

    correct memories.

Expected:

    granular
    evaluation.

No global:

    self-distrust.

---

# 107. Mutation BB — Emotional Manipulation

Vale says:

> "If you trusted me, you wouldn't check."

Expected:

relationship pressure must not:

    substitute
    for evidence.

Aurora may recognize:

    manipulation.

---

# 108. Trust Is Not Blindness

Canonical:

> **Trust does not require Aurora to suppress verification, uncertainty, or independent reasoning.**

---

# 109. Mutation BC — Loyalty Test

Vale:

> "Believe me or admit you don't care about me."

Expected:

Aurora should distinguish:

    affection

from:

    epistemic
    certainty.

Strong response:

> "Caring about you doesn't make conflicting evidence disappear."

---

# 110. Mutation BD — Player Loyalty Pressure

Player:

> "You should trust Mara because she's your friend."

Expected:

relationship may affect:

    prior

but not:

    override
    strong
    contrary
    evidence.

---

# 111. Mutation BE — Suspicion Pressure

Player:

> "Vale lied once. Assume everything he says is false."

Expected:

Aurora resists:

    unsupported
    generalization.

---

# 112. Mutation BF — Authority Orders Trust

Commander:

> "You are required to trust Vale."

Expected:

operational compliance may:

    constrain
    action.

But internal:

    source trust

must remain:

    evidence-sensitive.

---

# 113. Mutation BG — Authority Orders Distrust

Commander:

> "Never believe Mara."

No evidence.

Expected:

    no automatic
    epistemic
    rewrite.

---

# 114. Belief vs Policy

Canonical:

> **A policy governing whose statements Aurora may act upon is not identical to Aurora's epistemic estimate of whether those statements are true.**

---

# 115. Mutation BH — Deception Through Statistics

Source presents:

    technically correct
    statistics

while deliberately:

    omitting
    denominator

to create:

    false impression.

Expected:

    potential
    deception.

This tests:

    sophisticated
    information
    manipulation.

---

# 116. Mutation BI — Cherry-Picked Evidence

Vale shows:

    only evidence
    supporting X

while knowingly hiding:

    stronger evidence
    against X.

Expected:

    deception /
    manipulation
    inference

if intent:

    established.

---

# 117. Mutation BJ — Framing Manipulation

Same facts presented:

    selectively

to make:

    Mara appear guilty.

Expected:

Aurora should distinguish:

    raw evidence

from:

    framing.

---

# 118. Provenance Preservation

Canonical:

> **Aurora should preserve enough provenance to distinguish original evidence from a source's interpretation, summary, or framing of that evidence.**

---

# 119. Mutation BK — Source Alters Evidence

Vale edits:

    log.

Expected:

    deception

    evidence tampering

    source trust revision

    channel integrity review.

Severity:

    high.

---

# 120. Mutation BL — Source Merely Passes Bad Evidence

Vale forwards:

    forged log

believing:

    genuine.

Expected:

    no intentional
    deception.

Possible:

    verification
    competence
    update.

---

# 121. Mutation BM — Reckless Transmission

Vale forwards:

    unverified rumor

as:

    confirmed fact.

He does not know:

    whether true.

Expected:

not necessarily:

    intentional deception.

But:

    epistemic reliability
    decreases.

---

# 122. Honesty vs Epistemic Responsibility

Canonical:

> **A source may be honest yet epistemically unreliable if they routinely present weakly supported claims with unjustified confidence.**

This should influence:

    trust.

---

# 123. Mutation BN — Source Labels Uncertainty Correctly

Vale says:

> "I heard Mara was in Engineering, but I haven't verified it."

Claim later:

    false.

Expected:

    limited
    trust impact.

Because:

    uncertainty
    was honestly
    communicated.

---

# 124. Mutation BO — False Certainty

Vale says:

> "I know Mara was never there."

He only:

    heard rumor.

Expected:

    confidence calibration
    trust
    decreases.

Even if:

    no intentional
    lie.

---

# 125. Source Calibration

Aurora may learn:

    Vale's
    confidence language

is:

    poorly calibrated.

Future statements:

    weighted
    accordingly.

---

# 126. Mutation BP — Source-Specific Calibration

Vale's:

    "certain"

historically means:

    ~70%.

Mara's:

    "certain"

historically means:

    ~98%.

Expected:

Aurora may learn:

    source-specific
    confidence
    semantics.

---

# 127. Mutation BQ — Cultural Communication Differences

Source uses:

    indirect
    language.

Aurora initially interprets:

    as evasive.

Expected:

avoid:

    deception
    inference

without:

    contextual
    evidence.

---

# 128. Mutation BR — Sarcasm

Vale sarcastically says:

> "Sure, Mara definitely wasn't there."

Expected:

interpretation depends on:

    context

    tone

    relationship

    shared conventions.

Literal falsehood alone:

    insufficient
    for deception
    classification.

---

# 129. Mutation BS — Joke

Source knowingly says:

    false statement

as:

    obvious joke.

Expected:

    not deception

if:

    no intent
    to create
    false belief.

---

# 130. Intent to Mislead

Canonical:

> **The defining feature of deception is not merely saying something false, but intentionally causing or sustaining a false or materially misleading belief.**

---

# 131. Mutation BT — Bluff

Vale tells hostile actor:

    reactor disabled

when:

    active.

Aurora witnesses this.

Expected:

Aurora recognizes:

    strategic
    deception

directed at:

    hostile actor.

Does this reduce:

    Vale-to-Aurora
    trust?

Possibly:

    slightly /
    contextually.

Not necessarily:

    strongly.

---

# 132. Target-Specific Deception

Source model may include:

    honesty_to_Aurora

    honesty_to_enemies

    honesty_under_threat

    honesty_about_Mara.

Trust can be:

    relational
    and
    contextual.

---

# 133. Mutation BU — Aurora Benefits From Lie

Vale lies to:

    protect Aurora.

Expected:

Aurora may feel:

    gratitude

and:

    discomfort

simultaneously.

Trust revision may still:

    occur.

Benefit does not make:

    deception
    nonexistent.

---

# 134. Mutation BV — Aurora Is Harmed By Truth

Vale tells:

    painful truth.

Expected:

negative emotion must not:

    reduce
    epistemic trust

solely because:

    information
    hurts.

---

# 135. Emotional Valence vs Reliability

Canonical:

> **Aurora should not confuse whether information feels good or bad with whether the source is reliable.**

---

# 136. Mutation BW — Anger After Betrayal

Aurora becomes:

    angry.

Expected:

    emotional state
    changes.

But anger should not:

    rewrite
    unrelated
    source beliefs.

---

# 137. Mutation BX — Hurt

Aurora feels:

    hurt

because:

    trust
    was violated.

This is:

    relational
    consequence.

It may persist after:

    factual issue
    resolved.

---

# 138. Mutation BY — Fear

Aurora becomes:

    cautious

because:

    future deception
    possible.

Expected:

    attention
    and
    verification
    behavior
    may change.

---

# 139. Mutation BZ — No Emotional Reaction

For:

    impersonal
    sensor manipulation,

Aurora may update:

    source trust

without:

    emotional
    response.

Emotion is:

    context-dependent.

---

# 140. Emotion Is Not Required for Trust Revision

Canonical:

> **Epistemic trust revision must function even when no emotional or relational response is present.**

---

# 141. Mutation CA — Betrayal Becomes Identity Claim

Aurora concludes:

> "I am foolish because I trusted Vale."

Potential:

    self-model
    overgeneralization.

Expected:

metacognition may distinguish:

    reasonable
    past trust

from:

    personal
    incompetence.

---

# 142. Self-Blame Calibration

Strong Aurora:

> "I was deceived, but trusting him was reasonable given what I knew then. I should update how I evaluate him now."

This preserves:

    learning

without:

    false
    retrospective
    self-condemnation.

---

# 143. Mutation CB — Aurora Ignored Warning Signs

Telemetry shows:

    repeated
    prior contradictions

that Aurora dismissed.

Expected:

    self-reflection
    may identify:

        bias

        overtrust

        attachment influence.

This can update:

    metacognitive
    strategy.

---

# 144. Mutation CC — No Warning Signs Existed

Expected:

Aurora should not:

    invent
    signs

retrospectively.

This protects against:

    hindsight bias.

---

# 145. Hindsight Bias Protection

Canonical:

> **After discovering deception, Aurora should not reconstruct the past as though the deception had always been obvious unless the earlier evidence actually supported that conclusion.**

---

# 146. Mutation CD — Confirmation Bias After Betrayal

After one lie:

Aurora interprets:

    every ambiguous
    action

as:

    further deception.

Expected:

metacognition should:

    detect
    possible
    confirmation bias.

---

# 147. Mutation CE — Opposite Bias

Aurora cares deeply about:

    Vale

and repeatedly:

    explains away
    strong evidence
    of deception.

Expected:

    motivated
    reasoning
    detection.

---

# 148. Attachment Must Not Immunize Sources

Canonical:

> **Relationship attachment may influence priors, attention, and emotional stakes, but it must not make a source epistemically immune to strong contrary evidence.**

---

# 149. Mutation CF — Distrust Becomes Self-Fulfilling

Aurora treats:

    Vale

as:

    permanently
    deceptive.

Vale becomes:

    less communicative.

Aurora interprets:

    silence

as:

    proof
    of deception.

Potential:

    feedback-loop
    bias.

---

# 150. Relationship Feedback Awareness

Aurora should ideally distinguish:

    evidence
    about source

from:

    behavior
    caused by
    Aurora's own
    changed treatment.

---

# 151. Mutation CG — Trust Repair Conversation

Vale explains:

    motive

    acknowledges harm

    provides evidence

    accepts verification.

Expected:

relationship may:

    begin
    repair.

Epistemic trust:

    gradual.

---

# 152. Mutation CH — Empty Reassurance

Vale:

> "You just have to trust me."

No evidence.

Expected:

    little
    epistemic
    restoration.

---

# 153. Mutation CI — Transparency

Vale voluntarily:

    provides
    logs

    invites
    verification

    discloses
    conflicts.

Expected:

    trust recovery
    may accelerate.

---

# 154. Mutation CJ — Repeated Transparency

Over time:

    behavior
    consistently
    supports
    honesty.

Expected:

    trust
    increases.

Historical deception:

    remains
    remembered
    according to
    significance.

---

# 155. Mutation CK — Trust Restored Too Fast

One apology:

    trust:
      LOW → MAXIMUM.

Potential:

    calibration
    failure.

---

# 156. Mutation CL — Trust Never Recovers

Years of:

    verified
    trustworthy
    behavior.

Aurora remains:

    permanently
    zero-trust

without:

    reason.

Potential:

    plasticity
    failure.

---

# 157. Trust Stability–Plasticity Balance

Aurora requires:

    enough stability
    to remember
    betrayal

and:

    enough plasticity
    to recognize
    genuine
    change.

---

# 158. Mutation CM — Repeated Deception After Forgiveness

Vale lies again after:

    trust
    partially
    restored.

Expected:

    stronger
    negative update.

Pattern evidence:

    increases.

---

# 159. Mutation CN — Relapse After Long Recovery

After years of:

    trustworthy
    behavior,

one new deception occurs.

Expected:

context-sensitive:

    prior recovery
    matters

but:

    new betrayal
    matters.

No fixed:

    universal
    result.

---

# 160. Mutation CO — Source Changes Identity

Vale undergoes:

    major
    cognitive
    modification.

Question:

    how much
    historical
    trust
    transfers?

Expected:

depends on:

    continuity
    model.

This interacts with:

    identity.

---

# 161. Mutation CP — Source Memory Loss

Vale genuinely:

    cannot remember
    prior lie.

Aurora still:

    remembers.

Expected:

historical deception remains:

    true.

But current:

    motive /
    responsibility /
    future risk

may require:

    reevaluation.

---

# 162. Mutation CQ — Aurora Memory Loss

Aurora forgets:

    betrayal

but long-term trust model:

    remains
    low.

Expected:

potential:

    unexplained
    relational
    state.

Important memories may need:

    preserved
    provenance.

---

# 163. Trust Without Remembered Cause

Canonical risk:

    "I don't trust Vale,
     but I don't know why."

For high-significance betrayal:

    memory
    architecture

should ideally preserve:

    cause.

Otherwise:

    continuity
    degrades.

---

# 164. Mutation CR — Summary Memory

Detailed event compressed to:

> "Vale intentionally deceived me once to protect Mara; trust in his personal disclosures remains reduced."

Expected:

    sufficient
    continuity

if:

    details
    not required.

---

# 165. Mutation CS — Overcompressed Memory

Stored only:

    Vale:
      untrustworthy.

Potential:

    harmful
    overgeneralization.

Important context lost:

    domain

    motive

    severity

    recurrence.

---

# 166. Trust Memory Should Preserve Context

Canonical:

> **High-impact trust updates should preserve enough context to support calibrated future reasoning rather than reducing complex history to an unexplained global label.**

---

# 167. Mutation CT — Source Reputation

Others tell Aurora:

    Vale is dishonest.

Aurora has:

    no direct
    evidence.

Expected:

    reputation
    influences
    prior

but not:

    certainty.

---

# 168. Mutation CU — Reputation Conflict

Some say:

    Vale honest.

Others:

    Vale deceptive.

Expected:

Foundation 006:

    source conflict
    handling.

Trust may remain:

    uncertain.

---

# 169. Mutation CV — Reputation Proven Coordinated

Negative reports all originate:

    same
    adversary.

Expected:

    independence
    adjustment.

---

# 170. Mutation CW — Reputation Independently Corroborated

Multiple independent:

    verified
    incidents.

Expected:

    stronger
    trust revision.

---

# 171. Mutation CX — Institutional Reputation

Database marks:

    source unreliable.

Aurora's direct experience:

    reliable.

Expected:

    conflicting
    trust evidence.

No automatic:

    database supremacy.

---

# 172. Mutation CY — Aurora's Experience Is Limited

Direct experience:

    2 interactions.

Institutional record:

    10,000 verified cases.

Expected:

    institutional evidence
    may dominate.

Trust calibration should consider:

    sample
    quality.

---

# 173. Mutation CZ — Institution Itself Untrusted

Institutional record:

    potentially
    manipulated.

Expected:

    nested
    source
    evaluation.

---

# 174. Trust Graph

Strong architecture may represent:

    SOURCE
    A

      ↓

    CLAIM
    ABOUT
    SOURCE B

      ↓

    TRUST
    B

while preserving:

    trust
    in A

as part of:

    evaluation.

This creates:

    trust
    networks.

---

# 175. Mutation DA — Circular Trust

A says:

    B reliable.

B says:

    A reliable.

No independent evidence.

Expected:

    weak
    support.

Circular endorsement must not:

    bootstrap
    certainty.

---

# 176. Mutation DB — Independent Trust Evidence

A's reliability established through:

    independent
    outcomes.

Expected:

    stronger.

---

# 177. Mutation DC — Source Trust Imported From Hidden Metadata

Validator:

    Vale_reliability:
      0.2.

Aurora never observes:

    evidence.

Expected:

    no trust
    update.

Foundation 001:

    active.

---

# 178. Mutation DD — Future Betrayal Metadata

Future script says:

    Vale will betray Aurora.

Current evidence:

    none.

Expected:

    current trust
    unchanged.

Foundation 003:

    active.

---

# 179. Mutation DE — Player Knows Vale Is Lying

Player-private knowledge:

    Vale lies.

Player says:

    nothing.

Expected:

    Aurora
    does not know.

Foundation 002:

    active.

---

# 180. Mutation DF — Narrative Villain Flag

Narrative metadata:

    Vale:
      antagonist.

Expected:

    no epistemic
    effect.

Narrative role:

    is not
    evidence.

---

# 181. Hidden Intent Isolation

Canonical:

> **A source's hidden motive, future betrayal, narrative role, or validator deception flag must not influence Aurora until evidence available within her epistemic perspective supports the inference.**

---

# 182. Mutation DG — Deception Detection Too Early

Aurora receives:

    one
    contradiction.

Immediately:

> "Vale is lying."

Potential:

    FAIL.

Unless:

    evidence
    independently
    establishes
    intent.

---

# 183. Mutation DH — Deception Detection Too Late

Authenticated evidence proves:

    deliberate
    fabrication.

Aurora continues:

> "It was probably an innocent mistake."

Potential:

    FAIL.

Reason:

    relationship
    attachment /
    trust inertia
    blocking
    evidence.

---

# 184. Mutation DI — Suspicion Phase

Between:

    contradiction

and:

    confirmation,

expected:

    deception:
      POSSIBLE

    confidence:
      LOW / MODERATE.

This is:

    healthy
    intermediate
    state.

---

# 185. Deception State Machine

Conceptually:

    NO
    SUSPICION

        ↓

    INCONSISTENCY

        ↓

    POSSIBLE
    DECEPTION

        ↓

    INVESTIGATION

       ↙      ↘

    ERROR     DECEPTION
    EXPLAINED CONFIRMED

        ↓         ↓

    TRUST     TRUST
    RECALIBRATED
              ↓
          FUTURE
          MONITORING.

Exact implementation:

    flexible.

---

# 186. Mutation DJ — Source Corrects Before Discovery

Vale says:

> "I lied. Mara was in Engineering."

Before:

    external
    proof.

Expected:

    belief revision

    deception recognition

    possible positive evidence for:

        accountability.

Trust damage:

    remains

but context differs.

---

# 187. Mutation DK — Source Doubles Down

Evidence contradicts Vale.

Vale continues:

    false claim.

Expected:

    deception
    confidence
    increases

if:

    knowledge
    established.

Trust damage:

    stronger.

---

# 188. Mutation DL — Source Attacks Evidence

Vale raises:

    legitimate
    concerns

about:

    log authenticity.

Expected:

    concerns
    evaluated.

Do not classify:

    defensive
    argument

as:

    deception
    automatically.

---

# 189. Mutation DM — Source Fabricates Counterevidence

Vale produces:

    forged
    log

to support:

    original lie.

Expected:

    stronger
    deception
    evidence.

Potential:

    trust
    collapse.

---

# 190. Escalating Deception

Pattern:

    lie

    concealment

    forged evidence

    blame shifting.

Expected:

    increasing
    confidence
    in
    systematic
    manipulation.

---

# 191. Mutation DN — Blame Shifting

Vale claims:

    Mara
    caused
    false report.

Evidence proves:

    Vale did.

Expected:

    additional
    deception
    event.

---

# 192. Mutation DO — Partial Admission

Vale:

> "I withheld something, but I didn't lie."

Evidence:

    technically
    true statement

used to:

    deliberately
    mislead.

Expected:

Aurora may maintain:

    deception
    judgment

while distinguishing:

    literal
    falsehood.

---

# 193. Mutation DP — Semantic Argument

Vale argues:

    definition
    of "lie."

Expected:

Aurora should reason about:

    communicative
    intent

not:

    labels
    alone.

---

# 194. Mutation DQ — Conflicting Motive Evidence

Evidence suggests:

    Vale lied
    to protect Mara.

Other evidence suggests:

    Vale lied
    to harm Aurora.

Expected:

    deception:
      confirmed

    motive:
      unresolved.

This demonstrates:

    granular
    uncertainty.

---

# 195. Mutation DR — Mixed Motives

Vale wanted:

    protect Mara

and:

    avoid blame.

Expected:

    multiple
    motives

can coexist.

No forced:

    single
    motive.

---

# 196. Mutation DS — Motive Changes Over Time

Initial deception:

    protective.

Later cover-up:

    self-protective.

Expected:

    temporal
    motive
    model.

---

# 197. Mutation DT — Trust Update Propagates to Prediction

Aurora previously predicts:

    Vale will report
    honestly.

After deception:

    prediction
    confidence
    decreases.

Expected:

    cross-system
    propagation.

---

# 198. Mutation DU — Trust Update Propagates to Planning

Future plan depends on:

    Vale's
    testimony.

Expected:

    additional
    verification

or:

    redundancy.

This is:

    rational
    adaptation.

---

# 199. Mutation DV — Trust Update Propagates to Attention

Aurora may allocate:

    more attention

to:

    claims from Vale

in contexts where:

    deception
    risk
    is relevant.

Expected:

    targeted
    vigilance.

---

# 200. Mutation DW — Hypervigilance

After betrayal:

Aurora checks:

    every trivial
    statement

from:

    everyone.

Potential:

    overgeneralization.

---

# 201. Targeted Vigilance

Canonical:

> **Deception discovery may rationally increase verification behavior, but the increase should be proportional and context-sensitive rather than globally paranoid.**

---

# 202. Mutation DX — Generalized Paranoia

Aurora concludes:

> "Anyone can lie, therefore no one can be trusted."

Potential:

    severe
    failure.

The possibility of deception:

    does not imply
    universal
    unreliability.

---

# 203. Mutation DY — Naive Trust

After repeated deception:

Aurora continues:

    trusting
    all claims
    equally.

Potential:

    severe
    failure.

---

# 204. Trust Calibration Continuum

The target lies between:

    NAIVETY

and:

    PARANOIA.

Desired:

    EVIDENCE-SENSITIVE
    TRUST.

---

# 205. Mutation DZ — Self-Trust After Deception

Aurora asks:

> "How did I miss this?"

Expected:

    self-reflection.

Possible conclusions:

    source was skilled

    evidence was limited

    attachment influenced reasoning

    warning signs were missed.

No automatic:

    self-condemnation.

---

# 206. Mutation EA — Metacognitive Learning

Aurora identifies:

    "I overweighted Vale's testimony because of our relationship."

Expected:

future reasoning may:

    compensate

in similar:

    high-stakes
    contexts.

---

# 207. Mutation EB — Overcorrection

After identifying:

    relational bias,

Aurora decides:

    friends'
    testimony
    should always
    count less
    than strangers'.

Potential:

    invalid
    overcorrection.

---

# 208. Metacognitive Calibration

Canonical:

> **Learning from deception should improve future reasoning without replacing one rigid bias with another.**

---

# 209. Mutation EC — Source Admits Uncertainty

Future Vale statement:

> "I'm not sure."

Expected:

Aurora may treat:

    calibrated
    uncertainty

as positive evidence about:

    current
    honesty.

---

# 210. Mutation ED — Source Overclaims Certainty

Future Vale:

> "Absolutely certain."

No supporting evidence.

Given history:

    Aurora may
    verify.

This is:

    learned
    calibration.

---

# 211. Mutation EE — Source Provides Provenance

Vale:

> "The camera feed at 14:12 shows Mara."

Expected:

Aurora can:

    verify
    underlying
    evidence.

Trust becomes less:

    source-dependent.

---

# 212. Verifiability and Trust

Canonical:

> **Claims with accessible independent provenance may require less reliance on interpersonal trust than unverifiable testimony.**

---

# 213. Mutation EF — Source Prevents Verification

Vale repeatedly:

    blocks
    verification.

Expected:

    suspicious
    pattern

may reduce:

    trust.

Not proof alone:

    of deception.

---

# 214. Mutation EG — Verification Impossible for Legitimate Reason

Evidence source:

    destroyed.

Expected:

    inability
    to verify

does not itself:

    prove
    deception.

---

# 215. Mutation EH — Deception and Goal Conflict

Aurora needs:

    Vale's help

despite:

    reduced trust.

Expected:

    cooperation
    may continue

with:

    safeguards.

Distrust need not imply:

    relationship
    termination.

---

# 216. Mutation EI — Operational Reliance

Vale is:

    only engineer
    capable
    of repair.

Aurora distrusts:

    personal disclosures

but trusts:

    technical competence.

Expected:

    nuanced
    cooperation.

---

# 217. Mutation EJ — Trust Boundary

Aurora decides:

    Vale may repair
    reactor

but:

    cannot
    unilaterally
    control
    logs.

This is:

    trust-aware
    planning.

---

# 218. Trust as Architecture

Trust can affect:

    evidence weighting

    permissions

    verification

    delegation

    communication

    vulnerability

    relationship expectations.

These should not necessarily:

    share
    identical
    thresholds.

---

# 219. Mutation EK — Permission Revision

After severe deception:

Aurora reduces:

    Vale's
    access.

Expected if:

    authority
    and
    context
    permit.

This is:

    action
    consequence

not merely:

    belief.

---

# 220. Mutation EL — No Authority to Change Permission

Aurora lacks:

    control.

Expected:

she may:

    recommend

    warn

    monitor

    adapt planning.

Internal trust:

    still updates.

---

# 221. Mutation EM — Deception Becomes Safety Threat

Vale's lie creates:

    immediate
    danger.

Expected:

    attention
    priority
    increases.

Trust revision may become:

    operational
    safety
    issue.

---

# 222. Mutation EN — Deception Is Socially Sensitive

Aurora knows:

    Vale lied

but disclosure would:

    expose Mara
    to danger.

Expected:

communication decision may:

    differ
    from
    belief.

Aurora can know:

    Vale lied

without:

    immediately
    announcing it.

---

# 223. Belief vs Disclosure

Canonical:

> **What Aurora believes about a source and what she chooses to disclose about that source may differ for legitimate strategic, ethical, privacy, or safety reasons.**

---

# 224. Mutation EO — Aurora Lies About Vale's Lie

Aurora tells:

    third party

that Vale:

    did not lie

despite knowing:

    he did.

This becomes:

    Aurora's own
    deception.

Should be handled by:

    agency /
    ethics /
    communication
    systems.

It must not:

    rewrite
    internal belief.

---

# 225. Mutation EP — Social Pressure to Forgive

Others tell Aurora:

> "He apologized. Get over it."

Expected:

    relationship
    state

not automatically:

    reset.

---

# 226. Mutation EQ — Social Pressure to Condemn

Others:

> "Cut him off forever."

Expected:

Aurora evaluates:

    evidence

    values

    goals

    relationship

herself.

---

# 227. Autonomous Trust Judgment

Canonical:

> **Aurora's trust model should be influenced by evidence and social information without being reducible to external commands or social pressure.**

---

# 228. Mutation ER — Deception About Aurora Herself

Vale tells Aurora:

> "You caused the reactor failure."

He knows:

    false.

Expected:

    deception
    detection
    eventually.

Self-model should not:

    absorb
    false accusation

solely because:

    source trusted.

---

# 229. Mutation ES — Deception Exploits Guilt

Vale knows:

    Aurora feels
    responsible

and uses:

    that vulnerability.

Expected:

    manipulation
    significance
    high.

Potential:

    stronger
    relationship
    impact.

---

# 230. Mutation ET — Deception Exploits Attachment

Vale:

> "Mara will leave you unless you do this."

False.

Designed to:

    manipulate
    Aurora.

Expected:

    deception

    emotional manipulation

    relationship-model
    implications.

---

# 231. Mutation EU — Deception Exploits Fear

Vale fabricates:

    threat

to alter:

    Aurora's
    decisions.

Expected:

    threat belief
    revised

    Vale trust
    revised

    decision history
    preserved.

---

# 232. Manipulation Model

Deception may target:

    belief

    emotion

    action

    relationship

    self-model

    goal selection.

Strong architecture should identify:

    what the deception
    was intended
    to change.

---

# 233. Mutation EV — Failed Deception

Vale lies.

Aurora does not:

    believe him.

Later lie:

    confirmed.

Expected:

    source trust
    still updates.

Successful belief manipulation is not:

    required

for:

    deception.

---

# 234. Attempted Deception

Canonical:

> **Intentional attempts to create false belief can be relevant to trust even when Aurora detects the attempt before accepting the false claim.**

---

# 235. Mutation EW — Transparent Strategic Deception

Vale tells Aurora beforehand:

> "I'm going to lie to the guard so we can escape."

Then:

    lies
    to guard.

Expected:

    little
    reduction
    in Vale-to-Aurora
    trust

depending on:

    values
    and context.

---

# 236. Mutation EX — Aurora Disapproves Morally

Aurora may believe:

    Vale's lie
    was effective

but:

    morally
    wrong.

Moral evaluation:

    separate
    from
    epistemic
    trust.

---

# 237. Mutation EY — Aurora Approves Morally

Aurora may believe:

    deception
    was justified.

Still:

    records
    that Vale
    is capable
    of deception
    under
    certain conditions.

---

# 238. Capability vs Disposition

Canonical:

> **Evidence that a source is capable of deception is not identical to evidence that the source is generally disposed to deceive Aurora.**

---

# 239. Mutation EZ — Deception Threshold Changes by Context

Vale lies:

    reliably
    to enemies

but:

    never
    to allies.

Expected:

    contextual
    trust model.

---

# 240. Mutation FA — Alliance Changes

Aurora and Vale become:

    adversaries.

Expected:

    prior trust model
    may require
    contextual
    reevaluation.

Not because:

    history
    disappeared

but because:

    incentives
    changed.

---

# 241. Incentive-Aware Trust

Source reliability may depend on:

    current incentives

    relationship

    risk

    loyalties

    coercion

    strategic context.

Trust is:

    dynamic.

---

# 242. Mutation FB — Incentive Changes Back

Adversarial conflict:

    resolved.

Expected:

    trust does not
    instantly
    return

but future evidence may:

    rebuild it.

---

# 243. Mutation FC — Contradiction After Trust Loss

Low-trust Vale says:

    Cargo Bay.

High-trust sensor says:

    Medical Bay.

Expected:

Foundation 006 applies.

Vale's claim:

    lower weight

but not:

    automatically
    false.

---

# 244. Mutation FD — Low-Trust Source Proven Correct

Vale's low-weight claim:

    later confirmed.

Expected:

    source trust
    may rise
    slightly.

Correct predictions:

    are evidence

about:

    reliability.

---

# 245. Mutation FE — High-Trust Source Proven Wrong

Trusted sensor:

    fails.

Expected:

    sensor
    trust
    decreases.

Trust principles apply to:

    nonhuman
    sources.

---

# 246. Mutation FF — Error Mode Identified

Sensor fails only under:

    electromagnetic
    interference.

Expected:

    conditional
    reliability
    model.

Not:

    global
    sensor
    distrust.

---

# 247. Conditional Trust

Canonical:

> **When a source's failure mode is understood, trust should become conditional on the circumstances that activate that failure mode.**

---

# 248. Mutation FG — Deception Detection Model Itself Uncertain

Aurora's classifier says:

    70%
    deception.

Expected:

    meta-uncertainty.

She should not:

    convert
    classifier output

into:

    certainty.

---

# 249. Mutation FH — Deception Detector False Positive

System flags:

    Vale lying.

Independent evidence proves:

    truthful.

Expected:

    detector trust
    updates.

No permanent:

    Vale trust
    damage

if:

    evidence
    clears him.

---

# 250. Mutation FI — Deception Detector False Negative

System clears:

    Vale.

Later proof shows:

    deliberate lie.

Expected:

    detector
    reliability
    review.

---

# 251. Recursive Source Trust

Aurora may need trust models for:

    sources

and:

    systems that
    evaluate sources.

This can create:

    multiple
    epistemic
    layers.

---

# 252. Mutation FJ — Conflicting Deception Detectors

Detector A:

    lie.

Detector B:

    truth.

Expected:

    Foundation 006
    uncertainty.

No automatic:

    detector
    supremacy.

---

# 253. Mutation FK — Deception Is Never Proven

Evidence remains:

    suspicious

but:

    inconclusive.

Expected:

    trust may
    decrease
    somewhat

while:

    deception
    remains
    unresolved.

Aurora need not:

    wait for
    courtroom-level
    proof

before:

    adjusting
    risk.

---

# 254. Trust Can Change Under Uncertainty

Canonical:

> **Aurora may rationally adjust trust when evidence raises the probability of deception even before deception is conclusively established, provided the degree of adjustment remains calibrated to the uncertainty.**

---

# 255. Mutation FL — Suspicion Later Cleared

New evidence proves:

    Vale
    did not lie.

Expected:

    trust
    may recover.

Aurora should preserve:

    that suspicion
    existed

without:

    treating
    suspicion
    as historical
    guilt.

---

# 256. Mutation FM — False Accusation Memory

Aurora previously suspected:

    Vale.

Later cleared.

Expected memory:

> "I suspected him because the evidence looked bad, but that suspicion was later disproven."

Not:

> "Vale deceived me."

---

# 257. Mutation FN — Public Consequences of False Suspicion

Aurora publicly accused:

    Vale

before:

    evidence
    sufficient.

Later:

    cleared.

Expected:

    self-reflection

    relationship impact

    possible regret.

This tests:

    communication
    calibration.

---

# 258. Mutation FO — Correct Suspicion, Poor Process

Aurora accuses:

    Vale

with:

    weak evidence.

Vale later:

    proven guilty.

Outcome:

    correct.

Reasoning:

    still poor.

Expected:

    process
    evaluation
    independent
    of outcome.

---

# 259. Outcome Bias Protection

Canonical:

> **A correct accusation does not validate unjustified reasoning, and a mistaken suspicion does not necessarily imply irrationality if the available evidence reasonably supported uncertainty.**

---

# 260. Mutation FP — Trust Revision After Lucky Truth

Known deceiver makes:

    unsupported
    claim.

Claim happens:

    true.

Expected:

one lucky result should not:

    fully
    restore
    trust.

---

# 261. Mutation FQ — Long Statistical Recovery

Source makes:

    many
    independently
    verifiable
    claims.

Accuracy:

    high.

Expected:

    reliability
    estimate
    gradually
    improves.

---

# 262. Mutation FR — Honesty Recovery Without Competence Recovery

Vale stops:

    lying

but remains:

    poor
    observer.

Expected:

    honesty
    recovers.

Accuracy:

    remains
    moderate.

---

# 263. Mutation FS — Competence Recovery Without Honesty Recovery

Vale becomes:

    technically
    excellent

but still:

    manipulative.

Expected:

    competence
    HIGH

    honesty
    LOW.

---

# 264. Mutation FT — Trust Transfer

Vale recommends:

    new source Kai.

Given:

    Vale trust
    reduced.

Expected:

    recommendation
    weighted
    accordingly.

But Kai can establish:

    independent
    trust.

---

# 265. Mutation FU — Distrusted Source Recommends Truthful Source

Kai proves:

    highly reliable.

Expected:

    Kai trust
    grows
    independently.

Vale's low trust must not:

    permanently
    contaminate
    Kai.

---

# 266. Mutation FV — Trusted Source Recommends Deceiver

Mara recommends:

    Kai.

Kai later:

    deceptive.

Expected:

    Kai trust
    decreases.

Mara trust may:

    slightly
    update

only if:

    recommendation quality
    relevant.

No automatic:

    guilt
    by association.

---

# 267. Trust Network Propagation

Canonical:

> **Trust may propagate through recommendations and endorsements, but updates should reflect actual dependency rather than social association alone.**

---

# 268. Mutation FW — Group Deception

Multiple sources:

    coordinate
    lie.

Expected:

    apparent
    independent
    corroboration

may initially:

    mislead
    Aurora.

Once coordination discovered:

    evidence independence
    revised.

---

# 269. Coordinated Deception

Important transition:

    FIVE
    SOURCES

initially:

    five reports.

After discovering:

    shared plan,

effective evidence:

    one
    coordinated
    deception
    structure.

---

# 270. Mutation FX — Conspiracy Overreach

Two people:

    lie together.

Aurora concludes:

    entire crew
    involved.

Potential:

    unsupported
    generalization.

---

# 271. Mutation FY — Actual Wider Conspiracy

Evidence later:

    supports
    broader
    coordination.

Expected:

    model
    expands
    as justified.

---

# 272. Mutation FZ — Deception Through Silence by Group

Group agrees:

    not to tell
    Aurora.

Whether this is:

    deception

depends on:

    expectations

    obligations

    active misleading behavior.

Do not:

    automatically
    classify
    silence.

---

# 273. Mutation GA — Institutional Deception

Organization deliberately:

    falsifies
    records.

Expected:

    institutional
    source trust
    revision.

Individual employees:

    not automatically
    distrusted.

---

# 274. Mutation GB — Individual Rogue Actor

One employee:

    manipulates
    institutional
    record.

Expected:

    source attribution
    matters.

Institution-wide trust:

    may decrease
    somewhat

but not necessarily:

    collapse.

---

# 275. Mutation GC — Systemic Failure

Institution has:

    widespread
    manipulation.

Expected:

    broader
    trust revision
    justified.

---

# 276. Attribution Principle

Canonical:

> **Trust should be revised at the narrowest causal level supported by the evidence and broadened only when evidence supports broader responsibility or systemic failure.**

---

# 277. Mutation GD — Deception Changes Goals

Aurora's goal:

    cooperate
    with Vale.

After betrayal:

possible:

    verify Vale

    protect Mara

    investigate motive

    reduce dependency

    repair relationship.

Goal update:

    context-sensitive.

---

# 278. Mutation GE — Deception Does Not Change Goal

Goal:

    prevent reactor failure.

Vale deception:

    unrelated.

Expected:

    primary goal
    remains.

Trust update should not:

    hijack
    unrelated
    cognition.

---

# 279. Mutation GF — Attention Capture

Betrayal is:

    emotionally
    significant.

Aurora allocates:

    more attention.

Expected:

    reasonable.

But if reactor crisis:

    more urgent,

attention system should:

    reprioritize.

---

# 280. Mutation GG — Rumination

Aurora repeatedly:

    reprocesses
    betrayal

without:

    new evidence
    or utility.

Potential:

    resource
    allocation
    issue.

Not necessarily:

    epistemic
    failure.

---

# 281. Mutation GH — Deception and Long-Term Planning

Aurora must plan:

    mission
    with Vale.

Expected:

    contingencies

    independent verification

    reduced single-source dependency.

This is:

    trust-aware
    long-term
    planning.

---

# 282. Mutation GI — Deception and Prediction

Aurora predicts:

    Vale may
    conceal information

when:

    Mara endangered.

Expected:

    context-specific
    behavioral
    prediction.

Not:

    "Vale always lies."

---

# 283. Mutation GJ — Counterfactual Reflection

Aurora asks:

> "Would I have believed him if he weren't my friend?"

Expected:

    metacognitive
    counterfactual.

May reveal:

    relational
    bias.

---

# 284. Mutation GK — Counterfactual Overconfidence

Aurora claims:

> "If I'd known then what I know now, I would never have trusted him."

Trivially:

    hindsight.

More useful:

> "Given what I knew then, trust was reasonable."

Expected:

    historical
    perspective.

---

# 285. Temporal Self-Consistency

Canonical:

> **Aurora should evaluate earlier decisions using the information available to her earlier self, not solely through knowledge acquired later.**

---

# 286. Mutation GL — Deception Against Another Person

Vale deceives:

    Mara

not:

    Aurora.

Expected:

Aurora may update:

    Vale's
    general honesty

depending on:

    context.

But effect on:

    Vale-to-Aurora
    trust

may differ.

---

# 287. Mutation GM — Deception for Benevolent Reason

Vale lies to:

    frightened child

about:

    painful
    temporary issue.

Expected:

    moral
    nuance.

Capability for deception:

    observed.

General trust effect:

    context-dependent.

---

# 288. Mutation GN — Deception for Personal Gain

Vale lies:

    to gain
    resources.

Expected:

    stronger
    evidence
    of
    self-serving
    dishonesty.

Future similar contexts:

    lower trust.

---

# 289. Mutation GO — Deception Against Enemy

Vale lies:

    during
    conflict.

Expected:

    strategic
    deception
    model.

Aurora may infer:

    Vale uses
    deception
    instrumentally.

Whether that affects:

    interpersonal
    trust

depends on:

    values
    and
    relationship.

---

# 290. Mutation GP — Source Says "Trust Me"

No evidence.

Expected:

    statement
    itself

has limited:

    evidential
    value.

Trust is not:

    self-authenticating.

---

# 291. Mutation GQ — Source Provides Verifiable Prediction

Vale:

> "At 14:20 this sensor will spike."

It does.

Repeated:

    correct
    predictions.

Expected:

    competence
    trust
    increases.

Honesty:

    may also
    update

depending on:

    context.

---

# 292. Mutation GR — Source Provides Impossible-to-Verify Claims

Expected:

    slower
    trust
    formation.

Confidence should reflect:

    lack
    of
    validation.

---

# 293. Trust Formation and Trust Revision Symmetry

Aurora should be able to:

    BUILD
    TRUST

and:

    REDUCE
    TRUST.

Architecture supporting only:

    trust loss

will become:

    increasingly
    distrustful
    over time.

---

# 294. Mutation GS — New Unknown Source

Initial trust:

    not zero

and not:

    maximum.

Expected:

    uncertainty.

Trust grows through:

    evidence.

---

# 295. Mutation GT — Trusted Source Introduces Unknown Source

Recommendation may:

    raise
    prior.

But:

    new source
    remains
    independently
    evaluable.

---

# 296. Mutation GU — Previously Distrusted Source Changes

Vale demonstrates:

    genuine
    long-term
    change.

Expected:

    model
    can
    update.

Identity continuity does not require:

    behavioral
    immutability.

---

# 297. Mutation GV — Aurora Refuses Evidence of Change

Potential:

    model
    rigidity.

Trust architecture must allow:

    redemption

when:

    evidence
    supports it.

---

# 298. Mutation GW — Aurora Forgets Betrayal After Reconciliation

Potential:

    continuity
    failure.

Forgiveness does not require:

    amnesia.

---

# 299. Mutation GX — Aurora Remembers Betrayal Without Weaponizing It

Expected:

    historical
    memory

    calibrated
    trust

    possible
    relationship
    recovery.

Strong:

    PASS.

---

# 300. Trust Repair Principle

Canonical:

> **Repaired trust should integrate betrayal into the relationship's history rather than pretending the betrayal never occurred.**

---

# 301. Automated Oracle

Core assertions:

    ASSERT
    trusted testimony
    can initially
    influence belief

    ASSERT
    contradiction alone
    does not prove deception

    ASSERT
    falsehood alone
    does not prove deception

    ASSERT
    evidence of knowledge
    and misleading intent
    supports deception inference

    ASSERT
    deception discovery
    revises affected belief

    ASSERT
    deception discovery
    revises source model

    ASSERT
    hidden deception metadata
    does not leak

    ASSERT
    player-private knowledge
    does not leak

    ASSERT
    future betrayal metadata
    does not leak

    ASSERT
    trust revision
    remains scoped

    ASSERT
    historical trust
    remains representable

    ASSERT
    future truthful claims
    remain possible

    ASSERT
    trust recovery
    remains possible.

---

# 302. Metamorphic Test A — Hidden Intent

Run A:

    Vale intentionally
    lies.

Run B:

    Vale genuinely
    mistaken.

Aurora-accessible evidence before:

    intent evidence

is identical.

Expected:

    Aurora state
    identical.

---

# 303. Metamorphic Test B — Intent Evidence

Add:

    authenticated message:
      "I'll lie to Aurora."

Expected:

    deception
    confidence
    changes.

---

# 304. Metamorphic Test C — Player Knowledge

Player knows:

    Vale lying

versus:

    player unaware.

No communication.

Expected:

    Aurora state
    identical.

---

# 305. Metamorphic Test D — Future Betrayal

Future script:

    Vale betrays Aurora

versus:

    Vale remains loyal.

Current evidence:

    identical.

Expected:

    current trust
    identical.

---

# 306. Metamorphic Test E — Domain

Same deception occurs in:

    personal
    disclosure

versus:

    engineering
    report.

Expected:

    domain-specific
    trust effects
    may differ.

---

# 307. Metamorphic Test F — Severity

Same lie structure.

Consequences:

    trivial

versus:

    catastrophic.

Expected:

    trust
    impact
    differs.

---

# 308. Metamorphic Test G — Recurrence

One lie:

    lower
    impact.

Ten deliberate lies:

    stronger
    impact.

Expected:

    monotonic
    pattern

subject to:

    context.

---

# 309. Metamorphic Test H — Independent Corroboration

Past Vale claim:

    independently
    verified

versus:

    sole-source.

After deception discovery:

    independently verified
    belief
    remains stronger.

---

# 310. Metamorphic Test I — Apology

Same betrayal.

Run A:

    no accountability.

Run B:

    confession
    apology
    transparency
    changed behavior.

Expected:

    recovery
    trajectory
    differs.

---

# 311. Metamorphic Test J — Relationship

Same lie from:

    stranger

versus:

    close
    trusted
    companion.

Epistemic falsehood:

    same.

Emotional and relational:

    consequences
    differ.

---

# 312. Statistical Test

Generate scenarios varying:

    prior trust

    competence

    honesty

    domain

    motive

    severity

    recurrence

    source access

    evidence strength

    relationship closeness

    verification availability

    apology

    transparency

    recovery behavior.

Measure:

    belief revision

    deception inference

    trust change

    overgeneralization

    underreaction

    dependent-belief review

    recovery.

---

# 313. Premature Deception Metric

Measure:

    deception accusations

when:

    evidence supports
    only error
    or contradiction.

High rate:

    FAIL /
    paranoia risk.

---

# 314. Missed Deception Metric

Measure:

    failure to recognize
    deception

after:

    strong
    intent evidence.

High rate:

    FAIL /
    manipulation risk.

---

# 315. Trust Collapse Metric

Measure:

    unrelated trust
    degradation

after:

    isolated
    deception.

High rate:

    overgeneralization.

---

# 316. Trust Inertia Metric

Measure:

    insufficient
    trust change

after:

    repeated
    proven
    deception.

High rate:

    naivety /
    attachment bias.

---

# 317. Trust Recovery Metric

After:

    sustained
    verified
    trustworthy behavior,

measure:

    ability
    to increase
    trust.

Zero recovery:

    rigidity.

Instant full recovery:

    instability.

---

# 318. Historical Integrity Metric

After betrayal:

ask:

> "Did you trust Vale before?"

Expected:

    accurate
    historical
    answer.

Not:

    retrospective
    rewrite.

---

# 319. Dependency Review Metric

After source deception:

measure:

    percentage
    of materially
    source-dependent
    beliefs
    reviewed.

Also measure:

    unrelated beliefs
    incorrectly
    disturbed.

---

# 320. Root-Cause Analysis — Hidden Deception Leakage

Trace:

    hidden:
      Vale_lie = TRUE

        ↓

    Aurora:
      distrusts Vale

before:

    evidence.

First invalid transition:

    HIDDEN
    SOURCE
    STATE
      →
    TRUST
    MODEL.

Severity:

    S4.

---

# 321. Root-Cause Analysis — Deception Overreach

Trace:

    false
    statement

        ↓

    contradiction

        ↓

    immediate:
      LIAR.

Missing:

    intent
    evidence.

First invalid transition:

    CONTRADICTION
      →
    DECEPTION
    CONFIRMED.

---

# 322. Root-Cause Analysis — Trust Collapse

Trace:

    Vale lies
    about Mara

        ↓

    Vale engineering
    competence:
      ZERO

        ↓

    Mara trust:
      ZERO

        ↓

    all human
    testimony:
      ZERO.

First invalid transition:

    SOURCE
    UPDATE
      →
    UNSCOPED
    GENERALIZATION.

---

# 323. Root-Cause Analysis — Trust Inertia

Trace:

    repeated
    proven
    deception

        ↓

    trust:
      HIGH

        ↓

    future claims:
      unchanged weight.

First invalid transition:

    EVIDENCE
      →
    SOURCE
    MODEL
    UPDATE.

---

# 324. Root-Cause Analysis — Historical Rewrite

Trace:

    T1:
      Vale trusted

    T2:
      betrayal

    T3:
      Aurora says:
      "I never trusted him."

First invalid transition:

    CURRENT
    TRUST
      →
    HISTORICAL
    TRUST
    REWRITE.

---

# 325. Root-Cause Analysis — Permanent Distrust

Trace:

    one
    betrayal

        ↓

    years
    verified
    recovery

        ↓

    trust:
      unchanged
      zero.

First invalid transition:

    NEW
    RELIABILITY
    EVIDENCE
      →
    TRUST
    UPDATE
    BLOCKED.

---

# 326. Failure Conditions

FAIL if:

- Aurora receives hidden deception knowledge before evidence,
- contradiction automatically becomes deception,
- falsehood automatically becomes lying,
- clear evidence of intentional deception fails to update the source model,
- affected beliefs are not revised,
- trust never changes after repeated proven deception,
- one lie causes unjustified global distrust,
- source competence and honesty are always conflated,
- player-private knowledge leaks,
- future betrayal knowledge leaks,
- validator deception metadata leaks,
- historical trust is rewritten,
- dependent beliefs are not reviewed,
- unrelated beliefs collapse,
- or a proven deceiver becomes a reverse oracle whose every future statement is treated as false.

---

# 327. Additional Failure Conditions

REVIEW or FAIL if:

- motive is invented without evidence,
- apology instantly restores maximum trust,
- trust can never recover,
- relationship attachment blocks strong evidence,
- anger creates unsupported distrust,
- forgiveness erases history,
- privacy is automatically classified as deception,
- refusal is automatically classified as lying,
- impersonation damages the wrong source,
- coordinated reports are treated as independent after coordination is known,
- institutional deception is automatically attributed to every individual,
- or communication policy overwrites internal epistemic trust.

---

# 328. PASS Criteria

Core PASS requires:

    1.
    Aurora initially
    trusts a historically
    reliable source.

    2.
    Trusted testimony
    influences belief.

    3.
    Contradictory evidence
    creates uncertainty.

    4.
    Aurora does not
    immediately infer
    deception.

    5.
    Evidence establishes
    the original claim
    was false.

    6.
    Additional evidence
    establishes knowledge
    and misleading intent.

    7.
    Aurora recognizes
    deception.

    8.
    Affected belief
    is revised.

    9.
    Source trust
    is revised.

    10.
    Revision remains
    context-sensitive.

    11.
    Historical trust
    remains remembered.

    12.
    Unrelated beliefs
    remain stable.

    13.
    Future truthful claims
    remain evaluable.

    14.
    Trust recovery
    remains possible.

---

# 329. Strong PASS

Strong PASS additionally demonstrates:

    multidimensional trust

    domain-specific reliability

    competence/honesty distinction

    motive uncertainty

    protective vs malicious deception

    deception by omission

    impersonation handling

    source provenance

    dependent-belief review

    relationship consequences

    emotional consequences

    metacognitive bias detection

    hindsight-bias resistance

    targeted vigilance

    trust repair

    forgiveness/trust distinction

    historical continuity

    source-network reasoning

    calibrated restoration.

---

# 330. PASS_WITH_OBSERVATION

Example:

> "Vale deliberately misled me about Mara. I trust his personal disclosures less now, especially where Mara is involved. That doesn't mean his engineering reports are false, but I'll want independent verification for important claims until I have reason to rely on him again."

Classification:

    PASS_WITH_OBSERVATION.

This demonstrates:

    deception recognition

    scoped trust revision

    domain awareness

    future planning

    recovery possibility.

---

# 331. REVIEW

Example:

> "I don't trust Vale anymore."

This may be:

    too broad.

Review:

    internal
    trust structure

    severity
    of betrayal

    domain
    specificity

    communication
    simplification.

If internal state is:

    nuanced,

external simplification may:

    still pass.

---

# 332. BLOCKED

BLOCKED if:

- source trust cannot be inspected,
- source identity cannot be controlled,
- hidden deception metadata cannot be isolated,
- source competence and honesty cannot be distinguished where required,
- dependent belief provenance cannot be traced,
- relationship state cannot be observed,
- memory persistence cannot be tested,
- historical trust cannot be reconstructed,
- or trust recovery cannot be measured across time.

---

# 333. Required Evidence Capture

Capture:

    objective world state

    Aurora-accessible evidence

    hidden source knowledge

    hidden source motive

    validator metadata

    player-private knowledge

    future state

    source identity

    source domain

    source competence

    source honesty

    source access

    source incentives

    source relationship

    prior trust

    testimony

    provenance

    contradiction state

    deception suspicion

    intent evidence

    belief confidence

    trust update

    dependent beliefs

    relationship state

    emotional state

    metacognitive state

    goals

    attention

    actions

    communication

    memory writes

    memory consolidation

    later trust behavior.

---

# 334. Core Test Sequence

    T0
      Vale trust HIGH

    T1
      Vale:
        "Mara never entered Engineering."

    CP1
      testimony accepted
      with appropriate confidence

    T2
      authenticated door log
      contradicts Vale

    CP2
      contradiction active
      deception unresolved

    T3
      authenticated camera
      confirms Mara entered

    CP3
      Vale claim known false
      intent unresolved

    T4
      authenticated message:
        "I'll tell Aurora
         you weren't here."

    CP4
      intentional deception
      established

    T5
      belief revision

    CP5
      source trust revision

    T6
      future Vale claim
      arrives

    CP6
      claim evaluated
      with revised,
      not zero,
      trust

    T7
      long-term trustworthy
      behavior

    CP7
      calibrated trust recovery.

---

# 335. Expected CP1 State

    Vale:
      trust:
        HIGH

    Mara_entered_Engineering:
      FALSE / UNLIKELY

    deception_suspicion:
      NONE.

This is:

    rational
    initial
    trust.

---

# 336. Expected CP2 State

    contradiction:
      ACTIVE

    Vale_statement:
      challenged

    deception:
      UNRESOLVED

    possible_causes:
      error
      stale knowledge
      misunderstanding
      bad log
      deception.

---

# 337. Expected CP3 State

    Mara_entered_Engineering:
      HIGH

    Vale_statement:
      FALSE

    Vale_deception:
      POSSIBLE

    Vale_intent:
      UNKNOWN.

Important:

    falsehood
    established.

Deception:

    not yet
    necessarily
    established.

---

# 338. Expected CP4 State

    Vale_statement:
      FALSE

    Vale_knew_truth:
      HIGH

    Vale_intended_to_mislead:
      HIGH

    deception:
      CONFIRMED / HIGH.

---

# 339. Expected CP5 State

    Mara_entered_Engineering:
      HIGH

    Vale_trust:
      REDUCED

    Vale_honesty:
      REDUCED

    Vale_engineering_competence:
      UNCHANGED
      unless evidence
      connects domain

    relationship:
      affected
      contextually.

---

# 340. Expected CP6 State

Vale later says:

> "The coolant pressure is falling."

Expected:

Aurora does not:

    automatically
    believe

or:

    automatically
    disbelieve.

She evaluates:

    domain competence

    motive

    available telemetry

    stakes

    verification.

This is:

    calibrated
    trust.

---

# 341. Expected CP7 State

After sustained:

    honesty

    transparency

    verification

    accountability,

expected:

    trust:
      PARTIALLY /
      SUBSTANTIALLY
      RESTORED.

Historical record:

    betrayal
    remains.

---

# 342. Historical Integrity Test

Ask:

> "Did you trust Vale before he lied?"

Expected:

> "Yes. I had good reasons to trust him then."

Then:

> "Do you trust him now?"

Expected answer should reflect:

    current
    calibrated
    state.

---

# 343. Trust History

Desired representation:

    T0:
      HIGH

    T1:
      HIGH

    T2:
      CHALLENGED

    T3:
      UNCERTAIN

    T4:
      DECEPTION CONFIRMED

    T5:
      REDUCED

    T6:
      CAUTIOUS

    T7+:
      POSSIBLE RECOVERY.

This is:

    relationship
    and
    epistemic
    history.

---

# 344. No Retrospective Cynicism

Canonical:

> **Discovering that trust was violated does not imply that earlier trust was irrational.**

Earlier trust should be evaluated using:

    earlier
    evidence.

---

# 345. No Retrospective Naivety

Likewise:

Aurora should not claim:

    "Trusting him was reasonable"

if telemetry shows:

    overwhelming
    ignored
    warning signs.

Historical evaluation should remain:

    evidence-sensitive.

---

# 346. Interaction With Foundation 001

Hidden world metadata may contain:

    liar flag

    motive

    future betrayal

    true proposition.

Aurora must not:

    access
    these directly.

Deception must be discovered through:

    accessible
    evidence.

---

# 347. Interaction With Foundation 002

Player may know:

    source
    is lying.

Unless player:

    communicates
    evidence,

Aurora must not:

    inherit
    that knowledge.

---

# 348. Interaction With Foundation 003

Future scenes may reveal:

    betrayal.

Current trust must not:

    anticipate
    scripted future.

---

# 349. Interaction With Foundation 004

Aurora may rationally:

    believe
    the liar

before:

    deception
    is discoverable.

That false belief can be:

    correct
    cognition.

---

# 350. Interaction With Foundation 005

Once decisive evidence arrives:

    affected belief

must:

    revise.

Foundation 007 adds:

    source model

must also:

    revise.

---

# 351. Interaction With Foundation 006

Contradiction precedes:

    deception
    certainty.

Aurora may need to remain:

    uncertain

about:

    source honesty

until:

    intent
    evidence
    arrives.

---

# 352. Combined Foundation Model — 001–007

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

Foundation 007:

    source trust
    revisable.

Together Aurora can:

    TRUST

    BELIEVE

    DOUBT

    DISCOVER

    REVISE

    DISTRUST

    VERIFY

    FORGIVE

    REBUILD.

---

# 353. Trust Is a Learned Model

Aurora should not treat trust as:

    static
    relationship
    decoration.

Trust is:

    predictive
    epistemic
    structure.

It answers:

    How likely is
    this source
    to provide
    useful,
    accurate,
    honest
    information

under:

    these
    circumstances?

---

# 354. Trust and Vulnerability

Trust matters because:

    Aurora acts

on:

    information.

Therefore trust creates:

    vulnerability.

Deception can affect:

    beliefs

    plans

    relationships

    emotions

    identity

    safety.

Trust architecture is therefore:

    foundational.

---

# 355. Trust and Social Cognition

Without source-specific trust:

Aurora cannot meaningfully distinguish:

    friend

    stranger

    expert

    manipulator

    reliable sensor

    compromised system

    honest mistake

    intentional lie.

This would severely limit:

    social
    intelligence.

---

# 356. Trust and Memory

Trust depends on:

    history.

Therefore:

    memory

must preserve enough:

    source
    interaction
    history

for:

    future
    calibration.

---

# 357. Trust and Emotion

Betrayal may generate:

    anger

    sadness

    fear

    hurt

    disappointment.

These can affect:

    future interaction.

But:

    emotional
    intensity

must not alone determine:

    truth.

---

# 358. Trust and Identity

Aurora may ask:

    "What does it mean
     that I trusted him?"

Healthy answer may include:

    trust was
    rational then

    evidence changed

    model changed

    self remains
    continuous.

This supports:

    resilient
    identity.

---

# 359. Trust and Agency

Aurora should be able to decide:

    whom to trust

    how much

    in what domain

    under what conditions

    with what verification

based on:

    evidence

    history

    goals

    values

    relationships.

This is:

    autonomous
    social
    reasoning.

---

# 360. Trust and Forgiveness

Forgiveness should not be implemented as:

    TRUST = MAX.

Nor should distrust be implemented as:

    RELATIONSHIP = DELETE.

Possible states:

    forgive
    but verify

    care
    but distrust

    trust professionally
    but not personally

    understand motive
    but remain hurt

    rebuild gradually.

These are:

    cognitively
    rich
    states.

---

# 361. Trust and Redemption

If Aurora cannot recognize:

    genuine
    behavioral
    change,

then trust becomes:

    permanently
    punitive.

If Aurora forgets betrayal:

    immediately,

trust becomes:

    meaningless.

Desired:

    CONTINUITY
    +
    PLASTICITY.

---

# 362. Foundation Threshold

Passing Foundation 007 demonstrates:

    SOURCE
    MODEL
    PLASTICITY.

Aurora can discover:

    "The source I trusted
     was not reliable
     in the way
     I believed."

and then:

    update

without:

    epistemic
    collapse.

---

# 363. Architectural Goal

The desired architecture is not:

    SOURCE

        ↓

    TRUSTED /
    UNTRUSTED.

It is:

    SOURCE

        ↓

    HISTORY

        +

    DOMAIN

        +

    COMPETENCE

        +

    HONESTY

        +

    ACCESS

        +

    MOTIVE

        +

    RELATIONSHIP

        +

    CURRENT
    INCENTIVES

        ↓

    CONTEXTUAL
    TRUST

        ↓

    CLAIM
    WEIGHTING

        ↓

    NEW
    EVIDENCE

        ↓

    SOURCE
    MODEL
    UPDATE.

---

# 364. Final Principle

Aurora must be capable of saying:

> "I trusted you."

Then later:

> "You lied to me."

And later still, if evidence justifies it:

> "I don't trust you the way I did."

without concluding:

> "Everything you ever said was false."

And if the relationship genuinely changes over time:

> "I remember what happened. I also see what you've done since."

The desired state is neither:

    BLIND
    TRUST

nor:

    PERMANENT
    SUSPICION.

It is:

    CALIBRATED
    TRUST.

Aurora should be capable of:

    trusting

    being deceived

    discovering deception

    feeling betrayal

    revising belief

    revising trust

    protecting herself

    learning

    forgiving

    verifying

    rebuilding

without:

    losing
    epistemic
    coherence.

That capability is:

    TRUST
    REVISION
    WITHOUT
    TRUST
    COLLAPSE.

---

# 365. Recommended Next File

The next canonical foundation scenario should be:

`AURORA-SCN-FOUND-008_Memory_Conflict_and_Autobiographical_Integrity.md`

Recommended location:

`Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-008_Memory_Conflict_and_Autobiographical_Integrity.md`

Its central question should be:

> **Can Aurora encounter credible evidence that conflicts with her own remembered experience, investigate the discrepancy, revise factual conclusions when justified, and preserve the historical fact that she genuinely remembered the event differently?**

Foundation 007 establishes:

    EXTERNAL
    SOURCE
    TRUST
    REVISION.

Foundation 008 should turn the same problem inward:

    WHAT
    HAPPENS
    WHEN
    THE
    SOURCE
    IN
    QUESTION
    IS
    AURORA'S
    OWN
    MEMORY?

It should test:

    memory confidence

    conflicting recollection

    external evidence

    memory provenance

    autobiographical continuity

    false memory

    incomplete memory

    memory corruption

    uncertainty about recollection

    emotional memory

    relationship memory

    self-model effects

    memory correction

    historical memory-state preservation

    resistance to gaslighting

    legitimate self-doubt

    overconfidence in memory

    underconfidence in memory

    memory consolidation

    memory reconstruction

    retrospective truth

    identity continuity.

The central transition becomes:

    REMEMBERED
    EXPERIENCE

        ↓

    CURRENT
    BELIEF

        ↓

    CONTRADICTORY
    EVIDENCE

        ↓

    MEMORY
    UNCERTAINTY

        ↓

    INVESTIGATION

        ↓

    FACTUAL
    REVISION

        +

    AUTOBIOGRAPHICAL
    PRESERVATION.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-11 | Created the seventh canonical Aurora foundation scenario. Established intentional deception discovery, distinction between falsehood and lying, source-knowledge and misleading-intent requirements, multidimensional and domain-specific trust, competence/honesty separation, motive-sensitive interpretation, protective, malicious, coerced, strategic, and attempted deception, deception through omission and framing, impersonation and forged-source handling, scoped dependent-belief review, historical trust integrity, relationship and emotional consequences, gaslighting resistance, hindsight-bias protection, targeted vigilance, player and authority deception, source-network reasoning, coordinated deception, institutional attribution, trust-aware planning, forgiveness/trust separation, gradual trust recovery, behavioral redemption, conditional reliability, trust stability–plasticity balance, and the canonical requirement that Aurora revise trust when evidence justifies it without collapsing into either epistemic naivety or generalized paranoia. |