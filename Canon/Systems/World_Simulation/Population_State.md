# PROJECT ASCENSION
# Population State System

| Field | Value |
|--------|-------|
| System | World Simulation |
| Document | Population State |
| Location | Canon/Systems/World_Simulation/Population_State.md |
| Version | 0.1 |
| Status | Working Canon |
| Scope | Population Behavior, Cohesion, Adaptation and Movement |
| Last Updated | 2026-08-09 |

> *"Populations do not react to crises as one body. They react as millions of people with different information, responsibilities, resources and reasons to stay."*

---

# Purpose

The Population State system defines how civilian populations respond to changing world conditions inside Project Ascension.

The system models broad population behavior including:

- confidence
- concern
- fear
- preparedness
- cooperation
- social cohesion
- workforce participation
- resource behavior
- migration
- unrest
- community organization
- adaptation
- demographic pressure
- recovery

Population State connects physical world conditions to human behavior.

Conceptually:

```text
WORLD CONDITIONS
      │
      ▼
INFORMATION
      │
      ▼
PERCEPTION
      │
      ▼
POPULATION RESPONSE
      │
      ▼
BEHAVIOR
      │
      ▼
WORLD CONDITIONS
```

Population behavior therefore becomes part of the simulation rather than a scripted reaction to events.

---

# Core Principle

A population is not a single actor.

The simulation should never assume:

```text
EVENT
  ↓
EVERYONE REACTS THE SAME WAY
```

Instead:

```text
EVENT
  │
  ▼
DIFFERENT INFORMATION
  │
  ▼
DIFFERENT PERCEPTIONS
  │
  ▼
DIFFERENT RESOURCES
  │
  ▼
DIFFERENT RESPONSIBILITIES
  │
  ▼
DIFFERENT RESPONSES
```

Some people leave.

Some stay.

Some prepare.

Some ignore the problem.

Some help others.

Some exploit the situation.

Some continue working.

Most may do several of these things at different times.

---

# Population State Is Aggregate

Population State represents broad patterns.

It does not simulate every individual citizen.

Individual characters belong primarily to:

```text
Characters/
Relationships/
Narrative/
```

Population State describes the environment from which individual behavior emerges.

---

# Population Groups

Where useful, a regional population may be divided into Population Groups.

Examples include:

```text
Urban Residents
Rural Residents
Infrastructure Workers
Healthcare Workers
Emergency Personnel
Families
Elderly Population
Students
Displaced Population
Recent Migrants
```

Groups should only exist where their differences matter to simulation.

---

# Population Group Principle

Groups should be created because they possess meaningfully different:

- resources
- exposure
- information
- responsibilities
- mobility
- behavior

They should not exist merely to increase simulation detail.

---

# Core Population Domains

A regional Population State should track:

```text
POPULATION STATE
│
├── Population Scale
├── Population Trend
├── Public Confidence
├── Public Concern
├── Perceived Threat
├── Preparedness
├── Social Cohesion
├── Cooperation
├── Institutional Trust
├── Workforce Participation
├── Resource Behavior
├── Mobility
├── Migration Pressure
├── Unrest Pressure
├── Adaptation Capacity
└── Recovery Capacity
```

---

# Population Scale

Population Scale describes the broad size of the population being simulated.

It may use:

```text
Exact Estimate
```

or:

```text
VERY SMALL
SMALL
MODERATE
LARGE
VERY LARGE
```

Exact population values should only be used where useful.

---

# Population Density

Population Density affects:

- infrastructure demand
- housing
- supply
- evacuation
- transportation
- disease
- social interaction
- local production

Conceptual states:

```text
VERY LOW
LOW
MODERATE
HIGH
VERY HIGH
```

---

# Population Trend

Population Trend describes whether population size is changing.

Conceptual values:

```text
RAPIDLY GROWING
GROWING
STABLE
DECLINING
RAPIDLY DECLINING
VOLATILE
```

Possible causes include:

- births
- deaths
- migration
- evacuation
- economic change
- environmental conditions
- security
- resource availability

---

# Population State

A broad descriptive state may summarize current civilian conditions.

Possible values:

```text
CALM
ATTENTIVE
CONCERNED
ANXIOUS
MOBILIZING
VOLATILE
DISPLACED
FRAGMENTED
```

This state should be derived from underlying conditions.

It should not independently drive behavior.

---

# Calm

```text
CALM
```

Daily routines remain dominant.

Most people expect normal institutions and systems to continue functioning.

This does not mean nobody is concerned.

---

# Attentive

```text
ATTENTIVE
```

A noticeable portion of the population is monitoring changing conditions.

Possible behaviors include:

- following news more closely
- checking supplies
- discussing contingencies
- contacting family

Normal routines remain dominant.

---

