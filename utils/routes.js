export const routes = {
  category: {
    path: "/",
    showOnNavbar: true,
    title: "Services",
    subRoutes: {
      resources: {
        path: "/resources",
        title: "Resources",
        showOnNavbar: true,
      },
    },
  },
  contactUs: {
    showOnNavbar: true,
    path: "/contatus",
    title: "Contact Us",
    subRoutes: null,
  },
  aboutUs: {
    showOnNavbar: true,
    path: "/aboutus",
    title: "About Us",
    subRoutes: null,
  },
};
