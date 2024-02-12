const React = require('react');
const ReactRouter = require('react-router');

const App = require('./components/App').default; // Assuming default export
const UserApp = require('./containers/UserApp').default; // Assuming default export

const Route = ReactRouter.Route;
const IndexRoute = ReactRouter.IndexRoute;
const Redirect = ReactRouter.Redirect;

const routes = (
  <Route path="/app/" component={App}>
    <IndexRoute component={UserApp} />
    <Redirect from="/app/*" to="/app/" />
  </Route>
);

module.exports = routes;
