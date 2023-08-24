import * as React from "react";
import { useState, useCallback, useEffect } from "react";

import Timer from "./src/pages/Timer";

const Pomodoro = () => {
  const [flag, setFlag] = useState(true);
  const [count, setCount] = useState(1);
  const [break_count, setBreakCount] = useState(1);
  const [label_value, setLabelValue] = useState("");

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

  return (
    <>
      <label>{label_value}</label>
      <div className="state">
        <button onClick={onBtnClick}>Study</button>
        <button onClick={onBtnClick}>Break</button>
      </div>
      <Timer flag={flag} onChangeflag={onChangeflag} />
    </>
  );
};

export default Pomodoro;
