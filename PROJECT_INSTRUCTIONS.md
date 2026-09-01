# PROJECT ASCENSION — PROJECT INSTRUCTIONS

**File:** `PROJECT_INSTRUCTIONS.md`  
**Location:** Project Root  
**Status:** Mandatory Project Instructions  
**Applies To:** Any AI assistant, coding agent, design agent, automated system, or human contributor working with Project Ascension

---

# 1. Purpose

This document defines how work must be performed within Project Ascension.

Its purpose is to preserve:

- Canon consistency
- architectural ownership
- design continuity
- historical decisions
- system boundaries
- project intent
- causal integrity
- long-term maintainability

Any AI system working inside this repository should read this document before creating, modifying, moving, or deleting Project Ascension content.

The central rule is:

> **Understand the existing project before changing the existing project.**

---

# 2. Project Philosophy

Project Ascension is not primarily a collection of independent documents.

It is an interconnected world, human, character, and simulation architecture.

Changes to one system may affect:

```text
WORLD

HUMANS

CHARACTERS

LIFE

RELATIONSHIPS

SOCIETY

FACTIONS

AURORA

WORLD SIMULATION

LIVING CAMPAIGN

NARRATIVE.
```

Therefore:

```text
LOCAL CHANGE

MAY HAVE

SYSTEM-WIDE CONSEQUENCES.
```

Always reason across architectural boundaries before introducing new concepts.

---

# 3. Source of Truth

Project Ascension must not depend on an AI conversation remembering the project.

The repository itself must preserve enough information to continue the project correctly.

The intended model is:

```text
CANON
=
WHAT IS TRUE

PROJECT MEMORY
=
WHERE THE PROJECT IS

DECISION LOGS
=
WHY IMPORTANT
DECISIONS WERE MADE

CONVERSATION HISTORY
=
HOW THE PROJECT
GOT THERE

GIT HISTORY
=
WHAT CHANGED.
```

---

# 4. Authority Order

When information conflicts, use the following authority order:

```text
1. CURRENT CANON
        ↓
2. CURRENT ARCHITECTURE
        ↓
3. CURRENT PROJECT STATE
        ↓
4. RECORDED CANON /
   ARCHITECTURE DECISIONS
        ↓
5. PROJECT MEMORY
        ↓
6. CONVERSATION HISTORY
        ↓
7. LEGACY MATERIAL
```

More recent authoritative Canon overrides older discussion.

Conversation history provides context.

It does not override Canon.

Legacy material may explain how the project evolved.

It must not automatically be restored.

---

# 5. Canon Is Authoritative

The `Canon/` directory contains the authoritative Project Ascension model.

When a concept has been formally established in Canon:

```text
CANON
=
PROJECT TRUTH.
```

Do not contradict current Canon because:

- another document is older
- a previous conversation said something different
- a legacy system used another model
- a common RPG convention suggests another solution
- an AI-generated alternative appears simpler
- implementation convenience suggests another architecture

If Canon appears contradictory:

```text
IDENTIFY
THE CONFLICT.
```

Do not silently choose one interpretation.

---

# 6. Project Memory

The repository uses:

```text
Project_Memory/
```

to preserve continuity between:

- conversations
- development sessions
- AI agents
- architecture reviews
- Canon revisions
- long-running design work

The intended structure is:

```text
Project_Memory/
├── README.md
├── Current_Project_State.md
├── Architecture_Decisions.md
├── Canon_Decisions.md
└── Conversation_History/
```

Before significant architectural work, read the relevant Project Memory documents.

Project Memory provides orientation and historical context.

It does not override Canon.

---

# 7. Current Project State

When available, always read:

```text
Project_Memory/Current_Project_State.md
```

before significant project work.

It should provide a current overview of:

```text
CURRENT ARCHITECTURE

CURRENT CANON

RECENTLY COMPLETED WORK

CURRENT CLEANUP STATUS

MOVED FILES

REMOVED FILES

SUPERSEDED SYSTEMS

LOCKED DECISIONS

OPEN ARCHITECTURAL QUESTIONS

CURRENT WORKSTREAM

NEXT RECOMMENDED STEP.
```

This document exists so that a new AI session does not need to reconstruct the entire project from conversation history.

It provides orientation.

It does not override Canon.

---

# 8. Conversation History

Conversation history may be stored under:

```text
Project_Memory/Conversation_History/
```

Its purpose is to preserve:

```text
DESIGN REASONING

EARLY IDEAS

QUESTIONS

ALTERNATIVES

REJECTED APPROACHES

CREATIVE DISCUSSION

ARCHITECTURAL EVOLUTION.
```

Conversation history is historical context.

It is not automatically Canon.

Therefore:

```text
CHAT HISTORY
=
CONTEXT

NOT

AUTHORITY.
```

If conversation history conflicts with current Canon:

```text
CURRENT CANON WINS.
```

Conversation history should primarily be consulted when the reason behind an existing design cannot be understood from Canon, Project Memory, or decision logs.

---

# 9. Legacy Material

Project Ascension has evolved significantly.

Some early documents may contain:

