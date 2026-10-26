import { randomUUID } from "node:crypto";
import { MAX_PLAYERS, type PlayerIntent, type TranscriptEntry } from "@ascension/shared";
import type { GameMasterResult } from "../gameMaster/types.js";
import { generateRoomCode, generateToken } from "./codes.js";
import type { PlayerRecord, RecordedAction, Room, SocketBinding } from "./types.js";
import { sanitizeGameMasterResult, trimPrivateNotes, trimTranscript } from "./view.js";

export const UNDISCLOSED_FACT_CANARY =
  "UNDISCLOSED_CANARY_do_not_disclose_fuel_cache";

export const PLACEHOLDER_SCENE = {
  locationLabel: "Edge of town",
  timeLabel: "After dark",
} as const;

export type AddPlayerResult =
  | { ok: true; player: PlayerRecord; replacedSocketId: string | null }
  | { ok: false; reason: "NOT_FOUND" | "FULL" };

export class RoomStore {
  private readonly rooms = new Map<string, Room>();
  private readonly sockets = new Map<string, SocketBinding>();

  create(hostSocketId: string, openingNarration: string): Room {
    const code = this.allocateCode();
    const room: Room = {
      code,
      hostToken: generateToken(),
      hostSocketId,
      scene: { ...PLACEHOLDER_SCENE },
      players: [],
      transcript: [narrationEntry(openingNarration)],
      serverOnly: { undisclosedFact: UNDISCLOSED_FACT_CANARY },
      playStarted: false,
    };
    this.rooms.set(code, room);
    this.sockets.set(hostSocketId, { code, role: "host" });
    return room;
  }

  get(code: string): Room | undefined {
    return this.rooms.get(code);
  }

  attachHost(
    code: string,
    hostToken: string,
    socketId: string,
  ): { room: Room; replacedSocketId: string | null } | null {
    const room = this.rooms.get(code);
    if (!room || room.hostToken !== hostToken) return null;
    const replacedSocketId =
      room.hostSocketId && room.hostSocketId !== socketId ? room.hostSocketId : null;
    if (replacedSocketId) this.sockets.delete(replacedSocketId);
    room.hostSocketId = socketId;
    this.sockets.set(socketId, { code, role: "host" });
    return { room, replacedSocketId };
  }

  addPlayer(code: string, name: string, socketId: string): AddPlayerResult {
    const room = this.rooms.get(code);
    if (!room) return { ok: false, reason: "NOT_FOUND" };
    if (room.players.length >= MAX_PLAYERS) return { ok: false, reason: "FULL" };
    const player: PlayerRecord = {
      id: randomUUID(),
      token: generateToken(),
      name,
      connected: true,
      socketId,
      privateNotes: [],
    };
    room.players.push(player);
    room.playStarted = true;
    this.sockets.set(socketId, { code, role: "player", playerId: player.id });
    return { ok: true, player, replacedSocketId: null };
  }

  attachPlayer(
    code: string,
    playerToken: string,
    socketId: string,
  ): { room: Room; player: PlayerRecord; replacedSocketId: string | null } | null {
    const room = this.rooms.get(code);
    if (!room) return null;
    const player = room.players.find((candidate) => candidate.token === playerToken);
    if (!player) return null;
    const replacedSocketId =
      player.socketId && player.socketId !== socketId ? player.socketId : null;
    if (replacedSocketId) this.sockets.delete(replacedSocketId);
    player.socketId = socketId;
    player.connected = true;
    this.sockets.set(socketId, { code, role: "player", playerId: player.id });
    return { room, player, replacedSocketId };
  }

  detachSocket(socketId: string): Room | null {
    const binding = this.sockets.get(socketId);
    if (!binding) return null;
    this.sockets.delete(socketId);
    const room = this.rooms.get(binding.code);
    if (!room) return null;
    if (binding.role === "host" && room.hostSocketId === socketId) {
      room.hostSocketId = null;
    }
    if (binding.role === "player" && binding.playerId) {
      const player = room.players.find((candidate) => candidate.id === binding.playerId);
      if (player && player.socketId === socketId) {
        player.socketId = null;
        player.connected = false;
      }
    }
    return room;
  }

  findPlayerBySocket(socketId: string): { room: Room; player: PlayerRecord } | null {
    const binding = this.sockets.get(socketId);
    if (!binding || binding.role !== "player" || !binding.playerId) return null;
    const room = this.rooms.get(binding.code);
    if (!room) return null;
    const player = room.players.find((candidate) => candidate.id === binding.playerId);
    if (!player || player.socketId !== socketId) return null;
    return { room, player };
  }

  recordAction(room: Room, player: PlayerRecord, intent: PlayerIntent): RecordedAction {
    const entry: TranscriptEntry = {
      id: randomUUID(),
      at: new Date().toISOString(),
      kind: "action",
      text: intent.text,
      playerName: player.name,
    };
    room.transcript.push(entry);
    trimTranscript(room);
    return { player, entry, intent };
  }

  applyResult(room: Room, result: GameMasterResult): GameMasterResult {
    const clean = sanitizeGameMasterResult(room, result);
    if (clean.narration.length > 0) {
      room.transcript.push(narrationEntry(clean.narration));
      trimTranscript(room);
    }
    const now = new Date().toISOString();
    for (const note of clean.privateNotes) {
      const player = room.players.find((candidate) => candidate.id === note.playerId);
      if (!player) continue;
      player.privateNotes.push({
        id: randomUUID(),
        at: now,
        text: note.text,
      });
      trimPrivateNotes(player);
    }
    return clean;
  }

  private allocateCode(): string {
    for (let attempt = 0; attempt < 20; attempt += 1) {
      const code = generateRoomCode();
      if (!this.rooms.has(code)) return code;
    }
    throw new Error("Could not allocate a room code");
  }
}

function narrationEntry(text: string): TranscriptEntry {
  return {
    id: randomUUID(),
    at: new Date().toISOString(),
    kind: "narration",
    text,
    playerName: null,
  };
}
