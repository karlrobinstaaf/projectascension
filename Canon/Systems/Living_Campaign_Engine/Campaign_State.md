# PROJECT ASCENSION
# Campaign State System

| Field | Value |
|--------|-------|
| System | Living Campaign Engine |
| Document | Campaign State |
| Location | Canon/Systems/Living_Campaign_Engine/Campaign_State.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Player-Relevant Campaign Context and Dynamic Campaign State |
| Last Updated | 2026-08-09 |

> *"The world may be shared. The campaign is personal."*

---

# Purpose

The Campaign State system defines the dynamic state of a specific Project Ascension campaign.

It represents the information the Living Campaign Engine requires to determine:

- what matters to the player
- what the player currently knows
- where the player is
- who the player cares about
- which factions matter
- what goals are active
- which obligations remain unresolved
- which opportunities are visible
- what consequences are still unfolding
- how much active campaign pressure already exists

Campaign State is the primary reference point used when World Simulation events are evaluated for player relevance.

---

# Core Distinction

World State and Campaign State are not the same thing.

```text
WORLD STATE

What is actually happening in the world?
```

versus:

```text
CAMPAIGN STATE

What is currently meaningful,
known,
available,
or unresolved
for this player?
```

The Living Campaign Engine must preserve this distinction.

---

# Example

World Simulation may contain:

```text
REGION A

Fuel:
CRITICAL

Migration:
OUTBOUND

Authority:
FUNCTIONAL

Security:
STRAINED
```

Campaign State may contain:

```text
Player Location:
REGION B

Player Knowledge:
No confirmed information about Region A

Relationships:
Sibling lives in Region A

Active Goal:
Reach sibling

Result:
Region A has very high campaign relevance.
```

The world event becomes important because of the player's relationship to it.

---

# Campaign State Structure

Conceptually:

```text
CAMPAIGN STATE
│
├── Campaign Identity
├── Current Time
├── Player Position
├── Player Condition
├── Player Knowledge
├── Player Goals
├── Player Resources
├── Player Roles
├── Relationships
├── Faction Relationships
├── Reputation
├── Obligations
├── Active Story Situations
├── Active Hooks
├── Active Missions
├── Recent Events
├── Unresolved Consequences
├── Campaign Pressure
├── Campaign Memory
└── World References
```

---

# Campaign Identity

Every campaign should have a stable identity.

Conceptually:

```text
Campaign ID
Campaign Name
Start Date
Historical Era
Starting Region
Current Date
```

Example:

```text
Campaign ID:
CMP-001

Campaign Name:
Valley Reconnection

Historical Era:
WS-04 — The Reconnection

Starting Region:
Shenandoah Valley
```

---

# Campaign ID

A Campaign ID uniquely identifies the campaign state.

Example:

```text
CMP-0001
```

Exact naming conventions may be standardized later.

---

# Campaign Name

Campaign Name is human-readable.

It may be:

- player-defined
- Game Master-defined
- system-generated

It should not influence simulation directly.

---

# Historical Era

Campaign State should reference the active canonical historical era.

Example:

```text
Historical Era:
WS-03 — The Fractured World
```

This constrains:

- available technology
- world assumptions
- institutional structures
- baseline information horizon
- expected infrastructure conditions

---

# Current Time

Campaign State must maintain current simulation time.

Conceptually:

```text
Date
Time
Elapsed Campaign Time
Time Since Last Major Event
```

Time matters because:

- world events continue
- opportunity windows expire
- relationships change
- consequences mature
- supplies are consumed
- characters act independently

---

# Player Position

Player Position describes where the player currently exists in the world.

Conceptually:

```text
PLAYER POSITION
│
├── Region
├── Local Area
├── Settlement
├── Current Location
├── Travel State
└── Accessibility
```

---

# Region

Example:

```text
Region:
Shenandoah Valley
```

Regional location strongly affects World Event relevance.

---

# Local Area

Example:

```text
Local Area:
Northern Valley Corridor
```

This allows more granular proximity checks.

---

# Settlement

Example:

```text
Settlement:
Winchester
```

---

# Current Location

Current Location may represent:

```text
Hospital
Farm
Road
Shelter
Workshop
Settlement Center
Wilderness
```

This may affect immediate event exposure.

---

# Travel State

Conceptually:

```text
STATIONARY
TRAVELING
STRANDED
DELAYED
ESCORTING
EXPLORING
```

