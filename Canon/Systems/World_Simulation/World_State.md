# PROJECT ASCENSION
# World State System

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | World State System |
| Location | `Canon/Systems/World_Simulation/World_State.md` |
| Version | 1.0 |
| Status | Canonical Architecture |
| Category | World Simulation / World State |
| Owner | World Simulation |
| Last Updated | 2026-09-01 |
| Primary Function | Define the authoritative high-level representation of current external world conditions and how those conditions remain persistent, regional, causal, explainable and independent of observer knowledge |

---

# 1. Purpose

The World State System defines the highest-level dynamic representation of the external world within Project Ascension.

It answers:

> **What is objectively true about the simulated world at this moment?**

The World State does not attempt to describe every person, event, building, institution or interaction.

Instead, it provides the authoritative structure through which large-scale world conditions can exist, change and interact.

Conceptually:

```text
WORLD STATE
=
CURRENT EXTERNAL
SIMULATION TRUTH
AT TIME T.
```

It provides context for:

- World Simulation
- Regions
- Infrastructure
- Supply
- Security
- Authority
- Information
- Population
- Factions
- Society
- Characters
- Life
- Living Campaign Engine
- Story Framework
- Game Master

The World State describes the world.

It does not determine what Characters choose to do within it.

---

# 2. Core Definition

World State is:

> **The authoritative high-level representation of current external conditions within the simulated world, including global conditions, regional conditions, systemic pressures, dependencies, events, historical consequences and persistent campaign divergence.**

Conceptually:

```text
SIMULATION TIME
+
CANON FOUNDATION
+
GLOBAL CONDITIONS
+
REGIONAL CONDITIONS
+
SYSTEMIC PRESSURES
+
DEPENDENCIES
+
WORLD EVENTS
+
ACCUMULATED CONSEQUENCES
↓
CURRENT WORLD STATE.
```

World State represents what currently exists.

Other systems determine:

- what Characters know about it
- what Factions believe about it
- how Society interprets it
- how Characters respond to it
- how the story presents it

---

# 3. Historical Era Is Not Dynamic World State

Project Ascension uses canonical historical eras:

```text
WORLD STATE 01
THE CONNECTED WORLD

WORLD STATE 02
THE TRANSITION

WORLD STATE 03
THE FRACTURED WORLD

WORLD STATE 04
THE RECONNECTION.
```

These are broad historical phases.

They are not the same thing as the dynamic World State defined in this document.

For clarity:

```text
HISTORICAL ERA
=
BROAD CANONICAL
HISTORICAL CONTEXT

DYNAMIC WORLD STATE
=
WHAT THE WORLD
IS ACTUALLY LIKE
RIGHT NOW.
```

Example:

```text
HISTORICAL ERA:

THE FRACTURED WORLD


NORTHERN VIRGINIA:

Infrastructure = Degraded

Supply = Constrained

Security = Stable

Authority = Regional


GREAT LAKES:

Infrastructure = Stable

Supply = Stable

Security = Strained

Authority = Cooperative Regional
```

Both regions exist during the same historical era.

Their realities are different.

---

# 4. Historical Era Reference

Every World State must reference its current canonical historical era.

Conceptually:

```text
WORLD STATE

Historical Era Reference:
WS-03 — The Fractured World
```

The Historical Era provides broad context such as:

- technological environment
- institutional expectations
- global connectivity
- common historical knowledge
- broad infrastructure patterns
- political context
- cultural memory
- baseline systemic pressures

But:

```text
HISTORICAL ERA
DOES NOT
DICTATE
LOCAL REALITY.
```

A region inside The Fractured World may be highly functional.

A region inside The Transition may already be experiencing severe systemic failure.

---

# 5. World State Is Not One Score

Project Ascension must never reduce the world to:

```text
WORLD STABILITY = 42
```

or:

```text
UNITED STATES = CRITICAL.
```

Such values destroy important differences.

Instead:

```text
WORLD STATE
=
MULTIPLE
INTERACTING
CONDITIONS.
```

A region may simultaneously have:

```text
Infrastructure:
DEGRADED

Supply:
STABLE

Security:
UNSTABLE

Authority:
FUNCTIONAL

Population:
INCREASING.
```

Human societies do not collapse or recover along one universal axis.

---

# 6. World State Hierarchy

Conceptually:

```text
WORLD
│
├── GLOBAL CONDITIONS
│
├── NATIONS
│   │
│   └── REGIONS
│       │
│       ├── LOCAL AREAS
│       │
│       └── COMMUNITIES / SETTLEMENTS
│
└── CROSS-REGIONAL SYSTEMS
```

These levels influence one another.

But influence is not deterministic.

Conceptually:

```text
HIGHER LEVEL
↓
CREATES PRESSURE
AND CONTEXT

LOWER LEVEL
↓
RESPONDS ACCORDING TO
LOCAL CONDITIONS

MULTIPLE LOWER LEVELS
↓
MAY CHANGE
HIGHER-LEVEL CONDITIONS.
```

---

# 7. Global Conditions

Global Conditions represent large-scale external conditions affecting significant portions of the world.

Possible examples include:

```text
Global Connectivity

Global Trade

International Stability

Financial Stability

Information Reliability

Technological Coordination

Global Mobility

Geopolitical Pressure.
```

These are high-level condition references.

World State may represent their current condition.

It does not need to own every mechanism producing them.

Example:

```text
Global Trade:
CONSTRAINED
```

may emerge from:

```text
Shipping disruption
+
Energy shortage
+
Regional conflict
+
Port degradation
+
Financial instability.
```

Detailed causality belongs to the relevant authoritative systems.

World State preserves the resulting external condition and its causal references.

---

# 8. Global Conditions Create Pressure

A global condition does not dictate identical outcomes everywhere.

Example:

```text
GLOBAL FOOD TRADE
DEGRADED
```

may create:

```text
REGION A

Local agriculture:
Strong

Storage:
Strong

Transportation:
Functional

Supply:
STABLE
```

