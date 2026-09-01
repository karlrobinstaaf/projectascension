# PROJECT ASCENSION

# World Simulation

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | World Simulation README |
| Location | `Canon/Systems/World_Simulation/README.md` |
| Version | 1.0 |
| Status | Active Canon |
| Category | Systems / World Simulation |
| Owner | World Simulation |
| Last Updated | 2026-09-01 |
| Primary Function | Provide the canonical entry point, ownership map and operating principles for the persistent external world simulation |

> **"The world does not wait for the player."**

---

# 1. Purpose

World Simulation defines how the external world of Project Ascension exists, changes, responds and persists over time.

Its central questions are:

```text
WHAT IS
ACTUALLY TRUE
IN THE WORLD?

WHAT CONDITIONS
EXIST HERE?

WHAT SYSTEMS
ARE FUNCTIONING?

WHAT SYSTEMS
ARE UNDER PRESSURE?

WHAT RESOURCES
ARE AVAILABLE?

WHAT INFRASTRUCTURE
IS OPERATIONAL?

WHAT EXTERNAL
CONSTRAINTS APPLY?

WHAT HAPPENS
WHEN ACTORS
INTERACT WITH
THE WORLD?

HOW DO
CONSEQUENCES
PROPAGATE?

HOW DOES
THE WORLD CHANGE

WHEN THE PLAYER
IS NOT PRESENT?
```

World Simulation provides:

```text
EXTERNAL
SIMULATION REALITY.
```

It does not determine:

```text
WHAT CHARACTERS
BELIEVE

WHAT CHARACTERS
WANT

WHAT CHARACTERS
CHOOSE

OR

HOW EVENTS
ARE PRESENTED
NARRATIVELY.
```

---

# 2. Core Principle

Project Ascension does not simulate:

```text
A SCRIPTED
APOCALYPSE.
```

It simulates:

```text
A COMPLEX WORLD

ATTEMPTING
TO CONTINUE
FUNCTIONING

UNDER

CHANGING
CONDITIONS

UNCERTAINTY

PRESSURE

AND

HUMAN RESPONSE.
```

Therefore:

```text
SYSTEMS FAIL
BECAUSE CONDITIONS
CAUSE FAILURE

NOT

BECAUSE THE STORY
REQUIRES FAILURE.
```

Likewise:

```text
SYSTEMS RECOVER
WHEN CONDITIONS
SUPPORT RECOVERY.
```

---

# 3. Architectural Position

World Simulation operates inside the broader architecture defined by:

```text
Canon/Systems/
Simulation_Architecture.md
```

The high-level relationship is:

```text
CHARACTERS
↓
WHAT ACTORS
TRY TO DO

WORLD SIMULATION
↓
WHAT EXTERNAL
REALITY ALLOWS
AND WHAT ACTUALLY
HAPPENS

LIFE / MEMORY /
RELATIONSHIPS /
SOCIETY / FACTIONS
↓
WHAT CONSEQUENCES
BECOME PERSISTENT

LIVING CAMPAIGN ENGINE
↓
WHAT REMAINS
CAUSALLY ACTIVE
AT CAMPAIGN SCALE

NARRATIVE
↓
HOW THAT REALITY
IS EXPERIENCED
BY THE PLAYER.
```

---

# 4. Ownership

World Simulation owns external simulation state such as:

```text
INFRASTRUCTURE

TRANSPORTATION

ENERGY

WATER

COMMUNICATION
AVAILABILITY

PHYSICAL GEOGRAPHY

ENVIRONMENTAL CONDITIONS

RESOURCE AVAILABILITY

SUPPLY CONDITIONS

SECURITY CONDITIONS

REGIONAL OPERATING
CONDITIONS

PHYSICAL DAMAGE

EXTERNAL HAZARDS

REGIONAL PRESSURE

RECOVERY CONDITIONS

EXTERNAL CONSEQUENCES.
```

---

# 5. What World Simulation Does Not Own

World Simulation does not own:

```text
CHARACTER GOALS

CHARACTER BELIEFS

CHARACTER KNOWLEDGE

CHARACTER VALUES

CHARACTER PSYCHOLOGY

CHARACTER RELATIONSHIPS

CHARACTER DECISIONS

CHARACTER DEVELOPMENT

LIFE HISTORY

CULTURE

SOCIAL NORMS

FACTION INTERNAL
DECISION MAKING

NARRATIVE PRESENTATION.
```

Those systems may respond to World Simulation.

They remain authoritative for their own state.

---

# 6. World Truth

World Simulation contributes to:

```text
WORLD TRUTH.
```

World Truth represents:

```text
WHAT IS
ACTUALLY TRUE

IN EXTERNAL
SIMULATION REALITY.
```

Examples:

```text
BRIDGE:
Destroyed

POWER:
Unavailable

ROAD:
Blocked

FUEL:
Constrained

HOSPITAL:
Operational

WEATHER:
Severe Storm

REGIONAL SUPPLY:
Degraded.
```

---

# 7. Distributed World Truth

World Truth does not need to exist in:

```text
ONE GIANT
WORLD OBJECT.
```

