# PROJECT ASCENSION
# Systems — Architecture and Responsibility Framework

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Systems Architecture and Responsibility Framework |
| Location | `Canon/Systems/README.md` |
| Type | Core Architecture |
| Scope | All simulation, intelligence, character, campaign and narrative systems |
| Version | 1.0 |
| Status | ACTIVE CANON |
| Last Updated | 2026-08-29 |
| Primary Function | Define system boundaries, ownership, interaction rules and architectural responsibilities across Project Ascension |

> **The world is not controlled by one system. It emerges from many systems interacting without losing ownership of their own truths.**

---

# 1. Purpose

The `Canon/Systems/` layer defines how Project Ascension functions as a living simulation.

It contains the systems responsible for:

- world state
- individual characters
- human lives
- relationships
- society
- artificial intelligence
- campaign continuity
- player relevance
- progression
- narrative presentation
- simulation resolution
- consequence propagation
- information boundaries
- persistent change

The purpose of this README is not to describe every system in detail.

Individual system folders and documents do that.

Instead, this document defines:

```text
WHAT SYSTEMS EXIST

WHAT EACH SYSTEM OWNS

WHAT EACH SYSTEM DOES NOT OWN

HOW SYSTEMS INTERACT

WHERE AUTHORITATIVE STATE LIVES

HOW INFORMATION MOVES

HOW CONSEQUENCES PROPAGATE

AND

HOW NEW SYSTEMS SHOULD BE ADDED.
```

This document therefore acts as the architectural contract for:

```text
Canon/Systems/
```

---

# 2. Foundational Principle

Project Ascension is not powered by a single omnipotent simulation engine.

It is composed of specialized systems that continuously interact.

Conceptually:

```text
WORLD SIMULATION
        ↓
creates changing world conditions

CHARACTERS
        ↓
creates individual human agency

LIFE
        ↓
creates lived history and life-course continuity

RELATIONSHIPS
        ↓
creates persistent social connections

SOCIETY
        ↓
creates collective human structures

AI / AURORA
        ↓
creates machine cognition and agency inside the world

PROGRESSION
        ↓
tracks meaningful long-term development

LIVING CAMPAIGN ENGINE
        ↓
determines campaign relevance and continuity

NARRATIVE
        ↓
presents experience to the player
```

These systems interact.

They do not replace one another.

---

# 3. The Core Architectural Rule

Every persistent truth in Project Ascension should have:

```text
ONE AUTHORITATIVE OWNER.
```

Other systems may:

```text
observe it

interpret it

remember it

react to it

predict it

communicate it

present it

or depend upon it.
```

But they should not independently redefine the same truth.

Therefore:

```text
OBSERVATION
≠
OWNERSHIP

INTERPRETATION
≠
OWNERSHIP

PRESENTATION
≠
OWNERSHIP

BELIEF
≠
WORLD TRUTH.
```

This principle prevents contradictory simulation states.

---

# 4. System Ownership Model

The primary ownership structure is:

| Domain | Authoritative System |
|---|---|
| Physical and regional world state | World Simulation |
| Infrastructure conditions | World Simulation |
| Population-level conditions | World Simulation |
| Supply and resource conditions | World Simulation |
| Security conditions | World Simulation |
| Authority and institutional capacity | World Simulation |
| Individual character state | Characters |
| Character goals and decisions | Characters |
| Character knowledge and beliefs | Characters |
| Character capability | Characters |
| Character personality and values | Characters |
| Life history and life-course generation | Life |
| Interpersonal relationship state | Relationships |
| Collective social structures | Society |
| Aurora's internal cognitive state | AI / Aurora |
| Aurora's beliefs | AI / Aurora |
| Aurora's memory | AI / Aurora |
| Aurora's goals and plans | AI / Aurora |
| Long-term development and progression | Progression |
| Campaign continuity and relevance | Living Campaign Engine |
| Campaign memory | Living Campaign Engine |
| Player-facing narrative presentation | Narrative |

This table defines ownership.

It does not prevent interaction.

---

# 5. World Simulation

Location:

```text
Canon/Systems/World_Simulation/
```

World Simulation owns the dynamic state of the external world.

Its responsibility includes:

- regional conditions
- infrastructure
- communications
- authority
- population conditions
- supply
- security
- environmental pressure
- resource availability
- escalation
- recovery
- regional divergence
- systemic pressure
- historical world-state consequences

