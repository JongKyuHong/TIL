"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var React = require("react");
var react_1 = require("react");
var Timer = function (_a) {
    var flag = _a.flag, onChangeflag = _a.onChangeflag, onChangeTime = _a.onChangeTime, default_minute = _a.default_minute, default_second = _a.default_second;
    console.log(default_minute, default_second, "default");
    var _b = (0, react_1.useState)(default_minute), minute = _b[0], setMinute = _b[1];
    var _c = (0, react_1.useState)(default_second), second = _c[0], setSecond = _c[1];
    // const [minute, setMinute] = useState("25");
    // const [second, setSecond] = useState("00");
    // const [bminute, setBminute] = useState("00");
    // const [bsecond, setBsecond] = useState("10");
    var _d = (0, react_1.useState)("Start"), startBtn = _d[0], setStartBtn = _d[1]; // start버튼의 내용
    var timeout = (0, react_1.useRef)(null);
    (0, react_1.useEffect)(function () {
        if (startBtn === "Pause") {
            setStartBtn("Start");
        }
        setMinute(default_minute);
        setSecond(default_second);
        clearInterval(timeout.current);
    }, [flag]);
    (0, react_1.useEffect)(function () {
        console.log(default_minute, default_second, minute, second, "normal");
        // componentDidMount, componentDidUpdate 역할(1대1 대응은 아님)
        if (startBtn === "Pause") {
            console.log(flag, "flag");
            // if (flag) {
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
            // } else {
            //   timeout.current = window.setInterval(() => {
            //     if (parseInt(bsecond) === 0 && parseInt(bminute) === 0) {
            //       clearInterval(timeout.current!);
            //       onChangeflag(true);
            //       setBminute(bminute);
            //       setBsecond(bsecond);
            //     } else if (parseInt(bsecond) === 0) {
            //       let tmp = String(parseInt(bminute) - 1);
            //       if (tmp.length < 2) {
            //         setBminute("0" + tmp);
            //       } else {
            //         setBminute(tmp);
            //       }
            //       setBsecond("59");
            //       console.log(bsecond, "bsecond");
            //     } else {
            //       let tmp = String(parseInt(bsecond) - 1);
            //       if (tmp.length < 2) {
            //         setBsecond(`0${tmp}`);
            //       } else {
            //         setBsecond(tmp);
            //       }
            //     }
            //   }, 1000);
            //   return () => {
            //     // componentWillUnmount 역할
            //     clearInterval(timeout.current!);
            //   };
            // }
        }
    }, [second, minute, startBtn]); // , bminute, bsecond
    var onClickBtn = function () {
        if (startBtn === "Start") {
            setStartBtn("Pause");
        }
        else {
            setStartBtn("Start");
        }
    };
    var onClickMinute = function () {
        // 타임변경
        var set_minute = prompt("분을 입력해 주세요");
        if (set_minute) {
            if (set_minute.length < 2) {
                set_minute = "0".concat(set_minute);
            }
            setMinute(set_minute);
            onChangeTime(set_minute, 1);
        }
        else {
            alert("입력이 올바르지 않습니다.");
        }
    };
    var onClickSecond = function () {
        var set_second = prompt("초를 입력해 주세요");
        if (set_second) {
            if (set_second.length < 2) {
                set_second = "0".concat(set_second);
            }
            setSecond(set_second);
            onChangeTime(set_second, 0);
        }
        else {
            alert("입력이 올바르지 않습니다.");
        }
    };
    // {/* {flag ? minute : bminute} */}
    // {/* {flag ? second : bsecond} */}
    return (React.createElement(React.Fragment, null,
        React.createElement("div", { className: "timer" },
            React.createElement("div", { className: "minute", onClick: onClickMinute }, minute),
            React.createElement("div", null, ":"),
            React.createElement("div", { className: "second", onClick: onClickSecond }, second)),
        React.createElement("button", { className: "start_button", onClick: onClickBtn }, startBtn)));
};
exports.default = Timer;
