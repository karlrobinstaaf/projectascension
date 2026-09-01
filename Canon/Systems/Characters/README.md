# PROJECT ASCENSION

# Characters

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Characters README |
| Location | `Canon/Systems/Characters/README.md` |
| Version | 1.0 |
| Status | Active Canon |
| Category | Systems / Characters |
| Owner | Characters |
| Last Updated | 2026-08-31 |
| Primary Function | Provide the canonical entry point, ownership map and runtime overview for the Project Ascension Character architecture |

> **"A believable Character is not a collection of stats. They are a persistent human life shaped by history, relationships, knowledge, values, capability, choice and time."**

---

# 1. Purpose

The Characters section defines how individual human beings exist, think, want, choose, act and change within Project Ascension.

The architecture is designed around one central principle:

```text
CHARACTERS
ARE PEOPLE

NOT

GAME OBJECTS.
```

A Character should not exist only to:

```text
give missions

deliver dialogue

reward the player

block progress

provide exposition

or

fill a scene.
```

They should exist as:

```text
PERSISTENT
HUMAN ACTORS

WITH

HISTORY

RELATIONSHIPS

LIMITED KNOWLEDGE

VALUES

NEEDS

GOALS

CAPABILITY

AUTONOMY

AND

TIME.
```

---

# 2. Architectural Philosophy

No single Character document owns the whole person.

Instead, Project Ascension separates human state into narrowly defined authoritative systems.

The core rule is:

```text
ONE STATE DOMAIN

=

ONE AUTHORITATIVE OWNER.
```

Other systems may:

```text
READ

REFERENCE

DERIVE

SUMMARIZE

OR

REQUEST CHANGE.
```

They must not create competing authoritative copies.

---

# 3. Character Architecture Overview

The current Character architecture is:

```text
HUMANITY
↓
WHAT KIND OF HUMAN
IS THIS?

LIFE
↓
WHAT HAS HAPPENED
TO THEM?

CHARACTER STATE
↓
WHO ARE THEY,
WHERE ARE THEY,
AND WHAT IS
CURRENTLY TRUE?

VALUES / IDENTITY
↓
WHAT MATTERS
AND WHO DO THEY
BELIEVE THEY ARE?

NEEDS / MOTIVATION
↓
WHY DOES SOMETHING
MATTER NOW?

GOALS / PLANS
↓
WHAT FUTURE
DO THEY WANT?

KNOWLEDGE / BELIEFS
↓
WHAT DO THEY
THINK IS TRUE?

EXPERTISE
↓
WHAT HAVE THEY
LEARNED TO DO?

PROFESSION / CAPABILITY
↓
WHAT CAN THEY
REALISTICALLY ATTEMPT?

AUTONOMY
↓
WHY DOES ACTION
BECOME RELEVANT NOW?

DECISION MAKING
↓
WHAT DO THEY CHOOSE?

ACTION
↓
WHAT DO THEY TRY?

WORLD SIMULATION
↓
WHAT ACTUALLY HAPPENS?

MEMORY
+
LIFE
+
RELATIONSHIPS
+
CHARACTER DEVELOPMENT
↓
WHAT CHANGES?

CHARACTER SIMULATION RESOLUTION
↓
HOW MUCH OF THIS
MUST BE
SIMULATED EXPLICITLY
RIGHT NOW?
```

---

# 4. Directory Structure

```text
Canon/Systems/Characters/

├── Character_System/
│   ├── Character_Creation.md
│   └── Expertise_System.md
│
├── Autonomy_and_Initiative.md
├── CHARACTER_ARCHITECTURE_AUDIT.md
├── Character_Development.md
├── Character_Simulation_Resolution.md
├── Character_State.md
├── Decision_Making.md
├── Goals_and_Plans.md
├── Knowledge_and_Beliefs.md
├── Needs_and_Motivation.md
├── Profession_and_Capability.md
├── Values_and_Identity.md
└── README.md
```

---

# 5. Character Creation

Location:

```text
Character_System/
Character_Creation.md
```

Character Creation defines how a new Character receives plausible starting state.

Its responsibility is:

```text
CREATE
A BELIEVABLE
STARTING PERSON.
```

It may establish:

