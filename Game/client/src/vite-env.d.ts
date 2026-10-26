/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_SPEECH_INPUT?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
