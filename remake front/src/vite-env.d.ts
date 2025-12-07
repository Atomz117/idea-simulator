/// <reference types="vite/client" />

declare global {
  interface Window {
    UnicornStudio?: {
      init: () => void;
      isInitialized?: boolean;
    };
  }
}
