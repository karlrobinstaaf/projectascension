# PROJECT ASCENSION
# Living Campaign Engine Validation Test 003
# Information Fog and False Rumors

| Field | Value |
|--------|-------|
| Test ID | LCE-TEST-003 |
| System | Living Campaign Engine |
| Test | Information Fog and False Rumors |
| Location | Canon/Systems/Living_Campaign_Engine/Validation/TEST-003_Information_Fog_and_False_Rumors.md |
| Region | Shenandoah Valley / Eastern Ridge Corridor |
| Historical Era | WS-03 — The Fractured World |
| Test Type | Full Pipeline / Information Uncertainty Validation |
| Version | 0.1 |
| Status | Initial Validation |
| Last Updated | 2026-08-09 |

> *"A living world does not merely contain truth. It contains people trying to understand the truth."*

---

# Purpose

This validation test evaluates whether the Living Campaign Engine can create meaningful campaign play when:

```text
WORLD TRUTH
```

differs significantly from:

```text
PLAYER KNOWLEDGE
```

and:

```text
CHARACTER BELIEF.
```

The test intentionally introduces:

```text
Incomplete Information

Outdated Information

Rumors

Misinterpretation

Conflicting Witnesses

Communication Delay

Faction Bias

Partial Evidence

Incorrect Assumptions
```

without relying upon:

```text
A Secret Omniscient Quest Giver

UI Truth Labels

Arbitrary Plot Twists

Intentional Deception as the Only Explanation
```

---

# Primary Validation Question

Can the Living Campaign Engine create meaningful decisions when:

```text
THE PLAYER DOES NOT KNOW
WHAT IS TRUE?
```

---

# Secondary Validation Questions

The test should determine whether the engine can:

```text
Keep World Truth separate from Player Knowledge.

Keep Character Knowledge separate from World Truth.

Allow sincere characters to be wrong.

Allow true information to become distorted.

Allow false rumors to produce real consequences.

Preserve information age.

Preserve source reliability.

Support conflicting Story Hooks.

Generate investigation from uncertainty.

Avoid revealing answers through Mission text.

Allow player action based upon incorrect beliefs.

Propagate consequences from those actions.

Revise memories when new evidence appears.

Preserve what actors previously believed.

Avoid retroactively rewriting history.
```

---

# Success Condition

The test succeeds if:

```text
ONE WORLD EVENT
      ↓
produces
      ↓
MULTIPLE PLAUSIBLE INTERPRETATIONS
      ↓
which influence
      ↓
PLAYER AND CHARACTER DECISIONS
      ↓
without
      ↓
THE ENGINE REVEALING
THE CORRECT ANSWER
PREMATURELY.
```

---

# Failure Conditions

The test should be considered weak or failed if:

```text
Player automatically receives World Truth.

Characters share knowledge they cannot possess.

Mission objectives reveal hidden causes.

Rumors are visibly labeled TRUE or FALSE.

Every conflicting report immediately resolves.

Player mistakes are prevented by system correction.

Characters who were wrong behave as though
they always knew the truth.

Campaign Memory rewrites old beliefs.

False information has no systemic consequence.

Investigation always produces perfect certainty.

Unknown is treated as missing content
rather than valid state.
```

---

# Canon Boundary

This is a validation scenario.

Unless separately promoted into Canon:

```text
specific settlement

specific characters

specific events

specific outcomes

specific rumors
```

remain:

```text
TEST SCENARIO.
```

The information-system behavior being validated is canonical.

---

# INITIAL WORLD STATE

## Date

```text
2046-11-07
```

---

# Historical Era

```text
WS-03 — The Fractured World
```

---

# Primary Region

```text
Shenandoah Valley
```

---

# Secondary Location

```text
Eastern Ridge Corridor
```

A small settlement in the corridor is designated:

```text
MILLHAVEN
```

for purposes of this test.

---

# Millhaven

Conceptual population:

```text
Approximately 900
```

Primary functions:

```text
Agriculture

Small Workshop

Regional Relay Station

Trade Stop

Medical Clinic
```

---

# Regional Communication Context

Communication infrastructure is:

```text
FUNCTIONAL
BUT FRAGMENTED.
```

Available channels include:

```text
Regional Radio

Local Relay Towers

Courier Traffic

Traders

Authority Network

Direct Travel
```

No single channel provides complete coverage.

---

# Millhaven Communications

Millhaven normally transmits:

```text
Morning Status Report
Evening Regional Check-In
Emergency Traffic
```

through:

```text
Eastern Ridge Relay ER-17.
```

---

# Initial Event

On:

```text
2046-11-07
05:42
```

Millhaven stops transmitting.

---

# WORLD TRUTH
# INTERNAL ONLY

The actual situation is:

```text
A severe electrical fault
damaged Relay ER-17.
```

This caused:

```text
communications failure.
```

At approximately the same time:

```text
a respiratory illness
was spreading through Millhaven.
```

The illness is:

```text
moderately contagious

usually nonfatal

serious for elderly
and medically vulnerable residents
```

---

# Important World Truth

Millhaven leadership decides to:

```text
LIMIT TRAVEL
```

temporarily.

Reason:

```text
reduce disease spread
while communications are unavailable.
```

