import {
  FETCH_TIMESERIES_MAP_REQUEST,
  FETCH_TIMESERIES_MAP_FAILURE,
  FETCH_TIMESERIES_MAP_SUCCESS,
} from "../types/timeseries";

const initState = {
  timeseriesloading: false,
  timeseriesMap: "",
  errorMessage: "",
};

const timeseriesReducer = (state = initState, action) => {
  switch (action.type) {
    case FETCH_TIMESERIES_MAP_REQUEST:
      return {
        ...state,
        timeseriesloading: true,
      };
    case FETCH_TIMESERIES_MAP_SUCCESS:
      return {
        ...state,
        timeseriesloading: false,
        timeseriesMap: action.payload,
        errorMessage: "",
      };
    case FETCH_TIMESERIES_MAP_FAILURE:
      return {
        ...state,
        timeseriesloading: false,
        timeseriesMap: "",
        errorMessage: `Error: ${action.payload}`,
      };
    default:
      return state;
  }
};

export default timeseriesReducer;
