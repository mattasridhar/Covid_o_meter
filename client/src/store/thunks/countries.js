import axios from "axios";
import {
  fetchCountriesRequest,
  fetchCountriesSuccess,
  fetchCountriesFailure,
} from "../actions/countries";

// axios.defaults.headers.post["Content-Type"] = "application/json;charset=utf-8";
// axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
/* export const fetchCountries = () => {
  return (dispatch) => {
    dispatch(fetchCountriesRequest());
    axios
      .get("http://localhost:2393/api/hello/?format=json")
      .then((response) => {
        console.log("Thunk country resp: ", response);
        dispatch(fetchCountriesSuccess(["SRIDHAR"]));
      })
      .catch((error) => {
        console.log("Thunk error: ", error);
        dispatch(fetchCountriesFailure("error SRI"));
      });
  };
}; */

/* export const fetchCountries = () => {
  return (dispatch) => {
    dispatch(fetchCountriesRequest());
    axios({
      url: "http://localhost:2393/api/visualize/",
      method: "GET",
      // responseType: "blob",
    })
      .then((response) => {
        // const file = new Blob([response.data], { type: "image/gif" });
        // const url = URL.createObjectURL(blob);
        console.log("Thunk country resp: ", response);
        // console.log("Think FileSize: ", file.size); // !!! this line
        dispatch(fetchCountriesSuccess([response.data]));
      })
      .catch((error) => {
        console.log("Thunk error: ", error);
        dispatch(fetchCountriesFailure("error SRI"));
      });
  };
}; */

export const fetchCountries = () => {
  return (dispatch) => {
    dispatch(fetchCountriesRequest());
    setTimeout(() => {
      console.log("Waiting...");
    }, 2000);
    axios({
      url: "http://localhost:2393/api/countriesList/",
      method: "GET",
      // responseType: "blob",
    })
      .then((response) => {
        // const file = new Blob([response.data], { type: "image/gif" });
        // const url = URL.createObjectURL(blob);
        console.log("Thunk countryList resp: ", response);
        // console.log("Think FileSize: ", file.size); // !!! this line
        dispatch(fetchCountriesSuccess([response.data]));
        clearTimeout();
      })
      .catch((error) => {
        console.log("Thunk error: ", error);
        dispatch(fetchCountriesFailure("error SRI"));
      });
  };
};
