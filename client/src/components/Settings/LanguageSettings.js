// Core imports
import React from "react";
import { useTranslation } from "react-i18next";

// DOM imports
import uiStyles from "../App/UIStyles";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import Divider from "@material-ui/core/Divider";

// Custom component imports
import Localize from "../../i18n/Localize";

const LanguageSettings = () => {
  const myStyles = uiStyles();
  const { i18n } = useTranslation();

  // Alter the default language
  const changeLocale = (language) => {
    i18n.changeLanguage(language);
  };

  return (
    <>
      <Typography variant="subtitle1" gutterBottom>
        <Localize id="localeTitle" />
      </Typography>
      <Divider className={myStyles.divider} style={{ marginBottom: "12px" }} />
      <Grid container spacing={3}>
        <Grid item xs={3}>
          <Paper
            className={myStyles.paper}
            onClick={() => {
              changeLocale("en");
            }}
          >
            <Localize id="english" />
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper
            className={myStyles.paper}
            onClick={() => {
              changeLocale("fr");
            }}
          >
            <Localize id="french" />
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper
            className={myStyles.paper}
            onClick={() => {
              changeLocale("gr");
            }}
          >
            <Localize id="german" />
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper
            className={myStyles.paper}
            onClick={() => {
              changeLocale("hi");
            }}
          >
            <Localize id="hindi" />
          </Paper>
        </Grid>
      </Grid>
      <Divider className={myStyles.divider} />
    </>
  );
};

export default LanguageSettings;
