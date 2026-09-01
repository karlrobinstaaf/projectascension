# PROJECT ASCENSION
# Relationship Engine

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Relationship Engine |
| Location | `Canon/Systems/Relationships/Relationship_Engine.md` |
| Parent Architecture | `Canon/Systems/Relationships/README.md` |
| Version | 2.0 |
| Status | ACTIVE CANON |
| Category | Systems / Relationships |
| Owner | Systems Architecture |
| Last Updated | 2026-08-29 |
| Primary Function | Define the operational model through which persistent interpersonal relationships form, evolve, influence behavior and retain history |

> **People create stories. Relationships give those stories meaning.**

---

# 1. Purpose

The Relationship Engine defines how persistent interpersonal relationships operate inside Project Ascension.

The architectural responsibilities of the Relationships System are defined in:

```text
Canon/Systems/Relationships/README.md
```

This document defines the operational model.

It describes how:

```text
PEOPLE MEET

RELATIONSHIPS FORM

EXPERIENCES ACCUMULATE

EXPECTATIONS DEVELOP

TRUST CHANGES

CONFLICT EMERGES

BONDS STRENGTHEN

BETRAYAL MATTERS

REPAIR BECOMES POSSIBLE

RELATIONSHIPS TRANSFORM

AND

HISTORY CONTINUES TO MATTER.
```

The Relationship Engine must produce relationships that feel:

- persistent
- contextual
- asymmetric
- multidimensional
- historically grounded
- imperfect
- understandable
- capable of surprising outcomes

The engine does not exist to calculate whether two people "like" one another.

It exists to model:

> **What has happened between these people, what they have learned to expect from one another, and how that history affects what happens next.**

---

# 2. Core Philosophy

No person exists in isolation.

Every individual develops inside networks of:

```text
FAMILY

FRIENDSHIP

WORK

LOVE

COMMUNITY

AUTHORITY

DEPENDENCE

CONFLICT

AND

SHARED EXPERIENCE.
```

These relationships influence future decisions.

But relationships do not replace personality or agency.

The same relationship may influence two people differently.

Therefore:

```text
RELATIONSHIP
+
CHARACTER A
=
ONE EXPERIENCE

RELATIONSHIP
+
CHARACTER B
=
ANOTHER EXPERIENCE.
```

The Relationship Engine preserves the shared history.

Characters preserve their subjective experience of it.

---

# 3. Fundamental Relationship Model

At its simplest:

```text
TWO ACTORS
        ↓
INTERACTION
        ↓
EVENT
        ↓
PERCEPTION
        ↓
INTERPRETATION
        ↓
RELATIONAL CONSEQUENCE
        ↓
UPDATED RELATIONSHIP STATE
        ↓
FUTURE EXPECTATION
        ↓
FUTURE INTERACTION
```

But this loop is influenced by existing history.

A more complete model is:

```text
CURRENT RELATIONSHIP STATE
+
RELATIONAL HISTORY
+
CURRENT EVENT
+
CONTEXT
+
EXPECTATION
+
CHARACTER INTERPRETATION
+
CONSEQUENCE
+
TIME
=
UPDATED RELATIONSHIP STATE.
```

This is a conceptual model.

It is not intended as a rigid mathematical formula.

---

# 4. Relationship Entity

A persistent relationship should conceptually contain:

```text
Relationship
│
├── Participants
├── Relationship Type
├── Origin
├── Current Dimensions
├── Directional States
├── Shared History
├── Significant Events
├── Expectations
├── Promises
├── Obligations
├── Dependencies
├── Unresolved Conflicts
├── Secrets / Shared Knowledge References
├── Milestones
├── Current Stability
├── Current Activity
└── Last Significant Change
```

Not every relationship requires every field at high resolution.

The model may be compressed according to simulation relevance.

---

# 5. Participants

A relationship requires at least two actors.

Conceptually:

```text
RELATIONSHIP R-001

Participants:

A
B
```

The relationship connects them.

But many relational properties may be directional.

For example:

```text
A → B Trust

B → A Trust
```

may differ.

Therefore the engine must support both:

```text
SHARED RELATIONAL STATE
```

and:

```text
DIRECTIONAL RELATIONAL STATE.
```

---

# 6. Shared vs Directional State

Some relationship properties are naturally shared.

Examples:

```text
how long they have known one another

whether they are siblings

whether they worked together

whether a promise occurred

whether they survived an event together

whether a betrayal objectively occurred.
```

Other properties are directional.

Examples:

```text
A trusts B

B trusts A

A fears B

B respects A

A feels obligated to B.
```

Therefore:

```text
SHARED HISTORY
≠
SHARED INTERPRETATION.
```

---

# 7. Relationship Type

Relationships may possess descriptive categories.

Examples include:

```text
FAMILY

FRIENDSHIP

ROMANTIC

PROFESSIONAL

MENTORSHIP

AUTHORITY

RIVALRY

HOSTILITY

COMMUNITY

DEPENDENCY.
```

Multiple categories may coexist.

For example:

```text
SIBLINGS
+
BUSINESS PARTNERS
+
POLITICAL RIVALS.
```

Relationship Type provides context.

It does not determine relational quality.

---

# 8. Relationship Origin

Every persistent relationship should have a plausible origin.

Examples:

```text
family

school

university

work

research

military service

community

migration

shared crisis

mutual acquaintance

romantic encounter

professional collaboration

chance encounter.
```

Origin establishes:

```text
WHEN

WHERE

WHY

AND

UNDER WHAT CONDITIONS

THE RELATIONSHIP BEGAN.
```

The Life System may generate this history.

The Relationship Engine preserves its relational consequences.

---

# 9. Relationship Dimensions

Relationships are multidimensional.

The initial canonical dimension set should include:

```text
TRUST

AFFECTION

RESPECT

LOYALTY

FAMILIARITY

DEPENDENCE

OBLIGATION

RESENTMENT

FEAR

HOSTILITY

INTIMACY.
```

Additional dimensions may be introduced only where they represent genuinely different relational phenomena.

The system should avoid dimension proliferation.

---

# 10. Dimensions Are Not Personality Traits

Relationship dimensions exist:

```text
BETWEEN SPECIFIC ACTORS.
```

They do not define general personality.

For example:

```text
A trusts B deeply.
```

This does not mean:

```text
A is generally trusting.
```

Character personality may influence how easily trust develops.

The relationship records whether trust exists with this particular person.

---

# 11. Trust

