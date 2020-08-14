// Core imports
import React from "react";

// DOM imports
import Typography from "@material-ui/core/Typography";
import Link from "@material-ui/core/Link";

// Custom component imports
import Localize from "../../i18n/Localize";

// Store imports

const Copyrights = () => {
  return (
    <Typography variant="body2" color="tertiary" align="center">
      <Localize id="copyright" />
      <Link
        color="inherit"
        href="https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv"
        // href="https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"
      >
        Github User Content
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
};

export default Copyrights;
