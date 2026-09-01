# PROJECT ASCENSION

# Project Memory

| Field | Value |
|---|---|
| Document | Project Memory README |
| Version | 1.0 |
| Status | Active |
| Category | Project Memory |
| Owner | Project Architecture |
| Last Updated | 2026-08-30 |

> **"The project should remember itself."**

---

# Purpose

Project Memory preserves the current state, major decisions, architectural context and historical reasoning of Project Ascension.

Its purpose is to make the project understandable and continuable across:

- AI conversations
- AI models
- development sessions
- contributors
- long periods of time

Project Memory exists so that Project Ascension does not depend on one conversation remembering everything.

---

# Core Principle

Project Memory is not Canon.

It is the continuity layer around Canon.

Conceptually:

```text
CANON
=
WHAT IS TRUE

PROJECT MEMORY
=
WHERE WE ARE
AND WHY

CONVERSATION HISTORY
=
HOW WE GOT THERE

GIT
=
WHAT CHANGED.
```

---

# Authority

Project Memory must never silently override Canon.

When information conflicts:

```text
CURRENT CANON
↓
CURRENT ARCHITECTURE
↓
CURRENT PROJECT STATE
↓
DECISION LOGS
↓
PROJECT MEMORY
↓
CONVERSATION HISTORY
↓
LEGACY MATERIAL.
```

Canon remains authoritative.

---

# Directory Structure

The intended Project Memory structure is:

```text
Project_Memory/
├── README.md
├── Current_Project_State.md
├── Architecture_Decisions.md
├── Canon_Decisions.md
└── Conversation_History/
```

Additional files may be introduced later only when they have a clear unique responsibility.

---

# Current_Project_State.md

`Current_Project_State.md` is the primary orientation document.

It should answer:

```text
WHERE IS
THE PROJECT NOW?

WHAT HAS
RECENTLY CHANGED?

WHAT IS
CURRENTLY CANONICAL?

WHAT HAS
BEEN MOVED?

WHAT HAS
BEEN REMOVED?

WHAT IS
CURRENTLY BEING REVIEWED?

WHAT IS
THE NEXT LOGICAL STEP?
```

It should remain concise enough to read at the beginning of a new AI session.

It is not intended to duplicate every Canon file.

---

# Architecture_Decisions.md

`Architecture_Decisions.md` records important structural decisions.

Examples include:

```text
SYSTEM OWNERSHIP

FILE MOVES

SYSTEM SPLITS

SYSTEM MERGES

RESPONSIBILITY BOUNDARIES

SIMULATION PRINCIPLES

PROJECT STRUCTURE DECISIONS.
```

Its purpose is to preserve:

```text
WHY THE ARCHITECTURE
LOOKS THIS WAY.
```

---

# Canon_Decisions.md

`Canon_Decisions.md` records important creative or world decisions that should remain visible outside the full Canon structure.

Examples may include:

```text
WORLD HISTORY DECISIONS

AURORA DECISIONS

MAJOR SETTING RULES

MAJOR TERMINOLOGY

LOCKED CREATIVE DIRECTIONS.
```

This file is not a replacement for Canon.

It is a decision index.

The full authoritative definition remains in Canon.

---

# Conversation_History

`Conversation_History/` stores historical AI conversation material when useful for long-term continuity.

Its purpose is to preserve:

```text
EARLY REASONING

ALTERNATIVES

REJECTED IDEAS

DESIGN DISCUSSION

CONTEXT

PROJECT EVOLUTION.
```

Conversation history is not Canon.

---

# Conversation History Rule

```text
CONVERSATION HISTORY
MAY EXPLAIN

WHY

BUT IT DOES NOT
AUTOMATICALLY DEFINE

WHAT IS TRUE NOW.
```

If conversation history conflicts with current Canon:

```text
CANON WINS.
```

---

# When to Read Conversation History

Conversation History should not be required for normal project work.

Normal AI startup should be:

```text
PROJECT_INSTRUCTIONS.md
↓
Current_Project_State.md
↓
RELEVANT CANON
↓
RELEVANT DECISION LOGS.
```

Only inspect Conversation History when:

- a historical reason is unclear
- an old design needs to be audited
- a previous rejected idea must be understood
- a missing decision cannot be reconstructed from current documentation

---

# What Belongs in Project Memory

Project Memory should contain information such as:

```text
CURRENT WORKSTREAM

RECENT ARCHITECTURAL CHANGES

IMPORTANT MOVES

IMPORTANT REMOVALS

CURRENT CLEANUP STATUS

LOCKED DECISIONS

OPEN QUESTIONS

CURRENT PRIORITIES

NEXT RECOMMENDED STEP

REASONS BEHIND
IMPORTANT STRUCTURAL CHOICES.
```

---

# What Does Not Belong in Project Memory

Do not place full authoritative system definitions here if they already belong in Canon.

