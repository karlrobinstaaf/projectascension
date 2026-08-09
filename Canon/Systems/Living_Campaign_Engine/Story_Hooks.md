# PROJECT ASCENSION
# Story Hooks System

| Field | Value |
|--------|-------|
| System | Living Campaign Engine |
| Document | Story Hooks |
| Location | Canon/Systems/Living_Campaign_Engine/Story_Hooks.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Player Discovery, World Presentation and Campaign Entry Points |
| Last Updated | 2026-08-09 |

> *"The world should show the player that something is happening before it asks them to solve it."*

---

# Purpose

The Story Hooks system defines how relevant World Events become perceivable to the player.

At this stage of the Living Campaign Engine:

```text
WORLD SIMULATION

knows what is happening.

        ↓

WORLD EVENT INTAKE

knows which changes are meaningful.

        ↓

RELEVANCE AND PROXIMITY

knows which changes matter to this player.

        ↓

STORY HOOKS

determines how the player experiences them.
```

Story Hooks are therefore the primary interface between:

```text
SIMULATION
```

and:

```text
PLAYER EXPERIENCE
```

---

# Core Principle

The player should often:

```text
NOTICE THE PROBLEM
```

before anyone:

```text
ASKS THEM TO SOLVE IT
```

This distinction is essential.

Avoid:

```text
NPC:
"Hello traveler.

Our fuel supply is low.

Please collect 10 fuel containers."
```

Prefer:

```text
DAY 1

The normal morning bus does not arrive.

        ↓

DAY 2

Fuel prices rise at the market.

        ↓

DAY 3

A mechanic says deliveries from the north
have stopped.

        ↓

DAY 4

The hospital reduces generator use.

        ↓

DAY 5

A friend working at the hospital says:

"We're getting worried."
```

At this point the player may already decide to act.

No formal mission is required.

---

# Story Hook Definition

A Story Hook is a player-facing manifestation of a meaningful world condition.

Conceptually:

```text
STORY HOOK
=
WORLD EVENT
+
RELEVANCE PATH
+
INFORMATION PATH
+
PRESENTATION
```

A hook does not necessarily contain:

- an objective
- a reward
- a quest giver
- a solution

It communicates that something exists in the world.

---

# Hook Versus Mission

These must remain separate.

```text
STORY HOOK

"Something is happening."
```

versus:

```text
MISSION

"Here is a specific opportunity
for the player to intervene."
```

A Story Hook may never become a Mission.

---

# Hook Versus Information

Not every piece of information is a Story Hook.

Example:

```text
Weather tomorrow:
Rain.
```

This is information.

But:

```text
Unusual rainfall has closed the only road
used by the player's trade partner.
```

may become a Story Hook because it has campaign relevance.

---

# Hook Sources

Story Hooks may reach the player through:

```text
Direct Observation

Environmental Change

Character Contact

Conversation

Rumor

Regional Radio

Public Notice

Faction Intelligence

Authority Communication

Trade Activity

Physical Evidence

Recovered Record

Digital Communication

Travelers

Player Investigation
```

Different historical eras may favor different channels.

---

# Story Hook Categories

The initial system should support:

```text
HOOKS
│
├── Environmental
├── Observational
├── Character
├── Social
├── Informational
├── Institutional
├── Economic
├── Physical Evidence
├── Discovery
├── Consequence
└── Direct Crisis
```

---

# Environmental Hook

Environmental Hooks communicate world change through surroundings.

Examples:

```text
Streetlights remain off.

Market shelves are thinner.

Traffic decreases.

More people carry water containers.

A checkpoint appears.

A previously busy road is empty.

A hospital runs exterior lights at minimum power.
```

The player sees the consequence.

They may not know the cause.

---

# Environmental Storytelling

Environmental Hooks are particularly valuable because they allow:

```text
WORLD STATE
```

to become visible without exposition.

Example:

```text
Supply State:

Fuel = CONSTRAINED
```

may appear as:

```text
Fewer vehicles.

Higher transport prices.

Longer fuel queues.

Farm equipment running fewer hours.
```

---

# Environmental Hook Principle

Prefer:

```text
SHOW CONDITION
```

before:

```text
EXPLAIN CONDITION
```

when plausible.

---

# Observational Hook

An Observational Hook occurs when the player directly witnesses an event.

Examples:

```text
A convoy arrives damaged.

A bridge is blocked.

People are leaving town.

A radio tower stops transmitting.

Security forces close a market.
```

Direct observation usually has:

```text
HIGH INFORMATION CONFIDENCE
```

about what was physically observed.

It may still provide poor information about the cause.

---

# Observation Does Not Reveal Cause

Example:

```text
Player observes:

Fuel station closed.
```

This does not automatically reveal:

```text
WHY
```

Possible causes include:

- no fuel
- equipment failure
- authority restriction
- security problem
- owner decision

Observation is evidence.

Not omniscience.

---

# Character Hook

Character Hooks use known characters to connect world conditions to personal stakes.

Examples:

```text
Friend calls.

Sibling arrives unexpectedly.

Doctor asks whether player has heard the news.

Trader complains about route closures.

Technician appears exhausted.
```

Character Hooks should be strongly influenced by:

```text
Relationship Relevance
```

---

# Character Hook Example

World State:

```text
Medicine:
CONSTRAINED
```

Player Relationship:

```text
Close friend:
Doctor
```

Possible hook:

```text
The doctor messages:

"If you're coming into town,
I need to talk to you."
```

This is stronger than:

```text
SYSTEM:
Medicine shortage detected.
```

---

# Character Perspective

Characters should describe events from their own:

- knowledge
- profession
- beliefs
- priorities
- fears
- relationships

They should not speak from hidden World Simulation truth.

---

# Example Perspectives

Same fuel crisis:

```text
Mechanic:

"Deliveries stopped again."
```

```text
Authority Official:

"We're moving to priority allocation."
```

```text
Farmer:

"I can't run the harvest equipment like this."
```

```text
Trader:

"Fuel's worth more than medicine right now."
```

All may describe the same underlying situation differently.

---

# Social Hook

Social Hooks emerge through general population behavior.

Examples:

```text
Market discussion

Queues

Crowds

Community meeting

Sudden travel demand

Unusual purchasing behavior
```

Population behavior itself becomes information.

---

# Social Proof Hook

Example:

```text
Player sees several families loading vehicles.
```

The player may infer:

```text
Something is wrong.
```

Whether their inference is correct remains an Information State issue.

---

# Rumor Hook

A Rumor Hook communicates unverified information.

Examples:

```text
"They're closing the northern road."

"The hospital has no medicine."

"People from the city are coming south."

"The government lost contact with Richmond."
```

Rumors may be:

```text
TRUE
PARTIALLY TRUE
FALSE
OUTDATED
MISINTERPRETED
UNKNOWN
```

---

# Rumor Principle

The engine should never internally label a rumor to the player as:

```text
FALSE RUMOR
```

unless the player has independently verified it.

Player-facing presentation should preserve uncertainty.

---

# Rumor Source

Rumors should normally have a plausible transmission source.

Examples:

```text
Traveler

Market

Radio operator

Friend of friend

Security officer

Trader

Settlement resident
```

Avoid rumors appearing from nowhere.

---

# Rumor Mutation

A Story Hook may change as information moves.

Example:

```text
ORIGINAL EVENT

Fuel delivery delayed.
```

becomes:

```text
REPORT

Fuel delivery may not arrive this week.
```

becomes:

```text
RUMOR

There won't be any more fuel.
```

The campaign may expose several stages.

---

# Informational Hook

Informational Hooks use communication channels.

Examples:

```text
Radio report

Message

Newspaper

Public network

Emergency broadcast

Bulletin
```

Their reliability depends upon Information State.

---

# Radio Hook

Radio becomes especially important during:

```text
WS-03 — The Fractured World
```

Possible radio content includes:

- weather
- route reports
- trade information
- missing persons
- emergency announcements
- political news
- regional conditions

---

# Scheduled Information

Some information channels may appear at predictable times.

Example:

```text
Regional radio bulletin:
07:00
19:00
```

This creates world routine.

The player may choose whether to listen.

---

# Institutional Hook

Institutional Hooks come from:

- authorities
- factions
- organizations
- communities
- corporations
- military

Examples:

```text
Public notice

Emergency bulletin

Council announcement

Faction message

Official request
```

---

# Authority Communication

Authority Hook reliability should reflect:

```text
Authority Knowledge
+
Information Reliability
+
Institutional Trust
```

An official statement may be honest yet wrong.

---

# Faction Intelligence

Known factions may share restricted information.

Example:

```text
Trade Network message:

"Do not use Route 7 after sunset."
```

Access may depend upon:

- faction trust
- reputation
- membership
- role

---

# Economic Hook

Economic conditions may reveal world changes.

Examples:

```text
Price increase

Missing goods

Unusual demand

Trade route shifts

Merchant arrivals

Merchant absence

Barter preference changes
```

---

# Economic Hook Example

World State:

```text
Medicine Supply:
STRAINED
```

Possible presentation:

```text
Yesterday:

Antibiotics:
20 trade credits

Today:

Antibiotics:
35 trade credits
```

The player may notice the system changing without being explicitly told.

---

# Physical Evidence Hook

Players may encounter evidence of events that occurred earlier.

Examples:

```text
Abandoned convoy

Burned checkpoint

Damaged infrastructure

Empty settlement

Emergency markings

Discarded equipment
```

The event may already be resolved.

The hook reveals its history.

