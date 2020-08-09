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
        {/* <Grid item xs={12} md={4} lg={3}>
          <Paper className={myStyles}> Other Components </Paper>
        </Grid> */}
      </Grid>
    </>
  );
};

export default Bank;
