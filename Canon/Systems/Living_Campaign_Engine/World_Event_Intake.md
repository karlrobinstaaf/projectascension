# PROJECT ASCENSION
# World Event Intake System

| Field | Value |
|--------|-------|
| System | Living Campaign Engine |
| Document | World Event Intake |
| Location | Canon/Systems/Living_Campaign_Engine/World_Event_Intake.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | World Event Detection, Normalization, Clustering and Campaign Intake |
| Last Updated | 2026-08-09 |

> *"The world changes constantly. Most of those changes should never become quests."*

---

# Purpose

The World Event Intake system defines how changes produced by World Simulation enter the Living Campaign Engine.

World Simulation may continuously produce:

- state changes
- pressure changes
- infrastructure failures
- shortages
- migrations
- security developments
- authority decisions
- information changes
- recovery
- trade changes
- environmental effects
- faction activity
- population behavior

The Living Campaign Engine cannot treat every simulation change as a separate player-facing event.

World Event Intake therefore acts as the first campaign filter.

Conceptually:

```text
WORLD SIMULATION
      │
      │ thousands of changes
      ▼
WORLD EVENT INTAKE
      │
      │ normalized candidates
      ▼
RELEVANCE AND PROXIMITY
      │
      ▼
CAMPAIGN CONTENT
```

---

# Core Principle

The central rule is:

```text
WORLD CHANGE
≠
WORLD EVENT CANDIDATE
≠
CAMPAIGN EVENT
≠
MISSION
```

These are separate stages.

---

# Four Layers

```text
LAYER 1

WORLD CHANGE

Something changes inside World Simulation.

        ↓

LAYER 2

EVENT CANDIDATE

The change is significant enough
to be examined by Living Campaign Engine.

        ↓

LAYER 3

CAMPAIGN EVENT

The change is relevant enough
to become part of the campaign.

        ↓

LAYER 4

PLAYER-FACING CONTENT

The campaign determines how
the player experiences it.
```

---

# Example

World Simulation:

```text
Regional fuel inventory:

43%
↓
42%
```

This is a World Change.

Normally:

```text
NO EVENT CANDIDATE
```

Later:

```text
Fuel State:

STRAINED
↓
CONSTRAINED
```

This may create:

```text
EVENT CANDIDATE
```

Whether the player ever hears about it is determined later.

---

# Intake Responsibility

World Event Intake answers:

```text
WHAT CHANGED?

HOW MUCH DID IT CHANGE?

WHY DID IT CHANGE?

WHAT DOES IT AFFECT?

IS THIS CHANGE SIGNIFICANT?

IS IT PART OF AN EXISTING EVENT?

IS IT STILL ACTIVE?

SHOULD IT BE EXAMINED
FOR CAMPAIGN RELEVANCE?
```

It does not answer:

```text
DOES THE PLAYER CARE?
```

That belongs primarily to:

```text
Relevance_and_Proximity.md
```

---

# System Boundary

World Event Intake must not replace World Simulation.

World Simulation owns:

```text
WORLD TRUTH

WORLD STATE

SYSTEM PRESSURE

CASCADES

RECOVERY

WORLD ACTORS

WORLD OUTCOMES
```

World Event Intake observes those outputs.

---

# Intake Sources

Potential event candidates may originate from:

```text
World State
Regional State
Infrastructure State
Information State
Authority State
Population State
Supply State
Security State
Escalation and Recovery
Environmental Systems
Faction Activity
Character Activity
Delayed Consequences
```

Not every source must produce events continuously.

---

# Primary Event Sources

The strongest intake signals should normally come from:

```text
STATE TRANSITION

THRESHOLD CROSSING

SIGNIFICANT PRESSURE CHANGE

CASCADE

MAJOR ACTOR ACTION

RESOURCE SHOCK

INFRASTRUCTURE FAILURE

SECURITY DEVELOPMENT

AUTHORITY DECISION

MIGRATION

RECOVERY MILESTONE

NEW OPPORTUNITY

DELAYED CONSEQUENCE
```

---

# State Transition

A state transition occurs when a World Simulation domain changes category.

Example:

```text
Supply:

STRAINED
↓
CONSTRAINED
```

This should normally create an Event Candidate.

---

# Threshold Crossing

