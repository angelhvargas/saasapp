import optimization from 'webpack';
import baseConfig from './webpack.base.config.js';


module.exports = (opts) => {

  const config = baseConfig(opts);
  const {PROJECT_ROOT} = opts;
  var BundleTracker = require('webpack-bundle-tracker');
  var CaseSensitivePathsPlugin = require('case-sensitive-paths-webpack-plugin');

  return {
    ...config,
    output: {
      ...config.output,
      publicPath: 'http://0.0.0.0:8080/bundles/',
    },
    plugins: [
      ...config.plugins,
      // development bundle stats file
      new BundleTracker({
        filename: './webpack-stats.json',
        path: PROJECT_ROOT,
       }),
      new CaseSensitivePathsPlugin(),  // OSX wont check but other unix os will
      new optimization.NoEmitOnErrorsPlugin(),
    ],
  };
};
