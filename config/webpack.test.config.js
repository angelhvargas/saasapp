const baseConfig = require('./webpack.base.config.js');
const ESLintPlugin = require('eslint-webpack-plugin');

module.exports = (opts) => {
  const config = baseConfig(opts);

  return {
    ...config,
    devtool: 'inline-source-map',
    plugins: [
      ...config.plugins,
      new ESLintPlugin({
        // Plugin options
        extensions: ['js', 'jsx'],
        exclude: ['node_modules'],
        // You can specify other plugin options as needed. For example:
        // context: 'src',
        // files: 'src/**/*.{js,jsx,ts,tsx}',
      }),
    ],
    // Since eslint-loader is replaced with eslint-webpack-plugin, you no longer need
    // to add a rule for ESLint in the `module.rules` array.
  };
};
