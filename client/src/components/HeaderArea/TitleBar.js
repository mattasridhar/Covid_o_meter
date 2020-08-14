// Core imports
import React from "react";

// DOM imports
import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import Typography from "@material-ui/core/Typography";
import uiStyles from "../App/UIStyles";
import logo_white from "../App/logo_white.svg";
import Box from "@material-ui/core/Box";

// Custom component imports
import Localize from "../../i18n/Localize";
import Copyrights from "../Canvas/Copyrights";

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
          {"  "}
          <img src={logo_white} alt="Covid-logo" />
        </Typography>
        <Box pt={4}>
          <Copyrights />
        </Box>
      </Toolbar>
    </>
  );
};

export default TitleBar;
