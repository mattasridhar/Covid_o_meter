import axios from "axios";
import {
  fetchRadialChartRequest,
  fetchRadialChartSuccess,
  fetchRadialChartFailure,
} from "../actions/radialchart";

// Fetches the Gif from the Server
export const fetchRadialChartMap = () => {
  return (dispatch) => {
    dispatch(fetchRadialChartRequest());
    axios({
      url: "http://localhost:2393/api/visualize/radialchart/",
      method: "GET",
    })
      .then((response) => {
        console.log("Fetching the Radial Chart Visualization GIF.");
        dispatch(fetchRadialChartSuccess(response.data));
      })
      .catch((error) => {
        console.log(
          "Fetching the Radial Chart Visualization GIF Failed with error: \n",
          error
        );
        dispatch(fetchRadialChartFailure(error));
      });
  };
};
