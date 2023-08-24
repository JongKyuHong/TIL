"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var path = require("path");
var ReactRefreshPlugin = require("@pmmmwh/react-refresh-webpack-plugin");
var ForkTsCheckerWebpackPlugin = require("fork-ts-checker-webpack-plugin");
var config = {
    name: "pomodoro",
    mode: "development",
    devtool: "eval",
    resolve: {
        extensions: [".js", ".jsx", ".tsx", ".ts"],
    },
    entry: {
        app: "./client",
    },
    module: {
        rules: [
            {
                loader: "babel-loader",
                options: { plugins: ["react-refresh/babel"] },
            },
            {
                test: /\.tsx?$/,
                loader: "ts-loader",
                exclude: path.join(__dirname, "node_modules"),
            },
        ],
    },
    plugins: [new ReactRefreshPlugin(), new ForkTsCheckerWebpackPlugin()],
    output: {
        path: path.join(__dirname, "dist"),
        filename: "[name].js",
        publicPath: "/dist/",
    },
    devServer: {
        devMiddleware: { publicPath: "/dist" },
        static: { directory: path.resolve(__dirname) },
        hot: true,
    },
};
exports.default = config;
