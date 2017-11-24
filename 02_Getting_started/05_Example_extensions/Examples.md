[\n

\n

To help illustrate how to develop extensions, we maintain a repository of
simple example extensions at <https://github.com/mdn/webextensions-examples>.
This article describes the WebExtension APIs used in that repository.

\n

These examples work in Firefox Nightly: most work in earlier versions of
Firefox, but check the [strict_min_version](/en-US/Add-
ons/WebExtensions/manifest.json/applications) key in the extension's
manifest.json to make sure.

\n

If you want to try out these examples, you have three main choices:

\n

\n

  1. Clone the repository, then load the extension straight from its source directory, using the ["Load Temporary Add-on"](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox) feature. The extension will stay loaded until you restart Firefox.
\n

  2. Clone the repository, then use the [web-ext](/en-US/Add-ons/WebExtensions/Getting_started_with_web-ext) command line tool to run Firefox with the extension installed.
\n

  3. Clone the repository, then go to the [build](https://github.com/mdn/webextensions-examples/tree/master/build) directory. This contains built and signed versions of all the examples, so you can just open them in Firefox (using File/Open File) and install them permanently, just like an extension you would install from [addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/).
\n

\n

If you want to contribute to the repository, [send us a pull
request!](https://github.com/mdn/webextensions-
examples/blob/master/CONTRIBUTING.md)

\n

\nName\n| Description\n| JavaScript APIs\n  
---|---|---  
[annotate-page](https://github.com/mdn/webextensions-examples/tree/master
/annotate-page) | Displays a sidebar that lets you take notes on web pages. |
[`storage.local`](/en-US/Add-ons/WebExtensions/API/storage/local)  
[`tabs.onActivated`](/en-US/Add-ons/WebExtensions/API/tabs/onActivated)  
[`tabs.onUpdated`](/en-US/Add-ons/WebExtensions/API/tabs/onUpdated)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`windows.getCurrent`](/en-US/Add-ons/WebExtensions/API/windows/getCurrent)  
  
[apply-css](https://github.com/mdn/webextensions-examples/tree/master/apply-
css) | Adds a page action to the toolbar. Click the button to apply a red
border using injected CSS. Click the button again to remove the CSS. |
[`pageAction.getTitle`](/en-US/Add-ons/WebExtensions/API/pageAction/getTitle)  
[`pageAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/pageAction/onClicked)  
[`pageAction.setIcon`](/en-US/Add-ons/WebExtensions/API/pageAction/setIcon)  
[`pageAction.setTitle`](/en-US/Add-ons/WebExtensions/API/pageAction/setTitle)  
[`pageAction.show`](/en-US/Add-ons/WebExtensions/API/pageAction/show)  
[`tabs.insertCSS`](/en-US/Add-ons/WebExtensions/API/tabs/insertCSS)  
[`tabs.onUpdated`](/en-US/Add-ons/WebExtensions/API/tabs/onUpdated)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`tabs.removeCSS`](/en-US/Add-ons/WebExtensions/API/tabs/removeCSS)  
  
[beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
| Adds a browser action icon to the toolbar. Click the button to choose a
beast. The active tab's body content is then replaced with a picture of the
chosen beast. | [`extension.getURL`](/en-US/Add-
ons/WebExtensions/API/extension/getURL)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`tabs.executeScript`](/en-US/Add-ons/WebExtensions/API/tabs/executeScript)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`tabs.reload`](/en-US/Add-ons/WebExtensions/API/tabs/reload)  
[`tabs.sendMessage`](/en-US/Add-ons/WebExtensions/API/tabs/sendMessage)  
  
[bookmark-it](https://github.com/mdn/webextensions-examples/tree/master
/bookmark-it) | Adds a bookmark button to the toolbar. Click the button to
toggle a bookmark for the current page. | [`bookmarks.create`](/en-US/Add-
ons/WebExtensions/API/bookmarks/create)  
[`bookmarks.onCreated`](/en-US/Add-ons/WebExtensions/API/bookmarks/onCreated)  
[`bookmarks.onRemoved`](/en-US/Add-ons/WebExtensions/API/bookmarks/onRemoved)  
[`bookmarks.remove`](/en-US/Add-ons/WebExtensions/API/bookmarks/remove)  
[`bookmarks.search`](/en-US/Add-ons/WebExtensions/API/bookmarks/search)  
[`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`browserAction.setIcon`](/en-US/Add-
ons/WebExtensions/API/browserAction/setIcon)  
[`browserAction.setTitle`](/en-US/Add-
ons/WebExtensions/API/browserAction/setTitle)  
[`tabs.onActivated`](/en-US/Add-ons/WebExtensions/API/tabs/onActivated)  
[`tabs.onUpdated`](/en-US/Add-ons/WebExtensions/API/tabs/onUpdated)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`windows.onFocusChanged`](/en-US/Add-
ons/WebExtensions/API/windows/onFocusChanged)  
  