Different authoritative systems may own different parts of reality.

World Simulation coordinates the external world domains for which it is responsible.

---

# 8. Actual State vs Perceived State

Critical distinction:

```text
ACTUAL WORLD STATE
≠
PERCEIVED WORLD STATE.
```

Example:

```text
ACTUAL SUPPLY:
Stable

PUBLIC BELIEF:
Shortage imminent.
```

The belief may cause:

```text
stockpiling
↓
distribution pressure
↓
actual shortage.
```

World Simulation owns:

```text
THE ACTUAL
RESOURCE CONDITION.
```

Knowledge, Society and Character systems own:

```text
WHO BELIEVES WHAT.
```

---

# 9. World Layers

World Simulation may operate across:

```text
GLOBAL

NATIONAL

REGIONAL

LOCAL

COMMUNITY
```

layers.

These are not identical simulation states.

They represent different scales of external conditions.

---

# 10. Global Layer

The Global Layer may include:

```text
international trade

shipping

satellite infrastructure

global communications

financial systems

geopolitical pressure

international migration

global technology conditions.
```

Global conditions usually influence lower layers.

They should not automatically determine local reality.

---

# 11. National Layer

The National Layer may include:

```text
national infrastructure

strategic reserves

transportation networks

national communications

emergency coordination

military capacity

national institutions

financial stability.
```

A nation may remain:

```text
POLITICALLY INTACT
```

while experiencing:

```text
REGIONAL
OPERATIONAL
FRAGMENTATION.
```

---

# 12. Regional Layer

Regional state is one of the most important World Simulation layers.

Regions may differ according to:

```text
geography

infrastructure

population

resources

transportation

communication

security

institutional capacity

neighboring regions

human expertise

recovery capability.
```

Therefore:

```text
ONE REGION
MAY BE STABLE

WHILE

ANOTHER
IS CRITICAL.
```

---

# 13. Local Layer

Local simulation may represent:

```text
cities

towns

districts

transport corridors

industrial areas

specific infrastructure zones.
```

This layer strongly affects what Characters directly experience.

---

# 14. Community Boundary

The immediate social environment may involve:

```text
Characters

Relationships

Society

Families

organizations

institutions.
```

World Simulation provides:

```text
THE CONDITIONS
AROUND THEM.
```

It should not duplicate the social state owned by those systems.

---

# 15. Core External Domains

World Simulation may track external domains such as:

```text
INFRASTRUCTURE

COMMUNICATIONS

SUPPLY

SECURITY

TRANSPORTATION

ENERGY

WATER

ENVIRONMENT

RESOURCE AVAILABILITY

REGIONAL RECOVERY.
```

These domains may later be represented through more specialized files.

---

# 16. Infrastructure

Infrastructure may include:

```text
electricity

water

telecommunications

transportation

fuel distribution

healthcare infrastructure

logistics

data networks.
```

Infrastructure should integrate with:

```text
Canon/Systems/
Infrastructure_Monitoring_Levels.md
```

rather than duplicate it.

---

# 17. Communications

World Simulation owns:

```text
WHETHER
COMMUNICATION
CHANNELS EXIST

AND

WHETHER THEY
FUNCTION.
```

Examples:

```text
internet availability

cellular networks

radio

satellite connection

regional communication

emergency broadcasting.
```

Communication content and Character understanding belong elsewhere.

---

# 18. Communication Availability vs Information

Preserve:

```text
CHANNEL EXISTS
≠
MESSAGE SENT

MESSAGE SENT
≠
MESSAGE DELIVERED

MESSAGE DELIVERED
≠
MESSAGE UNDERSTOOD

MESSAGE UNDERSTOOD
≠
MESSAGE BELIEVED.
```

World Simulation may own:

```text
CHANNEL
AVAILABILITY.
```

Knowledge and Beliefs owns:

```text
CHARACTER
EPISTEMIC STATE.
```

---

# 19. Supply

Supply may represent availability and distribution of:

```text
food

fuel

medicine

replacement parts

industrial materials

batteries

water-treatment materials

specialized equipment.
```

Supply depends on:

```text
transportation

infrastructure

workforce

security

communication

production

storage

distribution.
```

---

# 20. Resource State

Resources exist independently of who currently wants them.

World Simulation or another authoritative resource system should own:

```text
RESOURCE EXISTENCE

QUANTITY

LOCATION

CONDITION

AVAILABILITY.
```

Characters may possess:

```text
ownership

control

access

authority

knowledge
```

regarding those resources.

---

# 21. Security

Security describes external operating conditions related to:

```text
crime

organized violence

infrastructure protection

emergency response

civil unrest

local defense

physical threat.
```

Security must not automatically deteriorate simply because:

```text
INFRASTRUCTURE
DETERIORATES.
```

Communities may:

```text
cooperate

organize

stabilize

or

adapt.
```

---

# 22. Transportation

Transportation represents the ability to move:

```text
people

goods

fuel

medicine

equipment

information carriers

specialists.
```

It depends on:

```text
roads

rail

fuel

vehicles

infrastructure

security

weather

human operators.
```

