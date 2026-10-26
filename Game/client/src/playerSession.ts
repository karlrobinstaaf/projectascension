import {
  ClientEvents,
  ServerEvents,
  type PlayerIntent,
  type PlayerReady,
  type PrivatePlayerState,
  type PublicRoomState,
  type SessionError,
} from "@ascension/shared";
import { io, type Socket } from "socket.io-client";
import { clearPlayerSession, loadPlayerSession, savePlayerSession } from "./storage";

export interface PlayerSnapshot {
  connection: "connecting" | "live" | "reconnecting";
  state: PublicRoomState | null;
  privateState: PrivatePlayerState | null;
  playerId: string | null;
  name: string | null;
  error: string | null;
  pending: boolean;
  yielded: boolean;
}

const listeners = new Set<() => void>();

let snapshot: PlayerSnapshot = {
  connection: "connecting",
  state: null,
  privateState: null,
  playerId: null,
  name: loadPlayerSession()?.name ?? null,
  error: null,
  pending: false,
  yielded: false,
};

let socket: Socket | null = null;
let started = false;
let pendingJoin: { code: string; name: string } | null = null;
let seenOwnActions = 0;
let inflight = false;

function publish(patch: Partial<PlayerSnapshot>): void {
  snapshot = { ...snapshot, ...patch };
  for (const listener of listeners) listener();
}

function ownActionCount(state: PublicRoomState, name: string | null): number {
  if (!name) return 0;
  return state.transcript.filter((entry) => entry.kind === "action" && entry.playerName === name)
    .length;
}

export function startPlayer(): void {
  if (started) return;
  started = true;
  socket = io({ transports: ["websocket", "polling"] });

  socket.on("connect", () => {
    if (snapshot.yielded) return;
    publish({ connection: "live" });
    if (pendingJoin) {
      socket?.emit(ClientEvents.playerJoin, pendingJoin);
      return;
    }
    const saved = loadPlayerSession();
    if (saved) socket?.emit(ClientEvents.playerRejoin, saved);
  });

  socket.on("disconnect", () => {
    if (!snapshot.yielded) publish({ connection: "reconnecting" });
  });

  socket.on(ServerEvents.playerReady, (payload: PlayerReady) => {
    pendingJoin = null;
    const name =
      payload.state.players.find((player) => player.id === payload.playerId)?.name ??
      snapshot.name;
    savePlayerSession({
      code: payload.state.code,
      playerToken: payload.playerToken,
      name: name ?? "Player",
    });
    seenOwnActions = ownActionCount(payload.state, name);
    inflight = false;
    publish({
      state: payload.state,
      privateState: payload.privateState,
      playerId: payload.playerId,
      name,
      error: null,
      pending: false,
      connection: "live",
    });
  });

  socket.on(ServerEvents.roomState, (state: PublicRoomState) => {
    const count = ownActionCount(state, snapshot.name);
    const landed = inflight && count > seenOwnActions;
    seenOwnActions = count;
    if (landed) inflight = false;
    publish({ state, pending: landed ? false : snapshot.pending });
  });

  socket.on(ServerEvents.privateState, (privateState: PrivatePlayerState) => {
    if (snapshot.playerId && privateState.playerId !== snapshot.playerId) return;
    publish({ privateState });
  });

  socket.on(ServerEvents.sessionError, (error: SessionError) => {
    inflight = false;
    if (error.code === "REPLACED") {
      clearPlayerSession();
      publish({
        yielded: true,
        error: error.message,
        pending: false,
        playerId: null,
        privateState: null,
      });
      socket?.io.reconnection(false);
      socket?.disconnect();
      return;
    }
    if (error.code === "REJOIN_FAILED") {
      clearPlayerSession();
      publish({
        error: error.message,
        pending: false,
        playerId: null,
        name: null,
        state: null,
        privateState: null,
      });
      return;
    }
    publish({ error: error.message, pending: false });
  });
}

export function joinRoom(code: string, name: string): void {
  startPlayer();
  pendingJoin = { code, name };
  publish({ error: null, pending: true, name });
  if (socket?.connected && !snapshot.yielded) {
    socket.emit(ClientEvents.playerJoin, { code, name });
  }
}

export function submitIntent(intent: PlayerIntent): void {
  if (!socket?.connected || snapshot.yielded) {
    publish({ error: "Not connected to the room." });
    return;
  }
  inflight = true;
  publish({ pending: true, error: null });
  socket.emit(ClientEvents.intentSubmit, intent);
}

export function subscribePlayer(listener: () => void): () => void {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

export function getPlayerSnapshot(): PlayerSnapshot {
  return snapshot;
}
