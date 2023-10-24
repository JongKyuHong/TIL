import * as React from "react";
import { useState } from "react";
import State from "./src/State";

const Calculator = () => {
  const [screen, setScreen] = useState();

  const onClickBtn = (e: React.MouseEvent) => {
    let tmp = e.currentTarget.firstChild;
    console.log(typeof tmp, "tmp");
    setScreen(tmp);
  };

  return (
    <>
      <State />
      <div id="row">
        <button id="num-7" onClick={onClickBtn}>
          7
        </button>
        <button id="num-8" onClick={onClickBtn}>
          8
        </button>
        <button id="num-9" onClick={onClickBtn}>
          9
        </button>
        <button id="divide" onClick={onClickBtn}>
          /
        </button>
      </div>
      <div id="row">
        <button id="num-4" onClick={onClickBtn}>
          4
        </button>
        <button id="num-5" onClick={onClickBtn}>
          5
        </button>
        <button id="num-6" onClick={onClickBtn}>
          6
        </button>
        <button id="multiply" onClick={onClickBtn}>
          X
        </button>
      </div>
      <div id="row">
        <button id="num-1" onClick={onClickBtn}>
          1
        </button>
        <button id="num-2" onClick={onClickBtn}>
          2
        </button>
        <button id="num-3" onClick={onClickBtn}>
          3
        </button>
        <button id="minus" onClick={onClickBtn}>
          -
        </button>
      </div>
      <div id="row">
        <button id="num-0" onClick={onClickBtn}>
          0
        </button>
        <button id="C" onClick={onClickBtn}>
          C
        </button>
        <button id="calculate" onClick={onClickBtn}>
          =
        </button>
        <button id="plus" onClick={onClickBtn}>
          +
        </button>
      </div>
    </>
  );
};

export default Calculator;
