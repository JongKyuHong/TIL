const React = require("react");
const ReactDom = require("react-dom/client");
import WordRelay from "./WordRelay";

//ReactDOM.render(<WordRelay />, document.querySelector("#root"));
ReactDom.createRoot(document.querySelector("#root")).render(<WordRelay />);