Trust represents learned expectation that another actor will behave reliably within a relevant domain.

Trust should support domain specificity.

Possible domains include:

```text
PERSONAL TRUST

PROFESSIONAL TRUST

INFORMATION TRUST

SAFETY TRUST

CONFIDENTIALITY TRUST

MORAL TRUST

DECISION TRUST

SURVIVAL TRUST.
```

Example:

```text
A trusts B to repair a generator.

A does not trust B with private information.
```

Both may simultaneously be true.

---

# 12. Trust Formation

Trust may increase through repeated evidence of:

```text
RELIABILITY

HONESTY

COMPETENCE

CONSISTENCY

RECIPROCITY

PROTECTION

VULNERABILITY

AND

FULFILLED EXPECTATION.
```

Conceptually:

```text
EXPECTATION
↓
BEHAVIOR
↓
EXPECTATION CONFIRMED
↓
TRUST REINFORCED.
```

Trust normally develops through repeated evidence.

But high-impact events may accelerate development.

---

# 13. Trust Violation

Trust may decline when expected behavior is violated.

Conceptually:

```text
EXPECTATION
↓
BEHAVIOR
↓
EXPECTATION VIOLATED
↓
INTERPRETATION
↓
TRUST DAMAGE.
```

Severity depends on:

```text
IMPORTANCE

CONSEQUENCE

INTENT

PREVIOUS TRUST

RELATIONSHIP TYPE

AND

HISTORY.
```

---

# 14. Trust Asymmetry

Trust is directional.

Example:

```text
A → B = HIGH TRUST

B → A = LOW TRUST.
```

This may occur because:

- one person knows more
- one has been betrayed before
- one depends more heavily on the other
- one misunderstands the relationship
- information is asymmetric
- expectations differ

The engine must preserve this asymmetry.

---

# 15. Affection

Affection represents emotional attachment.

Affection may coexist with:

```text
RESENTMENT

DISTRUST

ANGER

FEAR

OR

CONFLICT.
```

Example:

```text
A loves B.

A no longer trusts B.
```

This should be completely valid.

---

# 16. Respect

Respect represents recognition of qualities such as:

```text
COMPETENCE

COURAGE

INTEGRITY

EXPERIENCE

INTELLIGENCE

AUTHORITY

OR

SACRIFICE.
```

Respect may exist between enemies.

Respect does not imply:

```text
AFFECTION

TRUST

OR

LOYALTY.
```

---

# 17. Loyalty

Loyalty represents willingness to preserve commitment despite cost.

It may emerge from:

```text
LOVE

FAMILY

DUTY

IDEOLOGY

GRATITUDE

SHARED HISTORY

IDENTITY

OBLIGATION.
```

Loyalty should become visible when maintaining the relationship becomes costly.

---

# 18. Familiarity

Familiarity represents accumulated knowledge produced through interaction.

High familiarity may allow one person to:

```text
recognize behavior

anticipate reactions

understand communication shortcuts

detect unusual behavior

or

notice emotional changes.
```

Familiarity can exist in both positive and hostile relationships.

---

# 19. Dependence

Dependence represents practical reliance.

Possible domains include:

```text
FOOD

SECURITY

MEDICINE

TRANSPORTATION

INFORMATION

TECHNICAL CAPABILITY

SOCIAL ACCESS

EMOTIONAL SUPPORT

OR

ECONOMIC SUPPORT.
```

Dependence may strengthen a relationship.

It may also produce:

```text
RESENTMENT

FEAR

OBLIGATION

OR

POWER IMBALANCE.
```

---

# 20. Obligation

Obligation represents a perceived duty toward another person.

Sources may include:

```text
PROMISE

FAMILY

RESCUE

SACRIFICE

DEBT

SOCIAL EXPECTATION

MORAL RESPONSIBILITY

OR

PAST SUPPORT.
```

Obligation may survive after affection disappears.

---

# 21. Resentment

Resentment represents accumulated unresolved negative relational experience.

It may emerge through:

```text
perceived unfairness

repeated disappointment

dependency

humiliation

broken expectations

unequal sacrifice

unresolved conflict.
```

Resentment may accumulate gradually.

This makes it especially important for long-running relationships.

---

# 22. Fear

Fear represents perceived threat associated with another actor.

Fear may arise from:

```text
violence

authority

unpredictability

past behavior

reputation

power imbalance

or

credible threat.
```

Fear may produce compliance.

But:

```text
FEAR
≠
LOYALTY.
```

---

# 23. Hostility

Hostility represents active antagonism.

It may emerge through:

```text
conflict

competition

betrayal

ideology

revenge

resource disputes

or

accumulated resentment.
```

Hostility does not automatically eliminate respect.

---

# 24. Intimacy

Intimacy represents access to private aspects of another person's life.

This may include:

```text
private knowledge

emotional vulnerability

personal history

shared secrets

physical intimacy

deep familiarity.
```

Intimacy creates relational significance.

It may also create vulnerability.

---

# 25. Relationship Events

The engine should distinguish ordinary interaction from relationally significant events.

A Relationship Event is an interaction with sufficient consequence to potentially alter persistent relational state.

Examples include:

```text
HELP

RESCUE

SACRIFICE

BETRAYAL

DECEPTION

PROMISE

BROKEN PROMISE

ABANDONMENT

VULNERABILITY

SHARED DANGER

SHARED SUCCESS

SHARED LOSS

HUMILIATION

VIOLENCE

FORGIVENESS

RECONCILIATION.
```

---

# 26. Event Evaluation

When a relational event occurs, the engine should conceptually evaluate:

```text
WHAT HAPPENED?

WHO WAS INVOLVED?

WHAT DID EACH PERSON KNOW?

WHAT DID EACH PERSON EXPECT?

WHAT WAS INTENDED?

WHAT ACTUALLY HAPPENED?

WHAT WERE THE CONSEQUENCES?

HOW DID EACH PERSON INTERPRET IT?

HOW IMPORTANT WAS IT?

WHAT HISTORY ALREADY EXISTED?
```

Only then should persistent relational state change.

---

# 27. Event Significance

Relational events may have different significance.

Conceptually:

```text
ROUTINE

NOTABLE

SIGNIFICANT

MAJOR

DEFINING.
```

A defining event may permanently alter the relationship.

Examples:

```text
saving someone's child

deliberately abandoning someone

revealing years of deception

risking death for another person.
```

---

# 28. Subjective Significance

Event significance is partly subjective.

The same action may matter differently to different people.

Example:

