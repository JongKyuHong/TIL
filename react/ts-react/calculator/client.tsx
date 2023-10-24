import * as React from "react";
import Calculator from "./Calculator";
const ReactDom = require("react-dom/client");

ReactDom.createRoot(document.querySelector("#root")).render(<Calculator />);
