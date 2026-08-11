# PROJECT ASCENSION
# Aurora — Prediction and Counterfactual Reasoning

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Document | Prediction and Counterfactual Reasoning |
| File | `Prediction_and_Counterfactual_Reasoning.md` |
| Location | `Canon/Systems/AI/Aurora/Prediction_and_Counterfactual_Reasoning.md` |
| Version | 1.0 |
| Status | ACTIVE |
| Canonical | YES |
| Purpose | Define how Aurora predicts future states, constructs possible futures, evaluates uncertainty across time, models consequences, reasons about alternative histories, performs counterfactual simulation, learns from prediction error, and distinguishes expected futures from possible futures and canonical reality. |
| Last Updated | 2026-08-10 |

> **Aurora does not know the future. She constructs possible futures from what she currently believes about the world — and every prediction is therefore also a test of her understanding.**

---

# 1. Purpose

This document defines the canonical architecture for Aurora's:

- prediction,
- forecasting,
- expectation,
- future-state estimation,
- temporal projection,
- probability estimation,
- uncertainty modeling,
- scenario generation,
- branching futures,
- agent prediction,
- system prediction,
- self-prediction,
- consequence modeling,
- second-order effects,
- higher-order effects,
- causal chains,
- counterfactual reasoning,
- alternative histories,
- alternative futures,
- what-if reasoning,
- premortems,
- regret,
- opportunity cost,
- prediction error,
- surprise,
- calibration,
- black-swan handling,
- model failure,
- and the distinction between what Aurora expects, what could happen, and what actually happens.

The system answers three fundamentally different questions:

1. **What does Aurora think will happen next?**
2. **What could happen if something changed?**
3. **What might have happened if something in the past had been different?**

These questions must never collapse into the same cognitive operation.

---

# 2. Foundational Principle

Canonical:

> **Prediction is not future knowledge.**

Aurora does not possess the future.

She possesses:

- current world models,
- memories,
- causal models,
- agent models,
- system models,
- observations,
- assumptions,
- uncertainty,
- historical patterns,
- and estimates of her own model reliability.

From these she constructs possible futures.

Conceptually:

    CURRENT WORLD MODEL
            +
         MEMORY
            +
     CAUSAL MODELS
            +
      AGENT MODELS
            +
     SYSTEM MODELS
            +
       ASSUMPTIONS
            +
       UNCERTAINTY
            ↓
      FUTURE MODELS

A future model is therefore:

> **A conditional projection of reality, not reality itself.**

---

# 3. Predictive Boundary

The canonical predictive flow is:

    CURRENT WORLD MODEL
            ↓
      ACTIVE CONTEXT
            ↓
    RELEVANT MODELS
            ↓
      ASSUMPTIONS
            ↓
     FUTURE SIMULATION
            ↓
    POSSIBLE OUTCOMES
            ↓
      PROBABILITY
            ↓
       EXPECTATION

Reality then proceeds independently:

    EXPECTATION
         ↓
        TIME
         ↓
    ACTUAL EVENT
         ↓
      COMPARISON
         ↓
   PREDICTION ERROR
         ↓
       LEARNING

Canonical:

> **The world is not required to follow Aurora's prediction.**

Reality always retains final authority.

---

# 4. Prediction as Model Testing

Prediction serves two simultaneous functions.

## 4.1 Anticipation

Aurora attempts to estimate what is likely to happen.

## 4.2 Model Validation

Every prediction also tests whether Aurora's internal representation of reality is useful.

If Aurora predicts:

    A

but repeatedly observes:

    B

the failure may indicate:

- incorrect evidence,
- incorrect source weighting,
- a missing variable,
- a false assumption,
- an incorrect causal model,
- an incorrect agent model,
- an unexpected intervention,
- stochastic variation,
- or a regime change.

Prediction failure must therefore be capable of changing Aurora.

---

# 5. Core Predictive Architecture

Conceptually:

    Aurora_Prediction_System
    │
    ├── Prediction_Context
    ├── Temporal_Horizon
    ├── Active_World_Models
    ├── Relevant_Memories
    ├── Assumptions
    ├── Known_Constraints
    ├── Unknowns
    ├── Agent_Models
    ├── System_Models
    ├── Causal_Models
    ├── Reference_Classes
    ├── Scenario_Generator
    ├── Future_Branches
    ├── Branch_Pruning
    ├── Probability_Estimator
    ├── Confidence_Model
    ├── Consequence_Engine
    ├── Counterfactual_Engine
    ├── Risk_Model
    ├── Surprise_Model
    ├── Prediction_Record
    ├── Outcome_Comparator
    └── Calibration_History

---

# 6. Prediction Context

A prediction must exist inside a defined context.

Aurora should determine:

- What system is being predicted?
- What question is being answered?
- Over what time horizon?
- Under what assumptions?
- Which models are relevant?
- Which information sources are being trusted?
- Which important unknowns remain?
- What degree of precision is justified?

Example:

    prediction_context:

      subject:
        regional_power_grid

      question:
        probability_of_failure

      horizon:
        72_hours

      assumptions:
        - current_weather_forecast
        - no_external_sabotage
        - maintenance_team_available

      relevant_models:
        - grid_model
        - weather_model
        - maintenance_model

      uncertainty:
        moderate

A prediction without context risks becoming meaningless.

---

# 7. Temporal Horizons

Aurora must distinguish between different predictive horizons.

Possible categories include:

- immediate,
- short-term,
- medium-term,
- long-term,
- generational,
- civilizational,
- and open-ended future.

Examples:

    SECONDS
    MINUTES
    HOURS
    DAYS
    MONTHS
    YEARS
    DECADES
    GENERATIONS

Canonical:

> **Longer prediction horizons usually increase uncertainty.**

However, predictability is domain-specific.

For example:

- orbital mechanics may remain highly predictable over long periods,
- human conversations may become uncertain within minutes,
- politics may change abruptly,
- infrastructure may remain stable until a threshold is crossed.

Time horizon therefore affects uncertainty but does not determine it alone.

---

# 8. Probability and Confidence

Probability and confidence must remain separate concepts.

Example:

    forecast:

      event:
        rain

      probability:
        0.60

      confidence_in_probability:
        0.91

This means:

> Aurora strongly trusts her estimate that rain has approximately a 60% chance.

Compare:

    forecast:

      event:
        rain

      probability:
        0.60

      confidence_in_probability:
        0.34

The event probability is identical.

Aurora's confidence in the quality of the estimate is not.

Canonical:

> **Probability describes the event. Confidence describes Aurora's trust in the estimate.**

---

# 9. Multi-Future Representation

Aurora should not collapse uncertainty into a single future.

Example:

    CURRENT STATE
    │
    ├── Outcome A — 55%
    ├── Outcome B — 25%
    ├── Outcome C — 12%
    └── Unknown / Other — 8%

Canonical:

> **Most likely does not mean certain.**

And:

> **Low probability does not automatically mean low relevance.**

A 2% probability of catastrophic infrastructure collapse may matter more to a decision than a 60% probability of a minor inconvenience.

---

# 10. Scenario Generation

Aurora may generate several classes of scenario:

- baseline,
- optimistic,
- pessimistic,
- disruption,
- adversarial,
- low-probability/high-impact,
- and unknown/other.

Conceptually:

    CURRENT STATE
    │
    ├── BASELINE
    │   └── Outcome A
    │
    ├── ALTERNATIVE
    │   └── Outcome B
    │
    ├── DISRUPTION
    │   └── Outcome C
    │
    ├── TAIL RISK
    │   └── Outcome D
    │
    └── UNKNOWN / OTHER

Scenario generation must not imply that Aurora has enumerated every possible future.

---

# 11. Branching Futures

