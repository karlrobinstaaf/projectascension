/**
 * Speech-to-text sits behind this interface and only fills the text field.
 * Submitting still sends a normal player intent (`source: "text" | "speech"`).
 * A future engine replaces `createSpeechToTextSource` without changing the form.
 */

export interface SpeechTranscriptUpdate {
  transcript: string;
}

export interface SpeechToTextSource {
  /** False when the flag is off or this browser has no speech engine. */
  readonly available: boolean;
  start(): void;
  stop(): void;
  subscribe(listener: (update: SpeechTranscriptUpdate) => void): () => void;
  subscribeError(listener: (message: string) => void): () => void;
  subscribeListening(listener: (listening: boolean) => void): () => void;
}

interface RecognitionAlternative {
  transcript: string;
}

interface RecognitionResult {
  readonly isFinal: boolean;
  readonly 0?: RecognitionAlternative;
}

interface RecognitionEvent {
  readonly results: ArrayLike<RecognitionResult>;
}

interface Recognition {
  lang: string;
  interimResults: boolean;
  continuous: boolean;
  start(): void;
  stop(): void;
  onresult: ((event: RecognitionEvent) => void) | null;
  onerror: ((event: { error: string }) => void) | null;
  onend: (() => void) | null;
}

type RecognitionCtor = new () => Recognition;

function recognitionCtor(): RecognitionCtor | null {
  const candidate = window as Window & {
    SpeechRecognition?: RecognitionCtor;
    webkitSpeechRecognition?: RecognitionCtor;
  };
  return candidate.SpeechRecognition ?? candidate.webkitSpeechRecognition ?? null;
}

function speechErrorMessage(code: string): string {
  if (code === "not-allowed") return "The microphone is blocked. Type instead.";
  if (code === "no-speech") return "No speech heard. Type instead, or try the mic again.";
  if (code === "network") return "Voice input needs the browser speech service. Type instead.";
  return "Voice input stopped. Type instead.";
}

export function createSpeechToTextSource(enabled: boolean): SpeechToTextSource {
  const Ctor = enabled ? recognitionCtor() : null;
  const listeners = new Set<(update: SpeechTranscriptUpdate) => void>();
  const errors = new Set<(message: string) => void>();
  const listeningListeners = new Set<(listening: boolean) => void>();
  let active: Recognition | null = null;

  const setListening = (listening: boolean): void => {
    for (const listener of listeningListeners) listener(listening);
  };

  return {
    available: Ctor !== null,
    start() {
      if (!Ctor) return;
      active?.stop();
      const recognition = new Ctor();
      recognition.lang = navigator.language || "en-US";
      recognition.interimResults = true;
      recognition.continuous = false;
      recognition.onresult = (event) => {
        let transcript = "";
        for (let index = 0; index < event.results.length; index += 1) {
          transcript += event.results[index]?.[0]?.transcript ?? "";
        }
        const update = { transcript: transcript.trim() };
        for (const listener of listeners) listener(update);
      };
      recognition.onerror = (event) => {
        for (const listener of errors) listener(speechErrorMessage(event.error));
        setListening(false);
      };
      recognition.onend = () => {
        if (active === recognition) active = null;
        setListening(false);
      };
      active = recognition;
      try {
        recognition.start();
        setListening(true);
      } catch {
        active = null;
        setListening(false);
        for (const listener of errors) listener("Voice input could not start. Type instead.");
      }
    },
    stop() {
      active?.stop();
      active = null;
      setListening(false);
    },
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
    subscribeError(listener) {
      errors.add(listener);
      return () => errors.delete(listener);
    },
    subscribeListening(listener) {
      listeningListeners.add(listener);
      return () => listeningListeners.delete(listener);
    },
  };
}