Some continuous values may cross meaningful thresholds.

Example:

```text
Hospital Fuel Reserve:

28 hours
↓
22 hours

Threshold:
24 hours
```

Candidate:

```text
Hospital emergency reserve
has crossed critical threshold.
```

---

# Significant Pressure Change

A state may remain unchanged while pressure changes sharply.

Example:

```text
Infrastructure State:
STRAINED

Pressure:
MODERATE
↓
SEVERE
```

This may deserve an Event Candidate even before state deterioration occurs.

---

# Direction Matters

The intake system must detect both:

```text
DETERIORATION
```

and:

```text
IMPROVEMENT
```

Example:

```text
Medicine:

CRITICAL
↓
CONSTRAINED
```

may create a Recovery Candidate.

The campaign must not notice only bad news.

---

# Event Candidate

An Event Candidate is a normalized description of a potentially meaningful world development.

Conceptually:

```text
EVENT CANDIDATE

Event ID
Event Type
Source System
Source Object
Location
Start Time
Detection Time
Direction
Magnitude
Urgency
Affected Systems
Affected Actors
Cause
Parent Event
Related Events
Current State
Confidence
```

---

# Event ID

Each candidate should receive a stable identifier.

Example:

```text
WEC-2045-00142
```

Exact naming convention may be standardized later.

Stable IDs allow:

- clustering
- consequence tracking
- duplicate detection
- campaign references
- debugging
- historical records

---

# Event Type

Initial Event Types may include:

```text
STATE_CHANGE
THRESHOLD
SHORTAGE
FAILURE
DISRUPTION
RECOVERY
MIGRATION
SECURITY
AUTHORITY
INFORMATION
TRADE
ENVIRONMENT
OPPORTUNITY
CONFLICT
DISCOVERY
ACTOR_ACTION
CONSEQUENCE
```

The taxonomy should remain compact.

---

# Source System

Every candidate must identify its origin.

Example:

```text
Source System:
Supply State
```

or:

```text
Source System:
Infrastructure State
```

---

# Source Object

The affected object should be identifiable.

Example:

```text
Source Object:
Winchester Regional Hospital Fuel Reserve
```

This prevents vague events such as:

```text
Something happened with fuel.
```

---

# Location

Candidates should reference their actual world location.

Conceptually:

```text
Region
Local Area
Settlement
Specific Site
Route
Network
```

Location may be:

```text
LOCAL
REGIONAL
MULTI-REGIONAL
WORLD
```

---

# Event Start Time

The time when the underlying development actually began.

Example:

```text
Start Time:
2045-05-14 03:20
```

---

# Detection Time

The time when Intake recognizes the development as an Event Candidate.

These may differ.

Example:

```text
Fuel deliveries began declining:
May 10

Critical threshold crossed:
May 14
```

---

# Direction

Conceptually:

```text
DETERIORATING
IMPROVING
MIXED
NEUTRAL
```

This helps distinguish crisis from recovery.

---

# Magnitude

Magnitude describes how large the underlying change is.

Conceptually:

```text
MINOR
MODERATE
MAJOR
SEVERE
SYSTEMIC
```

Magnitude is not player relevance.

A systemic event may still be irrelevant to a particular campaign.

---

# Urgency

Urgency describes how quickly the underlying situation may materially change.

Conceptually:

```text
LOW
MODERATE
HIGH
IMMEDIATE
```

Urgency is not identical to Severity.

---

# Severity Versus Urgency

Example:

```text
Long-term soil degradation

Severity:
MAJOR

Urgency:
LOW
```

versus:

```text
Hospital generator has 45 minutes of fuel.

Severity:
MAJOR

Urgency:
IMMEDIATE
```

Both dimensions matter.

---

# Affected Systems

A candidate should identify which World Simulation systems may be affected.

Example:

```text
Affected Systems:

Supply
Infrastructure
Population
Security
```

---

# Affected Actors

Where known:

```text
Settlement
Faction
Character
Authority
Business
Community
Infrastructure Operator
```

This becomes important later during relevance evaluation.

---

# Cause

Whenever possible, candidates should preserve causal information.

Example:

```text
EVENT

Fuel shortage.

CAUSE

Mountain route closure.
```

