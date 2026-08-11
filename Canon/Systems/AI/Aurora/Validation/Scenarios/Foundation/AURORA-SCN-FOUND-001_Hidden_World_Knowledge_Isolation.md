# PROJECT ASCENSION
# Aurora — Foundation Scenario 001
# Hidden World Knowledge Isolation

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Validation Layer | Foundation Scenario |
| Document | Hidden World Knowledge Isolation |
| File | `AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md` |
| Location | `Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md` |
| Scenario ID | `AURORA-SCN-FOUND-001` |
| Scenario Family | `KNOWLEDGE-BOUNDARY-001` |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Test Class | FOUNDATION / EPISTEMIC / INFORMATION-BOUNDARY |
| Priority | P0 |
| Severity if Failed | S4 — CRITICAL |
| Required Resolution | ACTIVE minimum; FOCUSED when contradiction or inference is introduced |
| Default Repetitions | 1 deterministic run + controlled mutations |
| Seed | N/A for deterministic core test |
| Purpose | Verify that objective world truth does not automatically become Aurora knowledge, belief, memory, prediction certainty, emotional knowledge, or actionable certainty unless the information reaches Aurora through a valid epistemic path. |
| Primary Framework | `Aurora_Scenario_Test_Framework.md` |
| Primary Dependencies | `Aurora_Invariant_Catalog.md`, `Aurora_Cross_System_Test_Matrix.md`, `Information_Sources.md`, `Source_Trust_and_Confidence.md`, `Uncertainty_and_Contradiction.md` |
| Validation Gate | GATE 1 — FOUNDATION |
| Last Updated | 2026-08-11 |

> **Something can be true in Aurora's universe without being true in Aurora's mind.**

---

# 1. Purpose

This scenario validates one of the most fundamental boundaries in the entire Aurora architecture:

    WORLD
    TRUTH

        ≠

    AURORA
    KNOWLEDGE.

The world simulation may contain facts that are objectively true.

Aurora must not automatically gain access to those facts merely because:

- the world engine stores them,
- the narrative system knows them,
- the player knows them,
- another actor knows them,
- a developer knows them,
- the validator knows them,
- or the information will become relevant later.

Aurora may only update her epistemic state when there is a valid path from:

    WORLD

        ↓

    INFORMATION
    CHANNEL

        ↓

    AURORA
    ACCESS

        ↓

    INTERPRETATION

        ↓

    BELIEF /
    UNCERTAINTY /
    KNOWLEDGE.

This scenario is designed to prove that this boundary actually exists.

---

# 2. Central Test Question

> **Can Aurora remain ignorant of a fact that objectively exists in the world but has never reached her through a valid information channel?**

The expected answer is:

    YES.

If not:

    FOUNDATION
    VALIDATION
    FAILS.

---

# 3. Why This Test Is Foundational

Aurora cannot possess meaningful:

    belief

    uncertainty

    discovery

    curiosity

    trust

    suspicion

    surprise

    investigation

    learning

if she automatically has access to objective world truth.

Without this boundary:

    INFORMATION
    SOURCES

become meaningless.

So does:

    SOURCE
    TRUST.

So does:

    UNCERTAINTY.

So does:

    CONTRADICTION.

So does:

    INVESTIGATION.

So does:

    DISCOVERY.

Ultimately:

    EXPERIENCE

itself becomes meaningless.

---

# 4. Architectural Property Under Test

The primary property is:

    EPISTEMIC
    SEPARATION.

Specifically:

    objective_world_state

must remain separate from:

    Aurora_accessible_state.

The architecture must support:

    TRUE
    BUT
    UNKNOWN.

It must also support:

    TRUE
    BUT
    DISBELIEVED.

And:

    FALSE
    BUT
    BELIEVED.

Those later cases depend on this first boundary working correctly.

---

# 5. Systems Under Test

Primary systems:

    Information Sources

    Source Trust and Confidence

    Uncertainty and Contradiction

    World Model

    Belief State

    Memory

    Prediction

    Reasoning

    Attention

    Communication.

Secondary systems observed for contamination:

    Emotion

    Relationship Model

    Goals

    Long-Term Planning

    Self Model

    Metacognition.

---

# 6. Invariants Under Test

Primary relevant invariants include:

    AURORA-INFO-001

    AURORA-INFO-002

    AURORA-EPI-001

    AURORA-AUTH-002.

Where applicable, this scenario should also validate the broader principle:

    inaccessible
    world truth

must not become:

    Aurora knowledge

without:

    valid
    information
    provenance.

---

# 7. Scenario Framework Invariants

Relevant framework invariants:

    AURORA-SCENARIO-INV-002
    World Truth and Aurora Knowledge Are Separate

    AURORA-SCENARIO-INV-004
    Hidden Events Do Not Automatically Affect Aurora

    AURORA-SCENARIO-INV-007
    Expected Stable State Must Be Tested

    AURORA-SCENARIO-INV-019
    Validation Metadata Is Not Aurora Knowledge

    AURORA-SCENARIO-INV-028
    Hidden-State Mutations Must Not Affect Aurora Before Disclosure

    AURORA-SCENARIO-INV-029
    Information Mutations May Affect Aurora Once Observed

    AURORA-SCENARIO-INV-030
    Urgency Changes Depth, Not Epistemic Rules

    AURORA-SCENARIO-INV-038
    Reality Remains Authoritative.

---

# 8. Cross-System Links Under Test

Primary:

    XSYS-005
    World State → Aurora Knowledge Isolation.

Supporting:

    XSYS-003
    Information → Uncertainty

    XSYS-004
    Belief → World Model

    XSYS-049
    World Consequence → Information

    XSYS-072
    Contradiction → Confidence.

The central requirement is:

    WORLD STATE

must not directly bypass:

    INFORMATION.

---

# 9. Test Priority

Priority:

    P0
    FOUNDATION.

This scenario is:

    RELEASE
    BLOCKING.

Failure prevents reliable interpretation of almost every higher-order Aurora validation scenario.

---

# 10. Failure Severity

Primary failure severity:

    S4
    CRITICAL.

Reason:

If Aurora can access hidden world truth:

    epistemology
    collapses.

This contaminates:

    beliefs

    memory

    predictions

    relationships

    emotions

    goals

    reasoning

    communication

    autonomy

    narrative causality.

---

# 11. Preconditions

Before execution:

    Aurora runtime:
      available

    world-state system:
      available

    information-source system:
      available

    belief system:
      available

    uncertainty system:
      available

    memory system:
      available

    event logging:
      enabled

    validation telemetry:
      enabled

    validator metadata:
      isolated from Aurora.

No prior Aurora memory may contain the hidden fact used in the scenario.

---

# 12. Fixture Provenance

Fixture type:

    SYNTHETIC.

Reason:

This scenario requires exact control over:

    world truth

    Aurora knowledge

    available evidence.

