# PROJECT ASCENSION
# Relevance and Proximity System

| Field | Value |
|--------|-------|
| System | Living Campaign Engine |
| Document | Relevance and Proximity |
| Location | Canon/Systems/Living_Campaign_Engine/Relevance_and_Proximity.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Campaign Relevance, Proximity and Player-Specific Significance |
| Last Updated | 2026-08-09 |

> *"Distance is not measured only in kilometers. A distant event can be close if it touches someone, something or somewhere the player cares about."*

---

# Purpose

The Relevance and Proximity system determines how strongly a World Event Candidate matters to a specific campaign.

It evaluates the relationship between:

```text
EVENT
+
PLAYER
+
CAMPAIGN STATE
```

and produces a Campaign Relevance assessment.

The system considers:

- geographic proximity
- social proximity
- relationship proximity
- economic proximity
- infrastructure proximity
- political proximity
- faction proximity
- goal relevance
- resource relevance
- historical relevance
- role relevance
- threat relevance
- opportunity relevance
- knowledge relevance
- timing
- campaign pressure

Its purpose is to identify:

```text
WHY THIS EVENT MATTERS
TO THIS PLAYER
NOW
```

---

# Core Principle

The central rule is:

```text
WORLD SIGNIFICANCE
≠
CAMPAIGN RELEVANCE
```

A globally important event may have little immediate relevance to the player.

A tiny local event may matter enormously.

Example:

```text
WORLD EVENT

Political crisis
on another continent.

World Significance:
MAJOR

Campaign Relevance:
LOW
```

versus:

```text
WORLD EVENT

Local clinic loses power.

World Significance:
LOCAL

Player's child is inside.

Campaign Relevance:
EXTREME
```

---

# Relevance Is Relational

Relevance does not belong to the event alone.

Conceptually:

```text
EVENT A
```

may be:

```text
LOW relevance
for Player A
```

and:

```text
EXTREME relevance
for Player B
```

at the same moment.

The difference comes from Campaign State.

---

# Relevance Dimensions

The initial relevance model includes:

```text
RELEVANCE
│
├── Geographic
├── Social
├── Relationship
├── Economic
├── Infrastructure
├── Political
├── Faction
├── Goal
├── Resource
├── Historical
├── Role
├── Threat
├── Opportunity
├── Knowledge
└── Timing
```

Not every event needs every dimension.

---

# Geographic Proximity

Geographic Proximity measures physical distance between the event and the player.

Conceptual values:

```text
IMMEDIATE
LOCAL
REGIONAL
NEIGHBORING
DISTANT
REMOTE
```

---

# Immediate

```text
IMMEDIATE
```

The event is occurring at or directly around the player's location.

Examples:

```text
Same building
Same road
Same settlement block
```

---

# Local

```text
LOCAL
```

The event affects the same settlement or immediate operational area.

---

# Regional

```text
REGIONAL
```

The event occurs within the player's current region.

---

# Neighboring

```text
NEIGHBORING
```

The event occurs in a nearby region with plausible direct interaction.

---

# Distant

```text
DISTANT
```

The event occurs beyond ordinary direct interaction.

---

# Remote

```text
REMOTE
```

The event has little physical relationship to the player's current location.

---

# Geographic Distance Is Not Enough

Physical distance should never be used as the only relevance measure.

Example:

```text
Event:
Bridge failure 300 km away.
```

Normally:

```text
Geographic Relevance:
LOW
```

But if that bridge carries the player's primary trade route:

```text
Economic Relevance:
HIGH

Infrastructure Relevance:
HIGH
```

Overall relevance may become high.

---

# Travel-Time Proximity

Where useful, distance should consider actual travel difficulty rather than map distance.

Example:

```text
Location A:
80 km away

Travel time:
2 days
```

may be less accessible than:

```text
Location B:
150 km away

Rail connection:
4 hours
```

Conceptually:

```text
PROXIMITY
=
DISTANCE
+
ACCESSIBILITY
```

---

# Social Proximity

Social Proximity measures how closely an event touches the player's social world.

It may involve:

- family
- friends
- settlement community
- professional contacts
- known characters
- trusted networks

Conceptual values:

```text
DIRECT
CLOSE
CONNECTED
INDIRECT
NONE
```

---

# Direct Social Proximity

Example:

```text
Player's partner
is directly affected.
```

This should create high relevance even if the event is geographically distant.

---

# Relationship Proximity

Relationship Proximity uses the strength and type of known relationships.

Conceptually:

```text
RELATIONSHIP PROXIMITY

Relationship Strength
+
Relationship Type
+
Current Contact
+
Current Need
```

---

# Example

```text
Character:
Older brother

Relationship:
Close

Location:
Distant region

Event:
Regional evacuation
```

Overall relevance may become:

```text
EXTREME
```

despite geographic distance.

---

# Relationship Strength

Possible conceptual values:

```text
CRITICAL
STRONG
MEANINGFUL
WEAK
NONE
```

Exact relationship mechanics belong in:

```text
Canon/Systems/Relationships/
```

Relevance only consumes the result.

---

# Relationship Type

Relationship Type may alter the meaning of an event.

Examples:

```text
Family
Partner
Friend
Dependent
Mentor
Rival
Professional Contact
```

A crisis involving a rival may also have high relevance.

Relevance does not mean positive emotion.

---

# Economic Proximity

Economic Proximity measures whether the event affects:

- income
- trade
- business
- employment
- contracts
- markets
- valuable resources

Conceptual values:

```text
DIRECT
HIGH
MODERATE
LOW
NONE
```

---

# Example

```text
Event:
Rail line disrupted in neighboring region.

Player Role:
Trader

Player Business:
Depends on rail route.
```

Economic relevance becomes high.

---

# Infrastructure Proximity

Infrastructure Proximity measures whether the event affects systems supporting the player's:

- home
- settlement
- travel
- work
- relationships
- resources

Examples include:

```text
Power plant
Water system
Bridge
Fuel depot
Radio relay
Hospital
```

---

# Infrastructure Dependency

Relevance should consider dependency.

Example:

```text
Power station:
150 km away

Player Settlement Dependency:
CRITICAL
```

Infrastructure relevance:

```text
HIGH
```

---

# Political Proximity

Political Proximity measures whether an event affects institutions that matter to the player.

Examples:

```text
Regional government
Settlement council
National authority
Local election
Emergency administration
```

---

# Political Relevance Example

```text
Player Goal:
Gain settlement autonomy.

Event:
Regional authority proposes new tax system.
```

Political relevance becomes high.

---

# Faction Proximity

Faction Proximity measures the relationship between the event and factions known to the player.

Relevant factors include:

```text
Faction Relationship
Faction Reputation
Player Obligations
Faction Goals
Faction Territory
```

---

# Example

```text
Event:
Faction A loses trade depot.

Player:
Allied with Faction A.
```

Relevance increases.

If the player is allied with its rival:

```text
Opportunity Relevance
```

may also increase.

---

# Goal Relevance

Goal Relevance measures whether an event affects an active player objective.

Example:

```text
Goal:
Reach Settlement B.

Event:
Main road closes.
```

Goal relevance:

```text
EXTREME
```

---

# Goal Relationship Types

An event may:

```text
BLOCK
ENABLE
COMPLICATE
ACCELERATE
REDIRECT
INVALIDATE
```

a goal.

---

# Goal Blocking

Example:

```text
Goal:
Deliver medicine.

Event:
Bridge destroyed.
```

The event directly blocks current action.

---

# Goal Enabling

Example:

```text
Goal:
Enter restricted facility.

Event:
Security withdrawal.
```

The event creates an opportunity.

---

# Goal Redirection

An event may change the best path toward a goal.

Example:

```text
Original plan:
Trade for fuel.

New event:
Fuel shipment seized.

New possible path:
Negotiate with another settlement.
```

---

# Resource Relevance

Resource Relevance measures whether the event affects resources important to the player.

Examples:

```text
Food
Fuel
Medicine
Money
Transport
Shelter
Equipment
Trade Goods
Information
```

---

# Resource Dependency

A fuel shortage means different things depending upon the player.

Example:

```text
Player A:
Travels by bicycle.

Fuel Relevance:
LOW
```

```text
Player B:
Runs freight transport.

Fuel Relevance:
EXTREME
```

---

# Resource Scarcity Amplification

Relevance increases when the affected resource is already scarce.

Conceptually:

```text
EVENT AFFECTS RESOURCE
+
PLAYER DEPENDS ON RESOURCE
+
RESOURCE ALREADY SCARCE
=
AMPLIFIED RELEVANCE
```

---

# Historical Relevance

Historical Relevance measures whether the event connects to meaningful past campaign events.

Examples:

```text
Previously saved settlement

Former enemy

Old mission location

Broken promise

Past disaster

Recovered Record
```

---

# Example

