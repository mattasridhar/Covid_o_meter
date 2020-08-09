import {
  FETCH_COUNTRIES_REQUEST,
  FETCH_COUNTRIES_SUCCESS,
  FETCH_COUNTRIES_FAILURE,
  FETCH_COUNTRIES_MAP_REQUEST,
  FETCH_COUNTRIES_MAP_SUCCESS,
  FETCH_COUNTRIES_MAP_FAILURE,
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

export const fetchCountriesMapRequest = () => {
  return {
    type: FETCH_COUNTRIES_MAP_REQUEST,
  };
};

export const fetchCountriesMapSuccess = (countriesMap) => {
  return {
    type: FETCH_COUNTRIES_MAP_SUCCESS,
    payload: countriesMap,
  };
};

export const fetchCountriesMapFailure = (errorMessage) => {
  return {
    type: FETCH_COUNTRIES_MAP_FAILURE,
    payload: errorMessage,
  };
};
