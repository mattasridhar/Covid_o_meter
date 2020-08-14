// Core imports
import React from "react";
import { constants } from "../App/constants";

// DOM imports
import uiStyles from "../App/UIStyles";
import Container from "@material-ui/core/Container";

// Custom component imports
import Bank from "../Bank/Bank";
import Settings from "../Settings/Settings";
import WorldMapVisualization from "../Bank/WorldMapVisualization";
import TimeSeriesVisualization from "../Bank/TimeSeriesVisualization";
import RadialChartVisualization from "../Bank/RadialChartVisualization";
import HeatMapVisualization from "../Bank/HeatMapVisualization";
import StackedMapVisualization from "../Bank/StackedMapVisualization";
import ScatterPlotVisualization from "../Bank/ScatterPlotVisualization";

// Custom components imports

const ContentArea = ({ canvasContext }) => {
  const myStyles = uiStyles();

  // Return the appropriate component based on the Context selected from the Sidebar Panel
  const renderCanvas = () => {
    switch (canvasContext) {
      case constants.content.settings:
        return <Settings />;
      case constants.content.worldMap:
        return <WorldMapVisualization />;
      case constants.content.timeSeries:
        return <TimeSeriesVisualization />;
      case constants.content.radialChart:
        return <RadialChartVisualization />;
      case constants.content.heatMap:
        return <HeatMapVisualization />;
      case constants.content.stackedMap:
        return <StackedMapVisualization />;
      case constants.content.scatterPlot:
        return <ScatterPlotVisualization />;
      case constants.content.bank:
      default:
        return <Bank />;
    }
  };

  return (
    <>
      <main className={myStyles.content}>
        <div className={myStyles.appBarSpacer} />
        <Container maxWidth="lg" className={myStyles.container}>
          {renderCanvas()}
        </Container>
      </main>
    </>
  );
};

export default ContentArea;