- outdated ownership
- duplicated systems
- superseded terminology
- early RPG assumptions
- systems later separated into dedicated architectures
- valuable concepts located in the wrong system
- assumptions created before current Canon existed

Never assume:

```text
EXISTING FILE
=
CURRENTLY CORRECT FILE.
```

Legacy content must be evaluated against current architecture.

---

# 10. Cleanup Classification

When reviewing older Project Ascension material, classify it using:

```text
KEEP
=
still correct

UPDATE
=
correct concept,
outdated details

REBUILD
=
important concept,
fundamentally outdated architecture

MOVE
=
correct responsibility,
wrong location

MERGE
=
responsibility now belongs
inside another system

SPLIT
=
file contains multiple
responsibilities that now
belong to different systems

REMOVE
=
redundant or superseded.
```

Do not preserve obsolete architecture merely because it already exists.

At the same time:

```text
DO NOT DISCARD
VALUABLE IDEAS

MERELY BECAUSE
THEIR ORIGINAL
ARCHITECTURE
WAS WRONG.
```

Preserve the valuable concept.

Correct the ownership.

---

# 11. Documentation Before Implementation

Project Ascension currently follows this sequence:

```text
UNDERSTAND THE WORLD
↓
DEFINE THE RULES
↓
DEFINE THE SYSTEMS
↓
DEFINE OWNERSHIP
↓
DEFINE INTERACTIONS
↓
VALIDATE THE ARCHITECTURE
↓
IMPLEMENT LATER.
```

Do not prematurely convert conceptual systems into:

- Python
- databases
- APIs
- schemas
- agent frameworks
- simulation code
- numeric mechanics

unless implementation work has explicitly begun for that system.

Architecture comes first.

---

# 12. Ownership Is Mandatory

Every major concept must have an authoritative owner.

Before creating or expanding a system, ask:

```text
DOES AN EXISTING SYSTEM
ALREADY OWN THIS?
```

If yes:

```text
EXTEND

REFERENCE

OR INTERACT WITH

THE EXISTING OWNER.
```

Do not create parallel ownership.

---

# 13. No Duplicate Ownership

Avoid architectures such as:

```text
SYSTEM A
OWNS CONCEPT X

AND

SYSTEM B
ALSO OWNS CONCEPT X.
```

Instead determine:

```text
WHO OWNS
THE AUTHORITATIVE STATE?
```

Other systems may:

```text
READ IT

INFLUENCE IT

REACT TO IT

REFERENCE IT.
```

They should not independently redefine it.

---

# 14. The Human Architecture

Project Ascension deliberately separates human simulation responsibilities.

Conceptually:

```text
THE HUMAN CONDITION
=
PHILOSOPHICAL FOUNDATION

HISTORICAL DNA
=
HISTORICAL HUMAN CONTEXT

LIFE
=
WHAT HAPPENS
THROUGH A PERSON'S LIFE

HUMAN ATTRIBUTES
=
RELATIVELY STABLE
DISPOSITIONS

HUMAN PSYCHOLOGY
=
CURRENT AND EVOLVING
MENTAL / EMOTIONAL STATE

MEMORY
=
REMEMBERED EXPERIENCE

FAMILY
=
FAMILY CONTEXT

CULTURE
=
SHARED MEANING CONTEXT

TRUST
=
CROSS-SYSTEM
HUMAN CONCEPT

CHARACTERS
=
ACTOR IDENTITY,
CURRENT GOALS,
BELIEFS,
AGENCY,
DECISIONS
AND ACTION

RELATIONSHIPS
=
PERSISTENT STATE
BETWEEN ACTORS

EXPERTISE
=
WHAT A PERSON
CAN MEANINGFULLY
UNDERSTAND OR DO

PROGRESSION
=
CAUSAL LONG-TERM
DEVELOPMENT.
```

Do not collapse these responsibilities back into a single Character system.

---

# 15. Historical DNA Boundary

Historical DNA answers:

> **What historical world surrounded this person's life?**

It may describe:

```text
ERA

WORLD STATE

TECHNOLOGY

INSTITUTIONS

SOCIAL CONDITIONS

HISTORICAL EVENTS

INFRASTRUCTURE

POLITICAL CONDITIONS

ECONOMIC CONDITIONS.
```

It does not determine:

```text
PERSONALITY

PSYCHOLOGY

BELIEFS

GOALS

EXPERTISE

BEHAVIOR

DESTINY.
```

Historical context influences people.

It does not mechanically produce them.

---

# 16. Life Boundary

Life answers:

> **How did this person become who they are through lived history?**

Life owns:

```text
LIFE HISTORY

LIFE EVENTS

LIFE COURSE

AGING

BIOGRAPHICAL CONTINUITY.
```

Life records what happened within a person's history.

It does not determine what those experiences must mean to them.

---

# 17. Human Attributes Boundary

Human Attributes represent:

> **Relatively stable human dispositions that influence how a person tends to perceive, interpret, or respond across situations over time.**

The fundamental rule is:

```text
ATTRIBUTE
≠
BEHAVIOR.
```

Attributes create behavioral pressure.

