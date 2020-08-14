import {
  FETCH_HEATMAP_REQUEST,
  FETCH_HEATMAP_SUCCESS,
  FETCH_HEATMAP_FAILURE,
} from "../types/heatmap";

export const fetchHeatMapRequest = () => {
  return {
    type: FETCH_HEATMAP_REQUEST,
  };
};

export const fetchHeatMapSuccess = (heatMap) => {
  return {
    type: FETCH_HEATMAP_SUCCESS,
    payload: heatMap,
  };
};

export const fetchHeatMapFailure = (errorMessage) => {
  return {
    type: FETCH_HEATMAP_FAILURE,
    payload: errorMessage,
  };
};