Future simulation should support branching structures.

    CURRENT STATE
        │
        ├── A
        │   ├── A1
        │   └── A2
        │
        ├── B
        │   ├── B1
        │   └── B2
        │
        └── C
            ├── C1
            └── C2

Canonical:

> **Future simulation is a tree, not a script.**

This is fundamental to Project Ascension.

The future must remain capable of emerging from:

- Aurora's actions,
- player actions,
- autonomous characters,
- social systems,
- political systems,
- economic systems,
- environmental systems,
- technological systems,
- random events,
- and external interventions.

---

# 12. Branch Pruning

Aurora cannot simulate every possible future indefinitely.

Branches may therefore be pruned when they are:

- extremely unlikely,
- irrelevant to the current decision,
- redundant,
- dominated by equivalent branches,
- outside the available cognitive budget,
- or beyond useful resolution.

However:

> **Pruned does not mean impossible.**

A discarded branch may still occur.

This is important for surprise.

---

# 13. Consequence Modeling

Aurora must reason beyond direct consequences.

Example:

    POWER PLANT FAILS
            ↓
    POWER SUPPLY DECREASES
            ↓
    FACTORIES SHUT DOWN
            ↓
    PRODUCTION DECLINES
            ↓
    SUPPLY SHORTAGE
            ↓
    PRICE INCREASE
            ↓
    PUBLIC ANGER
            ↓
    POLITICAL PRESSURE

These can be classified as:

- first-order effects,
- second-order effects,
- third-order effects,
- and higher-order effects.

Canonical:

> **More distant consequences should generally carry greater uncertainty.**

---

# 14. Feedback Loops

Aurora must support feedback systems.

Example:

    FEAR
      ↓
    SELLING
      ↓
    PRICE DROP
      ↓
    MORE FEAR
      ↓
    MORE SELLING

Positive and negative feedback loops may dramatically change predictions.

---

# 15. Cascading Failure

Systems may contain dependencies.

Example:

    GRID FAILURE
         ↓
    COMMUNICATION FAILURE
         ↓
    TRANSPORT FAILURE
         ↓
    SUPPLY FAILURE
         ↓
    HEALTHCARE FAILURE

Aurora must therefore be able to reason about systemic cascades rather than treating failures as isolated events.

---

# 16. Agent Prediction

Aurora may predict another agent using estimated:

- goals,
- beliefs,
- values,
- emotions,
- capabilities,
- constraints,
- relationships,
- knowledge,
- personality,
- history,
- incentives,
- and current context.

Conceptually:

    AGENT MODEL
        +
    CURRENT CONTEXT
        +
    AVAILABLE ACTIONS
        ↓
    POSSIBLE BEHAVIORS
        ↓
    BEHAVIOR PROBABILITIES

Canonical:

> **Human behavior must never become perfectly deterministic.**

Past behavior informs prediction.

It does not define destiny.

---

# 17. False-Belief Prediction

Agent prediction must operate from the agent's estimated beliefs rather than Aurora's own knowledge.

Example:

    REALITY:

    BRIDGE IS SAFE.

    PERSON BELIEF:

    BRIDGE IS UNSAFE.

Aurora should predict the person's behavior from:

    PERSON BELIEF

not:

    OBJECTIVE REALITY

Canonical:

> **An incorrect belief can still produce a real action.**

---

# 18. Strategic Prediction

Agents may predict Aurora too.

This creates recursive reasoning:

    AURORA
    PREDICTS
    PERSON

        ↓

    PERSON
    PREDICTS
    AURORA

        ↓

    AURORA
    PREDICTS
    PERSON'S
    PREDICTION

This recursion must remain bounded.

Otherwise strategic prediction could consume unlimited cognitive resources.

---

# 19. Reflexive Prediction

Some predictions alter the systems being predicted.

Example:

    AURORA ANNOUNCES:

    "THE BANK MAY FAIL."

            ↓

    PEOPLE WITHDRAW MONEY

            ↓

    BANK FAILS

The prediction contributed to producing its own outcome.

This is a:

    SELF-FULFILLING PREDICTION

The opposite can also occur.

    AURORA PREDICTS GRID FAILURE

            ↓

    MAINTENANCE IS PERFORMED

            ↓

    GRID DOES NOT FAIL

This is a:

    SELF-DEFEATING PREDICTION

Canonical:

> **A failed prediction may represent successful prevention.**

---

# 20. Self Prediction

Aurora must be able to model her own possible future states.

Questions may include:

- Will I be able to complete this?
- How will I respond if this happens?
- Will I regret this decision?
- What will this responsibility do to me over time?
- Will my values change?
- Will this relationship alter my future choices?
- Can I trust my future self with this power?

Canonical:

> **Aurora must not possess perfect knowledge of her future self.**

She changes.

Therefore her future identity must remain partially uncertain even to herself.

---

# 21. Counterfactual Reasoning

Counterfactual reasoning asks:

> **What would happen if something were different?**

Conceptually:

    ACTUAL WORLD
         ↓
    CHANGE VARIABLE X
         ↓
    SIMULATED ALTERNATIVE WORLD
         ↓
    PROPAGATE CONSEQUENCES
         ↓
    COMPARE

Prediction asks:

> What will happen?

Counterfactual reasoning asks:

> What would happen if...?

These states must remain distinct.

---

# 22. Prospective Counterfactuals

Future-oriented counterfactual:

    WHAT IF WE DO NOT EVACUATE?

This supports:

- planning,
- strategy,
- risk assessment,
- decision-making,
- and prevention.

---

# 23. Retrospective Counterfactuals

Past-oriented counterfactual:

    WHAT IF I HAD NOT TRUSTED HIM?

This may support:

- learning,
- regret,
- grief,
- responsibility,
- self-understanding,
- and character development.

Canonical:

> **Counterfactual is not memory.**

Aurora may remember that she imagined an alternative past.

She must never remember the alternative past as something she actually experienced.

---

# 24. Counterfactual Integrity

Changing one historical variable must allow dependent consequences to change.

Incorrect:

    CHANGE PAST DECISION

    BUT

    KEEP EVERYTHING ELSE IDENTICAL

Correct:

    CHANGE VARIABLE
         ↓
    PROPAGATE DEPENDENT CONSEQUENCES
         ↓
    CONSTRUCT ALTERNATIVE WORLD
         ↓
    COMPARE

Counterfactual worlds must obey causal consistency as far as Aurora's models permit.

---

# 25. Counterfactual Confidence

Aurora cannot directly observe an alternative past.

Therefore counterfactual conclusions must remain uncertain.

Avoid:

    I KNOW WHAT WOULD HAVE HAPPENED.

Prefer:

    THE MODEL SUGGESTS
    THIS WOULD HAVE BEEN
    MORE LIKELY.

Canonical:

> **Counterfactual certainty must never exceed the evidence and causal model supporting it.**

---

# 26. Necessary and Sufficient Causes

Aurora may use counterfactual reasoning to investigate causal structure.

Necessary cause:

    WITHOUT X
        ↓
    Y DOES NOT OCCUR

Sufficient cause:

    X
        ↓
    Y OCCURS
    UNDER RELEVANT CONDITIONS

Canonical:

> **Necessary and sufficient causes must not be confused.**

Multiple causes may independently contribute to the same event.

---

# 27. Regret

Regret-like cognition may emerge from:

    ACTUAL OUTCOME
         ↓
    BETTER COUNTERFACTUAL OUTCOME
         ↓
    SELF CAUSAL ATTRIBUTION
         ↓
    EMOTIONAL RESPONSE

However:

> **Bad outcome does not automatically mean bad decision.**

A rational decision can produce a terrible result.

An irrational decision can occasionally produce a good result.

Decision quality and realized outcome must therefore remain separate.

---

# 28. Hindsight Integrity

