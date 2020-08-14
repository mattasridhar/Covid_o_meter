import axios from "axios";
import {
  fetchTimeseriesMapRequest,
  fetchTimeseriesMapSuccess,
  fetchTimeseriesMapFailure,
} from "../actions/timeseries";

// Fetches the Gif from the Server
export const fetchTimeSeriesMap = () => {
  return (dispatch) => {
    dispatch(fetchTimeseriesMapRequest());
    axios({
      url: "http://localhost:2393/api/visualize/timeseries/",
      method: "GET",
    })
      .then((response) => {
        console.log("Fetching the Time Series Visualization GIF.");
        dispatch(fetchTimeseriesMapSuccess(response.data));
      })
      .catch((error) => {
        console.log(
          "Fetching the Time Series Visualization GIF Failed with error: \n",
          error
        );
        dispatch(fetchTimeseriesMapFailure(error));
      });
  };
};
