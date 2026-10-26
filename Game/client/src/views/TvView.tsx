import { useEffect, useSyncExternalStore } from "react";
import { QrCode } from "../components/QrCode";
import { Transcript } from "../components/Transcript";
import { getTvSnapshot, openNewRoom, startTv, subscribeTv } from "../tvSession";

function formatCode(code: string): string {
  return code.split("").join(" ");
}

function joinLink(code: string): string {
  const url = new URL("/join", window.location.origin);
  url.searchParams.set("room", code);
  return url.toString();
}

export function TvView() {
  const snapshot = useSyncExternalStore(subscribeTv, getTvSnapshot, getTvSnapshot);

  useEffect(() => {
    startTv();
  }, []);

  const state = snapshot.state;
  const localHost = ["localhost", "127.0.0.1", "::1"].includes(window.location.hostname);
  const port = window.location.port ? `:${window.location.port}` : "";
  const lanLinks = snapshot.lanAddresses.map(
    (address) => `http://${address}${port}/tv`,
  );

  return (
    <main className={state?.phase === "in_play" ? "tv play" : "tv lobby"}>
      {snapshot.connection !== "live" ? (
        <p className="banner" role="status">
          {snapshot.yielded ? snapshot.error : "Reconnecting to the room…"}
        </p>
      ) : null}
      {snapshot.error && snapshot.connection === "live" ? (
        <p className="banner" role="alert">
          {snapshot.error}
        </p>
      ) : null}

      {!state ? (
        <section className="lobby-card">
          <p className="kicker">Project Ascension</p>
          <h1>Opening the room…</h1>
        </section>
      ) : state.phase === "lobby" ? (
        <section className="lobby-card">
          <p className="kicker">Project Ascension</p>
          <h1>The room is open.</h1>
          <p className="lede">
            Phones on this Wi-Fi join with the code or the QR. Say what you do in text. This
            screen is the window.
          </p>
          <p className="room-code" aria-label={`Room code ${state.code}`}>
            {formatCode(state.code)}
          </p>
          <QrCode className="qr" value={joinLink(state.code)} />
          <p className="join-url">{joinLink(state.code)}</p>
          {localHost ? (
            <div className="lan-note">
              <p>
                This page is on localhost, so a phone cannot open that link. On the television,
                use this computer’s address on the Wi-Fi.
              </p>
              {lanLinks.length > 0 ? (
                <ul>
                  {lanLinks.map((link) => (
                    <li key={link}>{link}</li>
                  ))}
                </ul>
              ) : (
                <p>No LAN address was found. Join the Wi-Fi and refresh.</p>
              )}
            </div>
          ) : null}
          <blockquote className="opening">
            {state.transcript.find((entry) => entry.kind === "narration")?.text}
          </blockquote>
          <button type="button" className="text-button" onClick={openNewRoom}>
            New room
          </button>
        </section>
      ) : (
        <>
          <header className="scene-bar">
            <p>{state.scene.locationLabel}</p>
            <p>{state.scene.timeLabel}</p>
          </header>
          <Transcript entries={state.transcript} />
          <footer className="tv-footer">
            <div>
              <ul className="roster">
                {state.players.map((player) => (
                  <li key={player.id} className={player.connected ? "on" : "off"}>
                    <span className="dot" aria-hidden="true" />
                    <span>{player.name}</span>
                    {player.connected ? null : <span className="away">away</span>}
                  </li>
                ))}
              </ul>
              <p className="seats">
                {state.seats.filled} of {state.seats.capacity}
              </p>
            </div>
            <div className="join-chip">
              <div>
                <p className="kicker">Join</p>
                <p className="room-code compact" aria-label={`Room code ${state.code}`}>
                  {formatCode(state.code)}
                </p>
                <button type="button" className="text-button" onClick={openNewRoom}>
                  New room
                </button>
              </div>
              <QrCode className="qr qr-small" value={joinLink(state.code)} />
            </div>
          </footer>
        </>
      )}
    </main>
  );
}
