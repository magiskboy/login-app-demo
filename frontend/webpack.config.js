const path = require('path')
const webpack = require('webpack')
const BrowserSyncPlugin = require('browser-sync-webpack-plugin')

module.exports = {
  entry: "./src/app.module.jsx",
  mode: "development",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "app.bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: ["style-loader", "css-loader"]
      },
      {
        test: /\.(scss|sass)$/,
        exclude: /node_modules/,
        use: ["style-loader", "css-loader", "sass-loader"]
      },
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.(jpe?g|png|gif|svg|ico)$/, 
        loader: [
          {
            loader: "file-loader",
            options: {
              name: "[name].[ext]",
              outputPath: "static/images/",
              publicPath: "static/images/"
            }
          }
        ]
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx', '.sass', '.scss']
  },
  plugins: [
    /*
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, "src", "index.html"),
      filename: "index.html",
      hash: true
    }),
    new BrowserSyncPlugin({
      host: "localhost",
      port: 3000,
      server: {
        baseDir: path.resolve(__dirname, ".")
      },
    }),
    */
    new webpack.ProgressPlugin(),
    new webpack.ProvidePlugin({
      "React": "react"
    }),
    new webpack.ProvidePlugin({
      jQuery: 'jquery',
      $: 'jquery'
    })
  ]
};
