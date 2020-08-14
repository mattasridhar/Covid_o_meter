import axios from "axios";
import {
  fetchCountriesRequest,
  fetchCountriesSuccess,
  fetchCountriesFailure,
  fetchCountriesMapRequest,
  fetchCountriesMapSuccess,
  fetchCountriesMapFailure,
} from "../actions/countries";

// Fetches the Gif from the Server
export const fetchCountriesMap = () => {
  return (dispatch) => {
    dispatch(fetchCountriesMapRequest());
    axios({
      url: "http://localhost:2393/api/visualize/worldheatmap/",
      method: "GET",
    })
      .then((response) => {
        console.log("Fetching the World Map Visualization GIF.");
        dispatch(fetchCountriesMapSuccess(response.data));
      })
      .catch((error) => {
        console.log(
          "Fetching the World Map Visualization GIF Failed with error: \n",
          error
        );
        dispatch(fetchCountriesMapFailure(error));
      });
  };
};

// Fetches the list of Covid-19 infected countries list from the Server
export const fetchCountriesList = () => {
  return (dispatch) => {
    dispatch(fetchCountriesRequest());
    axios({
      url: "http://localhost:2393/api/countriesList/",
      method: "GET",
    })
      .then((response) => {
        console.log("Fetching the List of countries.", response);
        dispatch(fetchCountriesSuccess(response.data));
        clearTimeout();
      })
      .catch((error) => {
        console.log("Fetching the Countries List Failed with error: \n", error);
        dispatch(fetchCountriesFailure("error SRI"));
      });
  };
};
