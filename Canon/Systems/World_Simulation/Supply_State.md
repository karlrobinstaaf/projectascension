# PROJECT ASCENSION
# Supply State System

| Field | Value |
|--------|-------|
| System | World Simulation |
| Document | Supply State |
| Location | Canon/Systems/World_Simulation/Supply_State.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Resource Availability, Production, Distribution and Strategic Reserves |
| Last Updated | 2026-08-09 |

> *"A resource does not matter because it exists. It matters because it can reach the place where it is needed."*

---

# Purpose

The Supply State system defines how essential resources are represented inside Project Ascension's World Simulation.

Supply includes:

- food
- water
- fuel
- medicine
- industrial materials
- spare parts
- agricultural inputs
- batteries
- critical chemicals
- other strategically important goods

The system determines whether resources are:

- produced
- imported
- stored
- transported
- distributed
- consumed
- rationed
- depleted
- redirected
- restored

Supply connects infrastructure, population, authority, trade and recovery.

---

# Core Principle

Supply is not a single inventory value.

A resource may exist while remaining unavailable.

Conceptually:

```text
RESOURCE EXISTS
      │
      ▼
CAN IT BE PRODUCED?
      │
      ▼
CAN IT BE STORED?
      │
      ▼
CAN IT BE TRANSPORTED?
      │
      ▼
CAN IT BE DISTRIBUTED?
      │
      ▼
CAN PEOPLE ACCESS IT?
```

Failure at any stage may create effective shortage.

---

# Supply Versus Logistics

Supply and Logistics must remain distinct.

```text
SUPPLY
What resources exist and are potentially available?

LOGISTICS
Can those resources be moved to where they are needed?
```

Example:

```text
Regional Food Supply:
ADEQUATE

Logistics:
DEGRADED
```

may still produce:

```text
Local Food Shortages
```

---

# Supply Versus Infrastructure

Infrastructure enables supply.

Examples:

```text
Power
Transportation
Fuel
Warehousing
Data Systems
Telecommunications
```

Supply in turn supports infrastructure through:

```text
Fuel
Replacement Parts
Industrial Materials
Chemicals
```

The relationship is bidirectional.

---

# Supply Hierarchy

Supply may be represented across several levels.

```text
SUPPLY
│
├── Global
├── National
├── Regional
├── Local
└── Household / Facility
```

World Simulation should normally operate at Regional level.

Critical facilities or missions may use Local or Facility-level detail.

---

# Core Supply Categories

The initial Supply model should include:

```text
SUPPLY
│
├── Food
├── Water
├── Fuel
├── Medicine
├── Spare Parts
├── Industrial Materials
├── Agricultural Inputs
├── Energy Storage
└── Critical Chemicals
```

Additional categories may be introduced when justified.

---

# Standard Supply Domain

Each Supply category should expose:

```text
SUPPLY CATEGORY
│
├── Availability
├── Production
├── Imports
├── Inventory
├── Strategic Reserves
├── Distribution Capacity
├── Demand
├── Consumption
├── Dependency
├── Pressure
├── Resilience
├── Trend
└── Confidence
```

---

# Availability

Availability represents the amount of usable resource currently accessible to the region.

Conceptual states:

```text
SURPLUS
ADEQUATE
STRAINED
CONSTRAINED
CRITICAL
UNAVAILABLE
```

---

# Surplus

```text
SURPLUS
```

The region possesses more usable supply than current demand requires.

Potential consequences include:

- export
- stockpiling
- reserve building
- price reduction
- diplomatic leverage

---

# Adequate

```text
ADEQUATE
```

Supply meets normal demand with reasonable margin.

---

# Strained

```text
STRAINED
```

Supply remains sufficient but operational margin is reduced.

Possible signs include:

- higher prices
- reduced variety
- delayed deliveries
- smaller inventories
- reduced reserves

---

# Constrained

```text
CONSTRAINED
```

Supply is insufficient for unrestricted normal consumption.

Possible responses include:

- rationing
- prioritization
- conservation
- reduced commercial use

---

# Critical

```text
CRITICAL
```

Supply cannot reliably meet essential demand.

Authorities and communities must decide who or what receives limited resources.

---

# Unavailable

```text
UNAVAILABLE
```

The resource cannot currently be accessed at the simulated level.

This does not necessarily mean the resource does not physically exist elsewhere.

