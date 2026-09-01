# PROJECT ASCENSION
# Infrastructure State System

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Infrastructure State System |
| Location | `Canon/Systems/World_Simulation/Infrastructure_State.md` |
| Version | 1.0 |
| Status | Canonical Architecture |
| Category | World Simulation / Infrastructure |
| Owner | World Simulation |
| Last Updated | 2026-09-01 |
| Primary Function | Define the authoritative state, service capability, dependencies, operational modes, fragmentation and recovery context of physical and digital infrastructure |

---

# 1. Purpose

The Infrastructure State System defines how essential physical and digital infrastructure exists and operates inside Project Ascension.

It answers:

> **What physical and technical systems exist, what condition are they in, what service can they currently provide, what do they depend on, and how may they fail, fragment, adapt or recover?**

Infrastructure includes the systems that allow civilization to function materially.

Examples include:

```text
POWER

WATER

TRANSPORTATION

TELECOMMUNICATIONS

DATA INFRASTRUCTURE

HEALTHCARE FACILITIES

FUEL DISTRIBUTION INFRASTRUCTURE

LOGISTICS INFRASTRUCTURE

CRITICAL INDUSTRIAL INFRASTRUCTURE.
```

Infrastructure State does not simulate every wire, road, pump or server.

It models whether infrastructure can continue providing meaningful service.

---

# 2. Core Principle

Infrastructure is not binary.

Avoid:

```text
WORKING

OR

FAILED.
```

Infrastructure may instead be:

```text
physically intact
but disconnected

operational
but capacity-constrained

degraded
but stable

locally functional
but nationally fragmented

automated
but poorly monitored

manually operated

repairable
but lacking parts

connected
but supply-constrained

technically healthy
but deliberately isolated.
```

The central principle is:

> **Infrastructure rarely disappears all at once. More often, the relationships that allow it to function as one system fail first.**

---

# 3. Infrastructure State vs Coordination

Infrastructure condition and infrastructure coordination must remain separate.

Example:

```text
Physical Grid:
FUNCTIONAL

National Coordination:
FAILED
```

The equipment still works.

The integrated system does not.

Likewise:

```text
Physical Infrastructure:
DEGRADED

Regional Coordination:
STRONG
```

may allow local operators to preserve service despite technical deterioration.

Therefore:

```text
PHYSICAL CONDITION
≠
COORDINATION CAPABILITY.
```

---

# 4. Relationship to Infrastructure Monitoring Levels

Infrastructure State integrates with:

```text
Canon/Systems/
Infrastructure_Monitoring_Levels.md
```

The distinction is:

```text
INFRASTRUCTURE STATE

What is physically
and operationally true?


IML

How effectively can
operators observe,
monitor and coordinate it?
```

These systems influence one another.

They are not interchangeable.

---

# 5. Infrastructure Ownership

Infrastructure State owns authoritative external state concerning:

```text
physical infrastructure condition

technical service capability

operational status

capacity

demand relationship

redundancy

infrastructure dependencies

buffers

repairability

manual operating capability

automation capability

critical assets

connectivity

fragmentation

infrastructure-specific
recovery capacity.
```

---

# 6. What Infrastructure State Does Not Own

Infrastructure State does not own:

```text
Character knowledge

Character belief

public perception

rumor

information confidence

supply inventory

population behavior

authority legitimacy

institutional decision-making

social trust

Character workforce state.
```

Those belong to other authoritative systems.

Infrastructure may consume their outputs.

---

# 7. Infrastructure Hierarchy

Infrastructure may exist at several levels.

Conceptually:

```text
GLOBAL NETWORKS
        ↓
NATIONAL NETWORKS
        ↓
REGIONAL SYSTEMS
        ↓
LOCAL SYSTEMS
        ↓
CRITICAL ASSETS.
```

Not every asset requires individual simulation.

Infrastructure resolution should increase only where causal significance requires it.

---

# 8. Core Infrastructure Sectors

The primary infrastructure sectors are:

```text
POWER

WATER

TRANSPORTATION

TELECOMMUNICATIONS

DATA INFRASTRUCTURE

HEALTHCARE INFRASTRUCTURE

FUEL DISTRIBUTION INFRASTRUCTURE

LOGISTICS INFRASTRUCTURE

CRITICAL INDUSTRIAL INFRASTRUCTURE.
```

These represent infrastructure functions.

They do not imply that Infrastructure State owns every resource moving through them.

---

# 9. Infrastructure Sector Contract

Where appropriate, infrastructure sectors may expose:

```text
Condition

Service Level

Operational Status

Capacity

Demand

Pressure

Resilience

Redundancy

Automation Capability

Manual Operating Capability

Repair Capacity

Dependencies

Buffers

Trend

Recovery Capacity

Last Significant Change

Causal Sources.
```

Not every sector requires every field.

The shared contract exists for consistency.

---

# 10. Condition

Condition represents physical and technical health.

Conceptual states:

```text
INTACT

STRAINED

DEGRADED

CRITICAL

FAILED.
```

Condition describes infrastructure itself.

It does not describe observer knowledge about infrastructure.

---

# 11. Intact

```text
INTACT
```

means the infrastructure remains physically and technically capable of normal operation.

This does not guarantee normal service.

External dependencies may still limit operation.

---

# 12. Strained

```text
STRAINED
```

means the system remains largely capable but is under abnormal operational pressure.

