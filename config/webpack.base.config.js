import path from 'path';
import webpack from 'webpack';


module.exports = (opts) => {

  const {PROJECT_ROOT, NODE_ENV} = opts;

  let plugins = [
    // add all common plugins here
    new webpack.DefinePlugin({
      'process.env.NODE_ENV' : JSON.stringify(NODE_ENV)
    }),
    // Promise and fetch polyfills
    //new ProvidePlugin({
      //Promise: 'imports-loader?this=>global!exports-loader?global.Promise!es6-promise',
      //fetch: 'imports-loader?this=>global!exports-loader?global.fetch!whatwg-fetch',
    //}),
  ];
  if (NODE_ENV !== 'test') {
    // karma webpack can't use these
    plugins = [
      ...plugins,
      // vendor chuncks
    ];
  }

  return {
    context: PROJECT_ROOT,

    externals: {
      // require("jquery") is external and available
      //  on the global var jQuery
      "jquery": "jQuery"
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
        maxInitialRequests: Infinity,
        minSize: 0,
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name(module) {
              // get the name. E.g. node_modules/packageName/not/this/part.js
              // or node_modules/packageName
              const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1];
  
              // npm package names are URL-safe, but some servers don't like @ symbols
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
      extensions: ['','.ts', '.js', '.jsx'],
      modules: [
        path.resolve(PROJECT_ROOT, 'saasapp-app-react'),
        "node_modules",
      ],
    },
  };
};
