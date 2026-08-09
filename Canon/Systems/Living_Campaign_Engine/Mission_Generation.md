# PROJECT ASCENSION
# Mission Generation System

| Field | Value |
|--------|-------|
| System | Living Campaign Engine |
| Document | Mission Generation |
| Location | Canon/Systems/Living_Campaign_Engine/Mission_Generation.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Dynamic Objectives, Player Intervention and Mission Resolution |
| Last Updated | 2026-08-09 |

> *"A mission should exist because the world created something worth doing — not because the game needs another objective marker."*

---

# Purpose

The Mission Generation system defines when and how situations inside the Living Campaign Engine become structured opportunities for player intervention.

Mission Generation receives context from:

```text
World Simulation
World Event Intake
Relevance and Proximity
Story Hooks
Campaign State
Characters
Factions
```

and determines whether:

```text
PLAYER ACTION
```

can meaningfully influence an existing situation.

The system must support:

- NPC-requested missions
- faction requests
- authority requests
- player-created objectives
- emergency objectives
- investigation missions
- trade missions
- repair missions
- exploration missions
- negotiation missions
- protection missions
- recovery missions
- opportunity missions
- multi-stage situations
- partial success
- changing objectives
- mission expiration
- world-resolved missions
- missionless intervention

The purpose is not to maximize mission quantity.

The purpose is to create meaningful opportunities for agency.

---

# Core Principle

The first Mission Generation question is:

```text
IS A MISSION NECESSARY?
```

Not:

```text
WHAT MISSION SHOULD WE GENERATE?
```

A relevant Story Situation may be fully successful campaign content without ever becoming a formal Mission.

---

# Mission Eligibility

A situation becomes eligible for Mission Generation when:

```text
MEANINGFUL SITUATION EXISTS

        +

PLAYER INTERVENTION IS PLAUSIBLE

        +

PLAYER ACTION COULD ALTER AN OUTCOME

        +

ACTION CAN BE EXPRESSED
AS A COHERENT OBJECTIVE
```

If these conditions do not exist:

```text
NO MISSION
```

---

# Mission Is One Form of Player Action

The Living Campaign Engine should treat a Mission as:

```text
STRUCTURED PLAYER INTERVENTION
```

not:

```text
THE ONLY WAY PLAYER ACTION OCCURS
```

The player may act through:

- spontaneous investigation
- conversation
- trade
- exploration
- resource allocation
- political influence
- direct repair
- travel
- observation

without ever accepting a formal Mission.

---

# Missionless Intervention

Example:

```text
Story Hook:

Fuel queues increasing.
```

The player decides:

```text
Travel to the regional depot.
```

They discover:

```text
Distribution problem.
```

They negotiate directly with a transport operator.

World Simulation updates.

No Mission was generated.

This is a valid and desirable campaign outcome.

---

# Player-Created Objectives

Players must be able to create their own objectives.

Examples:

```text
"I want to find out why the radio stopped."

"I want to reach my sister."

"I want to reopen the eastern road."

"I want to find a buyer for our grain."

"I want to investigate that facility."
```

These objectives may become structured Campaign Goals or Missions after player intent is clear.

---

# Player-Created Mission Principle

The engine should support:

```text
PLAYER CURIOSITY
      ↓
PLAYER INTENT
      ↓
OBJECTIVE
      ↓
WORLD RESPONSE
```

rather than requiring:

```text
QUEST GIVER
```

---

# Mission Sources

Missions may originate from:

```text
PLAYER
CHARACTER
FACTION
AUTHORITY
COMMUNITY
WORLD EMERGENCY
WORLD OPPORTUNITY
RELATIONSHIP
CONSEQUENCE
```

---

# Player-Origin Mission

The player defines the desired outcome.

Example:

```text
Player:
"I want to locate the missing convoy."
```

The system may formalize:

```text
Objective:
Determine what happened to the convoy.
```

No NPC needs to request it.

---

# Character-Origin Mission

A character has a real need.

Example:

```text
Doctor:
Needs medical supplies.
```

The request emerges from:

```text
Supply State
+
Character Profession
+
Relationship
```

rather than arbitrary quest generation.

---

# Faction-Origin Mission

A faction may request action connected to its:

- goals
- problems
- resources
- conflicts
- relationships

Example:

```text
Trade Coalition:
Needs route inspection.
```

---

# Authority-Origin Mission

Authorities may request:

- emergency assistance
- transport
- investigation
- repair
- negotiation
- resource delivery

Requests should reflect actual Authority State and available resources.

---

# Community-Origin Mission

Communities may collectively create needs.

Examples:

```text
Repair water system.

Establish radio connection.

Prepare winter shelter.

Find missing residents.
```

---

# World-Emergency Mission

Some missions arise directly from immediate conditions.

Example:

```text
Flood threatens settlement.
```

Possible objective:

```text
Evacuate isolated residents.
```

There may be no traditional quest giver.

---

# Opportunity Mission

Not all missions solve problems.

Examples:

```text
Explore newly accessible facility.

Establish trade with new settlement.

Survey possible rail restoration.

Investigate unknown radio signal.

Recover abandoned equipment.
```

---

# Consequence Mission

Earlier actions may create later objectives.

Example:

```text
Player repaired regional radio.
```

Later:

```text
New distant transmission detected.
```

Possible objective:

```text
Establish contact with transmitting settlement.
```

The new mission emerges from earlier campaign history.

---

# Mission Generation Pipeline

