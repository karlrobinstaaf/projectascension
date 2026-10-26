import type { PlayerIntent, PrivateNote, SceneLabel, TranscriptEntry } from "@ascension/shared";

export interface PlayerRecord {
  id: string;
  token: string;
  name: string;
  connected: boolean;
  socketId: string | null;
  privateNotes: PrivateNote[];
}

/**
 * Facts the room owns and does not disclose.
 * `toPublicState` and `toGameMasterActionContext` must not read this.
 */
export interface ServerOnlyState {
  undisclosedFact: string;
}

export interface Room {
  code: string;
  hostToken: string;
  hostSocketId: string | null;
  scene: SceneLabel;
  players: PlayerRecord[];
  transcript: TranscriptEntry[];
  serverOnly: ServerOnlyState;
  /** Set when the first human takes a seat. Stays on if they disconnect. */
  playStarted: boolean;
}

export interface SocketBinding {
  code: string;
  role: "host" | "player";
  playerId?: string;
}

export interface RecordedAction {
  player: PlayerRecord;
  entry: TranscriptEntry;
  intent: PlayerIntent;
}
