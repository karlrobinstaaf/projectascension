# PROJECT ASCENSION
# Life Generator

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Life Generator |
| Location | `Canon/Systems/Life/Life_Generator.md` |
| Parent Architecture | `Canon/Systems/Life/README.md` |
| Version | 2.0 |
| Status | ACTIVE CANON |
| Category | Systems / Life |
| Owner | Systems Architecture |
| Last Updated | 2026-08-29 |
| Primary Function | Generate causally coherent human life histories consistent with Canon, geography, history and the Human Model |

> **Lives are generated. Stories emerge.**

---

# 1. Purpose

The Life Generator creates believable human life histories inside Project Ascension.

It does not generate:

**NPCs.**

It does not generate:

**quest functions.**

It does not generate:

**game objects.**

It generates:

**people who have lived.**

Every generated person should feel as though they existed before the player encountered them.

They should possess:

- history
- family
- place
- culture
- experience
- relationships
- education
- work
- successes
- failures
- limitations
- memories
- opportunities
- current circumstances

The Life Generator therefore answers:

> **What sequence of plausible circumstances produced this particular person in this particular place at this particular moment?**

---

# 2. Core Philosophy

The Life Generator does not begin with:

```text
WHAT KIND OF CHARACTER
DOES THE STORY NEED?
```

It begins with:

```text
WHO COULD PLAUSIBLY
EXIST HERE?
```

This distinction is fundamental.

The generator should not construct people backward from narrative function.

Instead:

```text
WORLD
+
HISTORY
+
GEOGRAPHY
+
FAMILY
+
OPPORTUNITY
+
EXPERIENCE
+
CHOICE
+
CHANCE
+
TIME
=
PERSON.
```

Narrative significance may emerge later.

---

# 3. Life Generator vs Life System

The Life System defines:

```text
HOW HUMAN LIVES
SHOULD FUNCTION
ARCHITECTURALLY.
```

The Life Generator defines:

```text
HOW A SPECIFIC
COHERENT LIFE
IS CREATED.
```

Therefore:

```text
Life/README.md
=
SYSTEM RESPONSIBILITY.
```

```text
Life_Generator.md
=
GENERATION PROCESS.
```

The Life Generator must remain subordinate to the architectural principles defined in:

`Canon/Systems/Life/README.md`

---

# 4. Life Generator vs Character System

The Life Generator creates:

```text
THE PATH
TO THE PRESENT.
```

The Character System owns:

```text
THE PERSON
IN THE PRESENT.
```

Conceptually:

```text
LIFE GENERATOR
↓
biographical history
↓
CHARACTER INITIALIZATION
↓
living autonomous character
↓
future simulation.
```

Generation ends as the person's starting state becomes active simulation.

Their future is not generated in advance.

---

# 5. The Fundamental Generation Rule

Every generated element should answer:

> **Why is this true?**

If the generator produces:

```text
Profession:
Trauma Surgeon
```

there should be a plausible path involving:

```text
education

training

experience

location

time

opportunity

and

institutional access.
```

If the generator produces:

```text
Strong distrust of federal authority
```

there should ideally be plausible influences capable of contributing to that belief.

If the generator produces:

```text
Expert electrical-grid knowledge
```

the life should contain a credible route through which that expertise developed.

Generation should create:

**causal chains.**

Not disconnected attributes.

---

# 6. Primary Generation Flow

The conceptual Life Generation flow is:

```text
GENERATION CONTEXT
        ↓
BIRTH
        ↓
TIME PERIOD
        ↓
WORLD STATE EXPOSURE
        ↓
GEOGRAPHY
        ↓
FAMILY
        ↓
CULTURE
        ↓
CHILDHOOD CONDITIONS
        ↓
EDUCATION
        ↓
EARLY RELATIONSHIPS
        ↓
FORMATIVE EVENTS
        ↓
SKILLS / INTERESTS
        ↓
PROFESSIONAL DEVELOPMENT
        ↓
ADULT RELATIONSHIPS
        ↓
MAJOR LIFE EVENTS
        ↓
HISTORICAL EXPOSURE
        ↓
MIGRATION / LOCATION HISTORY
        ↓
EXPERTISE DEVELOPMENT
        ↓
CURRENT SOCIAL NETWORK
        ↓
CURRENT PURPOSE
        ↓
CURRENT SITUATION
        ↓
CHARACTER INITIALIZATION
        ↓
LIVING HUMAN.
```

The implementation may later parallelize parts of this flow.

The causal dependencies must remain.

---

# 7. Generation Context

Life generation should begin from known context.

Possible context may include:

```text
CURRENT DATE

CURRENT LOCATION

CURRENT WORLD STATE

REGION

SETTLEMENT

AGE RANGE

ROLE REQUIREMENTS

CAMPAIGN CONTEXT

EXISTING RELATIONSHIPS

KNOWN PROFESSION

KNOWN HISTORICAL FACTS.
```

Not every generation begins from zero.

The generator may need to fill gaps around already established facts.

---

# 8. Constraint-First Generation

Known canonical facts must become constraints.

Example:

```text
Required:

Age: 54

Location: Oakland

Profession: Electrical Engineer

Current World State:
Early Fracture
```

The generator should create a life compatible with these facts.

It should not regenerate them.

Conceptually:

```text
KNOWN FACTS
↓
CONSTRAINT SPACE
↓
PLAUSIBLE LIFE PATH
↓
PERSON.
```

---

# 9. Generation Modes

The Life Generator should support several conceptual generation modes.

## Full Generation

Used when very little is known.

The generator creates most of the life history.

## Constrained Generation

Used when some facts already exist.

Example:

```text
age

profession

location

family role

or

relationship.
```

The generator fills in compatible history.

## Player-Guided Generation

The player selects important elements.

The generator constructs plausible connecting history.

## Canon-Driven Generation

Used for individuals who must fit established historical conditions.

## Resolution Expansion

Used when an existing low-detail character becomes important.

