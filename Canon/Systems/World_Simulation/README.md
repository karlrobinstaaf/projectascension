# PROJECT ASCENSION
# World Simulation System

| Field | Value |
|--------|-------|
| System | World Simulation |
| Location | Canon/Systems/World_Simulation/ |
| Status | Working Canon |
| Scope | Global / National / Regional / Local |
| Function | Dynamic World-State Simulation |

> *"The world does not wait for the player."*

---

# Purpose

The World Simulation system defines how the world of Project Ascension changes over time independently of direct player action.

Its purpose is to create a world that behaves as a living system rather than a sequence of scripted events.

The simulation tracks interacting conditions across:

- infrastructure
- communications
- government authority
- population behavior
- supply systems
- security
- information reliability
- regional stability
- institutional capacity
- recovery capability

These conditions influence one another.

The result should be a world where consequences emerge from system interactions rather than from a predetermined collapse script.

---

# Core Principle

Project Ascension does not simulate:

**a scripted apocalypse.**

It simulates:

**a society attempting to continue functioning under increasing uncertainty and pressure.**

Systems do not fail simply because the narrative requires them to fail.

They degrade because:

- resources become unavailable
- dependencies fail
- information becomes unreliable
- personnel capacity decreases
- coordination breaks down
- institutions make protective decisions
- populations change behavior
- local solutions create wider consequences
- external events alter operating conditions

Likewise, degradation does not always continue.

Systems may:

- stabilize
- adapt
- recover
- reorganize
- decentralize
- fail temporarily
- develop new forms of resilience

Collapse is therefore a possible system state.

It is not the only system state.

---

# Simulation Philosophy

The World Simulation should follow five principles.

## 1. The World Continues Without the Player

Events occur whether the player witnesses them or not.

Communities make decisions.

Infrastructure changes.

Governments respond.

Organizations adapt.

People move.

Resources are consumed.

Conflicts develop.

Recovery efforts begin.

The player exists inside the world.

The world does not exist solely for the player.

---

## 2. Local Conditions Matter

There is no universal world state.

Different locations may experience radically different conditions at the same time.

One region may be:

**Stable**

while another is:

**Degraded**

and another:

**Critical**

National conditions are therefore aggregates of regional conditions rather than absolute states applied everywhere.

---

## 3. Systems Are Interdependent

No major world system exists in isolation.

For example:

```text
POWER
  │
  ├── affects → COMMUNICATIONS
  │
  ├── affects → WATER
  │
  ├── affects → HEALTHCARE
  │
  ├── affects → TRANSPORTATION
  │
  └── affects → SUPPLY
```

But the dependencies also operate in reverse.

```text
TRANSPORTATION
      │
      └── affects → FUEL DELIVERY
                       │
                       └── affects → POWER
```

The simulation should therefore allow cascading consequences without assuming every disruption becomes catastrophic.

---

## 4. Human Response Is Part of the System

People do not passively experience world-state changes.

They react.

Possible reactions include:

- adaptation
- conservation
- migration
- cooperation
- stockpiling
- volunteering
- avoidance
- protest
- crime
- local organization
- mutual aid
- political pressure
- defensive behavior

These responses may improve or worsen local conditions.

Human behavior is therefore part of the simulation rather than merely a consequence of it.

---

## 5. Recovery Must Always Be Possible

World Simulation must model recovery as seriously as degradation.

A damaged system may recover through:

- repair
- redundancy
- local adaptation
- resource redistribution
- political coordination
- community cooperation
- technological substitution
- restored communications
- improved information
- reduced demand

The simulation should avoid an automatic downward spiral.

A region may move:

```text
Stable
  ↓
Strained
  ↓
Degraded
  ↓
Critical
```

but it may also move:

```text
Critical
  ↑
Degraded
  ↑
Strained
  ↑
Stable
```

Recovery may be slow.

It may be incomplete.

It may produce a society different from the one that existed before.

But it remains possible.

---

# Simulation Layers

World Simulation operates across several interconnected layers.

```text
WORLD
│
├── Global
│
├── National
│
├── Regional
│
├── Local
│
└── Community
```

Each layer may influence the others.

---

# Global Layer

The Global Layer represents conditions that affect multiple nations or the international system.

Examples include:

- global communications
- international trade
- financial systems
- satellite infrastructure
- shipping
- international AI policy
- geopolitical tension
- international migration
- global information reliability

Global conditions should usually influence lower layers rather than directly determine them.

---

# National Layer

The National Layer represents state-level capability.

Examples include:

- federal authority
- national infrastructure coordination
- military readiness
- emergency management
- national communications
- strategic reserves
- national transportation networks
- financial stability

A nation may remain politically intact while losing operational coordination across parts of its territory.

---

# Regional Layer

The Regional Layer is one of the most important simulation layers.

Regions may develop different conditions based on:

- infrastructure
- geography
- population
- resources
- local government
- transportation
- security
- communications
- neighboring regions

Regional divergence becomes increasingly important during prolonged disruption.

---

# Local Layer

The Local Layer represents cities, towns, districts and other operational areas.

Local conditions determine much of what the player directly experiences.

Examples include:

- electricity availability
- fuel
- food supply
- water
- medical services
- police presence
- communications
- transportation
- public behavior
- local authority

---

# Community Layer

The Community Layer represents the immediate social environment surrounding characters.

Examples include:

- neighborhoods
- shelters
- workplaces
- survivor groups
- settlements
- families
- local organizations

This layer connects World Simulation to:

```text
Canon/Systems/Characters/
Canon/Systems/Relationships/
Canon/Systems/Life/
Canon/Systems/Society/
```

---

# Core World-State Domains

The initial World Simulation should track several major domains.

```text
WORLD STATE
│
├── Infrastructure
├── Communications
├── Authority
├── Information
├── Population
├── Supply
├── Security
└── Recovery
```

These domains represent broad conditions rather than individual technical systems.

---

# Infrastructure

Infrastructure represents the operational condition of essential physical and digital systems.

Examples include:

- electricity
- water
- telecommunications
- transportation
- fuel distribution
- healthcare infrastructure
- logistics
- data networks

Infrastructure should integrate with:

```text
Canon/Systems/Infrastructure_Monitoring_Levels.md
```

---

# Communications

Communications represents the ability of institutions and populations to exchange reliable operational information.

This includes:

- national communication
- regional communication
- emergency alerts
- internet availability
- cellular networks
- radio
- local communication systems

Communications should integrate with:

```text
Canon/Systems/Emergency_Communication_Levels.md
```

including:

```text
ECL-1 — Advisory
ECL-2 — Preparedness
ECL-3 — Regional Emergency
ECL-4 — National Emergency
ECL-5 — Continuity Operations
ECL-6 — Decentralized Communications
```

---

# Authority

Authority represents the practical ability of institutions to govern.

Authority is not simply whether a government legally exists.

It measures whether authorities can:

- communicate
- coordinate
- enforce decisions
- provide services
- distribute resources
- maintain legitimacy
- respond to emergencies

A government may remain legally intact while operational authority becomes increasingly regional or local.

---

# Information

Information represents the quality and reliability of the shared informational environment.

It includes:

- news availability
- verification capacity
- misinformation
- synthetic media
- rumor
- institutional credibility
- intelligence quality
- communications delays

Information failure does not mean that truth disappears.

It means determining truth becomes more difficult.

---

# Population

Population represents broad civilian behavior and demographic movement.

It may include:

- confidence
- fear
- mobility
- migration
- cooperation
- unrest
- workforce availability
- community organization

Population behavior should respond to perceived conditions.

Perception may differ from actual conditions.

This distinction is important.

---

# Supply

Supply represents availability and distribution of essential resources.

Examples include:

- food
- fuel
- medicine
- replacement parts
- industrial materials
- batteries
- water-treatment supplies

Supply depends heavily upon:

- transportation
- infrastructure
- workforce
- communications
- security

---

# Security

Security represents the ability of communities and institutions to maintain physical order.

It includes:

- police capacity
- emergency services
- military support
- crime
- civil unrest
- organized violence
- local defense
- protection of infrastructure

Security should not automatically deteriorate when infrastructure deteriorates.

Many communities may become more cooperative during emergencies.

---

# Recovery

Recovery represents the capacity of a region or institution to improve its condition.

Factors may include:

- technical expertise
- spare parts
- fuel
- communications
- political coordination
- community cooperation
- external assistance
- redundancy
- functioning transportation

Recovery Capacity should be treated as a major strategic resource.

---

# State Model

Each domain should use a limited number of understandable states.

The exact state scales will be defined in their respective system files.

A conceptual example:

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

Not every domain requires exactly the same terminology.

Existing canonical scales should be reused where appropriate.

---

# Example Regional State

A region might exist in the following condition:

```text
REGION: Northern Virginia

Infrastructure:      Degraded
Communications:      ECL-3 — Regional Emergency
Authority:           Functional
Information:         Unstable
Population:          Concerned
Supply:              Constrained
Security:            Stable
Recovery Capacity:   Moderate
```

