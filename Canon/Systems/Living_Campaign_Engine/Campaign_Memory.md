# PROJECT ASCENSION
# Campaign Memory System

| Field | Value |
|--------|-------|
| System | Living Campaign Engine |
| Document | Campaign Memory |
| Location | Canon/Systems/Living_Campaign_Engine/Campaign_Memory.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Long-Term Campaign Continuity, Meaningful History and Memory Persistence |
| Last Updated | 2026-08-09 |

> *"The world remembers what happened. The campaign remembers why it still matters."*

---

# Purpose

The Campaign Memory system defines what information from past campaign history must remain available because it may influence future:

- relationships
- characters
- factions
- reputation
- obligations
- Story Hooks
- player goals
- political decisions
- opportunities
- conflicts
- regional identity
- narrative continuity

Campaign Memory does not attempt to preserve every event forever.

Its purpose is to identify:

```text
WHAT MUST REMAIN MEANINGFUL
```

after immediate state and recent-event context have passed.

---

# Core Distinction

The system must separate:

```text
WORLD LEDGER
```

from:

```text
CAMPAIGN MEMORY
```

Conceptually:

```text
WORLD LEDGER
=
WHAT HAPPENED
```

while:

```text
CAMPAIGN MEMORY
=
WHAT STILL MATTERS
TO THIS CAMPAIGN
```

---

# Example

World Ledger may contain:

```text
2041-07-14

Bridge restored across South Fork.
```

Campaign Memory may contain:

```text
Player led restoration.

Settlement A remembers player
as reliable during the crisis.

Mara's family was able to return
because the bridge reopened.
```

The factual event and its campaign meaning are related but not identical.

---

# Memory Is Selective

The campaign should not remember everything at equal resolution.

Avoid:

```text
EVERY PURCHASE
EVERY CONVERSATION
EVERY DOOR OPENED
EVERY MINOR NPC INTERACTION
```

Instead preserve events with likely future significance.

---

# Memory Principle

A memory should normally exist because at least one of these is true:

```text
A relationship changed.

A promise was made.

A promise was broken.

A major decision was made.

A significant consequence occurred.

A character's life changed.

A faction relationship changed.

A major discovery occurred.

A regional state changed.

A player-created role was reinforced.

A historical event became personally meaningful.

An unresolved obligation remains.

A future decision may depend upon the history.
```

---

# Campaign Memory Structure

Conceptually:

```text
CAMPAIGN MEMORY
│
├── Player Decisions
├── Promises and Obligations
├── Relationship Milestones
├── Character History
├── Faction History
├── Reputation History
├── Mission Outcomes
├── Consequence History
├── Discoveries
├── Regional History
├── Political History
├── Conflict History
├── Opportunity History
├── Place Memory
├── Artifact / Record Memory
└── Turning Points
```

---

# Memory Entry

A Campaign Memory entry should conceptually contain:

```text
MEMORY ENTRY

Memory ID
Date
Location
Type
Actors
Subject
Event
Player Involvement
Outcome
Meaning
Known By
Emotional Weight
Political Weight
Relationship Weight
Future Relevance
Persistence
Source References
Current Status
```

---

# Memory ID

Example:

```text
MEM-2041-0042
```

Stable IDs allow:

- character references
- relationship references
- Story Hook callbacks
- debugging
- causal history
- World Ledger linking

---

# Memory Type

Initial Memory Types may include:

```text
DECISION
PROMISE
OBLIGATION
RELATIONSHIP
CHARACTER
FACTION
REPUTATION
MISSION
CONSEQUENCE
DISCOVERY
REGIONAL
POLITICAL
CONFLICT
OPPORTUNITY
PLACE
HISTORICAL
TURNING_POINT
```

The taxonomy should remain compact.

---

# Player Decision Memory

Major player decisions should be preserved when they alter:

```text
World State
Relationships
Reputation
Faction Relationships
Character Lives
Future Options
```

Example:

```text
Player allocated emergency fuel
to hospital rather than farms.
```

Memory should preserve more than:

```text
Fuel Choice = Hospital
```

It should preserve context.

---

# Decision Context

Conceptually:

```text
Decision:
Hospital received fuel.

Alternatives:
Farm Cooperative
Transport Authority

Known Conditions:
Hospital reserve critical.
Harvest at risk.

Player Reason:
May be unknown unless expressed.

Outcome:
Hospital remained operational.
Farm output later decreased.
```

This context allows meaningful future references.

---

# Player Intent

Where player intent is explicitly known, it may be remembered.

Example:

```text
Player said:
"I promised Mara I'd keep the hospital running."
```

This may give the decision additional relational meaning.

The system should not invent intent if none was expressed.

---

# Promise Memory

Promises are strong memory candidates.

Examples:

```text
"I'll come back."

"I'll find your brother."

"I'll repay you."

"I won't tell anyone."

"I'll support your proposal."
```

---

# Promise State

Conceptually:

```text
OPEN
FULFILLED
BROKEN
RELEASED
IMPOSSIBLE
FORGOTTEN_BY_ACTOR
```

---

# Open Promise

An unresolved promise should remain active in:

```text
Campaign State
```

and Campaign Memory.

---

# Fulfilled Promise

Fulfillment may become a positive relationship memory.

Example:

```text
Player promised to return
before winter.

Player returned.
```

---

# Broken Promise

A broken promise may affect:

```text
Trust
Reputation
Future Requests
Relationship Tone
```

But only for actors who know the promise was broken.

---

# Impossible Promise

World conditions may make fulfillment impossible.

Example:

```text
Player promised to rescue character.

Character dies before player can reach them.
```

This is not automatically:

```text
PLAYER BETRAYAL.
```

Character interpretation matters.

---

# Obligation Memory

Not all obligations are promises.

Examples:

```text
Debt

Favor

Contract

Political commitment

Faction duty

Family responsibility
```