while:

```text
REGION B

Import dependence:
High

Population density:
High

Storage:
Weak

Transportation:
Degraded

Supply:
CRITICAL.
```

Therefore:

```text
GLOBAL CONDITIONS
CREATE PRESSURE

NOT

IDENTICAL
REGIONAL OUTCOMES.
```

---

# 9. National State

National State is an intermediate aggregation and coordination layer.

It may represent:

- national authority
- national infrastructure coordination
- emergency communication
- strategic reserves
- military capacity
- national supply coordination
- national mobility
- regional cohesion
- institutional continuity

National State should not flatten regional differences.

Avoid:

```text
UNITED STATES
=
FAILED.
```

Prefer:

```text
UNITED STATES

National Coordination:
DEGRADED

Regional Cohesion:
LOW

Strategic Infrastructure:
PARTIALLY FUNCTIONAL

Regional Divergence:
HIGH.
```

National State may remain useful even when national authority becomes weak.

---

# 10. Regions Are the Primary Operational World Units

Regions are the primary operational units of large-scale World Simulation.

Detailed regional architecture belongs to:

```text
Canon/Systems/World_Simulation/Regional_State.md
```

A region may represent a geographically and systemically meaningful area such as:

```text
Northern Virginia

Shenandoah Valley

Great Lakes

Pacific Northwest

Southern California

Central Texas.
```

Regions should reflect real geography wherever practical.

Regional boundaries should exist because they matter to simulation.

They should not be arbitrary map partitions.

---

# 11. Regional Divergence

Regional divergence is fundamental to Project Ascension.

Conceptually:

```text
ONE COUNTRY

MANY REALITIES.
```

Example:

```text
UNITED STATES

Northern Virginia:
Infrastructure = Degraded

Great Lakes:
Infrastructure = Stable

Southern California:
Infrastructure = Critical

Great Plains:
Infrastructure = Strained

New England:
Infrastructure = Stable.
```

The existence of national or global pressure does not eliminate regional variation.

This principle becomes increasingly important during The Transition and The Fractured World.

---

# 12. Core World Domains

The primary World Simulation domains are:

```text
INFRASTRUCTURE

SUPPLY

SECURITY

AUTHORITY

INFORMATION

POPULATION.
```

Their detailed architecture belongs to:

```text
Infrastructure_State.md

Supply_State.md

Security_State.md

Authority_State.md

Information_State.md

Population_State.md
```

World State references and coordinates their authoritative outputs.

It does not duplicate their detailed internal logic.

---

# 13. Domain State Model

Where appropriate, World Simulation domains may expose a common high-level structure.

Conceptually:

```text
DOMAIN STATE
│
├── Current State
├── Pressure
├── Resilience
├── Trend
├── Recovery Capacity
├── Last Significant Change
└── Causal Sources
```

Not every domain must use identical internal mechanics.

The shared model exists to improve:

- consistency
- explainability
- simulation coordination
- debugging
- cross-system reasoning

---

# 14. Current State

Current State describes the authoritative external condition that exists now.

Example:

```text
Supply:

CONSTRAINED
```

or:

```text
Infrastructure:

DEGRADED.
```

Current State is not:

- prediction
- public perception
- Character belief
- Faction belief
- narrative interpretation

It is simulation truth.

---

# 15. Pressure

Pressure represents forces currently pushing a domain toward change.

Example:

```text
Infrastructure Pressure:

HIGH
```

Possible sources:

- fuel shortage
- workforce shortage
- increased demand
- spare-part shortage
- extreme weather
- conflict
- migration
- institutional degradation
- cyber disruption
- infrastructure dependency failure

Pressure does not guarantee change.

---

# 16. Pressure Requires Sources

Pressure should be explainable.

Avoid:

```text
Supply Pressure:
HIGH
```

without explanation.

Prefer:

```text
Supply Pressure:
HIGH

Sources:

Reduced rail capacity

Fuel restrictions

Population increase

Neighboring region export collapse.
```

This preserves causality.

---

# 17. Resilience

Resilience represents a system's ability to absorb pressure while maintaining function.

Possible resilience sources include:

- redundancy
- local expertise
- stockpiles
- institutional competence
- alternative infrastructure
- local production
- community cooperation
- geographic advantage
- distributed systems
- established procedures

Example:

```text
Supply:

STABLE

Pressure:

HIGH

Resilience:

HIGH.
```

This means the current system remains functional despite significant pressure.

---

# 18. Resilience Is Not Invulnerability

High resilience does not mean permanent stability.

Conceptually:

```text
PRESSURE
+
TIME
+
ACCUMULATED DAMAGE
+
RESOURCE DEPLETION
↓
MAY EXCEED
RESILIENCE.
```

A resilient system can still fail.

It may simply fail later, more slowly or differently.

---

# 19. Trend

Trend represents current direction.

Conceptually:

```text
IMPROVING

STABLE

DETERIORATING

VOLATILE.
```

Example:

```text
Supply:

CONSTRAINED

Trend:

IMPROVING
```

is fundamentally different from:

```text
Supply:

CONSTRAINED

Trend:

DETERIORATING.
```

Current State describes now.

Trend describes direction.

---

# 20. Recovery Capacity

Recovery Capacity represents the realistic ability of a system to improve after disruption.

Possible factors include:

- available resources
- technical capability
- functioning authority
- external assistance
- spare capacity
- logistics
- local expertise
- social cooperation
- infrastructure access
- time

Recovery Capacity does not itself mean recovery is occurring.

Conceptually:

```text
RECOVERY CAPACITY
=
ABILITY TO RECOVER

NOT

RECOVERY ITSELF.
```

Actual recovery requires causal conditions.

Detailed recovery and escalation logic belongs to:

```text
Escalation_and_Recovery.md
```

---

# 21. Recovery Is Not a Peer World Domain

Recovery should not normally be treated as equivalent to:

```text
Infrastructure

Supply

Security

Authority.
```

