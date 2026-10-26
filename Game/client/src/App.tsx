import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { JoinView } from "./views/JoinView";
import { PlayView } from "./views/PlayView";
import { TvView } from "./views/TvView";

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/tv" replace />} />
        <Route path="/tv" element={<TvView />} />
        <Route path="/join" element={<JoinView />} />
        <Route path="/play" element={<PlayView />} />
        <Route path="*" element={<Navigate to="/tv" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
