You can include html pages in your extension to provide forms, help, or any other content your extension needs.

![Example of a simple bundled page displayed as a detached panel.](https://mdn.mozillademos.org/files/15073/bundled_page_as_panel.png)

These pages also get access to the same privileged JavaScript APIs that are available to your extension's background scripts.

## Specifying extension pages

You can include HTML files, and their associated CSS or JavaScript files, in your extension. The files can be included in the root or organized within meaningful sub-folders.

    /my-extension
        /manifest.json
        /my-page.html
        /my-page.js

## Displaying extension pages

There are two options for displaying extension pages: [`windows.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/create "Creates a new window.") and [`tabs.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/create "Creates a new tab.").

Using `windows.create()`, for example, you can open an HTML page into a detached panel (a window without the normal browser UI of address bar,bookmark bar, and alike) to create a dialog-like user experience:

    var createData = {
      type: "detached_panel",
      url: "panel.html",
      width: 250,
      height: 100
    };
    var creating = browser.windows.create(createData);

When the window is no longer needed, it can be closed programmatically, for example, after the user clicks a button, by passing the id of the current window to [`windows.remove()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/remove "Closes a window and all the tabs insideit, given the window's ID."):

    document.getElementById("closeme").addEventListener("click", function(){
      var winId = browser.windows.WINDOW_ID_CURRENT;
      var removing = browser.windows.remove(winId);
    }); 

## Extension pages and history

By default, pages you open in this way will be stored in the user's history,just like normal web pages. If you don't want to have this behavior, use[`history.deleteUrl()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/history/deleteUrl "Removes all visits to the given URL from the browser history.") to remove the browser's record:

  
    const url = browser.extension.getURL("my-page.html");
    
    browser.tabs.create({url: url}).then(() => {
      // We don't want to sync this URL ever nor clutter the users history
      browser.history.deleteUrl({url: url});
    }).catch((e) => { throw e });

To use the history API, you must request the "history" [permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions) in your `[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)` file.

## Examples

The [window-manipulator](https://github.com/mdn/webextensions-examples/tree/master/window-manipulator) example WebExtension, from the [webextensions-examples](https://github.com/mdn/webextensions-examples) repo on GitHub, illustrates several of the options for creating windows.

