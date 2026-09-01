# PROJECT ASCENSION
# Supply State System

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Supply State System |
| Location | `Canon/Systems/World_Simulation/Supply_State.md` |
| Version | 1.0 |
| Status | Canonical Architecture |
| Category | World Simulation / Supply |
| Owner | World Simulation |
| Last Updated | 2026-09-01 |
| Primary Function | Define the authoritative availability, production, storage, consumption, dependency, scarcity, substitution, resilience and recovery state of strategically important resources |

---

# 1. Purpose

The Supply State System defines how essential resources exist and remain available within Project Ascension.

It answers:

> **What resources exist, where are they, how are they produced, how much is available, how quickly are they being consumed, what do they depend on, what buffers remain, and what happens when supply becomes constrained?**

Supply includes strategically important resources such as:

```text
FOOD

RAW WATER

POTABLE WATER STORES

FUEL

MEDICINE

MEDICAL CONSUMABLES

SPARE PARTS

INDUSTRIAL MATERIALS

AGRICULTURAL INPUTS

BATTERIES

CRITICAL CHEMICALS

SPECIALIZED COMPONENTS.
```

Supply State does not answer whether every resource can physically reach every user.

That requires interaction with Infrastructure, Security, Authority, Information, Population and other systems.

---

# 2. Core Principle

A resource does not matter merely because it exists.

It matters because it remains usable within the world.

Conceptually:

```text
RESOURCE EXISTS
↓
RESOURCE CAN BE PRODUCED
OR IMPORTED
↓
RESOURCE CAN BE STORED
↓
RESOURCE REMAINS USABLE
↓
RESOURCE CAN REACH
THE REQUIRED LOCATION
↓
RESOURCE CAN BE ACCESSED
↓
RESOURCE CAN BE CONSUMED
OR USED.
```

Supply State owns the resource side of this chain.

Other systems may determine whether movement, allocation or access succeeds.

---

# 3. Resource Existence vs Availability

Canonical distinction:

```text
RESOURCE EXISTENCE
≠
RESOURCE AVAILABILITY.
```

Example:

```text
Regional Fuel Inventory:
ADEQUATE

Local Fuel Availability:
CRITICAL.
```

The fuel exists.

It is not effectively available at the relevant location.

This may result from:

```text
distribution failure

route closure

allocation

security conditions

access restrictions

infrastructure failure.
```

Supply State must preserve this distinction.

---

# 4. Supply vs Infrastructure

Supply and Infrastructure are separate authoritative domains.

```text
SUPPLY

What resource exists?

How much exists?

Where is it?

How quickly is it
being produced,
consumed or depleted?


INFRASTRUCTURE

What physical systems
allow the resource
to be produced,
processed,
stored,
transported
or delivered?
```

Example:

```text
Fuel Supply:
ADEQUATE

Fuel Distribution Infrastructure:
DEGRADED.
```

The resource exists.

The physical system moving it does not operate normally.

---

# 5. Supply vs Logistics Infrastructure

Supply must not duplicate physical logistics state.

Infrastructure owns:

```text
roads

rail

ports

warehouses

distribution centers

pipelines

fuel terminals

freight terminals

physical logistics hubs.
```

Supply owns:

```text
resource inventory

resource production

resource imports

resource demand

resource consumption

resource reserves

resource dependency

resource scarcity.
```

Infrastructure determines whether movement is physically possible.

Supply determines what is available to move.

---

# 6. Supply vs Allocation

Supply State may identify scarcity.

It does not decide who receives scarce resources.

Example:

```text
Medicine Availability:
CRITICAL

Essential Demand:
HIGH.
```

Authority, institutions, communities or other Actors may decide:

```text
WHO RECEIVES
THE MEDICINE.
```

Supply State then records the resulting resource movement and consumption.

Therefore:

```text
SUPPLY
OWNS SCARCITY.

ACTORS
OWN ALLOCATION DECISIONS.
```

---

# 7. Supply vs Information

Supply State owns actual resource truth.

Information State owns:

```text
reported inventory

supply intelligence

observer knowledge

confidence

rumor

verification

information delay

information distortion.
```

Therefore:

```text
ACTUAL SUPPLY
≠
KNOWN SUPPLY.
```

Example:

```text
Actual Fuel Inventory:
LOW

Regional Government Belief:
ADEQUATE.
```

The discrepancy is valid.

---

# 8. Supply vs Population

Population behavior may influence Supply through:

```text
demand

consumption

stockpiling

conservation

migration

substitution.
```

Supply consumes these effects.

It does not own the behavior producing them.

---

# 9. Supply vs Security

Security may affect whether resources can safely move or remain accessible.

Supply State may expose:

```text
RESOURCE LOCATION

RESOURCE REQUIREMENT

RESOURCE CRITICALITY.
```

Security owns:

```text
route threat

theft risk

organized violence

territorial control

protection capability.
```

---

# 10. Supply Hierarchy

Supply may exist at multiple scales.

```text
GLOBAL
↓
NATIONAL
↓
REGIONAL
↓
LOCAL
↓
FACILITY
↓
HOUSEHOLD.
```

World Simulation should normally operate at the lowest resolution required to preserve causality.

Regional state will often be sufficient.

Critical facilities or events may require local or facility-level simulation.

---

# 11. Core Supply Categories

The default Supply architecture should support:

```text
FOOD

WATER RESOURCES

FUEL

MEDICINE

MEDICAL CONSUMABLES

SPARE PARTS

INDUSTRIAL MATERIALS

AGRICULTURAL INPUTS

ENERGY STORAGE

CRITICAL CHEMICALS.
```

Additional resources should be introduced only when causally significant.

---

# 12. Resource State Contract

A significant Supply category may expose:

```text
Availability

Production Capacity

Current Production

Imports

Inventory

Strategic Reserves

Demand

Essential Demand

Consumption

Import Dependency

Critical Dependencies

Pressure

Resilience

Substitutability

Criticality

Trend

Recovery Capacity

Last Significant Change

Causal Sources.
```

Not every resource requires every field.

---

# 13. Availability

Availability represents usable resource currently accessible at the simulated scale.

Conceptual states:

```text
SURPLUS

ADEQUATE

STRAINED

CONSTRAINED

CRITICAL

UNAVAILABLE.
```

---

# 14. Surplus

```text
SURPLUS
```

means usable supply exceeds current demand with meaningful margin.

Possible consequences may include:

```text
export potential

reserve building

local abundance

trade leverage.
```

Supply State records the surplus.

Actors determine what is done with it.

---

# 15. Adequate

```text
ADEQUATE
```

means usable supply meets current demand with reasonable operating margin.

Adequate does not imply independence.

A region may have:

```text
Availability:
ADEQUATE

Import Dependency:
CRITICAL.
```

---

# 16. Strained

```text
STRAINED
```

means supply remains sufficient but margins are declining.

Possible causes include:

```text
falling inventory

reduced imports

increasing demand

reduced production

increasing consumption.
```

---

# 17. Constrained

```text
CONSTRAINED
```

means supply cannot support unrestricted normal demand.

Essential demand may still be met.

---

# 18. Critical

```text
CRITICAL
```

means available supply cannot reliably satisfy essential demand.

This creates allocation pressure.

It does not itself determine allocation.

---

# 19. Unavailable

```text
UNAVAILABLE
```

means the resource cannot currently be accessed at the simulated scale.

The resource may still exist elsewhere.

---

# 20. Production Capacity

Production Capacity represents the maximum plausible current production capability before temporary operating constraints are applied.

Examples:

```text
Agricultural Capacity

Refining Capacity

Pharmaceutical Capacity

Industrial Production Capacity.
```

Conceptual values:

```text
SURPLUS

HIGH

MODERATE

LOW

MINIMAL

NONE.
```

---

# 21. Current Production

Current Production represents actual output.

This must remain separate from Production Capacity.

Example:

```text
Production Capacity:
HIGH

Current Production:
LOW.
```

Possible causes:

```text
fuel shortage

missing inputs

workforce shortage

power restriction

security conditions

infrastructure failure.
```

---

# 22. Production Dependency

Production may depend upon:

```text
power

water

fuel

raw materials

workforce

machinery

specialized parts

transportation

industrial chemicals

information

access.
```

Production therefore exists inside a dependency network.

---

# 23. Local Production

Local production may improve resilience.

But:

```text
LOCAL PRODUCTION
≠
SELF-SUFFICIENCY.
```

A farming region may still depend on:

```text
fertilizer

fuel

machinery parts

seed

electricity

transportation.
```

---

# 24. Imports

Imports represent externally sourced resources entering the simulated region.

Conceptual values:

```text
HIGH

MODERATE

LOW

MINIMAL

NONE.
```

Imports are current flow.

They are separate from Import Dependency.

---

# 25. Import Dependency

Import Dependency represents structural reliance on external sources.

Conceptually:

```text
LOW

MODERATE

HIGH

CRITICAL.
```

Example:

```text
Medicine Availability:
ADEQUATE

Import Dependency:
CRITICAL.
```

The current state is stable.

The future state may be vulnerable.

---

# 26. Inventory

Inventory represents stored resource available for normal use.

Conceptual states:

```text
HIGH

ADEQUATE

LOW

CRITICAL

DEPLETED.
```

Inventory is a buffer between inflow and consumption.

---

# 27. Inventory Duration

Where useful, inventory may be expressed in time.

Example:

```text
Hospital Oxygen:
4 days

Regional Diesel:
11 days
at current consumption.
```

Exact numbers should be used only when causally useful.

---

# 28. Strategic Reserves

Strategic Reserves are resources intentionally separated from normal consumption.

Examples:

```text
national fuel reserves

emergency medicine

food reserves

spare transformers

water-treatment chemicals.
```

Conceptual states:

```text
FULL

HIGH

MODERATE

LOW

CRITICAL

DEPLETED.
```

---

# 29. Reserve Release

Supply State records whether reserves remain and how they change.

The decision to release them belongs to the controlling Actor or institution.

Example:

```text
Fuel Availability:
CONSTRAINED

Strategic Reserve:
HIGH

Authority Decision:
Release Reserve

Result:

Current Availability:
Improves

Strategic Reserve:
Declines.
```

---

# 30. Reserve Tradeoff

Canonical principle:

```text
RESERVE USE
REDUCES
FUTURE RESILIENCE.
```

Conceptually:

```text
CURRENT SHORTAGE
↓
RESERVE RELEASE
↓
CURRENT PRESSURE FALLS
↓
FUTURE BUFFER SHRINKS.
```

Reserve use must never be free.

---

# 31. Demand