```text
identity

Life context

profession

Expertise

starting resources

Relationships

Values

Goals

personal history

strengths

weaknesses

secrets.
```

It must not redefine how those systems operate after creation.

---

# 6. Character Creation Principle

```text
CHARACTER CREATION
=
INITIAL STATE

NOT

ONGOING
CHARACTER LOGIC.
```

For example:

```text
Character Creation
may assign:

Engineering Expertise 3
```

but:

```text
Expertise_System.md
defines

what Expertise 3
actually means.
```

---

# 7. Expertise System

Location:

```text
Character_System/
Expertise_System.md
```

Expertise defines:

```text
WHAT A CHARACTER
HAS LEARNED
TO DO.
```

It owns:

```text
Expertise domains

Expertise levels

specialization

learned practical competence.
```

Expertise improves:

```text
information interpretation

available methods

risk awareness

technical understanding

possible actions.
```

But:

```text
EXPERTISE
DOES NOT
GUARANTEE SUCCESS.
```

---

# 8. Character State

Location:

```text
Character_State.md
```

Character State is the runtime coordination view of a persistent Character.

It answers:

```text
WHO IS THIS PERSON?

ARE THEY ALIVE?

WHERE ARE THEY?

WHAT ARE THEY
CURRENTLY DOING?

WHEN WAS
THIS STATE TRUE?

WHICH AUTHORITATIVE
SYSTEMS DEFINE
THE REST?
```

Character State owns:

```text
stable Character ID

current identity labels

existence status

current location

travel state

current activity

timestamps

runtime context

state references.
```

---

# 9. Character State Is Not the Whole Character

Character State must not become:

```text
A MONOLITHIC
CHARACTER DATABASE.
```

It references authoritative systems rather than duplicating them.

Conceptually:

```text
CHARACTER STATE
=
CURRENT
COORDINATION VIEW

OF

DISTRIBUTED
AUTHORITATIVE STATE.
```

---

# 10. Values and Identity

Location:

```text
Values_and_Identity.md
```

Values and Identity answers:

```text
WHAT MATTERS
TO THIS PERSON?

WHO DO THEY
BELIEVE THEY ARE?

WHAT WILL THEY
PROTECT?

WHAT WILL THEY
REFUSE?

WHAT CHOICE
WOULD CREATE
INTERNAL CONFLICT?
```

It owns:

```text
Values

value conflict

targeted Loyalty

moral boundaries

Identity statements

self-concept

Identity conflict

Preferences

Aversions.
```

---

# 11. Values and Identity Principle

```text
VALUES
=
WHAT MATTERS

IDENTITY
=
WHO I BELIEVE
I AM.
```

Neither directly determines behavior.

They create:

```text
PRESSURE

MEANING

BOUNDARIES

AND

INTERNAL COST.
```

---

# 12. Needs and Motivation

Location:

```text
Needs_and_Motivation.md
```

Needs and Motivation answers:

```text
WHY DOES
SOMETHING
MATTER NOW?
```

It owns:

```text
Need state

Need pressure

Need satisfaction

Need urgency

Motivational pressure

Motivational direction

competing motivations.
```

---

# 13. Need / Motivation Boundary

The architecture preserves:

```text
NEED
≠
MOTIVATION

MOTIVATION
≠
GOAL

GOAL
≠
ACTION.
```

A Need creates pressure.

Motivation gives that pressure direction.

Agency still determines what happens next.

---

# 14. Goals and Plans

Location:

```text
Goals_and_Plans.md
```

Goals and Plans defines intentional future state.

It answers:

```text
WHAT FUTURE
DOES THE CHARACTER
WANT?

AND

HOW DO THEY
CURRENTLY INTEND
TO PURSUE IT?
```

It owns:

```text
Goals

Goal state

Goal conflict

Goal hierarchy

Goal transformation

Plans

sub-goals

fallback plans

Plan adaptation.
```

---

# 15. Goal Principle

```text
GOAL
≠
MISSION.
```

A Character may have a Goal that:

```text
never involves
the player

never becomes
a Story Thread

never becomes
a quest.
```

The Character's life exists independently of narrative utility.

---

# 16. Knowledge and Beliefs

Location:

