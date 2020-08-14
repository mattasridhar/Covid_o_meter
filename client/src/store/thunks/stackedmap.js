import axios from "axios";
import {
  fetchStackedMapSuccess,
  fetchStackedMapRequest,
  fetchStackedMapFailure,
} from "../actions/stackedmap";

// Fetches the Gif from the Server
export const fetchStackedMap = () => {
  return (dispatch) => {
    dispatch(fetchStackedMapRequest());
    axios({
      url: "http://localhost:2393/api/visualize/stackedmap/",
      method: "GET",
    })
      .then((response) => {
        console.log("Fetching the Stacked Map Visualization GIF.");
        dispatch(fetchStackedMapSuccess(response.data));
      })
      .catch((error) => {
        console.log(
          "Fetching the Stacked Map Visualization GIF Failed with error: \n",
          error
        );
        dispatch(fetchStackedMapFailure(error));
      });
  };
};