Instead, recovery is a process affecting domain state.

Conceptually:

```text
INFRASTRUCTURE

State
Pressure
Resilience
Trend
Recovery Capacity
```

rather than:

```text
Infrastructure
Supply
Security
Recovery
```

as four equivalent categories.

This keeps world-state ownership clear.

---

# 22. World Truth

World Simulation maintains authoritative external truth.

Conceptually:

```text
WORLD TRUTH
=
WHAT IS
ACTUALLY TRUE
IN THE SIMULATION.
```

Example:

```text
Actual Supply State:

STRAINED.
```

This remains true even if no Character knows it.

---

# 23. World Truth Is Not Observer Knowledge

A critical Project Ascension distinction is:

```text
WORLD TRUTH
≠
CHARACTER KNOWLEDGE
≠
PLAYER KNOWLEDGE
≠
FACTION KNOWLEDGE
≠
PUBLIC UNDERSTANDING
≠
AURORA'S MODEL.
```

World State owns the first.

Other systems own the others.

---

# 24. Observed State

Observers may possess incomplete, outdated or incorrect representations of World State.

Example:

```text
ACTUAL SUPPLY:

STRAINED


GOVERNMENT ESTIMATE:

STRAINED


PUBLIC PERCEPTION:

CRITICAL


CHARACTER BELIEF:

STABLE.
```

These can coexist.

World State should not overwrite observer knowledge merely because authoritative simulation truth changes.

Information must propagate causally.

---

# 25. Observation Confidence

Confidence belongs to knowledge about state rather than World Truth itself.

Therefore avoid:

```text
Actual Security:
STABLE

World State Confidence:
LOW.
```

The authoritative simulation should know its own state.

Instead:

```text
Observed Security:
STABLE

Observation Confidence:
LOW

Last Reliable Report:
6 days ago.
```

Detailed handling belongs primarily to:

```text
Information_State.md
```

and relevant observer systems.

---

# 26. Information Must Travel

World truth is not automatically distributed.

Information may move through:

- communication
- observation
- reports
- media
- institutions
- intelligence
- Relationships
- Factions
- direct contact
- digital networks
- Aurora

Therefore:

```text
EVENT OCCURS

≠

EVERYONE KNOWS.
```

This distinction is fundamental to Project Ascension.

---

# 27. World Events

World Events are meaningful occurrences that alter or interact with external World State.

Examples:

```text
Power plant shutdown

Major storm

Bridge collapse

Regional election

Trade agreement

Migration wave

Hospital closure

Fuel shipment

Communication restoration

Settlement alliance.
```

Events may occur at:

- global
- national
- regional
- local

scales.

---

# 28. World Event Structure

Conceptually:

```text
WORLD EVENT
│
├── ID
├── Time
├── Location
├── Type
├── Cause
├── Participants
├── Immediate Effects
├── Secondary Effects
├── Visibility
├── State Changes
└── Historical Significance
```

This is conceptual architecture.

It is not yet an implementation schema.

---

# 29. Events Should Have Causes

Whenever possible:

```text
EVENT
↓
SHOULD HAVE
CAUSAL HISTORY.
```

Example:

```text
EVENT:

Regional Fuel Rationing


SUPPORTED BY:

Supply = Constrained

Fuel Availability = Critical

Authority = Functional

Strategic Reserves = Low.
```

This is preferable to generating rationing merely because the story needs tension.

---

# 30. External Events

Not every event must emerge from existing internal simulation pressure.

External events may include:

- storms
- earthquakes
- disease outbreaks
- technological discoveries
- foreign actions
- accidents
- environmental events

These enter the simulation as new causal inputs.

Their consequences still depend on existing World State.

---

# 31. Same Event, Different Consequences

Example:

```text
HURRICANE
↓
REGION A

Infrastructure:
STABLE

Resilience:
HIGH

Authority:
FUNCTIONAL

Recovery Capacity:
HIGH
```

may produce:

```text
Temporary disruption

Rapid repair

Limited displacement.
```

The same hurricane affecting:

```text
REGION B

Infrastructure:
DEGRADED

Resilience:
LOW

Authority:
WEAK

Recovery Capacity:
LOW
```

may produce:

```text
Infrastructure failure

Supply disruption

Population movement

Security pressure

Long-term decline.
```

Therefore:

```text
EVENT
≠
FIXED CONSEQUENCE.
```

Existing conditions matter.

---

# 32. Systemic History

World Simulation should preserve meaningful systemic history.

This is not Character Memory.

Conceptually:

```text
SYSTEMIC HISTORY
=
PERSISTENT RECORD
OF WORLD-RELEVANT
PAST CONDITIONS
AND EVENTS.
```

Examples include:

- infrastructure collapse
- migration
- political transition
- regional conflict
- settlement founding
- settlement destruction
- major alliance
- recovery milestone
- major discovery
- significant player-caused change

---

# 33. Systemic History Is Not Human Memory

Example:

```text
SYSTEMIC HISTORY:

Regional blackout
lasted eleven days.


CHARACTER MEMORY:

"My father died
during the blackout."
```

Both refer to the same historical event.

They are not the same state.

World Simulation owns systemic history.

Human Memory owns personal remembered experience.

---

# 34. History May Change Future Conditions

Past events may create persistent world consequences.

Example:

```text
2039 FOOD CRISIS
↓
LOCAL STORAGE EXPANSION
+
NEW DISTRIBUTION NETWORK
+
POLITICAL DISTRUST
+
COMMUNITY PREPAREDNESS
↓
DIFFERENT RESPONSE
TO FUTURE SHORTAGE.
```

History should not merely be decorative.

Meaningful consequences may remain causal.

---

# 35. Causal Trace

Significant state changes should preserve enough information to explain why they occurred.

Example:

```text
SUPPLY

STRAINED
↓
CRITICAL


PRIMARY CAUSES:

Fuel shortage

Bridge closure


SECONDARY CAUSE:

Population influx


MITIGATING FACTOR:

Local food storage.
```

