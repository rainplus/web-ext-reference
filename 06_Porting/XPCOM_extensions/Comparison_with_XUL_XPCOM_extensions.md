[\n

\n

This article is a technical comparison between the WebExtensions technology
and "classic" extensions developed using direct XUL manipulation and direct
access to XPCOM. It's intended to help orient people who maintain an add-on
like this, and who are planning to port it to use WebExtension APIs.

\n

This article covers both [overlay extensions](/en-US/Add-
ons/Overlay_Extensions) and [bootstrapped extensions](/en-US/docs/Mozilla/Add-
ons/Bootstrapped_extensions), but not extensions developed using the Add-on
SDK. For the Add-on SDK, please see [Comparison with the Add-on SDK](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK).

\n

At a very basic level, XUL/XPCOM extensions are similar to extensions
developed with WebExtensions. They both include:

\n

\n

  * manifest files defining metadata for the extension and some aspects of its behavior.
\n

  * JavaScript code that gets access to a set of privileged JavaScript APIs and that stays loaded for as long as the extension itself is enabled.
\n

  * the ability to add specific UI elements, such as buttons, to the browser.
\n

\n

Beyond that, though, the systems are very different. In particular:

\n

\n

  * Compared with XUL/XPCOM extensions, WebExtensions provide much more limited options for the extension's UI, and a much more limited set of privileged JavaScript APIs.
\n

  * WebExtensions can only access web content by injecting separate scripts into web pages and communicating with them using a messaging API (note, though, that this is also true of XUL/XPCOM extensions that expect to work with multiprocess Firefox).
\n

\n

## Manifest

\n

XUL/XPCOM extensions have two manifest files:

\n

\n

  * the [install.rdf](/en-US/Add-ons/Install_Manifests) contains metadata about the extension such as its name, icons, and so on
\n

  * the [chrome.manifest](/en-US/docs/Chrome_Registration), that tells Firefox where it can find the components of the extension, including XUL overlays for the extension's interface, scripts for its behavior, and files containing localized strings.
\n

\n

WebExtensions have a single manifest file called [manifest.json](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json), that has a similar
purpose. You use it to specify the extension's name, description, icons, and
so on, as well as to specify any buttons it adds to Firefox and to list
scripts it needs to run. To get an overview of the components of an extension
developed using WebExtension APIs, and how they are specified in
manifest.json, see ["Anatomy of an extension"](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension).

\n

### Learn more

\n

\n

  * [manifest.json documentation](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)
\n

  * [Anatomy of a extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Anatomy_of_a_WebExtension)
\n

\n

## UI

\n

XUL/XPCOM extensions can build their UI by directly manipulating the XUL used
to specify the browser's own UI. They do this either using overlays or, in the
case of bootstrapped/restartless extensions, using JavaScript to modify the
XUL document. They can not only add any elements to the browser's UI, they can
also modify or remove existing elements. They can also use APIs like
[CustomizableUI.jsm](/en-
US/docs/Mozilla/JavaScript_code_modules/CustomizableUI.jsm) to build their UI.

\n

Extensions built with WebExtension APIs don't get this kind of direct access.
Instead, a combination of manifest.json keys and JavaScript APIs enable them
to add a limited set of UI components to the browser. The available components
are:

\n\n\n\nName\n| Description\n| Specified using\n  
---|---|---  
\n\n\n\nBrowser action\n| Button in the browser toolbar, with an optional
popup panel.\n| \n

`[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` manifest key

\n

`[browserAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)`
API

\n\n  
\n\nPage action\n| Button in the URL bar, with an optional popup panel.\n| \n

`[page_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/page_action)` manifest key

\n

`[pageAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)` API

\n\n  
\n\nCommands\n| Keyboard shortcuts.\n| \n

`[commands](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands)`
manifest key

\n

`[commands](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands)` API

\n\n  
\n\nContext menu\n| Adds items and submenus to the browser's context menu.\n|
`[contextMenus](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextMenus)`
API\n  
\n\n\n

## Privileged APIs

\n

Both XUL/XPCOM extensions and extensions built with WebExtension APIs can
contain scripts that stay loaded for as long as the extension itself is
enabled, and that have access to a set of privileged APIs. However, XUL/XPCOM
extensions get access to a much wider range of APIs.

\n

The scripts packaged with XUL/XPCOM extensions get access to the full set of
[XPCOM APIs](/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface) and
[JavaScript code modules](/en-US/docs/Mozilla/JavaScript_code_modules) through
the `[Components](/en-
US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components_object)` object. They
also get direct access to the browser's internals through globals like
`[gBrowser](/en-US/docs/Mozilla/Tech/XUL/tabbrowser)`.

\n

The equivalent WebExtension scripts are called [background scripts](/en-US
/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts), and they
get access to a much smaller set of high-level JavaScript APIs. To see all the
privileged APIs available to background scripts, see the [summary API page
](/en-US/Add-ons/WebExtensions/API). Background scripts also get a
`[window](https://developer.mozilla.org/en-US/docs/Web/API/Window)` global,
with all the DOM objects that are available in a normal web page.

\n

There are vastly more APIs available to XUL/XPCOM extensions than are
available to WebExtensions, and for many XUL/XPCOM APIs, there isn't a
WebExtensions substitute. The table below lists every API in the popular
[Services.jsm](/en-US/docs/Mozilla/JavaScript_code_modules/Services.jsm)
module, describe what the equivalent WebExtensions API would be, if there is
one.

\n

You'll see that many APIs have no WebExtensions equivalent yet. However we are
intending to extend the WebExtension APIs to support the needs of add-on
developers, so if you have ideas, we'd love to hear them. You can reach us on
the [dev-addons mailing list](https://mail.mozilla.org/listinfo/dev-addons) or
[#webextensions](irc://irc.mozilla.org/webextensions) on
[IRC](https://wiki.mozilla.org/IRC).

\n\n\n\nServices.jsm API\n| WebExtensions equivalent\n  
---|---  
\n\n\n\n`[nsIAndroidBridge](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIAndroidBridge)`\n| None\n  
\n\n`[nsIXULAppInfo](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIXULAppInfo)`  
\n`[nsIXULRuntime](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIXULRuntime)`\n| None\n  
\n\n`[nsIAppShellService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIAppShellService)`\n| None\n  
\n\n`[nsIBlocklistService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIBlocklistService)`\n| None\n  
\n\n`[nsICacheService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsICacheService)`\n| None\n  
\n\n`[nsICacheStorageService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsICacheStorageService)`\n|
None\n  
\n\n`[nsIClipboard](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIClipboard)`\n| Partial: see
the [`clipboard`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/clipboard "The
clipboard API enables an extension to copy items to the system clipboard.
Currently the API only supports copying images, but it's intended to support
copying text and HTML in the future.") API, and [Interacting with the
clipboard](/en-US/Add-ons/WebExtensions/Interact_with_the_clipboard).\n  
\n\n`[nsIConsoleService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIConsoleService)`\n|
`[window.console](/en-US/docs/Web/API/Console)`\n  
\n\n`[nsIContentPrefService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIContentPrefService)`\n|
None\n  
\n\n`[nsICookieManager2](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsICookieManager2)`\n|
`[cookies](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies)`\n  
\n\n`[nsIMessageSender](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIMessageSender)`\n| [Content
scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts)\n  
\n\n`[CrashManager.jsm](http://dxr.mozilla.org/mozilla-
central/source/toolkit/components/crashes/CrashManager.jsm)`\n| None\n  
\n\n`[nsIDirectoryService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIDirectoryService)`  
\n`[nsIProperties](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIProperties)`\n| None\n  
\n\n`[nsIDOMStorageManager](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIDOMStorageManager)`\n|
None\n  
\n\n`[nsIDOMRequestService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIDOMRequestService)`\n|
None\n  
\n\n`[nsIDownloadManager](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIDownloadManager)`\n|
`[downloads](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads)`\n  
\n\n`[nsIDroppedLinkHandler](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIDroppedLinkHandler)`\n|
None\n  
\n\n`[nsIEventListenerService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIEventListenerService)`\n|
None\n  
\n\n`[nsIEffectiveTLDService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIEffectiveTLDService)`\n|
None\n  
\n\n`[nsIFocusManager](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIFocusManager)`\n| None\n  
\n\n`[nsIIOService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIIOService)`  
\n`[nsIIOService2](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIIOService2)`\n| None\n  
\n\n`[nsILocaleService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsILocaleService)`\n| `[i18n
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)`\n  
\n\n`[nsILoginManager](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsILoginManager)`\n| None\n  
\n\n`[nsIWinMetroUtils](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIWinMetroUtils)`\n| None\n  
\n\n`[nsIMessageBroadcaster](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIMessageBroadcaster)`  
\n`[nsIFrameScriptLoader](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIFrameScriptLoader)`\n|
[Content scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts)\n  
\n\n`[nsIObserverService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIObserverService)`\n| None\n  
\n\n`[nsIPermissionManager](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIPermissionManager)`\n|
None\n  
\n\n`[nsIMessageBroadcaster](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIMessageBroadcaster)`  
\n`[nsIProcessScriptLoader](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIProcessScriptLoader)`\n|
[Content scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts)\n  
\n\n`[nsIPrefBranch](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIPrefBranch)`  
\n`[nsIPrefBranch2](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIPrefBranch2)`  
\n`[nsIPrefService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIPrefService)`\n| See
[Settings](/en-US/Add-
ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions#Settings).\n  
\n\n`[nsIPromptService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIPromptService)`\n| None\n  
\n\n`[mozIJSSubScriptLoader](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/mozIJSSubScriptLoader)`\n|
None\n  
\n\n`[nsIScriptSecurityManager](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIScriptSecurityManager)`\n|
None\n  
\n\n`[nsIBrowserSearchService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIBrowserSearchService)`\n|
None\n  
\n\n`[nsIAppStartup](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIAppStartup)`\n| None\n  
\n\n`[mozIStorageService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/mozIStorageService)`\n|
`[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)`\n  
\n\n`[nsIStringBundleService](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIStringBundleService)`\n|
`[i18n](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)`\n  
\n\n`[nsIPropertyBag2](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIPropertyBag2)`\n| None\n  
\n\n`[nsITelemetry](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsITelemetry)`\n| None\n  
\n\n`[nsIThreadManager](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIThreadManager)`\n| None\n  
\n\n`[nsIURIFixup](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIURIFixup)`\n| None\n  
\n\n`[nsIURLFormatter](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIURLFormatter)`\n| None\n  
\n\n`[nsIVersionComparator](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIVersionComparator)`\n|
None\n  
\n\n`[nsIWindowMediator](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIWindowMediator)`\n| None\n  
\n\n`[nsIWindowWatcher](/en-
US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIWindowWatcher)`\n| None\n  
\n\n\n

### Learn more

\n

\n

  * [JavaScript APIs available for extensions](/en-US/Add-ons/WebExtensions/API)
\n

  * [Background scripts for extensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts)
\n

\n

## Interacting with web content

\n

Historically, XUL/XPCOM extensions have been able to get direct access to web
content. For example, they can directly access and modify the page DOM using
`[gBrowser](/en-US/docs/Mozilla/Tech/XUL/tabbrowser)`:

\n

    
    
    gBrowser.contentWindow.document.querySelector("h1").innerHTML = "yadda yadda";

\n

However, this is only possible in single-process Firefox. In [multiprocess
Firefox](/en-US/docs/Mozilla/Firefox/Multiprocess_Firefox), web content and
extension code run in different processes, so this direct access is no longer
possible, and extensions which rely on it will break. Multiprocess Firefox is
coming soon, and multiprocess compatibility will be a necessity.

\n

XUL/XPCOM extensions can still interact with web content in multiprocess
Firefox by [refactoring the code that accesses web content into separate
scripts called frame scripts, and using the message manager to communicate
with these scripts](/en-US/Add-ons/Working_with_multiprocess_Firefox). But
this is complex and can involve deep changes to the extension's code.

\n

WebExtensions are multiprocess-compatible by default: code that interacts with
web content is factored into separate scripts called [content scripts](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts), that can communicate
with the rest of the extension using a messaging API.

\n

### Learn more

\n

\n

  * [Content scripts for extensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Content_scripts)
\n

\n

## Localization

\n

In a XUL/XPCOM extension you handle localization by supplying DTD or
properties for each supported language, and referring to them using locale
statements inside the chrome.manifest. You can then include localized strings
in UI elements or in code.

\n

The general approach with WebExtensions is similar, but the details are all
different. With WebExtensions you supply localized strings as a collection of
JSON files, one for each locale.

\n

To retrieve localized strings in extension code, use the
`[i18n](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/i18n)` API.

\n

WebExtensions don't have direct support for localizing strings appearing in
HTML, so you have to do this yourself, using JavaScript to retrieve localized
strings and to replace the HTML with the localized version.

\n

### Learn more

\n

\n

  * [Extensions Internationalization guide.](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Internationalization)
\n

  * [Example internationalized extension.](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)
\n

\n

## Settings

\n

XUL/XPCOM extensions typically store settings using the [XPCOM preferences
service](/en-US/Add-ons/Code_snippets/Preferences) or the [inline options
](/en-US/docs/Mozilla/Add-ons/Inline_Options) system.

\n

With WebExtensions you write an HTML file that presents the settings UI, which
can include a script for persisting the settings for your extension. The
script gets access to all the WebExtensions APIs, and it's generally expected
that you should use the `[storage](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API to persist settings.

\n

You then assign the HTML file's URL to the
`[options_ui](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/options_ui)` key in manifest.json. Your
settings page then appears in the extension's entry in the Add-ons
Manager.\xa0 The options page can also be programmatically opened with an API
call to `[browser.runtime.openOptionsPage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage)`.

\n

Note that WebExtensions does not give you access to the [Preferences API](/en-
US/docs/Mozilla/Tech/Preferences_API), so you can't directly get or set the
browser's own preferences.  
\n Some browser-specific preferences can however still be controlled through
the `[browser.browserSettings](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings)` or `[browser.privacy](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)` API.

\n

### Learn more

\n

\n

  * [Introduction to options pages](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Options_pages)
\n

  * [An example extension that has an options page](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
\n

\n]

