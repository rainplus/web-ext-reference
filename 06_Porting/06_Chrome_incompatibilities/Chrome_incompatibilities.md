[\n

\n

Extensions built with WebExtension APIs are designed to be compatible with
Chrome and Opera extensions: as far as possible, extensions written for those
browsers should run on Firefox with minimal changes.

\n

However, Firefox currently has support for only a limited set of the features
and APIs supported by Chrome and Opera. We're working on adding more support,
but many features are not yet supported, and we may never support some.

\n

## JavaScript APIs

\n

### Callbacks and the chrome.* namespace

\n

In Chrome, extensions access privileged JavaScript APIs using the `chrome`
namespace:

\n

    
    
    chrome.browserAction.setIcon({path: "path/to/icon.png"});

\n

WebExtensions access the equivalent APIs using the `browser` namespace:

\n

    
    
    browser.browserAction.setIcon({path: "path/to/icon.png"});

\n

Many of the APIs are asynchronous. In Chrome, asynchronous APIs use callbacks
to return values, and [`runtime.lastError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/lastError "The runtime.lastError property is set
when an asynchronous function has an error condition that it needs to report
to its caller.") to communicate errors:

\n

    
    
    function logCookie(c) {\n  if (chrome.extension.lastError) {\n    console.error(chrome.extension.lastError);\n  } else {\n    console.log(c);\n  }\n}\n\nchrome.cookies.set(\n  {url: "https://developer.mozilla.org/"},\n  logCookie\n);

\n

The equivalent WebExtensions APIs use [promises](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise) instead:

\n

    
    
    function logCookie(c) {\n  console.log(c);\n}\n\nfunction logError(e) {\n  console.error(e);\n}\n\nvar setCookie = browser.cookies.set(\n  {url: "https://developer.mozilla.org/"}\n);\nsetCookie.then(logCookie, logError);

\n

### Firefox supports both `chrome` and `browser` namespaces

\n

As a porting aid, the Firefox implementation of WebExtensions supports
`chrome`, using callbacks, as well as `browser`, using promises. This means
that many Chrome extensions will just work in Firefox without any changes.
However, this is not part of the WebExtensions standard, and might not be
supported by all compliant browsers.

\n

If you do write your extension to use `browser` and promises, then we've also
developed a polyfill that will enable it to run in Chrome:
<https://github.com/mozilla/webextension-polyfill>.

\n

### Partially supported APIs

\n

The page [Browser support for JavaScript APIs](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Browser_support_for_JavaScript_APIs) includes compatibility
tables for all APIs that have any support in Firefox. Where there are caveats
around support for a given API item, this is indicated in these tables with an
asterisk "*" and in the reference page for the API item, the caveats are
explained.

\n

These tables are generated from compatibility data stored as [JSON files in
GitHub](https://github.com/mdn/browser-compat-data).

\n

The rest of this section describes compatibility issues that are not already
captured in the tables.

\n

#### [notifications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications)

\n

\n

  * For `notifications.create(), with the "basic"` `[type](/en-US/Add-ons/WebExtensions/API/notifications/TemplateType)`, `iconUrl` is optional in Firefox. It is required in Chrome.
\n

  * Notifications are cleared immediately when the user clicks on them. This is not the case in Chrome.
\n

  * If you call `notifications.create()` more than once in rapid succession, Firefox may end up not displaying any notification at all. Waiting to make subsequent calls until within the `chrome.notifications.create() callback` function is not a sufficiently long delay to prevent this from happening.
\n

\n

#### [proxy](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/proxy)

\n

\n

  * This API is completely different to the design of the Chrome API. With Chrome's API an extension can register a PAC file, but can also define explicit proxying rules. Since this is also possible using the extended PAC files, this API only supports the PAC file approach. Because this API is incompatible with the Chrome `proxy` API, this API is only available through the `browser` namespace.
\n

\n

#### [tabs](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)

\n

\n

  * \n

In Firefox, relative URLs passed into `tabs.executeScript()` or
`tabs.insertCSS()` are resolved relative to the current page URL. In Chrome,
these URLs are resolved relative to the extension's base URL. To work cross-
browser, you can specify the path as an absolute URL, starting at the
extension's root, like this:

\n

    
        /path/to/script.js

\n

\n

  * In Firefox, querying tabs by URL with `tabs.query() `requires\xa0`"tabs"`\xa0permission. In Chrome, it's possible without the `"tabs"`\xa0permission but will limit results to tabs whose URLs match host permissions.
\n

  * In Firefox, the `tabs.remove()` promise is fulfilled after the `beforeunload` event while in Chrome the callback does not wait for `beforeunload`.
\n

\n

#### [webRequest](/en-US/Add-ons/WebExtensions/API/webRequest)

\n

\n

  * In Firefox requests can be redirected only if their original URL uses the `http:`\xa0or `https:` scheme.
\n

  * In Firefox, events are not fired for system requests (for example, extension upgrades or searchbar suggestions). From Firefox 57 onwards, Firefox makes an exception for extensions that need to intercept [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.") for proxy authorization. See the documentation for [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.").
\n

\n

#### [windows](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)

\n

\n

  * In Firefox `onFocusChanged` will trigger multiple times for a given focus change.
\n

\n

### Miscellaneous incompatibilities

\n

#### URLs in CSS

\n

Firefox resolves URLs in injected CSS files relative to the CSS file itself,
rather than to the page it's injected into.

\n

#### Additional incompatibilities

\n

Firefox does not support using `[alert()](/en-US/docs/Web/API/Window/alert)`,
`[confirm()](/en-US/docs/Web/API/Window/confirm)`, or\xa0`[prompt()](/en-
US/docs/Web/API/Window/prompt)` from background pages.

\n

#### web_accessible_resources

\n

In chrome, when a resource is listed in\xa0web_accessible_resources, it is
accessible as chrome-extension://<your-extension-id>/<path/to/resource>.
\xa0The extension ID is fixed for a given extension.

\n

Firefox implements it otherwise, using a random UUID that changes for every
instance of Firefox: moz-extension://<random-UUID>/<path/to/resource>. This
randomness can prevent you from doing a few things, such as add your specific
extension's URL\xa0to another domain's\xa0CSP policy.

\n

#### Manifest "key" property

\n

When working with an unpacked extension, Chrome allows for a ["key"
property](https://developer.chrome.com/extensions/manifest/key) to be added to
the manifest to pin the extension ID across different machines. This is mainly
useful when working with web_accessible_resources. Since Firefox uses random
UUIDs for web_accessible_resources, this property is unsupported.

\n

#### Content script requests happen in the context of extension, not content
page

\n

In Chrome when request is called (for example, using `[fetch()](/en-
US/docs/Web/API/Fetch_API/Using_Fetch)`)\xa0to relative URL like
`/api`\xa0from content script, it will be sent to `https://example.com/api`.
In Firefox you have to provide absolute URLs.\xa0

\n

## manifest.json keys

\n

The main [manifest.json](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) page includes a table describing browser
support for manifest.json keys. Where there are caveats around support for a
given key, this is indicated in the table with an asterisk "*" and in the
reference page for the key, the caveats are explained.

\n

These tables are generated from compatibility data stored as [JSON files in
GitHub](https://github.com/mdn/browser-compat-data).

\n

## Native messaging

\n

### Command-line arguments

\n

On Linux and Mac, Chrome passes one argument to the native app, which is the
origin of the extension that started it, in the form: `chrome-
extension://[extensionID]`. This enables the app to identify the extension.

\n

On Windows, Chrome passes two arguments: the first is the origin of the
extension, and the second is a handle to the Chrome native window that started
the app.

\n

### allowed_extensions

\n

In Chrome, the `allowed_extensions` key in the app manifest is called
`allowed_origins` instead.

\n

### App manifest location

\n

Chrome expects to find the app manifest in a different place. See [Native
messaging host
location](https://developer.chrome.com/extensions/nativeMessaging#native-
messaging-host-location) in the Chrome docs.\xa0

\n]

