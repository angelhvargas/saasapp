const path = require('path');
const webpack = require('webpack');

const { DefinePlugin, ProvidePlugin } = webpack;

module.exports = (opts) => {
  const { PROJECT_ROOT, NODE_ENV } = opts;

  const plugins = [
    new DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(NODE_ENV),
    }),
  ];

  if (['development', 'production'].includes(NODE_ENV)) {
    plugins.push(
      new ProvidePlugin({
        Promise: 'es6-promise', // Assuming 'es6-promise' is installed and provides a 'Promise' polyfill
        fetch: 'whatwg-fetch', // Assuming 'whatwg-fetch' is installed and provides a 'fetch' polyfill
      }),
    );
  }

  return {
    context: PROJECT_ROOT,
    externals: {
      "jquery": "jQuery",
    },
    entry: {
      main: path.resolve(PROJECT_ROOT, 'saas-app-react/index.tsx'), // Ensure this path is correct
      vendor: ['react', 'redux', 'react-router', 'react-redux', 'react-dom'],
    },
    output: {
      path: path.resolve(PROJECT_ROOT, 'saas_app/static/react/bundles'),
      filename: '[name]-[chunkhash].js',
    },
    plugins,
    optimization: {
      runtimeChunk: 'single',
      splitChunks: {
        chunks: 'all',
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name: (module) => {
              const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1];
              return `npm.${packageName.replace('@', '')}`;
            },
          },
        },
      },
    },
    module: {
      rules: [
        {
          test: /\.([cm]?ts|tsx)$/, // or /\.ts$/ if you're only using TypeScript files without JSX
          use: {
            loader: 'ts-loader',
            options: {
              transpileOnly: true, // Skip type checking
            },
          },
          exclude: /node_modules/,
        },
        {
          test: /\.jsx?$/,
          exclude: /(node_modules|\.ts$|\.tsx$)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env', '@babel/preset-react'],
              plugins: ['@babel/plugin-proposal-class-properties', '@babel/plugin-transform-runtime'],
            },
          },
        },
        {
          test: /\.scss$/,
          use: ['style-loader', 'css-loader', 'sass-loader', 'postcss-loader'],
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        },
        {
          test: /\.(png|jpg|gif|ttf|eot|svg)$/,
          type: 'asset/resource',
        },
      ],
    },
    resolve: {
      extensions: ['.tsx', '.ts', '.js', '.jsx'],
      extensionAlias: {
        ".js": [".js", ".ts"],
        ".cjs": [".cjs", ".cts"],
        ".mjs": [".mjs", ".mts"]
       },
      modules: [path.resolve(PROJECT_ROOT, 'saasapp-app-react'), 'node_modules'],
    },
  };
};
