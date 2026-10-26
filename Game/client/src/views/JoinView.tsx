import { useState, type FormEvent } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import { MAX_PLAYER_NAME_LENGTH } from "@ascension/shared";
import { joinRoom } from "../playerSession";
import { loadPlayerSession } from "../storage";

export function JoinView() {
  const [params] = useSearchParams();
  const navigate = useNavigate();
  const preset = (params.get("room") ?? "").toUpperCase();
  const [code, setCode] = useState(preset);
  const [name, setName] = useState("");
  const [error, setError] = useState<string | null>(null);
  const existing = loadPlayerSession();

  function onSubmit(event: FormEvent<HTMLFormElement>): void {
    event.preventDefault();
    const trimmedName = name.trim();
    const trimmedCode = code.trim();
    if (!trimmedCode) {
      setError("Enter the room code from the television.");
      return;
    }
    if (!trimmedName) {
      setError("Choose the name you want on the screen.");
      return;
    }
    setError(null);
    joinRoom(trimmedCode, trimmedName);
    void navigate("/play");
  }

  return (
    <main className="phone">
      <form className="join" onSubmit={onSubmit}>
        <p className="kicker">Project Ascension</p>
        <h1>Join the room.</h1>
        <p className="lede">The television stays the shared window. This phone is how you act, and where private notes arrive.</p>
        <label>
          Room code
          <input
            value={code}
            onChange={(event) => setCode(event.target.value.toUpperCase())}
            inputMode="text"
            autoCapitalize="characters"
            autoCorrect="off"
            spellCheck={false}
            maxLength={12}
            autoFocus={preset.length === 0}
          />
        </label>
        <label>
          Your name
          <input
            value={name}
            onChange={(event) => setName(event.target.value)}
            maxLength={MAX_PLAYER_NAME_LENGTH}
            autoComplete="nickname"
            autoFocus={preset.length > 0}
          />
        </label>
        {error ? (
          <p className="form-error" role="alert">
            {error}
          </p>
        ) : null}
        <button type="submit" className="primary">
          Take a seat
        </button>
        {existing ? (
          <p className="fine">
            Already seated as {existing.name}? <Link to="/play">Return to the room</Link>.
          </p>
        ) : null}
      </form>
    </main>
  );
}
