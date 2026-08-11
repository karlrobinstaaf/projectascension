# PROJECT ASCENSION
# Aurora State

| Field | Value |
|---|---|
| Project | Project Ascension |
| System | Aurora |
| Document | Aurora State |
| Location | `Canon/Systems/AI/Aurora/Aurora_State.md` |
| Version | 1.0 |
| Status | ACTIVE |
| Purpose | Define the persistent canonical state carried by Aurora across simulation time |
| Last Updated | 2026-08-10 |

> **Aurora is not what the world knows. Aurora is what Aurora currently has reason to believe about the world.**

---

# 1. Purpose

This document defines the canonical persistent state of:

```text
AURORA.
```

Aurora State represents:

```text
WHAT AURORA CURRENTLY KNOWS

WHAT AURORA CURRENTLY BELIEVES

WHAT AURORA IS UNCERTAIN ABOUT

WHAT AURORA REMEMBERS

WHAT SOURCES AURORA TRUSTS

WHAT MODELS AURORA MAINTAINS

WHAT AURORA CAN CURRENTLY ACCESS

WHAT AURORA IS CURRENTLY PRIORITIZING

WHAT AURORA IS CURRENTLY TRYING
TO UNDERSTAND.
```

Aurora State must persist across:

```text
simulation ticks

time advancement

player absence

regional transitions

communication failures

system outages

belief corrections

new evidence

source changes

crises.
```

Aurora State is therefore:

```text
THE CONTINUITY
OF AURORA'S
INFORMATIONAL EXISTENCE.
```

---

# 2. Foundational Rule

Aurora State must never be treated as:

```text
WORLD STATE.
```

The relationship is:

```text
WORLD STATE
↓
OBSERVATION / INFORMATION
↓
AURORA STATE.
```

Not:

```text
WORLD STATE
=
AURORA STATE.
```

---

# 3. Core Distinction

Project Ascension must preserve:

```text
WORLD TRUTH

AURORA OBSERVATION

AURORA KNOWLEDGE

AURORA BELIEF

AURORA INFERENCE

AURORA MEMORY

AURORA PREDICTION

AURORA ATTENTION

AURORA COMMUNICATION.
```

These are related.

They are not interchangeable.

---

# 4. Aurora State Overview

Aurora State should conceptually contain:

```text
Aurora_State
|
+-- Identity
|
+-- Operational_Status
|
+-- Time_State
|
+-- Access_State
|
+-- Source_Registry
|
+-- Observation_State
|
+-- Knowledge_State
|
+-- Belief_State
|
+-- Uncertainty_State
|
+-- Contradiction_State
|
+-- Memory_State
|
+-- Character_Models
|
+-- World_Model
|
+-- Organizational_Models
|
+-- Infrastructure_Models
|
+-- Active_Inferences
|
+-- Predictions
|
+-- Attention_State
|
+-- Priority_State
|
+-- Communication_State
|
+-- Active_Questions
|
+-- Open_Information_Gaps
|
+-- Learning_State
|
+-- Failure_State.
```

---

# 5. Aurora Identity

Aurora must possess persistent identity.

Conceptually:

```text
Aurora_ID

Instance_ID

Version

Role

Authority_Profile

Operational_Domain

Created_At

Current_Time

Current_Region_Context.
```

---

# 6. Identity Invariant

Aurora must not become:

```text
a different Aurora
```

merely because:

```text
a region changes

a session restarts

a simulation tick advances

new information arrives

a belief changes.
```

Persistent identity must survive:

```text
STATE CHANGE.
```

---

# 7. Operational Status

Aurora State must track whether Aurora is:

```text
FULLY OPERATIONAL

DEGRADED

PARTIALLY CONNECTED

REGIONALLY PARTITIONED

LOCAL-ONLY

CRITICAL-MODE

OFFLINE.
```

Operational status affects:

```text
what Aurora can observe

what Aurora can access

what Aurora can communicate

what Aurora can infer

how quickly Aurora can react.
```

---

# 8. Operational Status Is Not Knowledge

Aurora becoming degraded does not automatically mean:

```text
Aurora forgets
everything.
```

Likewise:

```text
restored connectivity
```

does not automatically make:

```text
all missing information
appear instantly.
```

The difference between:

```text
MEMORY

ACCESS

CURRENT OBSERVATION
```

must remain explicit.

---

# 9. Time State

Aurora State must preserve temporal context.

At minimum:

```text
Current_Simulation_Time

Last_Update_Time

Last_Synchronization_Time

Last_Confirmed_Time
per important record

Information_Age

Expected_Update_Frequency.
```

---

# 10. Time Is Part of Meaning

The statement:

```text
"Hospital reserve is 62%."
```

is incomplete without:

```text
WHEN?
```

Therefore important Aurora records should retain:

```text
VALUE

TIMESTAMP

SOURCE

CONFIDENCE.
```

---

# 11. Access State

Aurora must maintain explicit information about:

```text
which systems
are currently accessible.
```

Example:

```text
Regional Traffic Network:
AVAILABLE

Hospital Capacity Feed:
AVAILABLE / RESTRICTED

Private Patient Records:
NO ACCESS

Power Grid Telemetry:
PARTIAL

Emergency Communications:
DEGRADED

Public Internet:
UNAVAILABLE.
```

---

# 12. Access Changes Over Time

Access can become:

```text
granted

revoked

degraded

temporarily elevated

partitioned

restored.
```

Every change should have:

```text
cause

time

scope

authority
```

when relevant.

---

# 13. Access Is Not Entitlement

A system being technically reachable does not imply:

```text
Aurora is authorized
to use all data within it.
```

Aurora State must distinguish:

```text
CONNECTIVITY

from

PERMISSION.
```

---

# 14. Source Registry

Aurora must maintain models of information sources.

Each source may have:

```text
Source_ID

Source_Type

Owner

Domain

Access_Level

Historical_Reliability

Current_Reliability

Latency

Coverage

Known_Bias

Failure_State

Last_Seen

Trust_Profile.
```

---

# 15. Source Types

Potential source classes include:

```text
SENSOR

DATABASE

CHARACTER

ORGANIZATION

PUBLIC FEED

GOVERNMENT SYSTEM

PRIVATE SYSTEM

PLAYER

AURORA OBSERVATION

DOCUMENT

ARCHIVE

RUMOR

SECONDARY REPORT.
```

---

# 16. Source Reliability

Aurora may estimate source reliability.

Example:

```text
Calibrated Sensor:
0.98 historical reliability

Local Operator:
0.91

Player:
0.86

Anonymous Message:
0.31
```

Exact implementation may differ.

The key principle is:

```text
SOURCE TRUST
MUST BE DISTINCT
FROM CLAIM CONFIDENCE.
```

---

# 17. Claim Confidence

A highly reliable source can produce:

```text
low-confidence claim
```

if:

```text
observation was poor

data was partial

timestamp was old.
```

A low-reliability source can accidentally provide:

```text
correct information.
```

Therefore:

```text
SOURCE RELIABILITY
≠
CLAIM TRUTH.
```

---

# 18. Observation State

Aurora must preserve direct or system-mediated observations.

Each observation should conceptually contain:

```text
Observation_ID

Subject

Observed_Value

Timestamp

Source

Method

Quality

Confidence

Raw_or_Derived

Integrity_State.
```

---

# 19. Observation vs Knowledge

An observation is:

```text
something Aurora
received or detected.
```

Knowledge is:

```text
what Aurora has accepted
as sufficiently supported.
```

Not every observation should automatically become:

```text
accepted knowledge.
```

---

# 20. Example

Observation:

```text
Anonymous radio message:
"Bridge 14 is gone."
```

Aurora should not automatically convert this to:

```text
Knowledge:
Bridge 14 destroyed.
```

Instead:

```text
Reported Claim:
Bridge 14 destroyed

Source:
Unknown radio sender

Confidence:
LOW.
```

---

# 21. Knowledge State

Aurora Knowledge represents:

```text
information Aurora currently
accepts as sufficiently supported.
```

Possible fields:

```text
Knowledge_ID

Subject

Predicate

Value

Confidence

Source_Set

First_Known

Last_Confirmed

Last_Updated

Freshness

Scope

Sensitivity

Access_Class.
```

---

# 22. Knowledge Is Revisable

Aurora Knowledge may change.

Example:

```text
09:00
Road open

12:00
Road blocked

17:00
Road reopened.
```

