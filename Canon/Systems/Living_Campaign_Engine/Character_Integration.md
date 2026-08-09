# PROJECT ASCENSION
# Character Integration System

| Field | Value |
|--------|-------|
| System | Living Campaign Engine |
| Document | Character Integration |
| Location | Canon/Systems/Living_Campaign_Engine/Character_Integration.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Character Autonomy, Needs, Knowledge, Relationships and Campaign Interaction |
| Last Updated | 2026-08-09 |

> *"A character should contact the player because they have a reason — not because the campaign needs a mission."*

---

# Purpose

The Character Integration system defines how individual characters interact with:

- World Simulation
- Campaign State
- Story Hooks
- Mission Generation
- Relationships
- Factions
- Population
- Authority
- Supply
- Security
- Information
- Campaign Memory

Its purpose is to ensure that characters behave as persistent inhabitants of the world rather than as static narrative interfaces.

Characters should possess:

- needs
- goals
- responsibilities
- knowledge
- relationships
- professions
- locations
- resources
- loyalties
- fears
- opportunities
- plans
- memories

These factors determine what they do.

---

# Core Principle

The central rule is:

```text
NPC
≠
QUEST DISPENSER
```

A character should never exist primarily to:

```text
stand in one place
+
wait for player
+
provide objective
+
reward completion
```

Instead:

```text
CHARACTER EXISTS
      ↓
WORLD AFFECTS CHARACTER
      ↓
CHARACTER INTERPRETS WORLD
      ↓
CHARACTER MAKES DECISION
      ↓
CHARACTER ACTS
      ↓
PLAYER MAY OR MAY NOT BECOME INVOLVED
```

---

# Character Autonomy

Characters continue acting whether or not the player is present.

Example:

```text
Character:
Doctor

Problem:
Hospital medicine shortage.
```

Possible actions:

```text
Request regional allocation.

Contact other clinics.

Reduce elective treatment.

Search private inventories.

Ask known trader.

Ask player.

Do nothing temporarily.
```

The player is one possible resource.

Not the default solution.

---

# Character State

Each important character should conceptually possess:

```text
CHARACTER STATE
│
├── Identity
├── Location
├── Condition
├── Profession
├── Responsibilities
├── Needs
├── Goals
├── Knowledge
├── Beliefs
├── Resources
├── Relationships
├── Faction Links
├── Authority Links
├── Current Plan
├── Stress
├── Availability
└── Memory References
```

Detailed character personality systems may live elsewhere.

Character Integration consumes the parts needed for campaign behavior.

---

# Character Identity

Character identity includes stable information such as:

```text
Character ID
Name
Age
Background
Profession
Home Region
Affiliations
```

Campaign systems should reference Character IDs rather than duplicating full character data.

---

# Character Location

Characters exist somewhere in the world.

Conceptually:

```text
Region
Settlement
Specific Location
Travel State
Destination
Accessibility
```

Location matters because characters cannot:

```text
appear anywhere
because player needs them.
```

---

# Character Travel

Characters may:

```text
Stay
Travel
Relocate
Evacuate
Migrate
Become stranded
Disappear from contact
```

Their location should update over time.

---

# No Teleporting Characters

If a character is:

```text
200 km away
```

they cannot suddenly appear in the player's settlement without:

- travel time
- transport
- route access
- plausible motivation

unless an explicit system permits otherwise.

---

# Character Condition

Broad operational condition may include:

```text
HEALTHY
TIRED
STRAINED
INJURED
ILL
CRITICAL
RECOVERING
```

Detailed health belongs elsewhere if required.

Condition affects:

- availability
- decisions
- travel
- requests
- work
- risk tolerance

---

# Profession

Profession strongly influences:

```text
what the character knows
what problems they notice
what resources they can access
who they know
what responsibilities they possess
```

Examples:

```text
Doctor
Farmer
Engineer
Trader
Security Officer
Radio Operator
Teacher
Government Official
Mechanic
Courier
Researcher
```

---

# Profession as Perspective

Same world event:

```text
Fuel shortage.
```

Doctor sees:

```text
Generator risk.
```

Farmer sees:

```text
Harvest risk.
```

Trader sees:

```text
Market opportunity.
```

Security officer sees:

```text
Route protection problem.
```

Character profession creates different Story Hooks from the same World Event.

---

# Responsibilities

Characters may possess obligations independent of personal goals.

Examples:

```text
Doctor:
Patients

Farmer:
Harvest

Security Officer:
Route security

Parent:
Children

Council Member:
Community

Trader:
Contracts
```

Responsibilities strongly influence decisions.

---

# Character Needs

Needs represent immediate pressures affecting the character.

Possible categories:

```text
Safety
Food
Water
Medicine
Shelter
Transport
Information
Money / Trade
Tools
Social Support
Protection
Access
```

---

# Need Severity

Conceptually:

```text
LOW
MODERATE
HIGH
CRITICAL
```

A critical need may override long-term goals.

---

# Need Versus Goal

These must remain distinct.

Example:

```text
Goal:
Expand clinic.

Need:
Find antibiotics today.
```