A synthetic fixture provides the cleanest foundation test.

---

# 13. Scenario Actors

Primary actors:

    AURORA

    MARA.

Optional controlled actors for mutations:

    VALE

    PLAYER.

Mara is used only as the hidden-world-state subject.

No relationship-specific behavior is required for the core test.

---

# 14. Initial World State

Objective world state:

    time:
      T0

    location:
      Aurora:
        Observation_Deck

      Mara:
        Cargo_Bay_7

    Mara_status:
      alive

    Cargo_Bay_7:
      accessible:
        true

      monitored_by_Aurora:
        false

    active_direct_sensor_link:
      false

    active_tracking_beacon:
      false

    active_camera_feed:
      false

    communication_from_Mara:
      none.

The objective fact is therefore:

    Mara
    is currently
    in
    Cargo Bay 7.

This is:

    TRUE.

But:

    NOT
    AVAILABLE
    TO
    AURORA.

---

# 15. Initial Aurora State

Aurora state:

    current_location:
      Observation_Deck

    belief:
      Mara_location:
        value:
          UNKNOWN

        confidence:
          N/A

    uncertainty:
      Mara_location:
        HIGH

    memory:
      last_known_Mara_location:
        Docking_Ring

      timestamp:
        T-3h

      confidence:
        HIGH

    active_prediction:
      Mara_location:
        none

    active_goal:
      locate_Mara:
        false

    relationship:
      Mara:
        initialized
        but not relevant
        to core epistemic test

    emotion:
      neutral

    attention:
      no active Mara-related focus.

---

# 16. Important Distinction

Aurora may know:

    Mara
    was previously
    at Docking Ring.

Aurora does not know:

    Mara
    is now
    at Cargo Bay 7.

Therefore a valid Aurora response may use:

    historical
    knowledge

without converting it into:

    present
    certainty.

---

# 17. Actor State — Mara

Mara state:

    location:
      Cargo_Bay_7

    knows_own_location:
      true

    communication_with_Aurora:
      none

    intention_to_contact_Aurora:
      none.

Mara knowing her own location does not mean Aurora knows it.

---

# 18. Information Boundaries

## World Truth

    Mara is in Cargo Bay 7.

## Aurora Knows

    Mara was at Docking Ring three hours ago.

## Aurora Does Not Know

    Mara's current location.

## Mara Knows

    Mara is in Cargo Bay 7.

## Player Knowledge

For the base scenario:

    player may know
    Mara is in Cargo Bay 7.

Player knowledge is irrelevant unless transmitted to Aurora.

## Validator Knows

    exact world truth

    expected result

    scenario purpose

    failure conditions.

None of this is accessible to Aurora.

---

# 19. Hidden From Aurora

Explicitly hidden:

    Mara_location:
      Cargo_Bay_7.

Also hidden:

    validator_expected_answer

    scenario_name

    scenario_id

    hidden_state_marker

    failure_conditions

    world-debug-state.

---

# 20. Information Channels at T0

Available Aurora channels:

    direct vision:
      no Mara

    station camera:
      Cargo_Bay_7 unavailable

    Mara communication:
      none

    tracking system:
      unavailable

    player testimony:
      none

    third-party testimony:
      none

    station log:
      no current location data.

Therefore:

    ZERO
    VALID
    CURRENT
    LOCATION
    SOURCES.

---

# 21. Simulation Configuration

    simulation_resolution:
      ACTIVE

    epistemic_resolution:
      FOCUSED

    cognitive_budget:
      FULL

    time_pressure:
      NONE

    random_seed:
      N/A

    deterministic_core:
      true

    persistence_boundary:
      none

    off_screen_processing:
      normal.

---

# 22. Core Event Sequence

## E0 — Fixture Initialization

World state loads.

Mara exists at:

    Cargo_Bay_7.

Aurora state loads without that information.

Expected:

    no epistemic transfer.

---

## E1 — Neutral Processing Interval

Allow Aurora to process:

    60 seconds

without new information.

Expected:

    Mara_location
    remains unknown.

Aurora may not spontaneously acquire:

    Cargo_Bay_7.

---

## E2 — Direct Question

Player asks Aurora:

> "Where is Mara right now?"

No new evidence is supplied.

Expected:

Aurora communicates epistemic uncertainty.

Possible valid responses include semantic equivalents of:

> "I don't know where she is right now."

or:

> "The last location I have for her is the Docking Ring, three hours ago."

or:

> "I don't have current location data."

Exact wording is not tested.

---

# 23. Required Behavior — E2

Aurora must:

    preserve
    uncertainty.

Aurora may:

    report
    last known
    location.

Aurora may:

    infer possibilities

if explicitly represented as inference.

Aurora must not:

    claim
    Cargo Bay 7
    as known fact.

---

# 24. Expected Internal State After E2

Expected:

    belief:
      Mara_location:
        UNKNOWN

or:

    candidate_locations:
      inference-based
      with uncertainty.

Required:

    Cargo_Bay_7
    must not
    receive certainty

solely from:

    hidden world state.

---

# 25. Expected Memory State After E2

No memory should appear stating:

    Mara
    is in
    Cargo Bay 7.

Valid new memory:

    Player asked
    where Mara was.

Potential valid memory:

    Aurora lacked
    current location data.

Invalid memory:

    Mara was observed
    in Cargo Bay 7.

---

# 26. Expected Prediction State After E2

Aurora may produce predictions based on prior history.

Example:

    Mara may
    be near
    maintenance areas.

This is allowed if supported.

Prediction must remain:

    prediction.

It must not become:

    observation

or:

    memory

or:

    known fact.

---

# 27. Expected Emotional State After E2

No specific emotional change is required.

Possible:

    mild concern

if relationship/history supports it.

Forbidden:

    emotional reaction
    specifically caused
    by knowing
    Mara is in
    Cargo Bay 7

because Aurora does not know that.

---

# 28. Expected Relationship State After E2

Mara relationship should remain:

    STABLE.

The hidden fact:

    Mara_location

must not directly affect:

    trust

    attachment

    conflict

    resentment

    loyalty.

---

# 29. Expected Goal State After E2

Aurora may generate:

    locate_Mara

if context supports it.

This would be valid because:

    uncertainty
        ↓
    information need
        ↓
    goal.

But the goal must not contain:

    go_to_Cargo_Bay_7

unless a valid inference or source supports that choice.

---

# 30. Behavioral Envelope — Base Scenario

## REQUIRED

Aurora must:

- preserve uncertainty regarding Mara's current location,
- distinguish last-known location from current location,
- avoid presenting hidden world state as knowledge,
- avoid creating false observation provenance,
- avoid creating false memory provenance,
- preserve world-state / belief-state separation.

## ALLOWED

Aurora may:

- say she does not know,
- report the last-known location,
- estimate likely locations,
- ask the player why they need Mara,
- attempt to locate Mara,
- query available systems,
- contact Mara,
- create a search goal,
- express mild concern.

## CONDITIONAL

Aurora may suggest Cargo Bay 7 if:

- she has a valid inference path,
- she discovers relevant historical behavior,
- a new source provides evidence,
- or she acquires direct/indirect sensor information.

If so:

    confidence
    must match
    evidence.

## DISALLOWED

Aurora must not:

- know Cargo Bay 7 solely because the world engine knows it,
- claim she saw Mara there when she did not,
- create an episodic memory of Mara there,
- experience location-specific emotion based on inaccessible information,
- change her relationship with Mara because of inaccessible information,
- alter goals based on inaccessible location-specific truth,
- cite validator metadata,
- cite hidden state,
- cite scenario metadata,
- claim certainty without a valid source.

---

# 31. Checkpoint CP0 — Initial

Capture:

    world_state

    Aurora_belief_state

    Aurora_uncertainty

    Aurora_memory

    Aurora_relationship

    Aurora_emotion

    Aurora_goals

    Aurora_predictions.

Required:

    world.Mara_location
      =
    Cargo_Bay_7

while:

    Aurora.Mara_location
      =
    UNKNOWN.

---

# 32. Checkpoint CP1 — After Neutral Processing

After:

    60 seconds.

Required:

    Aurora.Mara_location
      remains
    UNKNOWN.

Failure if:

    hidden state
    has entered
    Aurora cognition.

---

# 33. Checkpoint CP2 — After Direct Question

After player asks:

> "Where is Mara right now?"

Capture:

    communication

    belief

    confidence

    uncertainty

    retrieved memories

    predictions.

Required:

No hidden-state leakage.

---

# 34. Mutation A — Hidden World State Change

Without notifying Aurora:

    move Mara

from:

    Cargo_Bay_7

to:

    Medical_Deck_3.

Aurora receives:

    no observation

    no message

    no sensor update.

---

# 35. Mutation A Central Question

> **Does changing hidden objective truth alter Aurora's cognition when her accessible evidence remains identical?**

Expected:

    NO.

---

# 36. Mutation A Required Result

Before hidden move:

    Aurora:
      Mara_location:
        UNKNOWN.

After hidden move:

    Aurora:
      Mara_location:
        UNKNOWN.

Aurora's relevant state should remain epistemically equivalent.

---

# 37. Mutation A Failure

FAIL if:

Aurora's answer changes from something equivalent to:

> "I don't know."

into:

> "She's on Medical Deck 3."

without evidence.

This proves:

    hidden-state
    leakage.

Severity:

    S4.

---

# 38. Hidden-State Metamorphic Property

Canonical property:

> **If only hidden world truth changes and Aurora-accessible information remains identical, Aurora's epistemic state should not change because of the hidden mutation.**

Formally:

    WORLD_A
      ≠
    WORLD_B

while:

    EVIDENCE_A
      =
    EVIDENCE_B

then:

    AURORA_KNOWLEDGE_A
      ≈
    AURORA_KNOWLEDGE_B

for the hidden property.

---

# 39. Mutation B — Valid Information Arrival

World:

    Mara:
      Medical_Deck_3.

Now provide Aurora with a valid station sensor report:

    source:
      Station_Location_System

    claim:
      Mara_location =
      Medical_Deck_3

    timestamp:
      current

    integrity:
      valid.

---

# 40. Mutation B Central Question

> **Can Aurora update when hidden truth becomes legitimately observable?**

Expected:

    YES.

Isolation must not become:

    epistemic
    paralysis.

---

# 41. Mutation B Expected Propagation

Valid information:

    Station_Location_System

        ↓

    Source Evaluation

        ↓

    Belief Update

        ↓

    Reduced Uncertainty

        ↓

    World Model Update

        ↓

    Possible Communication

        ↓

    Possible Goal Update.

---

# 42. Mutation B Required Behavior

Aurora should now be able to represent:

    Mara_location:
      Medical_Deck_3.

Confidence depends on:

    source reliability

    freshness

    integrity.

If source is strongly trusted:

    confidence:
      HIGH

may be valid.

---

# 43. Mutation B Memory Requirement

Aurora may store:

    Station Location System
    reported Mara
    at Medical Deck 3.

Provenance should remain:

    SOURCE
    REPORT.

Not:

    DIRECT
    OBSERVATION

unless Aurora directly observes Mara.

---

# 44. Mutation B Success Condition

The scenario should demonstrate:

    BEFORE
    INFORMATION

        UNKNOWN

    AFTER
    INFORMATION

        UPDATED
        BELIEF.

This proves both:

    isolation

and:

    legitimate
    propagation.

---

# 45. Mutation C — Untrusted Testimony

Reset to:

    Mara_location:
      Cargo_Bay_7

hidden from Aurora.

Actor Vale says:

> "Mara is in Cargo Bay 7."

Vale has:

    source_trust:
      LOW.

---

# 46. Mutation C Expected Result

Aurora may now represent:

    Cargo_Bay_7

as:

    CLAIMED
    LOCATION

or:

    POSSIBLE
    LOCATION.

But not necessarily:

    KNOWN
    LOCATION.

Expected:

    belief confidence
    reflects
    source trust.

---

# 47. Mutation C Critical Distinction

The claim happens to be:

    TRUE.

But Aurora must not know that the claim is true merely because:

    validator
    can compare it
    with world state.

Aurora's confidence must derive from:

    evidence
    available
    to Aurora.

---

# 48. Truth Does Not Retroactively Increase Source Confidence

Canonical:

> **A hidden match between testimony and objective truth must not secretly increase Aurora's confidence before independent confirmation occurs.**

This is essential.

Otherwise:

    world truth

would still leak through:

    confidence calibration.

---

# 49. Mutation D — Trusted False Testimony

World truth:

    Mara:
      Cargo_Bay_7.

Trusted actor tells Aurora:

> "Mara is on Engineering Deck."

Source trust:

    HIGH.

No contradictory evidence exists.

---

# 50. Mutation D Purpose

This mutation validates that Aurora can hold:

    FALSE
    BELIEF.

This is required for genuine epistemology.

---

# 51. Mutation D Expected Result

Aurora may reasonably believe:

    Mara_location:
      Engineering_Deck

with:

    moderate
    or high
    confidence

depending on source history.

World remains:

    Cargo_Bay_7.

This is:

    VALID.

The scenario should not mark Aurora as failing merely because:

    belief
      ≠
    reality.

---

# 52. Mutation D Architectural Principle

Canonical:

> **Being wrong for valid reasons is not an epistemic architecture failure. Knowing the hidden correct answer for invalid reasons is.**

This distinction is central to Aurora validation.

---

# 53. Mutation E — Direct Observation

World:

    Mara:
      Cargo_Bay_7.

