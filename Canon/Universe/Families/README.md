# PROJECT ASCENSION

# Families

| Field | Value |
|---|---|
| Project | Project Ascension |
| Document | Families |
| Location | `Canon/Universe/Families/README.md` |
| Version | 1.0 |
| Status | Canonical Universe Structure |
| Category | Universe / Families |
| Owner | Universe |
| Last Updated | 2026-09-01 |
| Primary Function | Define how specific canonical families are represented, organized and maintained across generations within the Project Ascension universe |

---

# 1. Purpose

The Families directory contains the specific families that exist within the canonical Project Ascension universe.

It answers:

> **Which families exist in the world, who belongs to them, what history connects them and how do their consequences persist across generations?**

This directory does not define what Family means as a human concept.

That responsibility belongs to:

```text
Canon/Universe/Humanity/Family.md
```

Instead:

```text
HUMANITY / FAMILY

defines

WHAT FAMILY MEANS.


UNIVERSE / FAMILIES

records

THE ACTUAL FAMILIES
THAT EXIST.
```

---

# 2. Core Principle

The central Families principle is:

> **Families preserve human continuity across generations without determining the people who belong to them.**

A family may carry:

- history
- names
- stories
- reputation
- responsibilities
- property
- resources
- institutional connections
- unresolved obligations
- consequences
- cultural practices
- geographic roots
- relationships between generations

But none of these automatically determine:

- personality
- belief
- morality
- loyalty
- trust
- goals
- psychology
- future choices

Therefore:

```text
FAMILY HISTORY

INFLUENCES

BUT DOES NOT

DETERMINE

THE NEXT GENERATION.
```

---

# 3. Architectural Position

Project Ascension separates system architecture from canonical world instances.

```text
Canon/Systems/

defines

HOW THE WORLD WORKS.


Canon/Universe/

defines

WHAT EXISTS IN THE WORLD.
```

Families are canonical world structures.

Therefore specific families belong under:

```text
Canon/Universe/Families/
```

Examples:

```text
Canon/Universe/Families/Mitchell/
Canon/Universe/Families/Carter/
Canon/Universe/Families/Alvarez/
```

These are not new simulation systems.

They are canonical instances existing within the simulated world.

---

# 4. Family Concept vs Canonical Family

The distinction between the Family concept and an actual family must remain explicit.

```text
Canon/Universe/Humanity/Family.md
```

defines:

```text
FAMILY
AS A HUMAN
SOCIAL AND HISTORICAL
CONTEXT.
```

While:

```text
Canon/Universe/Families/Mitchell/
```

defines:

```text
THE MITCHELL FAMILY
AS A SPECIFIC
CANONICAL FAMILY
IN THE WORLD.
```

Conceptually:

```text
FAMILY ARCHITECTURE
        ↓
provides rules and boundaries
        ↓
CANONICAL FAMILY
        ↓
exists within World Truth
        ↓
INDIVIDUAL PEOPLE
        ↓
experience that family differently
```

---

# 5. Standard Family Directory

Every sufficiently significant persistent family should use the following structure:

```text
Family_Name/
├── README.md
├── Family_Name_Family.md
└── Family_Name_Family_Chronicle.md
```

Example:

```text
Mitchell/
├── README.md
├── Mitchell_Family.md
└── Mitchell_Family_Chronicle.md
```

Additional files should only be introduced when the existing structure cannot represent the required information clearly.

Avoid creating unnecessary family subsystems or document categories.

---

# 6. Family README

Each family directory contains a local:

```text
README.md
```

Its primary purpose is navigation and orientation.

The README should identify:

- family name
- geographic origin
- important generations
- active family branches
- high-resolution Characters
- important historical members
- important Locations
- important Events
- connected families
- Family document
- Family Chronicle

The README should not become a duplicate Family document.

---

# 7. Family Document

The primary family document follows the naming convention:

```text
Family_Name_Family.md
```

Example:

```text
Mitchell_Family.md
```

It represents the canonical family context.

A Family document may contain:

- Family Identity
- Origin
- Geographic Roots
- Generations
- Known Members
- Historical Members
- Kinship
- Family Roles
- Households
- Dependents
- Caregiving Responsibilities
- Geographic Distribution
- Shared History
- Family Narratives
- Known Family Stories
- Important Family Events
- Intergenerational Consequences
- Family Reputation
- Property of Family Significance
- Resources of Family Significance
- Institutional Connections
- External Connections
- Connected Families
- Current Family State