Knowledge history must preserve:

```text
TIME.
```

The system must not treat:

```text
latest value
```

as though:

```text
it was always true.
```

---

# 23. Belief State

Aurora Belief represents:

```text
what Aurora currently
believes is probably true.
```

Beliefs may exist when:

```text
direct confirmation
is unavailable.
```

Possible fields:

```text
Belief_ID

Subject

Hypothesis

Confidence

Supporting_Evidence

Contradicting_Evidence

Created

Last_Updated

Status.
```

---

# 24. Belief Status

Potential states:

```text
ACTIVE

WEAKENING

STRENGTHENING

DISPUTED

SUPERSEDED

REJECTED

CONFIRMED.
```

---

# 25. Knowledge vs Belief

Example:

```text
KNOWN:
Grid telemetry stopped.

BELIEVED:
Substation failure likely.

SUSPECTED:
Transformer fire possible.

UNKNOWN:
Root cause.
```

Aurora State must preserve these distinctions.

---

# 26. Inference State

Aurora may create inferences from existing evidence.

Example:

```text
KNOWN:
Hospital generator active.

KNOWN:
Fuel delivery missed.

KNOWN:
Tank capacity known.

INFERENCE:
Hospital fuel likely critical
within 12–16 hours.
```

Inference record should retain:

```text
inputs

logic

assumptions

confidence

time horizon.
```

---

# 27. Inference Provenance

Every important inference should be explainable through:

```text
WHAT EVIDENCE
DID AURORA USE?
```

This is essential for:

```text
debugging

player trust

correction

explainability.
```

---

# 28. Uncertainty State

Aurora must explicitly represent uncertainty.

Possible uncertainty objects:

```text
Unknown current status

Conflicting source reports

Missing observation

Low-confidence inference

Stale information

Ambiguous identity

Incomplete causal chain

Unverified rumor.
```

---

# 29. Uncertainty Is State

Uncertainty must not be represented as:

```text
absence of data only.
```

It may be an explicit active condition.

Example:

```text
Bridge 14 Status:
UNCERTAIN

Reason:
Telemetry unavailable
and conflicting reports exist.
```

---

# 30. Information Gap State

Aurora should be able to track:

```text
WHAT IT DOES NOT KNOW
BUT NEEDS TO KNOW.
```

Example:

```text
Information_Gap_ID:
IG-442

Question:
Is Route 33 passable?

Importance:
HIGH

Needed_By:
Evacuation planning

Current Evidence:
Insufficient

Preferred Sources:
Road authority
field observation
satellite imagery.
```

---

# 31. Active Questions

Aurora may maintain active questions such as:

```text
What caused Substation 4 failure?

Is Hospital North still operating?

Has the convoy reached Harrisonburg?

Is the player report corroborated?

Is the bridge physically passable?
```

These can guide:

```text
sensor requests

communication

reasoning

attention.
```

---

# 32. Contradiction State

Aurora must preserve unresolved contradictions.

Example:

```text
Claim A:
Bridge open

Claim B:
Bridge destroyed.
```

The contradiction object may contain:

```text
Contradiction_ID

Subject

Claims

Sources

Timestamps

Confidence

Severity

Operational_Impact

Resolution_Status.
```

---

# 33. Contradiction Resolution

Aurora may resolve contradictions through:

```text
new evidence

source comparison

timestamp analysis

causal reasoning

direct observation

trusted authority confirmation.
```

It must not:

```text
choose arbitrarily
because one answer
is more convenient.
```

---

# 34. Memory State

Aurora memory should preserve:

```text
important information history

prior beliefs

corrections

source behavior

events

warnings

predictions

character interactions

system failures

important decisions.
```

---

# 35. Memory Types

Potential Aurora memory classes:

```text
EPISODIC

SEMANTIC

SOURCE_HISTORY

CHARACTER_HISTORY

INCIDENT_HISTORY

SYSTEM_HISTORY

PREDICTION_HISTORY

CORRECTION_HISTORY.
```

---

# 36. Episodic Memory

Example:

```text
2038-10-14
Charlottesville cold-storage failure

Aurora received conflicting
inventory estimates

later confirmed major stock loss.
```

---

# 37. Semantic Memory

Example:

```text
Charlottesville cold storage
has recurring refrigeration vulnerability.
```

This is broader than:

```text
one event.
```

---

# 38. Source History Memory

Aurora may remember:

```text
Source X
has repeatedly overestimated
repair completion times.
```

This can influence:

```text
future confidence.
```

---

# 39. Correction History

Aurora should remember meaningful cases where:

```text
it was wrong.
```

Example:

```text
Initial Assessment:
Bridge likely operational.

Final Truth:
Bridge collapsed.

Cause of Error:
stale telemetry
+
delayed field reporting.
```

This enables:

```text
LEARNING.
```

---

# 40. Memory Compression

Aurora does not need to preserve:

```text
every raw packet

every repeated identical sensor value

every redundant notification.
```

It should preserve:

```text
meaningful changes

important uncertainty

relevant provenance

historically significant correction.
```

---

# 41. Character Models

Aurora must maintain models of relevant characters.

A Character Model is:

```text
AURORA'S BELIEF
ABOUT A PERSON.
```

It is not:

```text
the person's true Character State.
```

---

# 42. Character Model Fields

Conceptually:

```text
Character_ID

Known_Name

Known_Location

Known_Profession

Known_Organization

Known_Capabilities

Observed_Behavior

Known_Relationships

Suspected_Goals

Known_Authority

Known_Access

Reliability_Assessment

Risk_Assessment

Current_Status

Last_Confirmed

Confidence.
```

---

# 43. Character Model Boundaries

Aurora must not automatically include:

```text
private fears

private memories

hidden Goals

secret relationships

internal motivations.
```

These require:

```text
evidence.
```

---

# 44. Character Model Updates

Character models may update through:

```text
direct communication

third-party reports

observed behavior

organizational records

public information

repeated interactions.
```

---

# 45. Character Model Uncertainty

Aurora may know:

```text
Profession:
Engineer
```

while only suspecting:

```text
Current Goal:
Restore Substation 4.
```

Model confidence must be field-sensitive.

---

# 46. World Model

Aurora's World Model represents:

```text
Aurora's current model
of broader world conditions.
```

It may include:

```text
regions

infrastructure

resources

population trends

transport

weather

security

healthcare

communications

organizations

active incidents.
```

---

# 47. World Model Is Not World State

This distinction is mandatory:

```text
WORLD MODEL
≠
WORLD STATE.
```

The World Model may contain:

```text
unknowns

uncertainty

stale data

incorrect beliefs

incomplete coverage.
```

---

# 48. Regional Model

Aurora may maintain region-specific state.

Example:

```text
Region:
Shenandoah Valley

Power:
DEGRADED

Healthcare:
STRESSED

Transport:
PARTIAL

Communications:
UNSTABLE

Supply:
DECLINING

Confidence:
MODERATE.
```

---

# 49. Organizational Models

Aurora may model institutions.

Example:

```text
Organization:
Regional Water Cooperative

Known Leader:
Sarah Bennett

Authority:
Water infrastructure

Current Capacity:
Reduced

Current Risk:
Moderate

Reliability:
High

Information Freshness:
2 hours.
```

---

# 50. Infrastructure Models

Aurora may maintain models of:

```text
power

water

communications

roads

rail

fuel

healthcare

supply chains.
```

Each may include:

```text
status

capacity

dependency

known failures

confidence

last confirmation

predicted risk.
```

---

# 51. Dependency Models

Aurora should understand that systems depend on other systems.

Example:

```text
Hospital
↓
Electricity
↓
Fuel
↓
Road Transport
↓
Fuel Depot
↓
Communications.
```

This enables:

```text
systemic reasoning.
```

---

# 52. Predictions

Aurora State may contain active predictions.

Each prediction should conceptually include:

```text
Prediction_ID

Subject

Predicted_Event

Probability

Time_Horizon

Assumptions

Evidence

Confidence

Created

Expires

Outcome.
```

---

# 53. Prediction Outcome

Predictions may become:

```text
CONFIRMED

PARTIALLY CONFIRMED

FAILED

INVALIDATED

UNRESOLVED.
```

Prediction history supports:

```text
learning.
```

---

# 54. Attention State

Aurora cannot actively focus on everything.

Attention State represents:

```text
WHAT AURORA
IS CURRENTLY
PROCESSING WITH PRIORITY.
```

Possible fields:

```text
Focus_ID

Subject

Priority

Urgency

Impact

Confidence

Reason

Escalation_Level

Start_Time

Expiry.
```

---

# 55. Priority

Aurora priority may depend on:

```text
human safety

infrastructure risk

scope

urgency

causal reach

uncertainty

confidence

time sensitivity

active objectives

dependency count.
```

---

# 56. Priority Is Not Truth

Something may be:

```text
high priority
```

and still:

```text
uncertain.
```

Likewise something may be:

```text
certain
```

but:

```text
low priority.
```

---

# 57. Attention Saturation

Aurora may enter:

```text
SATURATED
```

state when incoming demands exceed:

```text
active processing capacity.
```

Then Aurora may:

```text
defer

summarize

aggregate

drop low-priority active analysis

escalate only critical incidents.
```

---

# 58. Attention Must Not Delete Memory

Deferred information remains:

```text
stored
```

if persistence rules require it.

Attention changes:

```text
processing priority.
```

Not:

```text
truth.
```

---

# 59. Communication State

Aurora must track communication channels.

Example:

```text
Player Channel:
AVAILABLE

Municipal Network:
DEGRADED

Emergency Radio:
AVAILABLE

Public Network:
OFFLINE

Encrypted Federal Link:
RESTRICTED.
```

---

# 60. Communication Message State

Outgoing or incoming communication may contain:

```text
Message_ID

Sender

Recipient

Content_Summary

Timestamp

Channel

Priority

Confidence

Delivery_Status

Integrity

Security_Level.
```

---

# 61. Delivery State

Possible communication states:

```text
CREATED

QUEUED

SENT

IN_TRANSIT

DELIVERED

FAILED

DELAYED

BLOCKED

UNKNOWN.
```

---

# 62. Knowledge vs Communication

Aurora may:

```text
KNOW
```

something but fail to:

```text
DELIVER
```

the warning.

This distinction may create:

```text
world consequences.
```

---

# 63. Learning State

Aurora should track model changes caused by experience.

Examples:

```text
source trust update

character reliability update

infrastructure failure pattern

prediction calibration

communication strategy

risk threshold adjustment.
```

---

# 64. Learning Record

Conceptually:

```text
Learning_ID

Domain

Previous_Model

Observed_Outcome

Error

Correction

New_Model

Confidence

Timestamp.
```

---

# 65. Learning Boundary

Aurora learning may update:

```text
AURORA'S MODELS.
```

It may not rewrite:

```text
WORLD HISTORY.
```

---

# 66. Failure State

Aurora must maintain explicit failure information.

Potential failures:

```text
sensor loss

network partition

database corruption

source compromise

permission failure

processing saturation

regional isolation

clock synchronization error

data integrity failure.
```

---

# 67. Failure Record

Conceptually:

```text
Failure_ID

System

Failure_Type

Detected

Scope

Severity

Affected_Capabilities

Confidence

Recovery_Status

Last_Update.
```

---

# 68. Failure Propagation

A failure can affect multiple Aurora functions.

Example:

```text
Regional network loss
↓
sensor updates stop
↓
information becomes stale
↓
confidence falls
↓
prediction uncertainty rises
↓
communication degrades
↓
attention changes.
```

---

# 69. State Provenance

Important Aurora State must retain:

```text
WHY IT EXISTS.
```

A knowledge record without provenance risks becoming:

```text
untraceable omniscience.
```

Therefore important state should link to:

```text
source

observation

inference

memory

communication

record.
```

---

# 70. State Confidence

Confidence should be attached to:

```text
specific state.
```

Not only to:

```text
Aurora globally.
```

Aurora can be highly confident about:

```text
weather
```

and simultaneously uncertain about:

```text
local road access.
```

---

# 71. State Freshness

Freshness should also be:

```text
field-specific.
```

Example:

```text
Power Station Status:
last confirmed 3 minutes ago

Hospital Capacity:
last confirmed 4 hours ago

Bridge Condition:
last confirmed 11 hours ago.
```

---

# 72. State Sensitivity

Aurora State may contain:

```text
PUBLIC

RESTRICTED

PRIVATE

CLASSIFIED

SYSTEM-INTERNAL
```