---

# Production

Production represents how much of a resource the region can generate internally.

Examples:

```text
Agriculture
Refining
Pharmaceutical Production
Manufacturing
Water Treatment
Battery Production
```

Conceptual states:

```text
SURPLUS
HIGH
MODERATE
LOW
MINIMAL
NONE
```

---

# Local Production

Local production increases resilience by reducing external dependency.

However, production itself may depend upon:

- power
- fuel
- workforce
- machinery
- raw materials
- water
- transportation

Local production is therefore not equivalent to independence.

---

# Production Capacity Versus Output

Production Capacity and actual Output should remain separate.

Example:

```text
Production Capacity:
HIGH

Current Output:
LOW
```

Possible causes:

- fuel shortage
- missing workforce
- missing inputs
- power restriction

---

# Imports

Imports represent externally sourced supply.

Conceptual states:

```text
HIGH
MODERATE
LOW
MINIMAL
NONE
```

---

# Import Dependency

Import Dependency represents how dependent the region is upon incoming resources.

Conceptual values:

```text
LOW
MODERATE
HIGH
CRITICAL
```

Example:

```text
Food Import Dependency:
HIGH
```

does not mean the region has low food supply today.

It means supply is vulnerable to sustained external disruption.

---

# Inventory

Inventory represents immediately available stored resources.

Conceptually:

```text
HIGH
ADEQUATE
LOW
CRITICAL
DEPLETED
```

Inventory is a buffer.

---

# Inventory Days

Where useful, supply may use estimated duration.

Example:

```text
Hospital Oxygen:
4 days
```

or:

```text
Regional Fuel Inventory:
11 days at current consumption
```

Exact numbers should only be used where they improve gameplay or simulation.

---

# Strategic Reserves

Strategic Reserves are resources intentionally held outside normal consumption.

Examples include:

- national fuel reserves
- emergency medical stockpiles
- food reserves
- spare transformers
- treatment chemicals

Conceptual states:

```text
FULL
HIGH
MODERATE
LOW
CRITICAL
DEPLETED
```

---

# Reserve Release

Authorities may release strategic reserves to reduce immediate pressure.

Example:

```text
Fuel Availability:
CONSTRAINED

Strategic Reserve:
HIGH

Intervention:
Reserve release

Result:
Availability improves temporarily.
```

---

# Reserve Tradeoff

Using reserves solves current problems by reducing future resilience.

Conceptually:

```text
CURRENT PRESSURE
      ↓
RESERVE RELEASE
      ↓
CURRENT PRESSURE DECREASES
      ↓
FUTURE BUFFER DECREASES
```

There should be no free reserve use.

---

# Distribution Capacity

Distribution Capacity represents the ability to move resources from inventory or production to users.

It depends upon:

- transportation
- fuel
- workforce
- warehouses
- communications
- security
- information systems

Conceptual states:

```text
HIGH
FUNCTIONAL
STRAINED
LOW
CRITICAL
FAILED
```

---

# Supply Availability Versus Distribution

Example:

```text
Food Availability:
ADEQUATE

Distribution Capacity:
LOW
```

may create:

```text
Urban Shortages
Rural Surplus
```

Regional totals can conceal local scarcity.

---

# Demand

Demand represents current resource requirement.

Conceptual states:

```text
LOW
NORMAL
HIGH
SEVERE
EXTREME
```

Demand may increase through:

- population growth
- migration
- weather
- infrastructure failure
- emergency operations
- stockpiling

---

# Essential Demand

Supply should distinguish:

```text
TOTAL DEMAND
```

from:

```text
ESSENTIAL DEMAND
```

Example:

Fuel may be insufficient for normal civilian consumption but sufficient for:

- hospitals
- emergency services
- water systems
- critical transport

This creates prioritization choices.

---

# Consumption

Consumption represents actual use.

Consumption may differ from Demand due to:

- rationing
- conservation
- scarcity
- inability to access supply

Example:

```text
Demand:
HIGH

Consumption:
MODERATE
```

because rationing restricts use.

---

# Supply Margin

Supply Margin represents the difference between usable supply and essential demand.

Conceptually:

```text
SURPLUS
SAFE
NARROW
CRITICAL
DEFICIT
```

---

# Supply Pressure

Supply Pressure represents forces pushing availability toward worse states.

Sources may include:

- import disruption
- production loss
- migration
- stockpiling
- transportation failure
- workforce loss
- infrastructure failure
- conflict
- seasonal demand

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

# Supply Resilience

Supply Resilience represents the ability to absorb disruption.

Sources may include:

- local production
- diversified suppliers
- strategic reserves
- storage
- alternate routes
- low demand
- strong logistics
- substitution

---

# Supply Buffers

Important buffers include:

```text
Inventory
Strategic Reserves
Household Stock
Commercial Stock
Substitute Goods
```

Buffers delay shortage.

---

# Buffer Depletion

Conceptually:

```text
IMPORTS FAIL
    ↓
INVENTORY USED
    ↓
STRATEGIC RESERVE USED
    ↓
HOUSEHOLD STOCK USED
    ↓
VISIBLE SHORTAGE
```

Different buffers operate at different levels.

---

# Substitution

Some resources may be replaced.

Example:

```text
Gasoline shortage
      ↓
Rail transport increased
```

or:

```text
Imported medicine unavailable
      ↓
Alternative local medication used
```

Substitution increases resilience.

---

# Substitution Limits

Not all resources are interchangeable.

Examples:

- specialized medicine
- transformer equipment
- water-treatment chemicals
- aircraft parts

Low substitutability creates strategic vulnerability.

---

# Resource Criticality

Resources may possess different Criticality.

Conceptually:

```text
LOW
MODERATE
HIGH
CRITICAL
```

Criticality reflects consequences of shortage.

---

# Resource Dependency Graph

Supply chains may depend upon one another.

Example:

```text
AGRICULTURE
│
├── Fuel
├── Fertilizer
├── Water
├── Equipment Parts
└── Transportation
       │
       ▼
      FOOD
```

Food supply can therefore degrade because of shortages outside agriculture itself.

---

# Food Supply

Food includes:

- production
- imports
- processing
- storage
- distribution
- retail
- emergency reserves

Important dependencies include:

```text
Fuel
Transportation
Electricity
Water
Labor
Agricultural Inputs
```

---

# Food Production

Regional food production should consider:

- farmland
- season
- labor
- fertilizer
- fuel
- machinery
- water
- storage

Food production changes slowly compared with many other resources.

---

# Food Distribution

Food shortage may occur quickly if distribution fails even when production remains intact.

Example:

```text
Regional Food Production:
HIGH

Transport:
FAILED

Urban Food Availability:
CRITICAL
```

---

# Water Supply

Water is unusual because it is both a resource and an infrastructure-delivered service.

Supply State should represent:

- raw water availability
- treatment chemicals
- stored potable water

Infrastructure State should represent:

- treatment
- pumping
- distribution

---

# Fuel Supply

Fuel includes:

- petroleum products
- alternative fuels
- generator fuel
- aviation fuel
- industrial fuel

Fuel strongly affects:

- transport
- logistics
- agriculture
- emergency power
- construction

---

# Fuel Distribution

Fuel distribution may become constrained before fuel itself becomes scarce.

Example:

```text
Regional Fuel Inventory:
ADEQUATE

Service Stations Operational:
40%
```

The resource exists.

Access is limited.

---

# Medicine

Medicine includes:

- pharmaceuticals
- medical consumables
- oxygen
- blood products
- specialized equipment

Medicine often has:

```text
HIGH CRITICALITY
LOW SUBSTITUTABILITY
```

and may therefore become a strategic supply priority.

---

# Medical Supply Chain

Medical supply may depend upon:

```text
Global Production
Cold Storage
Air Transport
Road Logistics
Hospitals
Pharmacies
```

This creates sensitivity to international and regional disruption.

---

# Spare Parts

Spare Parts are critical for infrastructure recovery.

Examples:

- transformers
- pumps
- telecommunications equipment
- vehicles
- industrial control components

Spare parts often produce delayed rather than immediate shortages.

---

# Spare-Part Delay

Example:

```text
MONTH 1
Equipment still operating.

MONTH 2
Failures begin accumulating.

MONTH 3
Replacement parts unavailable.

MONTH 4
Infrastructure reliability declines sharply.
```

Supply effects may therefore emerge long after trade disruption begins.

---

# Industrial Materials

Industrial Materials include:

- steel
- copper
- chemicals
- plastics
- electronics
- machine components

These support long-term repair and reconstruction.