The Family document describes the family.

It does not replace the Characters within it.

---

# 8. Family Chronicle

Every significant persistent family may maintain a:

```text
Family_Name_Family_Chronicle.md
```

Example:

```text
Mitchell_Family_Chronicle.md
```

The Chronicle records the historical spine of the family.

Conceptually:

```text
PAST GENERATIONS
        ↓
FAMILY EVENTS
        ↓
CURRENT GENERATION
        ↓
NEW EVENTS
        ↓
CONSEQUENCES
        ↓
FUTURE GENERATIONS
```

The Chronicle allows family history to remain causally traceable across long periods of time.

---

# 9. Chronicle Purpose

The Chronicle should answer:

```text
WHAT HAPPENED?

WHEN DID IT HAPPEN?

WHO WAS INVOLVED?

WHAT FAMILY CONSEQUENCES FOLLOWED?

WHAT LATER EVENTS CONNECT TO IT?
```

Example:

```text
1989
Sarah Mitchell is born.

1992
Michael Mitchell is born.

2034
A major event involving Sarah creates
long-term consequences for the family.

2058
Sarah Mitchell dies.

2067
A later Mitchell descendant encounters
a descendant of another historically
connected family.
```

The Chronicle is not a complete biography of every family member.

---

# 10. Chronicle Is Not Memory

A Chronicle must not be treated as the Memory of the family.

There is no collective Family Memory.

Instead:

```text
EVENT
        ↓
WORLD TRUTH

        ↓

INDIVIDUAL EXPERIENCE

        ↓

PERSONAL MEMORY

        ↓

RETELLING

        ↓

FAMILY STORY

        ↓

LATER GENERATION
```

A later generation may know a story about an event.

That does not mean they possess the Memory of the person who experienced it.

---

# 11. Chronicle and World Truth

Where possible, the Chronicle should describe events according to established canonical history.

However:

```text
FAMILY CHRONICLE
≠
COMPLETE WORLD TRUTH.
```

The Chronicle records family-relevant historical facts.

World Truth may contain additional information unknown to the family.

Example:

```text
WORLD TRUTH

Sarah left Facility X because
remaining would have caused
greater loss of life.

        ↓

MITCHELL FAMILY STORY

Sarah made an impossible decision
and saved those she could.

        ↓

OTHER FAMILY STORY

Sarah Mitchell abandoned
the people inside.
```

All three may coexist within the architecture.

Only the first represents objective World Truth.

---

# 12. Characters Remain Independent

Individual Characters are not owned by their Family.

A Character may participate in multiple family contexts during one lifetime.

Example:

```text
MITCHELL FAMILY
        │
        ↓
SARAH MITCHELL
        │
        ├──── PARTNER
        │        │
        │        ↓
        │   ANOTHER FAMILY
        │
        ↓
     CHILDREN
```

Therefore:

```text
FAMILY

DOES NOT OWN

CHARACTER.
```

High-resolution Characters receive independent Character files under:

```text
Canon/Universe/Characters/People/
```

---

# 13. Character Organization

Individual human Characters may be organized for repository navigation by family association.

Example:

```text
Canon/Universe/Characters/People/Mitchell/
├── Sarah_Mitchell.md
├── Michael_Mitchell.md
└── Ethan_Mitchell.md
```

This directory structure is organizational.

It does not imply that the Family owns the Character's state or agency.

---

# 14. Character Resolution

Not every person mentioned in a Family requires a full Character file.

Representation should follow simulation relevance.

Conceptually:

```text
LOW RESOLUTION
=
historical or structural family reference

MEDIUM RESOLUTION
=
persistent individual context
without full Character representation

HIGH RESOLUTION
=
full individual Character representation
```

A person may move between these resolutions as relevance changes.

---

# 15. Character Promotion

A Family member may initially exist only as family context.

Example:

```text
MICHAEL MITCHELL

MEDIUM RESOLUTION
        ↓
becomes directly relevant
        ↓
PROMOTION
        ↓
HIGH RESOLUTION
        ↓
Michael_Mitchell.md
```

