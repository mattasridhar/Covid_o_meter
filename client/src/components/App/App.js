// Core imports
import React, { Suspense } from "react";
import "../../i18n/i18n";
// import logo from "./logo.svg";
import { Provider } from "react-redux";
import store from "../../store/store";

// Custom components imports
import Canvas from "../Canvas/Canvas";

function App() {
  return (
    <Provider store={store}>
      <div>
        {/* <div className="App"> */}
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <Suspense fallback={<div>Loading locales and other Files....</div>}>
          <Canvas />
        </Suspense>
      </div>
    </Provider>
  );
}

export default App;