Conceptually:

```text
STORY SITUATION
      │
      ▼
PLAYER RELEVANCE
      │
      ▼
ACTIONABILITY CHECK
      │
      ▼
MISSION NECESSITY CHECK
      │
      ├──── NO ────► Remain Story Situation
      │
      └──── YES
             │
             ▼
       MISSION ORIGIN
             │
             ▼
       OBJECTIVE MODEL
             │
             ▼
       WORLD CONSTRAINTS
             │
             ▼
       POSSIBLE APPROACHES
             │
             ▼
       CONSEQUENCE PATHS
             │
             ▼
          MISSION
```

---

# Actionability

Actionability answers:

```text
CAN THE PLAYER PLAUSIBLY
INFLUENCE THIS SITUATION?
```

Conceptual values:

```text
NONE
INDIRECT
LIMITED
MEANINGFUL
HIGH
```

---

# No Actionability

Example:

```text
Distant earthquake already occurred.

No relationships affected.

Player has no ability to influence recovery.
```

The event may remain:

```text
News
Background
World consequence
```

No Mission is required.

---

# Indirect Actionability

Example:

```text
Foreign region has medicine shortage.
```

Player cannot solve the shortage.

But may:

```text
send supplies
share information
assist a known character
```

Mission scope should reflect that limited influence.

---

# Meaningful Actionability

The player can plausibly change one or more outcomes.

Example:

```text
Bridge damaged.

Player has technical contacts
and access to repair materials.
```

A repair mission becomes plausible.

---

# Actionability Versus Relevance

These remain separate.

Example:

```text
Close relative dies in distant region.

Relevance:
CRITICAL

Actionability:
NONE
```

The event matters enormously.

There is no mission to generate.

---

# Mission Necessity

Even when action is possible, a formal mission may still be unnecessary.

Example:

```text
Player sees injured traveler.
```

Action:

```text
Provide medicine.
```

This can happen directly without:

```text
MISSION:
Heal the Traveler
```

---

# Mission Necessity Factors

A formal Mission becomes more useful when:

```text
Objective spans time.

Objective spans locations.

Multiple actors are involved.

Outcome depends on several actions.

Opportunity window matters.

Player commitment matters.

Consequences require tracking.
```

---

# Lightweight Action

Prefer immediate interaction when:

```text
Action is simple
+
local
+
immediate
```

Example:

```text
Repair small generator.
```

No mission structure may be needed.

---

# Structured Mission

Use Mission structure when:

```text
Action requires planning
+
multiple steps
+
travel
+
resource commitment
+
meaningful consequence
```

---

# Mission Objective

A Mission Objective describes:

```text
WHAT OUTCOME
THE PLAYER IS TRYING TO PRODUCE
```

It should not unnecessarily dictate:

```text
HOW
```

---

# Outcome-Oriented Objectives

Prefer:

```text
Restore water service to Settlement A.
```

over:

```text
Go to Pump Station.
Kill enemies.
Collect Pump Part.
Return to NPC.
Press repair button.
```

The first allows systemic solutions.

---

# Objective Versus Method

Conceptually:

```text
OBJECTIVE

Restore water service.

POSSIBLE METHODS

Repair pump.

Find alternate water source.

Negotiate connection to nearby system.

Deliver emergency water.

Reduce demand temporarily.
```

Different methods may produce different outcomes.

---

# Mission Objective Types

Initial objective categories may include:

```text
INVESTIGATE
LOCATE
DELIVER
TRANSPORT
REPAIR
RESTORE
PROTECT
ESCORT
NEGOTIATE
TRADE
RECOVER
BUILD
CONNECT
EVACUATE
RESCUE
VERIFY
SURVEY
MEDIATE
SUPPLY
ESTABLISH
DISRUPT
PREVENT
```

The taxonomy should remain functional rather than narrative.

---

# Investigation Mission

Goal:

```text
REDUCE UNCERTAINTY
```

Examples:

```text
Determine why radio contact stopped.

Confirm whether route remains open.

Investigate unusual power behavior.

Locate missing team.
```

---

# Investigation Outcome

An investigation may produce:

```text
Confirmed information

Partial information

New uncertainty

Discovery

New Story Situation
```

Investigation does not require solving the underlying problem.

---

# Verification Mission

Sometimes the key problem is:

```text
IS THE INFORMATION TRUE?
```

Example:

```text
Rumor:
Settlement abandoned.
```

Objective:

```text
Verify settlement status.
```

This integrates directly with Information State.

---

# Delivery Mission

The objective is:

```text
MOVE RESOURCE
FROM A
TO B
```

The important variable is not the object itself.

It is the systemic need.

Example:

```text
Deliver medicine to remote clinic.
```

---

# Transport Mission

Transport may involve:

- people
- resources
- equipment
- information

Example:

```text
Bring repair technicians to substation.
```

---

# Repair Mission

Repair missions should identify:

```text
SYSTEM
DAMAGE
REQUIRED CAPABILITY
DEPENDENCIES
```

Example:

```text
Restore radio relay.
```

Possible constraints:

```text
Replacement component
Technical expertise
Power
Safe access
```

---

# Restoration Mission

Restoration differs from repair.

Example:

```text
Restore regional rail service.
```

may require:

- repair
- clearing route
- negotiation
- staffing
- fuel

This may become a larger Story Situation or multi-stage Mission.

---

# Protection Mission

Objective:

```text
KEEP ACTOR / PLACE / RESOURCE
FUNCTIONAL OR SAFE
```

Examples:

```text
Protect repair team.

Secure harvest.

Guard medical shipment.

Maintain evacuation route.
```

---

# Escort Mission

Escort is appropriate when movement itself creates risk.

The system should know:

```text
WHO

WHY THEY ARE MOVING

WHAT THREAT EXISTS

WHY PLAYER IS RELEVANT
```

Avoid escort missions merely because escort is a familiar gameplay type.

---

# Negotiation Mission

Objective:

```text
CHANGE ACTOR DECISION
OR RELATIONSHIP
```

Examples:

```text
Negotiate route access.

Secure trade agreement.

Resolve authority dispute.

Gain permission to use infrastructure.
```

---

# Mediation Mission

Unlike negotiation for player's own interests, mediation attempts to resolve conflict between other actors.

Example:

```text
Settlement A
and
Settlement B
dispute water allocation.
```

The player may act as mediator because of established reputation.

---

# Trade Mission

Trade missions should emerge from actual:

```text
SURPLUS
+
SHORTAGE
+
ACCESS
+
RELATIONSHIP
```

Example:

```text
Region A:
Food Surplus

Region B:
Medicine Surplus
```

Opportunity:

```text
Establish exchange.
```

---

# Exploration Mission

Exploration should be motivated by:

- information
- opportunity
- curiosity
- strategic need
- discovery

Example:

```text
Unknown radio signal detected east of valley.
```

---

# Survey Mission

Survey differs from exploration because the objective is systematic information gathering.

Example:

```text
Assess abandoned rail corridor
for restoration.
```

---

# Recovery Mission

Recovery missions help improve longer-term world capability.

Examples:

```text
Recover machine tools.

Reopen workshop.

Restore irrigation.

Retrieve archived technical data.
```

These should be especially important in WS-03 and WS-04.

---

# Construction Mission

Some objectives create new infrastructure rather than repair old infrastructure.

Examples:

```text
Build radio relay.

Establish checkpoint.

Construct water reservoir.

Create microgrid.
```

This supports development gameplay.

---

# Emergency Mission

Emergency Missions possess:

```text
SHORT TIME WINDOW
+
HIGH CONSEQUENCE
```

Examples:

```text
Evacuate hospital.

Restore water pump before reserve empties.

Reach trapped convoy before storm.
```

---

# Emergency Does Not Mean Combat

Emergency objectives may involve:

- logistics
- medicine
- repair
- negotiation
- evacuation
- communication

---

# Prevention Mission

Objective:

```text
STOP A PREDICTED EVENT
BEFORE IT OCCURS
```

Example:

```text
Reinforce bridge before flood arrives.
```

Success may mean:

```text
THE CRISIS NEVER HAPPENS.
```

This is an important valid outcome.

---

# Mission Scale

Mission scale should match player influence.

Conceptual levels:

```text
PERSONAL
LOCAL
COMMUNITY
REGIONAL
MULTI-REGIONAL
```

---

# Personal Mission

Examples:

```text
Find missing friend.

Obtain medicine for family member.
```

---

# Local Mission

Examples:

```text
Restore neighborhood water pump.

Find missing local trader.
```

---

# Community Mission

Examples:

```text
Restore settlement radio.

Secure winter fuel supply.
```

---

# Regional Mission

Examples:

```text
Reopen major trade corridor.

Negotiate regional agreement.
```

Regional missions should normally require substantial reputation or capability.

---

# Multi-Regional Mission

These should be rare.

Examples:

```text
Establish major trade network.

Coordinate interregional infrastructure.
```

The player must plausibly possess sufficient influence.

---

# Anti-Chosen-One Principle

Avoid:

```text
Unknown traveler arrives.

Regional government immediately asks
them to decide national strategy.
```

Mission scale must emerge from:

```text
ROLE
REPUTATION
RELATIONSHIP
CAPABILITY
HISTORY
```

---

# Capability Check

Before generating a Mission, the engine should evaluate whether the player can plausibly engage.

Factors include:

```text
Location
Mobility
Skills
Resources
Reputation
Relationships
Information
Access
Time
```

---

# Capability Does Not Require Certainty

The player may attempt something difficult.

Example:

```text
Player has limited technical skill.

Mission:
Repair advanced relay.
```

Possible approaches may include:

```text
Find technician.

Find manual.

Acquire replacement unit.

Create workaround.
```

The mission remains possible without requiring the player personally to possess every skill.

---

# Mission Constraints

Constraints create meaningful structure.

Examples:

```text
TIME
RESOURCE
ACCESS
INFORMATION
SECURITY
RELATIONSHIP
WEATHER
INFRASTRUCTURE
```

---

# Time Constraint

Example:

```text
Hospital reserve:
18 hours.
```

This is a real world constraint.

Not an arbitrary timer.

---

# Resource Constraint

Example:

```text
Repair requires transformer component.
```

The component must exist somewhere plausible.

---

# Access Constraint

Example:

```text
Facility controlled by faction.
```

Possible solutions:

- negotiate
- infiltrate
- gain reputation
- find alternate route

---

# Information Constraint

Example:

```text
Convoy location unknown.
```

The player may need to investigate first.

---

# Security Constraint

Example:

```text
Route:
Dangerous
```

This may require:

- escort
- alternate route
- negotiation
- timing

---

# Mission Approaches

A good systemic Mission should support multiple plausible approaches where the world allows them.

Example:

```text
OBJECTIVE:

Get medicine to Settlement A.
```

Possible approaches:

```text
Buy medicine.

Trade for medicine.

Ask allied faction.

Recover abandoned supply.

Redirect shipment.

Produce substitute.

Negotiate regional allocation.
```

---

# No Mandatory Solution Count

Not every Mission needs:

```text
3 solutions
```

The number of valid approaches should emerge naturally from world conditions.

---

# Solution Discovery

Players may discover methods the generator did not initially prioritize.

If the action is valid under simulation rules:

```text
THE WORLD SHOULD ACCEPT IT.
```

---

# Emergent Solution Principle

Example:

Mission expects:

```text
Repair damaged bridge.
```

Player instead:

```text
Builds temporary ferry crossing.
```

If World Simulation supports it:

```text
OBJECTIVE MAY BE SATISFIED
```

because the actual goal was:

```text
Restore crossing capability.
```

---

# Objective Granularity

Objectives should be expressed at the correct abstraction.

Too narrow:

```text
Collect exactly three valve components.
```

Too broad:

```text
Fix the region.
```

Appropriate:

```text
Restore water distribution
to western settlement.
```

---

# Mission Stages

Some Missions may contain stages.

Conceptually:

```text
DISCOVER
      ↓
PREPARE
      ↓
ACT
      ↓
RESOLVE
```

Stages should not automatically become checklist steps.

---

# Dynamic Stages

Mission stages may emerge as information becomes available.

Example:

```text
Objective:
Find missing convoy.
```

Player discovers:

```text
Convoy stranded.
```

Objective changes:

```text
Help convoy reach settlement.
```

Later:

```text
Bridge destroyed.
```

Mission changes again.

---

# Objective Mutation

Mission Objectives should be allowed to change when World Simulation changes.

Possible states:

```text
UNCHANGED
UPDATED
EXPANDED
REDUCED
REDIRECTED
INVALIDATED
```

---

# Objective Invalidation

Example:

```text
Mission:
Deliver medicine to hospital.

World Event:
Hospital evacuated.
```

Original objective may become invalid.

Possible transformation:

```text
Locate evacuation site
and redirect shipment.
```

or:

```text
Mission Expires.
```

---

# Mission World Continuity

Once a Mission begins:

```text
WORLD SIMULATION CONTINUES
```

The mission does not create a protected narrative bubble.

---

# World-Resolved Mission

Example:

```text
Mission:
Repair bridge.
```

Before player acts:

```text
Regional engineers repair bridge.
```

Mission state:

```text
RESOLVED ELSEWHERE
```

The player is not entitled to every opportunity.

---

# Competing Actors

NPCs and factions may pursue the same objective.

Example:

```text
Abandoned fuel depot discovered.
```

Interested:

```text
Player
Trader Coalition
Regional Authority
Criminal Group
```

The situation develops in real time.

---

# Mission Competition

Possible outcomes:

```text
Player arrives first.

Faction arrives first.

Actors cooperate.

Actors negotiate.

Actors conflict.

Resource already removed.
```

---

# Opportunity Window

Every Mission may possess an opportunity window where appropriate.

Conceptual types:

```text
IMMEDIATE
SHORT
MODERATE
OPEN
CONDITIONAL
```

---

# Opportunity Window Is World-Based

Example:

```text
Storm arrives in 18 hours.
```

The Mission's urgency comes from weather.

Avoid arbitrary:

```text
MISSION EXPIRES IN 17:59
```

unless the world provides that constraint.

---

# Expiration

A Mission may expire because:

- event resolved
- opportunity disappeared
- target moved
- resource consumed
- actor left
- player moved away
- world state changed

---

# Mission Expiration Is Not Failure

If the player never committed:

```text
EXPIRED
```

may be more appropriate than:

```text
FAILED
```

---

# Player Commitment

The engine should distinguish:

```text
AVAILABLE
```

from:

```text
PLAYER COMMITTED
```

This matters for:

- relationships
- obligations
- reputation

---

# Declining a Mission

Declining should not automatically produce negative consequences.

A character may understand.

Consequences depend upon:

```text
Relationship
Urgency
Expectation
Previous promises
Alternatives
```

---

# Accepting Creates Expectation

Once the player explicitly promises to help:

```text
MISSION
```

may also create:

```text
OBLIGATION
```

Failure to act may therefore affect relationships.

---

# Silent Non-Commitment

Hearing about a problem does not mean:

```text
PLAYER PROMISED TO SOLVE IT.
```

This distinction is essential.

---

# Mission Resolution States

Recommended states:

```text
AVAILABLE
ACCEPTED
ACTIVE
COMPLETED
PARTIAL
MIXED
FAILED
ABANDONED
EXPIRED
INVALIDATED
RESOLVED ELSEWHERE
TRANSFORMED
```

---

# Completed

The primary intended outcome was achieved.

This does not imply no negative side effects.

---

# Partial

The player achieved part of the desired outcome.

Example:

```text
60% of medicine delivered.
```

---

# Mixed

The objective was achieved but important secondary consequences occurred.

Example:

```text
Settlement saved.

Bridge destroyed during evacuation.
```

---

# Failed

The player committed to the objective and the primary desired outcome became impossible or was not achieved.

---

# Abandoned

The player explicitly stopped pursuing the objective while it remained potentially achievable.

---

# Invalidated

World conditions make the objective irrelevant or impossible.

Example:

```text
Target settlement evacuated.
```