These may remain relevant for long periods.

---

# Relationship Milestone

Important relationship developments should be preserved.

Examples:

```text
First meeting

First major act of trust

Conflict

Reconciliation

Romantic development

Betrayal

Rescue

Separation

Reunion

Death
```

---

# Relationship Memory

A relationship should not be represented only as:

```text
Trust = 72
```

It should retain major historical reasons.

Example:

```text
Mara trusts player because:

- Player protected clinic during 2038 flood.
- Player kept confidential information in 2039.
- Player broke delivery promise in 2041.
```

The current relationship emerges from history.

---

# Memory Contradiction

Relationships may contain conflicting memories.

Example:

```text
Player saved character's family.

Player later supported political rival.
```

Both remain true.

Characters may feel:

```text
gratitude
+
resentment
```

simultaneously.

---

# Character History

Campaign Memory should preserve major life changes of important characters.

Examples:

```text
Changed profession

Moved settlement

Joined faction

Left faction

Married

Had child

Lost family member

Became leader

Was injured

Recovered

Disappeared

Returned
```

---

# Character Continuity

When the player meets a character years later, Campaign Memory should help explain:

```text
WHO THEY HAVE BECOME
```

since the last encounter.

---

# Example

Last meeting:

```text
2038

Elias:
Young farmer
```

Player returns:

```text
2044

Elias:
Regional agricultural coordinator
```

Memory references may contain:

```text
Expanded cooperative

Led winter rationing

Lost brother during 2041 storm

Joined Valley Council
```

The character has lived between encounters.

---

# Faction History

Important faction events may become Campaign Memory.

Examples:

```text
Alliance formed

Leadership changed

Treaty signed

Treaty broken

Territory gained

Territory lost

Faction split

Faction merged

Player aided faction

Player opposed faction
```

---

# Faction Relationship Memory

Faction reputation should retain important reasons.

Example:

```text
Trade Coalition:
Respects player because
Northern Route negotiation succeeded.

Distrusts player because
player later shared route information
with regional authority.
```

---

# Reputation History

Reputation should remain contextual.

Campaign Memory may preserve:

```text
WHAT HAPPENED

WHO KNOWS

HOW THEY INTERPRET IT
```

---

# Reputation Event

Conceptually:

```text
REPUTATION MEMORY

Action:
Convoy rescued.

Witnesses:
Convoy crew.

Spread:
Regional trader network.

Interpretation:
Reliable under danger.

Affected Reputation:
Trader Reliability + strong positive.
```

---

# Reputation Decay

Some reputation memories should fade.

Examples:

```text
minor successful delivery
small trade dispute
routine favor
```

Others may persist for decades.

Examples:

```text
saved settlement
mass betrayal
major political agreement
historic disaster
```

---

# Mission Outcome Memory

Not every Mission deserves permanent memory.

Preserve Missions when they produce:

```text
meaningful relationship change

world-state change

historical significance

major failure

major success

unresolved consequence

role development
```

---

# Mission Memory Example

```text
Mission:
Restore Northern Relay

Outcome:
Completed

Meaning:
Reconnected eastern settlements.

Long-Term Effect:
Regional Information Horizon expanded.

Character Effect:
Player reunited Mara with sister.

Future Relevance:
High
```

---

# Consequence Memory

Consequences may become memories when their causal relationship matters later.

Example:

```text
Player redirected fuel.

Three months later:
Harvest reduced.

Memory:
Hospital decision contributed
to poor harvest.
```

This may later influence:

```text
Farmer relationship
political debates
regional policy
```

---

# Hidden Consequence Memory

Campaign Memory may internally retain a causal relationship even if the player does not know it.

Example:

```text
Player saved engineer.
Engineer later improved microgrid.
```

Memory Visibility:

```text
HIDDEN
```

Later it may become:

```text
DISCOVERED
```

---

# Discovery Memory

Important discoveries should be retained.

Examples:

```text
Hidden facility

Unknown settlement

Aurora evidence

New route

Recovered Record

Lost technology

Character truth

Political secret
```

---

# Discovery Versus Knowledge

Player Knowledge may contain:

```text
what player currently knows.
```

Campaign Memory preserves:

```text
the historical fact that
the discovery occurred
and why it mattered.
```

---

# Regional Memory

Important regional events may influence:

- identity
- politics
- trust
- customs
- preparedness
- relationships with outsiders

Examples:

```text
The Winter Closure

Regional Evacuation

Great Harvest

Fuel Crisis

Bridge Restoration

Valley Compact
```

---

# Regional Memory Versus World Ledger

World Ledger:

```text
records event.
```

Campaign Memory:

```text
records significance
for current campaign.
```

A regional event may become central to Campaign Memory because:

```text
player participated

important characters were affected

current conflict references it

regional identity depends upon it
```

---

# Collective Memory

Some events become part of shared cultural memory.

Conceptually:

```text
COLLECTIVE MEMORY
```

Examples:

```text
"We survived the winter because
the towns shared grain."

"The government abandoned us."

"The northern convoy never returned."

"The bridge reopening changed everything."
```

Collective memory may affect:

```text
Authority Legitimacy

Faction Relations

Risk Perception

Political Values

Social Cohesion
```

---

# Collective Memory May Be Wrong

Communities may remember events inaccurately.

Example:

World truth:

```text
Authority convoy was delayed.
```

Collective memory:

```text
Authority abandoned settlement.
```

If enough people believe it:

```text
the belief itself matters.
```

---

# Memory Perspective

Campaign Memory should distinguish:

```text
WORLD FACT

PLAYER MEMORY

CHARACTER MEMORY

FACTION MEMORY

COLLECTIVE MEMORY
```

These may differ.

---

# Example

Event:

```text
Bridge destroyed.
```

World fact:

```text
Flood caused collapse.
```

Character memory:

```text
Authority ignored warnings.
```

Faction memory:

```text
Rival sabotage suspected.
```

Player memory:

```text
Arrived after collapse.
```

All may influence future behavior.

---

# Political Memory

Political decisions should remain available when later actors reference precedent.

Examples:

```text
Emergency rationing

Regional autonomy agreement

Election dispute

Military intervention

Trade compact

Authority decentralization
```

---

# Political Precedent

Example:

```text
2040:
Council claimed emergency authority
over fuel allocation.
```

Later:

```text
2045:
Council proposes emergency control
of medical supplies.
```

Previous decision becomes:

```text
POLITICAL PRECEDENT.
```

Characters may support or oppose it based upon memory.

---

# Conflict History

Important conflicts should preserve:

```text
Participants

Cause

Claims

Escalation

Agreements

Violations

Outcome

Unresolved Grievances
```

---

# Conflict Memory

Example:

```text
Water dispute
between Settlement A and B.
```

Resolved through:

```text
shared aqueduct.
```

Years later:

```text
new drought.
```

The old agreement and historical trust may affect new negotiations.

---

# Grievance

An unresolved negative memory may become:

```text
GRIEVANCE
```

Examples:

```text
Broken agreement

Uncompensated loss

Abandonment

Resource seizure

Political exclusion
```

---

# Grievance Persistence

Conceptually:

```text
LOW
MODERATE
HIGH
GENERATIVE
```

A generative grievance actively influences future:

```text
conflict
identity
politics
```

---

# Reconciliation Memory

Positive resolution should also persist.

Examples:

```text
Enemies cooperated during flood.

Faction apologized.

Resource was returned.

Agreement honored for years.
```

These memories may reduce later conflict.

---

# Opportunity History

Important missed or realized opportunities may matter later.

Example:

```text
2040:
Factory restoration opportunity rejected.
```

Later:

```text
2043:
Industrial shortage.
```

Characters may remember:

```text
"We could have restored that plant."
```

This may influence politics.

---

# Missed Opportunity Memory

Not every missed opportunity deserves persistence.

Preserve when:

```text
actors knew about it

decision was meaningful

later consequences make it relevant
```

---

# Place Memory

Locations should accumulate history.

Example:

```text
OLD BRIDGE
```

may be remembered as:

```text
evacuation site

battle site

reunion location

trade reopening
```

---

# Place Significance

Conceptually:

```text
PLACE MEMORY

Location
Historical Events
Associated Characters
Player Actions
Current Meaning
```

---

# Player Return

When player returns to meaningful location:

```text
Story Hooks
```

may reference historical memory.

Example:

```text
Old hospital still carries
painted emergency markings
from 2037.
```

---

# Memorialization

Communities may physically preserve memory through:

```text
monuments

graffiti

memorials

names

holidays

archives

stories

rituals
```

This converts Campaign Memory into environmental storytelling.

---

# Artifact Memory

Important objects may carry history.

Examples:

```text
Weapon

Vehicle

Journal

Radio

Recovered Record

Photograph

Tool

Personal item
```

---

# Object History

Example:

```text
Radio:
Used during Valley evacuation.
Later repaired by player.
Later used to establish eastern contact.
```

The object gains significance beyond utility.

---

# Recovered Record Memory

Recovered Records may become Campaign Memory when:

```text
player discovered them

characters reacted to them

they changed knowledge

they influenced decisions
```

The file itself may be historical.

Its campaign discovery has its own history.

---

# Turning Point

A Turning Point is a memory with unusually high long-term influence.

Examples:

```text
Major death

Regional alliance

Faction betrayal

Discovery about Aurora

Settlement destruction

National reconnection

Player assumes leadership

Historic peace agreement
```

---

# Turning Point Criteria

A Turning Point normally affects several of:

```text
World State
Relationships
Player Goals
Regional Identity
Faction Structure
Future Opportunities
Campaign Direction
```

---

# Turning Point Persistence

Turning Points should normally have:

```text
VERY HIGH
```

memory persistence.

They may remain relevant for the rest of the campaign.

---

# Memory Weight

Conceptually:

```text
MINOR
MODERATE
MAJOR
CRITICAL
FOUNDATIONAL
```

---

# Minor Memory

May be retained temporarily.

Example:

```text
Small favor.
```

---

# Moderate Memory

Meaningful to a relationship or current Thread.

---

# Major Memory

Strongly affects future behavior.

---

# Critical Memory

Defines a major relationship, faction or regional history.

---

# Foundational Memory

Part of campaign identity.

Examples:

```text
Player's family disappearance

First major settlement saved

Discovery of Aurora truth

Foundation of regional alliance
```

---

# Memory Persistence

Conceptually:

```text
SHORT
MEDIUM
LONG
PERMANENT
CONDITIONAL
```

---

# Conditional Persistence

Some memories remain relevant only while a condition exists.

Example:

```text
Player owes faction debt.
```

Once repaid:

```text
active obligation ends
```

but historical memory may remain at lower weight.

---

# Memory Decay

Memory should be capable of fading.

Factors may include:

```text
time

low significance

lack of reinforcement

relationship distance

newer stronger events
```

---

# Memory Decay Does Not Mean Deletion

A faded memory may become:

```text
ARCHIVED
```

rather than removed.

It may resurface if relevant.

---

# Memory Reinforcement

A memory may strengthen when:

```text
referenced again

similar event occurs

character discusses it

location revisited

anniversary occurs

new consequence emerges
```

---

# Example

Player helped settlement ten years ago.

Memory weight:

```text
MODERATE
```

Player returns during new crisis.

Old residents remember.

Memory becomes:

```text
HIGH RELEVANCE
```

again.

---

# Memory Resurfacing

A dormant memory may generate Story Hooks when:

```text
current event resembles past event

character returns

player revisits place

promise becomes relevant

faction history repeats

new evidence changes interpretation
```

---

# Historical Echo

Campaign Memory supports:

```text
HISTORICAL ECHO
```

Example:

Past:

```text
Player failed to reach evacuation convoy.
```

Present:

```text
New evacuation begins.
```

The engine may increase relevance because of history.

---

# Memory Trigger

Conceptually:

```text
MEMORY TRIGGER

Character
Location
Event Type
Faction
Relationship
Object
Date
Goal
Conflict
```

---

# Character Trigger

Seeing Mara may surface:

```text
hospital crisis memory.
```

---

# Location Trigger

Returning to bridge may surface:

```text
repair history.
```

---

# Event Trigger

New fuel shortage may surface:

```text
previous fuel allocation decision.
```

---

# Anniversary Trigger

Some cultures or characters may remember:

```text
annual disaster anniversary

death anniversary

founding date

peace agreement
```

Not every memory needs anniversary behavior.

---

# Memory Visibility

Campaign Memory may be:

```text
PLAYER-KNOWN

PARTIALLY KNOWN

HIDDEN

DISCOVERABLE
```

---

# Player-Known

Player experienced or learned the event.

---

# Partially Known

Player understands some but not all of the history.

---

# Hidden

Campaign uses the causal history internally.

Player has no current knowledge.

---

# Discoverable

Evidence exists that may reveal the memory later.

---

# Memory Revision

New information may change interpretation of a past event.

Example:

Player believed:

```text
Faction betrayed settlement.
```

Years later:

```text
Recovered records show orders
were never received.
```

World Event did not change.

Meaning did.

---

# Memory Reinterpretation

The system should allow:

```text
SAME EVENT
+
NEW INFORMATION
=
NEW MEANING
```

This can alter:

- relationships
- grudges
- political views
- goals
- faction trust

---

# False Memory

Characters or communities may remember incorrectly.

The system should support:

```text
INACCURATE MEMORY
```

where appropriate.

This should emerge from:

- misinformation
- rumor
- trauma
- incomplete knowledge
- political narrative

not arbitrary randomness.

---

# Competing Memory

Different groups may remember the same event differently.

Example:

```text
THE SOUTH FORK AGREEMENT
```

Settlement A:

```text
Historic compromise.
```

Settlement B:

```text
Forced concession.
```

Authority:

```text
Successful stabilization.
```

This can influence future politics.

---

# Memory Ownership

Every memory should conceptually know:

```text
WHO REMEMBERS IT?
```

Possible owners:

```text
Player

Character

Faction

Community

Authority

Campaign

World Ledger
```

---

# Campaign-Level Memory

Campaign Memory may retain events that no individual character currently remembers because they remain structurally important.

Example:

```text
Player's early infrastructure choice
created long-term supply dependency.
```

This remains in causal history.

---

# Character Memory Reference

Character Integration may reference:

```text
MEM-2040-017
```

instead of duplicating full event details.

This supports consistency.

---

# Relationship Memory Reference

Relationship systems may reference key memories such as:

```text
First Trust Event

Betrayal

Rescue

Promise

Reconciliation
```

---

# Faction Memory Reference

Faction systems may reference:

```text
Treaty

Player action

Battle

Trade agreement

Political insult
```

---

# Campaign Memory and Relevance

Past history can amplify current relevance.

Conceptually:

```text
CURRENT EVENT
+
RELEVANT MEMORY
=
RELEVANCE AMPLIFICATION
```

Example:

```text
Current:
Hospital fuel shortage.

Memory:
Player once lost close friend
during hospital blackout.
```

Relevance may increase strongly.

---

# Campaign Memory and Story Hooks

Memory may alter how a Hook is presented.

Without history:

```text
"Hospital power is unstable."
```

With history:

```text
Mara pauses before saying:

"It's happening again."
```

The system does not need to explain the entire past.

Memory gives weight to a short line.

---

# Campaign Memory and Mission Generation

Mission generation may consider:

```text
Past promises

Past failures

Known expertise

Previous similar missions

Faction history
```

Example:

```text
Authority asks player again
because player restored same route
five years earlier.
```

---

# Campaign Memory and Character Integration

Characters may change behavior based upon remembered history.

Example:

```text
Player failed Mara previously.
```

Current crisis:

```text
Mara asks someone else first.
```

The world remembers without requiring explicit exposition.

---

# Campaign Memory and Opportunity

Past history may reveal or suppress opportunities.

Example:

```text
Player once helped trader.

Years later:
Trader offers access
to private network.
```

---

# Campaign Memory and Conflict

Old grievances may raise conflict pressure.

Old cooperation may lower it.

Example:

```text
Two settlements shared food
during Winter Closure.
```

Later resource conflict:

```text
higher willingness to negotiate.
```

---

# Campaign Memory and Pacing

Not every memory should resurface immediately.

Pacing should select memories that:

```text
clarify current situation

add emotional weight

explain consequence

support player understanding

create meaningful continuity
```

Avoid constant:

```text
REMEMBER WHEN...
```

dialogue.

---

# Memory Saturation

Too many callbacks can make history feel artificial.

Use memory when:

```text
it genuinely matters now.
```

---

# Memory Compression

Related minor memories may be compressed.

Example:

Instead of preserving:

```text
14 successful deliveries
```

retain:

```text
Player developed reputation
as reliable regional courier.
```

Important exceptions may remain individually referenced.

---

# Summary Memory

Conceptually:

```text
SUMMARY MEMORY

Subject:
Northern Trader Network

Pattern:
Player repeatedly honored contracts.

Period:
2041–2043

Result:
Reliable reputation established.
```

---

# Episodic Memory

Specific event:

```text
Player delivered medicine
through blizzard on 2042-01-17.
```

Both summary and episodic memory may coexist.

---

# Pattern Detection

Repeated actions may create a Memory Pattern.

Examples:

```text
Always prioritizes family.

Frequently breaks authority rules.

Pays debts.

Avoids violence.

Supports local autonomy.

Profits from shortages.
```