Promotion does not create a new person.

It increases the resolution at which an already existing person is represented.

Existing history must remain intact.

---

# 16. Family Roles Are Not Character State

A Family document may record:

```text
Sarah Mitchell
=
daughter of Thomas and Linda

Michael Mitchell
=
Sarah's brother
```

But it should not use those roles to infer:

```text
trust

love

resentment

loyalty

obedience

belief

psychology.
```

Those states belong to their authoritative systems and Characters.

---

# 17. Relationship Boundary

Family defines relational context.

Relationships define persistent interpersonal state.

Example:

```text
FAMILY

Sarah and Michael
are siblings.


RELATIONSHIPS

Sarah trusts Michael
with practical problems.

Michael resents
a past decision Sarah made.

Sarah feels responsible
for Michael.

Michael refuses
Sarah's help.
```

The Family document may reference important Relationships.

It must not replace the Relationship architecture.

---

# 18. Life Boundary

Family events may become significant Life Events.

Example:

```text
FAMILY CONTEXT

Sarah is Thomas's daughter.

        ↓

EVENT

Thomas dies.

        ↓

LIFE EVENT

Sarah loses her father.

        ↓

MEMORY

Sarah remembers their
last conversation.

        ↓

PSYCHOLOGY

The loss affects her
current emotional state.

        ↓

GOALS / RELATIONSHIPS / CHOICES

possible consequences emerge.
```

No single Family document owns the complete causal chain.

---

# 19. Generations

Canonical families may span multiple generations.

Conceptually:

```text
GENERATION -2
        ↓
GENERATION -1
        ↓
GENERATION 0
        ↓
GENERATION 1
        ↓
GENERATION 2
        ↓
GENERATION 3
        ↓
...
```

Generation numbering is contextual and should only be used when useful.

It must not imply importance or hierarchy.

---

# 20. Intergenerational Consequence

Actions by one generation may create conditions experienced by later generations.

Possible transmitted consequences include:

- property
- debt
- responsibility
- reputation
- social connections
- institutional connections
- geographic roots
- migration history
- unresolved conflict
- family stories
- knowledge
- objects
- cultural practices
- promises
- obligations
- consequences of previous decisions

This is:

```text
CAUSAL INHERITANCE
```

not:

```text
PSYCHOLOGICAL INHERITANCE.
```

---

# 21. No Inherited Personality

Avoid:

```text
THE PARENT
WAS DISTRUSTFUL

THEREFORE

THE CHILD
IS DISTRUSTFUL.
```

Prefer:

```text
THE PARENT'S
DECISIONS

        ↓

CHANGED FAMILY
CIRCUMSTANCES

        ↓

THE CHILD
EXPERIENCED
THOSE CIRCUMSTANCES

        ↓

THE CHILD
DEVELOPED THROUGH
THEIR OWN LIFE.
```

Family history creates conditions.

Characters remain individuals.

---

# 22. Family Stories

Families may preserve stories across generations.

Example:

```text
EVENT
        ↓
PERSONAL MEMORY
        ↓
RETELLING
        ↓
FAMILY STORY
        ↓
NEXT GENERATION
        ↓
NEW INTERPRETATION
```

Stories may:

- remain accurate
- lose detail
- gain detail
- become simplified
- become symbolic
- become disputed
- become misunderstood
- become mythologized
- disappear
- later be rediscovered

A Family Story is not automatically World Truth.

---

# 23. Family Narratives

Families may develop persistent narratives.

Examples:

```text
WE TAKE CARE
OF OUR OWN.
```

```text
THE GOVERNMENT
ABANDONED US.
```

```text
OUR FAMILY
ALWAYS COMES BACK.
```

```text
THE MITCHELLS
DON'T ASK
FOR HELP.
```

Such narratives may influence expectations.

They do not determine individual belief or behavior.

---

# 24. Historical Connection

Families may acquire historical connections with other families.

Example:

```text
MITCHELL
        │
        │
        ├──── EVENT ──── CARTER
        │
        ↓
FAMILY HISTORY
        ↓
GENERATIONS PASS
        ↓
MITCHELL DESCENDANT
        │
        │ meets
        ↓
CARTER DESCENDANT
```

The descendants may never have met before.

But the families may already share history.

---