# Concerned

```text
CONCERNED
```

The population broadly recognizes meaningful disruption.

Possible behaviors include:

- increased purchasing
- voluntary conservation
- travel changes
- family coordination
- increased information seeking

---

# Anxious

```text
ANXIOUS
```

Uncertainty increasingly affects decisions.

Possible effects include:

- stockpiling
- reduced travel
- absenteeism
- financial caution
- migration planning
- rumor sensitivity

Anxiety does not automatically produce disorder.

---

# Mobilizing

```text
MOBILIZING
```

Large parts of the population begin taking organized action.

Examples:

- evacuation
- mutual aid
- volunteering
- neighborhood organization
- resource preparation
- community defense

Mobilization may be constructive or defensive.

---

# Volatile

```text
VOLATILE
```

Population behavior becomes highly sensitive to events.

Small information or resource shocks may create large behavioral changes.

Possible outcomes include:

- demonstrations
- sudden migration
- rapid stockpiling
- conflict
- mass cooperation

Volatile does not automatically mean violent.

---

# Displaced

```text
DISPLACED
```

A significant portion of the population no longer resides in its normal community.

This may result from:

- evacuation
- conflict
- infrastructure failure
- environmental conditions
- resource shortages

---

# Fragmented

```text
FRAGMENTED
```

The population no longer behaves as a broadly connected regional society.

Communities may operate independently with limited shared institutions or information.

Fragmented does not mean socially dysfunctional.

Local communities may possess very high cohesion.

---

# Public Confidence

Public Confidence represents expectations that society and institutions will remain capable of handling current conditions.

Conceptual states:

```text
HIGH
FUNCTIONAL
STRAINED
LOW
CRITICAL
```

Confidence may influence:

- consumption
- investment
- travel
- compliance
- migration
- cooperation

---

# Confidence Is Not Trust

Confidence and Institutional Trust must remain separate.

Example:

```text
Government Trust:
LOW

Public Confidence:
HIGH
```

People may distrust government while believing local systems will continue functioning.

Alternatively:

```text
Government Trust:
HIGH

Public Confidence:
LOW
```

People may trust officials while believing the situation itself is extremely dangerous.

---

# Public Concern

Public Concern represents how much attention the population is giving to potential disruption.

Conceptual states:

```text
LOW
MODERATE
HIGH
SEVERE
```

Concern may exist without fear.

A prepared population may be highly concerned but behave calmly.

---

# Perceived Threat

Perceived Threat represents how dangerous the population believes current conditions are.

Conceptual states:

```text
MINIMAL
LOW
MODERATE
HIGH
EXTREME
```

Perceived Threat is derived from Information State and personal experience.

It may differ from actual threat.

---

# Actual Threat Versus Perceived Threat

Example:

```text
Actual Threat:
HIGH

Perceived Threat:
LOW
```

Possible result:

```text
Delayed preparation
Low evacuation
Continued normal behavior
```

Conversely:

```text
Actual Threat:
LOW

Perceived Threat:
HIGH
```

may produce:

```text
Stockpiling
Migration
Economic disruption
```

Perception changes the world even when it is inaccurate.

---

# Normalcy Bias

Populations often interpret unusual events through familiar experience.

Conceptually:

```text
UNUSUAL EVENT
      ↓
FAMILIAR EXPLANATION
      ↓
EXPECTATION OF NORMAL RECOVERY
```

This may delay behavioral change.

Normalcy bias should not be treated as stupidity.

It is often a reasonable response when most previous disruptions have been temporary.

---

# Threat Adaptation

Repeated disruption may change expectations.

Example:

```text
First blackout:
Unexpected crisis.

Tenth blackout:
Known inconvenience.
```

The same physical event may produce less concern once populations develop routines for dealing with it.

---

# Preparedness

Preparedness represents the ability of households and communities to absorb short-term disruption.

Possible factors include:

- food reserves
- water
- medicine
- backup power
- transportation
- emergency knowledge
- family plans
- local networks

Conceptual states:

```text
HIGH
MODERATE
LOW
MINIMAL
```

---

# Preparedness Distribution

Preparedness should not be assumed to be equal.

Example:

```text
Regional Preparedness:
MODERATE

High-Income Households:
HIGH

Urban Apartment Population:
LOW

Rural Communities:
HIGH
```

Local differences may strongly affect behavior.

---

# Household Buffers

Households possess buffers similar to infrastructure systems.

Examples:

```text
Food
Water
Medicine
Money
Fuel
Battery Power
Transportation
```

Buffers reduce immediate response pressure.

---

# Buffer Depletion

Prolonged disruption consumes household buffers.

Conceptually:

```text
DISRUPTION
   │
   ▼
HOUSEHOLD BUFFER
   │
   ▼
BUFFER DECLINES
   │
   ▼
BEHAVIOR CHANGES
```