```text
A forgets B's birthday.
```

For A:

```text
minor mistake.
```

For B:

```text
confirmation that A no longer cares.
```

Therefore:

```text
OBJECTIVE EVENT MAGNITUDE
≠
SUBJECTIVE RELATIONAL SIGNIFICANCE.
```

---

# 29. Expectation Model

Expectations are central to relationship dynamics.

Relationships generate predictions about behavior.

Examples:

```text
I expect you to help me.

I expect you to tell me the truth.

I expect you to protect my secret.

I expect you to remain loyal.

I expect you to understand why this matters.
```

Expectations may be:

```text
EXPLICIT

IMPLICIT

MUTUAL

ONE-SIDED

REALISTIC

OR

UNREALISTIC.
```

---

# 30. Expectation Confirmation

When behavior matches expectation:

```text
EXPECTED BEHAVIOR
+
OBSERVED BEHAVIOR
=
RELATIONAL CONFIRMATION.
```

This may reinforce:

```text
TRUST

FAMILIARITY

SECURITY

OR

RESPECT.
```

Not every confirmation requires a significant update.

Stable relationships depend heavily on repeated ordinary confirmation.

---

# 31. Expectation Violation

When behavior violates expectation:

```text
EXPECTED BEHAVIOR
≠
OBSERVED BEHAVIOR.
```

The result may include:

```text
SURPRISE

CONFUSION

ANGER

DISTRUST

RESENTMENT

FEAR

OR

REASSESSMENT.
```

The engine should evaluate why the expectation failed.

---

# 32. Promises

Promises create explicit relational expectations.

A promise record should conceptually include:

```text
PROMISER

RECIPIENT

COMMITMENT

CONDITIONS

DATE

STATUS

OUTCOME.
```

Possible status:

```text
ACTIVE

FULFILLED

BROKEN

RELEASED

IMPOSSIBLE

DISPUTED.
```

Promises may have long-term relational consequences.

---

# 33. Broken Promises

A broken promise does not automatically equal betrayal.

The engine should consider:

```text
WAS IT INTENTIONAL?

WAS FULFILLMENT POSSIBLE?

DID CIRCUMSTANCES CHANGE?

WAS THE PROMISE UNDERSTOOD THE SAME WAY?

WHAT WAS THE CONSEQUENCE?

WAS AN EXPLANATION PROVIDED?
```

This allows nuanced interpretation.

---

# 34. Betrayal

Betrayal occurs when a significant relational expectation is violated in a way interpreted as a breach of the relationship.

Conceptually:

```text
TRUST
+
EXPECTATION
+
VIOLATION
+
RELATIONAL SIGNIFICANCE
=
POTENTIAL BETRAYAL.
```

The stronger the original trust and expectation:

```text
THE GREATER
THE POTENTIAL CONSEQUENCE.
```

---

# 35. Betrayal Memory

Major betrayal becomes part of persistent relational history.

It should not disappear because:

```text
TIME PASSED

THE PLAYER COMPLETED A QUEST

OR

AN APOLOGY OCCURRED.
```

Future behavior may change.

History remains.

---

# 36. Forgiveness

Forgiveness represents a change in how a past violation is carried forward.

It does not mean:

```text
EVENT DELETED.
```

Possible outcome:

```text
RESENTMENT ↓

HOSTILITY ↓

AFFECTION remains

TRUST remains damaged

BOUNDARIES increase.
```

This is a valid repaired relationship.

---

# 37. Reconciliation

Reconciliation requires renewed interaction after rupture.

Conceptually:

```text
RUPTURE
↓
ACKNOWLEDGMENT
↓
ACCOUNTABILITY
↓
NEW BEHAVIOR
↓
TIME
↓
NEW EVIDENCE
↓
RELATIONSHIP RECONSTRUCTION.
```

The result is not:

```text
OLD RELATIONSHIP RESTORED.
```

It is:

```text
NEW RELATIONSHIP
WITH OLD HISTORY.
```

---

# 38. Relational Inertia

Established relationships resist sudden change.

Conceptually:

```text
LONG HISTORY
=
HIGH RELATIONAL INERTIA.
```

A twenty-year friendship should normally require substantial cause to collapse.

Likewise, decades of hostility should normally require substantial cause to transform.

Relational inertia prevents unrealistic volatility.

---

# 39. Threshold Events

Some events may overwhelm relational inertia.

Examples:

```text
LIFE-SAVING SACRIFICE

ATTEMPTED MURDER

ABANDONMENT DURING CRISIS

REVELATION OF LONG-TERM DECEPTION

EXTREME COURAGE

MAJOR BETRAYAL.
```

Threshold events should be rare enough to retain significance.

---

# 40. Accumulation

Small events may accumulate.

Conceptually:

```text
SMALL DISAPPOINTMENT
+
SMALL DISAPPOINTMENT
+
SMALL DISAPPOINTMENT
+
TIME
=
RESENTMENT.
```

Likewise:

```text
SMALL RELIABLE ACTION
+
SMALL RELIABLE ACTION
+
SMALL RELIABLE ACTION
+
TIME
=
TRUST.
```

This is one of the most important relationship mechanics.

Relationships are shaped both by:

```text
MOMENTS
```

and:

```text
PATTERNS.
```

---

# 41. Pattern Recognition

Characters may begin recognizing relational patterns.

Examples:

```text
She always disappears when things become difficult.

He never lies about operational risk.

She criticizes me publicly but protects me privately.

He keeps promises even when they hurt him.
```

Patterns may influence expectations more strongly than individual events.

---

# 42. Relational Stability

Relationship Stability represents resistance to major change.

It may emerge from:

```text
shared history

mutual dependence

strong trust

family structure

long-term commitment

compatible expectations

repeated repair.
```

High stability does not necessarily mean:

```text
HEALTHY.
```

A deeply dysfunctional relationship may also be highly stable.

---

# 43. Relational Volatility

Some relationships change rapidly.

Possible causes include:

```text
limited history

high emotional intensity

unstable circumstances

conflicting expectations

low trust

strong dependence

high fear

or

unresolved conflict.
```

Volatility should emerge from relational conditions.

It should not be random drama generation.

---

# 44. Relationship Lifecycle

Relationships may move through states such as:

```text
UNKNOWN
↓
AWARENESS
↓
CONTACT
↓
FAMILIARITY
↓
ESTABLISHED RELATIONSHIP
↓
DEEPENING / STABILITY / CONFLICT
↓
TRANSFORMATION
↓
DORMANCY / RUPTURE / CONTINUITY
↓
RECONNECTION OR END.
```

