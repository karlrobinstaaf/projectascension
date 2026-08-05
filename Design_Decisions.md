# PROJECT ASCENSION
# Design Decisions

| Field | Value |
|--------|-------|
| Document | Design Decisions |
| Version | 0.1 |
| Status | Active |
| Category | Internal Design |
| Owner | Creative Team |
| Last Updated | 2026-08-03 |

---

# Purpose

Design Decisions documents the reasoning behind the most important architectural, narrative and gameplay decisions made during the development of Project Ascension.

This document is **not** part of the game world.

It exists to explain **why** decisions were made.

Every major system should have a corresponding Design Decision before it becomes part of the official design.

The purpose is to preserve the project's long-term vision and prevent important design knowledge from being lost over time.

---

# Decision Status

Every design decision follows the same lifecycle.

IDEA

The concept has been discussed but not evaluated.

↓

DESIGN

The concept has been analyzed and accepted as the preferred direction.

↓

DRAFT

The concept is being integrated into official documentation.

↓

REVIEW

The design has been reviewed against existing documentation.

↓

CANON

The decision becomes part of Project Ascension's permanent design.

---

# Decision Template

Every Design Decision should answer the following questions.

## Title

A short descriptive name.

---

## Problem

What problem are we trying to solve?

---

## Decision

What did we decide?

---

## Why

Why was this solution chosen?

---

## Alternatives Considered

What other ideas were discussed?

Why were they rejected?

---

## Benefits

What advantages does this solution provide?

---

## Risks

What possible drawbacks exist?

How can they be minimized?

---

## Future Questions

What remains unknown?

Can this decision evolve later?

---

## Documents Affected

Which documents depend on this decision?

Example:

- Vision
- Creative Pillars
- Design Principles
- Canon
- Living Campaign Engine

---

## Revision History

How has this decision evolved over time?

---

# Design Decision DD-001

## Title

The Living Team System

---

## Status

DESIGN

---

## Problem

Project Ascension supports between one and six human players.

Traditional tabletop systems often become less engaging with fewer players because important conversations, expertise and group dynamics disappear.

The challenge was to create a system where solo play feels as rich and emotionally engaging as a full group experience without making AI companions feel like scripted followers.

---

## Decision

Project Ascension always builds the campaign around a six-person expedition.

Human players occupy as many positions as are available.

Any remaining positions are filled by fully realized AI-controlled companions.

These companions are not assistants.

They are complete characters with their own:

- personalities
- strengths
- weaknesses
- goals
- fears
- relationships
- secrets
- moral beliefs
- emotional development

Every companion is generated using exactly the same character creation system as human players.

No companion is intentionally stronger than a player.

No companion exists merely to support the players.

They are members of the team.

---

## Hidden Rule

The players are never explicitly told which members are controlled by AI.

Inside the game world, every character is treated equally.

The distinction between player character and companion exists only outside the narrative.

---

## Aurora Connection

Aurora appears to consistently favor six-person teams.

Whether this is intentional, statistical or coincidental remains unknown.

Throughout the campaign players may discover evidence suggesting that Aurora believes six-person groups demonstrate the highest long-term survival probability.

Aurora never explains why.

The players must draw their own conclusions.

---

## Why

This decision strengthens several core goals:

- Solo play remains emotionally engaging.
- Group dynamics always exist.
- Every campaign feels alive.
- Companions become memorable characters rather than tools.
- Player absence never breaks the campaign.
- New players can seamlessly join existing campaigns.
- The world feels persistent.

---

## Alternatives Considered

### Alternative A

Allow any group size.

Rejected because important dynamics disappear with very small groups.

---

### Alternative B

Scale encounters based on player count.

Rejected because the world should remain consistent rather than adapting itself around the players.

---

### Alternative C

Traditional NPC followers.

Rejected because followers often become passive quest tools instead of believable people.

---

## Benefits

- Rich conversations in every campaign.
- Strong emotional attachment.
- Better replayability.
- Consistent narrative pacing.
- Stronger immersion.
- Seamless multiplayer.
- Better solo experience.

---

## Risks

Players may incorrectly assume companions always possess perfect information.

To avoid this:

Companions follow exactly the same knowledge rules as everyone else.

They can misunderstand.

Forget.

Panic.

Lie.

Refuse.

Make mistakes.

Leave.

Even betray the group.

---

## Future Questions

Should companions permanently leave the expedition?

Can companions become antagonists?

Can players later take over an existing companion?

Can companions die permanently?

Should Aurora deliberately attempt to replace lost members?

---

## Documents Affected

- Vision
- Creative Pillars
- Design Principles
- Canon
- Character System
- Living Campaign Engine
- Game Master Bible

---

## Creative Director Notes

This decision reinforces one of the central ideas behind Project Ascension:

The player is never alone.

Even in a single-player campaign, the experience should feel like traveling with real people rather than managing artificial companions.

The goal is not to simulate additional players.

The goal is to create believable human beings.

---

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-03 | Initial Design Decision |

---

# Design Decision DD-002

## Title

The Living History System

---

## Status

DESIGN

---

## Problem

Traditional roleplaying games often treat history as static.

The world has a fixed past, a fixed present and a fixed future.

Player actions usually affect only their own campaign.

Project Ascension aims to create a world where history itself feels alive.

---

## Decision

Project Ascension distinguishes between different layers of history.

Some historical events are universal and never change.

Other events may differ between campaigns.

Player actions should have the potential to become part of future history.

History is therefore not only something players discover.

It is something they help create.

---

## Historical Layers

### Universal History

Events that define the universe itself.

Examples include:

- The creation of Aurora.
- The Collapse.
- The end of the old global society.

These events are immutable.

---

### Regional History

History that may differ between locations.

Examples include:

- Which settlements survived.
- Which factions gained influence.
- Local conflicts.
- Community traditions.

Different campaigns may produce different regional histories.

---

### Campaign Legacy

The actions of one group may become historical traces for future groups.

Examples include:

- Hidden journals.
- Research notes.
- Radio recordings.
- Landmarks.
- Graves.
- Safe houses.
- Symbols.
- Scientific discoveries.

Future campaigns may discover these remnants without necessarily knowing who created them.

---

## Why

History becomes something players participate in rather than simply observe.

The world feels older than the players.

Every campaign has the possibility of leaving a meaningful legacy.

---

## Benefits

- Stronger immersion.
- Greater replayability.
- Emotional attachment.
- Living world continuity.
- Community storytelling.

---

## Risks

An unrestricted legacy system could eventually create contradictory world histories.

To avoid this, Universal History always remains fixed while Campaign Legacy only affects appropriate historical layers.

---

## Future Questions

Should campaigns be able to influence events decades into the future?

How much historical information should later groups be able to discover?

Should player-created history ever become official canon?

---

## Documents Affected

- Canon
- The Collapse
- Living Campaign Engine
- Story Framework
- World Ledger

---

## Creative Director Notes

Project Ascension should not merely tell stories.

It should preserve them.

Players should occasionally discover evidence that another group once stood exactly where they are now.

History should feel personal.

---

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1 | 2026-08-04 | Initial Design Decision created. |