These patterns may affect:

```text
role emergence
reputation
character expectation
future requests
```

---

# Pattern Does Not Equal Alignment Lock

A behavioral pattern describes history.

It should not prevent the player from changing.

Later actions may alter or contradict the pattern.

---

# Player Evolution

Campaign Memory allows characters to perceive:

```text
YOU HAVE CHANGED.
```

Example:

Early campaign:

```text
Player avoided political involvement.
```

Later:

```text
Player becomes council leader.
```

History makes transformation meaningful.

---

# Memory Conflict

New player behavior may conflict with old reputation.

Example:

```text
Known pacifist
uses violence.
```

Different actors may interpret:

```text
necessary adaptation
hypocrisy
betrayal
growth
```

---

# Memory and Identity

Long-term Campaign Memory contributes to:

```text
PLAYER IDENTITY
CHARACTER IDENTITY
FACTION IDENTITY
REGIONAL IDENTITY
```

Identity should emerge from accumulated history.

---

# Campaign Chronicle

Campaign Memory may support a higher-level:

```text
CAMPAIGN CHRONICLE
```

This is a compressed chronological account of major campaign history.

Example:

```text
2038
Player arrived in Shenandoah.

2039
Northern Route reopened.

2040
Valley Fuel Crisis.

2041
Mara elected to council.

2042
Eastern radio restored.

2044
Regional Trade Compact signed.
```

---

# Chronicle Versus World Ledger

World Ledger may contain thousands of entries.

Campaign Chronicle contains:

```text
major campaign-relevant history.
```

---

# Chronicle Generation

Chronicle entries should normally derive from:

```text
MAJOR
CRITICAL
FOUNDATIONAL
```

Campaign Memories.

---

# Memory Promotion

A recent event may be promoted into Campaign Memory when:

```text
impact persists

relationship changed

future relevance is likely

event became historically meaningful
```

---

# Memory Promotion Pipeline

Conceptually:

```text
RECENT EVENT
      ↓
SIGNIFICANCE CHECK
      ↓
FUTURE RELEVANCE CHECK
      ↓
MEMORY ENTRY
      ↓
WEIGHT
      ↓
PERSISTENCE
```

---

# Memory Rejection

A recent event may be discarded from long-term memory when:

```text
routine

resolved

low significance

no future relevance

no relationship effect

no historical consequence
```

World Ledger may still retain it if appropriate.

---

# Memory Consolidation

Several related events may consolidate into one stronger memory.

Example:

```text
Week-long flood response
```

contains:

```text
20 minor actions.
```

Campaign Memory may retain:

```text
Player coordinated South Fork flood relief.
```

plus selected major episodes.

---

# Memory Decomposition

Conversely, one major event may contain several independently meaningful memories.

Example:

```text
Settlement evacuation
```

may create:

```text
Promise to Mara

Death of Elias

Faction betrayal

Bridge destruction
```

Each may deserve separate persistence.

---

# Memory Integrity

Campaign Memory must not silently rewrite history to improve narrative coherence.

If:

```text
events were contradictory
messy
unresolved
```

memory should preserve that complexity where relevant.

---

# Causal Integrity

Memory should preserve known causal relationships.

Example:

```text
Factory failed
because fuel was redirected.
```

Do not later simplify to:

```text
Factory mysteriously failed.
```

unless current characters genuinely do not know the cause.

---

# Perspective Integrity

World truth and actor interpretation must remain separate.

The campaign may know:

```text
what actually happened.
```

Characters may remember:

```text
what they believe happened.
```

Both matter.

---

# Memory and Death

Character death should create strong memory where relationships or world importance justify it.

Possible associated memories:

```text
Circumstances of death

Last conversation

Unfinished promise

Impact on faction

Place of death

Who knows
```

---

# Memory After Death

Dead characters may remain relevant through:

```text
family

records

places

politics

legacy

unfinished goals
```

Death should not automatically erase character significance.

---

# Legacy

A character may leave:

```text
institution
technology
family
political doctrine
building
relationship network
```

These can preserve their influence.

---

# Character Legacy Example

Engineer dies.

But:

```text
Engineer trained apprentices.
```

Years later:

```text
regional infrastructure still benefits.
```

Campaign Memory preserves connection.

---

# Memory and Reconnection

During WS-04 — The Reconnection, history becomes especially important.

Regions may remember:

```text
who helped

who abandoned them

who traded fairly

who attacked them

who preserved autonomy

who attempted control
```

These memories affect reunification.

---

# Historical Negotiation

Reconnection negotiations should frequently depend upon:

```text
PAST RELATIONSHIPS
```

rather than only current resources.

Example:

```text
National authority returns.
```

Region remembers:

```text
2034 abandonment narrative.
```

Current Authority Legitimacy is therefore influenced by history.

---

# Generational Memory

Long campaigns may span enough time for memories to become:

```text
SECONDHAND
```

Younger characters may know events through:

```text
stories
records
education
family
political narrative
```

---

# Firsthand Versus Inherited Memory

Conceptually:

```text
FIRSTHAND

SECONDHAND

INSTITUTIONAL

CULTURAL
```

The same event may migrate between forms over time.

---

# Cultural Memory

Some events may become:

```text
tradition

holiday

warning

myth

regional identity
```

At that point they may belong partly to:

```text
Society
```

rather than only Campaign Memory.

---

# Memory Handoff

When a campaign memory becomes structurally embedded into:

```text
Society
Faction
Authority
World State
```

Campaign Memory may retain a reference rather than duplicate full state.

---

# Memory Search

The engine should be capable of retrieving memories by:

```text
Character

Faction

Location

Event Type

Theme

Date

Player Decision

Promise

Conflict

Object

Region
```

---

# Contextual Retrieval

When a new situation occurs:

```text
DO NOT LOAD ALL MEMORY.
```