---

# Resolved Elsewhere

Another actor or world process solved the situation.

---

# Transformed

The Mission becomes a substantially different objective.

---

# Partial Success Principle

Avoid:

```text
SUCCESS
or
FAILURE
```

as the only outcomes.

World Simulation already supports gradients.

Mission outcomes should reflect them.

---

# Mission Outcome

Mission resolution should produce an Outcome Record.

Conceptually:

```text
MISSION OUTCOME

Objective
Result
Player Actions
Resources Used
Actors Affected
World State Changes
Relationship Changes
Reputation Changes
Unresolved Consequences
```

---

# Mission Consequence

Mission completion must feed back into:

```text
World Simulation
```

through:

```text
Consequence_Propagation.md
```

---

# Example

Mission:

```text
Restore radio relay.
```

Success:

```text
Communications:
Improves

Information Horizon:
Expands

Authority Coordination:
Improves
```

Later campaign consequences:

```text
New travelers arrive.

New reports become available.

New faction contact established.
```

---

# Success Does Not Mean Positive Everything

Example:

```text
Player restores trade route.
```

Positive:

```text
Supply improves.
```

Negative:

```text
Outside political influence increases.
```

The world responds systemically.

---

# Failure Does Not Mean Nothing

Example:

```text
Player fails to recover medicine.
```

Result:

```text
Hospital reduces services.

Authority seeks alternative source.

Character relationship changes.

New Story Situation emerges.
```

Failure produces history.

---

# Mission Rewards

Rewards should emerge from the world.

Possible rewards include:

```text
Resources
Money
Trade Goods
Information
Access
Trust
Relationship
Reputation
Infrastructure Improvement
Political Influence
Future Opportunity
```

---

# No Mandatory Reward

Some missions may have no explicit material reward.

Example:

```text
Help close friend find missing family member.
```

The motivation is relational.

---

# Reward Causality

Avoid:

```text
Player repairs radio tower.

Receives unrelated legendary weapon.
```

Prefer:

```text
Player repairs radio tower.

Receives:
regional trust,
communication access,
technical contacts,
future information.
```

Rewards should make sense.

---

# Reputation Reward

Actions may alter reputation based upon:

```text
WHO KNOWS
WHAT THEY BELIEVE HAPPENED
HOW THEY INTERPRET IT
```

Reputation is not automatically global.

---

# Hidden Outcome

Not every Mission result should be immediately visible.

Example:

```text
Player escorts engineering team.
```

Days later:

```text
Power reliability improves.
```

Weeks later:

```text
Workshop production increases.
```

---

# Delayed Mission Consequences

Delayed effects may become:

```text
Unresolved Consequences
```

in Campaign State.

---

# Mission Information

Mission descriptions must preserve player knowledge rather than World Truth.

Example:

World truth:

```text
Convoy destroyed.
```

Player knows only:

```text
Convoy overdue.
```

Mission objective:

```text
Find the convoy.
```

not:

```text
Investigate destroyed convoy.
```

---

# Objective Knowledge State

Mission objectives may contain:

```text
CONFIRMED
LIKELY
REPORTED
UNKNOWN
```

information.

---

# Uncertain Objective

Example:

```text
Reported:
Radio station may still be operating.
```

Objective:

```text
Determine whether contact can be restored.
```

The mission does not assume the answer.

---

# Mission Deception

A mission source may intentionally or unintentionally provide incorrect information.

Example:

```text
Faction claims:
Depot abandoned.
```

Actual:

```text
Depot occupied.
```

This must emerge through Character / Faction knowledge.

Mission Generation itself should not arbitrarily lie.

---

# Mission Conflict

A Mission may place the player between competing interests.

Example:

```text
Fuel Allocation Situation

Hospital needs fuel.

Farmers need fuel.

Transport network needs fuel.
```

Possible Mission:

```text
Secure additional fuel.
```

But if additional fuel cannot be found:

```text
Player may need to influence allocation.
```

---

# No Mandatory Villain

Conflict may arise because:

```text
MULTIPLE LEGITIMATE NEEDS
EXCEED AVAILABLE RESOURCES.
```

This should be common.

---

# Mission Moral Structure

Mission Generation should not assign simplistic moral labels such as:

```text
GOOD OPTION
EVIL OPTION
```

World Simulation provides consequences.

Characters and societies interpret choices.

---

# Player Values

Repeated choices may reveal player priorities:

- family
- community
- profit
- stability
- autonomy
- technology
- exploration
- authority

These may influence future relevance and role development.

---

# Mission Chains

Mission Chains may exist when one outcome naturally creates another.

Example:

```text
Investigate radio silence
      ↓
Discover relay failure
      ↓
Acquire component
      ↓
Repair relay
      ↓
Establish new contact
```

---

# Anti-Chain Padding

Avoid turning one coherent objective into artificial micro-missions purely to extend gameplay.

Example:

```text
Talk to A.
Talk to B.
Collect three objects.
Return to A.
```

unless each step has real systemic or narrative meaning.

---

# Story Situation Versus Mission Chain

Where multiple actors and outcomes exist, prefer:

```text
STORY SITUATION
```

containing several potential actions rather than a rigid linear mission chain.

---

# Mission Branching

Branches should emerge from world conditions and player choices.

Example:

```text
Medicine shortage
      │
      ├── Trade
      ├── Recover abandoned stock
      ├── Negotiate authority allocation
      ├── Find substitute
      └── Transport patients elsewhere
```

