import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./components/App/App";
import * as serviceWorker from "./serviceWorker";
// import { createStore, applyMiddleware } from 'redux';
// import { Provider } from 'react-redux';
// import reducerSet from './store/reducers'
// import thunk from 'redux-thunk';

// const store = createStore(reducerSet, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());

ReactDOM.render(
  // <React.StrictMode>
  // <Provider store={store}>
  <App />,
  // </Provider>,
  // </React.StrictMode>,
  document.getElementById("root")
);

serviceWorker.unregister();
