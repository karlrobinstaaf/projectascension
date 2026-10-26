import { useEffect, useMemo, useSyncExternalStore, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { MAX_INTENT_LENGTH } from "@ascension/shared";
import { createSpeechToTextSource } from "../input/speechSource";
import { useIntentDraft } from "../input/useIntentDraft";
import { getPlayerSnapshot, startPlayer, submitIntent, subscribePlayer } from "../playerSession";

const speechEnabled = import.meta.env.VITE_SPEECH_INPUT !== "false";

export function PlayView() {
  const snapshot = useSyncExternalStore(subscribePlayer, getPlayerSnapshot, getPlayerSnapshot);
  const speech = useMemo(() => createSpeechToTextSource(speechEnabled), []);
  const draft = useIntentDraft(speech);

  useEffect(() => {
    startPlayer();
  }, []);

  const latestNarration = [...(snapshot.state?.transcript ?? [])]
    .reverse()
    .find((entry) => entry.kind === "narration");
  const notes = snapshot.privateState?.notes ?? [];

  function onSubmit(event: FormEvent<HTMLFormElement>): void {
    event.preventDefault();
    const intent = draft.consume();
    if (!intent) return;
    submitIntent(intent);
  }

  if (!snapshot.playerId) {
    const waiting = snapshot.pending || snapshot.connection === "connecting";
    return (
      <main className="phone">
        <section className="join">
          <p className="kicker">Project Ascension</p>
          <h1>{snapshot.yielded ? "Seat moved." : waiting ? "Taking your seat…" : "No seat yet."}</h1>
          <p className="lede">
            {snapshot.error ??
              (snapshot.connection === "reconnecting"
                ? "Reconnecting…"
                : "Join with the code on the television.")}
          </p>
          <Link className="primary link-button" to="/join">
            Join a room
          </Link>
        </section>
      </main>
    );
  }

  return (
    <main className="phone play-phone">
      <header className="phone-bar">
        <p className="kicker">{snapshot.state?.code}</p>
        <p>
          {snapshot.name}
          {snapshot.connection === "live" ? "" : " · reconnecting"}
        </p>
      </header>

      <section className="private" aria-live="polite">
        <h2>Only you</h2>
        {notes.length === 0 ? (
          <p className="quiet">
            Nothing private yet. If the Game Master tells only you something, it stays on this
            phone.
          </p>
        ) : (
          <ul>
            {notes.map((note) => (
              <li key={note.id}>{note.text}</li>
            ))}
          </ul>
        )}
      </section>

      <section className="echo" aria-live="polite">
        <h2>On the television</h2>
        <p>{latestNarration?.text ?? "The room is quiet."}</p>
      </section>

      <form className="composer" onSubmit={onSubmit}>
        <label htmlFor="intent">What do you do?</label>
        <textarea
          id="intent"
          rows={3}
          maxLength={MAX_INTENT_LENGTH}
          value={draft.text}
          placeholder="I walk over to the diner."
          onChange={(event) => draft.onType(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter" && !event.shiftKey) {
              event.preventDefault();
              const intent = draft.consume();
              if (intent) submitIntent(intent);
            }
          }}
        />
        {draft.speechError ? (
          <p className="form-error" role="status">
            {draft.speechError}
          </p>
        ) : null}
        {snapshot.error ? (
          <p className="form-error" role="alert">
            {snapshot.error}
          </p>
        ) : null}
        <div className="composer-actions">
          {speechEnabled ? (
            <button
              type="button"
              className="secondary"
              aria-pressed={draft.listening}
              disabled={!speech.available}
              title={
                speech.available
                  ? "Optional. Fills the text field. The browser speech service may leave this device."
                  : "This browser has no speech engine. Type instead."
              }
              onClick={draft.toggleMic}
            >
              {draft.listening ? "Stop" : "Voice"}
            </button>
          ) : null}
          <button type="submit" className="primary" disabled={snapshot.pending || draft.text.trim().length === 0}>
            {snapshot.pending ? "Sending…" : "Send"}
          </button>
        </div>
      </form>
    </main>
  );
}
