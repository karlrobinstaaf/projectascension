# PROJECT ASCENSION
# Population State System

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Population State System |
| Location | `Canon/Systems/World_Simulation/Population_State.md` |
| Version | 1.0 |
| Status | Canonical Architecture |
| Category | World Simulation / Population |
| Owner | World Simulation |
| Last Updated | 2026-09-01 |
| Primary Function | Define the authoritative demographic, mobility, workforce, household-capacity and aggregate population-pattern state through which populations affect and are affected by the simulated world without treating populations as single Actors |

---

# 1. Purpose

The Population State System defines the large-scale human presence inside World Simulation.

It answers:

> **How many people are present, where are they, how are they distributed, how are they moving, what demographic pressures exist, what household and workforce capacity remains, and what broad observable population patterns are emerging?**

Population State is an aggregate simulation layer.

It exists because Project Ascension cannot simulate every human being at high resolution at all times.

Instead:

```text
INDIVIDUAL CHARACTERS
+
HOUSEHOLDS
+
COMMUNITIES
+
INSTITUTIONS
+
POPULATION GROUPS
↓
AGGREGATE
POPULATION STATE.
```

Population State preserves large-scale human consequences without turning populations into collective minds.

---

# 2. Core Principle

A population is not one Actor.

Canonical rule:

```text
POPULATION
≠
ONE PERSON

POPULATION
≠
ONE MIND

POPULATION
≠
ONE EMOTION

POPULATION
≠
ONE DECISION.
```

The system must never assume:

```text
EVENT
↓
EVERYONE REACTS
THE SAME WAY.
```

Instead:

```text
SAME EVENT
+
DIFFERENT PEOPLE
+
DIFFERENT INFORMATION
+
DIFFERENT RESOURCES
+
DIFFERENT RESPONSIBILITIES
+
DIFFERENT RELATIONSHIPS
+
DIFFERENT VALUES
+
DIFFERENT MOBILITY
↓
DIFFERENT RESPONSES.
```

Population State records the aggregate consequences of those differences.

---

# 3. Population State Is Aggregate

Population State represents broad patterns.

It does not replace Character simulation.

Individual human state belongs primarily to:

```text
Characters

Humanity

Relationships

Life

Society.
```

Population State provides the large-scale external human context in which those systems operate.

---

# 4. Ownership Boundary

Population State owns aggregate external population state such as:

```text
population size

population density

population distribution

population trend

demographic composition

household distribution

household buffer distribution

workforce participation

essential workforce availability

mobility capacity

migration pressure

migration flow

displacement

hosting pressure

demographic pressure

population concentration

resource-demand effects

aggregate observable behavior patterns

population adaptation indicators

population-system recovery capacity.
```

---

# 5. What Population State Does Not Own

Population State does not own:

```text
individual fear

individual Psychology

Character motivation

Character goals

Character decisions

Character beliefs

Character knowledge

Trust

social cohesion

social norms

collective identity

institutional legitimacy

Culture

Faction goals

Authority decisions

Narrative meaning.
```

These belong to their authoritative systems.

---

# 6. Population State vs Society

This boundary is critical.

```text
POPULATION STATE
=
WHO IS PRESENT,
WHERE,
IN WHAT NUMBERS,
WITH WHAT
MATERIAL CAPACITY,
MOVEMENT
AND AGGREGATE PATTERNS.


SOCIETY
=
HOW PEOPLE
ORGANIZE,
COOPERATE,
FORM NORMS,
BUILD TRUST,
CREATE INSTITUTIONS
AND UNDERSTAND
COLLECTIVE LIFE.
```

Examples:

```text
Population State:
25,000 displaced people
arrive in Region A.

Society:
Host-community tensions,
mutual aid,
new norms,
political response.
```

Population owns the demographic movement.

Society owns the social transformation.

---

# 7. Population State vs Characters

Population State must not decide:

```text
WHO LEAVES

WHO STAYS

WHO PANICS

WHO HELPS

WHO PROTESTS

WHO STOCKPILES.
```

Those are Actor decisions at individual or organized-group level.

Population State may represent the aggregate result after those decisions occur.

Example:

```text
12% of households
increase food reserves.
```

This is valid aggregate state.

It does not mean:

```text
THE POPULATION
DECIDED TO STOCKPILE.
```

---

# 8. Population State vs Human Psychology

Human Psychology owns:

```text
fear

stress

grief

confidence

fatigue

hope

anxiety

trauma response.
```

Population State may reference externally provided aggregate patterns where needed.

But it must not become the authority for psychological state.

---

# 9. Population State vs Trust

Trust belongs elsewhere.

Examples:

```text
General Social Trust
→ Humanity / Society

Institutional Trust
→ Society / Actor cognition

Person-to-Person Trust
→ Relationships.
```

Population State may consume trust-related effects.

It does not own them.

---

# 10. Population State vs Authority

Authority may:

```text
order evacuation

restrict movement

ration resources

close regions

open shelters.
```

Population State records resulting demographic and movement consequences.

It does not create the authority decision.

---

# 11. Population State vs Supply

Supply owns:

```text
what resources exist

how much exists

where they exist

how much is available.
```

Population State provides:

```text
how many people
require those resources

where demand is located

how population movement
changes demand.
```

---

# 12. Population State vs Infrastructure

Infrastructure owns:

```text
transport networks

housing infrastructure

water systems

power

healthcare facilities

physical communication systems.
```

Population State provides:

```text
population demand

population distribution

workforce availability

movement requirements.
```

---

# 13. Population State vs Security

Security State owns:

```text
threat

violence

crime

organized conflict

security capability

route danger.
```

Population State may represent:

```text
population exposure

displacement

movement

civilian concentration

evacuation flows.
```

---

# 14. Population State vs Information