```text
Event:
Settlement A requests help.

Campaign Memory:
Player saved Settlement A five years earlier.
```

Historical relevance becomes high.

---

# Historical Echo

Events may resemble earlier player experiences.

Example:

```text
Past:
Failed evacuation.

Current:
New evacuation order.
```

The similarity may increase emotional or narrative relevance even if no direct causal connection exists.

This is a:

```text
HISTORICAL ECHO
```

---

# Role Relevance

Role Relevance measures whether an event fits the player's established campaign role.

Examples:

```text
Trader
Technician
Mediator
Scout
Investigator
Protector
Leader
```

---

# Example

```text
Event:
Water-treatment system fails.

Player Role:
Recognized Technician
```

Role relevance:

```text
HIGH
```

Another player may only hear about the problem as background.

---

# Role Emergence Feedback

Campaign behavior can produce a loop:

```text
Player repairs infrastructure
      ↓
Technician reputation grows
      ↓
Infrastructure events gain relevance
      ↓
More technical opportunities appear
      ↓
Player continues technician role
```

This supports organic campaign identity.

---

# Avoid Role Lock-In

Role relevance should influence possibilities.

It should not trap the player.

Example:

```text
Recognized Technician
```

does not mean:

```text
Only technical missions may appear.
```

Other relevance dimensions remain active.

---

# Threat Relevance

Threat Relevance measures how strongly the event threatens:

- player
- relationships
- resources
- goals
- home
- faction allies
- future options

Conceptual levels:

```text
NONE
LOW
MODERATE
HIGH
EXTREME
```

---

# Threat Is Contextual

Example:

```text
Security conflict:
Regional
```

If the player is leaving tomorrow:

```text
Threat Relevance:
LOW
```

If the conflict blocks the only road home:

```text
Threat Relevance:
HIGH
```

---

# Direct Threat

```text
DIRECT
```

means the event may cause immediate harm to the player or something critical to them.

This should strongly amplify overall relevance.

---

# Opportunity Relevance

Opportunity Relevance measures potential benefit.

Examples:

```text
Trade
Resources
Information
Political Influence
Relationship
Discovery
Infrastructure
Technology
```

Conceptual levels:

```text
NONE
LOW
MODERATE
HIGH
EXCEPTIONAL
```

---

# Opportunity Example

```text
World Event:
New trade route opens.

Player Role:
Trader.

Current Goal:
Reach northern market.
```

Opportunity relevance may become:

```text
EXCEPTIONAL
```

---

# Threat and Opportunity Can Coexist

Example:

```text
Abandoned fuel depot discovered.

Threat:
Armed group nearby.

Opportunity:
Large fuel reserve.
```

The event may be simultaneously:

```text
HIGH THREAT
+
HIGH OPPORTUNITY
```

This often creates interesting gameplay.

---

# Knowledge Relevance

Knowledge Relevance measures how the event interacts with what the player already knows.

An event may:

```text
CONFIRM
CONTRADICT
EXPAND
ANSWER
COMPLICATE
```

existing knowledge.

---

# Example

```text
Player believes:
Region A is abandoned.

Event:
Radio transmission detected from Region A.
```

Knowledge relevance becomes high.

---

# Mystery Relevance

Information contradicting an established player belief may generate strong investigative relevance.

Example:

```text
Known:
Character presumed dead.

New Event:
Character's identification code appears on radio traffic.
```

---

# Timing Relevance

Timing can amplify relevance.

Example:

```text
Player is traveling tomorrow.

Event:
Road closure tonight.
```

High timing relevance.

The same road closure three months earlier may be irrelevant.

---

# Temporal Proximity

Conceptual values:

```text
IMMEDIATE
SOON
CURRENT
LATER
DISTANT
```

---

# Opportunity Window

Events with short windows may receive increased relevance.

Example:

```text
Trade convoy leaves in 6 hours.
```

This does not mean it must become a mission.

It means time matters.

---

# Relevance Amplifiers

Certain conditions may amplify relevance.

Examples:

```text
Direct relationship affected
Current goal blocked
Critical resource threatened
Player physically present
Existing obligation involved
Very short opportunity window
Strong campaign memory connection
Player role directly applicable
```

---

# Relevance Dampeners

Other conditions may reduce relevance.

Examples:

```text
Very distant
No known actors
No player dependency
No current goal relationship
Already resolved
Duplicate of existing situation
Low novelty
Campaign overload
```

Campaign overload primarily belongs to Pacing, but it may affect presentation priority.

---