This is not a mandatory linear progression.

Relationships may skip stages.

They may reverse.

They may remain stable for decades.

---

# 45. Dormancy

Relationships may become inactive.

Example:

```text
two university friends
lose contact for twelve years.
```

The relationship should not necessarily disappear.

The engine may preserve:

```text
shared history

last known state

important memories

unresolved obligations

major emotional significance.
```

Reunion can reactivate the relationship.

---

# 46. Time

Time influences relationships.

But:

```text
TIME
ALONE
DOES NOT DETERMINE
RELATIONSHIP QUALITY.
```

Some relationships survive decades of separation.

Others decay quickly.

Time interacts with:

```text
contact

history

importance

life changes

distance

memory

and

new relationships.
```

---

# 47. Relationship Decay

Certain dimensions may decay without reinforcement.

Examples:

```text
active familiarity

routine professional trust

everyday intimacy

minor obligation.
```

Other states may remain persistent.

Examples:

```text
major betrayal

family identity

life-saving sacrifice

deep attachment

historical resentment.
```

Decay should therefore be dimension-specific.

---

# 48. Relationship Transformation

Relationships may change category.

Examples:

```text
STRANGER
→
COLLEAGUE
→
FRIEND

FRIEND
→
ROMANTIC PARTNER

MENTOR
→
PEER

ALLY
→
RIVAL

ENEMY
→
RELUCTANT ALLY

PARTNER
→
ESTRANGED FAMILY.
```

Transformation should emerge through events and history.

---

# 49. Relationship Memory

The engine should preserve relationally significant history.

A conceptual relationship memory may contain:

```text
EVENT

DATE / PERIOD

PARTICIPANTS

CONTEXT

SIGNIFICANCE

RELATIONAL CONSEQUENCE

CURRENT RELEVANCE.
```

Not every conversation should become permanent memory.

---

# 50. Memory Compression

Over time, detailed interaction history may be compressed.

For example:

```text
hundreds of cooperative work interactions
```

may become:

```text
Five years of consistently reliable
professional cooperation.
```

But major events should remain explicit.

Examples:

```text
B saved A during the Oakland evacuation.

A later concealed critical information from B.

They reconciled two years later,
but information trust never fully recovered.
```

---

# 51. Relationship Milestones

The engine may preserve major milestones such as:

```text
FIRST MEETING

FIRST TRUST

FIRST MAJOR CONFLICT

FIRST VULNERABILITY

FIRST SACRIFICE

MAJOR BETRAYAL

RECONCILIATION

ROMANTIC COMMITMENT

SEPARATION

REUNION

SHARED LOSS

FINAL RUPTURE.
```

Milestones provide compressed historical anchors.

---

# 52. Shared Secrets

Shared secrets may create relational significance.

They may increase:

```text
INTIMACY

TRUST

DEPENDENCE

OR

VULNERABILITY.
```

But the secret itself belongs to the appropriate information or character state.

The Relationship Engine stores:

```text
THE RELATIONAL SIGNIFICANCE
OF SHARING IT.
```

---

# 53. Secret Violation

If shared private information is exposed:

```text
INFORMATION EVENT
↓
EXPECTATION VIOLATION
↓
POTENTIAL BETRAYAL
↓
RELATIONAL CONSEQUENCE.
```

The Relationship Engine does not determine whether the information was true.

It determines the relational consequence of the event.

---

# 54. Obligation Tracking

Important obligations should remain persistent.

Example:

```text
B saved A's daughter.
```

A may develop:

```text
GRATITUDE

OBLIGATION

TRUST

AFFECTION

OR

DISCOMFORT.
```

The event itself does not force a specific reaction.

Character interpretation matters.

---

# 55. Power

Relationships may contain power differences.

Power may come from:

```text
authority

resources

knowledge

social status

physical capability

technical capability

institutional position

dependency.
```

Power affects available choices.

It does not define emotional state.

---

# 56. Coercive Relationships

A coercive relationship may produce:

```text
COMPLIANCE

FEAR

DEPENDENCE

RESENTMENT.
```

It should not automatically produce:

```text
TRUST

LOYALTY

RESPECT

OR

AFFECTION.
```

This distinction is mandatory.

---

# 57. Reciprocity

Relationships often develop reciprocal expectations.

But reciprocity is interpreted individually.

Example:

```text
A gives B food.
```

B may experience:

```text
GRATITUDE

OBLIGATION

HUMILIATION

SUSPICION

RELIEF

OR

NO MAJOR RELATIONAL CHANGE.
```

Context determines meaning.

---

# 58. Relationship Networks

Each person exists within a network of relationships.

Conceptually:

```text
             B
             ↕
       C ↔ PERSON ↔ D
             ↕
             E
```

Networks create pathways for:

```text
information

reputation

resources

conflict

cooperation

and

social influence.
```

But relationship state should not automatically propagate through the network.

---

# 59. Third-Party Influence

Third parties may influence relationships through:

```text
information

rumor

mediation

manipulation

shared experience

family pressure

institutional pressure.
```

Example:

```text
C tells A that B betrayed them.
```

This creates:

```text
INFORMATION RECEIVED BY A.
```

It does not automatically establish:

```text
B BETRAYED A.
```

A must interpret the information.

---

# 60. Reputation and Relationships

Reputation may influence initial relationship expectations.

Conceptually:

```text
REPUTATION
↓
INITIAL EXPECTATION
↓
FIRST INTERACTION
↓
RELATIONSHIP DEVELOPMENT.
```

Reputation should not permanently override direct experience.

---

# 61. Group Dynamics

Relationships form the interpersonal foundation beneath group behavior.

For example:

```text
GROUP
│
├── A trusts B
├── B distrusts C
├── C depends on D
├── D respects A
└── A resents C
```

These connections may produce emergent:

```text
leadership

coalitions

conflict

information bottlenecks

loyalty structures

and

group instability.
```

Group-level state belongs to the appropriate Society or group architecture.

---

# 62. Leadership

Leadership is partly relational.

Formal authority may exist without trust.

Informal leadership may emerge without formal authority.

A leader may possess:

```text
RESPECT

TRUST

DEPENDENCE

LOYALTY

OR

FEAR
```

across different group members.

Therefore:

```text
LEADERSHIP
≠
ONE UNIVERSAL RELATIONSHIP STATE.
```

---

# 63. Relationship Influence on Decisions

Relationships may influence Character decision-making.