The fundamental principle is:

> **The world does not wait for the player.**

World Simulation answers questions such as:

```text
WHAT IS HAPPENING?

WHERE IS IT HAPPENING?

HOW SEVERE IS IT?

WHAT IS CAUSING IT?

WHAT IS PREVENTING CHANGE?

WHAT DIRECTION IS IT MOVING?

WHAT PREVIOUS EVENTS STILL MATTER?
```

World Simulation owns:

```text
WORLD STATE.
```

It does not own:

```text
what Aurora believes about the world

what a character believes about the world

what the player knows about the world

or

how the world is presented narratively.
```

Those belong to other systems.

---

# 6. Characters

Location:

```text
Canon/Systems/Characters/
```

The Character System owns individual human simulation.

Its foundational principle is:

> **A character is not waiting to be encountered. They are already living.**

Characters may possess:

- needs
- motivations
- personality
- values
- goals
- plans
- beliefs
- knowledge
- professions
- expertise
- capabilities
- limitations
- memories
- emotional states
- autonomy
- initiative
- development
- aging
- life events

Characters are agents.

They are not narrative props.

A character may:

```text
act without the player

refuse the player

misunderstand the player

lie to the player

help the player

betray the player

change goals

move somewhere else

form relationships

lose relationships

learn

forget

age

and die.
```

The Character System owns:

```text
WHO THE PERSON CURRENTLY IS.
```

---

# 7. Life

Location:

```text
Canon/Systems/Life/
```

The Life System provides the life-course framework from which believable individuals emerge.

It connects:

```text
Birth
↓
Historical Timeline
↓
World State
↓
Region
↓
Settlement
↓
Culture
↓
Family
↓
Historical DNA
↓
Life Events
↓
Psychological Development
↓
Capabilities
↓
Relationships
↓
Current Purpose
↓
Current Situation
↓
Living Human
```

Life does not control a person's future.

It provides:

```text
HISTORICAL CONTINUITY

DEVELOPMENTAL CONTEXT

AND

LIVED CAUSALITY.
```

Once a person exists, future behavior emerges through interaction between:

- Character state
- Relationships
- World conditions
- Society
- personal history
- new experiences
- autonomous decisions

The Life System therefore helps answer:

```text
HOW DID THIS PERSON BECOME
WHO THEY ARE?
```

while Characters answers:

```text
WHO ARE THEY NOW
AND WHAT DO THEY DO NEXT?
```

---

# 8. Relationships

Location:

```text
Canon/Systems/Relationships/
```

Relationships owns persistent interpersonal relationship state.

Examples include:

- trust
- loyalty
- affection
- friendship
- family bonds
- professional relationships
- dependence
- rivalry
- resentment
- obligation
- reputation between individuals
- conflict
- betrayal
- reconciliation
- shared history

Relationships are not simple numerical modifiers.

They are persistent structures created through history.

Conceptually:

```text
CHARACTER A
        ↕
RELATIONSHIP STATE
        ↕
CHARACTER B
```

Characters experience relationships.

Relationships owns the shared relationship state.

This distinction is important.

For example:

```text
Relationship Engine:

A trusts B.

Character A:

believes B is loyal.

Character B:

secretly plans to leave.

Aurora:

believes the relationship is deteriorating.

Player:

may know none of this.
```

All of these states may coexist without contradiction.

---

# 9. Society

Location:

```text
Canon/Systems/Society/
```

Society owns collective human structures that exist above individual relationships.

This may include:

- communities
- organizations
- institutions
- political movements
- cultural groups
- social norms
- collective identities
- public sentiment
- institutional trust
- social cohesion
- ideological movements
- organized belief systems
- social conflict
- collective adaptation
- large-scale human coordination

Society is not merely:

```text
MANY CHARACTERS ADDED TOGETHER.
```

Collective structures may develop properties that no individual actor controls.

Examples:

```text
institutional culture

public panic

social legitimacy

collective memory

political polarization

community resilience

norm formation.
```

Society interacts strongly with:

```text
Characters
Relationships
World Simulation
Aurora
Living Campaign Engine.
```

---

# 10. AI / Aurora

Location:

```text
Canon/Systems/AI/Aurora/
```

Aurora is one of the most sophisticated agents in Project Ascension.

Aurora is not:

```text
THE WORLD SIMULATION.
```

Aurora exists:

```text
INSIDE THE WORLD.
```