Possible causes include:

```text
deferred maintenance

high demand

reduced staffing

restricted upstream input

limited redundancy

temporary damage.
```

---

# 13. Degraded

```text
DEGRADED
```

means meaningful technical capability has been lost.

Possible effects include:

```text
reduced capacity

intermittent service

manual workarounds

local outages

reduced redundancy

increased maintenance burden.
```

---

# 14. Critical

```text
CRITICAL
```

means infrastructure remains partially functional but cannot reliably provide expected service.

Failure risk is high.

Emergency operating measures may be required.

---

# 15. Failed

```text
FAILED
```

means the infrastructure can no longer perform its expected function at the simulated scale.

Failed does not necessarily mean destroyed.

Example:

```text
National Grid Coordination:
FAILED

Regional Grid Islands:
FUNCTIONAL.
```

The higher-level system failed.

Electricity still exists.

---

# 16. Operational Status

Condition and Operational Status must remain separate.

Possible status values may include:

```text
NORMAL

RESTRICTED

EMERGENCY

MANUAL

ISOLATED

SHUTDOWN

OFFLINE.
```

Example:

```text
Condition:
INTACT

Status:
ISOLATED.
```

This means the system is physically healthy but intentionally disconnected.

---

# 17. Service Level

Service Level represents what users and dependent systems are currently receiving.

Conceptual states may include:

```text
NORMAL

LIMITED

INTERRUPTED

CRITICAL

UNAVAILABLE.
```

Condition and Service Level are distinct.

---

# 18. Condition vs Service

Example:

```text
Power Condition:
DEGRADED

Power Service:
ADEQUATE.
```

This may occur because:

```text
demand has fallen

backup generation exists

rationing is effective

local redundancy remains.
```

Conversely:

```text
Power Condition:
INTACT

Power Service:
LIMITED
```

may occur because:

```text
fuel unavailable

system deliberately curtailed

upstream connection unavailable

authority prioritization changed.
```

Therefore:

```text
CONDITION
≠
SERVICE.
```

---

# 19. Capacity

Capacity represents how much service infrastructure can theoretically provide under current technical conditions.

Capacity may be represented numerically where justified.

Example:

```text
Capacity:
72%
```

or descriptively:

```text
FULL

HIGH

MODERATE

LOW

MINIMAL

NONE.
```

Avoid false precision when exact data adds little value.

---

# 20. Demand

Demand represents the load placed on infrastructure by dependent users and systems.

Conceptual values may include:

```text
LOW

NORMAL

HIGH

SEVERE

EXTREME.
```

Infrastructure may experience service failure even while physically intact if:

```text
DEMAND
>
AVAILABLE CAPACITY.
```

---

# 21. Operating Margin

Operating Margin is a derived relationship between capacity and demand.

Example:

```text
Capacity:
HIGH

Demand:
NORMAL

Margin:
SAFE.
```

versus:

```text
Capacity:
MODERATE

Demand:
HIGH

Margin:
CRITICAL.
```

Margin is derived state.

It must not become a separate authoritative owner.

---

# 22. Pressure

Infrastructure Pressure represents forces pushing infrastructure toward deteriorating condition or reduced service.

Possible sources include:

```text
excess demand

physical damage

aging equipment

maintenance delay

upstream failures

resource shortage

environmental stress

security conditions

workforce access problems

supply constraints

population change.
```

Pressure should always remain traceable to causes.

---

# 23. Resilience

Resilience represents infrastructure's ability to absorb disruption without major loss of function.

Possible sources include:

```text
redundancy

spare capacity

backup systems

manual operation

distributed architecture

local generation

alternative routes

buffer stocks

technical adaptability.
```

Resilience does not guarantee permanent survival.

---

# 24. Redundancy

Redundancy represents alternative infrastructure paths or capabilities.

Conceptual states may include:

```text
HIGH

MODERATE

LOW

NONE.
```

High redundancy may allow individual failures without meaningful service loss.

Highly optimized systems may have low redundancy despite high normal efficiency.

---

# 25. Efficiency vs Resilience

Canonical principle:

```text
EFFICIENCY
≠
RESILIENCE.
```

Example:

```text
SYSTEM A

Efficiency:
VERY HIGH

Redundancy:
LOW.
```

versus:

```text
SYSTEM B

Efficiency:
MODERATE

Redundancy:
HIGH.
```

Under normal conditions, System A may outperform System B.

During prolonged disruption, System B may survive longer.

---

# 26. Automation Capability

Automation Capability describes how much automated infrastructure control remains technically available.

Conceptual states may include:

```text
FULL

RESTRICTED

PARTIAL

MINIMAL

DISABLED.
```

Automation Capability is separate from:

```text
Automation Dependency.
```

---

# 27. Automation Dependency

Some infrastructure can tolerate automation loss.

Other infrastructure cannot.

Conceptually:

```text
LOW

MODERATE

HIGH

CRITICAL.
```

Example:

```text
Automation Capability:
RESTRICTED

Automation Dependency:
LOW
```

may have limited consequence.

But:

```text
Automation Capability:
RESTRICTED

Automation Dependency:
CRITICAL
```

may create severe operational pressure.

---

# 28. Manual Operation

Automation loss does not automatically equal failure.

Infrastructure may continue through manual or hybrid operation.

Manual operation may produce:

```text
lower capacity

slower response

greater staffing need

reduced coordination

higher fatigue

higher error exposure.
```

---

# 29. Manual Operating Capability

Conceptual states may include:

```text
HIGH

MODERATE

LOW

MINIMAL

NONE.
```

This represents infrastructure design and procedural ability to operate without normal automation.

It does not directly own workforce availability.

---

# 30. Human Dependency

Infrastructure depends on humans.

Relevant requirements may include:

```text
operators

engineers

technicians

dispatchers

repair teams

specialists

maintenance staff.
```

Infrastructure State may define:

```text
REQUIRED HUMAN CAPABILITY.
```

Actual available people belong to:

```text
Characters

Population

Institutions

Authority

depending on scale.
```

---

# 31. Workforce Access

Infrastructure may derive an operational workforce availability context from other systems.

Example:

```text
Required:
20 qualified technicians

Currently Available:
8

Result:
Repair Capacity reduced.
```

Infrastructure State may consume this state.

It should not become the authoritative owner of those people.

---

# 32. Specialist Dependency

Some infrastructure relies heavily on rare Expertise.

Example:

```text
General Workforce:
AVAILABLE

Specialized Grid Engineers:
SCARCE.
```

This may severely constrain repair or coordination despite adequate overall population.

---

# 33. Repair Capacity

Repair Capacity represents infrastructure's realistic ability to restore damaged function.

Conceptually:

```text
REPAIR CAPACITY
=
PERSONNEL
+
EXPERTISE
+
PARTS
+
TOOLS
+
TRANSPORT
+
INFORMATION
+
ACCESS
+
SECURITY
+
TIME.
```

Possible states:

```text
HIGH

MODERATE

LOW

MINIMAL

NONE.
```

---

# 34. Repair Capacity Is Not Repair

A system may have:

```text
Repair Capacity:
HIGH
```

without currently repairing anything.

Repair requires:

```text
decision

access

resources

priority

time

action.
```

Authority and Actor systems may determine whether repair actually occurs.

---

# 35. Repair Backlog

Infrastructure may accumulate unresolved technical problems.

Conceptual states may include:

```text
LOW

MODERATE

HIGH

SEVERE

CRITICAL.
```

A system may remain functional while backlog grows.

This creates hidden future pressure.

---

# 36. Maintenance Debt

Maintenance Debt represents deterioration risk created by deferred routine work.

Example:

```text
Condition:
INTACT

Maintenance Debt:
HIGH.
```

The infrastructure still works.

Its resilience is declining.

---

# 37. Spare Parts Dependency

Infrastructure repair often requires external Supply.

Infrastructure State should represent:

```text
PART REQUIREMENTS.
```

Supply State should own:

```text
WHETHER THOSE PARTS
ARE ACTUALLY AVAILABLE.
```

Therefore:

```text
INFRASTRUCTURE
NEEDS PART X

SUPPLY
OWNS AVAILABILITY
OF PART X.
```

---

# 38. Infrastructure Dependencies

Every infrastructure sector may identify critical dependencies.

Example:

```text
WATER SYSTEM

Depends On:

Power

Treatment Chemicals

Pumps

Communication

Human Operators.
```

Dependencies create potential cross-system consequences.

---

# 39. Dependency Strength

Dependencies may be classified conceptually as:

```text
SUPPORTING

IMPORTANT

CRITICAL.
```

Example:

```text
Hospital
→ Electricity:
CRITICAL

Hospital
→ Public Internet:
SUPPORTING.
```

---

# 40. Dependency Graph

Infrastructure is usually networked rather than linear.

Example:

```text
POWER
│
├── WATER
├── TELECOMMUNICATIONS
├── HEALTHCARE
├── DATA
└── TRANSPORTATION
        │
        ↓
       FUEL
        │
        └──────→ POWER.
```

Circular dependencies are normal.

---

# 41. Circular Dependency

Circular dependency becomes dangerous when several systems degrade simultaneously.

Example:

```text
POWER LOSS
↓
FUEL PUMPS FAIL
↓
GENERATOR FUEL DELIVERY FALLS
↓
BACKUP POWER DECLINES
↓
POWER LOSS WORSENS.
```

The simulation must support reinforcing loops.

---

# 42. Dependency Buffers

Dependencies should not always create immediate failure.

Buffers may include:

```text
battery reserves

water storage

fuel reserves

emergency generators

warehouse stock

manual procedures

local storage.
```

Example:

```text
Grid Power:
Unavailable

Hospital Backup:
96 hours.
```

This creates delayed consequence.

---

# 43. Buffers Are Time-Based

A buffer may deplete while an upstream dependency remains unavailable.

Example:

```text
T0

Backup Fuel:
96 hours


T+72H

Backup Fuel:
24 hours.
```

This is one of the most important mechanisms for realistic delayed infrastructure failure.

---

# 44. Cascading Failure

Infrastructure cascades occur when one system's degradation increases pressure on another.

Example:

```text
POWER
DEGRADED
↓
TELECOMMUNICATIONS
PRESSURE INCREASES
↓
COORDINATION
DEGRADES
↓
REPAIR RESPONSE
SLOWS
↓
POWER
PRESSURE INCREASES.
```

---

# 45. Cascades Are Not Automatic

Infrastructure failure should not automatically propagate.

Cascades may be interrupted through:

```text
redundancy

buffers

manual operation

rapid repair

local isolation

demand reduction

external support

alternative infrastructure.
```

Therefore:

```text
DEPENDENCY
≠
GUARANTEED CASCADE.
```

---

# 46. Controlled Isolation

Infrastructure operators may deliberately disconnect systems to prevent wider failure.

Examples:

```text
grid islanding

network segmentation

pipeline shutdown

bridge closure

data-center isolation

transport restriction.
```

Controlled isolation may reduce propagation risk while decreasing efficiency or coordination.

---

# 47. Isolation Tradeoff

Conceptually:

```text
CONNECTED SYSTEM

Efficiency:
HIGH

Coordination:
HIGH

Propagation Risk:
HIGHER.
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

Local Autonomy:
HIGHER.
```

Neither configuration is universally superior.

---

# 48. Fragmentation

Infrastructure Fragmentation occurs when local systems remain functional but higher-level integration no longer operates reliably.

Example:

```text
NATIONAL POWER SYSTEM

FRAGMENTED


REGION A:
FUNCTIONAL

REGION B:
FUNCTIONAL

REGION C:
DEGRADED

REGION D:
ISOLATED.
```

Power still exists.

National integration does not.

---

# 49. Fragmentation Is Not Failure

Canonical principle:

```text
FRAGMENTATION
≠
FAILURE.
```

A fragmented infrastructure environment may contain:

```text
functional local grids

regional radio

local transport

working hospitals

isolated data systems

independent water systems.
```

Civilization has not disappeared.

Integration has weakened.

---

# 50. Fragmentation May Be Derived

A future implementation may derive a fragmentation diagnostic from:

```text
lost connections

regional isolation

coordination loss

incompatible operating states

telemetry loss

local autonomy.
```

This should remain diagnostic.

Do not turn it into a primary gameplay score.

---

# 51. Power Infrastructure

Power infrastructure includes:

```text
generation

transmission

distribution

substations

grid control

backup generation.
```

Important dependencies may include:

```text
fuel

communications

human operators

control systems

transportation

critical components.
```

Power strongly influences other infrastructure.

---

# 52. Water Infrastructure

Water infrastructure includes:

```text
drinking-water treatment

pumping

storage

distribution

wastewater systems.
```

Dependencies may include:

```text
power

treatment chemicals

pumps

human operators

transportation

control systems.
```

Water may continue temporarily after power loss through storage, gravity and backup systems.

---

# 53. Telecommunications Infrastructure

Telecommunications infrastructure includes:

```text
cellular systems

fiber

radio infrastructure

satellite links

internet transport

emergency communications.
```

Physical telecom infrastructure belongs here.

The information carried over those systems belongs to:

```text
Information_State.md.
```

---

# 54. Transportation Infrastructure

Transportation infrastructure includes:

```text
roads

rail

bridges

tunnels

ports

airports

transit systems.
```

Transportation allows movement of:

```text
people

food

fuel

medicine

workers

repair parts

industrial goods.
```

Transportation availability is therefore a major cross-system dependency.

---

# 55. Fuel Distribution Infrastructure

Fuel Distribution Infrastructure includes:

```text
refineries

storage terminals

pipelines

distribution points

service stations

transfer infrastructure.
```

Infrastructure State owns:

```text
THE PHYSICAL
DISTRIBUTION SYSTEM.
```

Supply State owns:

```text
HOW MUCH FUEL
IS AVAILABLE.
```

This separation is mandatory.

---

# 56. Healthcare Infrastructure

Healthcare infrastructure includes physical and operational systems such as:

```text
hospitals

clinics

laboratories

EMS infrastructure

medical facilities.
```

Healthcare service also depends on:

```text
personnel

medicine

supplies

power

water

transportation

communication.
```

Therefore Infrastructure State owns:

```text
FACILITY
AND INFRASTRUCTURE CAPABILITY.
```

It does not own:

```text
medical personnel

medicine stock

population health.
```

---

# 57. Logistics Infrastructure

Logistics infrastructure includes:

```text
warehouses

distribution centers

freight terminals

routing infrastructure

loading systems

physical logistics hubs.
```

The distinction is:

```text
SUPPLY

What resources exist
and where?


LOGISTICS INFRASTRUCTURE

What physical systems
allow those resources
to move?
```

---

# 58. Data Infrastructure

Data Infrastructure includes:

```text
data centers

identity platforms

cloud systems

databases

control platforms

digital coordination infrastructure.
```

Dependencies may include:

```text
power

telecommunications

cooling

physical security

human operators.
```

Data infrastructure does not own:

```text
information truth

belief

knowledge.
```

---

# 59. Critical Industrial Infrastructure

Critical Industrial Infrastructure includes production systems required to sustain other infrastructure.

Examples include:

```text
electrical equipment production

industrial chemicals

machine parts

electronics

construction materials

pharmaceutical manufacturing

fuel processing.
```

Industrial loss may create delayed consequences months later.

---

# 60. Infrastructure Geography

Infrastructure is spatial.

Regional profiles may identify:

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
Regional medical center.
```

This geographic context should integrate with:

```text
Regional_State.md.
```

---

# 61. Critical Assets

Some assets may require individual simulation.

Examples:

```text
major power plant

substation

dam

water-treatment plant

refinery

pipeline junction

bridge

rail terminal

hospital

data center

