// Core imports
import React, { Suspense } from "react";
import "../../i18n/i18n";
import { Provider } from "react-redux";

// Custom components imports
import Canvas from "../Canvas/Canvas";

// Store imports
import store from "../../store/store";

function App() {
  return (
    <Provider store={store}>
      <div>
        <Suspense fallback={<div>Loading locales and other Files....</div>}>
          <Canvas />
        </Suspense>
      </div>
    </Provider>
  );
}

export default App;
