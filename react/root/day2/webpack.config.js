const path = require("path");
const RefreshWebpackPlugin = require("@pmmmwh/react-refresh-webpack-plugin");

module.exports = {
  name: "wordrelay-setting",
  mode: "development", // 실서비스에서는 production으로 바꾸면 됨
  devtool: "eval",
  resolve: {
    //알아서 entry에 맞게 찾음 client로 되어있는 js나 jsx가 있는지
    extensions: [".js", ".jsx"],
  },

  entry: {
    app: ["./client"],
  },

  module: {
    rules: [
      {
        test: /\.jsx?/,
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
          plugins: [
            "@babel/plugin-proposal-class-properties",
            "react-refresh/babel",
          ],
        },
      },
    ],
  },
  plugins: [new RefreshWebpackPlugin()],
  output: {
    path: path.join(__dirname, "dist"),
    filename: "app.js",
  },
  devServer: {
    devMiddleware: { publicPath: "/dist" }, // 웹팩이 빌드한 파일들이 위치하는 곳
    static: { directory: path.resolve(__dirname) }, // 실제로 존재하는 정적파일들의 경로
    hot: true,
  },
};
