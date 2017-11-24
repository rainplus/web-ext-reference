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

If you have ideas or questions, or need help migrating a legacy add-on to use
WebExtensions APIs, you can reach us on the [dev-addons mailing
list](https://mail.mozilla.org/listinfo/dev-addons) or
[#webextensions](irc://irc.mozilla.org/webextensions) on
[IRC](https://wiki.mozilla.org/IRC).

## Getting started

  * [What are extensions?](/en-US/Add-ons/WebExtensions/What_are_WebExtensions)
  * [Your first extension](/en-US/Add-ons/WebExtensions/Your_first_WebExtension)
  * [Your second extension](/en-US/Add-ons/WebExtensions/Your_second_WebExtension)
  * [Anatomy of an extension](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension)
  * [Example extensions](/en-US/Add-ons/WebExtensions/Examples)

## How to

  * [Intercept HTTP requests](/en-US/docs/Mozilla/Add-ons/WebExtensions/Intercept_HTTP_requests)
  * [Modify a web page](/en-US/docs/Mozilla/Add-ons/WebExtensions/Modify_a_web_page)
  * [Add a button to the toolbar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Add_a_button_to_the_toolbar)
  * [Implement a settings page](/en-US/docs/Mozilla/Add-ons/WebExtensions/Implement_a_settings_page)
  * [Interact with the clipboard](/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard)

## User interface

  * [Introduction](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface)
  * [Browser toolbar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_action)
  * [Browser toolbar button with a popup](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)
  * [Address bar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Page_actions)
  * [Address bar button with a popup](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)
  * [Context menu items](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Context_menu_items)
  * [Sidebars](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars)
  * [Options page](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages)
  * [Bundled web pages](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Bundled_web_pages)
  * [Notifications](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Notifications)
  * [Address bar suggestions](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Omnibox)
  * [Developer tools panels](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/devtools_panels)

## Concepts

  * [JavaScript API overview](/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
  * [Content scripts](/en-US/Add-ons/WebExtensions/Content_scripts)
  * [Match patterns](/en-US/Add-ons/WebExtensions/Match_patterns)
  * [Working with files](/en-US/docs/Mozilla/Add-ons/WebExtensions/Working_with_files)
  * [Internationalization](/en-US/docs/Mozilla/Add-ons/WebExtensions/Internationalization)
  * [Content Security Policy](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy)
  * [Native messaging](/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging)
  * [Using the devtools APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/Using_the_devtools_APIs)
  * [User experience best practices](/en-US/Add-ons/WebExtensions/User_experience_best_practices)

## Porting

  * [Porting a Google Chrome extension](/en-US/Add-ons/WebExtensions/Porting_from_Google_Chrome)
  * [Porting a legacy Firefox extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Porting_a_legacy_Firefox_add-on)
  * [Developing for Firefox for Android](/en-US/docs/Mozilla/Add-ons/WebExtensions/Developing_WebExtensions_for_Firefox_for_Android)
  * [Embedded WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Embedded_WebExtensions)
  * [Comparison with the Add-on SDK](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK)
  * [Comparison with XUL/XPCOM extensions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions)
  * [Chrome incompatibilities](/en-US/docs/Mozilla/Add-ons/WebExtensions/Chrome_incompatibilities)
  * [Differences between desktop and Android](/en-US/docs/Mozilla/Add-ons/WebExtensions/Differences_between_desktop_and_Android)

## Firefox workflow

  * [User experience](/en-US/docs/Mozilla/Add-ons/WebExtensions/User_experience_best_practices)
  * [Installation](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)
  * [Debugging](/en-US/Add-ons/WebExtensions/Debugging)
  * [Getting started with web-ext](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)
  * [web-ext command reference](/en-US/docs/Mozilla/Add-ons/WebExtensions/web-ext_command_reference)
  * [Extensions and the Add-on ID](/en-US/docs/Mozilla/Add-ons/WebExtensions/WebExtensions_and_the_Add-on_ID)
  * [Alternative distribution options](/en-US/Add-ons/WebExtensions/Alternative_distribution_options)
  * [Publishing your extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Publishing_your_WebExtension)

## Reference

### JavaScript APIs

  * [JavaScript API overview](/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
  * [Browser compatibility tables for JavaScript APIs](/en-US/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs)

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

### Manifest keys

  * [manifest.json overview](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)
  * [Browser compatibility for manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_compatibility_for_manifest.json)

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

