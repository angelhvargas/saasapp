import { configureStore } from '@reduxjs/toolkit';
import rootReducer from '../reducers';

export default function configureAppStore(initialState?: RootState) {
  const store = configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) =>
      getDefaultMiddleware(),
    preloadedState: initialState,
    devTools: process.env.NODE_ENV !== 'production',
  });

  // Hot Module Replacement for reducers
  if (process.env.NODE_ENV !== 'production' && module.hot) {
    module.hot.accept('../reducers', () => {
      const newRootReducer = require('../reducers').default;
      store.replaceReducer(newRootReducer);
    });
  }

  return store;
}

export type RootState = ReturnType<typeof rootReducer>;
