Extensions built with WebExtension APIs are designed to be compatible with
Chrome and Opera extensions: as far as possible, extensions written for those
browsers should run on Firefox with minimal changes.

However, Firefox currently has support for only a limited set of the features
and APIs supported by Chrome and Opera. We're working on adding more support,
but many features are not yet supported, and we may never support some.

## JavaScript APIs

### Callbacks and the chrome.* namespace

In Chrome, extensions access privileged JavaScript APIs using the `chrome`
namespace:

    
    
    chrome.browserAction.setIcon({path: "path/to/icon.png"});

WebExtensions access the equivalent APIs using the `browser` namespace:

    
    
    browser.browserAction.setIcon({path: "path/to/icon.png"});

Many of the APIs are asynchronous. In Chrome, asynchronous APIs use callbacks
to return values, and [`runtime.lastError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/lastError "The runtime.lastError property is set
when an asynchronous function has an error condition that it needs to report
to its caller.") to communicate errors:

    
    
    function logCookie(c) {
      if (chrome.extension.lastError) {
        console.error(chrome.extension.lastError);
      } else {
        console.log(c);
      }
    }
    
    chrome.cookies.set(
      {url: "https://developer.mozilla.org/"},
      logCookie
    );

The equivalent WebExtensions APIs use [promises](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise) instead:

    
    
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

### Firefox supports both `chrome` and `browser` namespaces

As a porting aid, the Firefox implementation of WebExtensions supports
`chrome`, using callbacks, as well as `browser`, using promises. This means
that many Chrome extensions will just work in Firefox without any changes.
However, this is not part of the WebExtensions standard, and might not be
supported by all compliant browsers.

If you do write your extension to use `browser` and promises, then we've also
developed a polyfill that will enable it to run in Chrome:
<https://github.com/mozilla/webextension-polyfill>.

### Partially supported APIs

The page [Browser support for JavaScript APIs](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Browser_support_for_JavaScript_APIs) includes compatibility
tables for all APIs that have any support in Firefox. Where there are caveats
around support for a given API item, this is indicated in these tables with an
asterisk "*" and in the reference page for the API item, the caveats are
explained.

These tables are generated from compatibility data stored as [JSON files in
GitHub](https://github.com/mdn/browser-compat-data).

The rest of this section describes compatibility issues that are not already
captured in the tables.

#### [notifications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications)

  * For `notifications.create(), with the "basic"` `[type](/en-US/Add-ons/WebExtensions/API/notifications/TemplateType)`, `iconUrl` is optional in Firefox. It is required in Chrome.
  * Notifications are cleared immediately when the user clicks on them. This is not the case in Chrome.
  * If you call `notifications.create()` more than once in rapid succession, Firefox may end up not displaying any notification at all. Waiting to make subsequent calls until within the `chrome.notifications.create() callback` function is not a sufficiently long delay to prevent this from happening.

#### [proxy](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/proxy)

  * This API is completely different to the design of the Chrome API. With Chrome's API an extension can register a PAC file, but can also define explicit proxying rules. Since this is also possible using the extended PAC files, this API only supports the PAC file approach. Because this API is incompatible with the Chrome `proxy` API, this API is only available through the `browser` namespace.

#### [tabs](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)

  * In Firefox, relative URLs passed into `tabs.executeScript()` or `tabs.insertCSS()` are resolved relative to the current page URL. In Chrome, these URLs are resolved relative to the extension's base URL. To work cross-browser, you can specify the path as an absolute URL, starting at the extension's root, like this:
    
        /path/to/script.js

  * In Firefox, querying tabs by URL with `tabs.query() `requires `"tabs"` permission. In Chrome, it's possible without the `"tabs"` permission but will limit results to tabs whose URLs match host permissions.
  * In Firefox, the `tabs.remove()` promise is fulfilled after the `beforeunload` event while in Chrome the callback does not wait for `beforeunload`.

#### [webRequest](/en-US/Add-ons/WebExtensions/API/webRequest)

  * In Firefox requests can be redirected only if their original URL uses the `http:` or `https:` scheme.
  * In Firefox, events are not fired for system requests (for example, extension upgrades or searchbar suggestions). From Firefox 57 onwards, Firefox makes an exception for extensions that need to intercept [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.") for proxy authorization. See the documentation for [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.").

#### [windows](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)

  * In Firefox `onFocusChanged` will trigger multiple times for a given focus change.

### Miscellaneous incompatibilities

#### URLs in CSS

Firefox resolves URLs in injected CSS files relative to the CSS file itself,
rather than to the page it's injected into.

#### Additional incompatibilities

Firefox does not support using `[alert()](/en-US/docs/Web/API/Window/alert)`,
`[confirm()](/en-US/docs/Web/API/Window/confirm)`, or `[prompt()](/en-
US/docs/Web/API/Window/prompt)` from background pages.

#### web_accessible_resources

In chrome, when a resource is listed in web_accessible_resources, it is
accessible as chrome-extension://<your-extension-id>/<path/to/resource>.  The
extension ID is fixed for a given extension.

Firefox implements it otherwise, using a random UUID that changes for every
instance of Firefox: moz-extension://<random-UUID>/<path/to/resource>. This
randomness can prevent you from doing a few things, such as add your specific
extension's URL to another domain's CSP policy.

#### Manifest "key" property

When working with an unpacked extension, Chrome allows for a ["key"
property](https://developer.chrome.com/extensions/manifest/key) to be added to
the manifest to pin the extension ID across different machines. This is mainly
useful when working with web_accessible_resources. Since Firefox uses random
UUIDs for web_accessible_resources, this property is unsupported.

#### Content script requests happen in the context of extension, not content
page

In Chrome when request is called (for example, using `[fetch()](/en-
US/docs/Web/API/Fetch_API/Using_Fetch)`) to relative URL like `/api` from
content script, it will be sent to `https://example.com/api`. In Firefox you
have to provide absolute URLs.

## manifest.json keys

The main [manifest.json](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) page includes a table describing browser
support for manifest.json keys. Where there are caveats around support for a
given key, this is indicated in the table with an asterisk "*" and in the
reference page for the key, the caveats are explained.

These tables are generated from compatibility data stored as [JSON files in
GitHub](https://github.com/mdn/browser-compat-data).

## Native messaging

### Command-line arguments

On Linux and Mac, Chrome passes one argument to the native app, which is the
origin of the extension that started it, in the form: `chrome-
extension://[extensionID]`. This enables the app to identify the extension.

On Windows, Chrome passes two arguments: the first is the origin of the
extension, and the second is a handle to the Chrome native window that started
the app.

### allowed_extensions

In Chrome, the `allowed_extensions` key in the app manifest is called
`allowed_origins` instead.

### App manifest location

Chrome expects to find the app manifest in a different place. See [Native
messaging host
location](https://developer.chrome.com/extensions/nativeMessaging#native-
messaging-host-location) in the Chrome docs.