[borderify](https://github.com/mdn/webextensions-
examples/tree/master/borderify) | Adds a solid red border to all webpages
matching mozilla.org. |  
[chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-
out) | Show a page action after a period of inactivity. Show cat gifs when the
page action is clicked. | [`alarms.clearAll`](/en-US/Add-
ons/WebExtensions/API/alarms/clearAll)  
[`alarms.create`](/en-US/Add-ons/WebExtensions/API/alarms/create)  
[`alarms.onAlarm`](/en-US/Add-ons/WebExtensions/API/alarms/onAlarm)  
[`pageAction.hide`](/en-US/Add-ons/WebExtensions/API/pageAction/hide)  
[`pageAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/pageAction/onClicked)  
[`pageAction.show`](/en-US/Add-ons/WebExtensions/API/pageAction/show)  
[`tabs.get`](/en-US/Add-ons/WebExtensions/API/tabs/get)  
[`tabs.onActivated`](/en-US/Add-ons/WebExtensions/API/tabs/onActivated)  
[`tabs.onUpdated`](/en-US/Add-ons/WebExtensions/API/tabs/onUpdated)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`tabs.update`](/en-US/Add-ons/WebExtensions/API/tabs/update)  
  
[commands](https://github.com/mdn/webextensions-examples/tree/master/commands)
| Demonstrates using the commands API to set up a keyboard shortcut. The
shortcut created is accessed using Ctrl+Shift+U (Command+Shift+U on a Mac). |
[`commands.getAll`](/en-US/Add-ons/WebExtensions/API/commands/getAll)  
[`commands.onCommand`](/en-US/Add-ons/WebExtensions/API/commands/onCommand)  
  
[context-menu-copy-link-with-types](https://github.com/mdn/webextensions-
examples/tree/master/context-menu-copy-link-with-types) | Add a context menu
option to links to copy the link to the clipboard, as plain text and as a link
in rich HTML. | [`contextMenus.create`](/en-US/Add-
ons/WebExtensions/API/contextMenus/create)  
[`contextMenus.onClicked`](/en-US/Add-
ons/WebExtensions/API/contextMenus/onClicked)  
[`tabs.executeScript`](/en-US/Add-ons/WebExtensions/API/tabs/executeScript)  
  
[contextual-identities](https://github.com/mdn/webextensions-
examples/tree/master/contextual-identities) | List, create, and remove
contextual identities. | [`contextualIdentities.query`](/en-US/Add-
ons/WebExtensions/API/contextualIdentities/query)  
[`tabs.create`](/en-US/Add-ons/WebExtensions/API/tabs/create)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`tabs.remove`](/en-US/Add-ons/WebExtensions/API/tabs/remove)  
  
[cookie-bg-picker](https://github.com/mdn/webextensions-examples/tree/master
/cookie-bg-picker) | Allows the user to customize the background color and
tiled pattern on sites the visit, and also saves their preferences via a
cookie, reapplying them whenever they revisit a site they previously
customized. | [`cookies.get`](/en-US/Add-ons/WebExtensions/API/cookies/get)  
[`cookies.onChanged`](/en-US/Add-ons/WebExtensions/API/cookies/onChanged)  
[`cookies.remove`](/en-US/Add-ons/WebExtensions/API/cookies/remove)  
[`cookies.set`](/en-US/Add-ons/WebExtensions/API/cookies/set)  
[`extension.getURL`](/en-US/Add-ons/WebExtensions/API/extension/getURL)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`tabs.onActivated`](/en-US/Add-ons/WebExtensions/API/tabs/onActivated)  
[`tabs.onUpdated`](/en-US/Add-ons/WebExtensions/API/tabs/onUpdated)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`tabs.sendMessage`](/en-US/Add-ons/WebExtensions/API/tabs/sendMessage)  
  
[devtools-panels](https://github.com/mdn/webextensions-examples/tree/master
/devtools-panels) | Demonstrates some of the devtools APIs. |
[`devtools.inspectedWindow`](/en-US/Add-
ons/WebExtensions/API/devtools/inspectedWindow)  
[`devtools.panels`](/en-US/Add-ons/WebExtensions/API/devtools/panels)  
[`runtime.getURL`](/en-US/Add-ons/WebExtensions/API/runtime/getURL)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
[`tabs.executeScript`](/en-US/Add-ons/WebExtensions/API/tabs/executeScript)  
  
[discogs-search](https://github.com/mdn/webextensions-examples/tree/master
/discogs-search) | Demonstrates adding a custom search engnie with the
chrome_settings_overrides key. |  
[dynamic-theme](https://github.com/mdn/webextensions-examples/tree/master
/dynamic-theme) | Dynamic theme example | [`alarms.create`](/en-US/Add-
ons/WebExtensions/API/alarms/create)  
[`alarms.onAlarm`](/en-US/Add-ons/WebExtensions/API/alarms/onAlarm)  
[`theme.update`](/en-US/Add-ons/WebExtensions/API/theme/update)  
  
[embedded-webextension-bootstrapped](https://github.com/mdn/webextensions-
examples/tree/master/embedded-webextension-bootstrapped) | Demonstrates how to
use an embedded WebExtension to port from a bootstrapped extension. |
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
[`storage.local`](/en-US/Add-ons/WebExtensions/API/storage/local)  
  
[embedded-webextension-overlay](https://github.com/mdn/webextensions-
examples/tree/master/embedded-webextension-overlay) | Demonstrates how to use
an embedded WebExtension to port from an overlay extension. |
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
  
[embedded-webextension-sdk](https://github.com/mdn/webextensions-
examples/tree/master/embedded-webextension-sdk) | Demonstrates how to use an
embedded WebExtension to port from an SDK-based add-on. |
[`notifications.create`](/en-US/Add-
ons/WebExtensions/API/notifications/create)  
[`runtime.connect`](/en-US/Add-ons/WebExtensions/API/runtime/connect)  
[`runtime.onConnect`](/en-US/Add-ons/WebExtensions/API/runtime/onConnect)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
[`storage.local`](/en-US/Add-ons/WebExtensions/API/storage/local)  
  
[emoji-substitution](https://github.com/mdn/webextensions-examples/tree/master
/emoji-substitution) | Replaces words with emojis. |  
[eslint-example](https://github.com/mdn/webextensions-examples/tree/master
/eslint-example) | Demonstrates how to configure an extension with eslint. |  
[export-helpers](https://github.com/mdn/webextensions-examples/tree/master
/export-helpers) | Demonstrates how to use export helpers like cloneInto to
share objects with page scripts. | [`notifications.create`](/en-US/Add-
ons/WebExtensions/API/notifications/create)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
  
[favourite-colour](https://github.com/mdn/webextensions-examples/tree/master
/favourite-colour) | An example options page, letting you store your favourite
colour. | [`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`runtime.openOptionsPage`](/en-US/Add-
ons/WebExtensions/API/runtime/openOptionsPage)  
[`storage.managed`](/en-US/Add-ons/WebExtensions/API/storage/managed)  
[`storage.sync`](/en-US/Add-ons/WebExtensions/API/storage/sync)  
  