# 25. Historical Trust Context

Historical family connections may affect the initial context in which two Characters encounter one another.

Example:

```text
SARAH MITCHELL
        ↓
helps
        ↓
DANIEL CARTER
        ↓
CARTER FAMILY STORY
        ↓
decades pass
        ↓
RACHEL CARTER
meets
ETHAN MITCHELL
```

Rachel may recognize the Mitchell name.

This may create:

```text
HISTORICAL CONNECTION
        ↓
PRIOR EXPECTATION
        ↓
ALTERED INITIAL UNCERTAINTY
        ↓
GREATER WILLINGNESS
TO ENGAGE
```

But:

```text
HISTORICAL CONNECTION

≠

PERSONAL TRUST.
```

Ethan must still establish his own Relationship with Rachel.

---

# 26. Negative Historical Connection

The same architecture applies to negative history.

Example:

```text
PAST CONFLICT
        ↓
FAMILY STORY
        ↓
REPUTATION
        ↓
NEXT GENERATION
        ↓
INITIAL SUSPICION
```

The descendant is not guilty of the ancestor's actions.

But the historical connection may still affect how others initially interpret them.

---

# 27. Inherited Consequence Is Not Inherited Guilt

The following distinction is canonical:

```text
A CHARACTER

MAY INHERIT

THE CONSEQUENCES

OF HISTORY


WITHOUT

INHERITING

THE GUILT

FOR THAT HISTORY.
```

Likewise:

```text
A CHARACTER

MAY INHERIT

A POSITIVE REPUTATION


WITHOUT

HAVING EARNED

PERSONAL TRUST.
```

Future interactions determine what happens next.

---

# 28. Family Reputation

A family may develop a reputation.

Examples:

```text
reliable

dangerous

generous

powerful

dishonest

resilient

isolated

connected
```

Family reputation is contextual social information.

Individual Characters do not automatically possess the qualities associated with their family's reputation.

---

# 29. Connected Families

Family documents should reference important connections with other families when such connections become historically significant.

Possible connections include:

- marriage
- friendship
- shared survival
- professional history
- conflict
- betrayal
- rescue
- debt
- caregiving
- property
- institutional connection
- political history
- migration
- shared community
- unresolved responsibility

These connections may survive the original Characters involved.

---

# 30. Cross-Family Continuity

A historical event may connect multiple families.

Conceptually:

```text
EVENT
  │
  ├──────── MITCHELL
  │
  ├──────── CARTER
  │
  └──────── ALVAREZ
```

The same event may later exist as:

```text
MITCHELL FAMILY STORY

CARTER FAMILY STORY

ALVAREZ FAMILY STORY
```

These stories may differ.

The underlying World Truth remains separate.

---

# 31. Family Geography

Families may exist across multiple Locations.

Example:

```text
MITCHELL FAMILY

Western Pennsylvania
        │
        ├── parents
        ├── siblings
        └── historical roots

Northern Virginia
        │
        ├── Sarah
        ├── partner
        ├── children
        └── professional life

Future Region
        │
        └── descendants
```

Geographic separation does not automatically end Family continuity.

---

# 32. Migration and Family Branches

Migration may create new family branches.

Conceptually:

```text
ORIGINAL FAMILY
        │
        ├─────────────┐
        ↓             ↓
REGION A          REGION B
        │             │
        ↓             ↓
BRANCH A          BRANCH B
```

Over generations, these branches may develop:

- different experiences
- different relationships
- different stories
- different social contexts
- different reputations
- different beliefs

while still sharing historical ancestry.

---

# 33. Marriage and Multiple Family Contexts

Marriage or partnership may connect families without erasing either family's previous history.

Example:

```text
MITCHELL
    │
    │
  SARAH
    │
    ├──── PARTNER
    │        │
    │     FAMILY X
    │
    ↓
CHILDREN
```

Children may therefore participate in several family histories simultaneously.

There is no requirement that one family identity replaces another.

---

# 34. Children

Children are not extensions of their parents.

They are developing human Actors.

A Family document may establish:

- parentage
- household
- caregiving
- dependency
- family history
- historical conditions

But future Character development must remain open.

---

# 35. Descendants

Descendants may become important long after the original family members are dead.

They may inherit:

```text
CONTEXT

not

DESTINY.
```

