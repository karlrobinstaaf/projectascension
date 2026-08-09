# PROJECT ASCENSION
# World State System

| Field | Value |
|--------|-------|
| System | World Simulation |
| Document | World State |
| Location | Canon/Systems/World_Simulation/World_State.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Global Simulation State |
| Last Updated | 2026-08-09 |

> *"A world state is not a description of what the world looks like. It is a description of what the world is currently capable of becoming."*

---

# Purpose

The World State defines the highest-level dynamic representation of the Project Ascension world.

It provides the shared simulation structure used by:

- global systems
- nations
- regions
- settlements
- institutions
- infrastructure
- populations
- narrative systems
- the Living Campaign Engine

The World State does not describe every individual event.

It stores the conditions from which events may emerge.

---

# Important Distinction

The dynamic **World State System** defined in this document is not the same thing as the canonical historical eras:

- World State 01 — The Connected World
- World State 02 — The Transition
- World State 03 — The Fractured World
- World State 04 — The Reconnection

Those documents describe broad historical eras.

This system describes the underlying simulation state existing inside those eras.

For clarity:

```text
CANONICAL WORLD STATE
The historical era.

Example:
The Fractured World

DYNAMIC WORLD STATE
The current simulation condition.

Example:
Northern Virginia:
Infrastructure = Degraded
Authority = Regional
Supply = Constrained
Security = Stable
```

A campaign may exist within:

**World State 03 — The Fractured World**

while individual regions possess radically different dynamic conditions.

---

# Core Concept

The world should not be represented using a single variable such as:

```text
WORLD_STABILITY = 42
```

Such a value would hide too much important information.

Instead, the World State is composed of multiple interacting domains.

Conceptually:

```text
WORLD STATE
│
├── Historical Era
├── Global Conditions
├── National States
├── Regional States
├── Global Pressures
├── Global Events
├── Information Environment
└── Historical Memory
```

The World State provides structure.

Detailed conditions belong primarily to lower simulation layers.

---

# World State Hierarchy

The simulation hierarchy is:

```text
WORLD
│
├── GLOBAL STATE
│
├── NATION
│   │
│   ├── REGION
│   │   │
│   │   ├── LOCAL AREA
│   │   │   │
│   │   │   └── COMMUNITY / SETTLEMENT
│   │   │
│   │   └── LOCAL AREA
│   │
│   └── REGION
│
└── NATION
```

Higher levels influence lower levels.

Lower levels may collectively change higher levels.

Neither relationship should be absolute.

---

# State Inheritance

World conditions may propagate downward.

For example:

```text
GLOBAL TRADE
DEGRADED
    │
    ▼
NATIONAL IMPORT CAPACITY
STRAINED
    │
    ▼
REGIONAL SUPPLY
CONSTRAINED
```

However, lower levels may resist or compensate for higher-level pressure.

Example:

```text
GLOBAL FOOD TRADE
DEGRADED

REGION A
High local agriculture
Strong storage
Local transportation

Result:
SUPPLY = STABLE
```

while:

```text
REGION B
Import dependent
Dense population
Weak storage

Result:
SUPPLY = CRITICAL
```

Global conditions create pressure.

They do not dictate identical outcomes.

---

# Historical Era

Every World State must reference the current canonical historical era.

Example:

```text
Historical Era:
WS-02 — The Transition
```

or:

```text
Historical Era:
WS-03 — The Fractured World
```

The Historical Era provides broad constraints and expectations.

It should influence:

- available technology
- institutional structure
- global connectivity
- common knowledge
- cultural memory
- baseline risks

It should not determine the exact condition of every region.

---

# Historical Era Structure

Conceptually:

```text
historical_era:
    id
    name
    start_period
    end_period
    active
```

Example:

```text
historical_era:
    id: WS-02
    name: The Transition
    active: true
```

Exact implementation syntax may change later.

This document defines concepts rather than programming language requirements.

---

# Global Conditions

The Global State describes forces affecting large portions of the world.

Initial global domains include:

```text
GLOBAL STATE
│
├── Global Connectivity
├── Global Trade
├── International Stability
├── Financial Stability
├── Information Reliability
├── Technological Coordination
├── Global Mobility
└── Geopolitical Pressure
```