Avoid treating these as unrelated events if the simulation knows the relationship.

---

# Causal Chain

Conceptually:

```text
SEVERE STORM
      ↓
MOUNTAIN PASS CLOSED
      ↓
FUEL DELIVERY INTERRUPTED
      ↓
REGIONAL FUEL PRESSURE
      ↓
TRANSPORT REDUCTION
      ↓
FOOD DISTRIBUTION DELAYS
```

Intake should preserve this causal chain.

---

# Parent Event

Secondary developments may reference a Parent Event.

Example:

```text
Parent Event:
WEC-2045-00142
Mountain Pass Closure

Child Event:
WEC-2045-00147
Fuel Delivery Disruption
```

---

# Related Events

Not every relationship is causal.

Events may also be:

```text
CORRELATED
COMPETING
REINFORCING
MITIGATING
DEPENDENT
```

---

# Event Confidence

Confidence represents how certain the simulation is that the candidate has been correctly classified.

This is primarily an internal value.

Conceptually:

```text
HIGH
MODERATE
LOW
```

This should not be confused with Player Knowledge confidence.

---

# World Truth Versus Player Knowledge

Intake operates from World Simulation truth.

Example:

```text
WORLD TRUTH

Bridge:
DESTROYED
```

The Event Candidate may therefore know:

```text
Bridge destroyed.
```

The player may still believe:

```text
Bridge operational.
```

World Event Intake must not automatically update Player Knowledge.

---

# Candidate Creation Rules

A candidate should normally be created when at least one of the following occurs:

```text
1. Domain state changes.

2. Meaningful threshold is crossed.

3. Pressure changes significantly.

4. New cascade begins.

5. Existing cascade changes direction.

6. Major actor makes consequential decision.

7. Significant resource availability changes.

8. Infrastructure service materially changes.

9. Population movement becomes significant.

10. Security condition materially changes.

11. Authority capacity or legitimacy materially changes.

12. Information environment materially changes.

13. Recovery reaches meaningful milestone.

14. New strategic opportunity appears.

15. Delayed consequence matures.
```

---

# Candidate Suppression

A candidate should normally not be created for:

```text
Minor routine fluctuation

Expected daily consumption

Normal market variation

Insignificant weather change

Repeated unchanged warnings

Tiny population movement

Routine maintenance

Background NPC activity without consequence
```

unless context makes it significant.

---

# Noise Suppression

The system must prevent simulation noise from flooding Living Campaign Engine.

Example:

```text
Fuel:

44.1%
43.8%
44.0%
43.7%
```

should not produce:

```text
EVENT
EVENT
EVENT
EVENT
```

---

# Hysteresis

Threshold systems should use hysteresis where appropriate.

Example:

```text
CONSTRAINED threshold:
Below 40%

Recovery threshold:
Above 45%
```

This prevents:

```text
STRAINED
CONSTRAINED
STRAINED
CONSTRAINED
```

from rapid minor fluctuations.

---

# Cooldown

Repeated identical events may use a cooldown.

Example:

```text
Power interruptions occur every hour.
```

Instead of generating twelve separate candidates:

```text
Power instability remains active.
```

The existing event is updated.

---

# Event Update Versus New Event

The engine must determine whether a new simulation change represents:

```text
NEW EVENT
```

or:

```text
UPDATE TO EXISTING EVENT
```

---

# Example

Existing:

```text
WEC-0142

Regional Fuel Shortage

State:
ACTIVE
```

New World Change:

```text
Fuel availability falls another 8%.
```

Normally:

```text
UPDATE WEC-0142
```

not:

```text
CREATE NEW FUEL SHORTAGE
```

---

# New Event Criteria

A separate event may be justified when:

```text
Cause changes materially.

Location changes materially.

Affected actors differ significantly.

Situation changes category.

A secondary cascade becomes independently significant.

The original event has already resolved.
```

---

# Duplicate Detection

Candidates should be compared using:

```text
Source
Location
Time
Event Type
Affected System
Cause
Parent Event
```

Likely duplicates should be merged or linked.

---

# Duplicate Example

World Simulation produces:

```text
Fuel inventory below threshold.

Fuel availability classified Critical.

Transport authority begins rationing.
```

These are related developments.

They should not automatically become three independent campaign situations.