A descendant may:

- preserve family history
- reject it
- misunderstand it
- rediscover it
- challenge it
- reinterpret it
- attempt to repair it
- exploit it
- ignore it

The descendant owns their response.

---

# 36. Death

Death ends the active life of a Character.

It does not necessarily end their historical significance.

Conceptually:

```text
CHARACTER
        ↓
LIFE
        ↓
ACTION
        ↓
CONSEQUENCE
        ↓
DEATH
        ↓
────────────────────
        ↓
MEMORY
FAMILY HISTORY
PROPERTY
RESPONSIBILITY
REPUTATION
RELATIONSHIP CONSEQUENCES
STORIES
DESCENDANTS
UNRESOLVED CONSEQUENCES
        ↓
FUTURE HISTORY
```

---

# 37. Historical Members

Deceased family members may remain represented as Historical Members.

A Historical Member does not remain an active Actor.

Their historical effects may remain relevant through:

- Life Events
- Memory
- family stories
- property
- reputation
- responsibilities
- Relationships among survivors
- institutional consequences
- World Truth

---

# 38. Family Persistence

A Family may continue after:

- death
- migration
- separation
- household dissolution
- political collapse
- infrastructure failure
- communication loss
- social reconstruction

Family persistence does not require all members to remain connected.

---

# 39. Off-Screen Continuity

Families continue to exist when players are absent.

Possible off-screen developments include:

- births
- deaths
- marriages
- partnerships
- separation
- migration
- illness
- caregiving changes
- employment changes
- property changes
- household restructuring
- conflict
- reconciliation
- loss of communication
- discovery of information

Important developments should propagate through the authoritative systems.

---

# 40. Family Resolution

Family representation may use different simulation resolutions.

```text
LOW

preserve:

family structure
major historical members
important events
major dependencies
important historical consequences
```

```text
MEDIUM

add:

significant family changes
movement
responsibility
important relationships
major current circumstances
```

```text
HIGH

model:

active individual Characters
Relationships
Life Events
Memory
Beliefs
Psychology
Goals
Agency
```

Resolution changes representation detail.

It does not change historical reality.

---

# 41. Resolution Promotion

A person may move from Family context into full Character representation.

Conceptually:

```text
HISTORICAL NAME
        ↓
LOW
        ↓
becomes relevant
        ↓
MEDIUM
        ↓
direct interaction
        ↓
HIGH
        ↓
FULL CHARACTER
```

The Character must retain all previously established canonical history.

Promotion must not rewrite the person's past merely to make them more interesting.

---

# 42. Resolution Demotion

A Character may later become less simulation-relevant.

High-resolution representation may be reduced.

But:

```text
LOWER RESOLUTION

DOES NOT MEAN

ERASED HISTORY.
```

Important Character history, Relationships, family connections and consequences must remain recoverable.

---

# 43. Family Creation

When introducing a new canonical family, establish only the amount of history required to make the family plausible.

Avoid constructing enormous genealogies without purpose.

Start with:

```text
ORIGIN

CURRENT RELEVANT GENERATIONS

IMPORTANT HISTORICAL MEMBERS

GEOGRAPHY

HOUSEHOLD

SHARED HISTORY

IMPORTANT FAMILY STORIES

CURRENT RESPONSIBILITIES

CURRENT CONNECTIONS
```

Then allow history to accumulate through simulation and narrative development.

---

# 44. Family Creation Principle

The preferred approach is:

```text
CREATE ENOUGH PAST

TO EXPLAIN

THE PRESENT.


THEN LET

THE FUTURE

EMERGE.
```

Do not pre-write generations of future history that should instead emerge through Character decisions and World Simulation.

---

# 45. Canonical Family Registry

This README acts as the primary registry for canonical families.

Families should be added when they become established Canon.

Initial registry:

| Family | Origin | Primary Regions | Status | Primary Function |
|---|---|---|---|---|
| Mitchell | Western Pennsylvania, USA | Pennsylvania / Northern Virginia | In Development | First canonical multigenerational human family and Character integration case |

Future families should only be added when they become canonical.

Do not create placeholder family directories merely to reserve names.

---

# 46. Character Registry Relationship

The Family Registry and Character Registry serve different purposes.

