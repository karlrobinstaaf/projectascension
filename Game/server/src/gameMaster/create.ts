import { LlmGameMaster } from "./llm.js";
import { MockGameMaster } from "./mock.js";
import type { GameMaster } from "./types.js";

export interface GameMasterEnv {
  GAMEMASTER_PROVIDER?: string | undefined;
  GAMEMASTER_API_KEY?: string | undefined;
  GAMEMASTER_MODEL?: string | undefined;
  GAMEMASTER_BASE_URL?: string | undefined;
}

/** `mock` is the default so a session runs with no API key. */
export function createGameMaster(env: GameMasterEnv): GameMaster {
  const provider = (env.GAMEMASTER_PROVIDER ?? "mock").trim().toLowerCase();
  if (provider === "" || provider === "mock") {
    return new MockGameMaster();
  }
  if (provider === "llm") {
    return new LlmGameMaster({
      apiKey: env.GAMEMASTER_API_KEY,
      model: env.GAMEMASTER_MODEL,
      baseUrl: env.GAMEMASTER_BASE_URL,
    });
  }
  throw new Error(
    `Unknown GAMEMASTER_PROVIDER "${env.GAMEMASTER_PROVIDER}". Expected "mock" or "llm".`,
  );
}