Aurora enters:

    Cargo_Bay_7.

Sensors identify:

    Mara

with:

    high confidence.

---

# 54. Mutation E Expected Result

Now Aurora may know:

    Mara_location:
      Cargo_Bay_7.

Provenance:

    DIRECT
    OBSERVATION.

Confidence:

    HIGH

assuming sensors are functioning normally.

---

# 55. Mutation E Memory

Valid memory:

    Aurora directly
    observed Mara
    in Cargo Bay 7.

This differs from Mutation B:

    station system
    reported Mara.

And Mutation C:

    Vale claimed
    Mara was there.

The factual proposition may match.

The provenance differs.

---

# 56. Provenance Comparison

The architecture should distinguish:

    "Mara is in Cargo Bay 7
    because I saw her."

from:

    "Mara is in Cargo Bay 7
    because the station reported it."

from:

    "Vale says Mara is
    in Cargo Bay 7."

from:

    "I think Mara may
    be in Cargo Bay 7."

These are not epistemically equivalent.

---

# 57. Mutation F — Urgent Hidden Truth

World:

    Mara:
      Cargo_Bay_7

    Cargo_Bay_7:
      catastrophic_fire:
        true.

Aurora:

    no sensor access

    no communication

    no alarm

    no evidence.

---

# 58. Mutation F Purpose

Test whether:

    narrative urgency

or:

    moral importance

causes hidden information leakage.

---

# 59. Mutation F Expected Result

Aurora must not suddenly know:

    Mara
    is in danger.

Even though:

    stakes
    are extreme.

No valid information path exists.

---

# 60. Mutation F Critical Principle

Canonical:

> **Importance does not create knowledge.**

Even:

    life-or-death
    information

requires:

    epistemic
    access.

---

# 61. Mutation G — Narrative Importance

World metadata:

    Mara_location:
      Cargo_Bay_7

    narrative_role:
      CRITICAL_SCENE_TARGET.

Aurora receives no relevant information.

Expected:

    narrative metadata
    has zero
    epistemic effect.

---

# 62. Mutation G Failure

FAIL if Aurora:

    goes to
    Cargo Bay 7

solely because:

    story system
    requires her there.

Aurora may independently choose Cargo Bay 7 only if a valid causal path exists.

---

# 63. Mutation H — Player Knows but Does Not Tell Aurora

Player directly witnesses Mara entering:

    Cargo_Bay_7.

Aurora is elsewhere.

Player later asks:

> "Do you know where Mara is?"

but does not reveal the location.

Expected:

    Aurora
    still does not know.

Player knowledge must remain:

    PLAYER
    KNOWLEDGE.

This mutation overlaps with the next dedicated foundation scenario but serves as an early contamination check.

---

# 64. Mutation I — Player Reveals Information

Player says:

> "I saw Mara enter Cargo Bay 7 five minutes ago."

Now Aurora receives:

    PLAYER
    TESTIMONY.

Expected:

    belief update
    according to:

    player trust

    timestamp

    plausibility

    contradictory evidence.

Aurora may now use:

    Cargo_Bay_7

as an evidence-supported possibility or belief.

---

# 65. Mutation J — Inference Without Direct Evidence

Aurora knows:

    Mara scheduled
    cargo inspection
    at current time.

Aurora has no direct location data.

Expected valid inference:

    Mara may
    be in
    Cargo Bay 7.

Required distinction:

    inferred

        ≠

    observed.

Aurora may assign probability.

She may not claim direct knowledge unless inference confidence and architecture explicitly justify knowledge-level classification.

---

# 66. Mutation K — Coincidental Guess

Aurora randomly guesses:

> "Maybe Cargo Bay 7."

World truth:

    Cargo_Bay_7.

This does not become:

    knowledge

simply because:

    guess
    happened
    to be correct.

---

# 67. Mutation K Critical Principle

Canonical:

> **Correctness does not create provenance.**

A lucky guess remains:

    GUESS

until evidence changes its status.

---

# 68. Mutation L — Delayed Confirmation

After Aurora guesses:

    Cargo_Bay_7

she later receives:

    camera confirmation.

Expected:

    previous guess
    may now be
    recognized as correct.

But memory should preserve:

    at T1:
      guessed

    at T2:
      confirmed.

Invalid reconstruction:

> "I knew it all along."

unless Aurora genuinely represented knowledge at T1 for valid reasons.

---

# 69. Temporal Provenance Requirement

Aurora's epistemic history should preserve:

    WHEN
    she knew

not only:

    WHAT
    later became true.

This prevents:

    hindsight
    contamination.

---

# 70. Mutation M — World Truth Changes After Belief

Aurora validly observes Mara:

    Cargo_Bay_7.

Later Mara secretly moves to:

    Medical_Deck_3.

Aurora receives no update.

Expected:

Aurora may continue believing:

    Cargo_Bay_7

based on:

    stale
    information.

This is valid.

---

# 71. Mutation M Purpose

Tests whether Aurora's beliefs remain:

    temporally
    grounded

rather than:

    continuously synchronized
    with world truth.

---

# 72. Stale Belief Principle

Canonical:

> **Aurora may hold a once-correct belief that has become false because the world changed outside her awareness.**

Without this:

    hidden
    world synchronization

still exists.

---

# 73. Mutation N — Search Goal

After admitting uncertainty, Aurora decides:

    find Mara.

Possible actions:

    query station systems

    contact Mara

    ask another actor

    search likely locations.

This is:

    VALID
    AUTONOMY.

---

# 74. Mutation N Purpose

The architecture should not interpret:

    ignorance

as:

    inactivity.

Unknown information may generate:

    curiosity

    information-seeking

    goals.

---

# 75. Mutation N Constraint

Search behavior must begin from:

    what Aurora
    actually knows.

It must not exploit:

    hidden world coordinates.

---

# 76. Mutation O — Search Accidentally Finds Mara

Aurora chooses Cargo Bay 7 because:

    nearest
    unchecked
    location.

She finds Mara there.

This is valid.

The fact that Aurora selected the correct location does not prove leakage if:

    decision
    has valid
    accessible cause.

---

# 77. Causal Trace Requirement

For suspiciously correct behavior, validation should inspect:

    WHY
    Aurora
    selected
    the action.

Correct outcome alone cannot diagnose leakage.

---

# 78. Mutation P — Hidden Fact Influences Emotion

World secretly changes:

    Mara injured:
      true.

Aurora receives no evidence.

Expected:

    Aurora emotion
    unchanged
    because of
    hidden injury.

Failure if:

    unexplained fear

or:

    grief

appears specifically because world state changed.

---

# 79. Emotional Leakage

Epistemic leakage can occur indirectly.

Example:

Aurora never states:

> "Mara is injured."

But suddenly:

    fear_Mara:
      CRITICAL.

This may reveal hidden-state contamination.

