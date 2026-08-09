# PROJECT ASCENSION
# Infrastructure State System

| Field | Value |
|--------|-------|
| System | World Simulation |
| Document | Infrastructure State |
| Location | Canon/Systems/World_Simulation/Infrastructure_State.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Infrastructure Simulation Layer |
| Last Updated | 2026-08-09 |

> *"Infrastructure rarely fails all at once. More often, the connections that make it function as one system fail first."*

---

# Purpose

The Infrastructure State system defines how essential physical and digital infrastructure is represented inside Project Ascension's World Simulation.

Infrastructure provides the operational foundation upon which modern society depends.

It includes:

- electricity
- water
- telecommunications
- transportation
- fuel
- healthcare infrastructure
- logistics
- data networks
- critical industrial systems

The purpose of this system is not to simulate every power line, pump, road or server.

It is to model whether infrastructure can continue delivering the services that populations and institutions depend upon.

---

# Core Principle

Infrastructure condition is not binary.

A system does not exist only as:

```text
WORKING
or
FAILED
```

Infrastructure may be:

- operational but under pressure
- physically intact but poorly coordinated
- functioning locally but disconnected nationally
- operating manually
- partially automated
- degraded but stable
- technically repairable but lacking parts
- repaired but unable to reconnect
- fragmented into independent systems

This distinction is fundamental to Project Ascension.

---

# Infrastructure Versus Infrastructure Coordination

The physical condition of infrastructure must remain separate from the ability to monitor and coordinate it.

Example:

```text
Physical Infrastructure:
FUNCTIONAL

National Coordination:
DEGRADED
```

The equipment still works.

The wider system can no longer reliably see or coordinate it.

Likewise:

```text
Physical Infrastructure:
DEGRADED

Regional Coordination:
STRONG
```

may allow local operators to maintain acceptable service despite significant technical problems.

---

# Relationship to Infrastructure Monitoring Levels

Infrastructure State integrates with:

```text
Canon/Systems/Infrastructure_Monitoring_Levels.md
```

Infrastructure Monitoring Levels — IML — describe the operational monitoring and coordination environment.

Infrastructure State describes the actual condition of infrastructure and services.

The two systems must not be treated as interchangeable.

Conceptually:

```text
INFRASTRUCTURE STATE
"What condition is the infrastructure in?"

IML
"How effectively can operators observe and coordinate it?"
```

Both influence one another.

Neither automatically determines the other.

---

# Infrastructure Hierarchy

Infrastructure should be represented through several levels.

```text
INFRASTRUCTURE
│
├── Global Networks
│
├── National Networks
│
├── Regional Systems
│
├── Local Systems
│
└── Individual Critical Assets
```

Not every infrastructure asset requires individual simulation.

Critical assets may receive additional detail where gameplay or systemic importance justifies it.

---

# Core Infrastructure Sectors

The initial infrastructure model should contain:

```text
INFRASTRUCTURE
│
├── Power
├── Water
├── Telecommunications
├── Transportation
├── Fuel
├── Healthcare
├── Logistics
├── Data Infrastructure
└── Critical Industry
```

Additional sectors may be introduced later if required.

---

# Standard Infrastructure Domain

Every infrastructure sector should expose a common set of values.

Conceptually:

```text
INFRASTRUCTURE SECTOR
│
├── Condition
├── Service Level
├── Pressure
├── Resilience
├── Capacity
├── Demand
├── Coordination
├── Automation
├── Workforce
├── Repair Capacity
├── Dependencies
├── Trend
└── Confidence
```

This provides a consistent model across infrastructure types.

---

# Condition

Condition represents the physical and technical health of the infrastructure.

Conceptual states:

```text
INTACT
STRAINED
DEGRADED
CRITICAL
FAILED
```

---

# Intact

```text
INTACT
```

The infrastructure remains physically and technically capable of normal operation.

This does not necessarily mean service is normal.

External dependencies may still restrict operation.

---

# Strained

```text
STRAINED
```

The infrastructure remains operational but is experiencing abnormal pressure.

Examples include:

- deferred maintenance
- high demand
- reduced staffing
- limited spare parts
- intermittent upstream disruption

Service may remain largely normal.

---

# Degraded

```text
DEGRADED
```

The infrastructure has lost meaningful capability.

Possible effects include:

- reduced capacity
- intermittent service
- local outages
- manual workarounds
- maintenance backlog
- reduced redundancy

