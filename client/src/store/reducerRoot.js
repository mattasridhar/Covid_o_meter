import { combineReducers } from "redux";
import countriesReducer from "../store/reducers/countries";

const reducerRoot = combineReducers({
  countriesReducer,
});

export default reducerRoot;