Information State owns:

```text
reports

rumors

information availability

verification

information horizon.
```

Population State does not own:

```text
WHAT PEOPLE
BELIEVE.
```

Observed information may influence Actors.

Their resulting actions may later produce aggregate Population State changes.

---

# 15. Population Hierarchy

Population State may operate at:

```text
GLOBAL

NATIONAL

REGIONAL

LOCAL

COMMUNITY

GROUP.
```

The preferred operational level is normally:

```text
REGIONAL.
```

Higher or lower detail should be used when causally necessary.

---

# 16. Population Scale

Population Scale represents the number of people inside the relevant simulation area.

It may be represented as:

```text
EXACT ESTIMATE
```

or broadly:

```text
VERY SMALL

SMALL

MODERATE

LARGE

VERY LARGE.
```

Exact values should be used only when useful.

---

# 17. Population Estimate

Population totals may sometimes be estimates rather than exact values.

Important distinction:

```text
ACTUAL SIMULATION
POPULATION

≠

INSTITUTIONAL
POPULATION ESTIMATE.
```

If the simulation itself requires exact population state, it may maintain it internally.

Observer uncertainty belongs to Information State.

---

# 18. Population Density

Population Density describes how concentrated people are geographically.

Conceptual values:

```text
VERY LOW

LOW

MODERATE

HIGH

VERY HIGH.
```

Density may influence:

```text
infrastructure demand

housing pressure

transport demand

evacuation complexity

resource demand

disease exposure

service concentration.
```

Density does not dictate social behavior.

---

# 19. Population Distribution

Population distribution may distinguish:

```text
Urban

Suburban

Rural

Remote

Temporary Settlement

Institutional Population

Displaced Settlement

Transit Population.
```

This matters because equal population totals can create very different world conditions.

---

# 20. Population Trend

Population Trend describes directional population change.

Conceptual values:

```text
RAPIDLY GROWING

GROWING

STABLE

DECLINING

RAPIDLY DECLINING

VOLATILE.
```

Possible causes include:

```text
births

deaths

migration

displacement

evacuation

return migration

economic change

environmental conditions

security

resource conditions.
```

---

# 21. Demographic Composition

Population State may represent broad demographic structure where causally relevant.

Examples:

```text
Age Distribution

Household Structure

Dependency Ratio

Working-Age Share

Children

Older Population

Displaced Population

Specialist Workforce Share.
```

Avoid unnecessary demographic detail that does not affect simulation.

---

# 22. Dependency Ratio

Dependency Ratio represents the relationship between:

```text
people requiring
substantial support

and

people currently capable
of providing labor,
care or economic support.
```

This may change through:

```text
aging

migration

casualties

workforce loss

displacement.
```

---

# 23. Population Groups

Population Groups may be created when meaningful differences matter.

Examples:

```text
Urban Residents

Rural Residents

Infrastructure Workers

Healthcare Workers

Emergency Personnel

Displaced Population

Recent Migrants

Older Residents

Families With Children

Students.
```

---

# 24. Population Group Rule

Groups should exist only when they possess meaningfully different:

```text
location

resource access

exposure

mobility

workforce role

demographic characteristics

housing conditions

system dependencies.
```

Do not create groups merely to increase simulation detail.

---

# 25. Group Identity Is Not Personality

Population Groups must not receive personality traits such as:

```text
fearful

loyal

aggressive

trusting.
```

Those are human and social properties.

A group may instead have:

```text
Lower Mobility

Higher Exposure

Higher Fuel Dependency

Higher Medical Dependency.
```

These are legitimate population conditions.

---

# 26. Household Structure

Households are important because much human adaptation occurs at household scale.

Population State may represent:

```text
Average Household Size

Single-Person Households

Multi-Generational Households

Households With Children

Households With Care Dependents.
```

Detailed family relationships belong to Family and Character systems.

---

# 27. Household Buffers

Households may possess material buffers.

Examples:

```text
food

water

medicine

cash

fuel

battery power

transportation access.
```

Population State may represent the distribution of these buffers.

The resource itself remains owned by Supply or relevant systems.

---

# 28. Preparedness Boundary

Preparedness should be reframed materially.

Population State may own:

```text
HOUSEHOLD
MATERIAL PREPAREDNESS
```

such as:

```text
days of food

water storage

backup power access

vehicle access

emergency supplies.
```

It should not own psychological preparedness, confidence or willingness.

---

# 29. Preparedness Distribution

Preparedness should rarely be uniform.

Example:

```text
Regional Household
Material Preparedness:
MODERATE


Rural Households:
HIGH


Urban Apartments:
LOW


High-Income Suburban:
HIGH


Displaced Households:
MINIMAL.
```

This may create significantly different consequences during disruption.

---

# 30. Buffer Depletion

Household buffers decline with time.

Conceptually:

```text
DISRUPTION
↓
HOUSEHOLD BUFFER
↓
BUFFER DEPLETION
↓
NEW MATERIAL PRESSURE
↓
ACTOR RESPONSE.
```

Population State owns the aggregate buffer consequence.

Characters and Society own human response.

---

# 31. Workforce Participation

Workforce Participation represents how much of the population capable of working remains engaged in economically or institutionally necessary activity.

Conceptual values:

```text
NORMAL

HIGH

MODERATE

LOW

CRITICAL.
```

This is an observable aggregate condition.

---

# 32. Workforce Participation Is Not Motivation

Avoid:

```text
Workforce Participation:
LOW

therefore

people are afraid.
```

Low participation may result from:

```text
transport failure

illness

family responsibilities

migration

service shutdown

housing disruption

unpaid work

security conditions

infrastructure loss.
```

The causal explanation must come from actual systems.

---

# 33. Essential Workforce

Some professions have disproportionate systemic importance.

Examples include:

```text
Power Technicians

Water Operators

Healthcare Workers

Transport Workers

Logistics Workers

Telecommunication Engineers

Emergency Personnel

Fuel Workers.
```

Population State may track their broad availability.

---

# 34. Essential Workforce Availability

Conceptual values:

```text
ADEQUATE

STRAINED

LOW

CRITICAL

INSUFFICIENT.
```

This represents population-scale human availability.

Detailed individual capability belongs to Characters and Expertise.

---

# 35. Workforce Specialization

Population totals alone do not determine system capability.

Example:

```text
Population:
LARGE

Qualified Grid Engineers:
CRITICAL.
```

The region may contain many people and still lack one essential capability.

---

# 36. Workforce Movement

Migration may disproportionately affect:

```text
specialists

young workers

wealthier households

mobile professionals

essential personnel.
```

Therefore population decline may alter capability faster than total population numbers suggest.

---

# 37. Mobility

Population Mobility represents practical ability to move.

It depends on:

```text
transportation

fuel

road access

health

finances

security

authority restrictions

vehicle access.
```

Conceptual values:

```text
HIGH

FUNCTIONAL

LIMITED

RESTRICTED

MINIMAL.
```

---

# 38. Mobility Is Not Migration

Canonical distinction:

```text
MOBILITY
=
CAN PEOPLE MOVE?


MIGRATION
=
ARE PEOPLE
ACTUALLY MOVING
RESIDENCE OR REGION?
```

Example:

```text
Mobility:
HIGH

Migration:
LOW.
```

People can leave.

They are not leaving.

---

# 39. Migration Pressure

Migration Pressure represents material and situational conditions that make relocation increasingly relevant.

Possible sources include:

```text
resource shortage

housing loss

infrastructure failure

security pressure

employment collapse

environmental conditions

family separation

service loss.
```

Conceptual values:

```text
LOW

MODERATE

HIGH

SEVERE

EXTREME.
```

---

# 40. Migration Pressure Does Not Determine Migration

High migration pressure may coexist with low movement because:

```text
mobility is low

family ties remain

housing unavailable elsewhere

destination uncertain

property ties exist

work responsibilities remain

Actors choose to stay.
```

Population State records pressure and resulting aggregate flow separately.

---

# 41. Migration State

Possible aggregate migration states:

```text
STABLE

INBOUND

OUTBOUND

TRANSIT

MIXED

MASS DISPLACEMENT

RETURNING.
```

---

# 42. Inbound Migration

Incoming population may increase:

```text
workforce

skills

trade

demographic diversity

institutional capacity.
```

It may also increase:

```text
housing demand

food demand

water demand

healthcare demand

transport demand

service demand.
```

No universal positive or negative outcome is assumed.

---

# 43. Outbound Migration

Outbound migration may reduce:

```text
demand

housing pressure

resource consumption.
```

It may also reduce:

```text
workforce

specialists

tax base

institutional capacity

community continuity.
```

Migration is not simply pressure relief.

---

# 44. Selective Migration

Migration is rarely demographically neutral.

Those most able to move may differ systematically from those who remain.

Possible consequences include loss of:

```text
technical Expertise

working-age population

wealth

institutional leadership

medical personnel.
```

Or the reverse may occur where essential workers remain because their role becomes more important.

---

# 45. Displacement

Displacement is distinct from planned migration.

Displaced populations may experience:

```text
loss of housing

reduced resources

temporary settlement

network disruption

limited transportation

high dependency on host systems.
```

Population State owns the demographic condition.

Life and Character systems own the human experience.

---

# 46. Displacement State

A displaced population group may include:

```text
Origin

Current Location

Population Size

Housing Status

Mobility

Resource Dependency

Workforce Composition

Return Potential.
```

Do not embed Trust, Psychology or Relationship state directly.

---

# 47. Hosting Capacity

Hosting Capacity represents how many additional people a region can physically and materially support without severe system degradation.

It may depend on:

```text
housing

food

water

healthcare

infrastructure

employment

transportation

administrative capacity.
```

Conceptual values:

```text
HIGH

MODERATE

LOW

CRITICAL.
```

---

# 48. Hosting Capacity Is Derived

Hosting Capacity should be derived from underlying systems.

It is not one independent magic variable.

Conceptually:

```text
HOUSING
+
SUPPLY
+
INFRASTRUCTURE
+
SERVICES
+
WORKFORCE
+
AUTHORITY CAPACITY
↓
HOSTING CAPACITY.
```

---

# 49. Demographic Pressure

Demographic Pressure represents structural pressure caused by population composition or movement.

Possible causes include:

```text
rapid growth

rapid decline

aging

high dependency ratio

mass displacement

specialist loss

housing concentration

workforce shortage.
```

Conceptual values:

```text
LOW

MODERATE

HIGH

SEVERE.
```

---

# 50. Population Concentration

Population concentration may become strategically important during crisis.

Examples:

```text
dense evacuation corridor

large temporary settlement

crowded urban center

displaced camp

hospital catchment population.
```

Concentration may alter demand and exposure.

---

# 51. Aggregate Observable Behavior

Population State may represent observable broad behavioral patterns when they have measurable world consequences.

Examples:

```text
Consumption Increase

Consumption Reduction

Workforce Absence

Travel Reduction

Outward Movement

Resource Retention

Volunteer Participation

Return Migration.
```

These are patterns.

Not collective decisions.

---

# 52. Behavior Pattern Boundary

Prefer:

```text
Household Fuel Purchasing:
+30%
```

over:

```text
Population Fear:
HIGH.
```

Prefer:

```text
Outbound Migration:
RISING
```

over:

```text
Population Wants To Leave.
```

Population State should represent what populations are doing at aggregate scale.

Not why every person is doing it.

---

