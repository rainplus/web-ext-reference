Type | `Object`  
---|---  
Mandatory | No  
Example |

    
    
    
    
    
    
    "options_ui": {
      "page": "options/options.html"
    }  
  
Use the `options_ui` key to define an [options page](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Options_pages) for your extension.

The options page contains settings for the extension. The user can access it
from the browser's add-ons manager, and you can open it from within your
extension using [`runtime.openOptionsPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage "This is an asynchronous
function that returns a Promise.").

You specify `options_ui` as a path to an HTML file packaged with your
extension. The HTML file can include CSS and JavaScript files, just like a
normal web page. Unlike a normal page, though, the JavaScript can use all the
[WebExtension APIs](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/API) that the extension has
[permissions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) for. However, it runs in a
different scope than your background scripts.

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

## Syntax

The `options_ui` key is an object with the following contents:

Name | Type | Description  
---|---|---  
`browser_style` | `Boolean` |

Optional, defaulting to `true`.

Use this to include a stylesheet in your page that will make it look
consistent with the browser's UI and with other extensions that use the
`browser_style` property. Although it defaults to `true`, it's recommended
that you include this property.

In Firefox, the stylesheet can be seen at
chrome://browser/content/extension.css, or chrome://browser/content/extension-
mac.css on OS X.

The [Firefox Style Guide](https://firefoxux.github.io/StyleGuide/#/controls)
describes the classes you can apply to elements in the popup in order to get
particular styles.  
  
`open_in_tab` | `Boolean` |

Optional, defaults to `false`.

If `true`, the options page will open in a normal browser tab, rather than
being integrated into the browser's add-ons manager.  
  
`page` | `String` |

Mandatory.

The path to an HTML file containing the specification of your options page.

The path is relative to the location of manifest.json itself.  
  
## Example

    
    
      "options_ui": {
        "page": "options/options.html"
      }

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 52|  No|  Yes  
`chrome_style`|  Yes|  No|  No|  No|  Yes  
`browser_style`|  No|  No| 55|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`chrome_style`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`browser_style`|  No support No|  No support No|  Full support 55|  No support
No|  No support No

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