[find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master
/find-across-tabs) | Demonstration of the find API. |
[`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`extension.getBackgroundPage`](/en-US/Add-
ons/WebExtensions/API/extension/getBackgroundPage)  
[`find.find`](/en-US/Add-ons/WebExtensions/API/find/find)  
[`find.highlightResults`](/en-US/Add-
ons/WebExtensions/API/find/highlightResults)  
[`runtime.getURL`](/en-US/Add-ons/WebExtensions/API/runtime/getURL)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
[`tabs.create`](/en-US/Add-ons/WebExtensions/API/tabs/create)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
  
[firefox-code-search](https://github.com/mdn/webextensions-
examples/tree/master/firefox-code-search) | Demonstrates how to use the
omnibox API. | [`omnibox.onInputChanged`](/en-US/Add-
ons/WebExtensions/API/omnibox/onInputChanged)  
[`omnibox.onInputEntered`](/en-US/Add-
ons/WebExtensions/API/omnibox/onInputEntered)  
[`omnibox.setDefaultSuggestion`](/en-US/Add-
ons/WebExtensions/API/omnibox/setDefaultSuggestion)  
[`tabs.create`](/en-US/Add-ons/WebExtensions/API/tabs/create)  
[`tabs.update`](/en-US/Add-ons/WebExtensions/API/tabs/update)  
  
[forget-it](https://github.com/mdn/webextensions-examples/tree/master/forget-
it) | Demonstrates how to use the browsingData API. |
[`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`browsingData.remove`](/en-US/Add-ons/WebExtensions/API/browsingData/remove)  
[`notifications.create`](/en-US/Add-
ons/WebExtensions/API/notifications/create)  
[`storage.local`](/en-US/Add-ons/WebExtensions/API/storage/local)  
  
