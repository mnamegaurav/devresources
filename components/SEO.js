import React from "react";
import Head from "next/head";
import Script from "next/script";

export default function SEO() {
  return (
    <div>
      <Head>
        <meta charset="utf-8" />
        <meta name="author" content="My UK Education" />
        <link rel="icon" href="/favicon.png" />
        <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta content="/" name="app:pageurl" />

        <meta
          property="og:title"
          content="DevJunction - A developer's destination for all the learning resources at one place. We have hundreds of curated learning resources, grouped together at one place to ease your learning experience."
        />
        <meta property="og:image" content="images/seo/website.png" />
        <meta property="og:image:type" content="image/png" />
        <meta property="og:image:width" content="1350" />
        <meta property="og:image:height" content="768" />
        <meta
          property="og:image:alt"
          content="DevJunction - A developer's destination for all the learning resources at one place. We have hundreds of curated learning resources, grouped together at one place to ease your learning experience."
        />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://devjunction.in" />
        <meta
          property="og:description"
          content="DevJunction - A developer's destination for all the learning resources at one place. We have hundreds of curated learning resources, grouped together at one place to ease your learning experience."
        />
        <meta property="og:site_name" content="DevJunction" />
        <meta
          property="twitter:title"
          content="DevJunction — DevJunction - A developer's destination for all the learning resources at one place. We have hundreds of curated learning resources, grouped together at one place to ease your learning experience."
        />
        <meta
          property="twitter:description"
          content="DevJunction - A developer's destination for all the learning resources at one place. We have hundreds of curated learning resources, grouped together at one place to ease your learning experience."
        />
        <meta property="twitter:image" content="images/seo/website.jpg" />
        <meta
          name="description"
          content="DevJunction - A developer's destination for all the learning resources at one place. We have hundreds of curated learning resources, grouped together at one place to ease your learning experience."
        />

        <link rel="canonical" href="https://devjunction.in" />
        <link rel="prefetch" href="https://devjunction.in" />
        <link rel="prerender" href="https://devjunction.in" />

        <meta
          name="keywords"
          content="DevJunction, DevJunction gaurav, DevJunction django, DevJunction python tips, DevJunction django tips, DevJunction django orm, python, django, web development, software development, projects, online courses, django blogs, DevJunction learning resources, DevJunction"
        />
      </Head>

      {/* Global Site Tag (gtag.js) - Google Analytics */}
      <Script strategy="afterInteractive" src="https://www.googletagmanager.com/gtag/js?id=G-3GX7VC9BSJ" />
      <script
        dangerouslySetInnerHTML={{
          __html: `
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-3GX7VC9BSJ', {
                page_path: window.location.pathname,
            });
            `,
        }}
      />
    </div>
  );
}