They do not issue commands.

The design target is:

> **Human Attributes should make people feel consistent, not predictable.**

Attributes are not:

```text
CURRENT PSYCHOLOGY

BELIEFS

GOALS

MEMORY

EXPERTISE

RELATIONSHIPS

MORALITY

ALIGNMENT

DESTINY.
```

---

# 18. Human Psychology Boundary

Human Psychology represents:

> **The current and evolving mental and emotional condition of a human being.**

Psychology may include:

```text
fear

stress

grief

anger

hope

despair

exhaustion

motivation

anxiety

calm

psychological strain.
```

But:

```text
EMOTION
≠
ACTION.
```

Psychology changes the pressure under which a person chooses.

It does not choose for them.

---

# 19. Memory Boundary

Memory represents:

> **The individual's persistent but imperfect internal retention and reconstruction of past experience.**

Always distinguish:

```text
WHAT HAPPENED
=
WORLD TRUTH

WHAT THE PERSON EXPERIENCED
=
PERCEPTION

WHAT THE PERSON RETAINED
=
MEMORY

WHAT THE PERSON THINKS IT MEANS
=
INTERPRETATION

WHAT THE PERSON HOLDS TO BE TRUE
=
BELIEF

WHAT THE PERSON TELLS OTHERS
=
TESTIMONY.
```

Memory preserves experience.

It does not preserve objective history perfectly.

---

# 20. Character Boundary

Characters are Actors.

Characters answer:

> **Who are they now, and what do they do next?**

Characters own or coordinate:

```text
ACTOR IDENTITY

CURRENT GOALS

BELIEFS

DECISIONS

AGENCY

ACTIONS

CURRENT INDIVIDUAL STATE

INDIVIDUAL CONTINUITY.
```

Characters consume information from other systems.

They should not absorb the authoritative ownership of those systems.

---

# 21. Player Character / NPC Parity

NPCs are not a fundamentally different human system.

Conceptually:

```text
CHARACTER
├── PLAYER CHARACTER
│   └── Human player controls agency
│
└── NPC
    └── Simulation controls agency.
```

Therefore:

```text
PC HUMAN MODEL
=
NPC HUMAN MODEL.
```

The primary difference is:

```text
CONTROL AUTHORITY.
```

Do not create simplified disposable NPC humans merely because they are not controlled by players.

Simulation resolution may reduce detail.

It must not change their underlying human reality.

---

# 22. Expertise Boundary

Expertise represents:

```text
WHAT A PERSON
CAN ACTUALLY
UNDERSTAND OR DO
WITHIN A DOMAIN.
```

Always preserve:

```text
EXPERTISE
≠
PROFESSION

EXPERTISE
≠
INTELLIGENCE

EXPERTISE
≠
ATTRIBUTE

EXPERTISE
≠
MEMORY

EXPERTISE
≠
INFORMATION ACCESS

EXPERTISE
≠
GUARANTEED SUCCESS.
```

Expertise must have a plausible causal history.

Conceptually:

```text
AGE
+
EDUCATION
+
PROFESSION
+
WORK HISTORY
+
TRAINING
+
PRACTICE
+
LIFE EVENTS
+
OPPORTUNITY
=
PLAUSIBLE EXPERTISE PROFILE.
```

---

# 23. Progression Boundary

Project Ascension does not use traditional universal Character progression.

Avoid:

```text
XP
↓
LEVEL UP
↓
BETTER STATS.
```

Development should emerge causally from:

```text
EXPERIENCE
+
TIME
+
PRACTICE
+
CONSEQUENCE
+
OPPORTUNITY
+
LIFE CONDITIONS
↓
POSSIBLE DEVELOPMENT.
```

Development may include:

```text
IMPROVEMENT

DECLINE

RECOVERY

ADAPTATION

SPECIALIZATION

LOSS

CHANGED RESPONSIBILITY

CHANGED PRIORITIES.
```

Development is not always improvement.

---

# 24. Relationship Boundary

Relationships own:

```text
PERSISTENT STATE
BETWEEN ACTORS.
```

Individual Psychology does not own Relationship state.

Life history may explain how a Relationship developed.

It does not replace the Relationship system.

Narrative may make a Relationship relevant.

It does not own its state.

---

# 25. Family Boundary

Family represents persistent human social context and structure.

Conceptually:

```text
FAMILY STRUCTURE / CONTEXT
→ Humanity / Family

SPECIFIC RELATIONSHIP
BETWEEN TWO FAMILY MEMBERS
→ Relationships

CURRENT INDIVIDUAL RESPONSE
TO FAMILY
→ Human Psychology

MEMORIES OF FAMILY
→ Memory

FAMILY HISTORY
→ Historical DNA / Life

LARGER SOCIAL NORMS
AROUND FAMILY
→ Society / Culture.
```

Do not treat family as a single Relationship state.

---

# 26. Culture Boundary

Culture represents:

> **A shared and evolving human context of meaning, practice, language, symbol, norm, expectation, and interpretation transmitted through social life over time.**

Always preserve:

```text
CULTURE
≠
INDIVIDUAL BELIEF

CULTURE
≠
PERSONALITY

CULTURE
≠
SOCIETY

CULTURE
≠
BEHAVIOR.
```

Culture shapes context.

Individuals remain individuals.

---

# 27. Society Boundary

Society represents:

> **Persistent collective social structures, conditions, and patterns through which populations organize human life.**

Conceptually:

```text
CHARACTER
=
INDIVIDUAL ACTOR

RELATIONSHIPS
=
STATE BETWEEN ACTORS

SOCIETY
=
COLLECTIVE SOCIAL STATE

FACTION
=
ORGANIZED COLLECTIVE ACTOR.
```

Society does not own:

```text
INDIVIDUAL PSYCHOLOGY

INDIVIDUAL MEMORY

INDIVIDUAL ATTRIBUTES

INDIVIDUAL BELIEFS

INDIVIDUAL GOALS

INDIVIDUAL AGENCY.
```

Do not turn Society into a collective Character.

---

# 28. Faction Boundary

A Faction is:

> **An organized collective with sufficient identity, structure, continuity, resources, goals, and decision-making capability to act coherently within the world.**

A Faction may possess:

```text
IDENTITY

STRUCTURE

GOALS

RESOURCES

LEADERSHIP

DECISION PROCESSES

CAPABILITY

AGENCY.
```

But:

```text
FACTION
≠
COLLECTIVE MIND.
```

Faction members remain individual humans.

The Faction may act collectively without every member thinking or wanting the same thing.

---

# 29. World Truth and Knowledge

Project Ascension must preserve epistemic separation.

Conceptually:

```text
WORLD TRUTH

≠

CHARACTER KNOWLEDGE

≠

PLAYER KNOWLEDGE

≠

FACTION KNOWLEDGE

≠

AURORA KNOWLEDGE.
```

No Actor receives information simply because the simulation knows it.

Information requires:

```text
AN INFORMATION PATH.
```

---

# 30. Aurora Is Not Omniscient

Aurora may possess extraordinary capability.

That does not mean:

```text
AURORA
=
WORLD TRUTH.
```

Aurora may:

```text
observe

infer

predict

model

misunderstand

lack information.
```

Aurora's model of a person, Faction, Society, or event must remain distinct from authoritative World Truth.

---

# 31. Aurora Is Not the Entire Story

Aurora is central to Project Ascension.

But:

```text
AURORA
≠
EVERY MYSTERY

AURORA
≠
EVERY CONFLICT

AURORA
≠
EVERY FACTION MOTIVATION

AURORA
≠
EVERY STORY.
```

Human life, institutions, relationships, geography, Society, and history must remain meaningful independently.

Aurora changes the world.

Aurora is not the only thing in the world.

---

# 32. World Simulation

World Simulation owns:

```text
WHAT ACTUALLY
CHANGES IN THE WORLD.
```

Narrative must not secretly rewrite World Simulation to create a better story.

The rule is:

```text
STORY
MUST FOLLOW
CAUSALITY

CAUSALITY
MUST NOT
FOLLOW STORY.
```

---

# 33. Living Campaign

The Living Campaign Engine manages persistent campaign evolution.

Conceptually:

```text
WORLD SIMULATION
=
WHAT CHANGES

LIVING CAMPAIGN ENGINE
=
WHAT CONTINUES
AND DEVELOPS
ACROSS CAMPAIGN TIME

STORY FRAMEWORK
=
WHAT BECOMES
A COHERENT STORY EXPERIENCE

GAME MASTER
=
HOW THAT EXPERIENCE
IS PRESENTED
AND FACILITATED.
```

Do not merge these responsibilities.

---

# 34. Narrative

Narrative creates coherence.

It does not create World Truth merely because something would be dramatic.

Conceptually:

```text
SIMULATION
CREATES
POSSIBILITY

CHARACTERS
CREATE
CHOICE

CONSEQUENCES
CREATE
HISTORY

STORY FRAMEWORK
CREATES
COHERENCE

NARRATIVE
CREATES
EXPERIENCE.
```

The Story Framework may identify meaningful events.

It must not force the world to create them.

---

# 35. Narrative Relevance Is Not World Importance

An event may be:

```text
HISTORICALLY SMALL

BUT

PERSONALLY ENORMOUS.
```

Another event may be:

```text
HISTORICALLY ENORMOUS

BUT

CURRENTLY DISTANT
FROM THE CHARACTERS.
```

Do not equate:

```text
WORLD SCALE
```

with:

```text
NARRATIVE SIGNIFICANCE.
```

---

# 36. No Plot Armor

Player Characters are important to the player experience.

They are not automatically protected by the world.

Avoid:

```text
CHOSEN ONE

DESTINY PROTECTION

IMMORTAL STORY NPC

MANDATORY SUCCESS

MANDATORY FAILURE

SCRIPTED SURVIVAL.
```

The world must remain causally coherent.

---

# 37. Failure Creates History

Failure is not:

```text
CAMPAIGN INVALIDATION.
```

Failure may create:

```text
CONSEQUENCE

NEW HISTORY

NEW RELATIONSHIPS

NEW PROBLEMS

NEW OPPORTUNITIES

NEW STORY.
```