---

# Agricultural Inputs

Agricultural Inputs include:

- fertilizer
- seed
- fuel
- pesticides
- machinery parts
- animal feed

Shortages may reduce future food production rather than immediate availability.

---

# Delayed Supply Effects

Supply State should model delayed consequences.

Example:

```text
Fertilizer shortage today
      ↓
Reduced planting
      ↓
Lower harvest months later
      ↓
Food Pressure increases
```

This is a long-horizon cascade.

---

# Energy Storage

Energy Storage includes:

- batteries
- stored fuel
- grid-scale storage

It acts as a buffer between power production and demand.

---

# Critical Chemicals

Examples include:

- water-treatment chemicals
- industrial gases
- medical chemicals
- refinery inputs

Small shortages may create disproportionately large effects.

---

# Geographic Distribution

Supply should be spatial.

Example:

```text
REGION

Northern Zone:
Food Surplus

Urban Core:
Food Constrained

Southern Zone:
Adequate
```

Regional averages should not erase important local differences.

---

# Supply Nodes

Important supply infrastructure may be represented as nodes.

Examples:

```text
Warehouse
Fuel Depot
Port
Rail Terminal
Distribution Center
Reservoir
Refinery
```

Critical nodes may receive individual simulation where useful.

---

# Supply Routes

Resources move through routes.

Examples:

```text
Road
Rail
Pipeline
Ship
Air
Power Network
```

Each route may have:

```text
State
Capacity
Security
Reliability
```

---

# Route Failure

A route failure should increase supply pressure based upon dependency.

Example:

```text
Rail Route:
FAILED

Food Dependency on Rail:
HIGH

Result:
Food Pressure increases strongly.
```

If dependency is low, the effect should remain limited.

---

# Alternate Routes

Alternate routes increase resilience.

Example:

```text
Primary Rail:
FAILED

Secondary Road:
FUNCTIONAL
```

Result:

```text
Distribution Capacity:
STRAINED
```

rather than:

```text
FAILED
```

---

# Supply Chain Depth

Some resources require long chains.

Example:

```text
MEDICINE

Raw Material
    ↓
Manufacturing
    ↓
Packaging
    ↓
Cold Storage
    ↓
Transport
    ↓
Hospital
```

Failure at any stage may reduce supply.

---

# Supply Chain Visibility

Authorities may not have complete knowledge of supply chains.

Example:

```text
Regional Government:
Believes medicine supply adequate.

Hospital Network:
Knows one critical supplier is failing.
```

Information State therefore affects Supply planning.

---

# Inventory Visibility

Digital systems normally provide rapid inventory visibility.

During disruption:

```text
Actual Inventory:
Unknown

Reported Inventory:
Adequate

Confidence:
Low
```

Poor visibility may cause inefficient allocation.

---

# Supply Allocation

Authorities and organizations may prioritize resources.

Examples:

```text
Fuel Priority:
1. Hospitals
2. Water
3. Emergency Services
4. Freight
5. Civilian Use
```

Allocation may improve critical-system resilience while reducing general availability.

---

# Rationing

Rationing reduces demand or redistributes scarce supply.

Forms include:

```text
Voluntary
Price-Based
Quota-Based
Priority-Based
Community-Based
Authority-Enforced
```

---

# Rationing Effectiveness

Rationing depends upon:

- legitimacy
- enforcement
- information
- distribution capacity
- perceived fairness

Effective rationing may stabilize supply.

Poorly implemented rationing may increase:

- black markets
- distrust
- stockpiling

---

# Fairness

Perceived fairness matters.

Example:

```text
Supply:
Critical

Rationing:
Transparent and equitable
```

may preserve:

```text
Social Cohesion
Authority Legitimacy
```

while unequal access may increase unrest pressure.

---

# Black Markets

Black markets may emerge when:

```text
Demand:
HIGH

Legal Supply:
RESTRICTED

Enforcement:
LIMITED
```

They may:

- improve access for some
- increase inequality
- divert supply
- create crime pressure

Black markets should have mixed effects.

---

# Price

Price may function as a supply-pressure signal where markets remain active.

Conceptually:

```text
NORMAL
ELEVATED
HIGH
EXTREME
UNSTABLE
```

The system does not require detailed economic modeling at this stage.

---

# Price Versus Availability

High prices do not necessarily mean physical shortage.