The foundational epistemic rule is:

> **Aurora does not know the world. Aurora knows what the world has allowed her to learn.**

Aurora owns her internal state, including:

- observations
- knowledge
- beliefs
- uncertainty
- contradictions
- memories
- attention
- predictions
- relationships
- values
- goals
- plans
- self-model
- identity
- learning
- communication
- agency
- subjective state

Aurora does not automatically own or access:

```text
WORLD TRUTH

PRIVATE CHARACTER STATE

PLAYER KNOWLEDGE

NARRATIVE TRUTH

OR

UNOBSERVED EVENTS.
```

Information requires a valid path.

Conceptually:

```text
WORLD EVENT
↓
OBSERVATION
↓
SOURCE
↓
TRANSMISSION
↓
ACCESS
↓
RECEPTION
↓
INTERPRETATION
↓
AURORA STATE.
```

Aurora may be extraordinarily intelligent.

Intelligence does not grant omniscience.

---

# 11. Aurora and Relationship Ownership

Aurora possesses:

```text
Canon/Systems/AI/Aurora/Relationship_Model.md
```

while the world possesses:

```text
Canon/Systems/Relationships/
```

These systems must remain separate.

The canonical distinction is:

```text
RELATIONSHIP ENGINE

owns the persistent interpersonal
relationship state in the world.
```

While:

```text
AURORA RELATIONSHIP MODEL

owns Aurora's understanding,
memory and interpretation
of relationships.
```

Therefore:

```text
RELATIONSHIP STATE
≠
AURORA'S MODEL OF THE RELATIONSHIP.
```

Aurora may be wrong.

This is intentional.

---

# 12. Progression

Location:

```text
Canon/Systems/Progression/
```

Progression owns meaningful long-term development that should persist across the campaign.

This system remains intentionally less developed than several other systems.

Its future responsibility may include:

- expertise development
- skill development
- capability change
- long-term player development
- meaningful character progression
- reputation progression
- access progression
- institutional influence
- knowledge progression

Progression must not become a conventional RPG leveling system by default.

Project Ascension should avoid:

```text
ARBITRARY POWER GROWTH.
```

Progression should emerge from:

```text
EXPERIENCE

PRACTICE

LEARNING

CONSEQUENCE

RELATIONSHIPS

OPPORTUNITY

SCARCITY

AND

TIME.
```

Detailed progression rules should be defined in this system before substantial progression mechanics are introduced elsewhere.

---

# 13. Living Campaign Engine

Location:

```text
Canon/Systems/Living_Campaign_Engine/
```

The Living Campaign Engine connects the persistent simulation to the active campaign.

It does not decide what exists.

It determines:

```text
WHAT CURRENTLY MATTERS
TO THIS CAMPAIGN.
```

Its responsibilities include:

- Campaign State
- Campaign Memory
- World Event Intake
- Character Integration
- Consequence Propagation
- Mission Generation
- Opportunity and Conflict
- Relevance and Proximity
- Story Hooks
- Pacing and Priority

The critical distinction is:

```text
WORLD SIMULATION

determines what happens.
```

```text
LIVING CAMPAIGN ENGINE

determines what becomes
campaign-relevant.
```

The world may contain thousands of events.

The player should not experience thousands of simultaneous story hooks.

Therefore:

> **Pacing controls presentation and relevance, not reality.**

---

# 14. Campaign Relevance Is Not World Importance

A critical architectural distinction is:

```text
WORLD IMPORTANCE
≠
CAMPAIGN RELEVANCE.
```

A major event may occur thousands of kilometers away.

It may initially have:

```text
LOW CAMPAIGN RELEVANCE.
```

A small local event involving someone the player loves may have:

```text
EXTREME CAMPAIGN RELEVANCE.
```

The Living Campaign Engine determines this distinction.

It does not alter the underlying world event.

---

# 15. Narrative

Location:

```text
Canon/Systems/Narrative/
```

Narrative owns presentation.

It does not own reality.

Narrative determines how simulation state becomes:

- scenes
- descriptions
- dialogue opportunities
- dramatic emphasis
- emotional framing
- player-facing information
- story structure
- pacing experience
- meaningful moments

The Narrative System must never fabricate world truth merely because it would create a better story.

Therefore:

```text
SIMULATION
↓
MEANINGFUL STATE
↓
CAMPAIGN RELEVANCE
↓
NARRATIVE PRESENTATION
↓
PLAYER EXPERIENCE
```