---

# Branch Convergence

Different approaches may produce similar immediate outcomes but different long-term consequences.

Example:

Both:

```text
Trade
```

and:

```text
Authority requisition
```

provide medicine.

But:

```text
Trade:
Improves faction relations.
```

```text
Requisition:
May reduce authority legitimacy.
```

---

# Mission Generation and Characters

Character integration should determine:

```text
WHO REQUESTS HELP
WHY THEY ASK THE PLAYER
WHAT THEY KNOW
WHAT THEY WANT
```

Detailed logic belongs in:

```text
Character_Integration.md
```

---

# Mission Source Selection

If multiple actors could request intervention, Mission Generation should not arbitrarily choose one.

Selection should consider:

```text
Relationship
Knowledge
Authority
Need
Contactability
Role
Reputation
```

---

# Example

Fuel crisis.

Possible requesters:

```text
Doctor
Regional Authority
Farmer
Trader
```

Player has strongest relationship with:

```text
Doctor
```

The first direct request may naturally come through that relationship.

Other actors still exist.

---

# Competing Requests

Multiple actors may legitimately approach the player.

Example:

```text
Hospital:
Needs fuel.

Farmers:
Need fuel.

Authority:
Wants player to inspect depot.
```

These are not necessarily duplicate missions.

They may represent conflicting goals inside one Story Situation.

---

# Mission Density

Mission Generation must respect:

```text
Campaign Bandwidth
```

from Campaign State.

A high-actionability situation does not automatically justify another Mission if the campaign is already saturated.

---

# Background Actionability

A situation may remain:

```text
ACTIONABLE
```

without being formally surfaced as a Mission.

The player can discover and act on it independently.

---

# Mission Priority

Mission Generation may assign:

```text
Urgency
Importance
Opportunity Window
Player Commitment
```

But final presentation priority belongs partly to:

```text
Pacing_and_Priority.md
```

---

# Dynamic Urgency

Urgency may change.

Example:

```text
Day 1:
Bridge repair useful.

Day 5:
Storm approaching.

Bridge now needed for evacuation.
```

Mission urgency increases because the world changed.

---

# Mission Transformation Example

Initial:

```text
MISSION:
Repair Bridge.
```

Storm causes collapse.

New state:

```text
TRANSFORMED
```

New possible objective:

```text
Establish emergency crossing.
```

---

# Mission Expiration Example

Mission:

```text
Escort harvest convoy.
```

Player delays.

World Simulation:

```text
Harvest convoy leaves with another escort.
```

Mission:

```text
RESOLVED ELSEWHERE
```

---

# Mission Failure Example

Player commits to:

```text
Deliver medicine by Friday.
```

Medicine remains in player's possession past deadline.

Clinic:

```text
Runs out.
```

Mission:

```text
FAILED
```

Consequences may include:

- health effects
- relationship damage
- reputation changes

---

# Partial Success Example

Player delivers:

```text
half the required fuel.
```

World result:

```text
Hospital remains operational.

Outpatient clinic closes.
```

Mission:

```text
PARTIAL
```

The simulation decides what the delivered amount actually accomplished.

---

# Mixed Outcome Example

Player negotiates trade agreement.

Result:

```text
Fuel imports restored.
```

But agreement requires:

```text
Regional political concession.
```

Mission:

```text
COMPLETED
```

Outcome:

```text
MIXED
```

---

# Player Abandonment

The player may explicitly decide:

```text
"I am no longer doing this."
```

The Mission becomes:

```text
ABANDONED
```

World situation continues.

---

# Mission Reactivation

An abandoned or expired situation may later generate a new Mission if conditions change.

It should normally receive a new Mission ID while retaining causal history.

---

# Mission ID

Conceptually:

```text
MIS-2045-0042
```

Stable identifiers support:

- Campaign State
- consequences
- character memory
- debugging
- history

---

# Mission Data Structure

Conceptually:

```text
MISSION

Mission ID
Source Situation
Source Event / Cluster
Origin
Requester
Objective
Objective Type
Location
Affected Actors
Relevance Path
Actionability
Urgency
Opportunity Window
Known Constraints
Known Information
Player Commitment
Lifecycle State
Resolution State
World References
```

---

# Mission Lifecycle

Recommended lifecycle:

```text
POTENTIAL
AVAILABLE
OFFERED
ACCEPTED
ACTIVE
UPDATED
RESOLVING
RESOLVED
```

with resolution outcomes such as:

```text
COMPLETED
PARTIAL
MIXED
FAILED
ABANDONED
EXPIRED
INVALIDATED
RESOLVED ELSEWHERE
TRANSFORMED
```

---

# Potential

The situation could support a Mission but no Mission has been presented.

---

# Available

The player can plausibly engage.

---

# Offered

A character or organization explicitly presents the opportunity.

Player-created Missions may skip this state.

---

# Accepted

The player commits.

---

# Active

The player is currently pursuing the objective.

---

# Updated

Conditions have materially changed.

---

# Resolving

Player action has occurred and consequences are being calculated.

---

# Resolved

The Mission has reached an outcome.

---

# Mission Presentation

A mission should not necessarily appear as:

```text
MISSION ADDED
```

The interface may instead preserve the fiction.

Example:

```text
Mara:
"If you can find more diesel,
the hospital could use it."
```

Campaign State may internally register:

```text
Mission Available.
```

Player experience remains natural.

---

# Explicit Tracking

Players may choose to formally track an objective.

