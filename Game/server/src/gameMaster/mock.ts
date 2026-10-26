import type {
  GameMaster,
  GameMasterActionContext,
  GameMasterOpeningView,
  GameMasterResult,
} from "./types.js";

export const MOCK_GAME_MASTER_ID = "mock";

/** Fixed opener so a room comes up without an API key. Not scenario content. */
export const MOCK_OPENING_NARRATION =
  "Rain threads through the streetlights at the edge of a small town. A diner sign hums across the road. The car ticks as it cools. Nothing here tells you what to do.";

const FALLBACKS = [
  (spoken: string) =>
    `"${spoken}" The rain keeps tapping the roof. No one arrives to say whether it mattered.`,
  (spoken: string) =>
    `You go ahead with it. "${spoken}" The diner sign hums. The road does not answer.`,
  (spoken: string) =>
    `"${spoken}" It is done in the open, where the others can see. The night stays ordinary.`,
] as const;

function fnv1a(text: string): number {
  let hash = 0x811c9dc5;
  for (let index = 0; index < text.length; index += 1) {
    hash ^= text.charCodeAt(index);
    hash = Math.imul(hash, 0x01000193);
  }
  return hash >>> 0;
}

export function mockResolve(view: GameMasterActionContext): GameMasterResult {
  const spoken = view.action.text;
  const folded = spoken.toLowerCase();

  if (/\b(listen|hum|generator|power)\b/.test(folded)) {
    return {
      narration:
        "A low electrical hum comes from behind the diner. It stutters, then finds a rhythm again. Everyone can hear it.",
      privateNotes: [
        {
          playerId: view.action.playerId,
          text: "The rhythm is wrong for a healthy motor. It sounds like a building running on backup power. That reading is yours alone until you share it.",
        },
      ],
    };
  }

  if (/\b(wait|stay|nothing|silent|silence)\b/.test(folded)) {
    return {
      narration:
        "You wait. Rain keeps moving along the curb. A car passes without slowing down. The diner sign does not change.",
      privateNotes: [],
    };
  }

  if (/\b(leave|drive|turn around|go back)\b/.test(folded)) {
    return {
      narration:
        "You turn toward the car. The door is still unlocked. The lights of the town stay where they are.",
      privateNotes: [],
    };
  }

  if (/\b(look|watch|see|window|observe)\b/.test(folded)) {
    return {
      narration:
        "You look. Wet pavement, a dark window, your own reflection, and the diner across the road. Nothing in the picture announces itself as important.",
      privateNotes: [],
    };
  }

  const choice = FALLBACKS[fnv1a(`${view.action.playerName}|${spoken}`) % FALLBACKS.length];
  if (!choice) {
    return { narration: spoken, privateNotes: [] };
  }
  return { narration: choice(spoken), privateNotes: [] };
}

/** Deterministic stand-in used when no model provider is configured. */
export class MockGameMaster implements GameMaster {
  readonly id = MOCK_GAME_MASTER_ID;

  openScene(_view: GameMasterOpeningView): Promise<GameMasterResult> {
    return Promise.resolve({
      narration: MOCK_OPENING_NARRATION,
      privateNotes: [],
    });
  }

  resolveAction(view: GameMasterActionContext): Promise<GameMasterResult> {
    return Promise.resolve(mockResolve(view));
  }
}
