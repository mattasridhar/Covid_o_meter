import {
  FETCH_RADIALCHART_REQUEST,
  FETCH_RADIALCHART_SUCCESS,
  FETCH_RADIALCHART_FAILURE,
} from "../types/radialchart";

export const fetchRadialChartRequest = () => {
  return {
    type: FETCH_RADIALCHART_REQUEST,
  };
};

export const fetchRadialChartSuccess = (radialchartMap) => {
  return {
    type: FETCH_RADIALCHART_SUCCESS,
    payload: radialchartMap,
  };
};

export const fetchRadialChartFailure = (errorMessage) => {
  return {
    type: FETCH_RADIALCHART_FAILURE,
    payload: errorMessage,
  };
};
