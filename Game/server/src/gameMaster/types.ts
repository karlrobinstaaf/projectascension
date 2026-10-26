import type { IntentSource } from "@ascension/shared";

/**
 * Explicit view handed to the Game Master.
 *
 * The server builds this in `rooms/view.ts`. A Game Master implementation
 * must not import the room store, sockets, player tokens, or server-only
 * world facts. If a fact is not a field on these types, the model does not
 * receive it. Adding a field is a decision to disclose that fact.
 */

export interface GameMasterSceneView {
  locationLabel: string;
  timeLabel: string;
  /** Shared narration already on the television, oldest first. */
  sharedNarration: string[];
}

export interface GameMasterPlayerRef {
  id: string;
  name: string;
}

export interface GameMasterActionView {
  playerId: string;
  playerName: string;
  text: string;
  source: IntentSource;
  /**
   * Private notes already given to the acting player, and only that player.
   * Passed back so a future model can stay consistent with what it told them.
   */
  priorPrivateNotes: string[];
}

export interface GameMasterOpeningView {
  scene: GameMasterSceneView;
  players: GameMasterPlayerRef[];
}

export interface GameMasterActionContext {
  scene: GameMasterSceneView;
  players: GameMasterPlayerRef[];
  action: GameMasterActionView;
}

export interface GameMasterPrivateNote {
  playerId: string;
  text: string;
}

export interface GameMasterResult {
  /** Shared narration for the television. */
  narration: string;
  /** Notes routed only to the named player's phone. */
  privateNotes: GameMasterPrivateNote[];
}

export interface GameMaster {
  readonly id: string;
  openScene(view: GameMasterOpeningView): Promise<GameMasterResult>;
  resolveAction(view: GameMasterActionContext): Promise<GameMasterResult>;
}
