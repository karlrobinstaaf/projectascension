import {
  ClientEvents,
  ServerEvents,
  type HostInfo,
  type HostReady,
  type PublicRoomState,
  type SessionError,
} from "@ascension/shared";
import { io, type Socket } from "socket.io-client";
import { clearHostSession, loadHostSession, saveHostSession } from "./storage";

export interface TvSnapshot {
  connection: "connecting" | "live" | "reconnecting";
  state: PublicRoomState | null;
  error: string | null;
  lanAddresses: string[];
  yielded: boolean;
}

const listeners = new Set<() => void>();

let snapshot: TvSnapshot = {
  connection: "connecting",
  state: null,
  error: null,
  lanAddresses: [],
  yielded: false,
};

let socket: Socket | null = null;
let started = false;
let openingRoom = false;

function publish(patch: Partial<TvSnapshot>): void {
  snapshot = { ...snapshot, ...patch };
  for (const listener of listeners) listener();
}

export function startTv(): void {
  if (started) return;
  started = true;
  socket = io({ transports: ["websocket", "polling"] });

  socket.on("connect", () => {
    if (snapshot.yielded) return;
    publish({ connection: "live", error: null });
    const saved = loadHostSession();
    if (saved) {
      openingRoom = false;
      socket?.emit(ClientEvents.hostRejoin, saved);
      return;
    }
    if (openingRoom) return;
    openingRoom = true;
    socket?.emit(ClientEvents.hostCreate);
  });

  socket.on("disconnect", () => {
    if (!snapshot.yielded) publish({ connection: "reconnecting" });
  });

  socket.on(ServerEvents.hostReady, (payload: HostReady) => {
    openingRoom = false;
    saveHostSession({ code: payload.state.code, hostToken: payload.hostToken });
    publish({ state: payload.state, error: null, connection: "live" });
  });

  socket.on(ServerEvents.roomState, (state: PublicRoomState) => {
    publish({ state });
  });

  socket.on(ServerEvents.sessionError, (error: SessionError) => {
    if (error.code === "REPLACED") {
      publish({ yielded: true, error: error.message, connection: "reconnecting" });
      socket?.io.reconnection(false);
      socket?.disconnect();
      return;
    }
    if (error.code === "REJOIN_FAILED") {
      clearHostSession();
      openingRoom = true;
      socket?.emit(ClientEvents.hostCreate);
      return;
    }
    openingRoom = false;
    publish({ error: error.message });
  });

  void fetch("/host-info")
    .then((response) => response.json() as Promise<HostInfo>)
    .then((info) => {
      publish({ lanAddresses: info.lanAddresses });
    })
    .catch(() => undefined);
}

export function openNewRoom(): void {
  clearHostSession();
  window.location.assign("/tv");
}

export function subscribeTv(listener: () => void): () => void {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}

export function getTvSnapshot(): TvSnapshot {
  return snapshot;
}