# 53. Resource Behavior

Resource behavior should therefore be reframed as observable aggregate consumption patterns.

Possible patterns include:

```text
NORMAL CONSUMPTION

REDUCED CONSUMPTION

ELEVATED PURCHASING

RESOURCE RETENTION

HOUSEHOLD STOCK INCREASE

FORMAL RATIONING EFFECT

INFORMAL DISTRIBUTION.
```

---

# 54. Stockpiling Boundary

Stockpiling is not one population mental state.

Population State may record:

```text
HOUSEHOLD INVENTORY
INCREASING
```

or:

```text
RETAIL DEMAND
SPIKE.
```

The underlying reasons belong to Characters, Society and Information.

---

# 55. Conservation Boundary

Population State may record:

```text
REGIONAL ELECTRICITY
DEMAND:
-18%

HOUSEHOLD FUEL
CONSUMPTION:
DECLINING.
```

Whether conservation was:

```text
voluntary

authority-driven

necessity-driven

culturally normalized
```

belongs to other systems.

---

# 56. Rationing Boundary

Population State does not decide rationing.

Authority or relevant Actors may establish it.

Population State records population-level effects such as:

```text
consumption reduction

distribution change

household access change.
```

---

# 57. Public Order Boundary

Public Order should not remain a primary Population State variable.

Security State owns external order and threat conditions.

Society owns social organization.

Population State may record observable events such as:

```text
large demonstration

mass gathering

strike participation

population displacement

crowd concentration.
```

It should not assign a broad psychological Public Order state.

---

# 58. Protest Boundary

Protest is organized human action.

It may be represented through:

```text
Society

Factions

Characters

Narrative

Security consequences.
```

Population State may record participation scale.

Example:

```text
Demonstration Participation:
18,000.
```

It does not own the political motive.

---

# 59. Unrest Pressure Boundary

The old concept of universal Unrest Pressure should not remain a core Population State variable.

Conditions contributing to unrest already exist across:

```text
Society

Authority

Security

Supply

Information

Characters.
```

A derived risk diagnostic may be used if implementation requires it.

It must not become an authoritative driver of behavior.

---

# 60. Crime Boundary

Crime belongs primarily to:

```text
Security

Characters

Factions

Society.
```

Population State may provide demographic context such as:

```text
unemployment

population concentration

mobility

displacement.
```

It must not generate crime mechanically.

---

# 61. Informal Economy Boundary

Informal trade, barter and local exchange belong primarily to:

```text
Society

Economy if later created

Factions

Characters.
```

Population State may represent:

```text
participation scale

population dependence

market reach.
```

---

# 62. Population Adaptation

Population adaptation should be represented primarily through persistent observable changes in material behavior and demographic organization.

Examples:

```text
higher household reserves

different commuting patterns

new workforce distribution

local production participation

lower long-distance mobility

changed settlement distribution

greater household backup capacity.
```

---

# 63. Adaptation Is Not One Score

Avoid:

```text
Adaptation Capacity:
HIGH
```

as a universal explanatory variable.

Prefer explicit adaptive state:

```text
Household Water Storage:
INCREASED

Backup Power Access:
INCREASED

Local Food Production Participation:
INCREASED

Long-Distance Commuting:
DECREASED.
```

A derived summary may exist for diagnostics.

It must not replace causal state.

---

# 64. Learned Material Resilience

Repeated disruption may change population material behavior.

Example:

```text
YEAR 1

72-hour blackout

Household Backup Capacity:
LOW.


YEAR 5

72-hour blackout

Household Backup Capacity:
HIGH.
```

The same infrastructure event may now create different consequences.

---

# 65. Behavioral Memory Boundary

Population State should not own:

```text
collective Memory
```

as though a population possesses one mind.

Instead:

```text
SYSTEMIC HISTORY
+
SOCIETY
+
CULTURE
+
CHARACTER MEMORY
```

may produce persistent aggregate behavior.

Population State records the resulting structural change.

---

# 66. Preparedness History

Example:

```text
Past Event:
Three-week fuel shortage.

Systemic Consequence:

Household Fuel Storage:
Higher

Local Transit Use:
Higher

Average Vehicle Fuel Reserve:
Higher.
```

The historical event belongs to World/Systemic History.

The material population adaptation belongs here.

---

# 67. Crisis Fatigue Boundary

Crisis fatigue is psychological and social.

It should not be owned by Population State.

Possible population-level consequences may be recorded:

```text
Warning Response Rate:
DECLINING

Evacuation Participation:
DECLINING.
```

Why those patterns changed belongs to Psychology, Society and Information.

---

# 68. Social Proof Boundary

The fact that people observe one another belongs to human behavior and information systems.

Population State may record resulting aggregates.

Example:

```text
Outbound Movement:
INCREASING RAPIDLY.
```

Information State may then represent that visible behavior as evidence observed by others.

---

# 69. Population Feedback

Population state may change the world.

Example:

```text
OUTBOUND MIGRATION
↓
WORKFORCE DECLINE
↓
INFRASTRUCTURE
REPAIR CAPACITY FALLS
↓
SERVICE DECLINES
↓
MORE OUTBOUND
MIGRATION PRESSURE.
```

This is a legitimate feedback loop.

---

# 70. Positive Population Feedback

Positive loops must also be possible.

Example:

```text
INBOUND SPECIALISTS
↓
REPAIR CAPACITY
INCREASES
↓
INFRASTRUCTURE
IMPROVES
↓
REGION BECOMES
MORE ATTRACTIVE
↓
ADDITIONAL
INBOUND MIGRATION.
```

---

# 71. Workforce Feedback

Example:

```text
TRANSPORT
DEGRADED
↓
COMMUTING CAPACITY
DECLINES
↓
WORKFORCE
PARTICIPATION FALLS
↓
INFRASTRUCTURE STAFFING
DECLINES
↓
SERVICE DEGRADES.
```

