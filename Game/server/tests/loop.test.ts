import type { AddressInfo } from "node:net";
import { createServer } from "node:http";
import { Server } from "socket.io";
import { io as ioClient, type Socket } from "socket.io-client";
import { afterEach, describe, expect, it } from "vitest";
import {
  ClientEvents,
  ServerEvents,
  type HostReady,
  type PlayerReady,
  type PrivatePlayerState,
  type PublicRoomState,
  type SessionError,
} from "@ascension/shared";
import type {
  GameMaster,
  GameMasterActionContext,
  GameMasterOpeningView,
  GameMasterResult,
} from "../src/gameMaster/types.js";
import { UNDISCLOSED_FACT_CANARY, RoomStore } from "../src/rooms/store.js";
import { registerSockets } from "../src/socket/register.js";

class RecordingGameMaster implements GameMaster {
  readonly id = "recording";
  readonly views: GameMasterActionContext[] = [];
  private gate: (() => void) | null = null;
  holdNext = false;

  openScene(_view: GameMasterOpeningView): Promise<GameMasterResult> {
    return Promise.resolve({ narration: "Opening line.", privateNotes: [] });
  }

  async resolveAction(view: GameMasterActionContext): Promise<GameMasterResult> {
    this.views.push(view);
    if (this.holdNext) {
      this.holdNext = false;
      await new Promise<void>((resolve) => {
        this.gate = resolve;
      });
    }
    return {
      narration: `Echo ${view.action.text}`,
      privateNotes: [{ playerId: view.action.playerId, text: `ONLY_FOR_${view.action.playerName}` }],
    };
  }

  release(): void {
    this.gate?.();
    this.gate = null;
  }
}

interface Harness {
  url: string;
  gameMaster: RecordingGameMaster;
  close: () => Promise<void>;
}

async function startHarness(gameMaster = new RecordingGameMaster()): Promise<Harness> {
  const httpServer = createServer();
  const io = new Server(httpServer);
  registerSockets(io, new RoomStore(), gameMaster);
  await new Promise<void>((resolve) => {
    httpServer.listen(0, "127.0.0.1", resolve);
  });
  const address = httpServer.address() as AddressInfo;
  return {
    url: `http://127.0.0.1:${address.port}`,
    gameMaster,
    close: async () => {
      await io.close();
      if (httpServer.listening) {
        await new Promise<void>((resolve, reject) => {
          httpServer.close((error) => (error ? reject(error) : resolve()));
        });
      }
    },
  };
}

function connect(url: string): Socket {
  return ioClient(url, { transports: ["websocket"], forceNew: true });
}

function once<T>(socket: Socket, event: string): Promise<T> {
  return new Promise((resolve) => {
    socket.once(event, (payload: T) => resolve(payload));
  });
}

function whenConnected(socket: Socket): Promise<void> {
  if (socket.connected) return Promise.resolve();
  return once(socket, "connect");
}

