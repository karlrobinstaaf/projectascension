import { describe, expect, it, vi } from "vitest";
import { createGameMaster } from "../src/gameMaster/create.js";
import { GameMasterNotImplementedError } from "../src/gameMaster/errors.js";
import { LlmGameMaster } from "../src/gameMaster/llm.js";
import { MOCK_OPENING_NARRATION, MockGameMaster } from "../src/gameMaster/mock.js";
import type { GameMasterActionContext, GameMasterOpeningView } from "../src/gameMaster/types.js";

const opening: GameMasterOpeningView = {
  scene: {
    locationLabel: "Edge of town",
    timeLabel: "After dark",
    sharedNarration: [],
  },
  players: [],
};

function action(text: string, name = "Alex"): GameMasterActionContext {
  return {
    scene: {
      locationLabel: "Edge of town",
      timeLabel: "After dark",
      sharedNarration: [MOCK_OPENING_NARRATION],
    },
    players: [{ id: "p1", name }],
    action: {
      playerId: "p1",
      playerName: name,
      text,
      source: "text",
      priorPrivateNotes: [],
    },
  };
}

describe("MockGameMaster", () => {
  it("returns the same opening every time", async () => {
    const gameMaster = new MockGameMaster();
    const first = await gameMaster.openScene(opening);
    const second = await gameMaster.openScene(opening);
    expect(first).toEqual({ narration: MOCK_OPENING_NARRATION, privateNotes: [] });
    expect(second).toEqual(first);
  });

  it("is deterministic and can address a private note to the actor only", async () => {
    const gameMaster = new MockGameMaster();
    const listen = action("I listen to the hum behind the diner");
    const first = await gameMaster.resolveAction(listen);
    const second = await gameMaster.resolveAction(listen);
    expect(second).toEqual(first);
    expect(first.narration.toLowerCase()).toContain("hum");
    expect(first.privateNotes).toHaveLength(1);
    expect(first.privateNotes[0]?.playerId).toBe("p1");
    expect(first.privateNotes[0]?.text.toLowerCase()).toContain("backup power");

    const waiting = await gameMaster.resolveAction(action("I wait in the car"));
    expect(waiting.privateNotes).toEqual([]);
    expect(waiting.narration).not.toEqual(first.narration);

    const spoken = action("I check the glove box");
    const fallbackA = await gameMaster.resolveAction(spoken);
    const fallbackB = await gameMaster.resolveAction(spoken);
    expect(fallbackB).toEqual(fallbackA);
    expect(fallbackA.narration).toContain("I check the glove box");
  });
});

describe("LlmGameMaster", () => {
  it("does not call the network", async () => {
    const fetchSpy = vi.spyOn(globalThis, "fetch");
    const gameMaster = new LlmGameMaster({ model: "example", apiKey: undefined });
    await expect(gameMaster.openScene(opening)).rejects.toBeInstanceOf(
      GameMasterNotImplementedError,
    );
    await expect(gameMaster.resolveAction(action("hello"))).rejects.toThrow(/does not call a provider/);
    expect(fetchSpy).not.toHaveBeenCalled();
    fetchSpy.mockRestore();
  });
});

describe("createGameMaster", () => {
  it("defaults to the mock and selects the stub from the env", () => {
    expect(createGameMaster({}).id).toBe("mock");
    expect(createGameMaster({ GAMEMASTER_PROVIDER: "llm", GAMEMASTER_MODEL: "example" }).id).toBe(
      "llm-stub",
    );
    expect(() => createGameMaster({ GAMEMASTER_PROVIDER: "other" })).toThrow(/unknown/i);
  });
});