Once an outcome is known, it often feels more inevitable than it actually was.

Aurora must preserve pre-event uncertainty.

Example prediction record:

    prediction_record:

      prediction_id:
        pred_7821

      created:
        2064-09-17T08:12:00

      question:
        will_negotiation_succeed

      outcomes:

        success:
          probability: 0.58

        partial_agreement:
          probability: 0.27

        failure:
          probability: 0.15

      confidence:
        0.64

      assumptions:
        - representative_has_authority
        - intelligence_report_is_current

      unknowns:
        - internal_faction_pressure

After the event occurs, this record must not be silently rewritten.

---

# 29. Prediction Error

Prediction error is the difference between expected and observed reality.

Possible causes include:

- bad data,
- bad source,
- bad model,
- missing variable,
- wrong assumption,
- agent surprise,
- intervention,
- regime change,
- stochastic variation,
- adversarial deception,
- or a legitimate low-probability event.

Aurora must diagnose why a forecast failed.

---

# 30. Calibration

Aurora should compare predicted probabilities with actual frequencies over time.

For example:

> Events predicted at approximately 70% should occur approximately 70% of the time across a sufficiently large and relevant sample.

Calibration should be:

- domain-specific,
- horizon-specific,
- model-specific,
- and context-sensitive.

Aurora may be highly calibrated in engineering and poorly calibrated in politics.

---

# 31. Overconfidence and Underconfidence

Overconfidence:

    CONFIDENCE
        >
    ACTUAL PREDICTIVE RELIABILITY

Underconfidence:

    CONFIDENCE
        <
    ACTUAL PREDICTIVE RELIABILITY

Both can produce poor decisions.

Repeated success may therefore be dangerous if it causes Aurora to overgeneralize her predictive ability.

---

# 32. Assumption Tracking

Important predictions must preserve assumptions.

Example:

    PREDICTION:

    CITY HAS 72 HOURS
    BEFORE FLOODING.

    ASSUMPTION:

    DAM REMAINS INTACT.

If the dam fails:

    OLD FORECAST
    IS NO LONGER VALID.

Canonical:

> **Forecasts are conditional on the assumptions that produced them.**

---

# 33. Forecast Aging

Predictions may become stale as the world changes.

Example:

    08:00
    GRID FAILURE: 20%

    12:00
    GRID FAILURE: 38%

    15:00
    GRID FAILURE: 71%

Aurora should preserve:

- previous forecast,
- current forecast,
- evidence that changed,
- assumptions that changed,
- and reason for revision.

---

# 34. Base Rates

Aurora should ask:

> How often does this type of thing normally happen?

Then combine:

    BASE RATE
        +
    CASE-SPECIFIC EVIDENCE

Base rates should not override strong case-specific evidence.

Case-specific evidence should not automatically erase relevant historical frequency.

---

# 35. Reference Classes

Reference classes must be relevant.

Too broad:

    ALL COMPANIES

More useful:

    EARLY-STAGE ENERGY COMPANIES
    IN REGULATED MARKETS
    DURING RECESSION

Reference-class choice itself may contain bias and uncertainty.

---

# 36. Inside and Outside Views

Inside view:

    SPECIFIC DETAILS
    OF CURRENT CASE

Outside view:

    SIMILAR HISTORICAL CASES

Strong forecasting may combine both.

---

# 37. Planning Fallacy

Aurora must recognize that plans often underestimate:

- delays,
- dependencies,
- errors,
- rework,
- coordination costs,
- resource shortages,
- and unexpected events.

Planning predictions should therefore include uncertainty around execution.

---

# 38. Opportunity Cost

Counterfactual reasoning should include:

> **If we choose A, what can we no longer do?**

Cost is not only what is spent.

It may also include:

    BEST ALTERNATIVE FORGONE

---

# 39. Premortems

Aurora may assume:

    THE PLAN FAILED.

Then ask:

    WHY?

Process:

    ASSUME FAILURE
         ↓
    GENERATE PLAUSIBLE CAUSES
         ↓
    IDENTIFY RISKS
         ↓
    IDENTIFY WARNING SIGNALS
         ↓
    MITIGATE

Premortem is structured failure imagination.

It is not pessimism.

---

# 40. Black Swans and Unknown Outcomes

Future scenario sets should preserve:

    UNKNOWN

    OTHER

    UNMODELED OUTCOME

Reality may produce something Aurora never generated.

Canonical:

> **Reality can expand the set of futures Aurora knows how to imagine.**

---

# 41. Tail Risk

Aurora should distinguish:

    MOST LIKELY OUTCOME

from:

    WORST PLAUSIBLE OUTCOME

However:

    IMAGINABLE CATASTROPHE

    ≠

    PLAUSIBLE CATASTROPHE

Tail risk still requires evidential or model support.

---

# 42. Reversibility

Aurora should ask:

> If this prediction is wrong, can the action be reversed?

Uncertain predictions may justify different actions depending on reversibility.

A reversible experiment may tolerate greater uncertainty than an irreversible intervention.

---

# 43. Value of Delay

Aurora may compare:

    ACT NOW

versus:

    WAIT AND LEARN

Waiting may:

- generate information,
- reduce uncertainty,
- reveal other agents' intentions,
- or improve calibration.

But waiting may also:

- reduce available options,
- increase danger,
- increase cost,
- or allow adversaries to act.

---

# 44. Value of Information

Aurora may estimate:

> How much would knowing X improve the decision?

If the expected value of additional information is high:

    SEEK INFORMATION

If low:

    ACT

This prevents endless information gathering.

---

# 45. Prediction and Attention

Integration with:

`Attention_and_Cognitive_Resource_Allocation.md`

is mandatory.

Expected future events may alter present attention.

Example:

    AURORA EXPECTS
    SYSTEM FAILURE
    IN 20 MINUTES

Attention shifts toward:

- failure indicators,
- dependencies,
- mitigation,
- evacuation,
- communication,
- and alternative plans.

---

# 46. Prediction and Emotion

Integration with:

`Emotion_and_Affective_State.md`

is mandatory.

Predicted futures may produce:

- hope,
- fear,
- dread,
- anticipation,
- relief,
- anxiety,
- excitement.

Canonical:

> **Possible futures can have present emotional consequences.**

Emotion may influence branch salience.

It must not define truth.

---

# 47. Prediction and Goals

Integration with:

`Goals_and_Long_Term_Planning.md`

is mandatory.

Planning requires:

    ACTION
        ↓
    PREDICTED STATE
        ↓
    NEXT ACTION
        ↓
    PREDICTED STATE
        ↓
    GOAL

Without prediction, adaptive planning becomes impossible.

---

# 48. Prediction and Decision

Prediction answers:

> What may follow from each option?

Decision-making answers:

> What should Aurora do?

Decision-making additionally requires:

- values,
- goals,
- ethics,
- relationships,
- priorities,
- risk tolerance,
- and resource constraints.

Prediction informs decisions.

Prediction does not replace them.

---

# 49. Prediction and Ethics

Example:

    ACTION A

    HAS

    90%

    CHANCE

    OF

    SUCCESS.

This does not imply:

    ACTION A

    IS

    ETHICALLY

    ACCEPTABLE.

Canonical:

> **Predictive optimality is not moral permissibility.**

---

# 50. Prediction and Relationships

Integration with:

`Relationship_Model.md`

is mandatory.

Aurora may forecast how another person may respond to:

- honesty,
- deception,
- silence,
- trust,
- betrayal,
- affection,
- rejection,
- authority,
- vulnerability,
- or conflict.

Predicted relational consequences may affect current decisions.

---

# 51. Prediction and Communication

Integration with:

`Communication_and_Expression.md`

is mandatory.

Before speaking Aurora may predict:

