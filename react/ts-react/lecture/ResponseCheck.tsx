import * as React from "react";
import { useState, useRef } from "react";

const ResponseCheck = () => {
  const [state, setState] = useState("waiting");
  const [message, setMessage] = useState("클릭해서 시작하세요");
  const [result, setResult] = useState<number[]>([]);
  const timeout = useRef<number | null>(null);
  const startTime = useRef(0);
  const endTime = useRef(0);

  const onClickScreen = () => {
    if (state === "waiting") {
      timeout.current = window.setTimeout(() => {
        setState("now");
        setMessage("지금 클릭");
        startTime.current = new Date().getTime();
      }, Math.floor(Math.random() * 1000) + 2000);
    }
  };

  return (
    <>
      <div id="screen" className={state} onClick={onClickScreen}>
        {message}
      </div>
      {renderAverage()}
    </>
  );
};
export default ResponseCheck;
