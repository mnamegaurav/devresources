import React from "react";
import { useRouter } from "next/router";

import "../styles/globals.scss";
import BaseLayout from "../layouts/BaseLayout";

function MyApp(props) {
  const { Component, pageProps } = props;
  const router = useRouter();

  // Imports the bootstrap js only for client side browser
  React.useEffect(() => {
    import("bootstrap/dist/js/bootstrap");

    const handleRouteChange = (url) => {
      window.gtag("config", "G-3GX7VC9BSJ", {
        page_path: url,
      });
    };
    router.events.on("routeChangeComplete", handleRouteChange);
    return () => {
      router.events.off("routeChangeComplete", handleRouteChange);
    };
  }, [router.events]);

  return (
    <BaseLayout>
      <Component {...pageProps} />
    </BaseLayout>
  );
}

export default MyApp;