Demand represents how much resource would currently be required under prevailing conditions.

Conceptual states:

```text
LOW

NORMAL

HIGH

SEVERE

EXTREME.
```

Demand may change because of:

```text
population

weather

migration

infrastructure requirements

emergency operations

economic activity

institutional requirements.
```

---

# 32. Essential Demand

Supply must distinguish:

```text
TOTAL DEMAND
```

from:

```text
ESSENTIAL DEMAND.
```

Example:

Fuel may be insufficient for normal civilian demand while still being sufficient for:

```text
hospitals

water systems

emergency services

critical freight.
```

Who receives priority remains an Actor decision.

---

# 33. Consumption

Consumption represents actual resource use.

Demand and Consumption must remain separate.

Example:

```text
Demand:
HIGH

Consumption:
MODERATE.
```

Possible causes include:

```text
scarcity

rationing

conservation

access failure

substitution.
```

---

# 34. Consumption Rate

Where causally useful, consumption may be represented as a rate.

Example:

```text
Diesel Inventory:
10 million liters

Consumption:
1 million liters/day.
```

This enables meaningful depletion timing.

Avoid unnecessary precision.

---

# 35. Supply Margin

Supply Margin is a derived relationship between usable supply and demand.

Conceptually:

```text
SURPLUS

SAFE

NARROW

CRITICAL

DEFICIT.
```

It is diagnostic.

It should not become an independent authoritative state domain.

---

# 36. Supply Pressure

Supply Pressure represents forces pushing availability toward worse states.

Possible causes include:

```text
import disruption

production loss

inventory depletion

increasing demand

migration

resource diversion

infrastructure failure

security disruption

input shortage

seasonal change.
```

Conceptual scale:

```text
NONE

LOW

MODERATE

HIGH

SEVERE

CRITICAL.
```

---

# 37. Supply Resilience

Supply Resilience represents the ability to absorb disruption without severe loss of availability.

Sources may include:

```text
local production

diversified suppliers

inventory

strategic reserves

substitution

alternative inputs

lower demand

regional trade

multiple production sources.
```

---

# 38. Buffers

Important resource buffers may include:

```text
normal inventory

strategic reserves

commercial stock

household stock

facility stock

substitute resources.
```

Different buffers exist under different ownership.

Supply State may aggregate resource consequences while preserving ownership boundaries.

---

# 39. Buffer Depletion

Supply shortage often appears after delay.

Example:

```text
IMPORTS FAIL
↓
COMMERCIAL INVENTORY USED
↓
FACILITY INVENTORY USED
↓
STRATEGIC RESERVES RELEASED
↓
VISIBLE SHORTAGE.
```

The sequence depends on Actor decisions and resource access.

---

# 40. Delayed Supply Consequences

Supply effects may emerge long after the original disruption.

Example:

```text
FERTILIZER SHORTAGE
↓
REDUCED PLANTING
↓
LOWER HARVEST
↓
FOOD PRODUCTION FALLS
↓
FOOD PRESSURE INCREASES.
```

This may take months.

Delayed causality is mandatory.

---

# 41. Substitution

Some resources may be replaced by alternatives.

Example:

```text
Gasoline Shortage
↓
Rail Use Increases.
```

or:

```text
Specific Medicine Unavailable
↓
Alternative Treatment Used.
```

Substitution may reduce Supply Pressure.

---

# 42. Substitutability

Resources may have different levels of substitutability.

Conceptually:

```text
HIGH

MODERATE

LOW

NONE.
```

Examples of low-substitutability resources may include:

```text
specialized medicine

transformers

specific industrial components

water-treatment chemicals.
```

---

# 43. Resource Criticality

Criticality represents the consequences created if a resource becomes unavailable.

Conceptually:

```text
LOW

MODERATE

HIGH

CRITICAL.
```

Criticality does not mean scarcity.

A resource may be:

```text
Availability:
SURPLUS

Criticality:
CRITICAL.
```

---

# 44. Dependency Graph

Resources may depend on other resources.

Example:

```text
AGRICULTURE
│
├── Fuel
├── Fertilizer
├── Water
├── Seed
├── Equipment Parts
└── Chemicals
        ↓
      FOOD.
```

Resource dependency may therefore create delayed cascades.

---

# 45. Supply Cascades

Supply cascades occur when shortage of one resource reduces production or availability of another.

Example:

```text
FUEL SHORTAGE
↓
AGRICULTURAL OPERATIONS REDUCED
↓
FOOD PRODUCTION FALLS
↓
FOOD PRESSURE INCREASES.
```

---

# 46. Cascades Are Conditional

Dependency does not guarantee collapse.

A cascade may be interrupted by:

```text
inventory

substitution

alternative suppliers

demand reduction

reserve use

adaptation

restored infrastructure.
```

Therefore:

```text
DEPENDENCY
≠
GUARANTEED SHORTAGE.
```

---

# 47. Food Supply

Food Supply may include:

```text
agricultural output

processed food

stored food

imports

commercial inventory

emergency reserves.
```

Important dependencies may include:

```text
fuel

water

agricultural inputs

electricity

labor

storage

transportation.
```

---

# 48. Food Production

Food production should account for slow causal processes.

Relevant factors may include:

```text
season

planting

harvest

weather

fertilizer

fuel

water

labor

machinery

storage.
```

Food production cannot instantly respond to shortage.

---

# 49. Water Supply

