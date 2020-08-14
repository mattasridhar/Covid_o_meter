// Core imports
import React from "react";
import { Trans } from "react-i18next";

const Localize = ({ id }) => {
  return <Trans i18nKey={id}></Trans>;
};

export default Localize;
