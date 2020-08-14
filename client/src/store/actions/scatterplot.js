import {
  FETCH_SCATTERPLOT_REQUEST,
  FETCH_SCATTERPLOT_SUCCESS,
  FETCH_SCATTERPLOT_FAILURE,
} from "../types/scatterplot";

export const fetchScatterPlotRequest = () => {
  return {
    type: FETCH_SCATTERPLOT_REQUEST,
  };
};

export const fetchScatterPlotSuccess = (scatterPlot) => {
  return {
    type: FETCH_SCATTERPLOT_SUCCESS,
    payload: scatterPlot,
  };
};

export const fetchScatterPlotFailure = (errorMessage) => {
  return {
    type: FETCH_SCATTERPLOT_FAILURE,
    payload: errorMessage,
  };
};