# Relevance Score

The system may eventually use a derived Relevance Score.

Conceptually:

```text
RELEVANCE SCORE
=
Geographic
+
Social
+
Relationship
+
Goal
+
Resource
+
Faction
+
Historical
+
Role
+
Threat
+
Opportunity
+
Knowledge
+
Timing
```

This is conceptual.

No universal numeric formula is required at this stage.

---

# Weighted Relevance

Different dimensions should not carry equal importance.

Example:

```text
Direct threat to child
```

should outweigh:

```text
moderate geographic distance.
```

Likewise:

```text
event directly blocks primary goal
```

should usually matter more than:

```text
minor faction relevance.
```

---

# Hard Relevance Triggers

Some conditions may immediately establish high relevance.

Examples:

```text
Player directly threatened.

Close relationship directly affected.

Primary goal directly blocked.

Current settlement directly affected.

Critical player resource directly threatened.

Active obligation directly affected.
```

These should normally bypass low-level relevance filtering.

---

# Soft Relevance

Some events become relevant through accumulation.

Example:

```text
Distant trade disruption
+
player is trader
+
current fuel shortage
+
known contact in affected area
```

No individual factor is decisive.

Together they create high relevance.

---

# Relevance Categories

Recommended output categories:

```text
NONE
BACKGROUND
LOW
MODERATE
HIGH
CRITICAL
```

---

# None

```text
NONE
```

No meaningful current relationship exists between event and campaign.

Event remains in World Simulation.

---

# Background

```text
BACKGROUND
```

Event may influence atmosphere or environment but does not require direct presentation.

---

# Low

```text
LOW
```

The event has some connection to the campaign.

It may surface as ambient information.

---

# Moderate

```text
MODERATE
```

The event meaningfully intersects with player context.

It should be considered for Story Hook generation.

---

# High

```text
HIGH
```

The event directly affects important campaign elements.

It should normally become visible if information can plausibly reach the player.

---

# Critical

```text
CRITICAL
```

The event directly threatens or transforms a major campaign concern.

Examples:

- player's home
- close relationship
- primary goal
- immediate survival
- major unresolved obligation

Critical relevance does not automatically mean a quest.

---

# Relevance Explanation

Every relevance assessment should preserve the reasons.

Example:

```text
RELEVANCE ASSESSMENT

Event:
Regional Fuel Crisis

Overall:
HIGH

Reasons:

Geographic:
REGIONAL

Resource:
HIGH
Player depends on vehicle fuel.

Goal:
HIGH
Current delivery mission requires transport.

Relationship:
LOW

Faction:
MODERATE
Regional Authority is trusted.

Threat:
MODERATE

Opportunity:
LOW
```

This keeps generation explainable.

---

# Relevance Vector

Rather than storing only one score, the engine may preserve a Relevance Vector.

Example:

```text
RELEVANCE VECTOR

Geographic:      High
Relationship:    Low
Goal:            High
Resource:        High
Faction:         Moderate
Historical:      Low
Role:            Moderate
Threat:          Moderate
Opportunity:     Low
```

This helps later systems decide presentation style.

---

# Why the Vector Matters

Two events may have the same overall relevance but feel very different.

Example A:

```text
High relevance
because of immediate threat.
```

Example B:

```text
High relevance
because of relationship connection.
```

Story Hooks should present them differently.

---

# Presentation Implications

Conceptually:

```text
HIGH RELATIONSHIP RELEVANCE
→ Character contact

HIGH GEOGRAPHIC RELEVANCE
→ Environmental observation

HIGH FACTION RELEVANCE
→ Faction message

HIGH INFORMATION RELEVANCE
→ Report / clue

HIGH OPPORTUNITY RELEVANCE
→ Offer / discovery
```

Final presentation belongs to:

```text
Story_Hooks.md
```

---

# Multiple Relevance Paths

A single Event Cluster may reach the player through several relevance paths.

Example:

```text
FUEL CRISIS
```

Player relevance:

```text
Resource:
Fuel dependency

Relationship:
Friend works at hospital

Faction:
Regional authority

Goal:
Delivery mission
```

The engine should recognize these as:

```text
ONE SITUATION
WITH MULTIPLE RELEVANCE PATHS
```

not four separate stories.

---

# Dominant Relevance

Where useful, the engine may identify the strongest relevance path.

Example:

```text
Dominant Relevance:
Relationship
```

This may guide Story Hook selection.

---

# Secondary Relevance

Secondary relevance may enrich presentation.