---

# Evidence Reliability

Physical evidence may be highly reliable about:

```text
WHAT IS PRESENT
```

but ambiguous about:

```text
WHAT HAPPENED
```

Example:

```text
Abandoned vehicles
```

do not automatically prove:

```text
attack
```

They may result from:

- fuel shortage
- evacuation
- mechanical failure

---

# Discovery Hook

Discovery Hooks reveal previously unknown locations, systems, actors or information.

Examples:

```text
New radio signal

Hidden facility

Unknown settlement

Recovered archive

New trade route

Previously isolated community
```

---

# Discovery Versus Creation

The system must preserve:

```text
THE PLAYER DISCOVERED IT
```

rather than:

```text
IT APPEARED BECAUSE
THE PLAYER NEEDED CONTENT
```

The world object should already exist or emerge causally through simulation.

---

# Consequence Hook

Player actions may later become visible through consequences.

Example:

```text
PLAYER:
Restores bridge.
```

Later:

```text
More traders arrive.

Market prices fall.

An old friend reaches town.

Regional authority publicly credits the repair.
```

These are Consequence Hooks.

---

# Hidden Consequence Hook

A player action may produce an unexpected effect.

Example:

```text
Player redirects fuel to hospital.
```

Weeks later:

```text
Farmers report reduced harvest output.
```

The hook reveals a consequence that existed in World Simulation before the player knew it.

---

# Direct Crisis Hook

Direct Crisis occurs when world events reach the player's immediate environment.

Examples:

```text
Building loses power.

Convoy is attacked nearby.

Flood reaches settlement.

Authority seals district.

Large migrant group arrives.
```

These may bypass gradual presentation because the event itself is immediate.

---

# Direct Crisis Is Not Always Mission

Example:

```text
Storm arrives.
```

Player response may simply be:

```text
Find shelter.
```

No formal mission structure is required.

---

# Hook Visibility Ladder

Relevant events may progress through levels of visibility.

```text
LEVEL 0
Hidden

LEVEL 1
Subtle Signal

LEVEL 2
Noticeable Pattern

LEVEL 3
Explicit Information

LEVEL 4
Personal Connection

LEVEL 5
Actionable Situation

LEVEL 6
Direct Crisis
```

---

# Level 0 — Hidden

The event has relevance but no plausible information path has reached the player.

Example:

```text
Player's sibling evacuated
from distant city.
```

The player does not yet know.

---

# Level 1 — Subtle Signal

Small environmental or behavioral signs.

Example:

```text
Fuel prices increase slightly.
```

---

# Level 2 — Noticeable Pattern

Several signals begin forming a pattern.

Example:

```text
Fewer buses.

Longer queues.

Trader delayed.

Fuel prices rising.
```

---

# Level 3 — Explicit Information

The player receives direct information.

Example:

```text
Regional radio:

"Fuel distribution restrictions
begin tomorrow."
```

---

# Level 4 — Personal Connection

The situation affects someone or something personally important.

Example:

```text
Friend says hospital generators
are being rationed.
```

---

# Level 5 — Actionable Situation

The player recognizes a plausible intervention.

Example:

```text
An alternate fuel depot may still have reserves.
```

No request is necessary.

---

# Level 6 — Direct Crisis

The problem directly confronts the player.

---

# Visibility Does Not Always Progress Linearly

An event may begin immediately at:

```text
LEVEL 6
```

Example:

```text
Earthquake.
```

Another may remain at:

```text
LEVEL 1
```

for months.

---

# Hook Escalation

Hooks should evolve with the underlying world event.

Example:

```text
WORLD EVENT:
Fuel Crisis

Day 1:
Price increase.

Day 3:
Radio report.

Day 4:
Friend complains.

Day 6:
Hospital cuts generator use.

Day 7:
Direct request.
```

The escalation should reflect actual world change.

---

# No Artificial Escalation

Avoid:

```text
The hook becomes more dramatic
because the player ignored it.
```

unless World Simulation itself worsened.

The system must not punish non-engagement through arbitrary narrative escalation.

---

# Player-Initiated Escalation

The player may accelerate discovery.

Example:

```text
Subtle Hook:
Fuel price increase.
```

Player chooses:

```text
Ask mechanic.
```

This may reveal:

```text
Explicit Information
```

earlier than passive hook progression would.

---

# Player-Created Mission

This is a central Living Campaign Engine principle.

Example:

```text
HOOK:

Hospital reducing power use.
```

No mission exists.

Player says:

```text
"I want to find out why."
```

The campaign should allow:

```text
PLAYER INVESTIGATION
      ↓
NEW INFORMATION
      ↓
ACTIONABLE SITUATION
```

The player has effectively created their own objective.

---

# Self-Directed Action

A player should be able to act on:

- observation
- rumor
- curiosity
- concern
- opportunity