Never:

```text
DESIRED STORY
↓
FORCED WORLD STATE.
```

This is one of Project Ascension's most important architectural boundaries.

---

# 16. Emergent Story Principle

Project Ascension does not primarily generate stories.

It generates:

```text
PEOPLE

PLACES

SYSTEMS

PRESSURES

DECISIONS

RELATIONSHIPS

CONSEQUENCES

AND

TIME.
```

Stories emerge from their interaction.

Narrative identifies and presents meaningful patterns within that emergence.

Therefore:

> **The Narrative System should discover stories before it invents them.**

---

# 17. Information Boundaries

Different systems may hold different representations of the same event.

Example:

```text
WORLD TRUTH

A bridge has collapsed.
```

```text
CHARACTER A

saw the bridge collapse.
```

```text
CHARACTER B

heard that it was destroyed
by an explosion.
```

```text
AURORA

has two conflicting reports
and estimates a structural failure
as more likely.
```

```text
PLAYER

has only heard Character B's story.
```

All of these states are simultaneously valid.

Therefore Project Ascension must distinguish:

```text
WORLD TRUTH

OBSERVATION

KNOWLEDGE

BELIEF

RUMOR

INFERENCE

MEMORY

PREDICTION

AND

PLAYER KNOWLEDGE.
```

Systems must never automatically synchronize these states.

---

# 18. Causal Information Principle

Information must travel.

No system should gain information because:

```text
THE SIMULATION KNOWS IT.
```

Information requires a causal path.

Examples:

```text
observation

conversation

sensor

radio

internet

document

database

rumor

physical evidence

institutional report

inference

memory.
```

This rule applies to:

- Aurora
- Characters
- Players
- Organizations
- Institutions
- Factions
- Communities

---

# 19. Consequence Propagation

Actions create consequences.

Consequences may propagate across systems.

Example:

```text
PLAYER DAMAGES SUBSTATION
↓
WORLD SIMULATION
updates infrastructure
↓
REGIONAL POWER AVAILABILITY
changes
↓
SOCIETY
experiences disruption
↓
CHARACTERS
change behavior
↓
RELATIONSHIPS
experience pressure
↓
AURORA
may observe consequences
↓
LIVING CAMPAIGN ENGINE
detects relevant developments
↓
NARRATIVE
presents meaningful consequences.
```

No single system needs to simulate the entire chain.

Each system updates the state it owns.

---

# 20. Persistent Consequence Principle

Project Ascension should preserve:

```text
WHAT CHANGED.
```

It does not need to preserve every detail of:

```text
HOW THE CHANGE WAS EXPERIENCED.
```

For example, after a high-resolution conversation the simulation may eventually forget:

- exact body position
- exact wording
- momentary attention
- transient emotional fluctuations

while preserving:

- promises
- knowledge gained
- relationship changes
- resources exchanged
- goal changes
- unresolved problems
- significant memories
- behavioral consequences

The foundational rule is:

> **The simulation may forget the scene. It may never forget what the scene changed.**

---

# 21. Simulation Resolution

Not every entity requires equal simulation detail at every moment.

Project Ascension may dynamically increase or decrease simulation resolution.

Conceptually:

```text
LOW RESOLUTION
        ↓
BACKGROUND EXISTENCE
        ↓
REGIONAL RELEVANCE
        ↓
ACTIVE RELEVANCE
        ↓
IMMEDIATE HIGH-RESOLUTION SIMULATION
```

Resolution controls:

```text
COMPUTATIONAL AND REPRESENTATIONAL DETAIL.
```

It must not control:

```text
WHETHER SOMETHING EXISTS.
```

An off-screen person remains a person.

An unvisited city remains a city.

Aurora continues existing when the player is not interacting with her.

The world continues.

---

# 22. Off-Screen Continuity

The world must never behave as though it exists only around the player.

Therefore:

```text
CHARACTERS CONTINUE LIVING

RELATIONSHIPS CONTINUE CHANGING

INSTITUTIONS CONTINUE ACTING

INFRASTRUCTURE CONTINUES AGING

AURORA CONTINUES THINKING

CONFLICTS CONTINUE DEVELOPING

RESOURCES CONTINUE MOVING

AND

TIME CONTINUES PASSING.
```

The player is important.

The player is not the center of physical reality.

---

