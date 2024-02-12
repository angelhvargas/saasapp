const path = require('path');
const baseConfig = require('./webpack.base.config.js');
const BundleTracker = require('webpack-bundle-tracker'); // Ensure this is installed
const CaseSensitivePathsPlugin = require('case-sensitive-paths-webpack-plugin'); // Ensure this is installed

module.exports = (opts) => {
  const config = baseConfig(opts);
  const { PROJECT_ROOT } = opts;
  console.log('PROJECT_ROOT:', PROJECT_ROOT); // Debugging line

  if (!PROJECT_ROOT) throw new Error('PROJECT_ROOT is undefined');

  return {
    ...config,
    mode: 'development',
    output: {
      ...config.output,
      publicPath: 'http://0.0.0.0:8080/bundles/',
    },
    plugins: [
      ...config.plugins,
      new BundleTracker({
        filename: 'webpack-stats.json',
        path: PROJECT_ROOT,
      }),
      new CaseSensitivePathsPlugin(),
    ],
    devtool: 'eval-source-map',
    devServer: {
      static: {
        directory: path.join(__dirname, 'dist'), // Adjust the path as necessary
      },
      hot: true,
      host: '0.0.0.0',
      port: 8080,
      headers: { 'Access-Control-Allow-Origin': '*' },
      historyApiFallback: true,
    },
  };
};
