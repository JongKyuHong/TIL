import React, { Component } from "react";
import ReactDom from "react-dom/client";
import Pomodoro from "./Pomodoro";

ReactDom.createRoot(document.querySelector("#root")).render(<Pomodoro />);
