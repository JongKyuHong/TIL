const path = require("path");

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
  output: {
    path: path.join(__dirname, "dist"),
    filename: "app.js",
  },
};