This is a UI / player preference question.

It should not determine whether the objective exists in the simulation.

---

# Mission Journal

If a Mission Journal exists, it should reflect:

```text
PLAYER KNOWLEDGE
```

not hidden engine truth.

Example:

```text
Find out why the northern relay stopped responding.
```

not:

```text
Repair the lightning-damaged power converter.
```

until the cause is discovered.

---

# Journal Updates

Mission text may update as knowledge improves.

Example:

Initial:

```text
Investigate northern relay.
```

Later:

```text
Relay power converter damaged.
Find replacement or alternate power source.
```

---

# No Spoiler Objectives

Mission descriptions must not reveal:

- hidden actors
- undiscovered causes
- unknown locations
- future outcomes

---

# Mission and Player Failure Tolerance

The campaign should remain playable after failure.

Avoid critical dynamic missions whose failure makes the entire campaign impossible unless intentionally designed as a major narrative boundary.

---

# Failure Creates New State

Conceptually:

```text
MISSION FAILURE
      ↓
WORLD STATE CHANGES
      ↓
NEW STORY SITUATIONS
```

Failure should usually create new possibilities.

---

# Catastrophic Outcomes

Some actions may create severe consequences.

This is valid.

But the system should preserve:

```text
CAUSALITY
```

rather than:

```text
PUNISHMENT
```

---

# Mission Generation Update Cycle

A conceptual Mission Generation cycle:

```text
1. Read active Story Situations.

2. Read Story Hooks.

3. Read player actions and expressed intent.

4. Read Campaign State.

5. Determine actionability.

6. Determine whether formal Mission structure is useful.

7. Identify mission origin.

8. Determine outcome-oriented objective.

9. Determine known constraints.

10. Check player capability.

11. Identify plausible approaches.

12. Determine opportunity window.

13. Identify competing actors.

14. Identify potential consequences.

15. Create Mission if justified.

16. Track world-state changes during Mission.

17. Update objective when necessary.

18. Process player commitment.

19. Resolve outcome through World Simulation.

20. Generate Outcome Record.

21. Pass consequences forward.
```

---

# Mission Example 1
# NPC-Requested

World State:

```text
Medicine:
CONSTRAINED
```

Character:

```text
Mara
Doctor
Close relationship
```

Story Hook:

```text
"We're down to our last antibiotic stock."
```

Mission eligibility:

```text
Player can acquire medicine.

Player intervention can matter.
```

Possible Mission:

```text
Objective:
Increase antibiotic supply available
to the hospital.
```

Not:

```text
Collect 10 Antibiotics.
```

Possible approaches remain open.

---

# Mission Example 2
# Player-Created

Story Hook:

```text
Unknown radio transmission.
```

Player:

```text
"I want to find out who that is."
```

Mission:

```text
Origin:
Player

Objective:
Identify the source of the transmission.
```

No quest giver.

---

# Mission Example 3
# No Mission

Event:

```text
Friend announces wedding.
```

Relevance:

```text
HIGH
```

Actionability:

```text
Attend
Decline
Send gift
```

No formal Mission required unless broader circumstances make travel or participation itself meaningful.

---

# Mission Example 4
# World-Resolved

Mission:

```text
Restore road access.
```

Before player acts:

```text
Local crews clear landslide.
```

Result:

```text
RESOLVED ELSEWHERE
```

Player may hear:

```text
"The road reopened this morning."
```

---

# Mission Example 5
# Transformation

Mission:

```text
Deliver food to Settlement A.
```

During travel:

```text
Settlement A evacuates.
```

Mission transforms:

```text
Find evacuation convoy
and determine where supplies are needed.
```

---

# Mission Example 6
# Multiple Solutions

Objective:

```text
Restore drinking water
to Settlement B.
```

Potential solutions:

```text
Repair pump.

Deliver generator fuel.

Connect alternate pipeline.

Establish temporary water convoy.

Reduce demand and use stored reserve.
```

The simulation evaluates actual consequences.

---

# Mission Example 7
# Competing Needs

Situation:

```text
Regional fuel shortage.
```

Requests:

```text
Hospital:
Needs fuel.

Farmers:
Need fuel.

Authority:
Needs transport reserve.
```

There may be no solution satisfying everyone.

The mission structure should preserve the tradeoff.

---

# Mission Example 8
# Prevention

Information:

```text
Flood forecast in four days.

Bridge:
Structurally strained.
```

Possible player-created or authority mission:

```text
Objective:
Keep eastern crossing operational
during expected flood.
```

Possible successful outcome:

```text
Bridge never fails.
```

The player prevented the future crisis.

---

# Mission Example 9
# Investigation Without Solution

Objective:

```text
Determine why Settlement C
stopped transmitting.
```

Player discovers:

```text
Settlement voluntarily isolated itself.
```

Mission:

```text
COMPLETED
```

The player does not need to:

```text
fix
```

anything.

Information was the objective.

---

# Mission Example 10
# Recovery

World State:

```text
Machine Parts:
CONSTRAINED
```

Discovery:

```text
Abandoned machine shop
may still contain tooling.
```

Mission:

```text
Assess and recover usable industrial equipment.
```

Success may increase:

```text
Regional Manufacturing Capacity
```

for years.

---

# Mission Consistency Rules

## Rule 1

Relevant situations do not automatically become Missions.

---

## Rule 2

The first question is whether a Mission is necessary.

---

## Rule 3

Player intervention must be plausible.