describe("room loop", () => {
  const sockets: Socket[] = [];
  let harness: Harness | null = null;

  afterEach(async () => {
    for (const socket of sockets) socket.disconnect();
    sockets.length = 0;
    await harness?.close();
    harness = null;
  });

  it("takes a player action to the Game Master and keeps the private note on one phone", async () => {
    harness = await startHarness();
    const host = connect(harness.url);
    const alex = connect(harness.url);
    const jordan = connect(harness.url);
    sockets.push(host, alex, jordan);

    const hostReady = once<HostReady>(host, ServerEvents.hostReady);
    await whenConnected(host);
    host.emit(ClientEvents.hostCreate);
    const created = await hostReady;
    expect(created.state.phase).toBe("lobby");
    expect(created.state.transcript[0]?.text).toBe("Opening line.");
    expect(JSON.stringify(created.state)).not.toContain(created.hostToken);

    const alexReady = once<PlayerReady>(alex, ServerEvents.playerReady);
    await whenConnected(alex);
    alex.emit(ClientEvents.playerJoin, { code: created.state.code, name: "Alex" });
    const alexSeat = await alexReady;

    const jordanReady = once<PlayerReady>(jordan, ServerEvents.playerReady);
    await whenConnected(jordan);
    jordan.emit(ClientEvents.playerJoin, { code: created.state.code.toLowerCase(), name: "Jordan" });
    const jordanSeat = await jordanReady;
    expect(jordanSeat.state.seats.filled).toBe(2);

    const jordanPrivate: string[] = [];
    jordan.on(ServerEvents.privateState, (state: PrivatePlayerState) => {
      for (const note of state.notes) jordanPrivate.push(note.text);
    });

    const hostStates = collect<PublicRoomState>(host, ServerEvents.roomState);
    const alexPrivateNotes = collect<PrivatePlayerState>(alex, ServerEvents.privateState);

    alex.emit(ClientEvents.intentSubmit, {
      text: "I listen to the hum",
      source: "text",
    });

    await waitFor(
      () =>
        hostStates.some((state) => state.transcript.some((entry) => entry.text.startsWith("Echo "))) &&
        alexPrivateNotes.some((state) => state.notes.length > 0),
    );
    const state = hostStates.at(-1);
    const priv = alexPrivateNotes.at(-1);
    if (!state || !priv) throw new Error("missing room update");
    expect(state.transcript.map((entry) => entry.text)).toEqual([
      "Opening line.",
      "I listen to the hum",
      "Echo I listen to the hum",
    ]);
    expect(priv.notes.map((note) => note.text)).toEqual(["ONLY_FOR_Alex"]);
    expect(jordanPrivate).not.toContain("ONLY_FOR_Alex");
    expect(JSON.stringify(state)).not.toContain("ONLY_FOR_Alex");

    const view = harness.gameMaster.views[0];
    expect(view?.action.playerName).toBe("Alex");
    expect(view?.action.source).toBe("text");
    const serialized = JSON.stringify(harness.gameMaster.views);
    expect(serialized).not.toContain(UNDISCLOSED_FACT_CANARY);
    expect(serialized).not.toContain(created.hostToken);
    expect(serialized).not.toContain(alexSeat.playerToken);
    expect(serialized).not.toContain(jordanSeat.playerToken);

    alex.disconnect();
    await waitFor(
      () => hostStates.some((entry) => entry.players.some((player) => player.name === "Alex" && !player.connected)),
    );

    const again = connect(harness.url);
    sockets.push(again);
    const rejoined = once<PlayerReady>(again, ServerEvents.playerReady);
    await whenConnected(again);
    again.emit(ClientEvents.playerRejoin, {
      code: created.state.code,
      playerToken: alexSeat.playerToken,
    });
    const restored = await rejoined;
    expect(restored.playerId).toBe(alexSeat.playerId);
    expect(restored.privateState.notes.map((note) => note.text)).toEqual(["ONLY_FOR_Alex"]);
    expect(restored.state.players.find((player) => player.id === alexSeat.playerId)?.connected).toBe(
      true,
    );
  });

  it("resolves two actions in arrival order", async () => {
    const gameMaster = new RecordingGameMaster();
    gameMaster.holdNext = true;
    harness = await startHarness(gameMaster);
    const host = connect(harness.url);
    const phone = connect(harness.url);
    sockets.push(host, phone);

    const hostReady = once<HostReady>(host, ServerEvents.hostReady);
    await whenConnected(host);
    host.emit(ClientEvents.hostCreate);
    const created = await hostReady;

    const ready = once<PlayerReady>(phone, ServerEvents.playerReady);
    await whenConnected(phone);
    phone.emit(ClientEvents.playerJoin, { code: created.state.code, name: "Alex" });
    await ready;

    phone.emit(ClientEvents.intentSubmit, { text: "first", source: "text" });
    await waitFor(() => gameMaster.views.length === 1);
    phone.emit(ClientEvents.intentSubmit, { text: "second", source: "speech" });
    await delay(40);
    expect(gameMaster.views.map((view) => view.action.text)).toEqual(["first"]);

    const done = waitForPublic(host, (state) =>
      state.transcript.some((entry) => entry.text === "Echo second"),
    );
    gameMaster.release();
    const state = await done;
    expect(state.transcript.map((entry) => entry.text)).toEqual([
      "Opening line.",
      "first",
      "Echo first",
      "second",
      "Echo second",
    ]);
    expect(gameMaster.views.map((view) => view.action.source)).toEqual(["text", "speech"]);
  });

  it("rejects a seventh player and a missing room", async () => {
    harness = await startHarness();
    const host = connect(harness.url);
    sockets.push(host);
    const hostReady = once<HostReady>(host, ServerEvents.hostReady);
    await whenConnected(host);
    host.emit(ClientEvents.hostCreate);
    const created = await hostReady;

    for (let index = 0; index < 6; index += 1) {
      const phone = connect(harness.url);
      sockets.push(phone);
      const ready = once<PlayerReady>(phone, ServerEvents.playerReady);
      await whenConnected(phone);
      phone.emit(ClientEvents.playerJoin, { code: created.state.code, name: `P${index}` });
      await ready;
    }

    const extra = connect(harness.url);
    sockets.push(extra);
    const error = once<SessionError>(extra, ServerEvents.sessionError);
    await whenConnected(extra);
    extra.emit(ClientEvents.playerJoin, { code: created.state.code, name: "Extra" });
    expect((await error).code).toBe("ROOM_FULL");

    const stranger = connect(harness.url);
    sockets.push(stranger);
    const missing = once<SessionError>(stranger, ServerEvents.sessionError);
    await whenConnected(stranger);
    stranger.emit(ClientEvents.playerJoin, { code: "ABCDEF", name: "Pat" });
    expect((await missing).code).toBe("ROOM_NOT_FOUND");
  });
});

function collect<T>(socket: Socket, event: string): T[] {
  const items: T[] = [];
  socket.on(event, (payload: T) => {
    items.push(payload);
  });
  return items;
}

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function waitFor(predicate: () => boolean): Promise<void> {
  const start = Date.now();
  while (!predicate()) {
    if (Date.now() - start > 2000) throw new Error("timed out waiting");
    await delay(10);
  }
}

function waitForPublic(
  socket: Socket,
  predicate: (state: PublicRoomState) => boolean,
): Promise<PublicRoomState> {
  return new Promise((resolve) => {
    const onState = (state: PublicRoomState): void => {
      if (!predicate(state)) return;
      socket.off(ServerEvents.roomState, onState);
      resolve(state);
    };
    socket.on(ServerEvents.roomState, onState);
  });
}
