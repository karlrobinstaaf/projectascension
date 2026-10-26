import { describe, expect, it } from "vitest";
import { MAX_PLAYERS } from "@ascension/shared";
import {
  PLACEHOLDER_SCENE,
  RoomStore,
  UNDISCLOSED_FACT_CANARY,
} from "../src/rooms/store.js";
import { toGameMasterActionContext, toPrivateState, toPublicState } from "../src/rooms/view.js";

function seatedRoom(): { store: RoomStore; code: string; hostToken: string } {
  const store = new RoomStore();
  const room = store.create("host-socket", "The road is dark.");
  return { store, code: room.code, hostToken: room.hostToken };
}

describe("RoomStore", () => {
  it("opens a room with a host, a scene, and no players", () => {
    const { store, code } = seatedRoom();
    const room = store.get(code);
    expect(room?.players).toEqual([]);
    expect(room?.scene).toEqual(PLACEHOLDER_SCENE);
    expect(room?.playStarted).toBe(false);
    expect(room?.transcript[0]?.text).toBe("The road is dark.");
    expect(toPublicState(room!).phase).toBe("lobby");
  });

  it("seats at most six players and keeps a disconnected seat", () => {
    const { store, code } = seatedRoom();
    const ids: string[] = [];
    for (let index = 0; index < MAX_PLAYERS; index += 1) {
      const joined = store.addPlayer(code, `Player ${index + 1}`, `sock-${index}`);
      expect(joined.ok).toBe(true);
      if (joined.ok) ids.push(joined.player.id);
    }
    expect(store.addPlayer(code, "Extra", "sock-extra")).toEqual({ ok: false, reason: "FULL" });

    const room = store.get(code);
    expect(room?.playStarted).toBe(true);
    expect(toPublicState(room!).seats).toEqual({ filled: 6, capacity: 6 });

    store.detachSocket("sock-0");
    expect(store.get(code)?.players).toHaveLength(6);
    expect(store.get(code)?.players[0]?.connected).toBe(false);
    expect(store.addPlayer(code, "Still extra", "sock-extra")).toEqual({
      ok: false,
      reason: "FULL",
    });

    const token = store.get(code)?.players[0]?.token;
    const rejoined = store.attachPlayer(code, token ?? "", "sock-0b");
    expect(rejoined?.player.id).toBe(ids[0]);
    expect(rejoined?.player.connected).toBe(true);
    expect(rejoined?.replacedSocketId).toBeNull();
  });

  it("rejects a rejoin token from another room", () => {
    const first = new RoomStore();
    const room = first.create("host", "Open.");
    const joined = first.addPlayer(room.code, "Alex", "a");
    expect(joined.ok).toBe(true);
    if (!joined.ok) return;
    expect(first.attachPlayer("ZZZZZZ", joined.player.token, "b")).toBeNull();
    expect(first.attachHost(room.code, "nope", "host-2")).toBeNull();
  });

  it("keeps private notes on one player and drops notes for unknown ids", () => {
    const { store, code } = seatedRoom();
    const alex = store.addPlayer(code, "Alex", "alex");
    const jordan = store.addPlayer(code, "Jordan", "jordan");
    expect(alex.ok && jordan.ok).toBe(true);
    if (!alex.ok || !jordan.ok) return;
    const room = store.get(code);
    if (!room) throw new Error("missing room");

    store.applyResult(room, {
      narration: "A hum.",
      privateNotes: [
        { playerId: alex.player.id, text: "Backup power." },
        { playerId: "missing", text: "Should vanish." },
        { playerId: jordan.player.id, text: "   " },
      ],
    });

    expect(toPrivateState(alex.player).notes.map((note) => note.text)).toEqual(["Backup power."]);
    expect(toPrivateState(jordan.player).notes).toEqual([]);
    expect(JSON.stringify(toPublicState(room))).not.toContain("Backup power.");
  });
});

describe("Game Master view", () => {
  it("copies only the explicit fields and omits hidden state", () => {
    const { store, code, hostToken } = seatedRoom();
    const alex = store.addPlayer(code, "Alex", "alex");
    const jordan = store.addPlayer(code, "Jordan", "jordan");
    if (!alex.ok || !jordan.ok) throw new Error("join failed");
    const room = store.get(code);
    if (!room) throw new Error("missing room");

    store.applyResult(room, {
      narration: "Shared.",
      privateNotes: [
        { playerId: alex.player.id, text: "Alex only." },
        { playerId: jordan.player.id, text: "Jordan only." },
      ],
    });

    const view = toGameMasterActionContext(room, alex.player, {
      text: "I listen to the hum",
      source: "text",
    });

    expect(Object.keys(view).sort()).toEqual(["action", "players", "scene"]);
    expect(Object.keys(view.scene).sort()).toEqual([
      "locationLabel",
      "sharedNarration",
      "timeLabel",
    ]);
    expect(Object.keys(view.action).sort()).toEqual([
      "playerId",
      "playerName",
      "priorPrivateNotes",
      "source",
      "text",
    ]);
    expect(view.players.every((player) => Object.keys(player).sort().join() === "id,name")).toBe(
      true,
    );
    expect(view.action.priorPrivateNotes).toEqual(["Alex only."]);
    expect(view.scene.sharedNarration).toEqual(["The road is dark.", "Shared."]);

    const serialized = JSON.stringify(view);
    expect(serialized).not.toContain(UNDISCLOSED_FACT_CANARY);
    expect(serialized).not.toContain(hostToken);
    expect(serialized).not.toContain(alex.player.token);
    expect(serialized).not.toContain(jordan.player.token);
    expect(serialized).not.toContain("Jordan only.");

    const pub = JSON.stringify(toPublicState(room));
    expect(Object.keys(toPublicState(room)).sort()).toEqual([
      "code",
      "phase",
      "players",
      "scene",
      "seats",
      "transcript",
    ]);
    expect(pub).not.toContain(UNDISCLOSED_FACT_CANARY);
    expect(pub).not.toContain(hostToken);
    expect(pub).not.toContain(alex.player.token);
    expect(pub).not.toContain("Alex only.");
  });
});