These states primarily generate pressure on nations and regions.

---

# Global Connectivity

Global Connectivity represents the ability of distant systems and populations to interact.

It includes:

- internet backbone connectivity
- satellite communications
- international data exchange
- global telecommunications
- major transportation links
- interregional coordination

Possible conceptual states:

```text
INTEGRATED
CONNECTED
DEGRADED
FRAGMENTED
ISOLATED
```

---

# Global Trade

Global Trade represents the functioning of international supply networks.

It includes:

- maritime shipping
- international logistics
- raw materials
- food imports
- energy trade
- industrial components
- medical supply chains

Possible conceptual states:

```text
NORMAL
STRAINED
CONSTRAINED
REGIONALIZED
MINIMAL
```

---

# International Stability

International Stability represents the degree to which nation states cooperate or compete under current pressure.

Factors include:

- diplomacy
- military readiness
- border restrictions
- alliance cohesion
- sanctions
- resource competition
- strategic uncertainty

Possible conceptual states:

```text
COOPERATIVE
COMPETITIVE
TENSE
UNSTABLE
HOSTILE
```

Hostile does not automatically mean open warfare.

---

# Financial Stability

Financial Stability represents broad confidence in monetary and financial systems.

It includes:

- banking
- credit
- markets
- payment systems
- currency confidence
- financial coordination

Possible conceptual states:

```text
STABLE
VOLATILE
STRAINED
DISRUPTED
LOCALIZED
```

A localized financial environment may continue functioning through:

- regional currencies
- barter
- credit networks
- community exchange
- alternative systems

---

# Global Information Reliability

Global Information Reliability represents the ability to establish a widely trusted understanding of events.

It does not measure whether information exists.

It measures whether information can be:

- authenticated
- compared
- verified
- distributed
- trusted

Possible conceptual states:

```text
RELIABLE
CONTESTED
UNSTABLE
FRAGMENTED
LOCALIZED
```

---

# Technological Coordination

Technological Coordination represents the ability of advanced digital systems to operate as a connected technological environment.

This includes:

- software infrastructure
- AI systems
- cloud services
- identity systems
- automated coordination
- security infrastructure
- large-scale data exchange

Possible states:

```text
INTEGRATED
RESTRICTED
SEGMENTED
FRAGMENTED
LOCALIZED
```

This domain becomes especially important during The Transition.

---

# Global Mobility

Global Mobility represents the practical ability of people and goods to move long distances.

Factors include:

- aviation
- shipping
- rail
- road networks
- border controls
- fuel
- safety
- political restrictions

Possible conceptual states:

```text
OPEN
LIMITED
RESTRICTED
REGIONAL
LOCAL
```

---

# Geopolitical Pressure

Geopolitical Pressure measures strategic tension created by:

- uncertainty
- resource competition
- technological competition
- military readiness
- intelligence ambiguity
- migration
- infrastructure dependence

Unlike most state variables, this is primarily a pressure value.

Conceptually:

```text
LOW
MODERATE
HIGH
SEVERE
CRITICAL
```

High geopolitical pressure does not guarantee war.

It increases the probability of:

- defensive action
- misinterpretation
- isolation
- competition
- resource protection

---

# Nations

The World State contains references to active national states.

Conceptually:

```text
nations:
    United States
    Canada
    Mexico
    ...
```

Each nation should maintain its own state rather than inheriting one universal global condition.

A National State may contain:

- national authority
- economic capacity
- military capability
- infrastructure coordination
- emergency communication
- population pressure
- national supply
- regional cohesion
- strategic reserves

Detailed national design may eventually require a separate system document.

---

# Regions

Regions are the primary operational units of World Simulation.

The World State should maintain references to every active simulated region.

Example:

```text
regions:
    Northern Virginia
    Great Lakes
    Pacific Northwest
    Southern California
    Central Texas
```

Each region possesses its own dynamic state.

Detailed regional structure is defined in:

```text
Regional_State.md
```

---

# Why Regions Matter

World State should avoid representing an entire nation as:

```text
United States = Critical
```

because this destroys one of Project Ascension's most important principles.

Instead:

```text
UNITED STATES

Northern Virginia:
Degraded

Pacific Northwest:
Stable

Southern California:
Critical

Great Plains:
Strained

New England:
Stable
```

National conditions emerge from these differences.

---

# Core Simulation Domains

Every Region should eventually expose a standardized group of high-level domains.

Initial domains:

```text
Infrastructure
Communications
Authority
Information
Population
Supply
Security
Recovery
```

These domains should be understandable across the entire game.

---

# Domain State

Every domain should contain more than its current condition.

Conceptually:

```text
DOMAIN
│
├── Current State
├── Pressure
├── Resilience
├── Trend
├── Confidence
└── Last Significant Change
```

---

# Current State

Current State describes what exists now.

Example:

```text
Infrastructure:
DEGRADED
```

---

# Pressure

Pressure measures forces attempting to worsen or alter the state.

Example:

```text
Infrastructure Pressure:
HIGH
```

Sources may include:

- fuel shortage
- workforce shortage
- extreme weather
- spare-part shortage
- cyber restrictions
- increased demand

---

# Resilience

Resilience measures the ability to absorb pressure without changing state.

Example:

```text
Infrastructure Resilience:
MODERATE
```

Possible resilience factors:

- redundancy
- experienced personnel
- local resources
- stockpiles
- alternative systems
- community cooperation
- functioning institutions

---

# Trend

Trend describes current direction.

Conceptually:

```text
IMPROVING
STABLE
DETERIORATING
VOLATILE
```

Example:

```text
Supply:
CONSTRAINED

Trend:
IMPROVING
```

is very different from:

```text
Supply:
CONSTRAINED

Trend:
DETERIORATING
```

even though the current state is identical.

---

# Confidence

Confidence represents how reliable the simulation's knowledge of the state is.

This is particularly useful for distant or poorly connected areas.

Conceptually:

```text
HIGH
MODERATE
LOW
UNKNOWN
```

Example:

```text
Regional Security:
STABLE

Confidence:
LOW
```

means reports indicate stability but reliable verification is limited.

---

# Actual State

The simulation maintains an internal Actual State.

Example:

```text
Actual Supply State:
STRAINED
```

This value should not automatically be visible to:

- players
- NPCs
- governments
- factions
- Game Masters using limited-information modes

Actual State represents simulation truth.

---

# Observed State

Observers interact with representations of the Actual State.

Example:

```text
Actual Supply:
STRAINED

Government Estimate:
STRAINED

Public Perception:
CRITICAL

Player Knowledge:
UNKNOWN
```

These may all exist simultaneously.

---

# Knowledge Layers

The World State should support multiple knowledge layers.

Conceptually:

```text
ACTUAL STATE
      │
      ├── Institutional Knowledge
      ├── Faction Knowledge
      ├── Public Knowledge
      ├── Local Knowledge
      └── Player Knowledge
```

Different observers may possess different information about the same world condition.

---

# Knowledge Is Not Automatically Shared

If one institution learns something, other institutions do not automatically know it.

Knowledge must move through:

- communication
- intelligence
- observation
- reports
- relationships
- media
- direct contact

This preserves the information asymmetry established throughout Project Ascension.

---

# Global Pressures

The World State should maintain persistent global pressures.

Examples include:

```text
AI Uncertainty
Climate Pressure
Migration Pressure
Economic Pressure
Resource Pressure
Geopolitical Pressure
Infrastructure Pressure
Information Pressure
```

Not every campaign must use every pressure.

Pressures should exist only when relevant.

---

# Pressure Scale

A common conceptual scale may be:

```text
NONE
LOW
MODERATE
HIGH
SEVERE
CRITICAL
```

Pressure does not directly equal state.

Example:

```text
Food Supply:
STABLE

Food Pressure:
SEVERE

Resilience:
HIGH
```

The region currently has food.

Its ability to maintain that state is under serious pressure.

---

# Pressure Sources

Pressures should record their sources.

Example:

```text
Supply Pressure:
HIGH

Sources:
- reduced rail capacity
- fuel restrictions
- population increase
```