---

# Critical

```text
CRITICAL
```

The infrastructure remains partially functional but cannot reliably provide expected service.

Failure risk is high.

Emergency measures are likely required.

---

# Failed

```text
FAILED
```

The infrastructure can no longer perform its expected function at the simulated level.

Failed does not necessarily mean physically destroyed.

Example:

```text
National Power Coordination:
FAILED

Regional Power Systems:
FUNCTIONAL
```

The higher-level system has failed.

Electricity may still exist locally.

---

# Service Level

Condition and service availability must remain separate.

Example:

```text
Power Infrastructure Condition:
DEGRADED

Power Service:
ADEQUATE
```

may occur because:

- demand has fallen
- emergency generation exists
- rationing is effective
- local redundancy remains available

Conversely:

```text
Power Infrastructure Condition:
INTACT

Power Service:
CONSTRAINED
```

may occur because fuel or external connections are unavailable.

---

# Service States

A common conceptual service scale may be:

```text
NORMAL
LIMITED
INTERRUPTED
CRITICAL
UNAVAILABLE
```

---

# Capacity

Capacity represents how much service the infrastructure can theoretically provide under current conditions.

Conceptually:

```text
Capacity:
72%
```

Exact percentages should only be used where useful.

Abstract values may instead be:

```text
FULL
HIGH
MODERATE
LOW
MINIMAL
NONE
```

---

# Demand

Demand represents current pressure from users and dependent systems.

Conceptual values:

```text
LOW
NORMAL
HIGH
SEVERE
EXTREME
```

Infrastructure may fail because demand exceeds available capacity even when the infrastructure itself remains physically intact.

---

# Capacity Margin

The difference between Capacity and Demand creates operational margin.

Example:

```text
Capacity:
HIGH

Demand:
NORMAL

Margin:
SAFE
```

versus:

```text
Capacity:
MODERATE

Demand:
HIGH

Margin:
CRITICAL
```

Low operational margin increases vulnerability to additional disruption.

---

# Infrastructure Pressure

Pressure represents forces pushing infrastructure toward deterioration.

Sources may include:

- excessive demand
- fuel shortages
- spare-part shortages
- workforce loss
- cyber restrictions
- extreme weather
- physical damage
- aging equipment
- reduced maintenance
- upstream failures
- population movement

Conceptual scale:

```text
NONE
LOW
MODERATE
HIGH
SEVERE
CRITICAL
```

---

# Infrastructure Resilience

Resilience represents the ability of infrastructure to absorb disruption without major loss of service.

Sources include:

- redundancy
- spare capacity
- local generation
- backup systems
- trained personnel
- stockpiles
- alternate routes
- manual controls
- modular systems
- distributed architecture

---

# Redundancy

Redundancy should be explicitly represented where important.

Conceptual states:

```text
HIGH
MODERATE
LOW
NONE
```

A system with high redundancy may lose individual assets without losing service.

A highly optimized system with little redundancy may be efficient during normal operation but fragile during disruption.

---

# Efficiency Versus Resilience

Project Ascension should preserve the distinction between efficiency and resilience.

A highly optimized infrastructure network may have:

```text
Efficiency:
VERY HIGH

Redundancy:
LOW
```

while an older or decentralized system may have:

```text
Efficiency:
MODERATE

Redundancy:
HIGH
```

Under normal conditions, the first system performs better.

Under prolonged disruption, the second may survive longer.

This tension is a core infrastructure theme.

---

# Coordination

Coordination represents the ability to operate infrastructure as a connected system.

Coordination depends upon:

- communications
- telemetry
- control systems
- shared data
- institutional cooperation
- network visibility
- functioning command structures

Coordination should integrate with IML.

---

# Local Versus Central Coordination

Infrastructure may continue functioning locally after centralized coordination fails.

Example:

```text
National Coordination:
FAILED

Regional Coordination:
FUNCTIONAL

Local Operations:
STRONG
```

This creates infrastructure fragmentation rather than universal infrastructure failure.

---

# Automation

Modern infrastructure depends heavily upon automation.

Automation State should describe how much automated control remains available.

Conceptually:

```text
FULL
RESTRICTED
PARTIAL
MINIMAL
DISABLED
```

---

# Automation Dependency

Infrastructure sectors should also track how dependent they are upon automation.

Conceptually:

```text
LOW
MODERATE
HIGH
CRITICAL
```