Water requires a strict distinction between resource and infrastructure.

Supply State owns:

```text
raw water availability

stored potable water

treatment chemicals

portable water reserves.
```

Infrastructure State owns:

```text
treatment infrastructure

pumping

distribution systems

storage infrastructure.
```

---

# 50. Fuel Supply

Fuel Supply may include:

```text
petroleum products

diesel

gasoline

aviation fuel

generator fuel

industrial fuel

alternative fuels.
```

Fuel strongly affects:

```text
transportation

agriculture

emergency power

construction

logistics

industry.
```

---

# 51. Fuel Distribution Boundary

Supply State owns:

```text
fuel inventory

fuel production

fuel imports

fuel reserves

fuel demand

fuel consumption.
```

Infrastructure State owns:

```text
refineries as physical assets

pipelines

terminals

service stations

distribution infrastructure.
```

This boundary is mandatory.

---

# 52. Medicine

Medicine Supply may include:

```text
pharmaceuticals

medical consumables

oxygen

blood products

specialized equipment

diagnostic supplies.
```

Medicine often combines:

```text
HIGH CRITICALITY

LOW SUBSTITUTABILITY

HIGH IMPORT DEPENDENCY.
```

This creates strategic vulnerability.

---

# 53. Medicine vs Healthcare Infrastructure

Supply State owns:

```text
medicine

medical consumables

oxygen

blood products

medical equipment availability.
```

Infrastructure State owns:

```text
hospitals

clinics

laboratories

physical medical facilities.
```

Characters / Population own medical personnel depending on scale.

---

# 54. Spare Parts

Spare Parts are strategically important because they often influence future capability rather than immediate service.

Examples:

```text
transformers

pumps

vehicle parts

telecommunications components

industrial control systems

machine components.
```

---

# 55. Spare-Part Delay

Example:

```text
MONTH 1

Equipment remains operational.


MONTH 2

Failures accumulate.


MONTH 3

Replacement parts unavailable.


MONTH 4

Infrastructure reliability declines.
```

A Supply shock may therefore become an Infrastructure crisis much later.

---

# 56. Industrial Materials

Industrial Materials may include:

```text
steel

copper

plastics

industrial chemicals

electronics

machine components

construction materials.
```

They support:

```text
repair

maintenance

production

construction

recovery.
```

---

# 57. Agricultural Inputs

Agricultural Inputs may include:

```text
fertilizer

seed

fuel

pesticides

machinery parts

animal feed.
```

Shortages may affect future production rather than current Food Availability.

---

# 58. Energy Storage

Supply State may represent stored energy resources such as:

```text
batteries

stored fuel

replaceable battery systems.
```

Infrastructure State owns physical grid-scale storage infrastructure where appropriate.

The distinction should follow:

```text
RESOURCE
vs
PHYSICAL SYSTEM.
```

---

# 59. Critical Chemicals

Critical Chemicals may include:

```text
water-treatment chemicals

industrial gases

medical chemicals

refinery inputs

specialized manufacturing chemicals.
```

Small shortages may create disproportionately large consequences.

---

# 60. Geographic Distribution

Supply is spatial.

Example:

```text
REGION

Rural North:
Food Surplus

Urban Core:
Food Constrained

Southern Corridor:
Food Adequate.
```

Regional averages must not erase causally important local scarcity.

---

# 61. Resource Location

Where relevant, Supply State should preserve where important resources are located.

Examples:

```text
regional stockpile

hospital storage

fuel depot inventory

warehouse inventory

agricultural storage

industrial reserve.
```

The physical facility belongs to Infrastructure.

The resource inside it belongs to Supply.

---

# 62. Supply Routes

Supply State may reference routes required for resource movement.

It does not own route condition.

Example:

```text
Food Supply

Primary Route:
I-81 Corridor.
```

Infrastructure owns whether the route physically functions.

Security owns whether movement is safe.

Supply consumes both states.

---

# 63. Alternate Sources

Supply resilience may increase through alternative sources.

Examples:

```text
secondary supplier

regional production

alternative import source

substitute material

local manufacturing.
```

Alternate sources are distinct from alternate physical routes.

---

# 64. Supply Chain Depth

Some resources require long dependency chains.

Example:

```text
MEDICINE

Raw Materials
↓
Manufacturing
↓
Packaging
↓
Cold Storage
↓
Transport
↓
Regional Inventory
↓
Hospital Inventory.
```

Failure at any stage may eventually affect Availability.

---

# 65. Supply Chain Visibility Boundary

Supply State owns the actual chain.

Information State owns how much Actors know about it.

Example:

```text
Actual Supplier:
FAILED

Government Knowledge:
UNKNOWN.
```

Supply should never contain observer Confidence as authoritative resource state.

---

# 66. Stockpiling

Stockpiling may move resources between storage locations.

Example:

```text
COMMERCIAL INVENTORY
↓
HOUSEHOLD INVENTORY.
```

Total regional resource may remain unchanged.

Availability to other consumers may change significantly.

---

# 67. Stockpiling Is Not Automatically Irrational

Stockpiling may be:

```text
reasonable preparation

fear response

strategic preparation

institutional planning

speculation.
```

The behavior belongs to the relevant Actor or Population system.

Supply records the resulting inventory movement.

---

# 68. Hoarding

Hoarding may represent unusually concentrated resource control.

Supply may record:

```text
RESOURCE CONCENTRATION.
```