```text
Knowledge_and_Beliefs.md
```

Knowledge and Beliefs answers:

```text
WHAT HAS
THIS CHARACTER
PLAUSIBLY LEARNED?

WHAT DO THEY
CURRENTLY BELIEVE?

HOW CERTAIN
ARE THEY?

HOW DID
THEY LEARN IT?
```

It owns:

```text
Character Knowledge

source provenance

freshness

confidence

verification

uncertainty

Belief state

Belief revision

self-belief

causal Beliefs

future expectations.
```

---

# 17. Epistemic Principle

The architecture preserves:

```text
WORLD TRUTH
≠
CHARACTER PERCEPTION
≠
CHARACTER KNOWLEDGE
≠
CHARACTER BELIEF
≠
PLAYER KNOWLEDGE.
```

Characters act from:

```text
THE WORLD
AS THEY
BELIEVE IT TO BE.
```

---

# 18. Profession and Capability

Location:

```text
Profession_and_Capability.md
```

Profession and Capability answers:

```text
WHAT PROFESSIONAL
CONTEXT DOES
THIS CHARACTER HAVE?

AND

WHAT CAN THEY
REALISTICALLY
DO RIGHT NOW?
```

It owns:

```text
profession

occupation

professional role

professional access

authority

effective Capability

Capability requirements

Capability gaps

tool dependence

material dependence

facility dependence

environmental dependence

time dependence

assistance dependence.
```

---

# 19. Profession / Expertise / Capability Boundary

The architecture preserves:

```text
PROFESSION
=
PROFESSIONAL CONTEXT

EXPERTISE
=
WHAT I HAVE
LEARNED TO DO

CAPABILITY
=
WHAT I CAN
REALISTICALLY DO
HERE AND NOW.
```

And:

```text
CAPABILITY
≠
OUTCOME.
```

---

# 20. Actual vs Perceived Capability

Critical distinction:

```text
PERCEIVED CAPABILITY
=
WHAT THE CHARACTER
THINKS THEY CAN DO

ACTUAL CAPABILITY
=
WHAT THEY CAN
REALISTICALLY DO.
```

Decision Making uses:

```text
PERCEIVED CAPABILITY.
```

World resolution uses:

```text
ACTUAL CAPABILITY.
```

---

# 21. Autonomy and Initiative

Location:

```text
Autonomy_and_Initiative.md
```

Autonomy answers:

```text
WHY DOES
ACTION BECOME
RELEVANT NOW?

AND

WHEN DOES
THE CHARACTER
INITIATE ACTION
WITHOUT PLAYER
PROMPT?
```

It consumes:

```text
Goals

Needs

Plans

Open Loops

Responsibilities

Relationships

deadlines

new information

World Events

current Character State.
```

---

# 22. Autonomy Principle

Characters are not:

```text
PLAYER-TRIGGERED
ENTITIES.
```

They may:

```text
start conversations

follow up

change Plans

leave

travel

seek help

keep commitments

break commitments

respond to events

act without
player involvement.
```

---

# 23. Decision Making

Location:

```text
Decision_Making.md
```

Decision Making answers:

```text
WHAT DOES
THE CHARACTER
CHOOSE NOW?
```

It evaluates plausible options using current Character context.

Relevant inputs may include:

```text
Goals

Needs

Values

Identity

Beliefs

Relationships

Psychology

Perceived Capability

risk

time

current conditions.
```

---

# 24. Decision Principle

Decision Making must not become:

```text
ONE UNIVERSAL
WEIGHTED FORMULA.
```

Avoid:

```text
Goal 30%
Value 20%
Risk 25%
Relationship 25%.
```

Human decision-making should remain:

```text
CONTEXTUAL

CAUSAL

EXPLAINABLE

BUT

NOT
MECHANICALLY
DETERMINISTIC.
```

---

# 25. Character Development

Location:

```text
Character_Development.md
```

Character Development answers:

```text
HOW DOES
A CHARACTER
CHANGE OVER TIME?
```

It owns:

```text
developmental causality

development pressure

developmental inertia

persistent change plausibility

path dependence

regression

reversal

cross-system change coordination.
```

---

# 26. Character Development Principle