They may reflect:

- uncertainty
- transport cost
- speculative demand

Likewise, fixed prices do not guarantee availability.

---

# Stockpiling

Population stockpiling transfers supply from:

```text
COMMERCIAL INVENTORY
```

to:

```text
HOUSEHOLD INVENTORY
```

Total regional resources may initially remain unchanged.

But distribution changes.

---

# Stockpiling Effect

Example:

```text
Regional Food:
ADEQUATE

Retail Food:
CONSTRAINED

Household Food:
HIGH
```

Visible retail shortages may therefore overstate total resource shortage.

---

# Hoarding

Hoarding may be used for unusually concentrated resource accumulation beyond plausible household preparation.

It should remain distinct from normal preparedness.

Hoarding may increase:

- local scarcity
- inequality
- black-market potential

---

# Conservation

Conservation reduces demand.

Examples:

```text
Lower fuel use
Reduced electricity consumption
Food substitution
Water conservation
```

Conservation may create a stabilizing loop.

---

# Demand Destruction

Severe disruption may reduce demand because activities stop.

Example:

```text
Industry shuts down
      ↓
Industrial Fuel Demand falls
```

This may free fuel for essential services.

Economic decline can therefore create short-term supply relief.

---

# Supply and Migration

Migration changes both sides of the equation.

Origin region:

```text
Population declines
      ↓
Demand declines
```

Destination region:

```text
Population increases
      ↓
Demand increases
```

This can produce cross-regional supply pressure.

---

# Supply and Workforce

Production and distribution depend upon workers.

Example:

```text
Food Inventory:
Adequate

Warehouse Workforce:
Critical

Result:
Distribution Capacity declines.
```

---

# Supply and Authority

Authority may influence Supply through:

- reserves
- rationing
- requisition
- trade agreements
- allocation
- emergency imports

Supply outcomes affect legitimacy.

---

# Supply and Information

Information influences:

- demand expectations
- stockpiling
- route planning
- inventory allocation
- price

False shortage reports can create real distribution problems.

---

# Supply and Security

Supply routes may require protection.

Security degradation may cause:

- convoy disruption
- theft
- route closure
- increased transport cost

Supply scarcity may in return increase Security pressure.

---

# Supply and Recovery

Recovery requires materials.

Examples:

```text
Infrastructure repair
needs spare parts.

Healthcare recovery
needs medicine.

Agriculture recovery
needs fuel and fertilizer.
```

Supply may therefore become the primary Recovery Bottleneck.

---

# Supply Feedback Loops

## Shortage Loop

```text
SUPPLY PRESSURE
      ↓
STOCKPILING
      ↓
RETAIL AVAILABILITY FALLS
      ↓
PERCEIVED SHORTAGE INCREASES
      ↓
MORE STOCKPILING
```

---

# Conservation Loop

```text
SUPPLY PRESSURE
      ↓
CONSERVATION
      ↓
DEMAND FALLS
      ↓
SUPPLY PRESSURE DECREASES
```

---

# Logistics Loop

```text
FUEL SHORTAGE
      ↓
TRANSPORT CAPACITY FALLS
      ↓
SUPPLY DELIVERY FALLS
      ↓
FUEL DELIVERY ALSO FALLS
```

This can become strongly reinforcing.

---

# Recovery Loop

```text
SPARE PARTS ARRIVE
      ↓
INFRASTRUCTURE REPAIR IMPROVES
      ↓
LOGISTICS IMPROVES
      ↓
MORE SUPPLIES ARRIVE
```

Positive cascades must remain possible.

---

# Supply Shock

Examples include:

- port closure
- crop failure
- refinery shutdown
- trade embargo
- major warehouse loss
- sudden migration
- pipeline failure

Shock outcome depends upon:

- inventory
- reserves
- alternate routes
- production
- demand

---

# Supply Transition

A conceptual state progression:

```text
SURPLUS
   ↓
ADEQUATE
   ↓
STRAINED
   ↓
CONSTRAINED
   ↓
CRITICAL
   ↓
UNAVAILABLE
```

Improvement may move upward.

---

# State Transition Causes

Examples:

```text
ADEQUATE → STRAINED

Possible Causes:
- import reduction
- demand increase
- inventory decline
```

```text
CONSTRAINED → CRITICAL

Possible Causes:
- distribution failure
- reserve depletion
- migration surge
```

