// Core imports
import React from "react";
import Localize from "../../i18n/Localize";
import { constants } from "../App/constants";

// DOM imports
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import DashboardIcon from "@material-ui/icons/Dashboard";
import SettingsIcon from "@material-ui/icons/Settings";
import TimelineIcon from "@material-ui/icons/Timeline";
import PublicIcon from "@material-ui/icons/Public";
import TrackChangesIcon from "@material-ui/icons/TrackChanges";
import FilterHdrIcon from "@material-ui/icons/FilterHdr";
import GradientIcon from "@material-ui/icons/Gradient";
import ScatterPlotIcon from "@material-ui/icons/ScatterPlot";
import Divider from "@material-ui/core/Divider";
import IconButton from "@material-ui/core/IconButton";
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft";
import uiStyles from "../App/UIStyles";

const SideBar = ({ handleSidebarToggling, alterCanvas }) => {
  const myStyles = uiStyles();

  return (
    <>
      <div className={myStyles.toolbarIcon}>
        <IconButton onClick={handleSidebarToggling}>
          <ChevronLeftIcon />
        </IconButton>
      </div>
      <Divider />
      <List>
        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.bank);
          }}
        >
          <ListItemIcon>
            <DashboardIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="bank" />} />
        </ListItem>

        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.worldMap);
          }}
        >
          <ListItemIcon>
            <PublicIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="worldMapTitle" />} />
        </ListItem>

        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.timeSeries);
          }}
        >
          <ListItemIcon>
            <TimelineIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="timeSeriesTitle" />} />
        </ListItem>

        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.radialChart);
          }}
        >
          <ListItemIcon>
            <TrackChangesIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="radialChartTitle" />} />
        </ListItem>

        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.heatMap);
          }}
        >
          <ListItemIcon>
            <GradientIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="heatTitle" />} />
        </ListItem>

        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.stackedMap);
          }}
        >
          <ListItemIcon>
            <FilterHdrIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="stackedTitle" />} />
        </ListItem>

        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.scatterPlot);
          }}
        >
          <ListItemIcon>
            <ScatterPlotIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="scatterPlotTitle" />} />
        </ListItem>

        <ListItem
          button
          onClick={() => {
            alterCanvas(constants.content.settings);
          }}
        >
          <ListItemIcon>
            <SettingsIcon />
          </ListItemIcon>
          <ListItemText primary={<Localize id="settings" />} />
        </ListItem>
      </List>
    </>
  );
};

export default SideBar;