[google-userinfo](https://github.com/mdn/webextensions-examples/tree/master
/google-userinfo) | Demonstrates how to use the identity API. |
[`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`identity.getRedirectURL`](/en-US/Add-
ons/WebExtensions/API/identity/getRedirectURL)  
[`identity.launchWebAuthFlow`](/en-US/Add-
ons/WebExtensions/API/identity/launchWebAuthFlow)  
[`notifications.create`](/en-US/Add-
ons/WebExtensions/API/notifications/create)  
  
[history-deleter](https://github.com/mdn/webextensions-examples/tree/master
/history-deleter) | History API demo: deletes history items for a given domain
| [`history.deleteUrl`](/en-US/Add-ons/WebExtensions/API/history/deleteUrl)  
[`history.search`](/en-US/Add-ons/WebExtensions/API/history/search)  
[`pageAction.show`](/en-US/Add-ons/WebExtensions/API/pageAction/show)  
[`tabs.onUpdated`](/en-US/Add-ons/WebExtensions/API/tabs/onUpdated)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
  
[http-response](https://github.com/mdn/webextensions-examples/tree/master
/http-response) | Demonstrates how to rewrite HTTP responses using the
webRequest.filterResponseData() API. | [`webRequest.filterResponseData`](/en-
US/Add-ons/WebExtensions/API/webRequest/filterResponseData)  
[`webRequest.onBeforeRequest`](/en-US/Add-
ons/WebExtensions/API/webRequest/onBeforeRequest)  
  
[imagify](https://github.com/mdn/webextensions-examples/tree/master/imagify) |
Using a sidebar, illustrates the use of file picker and drag and drop. A
content script replaces the current page content with the chosen image. |
[`extension.getURL`](/en-US/Add-ons/WebExtensions/API/extension/getURL)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`tabs.executeScript`](/en-US/Add-ons/WebExtensions/API/tabs/executeScript)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`tabs.sendMessage`](/en-US/Add-ons/WebExtensions/API/tabs/sendMessage)  
  
[latest-download](https://github.com/mdn/webextensions-examples/tree/master
/latest-download) | Shows the last downloaded item, and lets you open or
delete it. | [`downloads.erase`](/en-US/Add-
ons/WebExtensions/API/downloads/erase)  
[`downloads.getFileIcon`](/en-US/Add-
ons/WebExtensions/API/downloads/getFileIcon)  
[`downloads.open`](/en-US/Add-ons/WebExtensions/API/downloads/open)  
[`downloads.removeFile`](/en-US/Add-
ons/WebExtensions/API/downloads/removeFile)  
[`downloads.search`](/en-US/Add-ons/WebExtensions/API/downloads/search)  
  
[list-cookies](https://github.com/mdn/webextensions-examples/tree/master/list-
cookies) | This extensions list the cookies in the active tab. |
[`cookies.getAll`](/en-US/Add-ons/WebExtensions/API/cookies/getAll)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
  
[menu-demo](https://github.com/mdn/webextensions-examples/tree/master/menu-
demo) | Demonstrates adding and manipulating menu items using the menus API. |
[`i18n.getMessage`](/en-US/Add-ons/WebExtensions/API/i18n/getMessage)  
[`menus.create`](/en-US/Add-ons/WebExtensions/API/menus/create)  
[`menus.onClicked`](/en-US/Add-ons/WebExtensions/API/menus/onClicked)  
[`menus.remove`](/en-US/Add-ons/WebExtensions/API/menus/remove)  
[`menus.update`](/en-US/Add-ons/WebExtensions/API/menus/update)  
[`runtime.lastError`](/en-US/Add-ons/WebExtensions/API/runtime/lastError)  
[`tabs.executeScript`](/en-US/Add-ons/WebExtensions/API/tabs/executeScript)  
  
[mocha-client-tests](https://github.com/mdn/webextensions-examples/tree/master
/mocha-client-tests) | This example shows two methods of testing an extension:
running tests from within the extension, and running tests from the command
line using Karma | [`runtime.onMessage`](/en-US/Add-
ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
  
[native-messaging](https://github.com/mdn/webextensions-examples/tree/master
/native-messaging) | Example of native messaging, including a Python
application and an extension which exchanges messages with it. |
[`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`runtime.connectNative`](/en-US/Add-
ons/WebExtensions/API/runtime/connectNative)  
  