---

## Rule 4

Player action must be capable of affecting an outcome.

---

## Rule 5

Players may create their own objectives.

---

## Rule 6

A Quest Giver is not required.

---

## Rule 7

Objectives should describe outcomes rather than mandatory methods.

---

## Rule 8

The simulation should accept emergent solutions when causally valid.

---

## Rule 9

Mission scale should match player capability and influence.

---

## Rule 10

The player should not become important to every crisis.

---

## Rule 11

Accepted Missions do not freeze World Simulation.

---

## Rule 12

Other actors may resolve Missions.

---

## Rule 13

Objectives may change when World State changes.

---

## Rule 14

Mission expiration should arise from world conditions.

---

## Rule 15

Hearing a request does not equal accepting an obligation.

---

## Rule 16

Explicit commitment may create an obligation.

---

## Rule 17

Mission outcomes should support partial and mixed results.

---

## Rule 18

Failure must create world consequences.

---

## Rule 19

Success may create negative secondary consequences.

---

## Rule 20

Rewards should arise from world and social causality.

---

## Rule 21

Not every Mission requires material reward.

---

## Rule 22

Mission information must respect Player Knowledge.

---

## Rule 23

Mission descriptions must not reveal hidden truth.

---

## Rule 24

Conflicting legitimate interests are valid mission structures.

---

## Rule 25

Combat is one possible method, not a mission requirement.

---

## Rule 26

Mission Chains should not be padded artificially.

---

## Rule 27

Mission Generation must respect Campaign Bandwidth.

---

## Rule 28

Missionless player intervention is a successful system outcome.

---

## Rule 29

Mission outcomes must feed back into World Simulation.

---

## Rule 30

Every generated Mission must remain explainable.

---

# Guiding Questions

Before generating a Mission, the engine should be able to answer:

**What situation already exists?**

**Why does it matter to the player?**

**Can the player actually influence it?**

**Is formal Mission structure useful?**

**Who wants something to change?**

**Why would they involve this player?**

**What outcome is desired?**

**What does the player currently know?**

**What constraints actually exist?**

**What alternatives are plausible?**

**What happens if the player does nothing?**

**Could another actor solve it?**

**How long does the opportunity remain?**

**What happens if the player partially succeeds?**

**What world systems will change afterward?**

If these questions cannot be answered, the Mission probably should not exist.

---

# Core Design Principle

Project Ascension should not create:

```text
QUESTS FOR THE PLAYER TO COMPLETE.
```

It should create:

```text
WORLD SITUATIONS
THE PLAYER MAY CHOOSE TO CHANGE.
```

Sometimes that choice becomes:

```text
A Mission.
```

Sometimes it becomes:

```text
A conversation.

A spontaneous journey.

A trade.

An investigation.

A decision.

Or nothing at all.
```

All are valid.

---

# Living Campaign Pipeline

With Mission Generation established:

```text
WORLD SIMULATION
      │
      ▼
WORLD EVENT INTAKE
      │
      ▼
RELEVANCE & PROXIMITY
      │
      ▼
STORY HOOKS
      │
      ▼
PLAYER RESPONSE
      │
      ├── Ignore
      ├── Observe
      ├── Investigate
      ├── Act Directly
      └── Commit
              │
              ▼
       MISSION GENERATION
        when appropriate
              │
              ▼
        PLAYER ACTION
              │
              ▼
         WORLD RESULT
```

This preserves the central Living Campaign philosophy:

```text
THE PLAYER ENTERS
BEFORE THE MISSION.
```

---

# Architectural Result

The campaign can now support:

```text
WORLD-DRIVEN MISSIONS

CHARACTER-DRIVEN MISSIONS

PLAYER-CREATED MISSIONS

FACTION-DRIVEN MISSIONS

OPPORTUNITY MISSIONS

MISSIONLESS INTERVENTION
```

all from the same underlying system.

This means Project Ascension does not require two separate modes:

```text
QUESTING
```

and:

```text
OPEN WORLD.
```

The same living world supports both.

---

# Current Status

```text
LIVING CAMPAIGN ENGINE

README.md
FOUNDATION DEFINED

Campaign_State.md
FOUNDATION DEFINED

World_Event_Intake.md
FOUNDATION DEFINED

Relevance_and_Proximity.md
FOUNDATION DEFINED

Story_Hooks.md
FOUNDATION DEFINED

Mission_Generation.md
FOUNDATION DEFINED

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
Canon/Systems/Living_Campaign_Engine/Character_Integration.md
```

Mission Generation can now establish:

```text
WHAT THE PLAYER COULD DO.
```

But Characters are what make many of those situations matter emotionally.

`Character_Integration.md` should define:

- character needs
- character goals
- character autonomy
- character knowledge
- character professions
- character location
- relationship relevance
- contact behavior
- character requests
- character reactions
- independent problem solving
- character migration
- character involvement in World Events
- character memory references
- character consequences
- recurring characters
- death, disappearance and separation
- when characters should NOT contact the player

Most importantly, it should preserve:

```text
NPC
≠
QUEST DISPENSER
```

A character should contact the player because:

```text
THE CHARACTER
HAS A REASON.
```

Not because:

```text
THE CAMPAIGN
NEEDS A MISSION.
```

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial Mission Generation framework established for mission eligibility, player-created objectives, missionless intervention, outcome-oriented objectives, multiple approaches, dynamic objectives, opportunity windows, partial outcomes and World Simulation feedback. |