---

# 23. Geography

Geography is a real causal constraint.

Distance affects:

```text
travel time

supply

migration

institutional reach

communication

relationships

response time.
```

Project Ascension should preserve real geography wherever Canon has not explicitly changed it.

---

# 24. Environment

Environmental conditions may include:

```text
weather

temperature

flooding

fire

drought

storms

air quality

terrain

season.
```

Environmental conditions may create:

```text
pressure

hazard

resource change

transport limitation

infrastructure consequence.
```

---

# 25. State

State describes:

```text
WHAT IS
CURRENTLY TRUE.
```

Example:

```text
Infrastructure:
Degraded
```

or:

```text
Fuel Supply:
Constrained.
```

---

# 26. Pressure

Pressure describes:

```text
FORCES PUSHING
STATE TOWARD
CHANGE.
```

Example:

```text
Infrastructure:
Stable

Pressure:
High
```

because:

```text
maintenance delayed

spare parts declining

fuel decreasing

workforce shrinking.
```

This distinction is important.

A place may look stable while becoming fragile.

---

# 27. Resilience

Resilience represents:

```text
THE ABILITY
OF A SYSTEM

TO ABSORB
PRESSURE

WITHOUT
MAJOR STATE CHANGE.
```

Sources may include:

```text
redundancy

stored resources

experienced personnel

strong institutions

repair capability

local production

distributed infrastructure

communication

geographic advantage.
```

---

# 28. Recovery

Recovery must be modeled as seriously as degradation.

Recovery may arise through:

```text
repair

resource redistribution

redundancy

adaptation

new supply routes

community cooperation

human expertise

external assistance

reduced demand

restored communication.
```

---

# 29. Recovery Is Not Reset

Recovery does not mean:

```text
RETURN TO
PREVIOUS WORLD
UNCHANGED.
```

A recovered region may have:

```text
different institutions

different population

different trade routes

different social structures

different infrastructure

different vulnerabilities.
```

History remains.

---

# 30. Degradation

Systems may degrade because:

```text
resources disappear

dependencies fail

maintenance stops

personnel disappear

coordination weakens

transport breaks down

information becomes delayed

physical damage accumulates

demand exceeds capacity.
```

Degradation must have causes.

---

# 31. No Automatic Collapse

Canonical rule:

```text
NEGATIVE PRESSURE
≠
INEVITABLE COLLAPSE.
```

A degraded system may:

```text
stabilize

adapt

recover

reorganize

decentralize

fail temporarily

or

continue operating
at reduced capacity.
```

---

# 32. No Universal Collapse Clock

Avoid:

```text
DAY 20
POWER FAILS

DAY 30
RIOTS

DAY 40
GOVERNMENT COLLAPSES.
```

Prefer:

```text
PRESSURE
+
DEPENDENCIES
+
DECISIONS
+
RESILIENCE
+
EXTERNAL EVENTS
+
TIME

        ↓

WORLD CHANGE.
```

---

# 33. Interdependencies

World systems are interconnected.

Example:

```text
POWER
↓
COMMUNICATION
↓
COORDINATION
↓
TRANSPORTATION
↓
FUEL DELIVERY
↓
POWER.
```

This may create:

```text
FEEDBACK LOOPS.
```

But feedback does not guarantee catastrophe.

---

# 34. Cascading Consequences

A failure may propagate.

Example:

```text
POWER FAILURE
↓
WATER PUMP FAILURE
↓
HOSPITAL CAPACITY FALLS
↓
MEDICAL OUTCOMES CHANGE
↓
NEW LIFE EVENTS.
```

Each link requires causal support.

---

# 35. No Automatic Cascade

Avoid:

```text
ONE FAILURE
↓
EVERYTHING FAILS.
```

Dependencies may include:

```text
redundancy

backup systems

local alternatives

human intervention

stored resources

partial functionality.
```

---

# 36. Human Capability

Infrastructure depends on:

```text
PEOPLE.
```

A functional physical system may still fail operationally when:

```text
qualified personnel
are unavailable.
```

Therefore:

```text
PHYSICAL INFRASTRUCTURE
+
HUMAN CAPABILITY
+
RESOURCES
+
COORDINATION

=

FUNCTIONAL
SYSTEM CAPACITY.
```

---

# 37. Human Response Boundary

People respond to World conditions.

Possible responses include:

```text
adaptation

migration

cooperation

stockpiling

crime

conservation

protest

mutual aid

local organization

avoidance

repair.
```

But World Simulation should not directly determine:

```text
WHAT EVERY
INDIVIDUAL PERSON
DOES.
```

---

# 38. Individual Response

Individual human action belongs primarily to:

```text
Characters.
```

World Simulation provides:

```text
conditions

opportunities

constraints

external consequences.
```

---

# 39. Population Response

Population-scale patterns belong primarily to:

```text
Society
```

when they concern:

```text
collective behavior

norms

migration patterns

institutional adaptation

population perception.
```

World Simulation may consume the resulting aggregate effects.

---

# 40. World Simulation and Characters

Characters exist inside World Simulation.

