import path from 'path';
import webpack, { DefinePlugin, ProvidePlugin } from 'webpack';

export default (opts) => {
  const { PROJECT_ROOT, NODE_ENV } = opts;

  let plugins = [
    new DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify(NODE_ENV),
    }),
  ];

  if (['development', 'production'].includes(NODE_ENV)) {
    plugins.push(
      new ProvidePlugin({
        // Include only if necessary for your project's browser support requirements
        Promise: ['es6-promise', 'Promise'],
        fetch: ['whatwg-fetch', 'fetch'],
      }),
    );
  }

  return {
    context: PROJECT_ROOT,
    externals: {
      "jquery": "jQuery", // Example: Avoid bundling jQuery if it's included via a CDN in your HTML
    },
    entry: {
      main: path.resolve(PROJECT_ROOT, 'saas-app-react/index.js'),
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
            name(module) {
              const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1];
              return `npm.${packageName.replace('@', '')}`;
            },
          },
        },
      },
    },
    module: {
      rules: [
        { test: /\.jsx?$/,
          exclude: /(node_modules)/,
          loader: 'babel-loader',
          options: {
            presets: [
              ['@babel/preset-env',
              {
                "targets": {
                  "esmodules": true
                }
              }]
            ],
            plugins: [
              '@babel/plugin-proposal-class-properties',
              '@babel/plugin-transform-runtime'
            ]
          }
        },
        {
          test: /\.scss$/,
          use: [
            {
              // Adds CSS to the DOM by injecting a `<style>` tag
              loader: 'style-loader'
            },
            {
              // Interprets `@import` and `url()` like `import/require()` and will resolve them
              loader: 'css-loader'
            },
            {
              loader: 'sass-loader'
            },
            {
              // Loader for webpack to process CSS with PostCSS
              loader: 'postcss-loader',
              options: {
                plugins: function () {
                  return [
                    require('autoprefixer')
                  ];
                }
              }
            },
            {
              // Loads a SASS/SCSS file and compiles it to CSS
              loader: 'sass-loader'
            }
          ]
        },
        {
          test: /\.css$/, 
          use: [
            'style-loader',
            'css-loader'
          ]
        },
        {test: /\.(png|jpg|gif)$/, loader: 'url-loader', options: {limit: 8192}},  // inline base64 URLs <=8k
        {test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'file-loader'},
      ], // add all common loaders here
    },
    resolve: {
      extensions: ['.ts', '.js', '.jsx'],
      modules: [path.resolve(PROJECT_ROOT, 'saasapp-app-react'), 'node_modules'],
    },
  };
};