This allows the system to explain why conditions are changing.

---

# Positive Pressure

Not all pressure needs to represent degradation.

The system may also track recovery momentum.

Example:

```text
Recovery Pressure:
HIGH

Sources:
- restored rail connection
- external assistance
- improved power availability
```

Alternatively, positive change may be represented through recovery factors rather than pressure.

The implementation should favor clarity over mathematical purity.

---

# Events

World Events represent meaningful changes generated by or applied to the simulation.

Examples:

```text
Power plant shutdown
Major storm
Regional election
Trade agreement
Bridge failure
Migration wave
New settlement alliance
Hospital closure
Emergency fuel shipment
Communication restoration
```

Events may be:

- global
- national
- regional
- local

---

# Event Structure

Conceptually:

```text
EVENT
│
├── ID
├── Date / Time
├── Location
├── Type
├── Cause
├── Immediate Effects
├── Secondary Effects
├── Visibility
└── Historical Significance
```

---

# Event Cause

Whenever possible, events should record why they occurred.

Example:

```text
Event:
Regional Fuel Rationing

Cause:
Supply State = Constrained
Fuel Pressure = Severe
Authority = Functional
Public Confidence = Moderate
```

The simulation can then explain why rationing occurred instead of simply generating it randomly.

---

# External Events

Not every event must emerge entirely from internal simulation states.

External events may include:

- weather
- natural disasters
- technological discoveries
- foreign decisions
- disease outbreaks
- major accidents

External events enter the simulation as new pressures or direct state changes.

They should still interact with existing conditions.

---

# Example

A hurricane striking two regions may produce very different outcomes.

```text
REGION A

Infrastructure:
Stable

Resilience:
High

Authority:
Strong

Recovery:
High
```

Result:

```text
Temporary disruption
Rapid repair
Limited migration
```

while:

```text
REGION B

Infrastructure:
Degraded

Resilience:
Low

Authority:
Weak

Recovery:
Low
```

may produce:

```text
Critical infrastructure failure
Supply disruption
Population movement
Long-term regional decline
```

The event is the same.

The world state determines the consequence.

---

# Historical Memory

The World State should retain important past events and state transitions.

Conceptually:

```text
history:
    event
    event
    state_change
    event
```

Not every simulation tick needs permanent storage.

Only meaningful events should enter Historical Memory.

---

# Historical Memory Categories

Examples include:

- major infrastructure failure
- mass migration
- political transition
- settlement founding
- settlement destruction
- major conflict
- recovery milestone
- major alliance
- important discovery
- player-caused regional change

---

# Historical Memory Effects

Past events may modify future behavior.

Example:

```text
Historical Event:
2039 Food Crisis

Long-Term Effects:
+ preparedness
+ food storage
+ distrust of centralized supply
```

The region may therefore respond differently to another shortage years later.

---

# World Memory Versus Character Memory

World State stores systemic history.

Characters maintain personal memory separately.

For example:

```text
WORLD MEMORY:
Regional power outage lasted 11 days.

CHARACTER MEMORY:
"My father died during the blackout."
```

Both may refer to the same event.

They belong to different systems.

---

# Global Aggregation

Global and national states may be derived partly from regional conditions.

Example:

```text
National Infrastructure Coordination
```

might consider:

- percentage of regions functioning
- major interregional connections
- strategic infrastructure
- regional divergence

However, simple averages should be avoided.

A failure in one strategically important region may matter more than multiple stable low-impact regions.

---

# Weighted Importance

Regions may possess different systemic importance.

Possible factors include:

- population
- energy production
- food production
- transportation hubs
- industrial capacity
- political importance
- communications infrastructure
- military significance

Conceptually:

```text
Regional Strategic Weight:
LOW
MODERATE
HIGH
CRITICAL
```

This should be used carefully.

It represents systemic influence, not human worth.

---

# Neighbor Influence

Regions should affect neighboring regions.

Possible flows include:

- people
- food
- fuel
- electricity
- information
- crime
- trade
- disease
- political influence
- security threats

Conceptually:

```text
REGION A
    │
    ├── Supply Flow → REGION B
    ├── Migration → REGION C
    └── Information → REGION D
```

Detailed mechanics belong in `Regional_State.md`.

---

# Time

World State changes over simulation time.

Time may operate at different resolutions depending upon campaign needs.

Possible levels include:

```text
REAL-TIME / ENCOUNTER
HOURS
DAYS
WEEKS
MONTHS
YEARS
```

The World Simulation should not require every domain to update at the same frequency.

---

# Update Frequency

Examples:

```text
Communications:
may change within hours

Infrastructure:
may change over hours or days

Supply:
may change over days or weeks

Population:
may change over days or months

Political legitimacy:
may change over weeks or years
```

Simulation timing should reflect plausible system behavior.

---

# State Transition

Domains should normally change gradually.

Example:

```text
STABLE
  ↓
STRAINED
  ↓
DEGRADED
  ↓
CRITICAL
  ↓
FAILED
```

Direct transitions may occur during extreme events.

Example:

```text
STABLE
  ↓
FAILED
```

after catastrophic physical destruction.

Such transitions should remain exceptional.

---

# State Stabilization

A state may remain unchanged despite significant pressure.

Example:

```text
Infrastructure:
STRAINED

Pressure:
HIGH

Resilience:
HIGH

Result:
STRAINED
```

This means resilience successfully absorbs current pressure.

---

# State Recovery

Improvement requires meaningful recovery factors.

Example:

```text
Infrastructure:
DEGRADED

Pressure:
LOW

Recovery Capacity:
HIGH

Result:
Movement toward STRAINED
```

Recovery should usually take time.

---

# Failed Does Not Mean Gone

A domain state of:

```text
FAILED
```

should not automatically mean complete destruction.

It means the system can no longer perform its expected function reliably.

Example:

```text
National Communications:
FAILED
```

may coexist with:

```text
Local Radio:
FUNCTIONAL

Regional Mesh Network:
FUNCTIONAL
```

The centralized system failed.

Communication did not disappear.

---

# Fragmentation

Fragmentation is a special systemic condition.

It occurs when lower-level systems continue functioning but no longer operate as one coordinated higher-level system.

Example:

```text
National Infrastructure:
FRAGMENTED

Region A:
Stable

Region B:
Degraded

Region C:
Stable

Region D:
Critical
```

This concept is fundamental to Project Ascension.

---

# Fragmentation Is Not Failure

A fragmented world may contain:

- functioning cities
- stable settlements
- trade networks
- local governments
- electricity
- agriculture
- healthcare
- transportation

What is missing is the previous level of integration.

This distinction directly supports:

**World State 03 — The Fractured World**

which is:

**not a wasteland.**

It is:

**a world of disconnected realities.**

---

# World State Snapshot

At any point, the World Simulation should be capable of producing a snapshot.

Example:

```text
WORLD STATE SNAPSHOT

Date:
2034-07-10

Historical Era:
WS-02 — The Transition

GLOBAL

Connectivity:
DEGRADED

Trade:
STRAINED

International Stability:
TENSE

Financial Stability:
VOLATILE

Information Reliability:
UNSTABLE

Technological Coordination:
SEGMENTED

Global Mobility:
LIMITED

Geopolitical Pressure:
HIGH


UNITED STATES

National Authority:
FUNCTIONAL

Infrastructure Coordination:
DEGRADING

Emergency Communication:
ECL-3

Regional Cohesion:
STRAINED


NORTHERN VIRGINIA

Infrastructure:
DEGRADED

Communications:
REGIONAL

Authority:
FUNCTIONAL

Information:
UNSTABLE

Population:
CONCERNED

Supply:
CONSTRAINED

Security:
STABLE

Recovery:
MODERATE
```

A snapshot should describe conditions.

It should not automatically explain them to the player.

---

# World State ID

Important World State snapshots may receive identifiers.

Conceptually:

```text
WSIM-2034-07-10-1200
```

or campaign-specific identifiers.

This allows:

- saves
- rollback
- debugging
- historical comparison
- campaign analysis

Exact technical implementation will be determined later.

---

# Canonical World State Snapshots

