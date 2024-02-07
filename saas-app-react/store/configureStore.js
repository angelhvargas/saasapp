import { configureStore, getDefaultMiddleware } from '@reduxjs/toolkit';
import rootReducer from '../reducers';

// If you have a custom DevTools setup
import DevTools from '../containers/DevTools';

export default function configureAppStore(initialState) {
  const store = configureStore({
    reducer: rootReducer,
    middleware: (getDefaultMiddleware) => [...getDefaultMiddleware()],
    preloadedState: initialState,
    // Corrected enhancers configuration
    enhancers: (defaultEnhancers) => [
      ...defaultEnhancers(),
      ...(process.env.NODE_ENV !== 'production' ? [DevTools.instrument()] : [])
    ],
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
