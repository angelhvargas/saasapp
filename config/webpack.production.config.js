import path from 'path';
import webpack from 'webpack';
import BundleTracker from 'webpack-bundle-tracker';
import baseConfig from './webpack.base.config.js';


module.exports = (opts) => {

  const
    {CDN_PATH, PROJECT_ROOT} = opts,
    config = baseConfig(opts);

  return {
    ...config,
    output: {
      ...config.output,
      path: path.resolve('/data/static', 'saas_app/dist/'),
      // set CDN_PATH to your cdn static file directory
      publicPath: '/static/saas_app/dist/',
    },
    plugins: [
      ...config.plugins,
      // production bundle stats file
      new BundleTracker({filename: 'webpack-stats-production.json', path: '/data/webpack'}),
      // pass options to uglify
      new webpack.LoaderOptionsPlugin({
        options: {
        },
        minimize: false,
        debug: true,
      }),
      // minifies your code
      new webpack.optimize.UglifyJsPlugin({
        compress: {
          warnings: false,
        },
        output: {
          comments: false,
        },
        sourceMap: false,
      }),
      // removes duplicate modules
      new webpack.optimize.DedupePlugin(),
    ],
  };
};