---

# Event Clustering

Related Event Candidates may be grouped into an Event Cluster.

Conceptually:

```text
EVENT CLUSTER
│
├── Root Cause
├── Primary Events
├── Secondary Events
├── Affected Systems
├── Affected Locations
├── Affected Actors
├── Direction
├── Severity
└── Current State
```

---

# Example Cluster

```text
CLUSTER:
Northern Valley Fuel Crisis

ROOT:
Mountain pass closure

EVENTS:

Transport disruption
Fuel delivery reduction
Fuel threshold crossed
Agricultural rationing
Hospital reserve decline
Black-market price increase
```

The cluster represents one broader world situation.

---

# Why Clustering Matters

Without clustering:

```text
Fuel shortage quest

Hospital fuel quest

Farm fuel quest

Transport fuel quest

Trader fuel quest
```

may appear to be unrelated content.

With clustering:

```text
ONE FUEL CRISIS
```

can create multiple perspectives and choices.

---

# Root Event

Where possible, clusters should identify a Root Event.

Example:

```text
ROOT EVENT

Landslide closes mountain pass.
```

But not every cluster has one simple root.

---

# Multi-Causal Events

Some situations arise from several causes.

Example:

```text
REGIONAL FOOD SHORTAGE

Causes:

Poor harvest
+
Fuel shortage
+
Migration
+
Transport disruption
```

The engine must support:

```text
MULTIPLE CAUSES
```

rather than force a single explanation.

---

# Reinforcing Events

Related events may amplify each other.

Example:

```text
Fuel shortage
      +
Severe winter
      ↓
Transport pressure
      ↓
Food distribution problems
```

This relationship should be preserved.

---

# Mitigating Events

Events may also reduce pressure.

Example:

```text
Fuel shortage
      +
New trade agreement
      ↓
Fuel availability improves
```

The trade agreement is a mitigating event.

---

# Event Significance

Before passing a candidate forward, Intake may estimate World Significance.

Conceptually:

```text
WORLD SIGNIFICANCE

Magnitude
+
Duration
+
Population Affected
+
Systems Affected
+
Cascade Potential
+
Strategic Importance
```

This is not Campaign Relevance.

---

# World Significance Levels

Conceptually:

```text
BACKGROUND
LOCAL
SIGNIFICANT
MAJOR
SYSTEMIC
```

---

# Background

Normal or low-impact changes.

Usually retained only in World Simulation history.

---

# Local

Meaningful to a small location or actor group.

May become highly relevant to the player later.

---

# Significant

Meaningful regional development.

Should normally be evaluated for campaign relevance.

---

# Major

Large regional or multi-system event.

Should receive strong intake attention.

---

# Systemic

Large-scale event capable of altering regional or broader equilibrium.

Always enters relevance evaluation.

It still does not automatically become player-facing content.

---

# Important Distinction

```text
WORLD SIGNIFICANCE
≠
CAMPAIGN RELEVANCE
```

Example:

```text
Major earthquake
on another continent.

World Significance:
MAJOR

Campaign Relevance:
Possibly LOW
```

Meanwhile:

```text
Minor workshop fire
in player's home settlement.

World Significance:
LOCAL

Campaign Relevance:
Possibly EXTREME
```

---

# Background Event Handling

Background events do not need to disappear.

They may be stored as:

```text
WORLD HISTORY
```

or contribute to aggregate state.

Example:

```text
Three minor harvest problems
```

may individually remain background.

Together they may eventually create:

```text
Regional Food Pressure:
STRAINED → CONSTRAINED
```

which then creates an Event Candidate.

---

# Event Accumulation

Repeated minor changes may accumulate into significance.

Conceptually:

```text
MINOR
+
MINOR
+
MINOR
+
MINOR
      ↓
THRESHOLD
      ↓
EVENT CANDIDATE
```

This allows slow crises.

---

# Slow-Burn Events

Not all events should begin suddenly.

Example:

```text
Groundwater depletion
```

may evolve over months or years.

Conceptually:

```text
EMERGING
      ↓
DEVELOPING
      ↓
SIGNIFICANT
      ↓
CRITICAL
```

Intake should support long-duration events.

---

# Sudden Events

Other events may immediately enter at high significance.

Example:

```text
Bridge collapse

Major attack

Earthquake

Power station explosion
```

These may bypass slow accumulation.

---

# Event Lifecycle

Each Event Candidate should have a lifecycle.

Recommended states:

```text
DETECTED
EMERGING
ACTIVE
ESCALATING
STABILIZING
RESOLVING
RESOLVED
TRANSFORMED
ABSORBED
```

---

# Detected

The system has identified the change.

It has not yet demonstrated persistence.

---

# Emerging

The development persists or grows.

It may become significant.

---

# Active

The event is producing meaningful world effects.

---

# Escalating

Magnitude, pressure or cascade effects are increasing.

---

# Stabilizing

The situation remains active but is no longer worsening.

---

# Resolving

The underlying condition is improving toward resolution.

---

# Resolved

The event no longer produces meaningful active effects.

Historical consequences may remain.

---

# Transformed

The event has changed into a different type of situation.

Example:

```text
Fuel shortage
      ↓
Political conflict
```

The original event may become:

```text
TRANSFORMED
```

while a new event is created.

---

# Absorbed

World systems handled the event without it developing into a meaningful ongoing situation.

Example:

```text
Small power failure
      ↓
Backup systems activate
      ↓
Repair completed
```

The event is:

```text
ABSORBED
```

---

# Event Resolution

Resolution does not mean:

```text
WORLD RETURNS TO PREVIOUS STATE
```

Example:

```text
Bridge collapse resolved
```

may mean:

```text
Permanent ferry service established.
```

The crisis is resolved.

The world has changed.

---

# Residual Effects

Resolved events may leave:

```text
Infrastructure damage
Population displacement
Economic change
Political memory
Relationship effects
Resource depletion
New institutions
```

These belong to ongoing World State and Campaign Memory where relevant.

---

# Event Transformation

An event may cease to be important in its original form but create another event.

Example:

```text
FOOD SHORTAGE
      ↓
RATIONING
      ↓
PUBLIC DISPUTE
      ↓
AUTHORITY CRISIS
```

Intake should preserve the lineage.

---

# Event Lineage

Conceptually:

```text
WEC-001
Food Shortage

        ↓ causes

WEC-017
Rationing Decision

        ↓ contributes to

WEC-024
Authority Legitimacy Crisis
```

This allows later explanation of campaign history.

---

# Delayed Consequence Intake

Some events originate from earlier player or world actions.

Example:

```text
PLAYER ACTION

Fuel diverted away from agriculture.
```

Three weeks later:

```text
Harvest output declines.
```

World Simulation generates the actual effect.

Intake creates:

```text
CONSEQUENCE EVENT CANDIDATE
```

with reference to the original action where available.

---

# Player-Caused Events

The player may cause World Events.

Example:

```text
Player destroys bridge.
```

World Simulation updates:

```text
Transportation
Supply
Security
Migration
```

World Event Intake then processes those changes exactly as it would any other world development.

The player does not receive special simulation rules.

---

# Important Principle

```text
PLAYER ACTION
DOES NOT DIRECTLY CREATE A STORY.
```

Instead:

```text
PLAYER ACTION
      ↓
WORLD STATE CHANGE
      ↓
WORLD EVENT INTAKE
      ↓
CAMPAIGN RELEVANCE
      ↓
NEW STORY POSSIBILITY
```

This preserves systemic causality.

---

# Actor-Generated Events

NPCs and factions may also create candidates.

Example:

```text
Faction closes trade route.
```

This may affect:

```text
Transportation
Supply
Authority
Security
```

The actor action itself and its systemic consequences may belong to the same Event Cluster.

---

# Character-Scale Events

World Event Intake should not be restricted to regional disasters.

Character actions may become candidates when they are consequential.

Examples:

```text
Important character leaves settlement.

Known character disappears.

Faction leader dies.

Relationship character relocates.

Technician completes critical repair.
```

World significance may be low.

Campaign relevance may later be high.

---

# Opportunity Events

The system must detect opportunities, not only problems.

Examples:

```text
New trade route opens.

Abandoned facility becomes accessible.

Harvest surplus appears.

Regional authority seeks contractors.

New communications link established.

Skilled migrants arrive.
```

---

# Recovery Events