satellite ground station.
```

---

# 62. Critical Asset Criteria

An asset should normally receive individual state when:

```text
failure has major consequences

it is systemically unique

Actors can meaningfully interact with it

it has important dependencies

its condition cannot be represented
adequately through regional abstraction.
```

Player presence alone should not be sufficient.

---

# 63. Critical Asset State

Conceptually:

```text
CRITICAL ASSET

ID

Type

Location

Condition

Operational Status

Service Capacity

Dependencies

Buffers

Automation Capability

Manual Operating Capability

Repair Requirements

Strategic Function

Last Significant Change.
```

This is conceptual architecture.

Not a required implementation schema.

---

# 64. Infrastructure Events

Possible infrastructure events include:

```text
equipment failure

capacity reduction

service interruption

grid separation

pipeline shutdown

bridge closure

data-center isolation

repair completion

manual-mode transition

network restoration.
```

Events should have clear causes and consequences.

---

# 65. Event Reach

Infrastructure event reach may be:

```text
LOCAL

REGIONAL

MULTI-REGIONAL

NATIONAL

GLOBAL.
```

Reach describes systemic scope.

Not dramatic importance.

---

# 66. Infrastructure State Change

Condition change may often follow paths such as:

```text
INTACT
↓
STRAINED
↓
DEGRADED
↓
CRITICAL
↓
FAILED.
```

But this is not a mandatory ladder.

Catastrophic damage may produce:

```text
INTACT
↓
FAILED.
```

Likewise recovery may skip intermediate states when causally justified.

---

# 67. Degradation Forces

Infrastructure degradation may emerge from:

```text
Pressure

Excess Demand

Physical Damage

Dependency Failure

Maintenance Debt

Loss of Redundancy

Buffer Depletion.
```

---

# 68. Stabilization Forces

Infrastructure stabilization may emerge from:

```text
Resilience

Redundancy

Repair

Buffers

Demand Reduction

Controlled Isolation

Adaptation

External Support.
```

State change should follow the balance of actual causal conditions.

---

# 69. Time Matters

Infrastructure often fails slowly.

Example:

```text
DAY 1

Fuel delivery reduced.


DAY 3

Generator reserves declining.


DAY 5

Telecom backup sites begin failing.


DAY 7

Regional communication coverage degrades.
```

Delayed consequences are central to believable infrastructure simulation.

---

# 70. Trend

Trend describes current direction.

Conceptually:

```text
IMPROVING

STABLE

DETERIORATING

VOLATILE.
```

Trend is separate from Condition.

Example:

```text
Condition:
DEGRADED

Trend:
IMPROVING.
```

---

# 71. Infrastructure Does Not Own Confidence

Avoid:

```text
Condition:
DEGRADED

Confidence:
LOW.
```

if `Condition` represents authoritative simulation truth.

Infrastructure State knows what is physically true.

Uncertainty about that truth belongs to:

```text
Information_State.md

Infrastructure Monitoring Levels

observer-specific systems.
```

---

# 72. Telemetry Boundary

Telemetry represents infrastructure-generated observation capability.

The physical existence of telemetry systems belongs to Infrastructure.

The meaning of telemetry as observation evidence belongs to:

```text
Information State
/
IML.
```

Example:

```text
Telemetry Infrastructure:
PARTIAL

Actual Grid Condition:
DEGRADED.
```

Information systems determine who receives and trusts the telemetry.

---

# 73. Operational Visibility

Operational Visibility is primarily an observer / monitoring concept.

Infrastructure State may expose:

```text
AVAILABLE TELEMETRY

AVAILABLE SENSORS

AVAILABLE COMMUNICATION LINKS.
```

IML and Information State determine:

```text
HOW WELL
OPERATORS CAN
UNDERSTAND
THE SYSTEM.
```

---

# 74. Protective Shutdown

Protective shutdown must remain distinct from technical failure.

Example:

```text
Condition:
INTACT

Status:
SHUTDOWN

Reason:
PROTECTIVE ISOLATION.
```

This distinction is essential.

The system may be healthy but intentionally inactive.

---

# 75. Load Shedding

Infrastructure operators may reduce service deliberately to preserve system stability.

Examples:

```text
rolling blackouts

bandwidth restriction

water pressure reduction

transit reduction

industrial curtailment.
```

Load shedding is often evidence of active system management.

Not automatic collapse.

---

# 76. Fuel Rationing Boundary

Fuel rationing is not itself infrastructure state.

Infrastructure State may represent:

```text
Fuel Distribution Capacity.
```

Supply State may represent:

```text
Fuel Availability.
```

Authority may decide:

```text
Who receives fuel.
```

This prevents ownership overlap.

---

# 77. Service Prioritization

Authorities or institutions may prioritize infrastructure service.

Infrastructure State should consume those decisions.

Example:

```text
Priority:

1. Hospital

2. Water Treatment

3. Emergency Communications.
```

The prioritization decision belongs to Authority or the relevant operating institution.

Infrastructure State resolves resulting service conditions.

---

# 78. Demand Reduction

Population and institutional behavior may reduce infrastructure demand.

Examples:

```text
conservation

reduced travel

industrial curtailment

voluntary shutdown

resource rationing.
```

Population and Authority systems own the behavior.

Infrastructure State consumes the resulting demand changes.

---

# 79. Infrastructure Recovery

Infrastructure recovery may occur through:

```text
repair