without waiting for:

```text
QUEST ACCEPTED
```

This is essential to systemic play.

---

# Hook Reliability

Every Story Hook should preserve information characteristics.

Conceptually:

```text
HOOK INFORMATION

Source
Reliability
Verification
Age
Confidence
Perspective
```

---

# Example

```text
Hook:
"The northern bridge is closed."

Source:
Traveler

Reliability:
Moderate

Age:
18 hours

Verification:
Unverified
```

The player decides whether to trust it.

---

# Direct Observation Reliability

Direct observation generally provides strong confidence about immediate facts.

Example:

```text
Player sees bridge destroyed.
```

High confidence:

```text
Bridge is physically impassable.
```

But not necessarily:

```text
Who destroyed it.
```

---

# Hook Information Age

Story Hooks should preserve time.

Example:

```text
Radio report:
Road open.

Report Age:
3 days.
```

Current reliability may be low even if the original report was accurate.

---

# Conflicting Hooks

The player may receive contradictory hooks.

Example:

```text
Radio:
Route 8 open.

Trader:
Route 8 closed.

Security officer:
Route 8 open only during daylight.
```

This should generate uncertainty rather than automatically resolve it.

---

# Contradiction as Gameplay

Conflicting information may create:

- investigation
- caution
- alternate planning
- relationship decisions

The system should allow ambiguity to become meaningful gameplay.

---

# Hook Provenance

Where useful, the system should preserve how information traveled.

Example:

```text
EVENT

Bridge closes.

        ↓

Regional Authority

        ↓

Radio Operator

        ↓

Trader

        ↓

Player
```

Each step may affect information quality.

---

# Hidden High-Relevance Events

`Relevance_and_Proximity.md` allows:

```text
HIDDEN HIGH RELEVANCE
```

Story Hooks must handle these carefully.

Example:

```text
Player's sibling is in danger.

No communication available.
```

The engine should search only plausible information paths.

It must not create:

```text
Convenient stranger
magically knows everything.
```

---

# Information Path Search

Possible paths include:

```text
Direct communication

Shared contact

Faction network

Regional radio

Traveler

Courier

Public notice

Physical evidence

Player travel
```

If no path exists:

```text
THE PLAYER REMAINS UNAWARE
```

even if the event is critical.

---

# Delayed Discovery

A high-relevance event may be discovered long afterward.

Example:

```text
Event:
Character disappeared six months ago.

Discovery:
Player finds their journal today.
```

The event can still become campaign-relevant.

---

# Hook Timing

Hook timing depends upon:

```text
Event Urgency
Information Speed
Player Location
Information Channel
Pacing
```

---

# Natural Delay

Example:

```text
Distant settlement crisis

Courier travel:
5 days
```

The hook should not arrive instantly unless another faster channel exists.

---

# Relevance Versus Delivery

High relevance increases the desirability of delivery.

It does not create impossible communication.

```text
RELEVANCE
≠
TELEPORTATION OF INFORMATION
```

---

# Multiple Hooks from One Event

One world event may generate multiple hooks.

This is useful when they reveal different aspects.

Example:

```text
Fuel Crisis

Environmental:
Fewer vehicles.

Economic:
Fuel price rises.

Character:
Mechanic complains.

Institutional:
Rationing notice.
```

---

# Duplicate Hook Prevention

Multiple hooks should not simply repeat identical information.

Avoid:

```text
NPC A:
Fuel is low.

NPC B:
Fuel is low.

Radio:
Fuel is low.

Notice:
Fuel is low.
```

Prefer each hook to add:

```text
NEW INFORMATION
NEW PERSPECTIVE
NEW PERSONAL CONNECTION
or
NEW ACTIONABILITY
```

---

# Hook Diversity

A Story Situation should ideally use varied hook channels where appropriate.

Example:

```text
First:
Environmental

Second:
Social

Third:
Character
```

This makes the world feel responsive rather than mechanically repetitive.

---

# Hook Saturation

The engine should track repeated exposure.

If the player already clearly understands:

```text
Fuel shortage exists.
```

additional hooks should not repeatedly explain the same fact.

They should advance the situation.

---

# Information Saturation Rule

Once a fact is established:

```text
REPEAT ONLY IF
```

- source difference matters
- reliability matters
- perspective matters
- state changed
- emotional meaning changed

---

# Hook Novelty

A hook should ideally add at least one of:

```text
NEW FACT

NEW SOURCE

NEW PERSPECTIVE

NEW CONSEQUENCE

NEW OPPORTUNITY

NEW THREAT

NEW PERSONAL CONNECTION
```

---

# Hook Lifecycle

Story Hooks should maintain lifecycle state.

Conceptually:

```text
POTENTIAL
AVAILABLE
DELIVERED
NOTICED
INVESTIGATED
ACTED UPON
IGNORED
EXPIRED
SUPERSEDED
```