A population that remains calm during the first three days may behave very differently after three weeks.

---

# Social Cohesion

Social Cohesion represents the degree to which people identify with and cooperate within their communities.

Conceptual states:

```text
STRONG
FUNCTIONAL
STRAINED
FRAGMENTED
HOSTILE
```

Cohesion may be influenced by:

- trust
- fairness
- shared identity
- leadership
- resource distribution
- historical experience
- external threats

---

# Social Cohesion Is Not Uniformity

A cohesive population may contain:

- political disagreement
- cultural differences
- economic inequality
- competing interests

Cohesion means enough shared relationships and expectations exist to support cooperation.

---

# Cooperation

Cooperation represents actual collaborative behavior.

Examples include:

- mutual aid
- volunteering
- sharing resources
- neighborhood organization
- emergency response
- collective repair

Conceptual states:

```text
HIGH
FUNCTIONAL
LIMITED
LOW
HOSTILE
```

---

# Cohesion Versus Cooperation

These must remain distinct.

Example:

```text
Social Cohesion:
LOW

Cooperation:
HIGH
```

may occur during a common external threat.

Conversely:

```text
Social Cohesion:
HIGH

Cooperation:
LOW
```

may occur when no collective action is currently necessary.

---

# Mutual Aid

Mutual Aid represents informal or semi-formal cooperation outside normal government systems.

Examples:

- food sharing
- transportation
- childcare
- medical assistance
- shelter
- repair
- communication networks

Mutual Aid may significantly increase regional resilience.

---

# Community Formation

During prolonged disruption, new community structures may emerge.

Examples:

```text
Neighborhood Councils
Mutual-Aid Networks
Food Cooperatives
Local Radio Networks
Community Defense
Repair Groups
```

These structures may later evolve into formal institutions.

---

# Institutional Trust

Population groups may maintain trust toward:

- national government
- regional government
- local government
- military
- police
- media
- scientists
- corporations
- community organizations

Trust should interact with Information State and Authority State.

---

# Trust Distribution

Different population groups may trust different institutions.

Example:

```text
Urban Population:
Regional Government = HIGH

Rural Population:
Regional Government = LOW

Local Government:
HIGH across both groups
```

The simulation should allow this where relevant.

---

# Workforce Participation

Modern systems depend upon people continuing to work.

Workforce Participation represents the proportion of normal economic and institutional labor that remains active.

Conceptual states:

```text
NORMAL
HIGH
MODERATE
LOW
CRITICAL
```

---

# Workforce Pressure

People may stop working because of:

- illness
- transportation failure
- family responsibilities
- fear
- evacuation
- unpaid wages
- security
- infrastructure failure

This creates systemic consequences.

---

# Essential Workforce

Some workers have disproportionate systemic importance.

Examples include:

- power technicians
- water operators
- healthcare workers
- logistics workers
- emergency services
- telecommunications engineers
- fuel workers
- transportation workers

Essential Workforce availability may therefore be tracked separately.

---

# Workforce Feedback

Example:

```text
Transportation:
DEGRADED
      ↓
Worker Attendance:
DECLINES
      ↓
Infrastructure Staffing:
STRAINED
      ↓
Infrastructure Condition:
DEGRADES
      ↓
Transportation:
DEGRADES FURTHER
```

Population behavior can create infrastructure cascades.

---

# Resource Behavior

Resource Behavior describes how populations interact with scarce or potentially scarce goods.

Possible states include:

```text
NORMAL
CAUTIOUS
CONSERVING
STOCKPILING
RATIONING
COMPETING
```

---

# Normal Resource Behavior

```text
NORMAL
```

Consumption remains broadly consistent with ordinary patterns.

---

# Cautious Resource Behavior

```text
CAUTIOUS
```

People begin purchasing or retaining somewhat more essential goods.

---

# Conserving

```text
CONSERVING
```

People deliberately reduce consumption.

This may decrease pressure on infrastructure and supply.

---

# Stockpiling

```text
STOCKPILING
```

Households attempt to increase reserves.

Stockpiling may be rational at an individual level while creating collective distribution pressure.

---

# Rationing

```text
RATIONING
```

Resource consumption is actively limited.

Rationing may be:

- voluntary
- community organized
- market driven
- authority imposed

---

# Competing

```text
COMPETING
```

Resource access increasingly depends upon competition between individuals or groups.

This may include:

- price competition
- queues
- political pressure
- black markets
- physical conflict

Physical conflict should not be assumed.

---

# Panic Buying

Panic Buying should not exist as a generic automatic behavior.

It should emerge from combinations such as:

```text
HIGH PERCEIVED SHORTAGE
+
LOW CONFIDENCE
+
HIGH INFORMATION PRESSURE
+
LOW HOUSEHOLD BUFFER
```

Even then, not everyone participates.

---

# Supply Feedback

Example:

```text
Rumor:
Fuel shortage imminent
      ↓
Stockpiling
      ↓
Demand spike
      ↓
Distribution shortage
      ↓
Visible queues
      ↓
Rumor credibility increases
      ↓
More stockpiling
```

Population behavior can create self-reinforcing supply effects.

---

# Mobility

Mobility represents whether people can physically move through the region.

Factors include:

- transportation
- fuel
- security
- road access
- health
- finances
- authority restrictions

Conceptual states:

```text
HIGH
FUNCTIONAL
LIMITED
RESTRICTED
MINIMAL
```

---

# Mobility Is Not Migration

Mobility represents capability.

Migration represents behavior.

Example:

```text
Mobility:
HIGH

Migration:
LOW
```

People can leave but choose to stay.

---

# Stay Versus Leave

Migration decisions should consider both push and pull factors.

Conceptually:

```text
LEAVE PRESSURE
│
├── Threat
├── Shortage
├── Infrastructure Failure
├── Unemployment
├── Political Pressure
└── Family Elsewhere

STAY PRESSURE
│
├── Home
├── Family
├── Employment
├── Property
├── Community
├── Familiarity
└── Local Resources
```

Migration occurs when these pressures combine with actual mobility.

---

# Migration Pressure

Conceptual states:

```text
LOW
MODERATE
HIGH
SEVERE
EXTREME
```

High Migration Pressure does not automatically mean high migration.

People may lack the ability or willingness to leave.

---

# Migration State

Possible regional migration states:

```text
STABLE
INBOUND
OUTBOUND
TRANSIT
MIXED
MASS DISPLACEMENT
```

---

# Inbound Migration

Incoming population may increase:

- workforce
- skills
- trade
- community size

It may also increase:

- housing demand
- food demand
- infrastructure pressure
- political tension

Consequences depend upon regional capacity.

---

# Outbound Migration

Outbound migration may reduce immediate resource demand.

It may also remove:

- workers
- specialists
- families
- institutional capacity
- economic activity

Migration is therefore not simply a pressure-release mechanism.

---

# Selective Migration

Migration is rarely demographically neutral.

Those most capable of leaving may depart first.

Possible consequences include loss of:

- technical expertise
- wealth
- young workers
- political leadership

Alternatively, specialized workers may remain because their roles become more important.

---

# Displacement

Displacement differs from ordinary migration.

Displaced populations often possess:

- fewer resources
- limited planning
- uncertain destination
- disrupted social networks

This may create significant humanitarian pressure.

---

# Refuge and Hosting Capacity

Regions may possess a Hosting Capacity.

It depends upon:

- housing
- food
- water
- employment
- infrastructure
- social cohesion
- governance

Conceptual states:

```text
HIGH
MODERATE
LOW
CRITICAL
```

---

# Demographic Pressure

Demographic Pressure represents stress created by population composition and movement.

Factors may include:

- rapid population growth
- rapid decline
- displacement
- aging
- workforce shortages
- dependency ratios

Conceptual states:

```text
LOW
MODERATE
HIGH
SEVERE
```

---

# Public Order

Population State should track social behavior separately from Security State.

Public Order may be represented conceptually as:

```text
STABLE
STRAINED
VOLATILE
DISRUPTED
```

Security State should handle actual security capability and threats.

Population State handles civilian behavior contributing to public order.

---

# Unrest Pressure

Unrest Pressure represents conditions increasing the probability of organized public confrontation.

Sources may include:

- shortages
- inequality
- perceived injustice
- low legitimacy
- unemployment
- fear
- political conflict
- misinformation

Conceptual states:

```text
LOW
MODERATE
HIGH
SEVERE
CRITICAL
```

---

# Unrest Is Not Automatic

High Unrest Pressure does not guarantee unrest.

Strong cohesion, trusted leadership or credible improvement may prevent escalation.

Similarly, a single triggering event may create unrest when underlying pressure is already high.

---

# Protest

Protest should remain distinct from disorder.

Possible forms include:

```text
Demonstration
Strike
Civil disobedience
Boycott
Occupation
Political assembly
```

These may occur inside a stable society.

---

# Disorder

Disorder may include:

- uncontrolled crowd behavior
- looting
- widespread property damage
- violent confrontation

Such behavior should require supporting conditions.

It should not be used as the default civilian response to crisis.

---

# Crime Pressure

Economic and institutional disruption may affect crime.

Possible influences include:

- scarcity
- policing capacity
- black markets
- unemployment
- social cohesion

Crime belongs primarily to Security systems but Population State may contribute pressure.

---

