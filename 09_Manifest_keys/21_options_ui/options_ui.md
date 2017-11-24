[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n\n\n\n\n"options_ui": {\n  "page": "options/options.html"\n}

\n\n  
\n\n\n

Use the `options_ui` key to define an [options page](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Options_pages) for your extension.

\n

The options page contains settings for the extension. The user can access it
from the browser's add-ons manager, and you can open it from within your
extension using [`runtime.openOptionsPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage "This is an asynchronous
function that returns a Promise.").

\n

You specify `options_ui` as a path to an HTML file packaged with your
extension. The HTML file can include CSS and JavaScript files, just like a
normal web page. Unlike a normal page, though, the JavaScript can use all the
[WebExtension APIs](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/API) that the extension has
[permissions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) for. However, it runs in a
different scope than your background scripts.

\n

If you want to share data or functions between the JavaScript on your options
page and your background script(s), you can do so directly by obtaining a
reference to the [Window](/en-US/docs/Web/API/Window) of your background
scripts by using [`extension.getBackgroundPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getBackgroundPage "Alias for
runtime.getBackgroundPage\(\)."), or a reference to the [`Window`](/en-
US/docs/Web/API/Window "The window object represents a window containing a DOM
document; the document property points to the DOM document loaded in that
window.") of any of the pages running within your extension with
[`extension.getViews()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getViews "Returns an array of the Window
objects for each of the pages running inside the current extension. This
includes, for example:"). Alternately, you can communicate between the
JavaScript for your options page and your background script(s) using
`[runtime.sendMessage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendMessage)`, `[runtime.onMessage](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`, and/or
`[runtime.connect()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/connect)`.

\n

In general, you will want to store options changed on option pages using the
[storage API](/en-US/Add-ons/WebExtensions/API/storage) to either
[storage.sync](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/sync) (if
you want the settings synchronized across all instances of that browser that
the user is logged into), or [storage.local](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/local) (if the settings are local to the current
machine/profile). If you do so and your background script(s) or content
script(s) need to know about the change, your script(s) might choose to add a
listener to [storage.onChanged](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/onChanged).

\n

## Syntax

\n

The `options_ui` key is an object with the following contents:

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`browser_style`\n| `Boolean`\n| \n

Optional, defaulting to `true`.

\n

Use this to include a stylesheet in your page that will make it look
consistent with the browser's UI and with other extensions that use the
`browser_style` property. Although it defaults to `true`, it's recommended
that you include this property.

\n

In Firefox, the stylesheet can be seen at
chrome://browser/content/extension.css, or chrome://browser/content/extension-
mac.css on OS X.

\n

The [Firefox Style Guide](https://firefoxux.github.io/StyleGuide/#/controls)
describes the classes you can apply to elements in the popup in order to get
particular styles.

\n\n  
\n\n`open_in_tab`\n| `Boolean`\n| \n

Optional, defaults to `false`.

\n

If `true`, the options page will open in a normal browser tab, rather than
being integrated into the browser's add-ons manager.

\n\n  
\n\n`page`\n| `String`\n| \n

Mandatory.

\n

The path to an HTML file containing the specification of your options page.

\n

The path is relative to the location of manifest.json itself.

\n\n  
\n\n\n

## Example

\n

    
    
    \xa0 "options_ui": {\n\xa0\xa0\xa0 "page": "options/options.html"\n\xa0 }

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 52| \n No| \n Yes  
`chrome_style`| \n Yes| \n No| \n No| \n No| \n Yes  
`browser_style`| \n No| \n No| 55| \n No| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`chrome_style`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`browser_style`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
55| \nNo support\n\n No| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

