const {
  FETCH_COUNTRIES_REQUEST,
  FETCH_COUNTRIES_SUCCESS,
  FETCH_COUNTRIES_FAILURE,
} = require("../types/countries");

const initState = {
  loading: false,
  countriesList: [],
  errorMessage: "",
};

const countriesReducer = (state = initState, action) => {
  switch (action.type) {
    case FETCH_COUNTRIES_REQUEST:
      return {
        ...state,
        loading: true,
      };
    case FETCH_COUNTRIES_SUCCESS:
      return {
        ...state,
        loading: false,
        countriesList: action.payload,
        errorMessage: "",
      };
    case FETCH_COUNTRIES_FAILURE:
      return {
        ...state,
        loading: false,
        countriesList: [],
        errorMessage: `Error: ${action.payload}`,
      };
    default:
      return state;
  }
};

export default countriesReducer;