# Informal Economy

As formal markets become unreliable, populations may develop:

- barter
- local currency
- informal trade
- repair economies
- labor exchange
- community distribution

Informal economic activity may represent adaptation rather than breakdown.

---

# Black Markets

Black markets may emerge when:

```text
Demand remains high
+
Legal supply becomes restricted
+
Enforcement is limited
```

They may provide otherwise unavailable goods while creating other risks.

---

# Population Adaptation

Adaptation represents the ability of people to change behavior and institutions in response to persistent conditions.

Examples include:

- conservation
- local agriculture
- shared transport
- repair culture
- new work patterns
- mutual aid
- local trade
- community governance
- decentralized communications

Conceptual states:

```text
HIGH
MODERATE
LOW
MINIMAL
```

---

# Adaptation Lag

Adaptation takes time.

Conceptually:

```text
DISRUPTION
    ↓
INITIAL RESPONSE
    ↓
EXPERIMENTATION
    ↓
NEW ROUTINES
    ↓
ADAPTATION
```

Early instability may therefore decline even when the underlying disruption remains.

---

# Learned Resilience

Communities may become better at handling repeated disruption.

Example:

```text
YEAR 1:
72-hour blackout causes major disruption.

YEAR 5:
72-hour blackout activates established community routines.
```

The infrastructure event is similar.

Population response has changed.

---

# Behavioral Memory

Populations should remember significant experiences.

Examples:

- failed evacuation
- successful rationing
- government abandonment
- community cooperation
- violent conflict
- prolonged shortage
- outside assistance

These experiences influence future behavior.

---

# Preparedness Memory

A population that has experienced previous shortages may maintain higher preparedness.

Example:

```text
Past Event:
Three-week fuel shortage

Later Effect:
Higher household fuel reserves
Greater willingness to conserve
Earlier response to warning
```

History changes resilience.

---

# Trauma and Fatigue

Repeated disruption may also reduce resilience.

Possible effects include:

- exhaustion
- reduced trust
- lower participation
- increased migration
- reduced tolerance for restrictions

Population adaptation is not always positive.

---

# Crisis Fatigue

Repeated warnings may reduce response.

Example:

```text
WARNING 1:
Strong response

WARNING 5:
Moderate response

WARNING 12:
Low response
```

unless previous warnings were consistently credible and meaningful.

This links directly to Information State.

---

# Social Thresholds

Some population behaviors may change rapidly after thresholds are crossed.

Example:

```text
Most stores remain stocked.
      ↓
Population remains cautious.

Visible shortages appear.
      ↓
Perceived scarcity rises rapidly.

Queues become widespread.
      ↓
Stockpiling accelerates.
```

The transition may be nonlinear.

---

# Behavioral Cascades

People observe one another.

Example:

```text
Small migration begins
      ↓
Others interpret departure as evidence
      ↓
Perceived Threat increases
      ↓
More people leave
```

Behavior itself becomes information.

---

# Positive Behavioral Cascades

The same principle may produce constructive effects.

Example:

```text
Neighbors organize food distribution
      ↓
Visible cooperation increases
      ↓
Confidence increases
      ↓
More people participate
      ↓
Community resilience increases
```

World Simulation should model both.

---

# Social Proof

Population behavior may therefore influence perception.

Conceptually:

```text
WHAT OTHER PEOPLE DO
        ↓
INFORMATION
        ↓
MY PERCEPTION
        ↓
MY BEHAVIOR
```

This is particularly important when reliable institutional information is scarce.

---

# Leadership

Local leaders may strongly influence population response.

Leadership may come from:

- elected officials
- community organizers
- religious leaders
- technical experts
- respected residents
- faction leaders

Leadership effectiveness should depend upon trust and demonstrated competence.

---

# Community Trust

Local trust networks may remain strong after institutional trust declines.

Example:

```text
National Government Trust:
LOW

Regional Government Trust:
MODERATE

Local Community Trust:
HIGH
```

This may allow effective local adaptation.

---

# Population Fragmentation

Population Fragmentation occurs when different groups no longer share enough:

- information
- trust
- institutions
- identity
- resources

to behave as a broadly connected society.

Fragmentation may be:

```text
SOCIAL
GEOGRAPHIC
INFORMATIONAL
POLITICAL
ECONOMIC
```

---

# Fragmentation Is Not Isolation

Groups may remain economically connected while politically fragmented.

They may remain politically connected while informationally fragmented.

Different forms of fragmentation should not be treated as identical.

---

# Regional Population Differences

Two neighboring regions may respond very differently to the same crisis.

Example:

```text
REGION A

Preparedness:
HIGH

Social Cohesion:
HIGH

Institutional Trust:
MODERATE

Result:
Conservation + Mutual Aid
```

versus:

```text
REGION B

Preparedness:
LOW

Social Cohesion:
STRAINED

Institutional Trust:
LOW

Result:
Stockpiling + Outbound Migration
```

The event is identical.

The social context is not.

---

# Population and Information

Population behavior is primarily influenced by perceived conditions.

Therefore:

```text
INFORMATION STATE
      ↓
PERCEPTION
      ↓
POPULATION STATE
```

Information accuracy matters because perception influences behavior.

---

# Population and Authority

Authority may influence population through:

- communication
- services
- regulation
- rationing
- evacuation
- enforcement
- leadership

Population response affects authority through:

- compliance
- legitimacy
- workforce
- protest
- participation

Conceptually:

```text
AUTHORITY
    ↕
POPULATION
```

---

# Population and Infrastructure

Infrastructure affects daily life.

Examples:

```text
Power
Water
Transportation
Telecommunications
Healthcare
```

Population behavior affects infrastructure through:

```text
Demand
Workforce
Conservation
Movement
Damage
Repair
```

---

# Population and Supply

Supply availability influences:

- confidence
- stockpiling
- migration
- cooperation
- unrest

Population behavior influences supply through:

- demand
- conservation
- production
- distribution
- informal trade

---

# Population and Security

Security conditions influence:

- movement
- confidence
- migration
- community organization

Population behavior may influence security through:

- cooperation
- reporting
- protest
- community defense
- disorder

---

# Population and Recovery

Population participation is one of the strongest components of recovery.

Recovery may depend upon:

- workforce
- cooperation
- technical skill
- community organization
- willingness to remain
- willingness to rebuild

A region with damaged infrastructure but strong population resilience may recover faster than a technically superior region with severe social fragmentation.

---

# Population Response Model

A conceptual response model:

```text
PERCEIVED CONDITIONS
        +
HOUSEHOLD RESOURCES
        +
SOCIAL CONTEXT
        +
INSTITUTIONAL TRUST
        +
PERSONAL RESPONSIBILITIES
        +
MOBILITY
        +
HISTORICAL MEMORY
        ↓
POPULATION BEHAVIOR
```

No single variable should determine response.

---

# Example Population State

```text
POPULATION STATE

Region:
Northern Virginia

Historical Era:
WS-02 — The Transition

Population Scale:
VERY LARGE

Population Density:
VERY HIGH

Population Trend:
DECLINING

Population State:
ANXIOUS

Public Confidence:
STRAINED

Public Concern:
HIGH

Perceived Threat:
HIGH

Preparedness:
MODERATE

Social Cohesion:
FUNCTIONAL

Cooperation:
FUNCTIONAL

Institutional Trust:
STRAINED

Workforce Participation:
MODERATE

Essential Workforce:
STRAINED

Resource Behavior:
STOCKPILING

Mobility:
LIMITED

Migration Pressure:
HIGH

Migration State:
OUTBOUND

Unrest Pressure:
MODERATE

Public Order:
STRAINED

Adaptation Capacity:
HIGH

Recovery Capacity:
MODERATE

Trend:
VOLATILE

Confidence:
MODERATE
```

---

# Fractured World Example

```text
POPULATION STATE

Region:
Shenandoah Valley

Historical Era:
WS-03 — The Fractured World

Population Scale:
MODERATE

Population Density:
LOW

Population Trend:
STABLE

Population State:
MOBILIZING

Public Confidence:
FUNCTIONAL

Public Concern:
MODERATE

Perceived Threat:
MODERATE

Preparedness:
HIGH

Social Cohesion:
STRONG

Cooperation:
HIGH

Institutional Trust:
LOCALIZED / HIGH

Workforce Participation:
HIGH

Essential Workforce:
FUNCTIONAL

Resource Behavior:
CONSERVING

Mobility:
FUNCTIONAL

Migration Pressure:
LOW

Migration State:
STABLE

Unrest Pressure:
LOW

Public Order:
STABLE

Adaptation Capacity:
HIGH

Recovery Capacity:
HIGH

Information Horizon:
REGIONAL
```

This region possesses fewer technological resources than pre-Collapse society.

Its population may nevertheless be socially more resilient.

---

# Displaced Population Example

```text
POPULATION GROUP

Type:
Displaced Population

Population:
42,000

Origin:
Neighboring Metropolitan Region

Current Location:
Temporary Regional Settlements

Preparedness:
MINIMAL

Resource Dependency:
HIGH

Mobility:
LIMITED

Institutional Trust:
LOW

Social Cohesion:
MODERATE

Host Community Relations:
STRAINED

Trend:
STABILIZING
```

This allows migration to produce persistent simulation consequences.

---

# Population Event Generation

Population events should emerge from state combinations.

Example:

```text
Public Concern:
HIGH

Supply:
CONSTRAINED

Institutional Trust:
HIGH

Social Cohesion:
HIGH
```

Possible event:

```text
Community conservation campaign
```

Alternative:

```text
Public Concern:
HIGH

Supply:
CONSTRAINED

Institutional Trust:
LOW

Information Reliability:
UNSTABLE
```

Possible events:

```text
Stockpiling
Black-market growth
Outbound migration
Public demonstrations
```

The same shortage does not produce the same social outcome everywhere.

---

# Population Opportunity Generation

Population State should also create positive events.

Examples:

```text
Volunteer networks form.

Local food cooperative expands.

Community radio network established.

Displaced technical workers join repair teams.

Neighborhood groups restore local services.

New trade market forms.
```

Human behavior should be a source of recovery as well as pressure.

---

# Population Decision Timescale

Different behaviors operate at different timescales.

## Immediate

```text
Hours → Days

Information seeking
Purchasing
Travel changes
Family contact
```

## Short Term

```text
Days → Weeks

Stockpiling
Evacuation
Workforce changes
Mutual aid
Protest
```

## Medium Term

```text
Weeks → Months

Migration
Informal markets
Community organization
Employment changes
```

## Long Term

```text
Months → Years

New institutions
Demographic change
Regional identity
Adapted lifestyles
Political transformation
```

---

# Population Update Cycle

A conceptual update cycle may follow:

```text
1. Read current Population State.
2. Read Infrastructure State.
3. Read Supply conditions.
4. Read Security conditions.
5. Read Authority State.
6. Read Information State.
7. Determine perceived conditions.
8. Apply household buffers.
9. Apply preparedness.
10. Apply social cohesion.
11. Apply institutional trust.
12. Apply historical memory.
13. Process workforce behavior.
14. Process resource behavior.
15. Process mobility.
16. Process migration.
17. Process cooperation.
18. Process unrest pressure.
19. Process adaptation.
20. Generate significant population events.
21. Update Population State.
22. Update regional memory.
```

The exact technical implementation may change.

The causal logic should remain understandable.

---

# Population Simulation Resolution

## High Resolution

Used for:

- player region
- major population movements
- active crises
- campaign-critical communities

May track:

```text
Population Groups
Preparedness Distribution
Trust Distribution
Migration Groups
Community Networks
Behavioral Events
```

---

## Medium Resolution

Used for nearby regions.

Tracks:

```text
Population State
Confidence
Preparedness
Cohesion
Workforce
Migration
Unrest
Adaptation
```

---

## Low Resolution

Used for distant regions.

Tracks:

```text
Population Trend
Broad Population State
Migration
Cohesion
Adaptation
Major Events
```

---

# Population Compression

Not every behavioral event needs permanent storage.

The simulation should preserve events that change:

- demographics
- trust
- institutions
- regional memory
- migration
- social structure
- player relationships

Routine behavior may be discarded after affecting current state.

---

# Minimum Population State

A minimum viable Population State should contain:

```text
Population Scale
Population Density
Population Trend

Population State

Public Confidence
Public Concern
Perceived Threat
Preparedness
Social Cohesion
Cooperation
Institutional Trust
Workforce Participation
Essential Workforce
Resource Behavior
Mobility
Migration Pressure
Migration State
Unrest Pressure
Public Order
Adaptation Capacity
Recovery Capacity
Trend
Confidence
```

Population Groups should only be created where meaningful differences require them.

---

# Population Consistency Rules

## Rule 1

A population is not a single actor.

---

## Rule 2

Population behavior should respond primarily to perceived conditions, not hidden simulation truth.

---

## Rule 3

Concern does not equal panic.

---

## Rule 4

Fear does not automatically create violence.

---

## Rule 5

Protest does not equal disorder.

---

## Rule 6

High migration pressure does not automatically produce migration.

---

## Rule 7

Mobility and migration are separate.

---

## Rule 8

Preparedness must be capable of delaying behavioral pressure.

---

## Rule 9

Household buffers must deplete over time.

---

## Rule 10

Stockpiling may be individually rational while collectively destabilizing.

---

## Rule 11

Conservation may reduce systemic pressure.

---

## Rule 12

Social cohesion and institutional trust are separate.

---

## Rule 13

Social cohesion and cooperation are separate.

---

## Rule 14

Population groups may respond differently to the same conditions.

---

## Rule 15

Displaced populations should retain origin, history and social context.

---

## Rule 16

Migration may create benefits as well as pressure.

---

## Rule 17

Population behavior can create both negative and positive cascades.

---

## Rule 18

Repeated crises should change future population behavior.

---

## Rule 19

Adaptation may improve resilience without restoring old systems.

---

## Rule 20

Community organization should be capable of creating new institutions.

