# PROJECT ASCENSION
# Character State System

| Field | Value |
|--------|-------|
| System | Characters |
| Document | Character State |
| Location | Canon/Systems/Characters/Character_State.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Canonical Individual Character State Model |
| Last Updated | 2026-08-09 |

> *"A character is not a dialogue tree. A character is a changing state inside a changing world."*

---

# Purpose

The Character State system defines the canonical state model used to represent an individual persistent character in Project Ascension.

It establishes:

```text
WHAT A CHARACTER IS

WHAT STATE BELONGS TO THE CHARACTER

WHAT OTHER SYSTEMS MAY READ

WHAT OTHER SYSTEMS MAY MODIFY

HOW CHARACTER STATE CHANGES

HOW HISTORY REMAINS TRACEABLE
```

This document does not attempt to fully define:

```text
needs

motivation

planning

decision making

relationships

life simulation

aging

profession

memory behavior
```

Those are expanded in dedicated Character System documents.

Instead, this file establishes the shared:

```text
CHARACTER STATE CONTRACT
```

used by all those systems.

---

# Core Principle

A persistent character should have a state that can answer:

```text
WHO ARE THEY?

WHERE ARE THEY?

WHAT CONDITION ARE THEY IN?

WHAT ARE THEY DOING?

WHAT DO THEY NEED?

WHAT DO THEY WANT?

WHAT DO THEY KNOW?

WHAT DO THEY BELIEVE?

WHAT CAN THEY DO?

WHO MATTERS TO THEM?

WHAT ARE THEY PLANNING?

WHAT HAS HAPPENED TO THEM?

HOW MUCH DETAIL ARE WE CURRENTLY SIMULATING?
```

---

# Canonical Character State

Conceptually:

```text
CHARACTER STATE
│
├── Identity
├── Temporal State
├── Location
├── Physical State
├── Mental / Emotional Context
├── Needs
├── Motivations
├── Goals
├── Plans
├── Knowledge
├── Beliefs
├── Personality
├── Values
├── Profession
├── Skills
├── Capabilities
├── Resources
├── Social Roles
├── Relationships
├── Reputation Context
├── Responsibilities
├── Current Activity
├── Commitments
├── Memory References
├── Life History
├── Simulation Resolution
└── State Metadata
```

---

# Character Identity

Every persistent character must possess a stable identity.

Minimum identity fields:

```text
Character ID

Name

Birth Date or Approximate Age

Origin

Current Identity Status
```

Optional identity fields may include:

```text
Aliases

Former Names

Preferred Name

Pronouns

Languages

Cultural Background

Nationality

Citizenship

Former Citizenship

Family Name History
```

---

# Character ID

Every persistent character must have:

```text
ONE STABLE UNIQUE ID.
```

Example:

```text
CHAR-000184
```

Character ID should not change if:

```text
the character changes name

gets married

changes profession

moves region

changes faction

changes social status.
```

---

# Character ID Principle

```text
IDENTITY LABELS MAY CHANGE.

CHARACTER ID DOES NOT.
```

---

# Name

Character names may contain:

```text
Given Name

Middle Name

Family Name

Nickname

Alias
```

The system should distinguish between:

```text
LEGAL / FORMAL NAME

KNOWN NAME

PREFERRED NAME

ALIAS
```

where relevant.

---

# Age

Age must derive from:

```text
WORLD DATE
-
BIRTH DATE
```

where possible.

Avoid storing:

```text
Age = 37
```

as the sole canonical value for persistent characters.

Prefer:

```text
Birth Date:
2014-06-18
```

which allows:

```text
automatic aging.
```

---

# Approximate Birth Data

Not every character needs precise birth information.

Valid examples:

```text
Birth Year:
2021

Birth Range:
2018–2020

Approximate Age:
Early 40s
```

Resolution may depend on character importance.

---

# Temporal State

Characters exist in time.

Character State should track:

```text
Last Simulation Update

Last High-Resolution Update

Last Known Player Contact

Last Known Location Update

State Effective Date
```

These fields help determine:

```text
how current the state is

whether reconstruction is required

whether information is stale.
```

---

# State Effective Date

Every Character State snapshot should conceptually answer:

```text
WHEN WAS THIS TRUE?
```

Example:

```text
State Effective Date:
2055-09-03 14:20
```

This is important because:

```text
CHARACTER STATE
IS NOT TIMELESS.
```

---

# Location State

Every persistent character should have a current location or location estimate.

Conceptually:

```text
LOCATION STATE

Region

Settlement

Specific Site

Travel State

Destination

Location Confidence

Last Confirmed
```

---

# Location Precision

Location precision depends upon simulation resolution.

High resolution:

```text
Winchester Regional Hospital
Second Floor
Medical Administration
```

Medium resolution:

```text
Winchester
```

Low resolution:

```text
Shenandoah Valley
```

Background:

```text
Regional Population Aggregate
```

---

# Unknown Location

The system must support:

```text
UNKNOWN.
```

Example:

```text
Current Location:
UNKNOWN

Last Confirmed:
Roanoke

Last Confirmed Date:
2054-11-12
```

Do not invent a current location merely because one is convenient.

---

# Travel State

Characters may be:

```text
STATIONARY

TRAVELING

RELOCATING

MISSING

DISPLACED

UNKNOWN
```

Travel State may include:

```text
Origin

Destination

Route

Departure Time

Expected Arrival

Travel Method

Travel Risk
```

---

# Physical State

Character physical state may include:

```text
Health

Injury

Illness

Fatigue

Hunger

Thirst

Sleep

Mobility

Physical Stress

Pregnancy

Disability

Recovery
```

Not every field must always be active.

---

# Physical Condition

Conceptual summary:

```text
HEALTHY

STRAINED

INJURED

ILL

CRITICAL

RECOVERING

DISABLED

DYING

DECEASED
```

Detailed state belongs to more specialized systems where required.

---

# Death State

If:

```text
Character Status:
DECEASED
```

the Character State should retain:

```text
Date of Death

Location of Death

Known Cause

Confidence

Known By

Legacy References
```

The character record should not be deleted.

---

# Character Existence Status

Recommended conceptual states:

```text
ACTIVE

INACTIVE

MISSING

UNCONFIRMED

DECEASED

HISTORICAL
```

---

# Active

Character is alive and persistent in current simulation.

---

# Inactive

Character remains alive but currently requires little or no individual simulation.

---

# Missing

Character was expected to be locatable but current whereabouts are unknown.

---

# Unconfirmed

Character survival itself may be uncertain.

---

# Deceased

Death is established as World Truth.

---

# Historical

Character is no longer an active living entity but remains relevant through:

```text
history

memory

institutions

family

legacy.
```

---

# Mental and Emotional Context

Character State may include current emotional context.

This should not be treated as:

```text
ONE PERMANENT EMOTION.
```

Instead it may include:

```text
Current Mood

Emotional Pressure

Fear

Hope

Anger

Grief

Confidence

Stress

Attachment

Concern
```

where relevant.

---

# Emotional State Principle

```text
EMOTION
MODIFIES DECISION MAKING.

IT DOES NOT
REPLACE CHARACTER IDENTITY.
```

---

# Emotional Context

Example:

```text
Current Mood:
TENSE

Primary Concern:
Hospital staffing

Stress:
HIGH

Grief:
LOW

Confidence:
MODERATE
```

This provides situational context without reducing the character to:

```text
ANGRY NPC.
```

---

# Emotional Duration

Emotional states may have different durations.

Examples:

```text
Momentary irritation:
SHORT

Fear during regional crisis:
SHORT / MEDIUM

Grief after family death:
LONG

Long-term resentment:
RELATIONSHIP / MEMORY DRIVEN
```

---

# Needs State

Character State should expose current active needs.

Conceptually:

```text
NEED

Type

Current Pressure

Minimum Requirement

Satisfaction

Urgency

Source

Expected Change
```

---

# Example

```text
Need:
Income

Pressure:
HIGH

Urgency:
MODERATE

Source:
Employment loss
```

---

# Need Priority

Needs may be:

```text
LOW

MODERATE

HIGH

CRITICAL
```

But:

```text
NEED PRIORITY
```

should not automatically equal:

```text
GOAL PRIORITY.
```

Values and responsibilities may override immediate personal needs.

---

# Motivation State

Character State may expose current motivations.

Example:

```text
Protect family

Preserve professional reputation

Keep clinic operational

Avoid dependence on regional authority
```

Motivation is expanded in:

```text
Needs_and_Motivation.md
```

---

# Goal State

Every persistent character may have multiple active goals.

Conceptually:

```text
GOAL

Goal ID

Description

Origin

Priority

Urgency

Importance

Status

Target State

Time Horizon

Dependencies

Related Actors

Related Locations

Current Progress
```

---

# Goal ID

Example:

```text
GOAL-CHAR184-004
```

Goal IDs allow plans and memories to reference:

```text
the same continuing intention.
```

---

# Goal Status

Recommended conceptual states:

```text
LATENT

ACTIVE

PAUSED

BLOCKED

AT RISK

ACHIEVED

FAILED

ABANDONED

IMPOSSIBLE

TRANSFORMED
```

---

# Latent Goal

A desire exists but the character is not actively pursuing it.

---

# Active Goal

The character currently intends to pursue it.

---

# Paused Goal

Temporarily deprioritized.

---

# Blocked Goal

Character wants to proceed but cannot.

---

# At Risk Goal

Conditions threaten likely completion.

---

# Achieved Goal

Target state reached.

---

# Failed Goal

The character attempted but outcome did not succeed.

---

# Abandoned Goal

Character voluntarily stopped pursuing it.

---

# Impossible Goal

World conditions make current formulation impossible.

---

# Transformed Goal

Goal changed into a different objective.

---

# Goal Hierarchy

Goals may be related.

Example:

```text
LIFE GOAL:
Protect family stability

      ↓

MEDIUM GOAL:
Maintain reliable income

      ↓

SHORT GOAL:
Keep workshop operating

      ↓

IMMEDIATE GOAL:
Acquire replacement bearing
```

