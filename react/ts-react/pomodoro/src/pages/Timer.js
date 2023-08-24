"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var React = require("react");
var react_1 = require("react");
var Timer = function (_a) {
    var flag = _a.flag, onChangeflag = _a.onChangeflag;
    var _b = (0, react_1.useState)("25"), minute = _b[0], setMinute = _b[1];
    var _c = (0, react_1.useState)("00"), second = _c[0], setSecond = _c[1];
    var _d = (0, react_1.useState)("00"), bminute = _d[0], setBminute = _d[1];
    var _e = (0, react_1.useState)("10"), bsecond = _e[0], setBsecond = _e[1];
    var _f = (0, react_1.useState)("Start"), startBtn = _f[0], setStartBtn = _f[1]; // start버튼의 내용
    var timeout = (0, react_1.useRef)(null);
    (0, react_1.useEffect)(function () {
        // componentDidMount, componentDidUpdate 역할(1대1 대응은 아님)
        if (startBtn === "Pause") {
            console.log(flag, "flag");
            if (flag) {
                timeout.current = window.setInterval(function () {
                    if (parseInt(second) === 0 && parseInt(minute) === 0) {
                        clearInterval(timeout.current);
                        onChangeflag(false);
                        setMinute(minute);
                        setSecond(second);
                    }
                    else if (parseInt(second) === 0) {
                        var tmp = String(parseInt(minute) - 1);
                        if (tmp.length < 2) {
                            setMinute("0" + tmp);
                        }
                        else {
                            setMinute(tmp);
                        }
                        setSecond("59");
                        console.log(second, "second");
                    }
                    else {
                        var tmp = String(parseInt(second) - 1);
                        if (tmp.length < 2) {
                            setSecond("0".concat(tmp));
                        }
                        else {
                            setSecond(tmp);
                        }
                    }
                }, 1000);
                return function () {
                    // componentWillUnmount 역할
                    clearInterval(timeout.current);
                };
            }
            else {
                timeout.current = window.setInterval(function () {
                    if (parseInt(bsecond) === 0 && parseInt(bminute) === 0) {
                        clearInterval(timeout.current);
                        onChangeflag(true);
                        setBminute(bminute);
                        setBsecond(bsecond);
                    }
                    else if (parseInt(bsecond) === 0) {
                        var tmp = String(parseInt(bminute) - 1);
                        if (tmp.length < 2) {
                            setBminute("0" + tmp);
                        }
                        else {
                            setBminute(tmp);
                        }
                        setBsecond("59");
                        console.log(bsecond, "bsecond");
                    }
                    else {
                        var tmp = String(parseInt(bsecond) - 1);
                        if (tmp.length < 2) {
                            setBsecond("0".concat(tmp));
                        }
                        else {
                            setBsecond(tmp);
                        }
                    }
                }, 1000);
                return function () {
                    // componentWillUnmount 역할
                    clearInterval(timeout.current);
                };
            }
        }
    }, [second, minute, startBtn, bminute, bsecond]);
    var onClickBtn = function () {
        if (startBtn === "Start") {
            setStartBtn("Pause");
        }
        else {
            setStartBtn("Start");
        }
    };
    return (React.createElement(React.Fragment, null,
        React.createElement("div", { className: "timer" },
            React.createElement("div", { className: "minute" }, flag ? minute : bminute),
            React.createElement("div", null, ":"),
            React.createElement("div", { className: "second" }, flag ? second : bsecond)),
        React.createElement("button", { className: "start_button", onClick: onClickBtn }, startBtn)));
};
exports.default = Timer;