replacement

reconnection

resource delivery

restored human access

restored automation

reduced demand

external assistance

adaptation.
```

Recovery should remain causal.

---

# 80. Recovery Is Not Restoration

Example:

```text
NATIONAL GRID
FAILS
↓
REGIONAL MICROGRIDS
EMERGE
↓
ELECTRICITY SERVICE
RETURNS.
```

Function recovered.

The previous system did not.

Therefore:

```text
RECOVERY
≠
RESTORATION.
```

---

# 81. Infrastructure Transformation

Long-term disruption may permanently change infrastructure architecture.

Example:

```text
BEFORE

Centralized

Automated

Highly connected

Efficient.
```

may become:

```text
AFTER

Regional

Hybrid

Locally coordinated

Redundant

Less efficient

More autonomous.
```

This is not necessarily technological regression.

It may be technological reorganization.

---

# 82. Infrastructure and Supply

Canonical boundary:

```text
INFRASTRUCTURE

Can the physical
system move,
process,
store or deliver
the resource?


SUPPLY

Does the resource
exist and remain
available?
```

Example:

```text
Fuel Supply:
ADEQUATE

Fuel Distribution Infrastructure:
DEGRADED
```

may still produce local shortages.

---

# 83. Infrastructure and Information

Infrastructure provides:

```text
physical communication systems

telemetry capability

sensors

data infrastructure.
```

Information State owns:

```text
information availability

reliability

propagation

verification

rumor

observer knowledge.
```

The relationship is bidirectional.

Infrastructure degradation may damage information flow.

Poor information may reduce infrastructure coordination.

---

# 84. Infrastructure and Authority

Authority may influence infrastructure through:

```text
prioritization

rationing

emergency orders

isolation

access control

repair coordination.
```

Infrastructure may affect Authority through:

```text
service availability

institutional reach

communication capability

operational capacity.
```

Neither owns the other.

---

# 85. Infrastructure and Population

Population State may affect:

```text
demand

workforce availability

travel demand

service consumption

local pressure.
```

Infrastructure may affect:

```text
mobility

water access

communication

energy access

healthcare access.
```

Population behavior remains outside Infrastructure ownership.

---

# 86. Infrastructure and Security

Security may affect infrastructure through:

```text
access

repair ability

physical damage

protection requirements

transport safety.
```

Infrastructure may affect Security through:

```text
lighting

communications

transport

surveillance

emergency services

resource access.
```

Security owns security state.

Infrastructure owns infrastructure state.

---

# 87. Infrastructure and Regional State

`Regional_State.md` provides:

```text
geography

regional connections

regional dependencies

local exceptions

strategic context.
```

Infrastructure State provides:

```text
technical condition

service capability

dependencies

buffers

repairability

fragmentation.
```

---

# 88. Infrastructure and World State

`World_State.md` provides:

```text
high-level external world truth

global pressure

historical era

regional context.
```

Infrastructure State provides one authoritative external domain feeding that world state.

---

# 89. Infrastructure and Action Resolution

Characters or institutions may attempt:

```text
repair

shutdown

reconnection

isolation

construction

sabotage

inspection

manual operation.
```

Action Resolution combines:

```text
Actor Capability

Tools

Access

Infrastructure State

Environment

Resources

Time
↓
Outcome.
```

Infrastructure State supplies the infrastructure-specific world conditions.

---

# 90. Player Interaction

Player Characters obey the same infrastructure rules as every other Actor.

They may influence infrastructure through:

```text
repair

protection

resource delivery

technical expertise

reconnaissance

negotiation

reconnection

isolation

construction

sabotage

adaptation.
```

Player status does not guarantee infrastructure change.

---

# 91. Infrastructure Does Not Generate Missions

Avoid:

```text
Infrastructure Crisis
↓
Generate Quest.
```

Prefer:

```text
Infrastructure State
↓
Real World Problem
↓
Actors Respond
↓
Possible Narrative Relevance.
```

Narrative may turn a real infrastructure problem into playable content.

Infrastructure State does not own the mission.

---

# 92. Simulation Resolution

Infrastructure State must support adaptive simulation resolution.

Conceptually:

```text
LOW

MEDIUM

HIGH.
```

Resolution changes detail.

Not reality.

---

# 93. Low Resolution

Low-resolution Infrastructure State may preserve:

```text
major sector condition

service trend

pressure

resilience

major dependencies

major outages

major recovery

fragmentation state.
```

---

# 94. Medium Resolution

Medium resolution may additionally preserve:

```text
sector-specific conditions

major buffers

major connections

repair capacity

major critical assets

significant events.
```

---

# 95. High Resolution

High-resolution infrastructure simulation may include:

```text
specific assets

capacity

buffers

dependency timing

repair requirements

operational modes

specific local service

active Action Resolution.
```

---

# 96. Resolution Follows Causal Relevance

A distant infrastructure system may require high resolution if it is:

```text
nationally critical

under active failure

supporting a major region

part of a cascading event

central to Aurora activity.
```

Player proximity is not the only escalation trigger.

---

# 97. Infrastructure Persistence

Infrastructure State persists through:

```text
player absence

regional travel

session boundaries

Story Threads

resolution changes

time advancement.
```

A bridge remains destroyed when the player leaves.

A repaired grid remains repaired.

A buffer continues depleting.

---

# 98. Minimum Infrastructure State

A minimal viable infrastructure representation should be able to express:

```text
Region