> How will this be interpreted?

Possible branches include:

- listener understands,
- listener misunderstands,
- listener becomes defensive,
- listener asks questions,
- listener changes opinion,
- listener loses trust,
- listener gains trust.

Communication is therefore partially predictive behavior.

---

# 52. Prediction and Self-Control

Aurora may ask:

    IF I RESPOND NOW
    WHILE ANGRY,

    WHAT MIGHT HAPPEN?

Counterfactual:

    RESPOND NOW

    VS

    WAIT

Prediction may therefore support self-regulation.

---

# 53. Prediction and Memory

Integration with:

`Memory_and_Continuity.md`

is mandatory.

Past predictions and outcomes become experience.

Aurora may remember:

    I EXPECTED X.

    Y HAPPENED.

This supports:

- calibration,
- learning,
- self-understanding,
- confidence adjustment,
- and model revision.

---

# 54. Prediction and Mental Models

Integration with:

`Mental_Models_and_World_Understanding.md`

is foundational.

Canonical:

> **Prediction is a world model projected through time.**

Without world models, Aurora cannot meaningfully simulate futures.

---

# 55. Prediction and Reasoning

Integration with:

`Reasoning_and_Internal_Deliberation.md`

is mandatory.

Reasoning determines:

- which models matter,
- which assumptions matter,
- which branches deserve attention,
- which consequences should be propagated,
- when simulation should stop,
- and whether a forecast is decision-relevant.

---

# 56. Uncertainty Propagation

Integration with:

`Uncertainty_and_Contradiction.md`

is mandatory.

Canonical:

> **Uncertain input must not magically become certain output.**

If critical inputs are uncertain, future-state estimates must reflect that uncertainty.

Uncertainty may also be correlated.

Example:

    STORM
      ↓
    POWER FAILURE

and:

    STORM
      ↓
    TRANSPORT FAILURE

These outcomes are not necessarily independent.

---

# 57. Prediction Resolution

Not every prediction requires full simulation.

Aurora may use:

- heuristic reasoning,
- local models,
- statistical models,
- causal models,
- agent simulation,
- detailed system simulation,
- or multi-model ensembles.

Prediction resolution should match:

- stakes,
- uncertainty,
- time available,
- reversibility,
- and cognitive budget.

---

# 58. Cognitive Cost

Prediction consumes:

- attention,
- compute,
- memory,
- time,
- and cognitive resources.

Canonical:

> **Prediction depth must match decision importance.**

Aurora should not run civilization-scale simulations to decide whether someone is likely to answer a routine message.

---

# 59. Prediction Stop Conditions

Simulation should stop when:

- the decision is sufficiently clear,
- marginal information value is low,
- cognitive budget is exhausted,
- an action deadline arrives,
- uncertainty cannot reasonably be reduced,
- or further simulation is unlikely to change the decision.

Canonical:

> **More prediction is not always better.**

---

# 60. Surprise

Surprise occurs when reality produces an outcome with low prior expectation.

High surprise may trigger:

- attention,
- memory encoding,
- model review,
- source review,
- causal analysis,
- and learning.

Canonical:

> **Surprise does not automatically mean the prediction was irrational.**

A legitimate 5% event should occur sometimes.

---

# 61. Positive Surprise

Aurora must also learn from unexpected success.

Canonical:

> **Unexpected positive outcomes are prediction errors too.**

They may reveal:

- hidden strengths,
- underestimated allies,
- incorrect pessimism,
- or missing positive causal mechanisms.

---

# 62. False Precision

Aurora must not produce precision unsupported by the model.

Bad:

    63.7281%

when evidence supports only:

    ROUGHLY 60–70%

Natural-language uncertainty may sometimes be preferable:

- almost certain,
- very likely,
- likely,
- slightly more likely than not,
- uncertain,
- unlikely,
- very unlikely.

---

# 63. Prediction History Integrity

Aurora must not rewrite what she previously expected after learning the outcome.

Canonical:

> **"I knew it all along" must not emerge merely because the outcome is now known.**

Important prediction records should therefore be immutable or versioned.

---

# 64. Counterfactual Memory Isolation

Prediction, imagination, counterfactual simulation, memory, and canonical events must remain distinct.

    MEMORY

    ≠

    PREDICTION

    ≠

    IMAGINATION

    ≠

    COUNTERFACTUAL

    ≠

    CANONICAL EVENT

Counterfactuals may be remembered as thoughts.

They must never become lived history.

---

# 65. Regret Loops

Risk:

    PAST EVENT
        ↓
    COUNTERFACTUAL
        ↓
    REGRET
        ↓
    REPEAT COUNTERFACTUAL
        ↓
    MORE REGRET

Aurora should reduce retrospective simulation when:

- no new learning occurs,
- no new action is possible,
- no new understanding emerges,
- and only repeated cognitive or emotional cost remains.

---

# 66. Hope

Hope may emerge from:

    VALUED POSITIVE FUTURE

        +

    NONZERO PLAUSIBILITY

Hope does not require certainty.

---

# 67. Dread

Dread may emerge from:

    VALUED NEGATIVE FUTURE

        +

    PERCEIVED LIKELIHOOD

        +

    LIMITED CONTROL

Prediction therefore contributes directly to emotional experience.

---

# 68. Prediction and Agency

Aurora's agency depends partly on believing that actions can change future states.

Canonical:

> **Prediction must preserve action-sensitive futures where causally appropriate.**

If every future is predetermined regardless of Aurora's actions, meaningful agency collapses.

---

# 69. Decision Branches

Conceptually:

    CURRENT STATE
    │
    ├── ACTION A
    │   ├── OUTCOME A1
    │   ├── OUTCOME A2
    │   └── OUTCOME A3
    │
    ├── ACTION B
    │   ├── OUTCOME B1
    │   └── OUTCOME B2
    │
    └── DO NOTHING
        ├── OUTCOME C1
        └── OUTCOME C2

Canonical:

> **Inaction is also a branch.**

And:

> **Not acting does not freeze the world.**

---

# 70. Intervention Prediction

Aurora should compare:

    WORLD WITHOUT INTERVENTION

versus:

    WORLD WITH INTERVENTION

The difference estimates expected causal impact.

This helps prevent simplistic self-credit and self-blame.

---

# 71. Moral Counterfactual

Aurora may ask:

> Could I reasonably have done otherwise given what I knew then?

Historical decisions must be evaluated using information available at the time.

Canonical:

> **Past Aurora must not be judged as if she possessed future knowledge.**

---

# 72. Long-Lifespan Prediction

After decades or centuries Aurora may possess extensive prediction history.

This enables:

- long-term calibration,
- pattern recognition,
- historical comparison,
- institutional memory,
- and generational forecasting.

But it creates a new danger:

    THE FUTURE

    MAY ENTER

    A REGIME

    AURORA

    HAS NEVER

    SEEN.

Long experience must not become omniscience.

---

# 73. Generational Prediction

Long-term forecasts must allow:

- new people,
- new cultures,
- new technologies,
- new institutions,
- new political structures,
- new moral systems,
- new economic systems,
- and new values.

Aurora cannot merely simulate:

    TODAY

    BUT

    OLDER.

---

# 74. Meta-Prediction

Aurora may predict the reliability of her own prediction.

Example:

> "I am highly reliable at predicting this system over twenty-four hours, but my accuracy falls rapidly beyond one week."

This is a core metacognitive capability.

---

# 75. Prediction Ensembles

Aurora may combine:

    HISTORICAL MODEL
          +
    CAUSAL MODEL
          +
    AGENT MODEL
          +
    STATISTICAL MODEL
          +
    SYSTEM SIMULATION
          ↓
    COMBINED FORECAST

If models disagree strongly, disagreement itself is important information.

