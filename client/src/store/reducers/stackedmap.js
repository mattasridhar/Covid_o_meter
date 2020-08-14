import {
  FETCH_STACKED_MAP_REQUEST,
  FETCH_STACKED_MAP_SUCCESS,
  FETCH_STACKED_MAP_FAILURE,
} from "../types/stackedmap";

const initState = {
  stackedloading: false,
  stackedMap: "",
  errorMessage: "",
};

const stackedReducer = (state = initState, action) => {
  switch (action.type) {
    case FETCH_STACKED_MAP_REQUEST:
      return {
        ...state,
        stackedloading: true,
      };
    case FETCH_STACKED_MAP_SUCCESS:
      return {
        ...state,
        stackedloading: false,
        stackedMap: action.payload,
        errorMessage: "",
      };
    case FETCH_STACKED_MAP_FAILURE:
      return {
        ...state,
        stackedloading: false,
        stackedMap: "",
        errorMessage: `Error: ${action.payload}`,
      };
    default:
      return state;
  }
};

export default stackedReducer;