---

# Supply Stabilization

A supply system may stabilize through:

- rationing
- new imports
- reduced demand
- local production
- substitution
- improved distribution

A constrained supply state may remain stable indefinitely if society adapts.

---

# Stable Scarcity

Example:

```text
Fuel:
CONSTRAINED

Trend:
STABLE

Rationing:
FUNCTIONAL
```

This may become a long-term equilibrium.

Scarcity does not automatically mean crisis.

---

# Supply Recovery

Supply may recover through:

- production restoration
- route restoration
- trade
- reserve replenishment
- improved distribution
- migration stabilization

---

# Reserve Replenishment

After immediate crisis:

```text
Current Supply:
ADEQUATE

Strategic Reserves:
LOW
```

The system is functional but remains fragile.

Full recovery requires rebuilding reserves.

---

# Supply Adaptation

Long-term adaptation may include:

```text
Global imports
        ↓
Regional production

Just-in-time inventory
        ↓
Strategic stockpiles

Long supply chains
        ↓
Shorter regional chains

Specialized goods
        ↓
Substitutable local alternatives
```

---

# Efficiency Versus Resilience

Modern supply chains may be:

```text
Efficient
Fast
Low Inventory
Globally Integrated
```

Post-Collapse supply may become:

```text
Slower
Higher Inventory
Regional
Redundant
Less Efficient
More Resilient
```

This is transformation, not simply regression.

---

# Supply State Snapshot

Example:

```text
SUPPLY STATE

Region:
Northern Virginia

Historical Era:
WS-02 — The Transition

Food:
    Availability: STRAINED
    Production: LOW
    Imports: HIGH
    Inventory: ADEQUATE
    Distribution: STRAINED
    Demand: HIGH
    Dependency: HIGH
    Pressure: HIGH
    Resilience: MODERATE
    Trend: DETERIORATING

Water:
    Availability: ADEQUATE
    Production: HIGH
    Distribution: FUNCTIONAL
    Pressure: MODERATE
    Resilience: HIGH
    Trend: STABLE

Fuel:
    Availability: CONSTRAINED
    Imports: HIGH
    Inventory: LOW
    Distribution: STRAINED
    Demand: HIGH
    Strategic Reserves: MODERATE
    Pressure: SEVERE
    Resilience: LOW
    Trend: DETERIORATING

Medicine:
    Availability: ADEQUATE
    Inventory: STRAINED
    Distribution: FUNCTIONAL
    Dependency: HIGH
    Pressure: HIGH
    Resilience: MODERATE
    Trend: DETERIORATING

Spare Parts:
    Availability: STRAINED
    Dependency: CRITICAL
    Pressure: HIGH
    Resilience: LOW
    Trend: DETERIORATING
```

---

# Fractured World Example

```text
SUPPLY STATE

Region:
Shenandoah Valley

Historical Era:
WS-03 — The Fractured World

Food:
    Availability: SURPLUS
    Production: HIGH
    Imports: LOW
    Distribution: FUNCTIONAL
    Demand: NORMAL
    Resilience: HIGH

Water:
    Availability: ADEQUATE
    Resilience: HIGH

Fuel:
    Availability: CONSTRAINED
    Local Production: MINIMAL
    Dependency: HIGH
    Rationing: FUNCTIONAL

Medicine:
    Availability: STRAINED
    Dependency: HIGH
    Resilience: LOW

Industrial Materials:
    Availability: CONSTRAINED

Overall Supply Trend:
STABLE
```

The region may be highly resilient in food while remaining dependent upon external medicine and industrial goods.

---

# Reconnection Example

```text
SUPPLY STATE

Region:
Shenandoah Valley

Historical Era:
WS-04 — The Reconnection

Food:
SURPLUS

Fuel:
STRAINED → ADEQUATE

Medicine:
STRAINED → ADEQUATE

Industrial Materials:
CONSTRAINED → STRAINED

New Trade Dependency:
INCREASING
```

Reconnection improves availability while creating new dependencies.

---

# Supply Event Generation

Example:

```text
Fuel:
CONSTRAINED

Distribution:
STRAINED

Authority:
FUNCTIONAL

Public Trust:
HIGH
```

Possible event:

```text
Regional fuel rationing
```

Alternative:

```text
Fuel:
CONSTRAINED

Authority:
LOW

Information:
UNSTABLE
```

Possible events:

```text
Fuel queues
Black-market expansion
Route competition
Stockpiling
```

---

# Supply Opportunity Generation

Supply should create positive gameplay opportunities.

Examples:

```text
New trade route discovered.

Warehouse reopened.

Local farm cooperative expands.

Refinery restart becomes possible.

Medicine convoy arrives.

Regional trade agreement proposed.
```

---

# Player Interaction

Players may affect supply through:

- escort
- trade
- production
- negotiation
- repair
- route discovery
- resource recovery
- rationing decisions
- protection
- information

---

# Player Supply Choices

Example:

```text
Medicine Supply:
Critical

Available Shipment:
Limited

Options:

Hospital A
Population: Large

Hospital B
Specialist Care

Remote Settlement
No alternative access
```

The system may create meaningful allocation decisions without a universally correct answer.

---

# Player-Created Supply Cascade

Example:

```text
Players restore bridge.
      ↓
Distribution improves.
      ↓
Food Availability improves.
      ↓
Public Confidence improves.
      ↓
Stockpiling decreases.
```

Player action may produce effects beyond the immediate mission.

---

# Supply Knowledge

Supply information may be uncertain.

Example:

```text
Reported Fuel Inventory:
ADEQUATE

Actual Fuel Inventory:
LOW

Confidence:
LOW
```

Authorities and populations respond to available knowledge rather than hidden truth.

---

# Supply Intelligence

Information about supply may itself become valuable.

Examples:

```text
Which town has fuel?

Which road is open?

Where are medical supplies stored?

Which region has grain surplus?
```

Supply intelligence may drive trade, migration and conflict.

---

# Supply Update Cycle

A conceptual Supply State update may follow:

```text
1. Read current inventory.
2. Read local production.
3. Read imports.
4. Process route capacity.
5. Process distribution.
6. Calculate demand.
7. Apply population behavior.
8. Apply rationing and conservation.
9. Apply authority allocation.
10. Apply infrastructure constraints.
11. Apply workforce constraints.
12. Apply security effects.
13. Consume inventory.
14. Apply reserve use.
15. Apply substitution.
16. Calculate pressure.
17. Evaluate thresholds.
18. Update availability.
19. Update trend.
20. Generate supply events.
21. Update historical memory where significant.
```

---

# Supply Simulation Resolution

## High Resolution

Used for:

- player region
- active shortages
- critical facilities
- major trade routes

May track:

```text
Individual resources
Inventory days
Routes
Warehouses
Strategic reserves
Allocation decisions
```

---

## Medium Resolution

Used for nearby regions.

Tracks:

```text
Resource categories
Availability
Production
Imports
Distribution
Pressure
Trend
```

---

## Low Resolution

Used for distant regions.

Tracks:

```text
Overall Supply
Key Surpluses
Key Shortages
Dependency
Trend
Major Events
```

---

# Minimum Supply State

A minimum viable Supply State should contain:

```text
Food
Water
Fuel
Medicine
Spare Parts

For each:

Availability
Production
Imports
Inventory
Distribution
Demand
Dependency
Pressure
Resilience
Trend

Plus:

Strategic Reserves
Major Supply Routes
Major Supply Dependencies
Rationing State
```

Additional resource categories should be added only where useful.

---

# Supply Consistency Rules

## Rule 1

Resource existence and resource access are separate.

---

## Rule 2

Supply and Logistics are separate.

---

## Rule 3

Availability and Distribution Capacity are separate.

---

## Rule 4

Production Capacity and current Production Output are separate.

---

## Rule 5

Imports increase current availability but may increase dependency.

---

## Rule 6

Inventory and Strategic Reserves are separate.

---

## Rule 7

Using reserves reduces future resilience.

---

## Rule 8

Demand and Consumption are separate.

---

## Rule 9

Population behavior may move inventory without changing total regional resources.

---

## Rule 10

Stockpiling does not automatically mean irrational behavior.

---

## Rule 11

Rationing may stabilize supply.

---

## Rule 12

Perceived fairness influences rationing effectiveness.

---

## Rule 13

Supply effects may be delayed.

---

## Rule 14

Supply chains require real dependencies.

---

## Rule 15

Alternate routes and substitution must be able to interrupt cascades.

---

## Rule 16

