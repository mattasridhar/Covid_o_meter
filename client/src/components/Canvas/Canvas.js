// Core imports
import React, { useState, useEffect } from "react";
import { useTranslation } from "react-i18next";

// DOM imports
import clsx from "clsx";
import CssBaseline from "@material-ui/core/CssBaseline";
import Drawer from "@material-ui/core/Drawer";
import AppBar from "@material-ui/core/AppBar";
import { makeStyles } from "@material-ui/core/styles";

// Custom components imports
import TitleBar from "../HeaderArea/TitleBar";
import SideBar from "../SideBar/SideBar";
import ContentArea from "../ContentArea/ContentArea";
import { constants } from "../App/constants";

const Canvas = () => {
  const [toggleSidebar, setToggleSidebar] = useState(true);
  const [canvasContext, setCanvasContext] = useState(constants.content.bank);
  const { i18n } = useTranslation();

  useEffect(() => {
    console.log("Default Language: ", i18n.language);
  }, [i18n.language]);

  // custom stlyes
  const customUI_Styles = makeStyles((theme) => ({
    root: {
      display: "flex",
    },
    appBar: {
      zIndex: theme.zIndex.drawer + 1,
      transition: theme.transitions.create(["width", "margin"], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
    },
    appBarShift: {
      marginLeft: 240,
      width: `calc(100% - ${240}px)`,
      transition: theme.transitions.create(["width", "margin"], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
    },
    drawerPaper: {
      position: "relative",
      whiteSpace: "nowrap",
      width: 240,
      transition: theme.transitions.create("width", {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
    },
    drawerPaperClose: {
      overflowX: "hidden",
      transition: theme.transitions.create("width", {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      width: theme.spacing(7),
      [theme.breakpoints.up("sm")]: {
        width: theme.spacing(9),
      },
    },
  }));
  const customStyles = customUI_Styles();

  // toggle the Sidebar panel
  const handleSidebarToggling = () => {
    setToggleSidebar(!toggleSidebar);
  };

  // change the content in the Content Area based on the option selected from Sidebar
  const alterCanvas = (canvasContent) => {
    setCanvasContext(canvasContent);
  };

  return (
    <div className={customStyles.root}>
      <CssBaseline />
      <AppBar
        position="absolute"
        className={clsx(
          customStyles.appBar,
          toggleSidebar && customStyles.appBarShift
        )}
      >
        <TitleBar
          toggleSidebar={toggleSidebar}
          handleSidebarToggling={handleSidebarToggling}
        />
      </AppBar>
      <Drawer
        variant="permanent"
        classes={{
          paper: clsx(
            customStyles.drawerPaper,
            !toggleSidebar && customStyles.drawerPaperClose
          ),
        }}
        open={toggleSidebar}
      >
        <SideBar
          handleSidebarToggling={handleSidebarToggling}
          alterCanvas={alterCanvas}
        />
      </Drawer>
      <ContentArea canvasContext={canvasContext} />
    </div>
  );
};

export default Canvas;