Some historical snapshots may eventually become Canon.

These would represent known historical conditions during established periods.

For example:

```text
Pre-Collapse United States
2034-08-16
```

could eventually have a canonical World Simulation snapshot.

This should only be created where useful.

Recovered Records remain the primary narrative evidence for historical conditions.

---

# Campaign World State

A campaign should maintain its own dynamic state.

Conceptually:

```text
CAMPAIGN WORLD STATE
│
├── Canon Foundation
├── Campaign Divergence
├── Player Effects
├── Generated Events
└── Persistent Changes
```

The campaign begins from Canon.

Gameplay may create divergence.

---

# Canon Boundary

Some events may be fixed by the selected campaign era.

Others may remain mutable.

Example:

If a campaign begins after The Collapse:

```text
The Collapse occurred.
```

is fixed Canon.

But:

```text
Settlement A survives until 2051.
```

may not be fixed unless specifically established.

This distinction allows meaningful player influence without rewriting foundational Canon unintentionally.

---

# Canon Locks

The simulation may eventually use Canon Locks.

Conceptually:

```text
CANON LOCK
```

means:

A state or historical fact cannot be changed by ordinary simulation.

Examples:

- historical emergence of Aurora
- established World State transitions
- major pre-campaign historical facts

Canon Locks should be used sparingly.

---

# Campaign Divergence

Campaign divergence represents history created during play.

Example:

Canonical starting condition:

```text
Settlement Haven:
Supply = Strained
```

Campaign event:

```text
Players restore rail connection.
```

New campaign state:

```text
Settlement Haven:
Supply = Stable
```

The campaign world has changed.

Canon has not been contradicted unless a later fixed Canon event requires otherwise.

---

# World State and Save Games

A saved campaign should preserve:

- current states
- pressures
- resilience
- active events
- important historical memory
- region relationships
- player effects
- knowledge states where required

World Simulation continuity depends upon persistent state.

---

# Explanation Layer

The simulation should preserve enough information to answer:

**Why is this state what it is?**

Example:

```text
Supply:
CRITICAL

WHY?

Rail:
Unavailable

Fuel:
Constrained

Population:
+18%

Neighboring Region:
No export capacity

Authority:
Weak
```

This explanation layer is important for:

- debugging
- Game Master tools
- AI narrative generation
- player-facing investigation
- consistency

---

# Causal Trace

Important state changes may record a causal trace.

Example:

```text
SUPPLY: STRAINED → CRITICAL

Primary Causes:
- fuel shortage
- bridge closure

Secondary Cause:
- population influx

Mitigating Factor:
- local food storage
```

The exact implementation can remain lightweight.

The principle is important.

---

# Uncertainty

The simulation should allow uncertain state estimates.

Example:

```text
Region:
Western Pennsylvania

Estimated Security:
Stable

Confidence:
Low

Last Reliable Report:
6 days ago
```

This becomes increasingly important during:

**The Fractured World.**

---

# Unknown Regions

A region does not need a fully known state.

Conceptually:

```text
Infrastructure:
UNKNOWN

Authority:
UNKNOWN

Population:
ESTIMATED

Communication:
NONE

Last Contact:
2046-03-18
```

The simulation may still maintain an internal state.

Characters and players simply do not know it.

---

# Dormant Simulation

Distant regions may operate at reduced simulation resolution.

Instead of calculating every domain continuously, the system may store:

```text
State
Trend
Pressure
Resilience
Major Events
```

When the region becomes relevant, higher-resolution simulation can resume.

---

# State Compression

Long periods may be summarized.

Example:

Instead of simulating 180 individual days:

```text
Winter 2048

Supply Pressure:
High

Infrastructure:
Stable → Strained

Population:
Stable

Recovery:
Low
```

Significant events remain preserved.

Routine events may be compressed.

---

# World State Consistency Rules

The following consistency rules should apply.

## Rule 1

A lower-level state may differ significantly from its parent state.

---

## Rule 2

Higher-level states should reflect meaningful lower-level patterns.

---

## Rule 3

State changes require causes.

---

## Rule 4

Pressure does not guarantee change.

---

## Rule 5

