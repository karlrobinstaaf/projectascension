import {
  ClientEvents,
  ServerEvents,
  type SessionError,
  type SessionErrorCode,
} from "@ascension/shared";
import type { Server, Socket } from "socket.io";
import type { GameMaster } from "../gameMaster/types.js";
import { PLACEHOLDER_SCENE, RoomStore } from "../rooms/store.js";
import { parseIntent, parsePlayerName, parseRoomCode, readStringField } from "../rooms/validate.js";
import { toGameMasterActionContext, toPrivateState, toPublicState } from "../rooms/view.js";

const MESSAGES: Record<SessionErrorCode, string> = {
  ROOM_NOT_FOUND: "No room is using that code.",
  ROOM_FULL: "This room already has six players.",
  INVALID_NAME: "Use a name of up to 24 letters or numbers.",
  INVALID_CODE: "Enter the six-character room code.",
  INVALID_INTENT: "Say what you do in a short sentence.",
  NOT_IN_ROOM: "Join the room before you act.",
  REJOIN_FAILED: "That seat is no longer in this room. Join again.",
  GM_UNAVAILABLE: "The Game Master could not respond.",
  REPLACED: "This seat was opened on another device.",
};

export function registerSockets(io: Server, store: RoomStore, gameMaster: GameMaster): void {
  const tails = new Map<string, Promise<void>>();

  const enqueue = (code: string, task: () => Promise<void>): void => {
    const previous = tails.get(code) ?? Promise.resolve();
    const next = previous.then(task, task);
    tails.set(
      code,
      next.then(
        () => undefined,
        () => undefined,
      ),
    );
  };

  const fail = (socket: Socket, code: SessionErrorCode, message?: string): void => {
    const error: SessionError = { code, message: message ?? MESSAGES[code] };
    socket.emit(ServerEvents.sessionError, error);
  };

  const broadcast = (code: string): void => {
    const room = store.get(code);
    if (!room) return;
    io.to(channel(code)).emit(ServerEvents.roomState, toPublicState(room));
  };

  const sendPrivate = (socketId: string | null, playerId: string, roomCode: string): void => {
    if (!socketId) return;
    const room = store.get(roomCode);
    const player = room?.players.find((candidate) => candidate.id === playerId);
    if (!player) return;
    io.to(socketId).emit(ServerEvents.privateState, toPrivateState(player));
  };

  const replaceSocket = (socketId: string | null): void => {
    if (!socketId) return;
    const previous = io.sockets.sockets.get(socketId);
    if (!previous) return;
    fail(previous, "REPLACED");
    previous.disconnect(true);
  };

  io.on("connection", (socket) => {
    socket.on(ClientEvents.hostCreate, () => {
      enqueue(`socket:${socket.id}`, async () => {
        try {
          for (const joined of socket.rooms) {
            if (joined !== socket.id) await socket.leave(joined);
          }
          store.detachSocket(socket.id);
          const opening = await gameMaster.openScene({
            scene: {
              locationLabel: PLACEHOLDER_SCENE.locationLabel,
              timeLabel: PLACEHOLDER_SCENE.timeLabel,
              sharedNarration: [],
            },
            players: [],
          });
          const narration = opening.narration.trim();
          if (!narration) {
            fail(socket, "GM_UNAVAILABLE");
            return;
          }
          const room = store.create(socket.id, narration);
          await socket.join(channel(room.code));
          socket.emit(ServerEvents.hostReady, {
            hostToken: room.hostToken,
            state: toPublicState(room),
          });
        } catch (error) {
          fail(socket, "GM_UNAVAILABLE", errorText(error));
        }
      });
    });

    socket.on(ClientEvents.hostRejoin, (payload: unknown) => {
      const code = parseRoomCode(readStringField(payload, "code"));
      const hostToken = readStringField(payload, "hostToken");
      if (!code || !hostToken) {
        fail(socket, "REJOIN_FAILED");
        return;
      }
      const attached = store.attachHost(code, hostToken, socket.id);
      if (!attached) {
        fail(socket, "REJOIN_FAILED");
        return;
      }
      void socket.join(channel(code));
      replaceSocket(attached.replacedSocketId);
      socket.emit(ServerEvents.hostReady, {
        hostToken: attached.room.hostToken,
        state: toPublicState(attached.room),
      });
      broadcast(code);
    });

    socket.on(ClientEvents.playerJoin, (payload: unknown) => {
      const code = parseRoomCode(readStringField(payload, "code"));
      if (!code) {
        fail(socket, "INVALID_CODE");
        return;
      }
      const name = parsePlayerName(readStringField(payload, "name"));
      if (!name) {
        fail(socket, "INVALID_NAME");
        return;
      }
      const alreadySeated = store.findPlayerBySocket(socket.id);
      if (alreadySeated) {
        socket.emit(ServerEvents.playerReady, {
          playerId: alreadySeated.player.id,
          playerToken: alreadySeated.player.token,
          state: toPublicState(alreadySeated.room),
          privateState: toPrivateState(alreadySeated.player),
        });
        return;
      }
      const joined = store.addPlayer(code, name, socket.id);
      if (!joined.ok) {
        fail(socket, joined.reason === "FULL" ? "ROOM_FULL" : "ROOM_NOT_FOUND");
        return;
      }
      void socket.join(channel(code));
      const room = store.get(code);
      if (!room) {
        fail(socket, "ROOM_NOT_FOUND");
        return;
      }
      socket.emit(ServerEvents.playerReady, {
        playerId: joined.player.id,
        playerToken: joined.player.token,
        state: toPublicState(room),
        privateState: toPrivateState(joined.player),
      });
      broadcast(code);
    });

    socket.on(ClientEvents.playerRejoin, (payload: unknown) => {
      const code = parseRoomCode(readStringField(payload, "code"));
      const playerToken = readStringField(payload, "playerToken");
      if (!code || !playerToken) {
        fail(socket, "REJOIN_FAILED");
        return;
      }
      const attached = store.attachPlayer(code, playerToken, socket.id);
      if (!attached) {
        fail(socket, "REJOIN_FAILED");
        return;
      }
      void socket.join(channel(code));
      replaceSocket(attached.replacedSocketId);
      socket.emit(ServerEvents.playerReady, {
        playerId: attached.player.id,
        playerToken: attached.player.token,
        state: toPublicState(attached.room),
        privateState: toPrivateState(attached.player),
      });
      broadcast(code);
    });

    socket.on(ClientEvents.intentSubmit, (payload: unknown) => {
      const seated = store.findPlayerBySocket(socket.id);
      if (!seated) {
        fail(socket, "NOT_IN_ROOM");
        return;
      }
      const intent = parseIntent(payload);
      if (!intent) {
        fail(socket, "INVALID_INTENT");
        return;
      }
      const { room, player } = seated;
      enqueue(room.code, async () => {
        const current = store.findPlayerBySocket(socket.id);
        if (!current || current.player.id !== player.id) {
          fail(socket, "NOT_IN_ROOM");
          return;
        }
        store.recordAction(current.room, current.player, intent);
        broadcast(current.room.code);
        try {
          const view = toGameMasterActionContext(current.room, current.player, intent);
          const result = await gameMaster.resolveAction(view);
          const applied = store.applyResult(current.room, result);
          broadcast(current.room.code);
          for (const note of applied.privateNotes) {
            const target = current.room.players.find((candidate) => candidate.id === note.playerId);
            sendPrivate(target?.socketId ?? null, note.playerId, current.room.code);
          }
        } catch (error) {
          const message = errorText(error);
          fail(socket, "GM_UNAVAILABLE", message);
          const hostSocketId = current.room.hostSocketId;
          if (hostSocketId && hostSocketId !== socket.id) {
            const hostSocket = io.sockets.sockets.get(hostSocketId);
            if (hostSocket) fail(hostSocket, "GM_UNAVAILABLE", message);
          }
        }
      });
    });

    socket.on("disconnect", () => {
      const room = store.detachSocket(socket.id);
      if (room) broadcast(room.code);
    });
  });
}

function channel(code: string): string {
  return `room:${code}`;
}

function errorText(error: unknown): string {
  if (error instanceof Error && error.message.trim().length > 0) {
    return error.message;
  }
  return MESSAGES.GM_UNAVAILABLE;
}