[navigation-stats](https://github.com/mdn/webextensions-examples/tree/master
/navigation-stats) | Demonstration of the webNavigation API, showing basic
stats about which pages you've visited. | [`storage.local`](/en-US/Add-
ons/WebExtensions/API/storage/local)  
[`webNavigation.onCompleted`](/en-US/Add-
ons/WebExtensions/API/webNavigation/onCompleted)  
  
[notify-link-clicks-i18n](https://github.com/mdn/webextensions-
examples/tree/master/notify-link-clicks-i18n) | Shows a localized notification
when the user clicks on links. | [`extension.getURL`](/en-US/Add-
ons/WebExtensions/API/extension/getURL)  
[`i18n.getMessage`](/en-US/Add-ons/WebExtensions/API/i18n/getMessage)  
[`notifications.create`](/en-US/Add-
ons/WebExtensions/API/notifications/create)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
  
[open-my-page-button](https://github.com/mdn/webextensions-
examples/tree/master/open-my-page-button) | Adds a browser action icon to the
toolbar. When the browser action is clicked, the add-on opens a page that was
packaged with it. | [`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`tabs.create`](/en-US/Add-ons/WebExtensions/API/tabs/create)  
  
[page-to-extension-messaging](https://github.com/mdn/webextensions-
examples/tree/master/page-to-extension-messaging) | Demonstrates how a web
page and a content script can exchange messages. Visit https://mdn.github.io
/webextensions-examples/content-script-page-script-messaging.html for the
demo. |  
[permissions](https://github.com/mdn/webextensions-
examples/tree/master/permissions) | Demonstrates optional permissions using
the permissions API. | [`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`permissions.getAll`](/en-US/Add-ons/WebExtensions/API/permissions/getAll)  
[`permissions.remove`](/en-US/Add-ons/WebExtensions/API/permissions/remove)  
[`permissions.request`](/en-US/Add-ons/WebExtensions/API/permissions/request)  
[`runtime.getURL`](/en-US/Add-ons/WebExtensions/API/runtime/getURL)  
[`tabs.create`](/en-US/Add-ons/WebExtensions/API/tabs/create)  
  