The Need becomes immediate.

The Goal remains longer-term.

---

# Character Goals

Characters should possess independent goals.

Examples:

```text
Protect family.

Expand business.

Restore infrastructure.

Gain political influence.

Leave dangerous region.

Find missing person.

Build settlement.

Understand Aurora.
```

Goals may exist for years.

---

# Goal Types

Possible conceptual categories:

```text
PERSONAL
RELATIONAL
PROFESSIONAL
ECONOMIC
POLITICAL
IDEOLOGICAL
SURVIVAL
INVESTIGATIVE
COMMUNITY
```

---

# Goal Priority

Character goals may be:

```text
PRIMARY
ACTIVE
SECONDARY
DORMANT
ABANDONED
COMPLETED
```

---

# Character Planning

Characters should create plans from:

```text
GOAL
+
KNOWLEDGE
+
RESOURCES
+
CONSTRAINTS
```

Conceptually:

```text
CHARACTER GOAL
      ↓
AVAILABLE OPTIONS
      ↓
PREFERRED ACTION
      ↓
CURRENT PLAN
```

---

# Current Plan

Example:

```text
Goal:
Obtain medicine.

Current Plan:
Contact regional clinic.

Fallback:
Ask trader.

Fallback:
Ask player.

Last Resort:
Travel personally.
```

The player should not automatically be Plan A.

---

# Plan Failure

If a plan fails:

```text
CHARACTER REEVALUATES
```

rather than freezing.

Example:

```text
Trader unavailable.
```

Character may:

```text
contact authority
travel
reduce demand
seek substitute
ask player
```

---

# Character Decision Inputs

A character decision may consider:

```text
Need Severity
Goal Priority
Knowledge
Beliefs
Resources
Relationships
Profession
Responsibilities
Risk
Trust
Stress
Time
World Conditions
```

No single input should determine behavior universally.

---

# Character Knowledge

Characters possess individual knowledge states.

They should not have access to World Simulation truth.

Character knowledge may include:

```text
Observed facts
Reports
Rumors
Professional knowledge
Faction information
Authority information
Personal communication
```

---

# Character Knowledge Entry

Conceptually:

```text
CHARACTER KNOWLEDGE

Subject
Known State
Source
Age
Reliability
Verification
Confidence
```

---

# Character Knowledge Limits

Example:

```text
Character:
Mechanic
```

may know:

```text
Fuel deliveries are late.
```

They may not know:

```text
why regional authority changed import allocation.
```

unless that information plausibly reached them.

---

# Character Misunderstanding

Characters may be wrong.

Example:

```text
Character believes:
Bridge closed because of attack.
```

Actual:

```text
Structural failure.
```

Their decisions should use their belief.

---

# Character Beliefs

Beliefs include interpretation beyond factual knowledge.

Examples:

```text
Authority cannot be trusted.

Region will recover.

Player is reliable.

Travel north is unsafe.
```

Beliefs may influence behavior even when incorrect.

---

# Character Perspective

Every character interaction should preserve perspective.

Avoid dialogue that sounds like:

```text
World Simulation status report.
```

Prefer information shaped by:

```text
profession
experience
emotion
knowledge
relationship
```

---

# Character Resources

Characters may possess access to:

```text
Food
Fuel
Medicine
Money
Trade Goods
Transport
Weapons
Equipment
Information
Authority Access
Social Connections
```

Resources influence autonomy.

---

# Resource-Rich Characters

A well-connected trader with fuel reserves may solve problems without player help.

This is desirable.

---

# Resource-Poor Characters

A character with:

```text
High need
+
Low resources
```

may be more likely to seek assistance.

Who they ask depends upon relationships and trust.

---

# Character Relationships

Characters maintain relationships with:

- player
- other characters
- factions
- authorities
- communities

Detailed relationship mechanics live in:

```text
Canon/Systems/Relationships/
```

Character Integration consumes relationship state.

---

# Player Relationship

Relevant factors include:

```text
Relationship Strength
Trust
Recent Interactions
Obligations
History
Accessibility
```

---

# Relationship Is Not Ownership

A close relationship does not mean:

```text
character always agrees with player.
```

Nor:

```text
character waits for player decisions.
```

Close characters retain independent goals and values.

---

# Character Contact Decision

Before contacting the player, the system should evaluate:

```text
Does the character need contact?

Does the character believe the player can help?

Does the character trust the player?

Can communication occur?

Are there better alternatives?

Does the character want the player involved?
```

---

# Contact Probability Concept

Conceptually:

```text
CONTACT LIKELIHOOD
=
Need
+
Relationship
+
Player Capability
+
Trust
+
Relevance
-
Alternative Options
-
Communication Barriers
```

No universal numeric formula is required.

---

# Reasons to Contact Player

Possible motives include:

```text
Ask for help

Share information

Warn player

Offer opportunity

Seek emotional support

Fulfill obligation

Negotiate

Trade

Report outcome

Invite participation

Manipulate

Say goodbye
```

Characters should not contact the player only to create Missions.

---

