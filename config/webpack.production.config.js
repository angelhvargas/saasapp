import path from 'path';
import { CleanWebpackPlugin } from 'clean-webpack-plugin'; // Automatically clean your build folder before each build
import BundleTracker from 'webpack-bundle-tracker'; // If needed for integration with backend frameworks like Django
import TerserPlugin from 'terser-webpack-plugin'; // For minification
import CssMinimizerPlugin from 'css-minimizer-webpack-plugin'; // For CSS optimization
import MiniCssExtractPlugin from 'mini-css-extract-plugin'; // Extracts CSS into separate files
import { DefinePlugin } from 'webpack'; // For defining environment variables
import baseConfig from './webpack.base.config.js';

module.exports = (opts) => {
  const { PROJECT_ROOT } = opts;
  const config = baseConfig(opts);

  return {
    ...config,
    mode: 'production',
    output: {
      ...config.output,
      path: path.resolve(PROJECT_ROOT, 'dist'),
      publicPath: '/static/saas_app/dist/',
      filename: '[name].[contenthash].js', // Use contenthash for better caching
    },
    plugins: [
      ...config.plugins,
      new CleanWebpackPlugin(),
      new BundleTracker({ filename: 'webpack-stats-production.json', path: path.resolve(PROJECT_ROOT, 'webpack') }),
      new MiniCssExtractPlugin({
        filename: '[name].[contenthash].css',
      }),
      new DefinePlugin({
        'process.env.NODE_ENV': JSON.stringify('production'),
      }),
      // Add other plugins here as needed
    ],
    optimization: {
      minimize: true,
      minimizer: [
        new TerserPlugin({
          terserOptions: {
            compress: {
              comparisons: false,
            },
            mangle: {
              safari10: true,
            },
            output: {
              comments: false,
              ascii_only: true,
            },
            warnings: false,
          },
        }),
        new CssMinimizerPlugin(),
      ],
      splitChunks: {
        chunks: 'all',
        maxInitialRequests: 25,
        minSize: 20000,
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name(module) {
              const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1];
              return `npm.${packageName.replace('@', '')}`;
            },
          },
        },
      },
      runtimeChunk: 'single',
    },
    performance: {
      hints: 'warning',
      maxEntrypointSize: 512000,
      maxAssetSize: 512000,
    },
    // Consider using 'source-map' or 'hidden-source-map' for production
    devtool: 'source-map',
  };
};
