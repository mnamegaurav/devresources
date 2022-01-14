module.exports = {
  ci: {
    collect: {
      staticDistDir: ".next/server/pages",
    },
    upload: {
      target: "temporary-public-storage",
    },
    asserts: {
      presets: "lighthouse:no-pwa",
    },
  },
};