Each step must be causally owned by the correct system.

---

# 72. Supply Feedback

Example:

```text
Household Purchasing:
INCREASES
↓
Retail Inventory:
DECLINES
↓
Local Availability:
CONSTRAINED
↓
Population Demand Pattern:
CHANGES FURTHER.
```

Population does not directly rewrite Supply.

Behavior changes demand.

Supply recalculates availability.

---

# 73. Authority Feedback

Example:

```text
AUTHORITY:
Evacuation Order

↓

Population Movement:
INCREASES

↓

Road Demand:
INCREASES

↓

Transport Capacity:
SATURATED

↓

Evacuation Throughput:
DECLINES.
```

Authority decision and population response remain distinct.

---

# 74. Information Feedback

Population behavior may itself become observable information.

Example:

```text
VISIBLE QUEUES
↓
INFORMATION OBJECT
↓
OTHER ACTORS
REASSESS CONDITIONS
↓
NEW DECISIONS.
```

The queue is Population State.

Its interpretation belongs elsewhere.

---

# 75. Regional Population Differences

Two neighboring regions may respond differently to the same material event.

This may result from:

```text
different population composition

different household buffers

different workforce structure

different mobility

different institutions

different Society state

different Information environments

different histories.
```

Population State should preserve those structural differences.

---

# 76. Population Fragmentation Boundary

The old concept of Population Fragmentation should be split.

Possible underlying states include:

```text
GEOGRAPHIC DISPERSION
→ Population State

INFORMATION FRAGMENTATION
→ Information State

SOCIAL FRAGMENTATION
→ Society

POLITICAL FRAGMENTATION
→ Authority / Society

ECONOMIC FRAGMENTATION
→ Society / future Economy.
```

Population State should not combine them into one variable.

---

# 77. Geographic Population Fragmentation

Population State may legitimately represent:

```text
population dispersed

settlements isolated

communities geographically separated

transport-linked population networks broken.
```

This is demographic and spatial.

---

# 78. Community Formation Boundary

New communities and institutions may emerge after disruption.

Population State may record:

```text
new settlement

population size

location

growth

demographic composition.
```

Society owns:

```text
norms

governance culture

social cohesion

identity.
```

Authority owns formal governance state where relevant.

---

# 79. Leadership Boundary

Leadership belongs to Characters, Factions, Society and Authority.

Population State does not own:

```text
leadership effectiveness

leader Trust

leader legitimacy.
```

It may record demographic reach or participation.

---

# 80. Population and Regional State

`Regional_State.md` provides:

```text
geography

regional structure

major settlements

dependencies

connections.
```

Population State provides:

```text
who lives there

how many

where they are

how they move

what demographic pressure exists.
```

---

# 81. Population and World State

`World_State.md` provides:

```text
global and regional
external context.
```

Population State is one authoritative domain contributing human-scale demographic reality to that World State.

---

# 82. Population and Infrastructure

Population affects infrastructure through:

```text
demand

workforce

movement

usage

settlement distribution.
```

Infrastructure affects population through:

```text
mobility

housing

water

power

healthcare access

communication

transport capacity.
```

Neither owns the other.

---

# 83. Population and Supply

Population influences:

```text
demand

consumption

resource location

household storage.
```

Supply determines:

```text
resource availability

inventory

production

scarcity.
```

---

# 84. Population and Security

Security may influence:

```text
migration

displacement

mobility

population concentration.
```

Population may influence Security through:

```text
crowd concentration

movement

resource demand

civilian exposure.
```

Behavioral intent remains outside Population State.

---

# 85. Population and Authority

Authority actions may change:

```text
mobility

settlement

resource access

evacuation

service availability.
```

Population changes may affect:

```text
administrative demand

territorial reach

service demand

workforce availability.
```

---

# 86. Population and Society

Population provides:

```text
the people

their distribution

their demographic structure

their movement.
```

Society provides:

```text
the social organization
that emerges among them.
```

This boundary is mandatory.

---

# 87. Population and Life

Demographic events may create individual Life Events.

Example:

```text
POPULATION STATE:

Mass displacement
from Region A.


CHARACTER:

Family loses home
and relocates.


LIFE EVENT:

Forced displacement.
```

Population State owns the aggregate event.

Life owns personal biography.

---

# 88. Population and Characters

Low-resolution population may later produce persistent Characters.

Example:

```text
Population Group:
Power Technicians

↓

Specific technician
becomes narratively
or causally important

↓

Persistent Character
is created.
```

The new Character should emerge consistently from the existing Population State.

---

# 89. Character Promotion

When an aggregate population member becomes an explicit Character, the simulation should preserve:

```text
region

population group

profession context

demographic context

historical context

current world conditions.
```

Do not invent incompatible personal history.

---

# 90. Character Demotion

A Character who no longer requires high-resolution simulation may return to lower-resolution population context where appropriate.

Persistent:

```text
Life Events

Relationships

Goals

major state

history
```

must not be erased.

---

# 91. Population Events

Population events are significant demographic or aggregate behavioral changes.

Examples:

```text
mass migration begins

population returns

temporary settlement forms

workforce participation falls sharply

specialist workforce leaves

household reserves increase regionally

major evacuation occurs

displaced population relocates.
```

---

# 92. Population Event Requires Cause

Avoid:

```text
RANDOM
MASS MIGRATION.
```

Prefer:

```text
HIGH MIGRATION PRESSURE
+
MOBILITY
+
DESTINATION ACCESS
+
ACTOR DECISIONS
+
TIME
↓
OUTBOUND MIGRATION.
```

---

# 93. Population Does Not Generate Story Events

Avoid:

```text
Population State:
Needs drama
↓
Generate riot.
```

Population creates world conditions.

Story emerges downstream.

---

# 94. Population Update Model

Conceptually:

```text
CURRENT POPULATION STATE
        ↓
WORLD CONDITIONS
+
SUPPLY
+
INFRASTRUCTURE
+
SECURITY
+
AUTHORITY
+
INFORMATION
+
SOCIETY
+
ACTOR DECISIONS
+
TIME
        ↓
DEMOGRAPHIC
AND MATERIAL EFFECTS
        ↓
MOVEMENT
+
WORKFORCE
+
HOUSEHOLD STATE
+
DEMAND
+
DISTRIBUTION
        ↓
UPDATED
POPULATION STATE
        ↓
WORLD CONSEQUENCES.
```

Population State does not calculate individual psychology.

---

# 95. Time

Population dynamics operate across multiple timescales.

```text
HOURS

Evacuation movement

Workforce absence


DAYS

Household buffer depletion

Temporary displacement


WEEKS

Migration

Workforce redistribution


MONTHS

Settlement growth

Demographic shift


YEARS

Aging

Births

Long-term migration

Population decline

Population recovery.
```

---

# 96. Population Recovery

Population recovery may involve:

```text
return migration

housing stabilization

workforce restoration

household buffer rebuilding

service access improvement

demographic stabilization.
```

Recovery need not mean returning to the previous population structure.

---

# 97. Population Adaptation

A region may emerge from crisis with:

```text
lower population

different workforce

different settlement pattern

greater household preparedness

different mobility patterns

more local production participation.
```

This is valid recovery through transformation.

---

# 98. Population Recovery Capacity

If a derived Population Recovery Capacity diagnostic is retained, it should reflect material and demographic recovery potential.

Possible factors include:

```text
housing

employment

services

infrastructure

supply

security

workforce

return mobility.
```

It must not hide underlying causal state.

---

# 99. Connected World

The Connected World may commonly contain:

```text
high mobility

large metropolitan concentration

high workforce specialization

high dependence on formal infrastructure

low household material buffers

long-distance commuting

global labor mobility.
```

These are structural tendencies.

Not mandatory values.

---

# 100. Transition

The Transition may create:

```text
uneven household preparation

workforce instability

temporary displacement

regional migration

specialist shortages

changing mobility

higher household resource storage.
```

These are emergent possibilities.

---

# 101. Fractured World

The Fractured World should not consist of populations permanently trapped in emergency behavior.

Over time:

```text
DISRUPTION
↓
EXPERIMENTATION
↓
NEW MATERIAL ROUTINES
↓
NEW POPULATION PATTERNS.
```

A generation born later may consider:

```text
regional employment

limited long-distance travel

local production

household reserves
```

completely normal.

---

# 102. Reconnection

Reconnection may create:

```text
return migration

new migration

urban growth

regional workforce exchange

new demographic pressure

settlement decline

new settlement growth.
```

Reconnection changes population flows.

It does not automatically reverse earlier migration.

---

# 103. Adaptive Simulation Resolution

Population State supports:

```text
LOW

MEDIUM

HIGH.
```

Resolution changes detail.

Not whether populations exist or move.

---

# 104. Low Resolution

Low-resolution Population State may preserve:

```text
Population Size

Population Trend

Major Migration

Major Displacement

Workforce Availability

Major Demographic Pressure

Major Population Events.
```

---

# 105. Medium Resolution

Medium resolution may additionally preserve:

```text
Population Groups

Density

Household Buffer Distribution

Mobility

Migration Pressure

Essential Workforce

Hosting Capacity

Major Aggregate Behavior Patterns.
```

---

# 106. High Resolution

High resolution may include:

```text
specific population groups

local settlement populations

detailed displacement flows

workforce sectors

household buffer distributions

specific demographic dependencies

migration routes

population-event timing.
```

Individual Actor cognition still belongs outside Population State.

---

# 107. Resolution Follows Causal Relevance

A distant region may require high population resolution if:

```text
mass migration is underway

essential workforce collapse occurs

major displacement affects neighbors

strategic population movement occurs

national demographic consequences emerge.
```

Player proximity is not the sole trigger.

---

# 108. Population Compression

Not every aggregate behavior must remain permanently stored.

Preserve changes affecting:

```text
demographics

migration

settlements

workforce

household material capacity

population distribution

regional demand

systemic history.
```

Routine temporary patterns may be compressed.

---

# 109. Population Systemic History

Significant population events should become part of Systemic History.

Examples:

```text
mass evacuation

large migration wave

urban depopulation

settlement creation

population return

specialist exodus

major demographic shift.
```

Population State does not own human Memory.

---

# 110. Minimum Population State

A minimum viable Regional Population State should contain:

```text
Population Size

Population Density

Population Distribution

Population Trend

Demographic Composition

Dependency Ratio

Household Material Preparedness

Workforce Participation

Essential Workforce Availability

Mobility

Migration Pressure

Migration State

Displacement

Hosting Capacity

Demographic Pressure

Major Population Groups

Major Population Events

Trend

Causal Sources.
```

---

# 111. Northern Virginia Example

```text
POPULATION STATE

Region:
Northern Virginia

Historical Era:
WS-02 — The Transition


Population Size:
VERY LARGE

Population Density:
VERY HIGH

Population Trend:
DECLINING


DISTRIBUTION

Urban / Suburban:
DOMINANT

Temporary Displacement:
INCREASING


HOUSEHOLD STATE

Material Preparedness:
MODERATE

Household Fuel Buffer:
LOW

Household Food Buffer:
MODERATE


WORKFORCE

Workforce Participation:
MODERATE

Essential Infrastructure Workforce:
STRAINED

Healthcare Workforce:
STRAINED


MOBILITY

Mobility:
LIMITED

Migration Pressure:
HIGH

Migration State:
OUTBOUND


DEMOGRAPHIC PRESSURE

Hosting Capacity:
LOW

Dependency Pressure:
MODERATE

Trend:
VOLATILE.
```