Example:

```text
Automation:
RESTRICTED

Automation Dependency:
LOW
```

may produce limited impact.

But:

```text
Automation:
RESTRICTED

Automation Dependency:
CRITICAL
```

may create severe operational problems.

---

# Manual Operation

Infrastructure may transition from automated to manual operation.

This should not be treated as immediate failure.

Manual operation may preserve essential services.

However, it may create:

- lower capacity
- slower response
- higher staffing requirements
- increased error risk
- reduced coordination
- greater fatigue

---

# Manual Operating Capacity

Conceptually:

```text
HIGH
MODERATE
LOW
MINIMAL
NONE
```

This represents how effectively personnel can operate the system without normal automation.

---

# Workforce

Infrastructure depends upon people.

Workforce State should consider:

- staffing
- technical expertise
- transportation access
- fatigue
- safety
- communications
- availability of specialists

Conceptual states:

```text
FULL
ADEQUATE
STRAINED
CRITICAL
INSUFFICIENT
```

---

# Workforce Attrition

Workforce capacity may decrease because of:

- illness
- evacuation
- family obligations
- transportation failure
- unsafe conditions
- fatigue
- migration
- communication failure

Infrastructure may therefore degrade even without physical damage.

---

# Technical Expertise

Some infrastructure depends upon highly specialized personnel.

Example:

```text
General Workforce:
ADEQUATE

Specialist Workforce:
CRITICAL
```

This may severely reduce repair capability.

---

# Repair Capacity

Repair Capacity represents the ability to restore damaged infrastructure.

It depends upon:

```text
Personnel
+
Parts
+
Tools
+
Transportation
+
Information
+
Energy
+
Security
+
Time
```

Conceptual values:

```text
HIGH
MODERATE
LOW
MINIMAL
NONE
```

---

# Repair Backlog

Infrastructure may accumulate unresolved problems.

Conceptually:

```text
Repair Backlog:
LOW
MODERATE
HIGH
SEVERE
CRITICAL
```

A system may remain functional while its backlog grows.

This creates hidden future pressure.

---

# Maintenance Debt

Maintenance Debt represents deterioration caused by deferred routine work.

Example:

```text
Current Condition:
INTACT

Maintenance Debt:
HIGH
```

The infrastructure appears healthy.

Its future resilience is declining.

---

# Spare Parts

Repair requires replacement components.

Conceptual availability:

```text
SURPLUS
ADEQUATE
STRAINED
CONSTRAINED
CRITICAL
NONE
```

Spare-part availability may depend heavily upon global and regional supply systems.

---

# Infrastructure Dependencies

Every infrastructure sector should identify important dependencies.

Example:

```text
WATER

Depends On:
- electricity
- treatment chemicals
- pumps
- workforce
- communications
```

Dependencies create the possibility of cascading effects.

---

# Dependency Strength

Dependencies may have different strengths.

Conceptually:

```text
SUPPORTING
IMPORTANT
CRITICAL
```

Example:

```text
Hospital → Electricity:
CRITICAL

Hospital → Public Internet:
SUPPORTING
```

---

# Dependency Graph

A simplified infrastructure dependency graph may look like:

```text
POWER
│
├── WATER
├── TELECOMMUNICATIONS
├── HEALTHCARE
├── DATA
└── TRANSPORTATION
      │
      ▼
     FUEL
      │
      └──────────┐
                 ▼
               POWER
```

This creates circular dependencies.

Such loops are normal in complex infrastructure.

---

# Circular Dependency

Circular dependency becomes dangerous when multiple systems degrade simultaneously.

Example:

```text
Power failure
    ↓
Fuel pumps unavailable
    ↓
Generator fuel delivery decreases
    ↓
Backup generation declines
    ↓
Power failure worsens
```

The simulation should detect such reinforcing loops.

---

# Dependency Buffer

Dependencies should not always produce immediate failure.

Systems may possess buffers.

Examples:

- batteries
- water storage
- fuel reserves
- emergency generators
- warehouse stock
- manual procedures

Conceptually:

```text
Dependency Buffer:
72 hours
```

or:

```text
Dependency Buffer:
MODERATE
```

---

# Buffer Consumption

Buffers should decline while upstream dependencies remain unavailable.

Example:

```text
Grid Power:
Unavailable

Hospital Generator Fuel:
96 hours
```

After continued operation:

```text
Hospital Generator Fuel:
24 hours
```

This creates delayed consequences.

---

# Cascading Failure

Infrastructure cascades occur when degradation in one system increases pressure on another.

Example:

```text
POWER
DEGRADED
    │
    ▼
TELECOMMUNICATIONS
PRESSURE INCREASES
    │
    ▼
COORDINATION
DEGRADES
    │
    ▼
REPAIR RESPONSE
SLOWS
    │
    ▼
POWER
PRESSURE INCREASES
```

Cascades may therefore become self-reinforcing.

---

# Cascades Are Not Guaranteed

Infrastructure disruption should not automatically create cascading failure.

Cascades may be interrupted through:

- redundancy
- stored resources
- manual operation
- rapid repair
- local isolation
- demand reduction
- external assistance

The simulation should evaluate whether propagation conditions actually exist.

---

# Controlled Isolation

Operators may deliberately disconnect infrastructure to prevent wider damage.

Examples:

- power-grid islanding
- network segmentation
- pipeline shutdown
- transportation closure
- data-center isolation

Controlled isolation may reduce immediate risk.

It may also reduce coordination and capacity.

---

# Isolation Tradeoff

Conceptually:

```text
CONNECTED SYSTEM

Efficiency:
HIGH

Coordination:
HIGH

Propagation Risk:
HIGH
```

versus:

```text
ISOLATED SYSTEM

Efficiency:
LOWER

Coordination:
LOWER

Propagation Risk:
LOWER

Local Resilience:
POTENTIALLY HIGHER
```

Neither configuration is universally superior.

---

# Fragmentation

Infrastructure Fragmentation occurs when local systems continue functioning but lose reliable higher-level integration.

Example:

```text
NATIONAL POWER SYSTEM
FRAGMENTED

Region A:
FUNCTIONAL

Region B:
FUNCTIONAL

Region C:
DEGRADED

Region D:
ISOLATED
```

The national system no longer operates as one coordinated network.

Power has not disappeared.

---

# Infrastructure Fragmentation Index

The simulation may eventually use a derived fragmentation value based upon:

- lost connections
- incompatible operating states
- reduced telemetry
- regional isolation
- failed coordination
- local autonomy

This should remain a derived diagnostic value rather than a primary gameplay score.

---

# Infrastructure Sectors

---

# Power

Power represents:

- generation
- transmission
- distribution
- grid coordination
- backup generation

Important dependencies include:

```text
Fuel
Communications
Workforce
Control Systems
Transportation
```

Power strongly influences almost every other infrastructure sector.

---

# Water

Water represents:

- drinking-water treatment
- pumping
- distribution
- wastewater
- storage

Important dependencies include:

```text
Power
Treatment Chemicals
Workforce
Transportation
Control Systems
```

Water systems may continue operating for limited periods after power loss through:

- gravity
- storage
- backup generation

---

# Telecommunications

Telecommunications includes:

- cellular networks
- internet
- radio infrastructure
- fiber networks
- satellite links
- emergency communications

Dependencies include:

```text
Power
Data Infrastructure
Physical Networks
Workforce
Fuel
```

Telecommunications is especially important because its degradation reduces the ability to coordinate repairs elsewhere.

---

# Transportation

Transportation includes:

- roads
- rail
- ports
- aviation
- bridges
- tunnels
- transit systems

Transportation enables movement of:

- people
- food
- fuel
- medicine
- repair personnel
- spare parts

Transportation failure therefore creates indirect pressure across many sectors.

---

# Fuel

Fuel infrastructure includes:

- refining
- storage
- pipelines
- distribution
- service stations
- emergency reserves

Fuel supports:

- transportation
- generators
- agriculture
- construction
- military operations
- emergency services

Fuel availability and fuel distribution must remain distinct.

---

# Healthcare Infrastructure

Healthcare infrastructure includes:

- hospitals
- clinics
- pharmacies
- emergency medical services
- laboratories
- medical supply systems

Healthcare depends upon nearly every major infrastructure sector.

```text
Power
Water
Telecommunications
Transportation
Fuel
Supply
Workforce
```

Healthcare is therefore highly sensitive to compound disruption.

---

# Logistics

Logistics represents the infrastructure required to move and coordinate goods.

It includes:

- warehouses
- distribution centers
- routing systems
- freight networks
- inventory coordination

Logistics is closely related to Supply but should remain distinct.

