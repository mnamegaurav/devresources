JAZZMIN_UI_TWEAKS = {
#     "navbar_small_text": False,
#     "footer_small_text": False,
    "body_small_text": True,
#     "brand_small_text": False,
#     "brand_colour": False,
#     "accent": "accent-primary",
    "navbar": "navbar-dark",
#     "no_navbar_border": False,
#     "navbar_fixed": False,
#     "layout_boxed": False,
#     "footer_fixed": False,
    "sidebar_fixed": True,
#     "sidebar": "sidebar-dark-primary",
#     "sidebar_nav_small_text": True,
#     "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
#     "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "flatly",
    # "dark_mode_theme": "darkly",
#     "button_classes": {
#         "primary": "btn-outline-primary",
#         "secondary": "btn-outline-secondary",
#         "info": "btn-outline-info",
#         "warning": "btn-outline-warning",
#         "danger": "btn-danger",
#         "success": "btn-success"
#     },
    # "dark_theme": "darkly",
#     "actions_sticky_top": False
}


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Dev Resources",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Dev Resources",

    # # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # "site_logo": "books/img/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to the Dev Resources",

    # Copyright on the footer
    "copyright": "DevJunction",

    # # The model admin to search from the search bar, search bar omitted if excluded
    # "search_model": "auth.User",

    # # Field name on user model that contains avatar image
    # "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Site",  "url": "/", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # # model admin to link to (Permissions checked against model)
        # {"model": "auth.User"},

        # # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    # "usermenu_links": [
    #     {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
    #     {"model": "auth.user"}
    # ],

    # #############
    # # Side Menu #
    # #############

    # # Whether to display the side menu
    # "show_sidebar": True,

    # # Whether to aut expand the menu
    # "navigation_expanded": True,

    # # Hide these apps when generating side menu e.g (auth)
    # "hide_apps": [],

    # # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": [],

    # # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    # "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "Site": [{
    #         "name": "Make Messages", 
    #         "url": "make_messages", 
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },

    # # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # # for a list of icon classes
    # "icons": {
    #     "auth": "fas fa-users-cog",
    #     "auth.user": "fas fa-user",
    #     "auth.Group": "fas fa-users",
    # },
    # # Icons that are used when one is not manually specified
    # "default_icon_parents": "fas fa-chevron-circle-right",
    # "default_icon_children": "fas fa-circle",

    # #################
    # # Related Modal #
    # #################
    # # Use modals instead of popups
    # "related_modal_active": False,

    # #############
    # # UI Tweaks #
    # #############
    # # Relative paths to custom CSS/JS scripts (must be present in static files)
    # "custom_css": None,
    # "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    # ###############
    # # Change view #
    # ###############
    # # Render out the change view as a single form, or in tabs, current options are
    # # - single
    # # - horizontal_tabs (default)
    # # - vertical_tabs
    # # - collapsible
    # # - carousel
    # "changeform_format": "horizontal_tabs",
    # # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # # Add a language dropdown into the admin
    # "language_chooser": True,
}