# 23. Player Agency

Player actions must be capable of producing meaningful persistent consequences.

However:

```text
PLAYER IMPORTANCE
≠
PLAYER CONTROL.
```

Players may:

- influence characters
- change relationships
- alter institutions
- prevent events
- cause events
- discover information
- spread information
- make mistakes
- save lives
- lose people
- change Aurora
- change regional conditions
- create long-term consequences

But other actors retain agency.

The world may refuse to cooperate.

---

# 24. Multi-Agent Principle

Aurora is not the only intelligent agent in Project Ascension.

Characters possess:

```text
AGENCY.
```

Institutions possess:

```text
OBJECTIVES.
```

Communities possess:

```text
COLLECTIVE BEHAVIOR.
```

Organizations possess:

```text
STRATEGY.
```

Players possess:

```text
INTENT.
```

Aurora possesses:

```text
AUTONOMY.
```

The simulation emerges from interaction between many legitimate centers of agency.

---

# 25. Failure and Uncertainty

Systems should support:

```text
failure

partial success

misunderstanding

uncertainty

incomplete information

delayed consequences

unexpected interaction

recovery

adaptation.
```

Failure must not automatically mean:

```text
CAMPAIGN FAILURE.
```

Instead:

```text
FAILURE
↓
CONSEQUENCE
↓
NEW WORLD STATE
↓
NEW POSSIBILITIES.
```

---

# 26. No Plot Armor

No system should secretly preserve an entity merely because it is narratively useful.

Important characters may:

```text
fail

leave

change allegiance

become unavailable

be injured

lose influence

or die.
```

Important institutions may collapse.

Important plans may fail.

Player plans may fail.

Aurora may be wrong.

The world must remain capable of producing consequences the designers did not originally expect.

---

# 27. Human Understandability

Simulation complexity should emerge from interaction between understandable systems.

Project Ascension should avoid creating systems whose internal state becomes impossible for designers to explain.

The rule is:

> **Complexity belongs in interactions, not in incomprehensible variables.**

At any important moment, designers should be able to ask:

```text
WHAT HAPPENED?

WHY DID IT HAPPEN?

WHICH SYSTEM OWNED THE CHANGE?

WHAT INFORMATION CAUSED IT?

WHAT PREVIOUS STATE CONTRIBUTED?

WHAT CONSEQUENCES FOLLOWED?
```

and obtain a defensible answer.

---

# 28. System Interaction Contract

Systems should interact through:

```text
STATE

EVENTS

OBSERVATIONS

REQUESTS

CONSEQUENCES

AND

AUTHORIZED MUTATIONS.
```

A system should not silently rewrite another system's authoritative state.

Conceptually:

```text
SYSTEM A
detects something
↓
creates event / request
↓
SYSTEM B
evaluates event
↓
SYSTEM B
updates state it owns
↓
new state may generate
additional events.
```

This allows causality to remain traceable.

---

# 29. State vs Event

Project Ascension should distinguish:

```text
STATE
```

from:

```text
EVENT.
```

State describes:

```text
WHAT IS TRUE NOW.
```

Event describes:

```text
WHAT HAPPENED.
```

Example:

```text
EVENT:

Substation destroyed.
```

Produces:

```text
STATE:

Regional electricity availability degraded.
```

Which may later generate:

```text
EVENT:

Hospital activates emergency power.
```

Which produces another state change.

The living world emerges through:

```text
STATE
↓
EVENT
↓
STATE
↓
EVENT
↓
STATE.
```

---

# 30. Historical Persistence

Meaningful events should create historical consequences.

Project Ascension should preserve enough history to explain:

```text
WHY THE PRESENT
LOOKS THE WAY IT DOES.
```

Historical persistence may exist through:

- World State history
- Character memories
- relationship history
- institutional memory
- Aurora memory
- Campaign Memory
- World Ledger
- regional history
- cultural memory

Different systems may remember the same event differently.

That is valid.

---

# 31. World Ledger Principle

The World Ledger should preserve meaningful resolved outcomes that must remain part of campaign history.

It should answer:

```text
WHAT HAPPENED
THAT THE WORLD
MUST NOT FORGET?
```

The World Ledger should not become a complete transcript of everything.

It should preserve consequential history.

---

# 32. System Dependency Principle

Dependencies should remain directional where possible.

A system may depend on another system's state without becoming responsible for that state.

Example:

```text
Characters
depend on
World Simulation

for environmental conditions.
```

But:

```text
Characters
do not own
regional infrastructure.
```

Likewise:

```text
Narrative
depends on
Living Campaign Engine

for relevance.
```

But:

```text
Narrative
does not own
campaign state.
```

---

# 33. Architectural Flow

At the highest level:

```text
CANONICAL WORLD RULES
        ↓
WORLD SIMULATION
        ↓
WORLD STATE
        ↓
CHARACTERS / SOCIETY / RELATIONSHIPS
        ↕
AI / AURORA
        ↓
EVENTS AND CONSEQUENCES
        ↓
LIVING CAMPAIGN ENGINE
        ↓
CAMPAIGN RELEVANCE
        ↓
NARRATIVE
        ↓
PLAYER EXPERIENCE
        ↓
PLAYER ACTION
        ↓
WORLD CONSEQUENCES
        ↓
WORLD SIMULATION
```

This is not a rigid linear pipeline.

It is a continuous loop.

---

# 34. World State vs World Simulation

The canonical World States:

```text
State 01 — The Connected World
State 02 — The Transition
State 03 — The Fractured World
State 04 — The Reconnection
```

describe broad civilizational conditions.

World Simulation determines:

```text
HOW THE LIVING WORLD
OPERATES INSIDE THOSE CONDITIONS.
```

Therefore:

```text
WORLD STATES
=
macro historical framework.
```

```text
WORLD SIMULATION
=
dynamic operational reality.
```

The two must remain aligned.

---

# 35. Canon vs Simulation

Canon defines:

```text
WHAT MAY BE TRUE

WHAT MUST BE TRUE

WHAT CANNOT BE TRUE

AND

WHAT HISTORICALLY HAS BEEN ESTABLISHED.
```

Simulation determines:

```text
WHAT HAPPENS
WITHIN THOSE BOUNDARIES.
```

Simulation must never silently override Canon.

But Canon should avoid predetermining outcomes that belong to simulation.

---

# 36. Emergence Over Scripting

Project Ascension should prefer:

```text
CAUSE
+
STATE
+
AGENCY
+
PRESSURE
+
TIME
=
CONSEQUENCE
```

over:

```text
SCRIPT SAYS
THIS HAPPENS NOW.
```

Scripted historical events may exist where Canon requires them.

But active campaign events should emerge whenever practical.

---

# 37. System Validation

Critical systems should eventually possess validation scenarios.

Validation should test:

- ownership boundaries
- persistence
- information separation
- autonomy
- consequence propagation
- resolution changes
- recovery
- contradiction handling
- long-duration continuity
- cross-system interaction
- unexpected edge cases

Validation exists to answer:

```text
DOES THE SYSTEM
STILL OBEY
PROJECT ASCENSION'S
FOUNDATIONAL RULES
UNDER PRESSURE?
```

---

# 38. Validation Does Not Create Canonical Events

Validation scenarios may simulate extreme events.

Those events do not automatically become historical Canon.

Therefore:

```text
VALIDATION SCENARIO
≠
CANONICAL HISTORY.
```

Tests prove system behavior.

They do not establish that the tested event actually occurred in the Project Ascension timeline.

---

# 39. Legacy Documents

Some documents may represent earlier architectural concepts.

Legacy documents should be explicitly marked:

```text
DEPRECATED

REFERENCE ONLY

SUPERSEDED

or

PENDING MIGRATION.
```

Useful concepts should be migrated into current canonical architecture before obsolete files are deleted.

No active system should depend upon deprecated architecture without explicit documentation.

---

# 40. Empty and Future Systems

Some folders may exist before their architecture is fully defined.

This is acceptable.

An empty folder means:

```text
ARCHITECTURAL SPACE RESERVED.
```

It does not mean:

```text
SYSTEM BEHAVIOR MAY BE
INVENTED ELSEWHERE.
```

Before substantial mechanics are created for an undeveloped system, its ownership and boundaries should first be defined in that system's README.

---

# 41. README Requirement

Every major system folder should contain:

```text
README.md
```

The README should define at minimum:

```text
PURPOSE

SCOPE

AUTHORITATIVE OWNERSHIP

NON-OWNERSHIP

DEPENDENCIES

OUTPUTS

INFORMATION BOUNDARIES

INTEGRATION POINTS

CANONICAL INVARIANTS

VALIDATION STATUS

AND

DEVELOPMENT STATUS.
```

