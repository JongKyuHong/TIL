import * as React from "react";
import { useState, useEffect, useRef, useCallback } from "react";

const Timer: React.FunctionComponent<{
  flag: boolean;
  onChangeflag: Function;
}> = ({ flag, onChangeflag }) => {
  const [minute, setMinute] = useState("25");
  const [second, setSecond] = useState("00");
  const [bminute, setBminute] = useState("00");
  const [bsecond, setBsecond] = useState("10");
  const [startBtn, setStartBtn] = useState("Start"); // start버튼의 내용
  const timeout = useRef<number | null>(null);

  useEffect(() => {
    // componentDidMount, componentDidUpdate 역할(1대1 대응은 아님)
    if (startBtn === "Pause") {
      console.log(flag, "flag");
      if (flag) {
        timeout.current = window.setInterval(() => {
          if (parseInt(second) === 0 && parseInt(minute) === 0) {
            clearInterval(timeout.current!);
            onChangeflag(false);
            setMinute(minute);
            setSecond(second);
          } else if (parseInt(second) === 0) {
            let tmp = String(parseInt(minute) - 1);
            if (tmp.length < 2) {
              setMinute("0" + tmp);
            } else {
              setMinute(tmp);
            }
            setSecond("59");
            console.log(second, "second");
          } else {
            let tmp = String(parseInt(second) - 1);
            if (tmp.length < 2) {
              setSecond(`0${tmp}`);
            } else {
              setSecond(tmp);
            }
          }
        }, 1000);
        return () => {
          // componentWillUnmount 역할
          clearInterval(timeout.current!);
        };
      } else {
        timeout.current = window.setInterval(() => {
          if (parseInt(bsecond) === 0 && parseInt(bminute) === 0) {
            clearInterval(timeout.current!);
            onChangeflag(true);
            setBminute(bminute);
            setBsecond(bsecond);
          } else if (parseInt(bsecond) === 0) {
            let tmp = String(parseInt(bminute) - 1);
            if (tmp.length < 2) {
              setBminute("0" + tmp);
            } else {
              setBminute(tmp);
            }
            setBsecond("59");
            console.log(bsecond, "bsecond");
          } else {
            let tmp = String(parseInt(bsecond) - 1);
            if (tmp.length < 2) {
              setBsecond(`0${tmp}`);
            } else {
              setBsecond(tmp);
            }
          }
        }, 1000);
        return () => {
          // componentWillUnmount 역할
          clearInterval(timeout.current!);
        };
      }
    }
  }, [second, minute, startBtn, bminute, bsecond]);

  const onClickBtn = () => {
    if (startBtn === "Start") {
      setStartBtn("Pause");
    } else {
      setStartBtn("Start");
    }
  };

  return (
    <>
      <div className="timer">
        <div className="minute">{flag ? minute : bminute}</div>
        <div>:</div>
        <div className="second">{flag ? second : bsecond}</div>
      </div>
      <button className="start_button" onClick={onClickBtn}>
        {startBtn}
      </button>
    </>
  );
};

export default Timer;