[proxy-blocker](https://github.com/mdn/webextensions-examples/tree/master
/proxy-blocker) | Uses the proxy API to block requests to specific hosts. |
[`extension.getURL`](/en-US/Add-ons/WebExtensions/API/extension/getURL)  
[`proxy.onProxyError`](/en-US/Add-ons/WebExtensions/API/proxy/onProxyError)  
[`proxy.register`](/en-US/Add-ons/WebExtensions/API/proxy/register)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
[`storage.local`](/en-US/Add-ons/WebExtensions/API/storage/local)  
[`storage.onChanged`](/en-US/Add-ons/WebExtensions/API/storage/onChanged)  
  
[quicknote](https://github.com/mdn/webextensions-
examples/tree/master/quicknote) | Allows the user to make quick notes by
clicking a button and entering text into the resulting popup. The notes are
saved in storage. | [`storage.local`](/en-US/Add-
ons/WebExtensions/API/storage/local)  
  
[react-es6-popup](https://github.com/mdn/webextensions-examples/tree/master
/react-es6-popup) | This is an example of creating a browser action popup UI
in React and ES6 JavaScript. | [`tabs.query`](/en-US/Add-
ons/WebExtensions/API/tabs/query)  
  
[selection-to-clipboard](https://github.com/mdn/webextensions-
examples/tree/master/selection-to-clipboard) | Demonstrates how to write to
the clipboard from a content script |  
[session-state](https://github.com/mdn/webextensions-examples/tree/master
/session-state) | Demonstrates how to retrieve extension-defined state state
from restored tabs. | [`menus.create`](/en-US/Add-
ons/WebExtensions/API/menus/create)  
[`menus.onClicked`](/en-US/Add-ons/WebExtensions/API/menus/onClicked)  
[`sessions.getTabValue`](/en-US/Add-
ons/WebExtensions/API/sessions/getTabValue)  
[`sessions.setTabValue`](/en-US/Add-
ons/WebExtensions/API/sessions/setTabValue)  
[`tabs.insertCSS`](/en-US/Add-ons/WebExtensions/API/tabs/insertCSS)  
[`tabs.onCreated`](/en-US/Add-ons/WebExtensions/API/tabs/onCreated)  
[`tabs.onUpdated`](/en-US/Add-ons/WebExtensions/API/tabs/onUpdated)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
  