The generator adds detail without rewriting established truth.

---

# 10. Input Authority

Generation inputs may originate from:

```text
CANON

PLAYER CHOICE

WORLD SIMULATION

REGIONAL STATE

SOCIETY

LIFE HISTORY

CHARACTER GENERATION FRAMEWORK

CAMPAIGN STATE

OR

CONTROLLED RANDOMNESS.
```

Input authority matters.

A canonical fact has greater authority than a generated possibility.

Therefore:

```text
CANON
>
ESTABLISHED SIMULATION STATE
>
PLAYER-LOCKED HISTORY
>
GENERATED DETAIL
>
RANDOM VARIATION.
```

Lower-authority generation must not contradict higher-authority state.

---

# 11. Birth

Generation begins with:

```text
BIRTH DATE

BIRTH LOCATION

FAMILY CONTEXT

INITIAL BIOLOGICAL CONDITIONS.
```

Birth date determines historical exposure possibilities.

Birth location establishes initial:

- geography
- language
- culture
- government
- infrastructure
- healthcare
- education
- socioeconomic conditions

These may later change.

---

# 12. Chronological Validity

Chronology must always be validated.

The generator must prevent:

```text
employment before plausible age

university before earlier education

children born before plausible parenthood

relationships before first contact

memory of events before birth

professional expertise before training

historical exposure after leaving a region

or

impossible overlapping life stages.
```

Time is a hard constraint.

---

# 13. World State Exposure

Generation must determine which World States the person experienced.

Conceptually:

```text
BIRTH YEAR
+
CURRENT YEAR
+
WORLD-STATE TIMELINE
=
POTENTIAL WORLD-STATE EXPOSURE.
```

But exposure must also include:

```text
AGE

LOCATION

AND

LOCAL CONDITIONS.
```

A person may technically live during State 03 while spending their childhood in a relatively stable region.

Their personal experience must reflect that.

---

# 14. Historical Exposure

The generator should compare a person's timeline with relevant historical events.

Conceptually:

```text
PERSON TIMELINE
∩
WORLD TIMELINE
∩
REGIONAL TIMELINE
=
POTENTIAL HISTORICAL EXPOSURE.
```

Then evaluate:

```text
WERE THEY PRESENT?

WOULD THEY KNOW?

WERE THEY AFFECTED?

HOW DIRECTLY?

AT WHAT AGE?
```

Only relevant events become personal history.

---

# 15. Historical DNA Generation

Historical DNA should emerge from actual exposure.

Example:

```text
EVENT:

Major regional infrastructure disruption.
```

Possible exposure:

```text
Age: 11

Location:
Affected region

Family consequence:
Parent temporarily unemployed

School consequence:
Three-week interruption

Long-term influence:
Higher familiarity with infrastructure failure.
```

Historical DNA is therefore:

```text
HISTORY EXPERIENCED
THROUGH A LIFE.
```

---

# 16. Geography

Geography must constrain generation.

The generator should know where a person lived during major life periods.

Conceptually:

```text
BIRTHPLACE
↓
CHILDHOOD LOCATION
↓
EDUCATION LOCATION
↓
WORK LOCATION
↓
MIGRATION
↓
CURRENT LOCATION.
```

Movement requires plausible cause.

---

# 17. Geographic Movement

Possible migration drivers include:

```text
family

education

employment

housing

relationships

war

security

climate

infrastructure

economics

politics

displacement

opportunity.
```

Movement should generate consequences.

Relocation may affect:

- relationships
- language
- education
- profession
- culture
- opportunity
- historical exposure

---

# 18. Family Generation

Family is one of the strongest early-generation contexts.

The generator may establish:

```text
parents

siblings

guardians

extended family

household structure

socioeconomic conditions

family culture

family profession patterns

family mobility

family stability

major family events.
```

Family generation should produce:

```text
CONTEXT.
```

Not:

```text
PERSONALITY DESTINY.
```

---

# 19. Family Causality

Family facts should interact.

Example:

```text
Parent profession:
Military logistics

↓

Frequent relocation

↓

Multiple childhood schools

↓

Broad geographic exposure

↓

Weak long-term childhood friendships

↓

High adaptation to relocation.
```

This does not dictate personality.

It creates plausible developmental context.

---

# 20. Socioeconomic Context

Economic background may influence:

```text
housing

education

healthcare

mobility

social networks

technology access

professional opportunity

family stress

travel

and

resilience.
```

Economic conditions should evolve over time.

A family may experience:

```text
wealth

stability

decline

recovery

poverty

or

rapid upward mobility.
```

---

# 21. Culture

Culture should influence the conditions under which the person develops.

Possible influences include:

```text
language

family expectations

religion

community

social roles

attitudes toward authority

education

work

relationships

and

identity.
```

Culture must never operate as:

```text
PERSONALITY PRESET.
```

Individuals remain varied.

---

# 22. Childhood

Childhood generation should establish enough context to explain later development.

Potential factors include:

```text
family stability

economic conditions

education

health

friendships

community

technology exposure

major moves

parental relationships

early interests

formative successes

formative failures.
```

Not every childhood requires trauma.

Ordinary childhoods are important.

---

# 23. Education Generation

Education should reflect:

```text
location

family resources

ability

interest

opportunity

historical period

technology

and

personal decisions.
```

Possible paths include:

```text
formal school

vocational education

university

military education

professional apprenticeship

self-directed learning

institutional training

AI-assisted education

or

interrupted education.
```

---

# 24. Education Does Not Equal Expertise

Completing education does not automatically create high expertise.

Expertise requires:

```text
EDUCATION
+
PRACTICE
+
EXPERIENCE
+
TIME.
```

Likewise:

significant expertise may sometimes develop outside formal education.

The generator should support both.

---

# 25. Interests

Interests may emerge from:

```text
family

school

friends

culture

chance

media

personal curiosity

technology

or

formative events.
```

Interests may later influence:

```text
education

profession

relationships

hobbies

and

identity.
```

Not all interests become professions.

---

# 26. Profession Generation

Profession should emerge from a plausible path.

Conceptually:

```text
INTEREST / OPPORTUNITY
↓
EDUCATION / TRAINING
↓
ENTRY ROLE
↓
EXPERIENCE
↓
CAREER DEVELOPMENT
↓
CURRENT PROFESSION.
```

Career paths may include:

```text
promotion

career change

unemployment

automation displacement

migration

retraining

entrepreneurship

retirement

or

professional decline.
```

---

# 27. Profession During The Transition

Transition-era profession generation must account for:

```text
AI AUGMENTATION

AUTOMATION

ROLE TRANSFORMATION

PRODUCTIVITY CHANGE

EXPERTISE PIPELINE DEGRADATION

AND

HUMAN CAPABILITY ATROPHY.
```

Two people with the same job title from different generations may possess very different practical capabilities.

---

# 28. Expertise Generation

Expertise must be causally earned.

Conceptually:

```text
EXPOSURE
↓
TRAINING
↓
PRACTICE
↓
REAL EXPERIENCE
↓
DIFFICULT EXPERIENCE
↓
EXPERTISE.
```

The generator should avoid:

```text
UNEXPLAINED EXPERT.
```

The rarer the expertise:

the stronger the expected developmental history.

---

# 29. Expertise Level Plausibility

Higher expertise should usually require combinations of:

```text
time

quality training

practice

high-complexity exposure

mentorship

failure

responsibility

and

continued use.
```

World-class expertise should be:

```text
RARE.
```

Not because the game requires rarity.

Because world-class humans are rare.

---

# 30. Opportunity

Potential does not guarantee opportunity.

The generator should distinguish:

```text
ABILITY

from

ACCESS.
```

A highly capable person may never receive elite education.

Another may receive extraordinary opportunity without becoming exceptional.

This creates realistic variation.

---

# 31. Life Events

Life Events should emerge throughout generation.

Possible categories:

```text
FAMILY

EDUCATION

RELATIONSHIP

CAREER

HEALTH

ECONOMIC

POLITICAL

HISTORICAL

MIGRATION

ACCIDENT

SUCCESS

FAILURE

LOSS

OPPORTUNITY

CONFLICT.
```

Events should not exist merely to make the biography interesting.

They should alter the life path when significant.

---

# 32. Event Generation

A Life Event may originate from:

```text
WORLD HISTORY

REGIONAL CONDITIONS

FAMILY STATE

RELATIONSHIP STATE

PROFESSION

HEALTH

CHANCE

OR

PERSONAL DECISION.
```

This keeps Life Events connected to the world.

---

# 33. Event Consequence

Every major Life Event should answer:

```text
WHAT CHANGED AFTER THIS?
```

Possible changes include:

```text
location

education

profession

relationship

health

resources

belief

opportunity

expertise

goal

or

social network.
```

If nothing meaningful changed:

the event may not need to become a major persistent Life Event.

---

# 34. Ordinary Periods

Lives should contain periods where:

```text
NOTHING HISTORICALLY DRAMATIC HAPPENS.
```

These periods may still contain:

- work
- friendships
- hobbies
- family
- routine
- learning
- travel
- relationships
- ordinary happiness
- ordinary frustration

This prevents generated biographies from becoming melodramatic.

---

# 35. Event Density

Event generation should avoid excessive density.

A person should not automatically experience:

```text
war

bereavement

divorce

career collapse

major illness

betrayal

disaster

and

heroic rescue
```

simply because these events make biographies dramatic.

Life is not a highlight reel of catastrophe.

---

# 36. Positive Life Events

Positive events should also matter.

Examples:

```text
friendship

love

mentorship

achievement

graduation

career success

birth of child

community belonging

travel

recovery

creative accomplishment

unexpected opportunity.
```

Positive history helps explain:

```text
WHAT THE PERSON
VALUES AND PROTECTS.
```

---

# 37. Chance

Controlled randomness may introduce:

```text
luck

accident

timing

unexpected opportunity

unexpected meeting

unexpected failure.
```

Randomness should operate within:

```text
PLAUSIBLE CONSTRAINTS.
```

Randomness creates variation.

It does not override causality.

---

# 38. Controlled Randomness

The generator should conceptually use:

```text
CONSTRAINTS
+
WEIGHTED POSSIBILITY
+
RANDOM VARIATION.
```

Not:

```text
PURE RANDOM TABLE.
```

For example:

someone raised in a coastal Norwegian town may plausibly have higher exposure to maritime occupations than someone raised inland.

But no occupation should become deterministic.

---

# 39. Psychological Development Inputs

The Life Generator provides developmental input to the Human Model.

Potential influences include:

```text
family

relationships

success

failure

culture

education

trauma

security

economic conditions

historical events

opportunity

and

agency.
```

It should not directly generate final personality from a simplistic event formula.

---

# 40. Psychological DNA

Psychological DNA should emerge from:

```text
TEMPERAMENT
+
DEVELOPMENTAL HISTORY
+
FORMATIVE EXPERIENCE
+
RELATIONSHIPS
+
ADAPTATION.
```

The generator may establish initial psychological tendencies.

Current psychological state remains part of Character simulation.

---

# 41. Trauma Generation

Trauma must not be used as:

```text
DEFAULT CHARACTER DEPTH.
```

If traumatic events occur:

their consequences should depend on:

```text
age

support network

severity

duration

personality

recovery environment

later experience.
```

Two people may respond very differently.

---

# 42. Resilience

Resilience should not be treated as immunity to hardship.

A resilient person may still experience:

```text
fear

grief

stress

uncertainty

or

temporary dysfunction.
```

Resilience concerns adaptation and recovery.

It may itself develop through life.

---

# 43. Relationships

The Life Generator should establish plausible relationship origins.

Possible relationships include:

```text
family

childhood friends

school friends

partners

spouses

children

colleagues

mentors

rivals

former partners

professional contacts.
```

But current relational state belongs to:

`Canon/Systems/Relationships/`

---

# 44. Relationship Generation Principle

The generator should not create:

```text
FRIEND: RANDOM_PERSON_04
```

without history.

Instead:

```text
met at university
↓
worked on project together
↓
remained friends
↓
moved to different cities
↓
maintained intermittent contact.
```

This creates relational causality.

---

# 45. Social Network Density

Different people have different social network structures.

Possible patterns include:

```text
SMALL / DEEP

LARGE / LOOSE

FAMILY-CENTERED

PROFESSIONAL

COMMUNITY-CENTERED

GEOGRAPHICALLY DISPERSED

ISOLATED

HIGHLY CONNECTED.
```

Network structure should reflect life history.

---

# 46. Family Formation

Adult life may include:

```text
partnership

marriage

children

separation

divorce

chosen family

or

no family formation.
```

The generator must not treat marriage or parenthood as universal life stages.

---

# 47. Relationship Loss

Relationships may end through:

```text
distance

conflict

separation

death

changing priorities

or

historical conditions.
```

Loss becomes part of biography.

It may continue affecting current relationships.

---

# 48. Health

Health history may include:

```text
ordinary illness

chronic conditions

injury

disability

recovery

mental health

aging

healthcare access.
```

Health events should remain plausible relative to:

```text
age

environment

technology

healthcare

and

history.
```

---

# 49. Aging

Life generation must account for aging.

A person's current state should reflect:

```text
AGE

LIFE STAGE

HEALTH

EXPERIENCE

CAREER POSITION

FAMILY POSITION

AND

GENERATION.
```

Older does not automatically mean less capable.

Age changes capability profiles.

---

# 50. Generational Identity

Age and historical exposure create generational differences.

Examples:

```text
CONNECTED WORLD GENERATION

TRANSITION GENERATION

FRACTURED WORLD GENERATION

RECONNECTION GENERATION.
```

These are not personality classes.

They indicate differing developmental environments.

---

# 51. Technology Exposure

The generator should track major technological exposure where relevant.

Examples:

```text
childhood before ubiquitous AI

AI-assisted education

AI-augmented career

high automation dependence

manual fallback training

Transition-era system instability

Fracture-era technological asymmetry.
```

Technology becomes part of biography.

---

# 52. Aurora Exposure

Aurora should only enter a person's life when a plausible path exists.

Possible exposure levels:

```text
NONE

PUBLIC AWARENESS

MEDIA AWARENESS

INDIRECT CONSEQUENCE

PROFESSIONAL EXPOSURE

INSTITUTIONAL EXPOSURE

DIRECT INTERACTION.
```

The Life Generator must not assume:

```text
EVERY IMPORTANT CHARACTER
KNOWS AURORA.
```

---

# 53. Information Exposure

Historical knowledge should depend on information access.

A person may know an event through:

```text
direct experience

family

news

institution

social media

rumor

education

archives

Aurora

or

professional networks.
```

Knowledge should never appear without path.

---

# 54. Current Purpose

Generation should eventually establish one or more plausible current purposes.

Examples:

```text
protect family

maintain profession

solve technical problem

find someone

leave region

remain in community

gain influence

help institution

recover something

learn truth

survive

rebuild.
```

Current Purpose should emerge from:

```text
CURRENT LIFE.
```

Not arbitrary quest generation.

---

# 55. Purpose vs Goal

Purpose is broader than immediate goal.

Example:

```text
PURPOSE:
Keep family safe.

CURRENT GOAL:
Secure fuel for the generator.
```

The Life Generator may initialize broad current purpose.

The Character System owns evolving goals.

---

# 56. Current Situation

The generator must end at:

```text
NOW.
```

Current Situation may include:

```text
location

profession

family status

key relationships

resources

obligations

current problems

current opportunities

institutional affiliations

current health

current purpose.
```

This becomes Character initialization context.

---

# 57. Character Initialization

Generation ends by producing enough coherent state to initialize a living Character.

Conceptually:

```text
LIFE HISTORY
↓
CURRENT CONTEXT
↓
CHARACTER INITIALIZATION
↓
AUTONOMOUS SIMULATION.
```

Once initialized:

future decisions are not predetermined by Life Generator.

---

# 58. No Predetermined Future

The Life Generator must not generate:

```text
THE CHARACTER WILL
BETRAY THE PLAYERS
IN THREE MONTHS.
```

It may generate:

```text
history

values

relationships

obligations

current goals

and

conditions
```

that could make betrayal plausible.

Future action must emerge from simulation.

---

# 59. Player Characters

Player characters use the same life architecture.

However, generation authority differs.

Players may specify:

```text
origin

family

profession

important history

values

relationships

or

major Life Events.
```

The generator fills plausible connective tissue.

---

# 60. Player History Validation

Player-created history must remain compatible with:

```text
CANON

TIMELINE

GEOGRAPHY

AGE

WORLD STATES

EDUCATION

EXPERTISE

AND

EXISTING WORLD TRUTH.
```

The goal is not to restrict creativity unnecessarily.

It is to preserve world coherence.

---

# 61. Player Interpretation Authority

Where possible:

```text
SYSTEM
OWNS
WHAT HAPPENED.
```

The player may retain authority over:

```text
HOW THEIR CHARACTER
INTERPRETED IT.
```

This preserves meaningful character ownership.

---

# 62. NPC Generation

NPCs use the same underlying life-generation principles.

An NPC should never be generated solely as:

```text
MERCHANT

DOCTOR

ENEMY

TECHNICIAN

QUEST GIVER

OR

INFORMANT.
```

These are roles.

Not identities.

---

# 63. Role-Driven NPC Request

Sometimes another system may request:

```text
NEED:
A qualified physician
within this settlement.
```

The Life Generator should not simply fabricate one.

It should first determine:

```text
COULD SUCH A PERSON
PLAUSIBLY EXIST HERE?
```

If yes:

generate a plausible life.

If no:

the answer may be:

```text
NO SUITABLE PERSON EXISTS.
```

This is important.

---

# 64. World-Constrained Population

Life Generation must respect population context.

A settlement of 300 people should not conveniently contain:

```text
three neurosurgeons

two nuclear physicists

an elite cryptographer

and

a world-class AI researcher
```

unless historical conditions explain why.

Population composition matters.

---

# 65. Scarcity of Expertise

Rare expertise should remain rare.

The Life Generator must understand that:

```text
NEED
DOES NOT CREATE
AVAILABLE EXPERTISE.
```

This allows scarcity to become gameplay.

---

# 66. Existing-Person-First Principle

When the campaign needs someone with a particular property:

prefer:

```text
SEARCH EXISTING POPULATION
```

before:

```text
GENERATE NEW PERSON.
```

This preserves world continuity.

---

# 67. Generation Trigger

New people should be generated when:

```text
world population requires them

simulation resolution increases

a region becomes active

a pre-existing low-resolution population
needs individualization

or

Canon requires a specific individual.
```

Narrative convenience alone should not automatically trigger creation.

---

# 68. Population Resolution

At low simulation resolution:

```text
REGION
may contain demographic populations
without individually generated lives.
```

As resolution increases:

```text
POPULATION
↓
HOUSEHOLDS
↓
INDIVIDUALS
↓
DETAILED LIVES.
```

This supports scalable simulation.

---

# 69. Late Instantiation

A person may exist in low-resolution World Truth before receiving detailed biography.

Example:

```text
Settlement has:

41 healthcare workers.
```

Later:

one becomes campaign relevant.

The generator may instantiate:

```text
Name

Age

Profession

Family

History

Relationships

Expertise

Current purpose.
```

New detail must remain consistent with the previously established population.

---

# 70. Resolution Levels

Suggested Life Generation resolution:

```text
LEVEL 0 — POPULATION EXISTENCE

No individual biography required.

LEVEL 1 — BASIC PERSON

Age, role, location, basic family context.

LEVEL 2 — COHERENT LIFE

Education, work, relationships, major history.

LEVEL 3 — DETAILED LIFE

Formative events, Historical DNA, social network,
expertise origins.

LEVEL 4 — HIGH-RESOLUTION LIFE

Detailed relational and developmental continuity.

LEVEL 5 — CRITICAL CONTINUITY

Full historical consistency for major long-term actors.
```

---

# 71. Resolution Expansion

When expanding an existing person:

```text
ESTABLISHED FACTS
=
LOCKED CONSTRAINTS.
```

New detail may explain.

It may not casually contradict.

---

# 72. Example Resolution Expansion

Existing:

```text
Name: Maria Alvarez
Age: 52
Profession: Civil Engineer
Location: Oakland
```

Expansion may add:

```text
Born in San Jose.

Parents immigrated before her birth.

Studied structural engineering.

Worked on Bay Area transport infrastructure.

Experienced Transition-era infrastructure automation.

Moved to Oakland after marriage.

Lost spouse during a regional accident.

Now works on bridge resilience.
```

But expansion may not suddenly establish:

```text
Age 37

Born in Seattle

Profession:
Trauma Surgeon.
```

---

# 73. Contradiction Resolution

If generated history conflicts with established Canon:

```text
ESTABLISHED CANON WINS.
```

The generator should attempt:

```text
REGENERATE

RECONCILE

OR

FLAG CONFLICT.
```

It should never silently rewrite Canon.

---

# 74. Hard Constraints

Hard constraints cannot be violated.

Examples:

```text
birth date

known parentage

established historical events

known profession

known location at a specific time

established relationships

Canon-locked expertise

death date.
```

---

# 75. Soft Constraints

Soft constraints may guide rather than dictate generation.

Examples:

```text
likely education

regional profession distribution

cultural background

economic opportunity

probable language exposure.
```

Soft constraints support plausibility.

They should not create stereotypes.

---

# 76. Consistency Pass

Every generated life should undergo a consistency pass.

Questions include:

```text
DOES THE TIMELINE WORK?

DOES THE GEOGRAPHY WORK?

DOES THE EDUCATION SUPPORT THE PROFESSION?

DOES THE EXPERIENCE SUPPORT THE EXPERTISE?

DO THE RELATIONSHIPS HAVE PLAUSIBLE ORIGINS?

DO THE CHILDREN'S AGES WORK?

DO THE HISTORICAL EVENTS MATCH THE PERSON'S LOCATION?

DOES THE WORLD-STATE EXPOSURE MAKE SENSE?

ARE CURRENT CONDITIONS CONSISTENT WITH THE PAST?
```

---

# 77. Plausibility Pass

Consistency is not enough.

A life may be technically possible but extremely unlikely.

Therefore a second pass should ask:

```text
IS THIS LIFE
PLAUSIBLE ENOUGH
FOR THIS PERSON
AND THIS WORLD?
```

Rare combinations are allowed.

They should remain rare.

---

# 78. Narrative Convenience Check

A final generation check should ask:

> **Does this person exist because the world plausibly produced them, or because the current scene conveniently needs them?**

If the latter:

generation should be reconsidered.

---

# 79. Diversity Through Causality

Variation should emerge naturally through:

```text
geography

family

culture

education

economics

history

personal choice

relationships

chance

and

opportunity.
```

Diversity should not require arbitrary personality randomization.

---

# 80. Internal Contradiction

Real humans contain contradictions.

Internal consistency does not mean:

```text
EVERY CHARACTER TRAIT
POINTS IN THE SAME DIRECTION.
```

A believable person may:

```text
value honesty
and still lie under pressure.

love technology
and fear AI dependency.

trust institutions
and distrust one agency.

be courageous professionally
and avoid personal conflict.
```

These are human contradictions.

Not generation errors.

---