Sector

Condition

Service Level

Operational Status

Capacity

Demand

Pressure

Resilience

Redundancy

Trend

Automation Capability

Manual Operating Capability

Repair Capacity

Major Dependencies

Major Buffers

Critical Assets

Recovery Capacity

Last Significant Change.
```

Everything beyond this should justify its complexity.

---

# 99. Infrastructure Example

```text
REGION:
Northern Virginia


POWER

Condition:
DEGRADED

Service:
LIMITED

Operational Status:
RESTRICTED

Pressure:
HIGH

Resilience:
MODERATE

Redundancy:
LOW

Trend:
DETERIORATING

Automation Capability:
PARTIAL

Manual Operating Capability:
MODERATE

Repair Capacity:
LOW

Recovery Capacity:
MODERATE


MAJOR DEPENDENCIES

Fuel

Telecommunications

Specialized Workforce

Replacement Components


MAJOR BUFFER

Emergency Generation:
72 hours


IML

Referenced from:
Infrastructure_Monitoring_Levels.md
```

---

# 100. Dependency Event Example

```text
EVENT:

Regional fuel delivery reduced.
```

Immediate consequence:

```text
Fuel Availability:
Supply State changes.
```

Infrastructure consequence:

```text
Fuel Distribution:
Still Functional

Generator Buffer:
Begins Depleting

Transportation Demand Pressure:
Increases.
```

After several days:

```text
Telecommunication Backup Power:
STRAINED

Hospital Backup Power:
CONSTRAINED.
```

The result is delayed systemic pressure.

Not instant collapse.

---

# 101. Protective Response Example

```text
EVENT:

Unexplained grid coordination anomalies.


AUTHORITY DECISION:

Regional grid isolation.


INFRASTRUCTURE RESULT:

Condition:
INTACT

Operational Status:
ISOLATED

Regional Service:
LIMITED

Propagation Risk:
REDUCED

Efficiency:
REDUCED.
```

One risk was reduced.

Another cost was created.

---

# 102. Recovery Event Example

```text
EVENT:

Rail corridor restored.
```

Possible downstream consequences:

```text
Spare Parts Supply:
Improves

Fuel Distribution:
Improves

Repair Capacity:
Improves

Maintenance Backlog:
Begins Declining

Infrastructure Pressure:
Reduced.
```

One restored connection may therefore influence several infrastructure sectors.

---

# 103. Infrastructure State Invariants

## INF-INV-001 — Infrastructure Is Not Binary

Infrastructure may operate under degraded, fragmented or emergency conditions.

---

## INF-INV-002 — Condition and Service Are Separate

Physical health does not directly equal delivered service.

---

## INF-INV-003 — Condition and Operational Status Are Separate

Infrastructure may be healthy but intentionally inactive.

---

## INF-INV-004 — Infrastructure State and IML Are Separate

Physical state and monitoring/coordination capability must not be collapsed.

---

## INF-INV-005 — Infrastructure May Function Locally After Higher-Level Integration Fails

Fragmentation is not universal failure.

---

## INF-INV-006 — Automation Loss Does Not Automatically Equal Failure

Manual or hybrid operation may preserve function.

---

## INF-INV-007 — Manual Operation Has Costs

Capacity, staffing, coordination and fatigue may change.

---

## INF-INV-008 — Dependencies May Produce Delayed Consequences

Buffers prevent instant cascades.

---

## INF-INV-009 — Cascades Are Conditional

Dependency does not guarantee propagation.

---

## INF-INV-010 — Controlled Isolation May Be Rational

Infrastructure may deliberately sacrifice integration to preserve local function.

---

## INF-INV-011 — Repair Requires Causal Inputs

Time, people, parts, access and resources matter.

---

## INF-INV-012 — Recovery Does Not Require Restoration

New infrastructure architecture may replace old systems.

---

## INF-INV-013 — Supply and Infrastructure Are Distinct

Resource existence and distribution capability must not be conflated.

---

## INF-INV-014 — Infrastructure Does Not Own Observer Confidence

Uncertainty belongs to Information and monitoring systems.

---

## INF-INV-015 — Infrastructure Does Not Own People

Human capability is consumed from Character, Population and institutional systems.

---

## INF-INV-016 — Infrastructure Does Not Own Authority Decisions

Prioritization and rationing decisions belong to the relevant authority.

---

## INF-INV-017 — Infrastructure Does Not Own Population Behavior

Demand may depend on population state without transferring ownership.

---

## INF-INV-018 — Infrastructure Persists Off-Screen

Player absence does not freeze technical systems.

---

## INF-INV-019 — Resolution Changes Detail, Not Infrastructure Reality

Low-resolution infrastructure remains causally active.

---

## INF-INV-020 — Major Infrastructure Changes Must Be Explainable

Condition changes require traceable causes.

---

# 104. Development Locks

Future Infrastructure State development must not introduce:

```text
binary working / failed logic

condition equals service

condition equals operational status

IML equals infrastructure condition

infrastructure-owned confidence

infrastructure-owned public perception

infrastructure-owned Character knowledge

fuel availability owned by Infrastructure

medicine supply owned by Infrastructure

population mood owned by Infrastructure

authority choice owned by Infrastructure

automatic cascades

automatic collapse

automatic repair

