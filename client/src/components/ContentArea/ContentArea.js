// Core imports
import React from "react";
import { constants } from "../App/constants";

// DOM imports
import uiStyles from "../App/UIStyles";
import Container from "@material-ui/core/Container";
import Box from "@material-ui/core/Box";

// Custom component imports
import Bank from "../Bank/Bank";
import Settings from "../Settings/Settings";
import Copyrights from "../Canvas/Copyrights";

// Custom components imports

const ContentArea = ({ canvasContext }) => {
  const myStyles = uiStyles();

  // Return the appropriate component based on the Context selected from the Sidebar Panel
  const renderCanvas = () => {
    switch (canvasContext) {
      case constants.content.settings:
        return <Settings />;
      case constants.content.bank:
      default:
        return <Bank />;
    }
  };

  return (
    <>
      <main className={myStyles.content}>
        <div className={myStyles.appBarSpacer} />
        <Box pt={4}>
          <Copyrights />
        </Box>
        <Container maxWidth="lg" className={myStyles.container}>
          {renderCanvas()}
        </Container>
      </main>
    </>
  );
};

export default ContentArea;