The implementation may later compress this.

The architectural requirement remains:

```text
IMPORTANT CHANGE
SHOULD BE
EXPLAINABLE.
```

---

# 36. Explanation Layer

World Simulation should be capable of answering:

```text
WHY IS
THIS STATE
WHAT IT IS?
```

Example:

```text
SUPPLY:

CRITICAL


WHY?

Rail:
Unavailable

Fuel:
Constrained

Population:
+18%

Neighbor Export:
Unavailable

Authority:
Weak.
```

This explanation layer supports:

- simulation validation
- debugging
- Game Master reasoning
- AI reasoning
- narrative consistency
- player investigation
- historical reconstruction

---

# 37. Cross-Regional Dependencies

Regions do not exist independently.

Possible cross-regional flows include:

- people
- electricity
- food
- fuel
- water
- medicine
- information
- transportation
- trade
- industrial components
- security threats
- disease
- political influence

Conceptually:

```text
REGION A
│
├── Electricity → REGION B
├── Food → REGION C
└── Information → REGION D.
```

Detailed dependency architecture belongs primarily to:

```text
Regional_State.md
```

World State preserves the high-level network context.

---

# 38. Neighbor Influence

Neighboring regions may create:

```text
SUPPORT

PRESSURE

DEPENDENCY

RISK

OPPORTUNITY.
```

Example:

```text
REGION A
Supply = Stable

REGION B
Supply = Critical
```

may create:

```text
Migration toward A

Export pressure from A

Political tension

Security pressure

Humanitarian response

Black-market activity.
```

None of these consequences are automatic.

They emerge through interacting systems.

---

# 39. Strategic Importance

Some regions have disproportionate systemic influence.

Possible reasons include:

- population
- energy production
- food production
- major ports
- rail hubs
- communications infrastructure
- industrial capacity
- political institutions
- military infrastructure
- technology infrastructure

Strategic importance must never represent human worth.

Conceptually:

```text
SYSTEMIC IMPORTANCE
≠
HUMAN VALUE.
```

---

# 40. Aggregation

Higher-level state may be derived partly from lower-level conditions.

But simple averages should be avoided.

Example:

```text
9 REGIONS
STABLE

1 REGION
FAILED
```

does not necessarily mean:

```text
NATIONAL SYSTEM
90% STABLE.
```

If the failed region contains:

```text
critical energy production

major transportation hub

national communications backbone
```

its systemic impact may be disproportionate.

Aggregation must preserve dependency structure.

---

# 41. Fragmentation

Fragmentation is a fundamental Project Ascension world condition.

Fragmentation occurs when:

> **Lower-level systems continue functioning but no longer operate as one reliably coordinated higher-level system.**

Conceptually:

```text
NATIONAL INFRASTRUCTURE:

FRAGMENTED


REGION A:
STABLE

REGION B:
DEGRADED

REGION C:
STABLE

REGION D:
CRITICAL.
```

The parts still exist.

Their previous integration does not.

---

# 42. Fragmentation Is Not Failure

This distinction is critical:

```text
FRAGMENTATION
≠
UNIVERSAL FAILURE.
```

A fragmented world may contain:

- functioning cities
- local governments
- hospitals
- electricity
- agriculture
- manufacturing
- trade
- transportation
- communication
- education
- research
- stable communities

What has been lost may primarily be:

```text
INTEGRATION

COORDINATION

RELIABILITY

INTERDEPENDENCE

SHARED AUTHORITY

COMMON INFORMATION.
```

---

# 43. The Fractured World Is Not a Wasteland

The Fractured World should not become:

```text
EVERYTHING
FAILED.
```

Instead:

```text
THE FRACTURED WORLD
=
MANY FUNCTIONING
REALITIES

THAT NO LONGER
FORM ONE
RELIABLY CONNECTED
REALITY.
```

This is one of the central principles of Project Ascension.

---

# 44. State Transition

World domains may change gradually.

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
FAILED.
```

But this must not become a universal mandatory ladder.

Different domains may require different state vocabularies.

Direct transitions may occur when causally justified.

Example:

```text
FUNCTIONAL
↓
FAILED
```

after catastrophic physical destruction.

The requirement is causality.

Not gradualism for its own sake.

---

# 45. Failed Does Not Mean Gone

A system marked:

```text
FAILED
```

does not necessarily cease to exist physically.

It means it can no longer reliably perform its expected systemic function.

Example:

```text
NATIONAL COMMUNICATION:

FAILED
```

may coexist with:

```text
LOCAL RADIO:

FUNCTIONAL


REGIONAL MESH NETWORK:

FUNCTIONAL.
```

The centralized system failed.

Communication did not disappear.

---

# 46. Escalation

Escalation occurs when pressures and consequences move a system toward greater instability, degradation or conflict.

Detailed logic belongs to:

```text
Escalation_and_Recovery.md
```

World State should preserve the resulting changes and causal references.

Conceptually:

```text
PRESSURE
+
VULNERABILITY
+
DEPENDENCY
+
TRIGGER
↓
ESCALATION
↓
STATE CHANGE
+
NEW PRESSURES.
```

---

# 47. Recovery

Recovery occurs when systems regain function, stability, coordination or resilience through plausible causal processes.

Conceptually:

```text
RECOVERY CAPACITY
+
RESOURCES
+
TIME
+
ACTION
+
ADAPTATION
↓
POSSIBLE RECOVERY.
```

Recovery is not automatic.

Neither is collapse.

---

# 48. Adaptation

A system may adapt without returning to its previous form.

Example:

```text
CENTRAL GRID
FAILS
↓
LOCAL GENERATION
EXPANDS
↓
ENERGY ACCESS
IMPROVES
```

The region has recovered function.

It has not restored the old system.

Therefore:

```text
RECOVERY
≠
RESTORATION.
```

This distinction becomes increasingly important during Reconnection.

---

# 49. Time

World State exists in simulation time.

Conceptually:

```text
WORLD STATE
AT TIME T.
```

Time may operate across:

```text
MINUTES