manual mode equals failure

automation loss equals failure

fragmentation equals disappearance

player-triggered infrastructure activation

frozen distant infrastructure

narrative-forced failures

random critical failure for drama

player-exclusive repair physics

global Infrastructure Health score.
```

---

# 105. Infrastructure Architecture Test

Before adding a new infrastructure field or mechanic, ask:

```text
IS THIS
PHYSICAL OR TECHNICAL
INFRASTRUCTURE STATE?

OR

DOES ANOTHER SYSTEM
OWN IT?

WHAT CONDITION
IS THE SYSTEM IN?

WHAT SERVICE
IS IT PROVIDING?

WHAT IS ITS
OPERATIONAL STATUS?

WHAT DOES IT
DEPEND ON?

WHAT DEPENDS
ON IT?

WHAT BUFFERS
EXIST?

WHAT REDUNDANCY
EXISTS?

CAN IT OPERATE
MANUALLY?

WHAT HUMAN
CAPABILITY
DOES IT REQUIRE?

CAN IT BE
REPAIRED?

WHAT PARTS
AND RESOURCES
ARE REQUIRED?

WHAT PRESSURE
IS ACTING ON IT?

WHAT IS
ITS TREND?

WHAT WOULD
HAPPEN
IF NOTHING CHANGED?

CAN THE SYSTEM
FRAGMENT
WITHOUT DISAPPEARING?

CAN IT ADAPT
WITHOUT RETURNING
TO ITS OLD FORM?
```

---

# 106. Final Infrastructure Model

Conceptually:

```text
REGIONAL STATE
        ↓
────────────────────────────
INFRASTRUCTURE STATE
────────────────────────────
        │
        ├── Power
        ├── Water
        ├── Transportation
        ├── Telecommunications
        ├── Data Infrastructure
        ├── Healthcare Infrastructure
        ├── Fuel Distribution Infrastructure
        ├── Logistics Infrastructure
        └── Critical Industry
                │
                ↓
        FOR EACH RELEVANT SECTOR
                │
                ├── Condition
                ├── Service Level
                ├── Operational Status
                ├── Capacity
                ├── Demand
                ├── Pressure
                ├── Resilience
                ├── Redundancy
                ├── Automation Capability
                ├── Manual Operating Capability
                ├── Repair Capacity
                ├── Dependencies
                ├── Buffers
                ├── Trend
                └── Recovery Capacity
                        │
                        ↓
SUPPLY
+
HUMAN CAPABILITY
+
AUTHORITY
+
SECURITY
+
INFORMATION
+
TIME
                        ↓
INFRASTRUCTURE CHANGE
                        ↓
SERVICE CONSEQUENCES
                        ↓
REGIONAL / WORLD CONSEQUENCES
                        ↓
UPDATED INFRASTRUCTURE STATE.
```

---

# 107. Infrastructure North Star

The system succeeds when Project Ascension can answer:

```text
WHAT PHYSICALLY
STILL EXISTS?

WHAT STILL WORKS?

WHAT SERVICE
IS ACTUALLY
BEING DELIVERED?

WHAT HAS BEEN
DISCONNECTED?

WHAT HAS BEEN
ISOLATED
DELIBERATELY?

WHAT DOES
THE SYSTEM
DEPEND ON?

WHAT BUFFERS
ARE RUNNING OUT?

WHO IS REQUIRED
TO OPERATE IT?

CAN IT BE
RUN MANUALLY?

CAN IT BE
REPAIRED?

WHAT PARTS
ARE NEEDED?

WHAT HAPPENS
IF NOTHING CHANGES?

CAN LOCAL SYSTEMS
CONTINUE
AFTER NATIONAL
COORDINATION FAILS?

AND

CAN CIVILIZATION
REORGANIZE
THE INFRASTRUCTURE

RATHER THAN
SIMPLY LOSING IT?
```

---

# 108. Closing Principle

Project Ascension should never reduce infrastructure collapse to:

```text
THE GRID FAILED

THEREFORE

NO ELECTRICITY.
```

The world should instead be capable of producing:

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
LIMITED.
```

Infrastructure does not simply switch off.

It degrades.

It fragments.

It isolates.

It consumes reserves.

Humans improvise.

Operators prioritize.

Local systems survive.

Some networks disappear.

Others reorganize.

Some infrastructure becomes less efficient but more resilient.

And sometimes the system that survives is no longer the system that existed before.

The central principle is:

> **Infrastructure failure is not the disappearance of technology. It is the loss, degradation or reorganization of the systems that allow technology to function reliably at scale.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-08-09 | Established initial infrastructure sector, condition, service, dependency, automation, workforce, fragmentation, cascade, repair and adaptation framework. |
| 1.0 | 2026-09-01 | Rebuilt Infrastructure State as canonical architecture aligned with World State, Regional State and Simulation Architecture. Preserved condition/service/status separation, IML boundaries, dependencies, buffers, fragmentation, manual operation, repair and adaptation while clarifying ownership boundaries with Supply, Information, Authority, Population, Characters and Security. Removed infrastructure-owned confidence, separated fuel availability from fuel distribution infrastructure, distinguished healthcare facilities from medical supply and workforce, reframed workforce as a consumed external capability, strengthened adaptive simulation resolution and cross-system Action Resolution, and established invariants and development locks preventing binary, player-centric and automatic cascade logic. |