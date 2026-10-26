import { MAX_PLAYERS, type PlayerIntent, type PrivatePlayerState, type PublicRoomState } from "@ascension/shared";
import type {
  GameMasterActionContext,
  GameMasterOpeningView,
  GameMasterPlayerRef,
  GameMasterResult,
  GameMasterSceneView,
} from "../gameMaster/types.js";
import type { PlayerRecord, Room } from "./types.js";

const TRANSCRIPT_LIMIT = 80;
const PRIVATE_NOTE_LIMIT = 40;

function playerRefs(room: Room): GameMasterPlayerRef[] {
  return room.players.map((player) => ({ id: player.id, name: player.name }));
}

function sceneView(room: Room): GameMasterSceneView {
  return {
    locationLabel: room.scene.locationLabel,
    timeLabel: room.scene.timeLabel,
    sharedNarration: room.transcript
      .filter((entry) => entry.kind === "narration")
      .map((entry) => entry.text),
  };
}

/**
 * The only object the Game Master may read before anyone has acted.
 * Built by copying fields. The room itself is never passed across this function.
 */
export function toGameMasterOpeningView(room: Room): GameMasterOpeningView {
  return {
    scene: sceneView(room),
    players: playerRefs(room),
  };
}

/**
 * The only object the Game Master may read for one action.
 * Other players' private notes, tokens, and `serverOnly` are not copied.
 */
export function toGameMasterActionContext(
  room: Room,
  player: PlayerRecord,
  intent: PlayerIntent,
): GameMasterActionContext {
  return {
    scene: sceneView(room),
    players: playerRefs(room),
    action: {
      playerId: player.id,
      playerName: player.name,
      text: intent.text,
      source: intent.source,
      priorPrivateNotes: player.privateNotes.map((note) => note.text),
    },
  };
}

export function toPublicState(room: Room): PublicRoomState {
  return {
    code: room.code,
    phase: room.playStarted ? "in_play" : "lobby",
    scene: {
      locationLabel: room.scene.locationLabel,
      timeLabel: room.scene.timeLabel,
    },
    players: room.players.map((player) => ({
      id: player.id,
      name: player.name,
      connected: player.connected,
    })),
    transcript: room.transcript.map((entry) => ({
      id: entry.id,
      at: entry.at,
      kind: entry.kind,
      text: entry.text,
      playerName: entry.playerName,
    })),
    seats: { filled: room.players.length, capacity: MAX_PLAYERS },
  };
}

export function toPrivateState(player: PlayerRecord): PrivatePlayerState {
  return {
    playerId: player.id,
    notes: player.privateNotes.map((note) => ({
      id: note.id,
      at: note.at,
      text: note.text,
    })),
  };
}

/** Drops private notes aimed at a player id that is not in the room. */
export function sanitizeGameMasterResult(room: Room, result: GameMasterResult): GameMasterResult {
  const ids = new Set(room.players.map((player) => player.id));
  return {
    narration: result.narration.trim(),
    privateNotes: result.privateNotes
      .filter((note) => ids.has(note.playerId) && note.text.trim().length > 0)
      .map((note) => ({ playerId: note.playerId, text: note.text.trim() })),
  };
}

export function trimTranscript(room: Room): void {
  if (room.transcript.length > TRANSCRIPT_LIMIT) {
    room.transcript.splice(0, room.transcript.length - TRANSCRIPT_LIMIT);
  }
}

export function trimPrivateNotes(player: PlayerRecord): void {
  if (player.privateNotes.length > PRIVATE_NOTE_LIMIT) {
    player.privateNotes.splice(0, player.privateNotes.length - PRIVATE_NOTE_LIMIT);
  }
}
