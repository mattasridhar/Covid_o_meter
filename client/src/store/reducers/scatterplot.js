import {
  FETCH_SCATTERPLOT_REQUEST,
  FETCH_SCATTERPLOT_FAILURE,
  FETCH_SCATTERPLOT_SUCCESS,
} from "../types/scatterplot";

const initState = {
  scatterloading: false,
  scatterPlot: "",
  errorMessage: "",
};

const scatterPlotReducer = (state = initState, action) => {
  switch (action.type) {
    case FETCH_SCATTERPLOT_REQUEST:
      return {
        ...state,
        scatterloading: true,
      };
    case FETCH_SCATTERPLOT_SUCCESS:
      return {
        ...state,
        scatterloading: false,
        scatterPlot: action.payload,
        errorMessage: "",
      };
    case FETCH_SCATTERPLOT_FAILURE:
      return {
        ...state,
        scatterloading: false,
        scatterPlot: "",
        errorMessage: `Error: ${action.payload}`,
      };
    default:
      return state;
  }
};

export default scatterPlotReducer;
