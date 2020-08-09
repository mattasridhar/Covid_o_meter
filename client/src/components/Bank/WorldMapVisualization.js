// Core imports
import React, { useState, useEffect } from "react";
import { connect } from "react-redux";

// DOM imports
import Button from "@material-ui/core/Button";
import CircularProgress from "@material-ui/core/CircularProgress";

// Custom component imports

// Store imports
import { fetchCountries } from "../../store";

export const WorldMapVisualization = ({
  countries,
  loading,
  fetchCountries,
}) => {
  const [url, setUrl] = useState("");

  useEffect(() => {
    fetchCountries();
    console.log("SRI WMV effect: ", countries);
    // eslint-disable-next-line
  }, []);

  console.log("SRI out: ", countries);

  //   const file = new Blob([countries], { type: "image/png" });
  //   // setUrl(URL.createObjectURL(file));
  //   const url1 = URL.createObjectURL(file);
  //   console.log("SRI file: ", file);
  //   console.log("SRI url: ", url1);

  return (
    <>
      <p>
        <button>{`Click Me`}</button>
      </p>
      <div>{loading && <CircularProgress disableShrink />}</div>
      <img
        src={`data:image/jpeg;base64,${countries}`}
        style={{ width: "120px", height: "120px" }}
      ></img>
      <Button variant="contained" color="primary">
        Hello World
      </Button>
    </>
  );
};

const mapStateToProps = (state) => {
  return {
    countries: state.countriesReducer.countriesList,
    loading: state.countriesReducer.loading,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    fetchCountries: () => dispatch(fetchCountries()),
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(WorldMapVisualization);

/* 
import React, { useState, useEffect } from "react";
import { connect } from "react-redux";
import { fetchCountries } from "../../store";
import Button from "@material-ui/core/Button";
import CircularProgress from "@material-ui/core/CircularProgress";

const WorldMapVisualization = ({ countries, loading, fetchCountries }) => {
  const [url, setUrl] = useState("");

  useEffect(() => {
    fetchCountries();
    console.log("SRI effect: ", countries);
    // eslint-disable-next-line
  }, []);

  console.log("SRI out: ", countries);

  const file = new Blob([countries], { type: "image/png" });
  // setUrl(URL.createObjectURL(file));
  const url1 = URL.createObjectURL(file);
  console.log("SRI file: ", file);
  console.log("SRI url: ", url1);

  return (
    <>
      <p>
        <button>{`Click Me`}</button>
      </p>
      <div>{loading && <CircularProgress disableShrink />}</div>
      <img
        src={`data:image/jpeg;base64,${countries}`}
        style={{ width: "120px", height: "120px" }}
      ></img>
      <Button variant="contained" color="primary">
        Hello World
      </Button>
    </>
  );
};

const mapStateToProps = (state) => {
  return {
    countries: state.countriesReducer.countriesList,
    loading: state.countriesReducer.loading,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    fetchCountries: () => dispatch(fetchCountries()),
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(WorldMapVisualization); */