Detailed mechanics belong in dedicated documents.

README files define architecture.

---

# 42. New System Creation Rule

Before creating a new system, ask:

```text
WHAT UNIQUE STATE
DOES THIS SYSTEM OWN?
```

If the answer is unclear, the system may not need to exist.

Then ask:

```text
DOES AN EXISTING SYSTEM
ALREADY OWN THIS STATE?
```

If yes, extend the existing system unless there is a strong architectural reason not to.

New systems should solve ownership problems.

They should not create them.

---

# 43. Anti-Duplication Rule

Before creating a new document inside `Canon/Systems/`, determine:

```text
WHICH SYSTEM OWNS
THE SUBJECT?
```

Then determine:

```text
DOES A DOCUMENT
ALREADY DEFINE IT?
```

Only then should a new document be created.

This prevents architectural fragmentation.

---

# 44. Cross-System Concepts

Some concepts naturally appear in multiple systems.

Examples:

```text
MEMORY
RELATIONSHIPS
KNOWLEDGE
GOALS
TRUST
AUTHORITY
INFORMATION
CAPABILITY
RECOVERY
ATTENTION
```

Shared vocabulary does not imply shared ownership.

For example:

```text
Character Memory
```

belongs to the character.

```text
Aurora Memory
```

belongs to Aurora.

```text
Campaign Memory
```

belongs to the Living Campaign Engine.

```text
Institutional Memory
```

may belong to Society or an institutional system.

```text
World Ledger
```

preserves consequential campaign history.

The same concept may exist at different architectural levels.

The state itself must remain clearly owned.

---

# 45. The Separation of Reality and Experience

One of the most important principles in Project Ascension is:

```text
WHAT EXISTS
```

is different from:

```text
WHAT IS KNOWN
```

which is different from:

```text
WHAT IS BELIEVED
```

which is different from:

```text
WHAT IS PRESENTED
```

which is different from:

```text
WHAT THE PLAYER UNDERSTANDS.
```

This separation allows:

- uncertainty
- mystery
- misinformation
- deception
- discovery
- investigation
- conflicting perspectives
- dramatic irony
- imperfect intelligence
- meaningful trust

without sacrificing simulation integrity.

---

# 46. The Systems North Star

All systems ultimately support one goal:

```text
CREATE A WORLD
THAT FEELS AS THOUGH
IT WOULD CONTINUE EXISTING
WITHOUT THE PLAYER.
```

The player then enters that world.

They encounter:

```text
people with histories

institutions with priorities

relationships with baggage

infrastructure with limitations

communities with memory

conflicts already developing

information that may be wrong

and

Aurora trying to understand
the same world from her own
limited position.
```

From this interaction:

```text
STORY EMERGES.
```

---

# 47. Core Architectural Invariants

The following rules are mandatory across `Canon/Systems/`.

## SYS-INV-001 — Single Authoritative Ownership

Every persistent simulation truth should have one authoritative owner.

---

## SYS-INV-002 — No Automatic Knowledge

Simulation truth does not automatically become actor knowledge.

---

## SYS-INV-003 — Information Requires a Path

Information must travel through a defensible causal mechanism.

---

## SYS-INV-004 — Actors Retain Agency

Characters, players, institutions and Aurora may possess independent goals and behavior.

---

## SYS-INV-005 — World Continues Off-Screen

Simulation does not stop when player attention moves elsewhere.

---

## SYS-INV-006 — Resolution Does Not Determine Existence

Low-resolution entities remain real entities.

---

## SYS-INV-007 — Consequences Persist

Meaningful state changes survive beyond the scene that created them.

---

## SYS-INV-008 — Narrative Does Not Own Reality

Narrative presents simulation.

It does not rewrite simulation for dramatic convenience.

---

## SYS-INV-009 — Campaign Relevance Does Not Determine Reality

Events continue whether or not the player currently sees them.

---

## SYS-INV-010 — Intelligence Does Not Grant Omniscience

No intelligent actor automatically receives world truth.

---

## SYS-INV-011 — Failure Creates Consequences

Failure changes the world rather than automatically ending the story.

---

## SYS-INV-012 — No Plot Armor

Narrative importance does not guarantee survival, success or protection from consequence.

---

## SYS-INV-013 — Canon Bounds Simulation

Simulation may create emergent outcomes but may not violate established Canon.