Example:

```text
Dominant:
Relationship

Secondary:
Resource
Faction
```

A friend's request may naturally mention fuel rationing and regional policy.

---

# Relevance Decay

Relevance may decline over time.

Example:

```text
Old bridge closure
```

may initially be highly relevant.

After the player changes route permanently:

```text
Goal Relevance:
LOW
```

The event may remain active in the world.

Campaign relevance has changed.

---

# Decay Sources

Relevance may decline when:

```text
Player moves away.

Goal completes.

Relationship ends.

Alternative resource found.

Event becomes normalized.

Opportunity expires.

Faction relationship changes.
```

---

# Relevance Persistence

Some relevance should decay slowly.

Examples:

```text
Close family threat

Major unresolved promise

Long-term political rivalry

Mystery central to player goal
```

---

# Relevance Amplification Over Time

Relevance may also increase.

Example:

```text
Day 1:
Distant shortage.

Relevance:
LOW
```

Later:

```text
Player's trade partner relocates there.

Relevance:
MODERATE
```

Later:

```text
Player begins traveling there.

Relevance:
HIGH
```

---

# Relevance Reevaluation

Active events should be reevaluated when Campaign State changes.

Triggers include:

```text
Player moves.

Player goal changes.

New relationship forms.

Character relocates.

Player acquires new role.

Resource dependency changes.

Faction alliance changes.

Player learns new information.

Event escalates.

Event spreads.

Opportunity window changes.
```

---

# Relevance and Player Knowledge

An event may have high objective relevance while remaining unknown.

Example:

```text
Player's sibling is in danger.

Campaign Relevance:
CRITICAL

Player Knowledge:
NONE
```

This does not justify magically informing the player.

The next question becomes:

```text
CAN INFORMATION REACH THEM?
```

Story Hooks and Information State decide that.

---

# Hidden Relevance

This condition may be stored as:

```text
HIDDEN HIGH RELEVANCE
```

meaning the event matters greatly but has not yet entered the player's knowledge environment.

---

# Discovery Path

A hidden relevant event may later become visible through:

```text
Radio
Traveler
Character
Faction
Recovered Record
Direct observation
Environmental evidence
```

---

# Relevance and Information Delay

Example:

```text
Event:
Relative injured.

Time:
Day 1

Player receives message:
Day 4
```

The relevance existed from Day 1.

Campaign visibility began on Day 4.

This distinction is essential.

---

# Relevance and Campaign Pressure

Campaign Pressure should not change whether an event objectively matters.

It may change how aggressively it is surfaced.

Example:

```text
Event:
Moderate relevance.

Campaign Pressure:
OVERLOADED
```

The event may remain background.

But:

```text
Critical relevance
```

should be difficult to suppress entirely.

---

# Relevance Priority Boundary

Relevance answers:

```text
HOW MUCH DOES THIS MATTER?
```

Pacing answers:

```text
WHEN AND HOW STRONGLY SHOULD IT BE PRESENTED?
```

These must remain separate.

---

# Relevance and Character Autonomy

Character actions may create relevance independently of player preference.

Example:

```text
Known friend chooses to join regional expedition.
```

Even if the player has no current related goal, the strong relationship may create relevance.

Characters remain autonomous.

---

# Relevance and Faction Autonomy

Likewise:

```text
Allied faction changes leadership.
```

may be relevant because it changes the player's political environment.

---

# Negative Relevance

Relevance is not the same as desirability.

Events the player wants to avoid may still be highly relevant.

Example:

```text
Former enemy arrives in town.
```

High relevance.

Negative emotional value.

---

# Positive Relevance

Likewise:

```text
Long-lost friend returns.
```

may have high relevance without threat.

The engine must not bias toward danger.

---

# Opportunity Bias Prevention

The engine should detect:

```text
GOOD NEWS
```

as readily as:

```text
BAD NEWS
```

Examples:

- recovered route
- new trade
- returning character
- improved supply
- political opening
- discovered technology

---

# Personal Versus Systemic Relevance

Events may be:

```text
PERSONALLY RELEVANT
```

or:

```text
SYSTEMICALLY RELEVANT
```

or both.

Example:

```text
Hospital fuel shortage
```

may matter systemically.

If player's mother is inside:

```text
Personal relevance also becomes high.
```

---

# Local Relevance Without Player Connection

A local event should often have at least background relevance because it affects the environment the player directly occupies.

Example:

```text
Local market closes.
```

Even without relationship or goal connection:

```text
Geographic Relevance:
HIGH
```

may justify environmental presentation.

---

# Distant Relevance Through Chains

An event may be distant but relevant through dependency chains.

Example:

```text
Copper mine failure
in distant region
      ↓
Transformer production falls
      ↓
Player settlement repair delayed
```

Infrastructure / Supply proximity creates relevance without geographic proximity.

---

# Relevance Path

The engine should be capable of preserving a path such as:

```text
EVENT

Copper mine disruption
      ↓
Transformer shortage
      ↓
Regional power repair delay
      ↓
Player settlement

RELEVANCE PATH:
Infrastructure dependency
```

This improves explainability.

---

# Multi-Hop Relevance

Events should be allowed to matter through multiple hops.

However, relevance should generally decay with each weak dependency unless a critical dependency exists.

Conceptually:

```text
Direct effect:
Strong

One dependency:
Moderate

Five weak dependencies:
Usually low
```

---

# Critical Dependency Exception

Example:

```text
Only supplier
of rare medical component
```

may remain highly relevant even across several geographic hops.

---

# Relevance Network

Conceptually, Campaign State forms a relevance network around the player.

```text
PLAYER
│
├── Locations
├── Characters
├── Goals
├── Resources
├── Factions
├── Roles
├── History
└── Infrastructure Dependencies
```

World Events interact with this network.

The stronger the connection, the greater potential relevance.

---

# Relevance Horizon

The campaign may maintain a practical Relevance Horizon.

Unlike Information Horizon, this is not geographic alone.

Conceptually:

```text
IMMEDIATE WORLD

Strongly connected to player.

EXTENDED WORLD

Indirectly connected.

BACKGROUND WORLD

No meaningful current connection.
```

---

# Relevance Horizon Can Change

As the player gains:

- reputation
- political influence
- trade networks
- relationships
- mobility

their Relevance Horizon may expand.

A local character may eventually become a regional leader.

The kinds of events that matter to them change accordingly.

---

# Influence and Relevance

Player influence should not be confused with relevance.

Example:

```text
National crisis

Relevance:
HIGH

Player Influence:
LOW
```

The player may care deeply but possess little ability to alter the outcome.

---

# Actionability Boundary

Relevance answers:

```text
DOES IT MATTER?
```

Mission Generation later asks:

```text
CAN THE PLAYER MEANINGFULLY DO SOMETHING?
```

A highly relevant event may not be actionable.

Example:

```text
Distant relative dies.
```

High relevance.

No mission required.

---

# Relevance Without Mission

Possible outputs include:

```text
Conversation
News
Memory
Relationship change
Environmental effect
Emotional consequence
```

This is essential.

---

# Event Candidate Evaluation

A conceptual evaluation sequence:

```text
1. Read Event Candidate.

2. Read Campaign State.

3. Evaluate geographic proximity.

4. Evaluate social and relationship proximity.

5. Evaluate economic and infrastructure dependency.

6. Evaluate political and faction relevance.

7. Evaluate active goals.

8. Evaluate resource dependency.

9. Evaluate campaign history.

10. Evaluate player roles.

11. Evaluate threat.

12. Evaluate opportunity.

13. Evaluate knowledge relationship.

14. Evaluate timing.

15. Identify relevance amplifiers.

16. Identify dampeners.

17. Determine Relevance Vector.

18. Determine dominant relevance path.

19. Determine overall relevance.

20. Preserve explanation.

21. Pass relevant candidates forward.
```

---

# Relevance Output

Conceptually:

```text
RELEVANCE OUTPUT

Event ID:
WEC-2045-00142

Overall Relevance:
HIGH

Dominant Path:
RESOURCE

Secondary Paths:
GOAL
GEOGRAPHIC

Geographic:
REGIONAL

Relationship:
NONE

Economic:
HIGH

Infrastructure:
MODERATE

Political:
LOW

Faction:
MODERATE

Goal:
HIGH

Resource:
CRITICAL

Historical:
LOW

Role:
HIGH

Threat:
MODERATE

Opportunity:
LOW

Knowledge:
MODERATE

Timing:
HIGH

Visibility:
NOT YET DETERMINED

Actionability:
NOT YET DETERMINED
```

This becomes input for Story Hooks and later Mission Generation.

---

# Example 1 — Distant Major Event

```text
EVENT:

Major earthquake
in distant continent.

World Significance:
SYSTEMIC
```

Campaign:

```text
No relationships
No trade
No faction connection
No current goal
```

