const {
  FETCH_COUNTRIES_REQUEST,
  FETCH_COUNTRIES_SUCCESS,
  FETCH_COUNTRIES_FAILURE,
  FETCH_COUNTRIES_MAP_REQUEST,
  FETCH_COUNTRIES_MAP_SUCCESS,
  FETCH_COUNTRIES_MAP_FAILURE,
} = require("../types/countries");

const initState = {
  loading: false,
  countriesList: [],
  countriesMap: "",
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
    case FETCH_COUNTRIES_MAP_REQUEST:
      return {
        ...state,
        loading: true,
      };
    case FETCH_COUNTRIES_MAP_SUCCESS:
      return {
        ...state,
        loading: false,
        countriesMap: action.payload,
        errorMessage: "",
      };
    case FETCH_COUNTRIES_MAP_FAILURE:
      return {
        ...state,
        loading: false,
        countriesMap: "",
        errorMessage: `Error: ${action.payload}`,
      };
    default:
      return state;
  }
};

export default countriesReducer;
