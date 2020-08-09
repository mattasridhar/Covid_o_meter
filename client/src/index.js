// Core imports
import React from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";

// DOM imports
import "./index.css";

// Custom component imports
import App from "./components/App/App";

// Store imports

ReactDOM.render(<App />, document.getElementById("root"));

serviceWorker.unregister();