Retrieve only memories likely relevant to:

```text
current actors
current location
current event
current goals
```

This keeps the system scalable.

---

# Memory Relevance

Conceptually:

```text
MEMORY RELEVANCE
=
Current Similarity
+
Actor Connection
+
Location Connection
+
Relationship Connection
+
Causal Connection
+
Historical Weight
```

---

# Memory Recall

Recall may be:

```text
DIRECT

ASSOCIATIVE

CAUSAL

RELATIONAL

GEOGRAPHIC

THEMATIC
```

---

# Direct Recall

Same event or actor.

---

# Associative Recall

Current situation resembles past situation.

---

# Causal Recall

Past event caused current condition.

---

# Relational Recall

Current character is tied to past memory.

---

# Geographic Recall

Current location carries history.

---

# Thematic Recall

Current dilemma echoes earlier values or choices.

Use carefully.

Thematic similarity should not override actual causal history.

---

# Memory Output

Conceptually:

```text
MEMORY QUERY

Current Situation:
Regional Fuel Allocation

Relevant Memories:

MEM-2041-0042
Player prioritized hospital
during previous fuel shortage.

Weight:
MAJOR

Relationship:
Mara

Current Relevance:
HIGH


MEM-2041-0051
Farm Cooperative suffered reduced harvest.

Weight:
MODERATE

Current Relevance:
HIGH
```

This helps current characters and Story Hooks respond coherently.

---

# Example 1
# Promise

2040:

```text
Mara:
"If this gets worse,
don't leave without telling me."

Player:
"I won't."
```

Memory:

```text
PROMISE
OPEN / CONTEXTUAL
```

2042:

Player prepares to leave region secretly.

Memory becomes relevant.

Mara's future response can reference the promise.

---

# Example 2
# Long-Term Reputation

2040–2044:

Player completes several difficult deliveries.

Campaign Memory consolidates:

```text
Player is known among
regional traders as reliable.
```

2045:

Major medical shipment needs transport.

Mission Generation may consider:

```text
WHY PLAYER?

Reliable regional courier.
```

The history created future content.

---

# Example 3
# Broken Agreement

Two settlements sign water-sharing agreement.

Player helped mediate.

Three years later:

Settlement A violates agreement.

Relevant memories include:

```text
Original terms

Who made concessions

Who guaranteed agreement

Player's mediator role
```

New conflict begins with history.

---

# Example 4
# Return After Years

Player returns to old settlement after six years.

Campaign Memory finds:

```text
Player restored clinic.

Friend moved away.

Old council collapsed.

Bridge remains operational.

Player was once highly trusted.
```

Story Hooks may surface:

```text
clinic plaque

older resident recognition

message from former friend

changed political reality
```

The settlement feels continuous.

---

# Example 5
# Reinterpreted History

Player once believed:

```text
Military abandoned evacuation.
```

Recovered Record later reveals:

```text
orders were intercepted.
```

Memory does not erase old belief.

Instead:

```text
Old Interpretation:
Abandonment

New Evidence:
Communication failure

Current Interpretation:
Uncertain / Revised
```

Characters may react differently.

---

# Example 6
# Hidden Butterfly

2037:

Player rescues unknown engineer.

Memory stored:

```text
Minor relationship
+
character survival
```

2044:

Engineer becomes infrastructure director.

Current regional power stability partly depends on them.

The old memory becomes:

```text
high future relevance.
```

---

# Example 7
# Place Memory

A rail station was once:

```text
evacuation center.
```

Years later:

```text
trade hub.
```

The location carries both memories.

Older characters may still call one platform:

```text
"The Departure Line."
```

World history becomes culture.

---

# Example 8
# Ordinary Positive Memory

Not every important memory is crisis.

Example:

```text
Player attended Mara's wedding.
```

Later:

```text
relationship reference
family memory
anniversary interaction
```

Ordinary life deserves continuity too.

---

# Memory Update Cycle

A conceptual Campaign Memory cycle:

```text
1. Read recent campaign events.

2. Read Mission outcomes.

3. Read Consequence outcomes.

4. Read Character milestones.

5. Read Relationship changes.

6. Read Faction changes.

7. Read promises and obligations.

8. Read significant discoveries.

9. Evaluate historical significance.

10. Evaluate relationship weight.

11. Evaluate future relevance.

12. Create new Memory Entries.

13. Update existing Memory Entries.

14. Link related memories.

15. Consolidate repetitive memories.

16. Promote major memories.

17. Reduce weight of low-value memories.

18. Archive inactive memories.

19. Detect new Memory Patterns.

20. Update Campaign Chronicle.

21. Provide relevant memories to active systems.
```

---

# Memory Promotion Criteria

A memory should be strongly considered for long-term retention if it affects at least one of:

```text
Major Relationship

Major Character

Player Identity

Faction Relationship

Regional State

Political History

Unresolved Obligation

Long-Term Consequence

Future Opportunity

Future Conflict

Campaign Turning Point
```

---

# Memory Compression Criteria

Compress when:

```text
events are repetitive

individual episodes are low-value

pattern matters more than exact instance
```

---

# Memory Deletion

Permanent deletion should be rare.

Possible reasons:

```text
Duplicate

Invalid system artifact

Corrupted data

No longer canonically meaningful
```

Normal forgetting should usually mean:

```text
ARCHIVED / LOW WEIGHT
```

not physical deletion.

---

# Memory Storage Levels

Conceptually:

```text
ACTIVE MEMORY

DORMANT MEMORY

ARCHIVED MEMORY

FOUNDATIONAL MEMORY
```

---

# Active Memory

Likely to affect current campaign.

---

# Dormant Memory

Currently irrelevant but may return.

---

# Archived Memory

Low current relevance.

Retrievable if specifically needed.

---

# Foundational Memory

Persistent identity-defining history.

---

# Memory Resolution

High-resolution memory should primarily exist for:

```text
Player

Primary Characters

Important Relationships

Active Factions

Player Regions

Major Turning Points
```

Lower-resolution memory may represent distant history.

---

# Memory and Simulation Scale

The system should not require:

```text
every NPC
```

to possess:

```text
complete lifetime episodic memory.
```

Different simulation resolutions remain valid.

---

# Primary Character Memory

May preserve:

```text
specific interactions

relationship events

promises

major observations

player behavior
```

---

# Recurring Character Memory

May preserve:

```text
relationship summary

major positive / negative events

important promises
```

---

# Background Character Memory

May be represented by:

```text
community reputation

faction reputation

collective memory
```

rather than individual history.

---

# Campaign Memory and World Ledger Integration

The two systems should exchange references.

Conceptually:

```text
WORLD LEDGER ENTRY

Event:
Bridge Restoration

        ↓

CAMPAIGN MEMORY

Player Role:
Led repair.

Character Effect:
Mara reunited with family.

Regional Effect:
Trade restored.
```

---

# World Ledger Candidate

Historically significant Campaign Memories may suggest:

```text
WORLD LEDGER
```

entries if none already exist.

But World Ledger remains the factual world-history authority.

---

# Memory Without Ledger

Personal memories do not necessarily belong in World Ledger.

Example:

```text
Player promised friend
to return.
```

Campaign Memory:

```text
YES
```

World Ledger:

```text
probably NO.
```

---

# Ledger Without Campaign Memory

A distant national event may belong in World Ledger but never matter to the campaign.

This is also valid.

---

# The Legacy Overview

The legacy `Overview.md` included:

```text
Write to the World Ledger
```

as the final Daily Update Cycle step.

The modern architecture clarifies that this should be split into:

```text
WORLD HISTORY
      ↓
WORLD LEDGER

CAMPAIGN SIGNIFICANCE
      ↓
CAMPAIGN MEMORY
```

This preserves both objective history and subjective continuity.

---

# Campaign Memory Output Example

```text
CAMPAIGN MEMORY

Memory ID:
MEM-2041-0042

Type:
DECISION / CONSEQUENCE

Date:
2041-10-17

Location:
Shenandoah Valley

Subject:
Regional Fuel Allocation

Actors:
Player
Mara Vale
Farm Cooperative
Regional Authority

Event:
Player supported hospital fuel priority
during regional shortage.

Immediate Outcome:
Hospital generators remained operational.

Delayed Outcome:
Agricultural output decreased.

Relationship Effect:
Mara trust increased.

Faction Effect:
Farm Cooperative trust decreased.

Player Knowledge:
Both major consequences known.

Weight:
MAJOR

Persistence:
LONG

Current Status:
DORMANT

Triggers:
Fuel shortage
Mara
Farm Cooperative
Resource allocation conflict
```

---

# Relationship Memory Example

```text
CAMPAIGN MEMORY

Memory ID:
MEM-2039-0112

Type:
RELATIONSHIP

Character:
Mara Vale

Event:
Player kept confidential
medical evacuation route secret.

Meaning:
Mara learned player
could be trusted with sensitive information.

Relationship Effect:
Strong positive trust memory.

Weight:
MAJOR

Persistence:
LONG
```

---

# Collective Memory Example

```text
CAMPAIGN MEMORY

Memory ID:
MEM-2040-0201

Type:
REGIONAL / COLLECTIVE

Event:
Winter Grain Sharing Agreement

Region:
Shenandoah Valley

Participants:
Five settlements

Meaning:
Remembered as moment
when regional cooperation
prevented widespread hunger.

Current Effects:
Higher regional cooperation
during food shortages.

Weight:
CRITICAL

Persistence:
PERMANENT
```

---

# Minimum Campaign Memory

A minimum viable implementation should support:

```text
Player Decisions

Promises

Relationship Milestones

Major Character Changes

Faction History

Mission Outcomes

Major Consequences

Discoveries

Regional Turning Points

Reputation History

Memory Weight

Memory Persistence

Memory Triggers

Memory References
```

---

# Campaign Memory Consistency Rules

## Rule 1

Campaign Memory does not attempt to remember everything.

---

## Rule 2

Memory preserves what remains meaningful.

---

## Rule 3

World Ledger and Campaign Memory are separate.

---

## Rule 4

World Ledger represents what happened.

---

## Rule 5

Campaign Memory represents why history still matters.

---

## Rule 6

Player decisions should retain relevant context.

---

## Rule 7

Promises should remain traceable.

---

## Rule 8

Relationships should preserve important historical reasons.

---

## Rule 9

Characters should have lives between player encounters.

---

## Rule 10

Faction reputation should preserve meaningful historical causes.

---

## Rule 11

Reputation must respect who knows what.

---

## Rule 12

Hidden consequences may remain hidden in memory.

---

## Rule 13

New information may reinterpret old memories.

---

## Rule 14

New information does not rewrite historical fact.

---

## Rule 15

Different actors may remember the same event differently.

---

## Rule 16

Collective memory may be inaccurate.

---

## Rule 17

Incorrect collective memory may still influence behavior.

---

## Rule 18

Important places may accumulate historical meaning.

---

## Rule 19

Objects may accumulate history.

---

## Rule 20

Positive memories are as valid as traumatic memories.

---

## Rule 21

Ordinary-life milestones may deserve long-term memory.

---

## Rule 22

Turning Points should receive strong persistence.

---

## Rule 23

Memory may decay in relevance without being deleted.

---

## Rule 24

Memories may resurface through meaningful triggers.

---

## Rule 25

Repeated minor events may consolidate into patterns.

---

## Rule 26

Patterns describe history; they do not lock future behavior.

---

## Rule 27

Memory callbacks should not overwhelm pacing.

---

## Rule 28

Campaign Memory must preserve causal integrity.

---

## Rule 29

Campaign Memory must preserve perspective differences.