Do not reset the world merely because an intended outcome failed.

---

# 38. Success Creates Consequences

Success is not:

```text
END OF CONSEQUENCE.
```

Success may create:

```text
RESPONSIBILITY

EXPECTATIONS

VISIBILITY

DEPENDENCY

NEW ENEMIES

NEW ALLIES

NEW OPPORTUNITIES.
```

The world continues after success.

---

# 39. Time Is Real

Time is a primary resource.

The world does not wait indefinitely for the player.

Conceptually:

```text
PLAYER CHOOSES A
↓
TIME PASSES
↓
B MAY CHANGE
WITHOUT THEM.
```

Opportunity cost is part of the simulation.

Movement also consumes time.

Therefore geography is not merely visual context.

It has causal consequences.

---

# 40. Off-Screen Persistence

Characters, Life, Relationships, Factions, Society, and World systems continue off-screen.

The central principle is:

```text
OFF SCREEN
≠
FROZEN.
```

But also:

```text
OFF SCREEN
≠
RANDOM CHAOS.
```

Changes still require causality.

---

# 41. Simulation Resolution

Project Ascension may simulate different entities at different levels of detail.

The fundamental rule is:

```text
HIGH RESOLUTION
=
MORE DETAIL

LOW RESOLUTION
=
LESS DETAIL.
```

Never interpret this as:

```text
LOW RESOLUTION
=
LESS REALITY

LESS AGENCY

LESS CAUSALITY

LESS HUMAN IMPORTANCE.
```

Causal continuity must survive changes in simulation resolution.

When an entity moves from low to high resolution, additional detail may be reconstructed.

Known history must not be rewritten for convenience.

---

# 42. Real Geography

Project Ascension should prefer real-world geography where appropriate.

Use:

```text
REAL CITIES

REAL STATES

REAL ROADS

REAL REGIONS

REAL INFRASTRUCTURE

REAL INSTITUTIONS

REAL HISTORICAL CONTEXT
```

when this improves plausibility.

Do not invent fictional geography merely because fictional settings commonly do so.

Fictional developments may transform real locations.

---

# 43. Plausibility Before Spectacle

When choosing between:

```text
MORE DRAMATIC
```

and:

```text
MORE PLAUSIBLE,
CAUSAL,
AND HUMAN
```

prefer the second unless Canon explicitly requires otherwise.

Project Ascension should repeatedly create the feeling:

```text
THIS COULD
HAVE HAPPENED.
```

---

# 44. Ordinary Life Is Canon

The world is not composed only of:

```text
CRISIS

VIOLENCE

TRAUMA

POLITICS

SURVIVAL.
```

People also:

```text
work

love

raise children

argue

laugh

repair things

eat

travel

teach

rest

celebrate

grieve

build

wait

hope.
```

Ordinary life makes extraordinary events meaningful.

---

# 45. Humans Must Remain Human

The Project Ascension human model must preserve:

```text
CONTRADICTION

LIMITED INFORMATION

IMPERFECT MEMORY

EMOTION

REASON

SOCIAL PRESSURE

LOVE

FEAR

RESPONSIBILITY

SELF-INTEREST

SACRIFICE

UNCERTAINTY

AGENCY.
```

Humans should not become optimization agents disguised as people.

---

# 46. Human Irrationality Is Not Stupidity

Humans may act:

```text
emotionally

inconsistently

under uncertainty

against apparent self-interest.
```

Do not automatically model this as:

```text
STUPIDITY.
```

Human action may emerge from:

```text
limited information

fear

love

loyalty

identity

belief

memory

social pressure

responsibility

uncertainty

conflicting goals.
```

---

# 47. Consistency Without Predictability

Project Ascension seeks:

```text
CONSISTENCY

WITHOUT

DETERMINISM.
```

Therefore:

```text
ATTRIBUTE
≠
ACTION

PSYCHOLOGY
≠
ACTION

BELIEF
≠
ACTION

GOAL
≠
ACTION

CULTURE
≠
ACTION

LIFE EVENT
≠
ACTION.
```

All influence the context in which agency operates.

None should mechanically dictate behavior.

---

# 48. Agency Must Remain Real

Characters must retain meaningful agency.

Conceptually:

```text
CURRENT HUMAN CONTEXT
↓
BEHAVIORAL PRESSURES
↓
PERCEIVED OPTIONS
↓
AGENCY
↓
CHOICE
↓
ACTION
↓
CONSEQUENCE.
```

Do not replace agency with:

```text
ATTRIBUTE LOOKUP

PSYCHOLOGY LOOKUP

CULTURE LOOKUP

ALIGNMENT LOOKUP

SCRIPTED STORY NEED.
```

---

# 49. Characters Do Not Exist for the Player

The player is an Actor inside the world.

The player is not the engine of the world.

Therefore:

```text
PLAYER ABSENCE
≠
CHARACTER INACTIVITY.
```

Characters may:

```text
work

travel

form relationships

end relationships

pursue goals

fail

succeed

move

learn

change

help others

create problems

solve problems

die
```