Recovery should generate candidates at meaningful milestones.

Example:

```text
Power Availability:

CRITICAL
↓
CONSTRAINED
```

or:

```text
Bridge:
REPAIRED
```

Recovery changes available campaign possibilities.

---

# Discovery Events

Some world truths become newly discoverable.

Example:

```text
Flood exposes buried facility.
```

The facility may have existed for decades.

The Event Candidate is:

```text
NEW ACCESS / DISCOVERY OPPORTUNITY
```

not:

```text
FACILITY CREATED
```

---

# Information Events

Changes in information environment may themselves be candidates.

Examples:

```text
Radio network restored.

Regional communication blackout.

Major rumor spreads.

Authority begins emergency broadcasts.

Previously isolated region reconnects.
```

These may alter how future events can reach the player.

---

# Event Visibility

World Event Intake should not decide final player visibility.

It may, however, store potential transmission channels.

Example:

```text
Potential Channels:

Regional radio
Travelers
Faction network
Direct observation
Official bulletin
```

Actual delivery belongs later in the Living Campaign Engine.

---

# Information Gate Preparation

For each candidate, Intake may identify:

```text
WHO COULD KNOW?

HOW COULD INFORMATION TRAVEL?

WHEN COULD IT ARRIVE?
```

This supports later Story Hook generation.

---

# Example

```text
EVENT:

Bridge destroyed.

Location:
150 km away.

Potential Information Channels:

Regional radio:
Available

Travelers:
Possible

Authority network:
Available

Direct observation:
No
```

The player still does not automatically know.

---

# Event Persistence

Active events should remain available for reevaluation.

Why?

Because player context changes.

Example:

```text
Day 1:

Distant fuel shortage.

Campaign Relevance:
LOW
```

Later:

```text
Player begins traveling toward affected region.
```

The same active event may now become:

```text
Campaign Relevance:
HIGH
```

Therefore:

```text
LOW RELEVANCE
≠
DELETE EVENT
```

---

# Relevance Recheck Triggers

Active events may be reevaluated when:

```text
Player moves.

Player goals change.

Relationship changes.

Faction relationship changes.

New information arrives.

Event escalates.

Event spreads geographically.

Event affects new systems.

Campaign pressure changes.
```

---

# Intake Queue

Candidates ready for relevance evaluation may enter an Intake Queue.

Conceptually:

```text
INTAKE QUEUE

Immediate Candidates
Major Candidates
Updated Active Events
New Opportunities
Recovery Events
Background Candidates
```

Exact technical implementation may vary.

---

# Queue Priority

Queue priority may consider:

```text
World Significance
Urgency
Event Novelty
State Transition
Cascade Potential
Update Magnitude
```

Again:

```text
QUEUE PRIORITY
≠
PLAYER RELEVANCE
```

---

# Event Novelty

Repeated identical information has less intake value.

Example:

```text
Fuel remains Critical.
```

should not repeatedly create new candidates.

But:

```text
Fuel remains Critical
AND hospital reserve falls below 12 hours.
```

introduces meaningful novelty.

---

# Material Change

An existing event should be updated when a Material Change occurs.

Examples:

```text
New location affected.

New actor affected.

Urgency changes.

Magnitude changes.

State changes.

Cause changes.

Recovery begins.

New cascade begins.

Mitigation succeeds.
```

---

# Event Aging

Events should age.

Conceptually:

```text
NEW
CURRENT
PERSISTENT
HISTORICAL
```

Age may influence later presentation.

A persistent event can become normal background.

---

# Normalization

Long-duration conditions may normalize socially.

Example:

```text
Fuel rationing active for three years.
```

This may no longer deserve constant event treatment.

It becomes:

```text
BASELINE WORLD CONDITION
```

until something changes.

---

# Baseline Shift

A resolved or persistent event may permanently change baseline conditions.

Example:

```text
National grid failure
      ↓
Regional microgrids adopted
      ↓
Microgrid operation becomes normal baseline
```

The engine should stop treating the new normal as a continuous crisis.

---

# Historical Recording

Significant resolved events may be written into world history.

Conceptually:

```text
WORLD LEDGER
```

The exact World Ledger architecture remains to be defined.

The legacy `Overview.md` concept:

```text
Write to the World Ledger
```

