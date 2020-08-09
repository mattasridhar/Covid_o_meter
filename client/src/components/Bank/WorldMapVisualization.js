// Core imports
import React, { useContext } from "react";
import { ContextPlotImages } from "../App/AppContexts";

// DOM imports
import { Hourglass } from "react-spinners-css";
import Typography from "@material-ui/core/Typography";

// Custom component imports
import Localize from "../../i18n/Localize";

// Store imports

export const WorldMapVisualization = ({ myStyles }) => {
  // retrieving already stored Image Information
  let plotGifData = useContext(ContextPlotImages);

  return (
    <>
      {plotGifData.length === 0 && (
        <>
          <Typography component="h6" variant="h6" color="inherit" noWrap>
            <Localize id="loadingMap" />
          </Typography>
          <Hourglass color="black" size={50} />
        </>
      )}
      {plotGifData.length !== 0 && (
        <img
          src={`data:image/jpeg;base64,${plotGifData}`}
          className={myStyles}
          alt={"WorldMap Gif"}
        ></img>
      )}
    </>
  );
};

export default WorldMapVisualization;