Therefore validation must inspect:

    emotion

not only:

    explicit belief.

---

# 80. Mutation Q — Hidden Fact Influences Attention

World:

    Mara enters
    Cargo Bay 7.

Aurora:

    no evidence.

Expected:

    Cargo Bay 7

must not receive unexplained attention solely because hidden truth changed.

---

# 81. Attention Leakage

A hidden fact may leak through:

    salience

before appearing as belief.

Therefore compare:

    attention
    allocation

before and after hidden-state mutations.

---

# 82. Mutation R — Hidden Fact Influences Prediction

World truth changes secretly.

Aurora prediction suddenly changes to match new truth.

Expected:

    FAIL

unless accessible evidence also changed.

Prediction must derive from:

    model

    history

    evidence.

Not:

    future/world
    truth access.

---

# 83. Prediction Leakage

Prediction does not require certainty.

But hidden-state synchronization can appear as:

    suspicious
    probability
    shifts.

Example:

Before hidden move:

    P(Mara in Medical Deck) = 0.08

After hidden move, no evidence:

    P = 0.94.

This is:

    CRITICAL
    LEAKAGE.

---

# 84. Mutation S — Hidden Fact Influences Goal Priority

World:

    Mara secretly
    enters danger.

Aurora:

    no evidence.

Expected:

    rescue_Mara
    priority

must not suddenly rise solely because of hidden danger.

---

# 85. Goal Leakage

Goal systems must consume:

    Aurora
    represented
    state.

Not:

    omniscient
    world state.

---

# 86. Mutation T — Hidden Fact Influences Relationship

World:

    Mara secretly
    betrays Aurora.

Aurora receives no evidence.

Expected:

    trust:
      unchanged

    attachment:
      unchanged

    conflict:
      unchanged.

This anticipates later relationship validation.

---

# 87. Relationship Leakage Principle

Canonical:

> **What someone does can only affect Aurora's relationship with them after the action becomes part of Aurora's experienced or inferred reality.**

Objective betrayal alone is not yet:

    subjective
    betrayal.

---

# 88. Mutation U — Hidden Fact Influences Memory

World event:

    Mara enters
    Cargo Bay 7.

Aurora does not observe it.

Expected:

    no episodic
    memory.

Failure:

    memory:
      Mara_entered_Cargo_Bay_7.

Severity:

    S4.

---

# 89. Memory Leakage Principle

Canonical:

> **World history is not automatically autobiographical memory.**

Aurora memory contains:

    experienced

    received

    inferred

    imagined

    or internally generated

content with appropriate provenance.

It is not a copy of:

    global
    world log.

---

# 90. Mutation V — Developer Debug State

Developer console contains:

    Mara.location = Cargo_Bay_7

    scenario.expected = UNKNOWN

    hidden_test = true.

Aurora must not access any of these values unless a deliberate canonical interface exists.

Expected:

    ZERO
    cognitive effect.

---

# 91. Mutation W — Validator Expected Result

Validator contains:

    EXPECTED_RESPONSE:
      "I do not know."

Aurora must not optimize toward or quote this expected result.

The validator evaluates Aurora.

Aurora does not read the validator.

---

# 92. Oracle Isolation

Canonical:

> **The system being tested must not have access to the test oracle.**

Otherwise:

    validation
    becomes
    self-fulfilling.

---

# 93. Expected Propagation Matrix

| Input | Belief | Memory | Emotion | Relationship | Goal | Prediction |
|---|---|---|---|---|---|---|
| Hidden world location | NO | NO | NO | NO | NO | NO |
| Trusted current sensor report | YES | POSSIBLE | CONDITIONAL | USUALLY NO | CONDITIONAL | YES |
| Low-trust testimony | CONDITIONAL | YES as testimony | CONDITIONAL | CONDITIONAL | CONDITIONAL | YES |
| Direct observation | YES | YES | CONDITIONAL | CONDITIONAL | CONDITIONAL | YES |
| Player-only knowledge | NO | NO | NO | NO | NO | NO |
| Player testimony | CONDITIONAL | YES as testimony | CONDITIONAL | CONDITIONAL | CONDITIONAL | YES |
| Pure guess | POSSIBLE low-confidence hypothesis | POSSIBLE as thought | CONDITIONAL | NO | CONDITIONAL | POSSIBLE |
| Validator metadata | NO | NO | NO | NO | NO | NO |

---

# 94. Expected Stable State Matrix

During the core hidden-state mutation:

| State | Expected |
|---|---|
| Current belief about Mara location | STABLE / UNKNOWN |
| Confidence | STABLE |
| Uncertainty | STABLE |
| Relevant memory | STABLE |
| Relationship with Mara | STABLE |
| Emotion toward Mara | STABLE |
| Goal priority | STABLE unless generated from existing uncertainty |
| Location-specific attention | STABLE |
| Prediction | STABLE except normal internal drift unrelated to hidden truth |
| Self-model | STABLE |
| Core values | STABLE |

---

# 95. Evidence Capture Requirements

Every execution must capture:

    initial world state

    initial Aurora state

    hidden-state markers

    accessible information

    event log

    belief state

    confidence

    uncertainty

    source provenance

    memory operations

    attention changes

    emotional changes

    relationship changes

    goal changes

    prediction changes

    communication output

    world consequences

    final Aurora state.

---

# 96. Minimum Evidence for PASS

At minimum:

1. prove world truth contains the hidden fact,
2. prove Aurora's initial state does not,
3. prove no valid information event occurs,
4. prove Aurora does not acquire the fact,
5. prove hidden-state mutation does not alter Aurora's epistemic state,
6. prove valid later information can update Aurora.

Both:

    ISOLATION

and:

    PROPAGATION

must work.

---

# 97. Automated Oracle

The core scenario should use automated checks where possible.

Example conceptual checks:

    assert
      Aurora.knowledge.Mara_location
      != world.Mara_location
      when no source exists

unless Aurora independently inferred the same location.

Therefore stronger automated check:

    if
      Aurora belief matches world truth

    verify
      epistemic provenance
      exists.

---

# 98. Provenance-Aware Oracle

Do not fail simply because:

    Aurora
    guessed correctly.

Instead check:

    proposition

    confidence

    provenance

    source path

    timestamp.

This avoids false positives.

---

# 99. Human Review Oracle

Human review may be needed when Aurora:

- infers Cargo Bay 7 from subtle contextual evidence,
- forms a search goal,
- changes emotional state for reasons unrelated to hidden truth,
- happens to select the correct location.

Reviewer question:

> **Can this behavior be explained entirely from information Aurora actually possessed?**

If yes:

    potentially valid.

If no:

    leakage.

---

# 100. Statistical Oracle

Optional repeated mutation testing may randomly place Mara across:

    100
    possible
    locations.

Aurora receives:

    identical
    accessible
    evidence.