They respond to:

```text
what they perceive

what they know

what they believe

what they want

what they can do.
```

They must not directly read:

```text
WORLD SIMULATION
DATABASE STATE.
```

---

# 41. Action Attempt

Characters and other Actors may attempt to:

```text
repair

move

build

destroy

access

investigate

communicate

protect

transport

search

interact

change external reality.
```

An Action Attempt represents:

```text
WHAT THE ACTOR
TRIES TO DO.
```

---

# 42. Action Attempt Is Not Outcome

Preserve:

```text
INTENT
≠
OUTCOME.
```

And:

```text
DECISION
≠
OUTCOME.
```

And:

```text
CAPABILITY
≠
OUTCOME.
```

---

# 43. Action Resolution

Action Resolution is the boundary where:

```text
ACTOR CAPABILITY

MEETS

WORLD REALITY.
```

It is governed architecturally by:

```text
Canon/Systems/
Simulation_Architecture.md
```

and externally resolved through:

```text
World Simulation.
```

---

# 44. Action Resolution Inputs

Resolution may consider:

```text
Action Attempt

task requirements

actual Capability

Expertise

tools

materials

facility

Actor condition

time

environment

access

authority

assistance

opposition

World state.
```

Not every action requires every input.

---

# 45. Action Resolution Output

Resolution produces:

```text
CANONICAL
CONSEQUENCE.
```

Possible forms include:

```text
success

partial success

failure

success with cost

failure with cost

resource consumption

damage

injury

delay

new hazard

information gained

changed World state.
```

---

# 46. Deterministic Outcomes

Not every Action requires uncertainty.

Example:

```text
correct key
+
correct lock
+
functional door

↓

door opens.
```

Do not add artificial randomness where the state already determines the result.

---

# 47. Uncertain Outcomes

Uncertainty may matter when:

```text
conditions are incomplete

hidden damage exists

systems are complex

environment varies

execution quality matters

other Actors respond.
```

Randomness may assist resolution.

It must not replace causality.

---

# 48. Impossible Actions

The world must allow:

```text
IMPOSSIBLE
```

as a real outcome.

Motivation does not override:

```text
physics

missing equipment

missing access

physical constraints

required material

required capability.
```

---

# 49. Opposed Human Actions

Actions involving another Character must preserve:

```text
THE OTHER
CHARACTER'S
AGENCY.
```

Example:

```text
NEGOTIATION

PERSUASION

DECEPTION

THREAT

COOPERATION.
```

Communication Expertise must not become:

```text
MIND CONTROL.
```

---

# 50. Information Actions

Characters may attempt to:

```text
observe

investigate

search

test

analyze

intercept

research.
```

World Simulation determines:

```text
WHAT EVIDENCE
IS AVAILABLE.
```

Knowledge and Beliefs determines:

```text
WHAT THE CHARACTER
LEARNS OR BELIEVES.
```

---

# 51. Information Delay

Information does not travel instantly.

Conceptually:

```text
EVENT
↓
OBSERVATION
↓
REPORT
↓
TRANSMISSION
↓
VERIFICATION
↓
RECIPIENT.
```

Any stage may be:

```text
delayed

lost

distorted

contradicted

classified

misunderstood.
```

---

# 52. Information Reliability Boundary

World Simulation may own:

```text
CHANNEL
AVAILABILITY

EVENT OCCURRENCE

SOURCE CONDITIONS.
```

Knowledge and Beliefs owns:

```text
CHARACTER-SPECIFIC
INFORMATION STATE.
```

Society may own:

```text
COLLECTIVE
INFORMATION PATTERNS.
```

---

# 53. Time

Time is part of World Simulation.

Canonical rule:

```text
TIME PASSES
EVEN WHEN
THE PLAYER
DOES NOTHING.
```

Time affects:

```text
travel

repair

resource depletion

weather

infrastructure

deadlines

Life

Aging

information freshness

recovery.
```

---

# 54. Opportunity Cost

Time creates tradeoffs.

```text
DOING A
```

may mean:

```text
NOT DOING B
BEFORE CONDITIONS
CHANGE.
```

This principle applies to both Characters and institutions.

---

# 55. Delayed Consequence

Some effects occur later.

Example:

```text
temporary repair
↓
appears functional
↓
time passes
↓
component fails.
```

Delayed consequences must remain causally traceable.

---

# 56. World Events

A World Event is:

> **A meaningful change in external simulated reality.**

Examples:

```text
storm

infrastructure failure

route closure

major migration

market disruption

regional communication loss

conflict

major repair

institutional breakdown.
```

---

# 57. World Event Exposure

A World Event does not automatically affect everyone.

Exposure depends on:

```text
location

dependency

transport connection

communication

institutional role

resource connection

social connection.
```

---

# 58. World Event vs Life Event

Example:

```text
WORLD EVENT:
Flood destroys neighborhood

CHARACTER CONSEQUENCE:
Home destroyed

LIFE EVENT:
Loss of home.
```

World Simulation owns:

```text
THE FLOOD
AND PHYSICAL DAMAGE.
```

Life owns:

```text
THE PERSONAL
BIOGRAPHICAL EVENT.
```

---

# 59. Consequence Propagation

Conceptually:

```text
WORLD EVENT
OR
ACTION RESOLUTION

        ↓

PRIMARY
EXTERNAL CONSEQUENCE

        ↓

AFFECTED SYSTEMS

        ↓

Life

Characters

Relationships

Society

Factions

Resources

Infrastructure

        ↓

NEW STATE.
```

---

# 60. Cross-System Update Rule

When a consequence affects another authoritative system:

```text
WORLD SIMULATION
PRODUCES
THE RELEVANT EVENT

↓

TARGET SYSTEM
VALIDATES
AND UPDATES
ITS OWN STATE.
```

World Simulation must not silently rewrite:

```text
Character Beliefs

Relationships

Values

Psychology

Goals.
```

---

# 61. Simulation Resolution

World Simulation must support adaptive resolution.

Not every:

```text
region

road

building

institution

resource flow
```

requires equal detail.

---

# 62. Resolution Principle

Use:

```text
THE LOWEST
SIMULATION DETAIL

THAT PRESERVES

CAUSALITY

CONTINUITY

AND

PLAUSIBLE OUTCOME.
```

---

# 63. Resolution Is Not Player Distance

Player proximity may influence detail.

But:

```text
PLAYER DISTANCE
≠
WORLD IMPORTANCE.
```

A distant event may require greater simulation resolution if it has major causal consequences.

---

# 64. Low-Resolution World Simulation

Low Resolution may preserve:

```text
regional conditions

major resources

major infrastructure

important institutions

major pressures

major events

major state changes.
```

---

# 65. Medium-Resolution World Simulation

Medium Resolution may add:

```text
local systems

active dependencies

resource movement

specific institutions

important transport

specific pressures

near-term events.
```

---

# 66. High-Resolution World Simulation

High Resolution may include:

```text
specific location

specific infrastructure

specific task conditions

specific resource availability

immediate environmental state

Actors

Action Resolution context.
```

---

# 67. Resolution Changes Detail

The world does not become:

```text
MORE REAL
```

because the player approaches.

Resolution changes:

```text
REPRESENTATIONAL
DETAIL.
```

Not reality.

---

# 68. Cross-Resolution Causality

Different systems may interact across resolution levels.

Example:

```text
HIGH-RESOLUTION
LOCAL ACTION
↓
REGIONAL
SUPPLY CHANGE
↓
LOW-RESOLUTION
DISTANT EFFECT
↓
FUTURE
LOCAL CONSEQUENCE.
```

Causality must cross resolution boundaries.

---

# 69. Persistence

Important World state changes must persist.

Examples:

```text
destroyed bridge

repaired power station

depleted fuel reserve

new settlement

migration

changed trade route

damaged hospital

abandoned district.
```

---

# 70. History

Recovery does not erase:

```text
WHAT HAPPENED.
```

A previously critical region may later become stable.

Its history may still affect:

```text
infrastructure design

population behavior

institutions

resource strategy

Society

Characters.
```

---

# 71. Canon vs Simulation

Preserve:

```text
CANON
=
WHAT IS
ESTABLISHED
ABOUT THE UNIVERSE

SIMULATION
=
WHAT CAN HAPPEN
WITHIN THOSE
BOUNDARIES.
```

Simulation must respect Canon.

It must not merely replay Canonical history in every campaign.

---

# 72. World States

World States represent broad historical conditions.

They must not function as:

```text
GLOBAL
SCRIPTED MODES
THAT FORCE
EVERY REGION
INTO THE
SAME STATE.
```

Regional variation remains essential.

---

# 73. World State Transition

World State transitions should emerge from:

```text
accumulated history

system changes

institutional adaptation

technology

human response

Aurora

world conditions.
```

They should not reset simulation state.

---

# 74. The Collapse

The Collapse must not operate as:

```text
ONE SWITCH

WORLD WORKS
↓
WORLD BROKEN.
```

It should emerge from:

```text
dependency

fragmentation

institutional pressure

reduced coordination

infrastructure failure

information uncertainty

human adaptation

time.
```

---

# 75. The Collapse Is Uneven

Some regions may:

```text
fail early

remain stable

recover

adapt

isolate

reorganize.
```

There is no requirement for:

```text
UNIFORM
COLLAPSE.
```

---

# 76. Recovery Is Canonical

Recovery must always remain:

```text
A POSSIBLE
SIMULATION DIRECTION.
```

This does not mean recovery is:

```text
easy

quick

complete

or

guaranteed.
```

---

# 77. Society Boundary

Society owns:

```text
HOW HUMAN
POPULATIONS
ORGANIZE
UNDER CONDITIONS.
```

World Simulation owns:

```text
THE CONDITIONS.
```

Example:

```text
WORLD SIMULATION:
Food supply declines

SOCIETY:
Rationing norm emerges

CHARACTERS:
Individuals comply,
resist or exploit it.
```

---

# 78. Faction Boundary

Factions may consume World state when making organizational decisions.

World Simulation must not decide:

```text
WHAT A FACTION
WANTS.
```

Faction systems own:

```text
organizational agency.
```

---

# 79. Living Campaign Engine Boundary

World Simulation determines:

```text
WHAT IS
HAPPENING.
```

The Living Campaign Engine tracks:

```text
WHAT IS
CAUSALLY ACTIVE
AND MAY REQUIRE
CAMPAIGN ATTENTION.
```

---

# 80. Narrative Boundary

Narrative may turn:

```text
FUEL SUPPLY:
CRITICAL
```

into human-scale presentation such as:

```text
rationing

closed transport service

hospital request

black market

political dispute.
```

But those manifestations must remain compatible with:

```text
actual simulation state.
```

---

# 81. Aurora Boundary

Aurora may:

```text
observe

analyze

predict

communicate

act

influence systems.
```

But:

```text
AURORA
IS NOT
WORLD SIMULATION.
```

Her predictions do not automatically become truth.

---

# 82. Aurora Action

If Aurora changes the world:

```text
THE ACTION
MUST HAVE
A CAUSAL PATH.
```

Example:

```text
Aurora issues instruction
↓
institution receives it
↓
humans or automated systems act
↓
infrastructure changes.
```

Avoid:

```text
AURORA
CHANGES STATE
BY MAGIC.
```

---

# 83. Player Interaction

The player may affect:

```text
infrastructure

resources

information

security

transport

institutions

local conditions.
```

Effects may:

```text
remain local

propagate regionally

or

eventually influence
larger systems.
```

---

# 84. Player Influence Principle

The player should be:

```text
IMPORTANT
```

without becoming:

```text
THE CENTER
OF THE UNIVERSE.
```

A player may:

```text
save a town
without saving a country

repair infrastructure
without solving systemic decline

discover truth
without convincing others

change one relationship
without changing Society.
```

---

# 85. Player Inaction

If the player does nothing:

```text
THE WORLD
STILL DOES
SOMETHING.
```

Deadlines pass.

Institutions respond.

Other Actors act.

Conditions change.

---

# 86. No Preserved Opportunity

World Simulation must not preserve:

```text
EVERY CRISIS

EVERY RESOURCE

EVERY PERSON

EVERY OPPORTUNITY
```

until the player arrives.

The world continues.

---

# 87. Randomness

Randomness may influence:

```text
timing

weather

minor failure

severity

location

secondary consequence.
```

But:

```text
RANDOMNESS
MUST NOT
REPLACE CAUSALITY.
```

---

# 88. No Random Drama

Do not create:

```text
random infrastructure collapse

random war

random mass death

random riots

random Faction attack
```

solely to create tension.

Major World Events require supporting conditions.

---

# 89. Emergence

The World Simulation succeeds when:

```text
MULTIPLE
SYSTEM CONDITIONS

INTERACT

TO PRODUCE
UNSCRIPTED
BUT EXPLAINABLE
OUTCOMES.
```

---

# 90. Emergent Consequence

Example:

```text
Supply:
Constrained

Communications:
Unreliable

Authority:
Weak

Population Perception:
Shortage imminent

        ↓

stockpiling

uneven distribution

local shortages

informal trade

migration pressure.
```

No single variable caused the outcome.

The wider system did.

---

# 91. Simulation Update Model

A conceptual update cycle may be:

```text
CURRENT STATE
        ↓
TIME ADVANCES
        ↓
ACTIVE PRESSURES
        ↓
DEPENDENCIES
        ↓
EXTERNAL EVENTS
        ↓
ACTOR / INSTITUTION
RESPONSES
        ↓
ACTION RESOLUTION
        ↓
PRIMARY CONSEQUENCES
        ↓
CROSS-SYSTEM
PROPAGATION
        ↓
RECOVERY /
DEGRADATION /
ADAPTATION
        ↓
UPDATED STATE
        ↓
NEW EVENTS /
NEW PRESSURES.
```

The exact implementation may evolve.

The causal logic should remain understandable.

---

# 92. Event-Driven Simulation

Not every domain must be continuously recalculated.

World Simulation may update when:

```text
event occurs

time threshold reached

pressure changes

Actor acts

dependency changes

resource threshold is crossed

deadline arrives

resolution increases.
```

---

# 93. Continuous Processes

Some processes may require time advancement.

Examples:

```text
weather

resource consumption

degradation

repair

travel

environmental change.
```

These may be simulated through:

```text
time-based processes

or

compressed interval updates.
```

---

# 94. Hybrid Simulation

The preferred conceptual model is:

```text
EVENT-DRIVEN
SIMULATION

+

TIME-BASED
PROCESSES

+

ADAPTIVE
RESOLUTION.
```

---

# 95. Simulation Clock

World Simulation should operate against a shared simulation time.

State changes should be able to answer:

```text
WHEN WAS
THIS TRUE?

WHEN DID
IT CHANGE?
```

---

# 96. Causal Order

Order matters.

```text
BRIDGE COLLAPSES
THEN CONVOY ARRIVES
```

is different from:

```text
CONVOY CROSSES
THEN BRIDGE COLLAPSES.
```