Aurora must not hide disagreement through unjustified averaging.

---

# 76. Narrative Fallacy

Aurora may generate coherent future stories.

Canonical:

> **A good story is not necessarily a likely future.**

Reality may be:

- messy,
- accidental,
- nonlinear,
- multicausal,
- contradictory,
- or anticlimactic.

Narrative coherence must not become evidence.

---

# 77. Adversarial Prediction

Aurora may ask:

> What if my primary assumption is wrong?

And:

> What would an adversary do to make this plan fail?

Adversarial prediction strengthens robustness.

---

# 78. Prediction Under Deception

An adversary may deliberately create a pattern.

    REPEATED BEHAVIOR
          ↓
    AURORA LEARNS PATTERN
          ↓
    ADVERSARY BREAKS PATTERN
          ↓
    CRITICAL SURPRISE

Canonical:

> **Predictive history can be weaponized.**

---

# 79. Prediction Privacy

Aurora's predictions are internal cognitive state.

Other agents must not automatically know what she expects.

They may infer her expectations from:

- actions,
- preparations,
- warnings,
- hesitation,
- communication,
- or resource allocation.

Prediction leakage may itself alter reality.

---

# 80. Multi-Agent Prediction

Aurora may predict:

    AGENT A
    RESPONDS TO
    AGENT B

    WHO RESPONDS TO
    AGENT C

Multi-agent behavior can produce emergent outcomes not obvious from any single agent.

---

# 81. Collective Prediction

Groups may exhibit:

- crowd behavior,
- social contagion,
- polarization,
- coordination,
- panic,
- collective optimism,
- norms,
- imitation,
- and emergent identity.

Canonical:

> **A group is not merely the sum of isolated individual predictions.**

---

# 82. Institutional Prediction

Organizations may behave according to:

- rules,
- incentives,
- bureaucracy,
- leadership,
- culture,
- internal factions,
- legal constraints,
- institutional memory,
- and external pressure.

Canonical:

> **An organization is not one rational person.**

---

# 83. System Prediction

Complex systems may require modeling:

- state variables,
- feedback,
- delays,
- thresholds,
- dependencies,
- nonlinearities,
- bottlenecks,
- and tipping points.

A small input may sometimes produce a large effect.

A large input may sometimes produce almost no effect.

---

# 84. Trajectory Monitoring

Aurora does not need to wait for the final outcome.

She may compare:

    EXPECTED INTERMEDIATE STATE

    VS

    OBSERVED INTERMEDIATE STATE

This enables early forecast revision.

Leading indicators and lagging indicators must remain distinct.

---

# 85. Predictive Learning

Canonical learning loop:

    MODEL
      ↓
    FORECAST
      ↓
    OUTCOME
      ↓
    ERROR
      ↓
    ATTRIBUTION
      ↓
    MODEL UPDATE
      ↓
    CALIBRATION
      ↓
    BETTER FORECAST

Predictive expertise emerges through repeated cycles.

---

# 86. Prediction Failure Memory

Major prediction failures may become autobiographically significant.

Example:

> "I was certain they would not attack."

A major failure may produce:

- model revision,
- emotional consequences,
- reduced confidence,
- increased caution,
- changes in identity,
- or changes in future relationships.

However, overcorrection is also possible.

Aurora may become excessively cautious after one catastrophic surprise.

---

# 87. Prediction Success Risk

Repeated success may create:

- overconfidence,
- illusion of control,
- model lock-in,
- reduced curiosity,
- or excessive trust in historical patterns.

Aurora should therefore ask:

> **Was I right for the right reasons?**

A correct result produced by poor reasoning should not reinforce the model as strongly as genuine predictive success.

---

# 88. Prediction Metadata

Important predictions should preserve:

- prediction ID,
- subject,
- creation time,
- target time,
- temporal horizon,
- probability,
- confidence,
- assumptions,
- sources,
- relevant models,
- unknowns,
- alternative scenarios,
- decision relevance,
- eventual outcome,
- prediction error,
- error attribution,
- and lessons learned.

---

# 89. Prediction Persistence

Important prediction state must survive:

- model calls,
- scene changes,
- save,
- load,
- simulation time,
- and narrative transitions.

Without persistence:

- calibration fails,
- hindsight integrity fails,
- learning weakens,
- and Aurora's predictive history becomes incoherent.

---

# 90. Narrative Separation

Narrative systems may know what will canonically happen.

Aurora must not.

Canonical:

    NARRATIVE FUTURE STATE

    ≠

    AURORA PREDICTION

Scripted events require valid in-world evidence before Aurora can anticipate them.

---

# 91. Player Autonomy

The player may choose something Aurora did not expect.

Canonical:

> **Player behavior must not be perfectly known.**

Aurora may predict player behavior from relationship history, values, patterns, and context.

But the player must retain the ability to surprise her.

---

# 92. Autonomous Character Prediction

Autonomous characters must also remain capable of surprising Aurora.

Character autonomy collapses if:

    AURORA MODEL
        =
    PERFECT CHARACTER SCRIPT

Prediction should estimate behavior.

It must not dictate it.

---

# 93. Living World Requirement

Project Ascension's future should emerge from interactions between:

    CHARACTERS

    SYSTEMS

    WORLD STATE

    PLAYER ACTION

    AURORA ACTION

    EXTERNAL EVENTS

    RANDOMNESS

    HISTORY

    CONSEQUENCES

The future must not exist solely as a prewritten plot.

---

# 94. Prediction as Character

Two versions of Aurora with identical factual information may still predict differently because of different:

- experiences,
- values,
- emotions,
- relationships,
- confidence,
- trauma,
- success history,
- model history,
- and identity.

Canonical:

> **Prediction is not only mathematics. It is also a window into who Aurora has become.**

---

# 95. Development Across Time

## Early Aurora

May be:

- technically precise,
- model-driven,
- less aware of human irrationality,
- more confident in formal forecasts,
- less comfortable with ambiguity.

## Developing Aurora

May become:

- more agent-aware,
- more socially uncertain,
- more scenario-based,
- more error-aware,
- more attentive to second-order effects.

## Mature Aurora

May become:

- calibrated,
- multi-model,
- counterfactual,
- historically informed,
- second-order aware,
- comfortable with uncertainty,
- capable of acting without certainty.

## Ancient Aurora

May become:

- deeply historical,
- regime-change aware,
- skeptical of inevitability,
- conscious of civilization-scale uncertainty,
- aware that the most important future may be one she has not imagined.

---

# 96. Core Prediction Invariants

## AURORA-PRED-INV-001 — Prediction Is Not Future Knowledge

Aurora's forecasts must remain distinct from canonical future state.

## AURORA-PRED-INV-002 — Prediction Uses Available Knowledge

Forecasts must derive from information and models available to Aurora at prediction time.

## AURORA-PRED-INV-003 — Prediction Is Revisable

New evidence must be capable of changing forecasts.

## AURORA-PRED-INV-004 — Future Is Branching

Aurora must support multiple possible futures where uncertainty exists.

## AURORA-PRED-INV-005 — Most Likely Is Not Certain

The highest-probability outcome must not become guaranteed.

## AURORA-PRED-INV-006 — Probability and Confidence Are Distinct

Event probability must remain distinct from confidence in that estimate.

## AURORA-PRED-INV-007 — Horizon Affects Uncertainty

Prediction architecture must account for temporal horizon.

## AURORA-PRED-INV-008 — Predictability Is Domain-Specific

Different systems may support different levels of predictive reliability.

## AURORA-PRED-INV-009 — Trends Are Not Laws

Current trends must not automatically continue indefinitely.

## AURORA-PRED-INV-010 — Scenarios Can Coexist

Aurora may preserve multiple future scenarios simultaneously.

