import {
  FETCH_COUNTRIES_REQUEST,
  FETCH_COUNTRIES_SUCCESS,
  FETCH_COUNTRIES_FAILURE,
} from "../types/countries";

export const fetchCountriesRequest = () => {
  return {
    type: FETCH_COUNTRIES_REQUEST,
  };
};

export const fetchCountriesSuccess = (countriesList) => {
  return {
    type: FETCH_COUNTRIES_SUCCESS,
    payload: countriesList,
  };
};

export const fetchCountriesFailure = (errorMessage) => {
  return {
    type: FETCH_COUNTRIES_FAILURE,
    payload: errorMessage,
  };
};
