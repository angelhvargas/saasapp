/**
 * The main webpack configuration.
 *
 * By default webpack commands will look for this file unless the --config [path] argument is used.
 * This config routes to other configs using, process.env.NODE_ENV to determine which config is being requested.
 *
 * Adding more configs:
 *  Just add the NODE_ENV=<config> prefix to your command or export to the environment.
 *  Add a case for your <config> value that returns the path to your config file.
 *
 * @returns {object} - returns a webpack config object
 */
// ES Module Syntax
const path = require('path');

const OPTIONS = {
  PROJECT_ROOT: path.resolve(__dirname),
  NODE_ENV: process.env.NODE_ENV,
  CDN_PATH: process.env.CDN_PATH,
};

// Define a function that selects and requires the appropriate config file
function getConfig(env) {
  switch (env) {
    case 'production':
      return require('./config/webpack.production.config');
    case 'development':
      return require('./config/webpack.development.config');
    case 'test':
      return require('./config/webpack.test.config');
    default:
      return require('./config/webpack.development.config');
  }
}

// Export the result of invoking the selected config function with OPTIONS
module.exports = getConfig(process.env.NODE_ENV)(OPTIONS);