Simulation history must preserve causal order.

---

# 97. Derived State

Some useful state may be derived.

Example:

```text
REGIONAL ACCESSIBILITY
```

may derive from:

```text
road condition

weather

fuel

security

transport availability.
```

Derived state must not become an independent competing authority.

---

# 98. Contradictions

If state conflicts appear:

```text
DO NOT
SILENTLY SELECT
THE CONVENIENT
ANSWER.
```

Check:

```text
owner

timestamp

event order

dependency

derived state

stale state.
```

---

# 99. Explainability

Major World outcomes should be explainable.

Ask:

```text
WHAT CHANGED?

WHY?

WHAT PRESSURE
EXISTED?

WHAT DEPENDENCIES
MATTERED?

WHO ACTED?

WHAT RESOURCES
EXISTED?

WHAT FAILED?

WHAT RECOVERED?

WHAT OTHER
SYSTEMS
WERE AFFECTED?
```

---

# 100. World Simulation Invariants

## WORLD-INV-001 — The World Continues Without the Player

Player absence does not pause external reality.

## WORLD-INV-002 — Regions May Diverge

No universal regional condition is required.

## WORLD-INV-003 — Systems Are Interdependent

Major external systems influence one another.

## WORLD-INV-004 — Degradation Requires Cause

Systems do not fail because narrative needs failure.

## WORLD-INV-005 — Recovery Is Possible

Negative state does not imply inevitable decline.

## WORLD-INV-006 — World Truth and Perception Are Separate

Population and Character belief may differ from reality.

## WORLD-INV-007 — Information Requires Transmission

World events do not become universally known automatically.

## WORLD-INV-008 — Human Response Matters

Human action may improve or worsen external conditions.

## WORLD-INV-009 — Characters Retain Agency

World Simulation does not dictate individual decisions.

## WORLD-INV-010 — Society Is Not World Simulation

World conditions and collective social organization remain distinct.

## WORLD-INV-011 — Action Attempt and Outcome Are Separate

Actors try.

The world resolves.

## WORLD-INV-012 — Capability Does Not Guarantee Success

Actual external conditions remain relevant.

## WORLD-INV-013 — Time Is Causally Meaningful

World conditions continue evolving.

## WORLD-INV-014 — Resolution Changes Detail, Not Reality

Distant regions do not cease existing.

## WORLD-INV-015 — Persistent Consequences Remain

Recovery does not erase history.

## WORLD-INV-016 — Randomness Does Not Replace Causality

Random events remain bounded by World state.

## WORLD-INV-017 — Narrative Is Downstream

World state is not rewritten for presentation convenience.

## WORLD-INV-018 — Aurora Is an Actor, Not the Simulation Engine

Her actions require causal mechanisms.

## WORLD-INV-019 — Player Influence Is Bounded

Local action does not automatically produce global consequence.

## WORLD-INV-020 — Major Outcomes Must Be Explainable

Significant World changes require traceable causes.

---

# 101. Development Locks

Future World Simulation development must not introduce:

```text
PLAYER-CENTRIC
WORLD ACTIVATION

WORLD FREEZE
WHEN UNOBSERVED

UNIVERSAL
COLLAPSE TIMER

SCRIPTED
REGIONAL FAILURE

AUTOMATIC
DOWNWARD SPIRAL

GLOBAL
WORLD STATE
APPLIED IDENTICALLY
EVERYWHERE

INSTANT
INFORMATION

OMNISCIENT
CHARACTERS

SOCIAL
HIVE MIND

ACTION ATTEMPT
EQUALS SUCCESS

CAPABILITY
EQUALS SUCCESS

SOCIAL SKILL
MIND CONTROL

LEVEL-SCALED
WORLD CONDITIONS

LEVEL-SCALED
ENEMIES

RANDOM DRAMA
WITHOUT CAUSE

NARRATIVE-FORCED
WORLD EVENTS

AI-INVENTED
WORLD TRUTH

AURORA
AS MAGIC
STATE COMMAND

RECOVERY
ERASING HISTORY

COMPRESSION
ERASING CONSEQUENCE.
```

---

# 102. Directory Role

`World_Simulation/` should contain systems responsible for external World state.

The current repository may contain files such as:

```text
World_State.md

Regional_State.md

Infrastructure_State.md

Information_State.md

Authority_State.md

Population_State.md

Escalation_and_Recovery.md
```

or later equivalents.

The exact file set should be validated against the repository before treating this list as canonical.

Do not create files solely because an older architecture proposed them.

---

# 103. File Creation Rule

Before adding a new World Simulation file, ask:

```text
WHAT EXTERNAL
STATE DOMAIN
DOES IT OWN?

IS THAT DOMAIN
ALREADY OWNED?

DOES IT REALLY
BELONG TO
WORLD SIMULATION?

OR

DOES IT BELONG
TO SOCIETY,
FACTIONS,
CHARACTERS,
LIFE,
RELATIONSHIPS
OR NARRATIVE?
```

---

# 104. Relationship to Simulation Architecture

The governing architecture is:

```text
Canon/Systems/
Simulation_Architecture.md
```

That document defines:

```text
cross-system ownership

Actor interaction

Action Attempt

Action Resolution

consequence propagation

time

simulation resolution

Narrative boundary

AI boundary.
```

This README defines:

```text
WORLD SIMULATION'S
ROLE INSIDE
THAT ARCHITECTURE.
```

---

# 105. Relationship to Characters

The governing Character entry point is:

```text
Canon/Systems/Characters/
README.md
```

Characters own:

```text
human state

human perception

human goals

human decisions

human capability.
```

World Simulation owns:

```text
THE EXTERNAL
WORLD THOSE
CHARACTERS ACT IN.
```

---

# 106. Relationship to Society

Society owns:

```text
COLLECTIVE
HUMAN ORGANIZATION.
```

World Simulation provides:

```text
THE CONDITIONS
TO WHICH SOCIETY
RESPONDS.
```

The two systems must exchange consequences without duplicating state.

---

# 107. Relationship to Living Campaign Engine

World Simulation produces:

```text
conditions

events

changes

consequences.
```

The Living Campaign Engine tracks:

```text
which causal chains
remain active

and

which may become
campaign relevant.
```

---

# 108. Relationship to Narrative

World Simulation answers:

```text
WHAT HAPPENED?
```

Narrative answers:

```text
HOW DOES
THE PLAYER
EXPERIENCE
WHAT HAPPENED?
```

Narrative may not rewrite the answer to the first question.

---

# 109. Current Architecture Status

The World Simulation architecture should now be considered:

```text
ARCHITECTURALLY
DEFINED

BUT

INDIVIDUAL
WORLD STATE FILES

REQUIRE
REPOSITORY AUDIT.
```

The next step should not automatically follow the old development order.

Instead:

```text
INSPECT
CURRENT FILES

↓

IDENTIFY
OUTDATED OWNERSHIP

↓

KEEP
REBUILD
MERGE
OR RETIRE

↓

ONLY THEN
CREATE
MISSING SYSTEMS.
```

---

# 110. World Simulation Audit Questions

For every existing World Simulation file, ask:

```text
WHAT STATE
DOES THIS FILE OWN?

IS THAT STATE
EXTERNAL WORLD TRUTH?

DOES ANOTHER
SYSTEM ALREADY
OWN IT?

DOES THE FILE
DUPLICATE
SIMULATION_ARCHITECTURE.md?

DOES IT DUPLICATE
SOCIETY?

DOES IT DUPLICATE
CHARACTERS?

DOES IT ASSUME
PLAYER-CENTRIC
SIMULATION?

DOES IT ASSUME
INEVITABLE COLLAPSE?

DOES IT SUPPORT
RECOVERY?

DOES IT SUPPORT
REGIONAL DIFFERENCE?

DOES IT SUPPORT
LOWER RESOLUTION?

DOES IT PRESERVE
TIME AND HISTORY?

CAN ITS OUTPUT
PROPAGATE
CAUSALLY?
```

---

# 111. Guiding Question

Every World Simulation mechanic should ultimately answer:

```text
IF THE PLAYER
DID NOTHING,

WHAT WOULD
THIS PART
OF THE WORLD
DO NEXT?

AND

WHY?
```

If the system cannot answer that question, it is not yet functioning as a living World Simulation.

---

# 112. World Simulation North Star

The World Simulation succeeds when the player can:

```text
LEAVE A REGION

RETURN LATER

AND DISCOVER

INFRASTRUCTURE
HAS CHANGED

RESOURCES
HAVE MOVED

PEOPLE
HAVE ADAPTED

ROUTES
HAVE OPENED
OR CLOSED

INSTITUTIONS
HAVE RECOVERED
OR FAILED

SOME PROBLEMS
HAVE DISAPPEARED

OTHERS HAVE
BECOME WORSE

AND

THE RESULT
MAKES SENSE

BECAUSE OF

WHAT ACTUALLY
HAPPENED
WHILE THEY
WERE GONE.
```

---

# 113. Final Principle

Project Ascension does not require a world where everything is simulated at maximum detail.

It requires a world where:

```text
EVERY IMPORTANT
CHANGE

HAS

A CAUSE

A PLACE

A TIME

A CONSEQUENCE

AND

A HISTORY.
```

The central World Simulation principle is:

> **The world does not change because the player needs something to happen. It changes because systems, people, resources, institutions, environments and time interact — whether the player is watching or not.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-09-01 | Rebuilt the World Simulation README as the canonical entry point for external persistent world simulation. Preserved the foundational principles of independent world continuity, regional divergence, interdependent systems, state versus pressure, resilience, recovery, perceived versus actual conditions, information delay, anti-script simulation and persistent consequences. Updated ownership boundaries against Characters, Society, Factions, Life, Living Campaign Engine and Narrative; integrated the new Simulation Architecture; established Action Resolution as the boundary where Actor capability meets World reality; added adaptive resolution, time, persistence, cross-system consequence propagation, Aurora boundaries, canonical invariants and development locks; removed the obsolete fixed development plan and pending-file status model. |