import * as React from "react";
import { useState, useCallback, useEffect } from "react";

import Timer from "./src/pages/Timer";

const Pomodoro = () => {
  const [flag, setFlag] = useState(true);
  const [count, setCount] = useState(1);
  const [break_count, setBreakCount] = useState(1);
  const [label_value, setLabelValue] = useState("");
  const [default_miunute, setMinute] = useState("25");
  const [default_second, setSecond] = useState("00");
  const [default_break_minute, setBminute] = useState("00");
  const [default_break_second, setBsecond] = useState("10");

  useEffect(() => {
    let tmp = localStorage.getItem("count");
    let tmp2 = localStorage.getItem("break_count");
    if (tmp && tmp2) {
      setCount(parseInt(tmp));
      setBreakCount(parseInt(tmp2));
    } else {
      localStorage.setItem("count", "1");
      localStorage.setItem("break_count", "1");
    }
  }, []);

  useEffect(() => {
    console.log(flag, "pomodoro_flag");
    if (flag) {
      setLabelValue(`#${count} study!!`);
    } else {
      setLabelValue(`#${break_count} break~~`);
    }
  }, [flag, count, break_count]);

  const onBtnClick = useCallback(
    (e: React.MouseEvent) => {
      if (e.currentTarget.innerHTML === "Study") {
        setFlag(true);
      } else {
        setFlag(false);
      }
    },
    [flag]
  );

  const onChangeflag = (e: boolean) => {
    if (!e) {
      // false로 오면 study 끝난거임
      localStorage.setItem("count", String(count + 1));
      setCount(count + 1);
      setFlag(true);
    } else {
      localStorage.setItem("break_count", String(break_count + 1));
      setBreakCount(break_count + 1);
      setFlag(true);
    }
  };

  const onChangeTime = (time: string, val: number) => {
    if (flag) {
      // study면
      if (val === 1) {
        setMinute(time);
      } else {
        setSecond(time);
      }
    } else {
      if (val === 1) {
        setBminute(time);
      } else {
        setBsecond(time);
      }
    }
  };

  return (
    <>
      <label>{label_value}</label>
      <div className="state">
        <button onClick={onBtnClick}>Study</button>
        <button onClick={onBtnClick}>Break</button>
      </div>

      <Timer
        flag={flag}
        onChangeflag={onChangeflag}
        onChangeTime={onChangeTime}
        default_minute={flag ? default_miunute : default_break_minute}
        default_second={flag ? default_second : default_break_second}
      />
    </>
  );
};

export default Pomodoro;
