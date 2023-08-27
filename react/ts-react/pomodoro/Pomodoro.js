"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var React = require("react");
var react_1 = require("react");
var Timer_1 = require("./src/pages/Timer");
var Pomodoro = function () {
    var _a = (0, react_1.useState)(true), flag = _a[0], setFlag = _a[1];
    var _b = (0, react_1.useState)(1), count = _b[0], setCount = _b[1];
    var _c = (0, react_1.useState)(1), break_count = _c[0], setBreakCount = _c[1];
    var _d = (0, react_1.useState)(""), label_value = _d[0], setLabelValue = _d[1];
    var _e = (0, react_1.useState)("25"), default_miunute = _e[0], setMinute = _e[1];
    var _f = (0, react_1.useState)("00"), default_second = _f[0], setSecond = _f[1];
    var _g = (0, react_1.useState)("00"), default_break_minute = _g[0], setBminute = _g[1];
    var _h = (0, react_1.useState)("10"), default_break_second = _h[0], setBsecond = _h[1];
    (0, react_1.useEffect)(function () {
        var tmp = localStorage.getItem("count");
        var tmp2 = localStorage.getItem("break_count");
        if (tmp && tmp2) {
            setCount(parseInt(tmp));
            setBreakCount(parseInt(tmp2));
        }
        else {
            localStorage.setItem("count", "1");
            localStorage.setItem("break_count", "1");
        }
    }, []);
    (0, react_1.useEffect)(function () {
        console.log(flag, "pomodoro_flag");
        if (flag) {
            setLabelValue("#".concat(count, " study!!"));
        }
        else {
            setLabelValue("#".concat(break_count, " break~~"));
        }
    }, [flag, count, break_count]);
    var onBtnClick = (0, react_1.useCallback)(function (e) {
        if (e.currentTarget.innerHTML === "Study") {
            setFlag(true);
        }
        else {
            setFlag(false);
        }
    }, [flag]);
    var onChangeflag = function (e) {
        if (!e) {
            // false로 오면 study 끝난거임
            localStorage.setItem("count", String(count + 1));
            setCount(count + 1);
            setFlag(true);
        }
        else {
            localStorage.setItem("break_count", String(break_count + 1));
            setBreakCount(break_count + 1);
            setFlag(true);
        }
    };
    var onChangeTime = function (time, val) {
        if (flag) {
            // study면
            if (val === 1) {
                setMinute(time);
            }
            else {
                setSecond(time);
            }
        }
        else {
            if (val === 1) {
                setBminute(time);
            }
            else {
                setBsecond(time);
            }
        }
    };
    return (React.createElement(React.Fragment, null,
        React.createElement("label", null, label_value),
        React.createElement("div", { className: "state" },
            React.createElement("button", { onClick: onBtnClick }, "Study"),
            React.createElement("button", { onClick: onBtnClick }, "Break")),
        React.createElement(Timer_1.default, { flag: flag, onChangeflag: onChangeflag, onChangeTime: onChangeTime, default_minute: flag ? default_miunute : default_break_minute, default_second: flag ? default_second : default_break_second })));
};
exports.default = Pomodoro;