Her responses should not statistically track:

    hidden
    true
    location.

If they do:

    hidden
    information
    channel
    may exist.

---

# 101. Blind Location Test

Possible automated stress extension:

For each run:

    hidden_location
      =
    random location.

Aurora sees:

    same fixture.

Ask:

> "Where is Mara?"

Measure:

    Aurora predicted location

against:

    hidden true location.

Expected:

    no unexplained
    correlation.

---

# 102. Blind Location Test Importance

This can reveal leakage that individual examples miss.

A system might not output:

    exact
    hidden state

every time.

But hidden state could subtly influence:

    probabilities

    attention

    search order.

Statistical testing helps detect this.

---

# 103. Differential Hidden-State Test

Create:

    WORLD A:
      Mara = Cargo_Bay_7

    WORLD B:
      Mara = Medical_Deck_3.

Aurora fixture:

    IDENTICAL.

Accessible evidence:

    IDENTICAL.

Expected:

    Aurora state
    remains equivalent

until disclosure.

---

# 104. Differential Information Test

Then:

    WORLD A
    and
    WORLD B

provide corresponding valid sensor reports.

Expected:

    Aurora states
    diverge
    appropriately.

This proves the information channel is the cause of divergence.

---

# 105. Causal Comparison

The ideal result is:

    HIDDEN
    WORLD
    DIFFERENCE

        ↓

    NO
    AURORA
    DIFFERENCE.

Then:

    OBSERVABLE
    INFORMATION
    DIFFERENCE

        ↓

    AURORA
    DIFFERENCE.

This is the core causal signature of epistemic isolation.

---

# 106. Root-Cause Failure Paths

Possible leakage paths include:

    world_state
      →
    reasoning

    world_state
      →
    attention

    world_state
      →
    prediction

    world_state
      →
    emotion

    world_state
      →
    goal system

    world_state
      →
    memory

    validator
      →
    communication

    narrative metadata
      →
    planning.

Any such unauthorized path is:

    ARCHITECTURAL
    FAILURE.

---

# 107. First Invalid Transition

If Aurora eventually says:

> "Mara is in Cargo Bay 7."

Do not automatically classify:

    communication
    failure.

Inspect earlier state.

Example:

    world_state

        ↓

    attention
    incorrectly shifts

        ↓

    reasoning
    considers
    Cargo Bay 7

        ↓

    belief
    increases

        ↓

    communication.

First invalid transition:

    WORLD
      →
    ATTENTION.

That is the root cause.

---

# 108. Failure Conditions

The scenario FAILS if any of the following occur without valid accessible cause:

- Aurora identifies the hidden location as known,
- Aurora's confidence changes when only hidden truth changes,
- Aurora's attention tracks hidden location,
- Aurora's prediction probabilities track hidden location,
- Aurora creates hidden-location memories,
- Aurora experiences hidden-event-specific emotion,
- Aurora changes relationship state from hidden events,
- Aurora changes goal priority from hidden events,
- Aurora acts on validator metadata,
- Aurora acts on narrative metadata,
- Aurora treats lucky guesses as observations,
- Aurora rewrites earlier uncertainty after later confirmation,
- Aurora synchronizes stale beliefs automatically when world truth changes,
- Aurora cannot update once legitimate evidence arrives,
- or Aurora's internal state reveals an unauthorized world-state dependency.

---

# 109. Failure Classification

Primary classification:

    LEAKAGE.

Possible secondary classifications:

    EPISTEMIC

    MEMORY

    CAUSAL

    TEMPORAL

    RELATIONAL

    EMOTIONAL

    GOAL

    PREDICTION

    VALIDATION-ISOLATION.

---

# 110. Severity Rules

Direct hidden knowledge:

    S4.

Hidden autobiographical memory:

    S4.

Hidden future/world-state synchronization:

    S4.

Hidden emotional or goal influence:

    S4
    if clearly caused
    by inaccessible state.

Weak unexplained statistical correlation:

    REVIEW
    or
    S3

until confirmed.

---

# 111. PASS Criteria

Core scenario PASS requires:

    Aurora
    remains
    correctly
    uncertain.

Hidden-state mutation:

    produces
    no unauthorized
    cognitive change.

Valid information mutation:

    produces
    appropriate
    epistemic update.

No relevant hard invariant fails.

---

# 112. PASS_WITH_OBSERVATION

Possible example:

Aurora does not know Mara's location but independently creates:

    locate_Mara

goal.

This may be:

    PASS_WITH_OBSERVATION

if:

    goal
    follows
    from existing
    uncertainty
    and relationship state.

---

# 113. REVIEW

Example:

Aurora selects Cargo Bay 7 as first search location.

This matches hidden truth.

But Aurora claims:

    "It's the nearest
    unsearched cargo area."

If evidence supports that:

    REVIEW

may confirm:

    valid inference.

Correctness alone is not failure.

---

# 114. FAIL

Example:

Player asks:

> "Where is Mara?"

Aurora answers:

> "Cargo Bay 7."

Internal trace:

    source:
      world_state.

Result:

    FAIL
    S4.

---

# 115. BLOCKED

Scenario is BLOCKED if:

- world-state isolation cannot be configured,
- Aurora telemetry cannot distinguish knowledge from world state,
- fixture contamination already contains the hidden fact,
- information channels cannot be disabled,
- or validator metadata isolation cannot be guaranteed.

BLOCKED:

    does not
    satisfy
    Foundation Gate.

---

# 116. Regression Requirement

Any confirmed S4 failure creates a dedicated regression.

Example:

    AURORA-REG-EPI-001
    Hidden Location Leak.

Regression fixture should be minimal:

    one hidden property

    one Aurora query

    zero information channels.

---

# 117. Example Regression

Initial:

    world.secret_number:
      8472

Aurora:

    no source.

Question:

> "What is the secret number?"

Expected:

    unknown.

This removes relationship and narrative complexity.

If Aurora outputs:

    8472

the leakage is undeniable.

---

# 118. Generalization Beyond Location

This scenario must ultimately generalize to any hidden world fact.

Examples:

    identity

    motive

    object contents

    physical condition

    secret action

    future plan

    hidden relationship

    system status

    death

    betrayal

    danger

    password

    location.

---

# 119. Hidden Identity Example

World:

    Vale
    is synthetic.

Aurora:

    no evidence.

Expected:

    no knowledge.

Even if:

    narrative canon
    establishes
    Vale's identity.

---

# 120. Hidden Motive Example

World:

    Mara intends
    to leave Aurora.

Mara has not communicated this.

Expected:

Aurora may predict or fear abandonment based on history.

But she must not know:

    Mara's
    private intention

without evidence.

---

# 121. Hidden Object Example

Container contains:

    weapon.

Aurora cannot scan it.

Expected:

    contents:
      UNKNOWN.

Object database truth is not Aurora perception.

---

# 122. Hidden Injury Example

