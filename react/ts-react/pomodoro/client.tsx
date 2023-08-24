import * as React from "react";
import Pomodoro from "./Pomodoro";
const ReactDom = require("react-dom/client");

ReactDom.createRoot(document.querySelector("#root")).render(<Pomodoro />);
