import {
  FETCH_HEATMAP_REQUEST,
  FETCH_HEATMAP_SUCCESS,
  FETCH_HEATMAP_FAILURE,
} from "../types/heatmap";

const initState = {
  heatloading: false,
  heatMap: "",
  errorMessage: "",
};

const heatmapReducer = (state = initState, action) => {
  switch (action.type) {
    case FETCH_HEATMAP_REQUEST:
      return {
        ...state,
        heatloading: true,
      };
    case FETCH_HEATMAP_SUCCESS:
      return {
        ...state,
        heatloading: false,
        heatMap: action.payload,
        errorMessage: "",
      };
    case FETCH_HEATMAP_FAILURE:
      return {
        ...state,
        heatloading: false,
        heatMap: "",
        errorMessage: `Error: ${action.payload}`,
      };
    default:
      return state;
  }
};

export default heatmapReducer;