# 81. Generated Imperfection

The Life Generator should allow:

```text
bad decisions

unfinished education

failed careers

broken relationships

missed opportunities

unfulfilled ambitions

regret

inconsistent choices.
```

Lives should not be optimized.

---

# 82. Life Templates

Future Life Templates may provide broad structures.

Examples:

```text
stable professional life

high-mobility childhood

military career

academic career

disrupted education

family-centered life

migration history

fracture displacement.
```

Templates should provide scaffolding.

They must not become fixed biographies.

---

# 83. Template Variation

A template should always allow substantial variation in:

```text
culture

family

relationships

success

failure

belief

personality

events

and

outcome.
```

Templates accelerate generation.

They must not create archetype clones.

---

# 84. Family Generation

Future Family Generation may create:

```text
household structure

parent occupations

siblings

family economic history

migration history

family relationships

intergenerational history.
```

Family generation should integrate with:

```text
Life

Relationships

and

Society.
```

---

# 85. Occupation Generation

Future Occupation Generation should consider:

```text
education

region

economy

age

historical period

technology

family

opportunity

previous employment.
```

Occupation should remain historically grounded.

---

# 86. Education Paths

Education generation may include:

```text
formal schooling

higher education

vocational training

military training

professional certification

apprenticeship

self-teaching

AI-assisted learning

interrupted education.
```

Educational paths should evolve across World States.

---

# 87. Transition-Era Generation

Characters who lived substantially through State 02 should reflect possible exposure to:

```text
AI acceleration

work transformation

education transformation

synthetic information

governance changes

AI fatigue

automation

Human Capability Atrophy

Human Operational Reserve

and

Managed Normality.
```

But these influences should vary.

Not everyone experienced them equally.

---

# 88. Fractured-World Generation

State 03 generation must be heavily geography-dependent.

Possible lives may emerge in:

```text
Stable Zones

Strained Zones

Degraded Zones

Contested Zones

Disconnected Zones.
```

Two people born the same year may therefore have radically different lives.

---

# 89. Mature Fracture Generation

If a region reaches Mature Fracture:

generation may incorporate:

```text
local governance

local economies

restricted travel

regional powers

limited healthcare

regional culture

informal education

community defense

local communications

or

limited national contact.
```

These conditions must not be applied universally to State 03.

---

# 90. Reconnection-Era Generation

State 04 may generate lives shaped by:

```text
regional reconnection

technological asymmetry

layered trust

federated infrastructure

cultural rediscovery

long-distance travel returning

new institutions

and

generational conflict over dependency.
```

Again:

regional variation remains central.

---

# 91. Life Generator and Relationships

The Life Generator creates plausible:

```text
RELATIONSHIP ORIGINS.
```

The Relationship Engine owns:

```text
RELATIONAL CONTINUITY.
```

Example:

```text
Life Generator:

A and B met during engineering school
and worked together for five years.
```

Relationship Engine:

```text
Determines what that shared history
currently means between them.
```

---

# 92. Life Generator and Society

Society provides:

```text
institutions

cultural norms

economic structures

education systems

social expectations

collective conditions.
```

The Life Generator converts them into:

```text
PERSONAL EXPOSURE.
```

---

# 93. Life Generator and World Simulation

World Simulation provides dynamic external conditions.

Life Generator uses relevant historical conditions when creating or expanding biographies.

It must not invent world conditions independently.

---

# 94. Life Generator and Timeline

Timeline defines:

```text
WHAT HAPPENED.
```

Life Generator determines:

```text
WHICH EVENTS
THIS PERSON EXPERIENCED.
```

---

# 95. Life Generator and Human Model

Human Model defines:

```text
WHAT A HUMAN
CONSISTS OF
SYSTEMICALLY.
```

Life Generator creates the developmental history needed to initialize those components coherently.

---

# 96. Life Generator and Character Generation Framework

`Character_Generation_Framework.md` defines broader character-creation principles.

The Life Generator provides the historical generation layer.

They should remain complementary.

If substantial duplication develops:

the architecture should be reviewed rather than maintained in parallel.

---

# 97. Life Generator and Progression

Initial expertise and capability must have historical origins.

After active simulation begins:

Progression handles future development where appropriate.

Therefore:

```text
LIFE GENERATOR
=
HOW DID THEY GET HERE?
```

```text
PROGRESSION
=
HOW DO THEY DEVELOP FROM HERE?
```

---

# 98. Life Generator and Living Campaign Engine

The Living Campaign Engine may request:

```text
a plausible existing person
meeting certain relevance conditions.
```

The preferred flow is:

```text
SEARCH EXISTING WORLD
↓
FOUND?
↓
USE EXISTING PERSON.
```

If not:

```text
VERIFY PERSON
COULD PLAUSIBLY EXIST
↓
GENERATE
↓
ADD TO WORLD
↓
CAMPAIGN MAY DISCOVER THEM.
```

---

# 99. Life Generator and Narrative

Narrative may reveal biography.

Narrative should not dictate biography retroactively merely to create a twist.

The correct direction is:

```text
LIFE TRUTH
↓
DISCOVERY
↓
NARRATIVE PRESENTATION.
```

---

# 100. AI and the Life Generator

AI may assist with generation.

But:

```text
AI
≠
LIFE GENERATOR.
```

The Life Generator is the architectural framework.

AI is one possible reasoning implementation.

This separation protects Project Ascension from dependence on one model or provider.

---

# 101. Explainability

A generated life should be explainable.

The system should eventually be able to answer:

```text
WHY DOES THIS PERSON
HAVE THIS PROFESSION?

WHY ARE THEY HERE?

HOW DID THEY MEET
THESE PEOPLE?

HOW DID THEY ACQUIRE
THIS EXPERTISE?

WHICH HISTORICAL EVENTS
AFFECTED THEM?

WHAT DID THEY NOT EXPERIENCE?

WHY DO THEY HAVE
THESE CURRENT OBLIGATIONS?
```