---

# Potential

The engine has identified a possible hook but it has not yet entered the player's environment.

---

# Available

Conditions allow the hook to appear.

Example:

```text
Player enters market.
```

Environmental fuel-queue hook becomes available.

---

# Delivered

The information or observation reaches the player.

---

# Noticed

Where gameplay supports it, the player actually registers the hook.

Not every environmental detail needs guaranteed attention.

---

# Investigated

The player actively seeks more information.

---

# Acted Upon

The player takes meaningful action because of the hook.

---

# Ignored

The player had opportunity to engage but did not.

Underlying world event continues.

---

# Expired

The hook can no longer occur.

Example:

```text
Trader leaves town.
```

---

# Superseded

A stronger or more current hook makes the old one unnecessary.

Example:

```text
Rumor:
Fuel shortage possible.

Later:

Official rationing begins.
```

The rumor is superseded.

---

# Hook Expiration

Hooks should expire naturally.

Examples:

```text
Traveler leaves.

Notice becomes outdated.

Rumor disproven.

Opportunity closes.

Player leaves region.
```

Expired hook does not mean underlying event resolved.

---

# Persistent Hooks

Some world conditions may provide recurring environmental manifestations.

Example:

```text
Long-term fuel rationing.
```

The engine should treat this as:

```text
WORLD BASELINE
```

rather than repeatedly delivering a formal Story Hook.

---

# Baseline Environmental State

Long-term conditions may become environmental normality.

Examples:

```text
Scheduled electricity.

Regional radio.

Fuel rationing.

Checkpoint inspections.
```

Players experience them through ordinary world behavior rather than repeated exposition.

---

# Hook Intensity

Hooks may possess presentation intensity.

Conceptually:

```text
SUBTLE
NOTICEABLE
EXPLICIT
PERSONAL
URGENT
```

Intensity should relate to:

- relevance
- event state
- information path
- pacing

---

# Subtle

Example:

```text
Prices slightly higher.
```

---

# Noticeable

Example:

```text
Several shops closed.
```

---

# Explicit

Example:

```text
Official announcement.
```

---

# Personal

Example:

```text
Friend affected.
```

---

# Urgent

Example:

```text
Direct warning:
"Leave now."
```

---

# Intensity Is Not Relevance

A highly relevant event may initially appear subtly.

Example:

```text
Player's family settlement
is beginning to experience water pressure.
```

Initial hook:

```text
A relative casually mentions
the taps have been unreliable.
```

Relevance:

```text
HIGH
```

Presentation intensity:

```text
SUBTLE
```

---

# Hook Tone

Presentation should reflect the world and source.

Examples:

```text
Institutional:
Formal

Friend:
Personal

Trader:
Practical

Rumor:
Uncertain

Environmental:
Nonverbal
```

The engine should not make every hook sound like a quest briefing.

---

# No Quest Language Requirement

Avoid generated dialogue such as:

```text
"I need you to travel to Location A,
retrieve Item B,
and return for your reward."
```

unless the character would naturally speak that way.

Prefer:

```text
"We're almost out.

There used to be a depot east of here.

I don't know if anything's left."
```

The player can decide what to do.

---

# Implicit Objectives

Story Hooks may imply possible action without formalizing it.

Example:

```text
"The radio relay stopped working yesterday."
```

Possible player interpretation:

```text
Investigate relay.
```

The game does not need to declare:

```text
OBJECTIVE ADDED.
```

---

# Explicit Requests

Some situations naturally justify direct requests.

Example:

```text
Authority:
"We need someone to escort the medical shipment."
```

This is valid.

The distinction is that the request emerges from a real systemic need.

---

# Character Motivation Requirement

When a character delivers a hook, the engine should know:

```text
WHY THIS CHARACTER
IS SHARING THIS INFORMATION.
```

Possible motives include:

- asking for help
- warning player
- seeking reassurance
- trade
- gossip
- duty
- manipulation
- friendship

---

# Character Knowledge Requirement

The character may only communicate what they plausibly know.

Example:

```text
Farmer
```

should not casually know:

```text
national classified infrastructure telemetry
```

unless a plausible information path exists.

---

# Perspective Preservation

Different characters may interpret the same event differently.

This is desirable.

Example:

```text
Regional Authority:

"Temporary supply stabilization measures."
```

```text
Trader:

"They're rationing because the route's broken."
```

```text
Resident:

"They're hiding how bad it is."
```

The campaign should not immediately tell the player which interpretation is correct.

---

# Emotional Hook

Some hooks matter primarily because of emotional relationships.

Examples:

```text
Friend misses meeting.

Parent sounds frightened.

Partner becomes distant.

Old rival asks for help.
```

These may connect to World Events indirectly.

---

# Ordinary-Life Hooks