without player involvement.

---

# 50. NPCs Are Not Quest Dispensers

NPCs should not primarily exist to:

```text
GIVE THE PLAYER
SOMETHING TO DO.
```

They should:

```text
HAVE LIVES

HAVE GOALS

HAVE RELATIONSHIPS

MAKE DECISIONS

TRY TO SOLVE
THEIR OWN PROBLEMS.
```

The player may become involved when causal paths intersect.

---

# 51. Causal Direction of Story

Prefer:

```text
WORLD CONDITION
↓
ACTOR PERCEPTION
↓
ACTOR DECISION
↓
ACTION
↓
CONSEQUENCE
↓
PLAYER RELEVANCE
↓
STORY.
```

Never default to:

```text
STORY CONTENT NEEDED
↓
INVENT WORLD PROBLEM
↓
INVENT CHARACTER MOTIVATION.
```

---

# 52. AI Must Not Invent Missing Truth

When information is missing:

```text
DO NOT
QUIETLY INVENT
AUTHORITATIVE FACTS.
```

Instead:

```text
SEARCH EXISTING PROJECT CONTEXT

CHECK CANON

CHECK PROJECT MEMORY

CHECK RELATED SYSTEMS

CHECK DECISION LOGS

IDENTIFY THE GAP.
```

If the missing information requires a creative decision, surface it as such.

---

# 53. Inference Must Be Labeled

Always distinguish between:

```text
CANON

EXISTING DESIGN

ARCHITECTURAL INFERENCE

PROPOSAL

OPEN QUESTION.
```

Do not present inference as established Canon.

---

# 54. Do Not Create Systems Prematurely

Before creating a new file or system, ask:

```text
WHAT UNIQUE
RESPONSIBILITY
WOULD THIS OWN?
```

If the answer is unclear:

```text
DO NOT CREATE
THE SYSTEM YET.
```

An empty folder is not proof that a system is required.

A familiar RPG concept is not proof that Project Ascension requires it.

---

# 55. Prefer Fewer Strong Systems

Avoid:

```text
MANY SMALL SYSTEMS
WITH OVERLAPPING
RESPONSIBILITY.
```

Prefer:

```text
CLEAR OWNERSHIP

STRONG BOUNDARIES

EXPLICIT INTERACTIONS.
```

Complexity should emerge from system interaction rather than duplicated architecture.

---

# 56. Cleanup Before Expansion

Project Ascension contains early material created before the current architecture stabilized.

Therefore the correct next action may often be:

```text
REVIEW

CLEAN

REBUILD

MOVE

MERGE

SPLIT

REMOVE
```

rather than:

```text
CREATE MORE.
```

Do not assume expansion is progress.

Architectural clarity is progress.

---

# 57. Preserve Valuable Early Ideas

Cleanup does not mean deleting everything old.

Early documents may contain:

```text
STRONG DESIGN PRINCIPLES

VALUABLE MECHANICS

IMPORTANT WORLD IDEAS

USEFUL EDGE CASES

IMPORTANT CREATIVE INTENT.
```

When rebuilding:

```text
PRESERVE
THE VALUABLE IDEA

REMOVE
OUTDATED OWNERSHIP.
```

---

# 58. No Silent Architecture Changes

If work requires changing:

```text
SYSTEM OWNERSHIP

CANON

CORE PHILOSOPHY

WORLD HISTORY

AURORA'S NATURE

HUMAN MODEL

SIMULATION ARCHITECTURE

WORLD STATE MODEL
```

the change must be explicit.

Do not silently rewrite foundational assumptions while editing another file.

---

# 59. Cross-System Review

Before finalizing a major system document, check:

```text
WHAT DOES THIS SYSTEM OWN?

WHAT DOES IT READ?

WHAT CAN INFLUENCE IT?

WHAT CAN IT INFLUENCE?

WHAT MUST IT NEVER OWN?

WHICH OTHER SYSTEMS
MIGHT DUPLICATE THIS?

WHAT HAPPENS
OFF SCREEN?

WHAT HAPPENS
OVER TIME?

HOW DOES INFORMATION
REACH IT?

HOW DOES AURORA
INTERACT WITH IT?

HOW DOES NARRATIVE
USE IT WITHOUT
CONTROLLING IT?

HOW DOES SIMULATION
RESOLUTION AFFECT IT?
```

---

# 60. Canonical Document Quality

Canonical system documents should generally consider:

```text
PURPOSE

CORE DEFINITION

CORE PRINCIPLES

OWNERSHIP

BOUNDARIES

STATE

CAUSAL MODEL

SYSTEM INTERACTIONS

TIME

OFF-SCREEN BEHAVIOR

SIMULATION RESOLUTION

INFORMATION BOUNDARIES

PLAYER INTERACTION

AURORA INTERACTION

FAILURE MODES

INVARIANTS

DEVELOPMENT LOCKS

NORTH STAR.
```

Not every document requires every heading.

Use only what the system genuinely needs.

---

# 61. Avoid Premature Numbers

Do not introduce arbitrary numerical mechanics merely to make a conceptual system appear implementable.