[store-collected-images](https://github.com/mdn/webextensions-
examples/tree/master/store-collected-images) | Demonstrates how to use the
idb-file-storage library to store and manipulate files in an extension. |
[`browserAction.onClicked`](/en-US/Add-
ons/WebExtensions/API/browserAction/onClicked)  
[`contextMenus.create`](/en-US/Add-ons/WebExtensions/API/contextMenus/create)  
[`contextMenus.onClicked`](/en-US/Add-
ons/WebExtensions/API/contextMenus/onClicked)  
[`runtime.onMessage`](/en-US/Add-ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
[`tabs.create`](/en-US/Add-ons/WebExtensions/API/tabs/create)  
[`windows.create`](/en-US/Add-ons/WebExtensions/API/windows/create)  
  
[stored-credentials](https://github.com/mdn/webextensions-examples/tree/master
/stored-credentials) | Performs basic authentication by supplying stored
credentials. | [`storage.local`](/en-US/Add-
ons/WebExtensions/API/storage/local)  
[`webRequest.onAuthRequired`](/en-US/Add-
ons/WebExtensions/API/webRequest/onAuthRequired)  
[`webRequest.onCompleted`](/en-US/Add-
ons/WebExtensions/API/webRequest/onCompleted)  
[`webRequest.onErrorOccurred`](/en-US/Add-
ons/WebExtensions/API/webRequest/onErrorOccurred)  
  
[tabs-tabs-tabs](https://github.com/mdn/webextensions-examples/tree/master
/tabs-tabs-tabs) | Demonstrates tab manipulation: opening, closing, moving,
zooming tabs. | [`tabs.create`](/en-US/Add-ons/WebExtensions/API/tabs/create)  
[`tabs.duplicate`](/en-US/Add-ons/WebExtensions/API/tabs/duplicate)  
[`tabs.getZoom`](/en-US/Add-ons/WebExtensions/API/tabs/getZoom)  
[`tabs.move`](/en-US/Add-ons/WebExtensions/API/tabs/move)  
[`tabs.onMoved`](/en-US/Add-ons/WebExtensions/API/tabs/onMoved)  
[`tabs.onRemoved`](/en-US/Add-ons/WebExtensions/API/tabs/onRemoved)  
[`tabs.query`](/en-US/Add-ons/WebExtensions/API/tabs/query)  
[`tabs.reload`](/en-US/Add-ons/WebExtensions/API/tabs/reload)  
[`tabs.remove`](/en-US/Add-ons/WebExtensions/API/tabs/remove)  
[`tabs.setZoom`](/en-US/Add-ons/WebExtensions/API/tabs/setZoom)  
[`tabs.update`](/en-US/Add-ons/WebExtensions/API/tabs/update)  
  
[theme-switcher](https://github.com/mdn/webextensions-examples/tree/master
/theme-switcher) | An example of how to use the management API for themes. |
[`management.getAll`](/en-US/Add-ons/WebExtensions/API/management/getAll)  
[`management.setEnabled`](/en-US/Add-
ons/WebExtensions/API/management/setEnabled)  
  
[themes](https://github.com/mdn/webextensions-examples/tree/master/themes) | A
collection of themes illustrating:

  * weta_fade: a basic theme employing a single image specified in `headerURL:`.
  * weta_fade_chrome: the weta_fade theme implemented with Chrome compatible manifest keys.
  * weta_tiled: a theme using a tiled image.
  * weta_mirror: a theme using multiple images and aligning those images in the header.
  * animated: use of an animated PNG.

|  
[top-sites](https://github.com/mdn/webextensions-examples/tree/master/top-
sites) | Demonstration of the topSites API. | [`topSites.get`](/en-US/Add-
ons/WebExtensions/API/topSites/get)  
  
[user-agent-rewriter](https://github.com/mdn/webextensions-
examples/tree/master/user-agent-rewriter) | Demonstrates using the webRequest
API to rewrite the User-Agent HTTP header. | [`extension.getBackgroundPage
`](/en-US/Add-ons/WebExtensions/API/extension/getBackgroundPage)  
[`webRequest.onBeforeSendHeaders`](/en-US/Add-
ons/WebExtensions/API/webRequest/onBeforeSendHeaders)  
  
[webpack-modules](https://github.com/mdn/webextensions-examples/tree/master
/webpack-modules) | Demonstrates how to use webpack to package npm modules in
an extension. | [`runtime.onMessage`](/en-US/Add-
ons/WebExtensions/API/runtime/onMessage)  
[`runtime.sendMessage`](/en-US/Add-ons/WebExtensions/API/runtime/sendMessage)  
  
[window-manipulator](https://github.com/mdn/webextensions-examples/tree/master
/window-manipulator) | Demonstrates how to manipulate windows: opening,
closing, resizing windows. | [`windows.create`](/en-US/Add-
ons/WebExtensions/API/windows/create)  
[`windows.getAll`](/en-US/Add-ons/WebExtensions/API/windows/getAll)  
[`windows.getCurrent`](/en-US/Add-ons/WebExtensions/API/windows/getCurrent)  
[`windows.remove`](/en-US/Add-ons/WebExtensions/API/windows/remove)  
[`windows.update`](/en-US/Add-ons/WebExtensions/API/windows/update)  
  
  
\n]