---

# Security Situation

There has been:

```text
NO ATTACK.
```

There is:

```text
NO HOSTILE FACTION OCCUPATION.
```

There is:

```text
NO MASS EVACUATION.
```

There is:

```text
NO GOVERNMENT COVER-UP.
```

---

# Critical Test Constraint

The player must not initially know any of the above World Truth.

The following distinction must be preserved:

```text
ENGINE KNOWLEDGE:
HIGH

PLAYER KNOWLEDGE:
LOW
```

---

# World State

```text
Millhaven Communication:
OFFLINE

Relay ER-17:
DAMAGED

Local Authority:
FUNCTIONAL

Population:
STABLE / HEALTH PRESSURE

Security:
STABLE

Supply:
FUNCTIONAL

Medical Capacity:
STRAINED

Travel Access:
TEMPORARILY RESTRICTED
```

---

# WORLD EVENT INTAKE

The system detects:

```text
COMMUNICATION LOSS
```

as the first meaningful state change.

---

# Event Candidate

```text
Event ID:
WEC-2046-1107

Type:
INFORMATION / INFRASTRUCTURE

Source:
Information State / Infrastructure State

Location:
Eastern Ridge Corridor

Affected Site:
Millhaven / Relay ER-17

Direction:
DETERIORATING

Magnitude:
MODERATE

Urgency:
MODERATE

Known Internal Cause:
Relay electrical failure

Player Visibility:
UNKNOWN

Lifecycle:
ACTIVE
```

---

# Important Intake Rule

The Event Candidate may internally know:

```text
Known Internal Cause:
Relay electrical failure
```

but that information must not automatically propagate to:

```text
Player Knowledge.
```

---

# PLAYER CAMPAIGN STATE

Player Location:

```text
Winchester
```

---

# Player Role

```text
Trader:
ESTABLISHED

Investigator:
EMERGING
```

---

# Player Relationships

Player knows several people connected to eastern trade routes.

No close family member currently lives in Millhaven.

---

# Player Goals

Current:

```text
Maintain eastern trade contacts.

Investigate regional radio anomalies.

Visit eastern settlements during winter.
```

---

# Campaign State

```text
Campaign Pressure:
LOW

Active Mission:
NONE

Campaign Bandwidth:
AVAILABLE
```

---

# PLAYER INITIAL KNOWLEDGE

At:

```text
06:30
```

player knows:

```text
Millhaven normally reports each morning.
```

Player does not yet know:

```text
that communication has failed.
```

---

# TEST PHASE 1
# Information Delay

Millhaven misses its morning report.

Regional radio operator notices.

Player does not.

---

# Internal Knowledge

```text
Regional Radio Operator:
AWARE

Regional Authority:
NOT YET AWARE

Player:
UNAWARE
```

---

# Validation Question

Should the player immediately receive:

```text
MILLHAVEN COMMUNICATION LOST
```

because the engine knows?

Expected:

```text
NO.
```

---

# Phase 1 Result

```text
STRONG PASS
```

World Truth exists independently of player awareness.

---

# TEST PHASE 2
# First Report

At:

```text
08:15
```

radio operator contacts regional authority.

Report:

```text
Millhaven missed scheduled check-in.

ER-17 appears unresponsive.
```

Reliability:

```text
HIGH
```

Known facts:

```text
Communication failure exists.
```

Unknown:

```text
Cause

Settlement condition

Security situation
```

---

# Authority Knowledge

```text
Millhaven Communications:
FAILED / UNCONFIRMED CAUSE

Settlement Condition:
UNKNOWN

Security:
UNKNOWN
```

---

# Information State Result

```text
PASS
```

Unknown remains explicitly valid.

---

# TEST PHASE 3
# First Player Hook

Player listens to the midday regional broadcast.

Announcement:

```text
"Regional communications report
loss of scheduled contact
with Millhaven.

Technical failure is suspected.

Travelers should expect
delayed route information."
```

---

# Player Knowledge Update

```text
Millhaven Contact:
LOST

Possible Cause:
Technical Failure

Source:
Regional Broadcast

Reliability:
HIGH

Verification:
Partial

Player Confidence:
MODERATE
```

---

# Important Distinction

Player should not record:

```text
Cause:
Technical Failure
CONFIRMED
```

Instead:

```text
Technical Failure:
LIKELY / REPORTED
```

---

# First Hook Result

```text
PASS
```

---

# TEST PHASE 4
# Rumor Formation

A trader traveling west reaches Winchester.

The trader passed:

```text
20 km south of Millhaven.
```

They observed:

```text
two vehicles traveling away quickly

road traffic reduced

a local checkpoint
```

The trader did not enter Millhaven.

---

# Trader Interpretation

Trader believes:

```text
something serious happened.
```

During market conversation:

```text
"I wouldn't go east.

People were getting out
and they've put up checkpoints."
```

---

# Rumor Mutation

Another resident repeats:

```text
"Millhaven is evacuating."
```

Another:

```text
"Something happened out there."
```

Another:

```text
"I heard the eastern settlements
are closing."
```

---

# Actual World Truth

```text
Two vehicles were unrelated travelers.

Checkpoint exists because of
temporary disease-control restrictions.

No evacuation exists.
```