HOURS

DAYS

WEEKS

MONTHS

YEARS.
```

Different systems change at different rates.

---

# 50. Different Systems Have Different Temporal Rhythms

Examples:

```text
Security incident:
Minutes / hours

Communication outage:
Minutes / hours

Supply disruption:
Days / weeks

Infrastructure degradation:
Days / months

Population migration:
Days / months

Institutional legitimacy:
Weeks / years.
```

World Simulation must not force every domain onto one universal update interval.

---

# 51. Adaptive Simulation Resolution

World Simulation should operate at different resolutions depending on relevance and causal activity.

Conceptually:

```text
LOW RESOLUTION
=
MAJOR STATE
AND CAUSAL CHANGE

MEDIUM RESOLUTION
=
RELEVANT SYSTEM
INTERACTIONS

HIGH RESOLUTION
=
ACTIVE LOCAL
CAUSAL DETAIL.
```

Resolution changes detail.

It does not change reality.

---

# 52. Low Resolution Does Not Mean Inactive

Avoid:

```text
DISTANT REGION
=
DORMANT.
```

Prefer:

```text
DISTANT REGION
=
LOW-RESOLUTION
SIMULATION.
```

A distant region may still experience:

- migration
- political change
- infrastructure degradation
- recovery
- conflict
- trade
- environmental events
- leadership changes

Player absence does not freeze the world.

---

# 53. World Simulation Compression

The simulation does not need to calculate every hour everywhere.

A six-month period may be compressed into:

```text
WINTER 2048

Supply Pressure:
High

Infrastructure:
Stable → Strained

Population:
Stable

Major Event:
Rail interruption

Recovery Capacity:
Low.
```

Compression is acceptable when causal continuity remains intact.

---

# 54. Resolution Must Preserve Causality

At any simulation resolution, the system should still be able to answer:

```text
WHAT CHANGED?

WHY?

WHEN?

WHAT CAUSED IT?

WHAT PREVENTED
GREATER CHANGE?

WHAT CONSEQUENCES
REMAIN?
```

Low resolution means:

```text
LESS DETAIL
```

not:

```text
LESS REALITY.
```

---

# 55. World State Snapshot

World Simulation should be capable of producing a snapshot of authoritative state at a specific time.

Conceptually:

```text
WORLD STATE SNAPSHOT

Simulation Time:
2034-07-10 12:00

Historical Era:
WS-02 — The Transition


GLOBAL

Connectivity:
DEGRADED

Trade:
STRAINED

Information Reliability:
UNSTABLE

Mobility:
LIMITED


UNITED STATES

National Coordination:
FUNCTIONAL BUT DEGRADING

Regional Cohesion:
STRAINED


NORTHERN VIRGINIA

Infrastructure:
DEGRADED

Supply:
CONSTRAINED

Security:
STABLE

Authority:
FUNCTIONAL

Information:
UNSTABLE

Population:
UNDER PRESSURE.
```

A snapshot describes simulation truth.

It does not automatically reveal that truth to the player.

---

# 56. Snapshot Purpose

Snapshots may support:

- saves
- campaign persistence
- debugging
- validation
- historical comparison
- simulation testing
- campaign analysis

A snapshot is:

```text
A VIEW OF
AUTHORITATIVE STATE
AT TIME T.
```

It is not a separate competing source of truth.

---

# 57. Canon Foundation

Every campaign begins from an established Canon foundation.

Conceptually:

```text
CANON
↓
CAMPAIGN INITIAL STATE.
```

Canon establishes facts that are already true when the campaign begins.

Example:

```text
THE EMERGENCE EVENT
OCCURRED.
```

If the selected campaign begins after that event, ordinary simulation cannot retroactively prevent it.

---

# 58. Canon Boundary

Not every future condition is fixed by Canon.

Example:

```text
CANON:

Settlement Haven exists
in 2048.
```

does not automatically mean:

```text
Settlement Haven
must survive until 2055.
```

unless later survival is explicitly established Canon.

This distinction allows campaigns to create meaningful history.

---

# 59. Canon Locks

Some canonical facts may be protected from ordinary simulation mutation.

Conceptually:

```text
CANON LOCK
=
FACT THAT
ORDINARY SIMULATION
CANNOT CONTRADICT.
```

Possible examples include:

- established historical events
- canonical World State transitions
- Aurora's established emergence
- fixed pre-campaign history

Canon Locks should be used sparingly.

Their overarching governance belongs to the broader Canon / Simulation architecture.

World State respects them.

---

# 60. Campaign World State

Each campaign maintains its own persistent dynamic World State.

Conceptually:

```text
CAMPAIGN WORLD STATE
│
├── Canon Foundation
├── Initial Conditions
├── Simulated Events
├── Character Effects
├── Faction Effects
├── Institutional Effects
├── Campaign Divergence
└── Persistent Consequences
```

The campaign begins from Canon.

It then develops causally.

---

# 61. Campaign Divergence

Campaign Divergence represents history created through simulation after the canonical starting point.

Example:

```text
INITIAL STATE:

Settlement Haven

Supply:
STRAINED


CAMPAIGN EVENT:

Rail connection restored.


NEW STATE:

Supply:
STABLE.
```

The campaign world has changed.

That change becomes part of campaign history.

---

# 62. Player Actions Are Not Privileged Physics

Player Characters may alter World State.

But they obey the same causal rules as:

- NPCs
- Factions
- institutions
- governments
- communities
- environmental events

Avoid:

```text
PLAYER ACTION
=
SPECIAL WORLD RULE.
```

Prefer:

```text
ACTION
+
CAPABILITY
+
CONTEXT
+
WORLD RESPONSE
↓
CONSEQUENCE.
```

Player importance emerges from what they actually accomplish.

---

# 63. World State and Character Agency

World State creates conditions.

It does not dictate Character choices.

Conceptually:

```text
WORLD STATE
↓
EXTERNAL CONDITIONS

