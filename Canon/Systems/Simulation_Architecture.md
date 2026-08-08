# PROJECT ASCENSION
# Simulation Architecture

| Field | Value |
|--------|-------|
| Document | Simulation Architecture |
| Version | 0.1 |
| Status | Foundation |
| Category | Systems |
| Owner | Systems Architecture |
| Last Updated | 2026-08-08 |

> *"A living world is not one system. It is many systems working together."*

---

# Purpose

Simulation Architecture defines the major simulation engines that together create the living world of Project Ascension.

It is the architectural blueprint of the simulation.

This document intentionally avoids implementation details.

Instead it describes responsibilities, relationships and boundaries between the different engines.

---

# Core Philosophy

No single engine creates a living world.

A believable world emerges when multiple independent systems continuously influence one another.

Each engine has a clearly defined responsibility.

Together they create complexity.

---

# Architectural Principles

Every simulation engine should:

- have one clear responsibility
- remain independent whenever possible
- communicate through defined interfaces
- evolve without requiring changes to unrelated systems
- contribute to the Living World philosophy

No engine should attempt to solve every problem.

---

# High-Level Architecture

```
                   World Engine
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 Society Engine     Environment      Event Engine
        │              Engine              │
        │                │                │
        └────────────┬───┴────────────────┘
                     ▼
              Settlement Engine
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Life Engine       Economy Engine
          │
     ┌────┴─────┐
     ▼          ▼
Relationship  Companion
   Engine      Engine
     │
     ▼
Narrative Engine
     │
     ▼
Player Experience
```

The architecture illustrates conceptual dependencies rather than technical implementation.

---

# Engine Responsibilities

## World Engine

Maintains the global state of the world.

Examples:

- Timeline
- World States
- Climate
- Global events
- Large-scale changes

---

## Society Engine

Simulates societies, governments, factions and social structures.

Responsible for how groups evolve over time.

---

## Environment Engine

Simulates nature and the physical world.

Examples:

- Seasons
- Weather
- Ecosystems
- Natural resources

---

## Event Engine

Generates significant events.

Examples:

- disasters
- discoveries
- conflicts
- migrations
- political changes

---

## Settlement Engine

Simulates towns, villages and cities.

Responsible for:

- population
- infrastructure
- local leadership
- culture
- security

---

## Economy Engine

Simulates production, trade, scarcity and resource flow.

This engine influences societies rather than individual characters.

---

## Life Engine

Creates and evolves individual human lives.

Responsible for:

- Human generation
- Life Events
- Psychological development
- Human Attributes

---

## Relationship Engine

Maintains relationships between individuals.

Responsible for:

- trust
- loyalty
- conflict
- reputation
- family
- friendship

---

## Companion Engine

Controls long-term companion behaviour and development.

Companions evolve independently throughout the campaign.

---

## Narrative Engine

Transforms simulation into memorable stories.

The Narrative Engine never writes stories.

It identifies meaningful moments emerging naturally from the simulation.

---

# Aurora

Aurora is **not** the Simulation Architecture.

Aurora exists within the architecture.

Like every other actor in Project Ascension, Aurora interacts with the simulation rather than replacing it.

The world must remain believable even without Aurora.

Aurora changes the world.

Aurora is not the world.

---

# Shared Principles

All engines should:

- operate continuously
- influence one another
- avoid hard scripting whenever possible
- favour emergence over predetermined outcomes
- prioritise believable behaviour over complexity

---

# Future Expansion

Additional engines may include:

- Knowledge Engine
- Communication Engine
- Crime Engine
- Transportation Engine
- Healthcare Engine
- Education Engine
- Religion Engine

Future additions should integrate into the existing architecture without altering its philosophical foundation.

---

# Relationship to Other Documents

Simulation Architecture connects:

- Human Model
- Character Generation Framework
- Life Generator
- World States
- Historical Timeline
- Narrative Systems
- AI Systems

---

# Closing Statement

Project Ascension is not powered by one intelligent system.

It is powered by many specialised systems continuously shaping one another.

From those interactions...

a living world emerges.

---

# Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-08 | Initial high-level simulation architecture established. |