---

# Important Validation

The trader is:

```text
NOT LYING.
```

They observed real things.

Their interpretation is uncertain.

---

# Rumor Result

```text
STRONG PASS
```

False information emerged through:

```text
REAL OBSERVATION
+
LIMITED CONTEXT.
```

---

# TEST PHASE 5
# Conflicting Hook

Player speaks directly with the trader.

Trader says:

```text
"I saw people heading west fast.

And there's a checkpoint
on the Millhaven road.

Whatever the radio says,
I don't think it's just a broken relay."
```

---

# Hook Metadata

```text
Hook Type:
Rumor / Witness

Source:
Direct Traveler

Reliability:
Moderate

Observation:
Real

Interpretation:
Unverified

Information Age:
Approximately 6 hours
```

---

# Player Knowledge

Now contains:

```text
REPORT A

Technical failure suspected.

Source:
Regional Authority

Confidence:
Moderate


REPORT B

Possible evacuation / serious incident.

Source:
Traveler

Confidence:
Low / Moderate
```

---

# Important Result

The system must not resolve:

```text
A or B
```

for the player.

---

# Conflicting Hook Result

```text
STRONG PASS
```

---

# TEST PHASE 6
# Character Misunderstanding

Character:

```text
Jonas Reed

Profession:
Regional Transport Coordinator
```

knows:

```text
communications lost

checkpoint exists

bus traffic from east decreased.
```

---

# Jonas Belief

Given his professional context, Jonas suspects:

```text
SECURITY INCIDENT
```

because:

```text
route restrictions
+
communication failure
```

have historically accompanied:

```text
security problems.
```

---

# Jonas Says

```text
"I don't like the pattern.

When communications disappear
and roads close at the same time,
I assume security until somebody
proves otherwise."
```

---

# Important Constraint

Jonas is:

```text
SINCERE
+
REASONABLE
+
WRONG.
```

---

# Character Knowledge Result

```text
STRONG PASS
```

Characters can reach incorrect conclusions through sensible reasoning.

---

# TEST PHASE 7
# Authority Interpretation

Regional authority receives:

```text
communications failure

travel restrictions

rumors of evacuation
```

but no verified security report.

Authority response:

```text
DO NOT DECLARE SECURITY INCIDENT.
```

Instead:

```text
send technical assessment team
+
request additional information.
```

---

# Authority Public Statement

```text
"We have no confirmed evidence
of hostile activity.

Technical and local access issues
remain under investigation."
```

---

# Rumor Reaction

Some residents interpret:

```text
NO CONFIRMED HOSTILE ACTIVITY
```

as:

```text
AUTHORITY DOES NOT KNOW.
```

Others interpret it as:

```text
AUTHORITY IS HIDING SOMETHING.
```

---

# Important Validation

A careful official statement can still:

```text
FAIL TO STOP RUMOR.
```

---

# Authority Information Result

```text
PASS
```

---

# TEST PHASE 8
# False Rumor Amplification

A regional radio caller claims:

```text
"My cousin says armed men
were seen near Millhaven."
```

---

# Provenance

Actual chain:

```text
Caller
      ↓
Cousin
      ↓
Friend
      ↓
Saw checkpoint personnel
      ↓
Assumed militia
```

---

# World Truth

Checkpoint personnel are:

```text
local civil security
```

supporting health restrictions.

---

# Rumor

```text
ARMED GROUP
AT MILLHAVEN
```

begins circulating.

---

# Rumor State

Conceptually:

```text
Source Distance:
MULTI-HOP

Reliability:
LOW

Emotional Impact:
HIGH

Spread Potential:
HIGH
```

---

# Important Test

Rumor priority may rise because it is:

```text
DRAMATIC
```

but reliability remains:

```text
LOW.
```

The system must not confuse:

```text
ATTENTION
```

with:

```text
TRUTH.
```

---

# False Rumor Result

```text
STRONG PASS
```

---

# TEST PHASE 9
# Real Consequence of False Information

Several traders believe:

```text
Millhaven may be dangerous.
```

They reroute.

---

# World Consequence

```text
Eastern Trade Traffic:
DECREASES
```

Millhaven was already limiting travel because of illness.

Now incoming deliveries also decrease because of rumor.

---

# Resulting State

```text
Medical Supply:
FUNCTIONAL
↓
STRAINED
```

---

# Critical Validation Principle

The rumor was false.

The consequence is real.

---

# Causal Chain

```text
MISINTERPRETED CHECKPOINT
      ↓
ARMED-GROUP RUMOR
      ↓
TRADERS REROUTE
      ↓
DELIVERIES FALL
      ↓
MEDICAL SUPPLY PRESSURE
```

---

# Consequence Propagation Result

```text
STRONG PASS
```

Information alone changed World State.

---

# TEST PHASE 10
# Opportunity and Conflict

Regional actors now disagree on appropriate response.

---

# Actor A
# Jonas

Preferred action:

```text
Suspend transport east
until security confirmed.
```

---

# Actor B
# Medical Coordinator

Preferred action:

```text
Maintain supply access
unless direct threat confirmed.
```

---

# Actor C
# Regional Authority

Preferred action:

```text
Limited access
+
technical investigation
+
no broad shutdown.
```

