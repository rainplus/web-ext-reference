[\n

\n

Extensions can extend and modify the capability of a browser. Extensions for
Firefox are built using the WebExtensions API, a cross-browser system for
developing extensions. To a large extent the system is compatible with the
[extension API](https://developer.chrome.com/extensions) supported by Google
Chrome and Opera and the [W3C Draft Community
Group](https://browserext.github.io/browserext/). Extensions written for these
browsers will in most cases run in Firefox or [Microsoft
Edge](https://developer.microsoft.com/en-us/microsoft-
edge/platform/documentation/extensions/) with [just a few
changes](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Porting_from_Google_Chrome). The API is also fully
compatible with [multiprocess Firefox](https://developer.mozilla.org/en-
US/Firefox/Multiprocess_Firefox).

\n

If you have ideas or questions, or need help migrating a legacy add-on to use
WebExtensions APIs, you can reach us on the [dev-addons mailing
list](https://mail.mozilla.org/listinfo/dev-addons) or
[#webextensions](irc://irc.mozilla.org/webextensions) on
[IRC](https://wiki.mozilla.org/IRC).

\n

\n

\n

## Getting started

\n

\n

  * [What are extensions?](/en-US/Add-ons/WebExtensions/What_are_WebExtensions)
\n

  * [Your first extension](/en-US/Add-ons/WebExtensions/Your_first_WebExtension)
\n

  * [Your second extension](/en-US/Add-ons/WebExtensions/Your_second_WebExtension)
\n

  * [Anatomy of an extension](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension)
\n

  * [Example extensions](/en-US/Add-ons/WebExtensions/Examples)
\n

\n

## How to

\n

\n

  * [Intercept HTTP requests](/en-US/docs/Mozilla/Add-ons/WebExtensions/Intercept_HTTP_requests)
\n

  * [Modify a web page](/en-US/docs/Mozilla/Add-ons/WebExtensions/Modify_a_web_page)
\n

  * [Add a button to the toolbar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Add_a_button_to_the_toolbar)
\n

  * [Implement a settings page](/en-US/docs/Mozilla/Add-ons/WebExtensions/Implement_a_settings_page)
\n

  * [Interact with the clipboard](/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard)
\n

\n

## User interface

\n

\n

  * [Introduction](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface)
\n

  * [Browser toolbar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_action)
\n

  * [Browser toolbar button with a popup](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)
\n

  * [Address bar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Page_actions)
\n

  * [Address bar button with a popup](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)
\n

  * [Context menu items](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Context_menu_items)
\n

  * [Sidebars](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars)
\n

  * [Options page](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages)
\n

  * [Bundled web pages](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Bundled_web_pages)
\n

  * [Notifications](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Notifications)
\n

  * [Address bar suggestions](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Omnibox)
\n

  * [Developer tools panels](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/devtools_panels)
\n

\n

## Concepts

\n

\n

  * [JavaScript API overview](/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
\n

  * [Content scripts](/en-US/Add-ons/WebExtensions/Content_scripts)
\n

  * [Match patterns](/en-US/Add-ons/WebExtensions/Match_patterns)
\n

  * [Working with files](/en-US/docs/Mozilla/Add-ons/WebExtensions/Working_with_files)
\n

  * [Internationalization](/en-US/docs/Mozilla/Add-ons/WebExtensions/Internationalization)
\n

  * [Content Security Policy](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy)
\n

  * [Native messaging](/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging)
\n

  * [Using the devtools APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/Using_the_devtools_APIs)
\n

  * [User experience best practices](/en-US/Add-ons/WebExtensions/User_experience_best_practices)
\n

\n

## Porting

\n

\n

  * [Porting a Google Chrome extension](/en-US/Add-ons/WebExtensions/Porting_from_Google_Chrome)
\n

  * [Porting a legacy Firefox extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Porting_a_legacy_Firefox_add-on)
\n

  * [Developing for Firefox for Android](/en-US/docs/Mozilla/Add-ons/WebExtensions/Developing_WebExtensions_for_Firefox_for_Android)
\n

  * [Embedded WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Embedded_WebExtensions)
\n

  * [Comparison with the Add-on SDK](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK)
\n

  * [Comparison with XUL/XPCOM extensions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions)
\n

  * [Chrome incompatibilities](/en-US/docs/Mozilla/Add-ons/WebExtensions/Chrome_incompatibilities)
\n

  * [Differences between desktop and Android](/en-US/docs/Mozilla/Add-ons/WebExtensions/Differences_between_desktop_and_Android)
\n

\n

## Firefox workflow

\n

\n

  * [User experience](/en-US/docs/Mozilla/Add-ons/WebExtensions/User_experience_best_practices)
\n

  * [Installation](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)
\n

  * [Debugging](/en-US/Add-ons/WebExtensions/Debugging)
\n

  * [Getting started with web-ext](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)
\n

  * [web-ext command reference](/en-US/docs/Mozilla/Add-ons/WebExtensions/web-ext_command_reference)
\n

  * [Extensions and the Add-on ID](/en-US/docs/Mozilla/Add-ons/WebExtensions/WebExtensions_and_the_Add-on_ID)
\n

  * [Alternative distribution options](/en-US/Add-ons/WebExtensions/Alternative_distribution_options)
\n

  * [Publishing your extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Publishing_your_WebExtension)
\n

\n

\n

\n

## Reference

\n

### JavaScript APIs

\n

\n

  * [JavaScript API overview](/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
\n

  * [Browser compatibility tables for JavaScript APIs](/en-US/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs)
\n

\n

  * [alarms](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms)
  * [bookmarks](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks)
  * [browserAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)
  * [browserSettings](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings)
  * [browsingData](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browsingData)
  * [clipboard](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/clipboard)
  * [commands](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands)
  * [contextualIdentities](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities)
  * [cookies](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies)
  * [devtools.inspectedWindow](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.inspectedWindow)
  * [devtools.network](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.network)
  * [devtools.panels](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.panels)
  * [downloads](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads)
  * [events](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events)
  * [extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension)
  * [extensionTypes](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes)
  * [find](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/find)
  * [history](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/history)
  * [i18n](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)
  * [identity](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity)
  * [idle](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/idle)
  * [management](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management)
  * [menus](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus)
  * [notifications](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications)
  * [omnibox](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox)
  * [pageAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)
  * [permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions)
  * [pkcs11](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11)
  * [privacy](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)
  * [proxy](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/proxy)
  * [runtime](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)
  * [sessions](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions)
  * [sidebarAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction)
  * [storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)
  * [tabs](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)
  * [theme](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme)
  * [topSites](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/topSites)
  * [types](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/types)
  * [webNavigation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation)
  * [webRequest](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest)
  * [windows](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)

\n

### Manifest keys

\n

\n

  * [manifest.json overview](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)
\n

  * [Browser compatibility for manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_compatibility_for_manifest.json)
\n

\n

  * [applications](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications)
  * [author](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/author)
  * [background](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/background)
  * [browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)
  * [chrome_settings_overrides](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/chrome_settings_overrides)
  * [chrome_url_overrides](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/chrome_url_overrides)
  * [commands](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands)
  * [content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)
  * [content_security_policy](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_security_policy)
  * [default_locale](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/default_locale)
  * [description](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/description)
  * [developer](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/developer)
  * [devtools_page](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/devtools_page)
  * [homepage_url](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/homepage_url)
  * [icons](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/icons)
  * [incognito](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/incognito)
  * [manifest_version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/manifest_version)
  * [name](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/name)
  * [omnibox](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox)
  * [optional_permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/optional_permissions)
  * [options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)
  * [page_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)
  * [permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)
  * [protocol_handlers](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/protocol_handlers)
  * [short_name](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/short_name)
  * [sidebar_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/sidebar_action)
  * [theme](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme)
  * [version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version)
  * [web_accessible_resources](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/web_accessible_resources)

\n

\n

\n]