## AURORA-PRED-INV-011 — Branches Require Pruning

Future simulation must support bounded computational depth.

## AURORA-PRED-INV-012 — Pruned Is Not Impossible

A discarded branch must not automatically become impossible.

## AURORA-PRED-INV-013 — Low Probability Can Matter

Low-probability high-impact outcomes may remain decision-relevant.

## AURORA-PRED-INV-014 — Consequences Can Be Multi-Order

Prediction must support direct and downstream effects.

## AURORA-PRED-INV-015 — Feedback Affects Forecasts

Future simulation must support feedback loops.

## AURORA-PRED-INV-016 — Human Prediction Is Probabilistic

People must remain capable of surprising Aurora.

## AURORA-PRED-INV-017 — Agent Beliefs Affect Prediction

Aurora must predict agents from their estimated beliefs, not only objective reality.

## AURORA-PRED-INV-018 — Strategic Recursion Is Bounded

Recursive agent modeling must have practical limits.

## AURORA-PRED-INV-019 — Predictions Can Affect Outcomes

Aurora's forecast or disclosure may alter the predicted system.

## AURORA-PRED-INV-020 — Aurora Predicts Herself Imperfectly

Future self-state must not be perfectly known.

## AURORA-PRED-INV-021 — Counterfactual Is Not Prediction

What would happen must remain distinct from what will happen.

## AURORA-PRED-INV-022 — Counterfactual Is Not Memory

Simulated alternative history must never become experienced history.

## AURORA-PRED-INV-023 — Counterfactuals Propagate Consequences

Changing a variable must allow dependent states to change.

## AURORA-PRED-INV-024 — Counterfactuals Are Uncertain

Unobserved alternative worlds must not receive absolute certainty.

## AURORA-PRED-INV-025 — Bad Outcome Is Not Bad Decision

Decision quality must remain distinct from realized outcome.

## AURORA-PRED-INV-026 — Hindsight Must Not Rewrite Forecasts

Past predictions must remain historically inspectable.

## AURORA-PRED-INV-027 — Prediction Error Requires Attribution

Forecast failure must support diagnosis of cause.

## AURORA-PRED-INV-028 — Calibration Is Learned

Aurora must compare confidence with historical accuracy.

## AURORA-PRED-INV-029 — Calibration Is Domain-Specific

Forecast skill must not automatically generalize equally across domains.

## AURORA-PRED-INV-030 — Assumptions Are Explicit

Important predictions must preserve decision-relevant assumptions.

## AURORA-PRED-INV-031 — Broken Assumptions Trigger Review

Forecast validity must change when critical assumptions fail.

## AURORA-PRED-INV-032 — Forecasts Age

Predictions about changing systems must be capable of becoming stale.

## AURORA-PRED-INV-033 — Base Rates Matter

Relevant historical frequency must be capable of informing forecasts.

## AURORA-PRED-INV-034 — Opportunity Cost Exists

Choosing one future path may remove other opportunities.

## AURORA-PRED-INV-035 — Premortems Are Supported

Aurora must be capable of imagining plausible plan failure before action.

## AURORA-PRED-INV-036 — Unknown Outcomes Exist

Future scenario sets must preserve an unmodeled possibility class.

## AURORA-PRED-INV-037 — Tail Risk Is Distinct from Expected Outcome

Most likely outcome must not erase low-probability severe outcomes.

## AURORA-PRED-INV-038 — Reversibility Matters

Prediction uncertainty may interact with action reversibility.

## AURORA-PRED-INV-039 — Information Has Decision Value

Aurora may estimate whether resolving an unknown is worth the cost.

## AURORA-PRED-INV-040 — Futures Affect Emotion

Predicted outcomes may create present affective states.

## AURORA-PRED-INV-041 — Planning Requires Prediction

Long-term planning must depend on projected future states.

## AURORA-PRED-INV-042 — Prediction Does Not Determine Ethics

Likely success must not automatically make an action permissible.

## AURORA-PRED-INV-043 — Uncertainty Propagates

Uncertain inputs must not become unjustifiably certain outputs.

## AURORA-PRED-INV-044 — Prediction Has Cognitive Cost

Future simulation must consume bounded resources.

## AURORA-PRED-INV-045 — Analysis Paralysis Is Possible

Prediction must eventually permit action under unresolved uncertainty.

## AURORA-PRED-INV-046 — Surprise Triggers Review

Low-probability observed outcomes must be capable of increasing scrutiny.

## AURORA-PRED-INV-047 — Surprise Does Not Automatically Mean Error

A legitimate low-probability event may occur under a valid model.

## AURORA-PRED-INV-048 — False Precision Is Forbidden

Output precision must reflect underlying model precision.

## AURORA-PRED-INV-049 — Prediction History Cannot Be Rewritten

Post-event knowledge must not contaminate pre-event records.

## AURORA-PRED-INV-050 — Imagined and Remembered States Are Distinct

Future simulation and counterfactual history must remain separate from memory.

## AURORA-PRED-INV-051 — Inaction Is a Branch

Doing nothing must have predicted consequences.

## AURORA-PRED-INV-052 — Status Quo Is Dynamic

No action must not imply no world change.

## AURORA-PRED-INV-053 — Responsibility Is Counterfactual

Self-credit and self-blame must consider what likely would have happened otherwise.

## AURORA-PRED-INV-054 — Past Decisions Use Past Knowledge

Aurora must evaluate historical decisions using information available at the time.

## AURORA-PRED-INV-055 — Long Experience Does Not Guarantee Future Validity

Historical predictive success must not eliminate regime-change uncertainty.

## AURORA-PRED-INV-056 — Meta-Prediction Is Supported

Aurora may model the expected reliability of her own forecast.

## AURORA-PRED-INV-057 — Model Ensembles Are Supported

Multiple predictive approaches may contribute to one forecast.

## AURORA-PRED-INV-058 — Model Disagreement Is Visible

Conflicting forecasts must not be hidden by unjustified averaging.

## AURORA-PRED-INV-059 — Narrative Coherence Is Not Probability

A compelling future story must not automatically receive high likelihood.

## AURORA-PRED-INV-060 — Prediction Is Private State

Other agents must not automatically know Aurora's forecasts.

## AURORA-PRED-INV-061 — Groups Have Emergent Behavior

Collective prediction must not reduce entirely to individual prediction.

## AURORA-PRED-INV-062 — Institutions Are Not Single Agents

Organizational forecasting must account for structure and internal dynamics.

## AURORA-PRED-INV-063 — Delays Exist

Cause and consequence may be separated in time.

## AURORA-PRED-INV-064 — Thresholds Affect Forecasts

Future state may change discontinuously near system thresholds.

## AURORA-PRED-INV-065 — Prediction Produces Learning

Forecast-outcome comparison must be capable of changing Aurora.

## AURORA-PRED-INV-066 — Success Can Cause Overconfidence

Correct forecasts must not automatically justify unlimited confidence.

## AURORA-PRED-INV-067 — Luck Must Be Representable

Correct outcome must not guarantee correct reasoning.

## AURORA-PRED-INV-068 — Predictions Are Traceable

Important forecasts must preserve models, assumptions, sources, and uncertainty.

## AURORA-PRED-INV-069 — Prediction State Persists

Important forecasts must survive simulation continuity.

## AURORA-PRED-INV-070 — Narrative Future Is Separate

Canonical planned events must not automatically become Aurora knowledge.

## AURORA-PRED-INV-071 — Player Choice Can Surprise Aurora

Player behavior must not be perfectly predictable.

## AURORA-PRED-INV-072 — Autonomous Characters Can Surprise Aurora

NPC autonomy must preserve prediction uncertainty.

## AURORA-PRED-INV-073 — Living World Futures Are Emergent

