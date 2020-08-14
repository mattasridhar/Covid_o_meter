// Core imports
import React from "react";

// DOM imports
import clsx from "clsx";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import uiStyles from "../App/UIStyles";
import Divider from "@material-ui/core/Divider";
import Typography from "@material-ui/core/Typography";

// Custom components imports
import WorldMapVisualization from "./WorldMapVisualization";
import Localize from "../../i18n/Localize";
import TimeSeriesVisualization from "./TimeSeriesVisualization";
import RadialChartVisualization from "./RadialChartVisualization";
import HeatMapVisualization from "./HeatMapVisualization";
import StackedMapVisualization from "./StackedMapVisualization";
import ScatterPlotVisualization from "./ScatterPlotVisualization";

const Bank = () => {
  const myStyles = clsx(uiStyles().paper, uiStyles().fixedHeight);

  return (
    <>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8} lg={9}>
          <Typography variant="subtitle1" gutterBottom>
            <Localize id="worldMapTitle" />
          </Typography>
          <Divider
            className={myStyles.divider}
            style={{ marginBottom: "12px" }}
          />
          <Paper className={myStyles}>
            <WorldMapVisualization myStyles={myStyles} />
          </Paper>
        </Grid>

        <Grid item xs={12} md={8} lg={9}>
          <Typography variant="subtitle1" gutterBottom>
            <Localize id="timeSeriesTitle" />
          </Typography>
          <Divider
            className={myStyles.divider}
            style={{ marginBottom: "12px" }}
          />
          <Paper className={myStyles}>
            <TimeSeriesVisualization myStyles={myStyles} />
          </Paper>
        </Grid>

        <Grid item xs={12} md={8} lg={9}>
          <Typography variant="subtitle1" gutterBottom>
            <Localize id="radialChartTitle" />
          </Typography>
          <Divider
            className={myStyles.divider}
            style={{ marginBottom: "12px" }}
          />
          <Paper className={myStyles}>
            <RadialChartVisualization myStyles={myStyles} />
          </Paper>
        </Grid>

        <Grid item xs={12} md={8} lg={9}>
          <Typography variant="subtitle1" gutterBottom>
            <Localize id="heatTitle" />
          </Typography>
          <Divider
            className={myStyles.divider}
            style={{ marginBottom: "12px" }}
          />
          <Paper className={myStyles}>
            <HeatMapVisualization myStyles={myStyles} />
          </Paper>
        </Grid>

        <Grid item xs={12} md={8} lg={9}>
          <Typography variant="subtitle1" gutterBottom>
            <Localize id="stackedTitle" />
          </Typography>
          <Divider
            className={myStyles.divider}
            style={{ marginBottom: "12px" }}
          />
          <Paper className={myStyles}>
            <StackedMapVisualization myStyles={myStyles} />
          </Paper>
        </Grid>

        <Grid item xs={12} md={8} lg={9}>
          <Typography variant="subtitle1" gutterBottom>
            <Localize id="scatterPlotTitle" />
          </Typography>
          <Divider
            className={myStyles.divider}
            style={{ marginBottom: "12px" }}
          />
          <Paper className={myStyles}>
            <ScatterPlotVisualization myStyles={myStyles} />
          </Paper>
        </Grid>
      </Grid>
    </>
  );
};

export default Bank;