This helps explain:

```text
WHY AN IMMEDIATE ACTION MATTERS.
```

---

# Plan State

Plans operationalize goals.

Conceptually:

```text
PLAN

Plan ID

Related Goal

Current Step

Expected Steps

Required Resources

Required Actors

Known Risks

Status

Fallback Options
```

---

# Plan Status

Possible:

```text
FORMING

ACTIVE

WAITING

BLOCKED

ADAPTING

SUCCEEDED

FAILED

ABANDONED
```

---

# Current Plan

Character State should expose:

```text
WHAT THE CHARACTER
IS CURRENTLY TRYING TO DO.
```

This is one of the most important fields for autonomy.

---

# Example

```text
Goal:
Maintain hospital fuel reserve.

Current Plan:
Request increased regional allocation.

Fallback:
Contact private suppliers.

Player Dependency:
NONE.
```

---

# Player Dependency

Plans may explicitly record whether the player is currently required.

Recommended:

```text
NONE

OPTIONAL

USEFUL

IMPORTANT

REQUIRED
```

Most character plans should normally begin as:

```text
NONE
```

unless there is a causal reason otherwise.

---

# Knowledge State

Character State must keep knowledge separate from World Truth.

Conceptually:

```text
KNOWLEDGE ITEM

Subject

Claim

Source

Acquired Date

Confidence

Freshness

Verification

Visibility

Current Status
```

---

# Knowledge Confidence

Possible:

```text
LOW

MODERATE

HIGH

CONFIRMED
```

---

# Knowledge Freshness

Possible:

```text
CURRENT

RECENT

AGING

STALE

UNKNOWN
```

---

# Knowledge Status

Possible:

```text
BELIEVED TRUE

BELIEVED FALSE

UNCERTAIN

CONTESTED

OUTDATED

SUPERSEDED
```

---

# Knowledge Example

```text
Subject:
Millhaven

Claim:
Travel access is restricted.

Source:
Regional radio

Confidence:
HIGH

Freshness:
RECENT

Status:
BELIEVED TRUE
```

---

# Belief State

Beliefs represent interpretations.

A belief may derive from:

```text
knowledge

personality

values

history

social influence

misinformation.
```

Conceptually:

```text
BELIEF

Subject

Belief Statement

Confidence

Evidence

Counter-Evidence

Origin

Persistence
```

---

# Example

```text
Belief:
Regional authorities react too slowly
to infrastructure failures.

Confidence:
MODERATE

Origin:
Previous outage experience

Persistence:
LONG
```

---

# Knowledge and Belief Boundary

Example:

```text
KNOWLEDGE:
Regional fuel prices increased 20%.

BELIEF:
Large traders are intentionally
restricting supply.
```

Only the first is an observation.

The second is an interpretation.

---

# Personality State

Personality should contain relatively stable traits.

Example dimensions:

```text
Risk Tolerance

Patience

Sociability

Trust Tendency

Competitiveness

Empathy

Discipline

Curiosity

Assertiveness

Adaptability
```

---

# Trait Stability

Personality is:

```text
RELATIVELY STABLE
```

not:

```text
IMMUTABLE.
```

Major experience may produce gradual changes.

---

# Personality Representation

Avoid simplistic universal values such as:

```text
Good = 80
Evil = 20
```

Prefer behavioral tendencies.

Example:

```text
Risk Tolerance:
LOW

Social Confidence:
HIGH

Trust Tendency:
MODERATE

Patience:
HIGH

Adaptability:
HIGH
```

---

# Values State

Character State should expose important values.

Conceptually:

```text
VALUE

Type

Importance

Interpretation

Current Conflict
```

---

# Example

```text
Value:
Local Autonomy

Importance:
HIGH

Interpretation:
Critical systems should remain
under local operational control.
```

---

# Value Conflict

Character State should allow:

```text
VALUE A
```

to conflict with:

```text
VALUE B.
```

Example:

```text
Family Loyalty:
HIGH

Public Duty:
HIGH
```

Current situation:

```text
Family member accused
of public corruption.
```

Decision Making must handle:

```text
INTERNAL VALUE CONFLICT.
```

---

# Profession State

Profession should include:

```text
Current Profession

Current Position

Employer / Organization

Experience

Professional Status

Work Location

Professional Network
```

---

# Profession History

Previous professions should remain in:

```text
Life History
```

rather than being overwritten.

Example:

```text
2042:
Field Doctor

2049:
Medical Coordinator

2055:
Network Director
```

---

# Skills

Character State may expose learned skills.

Examples:

```text
Medicine

Mechanical Repair

Farming

Negotiation

Leadership

Driving

Navigation

Electronics

Trade

Administration

Security

Teaching.
```

---

# Skill Model

Conceptually:

```text
SKILL

Type

Competence

Experience

Recent Use

Certification / Formal Training

Confidence
```

---

# Capability

Capability differs from skill.

Conceptually:

```text
CAPABILITY
=
SKILL
+
CURRENT CONDITION
+
TOOLS
+
RESOURCES
+
ACCESS
+
AUTHORITY
+
TIME.
```

---

# Example

Character:

```text
Expert electrician.
```

But:

```text
No tools

Injured hand

No access to facility.
```

Result:

```text
Skill:
HIGH

Current Capability:
LOW.
```

---

# Capability State

Possible conceptual values:

```text
NONE

LOW

MODERATE

HIGH

EXPERT
```

but actual action feasibility should remain contextual.

---

# Resource State

Characters may control resources.

Examples:

```text
Money

Food

Fuel

Vehicle

Property

Tools

Equipment

Information

Trade Goods

Access Rights.
```

---

# Ownership and Access

Distinguish:

```text
OWNS
```

from:

```text
CAN ACCESS.
```

Example:

```text
Character does not own
hospital ambulance.

But can authorize its use.
```

---

# Resource Entry

Conceptually:

```text
RESOURCE

Type

Quantity

Ownership

Access

Location

Condition

Restrictions
```

---

# Social Roles

A character may hold multiple roles.

Examples:

```text
Parent

Friend

Doctor

Council Member

Neighbor

Mentor

Employer

Faction Member

Community Leader.
```

---

# Role Conflict

Roles may create incompatible expectations.

Example:

```text
Doctor:
Protect patient confidentiality.

Council Member:
Provide public safety information.
```

This can create meaningful decisions.

---

# Responsibilities

Character State may expose obligations arising from:

```text
profession

family

contracts

law

social role

promises

authority

relationship.
```

---

# Responsibility Entry

Conceptually:

```text
RESPONSIBILITY

Subject

Origin

Importance

Deadline

Status

Affected Actors
```

---

# Commitments

Commitments should be explicit when a character has:

```text
promised

agreed

accepted responsibility

signed contract

scheduled action.
```

---

# Commitment State

Possible:

```text
OPEN

IN PROGRESS

FULFILLED

BROKEN

RENEGOTIATED

RELEASED

IMPOSSIBLE
```

---

# Character Commitments and Player

A character may have:

```text
commitments to player
```

or:

```text
commitments involving player.
```

These should not be confused with:

```text
player Missions.
```

---

# Current Activity

Character State should expose what the character is currently doing at appropriate resolution.

High resolution example:

```text
Reviewing hospital inventory
```

Medium resolution:

```text
Working at hospital
```

Low resolution:

```text
Performing professional duties
```

---

# Activity Categories

Possible:

```text
WORKING

TRAVELING

RESTING

SOCIALIZING

EATING

SLEEPING

PLANNING

TRADING

MEETING

CARING

RECOVERING

INVESTIGATING

WAITING

UNKNOWN.
```

---

# Activity Continuity

Current Activity should not arbitrarily reset when:

```text
player enters area.
```

Characters should already be:

```text
DOING SOMETHING.
```

---

# Relationship References

Character State should not duplicate the entire Relationship system.

Instead it may contain:

```text
Relationship IDs

Relationship Type

Current Relevance

Important Obligations

Important Relationship Memories
```

Detailed dynamics belong to:

```text
Canon/Systems/Relationships/
```

---

# Relationship Example

```text
Relationship ID:
REL-CHAR184-PLAYER

Type:
Close Friendship

Current Relevance:
HIGH

Current Tension:
LOW

Important Memory References:
MEM-2045-0103
MEM-2048-0211
```

---

# Reputation Context

Character State may store how the character is perceived by:

```text
groups

institutions

communities

factions

professional networks.
```

This should use references to broader reputation systems if established.

---

# Important Distinction

```text
CHARACTER REPUTATION
```

and:

```text
CHARACTER RELATIONSHIPS
```

are not identical.

Someone may:

```text
dislike a character personally
```

while still believing they are:

```text
professionally reliable.
```

---

# Memory References

Character State should reference meaningful memories rather than storing every historical detail inline.

Examples:

```text
MEM-CHAR184-001

MEM-CHAR184-002

MEM-2051-0617
```

Memory content may belong to:

```text
Character Memory

Campaign Memory

World Ledger
```

depending on context.

---

# Character Memory Ownership

A character memory must conceptually specify:

```text
THE CHARACTER REMEMBERS THIS.
```

Campaign Memory does not automatically mean:

```text
EVERY CHARACTER KNOWS IT.
```

---

# Life History

Life History should contain major state transitions.

Conceptually:

```text
LIFE HISTORY

Date

Event

Previous State

New State

Cause

References
```

---

# Example

```text
2049-03-12

Event:
Promoted to Medical Network Director

Previous Role:
Regional Medical Coordinator

New Role:
Director

Cause:
Network expansion
+
previous coordination experience
```

---

# Life History Principle

Do not record:

```text
every meal

every workday

every conversation.
```

Record:

```text
MEANINGFUL STATE TRANSITIONS.
```

---

# Character State Snapshot

A conceptual Character State snapshot may look like:

```text
CHARACTER STATE

Character ID:
CHAR-000184

Name:
Mara Vale

Status:
ACTIVE

Birth Date:
2013-04-09

Current Date:
2055-09-03

Age:
42

Location:
Winchester

Specific Site:
Valley Medical Coordination Network

Physical Condition:
HEALTHY

Current Mood:
SURPRISED / EMOTIONALLY ACTIVATED

Profession:
Physician

Position:
Network Director

Primary Role:
Medical Leader

Current Needs:
Maintain medical resilience
Personal reconnection

Primary Goals:
Expand specialist network
Maintain organizational stability

Current Plan:
Prepare quarterly regional medical review

Knowledge:
Player has returned to Winchester
CONFIRMED

Beliefs:
Interregional medical cooperation
remains essential

Personality:
Disciplined
Empathetic
Direct
Pragmatic

Values:
Duty
Medical Access
Professional Integrity
Community

Current Capability:
HIGH within medical organization

Important Relationships:
Player
Daughter
Medical Leadership Team
Elias Mercer

Current Player Relationship:
Historically Close
Currently Reconnecting

Current Activity:
Speaking with player

Simulation Resolution:
HIGH

Last Update:
2055-09-03 14:20
```

---

# State Change Example

Before:

```text
Location:
Winchester

Profession:
Doctor

Goal:
Improve local clinic
```

World changes:

```text
Regional Medical Network forms.
```

Character action:

```text
Mara joins planning group.
```

Experience accumulates.

Later:

```text
Profession:
Physician

Position:
Regional Medical Coordinator

Goal:
Improve interregional medical resilience
```

The state changed through:

```text
WORLD
+
ACTION
+
TIME
+
EXPERIENCE.
```

---

# State Transition

Conceptually:

```text
OLD CHARACTER STATE
      ↓
WORLD INPUT
      ↓
CHARACTER DECISION
      ↓
ACTION
      ↓
CONSEQUENCE
      ↓
MEMORY
      ↓
NEW CHARACTER STATE
```

---

# State Transition Integrity

Major state changes must have:

```text
CAUSE.
```

Avoid:

```text
Profession:
Mechanic
      ↓
one year later
      ↓
Governor
```

without intermediate history.

---

# Character State Ownership

Different systems may modify different state domains.

Conceptually:

```text
Characters System
├── Identity
├── Goals
├── Plans
├── Knowledge
├── Beliefs
├── Personality
├── Values
├── Capability
└── Development

Life System
├── Household
├── Family Life
├── Employment Context
├── Daily Routine
└── Life Events

Relationships System
├── Trust
├── Closeness
├── Relationship History
├── Expectations
└── Obligations

World Simulation
├── External Conditions
├── Location Environment
├── Supply Exposure
├── Security Exposure
└── Infrastructure Exposure
```

These systems interact through controlled state updates.

---

# External State Versus Character State

Example:

World State:

```text
Fuel Supply:
LOW
```

Character State:

```text
Personal Fuel Reserve:
MODERATE
```

Character Belief:

```text
Fuel shortage will worsen.
```

Character Goal:

```text
Secure additional reserve.
```

These are separate layers.

---

# Character State Should Not Duplicate World State

Avoid:

```text
Character:
Regional Fuel = LOW
```

Instead reference:

```text
Region:
Shenandoah Valley

Character Exposure:
Fuel-dependent profession

Relevant World State:
Supply_State / Fuel = LOW
```

This prevents state divergence.

---

# Derived State

Some Character State values should be:

```text
DERIVED
```

rather than independently stored.

Examples:

```text
Age
from Birth Date.

Current Relationship Relevance
from Relationship system.

Current Environmental Risk
from Location + World State.

Current Trade Opportunity
from Character profession + Market State.
```

---

# Stored Versus Derived

Recommended principle:

```text
STORE
what belongs uniquely
to the character.

DERIVE
what can reliably be calculated
from authoritative external state.
```

---

# State Confidence

Not every Character State field must be perfectly known to every system.

The simulation may know:

```text
World-True Character State
```

while the player or another character does not.

---

# State Visibility

Conceptually:

```text
SIMULATION TRUE

PLAYER KNOWN

CHARACTER KNOWN

PUBLIC

PRIVATE

SECRET

UNKNOWN
```

---

# Example

Simulation State:

```text
Character plans to leave region.
```

Player Knowledge:

```text
UNKNOWN.
```

Relationship System:

```text
May detect emotional distance.
```

Story Hooks:

```text
May reveal plan only
through plausible interaction.
```

---

# Hidden State

Character hidden state may include:

```text
private goals

private relationships

fears

secrets

undisclosed plans

unknown illness

political intentions.
```

Hidden state remains:

```text
REAL.
```

It is simply:

```text
NOT CURRENTLY KNOWN.
```

---

# State Privacy

Private character information should not automatically become:

```text
player-facing
```

because it exists in Character State.

A plausible:

```text
information path
```

is still required.

---

# Character State Validation

A valid Character State should answer:

**Who is this person?**

**Where are they?**

**How old are they?**

**What condition are they in?**