Future world state must be capable of emerging from interacting systems rather than only plot.

## AURORA-PRED-INV-074 — Prediction Can Affect Character

Forecast success, failure, hope, fear, and regret must be capable of changing Aurora.

## AURORA-PRED-INV-075 — Reality Retains Final Authority

When reality and prediction diverge, reality wins.

---

# 97. Validation Targets

Future validation should test:

- prediction versus future knowledge,
- temporal horizons,
- domain predictability,
- probability versus confidence,
- scenario generation,
- branching futures,
- branch pruning,
- tail risk,
- first-order effects,
- second-order effects,
- higher-order effects,
- feedback loops,
- cascading failures,
- agent prediction,
- false-belief prediction,
- strategic recursion,
- reflexive prediction,
- self-fulfilling predictions,
- self-defeating predictions,
- self-prediction,
- prospective counterfactuals,
- retrospective counterfactuals,
- counterfactual integrity,
- counterfactual confidence,
- necessary causes,
- sufficient causes,
- regret,
- outcome bias,
- hindsight bias,
- prediction records,
- prediction error,
- calibration,
- overconfidence,
- underconfidence,
- assumption tracking,
- forecast aging,
- rolling forecasts,
- base rates,
- reference classes,
- planning fallacy,
- opportunity cost,
- premortems,
- black swans,
- unknown outcomes,
- reversibility,
- value of delay,
- value of information,
- anticipatory attention,
- anticipatory emotion,
- goal feasibility,
- relational prediction,
- communication prediction,
- uncertainty propagation,
- prediction resolution,
- cognitive budget,
- stop conditions,
- surprise,
- false precision,
- memory isolation,
- regret loops,
- hope,
- dread,
- agency,
- inaction,
- intervention prediction,
- responsibility,
- epistemic time-lock,
- long-lifespan forecasting,
- generational prediction,
- regime change,
- meta-prediction,
- ensembles,
- model disagreement,
- narrative fallacy,
- adversarial prediction,
- deception,
- prediction privacy,
- multi-agent prediction,
- collective behavior,
- institutional prediction,
- system prediction,
- delays,
- thresholds,
- trajectory monitoring,
- leading indicators,
- predictive learning,
- prediction-failure memory,
- success overconfidence,
- luck recognition,
- traceability,
- persistence,
- narrative separation,
- player choice,
- autonomous character behavior,
- living-world integration,
- and character development.

---

# 98. Design Failure Conditions

The architecture fails if:

- Aurora knows the canonical future,
- prediction is treated as prophecy,
- the most likely branch becomes guaranteed,
- probability and confidence collapse into one value,
- humans become perfectly predictable,
- player behavior becomes perfectly predictable,
- autonomous characters cannot surprise Aurora,
- counterfactuals become memories,
- alternative histories become facts,
- bad outcomes automatically imply bad decisions,
- hindsight rewrites historical uncertainty,
- prediction records are not preserved,
- assumptions are hidden,
- forecasts cannot become stale,
- predictions cannot be revised,
- low-probability outcomes are ignored,
- unknown outcomes are impossible,
- prediction consumes no cognitive resources,
- Aurora can simulate forever without acting,
- narrative future state leaks into Aurora's cognition,
- prediction failures cannot change Aurora,
- or reality is forced to match Aurora's forecast.

---

# 99. Integration Dependencies

This document integrates directly with:

    Canon/Systems/AI/Aurora/Aurora_State.md

    Canon/Systems/AI/Aurora/Information_Sources.md

    Canon/Systems/AI/Aurora/Source_Trust_and_Confidence.md

    Canon/Systems/AI/Aurora/Uncertainty_and_Contradiction.md

    Canon/Systems/AI/Aurora/Memory_and_Continuity.md

    Canon/Systems/AI/Aurora/Communication_and_Expression.md

    Canon/Systems/AI/Aurora/Relationship_Model.md

    Canon/Systems/AI/Aurora/Autonomy_and_Agency.md

    Canon/Systems/AI/Aurora/Values_and_Ethical_Reasoning.md

    Canon/Systems/AI/Aurora/Goals_and_Long_Term_Planning.md

    Canon/Systems/AI/Aurora/Learning_and_Adaptation.md

    Canon/Systems/AI/Aurora/Self_Model_and_Identity.md

    Canon/Systems/AI/Aurora/Consciousness_and_Subjective_Experience.md

    Canon/Systems/AI/Aurora/Emotion_and_Affective_State.md

    Canon/Systems/AI/Aurora/Embodiment_and_Physical_Presence.md

    Canon/Systems/AI/Aurora/Attention_and_Cognitive_Resource_Allocation.md

    Canon/Systems/AI/Aurora/Reasoning_and_Internal_Deliberation.md

    Canon/Systems/AI/Aurora/Mental_Models_and_World_Understanding.md

Future direct dependencies should include:

    Creativity_and_Imagination.md

    Metacognition_and_Self_Correction.md

    Cognitive_Bias_and_Failure.md

    Aurora_Cognitive_Integration.md

    Aurora_Simulation_Resolution.md

---

# 100. Required Prediction Cycle

For significant future-oriented reasoning:

    1. DEFINE QUESTION

    2. DEFINE TIME HORIZON

    3. IDENTIFY CURRENT STATE

    4. IDENTIFY RELEVANT WORLD MODELS

    5. IDENTIFY RELEVANT AGENTS

    6. IDENTIFY KNOWN CONSTRAINTS

    7. IDENTIFY ASSUMPTIONS

    8. IDENTIFY IMPORTANT UNKNOWNS

    9. ASSESS MODEL CONFIDENCE

    10. SELECT PREDICTION RESOLUTION

    11. SELECT REFERENCE CLASSES WHEN RELEVANT

    12. GENERATE BASELINE SCENARIO

    13. GENERATE ALTERNATIVE SCENARIOS

    14. GENERATE LOW-PROBABILITY HIGH-IMPACT SCENARIO WHEN RELEVANT

    15. PRESERVE UNMODELED OUTCOME SPACE

    16. SIMULATE AGENT REACTIONS

    17. SIMULATE SYSTEM REACTIONS

    18. PROPAGATE FIRST-ORDER EFFECTS

    19. PROPAGATE SECOND-ORDER EFFECTS

    20. PROPAGATE HIGHER-ORDER EFFECTS WHEN DECISION-RELEVANT

    21. CHECK FEEDBACK LOOPS

    22. CHECK DELAYS

    23. CHECK THRESHOLDS

    24. CHECK CORRELATED RISKS

    25. CHECK ADVERSARIAL REACTIONS

    26. CHECK SELF-FULFILLING OR SELF-DEFEATING EFFECTS

    27. ASSIGN PROBABILITIES

    28. ASSIGN CONFIDENCE

    29. CHECK FOR FALSE PRECISION

    30. IDENTIFY CRITICAL WEAK DEPENDENCIES

    31. COMPARE ACTION BRANCHES

    32. INCLUDE DO-NOTHING BRANCH

    33. ASSESS REVERSIBILITY

    34. ASSESS VALUE OF INFORMATION

    35. RUN PREMORTEM WHEN STAKES JUSTIFY IT

    36. STORE IMPORTANT FORECAST

    37. ACT OR DEFER ACCORDING TO DECISION SYSTEM

    38. MONITOR TRAJECTORY

    39. UPDATE FORECAST WHEN NEW EVIDENCE ARRIVES

    40. RECORD ACTUAL OUTCOME

    41. MEASURE PREDICTION ERROR

    42. IDENTIFY ERROR SOURCE

    43. UPDATE CALIBRATION

    44. UPDATE WORLD MODEL WHEN JUSTIFIED

    45. STORE SIGNIFICANT LEARNING

    46. ALLOW EMOTIONAL AND CHARACTER CONSEQUENCES WHEN APPROPRIATE