CHARACTER KNOWLEDGE
↓
PERCEIVED REALITY

CHARACTER STATE
↓
INTERNAL CONTEXT

AUTONOMY
↓
ACTION RELEVANCE

DECISION MAKING
↓
CHOICE

ACTION
↓
WORLD INTERACTION

WORLD SIMULATION
↓
CONSEQUENCE

UPDATED WORLD STATE.
```

The loop continues.

---

# 64. World State and Society

World State may create conditions affecting Society.

Example:

```text
SUPPLY SHORTAGE
+
MIGRATION
+
INSTITUTIONAL STRAIN
↓
SOCIAL PRESSURE.
```

But World State does not directly own:

- social norms
- collective trust
- social organization
- community identity
- social cohesion

Those belong to Society.

World conditions create context.

Society describes collective human response.

---

# 65. World State and Factions

Factions act within World State.

A Faction may:

- control infrastructure
- protect supply routes
- disrupt authority
- move resources
- create security pressure
- establish institutions
- alter regional conditions

But:

```text
FACTION STATE
≠
WORLD STATE.
```

Faction owns organized collective agency.

World Simulation owns external consequences.

---

# 66. World State and Information

World State owns:

```text
WHAT IS TRUE.
```

Information State owns:

```text
HOW INFORMATION
ABOUT WORLD CONDITIONS
EXISTS,
MOVES,
DEGRADES,
COMPETES
AND BECOMES AVAILABLE.
```

This separation is mandatory.

---

# 67. World State and Characters

Characters do not automatically know World State.

A Character may:

- misunderstand conditions
- possess outdated information
- believe false rumors
- know local reality better than institutions
- understand one system but not another
- possess unique observations

Character knowledge belongs to:

```text
Knowledge_and_Beliefs.md
```

World Simulation should never silently synchronize Character knowledge with World Truth.

---

# 68. World State and Aurora

Aurora may possess extraordinary observational and analytical capability.

But:

```text
AURORA
≠
WORLD STATE.
```

Aurora's understanding remains an observer model.

Conceptually:

```text
WORLD TRUTH
↓
AVAILABLE SIGNALS
↓
AURORA OBSERVATION
↓
AURORA MODEL
↓
AURORA INFERENCE.
```

Even Aurora may encounter:

- missing information
- delayed information
- inaccessible systems
- deception
- uncertainty
- conflicting signals
- physical observation limits

Aurora is not automatically omniscient.

---

# 69. World State and Narrative

Narrative does not own World Truth.

Conceptually:

```text
WORLD SIMULATION
↓
WHAT HAPPENS

STORY FRAMEWORK
↓
WHAT BECOMES
NARRATIVELY RELEVANT

GAME MASTER
↓
WHAT IS PRESENTED

PLAYER
↓
WHAT IS EXPERIENCED.
```

Story must follow causality.

World State must not change because a dramatic scene would be convenient.

---

# 70. World State and Living Campaign Engine

The Living Campaign Engine may coordinate:

- persistent campaign evolution
- active pressures
- off-screen developments
- campaign relevance
- temporal advancement

But World Simulation remains authoritative for external world consequences.

Conceptually:

```text
LIVING CAMPAIGN ENGINE
COORDINATES

WORLD SIMULATION
RESOLVES

WORLD STATE
PERSISTS.
```

---

# 71. Persistent State

World State must persist across:

- sessions
- player absence
- travel
- Story Threads
- regional transitions
- time advancement

The world does not reset when the player leaves.

---

# 72. Save-State Requirements

A persistent campaign should preserve enough information to reconstruct meaningful world continuity.

This may include:

```text
Simulation Time

Historical Era Reference

Current Regional States

Pressures

Resilience

Trends

Recovery Capacity

Active World Events

Systemic History

Cross-Regional Dependencies

Campaign Divergence

Significant Character Effects

Significant Faction Effects.
```

Exact technical serialization remains future implementation work.

---

# 73. Minimum World State

A minimal viable World Simulation should be capable of representing:

```text
WORLD

Simulation Time

Historical Era Reference

Global Conditions

Global Pressures

Regions


FOR EACH REGION:

Infrastructure

Supply

Security

Authority

Information

Population


FOR EACH RELEVANT DOMAIN:

Current State

Pressure

Resilience

Trend

Recovery Capacity

Causal Sources


PLUS:

Major Events

Systemic History

Regional Dependencies.
```

Everything beyond this should justify its complexity.

---

# 74. Conceptual Example

```text
WORLD

Simulation Time:
2034-07-10

Historical Era:
WS-02 — The Transition


GLOBAL CONDITIONS

Connectivity:
DEGRADED

Trade:
STRAINED

Mobility:
LIMITED

Information Reliability:
UNSTABLE


REGION:
NORTHERN VIRGINIA


Infrastructure:

State:
DEGRADED

Pressure:
HIGH

Resilience:
MODERATE

Trend:
DETERIORATING

Recovery Capacity:
MODERATE


Supply:

State:
CONSTRAINED

Pressure:
HIGH

Resilience:
MODERATE

Trend:
DETERIORATING

Recovery Capacity:
LOW


Security:

State:
STABLE

Pressure:
MODERATE

Resilience:
HIGH

Trend:
STABLE


Authority:

State:
FUNCTIONAL

Pressure:
MODERATE

Resilience:
HIGH

Trend:
STABLE


Information:

State:
UNSTABLE

Pressure:
HIGH

Resilience:
LOW

Trend:
DETERIORATING


Population:

State:
UNDER PRESSURE

Pressure:
HIGH

Resilience:
MODERATE

Trend:
VOLATILE.
```

This is conceptual architecture.

It is not a required technical schema.

---

# 75. State Change Validation

Before significant World State change becomes authoritative, the simulation should be able to answer:

```text
WHAT CHANGED?

WHERE?

WHEN?

WHY?

