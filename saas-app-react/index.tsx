const React = require('react');
const ReactDOM = require('react-dom');
const { BrowserRouter } = require('react-router-dom');
const { Provider } = require('react-redux');

const App = require('./components/App').default; // Adjust this to your main App component
const configureStore = require('./store/configureStore').default;

const STORE = configureStore();

ReactDOM.render(
  <Provider store={STORE}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>,
  document.getElementById('app')
);