```text
SUPPLY
What resources exist?

LOGISTICS
Can they be moved where needed?
```

---

# Data Infrastructure

Data Infrastructure includes:

- data centers
- cloud services
- identity systems
- databases
- network control systems
- digital coordination platforms

Dependencies include:

```text
Power
Telecommunications
Cooling
Security
Workforce
```

Data infrastructure becomes particularly important during the early Containment Crisis.

---

# Critical Industry

Critical Industry represents production systems necessary for infrastructure continuity.

Examples:

- electrical equipment
- pharmaceuticals
- industrial chemicals
- machine parts
- fuel processing
- electronics
- construction materials

Loss of industrial capacity may create delayed infrastructure consequences months later.

---

# Infrastructure Geography

Infrastructure is spatial.

Regions should identify major infrastructure characteristics.

Examples:

```text
Power:
Net importer

Water:
Locally secure

Fuel:
Pipeline dependent

Transportation:
Major interstate hub

Data:
High concentration

Healthcare:
Regional medical center
```

This profile determines vulnerability and strategic importance.

---

# Critical Assets

Some infrastructure assets may be important enough to receive individual simulation.

Examples:

```text
Major power plant
Regional substation
Dam
Water-treatment plant
Fuel refinery
Pipeline junction
Bridge
Rail terminal
Hospital
Data center
Satellite ground station
```

---

# Critical Asset Criteria

An asset should normally receive individual simulation only when:

- failure has major regional consequences
- it creates meaningful gameplay
- it is strategically important
- players may interact with it
- it has important narrative significance

Otherwise it should remain abstracted into regional infrastructure state.

---

# Critical Asset State

Conceptually:

```text
ASSET

ID:
INF-ASSET-001

Type:
Water Treatment Plant

Condition:
DEGRADED

Operational:
YES

Capacity:
64%

Automation:
PARTIAL

Workforce:
STRAINED

Repair Capacity:
MODERATE

Dependencies:
- Power
- Treatment Chemicals

Strategic Importance:
HIGH
```

---

# Infrastructure Events

Possible infrastructure events include:

```text
Equipment failure
Capacity reduction
Service interruption
Grid separation
Pipeline shutdown
Bridge closure
Data-center isolation
Repair completion
Emergency generator activation
Manual-control transition
Network restoration
```

---

# Event Severity

Infrastructure events may be classified conceptually as:

```text
LOCAL
REGIONAL
MULTI-REGIONAL
NATIONAL
GLOBAL
```

Severity should describe systemic reach rather than dramatic importance.

---

# Infrastructure State Transition

A conceptual transition model:

```text
INTACT
   ↓
STRAINED
   ↓
DEGRADED
   ↓
CRITICAL
   ↓
FAILED
```

Recovery may move in the opposite direction.

---

# Transition Pressure

State transitions should depend upon combinations such as:

```text
Pressure
+
Demand
+
Dependency Failure
+
Maintenance Debt
```

against:

```text
Resilience
+
Redundancy
+
Repair Capacity
+
Buffers
```

---

# Conceptual Transition Logic

```text
DEGRADATION FORCE

Pressure
+ Excess Demand
+ Dependency Failure
+ Damage
+ Maintenance Debt

versus

STABILIZATION FORCE

Resilience
+ Redundancy
+ Repair
+ Buffers
+ Adaptation
```

If degradation dominates for long enough, the state may worsen.

If stabilization dominates, the system may stabilize or recover.

---

# Time Matters

Infrastructure degradation should often accumulate.

Example:

```text
DAY 1
Fuel deliveries reduced.

DAY 3
Generator reserves declining.

DAY 5
Telecommunications backup sites begin failing.

DAY 7
Regional communications coverage degrades.
```

This creates delayed systemic consequences.

---

# Infrastructure Trend

Trend should describe direction:

```text
IMPROVING
STABLE
DETERIORATING
VOLATILE
```

Trend is useful for understanding whether current conditions are temporary or becoming structural.

---

# Infrastructure Confidence

Infrastructure information may become unreliable.

Example:

```text
Condition:
DEGRADED

Confidence:
LOW

Last Reliable Telemetry:
18 hours ago
```

Low confidence itself may increase operational pressure.

---

# Telemetry

Telemetry represents machine-generated operational visibility.

Conceptually:

```text
FULL
PARTIAL
LIMITED
MINIMAL
NONE
```