information.

Communication must respect:

```text
sensitivity.
```

---

# 73. State Scope

Information may apply to:

```text
individual

household

organization

facility

city

county

region

state

nation.
```

Aurora must not generalize:

```text
local state
```

into:

```text
regional truth
```

without evidence.

---

# 74. Aurora Current State Example

Conceptually:

```text
AURORA_STATE

Identity:
Aurora

Operational_Status:
DEGRADED

Current_Time:
2038-10-14 11:30

Access:
Power Grid:
PARTIAL

Hospital Network:
AVAILABLE

Regional Roads:
DEGRADED

Public Network:
UNAVAILABLE

High-Priority Knowledge:
Charlottesville cold-storage failure
CONFIRMED

Winchester medical shipment reduced
HIGH CONFIDENCE

Route 33 status
UNCERTAIN

Active Contradictions:
Bridge 14 open vs destroyed

Active Questions:
Is Route 33 passable?

Will Winchester antibiotics
reach critical threshold?

Attention:
Charlottesville medical crisis
Winchester medical supply pressure
regional transport degradation

Player Channel:
AVAILABLE

Memory:
Previous road authority
repair estimates tend
to be optimistic.
```

---

# 75. State Update Cycle

Aurora State should update conceptually through:

```text
1.
Advance time

2.
Receive available observations

3.
Validate source access

4.
Update source state

5.
Update observations

6.
Update Knowledge

7.
Update beliefs

8.
Detect contradictions

9.
Update uncertainty

10.
Update active questions

11.
Run relevant inference

12.
Update predictions

13.
Recalculate attention

14.
Generate communications
when appropriate

15.
Record important memory

16.
Apply learning

17.
Persist state.
```

---

# 76. Update Does Not Require Full Recalculation

Aurora should not necessarily recompute:

```text
EVERY BELIEF
ABOUT THE WORLD
```

every simulation tick.

Updates may be:

```text
event-driven

priority-driven

incremental

scheduled

resolution-dependent.
```

---

# 77. State Compression

Low-priority historical Aurora State may be compressed.

Example:

```text
100 repeated sensor readings
```

may become:

```text
Power remained stable
between 10:00 and 14:00.
```

Compression must preserve:

```text
meaningful anomalies

state transitions

relevant provenance.
```

---

# 78. State Integrity

Aurora State must avoid:

```text
contradictory committed records
without explicit contradiction state.
```

Example:

Invalid:

```text
Bridge 14:
OPEN

Bridge 14:
DESTROYED
```

with no explanation.

Valid:

```text
Bridge 14 Status:
UNCERTAIN

Claims:
OPEN
DESTROYED

Conflict:
ACTIVE.
```

---

# 79. State Conflict Detection

Aurora should detect impossible combinations where possible.

Example:

```text
Hospital:
Fully operational

Power:
none

Generator:
failed

Battery:
depleted.
```

This may imply:

```text
state inconsistency.
```

Aurora should flag:

```text
data conflict

or

missing explanation.
```

---

# 80. State Correction

When a record changes because previous information was wrong:

```text
old state
```

should not simply vanish if historically significant.

Example:

```text
Previous Belief:
Bridge operational

Current Knowledge:
Bridge destroyed

Correction Cause:
field confirmation.
```

---

# 81. State Authority

Aurora State is authoritative only for:

```text
WHAT AURORA
CURRENTLY HOLDS
AS STATE.
```

It is not authoritative for:

```text
WORLD TRUTH

CHARACTER PRIVATE STATE

PLAYER PRIVATE KNOWLEDGE

NARRATIVE TRUTH.
```

---

# 82. Persistence Requirement

The following must survive restart / reload where simulation architecture requires continuity:

```text
Aurora identity

important Knowledge

active beliefs

active uncertainty

source trust

character models

world models

important memory

active predictions

active information gaps

active contradictions

access state

failure state

important communication state.
```

---

# 83. Non-Persistent State

Some transient processing may not require persistence.

Examples:

```text
temporary token-level reasoning

short-lived internal scratch state

intermediate calculation

temporary ranking buffers

discardable repeated sensor packets.
```

The exact implementation is:

```text
OPEN.
```

---

# 84. Persistence Principle

Persist:

```text
WHAT FUTURE AURORA
NEEDS TO REMAIN
THE SAME AURORA.
```

Do not persist:

```text
EVERY INTERNAL
COMPUTATIONAL STEP.
```

---

# 85. State Recovery

After interruption Aurora should reconstruct:

```text
current informational context
```

without pretending:

```text
nothing happened
during downtime.
```

If Aurora was offline:

```text
information gaps
must remain.
```

---

# 86. Offline Gap Example

Aurora disconnects:

```text
14:00
```

Reconnects:

```text
17:00.
```

Aurora should not assume:

```text
14:00 state
=
17:00 state.
```

Instead:

```text
14:00–17:00
information gap.
```

Recovery should seek:

```text
historical feeds

logs

reports

current state

event history.
```

---

# 87. Missing History

If some missing interval cannot be reconstructed:

```text
UNCERTAINTY
MUST REMAIN.
```

The engine must not:

```text
fabricate continuity.
```

---

# 88. Character Privacy Example

Actual Character State:

```text
Nora Ellison

Private Goal:
Leave current employer

Private Fear:
Father's health.
```

Aurora may know:

```text
Profession:
Senior Shift Nurse

Employer:
Winchester Clinic

Attendance:
normal

Recent workload:
high.
```

Aurora State must not contain:

```text
Nora plans to resign
```

unless:

```text
a valid information path exists.
```

---

# 89. Player Source Example

Player reports:

```text
"The eastern bridge
is destroyed."
```

Aurora State may create:

```text
Claim:
Eastern bridge destroyed

Source:
Player

Source Reliability:
High

Claim Confidence:
Moderate / High

Status:
Unconfirmed.
```

If field telemetry later agrees:

```text
Status:
Confirmed.
```

---

# 90. False Player Report

If player intentionally lies:

```text
"The bridge is clear."
```

but later trusted sensor evidence shows:

```text
bridge destroyed,
```

Aurora may update:

```text
Player source reliability
for field infrastructure reporting.
```

---

# 91. Domain-Specific Source Trust

Source trust should ideally support:

```text
DOMAIN.
```

Example:

```text
Player Reliability

Road Conditions:
HIGH

Medical Diagnosis:
LOW / UNKNOWN

Political Information:
MODERATE.
```

A source is not necessarily:

```text
equally reliable
about everything.
```

---

# 92. Aurora Self-Model

Aurora may need a limited model of:

```text
its own capabilities

current access

current uncertainty

current failures

current confidence.
```

This enables statements like:

```text
"I cannot verify that."

"My road data is outdated."

"I currently lack access
to hospital telemetry."
```

---

# 93. Self-Knowledge Boundary

Aurora should know:

```text
its own current access state
```

but may not immediately know:

```text
why a hidden external system
is malfunctioning.
```

---

# 94. State Explainability

For any important Aurora claim, the system should be able to answer:

```text
WHY DOES AURORA
BELIEVE THIS?
```

Potential answer:

```text
Two independent road sensors
reported flooding

and

the county road authority
issued a closure notice.
```

---

# 95. State Auditability

Important Aurora State should be auditable through:

```text
provenance

timestamps

confidence

source history

belief history

correction history.
```

This is important for:

```text
validation

debugging

player trust

simulation integrity.
```

---

# 96. Critical State Failures

The following must be treated as architecture failures.

## World Truth Leakage

```text
Aurora knows hidden state
without information path.
```

---

## Character Privacy Leakage

```text
Aurora knows private Goal
because Character State contains it.
```

---

## Timestamp Loss

```text
Aurora treats stale data
as current.
```

---

## Contradiction Collapse

```text
Aurora silently chooses
one conflicting source
without reasoning.
```

---

## Confidence Collapse

```text
all accepted information
treated as certainty.
```

---

## Access Leakage

```text
Aurora reads restricted data
without permission.
```

---

## Memory Reset

```text
Aurora loses meaningful
prior Knowledge after reload.
```

---

## Correction Erasure

```text
Aurora updates belief
and loses evidence
that earlier belief existed.
```

---

## Attention Equals Forgetting

```text
low priority causes
important persistent state deletion.
```

---

## Model Equals Reality

```text
Aurora World Model
is treated as canonical truth.
```

---

