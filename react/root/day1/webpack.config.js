const path = require("path");
const webpack = require("webpack");

module.exports = {
  mode: "development", // 개발중 development, 실서비스일때 production
  devtool: "eval", // 개발중은 eval production일때는 hidden-source-map
  resolve: {
    extensions: [".jsx", ".js"],
  },
  entry: {
    app: ["./client"],
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: "babel-loader",
        options: {
          presets: [
            [
              "@babel/preset-env",
              {
                // env에 대한 설정, 원하는 버전
                targets: {
                  browsers: ["> 1% in KR"],
                },
                debug: true,
              },
            ],
            "@babel/preset-react",
          ],
          plugins: [],
        },
      },
    ],
  },
  plugins: [],
  output: {
    filename: "app.js",
    path: path.join(__dirname, "dist"),
  },
};