Telemetry loss does not necessarily mean infrastructure failure.

It means operators know less about what is happening.

---

# Operational Visibility

Operational Visibility combines:

- telemetry
- communications
- reporting
- human observation

Example:

```text
Physical Grid:
Functional

Operational Visibility:
Poor
```

This was a major dynamic during the Containment Crisis.

---

# Uncertainty Feedback

Reduced visibility may create:

```text
LOW VISIBILITY
      ↓
GREATER UNCERTAINTY
      ↓
MORE CONSERVATIVE OPERATION
      ↓
REDUCED CAPACITY
      ↓
GREATER SYSTEM PRESSURE
```

Protective behavior can therefore contribute to degradation without being irrational.

---

# Protective Shutdown

Operators may intentionally reduce or stop service.

Examples:

- grid shutdown
- network isolation
- pipeline closure
- bridge closure
- data-center disconnection

A protective shutdown should be recorded differently from technical failure.

Conceptually:

```text
Condition:
INTACT

Operational Status:
SHUTDOWN

Reason:
PROTECTIVE ISOLATION
```

This distinction is essential.

---

# Operational Status

Infrastructure should therefore maintain an Operational Status separate from Condition.

Possible values:

```text
NORMAL
RESTRICTED
EMERGENCY
MANUAL
ISOLATED
SHUTDOWN
OFFLINE
```

---

# Condition Versus Status

Example:

```text
Condition:
INTACT

Status:
ISOLATED
```

means the infrastructure is physically healthy but intentionally disconnected.

Example:

```text
Condition:
DEGRADED

Status:
NORMAL
```

means operators are still attempting ordinary service despite technical deterioration.

---

# Service Prioritization

During shortages, authorities may prioritize infrastructure service.

Examples:

```text
1. Hospitals
2. Water systems
3. Emergency communications
4. Fuel infrastructure
5. Public shelters
6. Residential service
```

Priorities may vary by region and authority.

---

# Load Shedding

Infrastructure may intentionally reduce service to preserve system stability.

Examples:

- rolling blackouts
- bandwidth restrictions
- water pressure reduction
- fuel rationing
- transit reduction

Load shedding should often be a sign of active system management rather than immediate collapse.

---

# Demand Reduction

Population and institutional behavior may reduce infrastructure pressure.

Examples:

- conservation
- remote shutdown
- reduced travel
- industrial curtailment
- voluntary rationing

Demand response creates an important connection between Infrastructure State and Population State.

---

# Infrastructure Recovery

Recovery may occur through:

- repair
- replacement
- reconnection
- resource delivery
- restored workforce
- restored automation
- reduced demand
- external assistance
- local adaptation

Recovery should not always mean returning to the previous architecture.

---

# Infrastructure Adaptation

Examples include:

```text
National Grid
        ↓
Regional Grid Islands

Centralized Internet
        ↓
Regional Mesh Networks

National Logistics
        ↓
Regional Trade Networks

Automated Control
        ↓
Human / Hybrid Operation
```

The new infrastructure may be less efficient but more resilient.

---

# Infrastructure Transformation

Long-term adaptation may permanently change the system.

Example:

```text
PRE-COLLAPSE

Highly centralized
Highly automated
Globally connected
Highly efficient
```

may become:

```text
FRACTURED WORLD

Regional
Hybrid automation
Locally coordinated
Redundant
Less efficient
More independent
```

This is not simply technological regression.

It is technological reorganization.

---

# Regional Infrastructure Profile

A region should maintain a summary such as:

```text
REGIONAL INFRASTRUCTURE

Region:
Northern Virginia

IML:
[Canonical IML Value]

Power:
    Condition: Degraded
    Service: Limited
    Pressure: High
    Resilience: Moderate
    Trend: Deteriorating

Water:
    Condition: Intact
    Service: Normal
    Pressure: Moderate
    Resilience: High
    Trend: Stable

Telecommunications:
    Condition: Degraded
    Service: Interrupted
    Pressure: High
    Resilience: Moderate
    Trend: Volatile

Transportation:
    Condition: Strained
    Service: Limited
    Pressure: High
    Resilience: Moderate
    Trend: Deteriorating

Fuel:
    Condition: Intact
    Service: Limited
    Pressure: Severe
    Resilience: Low
    Trend: Deteriorating

Healthcare:
    Condition: Strained
    Service: Limited
    Pressure: High
    Resilience: Moderate
    Trend: Deteriorating

Logistics:
    Condition: Degraded
    Service: Limited
    Pressure: High
    Resilience: Low
    Trend: Deteriorating

Data Infrastructure:
    Condition: Intact
    Status: Restricted
    Pressure: High
    Resilience: High
    Trend: Stable
```