# Reasons NOT to Contact Player

A character may deliberately not contact the player because:

```text
They can handle it themselves.

They do not want to worry the player.

They distrust the player.

Communication unavailable.

Player is too far away.

Situation resolved already.

Character wants secrecy.

They asked someone else.
```

This is essential for believable autonomy.

---

# Contactability

Conceptually:

```text
DIRECT
AVAILABLE
LIMITED
UNREACHABLE
UNKNOWN
```

Contactability depends upon:

- communications
- information
- distance
- infrastructure
- security

---

# Communication Delay

Example:

```text
Character sends message:
Day 1

Courier reaches player:
Day 4
```

The character's state may have changed by then.

The message remains historically accurate to when it was sent.

---

# Outdated Character Hook

Example message:

```text
"We need help at the clinic."
```

Player arrives three days later.

Situation:

```text
Clinic already evacuated.
```

This is valid.

---

# Character Requests

A request should emerge from:

```text
CHARACTER NEED
+
CHARACTER PLAN
+
PLAYER RELATIONSHIP
+
PLAYER CAPABILITY
```

Not simply:

```text
Mission Generator selected character.
```

---

# Request Structure

Conceptually:

```text
CHARACTER REQUEST

Character
Underlying Need
Desired Outcome
Why Player
Urgency
Known Information
Alternatives
Expectation
Commitment Requested
```

---

# Why Player

Every direct request should be able to answer:

```text
WHY ARE THEY ASKING THIS PLAYER?
```

Possible answers:

```text
Trusted friend

Relevant skill

Local proximity

Faction access

Available transport

Past reliability

No other option
```

---

# Request Without Mission

Example:

```text
Friend:
"If you see any antibiotics,
could you keep us in mind?"
```

This may create:

```text
Obligation
Goal Relevance
Memory
```

without a formal Mission.

---

# Character Request Priority

Characters may ask for different levels of involvement.

Conceptually:

```text
MENTION

SUGGESTION

FAVOR

REQUEST

PLEA

FORMAL ASSIGNMENT
```

Tone depends upon relationship and context.

---

# Mention

```text
"Fuel's getting difficult again."
```

No expectation.

---

# Suggestion

```text
"If you're heading north,
you might ask about medicine."
```

---

# Favor

```text
"Could you bring this message
when you go?"
```

---

# Request

```text
"We need someone to inspect the relay."
```

---

# Plea

```text
"My son is still out there."
```

---

# Formal Assignment

Appropriate for:

- authority
- military
- faction command
- employment

Example:

```text
"Your task is to survey Route 7."
```

---

# Relationship Tone

The same request may be phrased differently by:

```text
Close friend

Unknown authority

Rival

Family member

Professional contact
```

Character Integration should preserve this difference.

---

# Character Autonomy After Request

After asking the player:

```text
THE CHARACTER STILL ACTS
```

Example:

```text
Doctor asks player for medicine.
```

While waiting, doctor may:

```text
reduce prescriptions
contact other clinics
trade supplies
relocate patients
```

---

# No Frozen Requester

Avoid:

```text
Player returns after two months.

Doctor still stands in same place
waiting for exact same shipment.
```

World and character states evolve.

---

# Character Alternatives

Every major need should ideally have one or more alternatives.

Example:

```text
Need:
Fuel.
```

Alternatives:

```text
Player
Authority
Trader
Conservation
Substitution
Relocation
```

This helps determine whether the character waits, adapts or escalates.

---

# Character Success Without Player

Characters may solve their own problems.

Example:

```text
Player ignores request.
```

Later:

```text
Character found alternate supplier.
```

This should be common enough to establish autonomy.

---

# Character Failure Without Player

Alternatively:

```text
No solution found.
```

Character's state may worsen.

The result follows world causality.

---

# Character Independent Success

Possible Story Hook:

```text
"You never made it back,
but we managed.

The clinic in Front Royal
sent us enough."
```

This communicates that the world did not wait.

---

# Character Independent Consequence

Example:

```text
Character leaves settlement
to find medicine.
```

This may create:

```text
new location
new risk
new relationship event
new Story Situation
```

---

# Character Profession Actions

Professions should create autonomous behavior.

Examples:

```text
Doctor:
Treats patients

Farmer:
Plants / harvests

Trader:
Seeks markets

Engineer:
Repairs systems

Radio Operator:
Maintains communications

Security Officer:
Responds to threats
```

Characters should continue performing these roles between player interactions.

---

# Character Workload

World conditions may alter character workload.

Example:

```text
Infrastructure degradation
      ↓
Engineer workload increases
      ↓
Fatigue increases
      ↓
Availability decreases
```

This may affect whether the character can meet the player.

---

# Character Availability

Conceptual states:

```text
AVAILABLE
BUSY
OVERLOADED
TRAVELING
UNAVAILABLE
MISSING
```

---

# Busy Character

The player may arrive and discover:

```text
Character cannot immediately talk.
```

This makes professions feel real.

---

# Character Stress

Broad conceptual states:

```text
LOW
MODERATE
HIGH
SEVERE
```