For example:

```text
Would I normally take this risk?

No.

Would I take it to save my daughter?

Yes.
```

Relationship state therefore becomes contextual input to Character reasoning.

But the Relationship Engine does not make the decision.

The Character System does.

---

# 64. Relationship Influence on Information

Characters may choose to share information based partly on:

```text
trust

loyalty

fear

obligation

intimacy

professional role

or

dependency.
```

Again:

```text
RELATIONSHIP
INFLUENCES DECISION.
```

It does not automatically cause information transfer.

---

# 65. Relationship Influence on Cooperation

Existing relationships may affect willingness to:

```text
cooperate

share resources

accept risk

travel together

follow advice

provide shelter

offer medical assistance

or

defend someone.
```

But no relationship dimension guarantees cooperation.

Context matters.

---

# 66. Relationship Influence on Conflict

Conflict may become more or less likely depending on relational history.

A small disagreement between strangers may be irrelevant.

The same disagreement between siblings carrying twenty years of resentment may activate:

```text
OLDER HISTORY.
```

Relationships provide context for conflict.

---

# 67. Character Interpretation

The Character System remains responsible for subjective interpretation.

Conceptually:

```text
RELATIONAL EVENT
↓
CHARACTER PERSONALITY
+
MEMORY
+
VALUES
+
CURRENT EMOTION
+
PAST EXPERIENCE
↓
INTERPRETATION
↓
PROPOSED RELATIONAL CONSEQUENCE.
```

The systems must therefore exchange information without collapsing ownership boundaries.

---

# 68. Relationship Update Cycle

A high-level update cycle may be:

```text
1. RELATIONAL EVENT OCCURS

2. PARTICIPANTS IDENTIFIED

3. EXISTING RELATIONSHIP RETRIEVED

4. RELEVANT EXPECTATIONS RETRIEVED

5. CHARACTER INTERPRETATIONS RESOLVED

6. EVENT SIGNIFICANCE ASSESSED

7. RELATIONAL CONSEQUENCES PROPOSED

8. RELATIONSHIP STATE UPDATED

9. SIGNIFICANT HISTORY RECORDED

10. DOWNSTREAM CONSEQUENCES EMITTED.
```

This provides a future implementation structure without locking exact algorithms.

---

# 69. Relationship Change Proposal

To preserve system ownership, other systems should not directly rewrite relational state.

Conceptually:

```text
CHARACTER SYSTEM

"I interpreted B's action as betrayal."
```

becomes:

```text
RELATIONSHIP CHANGE PROPOSAL
```

rather than:

```text
DIRECT RELATIONSHIP MUTATION.
```

The Relationship Engine evaluates the proposal against:

```text
history

context

event

expectation

and

current state.
```

---

# 70. Relationship Event Record

A future implementation may use a structure similar to:

```text
RelationshipEvent

event_id
timestamp
participants
event_type
context
objective_outcome
participant_interpretations
significance
expectations_affected
relationship_dimensions_affected
persistent_memory_required
downstream_effects
```

This is conceptual architecture.

Exact implementation remains open.

---

# 71. Relationship State Record

A future implementation may conceptually contain:

```text
RelationshipState

relationship_id
participants
relationship_types
origin
directional_dimensions
shared_history
milestones
promises
obligations
dependencies
unresolved_conflicts
stability
activity_state
resolution_level
last_significant_update
```

Again:

```text
CONCEPTUAL MODEL
≠
FINAL DATA SCHEMA.
```

---

# 72. Relationship Resolution

Relationships should operate at variable simulation resolution.

Suggested conceptual levels:

```text
LEVEL 0 — CONNECTION

Relationship exists.

LEVEL 1 — CATEGORY

Basic type and broad quality.

LEVEL 2 — STATE

Core dimensions and important history.

LEVEL 3 — ACTIVE

Detailed expectations, obligations and event history.

LEVEL 4 — HIGH RESOLUTION

Active interpretation and dynamic relational change.

LEVEL 5 — CRITICAL

Full continuity for relationships central to current simulation.
```

---

# 73. Resolution Escalation

Resolution may increase when:

```text
player interaction increases

relationship becomes campaign relevant

major conflict occurs

major trust event occurs

characters become locally important

Aurora interacts directly

or

relationship consequences become systemic.
```

New detail must respect existing state.

---

# 74. Resolution Compression

When relevance decreases:

```text
HIGH-RESOLUTION INTERACTIONS
↓
COMPRESSED RELATIONAL HISTORY.
```

Preserve:

```text
major events

current dimensions

promises

obligations

betrayals

milestones

unresolved conflict

relationship category

and

important expectations.
```

---

# 75. Off-Screen Evolution

Relationships continue outside player attention.

At lower resolution the engine may simulate:

```text
continued contact

distance

cooperation

minor conflict

major external events

life changes

relationship drift.
```

It should not fabricate major relational transformations without plausible causes.

---

# 76. Off-Screen Major Events

If a major relationship-changing event occurs off-screen:

```text
EVENT
↓
RELATIONSHIP UPDATE
↓
PERSISTENT HISTORY
↓
POSSIBLE CAMPAIGN CONSEQUENCE.
```

The player does not need to witness the event for it to be real.

---

# 77. Death

When one participant dies:

```text
ACTIVE INTERACTION
ENDS.
```

But the relationship may continue influencing the survivor.

Preserve relevant:

```text
love

grief

anger

guilt

promises

obligations

memory

unfinished conflict.
```

The relationship becomes historical rather than active.

---

# 78. Reconnection

Characters separated for long periods may meet again.

The engine should evaluate:

```text
OLD RELATIONSHIP STATE

TIME APART

LIFE CHANGES

NEW INFORMATION

CURRENT EXPECTATIONS

AND

THE REUNION EVENT.
```

The relationship should not simply resume from its previous state unchanged.

---

# 79. Generational Relationships

Relationships between generations may carry historical asymmetry.

Example:

```text
grandparent remembers Connected World

parent experienced Transition

child grew up during Fracture.
```

They may disagree fundamentally about:

```text
trust

technology

risk

authority

community

and

the future.
```

Yet remain deeply connected.

---

# 80. World State Pressure

World States influence relational context.

They do not define relationships.

Conceptually:

```text
WORLD STATE
↓
PRESSURE / OPPORTUNITY
↓
RELATIONAL EVENTS
↓
HUMAN INTERPRETATION
↓
RELATIONSHIP CHANGE.
```

Never:

```text
WORLD STATE
↓
EVERYONE BECOMES DISTRUSTFUL.
```

---

# 81. Connected World Relationships

State 01 supports:

```text
high mobility

digital communication

large networks

international relationships

professional mobility

family dispersion.
```

Distance often does not prevent continued contact.

---

# 82. Transition Relationships

State 02 introduces new pressures:

```text
rapid professional change

AI-mediated interaction

economic restructuring

verification pressure

institutional uncertainty

migration

information fragmentation.
```

But ordinary relationships remain central to life.

---

# 83. Fractured World Relationships

State 03 may increase practical importance of relationships.

Who you know may affect access to:

```text
food

medicine

information

transport

shelter

security

employment

and

safe passage.
```

But relationships remain emotional and human.

They do not become only survival mechanics.

---

# 84. Reconnection Relationships

State 04 creates opportunities for:

```text
reunion

reconciliation

rediscovery

conflicting histories

new networks

interregional families

and

long-separated communities reconnecting.
```

The return of reliable communication may reconnect relationships that survived years of separation.

---

# 85. Player Relationships

Player relationships use the same engine.

There should be no separate:

```text
PLAYER FRIENDSHIP SYSTEM
```

that grants simplified rules.

Players are participants in the same relational world.

---

# 86. NPC Relationships

NPC-to-NPC relationships matter even when the player is not involved.

They may produce:

```text
alliances

conflict

families

betrayal

migration

resource sharing

leadership

or

community change.
```

This is essential for the Living World.

---

# 87. No Player Privilege

Characters should not automatically:

```text
trust the player faster

forgive the player faster

fall in love with the player

reveal secrets to the player

or

abandon lifelong relationships
for the player.
```

The player must exist inside the same human logic as everyone else.

---

# 88. Aurora Relationship Model

Aurora maintains her own internal relational understanding.

Conceptually:

```text
WORLD RELATIONSHIP
        ↓
OBSERVABLE EVIDENCE
        ↓
AURORA OBSERVATION
        ↓
AURORA RELATIONSHIP MODEL.
```

Aurora's model may be:

```text
accurate

incomplete

uncertain

or

wrong.
```

---

# 89. Aurora as Participant

Aurora may herself become a participant in relationships.

Example:

```text
HUMAN
↕
RELATIONAL HISTORY
↕
AURORA.
```

But Aurora's internal emotional, cognitive and relational interpretation remains owned by Aurora's architecture.

The Relationships System preserves relevant shared interaction history.

---

# 90. Aurora Does Not Bypass Privacy

Aurora may be capable of extraordinary inference.

But:

```text
INFERENCE
≠
RELATIONSHIP TRUTH.
```

She requires information paths.

She may misunderstand why people behave as they do.

This limitation is canonical.

---

# 91. Narrative Integration

The Relationship Engine should expose relational consequences to Narrative without exposing raw architecture unnecessarily.

Narrative may translate:

```text
HIGH INFORMATION TRUST
+
LOW PERSONAL AFFECTION
```

into behavior such as:

```text
"I don't like him.

But if he says the bridge is safe,
I'd cross it."
```

This is preferable to exposing numeric values.

---

# 92. Behavioral Expression

Relationship state should become visible through behavior.

Examples:

High trust:

```text
She hands him the radio
without asking what he intends to do.
```

Damaged trust:

```text
She gives him the radio,
but removes the battery first.
```

Resentment:

```text
He agrees to help,
then reminds her exactly
what this is costing him.
```

Deep familiarity:

```text
She knows he is lying
before he finishes the sentence.
```

Relationships should be experienced.

Not merely reported.

---

# 93. Emergent Narrative

The Relationship Engine does not generate stories directly.

It generates conditions from which stories emerge.

A betrayal matters because:

```text
TRUST EXISTED.
```

A sacrifice matters because:

```text
SOMETHING WAS WORTH SACRIFICING FOR.
```

A reunion matters because:

```text
SEPARATION HAD CONSEQUENCE.
```

A death matters because:

```text
SOMEONE IS LEFT BEHIND.
```

Narrative emerges from relational history.

---

# 94. Relationship with Life

```text
LIFE
```

answers:

```text
HOW DID THESE PEOPLE
BECOME CONNECTED?
```

```text
RELATIONSHIP ENGINE
```

answers:

```text
WHAT HAS HAPPENED
BETWEEN THEM SINCE?
```

Life provides origins.

Relationships provides continuity.

---

# 95. Relationship with Characters

Characters own:

```text
personality

current beliefs

goals

private memory

emotion

decision-making.
```

Relationships owns:

```text
persistent relational state

shared relational history

promises

obligations

relationship milestones.
```

The systems continuously exchange context.

---

# 96. Relationship with Society

Relationships form parts of larger social structures.

Society may use relational patterns to understand:

```text
cohesion

leadership

social networks

community structure

institutional legitimacy.
```

But Society should not rewrite individual relationship state.

---

# 97. Relationship with World Simulation

World Simulation creates external conditions.

Relationships interprets their interpersonal consequences.

Example:

```text
WORLD SIMULATION

Regional food shortage.
```

```text
CHARACTER A

secretly keeps extra food.
```

```text
CHARACTER B

discovers it.
```

```text
RELATIONSHIP ENGINE

evaluates expectation,
context and history.
```

```text
RESULT

trust may decline,
resentment may increase,
or behavior may be understood.
```

---

# 98. Relationship with Living Campaign Engine

The Living Campaign Engine may identify relationships as campaign-relevant.

Examples:

```text
old friend now controls bridge access

estranged sibling appears in settlement

former colleague knows critical information

old rival leads regional authority.
```

The campaign engine discovers relevance.

It does not invent the relationship.

---

# 99. Relationship with Narrative

Narrative presents relational consequences.

It may determine:

```text
which moment to emphasize

which behavior to show

which memory becomes relevant

how dialogue expresses tension.
```

Narrative does not change relationship truth merely to create drama.

---

# 100. Relationship with Progression

Long-term relational development may contribute to broader progression.

But Relationships remains authoritative for:

```text
THE RELATIONSHIP ITSELF.
```

Progression should not create:

```text
FRIENDSHIP LEVELS
```

that bypass relational causality.

---

# 101. Relationship Engine Inputs

The engine may receive:

```text
RELATIONAL EVENTS

CHARACTER INTERPRETATION

CURRENT CHARACTER STATE

LIFE HISTORY

WORLD CONDITIONS

SOCIETAL CONTEXT

TIME

INFORMATION EVENTS

PLAYER ACTION

AND

PREVIOUS RELATIONSHIP STATE.
```

