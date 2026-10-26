import { existsSync } from "node:fs";
import { createServer } from "node:http";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import express, { type Request, type Response, type NextFunction } from "express";
import { Server } from "socket.io";
import { createGameMaster } from "./gameMaster/create.js";
import { listLanAddresses } from "./net/lan.js";
import { RoomStore } from "./rooms/store.js";
import { registerSockets } from "./socket/register.js";

const port = Number(process.env.PORT ?? 3001);
const host = process.env.HOST ?? "0.0.0.0";

if (!Number.isInteger(port) || port < 1) {
  throw new Error(`PORT must be a positive integer, received ${process.env.PORT ?? ""}`);
}

const gameMaster = createGameMaster(process.env);
const store = new RoomStore();

const app = express();
app.get("/health", (_request, response) => {
  response.json({ ok: true, gameMaster: gameMaster.id });
});
app.get("/host-info", (_request, response) => {
  response.json({
    lanAddresses: listLanAddresses(),
    gameMaster: gameMaster.id,
  });
});

const clientDist =
  process.env.CLIENT_DIST ??
  resolve(dirname(fileURLToPath(import.meta.url)), "../../client/dist");

if (existsSync(clientDist)) {
  app.use(express.static(clientDist));
  app.use((request: Request, response: Response, next: NextFunction) => {
    if (request.method !== "GET" && request.method !== "HEAD") {
      next();
      return;
    }
    if (request.path.startsWith("/socket.io")) {
      next();
      return;
    }
    response.sendFile(resolve(clientDist, "index.html"));
  });
}

const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: { origin: true },
});
registerSockets(io, store, gameMaster);

httpServer.listen(port, host, () => {
  console.log(
    `Project Ascension listening on http://${host}:${port} (Game Master: ${gameMaster.id})`,
  );
});