Travel creates its own campaign context.

---

# Accessibility

Accessibility describes how easily the player can currently reach other areas.

It depends upon:

- transport
- fuel
- route security
- authority restrictions
- weather
- infrastructure

Conceptually:

```text
HIGH
FUNCTIONAL
LIMITED
RESTRICTED
ISOLATED
```

---

# Player Condition

Campaign State may maintain broad player-operational context.

This should not replace detailed Character systems.

Possible values include:

```text
Available
Busy
Injured
Exhausted
Restricted
Traveling
```

The purpose is to help the Living Campaign Engine avoid generating implausible requests.

---

# Campaign Availability

If the player is:

```text
Injured
+
isolated
+
already inside an active crisis
```

the engine should not generate five new urgent missions simply because World Simulation produced them.

Campaign context matters.

---

# Player Knowledge

Player Knowledge represents what the player currently believes or knows about the world.

It should integrate with:

```text
Canon/Systems/World_Simulation/Information_State.md
```

Player Knowledge must remain separate from internal World State truth.

---

# Knowledge Entry

Conceptually:

```text
PLAYER KNOWLEDGE ENTRY

Subject
Known State
Source
Information Age
Reliability
Verification
Player Confidence
Last Updated
```

---

# Example

```text
Subject:
Fuel Supply — Northern Valley

Known State:
Constrained

Source:
Regional radio

Information Age:
6 hours

Reliability:
High

Verification:
Corroborated

Player Confidence:
High
```

---

# Unknown Knowledge

The system must allow:

```text
UNKNOWN
```

Example:

```text
Security State — Region C:
UNKNOWN
```

Lack of knowledge is meaningful.

---

# Incorrect Player Knowledge

Player Knowledge may be wrong.

Example:

```text
Player Belief:
Bridge is open.

Actual World State:
Bridge closed.
```

The engine must not silently correct player knowledge.

Discovery should occur through plausible information.

---

# Knowledge Relevance

Events connected to player knowledge may be more likely to surface.

Example:

```text
Player has been investigating fuel shortages.
```

A new fuel-related World Event may gain relevance.

---

# Player Goals

Player Goals represent objectives the player has chosen or adopted.

Goals are not the same as missions.

Examples:

```text
Find missing sister.

Build trade route.

Gain access to regional council.

Restore workshop.

Learn what happened to Aurora.
```

---

# Goal Types

Possible types include:

```text
PERSONAL
RELATIONSHIP
SURVIVAL
ECONOMIC
EXPLORATION
POLITICAL
TECHNOLOGICAL
SOCIAL
INVESTIGATIVE
```

---

# Goal Priority

Goals may be:

```text
PRIMARY
ACTIVE
SECONDARY
DORMANT
COMPLETED
ABANDONED
```

---

# Goal Relevance

World Events affecting active goals should receive additional relevance.

Example:

```text
Player Goal:
Reach Region B.

World Event:
Primary road becomes insecure.
```

Relevance becomes high.

---

# Player Resources

Campaign State should store player-relevant resources at an abstract level.

Detailed inventory belongs elsewhere if a separate system exists.

Possible resource categories:

```text
Money / Trade Value
Food
Water
Fuel
Medicine
Transport
Equipment
Information
Contacts
Shelter
```

---

# Resource Relevance

A World Event may become campaign-relevant when it affects resources the player depends upon.

Example:

```text
Fuel shortage
```

has low relevance for a player traveling on foot.

It may have extreme relevance for a transport operator.

---

# Resource Capability

Campaign State may include broad capability tags.

Examples:

```text
Has Vehicle
Has Radio
Has Medical Access
Has Workshop
Has Secure Shelter
Has Trade Goods
```

These affect available solutions.

---

# Player Roles

Player Roles describe identities that emerge from campaign behavior.

Examples:

```text
Trader
Technician
Mediator
Scout
Protector
Investigator
Leader
Courier
```

Roles should normally emerge rather than be rigidly assigned.

---

# Role Strength

Conceptually:

```text
EMERGING
ESTABLISHED
RECOGNIZED
PROMINENT
```

---

# Role Emergence

Example:

```text
Player repeatedly repairs infrastructure.
      ↓
Technician role emerges.
      ↓
Infrastructure actors increasingly contact player.
```

The campaign adapts to behavior.

---

# Role Decay

Roles may weaken if the player stops acting in that capacity for long periods.