This does not mean the region has "collapsed."

It describes the current operating environment.

---

# Emergent Consequences

World Simulation should generate consequences from combinations of states.

For example:

```text
Infrastructure: Degraded
Supply: Constrained
Communications: Functional
Authority: Functional
```

may produce:

```text
Controlled rationing
Repair prioritization
Public conservation requests
Regional resource coordination
```

While:

```text
Infrastructure: Degraded
Supply: Constrained
Communications: Unreliable
Authority: Weak
```

may produce:

```text
Localized shortages
Rumor-driven demand
Uneven distribution
Population movement
Black markets
Community self-organization
```

The infrastructure condition is similar.

The wider system produces different outcomes.

---

# Thresholds

Certain combinations of conditions may trigger major transitions.

Examples:

```text
LOW SUPPLY
+
HIGH POPULATION PRESSURE
+
LOW AUTHORITY
=
UNREST RISK
```

or:

```text
DEGRADED INFRASTRUCTURE
+
HIGH RECOVERY CAPACITY
+
FUNCTIONAL COMMUNICATIONS
=
STABILIZATION OPPORTUNITY
```

Thresholds should create probabilities and pressures rather than guaranteed scripted events.

---

# Pressure

World Simulation should distinguish between:

**State**

and:

**Pressure**

State describes current conditions.

Pressure describes forces pushing the state toward change.

Example:

```text
Infrastructure State:
STABLE

Infrastructure Pressure:
HIGH
```

The infrastructure still functions.

But:

- spare parts are declining
- maintenance is delayed
- workforce capacity is falling
- fuel reserves are decreasing

The player may therefore encounter a region that appears normal while the underlying system is becoming fragile.

This is important to Project Ascension.

---

# Resilience

Regions should also possess resilience.

Resilience represents the ability to absorb pressure without changing state.

Possible sources include:

- redundancy
- local resources
- experienced personnel
- strong institutions
- community trust
- geographic advantages
- stored supplies
- independent communications
- distributed energy
- repair capability

Two regions experiencing the same pressure may therefore develop very different outcomes.

---

# World State Versus Perceived State

The simulation should maintain a distinction between:

```text
ACTUAL WORLD STATE
```

and:

```text
PERCEIVED WORLD STATE
```

The player should not automatically know the true simulation state.

For example:

```text
Actual Supply:
Stable

Public Perception:
Critical shortage imminent
```

may produce stockpiling that creates a real shortage.

Likewise:

```text
Actual Infrastructure:
Critical

Public Perception:
Temporary technical problem
```

may delay preparation.

Information therefore influences behavior through perception.

---

# Information Delay

Knowledge should move through the world with delay.

A local event may progress through:

```text
EVENT
  ↓
LOCAL OBSERVATION
  ↓
REGIONAL REPORTING
  ↓
VERIFICATION
  ↓
NATIONAL AWARENESS
  ↓
PUBLIC COMMUNICATION
```

Any stage may be:

- delayed
- incomplete
- misunderstood
- classified
- contradicted
- lost

This preserves the information asymmetry established in the Recovered Records.

---

# Player Interaction

The player should influence World Simulation without becoming the sole cause of world events.

Player actions may affect:

- local resources
- community stability
- relationships
- information
- infrastructure repair
- security
- migration
- authority
- recovery capacity

Some effects may remain local.

Others may propagate outward.

---

# Player Influence Principle

The player should be:

**important**

without being:

**the center of the universe.**

A player may save a community without saving a state.

A player may repair infrastructure without solving the national crisis.

A player may discover important information without convincing anyone to believe it.

A player may influence events whose consequences appear much later.

This creates meaningful agency without destroying world credibility.

---

# No Universal Collapse Clock

World Simulation should not contain a hidden timer that inevitably moves every region toward failure.

Instead:

```text
PRESSURE
+
DEPENDENCIES
+
DECISIONS
+
RESILIENCE
+
RANDOM EVENTS
+
PLAYER ACTION
=
WORLD CHANGE
```

This allows different campaigns to produce different histories while remaining consistent with Project Ascension Canon.

---

# Canon Versus Simulation

Recovered Records describe historical events established in Canon.

World Simulation defines how similar systems operate dynamically during gameplay.

These functions must remain separate.

```text
RECOVERED RECORDS
"What happened?"

WORLD SIMULATION
"What can happen, and why?"
```

Canon provides boundaries.

Simulation provides variation.

---

# Relationship to Recovered Records

Recovered Records provide historical examples of system interactions.

Examples include:

```text
AI uncertainty
        ↓
Containment measures
        ↓
Reduced automation
        ↓
Infrastructure pressure
        ↓
Reduced coordination
        ↓
Regional divergence
        ↓
Emergency decentralization
```

World Simulation should be capable of producing comparable chains dynamically.

It should not simply replay the historical chain every campaign.

---

# Relationship to Living Campaign Engine

World Simulation determines:

**what is happening in the world.**

The Living Campaign Engine determines:

**which parts of that world become relevant to the player's campaign.**

Conceptually:

```text
WORLD SIMULATION
       │
       ▼
WORLD EVENTS
       │
       ▼
LIVING CAMPAIGN ENGINE
       │
       ▼
PLAYER-RELEVANT EVENTS
       │
       ▼
MISSIONS / ENCOUNTERS / CONSEQUENCES
```

This distinction prevents the simulation from requiring every world event to become gameplay content.

---

# Relationship to Narrative

Narrative should interpret simulation events rather than dictate every simulation event.

For example:

World Simulation may determine:

```text
Regional fuel supply becomes Critical.
```

Narrative systems may transform this into:

```text
Fuel rationing begins.

A hospital requests emergency diesel.

A transport company stops operating.

A local politician blames federal authorities.

A black market appears.
```

The state change creates narrative opportunities.

---

# Relationship to Characters

Characters exist inside World Simulation.

Their behavior may be influenced by:

- local conditions
- personal resources
- relationships
- beliefs
- personality
- responsibilities
- information available to them

Characters should not possess perfect knowledge of simulation variables.

They respond to what they perceive.

---

# Relationship to Society

Society systems should interpret population-level consequences of World Simulation.

Examples include:

- institutional trust
- community cohesion
- political legitimacy
- migration
- social norms
- economic adaptation
- emerging local organizations

World Simulation provides conditions.

Society determines how populations organize within those conditions.

---

# Randomness

Randomness may influence World Simulation.

However, randomness should operate inside plausible boundaries.

Random events may determine:

- timing
- severity
- location
- secondary failure
- weather
- equipment failure
- individual decisions

Randomness should not replace causality.

The player should usually be able to understand why something could have happened even if the exact occurrence was unpredictable.

---

# Simulation Update Cycle

A conceptual World Simulation cycle may operate as:

```text
1. READ CURRENT STATE
        ↓
2. APPLY EXISTING PRESSURES
        ↓
3. PROCESS DEPENDENCIES
        ↓
4. PROCESS INSTITUTIONAL RESPONSES
        ↓
5. PROCESS POPULATION RESPONSES
        ↓
6. APPLY EXTERNAL EVENTS
        ↓
7. APPLY PLAYER EFFECTS
        ↓
8. CALCULATE STATE CHANGES
        ↓
9. CALCULATE RECOVERY
        ↓
10. GENERATE WORLD EVENTS
        ↓
11. UPDATE INFORMATION FLOW
        ↓
12. SAVE NEW WORLD STATE
```

The exact implementation may change during development.

The conceptual order should remain understandable.

---

# Simulation Granularity

The simulation should not attempt to model every individual person, vehicle, power line or shipment.

World Simulation operates primarily through abstraction.

Detailed simulation should occur only where it creates meaningful gameplay.

The design goal is:

**credible complexity**

not:

**maximum complexity.**

---

# Performance Principle

World systems distant from the player may operate at lower simulation resolution.

Conceptually:

```text
PLAYER REGION
High-resolution simulation

NEIGHBORING REGIONS
Medium-resolution simulation

DISTANT REGIONS
Low-resolution simulation

GLOBAL SYSTEMS
Aggregate simulation
```

Simulation resolution may increase when a region becomes relevant.

This allows the world to remain dynamic without requiring unnecessary computation.

---

# Persistence

Important world-state changes should persist.

Examples:

- damaged infrastructure
- population migration
- depleted supplies
- destroyed facilities
- political changes
- repaired systems
- established settlements
- changed trade routes
- altered relationships between communities

The world should remember significant consequences.

---

# Historical Memory

World Simulation should maintain limited historical state.

A region that experienced:

```text
Critical food shortage
```

may later recover to:

```text
Stable supply
```

but the earlier crisis may continue influencing:

- public trust
- stockpiling behavior
- political attitudes
- migration
- local preparedness
- community relationships

Recovery does not erase history.

---

# Anti-Script Principle

Avoid logic such as:

```text
DAY 20 = POWER FAILURE

DAY 30 = RIOTS

DAY 40 = GOVERNMENT COLLAPSE
```

Prefer:

```text
POWER PRESSURE
+
LOW MAINTENANCE
+
FUEL SHORTAGE
+
FAILED REDUNDANCY
=
INCREASED FAILURE RISK
```

and:

```text
SUPPLY SHORTAGE
+
LOW TRUST
+
HIGH FEAR
+
WEAK AUTHORITY
=
INCREASED UNREST RISK
```

The world should produce events because conditions support them.

---

# Anti-Doom Principle

Likewise, avoid assuming every negative state must escalate.

For example:

```text
Food Supply: Degraded
```

does not automatically become:

```text
Food Supply: Critical
```

Possible outcomes include:

```text
rationing
local production
external assistance
reduced demand
alternative supply routes
community distribution
recovery
```

Adaptation is part of the simulation.

---

# Design Objective

The ideal World Simulation produces situations where the player can look at an event and think:

**"Of course that happened."**

Not because the event was predictable.

But because the world conditions make the event understandable.

---

# Proposed System Files

The World Simulation system should initially contain:

```text
Canon/
└── Systems/
    └── World_Simulation/
        ├── README.md
        ├── World_State.md
        ├── Regional_State.md
        ├── Infrastructure_State.md
        ├── Information_State.md
        ├── Authority_State.md
        ├── Population_State.md
        └── Escalation_and_Recovery.md
```

Additional files should only be created when a system becomes complex enough to require separation.

---

# File Responsibilities

## World_State.md

Defines the global structure of the simulation state.

Includes:

- world-level variables
- simulation hierarchy
- state inheritance
- global pressures
- cross-regional effects

---

## Regional_State.md

Defines how individual regions are represented.

Includes:

- regional variables
- resilience
- regional dependencies
- neighboring-region influence
- regional divergence

---

## Infrastructure_State.md

Defines how infrastructure conditions interact with World Simulation.

Includes:

- infrastructure health
- dependency chains
- service degradation
- repair
- redundancy
- infrastructure pressure

This file should integrate existing Infrastructure Monitoring Levels rather than duplicate them.

---

## Information_State.md

Defines:

- information reliability
- public knowledge
- rumor
- misinformation
- verification
- information delay
- perceived versus actual state

---

## Authority_State.md

Defines:

- government capability
- institutional legitimacy
- command effectiveness
- regional authority
- emergency powers
- decentralization

---

## Population_State.md

Defines:

- population confidence
- fear
- movement
- cooperation
- unrest
- workforce availability
- community behavior

---

## Escalation_and_Recovery.md

Defines how world states move in both directions.

Includes:

- pressure
- thresholds
- resilience
- cascading failures
- stabilization
- adaptation
- recovery
- long-term transformation

---

# Development Order

Recommended implementation order:

```text
README.md
   ↓
World_State.md
   ↓
Regional_State.md
   ↓
Infrastructure_State.md
   ↓
Information_State.md
   ↓
Authority_State.md
   ↓
Population_State.md
   ↓
Escalation_and_Recovery.md
```

This order builds from the general simulation model toward increasingly specific behavior.

---

# Canon Rules

The following principles are currently canonical for World Simulation:

1. The world continues independently of the player.
2. Different regions may exist in different states simultaneously.
3. Major systems influence one another.
4. Human responses are part of the simulation.
5. Degradation is not automatically irreversible.
6. Recovery is always theoretically possible.
7. Actual conditions and perceived conditions may differ.
8. Information travels with delay and uncertainty.
9. The player influences the world without controlling the entire world.
10. World events should emerge from conditions rather than fixed timers.
11. Historical consequences should persist.
12. Simulation complexity should serve gameplay rather than exist for its own sake.
13. Existing canonical systems should be integrated rather than duplicated.
14. World Simulation defines possibilities and processes; Canon defines established historical facts.

---

# Guiding Question

Every World Simulation mechanic should ultimately answer:

**If the player did nothing, what would this part of the world do next — and why?**

If the system cannot answer that question, it is probably not yet functioning as a world simulation.

---

# Current Status

```text
WORLD SIMULATION
Status: FOUNDATION DEFINED

README.md                  COMPLETE
World_State.md             PENDING
Regional_State.md          PENDING
Infrastructure_State.md    PENDING
Information_State.md       PENDING
Authority_State.md         PENDING
Population_State.md        PENDING
Escalation_and_Recovery.md PENDING
```

---

# Next Document

The next recommended document is:

```text
Canon/Systems/World_Simulation/World_State.md
```

Its purpose will be to define the actual data model that represents the living world.

README establishes the philosophy.

**World_State.md begins turning that philosophy into a system.**