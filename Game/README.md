# Project Ascension — Game

Living-room client and room server for Project Ascension. This folder is the technical foundation: a shared television, phones as controllers, and an authoritative room server. It is not campaign content. Canon and the Aurora validation harness are unchanged.

One to six people play together in front of a large screen. The television is the host and the shared window. Each phone is one character. With fewer than six humans, empty seats stay empty in this version — NPC characters are not implemented yet. A single human can play alone.

## Run locally

Requires Node.js 22 or newer.

```bash
cd Game
npm install
npm run dev
```

That starts three processes: the shared types watcher, the room server on port `3001`, and the Vite client on port `5173` (reachable on your LAN).

Open the television view:

```text
http://localhost:5173/tv
```

A room code and QR code appear, with a short opening narration from the mock Game Master.

### Join from a phone on the same Wi-Fi

The QR code uses the address currently open in the television browser. `localhost` is not reachable from a phone. On the television, open the page with this computer’s LAN address instead, for example:

```text
http://192.168.1.20:5173/tv
```

The lobby lists that address when it can see one. Then scan the QR code, or on the phone open `http://<lan-address>:5173/join` and type the room code. Choose a name and take a seat.

If the phone cannot connect, allow inbound TCP `5173` on the computer’s firewall. Phones do not need port `3001`; the client proxies the socket through Vite.

Type what the character does and press Send. The server passes an explicit view to the Game Master. The reply’s narration shows on the television. A private note, when the mock sends one, appears only on that player’s phone under **Only you**. Try: `I listen to the hum behind the diner.`

Refresh either device to reconnect. The television keeps the room with its host token. A phone keeps its seat with a player token. Seats are not freed when someone disconnects, so a refresh cannot be crowded out. Restarting the server drops every room (state is in memory).

### Single-port production mode

```bash
npm run build
npm start
```

The server listens on `PORT` (default `3001`), serves the built client, and hosts the socket on the same origin. Open `/tv` on that port.

## Scripts

| Command | What it does |
|---|---|
| `npm run dev` | Shared watcher, server, and client together |
| `npm test` | Room, view-boundary, Game Master, and socket loop tests |
| `npm run lint` | ESLint |
| `npm run typecheck` | `tsc` for shared, server, and client |
| `npm run build` | Compile shared and server, and build the client |
| `npm start` | Serve the built client and the socket on one port |

## Environment

Server:

| Variable | Default | Purpose |
|---|---|---|
| `PORT` | `3001` | HTTP and socket port |
| `HOST` | `0.0.0.0` | Bind address |
| `GAMEMASTER_PROVIDER` | `mock` | `mock` or `llm` |
| `GAMEMASTER_API_KEY` | unset | Read by the LLM stub. Not used. |
| `GAMEMASTER_MODEL` | unset | Read by the LLM stub. Not used. |
| `GAMEMASTER_BASE_URL` | unset | Read by the LLM stub. Not used. |
| `CLIENT_DIST` | `client/dist` | Built client, for `npm start` |

Client:

| Variable | Default | Purpose |
|---|---|---|
| `VITE_SPEECH_INPUT` | on | Set to `false` to hide the mic button |

`mock` needs no API key. `llm` constructs the stub and fails closed: it does not call a provider.

## Architecture

```text
TV browser  ──┐
              ├── socket.io ── RoomStore (authoritative)
phone       ──┘                    │
                                   │ explicit view only
                                   ▼
                             GameMaster
                               ├── MockGameMaster   (default)
                               └── LlmGameMaster    (stub)
```

Two boundaries are intentional:

- **Wire.** Clients receive `PublicRoomState`. A phone also receives `PrivatePlayerState` for its own seat. Tokens, other players’ private notes, and server-only facts are not on those objects.
- **Game Master.** `toGameMasterOpeningView` and `toGameMasterActionContext` copy the fields the model is allowed to read. Implementations take those types and do not import the room. Hidden world facts stay on `Room.serverOnly` and are covered by tests that fail if they leak.

Player input is a `PlayerIntent`: `{ text, source }` where `source` is `text` or `speech`. The text field is the path that matters. The mic button is optional. It uses the browser Web Speech API behind `SpeechToTextSource`, writes into the same field, and does not submit on its own. That API may send audio to the browser vendor’s speech service. Set `VITE_SPEECH_INPUT=false` to remove the button. Typing never does that.

## Implemented

- Television view: room code, QR join link, player list, shared narration, dark type that scales from a laptop to 1080p and 4K.
- Phone view: join by code or QR, name, text action, private panel.
- Rooms of 1–6 players, host is the television, reconnect after refresh.
- Mock Game Master with deterministic canned replies, including one private-note example.
- LLM provider stub selected with `GAMEMASTER_PROVIDER=llm`.
- Lint, typecheck, tests, and a GitHub Actions workflow that also runs the Aurora validation harness.

## Not implemented

- A real model call, world simulation, resolution rolls, inventory, map, journal, images, music, or NPC characters.
- Leaving a seat. A disconnect keeps the seat until the server process stops.
- Persistence. Rooms live in memory.
- Accounts. The room code plus the unguessable seat token are the only credentials, meant for a trusted home network.