Example:

```text
Recognized Trader
```

may decline if the player leaves trade networks behind.

---

# Relationships

Campaign State should reference important character relationships.

Detailed relationship mechanics belong in:

```text
Canon/Systems/Relationships/
```

Campaign State only stores or references information required for relevance.

---

# Relationship Entry

Conceptually:

```text
CHARACTER
Relationship Strength
Relationship Type
Current Status
Last Meaningful Interaction
Active Need
Current Location
Contact Availability
```

---

# Relationship Types

Examples:

```text
Family
Friend
Partner
Professional
Ally
Rival
Dependent
Mentor
```

Exact relationship structure belongs elsewhere.

---

# Relationship Relevance

A World Event affecting a high-value relationship should receive strong relevance.

Example:

```text
EVENT:
Hospital loses power.

CHARACTER:
Player's partner works there.
```

Campaign significance increases dramatically.

---

# Contactability

A character may matter to the player but remain unreachable.

Conceptually:

```text
CONTACTABLE
LIMITED
UNREACHABLE
UNKNOWN
```

This affects how Story Hooks can be delivered.

---

# Faction Relationships

Campaign State should reference relationships with known factions.

Examples:

```text
Regional Authority
Trade Network
Settlement Council
Military Unit
Local Faction
Corporate Remnant
```

---

# Faction Relationship Entry

Conceptually:

```text
Faction
Reputation
Trust
Access
Obligations
Hostility
Last Interaction
```

---

# Faction Reputation

Conceptual values might include:

```text
HOSTILE
DISTRUSTED
NEUTRAL
TRUSTED
RESPECTED
ALLIED
```

Exact reputation mechanics may be defined elsewhere.

---

# Faction Access

Access represents what the player is permitted to reach.

Examples:

```text
Public
Restricted
Operational
Leadership
```

Access may affect which hooks become available.

---

# Reputation

Reputation represents how the wider world understands the player's past behavior.

Reputation should be contextual.

Avoid:

```text
GLOBAL REPUTATION = 73
```

Prefer:

```text
Regional Traders:
Reliable

Regional Authority:
Useful but independent

Settlement A:
Trusted

Settlement B:
Unknown
```

---

# Reputation Domains

Possible domains:

```text
Reliability
Honesty
Competence
Violence
Generosity
Political Alignment
Technical Skill
Trade Fairness
```

---

# Reputation Relevance

Reputation may influence:

- who asks for help
- who shares information
- who offers trade
- who distrusts the player
- which roles emerge

---

# Obligations

Obligations represent commitments that may create future relevance.

Examples:

```text
Promise to return medicine.

Debt owed to trader.

Agreement to contact family.

Commitment to regional council.

Favor owed to character.
```

---

# Obligation State

Conceptually:

```text
OPEN
DUE
OVERDUE
FULFILLED
BROKEN
FORGIVEN
```

---

# Obligation Pressure

Open obligations may increase relevance of related events.

Example:

```text
Player promised to help Settlement A.
```

A crisis affecting Settlement A should carry additional campaign weight.

---

# Broken Obligations

Breaking an obligation may affect:

- relationships
- reputation
- faction trust
- future access

Consequences should persist.

---

# Story Situations

Campaign State should track active Story Situations.

A Story Situation is broader than a mission.

Example:

```text
Regional fuel shortage
+
Hospital demand
+
Farm demand
+
Authority rationing
+
Trader stockpile
```

The player may interact with several parts of the situation.

---

# Story Situation Entry

Conceptually:

```text
STORY SITUATION

ID
Source World Event / Event Cluster
Location
Actors
Player Relevance
Urgency
Current State
Known Information
Possible Interaction
Expiration
```

---

# Situation State

Possible values:

```text
BACKGROUND
EMERGING
ACTIVE
ESCALATING
STABILIZING
RESOLVED
TRANSFORMED
EXPIRED
```

---

# Active Hooks

Hooks are visible campaign signals.

Examples:

```text
Rumor
Radio report
Character message
Environmental clue
Official notice
```

---

# Hook Entry

Conceptually:

```text
HOOK

ID
Source Situation
Presentation Type
Source
Player Relevance
Reliability
Urgency
Status
Expiration
```

---

# Hook State

Possible values:

```text
UNSEEN
VISIBLE
ACKNOWLEDGED
INVESTIGATED
IGNORED
EXPIRED
```

