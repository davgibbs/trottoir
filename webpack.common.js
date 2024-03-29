/* This is the Webpack config common to both production and development */

const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  context: __dirname + '/apps/controls/static/controls',
  entry: {
    app: './js/index.js',
  },
  output: {
    path: __dirname + '/apps/controls/static/controls/bundles',
    filename: '[name].[hash].bundle.js',
    chunkFilename: '[name].[chunkhash].bundle.js',
  },
  plugins: [
    new BundleTracker({
      filename: './apps/webpack-stats.json',
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
    }),
    new CleanWebpackPlugin([
      __dirname + '/apps/controls/static/controls/bundles',
    ]),
    new MiniCssExtractPlugin({
      filename: '[name].[hash].css',
    }),
    new VueLoaderPlugin(),
  ],
  optimization: {
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          chunks: 'initial',
          name: 'vendor',
        },
      },
    },
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [{
          loader: MiniCssExtractPlugin.loader,
          options: {
            // you can specify a publicPath here by default it use publicPath in webpackOptions.output
            publicPath: '/static/bundles/css/',
          },
        },
        'css-loader',
        ],
      },
      {
        test: /\.html$/,
        use: [{
          loader: 'html-loader',
        }],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.vue$/,
        use: 'vue-loader',
      },
      {
        enforce: 'pre',
        test: /\.(js|vue)$/,
        exclude: /node_modules/,
        loader: 'eslint-loader',
      },
    ],
  },
};