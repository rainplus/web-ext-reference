A sidebar is a pane that is displayed at the left-hand side of the browser
window, next to the web page. The browser provides a UI that enables the user
to see the currently available sidebars and to select a sidebar to display.
For example, Firefox has a "View > Sidebar" menu. Only one sidebar can be
shown at a time, and that sidebar will be displayed for all tabs and all
browser windows.

The browser may include a number of built-in sidebars. For example, Firefox
includes a sidebar for interacting with bookmarks:

![](https://mdn.mozillademos.org/files/14825/bookmarks-sidebar.png)Using the
`sidebar_action` manifest.json key, an extension can add its own sidebar to
the browser. It will be listed alongside the built-in sidebars, and the user
will be able to open it using the same mechanism as for the built-in sidebars.

Like a browser action popup, you specify the sidebar's contents as an HTML
document. When the user opens the sidebar, its document is loaded into every
open browser window. Each window gets its own instance of the document. When
new windows are opened, they get their own sidebar documents as well.

You can set a document for a particular tab using the [`sidebarAction.setPanel
()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction/setPanel
"Sets the HTML document that defines the content of this sidebar.") function.
A sidebar can figure out which window it belongs to using the
[`windows.getCurrent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/getCurrent "The documentation about this has not
yet been written; please consider contributing!") API:

    
    
    // sidebar.js
    browser.windows.getCurrent({populate: true}).then((windowInfo) => {
      myWindowId = windowInfo.id;
    });

This is useful if a sidebar wants to display different content for different
windows. For an example of this, see the ["annotate-page"
example](https://github.com/mdn/webextensions-examples/tree/master/annotate-
page).

Sidebar documents get access to the same set of privileged JavaScript APIs
that the extension's background and popup scripts get. They can get direct
access to the background page (unless the sidebar belongs to incognito mode
window) using [`runtime.getBackgroundPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBackgroundPage "Retrieves the Window object
for the background page running inside the current extension."), and can
interact with content scripts or native applications using messaging APIs like
[`tabs.sendMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage "Sends a single message from the
extension's background scripts \(or other privileged scripts, such as popup
scripts or options page scripts\) to any content scripts that belong to the
extension and are running in the specified tab.") and
[`runtime.sendNativeMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendNativeMessage "Sends a single message from
an extension to a native application.").

Sidebar documents are unloaded when their browser window is closed or when the
user closes the sidebar. This means that unlike background pages, sidebar
documents don't stay loaded all the time, but unlike browser action popups,
they stay loaded while the user interacts with web pages.

When an extension that defines a sidebar is first installed, its sidebar will
be opened automatically. This is intended to help the user understand that the
extension includes a sidebar. Note that it's not possible for extension to
open sidebars programmatically: sidebars can only be opened by the user.

## Specifying sidebars

To specify a sidebar, define the default document with the `[sidebar_action
](/en-US/Add-ons/WebExtensions/manifest.json/sidebar_action)` manifest.json
key, alongside a default title and icon:

    
    
    "sidebar_action": {
      "default_title": "My sidebar",
      "default_panel": "sidebar.html",
      "default_icon": "sidebar_icon.png"
    }

You can change the title, panel, and icon programmatically using the
[`sidebarAction`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction
"Gets and sets properties of an extension's sidebar.") API.

Title and icon are shown to the user in any UI provided by the browser to list
sidebars, such as the "View > Sidebar" menu in Firefox.

## Example

The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use a sidebar:

  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page) uses a sidebar.