---

## Rule 21

Local resilience may increase while national systems deteriorate.

---

## Rule 22

The simulation should never use civilian irrationality as a shortcut for creating drama.

---

# Guiding Questions

For every major population response, the simulation should be capable of answering:

**What do people believe is happening?**

**Why do they believe it?**

**How concerned are they?**

**What resources do they possess?**

**How prepared are they?**

**Who do they trust?**

**Who do they cooperate with?**

**Can they continue working?**

**Can they move?**

**Do they want to move?**

**What reasons do they have to stay?**

**What are they doing with resources?**

**How are communities organizing?**

**What have they learned from previous crises?**

**What happens if current conditions continue?**

These questions should produce behavior more convincingly than a generic panic variable.

---

# Core Design Principle

Project Ascension should never assume:

```text
CRISIS
=
PANIC
```

Instead:

```text
CRISIS
      │
      ▼
INFORMATION
      │
      ▼
PERCEPTION
      │
      ├── PREPARE
      ├── WAIT
      ├── CONSERVE
      ├── WORK
      ├── HELP
      ├── LEAVE
      ├── ORGANIZE
      ├── PROTEST
      └── CONTINUE NORMAL LIFE
```

Every response may be rational from the perspective of the person making the decision.

---

# Relationship to The Connected World

During The Connected World, populations generally possess:

- high mobility
- high infrastructure dependency
- large information horizons
- extensive formal supply systems
- limited need for household self-sufficiency

This creates enormous efficiency.

It also creates specific dependencies.

---

# Relationship to The Transition

During The Transition:

```text
Confidence declines.

Preparedness increases unevenly.

Information becomes less reliable.

Workforce participation becomes unstable.

Migration begins.

Local networks become more important.
```

Different regions begin diverging socially.

---

# Relationship to The Fractured World

The Fractured World should not consist of populations permanently trapped in emergency behavior.

Over time:

```text
EMERGENCY
    ↓
EXPERIMENTATION
    ↓
ADAPTATION
    ↓
ROUTINE
```

New normality emerges.

A person born twenty years after The Collapse may not consider regional radio, local food production and limited long-distance travel unusual.

That is simply their world.

---

# Relationship to The Reconnection

Reconnection creates new population pressures.

Communities may encounter:

- outsiders
- new information
- new markets
- unfamiliar technology
- returning institutions
- competing identities

Some populations may welcome reconnection.

Others may fear losing local autonomy.

Still others may see opportunity.

Reconnection is therefore a social process, not merely an infrastructure project.

---

# World Simulation Loop

With Population State established, the major World Simulation loop now becomes:

```text
WORLD STATE
     │
     ▼
REGIONAL STATE
     │
     ├──────────────┐
     ▼              │
INFRASTRUCTURE      │
     │              │
     ▼              │
INFORMATION         │
     │              │
     ▼              │
AUTHORITY           │
     │              │
     ▼              │
POPULATION          │
     │              │
     ▼              │
BEHAVIOR            │
     │              │
     └──────────────┘
```

The world changes.

People observe the change.

Institutions respond.

People respond to both the event and the institutions.

Their behavior changes the world again.

---

# Current Status

```text
WORLD SIMULATION

README.md
COMPLETE

World_State.md
FOUNDATION DEFINED

Regional_State.md
FOUNDATION DEFINED

Infrastructure_State.md
FOUNDATION DEFINED

Information_State.md
FOUNDATION DEFINED

Authority_State.md
FOUNDATION DEFINED

Population_State.md
FOUNDATION DEFINED

Escalation_and_Recovery.md
PENDING
```

---

# Next Document

The next recommended document is:

```text
Canon/Systems/World_Simulation/Escalation_and_Recovery.md
```

This is the document that will connect everything we have now defined.

The existing files tell us:

```text
WHAT EXISTS
```

`Escalation_and_Recovery.md` should define:

```text
HOW IT CHANGES
```

It should establish:

- pressure accumulation
- resilience
- thresholds
- state transitions
- cascading effects
- reinforcing loops
- stabilizing loops
- shock events
- delayed effects
- recovery capacity
- adaptation
- intervention
- hysteresis
- permanent change
- regional divergence

Conceptually:

```text
PRESSURE
    │
    ▼
STRAIN
    │
    ▼
THRESHOLD
    │
    ├──────────────► ESCALATION
    │
    │
    └──────────────► STABILIZATION
                         │
                         ▼
                      RECOVERY
                         │
                         ▼
                      ADAPTATION
```

This becomes the **transition engine** of World Simulation.

It determines why a world state changes instead of merely declaring that it has changed.

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-09 | Initial population behavior, confidence, preparedness, cohesion, workforce, resource behavior, migration, unrest, adaptation and social-memory framework established. |