Stress may influence:

- risk tolerance
- patience
- communication
- planning
- relationship behavior

It should not replace personality.

---

# Stress Versus Behavior

Avoid universal rules such as:

```text
High stress = angry.
```

Different characters may respond through:

```text
withdrawal
focus
humor
irritability
planning
avoidance
```

Personality systems should influence expression.

---

# Character Risk Assessment

Characters decide whether actions are acceptable based upon perceived risk.

Example:

```text
Farmer may refuse dangerous trade trip
despite urgent need.
```

Another character may accept.

---

# Character Agency

Characters should be capable of:

```text
Saying yes.

Saying no.

Changing their mind.

Leaving.

Refusing player request.

Making mistakes.

Acting independently.
```

---

# Characters Can Refuse Player

Player reputation or relationship does not guarantee compliance.

Example:

```text
Player:
"Come with me."
```

Character:

```text
"No. I have patients here."
```

This strengthens character credibility.

---

# Character Goals Can Conflict With Player Goals

Example:

```text
Player wants:
Character to remain in settlement.

Character wants:
Leave to find family.
```

The character should not automatically surrender their goal.

---

# Character-Character Relationships

Characters should possess relationships independent of player.

Examples:

```text
Family
Friends
Colleagues
Rivals
Authority connections
Faction relationships
```

These networks create autonomous social behavior.

---

# Social Network Propagation

Information and needs may move through character relationships.

Example:

```text
Doctor
      ↓
knows Trader
      ↓
Trader knows Player
```

A request may reach player indirectly.

---

# Character Network Relevance

A character not personally known to player may become relevant through:

```text
close contact of known character
```

Example:

```text
Player's friend's daughter is missing.
```

Relationship relevance propagates through the network.

---

# Relationship Distance

Conceptually:

```text
DIRECT
ONE-HOP
EXTENDED
NONE
```

Relevance normally decays with distance.

---

# Character Faction Links

Characters may belong to or work with:

- government
- factions
- companies
- military
- communities
- trade groups

Affiliation affects:

- access
- information
- goals
- requests
- loyalty

---

# Character Loyalty

Possible loyalty targets include:

```text
Family
Community
Faction
Profession
Authority
Ideology
Self
```

Characters may possess competing loyalties.

---

# Loyalty Conflict

Example:

```text
Security officer:

Duty:
Regional authority

Family:
Lives in threatened settlement
```

The character may face an internal conflict.

This can create strong Story Situations without arbitrary drama.

---

# Character Authority

Some characters possess authority.

Examples:

```text
Mayor
Officer
Council Member
Military Commander
Doctor in charge
Faction Leader
```

Authority affects what they can request or order.

---

# Request Versus Order

Authority may change language and consequence.

Example:

```text
Friend:
"Could you help?"
```

versus:

```text
Commanding Officer:
"You're assigned to this route."
```

---

# Character Information Sharing

Characters decide what to share.

Factors may include:

```text
Trust
Classification
Fear
Self-interest
Duty
Relationship
Relevance
```

---

# Withholding Information

Characters may withhold information because:

```text
They are protecting someone.

They fear consequences.

They lack trust.

They are ordered not to disclose.

They believe it is irrelevant.
```

This creates information asymmetry naturally.

---

# Character Deception

Characters may intentionally mislead when consistent with:

- goals
- beliefs
- fear
- self-interest
- faction loyalty

Mission Generation should not create arbitrary deception merely for plot twists.

---

# Character Rumor Transmission

Characters may pass rumors they believe.

Example:

```text
Character:
"I heard the northern bridge was attacked."
```

They may be sincere.

The information may still be false.

---

# Character Memory

Characters should remember meaningful interactions.

Detailed character memory may belong to existing Character or Relationship systems.

Living Campaign Engine should reference memories such as:

```text
Player helped me.

Player lied to me.

Player failed promise.

Player saved family member.

Player abandoned settlement.
```

---

# Character Memory Versus Campaign Memory

```text
CHARACTER MEMORY

What this character remembers.
```

```text
CAMPAIGN MEMORY

What the campaign needs to preserve.
```

These may overlap.

They should not be assumed identical.

---

# Character Reaction

Characters respond to player actions based upon:

```text
Outcome
Knowledge
Relationship
Expectations
Values
Personal Consequences
```

---

# Outcome Versus Perception

Example:

```text
Player saves hospital.
```

Character may not know the player was responsible.

Therefore:

```text
No relationship improvement.
```

World result exists.

Social credit requires information.

---

# Misattributed Outcomes

Characters may credit the wrong actor.

Example:

```text
Player secretly repairs system.

Public believes authority fixed it.
```

This is valid.

---

# Character Gratitude

Gratitude should not automatically mean:

```text
+10 Reputation
```

It may appear as:

- trust
- future help
- information
- changed dialogue
- willingness to take risk
- relationship development

---

# Character Resentment

Likewise, negative responses may persist through:

- reduced trust
- refusal
- gossip
- faction consequences
- changed plans

---

# Character Needs May Compete

Example:

```text
Doctor:
Needs fuel.

Farmer:
Needs fuel.

Trader:
Wants fuel for transport.
```

Each character's request is rational.

The campaign conflict emerges from scarcity.

---

# No Villain Requirement

Character conflict does not require one side to be wrong.

Characters may possess:

```text
LEGITIMATE
BUT INCOMPATIBLE
GOALS
```

---

# Character Conflict

Possible forms include:

```text
Resource disagreement
Political disagreement
Relationship conflict
Professional conflict
Territorial dispute
Value conflict
```

Combat is only one possible extreme outcome.

---

# Character Cooperation

Characters may also independently cooperate.

Example:

```text
Farmer and mechanic establish
shared fuel pool.
```

This may resolve a World Event without player action.

---

# Character Coalition

Repeated cooperation may create:

```text
new institution
new faction
new relationship network
```

Character behavior may therefore influence Society and Authority.

---

# Character Migration

Characters may relocate because of:

- family
- work
- security
- opportunity
- migration
- faction activity
- player action

Character location must remain dynamic.

---

# Migration Consequences

A known character relocating may change:

```text
relationship proximity
contactability
campaign relevance
regional knowledge
future hooks
```

---

# Character Separation

Characters may become separated from the player through:

```text
migration
communication failure
conflict
travel
```

Separation itself can be meaningful without automatically generating a Mission.

---

# Character Disappearance

A character may become:

```text
MISSING
```

when:

```text
expected contact fails
+
location unknown
```

This does not mean:

```text
DEAD
```

The distinction must remain.

---

# Missing Character State

Conceptually:

```text
KNOWN LOCATION
EXPECTED LOCATION
OVERDUE
MISSING
PRESUMED LOST
CONFIRMED DEAD
```

---

# Character Death

Character death should arise from:

- World Simulation
- player action
- narrative boundaries where intentionally authored

It should not occur randomly merely to create emotional content.

---

# Death Information

The player may not know immediately that a character died.

Possible states:

```text
Actual State:
Dead

Player Knowledge:
Missing
```

This can persist.

---

# Character Survival

Important characters should not possess invisible immunity unless canonical narrative requires it.

Likewise, they should not be targeted simply because they are important.

---

# Character Replacement

If a functional role becomes vacant:

```text
Doctor dies.
```

World systems may eventually produce:

```text
New doctor
Promoted assistant
Reduced healthcare capacity
```

The role exists independently of a specific character.

---

# Character Significance

Characters may possess different simulation resolution.

Conceptually:

```text
PRIMARY
IMPORTANT
RECURRING
LOCAL
BACKGROUND
```

---

# Primary Characters

High-detail persistent simulation.

May track:

```text
Goals
Plans
Knowledge
Relationships
Memory
Location
Resources
```

---

# Important Characters

Moderate detail.

Tracked when relevant to active Story Situations.

---

# Recurring Characters

Persistent identity but lower continuous simulation detail.

---

# Local Characters

Generated or maintained for local context.

May be promoted if relationships develop.

---

# Background Characters

Represent population context.

Not individually simulated over long periods unless promoted.

---

# Character Promotion

A low-resolution character may become more important when:

- player forms relationship
- character becomes politically important
- character becomes involved in major event
- repeated interaction occurs

Example:

```text
Random mechanic
      ↓
Player repeatedly works with mechanic
      ↓
Recurring Character
```

---

# Character Demotion

A character may become less simulation-intensive when:

- player leaves region
- relationship fades
- narrative relevance declines

The character should not cease existing.

Their detailed simulation may be compressed.

---

# Character Compression

When off-screen for long periods:

```text
Goals
Major events
Location
Relationships
```

may be tracked at lower resolution.

Routine daily behavior need not be simulated individually.

---

# Character Return

When a compressed character becomes relevant again:

```text
Reconstruct current state
from:
World history
Character goals
Location
Relationships
Major events
```

The character should feel as though they continued living.

---

# Recurring Character Principle

A recurring character should have:

```text
LIFE BETWEEN MEETINGS
```

When player returns after six months, something should often have changed:

- job
- relationship
- opinion
- family
- location
- goals
- circumstances

---

# Character Routine

Characters may possess normal routines.

Examples:

```text
Work
Meals
Travel
Rest
Social activity
Community duties
```

Routine makes interruptions meaningful.

---

# Routine Disruption

World Events may alter routine.

Example:

```text
Fuel shortage
      ↓
Trader travels less
```

This can become an Environmental or Character Hook.

---

# Character Initiative

Characters may initiate:

```text
conversation
trade
travel
cooperation
conflict
request
information sharing
relationship development
```

without player prompting.

---

# Character Contact Frequency

Repeated contact should depend upon:

```text
Relationship
Need
Personality
Distance
Communication
Recent contact
```

Avoid every known character constantly messaging the player.

---

# Contact Saturation

If several characters are affected by one Event Cluster, Character Integration should coordinate with Story Hooks to avoid:

```text
five identical messages
```

Each contact should add:

- perspective
- information
- emotion
- conflict
- opportunity