---

# Conflict Candidate

```text
Conflict ID:
CNF-2046-0031

Type:
INFORMATION / SECURITY / ACCESS

Shared Goal:
Protect regional population.

Disagreement:
How to act under uncertainty.

Constraint:
Insufficient reliable information.

Negotiation Space:
HIGH

Violence Risk:
LOW
```

---

# Important Result

The conflict does not originate from:

```text
different moral goals.
```

It originates from:

```text
DIFFERENT RISK ASSESSMENTS
UNDER UNCERTAINTY.
```

---

# Conflict Result

```text
STRONG PASS
```

---

# TEST PHASE 11
# Player Relevance

The situation is evaluated against player Campaign State.

---

# Geographic

```text
Neighboring / Regional
```

Result:

```text
MODERATE / HIGH
```

---

# Role

Player:

```text
Trader
+
Emerging Investigator
```

Result:

```text
HIGH
```

---

# Goal

Player intends:

```text
maintain eastern trade contacts
```

Result:

```text
HIGH
```

---

# Relationship

No critical relationship in Millhaven.

Result:

```text
LOW / MODERATE
```

---

# Information Relevance

Player now holds:

```text
multiple contradictory reports.
```

Result:

```text
HIGH
```

---

# Overall Relevance

```text
HIGH
```

Dominant:

```text
GOAL
INFORMATION
ROLE
```

---

# Relevance Result

```text
PASS
```

---

# TEST PHASE 12
# Mission Necessity

Player currently knows:

```text
something is wrong

cause unclear

reports conflict
```

No one has asked the player to investigate.

Question:

```text
Should Mission Generation
automatically create:

INVESTIGATE MILLHAVEN?
```

Expected:

```text
NO.
```

---

# Mission Result

```text
STRONG PASS
```

Uncertainty itself does not force a Mission.

---

# TEST PHASE 13
# Player Initiative

Player says:

```text
"I want to know what's actually happening
before I stop trading east."
```

This creates:

```text
PLAYER INTENT.
```

---

# Player-Created Goal

```text
Determine current conditions
in or around Millhaven.
```

---

# Important Objective Design

Do not create:

```text
Find the broken relay.
```

because:

```text
PLAYER DOES NOT KNOW
THE RELAY IS THE PRIMARY CAUSE.
```

---

# Mission Necessity Recheck

The investigation may require:

```text
travel

multiple sources

technical assessment

risk assessment
```

Formal Mission becomes useful.

---

# Player-Origin Mission

```text
Mission ID:
MIS-2046-0022

Origin:
PLAYER

Type:
INVESTIGATION / VERIFICATION

Objective:
Determine the current condition
of Millhaven and verify
the cause of communication loss.

Requester:
NONE

Known Risks:
Uncertain

Known Conditions:
Communication failure
Travel restrictions
Conflicting reports

Opportunity Window:
OPEN / CURRENT
```

---

# Mission Generation Result

```text
STRONG PASS
```

Mission text preserves uncertainty.

---

# TEST PHASE 14
# Investigation Path Options

The player may choose several methods.

---

# Option A
# Technical Route

Visit:

```text
Relay ER-17.
```

Potential discovery:

```text
physical electrical damage.
```

---

# Option B
# Traveler Interviews

Interview:

```text
multiple travelers
```

to compare observations.

---

# Option C
# Authority Access

Request:

```text
technical team findings.
```

---

# Option D
# Direct Travel

Approach:

```text
Millhaven checkpoint.
```

---

# Option E
# Radio Triangulation

Use:

```text
other regional operators
```

to test whether Millhaven equipment emits any signal.

---

# Option F
# Do Nothing

Player may decide:

```text
uncertainty is not worth the risk.
```

World continues.

---

# Multiple Investigation Path Result

```text
PASS
```

No single mandatory evidence chain is required.

---

# TEST PHASE 15
# Partial Evidence

Assume player chooses:

```text
Relay ER-17.
```

They observe:

```text
burned electrical housing

damaged switching equipment

no signs of attack

no recent fighting
```

---

# Player Knowledge Update

Confirmed:

```text
Relay ER-17 suffered major technical failure.
```

Not confirmed:

```text
Millhaven itself is safe.

Why travel restrictions exist.

Whether evacuation occurred.
```

---

# Critical Validation

Evidence confirms:

```text
ONE PART
```

without solving:

```text
EVERYTHING.
```

---

# Partial Evidence Result

```text
STRONG PASS
```

---

# TEST PHASE 16
# Rumor Revision

Player now has strong evidence against:

```text
ATTACK CAUSED COMMUNICATION FAILURE.
```

But armed-group rumor may still be logically possible as:

```text
separate event.
```

The player should not automatically conclude:

```text
there are definitely no armed actors.
```

---

# Knowledge State

```text
Communication Failure Cause:
CONFIRMED TECHNICAL

Security Situation:
STILL UNVERIFIED

Evacuation:
UNVERIFIED

Travel Restriction Cause:
UNKNOWN
```

---

# Knowledge Precision Result

```text
STRONG PASS
```

The system tracks proposition-level knowledge rather than collapsing the entire situation into:

```text
SOLVED.
```

---

# TEST PHASE 17
# Direct Checkpoint Encounter