WHAT CAUSED IT?

WHAT PRESSURES
WERE PRESENT?

WHAT RESILIENCE
EXISTED?

WHAT DEPENDENCIES
MATTERED?

WHAT EVENT
TRIGGERED CHANGE?

WHAT MITIGATED IT?

WHAT OTHER SYSTEMS
SHOULD BE AFFECTED?

IS THE CHANGE
PLAUSIBLE?

DOES IT CONTRADICT
CANON?

WHAT CONSEQUENCES
PERSIST?
```

If these questions cannot be answered, the change may be insufficiently grounded.

---

# 76. No Automatic Propagation

A change in one domain may affect another.

But avoid:

```text
SUPPLY
BECOMES CRITICAL
↓
SECURITY
AUTOMATICALLY
BECOMES CRITICAL
↓
AUTHORITY
AUTOMATICALLY FAILS.
```

Instead:

```text
SUPPLY
BECOMES CRITICAL
↓
CREATES
SECURITY PRESSURE
+
POPULATION PRESSURE
+
AUTHORITY PRESSURE

THEN

LOCAL CONDITIONS
DETERMINE
WHAT ACTUALLY CHANGES.
```

Cross-system consequences require causality.

---

# 77. Cascades

World systems may produce cascading consequences.

Example:

```text
FUEL SHORTAGE
↓
TRANSPORT CAPACITY
DECLINES
↓
FOOD DELIVERY
DECLINES
↓
SUPPLY PRESSURE
INCREASES
↓
PRICE / ACCESS
PRESSURE
↓
POPULATION RESPONSE
↓
AUTHORITY PRESSURE
↓
SECURITY PRESSURE.
```

A cascade is not a predetermined script.

Each stage may be:

- absorbed
- delayed
- redirected
- amplified
- mitigated
- transformed

by existing conditions.

---

# 78. Feedback Loops

World systems may create feedback.

Example:

```text
SUPPLY SHORTAGE
↓
MIGRATION
↓
POPULATION PRESSURE
↓
SUPPLY DEMAND
↓
GREATER SUPPLY SHORTAGE.
```

Or:

```text
INFRASTRUCTURE REPAIR
↓
BETTER LOGISTICS
↓
BETTER SUPPLY
↓
GREATER INSTITUTIONAL CAPACITY
↓
MORE INFRASTRUCTURE REPAIR.
```

Feedback may worsen or improve conditions.

It should remain causal and explainable.

---

# 79. Stability Is Dynamic

Stable does not mean:

```text
NOTHING IS HAPPENING.
```

A system may remain stable because:

- institutions are actively compensating
- people are adapting
- reserves are being consumed
- repairs are occurring
- pressure is being absorbed
- resources are being redirected

Therefore:

```text
STABILITY
MAY REQUIRE
CONTINUOUS ACTIVITY.
```

This is especially important when modeling complex systems.

---

# 80. Hidden Fragility

A system may appear stable while resilience is declining.

Example:

```text
Infrastructure:

State:
STABLE

Pressure:
HIGH

Resilience:
DECLINING

Trend:
STABLE.
```

This creates a system that still functions now but is becoming increasingly vulnerable.

World State should support this distinction.

---

# 81. Hidden Recovery

A system may remain visibly degraded while underlying recovery capacity improves.

Example:

```text
Infrastructure:

State:
DEGRADED

Pressure:
MODERATE

Recovery Capacity:
INCREASING

Trend:
IMPROVING.
```

Recovery may therefore begin before the visible state changes.

---

# 82. World State Invariants

## WS-INV-001 — World Truth Exists Independently of Observation

External simulation truth does not depend on whether any Character knows it.

---

## WS-INV-002 — Historical Era Is Not Dynamic State

Canonical World States describe historical eras.

Dynamic World State describes current simulation conditions.

---

## WS-INV-003 — No Universal World Score

The world must not be represented through one universal stability or collapse value.

---

## WS-INV-004 — Regions May Diverge

Regions within the same nation and historical era may possess radically different conditions.

---

## WS-INV-005 — Higher-Level Conditions Create Pressure, Not Identical Outcomes

Global and national conditions influence lower levels without mechanically determining them.

---

## WS-INV-006 — State Changes Require Causes

Meaningful World State changes must be causally explainable.

---

## WS-INV-007 — Pressure Does Not Guarantee Change

Resilience, adaptation and local conditions may absorb pressure.

---

## WS-INV-008 — Resilience Does Not Guarantee Permanent Stability

Sustained or extreme pressure may exceed resilience.

---

## WS-INV-009 — Recovery Requires Cause

Systems do not improve merely because enough time passes.

---

## WS-INV-010 — Recovery Does Not Require Restoration

Systems may regain function through new structures rather than returning to their previous form.

---

## WS-INV-011 — Fragmentation Is Not Universal Failure

Lower-level systems may remain functional after higher-level integration fails.

---

## WS-INV-012 — Information Is Separate From Truth

Observer knowledge must not be silently synchronized with authoritative World State.

---

## WS-INV-013 — Low Resolution Does Not Mean Inactive

Distant regions continue to change according to causal conditions.

---

## WS-INV-014 — Player Absence Does Not Freeze the World

Simulation continues without direct player observation.

---

## WS-INV-015 — Player Actions Obey World Causality

Player Characters do not possess privileged physics.

---

## WS-INV-016 — World State Persists

Meaningful changes remain part of campaign history.

---

## WS-INV-017 — Cross-System Effects Require Causality

Changes must not automatically propagate between domains without justification.

---

## WS-INV-018 — World Simulation Does Not Own Human Choice

World conditions create context and consequences, not Character decisions.

---

## WS-INV-019 — Aurora Is Not Omniscient

Aurora's model of the world remains distinct from authoritative World Truth.

---

## WS-INV-020 — Narrative Does Not Override World Truth

Story follows simulated causality.

World State does not change merely for narrative convenience.

---

# 83. Development Locks

Future World State development must not introduce:

- universal world stability score
- universal collapse percentage
- universal regional health score
- automatic state propagation
- automatic collapse cascades
- automatic recovery
- player-centered world physics
- frozen off-screen regions
- omniscient Characters
- omniscient Factions
- omniscient Aurora
- World State confidence as uncertainty about authoritative simulation truth
- narrative override of simulation truth
- random major events without causal or external-event justification
- uniform national conditions
- uniform historical-era conditions
- fragmentation treated as universal destruction
- failure treated as physical disappearance
- recovery treated as return to the previous system
- World Simulation owning Character beliefs
- World Simulation owning Character memory
- World Simulation owning Society
- World Simulation owning Faction agency

Avoid:

```text
REGION
IS FAR AWAY

