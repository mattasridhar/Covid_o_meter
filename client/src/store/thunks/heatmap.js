import axios from "axios";
import {
  fetchHeatMapRequest,
  fetchHeatMapSuccess,
  fetchHeatMapFailure,
} from "../actions/heatmap";

// Fetches the Gif from the Server
export const fetchHeatMap = () => {
  return (dispatch) => {
    dispatch(fetchHeatMapRequest());
    axios({
      url: "http://localhost:2393/api/visualize/heatmap/",
      method: "GET",
    })
      .then((response) => {
        console.log("Fetching the Heat Map Visualization GIF.");
        dispatch(fetchHeatMapSuccess(response.data));
      })
      .catch((error) => {
        console.log(
          "Fetching the Heat Map Visualization GIF Failed with error: \n",
          error
        );
        dispatch(fetchHeatMapFailure(error));
      });
  };
};