No regional Fear, Trust or Social Cohesion score is stored here.

---

# 112. Shenandoah Valley Example

```text
POPULATION STATE

Region:
Shenandoah Valley

Historical Era:
WS-03 — The Fractured World


Population Size:
MODERATE

Population Density:
LOW

Population Trend:
STABLE


HOUSEHOLD STATE

Material Preparedness:
HIGH

Food Buffer:
HIGH

Water Buffer:
MODERATE

Backup Energy Access:
MODERATE


WORKFORCE

Workforce Participation:
HIGH

Agricultural Workforce:
ADEQUATE

Infrastructure Specialists:
STRAINED

Healthcare Workforce:
LOW


MOBILITY

Mobility:
FUNCTIONAL

Migration Pressure:
LOW

Migration State:
STABLE


DEMOGRAPHIC PRESSURE

Aging Pressure:
MODERATE

Hosting Capacity:
MODERATE

Trend:
STABLE.
```

The region may be socially cohesive.

That fact belongs to Society rather than Population State.

---

# 113. Displaced Population Example

```text
POPULATION GROUP

Type:
Displaced Population

Origin:
Neighboring Metropolitan Region

Current Location:
Temporary Regional Settlements

Population:
42,000

Housing:
TEMPORARY

Material Preparedness:
MINIMAL

Resource Dependency:
HIGH

Mobility:
LIMITED

Working-Age Share:
MODERATE

Essential Skills:
MIXED

Return Potential:
UNCERTAIN.
```

Observer uncertainty about return potential may belong to Information if necessary.

---

# 114. Migration Cascade Example

```text
REGION A

Security deteriorates
↓
Migration Pressure rises
↓
Actors begin leaving
↓
Outbound Population Flow grows


REGION B

Inbound Population rises
↓
Housing Demand rises
↓
Supply Demand rises
↓
Workforce also increases
↓
New regional conditions emerge.
```

Migration creates both pressure and opportunity.

---

# 115. Workforce Cascade Example

```text
OUTBOUND MIGRATION
↓
POWER TECHNICIANS
DECLINE
↓
INFRASTRUCTURE
REPAIR CAPACITY FALLS
↓
POWER SERVICE
DEGRADES
↓
REGIONAL MOBILITY
AND EMPLOYMENT
DECLINE
↓
NEW MIGRATION
PRESSURE.
```

This is a cross-system causal loop.

---

# 116. Population State Invariants

## POP-INV-001 — A Population Is Not One Actor

Aggregate state must not become collective cognition.

---

## POP-INV-002 — Population State Does Not Own Individual Psychology

Fear, anxiety, confidence and trauma belong elsewhere.

---

## POP-INV-003 — Population State Does Not Own Trust

Trust remains socially and relationally owned.

---

## POP-INV-004 — Population State Does Not Own Social Cohesion

Cohesion belongs primarily to Society.

---

## POP-INV-005 — Population State Does Not Own Character Decisions

Aggregate behavior emerges from Actor decisions and circumstances.

---

## POP-INV-006 — Population Groups Are Structural, Not Personality Types

Groups exist because of meaningful simulation differences.

---

## POP-INV-007 — Mobility and Migration Are Separate

Ability to move does not imply movement.

---

## POP-INV-008 — Migration Pressure Does Not Guarantee Migration

Actor choice and mobility remain necessary.

---

## POP-INV-009 — Migration May Create Benefits and Costs

Population movement is not inherently destabilizing.

---

## POP-INV-010 — Population Size Does Not Equal System Capability

Workforce composition and specialization matter.

---

## POP-INV-011 — Household Buffers Matter

Material household resilience can delay system pressure.

---

## POP-INV-012 — Household Buffers Deplete Over Time

Preparedness is not permanent.

---

## POP-INV-013 — Aggregate Behavior Should Be Observable

Population State should prefer measurable patterns over inferred collective mental states.

---

## POP-INV-014 — Supply and Population Are Separate

Population creates demand.

Supply owns resource truth.

---

## POP-INV-015 — Infrastructure and Population Are Separate

Population consumes infrastructure service but does not own infrastructure state.

---

## POP-INV-016 — Population Does Not Own Public Order

Security and Society remain authoritative for order and social structure.

---

## POP-INV-017 — Population Does Not Own Political Legitimacy

Authority and Society own relevant governance and legitimacy state.

---

## POP-INV-018 — Population Fragmentation Must Be Decomposed

Demographic, social, political and informational fragmentation are different phenomena.

---

## POP-INV-019 — Population State Persists Off-Screen

People continue to move, age, work and migrate without player observation.

---

## POP-INV-020 — Resolution Changes Detail, Not Population Reality

Low-resolution populations remain causally active.

---

## POP-INV-021 — Demographic Change Requires Cause

Population shifts must arise from birth, death, movement or other real demographic processes.

---

## POP-INV-022 — Population Recovery May Transform Structure

Recovery does not require restoring previous demographics.

---

## POP-INV-023 — Positive Population Cascades Are Valid

Population change may improve world conditions.

---

## POP-INV-024 — Civilian Irrationality Must Not Be Used as Drama Shortcut

Aggregate behavior must remain causally grounded.

---

# 117. Development Locks

Future Population State development must not introduce:

```text
population as hive mind

universal Population Emotion

universal Fear score

universal Public Confidence

universal Perceived Threat

Population-owned Trust

Population-owned Social Cohesion

Population-owned Culture

Population-owned Identity

Population-owned Authority legitimacy

Population-owned Character goals

Population-owned Character decisions

automatic panic

automatic riot

automatic protest

automatic migration

automatic stockpiling

automatic crime

automatic black market

automatic cooperation

automatic unrest

crisis equals panic

fear equals violence

protest equals disorder

migration equals failure

population decline equals collapse

population growth equals recovery

displaced population as homogeneous group

distant populations frozen off-screen

player-triggered migration

narrative-generated civilian behavior

random unrest for drama

random panic for drama.
```

---

# 118. Population Architecture Test

Before adding a Population mechanic, ask:

```text
IS THIS
DEMOGRAPHIC
OR MATERIAL
POPULATION STATE?

OR

IS IT ACTUALLY
PSYCHOLOGY?

SOCIETY?

TRUST?

AUTHORITY?

SECURITY?

CHARACTER DECISION?

HOW MANY PEOPLE
ARE AFFECTED?

WHERE ARE THEY?

WHAT IS THEIR
DEMOGRAPHIC STRUCTURE?

WHAT MATERIAL
BUFFERS EXIST?

CAN THEY MOVE?

ARE THEY
ACTUALLY MOVING?

WHAT WORKFORCE
CAPABILITY EXISTS?

WHAT DEMAND
DO THEY CREATE?

WHAT EXTERNAL
SYSTEMS ARE
AFFECTING THEM?

WHAT AGGREGATE
BEHAVIOR IS
ACTUALLY OBSERVED?

WHAT CAUSED
THE CHANGE?

WHAT OTHER
SYSTEMS SHOULD
UPDATE?

CAN THIS CHANGE
OFF-SCREEN?

CAN IT BE
REPRESENTED
WITHOUT PRETENDING
THE POPULATION
HAS ONE MIND?
```

---

# 119. Final Population Model

Conceptually:

```text
REGIONAL WORLD STATE
        ↓
────────────────────────────
POPULATION STATE
────────────────────────────
        │
        ├── Population Size
        ├── Density
        ├── Distribution
        ├── Trend
        ├── Demographics
        ├── Household Structure
        ├── Household Buffers
        ├── Workforce
        ├── Essential Workforce
        ├── Mobility
        ├── Migration Pressure
        ├── Migration
        ├── Displacement
        ├── Hosting Capacity
        ├── Demographic Pressure
        └── Aggregate Observable Patterns
                ↓
WORLD CONDITIONS
+
INFORMATION
+
SOCIETY
+
CHARACTER DECISIONS
+
AUTHORITY ACTION
+
SECURITY
+
SUPPLY
+
INFRASTRUCTURE
+
TIME
                ↓
POPULATION CHANGE
                ↓
NEW DEMAND
+
NEW WORKFORCE
+
NEW MOVEMENT
+
NEW DISTRIBUTION
+
NEW DEMOGRAPHIC STATE
                ↓
WORLD CONSEQUENCES.
```

---

# 120. Population North Star

The system succeeds when Project Ascension can answer:

```text
HOW MANY PEOPLE
ARE HERE?

WHERE ARE THEY?

HOW DENSELY
ARE THEY
DISTRIBUTED?

IS THE POPULATION
GROWING OR
DECLINING?

WHO IS
MOVING?

WHERE?

WHY ARE
MATERIAL CONDITIONS
PUSHING MOVEMENT?

CAN PEOPLE
ACTUALLY MOVE?

WHAT HOUSEHOLD
BUFFERS REMAIN?

HOW LONG
CAN THOSE
BUFFERS LAST?

HOW MUCH
WORKFORCE
REMAINS?

WHICH SPECIALISTS
ARE MISSING?

WHAT DEMAND
IS THE POPULATION
CREATING?

WHAT DEMOGRAPHIC
PRESSURES EXIST?

WHAT CHANGES
WHEN PEOPLE
LEAVE?

WHAT CHANGES
WHEN PEOPLE
ARRIVE?

AND

WHAT HAPPENS
TO THIS POPULATION
IF THE PLAYER
NEVER COMES HERE?
```

---

# 121. Closing Principle

Project Ascension should never model civilians as:

```text
THE CROWD.
```

There is no single crowd.

There are:

```text
families

workers

parents

children

specialists

older people

migrants

displaced people

people with cars

people without cars

people with savings

people without savings

people tied to a place

people looking for somewhere else

people who stay

people who leave

people who return.
```

At high resolution, these are individuals.

At lower resolution, they become population patterns.

The abstraction must never erase the fact that the pattern came from individual human lives.

Population State therefore does not answer:

```text
WHAT DOES
THE POPULATION
THINK?
```

It answers:

```text
WHO IS HERE?

WHERE ARE THEY?

WHAT MATERIAL
CAPACITY DO
THEY HAVE?

HOW ARE THEY
MOVING?

WHAT ARE THEY
DOING IN
AGGREGATE?

AND

HOW IS THAT
CHANGING
THE WORLD?
```

The central principle is:

> **Population State represents the large-scale consequences of millions of individual human lives without pretending those lives have become one mind.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-08-09 | Established initial population behavior, confidence, preparedness, cohesion, workforce, resource behavior, migration, unrest, adaptation and social-memory framework. |
| 1.0 | 2026-09-01 | Rebuilt Population State as canonical aggregate demographic and material population architecture. Preserved population scale, density, population groups, household buffers, workforce, essential workforce, mobility, migration, displacement, demographic pressure, population adaptation, feedback loops and adaptive simulation resolution while redirecting fear, confidence, perceived threat and psychology to human systems; Trust, cohesion, community organization and collective identity to Society; legitimacy and governance decisions to Authority; public order and crime to Security; observer knowledge to Information; and individual action to Characters. Reframed Population behavior around observable aggregate patterns rather than collective cognition and established explicit boundaries preventing hive-mind simulation. |