Local production does not automatically equal self-sufficiency.

---

## Rule 17

Critical specialized goods may remain import dependent even in resilient regions.

---

## Rule 18

Stable scarcity is a valid long-term equilibrium.

---

## Rule 19

Supply recovery may require rebuilding reserves after availability returns.

---

## Rule 20

Supply adaptation may increase resilience while reducing efficiency.

---

## Rule 21

Regional supply conditions may vary internally.

---

## Rule 22

Supply allocation decisions should create understandable tradeoffs.

---

# Guiding Questions

For every important resource, the simulation should be capable of answering:

**How much exists?**

**Where is it?**

**Where does it come from?**

**Can it be produced locally?**

**How dependent is the region on imports?**

**How much inventory exists?**

**How large are strategic reserves?**

**Can it be transported?**

**Can it be distributed?**

**Who needs it?**

**Who receives priority?**

**How quickly is it being consumed?**

**What happens when buffers run out?**

**Can something substitute for it?**

**What is the current bottleneck?**

**What would allow supply to recover?**

These questions define supply more accurately than a single shortage value.

---

# Core Design Principle

Project Ascension should never assume:

```text
FOOD EXISTS IN THE REGION
=
PEOPLE HAVE FOOD
```

Instead:

```text
PRODUCTION
    +
IMPORTS
    +
INVENTORY
    +
TRANSPORT
    +
DISTRIBUTION
    +
ACCESS
=
USABLE SUPPLY
```

Any link can become the limiting factor.

---

# Relationship to The Connected World

The Connected World typically possesses:

```text
High trade
Low inventory
High logistics efficiency
High specialization
High external dependency
```

This produces tremendous abundance.

It may also create vulnerability to systemic disruption.

---

# Relationship to The Transition

The Transition exposes those dependencies.

Typical progression:

```text
Imports remain available
        ↓
Coordination becomes less reliable
        ↓
Distribution slows
        ↓
Inventory falls
        ↓
Rationing begins
        ↓
Regional supply conditions diverge
```

Physical scarcity may appear later than operational scarcity.

---

# Relationship to The Fractured World

Supply systems adapt toward:

```text
Regional production
Higher inventories
Local storage
Trade networks
Rationing
Substitution
```

Different regions develop distinctive resource profiles.

---

# Relationship to The Reconnection

Reconnection restores:

- long-distance trade
- specialized production
- larger markets
- greater resource variety

But also recreates external dependency.

The strategic question becomes:

```text
How much efficiency should be exchanged for dependency?
```

---

# World Simulation Integration

Supply now completes another major loop:

```text
INFRASTRUCTURE
      ↓
LOGISTICS
      ↓
SUPPLY
      ↓
POPULATION
      ↓
AUTHORITY
      ↓
ALLOCATION / BEHAVIOR
      ↓
SUPPLY
```

and:

```text
SUPPLY
      ↓
INFRASTRUCTURE REPAIR
      ↓
RECOVERY
      ↓
SUPPLY CAPACITY
```

Supply is therefore both an outcome and a driver of world state.

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
FOUNDATION DEFINED

Authority_State.md
FOUNDATION DEFINED

Population_State.md
FOUNDATION DEFINED

Supply_State.md
FOUNDATION DEFINED

Security_State.md
PENDING

Escalation_and_Recovery.md
FOUNDATION DEFINED

Validation/
    TEST-001_Northern_Virginia_Transition.md
    PASS
```

---

# Next Document

The next recommended document is:

```text
Canon/Systems/World_Simulation/Security_State.md
```

Supply State defines:

```text
WHAT PEOPLE AND SYSTEMS NEED
```

Security State will define:

```text
WHETHER PEOPLE, INSTITUTIONS AND RESOURCE FLOWS CAN OPERATE SAFELY
```

It should distinguish:

- security condition
- security capacity
- threat
- crime
- unrest
- organized violence
- policing
- military support
- infrastructure protection
- territorial security
- community defense
- perceived security

Most importantly, it should preserve the same principle we used for Population:

```text
CRISIS
≠
VIOLENCE
```

A region can be under severe infrastructure and supply pressure while remaining socially peaceful.

That distinction will be essential when we later test a stable society in **The Fractured World**.

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial supply availability, production, imports, inventory, reserves, distribution, demand, rationing, dependency, feedback and adaptation framework established. |