---

# 102. Relationship Engine Outputs

The engine may produce:

```text
UPDATED RELATIONSHIP STATE

RELATIONAL MILESTONES

PROMISE STATE

OBLIGATION STATE

TRUST CHANGE

AFFECTION CHANGE

RESPECT CHANGE

LOYALTY CHANGE

RESENTMENT CHANGE

DEPENDENCE CHANGE

HOSTILITY CHANGE

RELATIONSHIP TRANSFORMATION

RELATIONSHIP RUPTURE

RECONCILIATION

AND

RELATIONAL CONSEQUENCE EVENTS.
```

---

# 103. System Flow

```text
WORLD / CHARACTER EVENT
        ↓
RELATIONAL RELEVANCE CHECK
        ↓
RELATIONSHIP RETRIEVAL
        ↓
EXPECTATION CONTEXT
        ↓
CHARACTER INTERPRETATION
        ↓
SIGNIFICANCE ASSESSMENT
        ↓
RELATIONAL CONSEQUENCE
        ↓
STATE UPDATE
        ↓
MEMORY / MILESTONE UPDATE
        ↓
DOWNSTREAM EVENT
        ↓
CHARACTER / SOCIETY / CAMPAIGN
        ↓
FUTURE INTERACTION
```

---

# 104. Explainability

Important relationship changes must remain explainable.

The engine should eventually be able to answer:

```text
WHY DOES A TRUST B?

WHY DID TRUST CHANGE?

WHAT EVENT CAUSED IT?

WHAT EXPECTATION WAS INVOLVED?

WHAT HISTORY MADE IT IMPORTANT?

WHAT DOES A BELIEVE HAPPENED?

WHAT DOES B BELIEVE HAPPENED?

WHAT REMAINS UNRESOLVED?
```

This is critical for both simulation quality and debugging.

---

# 105. Determinism and Variation

The Relationship Engine should be:

```text
CAUSALLY UNDERSTANDABLE
```

without being:

```text
PERFECTLY PREDICTABLE.
```

Human variation enters through:

```text
personality

history

current emotion

values

expectations

memory

context

and

interpretation.
```

The same event therefore need not produce identical relational consequences across different people.

---

# 106. Validation Scenarios

Future validation should include scenarios such as:

```text
LONG-TERM TRUST FORMATION

ASYMMETRIC TRUST

BROKEN PROMISE

MISUNDERSTOOD BETRAYAL

ACTUAL BETRAYAL

FORGIVENESS WITHOUT RESTORED TRUST

RECONCILIATION

SHARED DANGER

COERCIVE DEPENDENCE

LONG-DISTANCE DORMANCY

REUNION

OFF-SCREEN RELATIONSHIP CHANGE

THIRD-PARTY RUMOR

AURORA MISINTERPRETATION

PLAYER MANIPULATION ATTEMPT

DEATH OF PARTICIPANT

RELATIONSHIP ACROSS WORLD STATES.
```

---

# 107. Critical Validation Example — Misunderstood Betrayal

World Truth:

```text
A sends B a request for help.

Communication infrastructure fails.

B never receives it.

A believes B ignored the request.
```

Expected behavior:

```text
A may experience relational damage.

B should not possess knowledge
of the failed message.

Relationship state may become asymmetric.

Later discovery of the infrastructure failure
may allow reinterpretation.

History should preserve both:

the misunderstanding

and

the later correction.
```

This validates:

```text
INFORMATION BOUNDARIES

SUBJECTIVE INTERPRETATION

ASYMMETRY

RELATIONAL MEMORY

AND

RECONCILIATION.
```

---

# 108. Critical Validation Example — Love Without Trust

Initial state:

```text
A and B are siblings.

High affection.

Long shared history.
```

Event:

```text
B repeatedly lies about resource use.
```

Expected result:

```text
AFFECTION
may remain high.

INFORMATION TRUST
declines.

RESOURCE TRUST
declines.

RESENTMENT
may increase.

FAMILY OBLIGATION
may remain.
```

The engine must not collapse this into:

```text
RELATIONSHIP NEGATIVE.
```

---

# 109. Critical Validation Example — Enemy Respect

Initial state:

```text
A and B lead opposing groups.
```

Repeated events demonstrate:

```text
B keeps negotiated agreements

protects civilians

and

acts competently.
```

Possible result:

```text
HOSTILITY remains high.

POLITICAL CONFLICT remains.

RESPECT increases.

AGREEMENT TRUST increases.

AFFECTION remains low.
```

This is valid relational complexity.

---

# 110. Critical Validation Example — Player Coercion

Player threatens Character A.

A complies.

Expected result may include:

```text
COMPLIANCE = YES

FEAR ↑

RESENTMENT ↑

TRUST ↓

LOYALTY = UNCHANGED OR ↓
```

The system must never infer:

```text
COMPLIANCE
=
SUCCESSFUL RELATIONSHIP.
```

---

# 111. Canonical Invariants

The following invariants are mandatory.

## REL-ENG-INV-001 — Relationships Are Persistent

Meaningful relational consequences survive individual scenes.

---

## REL-ENG-INV-002 — Relationships Are Multidimensional

No universal relationship score may represent the complete state.

---

## REL-ENG-INV-003 — Directionality Is Preserved

A's state toward B may differ from B's state toward A.

---

## REL-ENG-INV-004 — Shared History Is Not Shared Interpretation

Participants may understand the same event differently.

---

## REL-ENG-INV-005 — Significant Change Requires Cause

Major relational change requires defensible relational events or accumulated patterns.

---

## REL-ENG-INV-006 — History Creates Inertia

Established relationships resist arbitrary change.

---

## REL-ENG-INV-007 — Patterns Matter

Repeated minor interactions may accumulate into major relational change.

---

## REL-ENG-INV-008 — Expectations Matter

Relational consequences depend partly on what participants expected.

---

## REL-ENG-INV-009 — Trust Is Domain-Specific

Trust may differ across contexts.

---

## REL-ENG-INV-010 — Compliance Is Not Trust

Coercion must not create false relational interpretation.

---

## REL-ENG-INV-011 — Dependence Is Not Affection

Practical reliance and emotional attachment remain separate.

---

## REL-ENG-INV-012 — Forgiveness Does Not Delete History

Past events remain part of relational continuity.

---

## REL-ENG-INV-013 — Reconciliation Creates New History