Story Hooks should not be limited to crisis.

Examples:

```text
Wedding invitation

Market reopening

Festival announced

New child born

Friend starts business

School reopens

Trade caravan arrives

Community election begins
```

These help transform World Simulation into a world worth caring about.

---

# Recovery Hooks

Recovery should become visible.

Examples:

```text
Streetlights return.

Market shelves refill.

Train arrives for first time in years.

Radio reconnects to another region.

Hospital reopens ward.
```

Players should feel the consequences of improvement.

---

# Development Hooks

Later campaigns may surface:

```text
New construction

Political reform

Technology projects

Expanding trade

New settlements

Infrastructure upgrades
```

The world should visibly build itself.

---

# Quiet Hooks

Not every hook needs consequence.

Example:

```text
A repaired fountain works again.
```

This may simply communicate:

```text
THE WORLD IS HEALING.
```

Such signals matter emotionally.

---

# Butterfly Hooks

The legacy `Overview.md` referenced:

```text
Butterfly Engine
```

The useful concept should be retained within current architecture.

Small earlier changes may produce distant later hooks.

Example:

```text
Player helps displaced engineer.

Six months later:

Engineer restores regional radio link.
```

Later hook:

```text
Player hears first broadcast
from distant region.
```

The effect should arise through:

```text
Consequence Propagation
+
World Simulation
+
Story Hooks
```

A separate Butterfly Engine may therefore not be necessary unless later design proves otherwise.

---

# World Ledger Hooks

Historical events recorded in a future World Ledger may become discoverable through:

- archives
- conversations
- memorials
- records
- historical sites

These are retrospective Story Hooks.

Example:

```text
Player discovers marker:

"47 people died here
during the Winter Closure."
```

The world remembers its past.

---

# Hook Selection

When multiple hook options exist, selection should consider:

```text
Dominant Relevance Path
Player Location
Information Availability
Relationship Context
Novelty
Pacing
Presentation Variety
```

---

# Example Selection

Event:

```text
Hospital Fuel Crisis
```

Relevance:

```text
Dominant:
Relationship

Secondary:
Resource
```

Possible hooks:

```text
Radio announcement
Fuel queue
Friend at hospital
```

Preferred:

```text
Friend at hospital
```

because it best reflects dominant relevance.

---

# Hook Escalation Logic

Conceptually:

```text
EVENT ACTIVE
      ↓
AVAILABLE HOOKS
      ↓
SELECT PRESENTATION
      ↓
PLAYER RECEIVES SIGNAL
      ↓
PLAYER RESPONSE?
      │
      ├── Investigates
      │      ↓
      │   More information
      │
      ├── Acts
      │      ↓
      │   Player intervention
      │
      └── Ignores
             ↓
          World continues
```

---

# No Forced Escalation

If the player ignores:

```text
"Fuel prices rising."
```

the system should not automatically create:

```text
Friend suddenly needs fuel.
```

unless World Simulation and relationships justify it.

---

# Natural Escalation

If the underlying Fuel Crisis worsens and the hospital becomes affected:

```text
Friend at hospital
```

may naturally become involved.

This is valid escalation.

---

# Player Investigation

When the player investigates a hook, the engine should query:

```text
Information State
World State
Characters
Factions
Locations
```

to determine what can plausibly be learned.

---

# Investigation Depth

Possible progression:

```text
SURFACE

"What is happening?"
```

```text
CAUSE

"Why is it happening?"
```

```text
SYSTEM

"What else does it affect?"
```

```text
ACTORS

"Who benefits or suffers?"
```

```text
OPTIONS

"What could be done?"
```

The player determines how deep to investigate.

---

# Investigation Does Not Guarantee Truth

Sources may still be:

- wrong
- deceptive
- outdated
- incomplete

Player effort improves information access.

It does not magically reveal simulation truth.

---

# Hook-to-Mission Boundary

A hook becomes eligible for Mission Generation when:

```text
Player intervention is plausible
+
Meaningful outcome can change
+
Action window exists
```

But eligibility does not require conversion.

---

# Missionless Resolution

Many hooks should resolve without missions.

Example:

```text
Rumor:
Bridge may close.
```

Later:

```text
Bridge remains open.

Rumor fades.
```

or:

```text
Authority repairs issue.
```

Player never intervenes.

The world handled itself.

---

# Self-Directed Resolution

Player may resolve situation without a mission.

Example:

```text
Player hears market rumor.

Player visits depot.

Player negotiates fuel purchase.

World State changes.
```

Mission Generator may never have been invoked.

This is a successful Living Campaign outcome.

---

# Hook Clustering

Hooks tied to one Event Cluster should preserve that connection.

Example:

```text
Northern Valley Fuel Crisis

Hook 1:
Fuel price increase

Hook 2:
Radio rationing notice

Hook 3:
Hospital friend warning
```

