import {
  FETCH_RADIALCHART_FAILURE,
  FETCH_RADIALCHART_SUCCESS,
  FETCH_RADIALCHART_REQUEST,
} from "../types/radialchart";

const initState = {
  radialloading: false,
  radialchartMap: "",
  errorMessage: "",
};

const radialchartReducer = (state = initState, action) => {
  switch (action.type) {
    case FETCH_RADIALCHART_REQUEST:
      return {
        ...state,
        radialloading: true,
      };
    case FETCH_RADIALCHART_SUCCESS:
      return {
        ...state,
        radialloading: false,
        radialchartMap: action.payload,
        errorMessage: "",
      };
    case FETCH_RADIALCHART_FAILURE:
      return {
        ...state,
        radialloading: false,
        radialchartMap: "",
        errorMessage: `Error: ${action.payload}`,
      };
    default:
      return state;
  }
};

export default radialchartReducer;