```text
CHARACTER DEVELOPMENT
≠
LEVELING UP

CHARACTER DEVELOPMENT
≠
AUTOMATIC IMPROVEMENT

CHARACTER DEVELOPMENT
≠
PREWRITTEN ARC.
```

Instead:

```text
CHARACTER DEVELOPMENT
=
CAUSALLY EXPLAINABLE
CHANGE THROUGH
LIVED HISTORY.
```

---

# 27. Development Does Not Own Resulting State

Example:

```text
Repeated technical work
↓
Development pressure
↓
Possible Expertise change
↓
Expertise System
owns the result.
```

Character Development coordinates:

```text
WHY CHANGE
IS PLAUSIBLE.
```

It does not become a second owner of every changing state.

---

# 28. Character Simulation Resolution

Location:

```text
Character_Simulation_Resolution.md
```

Character Simulation Resolution answers:

```text
HOW MUCH
OF THIS PERSON'S
LIFE

MUST BE
SIMULATED
EXPLICITLY
RIGHT NOW?
```

It defines:

```text
LOW

MEDIUM

HIGH
```

simulation resolution.

---

# 29. Resolution Principle

The central rule is:

```text
SIMULATION RESOLUTION
CHANGES

DETAIL

NOT

REALITY.
```

Therefore:

```text
LOW RESOLUTION
≠
FROZEN

LOW RESOLUTION
≠
NO AGENCY

LOW RESOLUTION
≠
NO CHANGE

LOW RESOLUTION
≠
LESS HUMAN.
```

---

# 30. Low Resolution

Low Resolution preserves major causal continuity.

Typical state may include:

```text
identity

location / region

Life situation

major Goals

major Relationships

major responsibilities

major Expertise

major constraints

major events

major Character change.
```

---

# 31. Medium Resolution

Medium Resolution adds enough current state for meaningful near-term simulation.

Typical state may include:

```text
active Goals

broad Plans

important Needs

Motivations

Beliefs

Knowledge

Psychology

Relationships

resources

Open Loops

recent events.
```

---

# 32. High Resolution

High Resolution exposes detailed current state required for immediate interaction and choice.

Typical state may include:

```text
current activity

immediate Goals

active Plans

current pressure

Values

Identity

Memory

Knowledge

Beliefs

Psychology

Relationship context

Capability

available options

Autonomy

Decision Making.
```

---

# 33. Resolution Is an Overlay

Character Simulation Resolution is not:

```text
ANOTHER STEP
IN THE RUNTIME.
```

It operates across the Character architecture.

Conceptually:

```text
LOW
MEDIUM
HIGH

=

HOW MUCH
OF THE SAME
CHARACTER SYSTEM
MUST BE
EXPLICITLY REPRESENTED.
```

---

# 34. Character Architecture Audit

Location:

```text
CHARACTER_ARCHITECTURE_AUDIT.md
```

The audit validates:

```text
ownership

system boundaries

runtime flow

off-screen continuity

simulation resolution

AI boundaries

Narrative boundaries

remaining architectural gaps.
```

It should be used when adding or modifying major Character architecture.

---

# 35. Humanity Dependencies

Character systems depend heavily on:

```text
Canon/Universe/Humanity/
```

Key documents include:

```text
The_Human_Condition.md

Human_Attributes.md

Human_Psychology.md

Historical_DNA.md

Memory.md

Family.md

Trust.md

Culture.md
```

---

# 36. Human Attributes Boundary

Human Attributes answers:

```text
HOW DOES
THIS PERSON
TEND TO RESPOND?
```

It does not answer:

```text
WHAT DO THEY
VALUE?

WHAT DO THEY
BELIEVE?

WHAT DO THEY
WANT?

HOW DO THEY
FEEL RIGHT NOW?
```

---

# 37. Human Psychology Boundary

Human Psychology answers:

```text
WHAT IS
THE CHARACTER'S
CURRENT OR EVOLVING
PSYCHOLOGICAL CONDITION?
```

It does not own:

```text
Values

Identity

Goals

Motivation

stable Attributes.
```

---

# 38. Memory Boundary

Memory answers:

```text
WHAT REMAINS
OF EXPERIENCE?
```

It owns:

```text
remembered experience

Memory significance

Memory accessibility

Memory reconstruction

fading

distortion.
```

Memory is not identical to:

```text
Knowledge

World Truth

Life Event

Character Development.
```

---

# 39. Life Dependency

Character systems depend on:

```text
Canon/Systems/Life/
```

Life answers:

```text
WHAT HAPPENS
ACROSS
THE CHARACTER'S LIFE?
```

It owns:

```text
Life Events

Life Course

Aging

biographical continuity

major personal transitions.
```

---

# 40. Life vs Character Development

The distinction is:

```text
LIFE
=
WHAT HAPPENED

CHARACTER DEVELOPMENT
=
HOW THAT HISTORY
MAY HAVE
PERSISTENTLY
CHANGED THE PERSON.
```

---

# 41. Relationships Dependency

Character systems depend on:

```text
Canon/Systems/Relationships/
```

Relationships owns:

```text
PERSISTENT
ACTOR-TO-ACTOR
RELATIONAL STATE.
```

Examples may include:

```text
Trust

affection

resentment

obligation

dependency

distance

relational history.
```

---

# 42. Trust Boundary

The architecture must preserve:

```text
SOCIAL TRUST
=
GENERAL HUMAN
DISPOSITION

RELATIONSHIP TRUST
=
STATE TOWARD
SPECIFIC ACTOR

TARGETED LOYALTY
=
VALUE-BASED
COMMITMENT TOWARD
SPECIFIC TARGET.
```

These are different concepts.

---

# 43. World Simulation Dependency

World Simulation owns:

```text
WHAT ACTUALLY
HAPPENS.
```

Characters provide:

```text
intent

action attempt

Capability

location

context.
```

World Simulation provides:

```text
physical consequence

external consequence

environmental response.
```

---

# 44. World Truth Boundary

Never collapse:

```text
CHARACTER BELIEF

INTO

WORLD TRUTH.
```

Likewise:

```text
CHARACTER INTENTION

DOES NOT

CREATE
WORLD OUTCOME.
```

---

# 45. Society Dependency

Society handles collective patterns that should not require individual Character simulation everywhere.

Examples may include:

```text
population behavior

social norms

migration

institutional patterns

collective belief distribution

economic adaptation.
```

Character systems remain responsible for:

```text
INDIVIDUAL HUMAN
STATE AND AGENCY.
```

---

# 46. Faction Boundary

Factions may own:

```text
organizational Goals

resources

leadership

territory

operations

institutional state.
```

Individual members remain:

```text
CHARACTERS.
```

Faction membership must not erase:

```text
individual Values

individual Beliefs

individual Goals

individual Relationships

individual agency.
```

---

# 47. Living Campaign Engine Boundary

The Living Campaign Engine may identify:

```text
important conditions

active conflicts

open consequences

Characters requiring attention

regional change

emerging Story Threads.
```

It may request:

```text
greater simulation resolution.
```

It may not determine:

```text
what a Character
must choose.
```

---

# 48. Narrative Boundary

Narrative systems may:

```text
present

frame

summarize

reveal

dramatize
```

Character state.

They may not:

```text
invent

override

rewrite

or

retroactively alter
```

Character reality for scene convenience.

---

# 49. Story Relevance Boundary

A Character may have:

```text
Need

Goal

Problem

Secret

Conflict

Relationship

Responsibility.
```

None automatically becomes:

```text
MISSION

QUEST

STORY HOOK.
```

Narrative relevance is downstream from Character reality.

---

# 50. Character Runtime

The Character runtime should be understood as a causal network rather than a rigid one-way pipeline.

A useful conceptual flow is:

```text
WORLD CONDITION
        ↓
CHARACTER EXPOSURE
        ↓
PERCEPTION
        ↓
KNOWLEDGE
        ↓
BELIEF
        ↓
VALUES / IDENTITY
+
NEEDS / MOTIVATION
        ↓
GOALS / PLANS
        ↓
AUTONOMY
        ↓
DECISION MAKING
        ↓
ACTION ATTEMPT
        ↓
ACTUAL CAPABILITY
+
WORLD CONDITIONS
        ↓
WORLD CONSEQUENCE
        ↓
LIFE
+
MEMORY
+
RELATIONSHIPS
+
PSYCHOLOGY
+
CHARACTER DEVELOPMENT
        ↓
UPDATED
AUTHORITATIVE STATE
        ↓
NEW CHARACTER CONTEXT.
```