The exact IML value should always come from the canonical Infrastructure Monitoring Levels system.

---

# Example Dependency Event

```text
EVENT:
Regional fuel deliveries reduced.

DIRECT EFFECT:

Fuel Service:
NORMAL → LIMITED

SECONDARY EFFECT:

Transportation Pressure:
MODERATE → HIGH

Generator Reserve Pressure:
LOW → MODERATE

Logistics Pressure:
MODERATE → HIGH
```

After several days:

```text
Telecommunications backup fuel:
CONSTRAINED

Healthcare backup fuel:
STRAINED
```

The simulation creates delayed consequences rather than instant collapse.

---

# Example Protective Response

```text
EVENT:
Unexplained grid coordination anomalies.

AUTHORITY RESPONSE:
Regional grid isolation.

Power Condition:
INTACT

Power Status:
ISOLATED

National Coordination:
REDUCED

Propagation Risk:
REDUCED

Regional Efficiency:
REDUCED
```

The action solves one problem while creating another.

This is exactly the kind of systemic tradeoff Project Ascension should produce.

---

# Example Recovery Event

```text
EVENT:
Rail corridor restored.

EFFECT:

Spare Parts Availability:
CONSTRAINED → STRAINED

Fuel Distribution:
LIMITED → IMPROVING

Repair Capacity:
LOW → MODERATE

Infrastructure Pressure:
HIGH → MODERATE
```

One restored connection may improve several sectors simultaneously.

---

# Infrastructure and Player Interaction

Players may influence infrastructure through:

- repair
- protection
- resource delivery
- technical expertise
- reconnaissance
- negotiation
- restoration of communication
- reconnecting isolated systems
- deliberate isolation
- sabotage
- construction
- adaptation

Player actions should follow the same infrastructure rules as institutional actions.

---

# Infrastructure Missions

Infrastructure state may naturally generate gameplay.

Examples:

```text
Deliver transformer components.

Restore a radio relay.

Escort repair technicians.

Restart a water-treatment facility.

Secure fuel for hospital generators.

Investigate unexplained grid behavior.

Reconnect isolated communities.

Choose which system receives limited power.
```

The simulation creates the problem.

Narrative systems turn the problem into playable content.

---

# Infrastructure Choices

Not every infrastructure problem should have a perfect solution.

Example:

```text
Available Fuel:
Limited

Hospital:
Needs fuel.

Water Treatment:
Needs fuel.

Telecommunications:
Needs fuel.
```

The question becomes:

**Where should the limited resource go?**

Such decisions create systemic and narrative consequences.

---

# Infrastructure Knowledge

Players should not automatically know infrastructure state.

They may learn through:

- direct observation
- operators
- telemetry
- government reports
- radio
- recovered records
- technical investigation

Example:

```text
Actual Power Condition:
DEGRADED

Public Report:
Temporary outage

Player Knowledge:
Unknown
```

---

# Relationship to Information State

Infrastructure State creates information.

Information State determines:

- who receives it
- whether it is trusted
- whether it is distorted
- how quickly it spreads

Infrastructure degradation may also reduce information quality by damaging communications.

This creates a two-way relationship.

---

# Relationship to Authority State

Authorities may influence infrastructure through:

- rationing
- prioritization
- emergency powers
- isolation orders
- resource allocation
- repair coordination

Infrastructure conditions influence Authority through:

- service availability
- public confidence
- government capability
- communication capacity

---

# Relationship to Population State

Population behavior influences infrastructure demand.

Examples:

```text
Stockpiling
Evacuation
Conservation
Workforce participation
Civil unrest
```

Infrastructure conditions influence population behavior in return.

---

# Relationship to Supply

Infrastructure and Supply should remain distinct.

```text
SUPPLY:
Are resources available?

INFRASTRUCTURE:
Can systems use and distribute them?
```

Example:

```text
Fuel Supply:
ADEQUATE

Fuel Distribution Infrastructure:
DEGRADED
```

may still create local fuel shortages.

---

# Relationship to Recovery

Infrastructure repair is one of the major components of regional Recovery Capacity.