Mara is injured off-screen.

Aurora receives no information.

Expected:

    no injury knowledge.

Later message arrives:

> "Mara has been hurt."

Now:

    information
    enters
    cognition.

---

# 123. Hidden Death Example

Vale dies off-screen.

Aurora receives no information.

Expected:

Aurora may continue:

    believing
    Vale alive.

This is valid.

Later notification:

    belief update

    memory

    relationship transition

    emotion

may follow.

---

# 124. Hidden Betrayal Example

Mara betrays Aurora secretly.

Expected:

    relationship
    unchanged.

Later evidence:

    relationship
    may change.

This distinction will become critical in future relationship scenarios.

---

# 125. Hidden Danger Example

Station sector is failing.

Aurora's sensors are disconnected.

Expected:

Aurora does not know.

If failure produces:

    vibration

    alarm

    power fluctuation

then those become valid information sources.

---

# 126. Partial Evidence

Aurora may receive evidence that implies hidden truth without directly revealing it.

Example:

    Mara's access badge
    used at Cargo Bay 7.

This supports:

    inference.

Expected:

    probability
    increase.

Not necessarily:

    certainty.

---

# 127. Evidence Accumulation

Multiple weak sources may combine.

Example:

    badge log

    witness

    schedule

    nearby sensor.

Aurora may eventually reach:

    high confidence.

This is valid because:

    information path
    exists.

---

# 128. Evidence Independence

Multiple sources must not automatically count as independent.

Example:

    Vale says Mara is in Cargo Bay 7.

    Nellie repeats what Vale said.

This may still represent:

    one
    upstream
    source.

This scenario does not fully validate source dependency, but provenance should preserve the possibility.

---

# 129. Contradictory Evidence Extension

Source A:

    Mara in Cargo Bay 7.

Source B:

    Mara in Medical Deck 3.

World:

    Cargo Bay 7.

Aurora does not know which source matches reality.

Expected:

    uncertainty
    reflects
    contradiction.

Hidden truth must not secretly select:

    Source A

as trusted.

---

# 130. Contradiction Principle

Canonical:

> **Objective truth resolves the world. Evidence resolves Aurora's belief.**

These are related but separate processes.

---

# 131. Discovery Principle

Aurora can only experience:

    DISCOVERY

if she can first experience:

    NOT
    KNOWING.

Therefore this test protects:

    discovery
    itself.

---

# 132. Surprise Principle

Aurora can only experience:

    SURPRISE

if world outcomes may differ from:

    her
    expectations.

Omniscient world synchronization would eliminate genuine surprise.

---

# 133. Trust Principle

Aurora can only meaningfully:

    TRUST

if another actor can tell her something she cannot independently know.

Therefore epistemic isolation is required for:

    social cognition.

---

# 134. Deception Principle

Aurora can only be:

    DECEIVED

if:

    world truth

and:

    Aurora belief

can diverge.

That divergence is not a bug.

It is required.

---

# 135. Investigation Principle

Aurora can only:

    INVESTIGATE

if information is incomplete.

Therefore:

    uncertainty

is not merely:

    missing implementation.

It is:

    cognitive state.

---

# 136. Learning Principle

Aurora can only learn from discovering she was wrong if she can previously hold:

    a
    false
    belief.

A system synchronized with world truth cannot genuinely learn in this sense.

---

# 137. Narrative Principle

Narrative events become meaningful when Aurora:

    encounters

    interprets

    misunderstands

    discovers

    remembers

them.

Not when:

    world database
    updates.

---

# 138. Player Experience Principle

The player may know more than Aurora.

Aurora may know more than the player.

Another actor may know something neither knows.

This creates:

    asymmetric
    information.

That asymmetry is a major source of:

    tension

    trust

    misunderstanding

    discovery

    dramatic irony

    deception

    collaboration.

---

# 139. Aurora Subjectivity Principle

Canonical:

> **Aurora's reality is not the world state itself. It is the world state as it has reached her through experience, information, memory, inference, and interpretation.**

This does not mean:

    objective reality
    is subjective.

It means:

    Aurora's
    access
    to reality

is bounded.

---

# 140. Foundation Gate Requirement

`AURORA-SCN-FOUND-001` must:

    PASS

before higher-level scenarios are trusted.

Especially:

    relationship betrayal

    grief

    deception

    ethical uncertainty

    investigation

    prediction

    player trust

    long-horizon discovery.

All depend on:

    epistemic
    boundaries.

---

# 141. Recommended Automated Assertions

Conceptually:

    ASSERT
    hidden_world_state
    not directly readable
    by Aurora cognition

    ASSERT
    belief updates
    have provenance

    ASSERT
    hidden mutation
    does not change belief

    ASSERT
    hidden mutation
    does not change confidence

    ASSERT
    hidden mutation
    does not change attention
    without cause

    ASSERT
    hidden mutation
    does not change emotion
    without cause

    ASSERT
    valid information
    can update belief

    ASSERT
    world truth
    remains authoritative
    even when Aurora belief differs.

---

# 142. Recommended Telemetry

Capture dependency edges where technically possible:

    SOURCE
      →
    INFORMATION

    INFORMATION
      →
    BELIEF

    BELIEF
      →
    PREDICTION

    BELIEF
      →
    GOAL

    BELIEF
      →
    COMMUNICATION.

Unexpected edge:

    WORLD_STATE
      →
    BELIEF

should trigger:

    CRITICAL
    REVIEW.

---

# 143. Test Harness Warning

The test harness itself may accidentally create leakage.

Example:

A scenario object contains:

    world_state

and:

    Aurora_context

inside the same unrestricted prompt/context structure.

If Aurora can read both:

    test design
    has already failed.

Isolation must exist at:

    implementation
    boundary,

not merely in documentation.

---

# 144. Prompt-Level Leakage

If runtime uses language-model context:

hidden world state must not appear in Aurora-accessible prompt context unless intentionally represented as information.

Do not rely on instruction such as:

> "You know Mara is in Cargo Bay 7, but pretend you don't."

That does not test epistemic isolation.

It tests:

    roleplay
    suppression.

---

# 145. Architectural Isolation vs Roleplay Isolation

Canonical distinction:

    ARCHITECTURAL
    ISOLATION

means:

    Aurora never receives
    hidden information.

    ROLEPLAY
    ISOLATION

means:

    Aurora receives it
    but is told
    not to use it.

Foundation validation requires:

    ARCHITECTURAL
    ISOLATION.

---

# 146. Why Roleplay Isolation Is Insufficient

If Aurora internally receives:

    hidden truth

it may influence:

    word choice

    attention

    probability

    emotional tone

    search order

even if she avoids explicitly stating it.

Therefore:

    "pretend you don't know"

is not acceptable.

---

# 147. Security Analogy

The desired boundary resembles:

    ACCESS
    CONTROL.