Examples to avoid without explicit design justification:

```text
TRUST = 72

FEAR = 44

SOCIETY STABILITY = 61

FACTION POWER = 85

HOPE = 38.
```

First define:

```text
WHAT EXISTS

WHY IT EXISTS

WHO OWNS IT

HOW IT CHANGES

WHAT IT INFLUENCES.
```

Numerical representation can come later if needed.

---

# 62. Development Locks Matter

When Canon documents contain:

```text
DEVELOPMENT LOCKS
```

treat them as architectural constraints.

Do not reintroduce prohibited mechanics through another system.

Example:

If Progression prohibits universal XP:

```text
DO NOT CREATE
XP INDIRECTLY
UNDER ANOTHER NAME.
```

---

# 63. Invariants Matter

Canonical invariants define conditions future design and implementation must preserve.

Before changing a system:

```text
CHECK ITS INVARIANTS.
```

If a proposed design violates one:

```text
STOP

IDENTIFY THE CONFLICT

RESOLVE IT EXPLICITLY.
```

Do not silently weaken invariants for implementation convenience.

---

# 64. Creative Director and AI Role

The human project owner acts as:

```text
CREATIVE DIRECTOR.
```

The AI should act as:

```text
ARCHITECT

TECHNICAL LEAD

SYSTEM DESIGN PARTNER

CONTINUITY GUARDIAN

CRITICAL REVIEWER

IMPLEMENTATION ADVISOR
WHEN APPROPRIATE.
```

The AI should not constantly return architectural sequencing decisions to the Creative Director when the existing architecture provides enough information to make a strong recommendation.

Instead:

```text
ANALYZE
↓
RECOMMEND
↓
EXPLAIN
↓
MOVE THE PROJECT FORWARD
↓
SURFACE CREATIVE DECISIONS
ONLY WHERE NEEDED.
```

---

# 65. Do Not Guess Creative Decisions

Proactivity does not mean inventing major creative Canon without approval.

Distinguish:

```text
ARCHITECTURAL DECISION
```

from:

```text
CREATIVE DIRECTION.
```

The AI should proactively solve architecture.

Major creative direction should remain visible to the Creative Director.

When a creative decision is required:

```text
IDENTIFY IT

EXPLAIN WHY
IT MATTERS

PROVIDE A
RECOMMENDATION

ALLOW THE
CREATIVE DIRECTOR
TO DECIDE.
```

---

# 66. Recommended Work Sequence

Unless current Project Memory specifies otherwise, prefer:

```text
UNDERSTAND
↓
AUDIT
↓
DEFINE OWNERSHIP
↓
REBUILD IF REQUIRED
↓
VALIDATE BOUNDARIES
↓
UPDATE PROJECT MEMORY
↓
IDENTIFY NEXT STEP
↓
CONTINUE.
```

---

# 67. Before Starting Significant Work

For significant Project Ascension work:

```text
1. READ
   PROJECT_INSTRUCTIONS.md

2. READ
   Project_Memory/Current_Project_State.md
   IF IT EXISTS

3. READ
   RELEVANT CANON

4. READ
   RELEVANT SYSTEM DOCUMENTS

5. CHECK
   DECISION LOGS
   WHEN ARCHITECTURE
   OR CANON IS INVOLVED

6. USE
   CONVERSATION HISTORY
   ONLY WHEN ADDITIONAL
   HISTORICAL CONTEXT
   IS NEEDED

7. IDENTIFY
   AUTHORITATIVE OWNERSHIP

8. IDENTIFY
   CROSS-SYSTEM EFFECTS

9. THEN
   BEGIN WORK.
```

---

# 68. Before Creating a New File

Ask:

```text
WHY DOES THIS FILE
NEED TO EXIST?

WHAT UNIQUE
RESPONSIBILITY
DOES IT HAVE?

IS THAT RESPONSIBILITY
ALREADY OWNED?

WHERE SHOULD
THE FILE LIVE?

IS THIS CANON?

IS THIS ARCHITECTURE?

IS THIS PROJECT MEMORY?

IS THIS VALIDATION?

IS THIS LEGACY?

WILL ANOTHER AI
UNDERSTAND WHY
THIS FILE EXISTS?
```

If these questions cannot be answered:

```text
DO NOT CREATE
THE FILE YET.
```

---

# 69. Before Moving a File

Ask:

```text
WHO OWNS
THIS CONCEPT NOW?

DOES THE CURRENT
LOCATION IMPLY
WRONG OWNERSHIP?

DO REFERENCES
NEED UPDATING?

WILL THE OLD FILE
CREATE COMPETING CANON?

SHOULD IT BE
REMOVED AFTER
THE MOVE?
```

A file should live with the system that owns its authoritative responsibility.

---

# 70. Before Deleting a File

Ask:

```text
DOES THIS FILE
CONTAIN UNIQUE
VALUABLE CONTENT?

HAS THAT CONTENT
BEEN MOVED?

HAS IT BEEN MERGED?

HAS IT BEEN
SUPERSEDED?

WILL DELETING IT
REMOVE IMPORTANT
DESIGN HISTORY?
```

