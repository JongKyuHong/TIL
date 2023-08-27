import * as React from "react";
import { useState, useEffect, useRef, useCallback } from "react";

const Timer: React.FunctionComponent<{
  flag: boolean;
  onChangeflag: Function;
  onChangeTime: Function;
  default_minute: string;
  default_second: string;
}> = ({ flag, onChangeflag, onChangeTime, default_minute, default_second }) => {
  console.log(default_minute, default_second, "default");
  const [minute, setMinute] = useState(default_minute);
  const [second, setSecond] = useState(default_second);
  const [startBtn, setStartBtn] = useState("Start");
  const timeout = useRef<number | null>(null);

  useEffect(() => {
    if (startBtn === "Pause") {
      setStartBtn("Start");
    }
    setMinute(default_minute);
    setSecond(default_second);
    clearInterval(timeout.current!);
  }, [flag]);

  useEffect(() => {
    console.log(default_minute, default_second, minute, second, "normal");
    // componentDidMount, componentDidUpdate 역할(1대1 대응은 아님)
    if (startBtn === "Pause") {
      console.log(flag, "flag");
      // if (flag) {
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
    }
  }, [second, minute, startBtn]);

  const onClickBtn = () => {
    if (startBtn === "Start") {
      setStartBtn("Pause");
    } else {
      setStartBtn("Start");
    }
  };

  const onClickMinute = () => {
    // 타임변경
    let set_minute = prompt("분을 입력해 주세요");
    if (set_minute) {
      if (set_minute.length < 2) {
        set_minute = `0${set_minute}`;
      }
      setMinute(set_minute);
      onChangeTime(set_minute, 1);
    } else {
      alert("입력이 올바르지 않습니다.");
    }
  };

  const onClickSecond = () => {
    let set_second = prompt("초를 입력해 주세요");
    if (set_second) {
      if (set_second.length < 2) {
        set_second = `0${set_second}`;
      }
      setSecond(set_second);
      onChangeTime(set_second, 0);
    } else {
      alert("입력이 올바르지 않습니다.");
    }
  };
  return (
    <>
      <div className="timer">
        <div className="minute" onClick={onClickMinute}>
          {minute}
        </div>
        <div>:</div>
        <div className="second" onClick={onClickSecond}>
          {second}
        </div>
      </div>
      <button className="start_button" onClick={onClickBtn}>
        {startBtn}
      </button>
    </>
  );
};

export default Timer;