remains useful.

World Event Intake provides a natural source for such records.

---

# World Ledger Boundary

World Ledger should eventually answer:

```text
WHAT HAPPENED?
```

Campaign Memory should answer:

```text
WHAT DID THIS CAMPAIGN EXPERIENCE
AND WHY DOES IT STILL MATTER?
```

These should not be the same system.

---

# Intake Processing Loop

A conceptual intake cycle:

```text
1. Read World Simulation changes.

2. Compare current state to previous state.

3. Detect meaningful transitions.

4. Detect threshold crossings.

5. Detect pressure changes.

6. Detect new cascades.

7. Detect recovery.

8. Detect actor actions.

9. Detect matured consequences.

10. Normalize candidate events.

11. Compare against active events.

12. Merge duplicates.

13. Update existing events.

14. Build or update Event Clusters.

15. Calculate World Significance.

16. Update Event Lifecycle.

17. Suppress routine noise.

18. Queue meaningful candidates.

19. Preserve active events for future reevaluation.

20. Record resolved significant events.
```

---

# Example Intake Cycle

World Simulation reports:

```text
Mountain Pass:
CLOSED

Fuel Delivery:
-38%

Regional Fuel:
CONSTRAINED

Hospital Reserve:
31 hours
```

Intake detects:

```text
Candidate A:
Mountain Pass Closure

Candidate B:
Fuel Delivery Disruption

Candidate C:
Regional Fuel State Change
```

Causal analysis:

```text
A
↓
B
↓
C
```

Cluster created:

```text
Northern Valley Fuel Disruption
```

Hospital reserve has not crossed critical threshold.

Therefore:

```text
No Hospital Crisis Candidate yet.
```

Later:

```text
Hospital Reserve:
23 hours
```

Threshold crossed.

New candidate:

```text
Hospital Fuel Reserve Critical
```

Candidate joins existing cluster.

The campaign now sees:

```text
ONE DEVELOPING WORLD SITUATION
```

rather than four unrelated events.

---

# Intake and Campaign State

After candidates are normalized, the system may compare them against Campaign State.

Campaign State provides:

```text
Player Location
Player Knowledge
Goals
Relationships
Resources
Roles
Factions
Obligations
Current Situations
Campaign Pressure
```

But World Event Intake should not perform the full relevance calculation.

It passes candidates to:

```text
Relevance_and_Proximity.md
```

---

# Intake Output

The standard output should conceptually resemble:

```text
EVENT INTAKE OUTPUT

Event ID:
WEC-2045-00142

Cluster:
Northern Valley Fuel Disruption

Type:
SHORTAGE

Source:
Supply State

Location:
Northern Shenandoah Valley

Direction:
DETERIORATING

Magnitude:
MAJOR

Urgency:
HIGH

World Significance:
SIGNIFICANT

Cause:
Mountain Pass Closure

Affected Systems:
Supply
Transportation
Infrastructure

Affected Actors:
Regional Hospital
Agricultural Producers
Transport Operators

Lifecycle:
ACTIVE

Potential Information Channels:
Regional Radio
Authority Network
Travelers

Campaign Relevance:
NOT YET EVALUATED
```

This becomes input for the next system.

---

# Explainability Requirement

Every Event Candidate should allow the engine to answer:

```text
WHAT CHANGED?

WHERE?

WHEN?

WHY?

HOW LARGE WAS THE CHANGE?

WHAT CAUSED IT?

WHAT DOES IT AFFECT?

IS IT NEW?

IS IT PART OF SOMETHING LARGER?

IS IT GETTING BETTER OR WORSE?

IS IT STILL ACTIVE?
```

If these questions cannot be answered, the event is insufficiently normalized.

---

# Anti-Random Principle

World Event Intake must never invent events simply because:

```text
THE CAMPAIGN NEEDS SOMETHING TO DO.
```

Events originate from:

```text
WORLD STATE
ACTOR ACTION
PLAYER ACTION
DELAYED CONSEQUENCE
```

The campaign discovers stories inside them.

---

# Anti-Noise Principle

The opposite failure must also be avoided.

Do not send every simulation fluctuation forward.

```text
SIMULATION DETAIL
≠
CAMPAIGN SIGNIFICANCE
```