Resilience does not guarantee stability forever.

---

## Rule 6

Recovery requires resources, time or adaptation.

---

## Rule 7

Information about a state is separate from the state itself.

---

## Rule 8

Fragmentation does not equal universal failure.

---

## Rule 9

The simulation should remember major consequences.

---

## Rule 10

Player actions may modify state but should obey the same causal rules as NPC and institutional actions.

---

# Integration With Existing Canon Systems

World State should integrate with existing systems rather than duplicate them.

---

## Emergency Communication Levels

Source:

```text
Canon/Systems/Emergency_Communication_Levels.md
```

ECL provides a standardized description of emergency communication and coordination.

World Simulation should reference the canonical ECL values.

---

## Infrastructure Monitoring Levels

Source:

```text
Canon/Systems/Infrastructure_Monitoring_Levels.md
```

IML provides a standardized infrastructure coordination framework.

World Simulation should reference IML rather than invent a competing infrastructure scale where appropriate.

---

# ECL and IML Are Not Universal Scores

A region may have:

```text
IML-4
```

while national communications remain:

```text
ECL-2
```

or vice versa.

The systems describe different dimensions.

World State combines them without assuming numerical equivalence.

---

# World Simulation Minimum State

A minimal functioning simulation should be able to store:

```text
Date
Historical Era
Regions

For each region:
    Infrastructure
    Communications
    Authority
    Information
    Population
    Supply
    Security
    Recovery

For each domain:
    State
    Pressure
    Resilience
    Trend

Plus:
    Active Events
    Historical Memory
```

Everything beyond this should justify its complexity.

---

# Example Minimal Data Model

Conceptually:

```text
WORLD

Date:
2034-07-10

Historical Era:
WS-02

Regions:

    Northern Virginia:

        Infrastructure:
            State: Degraded
            Pressure: High
            Resilience: Moderate
            Trend: Deteriorating

        Communications:
            State: Regional
            Pressure: Moderate
            Resilience: Moderate
            Trend: Stable

        Authority:
            State: Functional
            Pressure: Moderate
            Resilience: High
            Trend: Stable

        Information:
            State: Unstable
            Pressure: High
            Resilience: Low
            Trend: Deteriorating

        Population:
            State: Concerned
            Pressure: High
            Resilience: Moderate
            Trend: Volatile

        Supply:
            State: Constrained
            Pressure: High
            Resilience: Moderate
            Trend: Deteriorating

        Security:
            State: Stable
            Pressure: Moderate
            Resilience: High
            Trend: Stable

        Recovery:
            State: Moderate
            Pressure: Moderate
            Resilience: Moderate
            Trend: Stable
```

This is a conceptual model.

It is not yet a required technical schema.

---

# Design Principle

World State should always remain understandable by humans.

If designers cannot explain why a region is in a particular state without reading code, the simulation has become too opaque.

Complexity belongs in interactions.

Not in incomprehensible variables.

---

# Guiding Questions

At any moment, World State should allow the system to answer:

**What is happening?**

**Where is it happening?**

**How severe is it?**

**What is pushing it to change?**

**What is preventing it from changing?**

**Which direction is it moving?**

**Who knows about it?**

**What happened previously that affects it now?**

These answers form the foundation of the living world.

---

# Current Status

```text
WORLD SIMULATION

README.md
COMPLETE

World_State.md
FOUNDATION DEFINED

Regional_State.md
PENDING

Infrastructure_State.md
PENDING

Information_State.md
PENDING

Authority_State.md
PENDING

Population_State.md
PENDING

Escalation_and_Recovery.md
PENDING
```

---

# Next Document

The next recommended document is:

```text
Canon/Systems/World_Simulation/Regional_State.md
```

World State defines the hierarchy.

Regional State defines the level where most of the simulation actually becomes alive.

It will establish:

- regional identity
- geography
- strategic importance
- domain values
- resilience
- dependencies
- neighboring regions
- resource flows
- regional divergence
- regional memory

The world exists globally.

**Project Ascension is experienced regionally.**

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial World State hierarchy, domain model, pressure, resilience, knowledge and historical-memory framework established. |