---

# 51. Runtime Is Not Strictly Linear

Feedback occurs continuously.

Examples:

```text
NEW INFORMATION
→ Goal changes

MOTIVATION
→ information seeking

RELATIONSHIP CHANGE
→ Belief change

WORLD EVENT
→ new Need pressure

FAILURE
→ Plan change

MEMORY
→ future Decision pressure.
```

Therefore:

```text
CHARACTER ARCHITECTURE
=
CAUSAL NETWORK

NOT

LINEAR SCRIPT.
```

---

# 52. Character State Overlay

Character State operates across the runtime.

It provides:

```text
THE CURRENT
CHARACTER-CENTRIC
COORDINATION VIEW.
```

It is not:

```text
ONE STEP
BETWEEN SYSTEMS.
```

---

# 53. Simulation Resolution Overlay

Character Simulation Resolution also operates across the runtime.

It determines:

```text
HOW MUCH
OF EACH RELEVANT
SYSTEM

MUST BE
REPRESENTED
RIGHT NOW.
```

---

# 54. Off-Screen Continuity

The architecture requires:

```text
PLAYER ABSENCE
≠
CHARACTER PAUSE.
```

Characters may continue:

```text
working

traveling

aging

learning

changing roles

maintaining Relationships

forming Relationships

pursuing Goals

abandoning Goals

changing Plans

experiencing Life Events

responding to World Events

making decisions

developing.
```

---

# 55. Player Absence Principle

The world must never behave as:

```text
PLAYER LEFT

↓

NPCS WAIT.
```

Instead:

```text
PLAYER LEFT

↓

TIME CONTINUED

↓

OTHER PEOPLE
KEPT LIVING.
```

---

# 56. Human Agency

Character systems should support:

```text
SAME SITUATION

+

DIFFERENT PERSON

=

DIFFERENT
PLAUSIBLE RESPONSE.
```

Variation may emerge from:

```text
Attributes

Values

Identity

Beliefs

Relationships

Goals

Needs

Psychology

Expertise

Life history

current context.
```

---

# 57. Human Contradiction

Characters may:

```text
value honesty
and lie

value family
and fail family

believe themselves brave
and feel afraid

want safety
and take risk

trust someone
and still disagree

hold two conflicting Goals.
```

This is not automatically inconsistent design.

The question is:

```text
IS THE
CAUSAL PATH
UNDERSTANDABLE?
```

---

# 58. No Deterministic Character Logic

Avoid:

```text
ATTRIBUTE X
=
ACTION Y

NEED X
=
ACTION Y

VALUE X
=
ACTION Y

GOAL X
=
ACTION Y

PROFESSION X
=
CAPABILITY Y.
```

Characters should emerge from interaction between multiple systems.

---

# 59. No Omniscience

Characters must only reason from:

```text
INFORMATION
THEY PLAUSIBLY
POSSESS.
```

Never allow:

```text
WORLD DATABASE
KNOWLEDGE

TO BECOME

CHARACTER KNOWLEDGE
WITHOUT A PATH.
```

---

# 60. No Player-Centric Character Model

Characters should not exist primarily as:

```text
QUEST GIVERS

VENDORS

COMPANIONS

ENEMIES

REWARD SOURCES.
```

Those may describe:

```text
THE PLAYER'S
CURRENT RELATIONSHIP
TO THEM.
```

They must not define:

```text
WHO THE PERSON IS.
```

---

# 61. No Universal Character Level

Project Ascension must not introduce:

```text
CHARACTER LEVEL.
```

A person may simultaneously be:

```text
world-class researcher

poor driver

injured

socially isolated

trusted professionally

inexperienced at survival.
```

One number cannot represent this.

---

# 62. No Universal XP

The Character architecture must not use:

```text
GENERIC XP

MISSION XP

KILL XP

SESSION XP.
```

Development must remain:

```text
DOMAIN-SPECIFIC

CAUSAL

HISTORICAL.
```

---