Avoid duplicating:

```text
WORLD RULES

HUMAN SYSTEM DEFINITIONS

AURORA COGNITION

FACTION STATE

SOCIETY STATE

CHARACTER SYSTEMS

NARRATIVE ARCHITECTURE

WORLD SIMULATION RULES.
```

Those belong in their authoritative Canon locations.

---

# Project Memory Is Curated

Project Memory should not become a dumping ground.

The goal is:

```text
HIGH SIGNAL

LOW DUPLICATION

CLEAR CONTINUITY.
```

Do not copy every discussion into every memory file.

---

# Update Triggers

`Current_Project_State.md` should normally be updated after:

```text
MAJOR SYSTEM REBUILD

MAJOR FILE MOVE

SYSTEM REMOVAL

NEW SYSTEM CREATION

OWNERSHIP CHANGE

NEW CANON FOUNDATION

MAJOR CLEANUP MILESTONE

CHANGE IN CURRENT WORKSTREAM.
```

---

# Decision Logging

A decision should normally be logged when:

```text
FUTURE CONTRIBUTORS
MIGHT OTHERWISE
REINTRODUCE
THE OLD APPROACH.
```

Examples:

```text
REMOVING UNIVERSAL XP

MOVING AGING
FROM CHARACTERS TO LIFE

SEPARATING SOCIETY
FROM FACTIONS

DEFINING NPCs
AS CHARACTERS

SEPARATING STORY
FROM WORLD TRUTH.
```

---

# Decision Record Structure

Decision entries should preferably include:

```text
DATE

DECISION

STATUS

CONTEXT

RATIONALE

CONSEQUENCES

AFFECTED FILES

SUPERSEDED APPROACH.
```

Keep entries concise.

---

# Memory vs Git

Git answers:

```text
WHAT CHANGED?
```

Project Memory answers:

```text
WHY DOES
THE CURRENT PROJECT
LOOK THIS WAY?
```

Do not duplicate full Git history inside Project Memory.

---

# Memory vs Canon

Canon answers:

```text
WHAT IS TRUE?
```

Project Memory answers:

```text
WHAT ARE WE
WORKING ON?

WHAT CHANGED?

WHY DID
WE CHANGE IT?
```

These responsibilities must remain separate.

---

# Memory vs README

Repository or system README files explain:

```text
WHAT THIS AREA IS

HOW IT IS ORGANIZED

WHAT DOCUMENTS
LIVE HERE.
```

Project Memory explains:

```text
WHERE THE PROJECT
CURRENTLY STANDS.
```

---

# Memory and Legacy Cleanup

Project Ascension contains material from earlier architectural phases.

Project Memory should track significant cleanup decisions such as:

```text
FILE MOVED

FILE REBUILT

FILE MERGED

FILE SPLIT

FILE REMOVED

OWNERSHIP CHANGED.
```

This prevents old architecture from being accidentally recreated later.

---

# Memory and AI

Any AI working on Project Ascension should use Project Memory to establish continuity before making significant changes.

The expected sequence is:

```text
READ
PROJECT_INSTRUCTIONS.md
↓
READ
Current_Project_State.md
↓
READ
RELEVANT CANON
↓
CHECK
DECISION LOGS
↓
WORK
↓
UPDATE MEMORY
IF REQUIRED.
```

---

# AI Must Not Treat Memory as Canon

If Project Memory says:

```text
WE PLAN TO
BUILD X
```

that does not mean:

```text
X IS CANON.
```

Likewise:

```text
WE ARE CONSIDERING Y
```

does not mean:

```text
Y HAS BEEN DECIDED.
```

Status must remain explicit.

---

# Status Language

Project Memory should distinguish:

```text
CANONICAL

DECIDED

CURRENT

IN REVIEW

PROPOSED

OPEN

SUPERSEDED

REMOVED.
```

Avoid ambiguous statements.

---

# Open Questions

Open questions should remain visibly open.

Do not silently resolve them during unrelated work.

A question remains open until:

```text
A DECISION
IS EXPLICITLY MADE.
```

---

# Superseded Decisions

When a decision is replaced:

```text
DO NOT DELETE
THE HISTORICAL REASON
IF IT REMAINS USEFUL.
```

Instead mark it:

```text
SUPERSEDED.
```

Then reference the newer decision.

This preserves architectural history without creating competing authority.

---

# Canon Promotion

An idea may begin as:

```text
DISCUSSION
↓
PROPOSAL
↓
DECISION
↓
CANON.
```

Project Memory may preserve the earlier stages.

Once promoted to Canon, the authoritative definition belongs in Canon.

---

# Project Continuity

The goal of Project Memory is that a new contributor or AI can determine:

```text
WHAT PROJECT ASCENSION IS

WHAT WE HAVE ALREADY BUILT

WHAT HAS RECENTLY CHANGED

WHAT OLD ASSUMPTIONS
ARE NO LONGER VALID

WHAT IS CURRENTLY
BEING REVIEWED

WHAT SHOULD
HAPPEN NEXT.
```

without reading the entire project history.

---

# Anti-Duplication Principle

Do not maintain the same authoritative information in multiple places.

Prefer:

```text
ONE OWNER
+
REFERENCES.
```

Not:

```text
MULTIPLE COPIES
THAT CAN DRIFT.
```

---

# Anti-Memory-Bloat Principle

Project Memory must remain usable.

Do not turn:

```text
Current_Project_State.md
```

into:

```text
THE ENTIRE PROJECT
IN ONE FILE.
```

It is an orientation document.

Not a replacement for Canon.

---

# Conversation Archive Naming

Conversation history files should use clear chronological naming.

Recommended pattern:

```text
YYYY-MM_Project_Ascension_Chat_XX.md
```

Example:

```text
2026-08_Project_Ascension_Chat_01.md
2026-08_Project_Ascension_Chat_02.md
2026-09_Project_Ascension_Chat_01.md
```

If a conversation has a clearly defined topic, a short suffix may be used:

```text
2026-08_Chat_Character_Architecture.md
```

Consistency is more important than the exact naming convention.

---

# Conversation Archive Content

A Conversation History file may contain:

```text
DATE RANGE

SOURCE

TOPICS

RAW OR CURATED TRANSCRIPT

IMPORTANT DECISIONS

NOTES ON
WHAT WAS LATER SUPERSEDED.
```

Raw transcripts may be preserved.

Curated summaries are preferred for routine access.

---

# Raw Conversation Rule

If raw conversation history is stored:

```text
DO NOT EDIT IT
TO MAKE OLD DISCUSSION
LOOK CURRENT.
```

Historical material should remain historical.

Corrections belong in:

```text
CURRENT PROJECT STATE

DECISION LOGS

CANON.
```

---

# Memory Maintenance Rule

Project Memory should evolve whenever the architecture meaningfully changes.

But maintenance should remain proportional.

Do not update ten memory files for a trivial text correction.

Update memory when continuity would otherwise be lost.

---

# Recommended Minimal Workflow

After a major work session:

```text
1. CANON FILES UPDATED

2. ARCHITECTURE VALIDATED

3. Current_Project_State.md
   UPDATED

4. IMPORTANT DECISION
   LOGGED IF REQUIRED

5. NEXT STEP
   RECORDED

6. GIT COMMIT.
```

---

# Project Memory Invariants

## MEMORY-INV-001

Project Memory does not override Canon.

## MEMORY-INV-002

Conversation history is context, not authority.

## MEMORY-INV-003

Current Project State must reflect the current project, not historical state.

## MEMORY-INV-004

Important architectural decisions should remain explainable.

## MEMORY-INV-005

Superseded design must not appear current.

## MEMORY-INV-006

Project Memory should minimize duplication of Canon.

## MEMORY-INV-007

Open questions must remain explicitly open.

## MEMORY-INV-008

A new AI should not need the full conversation archive for normal work.

## MEMORY-INV-009

Major cleanup decisions should be recorded.

## MEMORY-INV-010

Project Memory should remain readable enough to serve as a startup context layer.

---

# Development Locks

Project Memory must not become:

```text
A SECOND CANON

A DUPLICATE REPOSITORY

A GIANT UNCURATED CHAT DUMP

A SUBSTITUTE FOR GIT

A PLACE FOR IMPLEMENTATION CODE

AN EXCUSE TO STOP
MAINTAINING SYSTEM DOCUMENTATION.
```

---

# Project Memory North Star

Project Memory succeeds when a new AI can open the repository, read a small number of files, and understand:

```text
WHERE ARE WE?

WHAT HAS CHANGED?

WHAT IS TRUE?

WHY IS THE
ARCHITECTURE LIKE THIS?

WHAT SHOULD
I NOT REINTRODUCE?

WHAT ARE WE
DOING NEXT?
```

without depending on the memory of a previous conversation.

---

# Closing Principle

Project Ascension is intended to grow over a long period of time.

Its architecture, world, history, and human systems will continue to evolve.

The continuity of that work cannot depend on one chat session.

It cannot depend on one AI model.

It cannot depend on one person's memory.

The project itself must preserve enough context to continue correctly.

The central principle is:

> **Canon preserves truth. Project Memory preserves continuity. Conversation History preserves context. Git preserves change. Together they allow Project Ascension to remember itself.**

---

# Revision History

| Version | Date | Description |
|---|---|---|
| 1.0 | 2026-08-30 | Established the Project Memory architecture and defined the role, authority, directory structure, update rules, decision logging, conversation history handling, AI startup workflow, invariants and development locks for long-term Project Ascension continuity. |