export class GameMasterNotImplementedError extends Error {
  readonly code = "GM_NOT_IMPLEMENTED" as const;

  constructor(message: string) {
    super(message);
    this.name = "GameMasterNotImplementedError";
  }
}