If the generator cannot explain its major outputs:

the generation is too opaque.

---

# 102. Generation Record

A future implementation may conceptually preserve:

```text
LifeGenerationRecord

generation_id
person_id
generation_mode
hard_constraints
soft_constraints
random_seed
canonical_inputs
world_state_exposure
regional_history
family_history
education_history
professional_history
life_events
relationship_origins
expertise_origins
current_context
validation_results
unresolved_questions
```

This is conceptual architecture.

It is not a locked technical schema.

---

# 103. Reproducibility

Where technically useful, generation may preserve enough state to explain or reproduce outcomes.

This may include:

```text
generation context

constraints

random seed

major decisions

validation results.
```

The purpose is:

```text
DEBUGGABILITY

CONSISTENCY

AND

CANON TRACEABILITY.
```

---

# 104. Generated vs Established Truth

Once a generated fact is accepted into active World Truth:

it is no longer merely:

```text
GENERATED POSSIBILITY.
```

It becomes:

```text
ESTABLISHED HISTORY.
```

Future generation must respect it.

---

# 105. Life Generation Lifecycle

Conceptually:

```text
REQUEST
↓
CONTEXT COLLECTION
↓
CONSTRAINT RESOLUTION
↓
HISTORICAL FRAME
↓
FAMILY / CULTURE
↓
EDUCATION
↓
RELATIONSHIPS
↓
PROFESSIONAL DEVELOPMENT
↓
LIFE EVENTS
↓
HISTORICAL EXPOSURE
↓
CURRENT SITUATION
↓
CONSISTENCY PASS
↓
PLAUSIBILITY PASS
↓
CHARACTER INITIALIZATION
↓
CANONICAL REGISTRATION
↓
ACTIVE SIMULATION.
```

---

# 106. Generation Failure

The generator must be allowed to fail.

Example:

```text
REQUEST:

Generate a world-class pediatric
neurosurgeon currently living in
a settlement of 140 isolated people.
```

The correct output may be:

```text
NO PLAUSIBLE MATCH.
```

The system should not bend the world merely to satisfy the request.

This is a feature.

---

# 107. Partial Generation

Sometimes only partial generation is required.

Example:

```text
Need:

name
age
basic profession
family status.
```

The system should not automatically generate a 5,000-word biography.

Resolution should match need.

---

# 108. Deferred Detail

Unknown biography may remain:

```text
UNRESOLVED
```

rather than be prematurely invented.

Later resolution can fill gaps while respecting established constraints.

This is preferable to over-generation.

---

# 109. Canonical Invariants

## LIFE-GEN-INV-001 — Lives Are Causal

Generated biographies must contain plausible developmental relationships.

## LIFE-GEN-INV-002 — Canon Has Priority

Generated detail may not override established Canon.

## LIFE-GEN-INV-003 — Chronology Must Hold

Life history must respect time.

## LIFE-GEN-INV-004 — Geography Must Hold

Location must affect possibility and exposure.

## LIFE-GEN-INV-005 — Expertise Requires History

Significant capability requires plausible development.

## LIFE-GEN-INV-006 — Relationships Require Origins

Persistent social connections require plausible contact history.

## LIFE-GEN-INV-007 — Historical Knowledge Requires Exposure

Characters do not automatically know global events.

## LIFE-GEN-INV-008 — World State Is Context, Not Personality

Historical era does not dictate character traits.

## LIFE-GEN-INV-009 — Culture Is Context, Not Personality

Cultural background does not produce deterministic behavior.

## LIFE-GEN-INV-010 — Trauma Is Not Required

Character depth must not depend on suffering.

## LIFE-GEN-INV-011 — Ordinary Life Exists

Generated lives must contain realistic non-dramatic periods.

## LIFE-GEN-INV-012 — Positive Experience Matters

Love, achievement, friendship and belonging are legitimate formative experiences.

## LIFE-GEN-INV-013 — Randomness Is Constrained

Chance must operate inside plausible conditions.

## LIFE-GEN-INV-014 — Need Does Not Create Availability

Campaign requirements do not guarantee an appropriate person exists.

## LIFE-GEN-INV-015 — Existing People Come First

Search the established population before generating new individuals.

## LIFE-GEN-INV-016 — Resolution Expansion Preserves History

New detail may not casually rewrite established facts.

## LIFE-GEN-INV-017 — Generation Ends At The Present

Future autonomous decisions belong to Character simulation.

## LIFE-GEN-INV-018 — NPCs and Players Share Human Logic

They use the same conceptual life framework.

## LIFE-GEN-INV-019 — Aurora Exposure Requires Path

Important characters do not automatically know or interact with Aurora.

## LIFE-GEN-INV-020 — Every Major Output Should Be Explainable

Generation must preserve causal traceability.

---

# 110. Development Locks

Do not generate people backward from quest function.

Do not generate experts merely because the campaign needs them.

Do not ignore population plausibility.

Do not ignore chronology.

Do not ignore geography.

Do not ignore World State exposure.

Do not give characters historical memories from before their birth.

Do not give characters expertise without development.

Do not make every important character exceptional.

Do not make every character's childhood dramatic.

Do not use trauma as automatic depth.

Do not optimize every biography.

Do not treat culture as personality.

Do not treat profession as personality.

Do not treat generation templates as final lives.

Do not over-generate low-resolution characters.

Do not resolve unknown history unnecessarily.

Do not generate private relationships without plausible origins.

Do not give characters automatic knowledge of Aurora.

Do not give characters automatic knowledge of world events.

Do not allow randomization to violate Canon.

Do not allow Narrative to retroactively demand convenient biography.

Do not allow Campaign needs to override world plausibility.

Do not allow resolution expansion to rewrite established history.

Do not pre-script future betrayal, death, loyalty or success.

Do not turn the Life Generator into the Character System.

Do not turn the Life Generator into the Relationship Engine.

Do not turn the Life Generator into the World Simulation.

