[\n

\n

\n

This user interface option adds one or more items to a browser context menu.

\n

![Example of content menu items added by a WebExtension, from the context-
menu-demo
example](https://mdn.mozillademos.org/files/15051/context_menu_example.png)

\n

You would use this option to expose features that are relevant to specific
browser or web page contexts. For example, you could show features to open a
graphic editor when the user clicks on an image or offer a feature to save
page content when part of a page is selected. You can add plain menu items,
checkbox items, radio button groups, and separators to menus. Once a context
menu item has been added using [`contextMenus.create`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/contextMenus/create "The documentation about this
has not yet been written; please consider contributing!") it's displayed in
all browser tabs, but you can hide it by removing it with
[`contextMenus.remove`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextMenus/remove "The documentation about this has
not yet been written; please consider contributing!").

\n

## Specifying context menu items

\n

You manage context menu items programmatically, using the [`contextMenus
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextMenus "The
documentation about this has not yet been written; please consider
contributing!") API. However, you need to request the `contextMenus`
permission in your manifest.json to be able to take advantage of the API.

\n

    
    
    "permissions": ["contextMenus"]

\n

You can then add (and update or delete) the context menu items in your
extension's background script. To create a menu item you specify an id, its
title, and the context menus it should appear on:

\n

    
    
    browser.contextMenus.create({\n  id: "log-selection",\n  title: browser.i18n.getMessage("contextMenuItemSelectionLogger"),\n  contexts: ["selection"]\n}, onCreated);

\n

Your extension then listens for clicks on the menu items. The passed
information about the item clicked, the context where the click happened, and
details of the tab where the click took place can then be used to invoke the
appropriate extension functionality.

\n

    
    
    browser.contextMenus.onClicked.addListener(function(info, tab) {\n  switch (info.menuItemId) {\n    case "log-selection":\n      console.log(info.selectionText);\n      break;\n    ...\n  }\n})

\n

## Examples

\n

The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use context menu
items:

\n

\n

  * [menu-demo](https://github.com/mdn/webextensions-examples/tree/master/menu-demo) adds several items to the browser's context menu.
\n

  * [context-menu-copy-link-with-types](https://github.com/mdn/webextensions-examples/tree/master/context-menu-copy-link-with-types) adds a context menu item to links that copies the URL to the clipboard, as plain text and rich HTML.
\n

\n

\n]

