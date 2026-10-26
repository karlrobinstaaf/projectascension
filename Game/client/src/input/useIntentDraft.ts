import { useEffect, useState } from "react";
import type { IntentSource, PlayerIntent } from "@ascension/shared";
import type { SpeechToTextSource } from "./speechSource";

export function useIntentDraft(speech: SpeechToTextSource): {
  text: string;
  listening: boolean;
  speechError: string | null;
  onType: (value: string) => void;
  toggleMic: () => void;
  consume: () => PlayerIntent | null;
} {
  const [text, setText] = useState("");
  const [source, setSource] = useState<IntentSource>("text");
  const [listening, setListening] = useState(false);
  const [speechError, setSpeechError] = useState<string | null>(null);

  useEffect(() => {
    const unsubscribe = speech.subscribe((update) => {
      setText(update.transcript);
      setSource("speech");
      setSpeechError(null);
    });
    const unsubscribeError = speech.subscribeError((message) => {
      setSpeechError(message);
      setListening(false);
    });
    const unsubscribeListening = speech.subscribeListening(setListening);
    return () => {
      unsubscribe();
      unsubscribeError();
      unsubscribeListening();
      speech.stop();
    };
  }, [speech]);

  return {
    text,
    listening,
    speechError,
    onType(value) {
      setText(value);
      setSource("text");
    },
    toggleMic() {
      setSpeechError(null);
      if (listening) speech.stop();
      else speech.start();
    },
    consume() {
      const trimmed = text.trim();
      if (!trimmed) return null;
      speech.stop();
      const intent: PlayerIntent = { text: trimmed, source };
      setText("");
      setSource("text");
      setListening(false);
      return intent;
    },
  };
}