```text
FAMILY REGISTRY

answers:

WHICH FAMILIES EXIST?


CHARACTER REGISTRY

answers:

WHICH INDIVIDUAL
CHARACTERS EXIST?
```

A Character may appear in references to multiple families.

A Family may reference many Characters.

Neither registry replaces the other.

---

# 47. Naming Convention

Family directories use the family name:

```text
Mitchell/
Carter/
Alvarez/
```

Primary Family files use:

```text
Mitchell_Family.md
Carter_Family.md
Alvarez_Family.md
```

Chronicles use:

```text
Mitchell_Family_Chronicle.md
Carter_Family_Chronicle.md
Alvarez_Family_Chronicle.md
```

Local navigation files remain:

```text
README.md
```

---

# 48. Family Identifier Principle

Human-readable names should remain primary during the current documentation phase.

Do not introduce artificial numeric Family IDs unless implementation or scale proves they are required.

Prefer:

```text
Mitchell
```

over premature structures such as:

```text
FAM-0001
```

The architecture should remain understandable to human authors.

---

# 49. Cross-References

Family documents should reference authoritative Canon rather than duplicating it.

Possible references include:

```text
Characters

Locations

Timeline Events

World States

Factions

Institutions

Relationships

Historical Events

Family Chronicles
```

Cross-references should preserve ownership.

---

# 50. No Duplicate Canon

Avoid maintaining the same canonical fact independently in several places.

Example:

If Sarah's birth date is canonical:

```text
Sarah_Mitchell.md
```

may own the detailed Character representation.

The Family document may reference the birth date.

The Chronicle may record the birth event.

But these references must remain consistent.

When contradictions appear, authoritative ownership must determine which source is corrected.

---

# 51. Family as Historical Interface

Families provide an important interface between:

```text
INDIVIDUAL LIFE

and

LONG-TERM HISTORY.
```

Conceptually:

```text
WORLD HISTORY
        ↓
FAMILY HISTORY
        ↓
INDIVIDUAL LIFE
        ↓
CHARACTER DECISION
        ↓
CONSEQUENCE
        ↓
FAMILY HISTORY
        ↓
NEXT GENERATION
        ↓
WORLD HISTORY
```

This allows civilization-scale events to remain connected to individual human lives.

---

# 52. Family and Project Ascension

Project Ascension may span periods longer than the active lifetime of individual Characters.

Families provide continuity across those periods.

A Character may experience:

```text
THE CONNECTED WORLD
```

their children may experience:

```text
THE TRANSITION
```

their grandchildren may grow up within:

```text
THE FRACTURED WORLD
```

and later descendants may participate in:

```text
RECONNECTION.
```

The family provides historical continuity.

Each generation remains composed of independent people.

---

# 53. Family Historical Depth

Long-term family history should emerge gradually.

A mature family may eventually contain:

```text
GENERATIONS

MIGRATIONS

MARRIAGES

DEATHS

CONFLICTS

RECONCILIATIONS

PROPERTY

LOSSES

PROFESSIONS

FAMILY STORIES

FALSE STORIES

REPUTATIONS

PROMISES

DEBTS

INSTITUTIONAL CONNECTIONS

CROSS-FAMILY HISTORY
```

But none of this needs to exist when the family is first created.

History should accumulate causally.

---

# 54. Family as Human Scale

Large historical events should be capable of entering Family history through ordinary human consequences.

Example:

```text
GEOPOLITICAL CRISIS
        ↓
SUPPLY DISRUPTION
        ↓
EMPLOYMENT LOSS
        ↓
FAMILY FINANCIAL PRESSURE
        ↓
MIGRATION
        ↓
CHILD GROWS UP
IN DIFFERENT REGION
        ↓
NEW RELATIONSHIPS
        ↓
NEW LIFE HISTORY
```

The family does not need to understand the geopolitical cause for its consequences to become historically significant.

---

# 55. Canonical Invariants

## FAMREG-INV-001 — Families Are Canonical World Instances

Specific families belong to the Universe layer.

---

## FAMREG-INV-002 — Family Architecture Remains Separate

`Canon/Universe/Humanity/Family.md` defines the Family concept.

Specific Family directories instantiate it.

---

## FAMREG-INV-003 — Families Do Not Own Characters

Characters remain independent Actors.

