// Core imports
import React, { useState, useEffect } from "react";
import { connect } from "react-redux";
import { useTranslation } from "react-i18next";
import { ContextPlotData } from "../App/AppContexts";
import { constants } from "../App/constants";

// DOM imports
import clsx from "clsx";
import CssBaseline from "@material-ui/core/CssBaseline";
import Drawer from "@material-ui/core/Drawer";
import AppBar from "@material-ui/core/AppBar";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { Default } from "react-spinners-css";

// Custom components imports
import TitleBar from "../HeaderArea/TitleBar";
import SideBar from "../SideBar/SideBar";
import ContentArea from "../ContentArea/ContentArea";
import Localize from "../../i18n/Localize";

// Store imports
import { fetchCountriesList, fetchCountriesMap } from "../../store";
import { fetchTimeSeriesMap } from "../../store/thunks/timeseries";
import { fetchRadialChartMap } from "../../store/thunks/radialchart";
import { fetchHeatMap } from "../../store/thunks/heatmap";
import { fetchStackedMap } from "../../store/thunks/stackedmap";
import { fetchScatterPlot } from "../../store/thunks/scatterplot";

const Canvas = ({
  countriesList,
  countriesMap,
  timeseriesMap,
  radialchartMap,
  heatMap,
  stackedMap,
  scatterPlot,
  loading,
  timeseriesloading,
  radialchartloading,
  heatloading,
  stackedloading,
  scatterloading,
  fetchCountriesMap,
  fetchCountriesList,
  fetchTimeSeriesMap,
  fetchRadialChartMap,
  fetchHeatMap,
  fetchStackedMap,
  fetchScatterPlot,
}) => {
  const [toggleSidebar, setToggleSidebar] = useState(false);
  const [canvasContext, setCanvasContext] = useState(constants.content.bank);
  const [contextInfo, setContextInfo] = useState({
    worldHeatData: countriesMap,
    timeseriesData: timeseriesMap,
    radialchartData: radialchartMap,
    heatData: heatMap,
    stackedData: stackedMap,
    scatterplotData: scatterPlot,
  });
  const { i18n } = useTranslation();

  // For Checking the availability of Locales
  useEffect(() => {
    console.log("Default Language: ", i18n.language);
  }, [i18n.language]);

  // Fetching the plotted information from API
  useEffect(() => {
    if (countriesMap.length === 0) {
      fetchCountriesMap();
    }
    if (timeseriesMap.length === 0) {
      fetchTimeSeriesMap();
    }
    if (radialchartMap.length === 0) {
      fetchRadialChartMap();
    }
    if (heatMap.length === 0) {
      fetchHeatMap();
    }
    if (stackedMap.length === 0) {
      fetchStackedMap();
    }
    if (scatterPlot.length === 0) {
      fetchScatterPlot();
    }
    setContextInfo({
      worldHeatData: countriesMap,
      timeseriesData: timeseriesMap,
      radialchartData: radialchartMap,
      heatData: heatMap,
      stackedData: stackedMap,
      scatterplotData: scatterPlot,
    });
    // eslint-disable-next-line
  }, [countriesMap, timeseriesMap, radialchartMap, heatMap, stackedMap]);

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
    overlayLoaderBackground: {
      display: "overlay",
      position: "fixed",
      zIndex: 9999,
      left: 0,
      top: 0,
      width: "100%",
      height: "100%",
      overflow: "auto",
      backgroundColor: "rgba(0, 0, 0, 0.4)",
    },
    overlayLoader: {
      display: "overlay",
      position: "fixed",
      zIndex: 9999,
      left: "35%",
      top: "22.5%",
      width: "100%",
      height: "100%",
      overflow: "auto",
    },
    overlayLoaderTitle: {
      display: "overlay",
      position: "fixed",
      zIndex: 9998,
      left: "15%",
      top: "40%",
      width: "100%",
      height: "100%",
      overflow: "auto",
      color: "#FFFFFF",
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
    <>
      {((loading &&
        timeseriesloading &&
        radialchartloading &&
        heatloading &&
        stackedloading) ||
        contextInfo.worldHeatData.length === 0) && (
        <div className={customStyles.overlayLoaderBackground}>
          <Typography
            component="h3"
            variant="h4"
            color="inherit"
            noWrap
            className={customStyles.overlayLoaderTitle}
          >
            <Localize id="loading" />
          </Typography>
          <Default
            color="black"
            size={450}
            className={customStyles.overlayLoader}
          />
        </div>
      )}
      <div className={customStyles.root}>
        <>
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
          <ContextPlotData.Provider value={contextInfo}>
            <ContentArea canvasContext={canvasContext} />
          </ContextPlotData.Provider>
        </>
      </div>
    </>
  );
};

const mapStateToProps = (state) => {
  return {
    countriesMap: state.countriesReducer.countriesMap,
    countriesList: state.countriesReducer.countriesList,
    loading: state.countriesReducer.loading,
    timeseriesloading: state.timeseriesReducer.timeseriesloading,
    timeseriesMap: state.timeseriesReducer.timeseriesMap,
    radialchartloading: state.radialchartReducer.radialchartloading,
    radialchartMap: state.radialchartReducer.radialchartMap,
    heatloading: state.heatmapReducer.heatloading,
    heatMap: state.heatmapReducer.heatMap,
    stackedloading: state.stackedReducer.stackedloading,
    stackedMap: state.stackedReducer.stackedMap,
    scatterloading: state.scatterPlotReducer.scatterloading,
    scatterPlot: state.scatterPlotReducer.scatterPlot,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    fetchCountriesMap: () => dispatch(fetchCountriesMap()),
    fetchCountriesList: () => dispatch(fetchCountriesList()),
    fetchTimeSeriesMap: () => dispatch(fetchTimeSeriesMap()),
    fetchRadialChartMap: () => dispatch(fetchRadialChartMap()),
    fetchHeatMap: () => dispatch(fetchHeatMap()),
    fetchStackedMap: () => dispatch(fetchStackedMap()),
    fetchScatterPlot: () => dispatch(fetchScatterPlot()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Canvas);
