const HOST_KEY = "ascension.host";
const PLAYER_KEY = "ascension.player";

export interface HostSession {
  code: string;
  hostToken: string;
}

export interface PlayerSession {
  code: string;
  playerToken: string;
  name: string;
}

function read(key: string): unknown {
  try {
    const raw = localStorage.getItem(key);
    if (!raw) return null;
    return JSON.parse(raw) as unknown;
  } catch {
    return null;
  }
}

function write(key: string, value: unknown): void {
  localStorage.setItem(key, JSON.stringify(value));
}

export function loadHostSession(): HostSession | null {
  const value = read(HOST_KEY);
  if (!value || typeof value !== "object") return null;
  const record = value as Record<string, unknown>;
  if (typeof record.code !== "string" || typeof record.hostToken !== "string") return null;
  return { code: record.code, hostToken: record.hostToken };
}

export function saveHostSession(session: HostSession): void {
  write(HOST_KEY, session);
}

export function clearHostSession(): void {
  localStorage.removeItem(HOST_KEY);
}

export function loadPlayerSession(): PlayerSession | null {
  const value = read(PLAYER_KEY);
  if (!value || typeof value !== "object") return null;
  const record = value as Record<string, unknown>;
  if (
    typeof record.code !== "string" ||
    typeof record.playerToken !== "string" ||
    typeof record.name !== "string"
  ) {
    return null;
  }
  return { code: record.code, playerToken: record.playerToken, name: record.name };
}

export function savePlayerSession(session: PlayerSession): void {
  write(PLAYER_KEY, session);
}

export function clearPlayerSession(): void {
  localStorage.removeItem(PLAYER_KEY);
}
