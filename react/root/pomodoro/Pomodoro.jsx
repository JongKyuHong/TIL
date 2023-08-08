import React, { useState, useEffect } from "react";
import Timer from "./src/component/Timer";

const Pomodoro = () => {
  const [isSelectedBtn, setSelectedBtn] = useState("Pomodoro");

  // pomodoro button
  // Short Break button
  // Long Break button
  // Pause button
  // timer
  // 넘기기 버튼??

  const style = {
    backgroundColor: "rgb(193, 92, 92)",
    width: "120px",
    height: "30px",
    border: "0px",
    fontSize: "20px",
    fontFamily: "ArialRounded",
    color: "white",
  };

  const btn_style = {
    width: "200px",
    height: "55px",
    color: "rgb(186, 73, 73)",
    fontSize: "30px",
    margin: "20 0 0",
    padding: "0 12",
    border: "none",
    boxShadow: "1px 2px 9px",
    borderRadius: "5px",
  };

  useEffect(() => {
    document.getElementById(isSelectedBtn).style.backgroundColor =
      "rgb(186, 73, 73)";
  }, []);

  const btn_clicked = (e) => {
    if (e.target.innerText.replace(/ /g, "") !== isSelectedBtn) {
      document.getElementById(isSelectedBtn).style.backgroundColor =
        "rgb(193, 92, 92)";
    }
    setSelectedBtn(e.target.innerText.replace(/ /g, ""));
    e.target.style.backgroundColor = "rgb(186, 73, 73)";
  };

  return (
    <div className="root_div">
      <div className="screen">
        <div>
          <button id="Pomodoro" style={style} onClick={btn_clicked}>
            Pomodoro
          </button>
          <button id="ShortBreak" style={style} onClick={btn_clicked}>
            Short Break
          </button>
          <button id="LongBreak" style={style} onClick={btn_clicked}>
            Long Break
          </button>
        </div>
        <Timer></Timer>
        <button style={btn_style}>Start</button>
      </div>
    </div>
  );
};

export default Pomodoro;