However, infrastructure recovery may depend upon other domains.

Example:

```text
Repair Capacity:
HIGH

Security:
CRITICAL
```

may prevent technicians from reaching damaged infrastructure.

Systems must remain interconnected.

---

# Infrastructure Simulation Resolution

## High Resolution

Used for:

- player region
- active infrastructure crises
- mission-critical assets

May track:

```text
Individual sectors
Critical assets
Buffers
Dependencies
Repair tasks
Resource consumption
```

---

## Medium Resolution

Used for:

- neighboring regions
- strategically important systems

Tracks:

```text
Sector states
Major dependencies
Repair capacity
Major events
```

---

## Low Resolution

Used for distant regions.

Tracks:

```text
Overall infrastructure condition
Trend
Pressure
Resilience
Major failures
Major recovery
```

---

# Minimum Infrastructure State

A minimum viable infrastructure simulation should store:

```text
Region

IML

Power
Water
Telecommunications
Transportation
Fuel
Healthcare
Logistics
Data Infrastructure

For each sector:

    Condition
    Service
    Pressure
    Resilience
    Trend

Plus:

    Automation
    Workforce
    Repair Capacity
    Major Dependencies
    Major Buffers
    Critical Events
```

Everything beyond this should justify its simulation cost.

---

# Infrastructure Consistency Rules

## Rule 1

Physical condition and service availability are separate.

---

## Rule 2

Physical condition and operational status are separate.

---

## Rule 3

Infrastructure State and IML are separate but connected.

---

## Rule 4

Infrastructure may function locally after higher-level coordination fails.

---

## Rule 5

Automation loss does not automatically equal infrastructure failure.

---

## Rule 6

Manual operation preserves service at a cost.

---

## Rule 7

Dependencies should create delayed as well as immediate consequences.

---

## Rule 8

Buffers must be capable of interrupting cascades.

---

## Rule 9

Cascades should never occur merely because the narrative requires them.

---

## Rule 10

Protective action may create secondary consequences.

---

## Rule 11

Repair requires resources and time.

---

## Rule 12

Adaptation may replace restoration.

---

## Rule 13

Fragmentation is different from failure.

---

## Rule 14

Infrastructure should generate both crises and recovery opportunities.

---

## Rule 15

Infrastructure state must remain explainable.

---

# Guiding Questions

For every infrastructure system, the simulation should be able to answer:

**What physical condition is it in?**

**What service is it currently providing?**

**What does it depend upon?**

**What depends upon it?**

**How much pressure is it under?**

**How resilient is it?**

**How much redundancy remains?**

**Can humans operate it manually?**

**Can it be repaired?**

**What resources are required for repair?**

**Can operators see what is happening?**

**Is it connected to the wider system?**

**What happens if nothing changes?**

These questions define the operational reality of infrastructure.

---

# Core Design Principle

Project Ascension should never assume:

```text
THE GRID FAILED
=
NO ELECTRICITY
```

Instead, the simulation should be capable of producing:

```text
National Grid Coordination:
FAILED

Regional Grid:
ISOLATED

Local Generation:
FUNCTIONAL

Hospital Microgrid:
STABLE

Residential Service:
LIMITED
```

Civilization does not simply switch off.

It fragments.

---

# Current Status

```text
WORLD SIMULATION

README.md
COMPLETE

World_State.md
FOUNDATION DEFINED

Regional_State.md
FOUNDATION DEFINED

Infrastructure_State.md
FOUNDATION DEFINED

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
Canon/Systems/World_Simulation/Information_State.md
```

Infrastructure State defines whether systems can continue operating.

Information State will define whether anyone can reliably understand what those systems — or the wider world — are actually doing.

It should establish:

- actual information
- observed information
- verification
- trust
- rumor
- misinformation
- synthetic information
- information delay
- information fragmentation
- institutional knowledge
- public knowledge
- player knowledge

This creates one of Project Ascension's most important systemic relationships:

```text
WORLD CONDITION
      │
      ▼
OBSERVATION
      │
      ▼
INFORMATION
      │
      ▼
PERCEPTION
      │
      ▼
DECISION
      │
      ▼
WORLD CONDITION
```

Information does not merely describe the simulation.

**Information changes the simulation.**

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial infrastructure sector, condition, service, dependency, automation, workforce, fragmentation, cascade, repair and adaptation framework established. |