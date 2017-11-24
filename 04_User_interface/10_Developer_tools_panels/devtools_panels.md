[\n

\n

\n

This feature is available since Firefox 54.

\n

\n

When an extension provides tools that are of use to developers, it's possible
to add a UI for them to the browser's developer tools as a new panel.

\n

![Simple example showing the addition of "My panel" to the Developer Tools
tabs.](https://mdn.mozillademos.org/files/15035/devtools_panel_example.png)

\n

## Specifying a developer tools panel

\n

A developer tools panel is added using the
`[devtools.panels](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/devtools.panels)` API, which in turn needs to be run
from a special devtools page.

\n

Add the devtools page by including the
`[devtools_page](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/devtools_page)` key in extension's
[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) and provide the location of the page's HTML
file in the extension:

\n

    
    
    "devtools_page": "devtools-page.html"

\n

From the devtools page, call a script that will add the devtools panel:

\n

    
    
    <body>\n\xa0 <script src="devtools.js"></script>\n</body>

\n

In the script, create the devtools panel by specifying the panel's title,
icon, and HTML file that provides the panel's content:

\n

    
    
    function handleShown() {\n  console.log("panel is being shown");\n}\n\nfunction handleHidden() {\n  console.log("panel is being hidden");\n}\n\nbrowser.devtools.panels.create(\n  "My Panel",           // title\n  "icons/star.png",           // icon\n  "devtools/panel/panel.html"          // content\n).then((newPanel) => {\n  newPanel.onShown.addListener(handleShown);\n  newPanel.onHidden.addListener(handleHidden);\n});

\n

The extension can now run code in the inspected window using
`[`devtools`.inspectedWindow.eval()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/devtools.inspectedWindow/eval)` or by injecting a
content script via the background script by passing a message. You can find
more details on how to do this in [Extending the developer
tools.](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/Extending_the_developer_tools)

\n

## Examples

\n

The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use devtools
panels:

\n

\n

  * [devtools-panels](https://github.com/mdn/webextensions-examples/blob/master/devtools-panels/) use devtools panels:
\n

\n]

