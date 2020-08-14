import { combineReducers } from "redux";
import countriesReducer from "../store/reducers/countries";
import timeseriesReducer from "../store/reducers/timeseries";
import radialchartReducer from "../store/reducers/radialchart";
import heatmapReducer from "../store/reducers/heatmap";
import stackedReducer from "../store/reducers/stackedmap";
import scatterPlotReducer from "../store/reducers/scatterplot";

const reducerRoot = combineReducers({
  countriesReducer,
  timeseriesReducer,
  radialchartReducer,
  heatmapReducer,
  stackedReducer,
  scatterPlotReducer,
});

export default reducerRoot;
