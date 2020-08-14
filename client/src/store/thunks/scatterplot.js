import axios from "axios";
import {
  fetchScatterPlotRequest,
  fetchScatterPlotSuccess,
  fetchScatterPlotFailure,
} from "../actions/scatterplot";

// Fetches the Gif from the Server
export const fetchScatterPlot = () => {
  return (dispatch) => {
    dispatch(fetchScatterPlotRequest());
    axios({
      url: "http://localhost:2393/api/visualize/scattermap/",
      method: "GET",
    })
      .then((response) => {
        console.log("Fetching the Scatter Plot Visualization GIF.");
        dispatch(fetchScatterPlotSuccess(response.data));
      })
      .catch((error) => {
        console.log(
          "Fetching the Scatter Plot Visualization GIF Failed with error: \n",
          error
        );
        dispatch(fetchScatterPlotFailure(error));
      });
  };
};