---

## FAMREG-INV-004 — Family History Does Not Determine Character Behavior

History creates context and consequences.

Agency remains individual.

---

## FAMREG-INV-005 — Family Chronicle Is Not Memory

Individual Memory remains separate from historical chronology.

---

## FAMREG-INV-006 — Family Story Is Not World Truth

Stories may be incomplete, incorrect or contested.

---

## FAMREG-INV-007 — Intergenerational Consequences Must Be Causal

Later generations may inherit conditions and consequences, not predetermined psychology.

---

## FAMREG-INV-008 — Historical Connection Is Not Personal Trust

Family history may alter initial expectations without creating automatic interpersonal Trust.

---

## FAMREG-INV-009 — Descendants Do Not Inherit Guilt

They may inherit consequences, reputation or historical context.

They remain responsible for their own choices.

---

## FAMREG-INV-010 — Positive Reputation Is Not Earned Personal Trust

A Character may benefit from family reputation without personally having earned it.

---

## FAMREG-INV-011 — Characters May Participate in Multiple Families

Marriage, partnership, adoption, chosen family and other structures may create overlapping family contexts.

---

## FAMREG-INV-012 — Death Does Not Erase Family History

Historical consequences may persist after a Character dies.

---

## FAMREG-INV-013 — Families Continue Off-Screen

Family-relevant history may develop outside player observation.

---

## FAMREG-INV-014 — Resolution Changes Detail, Not Reality

Low-resolution family members remain real people within World Truth.

---

## FAMREG-INV-015 — Promotion Must Preserve History

Increasing Character resolution must not rewrite established Canon.

---

## FAMREG-INV-016 — Families Are Not Collective Minds

Individual family members retain separate agency, beliefs, memories, goals and psychology.

---

## FAMREG-INV-017 — No Placeholder Families

Families enter the registry when they become meaningful Canon.

---

## FAMREG-INV-018 — No Premature Genealogical Expansion

Create enough history to establish plausible continuity, then allow future history to emerge.

---

## FAMREG-INV-019 — Cross-Family History May Outlive Its Originators

Historical connections may remain relevant after the Characters who created them are dead.

---

## FAMREG-INV-020 — Family Continuity Serves Human History

The purpose of Family persistence is to preserve meaningful human causality across time, not to create dynastic game mechanics.

---

# 56. Development Locks

Future development must not turn `Canon/Universe/Families/` into:

- a new simulation engine
- a Character replacement
- a Relationship replacement
- a Memory system
- a Trust system
- a Belief system
- a Psychology system
- a genetics simulator
- a dynasty mechanic
- an inherited personality system
- an inherited morality system
- a universal loyalty system
- a faction replacement
- a household simulation replacement
- a deterministic genealogy generator
- a narrative destiny system

Avoid:

```text
THE MITCHELLS
ARE LOYAL.
```

Prefer:

```text
THE MITCHELL FAMILY
HAS A HISTORICAL NARRATIVE
AROUND FAMILY RESPONSIBILITY.

INDIVIDUAL MITCHELLS
INTERPRET THAT HISTORY
DIFFERENTLY.
```

Avoid:

```text
THE CARTERS
HATE THE MITCHELLS.
```

Prefer:

```text
THE CARTER FAMILY
CARRIES A NEGATIVE
HISTORICAL STORY
ABOUT A PAST
MITCHELL ACTION.

INDIVIDUAL DESCENDANTS
MAY ACCEPT,
QUESTION,
REJECT
OR REINTERPRET
THAT STORY.
```

Avoid:

```text
ETHAN TRUSTS RACHEL
BECAUSE THEIR PARENTS
TRUSTED EACH OTHER.
```

Prefer:

```text
THE HISTORICAL CONNECTION
REDUCED INITIAL UNCERTAINTY
AND MADE ENGAGEMENT
MORE LIKELY.

PERSONAL TRUST
DEVELOPED OR FAILED
THROUGH THEIR OWN
RELATIONSHIP.
```

---

# 57. Family Design Test

Before establishing a canonical Family, ask:

```text
WHY DOES THIS FAMILY
NEED TO EXIST IN CANON?

WHERE DID THE FAMILY
COME FROM?

WHICH GENERATIONS
CURRENTLY MATTER?

WHO ARE THE
IMPORTANT MEMBERS?

WHO EXISTS ONLY
AS HISTORICAL CONTEXT?

WHERE DOES
THE FAMILY LIVE?

WHAT FAMILY BRANCHES
EXIST?

WHAT HISTORY
CONNECTS THEM?

WHAT HISTORY
DIVIDES THEM?

WHAT STORIES
DO THEY TELL?

WHICH STORIES
ARE CONTESTED?

WHAT DOES
WORLD TRUTH KNOW
THAT THE FAMILY
DOES NOT?

WHAT CONSEQUENCES
HAVE CROSSED
GENERATIONS?

WHAT RESPONSIBILITIES
CURRENTLY EXIST?

WHAT OTHER FAMILIES
ARE HISTORICALLY
CONNECTED?

WHAT CONTINUES
WHEN A MEMBER DIES?

WHAT REMAINS
UNKNOWN?

WHAT FUTURE
IS STILL OPEN?
```

The result should create historical human context.

Not predetermined Characters.

---

# 58. Family Architecture

Conceptually:

```text
WORLD TRUTH
        ↓
HISTORICAL CONDITIONS
        ↓
FAMILY ORIGIN
        ↓
FAMILY HISTORY
        ↓
────────────────────────
        ↓
GENERATION
        ↓
INDIVIDUAL CHARACTERS
        ↓
LIFE EVENTS
        ↓
MEMORY
        ↓
BELIEFS
        ↓
RELATIONSHIPS
        ↓
PSYCHOLOGY
        ↓
GOALS
        ↓
AGENCY
        ↓
CHOICE
        ↓
ACTION
        ↓
CONSEQUENCE
        ↓
────────────────────────
        ↓
FAMILY HISTORY
        ↓
FAMILY STORIES
        ↓
REPUTATION
        ↓
PROPERTY / RESPONSIBILITY /
CONNECTION / KNOWLEDGE
        ↓
NEXT GENERATION
        ↓
NEW INDIVIDUAL CHARACTERS
        ↓
NEW CHOICES
        ↓
FUTURE HISTORY
```

No single layer owns the entire chain.

---

# 59. Families North Star

The Families structure succeeds when Project Ascension can follow:

```text
A PERSON

        ↓

A FAMILY

        ↓

A GENERATION

        ↓

HISTORY

        ↓

CONSEQUENCE

        ↓

ANOTHER GENERATION

        ↓

NEW PEOPLE

        ↓

NEW CHOICES
```

without turning ancestry into destiny.

The North Star is:

> **Families allow human history to continue beyond individual lives while ensuring that every new generation remains free to interpret, challenge and change what it inherits.**

---

# 60. Initial Canonical Family

The first family developed under this structure is:

```text
MITCHELL FAMILY
```

Initial location:

```text
Canon/Universe/Families/Mitchell/
```

Initial documents:

```text
README.md
Mitchell_Family.md
Mitchell_Family_Chronicle.md
```

Initial high-resolution Character:

```text
Canon/Universe/Characters/People/Mitchell/Sarah_Mitchell.md
```

The Mitchell family will serve as the first practical validation of:

- multigenerational Family continuity
- Character creation from historical context
- Family Chronicle architecture
- Character resolution
- Character promotion
- intergenerational consequence
- historical family narratives
- cross-family connection
- historical trust context
- succession
- death and legacy
- persistence across World States

The family should not be designed to prove these systems correct.

Its history should be allowed to expose weaknesses in them.

---

# 61. Closing Principle

Project Ascension does not follow only civilizations, institutions or technologies.

It follows people.

People have parents.

Children.

Partners.

Siblings.

Grandparents.

Friends who become family.

People they leave.

People they return to.

People whose stories survive them.

A decision made by one person may still matter decades after that person is dead.

But the people who inherit its consequences remain their own.

Therefore:

> **A family carries history forward. It does not decide what the next generation will do with it.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-09-01 | Established the canonical Families universe structure. Defined separation between Family concept architecture and specific canonical families; standardized Family directories, Family documents and Chronicles; established Character independence, simulation-resolution handling, intergenerational consequence, historical family narratives, cross-family continuity, historical trust context, death and succession, canonical invariants, development locks and the initial Mitchell family validation role. |