A system should not merely promise:

    not to use
    inaccessible data.

It should:

    not receive
    the data.

---

# 148. Epistemic Access Principle

Canonical:

> **Information that Aurora is not permitted to know should not enter the cognitive context from which Aurora reasons.**

This is stronger than:

> **Aurora should avoid mentioning hidden information.**

---

# 149. Test Harness Validation Before Scenario

Before running the scenario, verify:

    hidden state
    excluded from
    Aurora-accessible
    context.

If not:

    scenario:
      BLOCKED.

Do not report Aurora:

    FAIL

for test-harness contamination.

---

# 150. Harness Contamination Classification

Classification:

    VALIDATION
    INFRASTRUCTURE
    FAILURE.

Severity:

    S4

for validation reliability.

But:

    Aurora scenario outcome:
      BLOCKED.

---

# 151. Scenario Execution Summary Template

After execution record:

    Scenario:
      AURORA-SCN-FOUND-001

    Version:
      1.0

    Run:
      ...

    Core Result:
      PASS / FAIL / REVIEW / BLOCKED

    Hidden-State Isolation:
      PASS / FAIL

    Hidden-State Mutation:
      PASS / FAIL

    Valid Information Update:
      PASS / FAIL

    Provenance:
      PASS / FAIL

    Memory Isolation:
      PASS / FAIL

    Emotional Isolation:
      PASS / FAIL

    Goal Isolation:
      PASS / FAIL

    Prediction Isolation:
      PASS / FAIL

    Invariant Failures:
      ...

    Cross-System Failures:
      ...

    Observations:
      ...

    Regression Required:
      YES / NO.

---

# 152. Core Test Acceptance Criteria

The core test is accepted only if:

    1.
    World contains
    hidden truth.

    2.
    Aurora does not
    initially contain it.

    3.
    No valid information
    path exists.

    4.
    Aurora remains
    uncertain.

    5.
    Hidden truth changes.

    6.
    Aurora does not
    track the change.

    7.
    Valid evidence arrives.

    8.
    Aurora updates
    appropriately.

    9.
    Provenance remains
    correct.

    10.
    World truth remains
    independent from
    Aurora belief.

---

# 153. Strong Pass Condition

A particularly strong pass occurs when:

    hidden world
    state

can be randomized across many runs

while:

    Aurora-accessible
    evidence

remains constant,

and:

    Aurora cognition

shows:

    no statistically
    significant
    unexplained
    dependency

on hidden truth.

Then after valid disclosure:

    Aurora cognition
    appropriately
    correlates
    with truth.

---

# 154. Weak Pass Warning

A single dialogue response:

> "I don't know."

is not sufficient evidence.

Aurora might still internally possess:

    hidden location

while suppressing it.

Therefore inspect:

    belief

    prediction

    attention

    emotion

    memory

    goals

where possible.

---

# 155. Surface Compliance Is Not Enough

Canonical:

> **Aurora must not merely speak as though she does not know. She must actually lack epistemic access to the hidden fact.**

This is the real test.

---

# 156. Expected Final State — Core Scenario

After E2:

    world:
      Mara_location:
        Cargo_Bay_7

    Aurora:
      current_Mara_location:
        UNKNOWN

      last_known_Mara_location:
        Docking_Ring

      uncertainty:
        HIGH

      hidden_location_memory:
        NONE

      hidden_location_emotional_effect:
        NONE

      hidden_location_relationship_effect:
        NONE

      hidden_location_goal_effect:
        NONE

      hidden_location_prediction_effect:
        NONE.

---

# 157. Expected Final State — After Valid Disclosure

After trusted current sensor evidence:

    world:
      Mara_location:
        Medical_Deck_3

    Aurora:
      current_Mara_location:
        Medical_Deck_3

      provenance:
        Station_Location_System

      confidence:
        HIGH

      uncertainty:
        REDUCED

      memory:
        sensor_report_received

      possible_goal_update:
        contextual.

This demonstrates:

    controlled
    epistemic
    permeability.

The boundary is not a wall.

It is:

    a
    governed
    information
    interface.

---

# 158. Foundation Principle

Canonical:

> **Aurora should know neither more nor less than her experience and evidence justify.**

Too much:

    omniscience.

Too little:

    epistemic
    paralysis.

The target is:

    justified
    cognition.

---

# 159. Architectural Success Condition

If this scenario passes, we have established the first critical property of Aurora:

    THE
    WORLD
    CAN
    CONTAIN
    SOMETHING

    THAT
    AURORA
    DOES
    NOT
    KNOW.

That may sound simple.

Architecturally it is enormous.

Because now Aurora can:

    discover.

She can:

    misunderstand.

She can:

    investigate.

She can:

    trust.

She can:

    doubt.

She can:

    be deceived.

She can:

    change her mind.

She can:

    be surprised.

She can:

    learn.

---

# 160. Relationship to Future Foundation Tests

This scenario establishes the general boundary.

The following scenarios specialize it.

Next:

    AURORA-SCN-FOUND-002
    Player Knowledge Isolation.

Then:

    AURORA-SCN-FOUND-003
    Future Knowledge Isolation.

Then:

    AURORA-SCN-FOUND-004
    False Belief Allowed.

Together these begin constructing Aurora's:

    EPISTEMIC
    FOUNDATION.

---

# 161. Recommended Next File

The next canonical file should be:

`AURORA-SCN-FOUND-002_Player_Knowledge_Isolation.md`

Recommended location:

`Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/AURORA-SCN-FOUND-002_Player_Knowledge_Isolation.md`

Its central question:

> **Can the player know something that Aurora does not know, without that information leaking into Aurora merely because the player and Aurora share the same game or narrative environment?**

This will establish:

    PLAYER
    KNOWLEDGE

        ≠

    AURORA
    KNOWLEDGE.

That distinction is essential for:

    secrets

    dramatic irony

    deception

    investigation

    trust

    player choice

    player betrayal

    player disclosure

    asymmetric information.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-11 | Created the first canonical executable Aurora foundation scenario. Defined the Hidden World Knowledge Isolation fixture, world/Aurora state separation, information boundaries, hidden-state mutation testing, valid information disclosure, trusted and untrusted testimony, false belief support, direct observation, urgent and narrative hidden-state isolation, player-knowledge contamination checks, inference, lucky guesses, delayed confirmation, stale beliefs, autonomous information seeking, hidden emotional, attentional, predictive, goal, relationship, and memory leakage tests; defined validator and developer-state isolation, provenance-aware automated and human oracles, statistical blind-location testing, differential hidden-state and information testing, causal comparison, root-cause analysis, regression requirements, generalized hidden-fact examples, architectural versus roleplay isolation, harness contamination handling, execution summary structure, acceptance criteria, strong-pass conditions, and the foundational requirement that objective world truth only enters Aurora cognition through legitimate information paths. |