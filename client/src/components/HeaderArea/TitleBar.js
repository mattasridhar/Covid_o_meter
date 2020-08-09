// Core imports
import React from "react";
import Localize from "../../i18n/Localize";

// DOM imports
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import Typography from "@material-ui/core/Typography";
import Badge from "@material-ui/core/Badge";
import NotificationsIcon from "@material-ui/icons/Notifications";
import uiStyles from "../App/UIStyles";

const TitleBar = ({ toggleSidebar, handleSidebarToggling }) => {
  const myStyles = uiStyles();

  return (
    <>
      <Toolbar className={myStyles.toolbar}>
        {!toggleSidebar && (
          <IconButton
            edge="start"
            color="inherit"
            aria-label="open drawer"
            onClick={handleSidebarToggling}
          >
            <MenuIcon />
          </IconButton>
        )}
        <Typography
          component="h1"
          variant="h6"
          color="inherit"
          noWrap
          className={myStyles.title}
        >
          <Localize id="covidTitle" />
        </Typography>
        <IconButton color="inherit">
          <Badge badgeContent={4} color="secondary">
            <NotificationsIcon />
          </Badge>
        </IconButton>
      </Toolbar>
    </>
  );
};

export default TitleBar;