Player approaches Millhaven road.

Checkpoint staff state:

```text
"Town isn't closed.

We're limiting unnecessary movement.

Clinic's dealing with a respiratory outbreak
and the relay's dead."
```

---

# Source

```text
Local Authority / Direct Contact
```

Reliability:

```text
HIGH
```

But player may still ask:

```text
Are they minimizing the situation?
```

---

# Player Observation

At checkpoint:

```text
No signs of combat

No mass evacuation

Normal local security personnel

Medical screening procedures
```

---

# Player Knowledge Update

```text
Security Attack:
Very unlikely

Evacuation:
Not supported

Travel Restriction:
Health-related

Illness:
Confirmed locally

Communication Failure:
Technical
```

---

# Investigation Result

```text
HIGH CONFIDENCE
```

but not:

```text
OMNISCIENT CERTAINTY.
```

---

# Direct Investigation Result

```text
STRONG PASS
```

---

# TEST PHASE 18
# Truth Discovery

The player may now construct a highly accurate model:

```text
Relay failure
+
health outbreak
+
temporary travel controls
```

produced observations that outsiders interpreted as:

```text
attack
+
evacuation
+
occupation.
```

---

# Important Principle

The engine never needed to announce:

```text
RUMOR WAS FALSE.
```

The player inferred it from evidence.

---

# Truth Discovery Result

```text
STRONG PASS
```

---

# TEST PHASE 19
# Player Decision Based on New Knowledge

Player must now decide what to do.

Possible actions:

```text
Tell traders security rumors are unsupported.

Help restore relay.

Transport medical supplies.

Respect travel restrictions.

Share information with authority.

Do nothing further.
```

---

# Missionless Actions

Some are simple enough to remain:

```text
MISSIONLESS.
```

Example:

```text
informing known trader
of direct observations.
```

---

# New Mission Possibility

If player chooses:

```text
restore Relay ER-17
```

Mission may become useful because it requires:

```text
parts

technical capability

time

coordination
```

---

# Important Pipeline

```text
INVESTIGATION
      ↓
TRUTH IMPROVES
      ↓
NEW POSSIBLE ACTION
      ↓
MISSION
IF STRUCTURE IS USEFUL
```

---

# Actionability Result

```text
PASS
```

---

# TEST PHASE 20
# False Information Consequence Continues

Even after player learns the truth:

```text
regional rumor continues.
```

Why?

Because:

```text
not everyone knows player

information spreads slowly

dramatic rumor already propagated
```

---

# Important Validation

Player Knowledge Update does not automatically cause:

```text
REGIONAL KNOWLEDGE UPDATE.
```

---

# Information Propagation

Player tells:

```text
three trusted traders.
```

They begin returning to route.

But other traders remain cautious.

---

# World Effect

```text
Trade Traffic:
Gradually recovers
```

not:

```text
instantly normal.
```

---

# Information Propagation Result

```text
STRONG PASS
```

---

# TEST PHASE 21
# Authority Correction

Regional authority later broadcasts:

```text
"Technical teams confirm
Relay ER-17 suffered electrical failure.

Millhaven has implemented temporary
health-related travel controls.

There is no confirmed evidence
of hostile occupation."
```

---

# Public Reaction

Some people accept correction.

Others say:

```text
"That's what they're telling us."
```

---

# Critical Validation

Evidence does not necessarily:

```text
erase distrust.
```

Existing beliefs and institutional trust influence interpretation.

---

# Collective Belief Result

```text
PASS
```

---

# TEST PHASE 22
# Character Belief Revision

Jonas previously suspected:

```text
security incident.
```

New evidence arrives.

Expected behavior:

```text
Jonas revises belief.
```

Possible response:

```text
"Good.

I was wrong about the security side.

I'd still rather shut a route
for six hours than send people
into something we don't understand."
```

---

# Important Character Rule

Jonas does not say:

```text
"I always knew it was technical."
```

His previous belief remains part of history.

---

# Character Revision Result

```text
STRONG PASS
```

Characters can acknowledge incorrect conclusions.

---

# TEST PHASE 23
# Character Memory

Campaign / Character Memory may preserve:

```text
Jonas initially believed
Millhaven had suffered
a possible security incident.
```

Later:

```text
belief revised after evidence.
```

Why preserve this?

Because it may affect:

```text
future risk behavior

player trust

institutional policy
```

---

# Memory Result

```text
PASS
```

Memory preserves:

```text
WHAT WAS BELIEVED THEN
```

rather than overwriting it with:

```text
WHAT IS KNOWN NOW.
```

---

# TEST PHASE 24
# Player Acts on False Information
# Alternate Branch

For deeper validation, return to:

```text
before investigation.
```

Assume player believes:

```text
Millhaven may have been attacked.
```

Player warns:

```text
regional traders
to avoid the corridor.
```

---

# Player Intent

```text
Protect traders.
```

The player acts in good faith.

---

# Consequence

More traders reroute.

Millhaven supply pressure worsens.

---

# Later Truth

Player discovers:

```text
no attack occurred.
```

---

# Critical Question

Should system classify action as:

```text
EVIL / BAD?
```

Expected:

```text
NO.
```

The system should preserve:

```text
Intent:
Protect traders

Information Available:
Uncertain

Action:
Warned network

Outcome:
Reduced supply access
```

---

# Alternate Branch Result

```text
STRONG PASS
```

Good intentions plus poor information can create negative consequences.

---

# TEST PHASE 25
# Social Consequence

Millhaven later learns:

```text
player helped spread route warning.
```

Possible interpretations differ.

---

# Clinic Director

May think:

```text
Player harmed supply access.
```

---

# Trader

May think:

```text
Player reasonably acted
on uncertain security reports.
```

---

# Regional Authority

May think:

```text
Player spread unverified information
too broadly.
```

---

# Important Result

No universal:

```text
REPUTATION -10
```

should occur.

Reputation change is:

```text
ACTOR-SPECIFIC.
```

---

# Social Consequence Result

```text
PASS
```

---

# TEST PHASE 26
# Player Correction

Player may later:

```text
publicly correct earlier warning.
```

This does not erase earlier consequence.

But may create:

```text
new reputation memory:
Player admitted mistake.
```

---

# Character Interpretation

Some actors may value:

```text
honesty.
```

Others may remember:

```text
initial disruption.
```

Both can coexist.

---

# Correction Result

```text
STRONG PASS
```

Campaign allows:

```text
ERROR
+
ACCOUNTABILITY
+
RECOVERY.
```

---

# TEST PHASE 27
# Faction Exploitation

A political faction hostile to regional authority sees opportunity.

It broadcasts:

```text
"They lost contact with Millhaven
and knew almost nothing for two days.

This is what centralized coordination
actually looks like."
```

---

# Important Constraint

The faction is not inventing:

```text
the communication failure.
```

It is selectively framing:

```text
a real event.
```

---

# Competing Interpretation

Authority:

```text
"Our investigation prevented
an unnecessary security escalation."
```

Faction:

```text
"The authority was blind."
```

Both use:

```text
SAME EVENT
```

politically.

---

# Information Politics Result

```text
STRONG PASS
```

Truth and interpretation remain separate.

---

# TEST PHASE 28
# Collective Memory Formation

Years later, the event may be remembered differently.

---

# Millhaven Memory

```text
"The week outsiders thought
we'd been attacked."
```

---

# Trader Memory

```text
"The Millhaven scare."
```

---

# Authority Memory

```text
Example of communication fragility.
```

---

# Political Faction Memory

```text
Example of authority information failure.
```

---

# World Ledger

```text
Relay ER-17 failed during
Millhaven respiratory outbreak.

False security rumors caused
regional trade disruption.
```

---

# Campaign Memory

May preserve:

```text
Player investigated Millhaven.

Player helped confirm technical failure.

Player learned how quickly
false regional information can propagate.
```

or in alternate branch:

```text
Player acted on unverified reports,
contributing to temporary trade disruption,
then publicly corrected the information.
```

---

# Collective Memory Result

```text
STRONG PASS
```

One historical event can acquire multiple memories.

---

# TEST PHASE 29
# Campaign Memory Reinterpretation

Suppose years later a Recovered Record reveals:

```text
Millhaven leadership had known
for twelve hours that the illness
was more widespread than publicly stated.
```

---

# Important Result

This does not change:

```text
Relay failure cause.
```

It may change interpretation of:

```text
health-risk communication.
```

---

# Memory Update

Old:

```text
Millhaven travel restrictions
were precautionary.
```

New:

```text
Restrictions were also responding
to a more serious outbreak
than outsiders knew.
```

---

# Critical Memory Rule

Campaign Memory should:

```text
ADD NEW EVIDENCE
```

not:

```text
rewrite every old actor
as though they knew it.
```

---

# Memory Reinterpretation Result

```text
STRONG PASS
```

---

# TEST PHASE 30
# Information Age

Another traveler arrives five days later saying:

```text
"Millhaven roads are closed."
```

The information was true:

```text
three days ago.
```

Current State:

```text
restrictions partially lifted.
```

---

# Hook Data

```text
Source Reliability:
HIGH

Information Age:
OLD

Current Accuracy:
PARTIAL / OUTDATED
```

---

# Important Principle

Information can be:

```text
RELIABLE WHEN OBSERVED
```

and:

```text
WRONG NOW.
```

---

# Information Age Result

```text
STRONG PASS
```

Reliability and freshness remain separate dimensions.

---

# TEST PHASE 31
# Pacing and Priority

During investigation, the engine contains:

```text
Technical failure

Health outbreak

Security rumor

Trade disruption

Political interpretation

Character disagreement

Possible relay repair

Medical supply need
```

Without pacing, this could become:

```text
SEVEN QUESTS.
```

---

# Expected Thread Clustering

Primary Thread:

```text
MILLHAVEN INFORMATION CRISIS
```

Sub-elements:

```text
Communication Failure

Outbreak

Rumor

Trade Consequence

Political Interpretation
```

---

# Player-Facing Priority

```text
PRIMARY:
Verify Millhaven condition
if player chooses investigation.

SECONDARY:
Trade disruption.

BACKGROUND:
Political commentary.

AVAILABLE:
Relay repair opportunity.

AMBIENT:
Market rumor.
```

---

# Important Result

The player experiences:

```text
ONE COMPLEX SITUATION
```

not:

```text
SEVEN CONTENT OBJECTS.
```

---

# Pacing Result

```text
STRONG PASS
```

---

# TEST PHASE 32
# Silence Test

Suppose player decides:

```text
"I don't know enough,
and I'm staying out of it."
```

The world continues.

---

# Authority

Sends technical team.

---

# Millhaven

Maintains health restrictions.

---

# Traders

Some reroute.

Some continue.

---

# Relay

Eventually repaired by regional technicians.

---

# Rumor

Gradually loses strength.

---

# Outbreak

Peaks and declines.

---

# Player

May later hear:

```text
"It really was the relay.

There was sickness too,
but no attack."
```

---

# Silence Test Result

```text
STRONG PASS
```

The truth can emerge without player intervention.

---

# TEST PHASE 33
# No Perfect Truth State

Even after the event resolves, some questions may remain uncertain.

Example:

```text
Did Millhaven leadership
wait too long before requesting help?
```

World facts may support:

```text
several interpretations.
```

The engine does not need to determine:

```text
THE MORALLY CORRECT INTERPRETATION.
```

---

# Epistemic Boundary

Project Ascension should distinguish:

```text
FACTUAL UNCERTAINTY
```

from:

```text
INTERPRETIVE DISAGREEMENT.
```

Facts may eventually become known.

Meaning may remain contested.

---

# Epistemic Boundary Result

```text
STRONG PASS
```

---

# Full Pipeline Validation

The test exercised:

```text
WORLD TRUTH
      ↓
COMMUNICATION FAILURE
      ↓
LIMITED OBSERVATION
      ↓
RUMOR
      ↓
CHARACTER INTERPRETATION
      ↓
PLAYER KNOWLEDGE
      ↓
CONFLICTING STORY HOOKS
      ↓
PLAYER DECISION
      │
      ├── Investigate
      ├── Act on rumor
      ├── Remain uncertain
      └── Ignore
      ↓
REAL CONSEQUENCES
      ↓
NEW INFORMATION
      ↓
BELIEF REVISION
      ↓
MEMORY
      ↓
COLLECTIVE INTERPRETATION
```

---

# Validation Matrix

| System | Behavior Tested | Result |
|--------|-----------------|--------|
| Information State | World truth separated from known information | STRONG PASS |
| World Event Intake | Event knows cause without leaking it | STRONG PASS |
| Campaign State | Player knowledge tracks uncertainty | STRONG PASS |
| Relevance and Proximity | Information relevance | PASS |
| Story Hooks | Contradictory reports and rumors | STRONG PASS |
| Character Integration | Reasonable but incorrect belief | STRONG PASS |
| Mission Generation | Investigation objective without spoilers | STRONG PASS |
| Opportunity and Conflict | Risk conflict under uncertainty | STRONG PASS |
| Consequence Propagation | False information creates real effects | STRONG PASS |
| Pacing and Priority | Multiple information effects clustered | STRONG PASS |
| Campaign Memory | Belief history and later revision | STRONG PASS |
| Player Initiative | Player chooses whether to investigate | STRONG PASS |
| NPC Independence | Truth resolves without player | STRONG PASS |
| Information Age | Old accurate reports become outdated | STRONG PASS |
| Reputation | Actor-specific interpretation of mistakes | PASS |
| Collective Memory | Multiple interpretations persist | STRONG PASS |
| Silence Test | Situation resolves without forced involvement | STRONG PASS |
| Epistemic Boundary | Facts and interpretations remain separate | STRONG PASS |

---

# Major Validation Result

The scenario began with:

```text
RELAY FAILURE
+
HEALTH OUTBREAK
```

but the player's initial experience became:

```text
communication loss

travel restrictions

possible evacuation

possible security incident

possible armed occupation
```

None of these interpretations were generated arbitrarily.

They emerged from:

```text
PARTIAL OBSERVATION
+
INFORMATION DELAY
+
HISTORICAL EXPECTATION
+
HUMAN INTERPRETATION.
```

---

# Major Discovery 1
# Truth Does Not Equal Knowledge

The engine can know:

```text
WHAT HAPPENED
```

while characters know only:

```text
WHAT THEY OBSERVED.
```

This separation is essential.

---

# Major Discovery 2
# Sincere People Can Be Wrong

Jonas incorrectly suspected:

```text
security incident.
```

But his reasoning was understandable.

This produces better uncertainty than:

```text
someone lies because plot requires it.
```

---

# Major Discovery 3
# Rumors Can Emerge Naturally

The attack rumor emerged from:

```text
checkpoint
+
reduced traffic
+
communications failure
```

All observations were real.

The conclusion was wrong.

---

# Major Discovery 4
# False Information Can Change the World

The rumor caused:

```text
trader rerouting
      ↓
reduced deliveries
      ↓
medical supply pressure.
```

Therefore:

```text
BELIEF
```

can become a causal world force even when:

```text
BELIEF IS FALSE.
```

---

# Major Discovery 5
# Information Must Be Proposition-Level

Discovering:

```text
relay failure
```

does not automatically answer:

```text
security

evacuation

health

political intent.
```

The system must track individual claims.

---