# 63. No Global Trust

Trust must remain contextual.

Avoid:

```text
TRUST = 72.
```

Prefer:

```text
GENERAL SOCIAL TRUST
→ Human Attributes

TRUST IN PERSON A
→ Relationships

TRUST IN INSTITUTION
→ Belief / social context

LOYALTY TO PERSON A
→ Values and Identity.
```

---

# 64. No Global Reputation

A universal Reputation score should not be introduced.

Different people and institutions may hold:

```text
different information

different interpretations

different opinions

different histories
```

about the same Character.

---

# 65. AI Boundary

AI may assist with:

```text
reasoning

summarization

dialogue

causal interpretation

context selection

plausible inference

Character expression.
```

AI must not silently create Canon.

---

# 66. AI Must Not Invent Character State

AI must not invent:

```text
family

trauma

Expertise

Relationships

Goals

Values

Memories

resources

authority

knowledge

Life Events
```

merely because they would make a scene work.

---

# 67. Unknown Is Valid

The architecture should prefer:

```text
UNKNOWN

UNRESOLVED

INSUFFICIENT INFORMATION
```

over:

```text
CONVENIENT INVENTION.
```

---

# 68. Character Architecture Locks

The following principles are considered architectural locks:

```text
ONE AUTHORITATIVE OWNER
PER STATE DOMAIN

NO CHARACTER LEVEL

NO GENERIC XP

NO GLOBAL TRUST

NO GLOBAL LOYALTY

NO GLOBAL REPUTATION

NO PLAYER-CENTRIC NPC ACTIVATION

NO QUEST-GIVER CHARACTER MODEL

NO OFF-SCREEN FREEZE

NO OMNISCIENT CHARACTER KNOWLEDGE

NO ATTRIBUTE-TO-ACTION LOOKUP

NO NEED-TO-ACTION LOOKUP

NO GOAL-TO-ACTION LOOKUP

NO PROFESSION-MAGIC

NO AUTOMATIC CHARACTER ARC

NO NARRATIVE OVERRIDE

NO AI-INVENTED CANON

NO RESOLUTION-BASED PERSONHOOD.
```

---

# 69. Retired Architecture

The following former Character architecture is no longer canonical:

```text
Personality_and_Values.md
```

Its responsibilities are now split between:

```text
Human_Attributes.md

and

Values_and_Identity.md.
```

If the old file remains in the repository, it should be retired or removed after repository verification.

---

# 70. Progression Architecture

A separate generic Character Progression layer is not currently required.

Long-term individual Character change is owned by:

```text
Character_Development.md
```

while resulting state remains owned by domain systems such as:

```text
Expertise

Human Psychology

Relationships

Knowledge and Beliefs

Values and Identity

Goals and Plans

Life.
```

A legacy Progression system should not remain authoritative if it duplicates Character Development.

---

# 71. Known Cross-System Questions

The Character architecture is currently considered coherent.

Remaining questions belong primarily to wider Simulation architecture.

These include:

```text
Action Resolution

Resource Ownership

Reputation Aggregation

Institutional Roles

Responsibility Coordination.
```

These should not automatically become new Character subsystems.

---

# 72. Action Resolution Question

The remaining architectural chain includes:

```text
CHARACTER CHOOSES
↓
ACTION ATTEMPT
↓
ACTUAL CAPABILITY
+
TASK REQUIREMENTS
+
WORLD CONDITIONS
↓
OUTCOME.
```

The exact ownership of:

```text
ACTION RESOLUTION
```

should be confirmed against:

```text
Simulation_Architecture.md

and

World_Simulation/
```

before any new system is created.

---

# 73. Resource Ownership Question

Characters may:

```text
own

control

borrow

access

lose

or

be denied
```

resources.

Character State and Capability may reference those resources.

The authoritative resource architecture should be validated elsewhere.

Do not create:

```text
Character_Inventory.md
```

without confirming a real ownership gap.

---

# 74. Reputation Question

Reputation may exist as:

```text
individual belief

relationship history

community perception

professional reputation

institutional reputation

Faction reputation.
```

These may require different owners.

Do not collapse them into:

```text
ONE GLOBAL
REPUTATION SYSTEM.
```