**What are they currently doing?**

**What do they need?**

**What are their active goals?**

**What are they currently planning?**

**What do they know?**

**What do they believe?**

**What are their important values?**

**What can they realistically do?**

**Which relationships currently matter?**

**What commitments do they have?**

**What major history shaped them?**

**At what simulation resolution are they running?**

If several of these cannot be answered for an important persistent character, their state may be underdefined.

---

# Minimum Persistent Character State

A minimum persistent character record should contain:

```text
Character ID

Name

Status

Birth Date / Approximate Age

Location

Physical Condition

Profession / Primary Role

Primary Needs

Active Goals

Current Plan

Key Knowledge

Important Beliefs

Personality Summary

Values Summary

Core Capabilities

Important Relationship References

Current Activity

Major Memory References

Life History Summary

Simulation Resolution

Last Updated
```

---

# High-Resolution Character State

High-resolution characters may additionally contain:

```text
detailed emotional context

short-term needs

multiple active plans

current conversation state

fine-grained knowledge

local resource access

immediate commitments

current schedule

current relationship tension

current environmental exposure.
```

---

# Medium-Resolution Character State

May contain:

```text
major needs

active goals

profession

location

important relationships

major beliefs

current broad plan

important recent events.
```

---

# Low-Resolution Character State

May contain:

```text
location region

profession

major goal

important relationships

major life-state changes

compressed knowledge

long-term trajectory.
```

---

# State Promotion

When a character becomes newly relevant:

```text
LOW
↓
MEDIUM
↓
HIGH
```

the engine may expand Character State using:

```text
existing history

regional history

current location

profession

relationships

goals

life events.
```

---

# State Demotion

When relevance declines:

```text
HIGH
↓
MEDIUM
↓
LOW
```

the engine should compress:

```text
routine detail
```

while retaining:

```text
meaningful state.
```

---

# Promotion Integrity

Promotion must not invent:

```text
new history
```

that contradicts existing records.

It may fill previously unspecified routine detail only where:

```text
causally safe.
```

---

# Demotion Integrity

Demotion must not discard:

```text
open promises

major goals

relationship milestones

critical knowledge

major injuries

life-changing events.
```

---

# Reconstruction Example

Character at last high-resolution state:

```text
2046

Profession:
Mechanic

Location:
Winchester

Goal:
Open own workshop
```

During low-resolution simulation:

```text
2048:
Obtains business loan

2049:
Workshop opens

2051:
Hires assistant

2053:
Expands production
```

Player returns:

```text
2055
```

Reconstructed Character State:

```text
Profession:
Mechanic / Business Owner

Position:
Workshop Owner

Goal:
Expand regional manufacturing

Resources:
Workshop

Employees:
4

Reputation:
Strong local professional reputation
```

The state is explainable.

---

# State Contradictions

Systems must detect impossible combinations.

Examples:

```text
Status:
DECEASED

Current Activity:
Working
```

Invalid.

---

```text
Location:
Winchester

Current Activity:
Driving convoy in Roanoke
```

potentially invalid.

---

```text
Profession:
Doctor

Skill:
Medicine NONE
```

requires explanation.

---

# Contradiction Handling

When contradiction occurs:

```text
DO NOT SILENTLY PICK
WHICHEVER STATE IS CONVENIENT.
```

Instead determine:

```text
authoritative field

timestamp

source

causal transition.
```

---

# State Authority

Each field should ideally have:

```text
Authoritative System

Last Update

Source Event
```

where implementation requires robust synchronization.

---

# Example

```text
Field:
Location

Authority:
Characters

Updated:
2055-09-03 13:51

Source:
Travel Completion
```

---

# Derived State Invalidity

Derived state must be recalculated when source state changes.

Example:

```text
Character Capability:
High
```

may become:

```text
Low
```

after:

```text
serious injury.
```

Do not leave stale capability summaries active.

---

# State Update Ordering

Conceptually:

```text
WORLD CHANGE
      ↓
CHARACTER EXPOSURE
      ↓
PHYSICAL / INFORMATION UPDATE
      ↓
NEED UPDATE
      ↓
GOAL / PLAN EVALUATION
      ↓
ACTION
      ↓
CONSEQUENCE
      ↓
MEMORY
      ↓
STATE COMMIT
```

Exact implementation may vary.

---

# Character State and World Time

Time advancement may change state even without events.

Examples:

```text
age increases

fatigue changes

hunger changes

scheduled activity begins

deadline approaches

pregnancy progresses

recovery progresses

education progresses

employment duration increases.
```

---

# Time-Driven State Change

Therefore:

```text
NO WORLD EVENT
```

does not mean:

```text
NO CHARACTER CHANGE.
```

Time itself is causal.

---

# Character State and Player Time Skip

If player skips:

```text
one day

one month

one year

ten years
```

Character State must advance accordingly at appropriate resolution.

---

# Time Skip Principle

```text
TIME SKIP
≠
CHARACTER PAUSE.
```

---

# Character State and Save / Load

A saved campaign must preserve enough Character State to reconstruct:

```text
current identity

current location

active goals

active plans

important relationships

important memory

important resources

simulation resolution

current lifecycle state.
```

Implementation details belong outside current Canon scope.

---

# Character State and AI

When AI generates:

```text
dialogue

planning suggestions

behavior interpretation
```

it should receive only relevant state.

Example dialogue context:

```text
Identity

Current Situation

Relationship

Knowledge

Beliefs

Mood

Goal

Relevant Memories
```

Avoid providing:

```text
hidden World Truth
```

unless the character plausibly knows it.

---

# AI State Boundary

AI output must not change canonical Character State merely because:

```text
the generated dialogue implied something.
```

State changes should occur through:

```text
validated simulation updates.
```

---

# Example

AI dialogue says:

```text
"My brother lives in Richmond."
```

If Character State contains no brother:

```text
this must not silently become Canon.
```

The dialogue generator should instead be constrained by state.

---

# State and Narrative

Narrative presentation may interpret Character State.

It may not overwrite it for dramatic convenience.

Example:

Character State:

```text
Mara currently in Roanoke.
```

Narrative cannot place her:

```text
in Winchester
```

merely because a scene would be emotionally stronger.

---

# State and Mission Generation

Mission Generation may read:

```text
Character Need

Character Goal

Character Plan

Player Relationship

Player Capability
```

to determine whether a Character-related Mission is plausible.

It must not assume:

```text
CHARACTER NEED
=
MISSION.
```

---

# State and Story Hooks

Story Hooks may read:

```text
Character Activity

Character Knowledge

Relationship

Current Goal

Current Situation
```

to decide how a character could plausibly enter player experience.

---

# State and Campaign Memory

Campaign Memory may reference:

```text
significant Character State transitions.
```

Examples:

```text
became council leader

moved region

married

relationship reconciled

survived disaster

died.
```

---

# State and World Ledger

World Ledger may receive character transitions when they are:

```text
historically significant.
```

Not every Character State change belongs there.

---

# State and Relationships

Relationships may influence:

```text
goal formation

planning

risk tolerance

information sharing

help seeking

emotional state

decision making.
```

Character State should expose enough relationship references for those influences to occur.

---

# State and Life

Life System may produce:

```text
marriage

children

education

employment

household change

retirement.
```

These become:

```text
Character State transitions.
```

---

# State and Society

Society may alter:

```text
social roles

employment

legal status

professional opportunities

political participation

community expectations.
```

Character State receives the individual-level consequences.

---

# State and World Simulation

World Simulation provides:

```text
weather

supply

security

infrastructure

authority

population

information environment.
```

Character State records:

```text
HOW THIS PARTICULAR PERSON
IS AFFECTED.
```

---

# Example

World State:

```text
Regional Security:
UNSTABLE.
```

Character State A:

```text
Lives in fortified town.

Personal Exposure:
LOW.
```

Character State B:

```text
Travels remote trade routes.

Personal Exposure:
HIGH.
```

Same World State.

Different Character State impact.

---

# State and Consequence Propagation

Character actions may produce consequences.

Example:

```text
Character:
Engineer

Action:
Repairs water pump

      ↓

Infrastructure State:
Improves

      ↓

Population Need:
Reduced

      ↓

Character Reputation:
Improves
```

Character State both:

```text
receives
```

and:

```text
creates
```

consequences.

---

# Character State Consistency Rules

## Rule 1

Every persistent character has a stable Character ID.

---

## Rule 2

Character State is time-dependent.

---

## Rule 3

Character State must include a current or estimated location.

---

## Rule 4

Unknown is a valid state.

---

## Rule 5

Character knowledge must remain separate from World Truth.

---

## Rule 6

Beliefs may be incorrect.

---

## Rule 7

Goals may change.

---

## Rule 8

Plans may fail.

---

## Rule 9

Characters may act without player involvement.

---

## Rule 10

Character capability is contextual.

---

## Rule 11

Profession is not identical to capability.

---

## Rule 12

Relationships belong to separate detailed relationship state.

---

## Rule 13

Character State should reference rather than duplicate external authoritative state.

---

## Rule 14

Major state transitions require causal explanation.

---

## Rule 15

Time itself may change Character State.

---

## Rule 16

Player absence does not pause Character State.

---

## Rule 17

Character importance may rise or fall.

---

## Rule 18

Simulation resolution may change.

---

## Rule 19

Compression must preserve meaningful history.

---

## Rule 20

Reconstruction must remain causally consistent.

---

## Rule 21

Character death does not delete Character State history.

---

## Rule 22

Private state does not automatically become player knowledge.

---

## Rule 23

AI-generated content cannot silently invent canonical Character State.

---

## Rule 24

Narrative presentation cannot override canonical Character State.

---

## Rule 25

Mission Generation cannot convert every need into a Mission.

---

## Rule 26

Player relevance and character importance remain separate.

---

## Rule 27

Character State must support contradictory emotions and motivations.

---

## Rule 28

Major relationships should preserve historical context.

---

## Rule 29