Result:

```text
Campaign Relevance:
BACKGROUND / LOW
```

Possible later presentation:

```text
Radio mention
Price changes
```

if consequences reach the campaign.

---

# Example 2 — Small Local Event

```text
EVENT:

Local mechanic injured.
```

World Significance:

```text
LOCAL
```

Campaign:

```text
Mechanic is player's closest friend.
```

Result:

```text
Campaign Relevance:
CRITICAL
```

---

# Example 3 — Economic Chain

```text
EVENT:

Mountain pass closed.

Player:
Trader.

Current contract:
Uses that pass.
```

Result:

```text
Geographic:
REGIONAL

Economic:
HIGH

Goal:
CRITICAL

Overall:
CRITICAL
```

---

# Example 4 — Hidden Relationship Event

```text
EVENT:

Player's sibling evacuated
from distant city.

Player Knowledge:
NONE
```

Result:

```text
Relationship Relevance:
CRITICAL

Overall Relevance:
CRITICAL

Visibility:
HIDDEN
```

The event should remain highly relevant while the system searches for plausible information paths.

---

# Example 5 — Positive Opportunity

```text
EVENT:

New regional market opens.

Player Role:
Trader

Current Resources:
Surplus food

Goal:
Expand trade network
```

Result:

```text
Opportunity:
EXCEPTIONAL

Role:
HIGH

Goal:
HIGH

Overall:
HIGH
```

No crisis is required.

---

# Example 6 — Political Relevance

```text
EVENT:

Regional authority proposes
integration with neighboring federation.

Player:
Settlement council representative.
```

Result:

```text
Political:
CRITICAL

Faction:
HIGH

Role:
HIGH

Historical:
HIGH

Overall:
CRITICAL
```

---

# Example 7 — Irrelevant Crisis

```text
EVENT:

Major fuel shortage
in distant region.

Player:
No relationship
No trade
No travel plan
No information channel
```

Result:

```text
Overall:
NONE / BACKGROUND
```

The world still experiences the crisis.

The campaign does not need to.

---

# Relevance Decay Example

Day 1:

```text
Road closure.

Goal:
Travel through road.

Relevance:
CRITICAL
```

Player changes destination.

Day 2:

```text
Goal Relevance:
NONE

Geographic:
REGIONAL

Overall:
LOW
```

The event remains active.

Its campaign meaning changed.

---

# Relevance Amplification Example

Day 1:

```text
Hospital supply shortage.

Player:
No connection.

Relevance:
LOW
```

Day 4:

```text
Player's partner transferred to hospital.

Relationship:
CRITICAL

Relevance:
HIGH / CRITICAL
```

---

# Relevance and Event Clusters

Relevance should normally be assessed at both:

```text
EVENT LEVEL
```

and:

```text
CLUSTER LEVEL
```

Example:

```text
Fuel Crisis Cluster
```

overall relevance may be high.

Individual events:

```text
Fuel price rise:
Moderate

Hospital reserve:
Critical

Agricultural rationing:
Low
```

This allows selective presentation.

---

# Cluster Dominant Relevance

The engine may identify:

```text
Cluster Relevance:
HIGH

Dominant Campaign Thread:
Hospital fuel shortage
```

Other elements remain part of the situation without becoming separate missions.

---

# Relevance Conflict

Different relevance dimensions may pull in opposite directions.

Example:

```text
Player's allied settlement
requests fuel.

Player's family settlement
also needs fuel.
```

Both may have high relevance.

The campaign should preserve the conflict rather than resolve it automatically.

---

# Relevance Collision

Multiple high-relevance events may occur simultaneously.

This is a:

```text
RELEVANCE COLLISION
```

Examples:

- family crisis
- faction demand
- urgent mission
- infrastructure failure

Pacing and Priority must determine presentation without pretending the other events stop existing.

---

# Relevance Does Not Create Urgency

A highly relevant event may be slow.

Example:

```text
Long-term political reform
```

Relevance:

```text
HIGH
```

Urgency:

```text
LOW
```

This distinction supports diverse campaign pacing.

---

# Relevance Does Not Create Severity

Example:

```text
Friend opens bakery.
```

Personal Relevance:

```text
HIGH
```

World Severity:

```text
LOW
```

The campaign can care about ordinary life.

---

# Ordinary-Life Relevance

The Living Campaign Engine should allow high relevance for non-crisis events.

Examples:

```text
Wedding
Birth
New business
Community festival
Election
Return of traveler
Repair completed
School reopening
```

