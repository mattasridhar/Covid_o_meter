import { createStore, applyMiddleware } from "redux";
import reducerRoot from "./reducerRoot";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

const store = createStore(
  reducerRoot,
  composeWithDevTools(applyMiddleware(thunk))
);

export default store;
