// Core imports
import React, { useContext } from "react";
import { ContextPlotData } from "../App/AppContexts";

// DOM imports
import { Hourglass } from "react-spinners-css";
import Typography from "@material-ui/core/Typography";

// Custom component imports
import Localize from "../../i18n/Localize";

// Store imports

export const ScatterPlotVisualization = ({ myStyles }) => {
  // retrieving already stored Image Information
  const plotData = useContext(ContextPlotData);
  const plotGifData = plotData.scatterplotData;

  return (
    <>
      {plotGifData.length === 0 && (
        <>
          <Typography component="h6" variant="h6" color="inherit" noWrap>
            <Localize id="loadingScatterPlot" />
          </Typography>
          <Hourglass color="black" size={50} />
        </>
      )}
      {plotGifData.length !== 0 && (
        <img
          src={`data:image/jpeg;base64,${plotGifData}`}
          className={myStyles}
          alt={"Scatter Plot Gif"}
        ></img>
      )}
    </>
  );
};

export default ScatterPlotVisualization;