---

## Rule 30

Character death does not erase character legacy.

---

## Rule 31

Historical memory should influence Reconnection politics.

---

## Rule 32

Only contextually relevant memories should normally be retrieved.

---

## Rule 33

Major campaign history should support a Campaign Chronicle.

---

## Rule 34

Memory must support both personal and systemic continuity.

---

# Guiding Questions

Before promoting something into Campaign Memory, ask:

**Did this change a relationship?**

**Did someone make or break a promise?**

**Did a character's life materially change?**

**Did the player make a meaningful decision?**

**Did this alter World State?**

**Did this create a long-term consequence?**

**Did a faction or authority change because of it?**

**Might a future actor reasonably reference this?**

**Does this explain a current reputation?**

**Does this change how a place or object is understood?**

**Could this matter years later?**

If the answer to all of these is:

```text
NO
```

the event probably does not need persistent Campaign Memory.

---

# Memory Retrieval Questions

When current events require history, ask:

**Who is involved now?**

**Where are we?**

**What similar event happened before?**

**What promises connect to this?**

**Which relationship memories matter?**

**What unresolved consequences remain?**

**What does each actor remember?**

**What does the player know?**

**What does the world know to be true?**

These questions prevent generic callbacks.

---

# Core Design Principle

Project Ascension should never behave as though:

```text
THE PAST DISAPPEARS
WHEN THE QUEST ENDS.
```

Instead:

```text
THE PAST BECOMES
PART OF THE PRESENT.
```

---

# Continuity Principle

The player should be able to return to:

```text
a person

a settlement

a faction

a road

a house

a region
```

years later and discover:

```text
THE HISTORY IS STILL THERE.
```

Sometimes visibly.

Sometimes socially.

Sometimes politically.

Sometimes only in memory.

---

# Personal History Principle

A relationship should eventually be capable of containing sentences like:

```text
"You always do this."

"You came back."

"You weren't there."

"We survived that together."

"I still remember what you told me."

"You've changed."

"I haven't forgotten."
```

These lines should not be arbitrary narrative flavor.

The system should know:

```text
WHY THEY ARE TRUE.
```

---

# World History Principle

Regions should similarly be capable of saying:

```text
"We remember who helped us."

"We remember who left."

"We do not depend on them anymore."

"That winter changed us."

"We tried that once."

"We made that mistake before."
```

Civilization itself accumulates memory.

---

# Architectural Result

With Campaign Memory established, the Living Campaign Engine can preserve:

```text
CAUSE
+
ACTION
+
CONSEQUENCE
+
MEANING
+
TIME
```

This transforms dynamic events into:

```text
HISTORY.
```

The full loop becomes:

```text
WORLD
      ↓
EVENT
      ↓
RELEVANCE
      ↓
HOOK
      ↓
PLAYER / CHARACTER ACTION
      ↓
CONSEQUENCE
      ↓
NEW WORLD
      ↓
MEMORY
      ↓
FUTURE RELEVANCE
      ↓
FUTURE ACTION
```

Memory therefore does not sit outside the Living Campaign Engine.

It feeds the next generation of stories.

---

# Living Campaign Memory Loop

```text
PAST ACTION
      ↓
MEMORY
      ↓
CURRENT CHARACTER EXPECTATION
      ↓
CURRENT DECISION
      ↓
NEW CONSEQUENCE
      ↓
NEW MEMORY
```

History becomes part of simulation causality.

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
FOUNDATION DEFINED

Consequence_Propagation.md
FOUNDATION DEFINED

Opportunity_and_Conflict.md
FOUNDATION DEFINED

Pacing_and_Priority.md
FOUNDATION DEFINED

Campaign_Memory.md
FOUNDATION DEFINED
```

---

# Foundation Status

The planned foundational Living Campaign Engine documents are now defined.

The system can conceptually answer:

```text
WHAT IS HAPPENING?
World Simulation

WHAT CHANGED?
World Event Intake

WHY DOES IT MATTER?
Relevance and Proximity

HOW DOES THE PLAYER EXPERIENCE IT?
Story Hooks

CAN THE PLAYER MEANINGFULLY INTERVENE?
Mission Generation

WHAT ARE CHARACTERS DOING?
Character Integration

WHAT HAPPENS AFTERWARD?
Consequence Propagation

WHAT POSSIBILITIES AND DISPUTES EXIST?
Opportunity and Conflict

WHAT DESERVES ATTENTION NOW?
Pacing and Priority

WHAT MUST REMAIN MEANINGFUL?
Campaign Memory
```

---

# Recommended Next Phase

The Living Campaign Engine foundation should now be validated before adding more conceptual systems.

Recommended:

```text
Canon/
└── Systems/
    └── Living_Campaign_Engine/
        └── Validation/
            └── TEST-001_Fuel_Crisis_Emergent_Campaign.md
```

The test should begin with only World State conditions.

For example:

```text
REGION:
Shenandoah Valley

Fuel:
CONSTRAINED

Hospital Reserve:
LOW

Farm Fuel Demand:
HIGH

Transport Reserve:
LOW

Player:
Known to Mara
Established Trader
No active Mission
```

Then test whether the Living Campaign Engine naturally produces:

```text
World Event Candidate

Relevance

Environmental Hook

Character Hook

Conflict

Opportunity

Possible Player-Created Objective

Mission only if necessary

Character Independent Action

Consequences

Memory
```

without scripting:

```text
THE FUEL CRISIS QUEST.
```

If that succeeds, we have validated the complete loop:

```text
WORLD CONDITION
      ↓
EMERGENT CAMPAIGN
      ↓
PLAYER ACTION
      ↓
WORLD HISTORY
```

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial Campaign Memory framework established for meaningful long-term history, player decisions, promises, relationships, character and faction continuity, reputation, collective memory, historical reinterpretation, Campaign Chronicle and World Ledger integration. |