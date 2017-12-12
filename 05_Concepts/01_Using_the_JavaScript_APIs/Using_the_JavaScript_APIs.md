JavaScript APIs for WebExtensions can be used inside the extension's [background scripts](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts) and in any other documents bundled with the extension, including [browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action) or [page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) popups, [sidebars](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars), [options pages](/en-US/docs/Mozilla/Add-ons/WebExtensions/Options_pages), or [new tab pages](/en-US/Add-ons/WebExtensions/manifest.json/chrome_url_overrides). A few of these APIs can also be accessed by an extension's [content scripts](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Content_scripts) (see the [list in the content script guide](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Content_scripts#WebExtension_APIs)).

To use the more powerful APIs you need to [request permission](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/permissions) in your extension's manifest.json.

You can access the APIs using the `browser` namespace:

    
    
    function logTabs(tabs) {
      console.log(tabs);
    }
    
    browser.tabs.query({currentWindow: true}, logTabs);

Many of the APIs are asynchronous, returning a `[Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)`:

    
    
    function logCookie(c) {
      console.log(c);
    }
    
    function logError(e) {
      console.error(e);
    }
    
    var setCookie = browser.cookies.set(
      {url: "https://developer.mozilla.org/"}
    );
    setCookie.then(logCookie, logError);

Note that this is different from Google Chrome's extension system, which uses the `chrome` namespace instead of `browser`, and which uses callbacks instead of promises for asynchronous functions. As a porting aid, the Firefox implementation of WebExtensions APIs supports `chrome` and callbacks as well as `browser` and promises. Mozilla has also written a polyfill which enables code that uses `browser` and promises to work unchanged in Chrome: <https://github.com/mozilla/webextension-polyfill>.

Firefox also implements these APIs under the `chrome` namespace using callbacks. This allows code written for Chrome to run largely unchanged in Firefox for the APIs documented here.

Microsoft Edge uses the `browser` namespace, but doesn't yet support promise-based asynchronous APIs. In Edge, for the time being, asynchronous APIs must use callbacks.

Not all browsers support all the APIs: for the details, see [Browser support for JavaScript APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs).

## alarms

Schedule code to run at a specific time in the future. This is like`[setTimeout()](/en-US/docs/Web/API/WindowTimers/setTimeout)` and`[setInterval()](/en-US/docs/Web/API/WindowTimers/setInterval)`, except that those functions don't work with background pages that are loaded on demand.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms)

## bookmarks

The [WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions) [`bookmarks`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks "The documentation about this has not yet been written; please consider contributing!") API lets an extension interact with and manipulate the browser's bookmarking system.You can use it to bookmark pages, retrieve existing bookmarks, and edit,remove, and organize bookmarks.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks)

## browserAction

Adds a button to the browser's toolbar.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)

## browserSettings

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings)

## browsingData

Enables extensions to clear the data that is accumulated while the user is browsing.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browsingData)

## clipboard

The clipboard API enables an extension to copy items to the system clipboard.Currently the API only supports copying images, but it's intended to support copying text and HTML in the future.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/clipboard)

## commands

Listen for the user executing commands that you have registered using the [`commands` manifest.json key](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/commands).

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands)

## contextualIdentities

Work with contextual identities: list, create, remove, and update contextual identities.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities)

## cookies

Enables extensions to get and set cookies, and be notified when they change.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies)

## devtools.inspectedWindow

The `devtools.inspectedWindow` API lets a devtools extension interact with the window that the developer tools are attached to.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.inspectedWindow)

## devtools.network

The `devtools.network` API lets a devtools extension get information about network requests associated with the window that the devtools are attached to (the inspected window).

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.network)

## devtools.panels

The `devtools.panels` API lets a devtools extension define its user interface inside the devtools window.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.panels)

## downloads

Enables extensions to interact with the browser's download manager. You can use this API module to download files, cancel, pause, resume downloads, and show downloaded files in the file manager.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads)

## events

Common types used by APIs that dispatch events.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events)

## extension

Utilities related to your extension. Get URLs to resources packages with your extension, get the `[Window](/en-US/docs/Web/API/Window)` object for your extension's pages, get the values for various settings. Note that the messaging APIs in this module are deprecated in favor of the equivalent APIs in the `[runtime](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)` module.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension)

## extensionTypes

Some common types used in other WebExtension APIs.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes)

## find

Finds text in a web page, and highlights matches.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/find)

## history

Use the `history` API to interact with the browser history.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/history)

## i18n

Functions to internationalize your extension. You can use these APIs to get localized strings from locale files packaged with your extension, find out the browser's current language, and find out the value of its [Accept-Language header](/en-US/docs/Web/HTTP/Content_negotiation#The_Accept-Language_header).

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)

## identity

Use the identity API to get an [OAuth2](https://oauth.net/2/) authorization code or access token, which an extension can then use to access user data from a service which supports OAuth2 access (such as a Google or a Facebook account).

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity)

## idle

Find out when the user's system is idle, locked, or active.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/idle)

## management

Get information about installed add-ons.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management)

## menus

Add items to the browser's menu system.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus)

## notifications

Display notifications to the user, using the underlying operating system's notification mechanism. Because this API uses the operating system's notification mechanism, the details of how notifications appear and behave may differ according to the operating system and the user's settings.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications)

## omnibox

Enables extensions to implement customised behavior when the user types into the browser's address bar.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox)

## pageAction

A [page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) is a lickable icon inside the browser's address bar.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)

## permissions

Extensions need permissions to access many of the more powerful WebExtension APIs. They can ask for permissions at install time by including the permissions they need in the `[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)` manifest.json key. The main advantages of asking for permissions at install time are:

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions)

## pkcs11

The `pkcs11` API enables an extension to enumerate [PKCS#11](https://en.wikipedia.org/wiki/PKCS_11) security modules, and to make them accessible to the browser as sources of keys and certificates.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11)

## privacy

Access and modify various privacy-related browser settings.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)

## proxy

Use the proxy API to register an extended [Proxy Auto-Configuration (PAC) file](/en-US/Add-ons/WebExtensions/API/proxy#PAC_file_specification), which implements a policy for proxying web requests. This implementation deviates from standard PAC design in several ways because the de-facto specification for PAC files hasn't changed since its initial implementation circa 1995. There is no standards body maintaining the specification.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/proxy)

## runtime

This module provides information about your extension and the environment it's running in.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)

## sessions

Use the sessions API to list, and restore, tabs and windows that have been closed while the browser has been running.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions)

## sidebarAction

Gets and sets properties of an extension's sidebar.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction)

## storage

Enables extensions to store and retrieve data, and listen for changes to stored items.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)

## tabs

Interact with the browser's tab system.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)

## theme

Enables browser extensions to update the browser theme.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme)

## topSites

Use the topSites API to get an array containing all the sites listed in the browser's "New Tab" page.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/topSites)

## types

Defines the `BrowserSetting` type, which is used to represent a browser setting.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/types)

## webNavigation

Add event listeners for the various stages of a navigation. A navigation consists of a frame in the browser transitioning from one URL to another, usually (but not always) in response to a user action like clicking a link or entering a URL in the location bar.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation)

## webRequest

Add event listeners for the various stages of making an HTTP request. The event listener receives detailed information about the request, and can modify or cancel the request.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest)

## windows

Interact with browser windows. You can use this API to get information about open windows and to open, modify, and close windows. You can also listen for window open, close, and activate events.

[API reference documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)

