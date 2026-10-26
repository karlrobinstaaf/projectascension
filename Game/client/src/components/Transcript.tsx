import { useEffect, useRef } from "react";
import type { TranscriptEntry } from "@ascension/shared";

export function Transcript({ entries }: { entries: TranscriptEntry[] }) {
  const endRef = useRef<HTMLDivElement>(null);
  const lastNarrationId = [...entries].reverse().find((entry) => entry.kind === "narration")?.id;

  useEffect(() => {
    endRef.current?.scrollIntoView({ block: "end" });
  }, [entries.length]);

  return (
    <div className="transcript">
      {entries.map((entry) =>
        entry.kind === "action" ? (
          <p key={entry.id} className="beat action">
            <span className="who">{entry.playerName}</span>
            {entry.text}
          </p>
        ) : (
          <p
            key={entry.id}
            className={entry.id === lastNarrationId ? "beat narration latest" : "beat narration"}
          >
            {entry.text}
          </p>
        ),
      )}
      <div ref={endRef} />
    </div>
  );
}