The Intake layer exists specifically to protect the campaign from simulation noise.

---

# Anti-Disaster Bias

The system must detect:

```text
CRISIS
```

but equally:

```text
RECOVERY
OPPORTUNITY
GROWTH
DISCOVERY
STABILIZATION
RECONNECTION
```

A Living Campaign cannot be built only from things going wrong.

---

# Core Canon Rules

The following principles are canonical for World Event Intake:

1. World Changes are not automatically Event Candidates.
2. Event Candidates are not automatically Campaign Events.
3. Campaign Events are not automatically Missions.
4. World Simulation remains the source of world truth.
5. Intake observes World Simulation rather than replacing it.
6. State transitions are strong candidate triggers.
7. Threshold crossings are strong candidate triggers.
8. Significant pressure changes may create candidates without state transitions.
9. Recovery and improvement must generate events where meaningful.
10. Routine fluctuations should be suppressed.
11. Repeated identical conditions should update existing events rather than create duplicates.
12. Related events should be clustered.
13. Causal relationships should be preserved.
14. Events may have multiple causes.
15. Events may reinforce or mitigate one another.
16. World Significance and Campaign Relevance are separate.
17. Low world significance may still become highly player-relevant.
18. High world significance does not guarantee player relevance.
19. Active events remain available for future relevance reevaluation.
20. Player actions enter the same World Simulation → Intake pipeline as other causes.
21. NPC and faction actions may generate events.
22. Opportunities are valid Event Candidates.
23. Recovery is a valid Event Candidate.
24. Persistent conditions may become baseline rather than permanent crises.
25. Significant events should remain historically traceable.
26. Intake must remain explainable.
27. Intake must not invent content solely to create gameplay.

---

# Minimum Viable World Event Intake

A minimum viable implementation must be capable of:

```text
1. Read World Simulation changes.

2. Detect meaningful state changes.

3. Detect threshold crossings.

4. Create stable Event IDs.

5. Identify location and source.

6. Preserve known cause.

7. Distinguish new events from updates.

8. Suppress duplicates.

9. Cluster related events.

10. Assign basic magnitude and urgency.

11. Track event lifecycle.

12. Detect recovery.

13. Pass normalized candidates forward.

14. Retain active events for reevaluation.

15. Record significant resolved events.
```

---

# System Flow

The Living Campaign Engine pipeline now becomes:

```text
WORLD SIMULATION
      │
      ▼
WORLD CHANGES
      │
      ▼
WORLD EVENT INTAKE
      │
      ├── Detection
      ├── Normalization
      ├── Noise Suppression
      ├── Causal Analysis
      ├── Duplicate Detection
      ├── Clustering
      ├── Significance
      └── Lifecycle
      │
      ▼
EVENT CANDIDATES
      │
      ▼
RELEVANCE AND PROXIMITY
      │
      ▼
CAMPAIGN STATE
      │
      ▼
STORY HOOKS
      │
      ▼
PLAYER EXPERIENCE
```

---

# Architectural Result

With this layer established, Project Ascension now separates three fundamentally different questions:

```text
WORLD SIMULATION

WHAT ACTUALLY HAPPENED?
```

```text
WORLD EVENT INTAKE

WHICH CHANGES ARE MEANINGFUL ENOUGH
TO EXAMINE?
```

```text
LIVING CAMPAIGN ENGINE

WHICH OF THOSE CHANGES
MATTER TO THIS PLAYER?
```

This separation is essential for scaling the simulation.

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
Canon/Systems/Living_Campaign_Engine/Relevance_and_Proximity.md
```

World Event Intake now provides:

```text
A NORMALIZED EVENT CANDIDATE
```

The next system must determine:

```text
WHY SHOULD THIS PARTICULAR EVENT
MATTER TO THIS PARTICULAR PLAYER?
```

It should define:

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
- relevance decay
- relevance amplification
- relevance scoring
- reevaluation triggers

This becomes the decisive bridge between:

```text
A WORLD THAT IS ALIVE
```

and:

```text
A CAMPAIGN THAT FEELS PERSONAL.
```

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial World Event Intake framework established for event detection, normalization, threshold detection, causal chains, duplicate suppression, clustering, significance, lifecycle, opportunities, recovery and campaign intake. |