The motivations and social consequences belong elsewhere.

---

# 69. Conservation

Conservation reduces Consumption.

Example:

```text
Fuel Demand:
HIGH

Conservation Behavior:
ACTIVE

Actual Consumption:
MODERATE.
```

The behavior belongs to Actors, Population or Authority.

Supply records its resource consequence.

---

# 70. Demand Destruction

Demand may fall because activities cease.

Example:

```text
Industrial Activity Falls
↓
Industrial Fuel Demand Falls.
```

This may temporarily improve Fuel Availability despite worsening economic conditions.

---

# 71. Migration

Migration may change regional demand.

Origin:

```text
Population Falls
↓
Demand Falls.
```

Destination:

```text
Population Rises
↓
Demand Rises.
```

Population owns migration.

Supply consumes resulting demand change.

---

# 72. Workforce Boundary

Production may require workers.

Supply State may expose:

```text
Required Workforce Capability.
```

Actual workers belong to:

```text
Characters

Population

Institutions.
```

Example:

```text
Food Inventory:
ADEQUATE

Required Warehouse Workforce:
Unavailable

Result:
Resource Access may decline.
```

The cause remains cross-system.

---

# 73. Rationing Boundary

Rationing is an Actor policy or behavior.

Supply State may record its consequences:

```text
reduced consumption

changed access

resource preservation

reserve preservation.
```

But Supply State does not independently decide to ration.

---

# 74. Allocation Boundary

Allocation belongs to:

```text
Authority

Institutions

Communities

Factions

other controlling Actors.
```

Supply provides:

```text
what exists

how much exists

where it exists

what demand exists

what scarcity exists.
```

Actors decide what to do.

---

# 75. Price Boundary

Price may act as a signal where markets function.

Supply State does not require a detailed economic simulation.

Where relevant, price may be derived from:

```text
scarcity

demand

transport cost

risk

market behavior

policy.
```

Economic ownership should be established separately before detailed price mechanics are introduced.

---

# 76. Black Market Boundary

Black markets are not Supply mechanics.

They emerge through interaction between:

```text
scarcity

Actors

Authority

Security

Society

economic exchange.
```

Supply State records resource movement resulting from them.

It does not generate them automatically.

---

# 77. Supply Shock

A Supply Shock is a significant causal event affecting resource availability or future availability.

Examples:

```text
crop failure

import interruption

production shutdown

warehouse inventory loss

trade interruption

resource contamination

strategic reserve loss.
```

Infrastructure failures may cause Supply shocks but remain infrastructure events at their source.

---

# 78. Supply Shock Consequences

Shock severity depends upon:

```text
inventory

reserves

production

imports

demand

substitutability

dependency

alternative sources

time.
```

A major external shock may have little immediate visible effect if buffers are strong.

---

# 79. Stable Scarcity

Scarcity does not automatically equal crisis.

Example:

```text
Fuel Availability:
CONSTRAINED

Trend:
STABLE

Consumption:
CONTROLLED

Strategic Reserves:
MODERATE.
```

A society may adapt to persistent scarcity.

---

# 80. Supply Stabilization

Supply may stabilize through:

```text
reduced consumption

new production

new imports

substitution

reserve release

alternative sources

lower demand

infrastructure recovery.
```

Some mechanisms are Supply changes.

Others originate in external systems.

---

# 81. Supply Recovery

Supply may recover through:

```text
production restoration

new suppliers

restored imports

inventory rebuilding

reserve replenishment

substitution

demand stabilization

resource recovery.
```

Recovery must remain causal.

---

# 82. Availability Recovery vs Resilience Recovery

These are separate.

Example:

```text
Current Availability:
ADEQUATE

Strategic Reserves:
LOW

Import Dependency:
CRITICAL.
```

The immediate shortage is over.

The system remains fragile.

---

# 83. Reserve Replenishment

Full recovery may require rebuilding buffers after current Availability returns.

Example:

```text
Availability:
ADEQUATE

Strategic Reserve:
LOW

Trend:
IMPROVING.
```

This is partial recovery.

---

# 84. Supply Adaptation

Long-term adaptation may transform supply architecture.

Example:

```text
GLOBAL IMPORTS
↓
REGIONAL PRODUCTION

JUST-IN-TIME INVENTORY
↓
STRATEGIC STOCKPILES

SINGLE SUPPLIERS
↓
DIVERSIFIED SOURCES

SPECIALIZED GOODS
↓
SUBSTITUTABLE ALTERNATIVES.
```

---

# 85. Efficiency vs Resilience

Canonical principle:

```text
EFFICIENCY
≠
RESILIENCE.
```

Connected World supply chains may be:

```text
fast

specialized

globally integrated

low inventory

highly efficient.
```

Fractured World supply chains may become:

```text
slower

regional

redundant

higher inventory

less efficient

more resilient.
```

This is transformation.

Not simple regression.

---

# 86. Supply Feedback Loops

Supply may participate in reinforcing or stabilizing loops.

Example:

```text
FUEL SHORTAGE
↓
TRANSPORT CAPABILITY FALLS
↓
RESOURCE MOVEMENT FALLS
↓
FUEL DELIVERY FALLS
↓
FUEL SHORTAGE WORSENS.
```

But the physical transport effect belongs to Infrastructure.

Supply records the resource consequences.

---

# 87. Positive Recovery Loop

Example:

```text
SPARE PARTS ARRIVE
↓
INFRASTRUCTURE REPAIR IMPROVES
↓
PRODUCTION CAPABILITY IMPROVES
↓
SUPPLY AVAILABILITY IMPROVES.
```

Positive cascades must remain possible.

---

# 88. Cross-System Causality

Supply should interact through explicit causal contracts.

Example:

```text
INFRASTRUCTURE EVENT:

Rail corridor fails.
```

Infrastructure updates:

```text
Rail Capacity:
UNAVAILABLE.
```

Supply consumes that state:

```text
Food Imports:
REDUCED

Fuel Imports:
REDUCED.
```

Supply then updates:

```text
Inventory Trend:
DETERIORATING

Supply Pressure:
INCREASING.
```

No system silently edits another system's authoritative state.

---

# 89. World Event vs Supply Consequence

A World Event may affect Supply.

Example:

```text
Hurricane
↓
Port Closed
↓
Imports Reduced
↓
Inventory Depletes
↓
Availability Becomes Constrained.
```

The hurricane is not a Supply Event.

The reduced imports and resulting scarcity are Supply consequences.

---

# 90. Supply and Action Resolution

Actors may attempt:

```text
produce

transport

recover

trade

allocate

consume

store

release reserves

substitute

protect

steal

destroy.
```

Supply State provides resource-specific world truth to Action Resolution.

It does not decide Actor intent.

---

# 91. Player Interaction

Player Characters obey the same Supply rules as all other Actors.

They may affect Supply through plausible actions such as:

```text
restoring access

recovering resources

negotiating trade

supporting production

transporting resources

protecting resources

discovering new sources.
```

Their actions require normal Action Resolution.

---

# 92. Supply Does Not Generate Quests

Avoid:

```text
MEDICINE LOW
↓
GENERATE MEDICINE QUEST.
```

Prefer:

```text
MEDICINE LOW
↓
REAL WORLD CONSEQUENCE
↓
ACTORS RESPOND
↓
POSSIBLE PLAYER RELEVANCE
↓
NARRATIVE PRESENTATION.
```

Supply creates state.

Narrative determines presentation.

---

# 93. Supply Knowledge

Supply State contains actual resource truth.

Actors may know:

```text
less

more

incorrect information

outdated information

partial information.
```

Knowledge and Information systems own those epistemic states.

---

# 94. Information Can Create Real Supply Consequences

False information may still affect Supply indirectly.

Example:

```text
False Shortage Report
↓
Population Stockpiling
↓
Commercial Inventory Falls
↓
Local Availability Falls.
```

Information caused behavior.

Behavior caused resource movement.

Supply records the resulting state.

---

# 95. Supply and World States

World States provide historical context.

They do not mechanically set Supply values.

---

# 96. Connected World

The Connected World may commonly feature:

```text
high trade

high specialization

low inventories

fast logistics

high efficiency

high external dependency.
```

This produces abundance.

It may also create vulnerability.

---

# 97. Transition

The Transition may expose hidden dependencies.

Possible patterns include:

```text
imports become unreliable

inventory begins declining

regional conditions diverge

strategic reserves become relevant

substitution increases

scarcity becomes uneven.
```

These are possible emergent outcomes.

Not scripted requirements.

---

# 98. Fractured World

The Fractured World may develop:

```text
regional production

higher inventories

local stockpiles

shorter supply chains

regional trade

greater substitution

persistent specialized shortages.
```

Different regions may develop very different resource profiles.

---

# 99. Reconnection

Reconnection may restore:

```text
long-distance trade

specialized production

larger markets

resource variety.
```

It may also recreate:

```text
external dependency

systemic coupling

long supply chains.
```

Reconnection therefore creates both opportunity and vulnerability.

---

# 100. Simulation Resolution

Supply State supports adaptive simulation resolution.

Conceptually:

```text
LOW

MEDIUM

HIGH.
```

Resolution changes detail.

Not resource reality.

---

# 101. Low Resolution

Low-resolution Supply State may preserve:

```text
major shortages

major surpluses

key dependencies

overall trend

major resource shocks.
```

Resources continue changing off-screen.

---

# 102. Medium Resolution

Medium resolution may preserve:

```text
resource categories

availability

production

imports

inventory

demand

pressure

resilience

trend.
```

---

# 103. High Resolution

High resolution may preserve:

```text
specific resources

inventory duration

facility inventories

strategic reserves

specific dependencies

production inputs

consumption rates

resource locations

active allocation consequences.
```

---

# 104. Resolution Follows Causal Relevance

A distant Supply system may require high resolution if:

```text
it supplies multiple regions

a strategic resource is failing

a major cascade is developing

it supports critical infrastructure

it influences Aurora-related events.
```

Player proximity is not the only trigger.

---

# 105. Supply Persistence

Supply State persists through:

```text
player absence

session boundaries

regional travel

time advancement

Story Threads

resolution changes.
```

Inventory continues depleting.

Crops continue growing.

Production continues or stops.

Reserves remain consumed.

---

# 106. Minimum Supply State

A minimum regional Supply representation should normally include:

```text
Food

Water Resources

Fuel

Medicine

Spare Parts.
```

For each relevant category:

```text
Availability

Production

Imports

Inventory

Demand

Essential Demand

Consumption

Dependency

Pressure

Resilience

Trend.
```

Additional detail should be added only when causally necessary.