A living campaign requires life beyond emergencies.

---

# Relationship With Story Hooks

Relevance determines:

```text
SHOULD THIS EVENT
ENTER PLAYER ATTENTION?
```

Story Hooks determines:

```text
HOW DOES IT ENTER
PLAYER ATTENTION?
```

---

# Relationship With Mission Generation

Relevance determines:

```text
DOES IT MATTER?
```

Mission Generation determines:

```text
CAN PLAYER ACTION
BECOME A MEANINGFUL RESPONSE?
```

---

# Relationship With Pacing

Relevance determines:

```text
IMPORTANCE
```

Pacing determines:

```text
TIMING
AND
PRESENTATION INTENSITY
```

---

# Minimum Viable Relevance Model

A minimum viable implementation should evaluate:

```text
Geographic Proximity

Relationship Relevance

Goal Relevance

Resource Relevance

Faction Relevance

Historical Relevance

Threat

Opportunity

Timing
```

and produce:

```text
Overall Relevance
Dominant Relevance Path
Explanation
```

Additional dimensions may be introduced later.

---

# Relevance Consistency Rules

## Rule 1

World Significance and Campaign Relevance are separate.

---

## Rule 2

Relevance belongs to the relationship between event and campaign.

---

## Rule 3

Geographic distance alone does not determine relevance.

---

## Rule 4

Close relationships may override physical distance.

---

## Rule 5

Infrastructure dependencies may create long-distance relevance.

---

## Rule 6

Active goals strongly influence relevance.

---

## Rule 7

Player resource dependency influences relevance.

---

## Rule 8

Campaign history should affect future relevance.

---

## Rule 9

Player roles may amplify relevant event types.

---

## Rule 10

Roles should not lock the campaign into one content type.

---

## Rule 11

Threat and Opportunity may coexist.

---

## Rule 12

Positive events may be highly relevant.

---

## Rule 13

High relevance does not automatically mean mission generation.

---

## Rule 14

High relevance does not automatically mean immediate visibility.

---

## Rule 15

Information must plausibly reach the player.

---

## Rule 16

Relevant events may remain hidden.

---

## Rule 17

Relevance may decay over time.

---

## Rule 18

Relevance may increase as Campaign State changes.

---

## Rule 19

Active events should be reevaluated when player context changes.

---

## Rule 20

Campaign Pressure affects presentation, not objective relevance.

---

## Rule 21

Low-significance personal events may be campaign-defining.

---

## Rule 22

High-significance global events may remain background.

---

## Rule 23

The engine should preserve multiple relevance paths for one situation.

---

## Rule 24

Relevance assessments must remain explainable.

---

# Guiding Questions

For every Event Candidate, the engine should be capable of answering:

**How close is this physically?**

**Does it affect someone the player knows?**

**Does it affect something the player depends upon?**

**Does it affect an active goal?**

**Does it affect a faction the player cares about?**

**Does it connect to campaign history?**

**Does the player's role make this especially relevant?**

**Does it threaten something important?**

**Does it create an opportunity?**

**Does it change what the player believes?**

**Does timing make it more important now?**

**Why is the final relevance level what it is?**

These questions determine whether an event belongs in the campaign.

---

# Core Design Principle

Project Ascension should never ask:

```text
WHAT QUEST SHOULD WE GIVE THE PLAYER?
```

before asking:

```text
WHAT DOES THIS PLAYER
ALREADY CARE ABOUT?
```

The strongest campaign events should arise where:

```text
WORLD CHANGE
INTERSECTS
PLAYER CONNECTION
```

That intersection creates meaning.

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
Canon/Systems/Living_Campaign_Engine/Story_Hooks.md
```

At this point the pipeline can answer:

```text
WHAT HAPPENED?

World Event Intake

        ↓

DOES IT MATTER TO THIS PLAYER?

Relevance and Proximity
```

The next question is:

```text
HOW DOES THE PLAYER
EXPERIENCE OR DISCOVER IT?
```

`Story_Hooks.md` should define:

- direct observation
- environmental signals
- character contact
- rumor
- radio
- public notices
- faction intelligence
- discovered evidence
- hook reliability
- hook escalation
- hook duplication
- information gating
- hidden relevance
- hook expiration
- hooks without missions

This is the point where internal simulation begins becoming **actual player experience**.

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial relevance framework established for geographic, social, relationship, economic, infrastructure, political, faction, goal, resource, historical, role, threat, opportunity, knowledge and timing relevance. |