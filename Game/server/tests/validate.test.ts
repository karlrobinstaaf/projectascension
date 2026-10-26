import { describe, expect, it } from "vitest";
import { ROOM_CODE_ALPHABET } from "@ascension/shared";
import { generateRoomCode } from "../src/rooms/codes.js";
import { parseIntent, parsePlayerName, parseRoomCode } from "../src/rooms/validate.js";

describe("parsePlayerName", () => {
  it("accepts ordinary names, including non-English letters", () => {
    expect(parsePlayerName("  Åsa  ")).toBe("Åsa");
    expect(parsePlayerName("Mary-Jane")).toBe("Mary-Jane");
    expect(parsePlayerName("O'Neil")).toBe("O'Neil");
  });

  it("rejects empty, oversized, and symbolic names", () => {
    expect(parsePlayerName("")).toBeNull();
    expect(parsePlayerName("   ")).toBeNull();
    expect(parsePlayerName("x".repeat(25))).toBeNull();
    expect(parsePlayerName("nope@home")).toBeNull();
    expect(parsePlayerName(12)).toBeNull();
  });
});

describe("parseRoomCode", () => {
  it("normalizes spacing and case", () => {
    expect(parseRoomCode("k7mp2q")).toBe("K7MP2Q");
    expect(parseRoomCode("k7 mp-2q")).toBe("K7MP2Q");
  });

  it("rejects ambiguous characters and the wrong length", () => {
    expect(parseRoomCode("O0OOOO")).toBeNull();
    expect(parseRoomCode("I1IIII")).toBeNull();
    expect(parseRoomCode("ABC")).toBeNull();
    expect(parseRoomCode("ABCDEFG")).toBeNull();
  });
});

describe("parseIntent", () => {
  it("keeps text and speech on the same shape", () => {
    expect(parseIntent({ text: " I wait. ", source: "text" })).toEqual({
      text: "I wait.",
      source: "text",
    });
    expect(parseIntent({ text: "I listen", source: "speech" })).toEqual({
      text: "I listen",
      source: "speech",
    });
  });

  it("rejects unknown sources and empty text", () => {
    expect(parseIntent({ text: "hello", source: "voice" })).toBeNull();
    expect(parseIntent({ text: "   ", source: "text" })).toBeNull();
    expect(parseIntent({ text: "x".repeat(501), source: "text" })).toBeNull();
    expect(parseIntent(null)).toBeNull();
  });
});

describe("generateRoomCode", () => {
  it("uses only the unambiguous alphabet", () => {
    for (let index = 0; index < 40; index += 1) {
      const code = generateRoomCode();
      expect(code).toHaveLength(6);
      for (const character of code) {
        expect(ROOM_CODE_ALPHABET.includes(character)).toBe(true);
      }
    }
  });
});