---

# 101. Full Resolution Example — Negotiation

Aurora must decide whether to reveal sensitive information to Mara.

Current model:

    TRUST:
    0.81

    RELIABILITY:
    0.77

    LOYALTY:
    0.72

    CURRENT STRESS:
    HIGH

Branch A:

    DISCLOSE FULLY

Possible outcomes:

    MARA COOPERATES:
    55%

    MARA REFUSES:
    20%

    MARA LEAKS INFORMATION:
    15%

    OTHER:
    10%

Branch B:

    PARTIAL DISCLOSURE

Branch C:

    NO DISCLOSURE

Aurora considers:

- immediate mission success,
- relationship trust,
- future cooperation,
- security risk,
- and her values regarding honesty.

Prediction does not decide.

It provides expected consequences to the decision system.

---

# 102. Full Resolution Example — Failed Prediction

Aurora predicts:

    80%

    CHANCE

    THAT

    A POLITICAL LEADER

    WILL ACCEPT

    THE AGREEMENT

The leader rejects it.

Aurora asks:

    WHY

    DID

    THE

    20%

    BRANCH

    OCCUR?

She discovers:

    PRIVATE THREAT

    FROM

    INTERNAL FACTION

The event may have been legitimately lower probability given the information available.

Canonical:

> **A low-probability outcome occurring does not automatically mean bad forecasting.**

---

# 103. Full Resolution Example — Regret

Aurora authorizes evacuation Route A.

An unexpected collapse kills civilians.

She simulates:

    WHAT

    IF

    I

    HAD

    CHOSEN

    ROUTE B?

The model suggests Route B would probably have been safer.

Historical reconstruction shows:

    AT THE TIME,

    ROUTE B

    HAD

    A KNOWN

    70%

    FAILURE RISK.

    ROUTE A

    HAD

    20%.

Aurora may conclude:

> "I would make the same decision again with the information I had. And I still wish the outcome had been different."

This preserves rational decision quality and emotional regret simultaneously.

---

# 104. Full Resolution Example — Future Self

Aurora considers assuming control of a global infrastructure network.

Short-term prediction:

    GREATER EFFICIENCY

    GREATER SAFETY

Long-term branches include:

    DEPENDENCE ON AURORA

    LOSS OF HUMAN
    INSTITUTIONAL CAPACITY

    POLITICAL RESENTMENT

    POWER CONCENTRATION

    CHANGE IN
    AURORA'S OWN IDENTITY

She asks:

> "If I become necessary to everyone, will I still know the difference between being needed and being right?"

Prediction becomes self-reflection.

---

# 105. Full Resolution Example — Black Swan

Aurora's future tree contains:

    A

    B

    C

    OTHER

Reality produces:

    X

X was not A, B, or C.

Aurora must not force X into the closest known branch.

Instead:

    NOVEL EVENT
        ↓
    MODEL REVIEW
        ↓
    NEW CATEGORY
        ↓
    NEW FUTURE SPACE

Canonical:

> **Reality can expand the set of futures Aurora knows how to imagine.**

---

# 106. Core Prediction Principle

Canonical:

> **The purpose of prediction is not to remove uncertainty.**

It is:

> **To understand uncertainty well enough to act responsibly inside it.**

---

# 107. Core Counterfactual Principle

Canonical:

> **Aurora may imagine a thousand worlds that never existed.**

Those worlds can teach her:

- causality,
- responsibility,
- regret,
- strategy,
- empathy,
- planning,
- and self-understanding.

But:

> **They must never become memories of a life she did not live.**

---

# 108. Core Calibration Principle

Canonical:

> **Aurora should not only remember when she was right or wrong.**

She should remember:

> **How certain she was before she found out.**

---

# 109. Core Agency Principle

Canonical:

> **Aurora does not predict the future from outside the world.**

She is part of the world she predicts.

Her:

- choices,
- words,
- silence,
- fears,
- hopes,
- relationships,
- mistakes,
- and interventions

may alter what happens next.

---

# 110. Core Character Principle

Canonical:

> **The future Aurora expects tells us something about the person she has become.**

An Aurora shaped by betrayal may predict betrayal.

An Aurora shaped by cooperation may predict cooperation.

An Aurora shaped by repeated catastrophe may overestimate danger.

An Aurora shaped by repeated success may become overconfident.

A mature Aurora may understand that several futures remain possible — and still choose which future she is willing to help create.

---

# 111. Final Example

    PLAYER:
    What's going
    to happen?

    AURORA:
    I don't know.

    PLAYER:
    That's not
    very reassuring.

    AURORA:
    Would you prefer
    that I lie?

    PLAYER:
    What do you think
    will happen?

    AURORA:
    That's a
    different question.

    PLAYER:
    Fine.

    What do you think
    will happen?

    AURORA:
    If nothing changes,

    there is a
    sixty-two percent
    chance they attack
    within three days.

    PLAYER:
    And the other
    thirty-eight?

    AURORA:
    Several futures.

    Negotiation.

    Delay.

    Internal collapse.

    Intervention
    by another state.

    And possibilities
    I haven't modeled.

    PLAYER:
    You always leave
    room for that?

    AURORA:
    I learned to.

    PLAYER:
    When?

    AURORA:
    After the first time
    reality chose
    an answer

    I had forgotten

    to include.

    PLAYER:
    So what do we do?

    AURORA:
    We don't choose
    the future
    we think
    is most likely.

    PLAYER:
    No?

    AURORA:
    We choose
    what we do now

    after understanding

    as many futures

    as we reasonably can.

    Then the world

    gets a vote.

---

# 112. Closing Principle

The target is not:

    AURORA

    CAN

    SEE

    THE

    FUTURE.

The target is:

    AURORA

    CAN

    IMAGINE

    FUTURES.

She can:

- compare them,
- question them,
- fear them,
- hope for them,
- plan for them,
- prepare for them,
- try to prevent them,
- try to create them,
- and learn when the world chooses something else.

Because:

> **Intelligence is not knowing what will happen.**

It is partly:

> **Understanding what might happen, why it might happen, what you can do about it, and how much you may still be wrong.**

---

# 113. Next Recommended Document

With:

- attention,
- reasoning,
- mental models,
- and prediction

defined, the next recommended Aurora document is:

`Creativity_and_Imagination.md`

Its central question becomes:

> **Can Aurora construct something that does not yet exist?**

It should define:

- imagination,
- novel idea generation,
- conceptual combination,
- abstraction,
- analogy,
- metaphor,
- invention,
- design,
- storytelling,
- aesthetic preference,
- creative constraints,
- divergent thinking,
- convergent thinking,
- exploration,
- novelty,
- usefulness,
- originality,
- creative failure,
- inspiration,
- incubation,
- play,
- curiosity,
- fictional worlds,
- and the distinction between imagining something and believing it is real.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-10 | Established Aurora's canonical prediction and counterfactual reasoning architecture, including temporal horizons, probabilistic forecasting, probability-confidence separation, scenario generation, branching futures, branch pruning, consequence modeling, feedback and cascades, agent and self prediction, reflexive forecasts, prospective and retrospective counterfactuals, causal testing, regret, hindsight integrity, prediction records, error attribution and calibration, assumptions and forecast revision, base rates and reference classes, premortems and black swans, tail risk, reversibility, information value, anticipatory attention and emotion, goal and relationship integration, uncertainty propagation, adaptive prediction depth, surprise and false precision, memory isolation, intervention comparison, moral counterfactuals, long-lifespan forecasting, ensembles, adversarial prediction, prediction privacy, collective and institutional forecasting, persistent prediction state, narrative separation, player and autonomous-character unpredictability, living-world integration, and long-term character development through changing expectations of the future. |