or not occur.

---

# Character Selection for Hooks

When several characters could communicate an event, consider:

```text
Knowledge

Relationship

Relevance Path

Motivation

Contactability

Novelty

Pacing
```

---

# Dominant Character Hook

Example:

Fuel crisis affects:

```text
Doctor
Farmer
Trader
Council Member
```

Player's strongest relevant relationship:

```text
Doctor
```

The first Character Hook may naturally come from Doctor.

Later hooks may introduce other perspectives if useful.

---

# Character Contact Should Not Replace Environment

Even when known characters exist, Story Hooks should still use:

- environment
- radio
- markets
- direct observation

Characters are one interface, not the only interface.

---

# Character and Mission Generation

Character Integration provides Mission Generation with:

```text
Need
Goal
Knowledge
Reason to ask player
Desired Outcome
Alternatives
Expectation
```

Mission Generation determines whether formal Mission structure is useful.

---

# Character-Origin Mission Flow

Conceptually:

```text
WORLD EVENT
      ↓
CHARACTER AFFECTED
      ↓
CHARACTER NEED
      ↓
CHARACTER PLAN
      ↓
PLAYER IDENTIFIED AS POSSIBLE RESOURCE
      ↓
CONTACT
      ↓
REQUEST
      ↓
PLAYER RESPONSE
      │
      ├── Help directly
      ├── Decline
      ├── Investigate
      └── Commit
             ↓
       Mission if useful
```

---

# Player as Character Resource

The player may be treated by characters as:

```text
friend
professional
trader
political contact
protector
technician
courier
```

depending upon campaign history.

This is how player role gains social meaning.

---

# Player Reliability

Characters should remember whether the player:

```text
usually fulfills promises
often arrives late
takes high risks
keeps information confidential
charges high prices
```

This changes future requests.

---

# Reliable Player

May receive:

```text
more sensitive
more urgent
higher-responsibility
requests
```

---

# Unreliable Player

Characters may:

```text
ask someone else
withhold critical responsibility
require payment or proof
```

---

# Reputation Versus Personal Relationship

A player may have:

```text
Excellent regional reputation
```

but:

```text
Poor relationship with one character.
```

The character may still refuse help.

Conversely:

```text
Bad public reputation
```

but:

```text
Close friend
```

may still trust them.

---

# Character Values

Characters may prioritize values such as:

```text
Family
Duty
Freedom
Order
Community
Profit
Knowledge
Faith
Security
Technology
Autonomy
```

Values help explain decisions.

Detailed value/personality systems may live elsewhere.

---

# Values and Requests

Example:

Two authority characters face same shortage.

Character A values:

```text
Order
```

and supports rationing.

Character B values:

```text
Local autonomy
```

and prefers voluntary agreements.

Both remain rational.

---

# Character Change

Characters should be capable of changing through:

- experience
- relationships
- trauma
- success
- failure
- political change
- aging
- new responsibilities

---

# No Static Personality Principle

Character identity should be persistent.

Character state should not be frozen.

---

# Character Arcs

Narrative systems may identify emerging arcs from:

```text
GOALS
+
WORLD EVENTS
+
PLAYER INTERACTION
+
CHARACTER CHANGE
```

Character Integration supplies the causal history.

Narrative shapes presentation.

---

# Character Arc Without Player

Some arcs should occur largely without player participation.

Example:

```text
Local trader
      ↓
Builds trade network
      ↓
Becomes regional political actor
```

The player may witness or influence the process without causing all of it.

---

# Character Opportunity

World Events may create opportunities for characters.

Example:

```text
New trade route opens.
```

Trader may:

```text
expand business.
```

Engineer may:

```text
move to new infrastructure project.
```

Player may hear about the consequences later.

---

# Character Failure

Characters may make bad decisions.

Bad decisions should emerge from:

- imperfect information
- stress
- values
- limited resources
- risk tolerance

not arbitrary incompetence.

---

# Character Competence

Competent characters should often solve ordinary problems without player intervention.

This makes the world more believable and makes genuine requests more meaningful.

---

# Player Importance Principle

The player becomes important because:

```text
RELATIONSHIPS
+
CAPABILITY
+
HISTORY
+
CHOICES
```

not because every character somehow recognizes them as the protagonist.

---

# Character Integration With World Simulation

Characters both consume and affect World State.

Example:

```text
Supply shortage
      ↓
Trader changes route
      ↓
New regional supply flow
      ↓
Supply State changes
```

Individual characters may have systemic impact when their role supports it.

---

# Character Integration With Population State

Individual behavior emerges within population context.

Example:

```text
Regional Migration Pressure:
HIGH
```

does not force every character to migrate.

It increases the contextual pressure affecting their decisions.

---

# Character Integration With Authority

Authority characters may:

- make decisions
- issue orders
- implement policy
- disagree internally

Characters give institutions human agency.

---

# Character Integration With Security

Characters may be:

- threatened
- security actors
- witnesses
- organizers
- victims
- negotiators

Security events affect personal plans.

---

# Character Integration With Information

Characters are both:

```text
INFORMATION CONSUMERS
```

and:

```text
INFORMATION SOURCES
```

Their knowledge quality matters.

---

# Character Integration With Supply

Supply determines what characters can:

- buy
- trade
- consume
- repair
- deliver

Character actions may change distribution.

---

# Character Integration With Campaign Memory

Significant character interactions should be eligible for Campaign Memory.

Examples:

```text
First meeting

Major promise

Betrayal

Rescue

Death

Reunion

Relationship turning point
```

---

# Character Event

Important autonomous character changes may produce Character Event Candidates.

Examples:

```text
Character relocates.

Character becomes faction leader.

Character loses family member.

Character completes major project.

Character disappears.

Character changes allegiance.
```

These may enter:

```text
World Event Intake
```

when sufficiently significant.

---

# Character Event Principle

Character Integration does not bypass the Living Campaign pipeline.

Conceptually:

```text
CHARACTER ACTION
      ↓
WORLD / CHARACTER STATE CHANGE
      ↓
WORLD EVENT INTAKE
      ↓
RELEVANCE
      ↓
STORY HOOK
```

This preserves consistency.

---

# Character Contact Example

World State:

```text
Fuel:
CONSTRAINED
```

Character:

```text
Mara

Profession:
Doctor

Relationship:
Close

Hospital generator reserve:
14 hours

Alternatives:
Authority contacted
No response yet
```

Character decision:

```text
Contact Player:
YES
```

Reason:

```text
Player has transport contacts
+
high trust
+
time pressure
```

Possible message:

```text
"If you're near the transport yard,
call me.

We're running shorter than I thought."
```

This is:

```text
Character Hook
```

not automatically:

```text
Mission
```

---

# Character Independent Resolution Example

Player does nothing.

Character:

```text
contacts neighboring clinic
```

Neighbor provides:

```text
limited fuel
```

World result:

```text
Hospital reserve:
14 hours → 30 hours

Crisis:
STABILIZED
```

Later Character Hook:

```text
"We found enough to get through tomorrow."
```

No Mission.

The world lived without the player.

---

# Character Escalation Example

Alternative outcome:

```text
Neighboring clinic cannot help.
```

Hospital reserve:

```text
6 hours.
```

Character:

```text
contacts Player again
```

This second contact is justified because:

```text
WORLD CONDITION WORSENED.
```

Not because:

```text
PLAYER IGNORED FIRST HOOK.
```

---

# Character Relationship Example

Player later secures fuel.

Character knows player was responsible.

Possible changes:

```text
Trust:
Increases

Reliability Memory:
Positive

Future Request Likelihood:
Increases
```

---

# Unknown Credit Example

Player anonymously redirects fuel.

Character does not know.

World result:

```text
Hospital stabilizes.
```

Relationship result:

```text
No direct change.
```

This preserves information causality.

---

# Character Conflict Example

Fuel shortage.

Character A:

```text
Doctor
Needs hospital fuel.
```

Character B:

```text
Farmer
Needs harvest fuel.
```

Both know player.

Both make requests.

The campaign does not decide:

```text
who is morally correct.
```

Player decisions create consequences.

---

# Character Reunion Example

A known character disappears during migration.

Actual State:

```text
Alive
Relocated
Communication Lost
```

Player Knowledge:

```text
Missing
```

Months later:

```text
Regional radio restored.
```

Character sends:

```text
message.
```

Story Hook:

```text
Reunion Opportunity
```

The event emerges naturally from:

```text
Character State
+
Information State
+
Infrastructure Recovery
```

---

# Character Integration Update Cycle

A conceptual update cycle:

```text
1. Read important Character States.

2. Read current World State.

3. Update character location.

4. Update character condition.

5. Update needs.

6. Update responsibilities.

7. Update knowledge.

8. Update beliefs where appropriate.

9. Update resources.

10. Evaluate active goals.

11. Update current plan.

12. Process profession behavior.

13. Process faction and authority obligations.

14. Process relationships.

15. Evaluate communication needs.

16. Evaluate whether to contact player.

17. Process autonomous actions.

18. Apply outcomes to World Simulation.

19. Generate significant Character Events.

20. Update character memories.

21. Compress inactive characters where appropriate.
```

---

# Minimum Character Integration State

A minimum viable important character should expose:

```text
Character ID
Location
Condition
Profession
Responsibilities

Primary Need
Active Goal
Current Plan

Knowledge
Resources

Player Relationship
Faction Links
Authority Links

Availability
Contactability

Recent Significant Event
Memory References
```

Everything beyond this should justify its complexity.

---

# Character Integration Resolution

## High Resolution

Used for:

- close relationships
- active Story Situations
- campaign-critical characters

Tracks:

```text
Goals
Plans
Needs
Knowledge
Resources
Relationships
Actions
Memory
```

---

## Medium Resolution

Used for recurring characters.

Tracks:

```text
Location
Profession
Goal
Major Need
Relationship
Major Events
```

---

## Low Resolution

Used for distant or inactive characters.

Tracks:

```text
Location
Status
Major affiliation
Major life changes
```