All reference:

```text
Same Story Situation
```

---

# Hook Cross-Pollination

One hook may reveal another Event Cluster.

Example:

```text
Trader discusses fuel shortage.
```

During conversation:

```text
mentions armed checkpoints
on northern route.
```

This may introduce a Security situation.

The world should feel interconnected.

---

# Story Situation Assembly

Multiple hooks may help construct a Story Situation.

Example:

```text
HOOK A

Fuel prices rise.

HOOK B

Friend at hospital worried.

HOOK C

Authority starts rationing.

        ↓

PLAYER UNDERSTANDS:

Regional fuel crisis.
```

The player's mental model emerges gradually.

---

# Player Understanding State

Where useful, Campaign State may track whether the player:

```text
UNAWARE

SUSPECTS

AWARE

UNDERSTANDS

DEEPLY INFORMED
```

about a Story Situation.

This should not replace individual knowledge entries.

It is a campaign presentation aid.

---

# Hook Resolution Feedback

After a player response:

```text
STORY HOOK
      ↓
PLAYER ACTION
      ↓
WORLD SIMULATION
      ↓
NEW STATE
      ↓
NEW HOOK
```

Example:

```text
Player repairs radio tower.
```

Later:

```text
First distant transmission arrives.
```

The world visibly acknowledges action.

---

# Consequence Visibility

Not every consequence should be shown immediately.

But meaningful actions should eventually produce understandable evidence where plausible.

Otherwise player agency becomes invisible.

---

# Feedback Principle

Important player actions should create:

```text
VISIBLE CONSEQUENCES
```

where the world permits them.

This may occur through:

- characters
- environment
- prices
- infrastructure
- news
- reputation
- population behavior

---

# Story Hook Update Cycle

A conceptual cycle:

```text
1. Read relevant Event Candidates.

2. Read Relevance Vector.

3. Read Campaign State.

4. Check player knowledge.

5. Check Information State.

6. Find plausible information paths.

7. Generate possible hook channels.

8. Remove impossible hooks.

9. Remove duplicate hooks.

10. Evaluate hook novelty.

11. Evaluate current campaign pacing.

12. Select presentation type.

13. Assign hook intensity.

14. Deliver or stage hook.

15. Track whether player notices.

16. Process player investigation.

17. Process player action.

18. Update hook lifecycle.

19. Supersede outdated hooks.

20. Generate consequence hooks where appropriate.
```

---

# Story Hook Output

Conceptually:

```text
STORY HOOK

Hook ID:
SH-2045-0041

Source Event:
WEC-2045-00142

Story Situation:
Northern Valley Fuel Crisis

Hook Type:
Character

Character:
Mara Vale

Relevance Path:
Relationship

Information:
Hospital generator fuel
below expected reserve.

Reliability:
High

Verification:
Direct professional knowledge

Information Age:
2 hours

Intensity:
Personal

Urgency:
High

Lifecycle:
Available

Possible Player Responses:

Ask for details
Offer help
Ignore
Investigate independently
Contact authority
Seek fuel
```

The system should not require these to become explicit menu options.

They describe possible interaction paths.

---

# Environmental Hook Output

```text
STORY HOOK

Hook ID:
SH-2045-0042

Source Event:
WEC-2045-00142

Type:
Environmental

Presentation:

Three of the six regional buses
scheduled for the morning route
do not arrive.

Relevance Path:
Geographic / Resource

Reliability:
Direct Observation

Intensity:
Subtle

Player Understanding:
Unknown cause
```

---

# Rumor Hook Output

```text
STORY HOOK

Hook ID:
SH-2045-0043

Source Event:
WEC-2045-00142

Type:
Rumor

Source:
Market trader

Content:
"North route's finished.
No fuel's coming through."

Reliability:
Unknown

Truth State:
Internal Only

Information Age:
Unknown

Intensity:
Noticeable
```

The player does not see:

```text
Truth State
```

---

# Story Hook Minimum Data

A minimum viable Story Hook should contain:

```text
Hook ID
Source Event / Cluster
Hook Type
Information Source
Information Content
Reliability
Information Age
Relevance Path
Intensity
Lifecycle
Expiration
```

where appropriate.

---

# Minimum Viable Hook System

A minimum implementation should support:

```text
Environmental Hooks

Direct Observation

Character Hooks

Rumors

Radio / Information

Institutional Communication

Physical Evidence

Discovery

Direct Crisis
```

and must be capable of:

```text
information gating
hook escalation
duplicate suppression
hook expiration
player investigation
missionless resolution
```

---

# Story Hook Consistency Rules

## Rule 1

Story Hooks present world conditions; they do not create world truth.

---

## Rule 2

Relevant events do not automatically become visible.

---

## Rule 3

Information must travel through plausible channels.

---