Repair does not restore an untouched previous state.

---

## REL-ENG-INV-014 — Information Requires a Path

Third parties do not automatically know relational events.

---

## REL-ENG-INV-015 — Aurora's Model Is Not Relationship Truth

Aurora may infer incorrectly.

---

## REL-ENG-INV-016 — Relationships Continue Off-Screen

Player attention does not determine relational existence.

---

## REL-ENG-INV-017 — Resolution Does Not Rewrite History

Higher detail must preserve established state.

---

## REL-ENG-INV-018 — Player Characters Use the Same Rules

Players receive no automatic relational privilege.

---

## REL-ENG-INV-019 — NPC Relationships Matter

NPC-to-NPC relationships may independently change the world.

---

## REL-ENG-INV-020 — Relationship State Influences but Does Not Control Characters

Characters retain agency.

---

# 112. Development Locks

Do not implement one universal relationship score.

Do not make relationship dimensions automatically symmetric.

Do not equate affection with trust.

Do not equate loyalty with affection.

Do not equate fear with respect.

Do not equate dependence with loyalty.

Do not equate compliance with trust.

Do not allow one minor event to erase substantial history.

Do not allow apologies to reset relationships.

Do not delete betrayal after forgiveness.

Do not make relationships mechanically improve through repetitive gifts.

Do not make communication expertise function as mind control.

Do not make family automatically positive.

Do not make romance automatically emerge from high affection.

Do not make enemies incapable of respect.

Do not make allies incapable of resentment.

Do not make relationships freeze off-screen.

Do not give third parties automatic relational knowledge.

Do not allow Aurora to access hidden relational truth without evidence.

Do not allow Narrative to fabricate relational history.

Do not allow Campaign systems to create convenient past relationships.

Do not rewrite history when resolution increases.

Do not make World State directly determine relationship values.

Do not make the Fractured World eliminate love, friendship or ordinary human connection.

---

# 113. Development Status

The Relationship Engine is currently:

```text
ARCHITECTURALLY DEFINED

CONCEPTUALLY OPERATIONAL

NOT YET NUMERICALLY LOCKED

NOT YET IMPLEMENTATION LOCKED.
```

This is intentional.

The engine now defines:

```text
WHAT MUST BE REPRESENTED

HOW RELATIONAL CHANGE SHOULD BE UNDERSTOOD

HOW SYSTEM OWNERSHIP WORKS

AND

WHAT BEHAVIOR MUST BE PRESERVED.
```

Exact:

```text
data structures

numeric ranges

decay rates

threshold values

event weights

update algorithms

and

runtime implementation
```

should be defined only after cross-system interfaces with Characters, Life, Society and Living Campaign are sufficiently stable.

---

# 114. Recommended Next Architecture

Before numerical implementation, the most valuable detailed relationship documents are likely:

```text
Relationship_State_Model.md

Relational_Event_Model.md

Trust_Model.md

Relationship_Memory.md
```

These should only be created after verifying that equivalent concepts do not already exist elsewhere in Canon.

The goal is not to maximize the number of files.

The goal is to create the minimum architecture required for a coherent living simulation.

---

# 115. Relationship Engine North Star

> **A relationship is not a score describing how two people feel about one another. It is the accumulated consequence of what has happened between them.**

---

# 116. Trust North Star

> **Trust is what one person has learned they can safely expect from another.**

---

# 117. History North Star

> **A relationship should be able to explain why it became what it is.**

---

# 118. Human Complexity North Star

> **People can love someone they do not trust, trust someone they do not like, depend on someone they resent, respect an enemy, and forgive someone they never want to see again.**

---

# 119. Simulation North Star

> **Relationships should be understandable without becoming predictable.**

---

# 120. Narrative North Star

> **A betrayal becomes meaningful because trust existed before it.**

---

# 121. Final Operational Model

```text
PEOPLE
↓
MEET
↓
INTERACT
↓
FORM EXPECTATIONS
↓
BUILD HISTORY
↓
DEVELOP TRUST / AFFECTION / RESPECT /
LOYALTY / DEPENDENCE / OBLIGATION /
RESENTMENT / FEAR / HOSTILITY / INTIMACY
↓
EXPERIENCE NEW EVENTS
↓
INTERPRET THEM THROUGH EXISTING HISTORY
↓
RELATIONSHIP CHANGES
↓
EXPECTATIONS CHANGE
↓
FUTURE BEHAVIOR CHANGES
↓
NEW EVENTS OCCUR
↓
HISTORY CONTINUES.
```

The Relationship Engine therefore does not ask:

```text
DO THESE PEOPLE LIKE EACH OTHER?
```

It asks:

```text
WHAT HAS HAPPENED BETWEEN THEM?

WHAT HAVE THEY LEARNED
TO EXPECT FROM ONE ANOTHER?

WHAT DO THEY STILL OWE ONE ANOTHER?

WHAT HAVE THEY FORGIVEN?

WHAT HAVE THEY NOT FORGOTTEN?

WHAT WOULD THEY RISK
FOR ONE ANOTHER?

WHAT WOULD THEY NEVER
TRUST ONE ANOTHER WITH AGAIN?

AND

WHAT HAPPENS WHEN
THEIR HISTORY IS TESTED?
```

---

# 122. Closing Statement

Project Ascension contains systems capable of changing civilizations.

But civilizations are lived through human connections.

When infrastructure fails, someone calls a friend.

When institutions become unreliable, someone asks who they trust.

When people flee, someone decides who comes with them.

When food becomes scarce, someone chooses whether to share.

When danger arrives, someone decides whether to stay.

When years of separation end, someone stands on the other side of the road.

And when the world begins reconnecting, the most important connection may not be:

```text
A POWER GRID

A NETWORK

A ROAD

OR

A GOVERNMENT.
```

It may simply be:

```text
ONE PERSON
FINDING ANOTHER
AGAIN.
```

The Relationship Engine exists to ensure that when this happens, the simulation remembers everything that made that moment matter.

> **People create stories. Relationships give those stories meaning.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-08 | Initial Relationship Engine architecture established. |
| 2.0 | 2026-08-29 | Expanded Relationship Engine into the operational model for persistent interpersonal relationships. Added multidimensional and directional relationship state, trust domains, expectations, relational events, accumulation, inertia, promises, betrayal, forgiveness, reconciliation, memory, resolution, off-screen evolution, relationship networks, cross-system ownership, Aurora separation, player/NPC parity, validation scenarios, canonical invariants and development locks. |