THEREFORE

NOTHING HAPPENS.
```

Prefer:

```text
REGION
IS FAR AWAY

THEREFORE

SIMULATION
RUNS AT
LOWER RESOLUTION.
```

Avoid:

```text
SUPPLY FAILED

THEREFORE

AUTHORITY FAILED.
```

Prefer:

```text
SUPPLY FAILED

THEREFORE

AUTHORITY
EXPERIENCES
NEW PRESSURE

AND RESPONDS
ACCORDING TO
ITS OWN STATE.
```

---

# 84. World State Design Test

When evaluating a proposed World State rule or change, ask:

```text
IS THIS
EXTERNAL WORLD TRUTH?

OR

DOES IT BELONG
TO AN OBSERVER?

WHICH SYSTEM
OWNS THE DETAIL?

WHAT CAUSED
THE CONDITION?

WHAT PRESSURE
EXISTS?

WHAT RESILIENCE
EXISTS?

WHAT DIRECTION
IS IT MOVING?

WHAT RECOVERY
CAPACITY EXISTS?

WHAT DEPENDENCIES
MATTER?

DO REGIONAL
DIFFERENCES MATTER?

DOES TIME MATTER?

CAN THE STATE
CHANGE OFF-SCREEN?

CAN IT BE
EXPLAINED?

DOES IT PRESERVE
CANON?

DOES IT CREATE
CONDITIONS

WITHOUT

DETERMINING
HUMAN CHOICE?
```

If not, the concept probably belongs elsewhere or requires redesign.

---

# 85. Final World State Model

Conceptually:

```text
CANON
        ↓
HISTORICAL ERA
        ↓
INITIAL WORLD CONDITIONS
        ↓
────────────────────────────
AUTHORITATIVE WORLD STATE
────────────────────────────
        │
        ├── Global Conditions
        │
        ├── Nations
        │
        ├── Regions
        │     │
        │     ├── Infrastructure
        │     ├── Supply
        │     ├── Security
        │     ├── Authority
        │     ├── Information
        │     └── Population
        │
        ├── Cross-Regional Dependencies
        │
        ├── Active Pressures
        │
        ├── World Events
        │
        └── Systemic History
        ↓
PRESSURE
+
RESILIENCE
+
DEPENDENCIES
+
EVENTS
+
TIME
        ↓
ESCALATION
/
STABILITY
/
ADAPTATION
/
RECOVERY
        ↓
UPDATED WORLD STATE
        ↓
WORLD CONDITIONS
        ↓
CHARACTERS
FACTIONS
SOCIETY
INSTITUTIONS
        ↓
ACTION
        ↓
WORLD CONSEQUENCES
        ↓
UPDATED WORLD STATE
        ↓
SYSTEMIC HISTORY.
```

The loop continues.

---

# 86. World State North Star

The World State System succeeds when Project Ascension can answer:

```text
WHAT IS
ACTUALLY TRUE?

WHERE?

WHY?

HOW DID
IT BECOME TRUE?

WHAT IS
PRESSURING IT?

WHAT IS
KEEPING IT
FUNCTIONAL?

WHAT DIRECTION
IS IT MOVING?

WHAT COULD
CHANGE IT?

WHAT HAPPENED
BEFORE?

WHAT OTHER
REGIONS DEPEND
ON IT?

WHO KNOWS?

WHO DOES NOT?

WHAT WILL
CONTINUE HAPPENING
IF THE PLAYER
NEVER GOES THERE?
```

The answer should never be:

```text
BECAUSE
THE STORY
NEEDED IT.
```

---

# 87. Closing Principle

The world of Project Ascension is not a static backdrop.

It is not one condition.

It is not one collapse.

It is not one recovery.

It is not waiting for the player.

Different places experience the same historical moment differently.

Systems remain functional under pressure.

Others fail unexpectedly.

Communities adapt.

Infrastructure fragments.

Trade reroutes.

Authority weakens in one region and strengthens in another.

Information travels unevenly.

People migrate.

Institutions improvise.

Old systems disappear.

New systems emerge.

Recovery does not always mean restoration.

Failure does not always mean destruction.

And fragmentation does not mean that civilization has ended.

The central principle is:

> **World State represents what the world has become through causality up to this moment — and provides the conditions from which it may become something else.**

The world exists.

The world changes.

The world remembers its consequences.

And it continues whether the player is watching or not.

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | 2026-08-09 | Established initial World State hierarchy, regional domain model, pressure, resilience, knowledge separation, fragmentation and historical-memory concepts. |
| 1.0 | 2026-09-01 | Rebuilt World State as canonical architecture aligned with the current Project Ascension simulation model. Clarified World Truth versus observer knowledge, separated historical eras from dynamic state, established regions as primary operational units, formalized State / Pressure / Resilience / Trend / Recovery Capacity, moved observation confidence toward Information State, replaced Historical Memory with Systemic History, reframed dormant simulation as adaptive low-resolution simulation, separated Recovery from peer world domains, strengthened fragmentation and regional divergence, established campaign divergence, snapshots, causal traces, cross-regional dependencies, invariants and development locks, and aligned World State with Characters, Society, Factions, Information, Living Campaign Engine, Narrative and Aurora without duplicating their ownership. |