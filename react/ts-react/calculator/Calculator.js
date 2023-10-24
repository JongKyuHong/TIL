"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var React = require("react");
var react_1 = require("react");
var State_1 = require("./src/State");
var Calculator = function () {
    var _a = (0, react_1.useState)(""), screen = _a[0], setScreen = _a[1];
    var onClickBtn = function (e) {
        var tmp = e.currentTarget.firstChild;
        console.log(typeof tmp, "tmp");
        // setScreen(tmp);
    };
    return (React.createElement(React.Fragment, null,
        React.createElement(State_1.default, null),
        React.createElement("div", { id: "row" },
            React.createElement("button", { id: "num-7", onClick: onClickBtn }, "7"),
            React.createElement("button", { id: "num-8", onClick: onClickBtn }, "8"),
            React.createElement("button", { id: "num-9", onClick: onClickBtn }, "9"),
            React.createElement("button", { id: "divide", onClick: onClickBtn }, "/")),
        React.createElement("div", { id: "row" },
            React.createElement("button", { id: "num-4", onClick: onClickBtn }, "4"),
            React.createElement("button", { id: "num-5", onClick: onClickBtn }, "5"),
            React.createElement("button", { id: "num-6", onClick: onClickBtn }, "6"),
            React.createElement("button", { id: "multiply", onClick: onClickBtn }, "X")),
        React.createElement("div", { id: "row" },
            React.createElement("button", { id: "num-1", onClick: onClickBtn }, "1"),
            React.createElement("button", { id: "num-2", onClick: onClickBtn }, "2"),
            React.createElement("button", { id: "num-3", onClick: onClickBtn }, "3"),
            React.createElement("button", { id: "minus", onClick: onClickBtn }, "-")),
        React.createElement("div", { id: "row" },
            React.createElement("button", { id: "num-0", onClick: onClickBtn }, "0"),
            React.createElement("button", { id: "C", onClick: onClickBtn }, "C"),
            React.createElement("button", { id: "calculate", onClick: onClickBtn }, "="),
            React.createElement("button", { id: "plus", onClick: onClickBtn }, "+"))));
};
exports.default = Calculator;
