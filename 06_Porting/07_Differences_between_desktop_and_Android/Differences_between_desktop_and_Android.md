[



Firefox for Android offers a subset of the WebExtensions APIs available to the
desktop version of Firefox. Some of these differences are due to the nature of
the Android environment and therefore the features Firefox can implement,
others are where Firefox for Android does not yet offer all the desktop
features. This article describes and explains these differences and looks at
the impact they might have on your add-on development.



This summary is based on the features planned for Firefox version 54.



A detailed list of the WebExtension APIs supported in Firefox for Android is
provided on the\xa0[Browser support for JavaScript
APIs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/Browser_support_for_JavaScript_APIs) page and details of the
supported manifest.json keys are provided on the [manifest.json section
](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json)page.



## User interface



Firefox for Android offers a streamlined version of the UI found in desktop
Firefox, ensuring Firefox offers an enjoyable and engaging experience on
mobile. Some of the differences relate to how the Android UI differs from the
desktop UIs found in Linux, Mac OS, and Windows. For example, Android does not
support a windowing environment, and devices do not usually include a physical
keyboard, from which keyboard shortcuts can be issued. Other differences
relate to optimizing usability on smaller mobile device screens.



As a result of the UI differences, extensions for Firefox for Android do not
support the following APIs and manifest.json keys:\xa0





  * [`commands`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands "Listen for the user executing commands that you have registered using the commands manifest.json key.") and the related [`commands` ](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/commands)manifest.json key, as Android tablets and smartphones do not usually have a physical keyboard from which \u2018commands\u2019 can be issued.


  * [`sidebarAction`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction "Gets and sets properties of an extension's sidebar.") and the related\xa0`[sidebar_action](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/sidebar_action)` manifest.json key, due to the limited screen real estate on Android devices sidebars, such as the browser history, are presented in full browser tabs. Where possible, you should move any sidebar content to tabs as well.


  * [`windows`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows "Interact with browser windows. You can use this API to get information about open windows and to open, modify, and close windows. You can also listen for window open, close, and activate events.") as there is only one Firefox on Android 'window', so it has no ability to open or otherwise manipulate additional browser windows.




Support for [`browserAction`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction "Adds a button to the browser's toolbar.")
and the [browser_action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action) manifest.json key is under
development. Firefox 55 will support `default_title` and `default_popup` of
the manifest.json key `[browser_action](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)`, using
`default_title` to add an item to the Firefox for Android menu, and the
[`browserAction.onClicked()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/onClicked "Fired when a browser action
icon is clicked. This event will not fire if the browser action has a popup.")
event will be available to listen for the menu item being tapped.
Additionally, in Firefox 57 support for the [`browserAction.setTitle`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction/setTitle "Sets the
browser action's title. The title is displayed in a tooltip over the browser
action's icon. You can pass a tabId in as an optional parameter \\u2014 if you
do this then the title is changed only for the given tab.") and
[`browserAction.getTitle`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getTitle "Gets the browser action's
title.") methods will be added.



### Effect on your add-on UI



These differences impact the way you expose your add-on in the Firefox UI. The
most common option, adding a button for your add-on to the Firefox toolbar
with `[browserAction](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction)`, is not available (at least until
Firefox 55). Nor can you expose your add-on through a sidebar or context menu.
You will, therefore, use an address bar button (through the manifest.json
`[page_action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/page_action)` key and
`[pageAction](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/API/pageAction)` API) remembering that by default this
button is hidden and must be shown programmatically.



The features of [`pageAction`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction "A page action is a clickable icon inside the
browser's address bar.") are also reduced in Firefox for Android. The
manifest.json key [page_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/page_action) enables you to define the button
icon and a popup. You then have use of [`pageAction.show()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction/show "Shows the page
action for a given tab. The page action is shown whenever the given tab is the
active tab.") and [`pageAction.hide()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/hide "Hides the page action for a given
tab.") however, once \u2018shown\u2019, note that the address bar button is
visible in all tabs (unlike the desktop behavior, where the button is shown
only for a specified tab.) And you can set a listener to
[`pageAction.onClicked()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/onClicked "Fired when a page action icon is
clicked. This event will not fire if the page action has a popup.").
[`pageAction.setPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/setPopup "Sets the HTML document to be opened
as a popup when the user clicks on the page action's icon.") and
[`pageAction.getPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/getPopup "Gets the URL for the HTML document
set as the popup for this page action.") are also available, so you can update
the popup or create a popup once the add-on is running.\xa0



Also, in both [`pageAction`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction "A page action is a clickable icon inside the
browser's address bar.") and [`browserAction`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction "Adds a button to the browser's toolbar.")
popup content is opened in a new tab and persists until the user manually
closes the tab.



You can also manipulate tabs on Firefox for Android. The [`tabs`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/tabs "Interact with the browser's
tab system.") API enables you to perform most of the actions you can on the
desktop, the main exceptions are:





  * zoom features, Firefox for Android has one zoom level only, which the user can override with a pinch gesture on the page.


  * features related to selecting and moving tabs, again as these features are not supported on Android.


  * the ability to detect a tab's language or muted status.\xa0




### Other UI related API and manifest.json key differences



There are some other UI features not supported, these are:





  * [`bookmarks`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks "The WebExtensions bookmarks API lets an extension interact with and manipulate the browser's bookmarking system. You can use it to bookmark pages, retrieve existing bookmarks, and edit, remove, and organize bookmarks."), which means you cannot manipulate the user's bookmarks, although the user can do this themselves through the UI.


  * [`browsingData`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browsingData "Enables extensions to clear the data that is accumulated while the user is browsing."), which means you cannot offer users features to clear browser data such as history, downloads, passwords, and alike.


  * The [chrome_url_overrides](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/chrome_url_overrides)\xa0and [chrome_settings_overrides](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/chrome_settings_overrides) manifest.json keys, which means you cannot add custom home and new tab pages.


  * [`contextMenus`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextMenus "The documentation about this has not yet been written; please consider contributing!"), which means you cannot add options to context menus.


  * [`history`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/history "Use the history API to interact with the browser history."), which means you cannot search or manipulate the history of browsed pages.


  * [`omnibox`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox "Enables extensions to implement customised behavior when the user types into the browser's address bar.") and the related\xa0[omnibox](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/omnibox) manifest.json key, which means you cannot provide custom address bar suggestions.


  * [`sessions`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions "Use the sessions API to list, and restore, tabs and windows that have been closed while the browser has been running."), which means you cannot list and restore tabs that have been closed while the browser has been running.


  * The\xa0[options_ui\xa0](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/options_ui) manifest.json key, which means you cannot provide options settings on about:addons. (And, as a consequence, [`runtime.openOptionsPage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/openOptionsPage "This is an asynchronous function that returns a Promise.") is not available either.) You can, however, offer your users a page for setting add-on options using a [bundled wep page](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Bundled_web_pages) displayed using [`tabs`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs "Interact with the browser's tab system."), you just have to add a button or other mechanism in your add-on to access the page.


  * At the time of writing the options_ui key was being implemented under [bug 1302504](https://bugzilla.mozilla.org/show_bug.cgi?id=1302504).






## Developer tools



Developer tools for Firefox for Android are provided through remote debugging
mechanisms [over USB](https://developer.mozilla.org/en-
US/docs/Tools/Remote_Debugging/Debugging_Firefox_for_Android_with_WebIDE) or
[Wi-Fi](https://developer.mozilla.org/en-
US/docs/Tools/Remote_Debugging/Debugging_Firefox_for_Android_over_Wifi) that
connect to the WebIDE on a desktop. Therefore, Firefox for Android does not
provide any built-in developer tools and its extensions do not support the
APIs to extend the developer tools:





  * [devtools.inspectedWindow](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.inspectedWindow)


  * [devtools.network](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.network)


  * [devtools.panels](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.panels) and the related [devtools_page](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/devtools_page) manifest.json key.




## Native application interaction



You do not have the ability to interact with native applications as
[`runtime.connectNative()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/connectNative "For more information, see Native
messaging.") and [`runtime.sendNativeMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendNativeMessage "Sends a single message from
an extension to a native application.") are not available.



## Permissions



Permissions to use certain WebExtension APIs must be requested in the
manifest.json file. On the desktop version of Firefox users are warned when an
extension requests a permission and are given the option to deny the add-on
that permission. However, on Firefox for Android permissions are granted
automatically and the user isn\u2019t given the option to deny them. It is
currently planned to resolve this issue in Firefox 57.



## Other notes





  * At the time of writing there was an issue with [`storage.sync()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/sync "Represents the sync storage area. Items in sync storage are synced by the browser, and are available across all instances of that browser that the user is logged into \(e.g. via Firefox sync, or a Google account\), across different devices.") and data is not synchronized with the user\u2019s Firefox account from Firefox for Android. More details can be found in [bug 1316442](https://bugzilla.mozilla.org/show_bug.cgi?id=1316442).


]