---

# 107. Supply State Example

```text
REGION:
Northern Virginia


FOOD

Availability:
STRAINED

Production:
LOW

Imports:
HIGH

Inventory:
ADEQUATE

Demand:
HIGH

Import Dependency:
HIGH

Pressure:
HIGH

Resilience:
MODERATE

Trend:
DETERIORATING


FUEL

Availability:
CONSTRAINED

Production:
MINIMAL

Imports:
HIGH

Inventory:
LOW

Strategic Reserves:
MODERATE

Demand:
HIGH

Import Dependency:
CRITICAL

Pressure:
SEVERE

Resilience:
LOW

Trend:
DETERIORATING


MEDICINE

Availability:
ADEQUATE

Inventory:
STRAINED

Import Dependency:
HIGH

Criticality:
CRITICAL

Substitutability:
LOW

Pressure:
HIGH

Trend:
DETERIORATING.
```

Infrastructure determines whether those resources can physically move through the region.

---

# 108. Fractured World Example

```text
REGION:
Shenandoah Valley


FOOD

Availability:
SURPLUS

Production:
HIGH

Import Dependency:
LOW

Inventory:
HIGH

Resilience:
HIGH

Trend:
STABLE


FUEL

Availability:
CONSTRAINED

Production:
MINIMAL

Import Dependency:
HIGH

Inventory:
LOW

Resilience:
LOW

Trend:
STABLE


MEDICINE

Availability:
STRAINED

Import Dependency:
CRITICAL

Substitutability:
LOW

Resilience:
LOW

Trend:
STABLE


INDUSTRIAL MATERIALS

Availability:
CONSTRAINED

Import Dependency:
HIGH

Trend:
STABLE.
```

This region is not simply:

```text
STABLE
```

or:

```text
COLLAPSED.
```

It is resilient in some resources and vulnerable in others.

---

# 109. Supply State Invariants

## SUP-INV-001 — Resource Existence and Availability Are Separate

A resource may exist without being accessible.

---

## SUP-INV-002 — Supply and Infrastructure Are Separate

Supply owns resources.

Infrastructure owns physical systems.

---

## SUP-INV-003 — Production Capacity and Current Production Are Separate

Potential output does not equal actual output.

---

## SUP-INV-004 — Inventory and Strategic Reserves Are Separate

Normal stock and protected reserve stock must not be conflated.

---

## SUP-INV-005 — Demand and Consumption Are Separate

Need does not equal actual use.

---

## SUP-INV-006 — Availability and Import Dependency Are Separate

Current abundance may coexist with structural vulnerability.

---

## SUP-INV-007 — Supply Does Not Own Allocation Decisions

Actors decide who receives scarce resources.

---

## SUP-INV-008 — Supply Does Not Own Observer Knowledge

Actual resource truth remains separate from reported or believed supply.

---

## SUP-INV-009 — Supply Does Not Own Physical Route State

Infrastructure owns transportation and distribution infrastructure.

---

## SUP-INV-010 — Supply Does Not Own Security State

Threat and protection belong to Security.

---

## SUP-INV-011 — Supply Does Not Own Population Behavior

Stockpiling, conservation and migration originate elsewhere.

---

## SUP-INV-012 — Reserve Use Reduces Future Resilience

Buffers cannot be consumed without consequence.

---

## SUP-INV-013 — Supply Effects May Be Delayed

Shortage does not always appear immediately after disruption.

---

## SUP-INV-014 — Dependencies Require Real Causal Links

Supply cascades must be explainable.

---

## SUP-INV-015 — Cascades Are Conditional

Buffers, substitution and adaptation may interrupt them.

---

## SUP-INV-016 — Stable Scarcity Is Valid

Scarcity does not automatically create collapse.

---

## SUP-INV-017 — Local Production Does Not Equal Self-Sufficiency

Production itself may depend on external inputs.

---

## SUP-INV-018 — Recovery Does Not End When Availability Returns

Inventories and reserves may remain dangerously low.

---

## SUP-INV-019 — Resolution Changes Detail, Not Resource Reality

Low-resolution Supply remains causally active.

---

## SUP-INV-020 — Player Absence Does Not Freeze Supply

Resources continue to be produced, consumed and depleted.

---

## SUP-INV-021 — Supply Does Not Generate Narrative Need

Resource state exists independently of story requirements.

---

## SUP-INV-022 — Major Supply Changes Must Be Explainable

Availability changes require traceable causes.

---

# 110. Development Locks

Future Supply development must not introduce:

```text
single universal Supply score

resource exists equals resource available

availability equals distribution capability

Supply-owned road state

Supply-owned warehouse condition

Supply-owned pipeline condition

Supply-owned security

Supply-owned Authority decisions

Supply-owned public trust

Supply-owned observer confidence

Supply-owned Character knowledge

automatic rationing

automatic black markets

automatic stockpiling

automatic violence

automatic cascades

automatic shortage from dependency

automatic recovery

free reserve use

local production equals independence

player-triggered resource existence

frozen distant resources

quest-generated scarcity

narrative-forced shortage

random shortage for drama

player-exclusive resource rules.
```

---

# 111. Supply Architecture Test

Before adding a Supply mechanic, ask:

```text
WHAT RESOURCE
ARE WE MODELING?

DOES IT
ACTUALLY EXIST?

WHERE IS IT?

HOW MUCH
IS AVAILABLE?

HOW MUCH
IS STORED?

HOW MUCH
IS RESERVED?

HOW MUCH
IS BEING PRODUCED?

WHAT IS
PRODUCTION CAPACITY?

WHAT IS
CURRENT DEMAND?

WHAT IS
ESSENTIAL DEMAND?

WHAT IS
ACTUAL CONSUMPTION?

WHAT DOES
PRODUCTION
DEPEND ON?

HOW DEPENDENT
IS THE REGION
ON IMPORTS?

WHAT BUFFERS
EXIST?

HOW FAST
ARE THEY
BEING DEPLETED?

CAN THE RESOURCE
BE SUBSTITUTED?

HOW CRITICAL
IS IT?

WHAT IS
THE CURRENT
BOTTLENECK?

IS THE BOTTLENECK
ACTUALLY SUPPLY

OR

INFRASTRUCTURE?

SECURITY?

AUTHORITY?

INFORMATION?

WORKFORCE?

WHAT HAPPENS
IF NOTHING CHANGES?

WHAT WOULD
ALLOW RECOVERY?
```

---

# 112. Final Supply Model

Conceptually:

```text
RESOURCE SOURCES
        │
        ├── Local Production
        ├── Imports
        └── Existing Inventory
                │
                ↓
        RESOURCE AVAILABILITY
                │
                ├── Inventory
                ├── Strategic Reserves
                ├── Demand
                ├── Essential Demand
                ├── Consumption
                ├── Dependency
                ├── Criticality
                ├── Substitutability
                ├── Pressure
                ├── Resilience
                └── Trend
                        │
                        ↓
        INFRASTRUCTURE
        +
        SECURITY
        +
        AUTHORITY
        +
        POPULATION
        +
        INFORMATION
        +
        TIME
                        ↓
        REAL RESOURCE ACCESS
                        ↓
        CONSUMPTION
        /
        STORAGE
        /
        REDIRECTION
        /
        RESERVE USE
                        ↓
        UPDATED SUPPLY STATE
                        ↓
        FUTURE AVAILABILITY.
```

---

# 113. Supply North Star

The system succeeds when Project Ascension can answer:

```text
WHAT EXISTS?

WHERE IS IT?

HOW MUCH EXISTS?

HOW MUCH
IS ACTUALLY
AVAILABLE?

WHERE DOES IT
COME FROM?

CAN IT
BE PRODUCED
LOCALLY?

WHAT INPUTS
DOES PRODUCTION
REQUIRE?

HOW DEPENDENT
IS THE REGION
ON IMPORTS?

HOW MUCH
INVENTORY REMAINS?

HOW LARGE
ARE THE RESERVES?

HOW QUICKLY
ARE THEY
BEING CONSUMED?

WHAT IS
NORMAL DEMAND?

WHAT IS
ESSENTIAL DEMAND?

WHAT IS
THE BOTTLENECK?

CAN THE RESOURCE
BE SUBSTITUTED?

WHAT HAPPENS
WHEN THE BUFFER
RUNS OUT?

WHAT HAPPENS
IF NOTHING CHANGES?

CAN THE REGION
ADAPT TO
LONG-TERM SCARCITY?

AND

CAN SUPPLY
RECOVER
WITHOUT RETURNING
TO THE OLD
GLOBAL SYSTEM?
```

---

# 114. Closing Principle

Project Ascension should never reduce resource scarcity to:

```text
THERE IS FOOD

THEREFORE

PEOPLE HAVE FOOD.
```

Nor should it reduce shortage to:

```text
IMPORTS STOPPED

THEREFORE

THE REGION STARVES.
```

The simulation should instead understand:

```text
Food Production:
MODERATE

Imports:
FAILED

Commercial Inventory:
ADEQUATE

Strategic Reserves:
HIGH

Demand:
HIGH

Import Dependency:
HIGH

Trend:
DETERIORATING.
```

The shortage has not arrived yet.

But the conditions that may create it already exist.

Likewise:

```text
Regional Food:
SURPLUS

Urban Availability:
CONSTRAINED

Transport Infrastructure:
DEGRADED.
```

The food exists.

The problem is somewhere else.

Supply therefore represents more than scarcity.

It represents the material relationship between:

```text
PRODUCTION

STORAGE

DEPENDENCY

DEMAND

CONSUMPTION

BUFFERS

SUBSTITUTION

TIME.
```

Resources move through a living world.

They are produced.

Stored.

Consumed.

Protected.

Redirected.

Lost.

Substituted.

Replenished.

And sometimes transformed into entirely new supply systems.

The central principle is:

> **A resource shortage is not simply the absence of a resource. It is the point at which production, inventory, dependency, demand, access and time can no longer provide enough usable supply where it is needed.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-08-09 | Established initial supply availability, production, imports, inventory, reserves, distribution, demand, rationing, dependency, feedback and adaptation framework. |
| 1.0 | 2026-09-01 | Rebuilt Supply State as canonical resource architecture aligned with Simulation Architecture and Infrastructure State. Preserved availability, production, imports, inventory, strategic reserves, demand, consumption, dependency, substitution, criticality, delayed effects, resilience, stable scarcity and adaptation while separating physical logistics from Supply, allocation from resource state, population behavior from Supply, observer knowledge from actual resource truth, and Security from resource availability. Established explicit cross-system contracts, adaptive simulation resolution, invariants and development locks. |