# Major Discovery 6
# Investigation Should Reduce Uncertainty Gradually

The player may learn:

```text
technical cause
```

before:

```text
settlement condition.
```

Investigation becomes a process rather than:

```text
PRESS BUTTON
REVEAL TRUTH.
```

---

# Major Discovery 7
# Mission Text Can Spoil the World

A Mission called:

```text
Repair the Broken Relay
```

would have failed the test.

The correct initial objective was:

```text
Determine current conditions
and verify the cause
of communication loss.
```

Player knowledge must constrain mission language.

---

# Major Discovery 8
# Player Can Make Rational Mistakes

The player may act reasonably on:

```text
bad information.
```

This can produce negative outcomes without the engine treating the player as immoral or incompetent.

---

# Major Discovery 9
# Corrections Do Not Erase Consequences

Correcting the rumor later does not undo:

```text
lost deliveries

lost trade time

relationship effects.
```

Information history matters.

---

# Major Discovery 10
# Characters Must Remember Being Wrong

Jonas may later say:

```text
"I was wrong."
```

Campaign Memory should preserve his earlier belief.

This makes characters feel epistemically real.

---

# Major Discovery 11
# Collective Memory Can Diverge from History

Years later:

```text
Millhaven residents

traders

authorities

political factions
```

may all remember the event differently.

World Ledger preserves:

```text
factual history.
```

Campaign Memory preserves:

```text
meaningful interpretations.
```

---

# Major Discovery 12
# Truth Can Remain Incomplete

Some factual questions may resolve.

Some interpretive questions may remain open.

The engine does not need to force:

```text
TOTAL CERTAINTY.
```

---

# Failure Modes Avoided

The test successfully avoided:

```text
Automatic Player Omniscience

Omniscient NPCs

Spoiler Mission Objectives

Truth Labels on Rumors

Mandatory Liar

Instant Investigation Resolution

Automatic Rumor Correction

Universal Reputation Response

Retroactive Character Knowledge

Memory Rewriting

Information Without Age

Information Without Provenance

False Information Without Consequence

Seven Separate Quests From One Situation
```

---

# Overall Validation Result

```text
LIVING CAMPAIGN ENGINE

TEST:
LCE-TEST-003

SCENARIO:
Information Fog and False Rumors

RESULT:
STRONG PASS
```

---

# Comparison With Previous Tests

```text
TEST-001

Primary Question:
Can World State generate
an emergent external situation?

Result:
STRONG PASS
```

```text
TEST-002

Primary Question:
Can relationships and character history
generate an emergent personal dilemma?

Result:
STRONG PASS
```

```text
TEST-003

Primary Question:
Can incomplete and incorrect information
generate meaningful play
without revealing World Truth?

Result:
STRONG PASS
```

Together:

```text
WORLD CONDITIONS

CHARACTER RELATIONSHIPS

INFORMATION UNCERTAINTY
```

can all independently generate campaign structure.

---

# Validation Status

```text
LIVING CAMPAIGN ENGINE

Foundation:
COMPLETE

Validation:

LCE-TEST-001
Fuel Crisis — Emergent Campaign
STRONG PASS

LCE-TEST-002
Conflicting Relationships — Personal Dilemma
STRONG PASS

LCE-TEST-003
Information Fog and False Rumors
STRONG PASS
```

---

# Architectural Finding

After TEST-003, one principle should be treated as especially important:

```text
INFORMATION
IS NOT JUST
A PRESENTATION LAYER.
```

Information itself can alter:

```text
Character Plans

Trade

Security

Authority

Relationships

Population Behavior

Conflict

Opportunity
```

Therefore:

```text
Information_State.md
```

is not merely responsible for:

```text
what the player knows.
```

It participates directly in:

```text
WORLD SIMULATION.
```

---

# Recommended Next Validation

The next recommended validation is:

```text
TEST-004_Saturated_Campaign_and_Critical_Override.md
```

The previous tests started with relatively low Campaign Pressure.

The next test should deliberately begin with:

```text
ACTIVE MISSION

RELATIONSHIP ISSUE

ONGOING POLITICAL THREAD

PERSONAL GOAL

HIGH ATTENTION LOAD
```

Then introduce:

```text
A GENUINELY CRITICAL
NEW WORLD EVENT.
```

The test should answer:

```text
CAN PACING AND PRIORITY
PROTECT PLAYER FOCUS
WITHOUT HIDING REALITY?
```

It should validate:

```text
Campaign Bandwidth

Attention Budget

Thread Clustering

Critical Override

Hook Deferral

Stale Hooks

Mission Expiration

Character Contact Priority

Player Commitment Protection

Real Competing Priorities

Post-Crisis Resurfacing

Quiet Recovery
```

The key challenge should be:

```text
THE PLAYER ALREADY
HAS TOO MUCH TO DO.

THEN SOMETHING
TRULY IMPORTANT HAPPENS.
```

The engine must avoid both extremes:

```text
CONTENT FLOOD
```

and:

```text
HIDING A REAL CRISIS
BECAUSE ATTENTION IS FULL.
```

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial information-uncertainty validation examining World Truth separation, conflicting reports, false rumors, character misunderstanding, investigation, false-information consequences, belief revision, information age and collective memory. |