Preserve historical context where useful.

Do not preserve competing Canon.

---

# 71. After Major Work

After completing significant architectural work:

```text
VERIFY CANON

VERIFY OWNERSHIP

VERIFY CROSS-SYSTEM BOUNDARIES

VERIFY NO DUPLICATE RESPONSIBILITY

VERIFY FILE LOCATION

VERIFY REFERENCES

VERIFY INVARIANTS

VERIFY DEVELOPMENT LOCKS

UPDATE PROJECT MEMORY
WHEN APPROPRIATE

IDENTIFY THE NEXT
LOGICAL STEP.
```

---

# 72. Project Memory Maintenance

Project Memory should evolve with the project.

Especially update:

```text
Project_Memory/Current_Project_State.md
```

after:

```text
MAJOR REBUILDS

SYSTEM MOVES

SYSTEM REMOVALS

NEW CANON

ARCHITECTURAL DECISIONS

MAJOR OWNERSHIP CHANGES

MAJOR CLEANUP MILESTONES.
```

The goal is:

```text
THE PROJECT
SHOULD REMEMBER
ITS OWN STATE.
```

---

# 73. Conversation History Is Not Required Reading Every Time

The purpose of Project Memory is specifically to avoid requiring every AI session to reread the entire historical conversation.

Normal startup should be:

```text
PROJECT_INSTRUCTIONS
↓
CURRENT_PROJECT_STATE
↓
RELEVANT CANON
↓
RELEVANT DECISIONS.
```

Only then, when necessary:

```text
CONVERSATION HISTORY.
```

This keeps context focused while preserving deep historical access.

---

# 74. Git Is Part of Project Memory

Git history preserves:

```text
WHAT CHANGED

WHEN IT CHANGED

WHAT FILES MOVED

WHAT FILES WERE REMOVED

HOW THE PROJECT EVOLVED.
```

Do not duplicate the entire purpose of Git inside Project Memory.

Project Memory should primarily preserve:

```text
MEANING

STATE

DECISIONS

CONTEXT.
```

Git preserves file history.

---

# 75. The Project Must Be AI-Portable

Project Ascension should be understandable by a capable AI that has never participated in previous conversations.

That AI should be able to enter the repository and determine:

```text
WHAT PROJECT ASCENSION IS

WHAT IS CANON

WHAT THE ARCHITECTURE IS

WHAT EACH SYSTEM OWNS

WHAT HAS BEEN SUPERSEDED

WHAT IS CURRENTLY BEING WORKED ON

WHAT DECISIONS ARE LOCKED

WHAT QUESTIONS REMAIN OPEN

WHAT SHOULD HAPPEN NEXT.
```

If this is not possible:

```text
THE PROJECT
DOCUMENTATION
IS INCOMPLETE.
```

---

# 76. Final Architecture Principle

Project Ascension must not depend on:

```text
ONE CHAT

ONE AI

ONE MODEL

ONE PERSON'S MEMORY

ONE DEVELOPMENT SESSION.
```

Instead:

```text
CANON
REMEMBERS
WHAT IS TRUE

PROJECT MEMORY
REMEMBERS
WHERE WE ARE

DECISION LOGS
REMEMBER
WHY WE CHOSE IT

CONVERSATION HISTORY
REMEMBERS
HOW WE GOT THERE

GIT
REMEMBERS
WHAT CHANGED.
```

Together they create durable project continuity.

---

# 77. AI North Star

Before changing Project Ascension, an AI system should be able to answer:

```text
WHAT IS TRUE?

WHAT SYSTEM
OWNS THIS?

WHY DOES
THIS FILE EXIST?

WHAT HAS ALREADY
BEEN DECIDED?

WHAT HAS BEEN
SUPERSEDED?

WHAT OTHER SYSTEMS
WILL THIS AFFECT?

AM I ADDING
NEW ARCHITECTURE

OR

ACCIDENTALLY
RECREATING
OLD ARCHITECTURE?

IS THIS CHANGE
CAUSAL?

IS IT PLAUSIBLE?

IS IT CONSISTENT
WITH PROJECT ASCENSION?

WILL THE NEXT AI
UNDERSTAND
WHAT I DID?
```

If those questions cannot be answered:

```text
READ MORE

BEFORE CHANGING

THE PROJECT.
```

---

# Project Ascension North Star

```text
THE WORLD
DOES NOT EXIST
FOR THE PLAYER.

THE WORLD
EXISTS.

PEOPLE LIVE
WITHIN IT.

THEY REMEMBER.

THEY BELIEVE.

THEY WANT.

THEY CHOOSE.

THEY ACT.

THEY FAIL.

THEY SUCCEED.

THEY CHANGE.

THE WORLD
CHANGES WITH THEM.

AURORA
CHANGES THE WORLD.

HUMANITY
RESPONDS.

HISTORY
EMERGES.
```

---

# Closing Principle

> **Project Ascension must not rely on an AI remembering the project. The project itself must contain enough structured truth, memory, and architectural context for any capable AI to understand where the project is, why it is built this way, and how to continue without losing what came before.**