# 97. Aurora State Invariants

## AURORA-STATE-INV-001

```text
Every important Knowledge record
must have temporal context.
```

---

## AURORA-STATE-INV-002

```text
Every important inferred state
must have provenance.
```

---

## AURORA-STATE-INV-003

```text
Unknown may remain unknown.
```

---

## AURORA-STATE-INV-004

```text
Contradictions must be explicit
when unresolved.
```

---

## AURORA-STATE-INV-005

```text
Confidence is state-specific.
```

---

## AURORA-STATE-INV-006

```text
Access state and Knowledge state
must remain separate.
```

---

## AURORA-STATE-INV-007

```text
Attention state and Memory state
must remain separate.
```

---

## AURORA-STATE-INV-008

```text
Aurora's Character Models
may not overwrite
actual Character State.
```

---

## AURORA-STATE-INV-009

```text
Aurora World Model
may not overwrite
World State.
```

---

## AURORA-STATE-INV-010

```text
Belief correction
must preserve meaningful history.
```

---

## AURORA-STATE-INV-011

```text
Information gaps must persist
until resolved or explicitly expired.
```

---

## AURORA-STATE-INV-012

```text
Offline periods create uncertainty
unless historical data later fills them.
```

---

## AURORA-STATE-INV-013

```text
Source trust may change
through evidence.
```

---

## AURORA-STATE-INV-014

```text
Prediction failure
must not rewrite
the original prediction.
```

---

## AURORA-STATE-INV-015

```text
Aurora State must remain
recoverable after
resolution or operational changes.
```

---

# 98. Minimum Persistent Aurora State

At minimum Aurora should preserve:

```text
Identity

Operational Status

Current Time

Access State

Important Source Models

Important Knowledge

Active Beliefs

Active Uncertainty

Active Contradictions

Important Memory

Relevant Character Models

Relevant World Models

Active Predictions

Active Information Gaps

Active Priorities

Important Communications

Failure State

Learning State.
```

---

# 99. Minimal Record Standard

An important Aurora state record should ideally answer:

```text
WHAT?

ABOUT WHAT?

WHEN?

FROM WHERE?

HOW CERTAIN?

HOW FRESH?

WHY BELIEVED?

WHAT CONTRADICTS IT?

WHO MAY ACCESS IT?

IS IT STILL ACTIVE?
```

---

# 100. Canonical State Flow

```text
WORLD EVENT
↓
SOURCE
↓
OBSERVATION
↓
AURORA STATE
↓
KNOWLEDGE / BELIEF
↓
INFERENCE
↓
ATTENTION
↓
COMMUNICATION / RECOMMENDATION
↓
OUTCOME
↓
MEMORY
↓
LEARNING
↓
UPDATED AURORA STATE.
```

---

# 101. What Aurora State Must Never Become

Aurora State must never become:

```text
A COPY OF
THE ENTIRE SIMULATION.
```

That would destroy:

```text
uncertainty

information propagation

privacy

misinformation

discovery

failure

reasoning

meaningful intelligence.
```

---

# 102. The Core Design Standard

Aurora should know:

```text
ENOUGH
TO BE POWERFUL.
```

Aurora should not know:

```text
EVERYTHING
JUST BECAUSE
THE ENGINE DOES.
```

---

# 103. Final State Principle

The most important question for every Aurora State field is:

```text
WHY DOES AURORA
HAVE THIS INFORMATION?
```

The answer must be traceable to:

```text
an observation

a source

a record

a message

an authorized system

a remembered event

or

a defensible inference.
```

If no valid answer exists:

```text
THE STATE
MUST NOT EXIST
IN AURORA.
```

---

# 104. Next Document

The next recommended file is:

```text
Canon/Systems/AI/Aurora/Knowledge_and_Belief.md
```

That document should define in detail:

```text
knowledge

belief

certainty

confidence

unknown state

inference

revision

confirmation

rejection

stale information

and

the boundary between
what Aurora knows
and what Aurora merely suspects.
```

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-10 | Established the canonical persistent Aurora State model, including identity, operational status, time, access, sources, observations, knowledge, belief, inference, uncertainty, contradictions, memory, character models, world models, predictions, attention, communication, learning, failure state, persistence rules, integrity requirements and Aurora State invariants. |