---

# 75. Responsibility Question

Responsibilities may originate from:

```text
profession

relationship

promise

role

institution

law

family.
```

The origin should remain authoritative.

Character State may expose current responsibility context.

Autonomy may consume it.

---

# 76. Open Loops

An Open Loop represents something unresolved that may require future attention.

Examples:

```text
promise

pending response

unfinished task

planned follow-up

unresolved question.
```

Open Loops should remain contextual.

For now:

```text
Goals / Plans
own intentional loops

Relationships
own relational obligations

Character State
exposes relevant loops

Autonomy
consumes them.
```

---

# 77. Character Architecture Validation

Before adding a new Character system, ask:

```text
WHAT QUESTION
DOES THIS NEW
SYSTEM ANSWER?

IS THAT QUESTION
ALREADY OWNED?

WHAT STATE
WOULD IT OWN?

DOES THAT STATE
ALREADY HAVE
AN AUTHORITATIVE OWNER?

IS THIS REALLY
A CHARACTER SYSTEM

OR

DOES IT BELONG
TO LIFE,
SOCIETY,
RELATIONSHIPS,
WORLD SIMULATION,
NARRATIVE
OR ANOTHER AREA?

CAN THE SAME
PROBLEM BE SOLVED
THROUGH REFERENCES
INSTEAD OF
A NEW SYSTEM?
```

---

# 78. New System Rule

Create a new Character system only when:

```text
A REAL
AUTHORITATIVE
STATE DOMAIN
IS MISSING.
```

Do not create new systems merely because:

```text
A CONCEPT
IS INTERESTING

OR

A DOCUMENT
WOULD BE USEFUL.
```

---

# 79. Character Architecture North Star

The Character architecture succeeds when the simulation can answer:

```text
WHO IS THIS PERSON?

WHAT HAVE
THEY LIVED THROUGH?

WHAT MATTERS
TO THEM?

WHO DO THEY
BELIEVE THEY ARE?

WHAT DO THEY WANT?

WHAT DO THEY
THINK IS TRUE?

WHAT HAVE THEY
LEARNED TO DO?

WHAT CAN THEY
ACTUALLY DO HERE?

WHY DO THEY
CARE NOW?

WHY WOULD THEY
ACT NOW?

WHAT DO THEY
CHOOSE?

WHAT HAPPENS?

WHAT DO THEY
REMEMBER?

HOW DOES
THE EXPERIENCE
AFFECT THEM?

AND

WHAT HAPPENS
TO THEIR LIFE

WHEN THE PLAYER
IS SOMEWHERE ELSE?
```

---

# 80. Character Architecture Principle

A believable Character does not emerge from:

```text
ONE PERSONALITY SCORE

ONE MOTIVATION SCORE

ONE RELATIONSHIP SCORE

ONE CHARACTER LEVEL

OR

ONE AI PROMPT.
```

They emerge from the interaction of:

```text
History

Human Attributes

Psychology

Values

Identity

Needs

Motivation

Goals

Plans

Knowledge

Beliefs

Expertise

Capability

Relationships

Autonomy

Choice

Consequence

Memory

Development

Time.
```

---

# 81. Closing Principle

Project Ascension should create Characters who feel like people who existed before the player met them and who continue to exist after the player leaves.

They should have:

```text
PASTS
THE PLAYER
DID NOT CAUSE

RELATIONSHIPS
THE PLAYER
DOES NOT CONTROL

GOALS
THE PLAYER
MAY NEVER KNOW

BELIEFS
THAT MAY BE WRONG

VALUES
THAT MAY CONFLICT

CAPABILITIES
THAT HAVE LIMITS

RESPONSIBILITIES
THAT CONTINUE

AND

FUTURES
THAT DO NOT
WAIT FOR
THE PLAYER.
```

The final principle is:

> **The player enters the Character's life. The Character does not begin existing when the player arrives.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-31 | Rebuilt the Characters README as the canonical entry point for the current Character architecture. Documented system ownership, directory structure, runtime relationships, Humanity/Life/Relationships/World boundaries, Character State and Simulation Resolution overlays, off-screen continuity, AI and Narrative constraints, retired architecture, cross-system questions and architectural locks. |