---

# Ignored Hooks

Ignored does not mean removed from the world.

The underlying Story Situation continues according to World Simulation.

---

# Active Missions

Campaign State should track missions created from Story Situations.

Mission data belongs primarily in:

```text
Mission_Generation.md
```

Campaign State needs only enough information to manage active content.

---

# Mission Entry

Conceptually:

```text
MISSION

ID
Origin Situation
Objective
Location
Actors
Urgency
Opportunity Window
Current State
Player Commitment
```

---

# Mission States

Possible values:

```text
AVAILABLE
ACCEPTED
ACTIVE
PAUSED
COMPLETED
PARTIAL
FAILED
ABANDONED
RESOLVED ELSEWHERE
EXPIRED
```

---

# Accepted Mission Does Not Freeze World

Even after acceptance:

```text
WORLD SIMULATION CONTINUES
```

Example:

A mission to deliver medicine may change if the hospital receives another shipment first.

---

# Recent Events

Campaign State should maintain recent player-relevant events.

Examples:

```text
Recent Mission
Character Death
Settlement Visit
Major Discovery
Faction Conflict
Infrastructure Failure
```

Recent events help determine:

- narrative continuity
- conversation context
- relevance
- pacing

---

# Recent Event Window

Not every event remains "recent" forever.

Conceptually:

```text
Immediate:
Hours / Days

Recent:
Days / Weeks

Historical:
Months / Years
```

Historical events may move into Campaign Memory.

---

# Unresolved Consequences

Some player actions create delayed effects.

Campaign State must track them.

Example:

```text
Player rerouted fuel from Settlement A to Hospital B.
```

Immediate:

```text
Hospital stabilizes.
```

Delayed:

```text
Settlement A agricultural output may fall.
```

This unresolved consequence remains active until World Simulation resolves it.

---

# Consequence Entry

Conceptually:

```text
CONSEQUENCE

Origin Action
Affected System
Affected Location
Expected Delay
Current Status
Visibility
Potential Severity
```

---

# Consequence Visibility

Possible values:

```text
KNOWN
PARTIALLY KNOWN
HIDDEN
```

The player does not need to know all consequences in advance.

---

# Campaign Pressure

Campaign Pressure represents the amount of unresolved player-facing demand currently active.

It is not World Pressure.

Possible dimensions include:

```text
Urgent Situations
Active Missions
Character Needs
Faction Demands
Personal Goals
Unresolved Consequences
```

---

# Campaign Pressure State

Conceptually:

```text
LOW
NORMAL
HIGH
OVERLOADED
```

---

# Low

The player has little immediate demand.

Appropriate for:

- exploration
- relationships
- building
- quiet content

---

# Normal

Several meaningful options exist.

The player can choose priorities without feeling overwhelmed.

---

# High

Multiple urgent situations compete for attention.

This may be appropriate during active crisis.

---

# Overloaded

The player cannot realistically respond to all available demands.

This may be intentional during major systemic emergencies.

It should not become the default campaign state.

---

# Campaign Bandwidth

Campaign Bandwidth represents how much additional player-facing content should be surfaced.

Conceptually:

```text
AVAILABLE
LIMITED
SATURATED
```

This helps Pacing systems decide whether new World Events should remain background.

---

# Saturation Example

World Simulation produces:

```text
5 relevant events.
```

Campaign State already contains:

```text
2 urgent missions
1 relationship crisis
1 active political situation
```

Pacing may surface only one new event directly.

The others remain:

- ambient
- delayed
- unresolved in background

---

# Campaign Memory

Campaign State should reference long-term Campaign Memory.

Detailed mechanics belong in:

```text
Campaign_Memory.md
```

Memory includes significant:

- player choices
- relationships
- promises
- victories
- failures
- discoveries
- faction interactions
- historical participation

---

# Memory Versus Recent Events

```text
RECENT EVENTS
Short-term context.

CAMPAIGN MEMORY
Long-term campaign history.
```

Not every recent event should become permanent memory.

---

# World References

Campaign State should maintain references to relevant World Simulation objects.

Examples:

```text
Current Region
Neighboring Regions
Known Regions
Known World Events
Relevant Event Clusters
Known Infrastructure
Known Factions
```

This prevents duplication of World State data.

---

# Reference Principle

Campaign State should not copy full World Simulation state where a reference is sufficient.

Avoid:

```text
Campaign State contains complete Northern Virginia Infrastructure model.
```

Prefer:

```text
Campaign State references Northern Virginia World State
+
stores player knowledge about it.
```

---

# Actual Versus Campaign State

Example:

```text
WORLD STATE

Fuel:
CRITICAL
```

Campaign State:

```text
Player Knowledge:
Fuel = STRAINED

Player Confidence:
Moderate

Relevant Situation:
Fuel queues increasing
```

The mismatch is intentional.

---

# Campaign-State Update Cycle

A conceptual update cycle:

```text
1. Advance campaign time.
2. Update player position.
3. Update player condition.
4. Read relevant World Simulation changes.
5. Update player knowledge.
6. Update relationships.
7. Update faction relationships.
8. Update active goals.
9. Process obligations.
10. Update Story Situations.
11. Update Hooks.
12. Update Missions.
13. Process unresolved consequences.
14. Update Campaign Pressure.
15. Update Campaign Bandwidth.
16. Promote important recent events to memory.
17. Remove expired short-term state.
```

---

# Campaign State and Daily Update Cycle

The legacy `Overview.md` contains an earlier Daily Update Cycle:

```text
1. Advance time
2. Update weather and environment
3. Resolve infrastructure changes
4. Advance faction plans
5. Advance NPC plans
6. Update Aurora knowledge
7. Resolve resources
8. Trigger world events
9. Update delayed consequences
10. Write to the World Ledger
```

This concept remains useful.

However, responsibility should now be distributed between systems.

Conceptually:

```text
WORLD SIMULATION

Advance environment
Infrastructure
Resources
World actors
World events

        ↓

LIVING CAMPAIGN ENGINE

Update relevance
Hooks
Situations
Consequences
Campaign Memory
```

The legacy cycle should therefore not be copied directly into Campaign State.

Its useful concepts should be migrated into the current architecture.

---

# Player Action Intake

Campaign State must receive meaningful player actions.

Examples:

```text
Travel
Trade
Conversation
Mission Action
Resource Allocation
Relationship Decision
Political Decision
Combat
Repair
Exploration
```

Actions may update:

- position
- goals
- reputation
- relationships
- obligations
- active situations
- World Simulation

---

# Player Intent

Where possible, the engine should distinguish:

```text
ACTION
```

from:

```text
INTENT
```

Example:

```text
Action:
Give fuel to settlement.

Intent:
Help community.
```

The world responds primarily to the action.

Characters may interpret intent differently.

---

# Player Choice History

Important choices should preserve context.

Example:

```text
Decision:
Give medicine to remote clinic.

Alternative:
Hospital.

Reason Known:
Clinic had no alternative supply.
```

This context may matter later.

---

# Campaign State Snapshot

A snapshot may look like:

```text
CAMPAIGN STATE

Campaign:
CMP-001 — Valley Reconnection

Date:
2045-05-14

Historical Era:
WS-04 — The Reconnection


PLAYER

Region:
Shenandoah Valley

Settlement:
Winchester

Travel State:
Stationary

Accessibility:
Functional


KNOWLEDGE

Northern Trade Route:
Open
Confidence: High

Eastern Region Security:
Unstable
Confidence: Low

National Authority Expansion:
Reported
Verification: Partial


GOALS

Primary:
Establish northern trade agreement

Active:
Find replacement turbine controller

Secondary:
Learn fate of former Asterion facility


ROLES

Trader:
Established

Mediator:
Emerging


RELATIONSHIPS

Mara Vale:
Close / Trusted

Valley Council:
Trusted

Northern Traders:
Respected


OBLIGATIONS

Deliver medical parts:
Due in 5 days

Return radio equipment:
Open


ACTIVE STORY SITUATIONS

1. Northern Trade Negotiation
   State: Active
   Relevance: High

2. Fuel Supply Pressure
   State: Emerging
   Relevance: Moderate


HOOKS

Radio report:
New road restrictions north.

Status:
Visible


MISSIONS

Medical Parts Delivery:
Accepted

Opportunity Window:
5 days


UNRESOLVED CONSEQUENCES

Fuel redirected from agriculture:
Potential harvest impact in 3 weeks.


CAMPAIGN PRESSURE

State:
NORMAL

Campaign Bandwidth:
AVAILABLE
```

---

# Minimum Campaign State

A minimum viable Campaign State should contain:

```text
Campaign ID
Historical Era
Current Time

Player Region
Player Local Position
Player Knowledge

Active Goals
Player Resources
Player Roles

Key Relationships
Faction Relationships
Reputation
Obligations

Active Story Situations
Active Hooks
Active Missions

Recent Events
Unresolved Consequences

Campaign Pressure
Campaign Bandwidth
Campaign Memory References
```

Everything beyond this should justify its complexity.

---

# Campaign State Consistency Rules

## Rule 1

Campaign State and World State are separate.

---

## Rule 2

Campaign State should reference World State rather than duplicate it unnecessarily.

---

## Rule 3

Player Knowledge must remain separate from World truth.

---

## Rule 4

The player may hold incorrect information.

---

## Rule 5

Unknown is a valid Player Knowledge state.

---

## Rule 6

Player goals and missions are separate.

---

## Rule 7

Relationships should influence relevance.

---

## Rule 8

Reputation should be contextual rather than universally global.

---

## Rule 9

Obligations should persist until resolved.

---

## Rule 10

Accepted missions do not freeze World Simulation.

---

## Rule 11

Ignored hooks continue evolving through their underlying world situations.

---

## Rule 12

Consequences may be delayed or hidden.

---

## Rule 13

Campaign Pressure and World Pressure are separate.

---

## Rule 14

The engine should consider Campaign Bandwidth before surfacing additional content.

---

## Rule 15

Quiet campaign states are valid.

---

## Rule 16

Roles should primarily emerge from player behavior.

---

## Rule 17

Player actions should update both campaign context and relevant world systems.

---

## Rule 18

Only meaningful events should become long-term Campaign Memory.

---

## Rule 19

Campaign State must remain explainable.

---

## Rule 20

The campaign should never require the player to matter to every world event.

---

# Guiding Questions

At any moment, Campaign State should allow the engine to answer:

**Where is the player?**

**What does the player know?**

**What does the player believe?**

**What does the player currently want?**

**Who matters to the player?**

**Who knows or trusts the player?**

**What resources does the player depend upon?**

**What obligations remain open?**

**Which world situations currently matter?**

**Which hooks are visible?**

**What has the player already committed to?**

**Which consequences are still developing?**

**How much campaign pressure already exists?**

**What should not be surfaced right now?**

These answers provide the context required for meaningful campaign generation.

---

# Core Design Principle

The Living Campaign Engine should never ask only:

```text
WHAT WORLD EVENT HAPPENED?
```

It should ask:

```text
WHAT WORLD EVENT HAPPENED?

        +

WHO IS THIS PLAYER?

        +

WHAT DO THEY CARE ABOUT?

        +

WHAT DO THEY KNOW?

        +

WHAT ARE THEY ALREADY DEALING WITH?
```

Only then should it decide what becomes campaign content.

---

# Current Status

```text
LIVING CAMPAIGN ENGINE

README.md
FOUNDATION DEFINED

Campaign_State.md
FOUNDATION DEFINED

World_Event_Intake.md
PENDING

Relevance_and_Proximity.md
PENDING

Story_Hooks.md
PENDING

Mission_Generation.md
PENDING

Character_Integration.md
PENDING

Consequence_Propagation.md
PENDING

Opportunity_and_Conflict.md
PENDING

Pacing_and_Priority.md
PENDING

Campaign_Memory.md
PENDING
```

---

# Next Document

The next recommended document is:

```text
Canon/Systems/Living_Campaign_Engine/World_Event_Intake.md
```

Campaign State now establishes:

```text
WHO THE PLAYER IS
IN THE CURRENT CAMPAIGN.
```

World Event Intake must establish:

```text
HOW THE ENORMOUS NUMBER OF CHANGES
IN WORLD SIMULATION ENTER THE
LIVING CAMPAIGN ENGINE.
```

It should define:

- event candidates
- state-change detection
- event normalization
- event clustering
- duplicate suppression
- causal relationships
- event lifecycle
- event significance
- background events
- event transformation
- event resolution

The challenge is important:

```text
WORLD SIMULATION
may generate thousands of changes.

LIVING CAMPAIGN ENGINE
must identify the handful worth examining.
```

`World_Event_Intake.md` becomes the first filter.

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial Campaign State framework established for player position, knowledge, goals, resources, roles, relationships, reputation, obligations, story situations, hooks, missions, consequences, pressure and campaign bandwidth. |