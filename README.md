# Project Ascension

> The world does not exist because of the players. The players exist inside the world.

Project Ascension is an AI-driven cooperative narrative RPG for 1–6 players, fully playable solo. With fewer than six humans, NPC characters fill out the six-character group. It is set in a near-future United States after the emergence of the superintelligence Aurora.

## Core Pillars

- A living world that changes without waiting for the players.
- Human relationships, trust and betrayal at the center of play.
- Expertise creates better choices, not automatic answers.
- Aurora is highly intelligent but never omniscient.
- Every session creates permanent history in the World Ledger.

## Getting Oriented

- [`PROJECT_OVERVIEW_SV.md`](PROJECT_OVERVIEW_SV.md) — overview of the project, its purpose and current state (Swedish).
- [`PROJECT_INSTRUCTIONS.md`](PROJECT_INSTRUCTIONS.md) — how work is performed in this repository.
- [`Project_Memory/Current_Project_State.md`](Project_Memory/Current_Project_State.md) — where the project currently is and what comes next.

## Play

The living-room client and room server are in [`Game/`](Game/README.md): a shared television view, a phone controller, and an authoritative server with a mock Game Master. Canon and the Aurora validation harness are separate.

```bash
cd Game
npm install
npm run dev
```

Open the television at [http://localhost:5173/tv](http://localhost:5173/tv). Use this computer’s LAN address instead of `localhost` when a phone on the same Wi-Fi should join.
