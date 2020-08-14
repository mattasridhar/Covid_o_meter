import {
  FETCH_TIMESERIES_MAP_REQUEST,
  FETCH_TIMESERIES_MAP_SUCCESS,
  FETCH_TIMESERIES_MAP_FAILURE,
} from "../types/timeseries";

export const fetchTimeseriesMapRequest = () => {
  return {
    type: FETCH_TIMESERIES_MAP_REQUEST,
  };
};

export const fetchTimeseriesMapSuccess = (timeseriesMap) => {
  return {
    type: FETCH_TIMESERIES_MAP_SUCCESS,
    payload: timeseriesMap,
  };
};

export const fetchTimeseriesMapFailure = (errorMessage) => {
  return {
    type: FETCH_TIMESERIES_MAP_FAILURE,
    payload: errorMessage,
  };
};
