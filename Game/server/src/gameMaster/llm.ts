import { GameMasterNotImplementedError } from "./errors.js";
import type {
  GameMaster,
  GameMasterActionContext,
  GameMasterOpeningView,
  GameMasterResult,
} from "./types.js";

export const LLM_GAME_MASTER_ID = "llm-stub";

export interface LlmGameMasterOptions {
  apiKey?: string | undefined;
  model?: string | undefined;
  baseUrl?: string | undefined;
}

/**
 * Placeholder for a real provider.
 *
 * A future implementation must accept only `GameMasterOpeningView` and
 * `GameMasterActionContext`. It must not be given the room, tokens, or
 * server-only world facts. This stub never calls the network.
 */
export class LlmGameMaster implements GameMaster {
  readonly id = LLM_GAME_MASTER_ID;

  constructor(private readonly options: LlmGameMasterOptions) {}

  openScene(_view: GameMasterOpeningView): Promise<GameMasterResult> {
    return this.unimplemented();
  }

  resolveAction(_view: GameMasterActionContext): Promise<GameMasterResult> {
    return this.unimplemented();
  }

  private unimplemented(): Promise<GameMasterResult> {
    const model = this.options.model ?? "(unset)";
    const key = this.options.apiKey ? "set" : "unset";
    return Promise.reject(
      new GameMasterNotImplementedError(
        `The LLM Game Master is a stub and does not call a provider (model ${model}, API key ${key}). Set GAMEMASTER_PROVIDER=mock.`,
      ),
    );
  }
}
