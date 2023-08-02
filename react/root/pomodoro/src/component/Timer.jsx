import React, { useState } from "react";

// const style = {
//   font-size: '120px',

// }

const Timer = () => {
  const [minute, setMinute] = useState("25");
  const [second, setSecond] = useState("00");

  return (
    <div
      style={{
        fontSize: "120px",
        fontWeight: "bold",
        margin: "20px",
        color: "white",
      }}
    >
      {minute}:{second}
    </div>
  );
};

export default Timer;
