declare module 'node:module' {
    interface Module {
      hot: {
        accept(path: string, callback: () => void): void;
      };
    }
  }
  
declare interface NodeModule {
    hot?: {
      accept(path?: string, callback?: () => void): void;
    };
  }
  