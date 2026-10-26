import { MAX_PLAYERS } from "./limits.js";

export const ClientEvents = {
  hostCreate: "host:create",
  hostRejoin: "host:rejoin",
  playerJoin: "player:join",
  playerRejoin: "player:rejoin",
  intentSubmit: "intent:submit",
} as const;

export const ServerEvents = {
  hostReady: "host:ready",
  playerReady: "player:ready",
  roomState: "room:state",
  privateState: "private:state",
  sessionError: "session:error",
} as const;

export type IntentSource = "text" | "speech";

/** What a player submits. Speech engines must produce this same shape. */
export interface PlayerIntent {
  text: string;
  source: IntentSource;
}

export interface SceneLabel {
  locationLabel: string;
  timeLabel: string;
}

export interface PublicPlayer {
  id: string;
  name: string;
  connected: boolean;
}

export interface TranscriptEntry {
  id: string;
  at: string;
  kind: "narration" | "action";
  text: string;
  playerName: string | null;
}

/** State that may be shown on the shared television and to every phone. */
export interface PublicRoomState {
  code: string;
  phase: "lobby" | "in_play";
  scene: SceneLabel;
  players: PublicPlayer[];
  transcript: TranscriptEntry[];
  seats: { filled: number; capacity: typeof MAX_PLAYERS };
}

export interface PrivateNote {
  id: string;
  at: string;
  text: string;
}

/** State delivered only to the phone that owns it. */
export interface PrivatePlayerState {
  playerId: string;
  notes: PrivateNote[];
}

export interface HostReady {
  hostToken: string;
  state: PublicRoomState;
}

export interface PlayerReady {
  playerId: string;
  playerToken: string;
  state: PublicRoomState;
  privateState: PrivatePlayerState;
}

export interface HostRejoinPayload {
  code: string;
  hostToken: string;
}

export interface PlayerJoinPayload {
  code: string;
  name: string;
}

export interface PlayerRejoinPayload {
  code: string;
  playerToken: string;
}

export type SessionErrorCode =
  | "ROOM_NOT_FOUND"
  | "ROOM_FULL"
  | "INVALID_NAME"
  | "INVALID_CODE"
  | "INVALID_INTENT"
  | "NOT_IN_ROOM"
  | "REJOIN_FAILED"
  | "GM_UNAVAILABLE"
  | "REPLACED";

export interface SessionError {
  code: SessionErrorCode;
  message: string;
}

export interface HostInfo {
  lanAddresses: string[];
  gameMaster: string;
}