## Rule 4

The player may remain unaware of highly relevant events.

---

## Rule 5

Environmental signals should often precede explicit explanation.

---

## Rule 6

Direct observation does not automatically reveal causation.

---

## Rule 7

Characters may only communicate information they plausibly possess.

---

## Rule 8

Characters should speak from their own perspective.

---

## Rule 9

Rumors may be true, false, partial, outdated or unknown.

---

## Rule 10

Contradictory information is valid.

---

## Rule 11

Multiple hooks should not simply repeat identical information.

---

## Rule 12

Each repeated hook should ideally add new meaning.

---

## Rule 13

One Event Cluster may generate several perspectives without becoming several unrelated quests.

---

## Rule 14

Hooks may escalate only when world conditions or player investigation justify escalation.

---

## Rule 15

Ignoring a hook does not freeze the world.

---

## Rule 16

Ignoring a hook should not arbitrarily worsen the event.

---

## Rule 17

Players may act before a formal mission exists.

---

## Rule 18

Players may create their own objectives from world observation.

---

## Rule 19

Many Story Hooks should never become Missions.

---

## Rule 20

Positive developments should generate Story Hooks.

---

## Rule 21

Ordinary-life events may be campaign-relevant.

---

## Rule 22

Recovery should be visible.

---

## Rule 23

Persistent conditions should eventually become baseline rather than repeated exposition.

---

## Rule 24

Player actions should produce visible world feedback where plausible.

---

## Rule 25

Information age should matter.

---

## Rule 26

Hook tone should reflect its source.

---

## Rule 27

Story Hooks should avoid artificial quest language.

---

## Rule 28

Story Hooks must remain traceable to world causes.

---

# Guiding Questions

For every Story Hook, the engine should be capable of answering:

**What World Event caused this?**

**Why does it matter to the player?**

**How could the player plausibly encounter it?**

**Who knows about it?**

**How did they learn it?**

**How old is the information?**

**How reliable is it?**

**What does the player actually perceive?**

**What remains unknown?**

**Does this hook add something new?**

**Could the player investigate further?**

**Could the player act without receiving a mission?**

**What happens if the player ignores it?**

If these questions cannot be answered, the hook is probably artificial.

---

# Core Design Principle

Project Ascension should strive for:

```text
THE WORLD SHOWS SOMETHING.

THE PLAYER NOTICES.

THE PLAYER BECOMES CURIOUS.

THE PLAYER DECIDES IT MATTERS.

THE PLAYER ACTS.
```

rather than:

```text
THE GAME TELLS THE PLAYER:

THIS IS YOUR NEXT QUEST.
```

The difference is the difference between:

```text
PLAYING THROUGH CONTENT
```

and:

```text
LIVING INSIDE A WORLD.
```

---

# Living Campaign Pipeline

With Story Hooks established:

```text
WORLD SIMULATION

"What is happening?"

        ↓

WORLD EVENT INTAKE

"What changed enough to matter?"

        ↓

RELEVANCE AND PROXIMITY

"Does it matter to this player?"

        ↓

STORY HOOKS

"How does the player experience it?"

        ↓

PLAYER

"Do I care?"

        ↓

PLAYER RESPONSE

Ignore
Observe
Investigate
Act
Discuss
Prepare

        ↓

MISSION GENERATION
if appropriate

        ↓

WORLD CONSEQUENCE
```

The critical change occurs here:

```text
THE PLAYER
```

enters the loop before:

```text
MISSION GENERATION.
```

---

# Architectural Result

The Living Campaign Engine now supports a player discovering a problem and acting on it before any explicit quest exists.

This means:

```text
PLAYER CURIOSITY
```

can become a legitimate campaign driver.

That principle should remain central to Project Ascension.

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
Canon/Systems/Living_Campaign_Engine/Mission_Generation.md
```

But Mission Generation must now follow an important constraint established here:

```text
MISSION GENERATION
IS NOT THE DEFAULT ENDPOINT
OF A STORY HOOK.
```

It should only occur when:

```text
A meaningful situation exists

+

Player intervention is possible

+

Player action could alter an outcome

+

There is a plausible reason
for the player to become involved.
```

`Mission_Generation.md` should therefore define:

- player-created missions
- NPC-requested missions
- faction missions
- emergency objectives
- opportunity objectives
- investigation objectives
- mission scope
- mission timing
- multiple solutions
- partial success
- changing objectives
- world-resolved missions
- mission expiration
- mission transformation
- missionless player intervention

The fundamental question must not be:

```text
WHAT QUEST DO WE GENERATE?
```

It must be:

```text
IS A MISSION EVEN NECESSARY?
```

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial Story Hook framework established for environmental presentation, direct observation, characters, rumors, information channels, physical evidence, discovery, information gating, hook escalation, player investigation and self-directed action. |