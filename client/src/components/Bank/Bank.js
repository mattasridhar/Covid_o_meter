// Core imports
import React from "react";

// DOM imports
import clsx from "clsx";
import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import uiStyles from "../App/UIStyles";
import WorldMapVisualization from "./WorldMapVisualization";
// import { WorldMapVisualization } from "./WorldMapVisualization";

// Custom components imports

const Bank = () => {
  const myStyles = uiStyles();

  return (
    <>
      <Grid container spacing={3}>
        <Grid item xs={12} md={8} lg={9}>
          <Paper className={clsx(myStyles.paper, myStyles.fixedHeight)}>
            <WorldMapVisualization />
          </Paper>
        </Grid>
        <Grid item xs={12} md={4} lg={3}>
          <Paper className={clsx(myStyles.paper, myStyles.fixedHeight)}>
            {/* <Deposits /> */}
          </Paper>
        </Grid>
      </Grid>
      <Box pt={4}>{/* <Copyright /> */}</Box>
    </>
  );
};

export default Bank;
