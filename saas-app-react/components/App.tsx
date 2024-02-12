import React from 'react';

interface AppProps {
  children: React.ReactNode;
}

function App({ children }: AppProps) {
  return <main>{children}</main>;
}

export default App;
