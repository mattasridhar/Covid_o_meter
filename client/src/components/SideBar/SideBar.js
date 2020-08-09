// Core imports
import React from "react";
import Localize from "../../i18n/Localize";

// DOM imports
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import DashboardIcon from "@material-ui/icons/Dashboard";
import SettingsIcon from "@material-ui/icons/Settings";
import Divider from "@material-ui/core/Divider";
import IconButton from "@material-ui/core/IconButton";
import ChevronLeftIcon from "@material-ui/icons/ChevronLeft";
import uiStyles from "../App/UIStyles";
import { constants } from "../App/constants";

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