State updates should use authoritative system ownership.

---

## Rule 30

Stale derived state must be recalculated.

---

## Rule 31

Characters should already be doing something before player arrival.

---

## Rule 32

A Character State should remain explainable through history.

---

# Guiding Questions

For any persistent character, the engine should be able to answer:

**Who is this person?**

**Where are they now?**

**How certain is that location?**

**What condition are they in?**

**What are they currently doing?**

**What do they need right now?**

**What do they want?**

**Which goal matters most?**

**What are they currently trying to do about it?**

**What do they know?**

**What are they wrong about?**

**What do they believe?**

**Which values are influencing them?**

**What can they realistically do?**

**Which people currently matter to them?**

**What promises or responsibilities exist?**

**What major experiences shaped their present state?**

**What changed since the last time they were relevant?**

**What simulation resolution do they require?**

If these questions cannot be answered, the Character State may not be sufficiently defined for autonomous simulation.

---

# Core State Principle

The Character State system should make it impossible to reduce a character to:

```text
NAME

LOCATION

DIALOGUE

QUEST.
```

Instead:

```text
CHARACTER
=
IDENTITY
+
STATE
+
HISTORY
+
INTENTION
+
CAPABILITY
+
RELATIONSHIPS
+
TIME.
```

---

# Autonomy Principle

A character should be able to exist at:

```text
09:00
```

with:

```text
a location

a goal

a plan

a job

a relationship

a problem

a belief
```

even if:

```text
THE PLAYER NEVER SHOWS UP.
```

At:

```text
17:00
```

their state may be different because:

```text
THEY LIVED THE DAY.
```

---

# Continuity Principle

If the player meets the character again:

```text
TEN YEARS LATER
```

the system should not ask:

```text
WHAT VERSION OF THIS CHARACTER
WOULD MAKE A GOOD SCENE?
```

It should ask:

```text
WHAT HAPPENED TO THIS PERSON
DURING THOSE TEN YEARS?
```

and derive:

```text
CURRENT CHARACTER STATE.
```

---

# Architectural Result

With `Character_State.md` established, the Character System now has a canonical object that the remaining character subsystems can operate upon.

Conceptually:

```text
Character_State.md
      ↓
defines
      ↓
WHO / WHERE / CURRENT STATE

Needs_and_Motivation.md
      ↓
defines
      ↓
WHY PRESSURE EXISTS

Goals_and_Plans.md
      ↓
defines
      ↓
WHAT THEY WANT TO CHANGE

Knowledge_and_Beliefs.md
      ↓
defines
      ↓
WHAT THEY THINK IS TRUE

Decision_Making.md
      ↓
defines
      ↓
HOW THEY CHOOSE

Autonomy_and_Initiative.md
      ↓
defines
      ↓
WHEN THEY ACT

Profession_and_Capability.md
      ↓
defines
      ↓
WHAT THEY CAN DO

Personality_and_Values.md
      ↓
defines
      ↓
HOW THEY TEND TO INTERPRET

Character_Development.md
      ↓
defines
      ↓
HOW THEY CHANGE

Aging_and_Life_Events.md
      ↓
defines
      ↓
HOW LIFE CHANGES THEM

Character_Simulation_Resolution.md
      ↓
defines
      ↓
HOW MUCH DETAIL IS REQUIRED
```

---

# Current Status

```text
CHARACTER SYSTEM

README.md
FOUNDATION DEFINED

Character_State.md
FOUNDATION DEFINED

Needs_and_Motivation.md
PENDING

Goals_and_Plans.md
PENDING

Knowledge_and_Beliefs.md
PENDING

Decision_Making.md
PENDING

Autonomy_and_Initiative.md
PENDING

Profession_and_Capability.md
PENDING

Personality_and_Values.md
PENDING

Character_Development.md
PENDING

Aging_and_Life_Events.md
PENDING

Character_Simulation_Resolution.md
PENDING
```

---

# Next Document

The next recommended document is:

```text
Canon/Systems/Characters/Needs_and_Motivation.md
```

This should define the pressure layer beneath Character Goals.

The central question will be:

```text
WHY DOES THIS CHARACTER
WANT ANYTHING AT ALL?
```

It should establish:

```text
physical needs

social needs

security needs

economic needs

psychological needs

role-based needs

relationship needs

need urgency

need satisfaction

need conflict

motivation formation

competing motivations

need adaptation

chronic pressure

temporary pressure
```

Most importantly:

```text
NEED
MUST NOT DIRECTLY
BECOME ACTION.
```

Instead:

```text
NEED
+
VALUES
+
PERSONALITY
+
KNOWLEDGE
+
RELATIONSHIPS
+
WORLD CONDITIONS
      ↓
MOTIVATION
      ↓
GOAL
```

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial canonical Character State model defining identity, temporal state, location, physical and emotional condition, needs, motivation, goals, plans, knowledge, beliefs, personality, values, profession, skills, capability, resources, roles, responsibilities, commitments, activities, relationship references, memory, life history, simulation resolution, state ownership and transition integrity. |