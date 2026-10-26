import {
  MAX_INTENT_LENGTH,
  MAX_PLAYER_NAME_LENGTH,
  ROOM_CODE_ALPHABET,
  ROOM_CODE_LENGTH,
  type PlayerIntent,
} from "@ascension/shared";

export function parsePlayerName(input: unknown): string | null {
  if (typeof input !== "string") return null;
  const collapsed = input.trim().replace(/\s+/g, " ");
  if (collapsed.length < 1 || collapsed.length > MAX_PLAYER_NAME_LENGTH) return null;
  if (!/^[\p{L}\p{N}][\p{L}\p{N} '’-]*$/u.test(collapsed)) return null;
  return collapsed;
}

export function parseRoomCode(input: unknown): string | null {
  if (typeof input !== "string") return null;
  const code = input.trim().toUpperCase().replace(/[\s-]/g, "");
  if (code.length !== ROOM_CODE_LENGTH) return null;
  if (![...code].every((character) => ROOM_CODE_ALPHABET.includes(character))) return null;
  return code;
}

export function parseIntent(input: unknown): PlayerIntent | null {
  if (!input || typeof input !== "object") return null;
  const record = input as Record<string, unknown>;
  const { text, source } = record;
  if (typeof text !== "string") return null;
  if (source !== "text" && source !== "speech") return null;
  const cleaned = stripControlCharacters(text).trim();
  if (cleaned.length < 1 || cleaned.length > MAX_INTENT_LENGTH) return null;
  return { text: cleaned, source };
}

function stripControlCharacters(text: string): string {
  let cleaned = "";
  for (const character of text) {
    const code = character.codePointAt(0) ?? 0;
    const isControl =
      code <= 8 || code === 11 || code === 12 || (code >= 14 && code <= 31) || code === 127;
    if (!isControl) cleaned += character;
  }
  return cleaned;
}

export function readStringField(input: unknown, key: string): string | null {
  if (!input || typeof input !== "object") return null;
  const value = (input as Record<string, unknown>)[key];
  return typeof value === "string" ? value : null;
}