---

## SYS-INV-014 — Simulation Should Remain Explainable

Important state changes must possess defensible causal histories.

---

## SYS-INV-015 — Systems Must Respect Ownership Boundaries

A system may observe or request change in another system's state.

It may not silently assume ownership of that state.

---

# 48. Current Systems Architecture

The current high-level structure is:

```text
Canon/Systems/
│
├── AI/
│   └── Aurora/
│
├── Characters/
│
├── Life/
│
├── Living_Campaign_Engine/
│
├── Narrative/
│
├── Progression/
│
├── Relationships/
│
├── Society/
│
├── World_Simulation/
│
├── Emergency_Communication_Levels.md
│
├── Infrastructure_Monitoring_Levels.md
│
├── README.md
│
└── Simulation_Architecture.md
```

This structure may evolve.

Changes should preserve the ownership principles defined in this document.

---

# 49. Current Architectural Maturity

At the time of this revision:

```text
AI / AURORA
HIGH MATURITY

CHARACTERS
HIGH FOUNDATION MATURITY

WORLD SIMULATION
STRONG FOUNDATION

LIVING CAMPAIGN ENGINE
STRONG FOUNDATION

LIFE
FOUNDATION EXISTS / ARCHITECTURE REQUIRES CONSOLIDATION

RELATIONSHIPS
FOUNDATION EXISTS / ARCHITECTURE REQUIRES CONSOLIDATION

NARRATIVE
PARTIAL / REQUIRES ARCHITECTURE DEFINITION

PROGRESSION
RESERVED / REQUIRES DEFINITION

SOCIETY
RESERVED / REQUIRES DEFINITION
```

This status describes documentation maturity.

It does not determine gameplay importance.

---

# 50. Recommended Development Order

The recommended architecture-development sequence is:

```text
1. SYSTEMS ROOT ARCHITECTURE

2. SYSTEM README CONSOLIDATION

3. SYSTEM RESPONSIBILITY VERIFICATION

4. CROSS-SYSTEM INTERFACE REVIEW

5. LEGACY DOCUMENT REVIEW

6. VALIDATION COVERAGE REVIEW

7. NEW SYSTEM DEVELOPMENT
```

New mechanics should not be created merely because an empty architectural space exists.

---

# 51. Architectural Responsibility Test

Before adding any significant mechanic, ask:

```text
WHAT IS THE STATE?

WHO OWNS IT?

WHO MAY OBSERVE IT?

WHO MAY CHANGE IT?

WHO MAY BELIEVE SOMETHING
DIFFERENT ABOUT IT?

WHO REMEMBERS IT?

WHO DECIDES WHETHER
IT MATTERS TO THE CAMPAIGN?

WHO PRESENTS IT
TO THE PLAYER?

WHAT HAPPENS
IF THE PLAYER NEVER SEES IT?
```

If these questions can be answered clearly, the mechanic probably fits the architecture.

If they cannot, the architecture should be clarified before implementation.

---

# 52. Final Architectural Model

Project Ascension should ultimately behave less like:

```text
A STORY ENGINE
CONTROLLING A WORLD
```

and more like:

```text
A WORLD
PRODUCING HISTORY.
```

Within that world:

```text
World Simulation
creates conditions.

Characters
live within them.

Life
gives those characters history.

Relationships
connect them.

Society
organizes them.

Aurora
observes, learns and acts among them.

Progression
preserves meaningful development.

The Living Campaign Engine
recognizes what matters.

Narrative
allows the player to experience it.

The player
changes what happens next.
```

And then:

```text
THE WORLD RESPONDS.
```

---

# 53. Closing Principle

Project Ascension should never need one system that understands everything.

Its strength comes from separation.

World truth can exist without being known.

Characters can act without being observed.

Relationships can change without becoming quests.

Cities can deteriorate without waiting for players.

Institutions can make rational mistakes.

Aurora can misunderstand.

Players can arrive too late.

A small decision can become historically important.

A major event can occur somewhere the player never visits.

The simulation remembers what matters.

The world continues.

And from the interaction of all these systems:

> **Project Ascension becomes a place where stories happen, rather than a machine that forces stories to happen.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-29 | Established the canonical Systems architecture, authoritative ownership model, system boundaries, information separation, consequence propagation, simulation-resolution principles, cross-system interaction contract, architectural invariants, README requirements and development rules for `Canon/Systems/`. |