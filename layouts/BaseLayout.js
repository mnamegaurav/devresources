import React from "react";
import PropTypes from "prop-types";

import SEO from "../components/SEO";
import Header from "../components/Header";
import Footer from "../components/Footer";
import Head from "next/head";

function BaseLayout(props) {
  const { children } = props;

  return (
    <>
      <Head>
        <SEO />
      </Head>
      <div className="bodyContainer">
        <Header />
        {children}
        {props?.children?.props?.statusCode !== 404 ? <Footer /> : null}
      </div>
    </>
  );
}

BaseLayout.propTypes = {
  children: PropTypes.objectOf(PropTypes.any).isRequired,
};

export default BaseLayout;
