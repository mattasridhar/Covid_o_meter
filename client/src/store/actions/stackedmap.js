import {
  FETCH_STACKED_MAP_REQUEST,
  FETCH_STACKED_MAP_SUCCESS,
  FETCH_STACKED_MAP_FAILURE,
} from "../types/stackedmap";

export const fetchStackedMapRequest = () => {
  return {
    type: FETCH_STACKED_MAP_REQUEST,
  };
};

export const fetchStackedMapSuccess = (stackedMap) => {
  return {
    type: FETCH_STACKED_MAP_SUCCESS,
    payload: stackedMap,
  };
};

export const fetchStackedMapFailure = (errorMessage) => {
  return {
    type: FETCH_STACKED_MAP_FAILURE,
    payload: errorMessage,
  };
};