Routine behavior may be abstracted.

---

# Character Consistency Rules

## Rule 1

Characters are not Quest Dispensers.

---

## Rule 2

Characters continue acting without player involvement.

---

## Rule 3

Characters may solve problems independently.

---

## Rule 4

Characters may fail independently.

---

## Rule 5

Characters possess limited knowledge.

---

## Rule 6

Characters do not know World Simulation truth automatically.

---

## Rule 7

Characters may hold incorrect beliefs.

---

## Rule 8

Profession influences perspective and behavior.

---

## Rule 9

Needs and goals are separate.

---

## Rule 10

Responsibilities influence decisions.

---

## Rule 11

Characters should possess alternatives before defaulting to player help.

---

## Rule 12

Every direct request should have a plausible reason for involving the player.

---

## Rule 13

Communication requires plausible contactability.

---

## Rule 14

Messages may arrive late.

---

## Rule 15

Characters should not teleport for narrative convenience.

---

## Rule 16

Characters may relocate.

---

## Rule 17

Characters may refuse player requests.

---

## Rule 18

Close relationships do not remove character autonomy.

---

## Rule 19

Character goals may conflict with player goals.

---

## Rule 20

Characters should maintain relationships independent of the player.

---

## Rule 21

Character information sharing depends upon knowledge and motivation.

---

## Rule 22

Character deception requires motive.

---

## Rule 23

Character responses depend upon what they know happened.

---

## Rule 24

Player credit requires plausible information.

---

## Rule 25

Important characters should not possess automatic plot immunity.

---

## Rule 26

Important characters should not be harmed merely for dramatic convenience.

---

## Rule 27

Characters may become more or less simulation-relevant over time.

---

## Rule 28

Recurring characters should have lives between player encounters.

---

## Rule 29

Competent characters should solve ordinary problems frequently.

---

## Rule 30

Character Events should enter the same Event Intake pipeline as other world developments.

---

## Rule 31

Character change should remain causally explainable.

---

## Rule 32

NPC behavior should never depend upon knowing that the player is the protagonist.

---

# Guiding Questions

For every important character action, the engine should be able to answer:

**Where is this character?**

**What do they need?**

**What do they want?**

**What are they responsible for?**

**What do they know?**

**What do they believe?**

**What resources do they possess?**

**What are they currently trying to do?**

**What alternatives do they have?**

**Who do they trust?**

**Why would they contact the player?**

**Can they actually contact the player?**

**What will they do if the player refuses?**

**What happens if their plan succeeds?**

**What happens if it fails?**

**What will they remember?**

If these questions cannot be answered, the character is probably functioning as a plot device rather than a simulated person.

---

# Core Design Principle

Project Ascension should strive for:

```text
THE CHARACTER HAS A LIFE.

THE WORLD CHANGES THAT LIFE.

THE CHARACTER RESPONDS.

THE PLAYER MAY BECOME INVOLVED.
```

rather than:

```text
THE PLAYER ARRIVES.

THE CHARACTER ACTIVATES.
```

This distinction is central to the Living Campaign Engine.

---

# Architectural Result

Characters now become active participants in the same causal world as:

```text
Player
Factions
Authorities
Communities
World Systems
```

This creates the possibility that:

```text
A CHARACTER
```

may:

```text
solve a crisis

create a crisis

discover something

form a faction

leave the region

repair infrastructure

change political alignment

help another character

fail

survive

die

return years later
```

without those outcomes existing solely for player content.

---

# Living Campaign Pipeline

With Character Integration established:

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
      ├──────────────┐
      │              │
      ▼              ▼
PLAYER          CHARACTERS
      │              │
      │              ├── Goals
      │              ├── Needs
      │              ├── Plans
      │              └── Actions
      │              │
      └──────┬───────┘
             ▼
      MISSION GENERATION
        when appropriate
             │
             ▼
        WORLD RESULT
```

The player and characters now inhabit the same campaign loop.

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
Canon/Systems/Living_Campaign_Engine/Consequence_Propagation.md
```

We can now model:

```text
WORLD
      ↓
CHARACTER
      ↓
PLAYER
      ↓
ACTION
```

The next system must answer:

```text
WHAT HAPPENS AFTERWARD?
```

`Consequence_Propagation.md` should define:

- direct consequences
- indirect consequences
- delayed consequences
- hidden consequences
- relationship consequences
- faction consequences
- world-state consequences
- character consequences
- regional propagation
- multi-hop consequences
- consequence decay
- positive feedback
- negative feedback
- unintended consequences
- consequence visibility
- causal attribution
- Butterfly effects
- World Ledger integration

This is where the Living Campaign Engine closes the loop:

```text
PLAYER ACTION
      ↓
WORLD CHANGES
      ↓
NEW EVENTS
      ↓
NEW STORIES
```

Without consequence propagation, player agency is temporary.

With it, the campaign develops history.

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial Character Integration framework established for character autonomy, needs, goals, knowledge, planning, professions, relationships, requests, independent action, contact behavior, migration, memory and campaign interaction. |