---

# 111. Development Status

The Life Generator is now:

```text
ARCHITECTURALLY DEFINED

GENERATION LOGIC DEFINED

CAUSALITY MODEL DEFINED

RESOLUTION MODEL DEFINED

NOT YET IMPLEMENTATION LOCKED

NOT YET NUMERICALLY LOCKED.
```

The next implementation stage should not begin by defining random tables.

It should begin by establishing:

```text
CONSTRAINT REPRESENTATION

TIMELINE VALIDATION

GEOGRAPHIC VALIDATION

LIFE-EVENT REPRESENTATION

EXPERTISE PATH VALIDATION

RELATIONSHIP-ORIGIN VALIDATION

AND

GENERATION CONSISTENCY CHECKING.
```

---

# 112. Recommended Future Documents

Potential future documents include:

```text
Life_Generation_Context.md

Life_Generation_Constraints.md

Life_Event_System.md

Historical_DNA_Framework.md

Family_Generation.md

Education_and_Career_Generation.md

Expertise_Origin_Model.md

Geographic_Life_History.md

World_State_Exposure_Model.md

Life_Generation_Resolution.md

Life_Consistency_Validator.md

Life_Generator_Test_Scenarios.md
```

These are architectural candidates.

They should not automatically be created.

Existing Canon must first be checked for overlap.

---

# 113. Validation Scenarios

Future Life Generator validation should include:

```text
ordinary Connected World adult

Transition-era AI professional

Fractured World child

elderly person spanning multiple World States

high-expertise specialist

low-opportunity high-potential individual

migrant family

isolated rural resident

urban professional

person with interrupted education

person changing careers after automation

player-created constrained biography

late-instantiated NPC

rare-expertise population check

contradictory input rejection.
```

---

# 114. Critical Validation — Expertise

Request:

```text
Generate:
45-year-old experienced trauma surgeon.
```

Expected history should plausibly include:

```text
appropriate education

medical training

residency

years of practice

clinical exposure

and

relevant institutional access.
```

The generator must reject histories where the expertise cannot plausibly exist.

---

# 115. Critical Validation — Historical Exposure

Person:

```text
Born 2028.

Raised in California.
```

Historical event:

```text
Occurred 2024.
```

Expected:

```text
NO PERSONAL MEMORY.
```

Family history may contain the event.

The character may later learn about it.

But personal exposure cannot be generated.

---

# 116. Critical Validation — Geography

Person:

```text
Lives in disconnected rural region.
```

Generation proposes:

```text
daily employment
at distant metropolitan institution
without transport or communication path.
```

Expected:

```text
REJECT OR RECONCILE.
```

Geography must remain causal.

---

# 117. Critical Validation — Campaign Convenience

Campaign asks for:

```text
expert who knows exactly
how to solve current problem.
```

Population search finds no plausible candidate.

Expected:

```text
NO CONVENIENT EXPERT
IS GENERATED AUTOMATICALLY.
```

Possible consequences:

```text
travel required

partial expert available

remote knowledge sought

players improvise

problem remains unsolved.
```

This protects emergent gameplay.

---

# 118. Life Generator North Star

> **The Life Generator should not ask what character would make the story interesting. It should ask what life could plausibly have produced this person.**

---

# 119. Causality North Star

> **Every extraordinary person should have an ordinary chain of causes connecting them to the world.**

---

# 120. Human North Star

> **People should contain enough history that their present feels inherited rather than invented.**

---

# 121. World North Star

> **The world should produce people appropriate to itself, not people appropriate to the player's immediate needs.**

---

# 122. Resolution North Star

> **Generate only as much detail as the world currently needs, but never generate detail that contradicts what the world already knows.**

---

# 123. Player North Star

> **Players may help define who their characters were. The simulation determines what that history makes possible, not what it forces them to become.**

---

# 124. Final Generation Model

```text
CANON
+
HISTORY
+
WORLD STATE
+
GEOGRAPHY
+
SOCIETY
+
FAMILY
+
CULTURE
+
OPPORTUNITY
+
EDUCATION
+
RELATIONSHIPS
+
LIFE EVENTS
+
CHOICES
+
CHANCE
+
TIME
=
LIFE HISTORY
```

Then:

```text
LIFE HISTORY
+
CURRENT WORLD
+
CURRENT RELATIONSHIPS
+
CURRENT PURPOSE
=
CHARACTER INITIALIZATION.
```

And from that moment:

```text
GENERATION ENDS.

LIFE CONTINUES.
```

The Character System takes over.

The Relationships System continues changing connections.

World Simulation changes conditions.

Society changes institutions.

Aurora observes and acts.

The player intervenes.

New Life Events occur.

The person's biography continues being written by:

```text
SIMULATION.
```

---

# 125. Closing Statement

The Life Generator exists because nobody should appear in Project Ascension as though they were created five seconds before the player opened the door.

The doctor had patients before the player arrived.

The technician had a childhood.

The soldier had teachers.

The mayor has old friends.

The criminal has a family.

The stranger on the road was going somewhere.

The person who helps the player may have people depending on them.

The person who refuses may have good reasons.

The person who appears insignificant may have lived through events the player has spent weeks trying to understand.

Every person should carry evidence of:

```text
TIME.
```

Because Project Ascension is not populated by characters waiting for a story.

It is populated by:

**lives already in progress.**

> **Lives are generated. Stories emerge.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-08 | Initial Life Generator architecture established. |
| 2.0 | 2026-08-29 | Expanded the Life Generator into the operational generation model for human life histories. Added constraint-first generation, generation modes, chronological and geographic validation, World State and historical exposure, family, education, profession, expertise development, Life Events, relationships, current purpose, NPC/player parity, population-aware generation, late instantiation, resolution management, consistency and plausibility passes, generation failure, AI separation, canonical invariants, development locks and validation scenarios. Clarified that generation produces the causal history leading to Character initialization while future behavior remains emergent simulation. |