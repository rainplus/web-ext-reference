[\n

\n

Commonly referred to as a [browser action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction), this user interface option is a button
added to the browser toolbar. Users click the button to interact with your
extension.  
\n![](https://mdn.mozillademos.org/files/12966/browser-action.png)

\n

Use this button when your extension's features are applicable to almost all
web pages. The toolbar button is visible in all browser tabs.

\n

Compare to the [address bar button](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Page_actions), which offers similar behavior but is used in
situations where the extension needs to be accessed on specific pages only.

\n

## Specifying the browser action

\n

You define the browser action's properties using the
`[browser_action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` key in manifest.json:

\n

    
    
    "browser_action": {\n  "default_icon": {\n    "19": "button/geo-19.png",\n    "38": "button/geo-38.png"\n  },\n  "default_title": "Whereami?"\n}

\n

The only mandatory key is `default_icon`.

\n

There are two ways to specify a browser action: with or without a [popup](/en-
US/Add-ons/WebExtensions/Popups). If you don't specify a popup, when the user
clicks the button an event is dispatched to the extension, which the extension
listens for using [`browserAction.onClicked`](https://developer.mozilla.org
/en-US/docs/Mozilla/Add-ons/WebExtensions/API/BrowserAction/onClicked "Fired
when a browser action icon is clicked. This event will not fire if the browser
action has a popup."):

\n

    
    
    browser.browserAction.onClicked.addListener(handleClick);

\n

If you specify a popup, the click event is not dispatched: instead, the popup
is shown when the user clicks the button. The user is able to interact with
the popup and it closes automatically when the user clicks outside it. See the
[Popup ](/en-US/Add-ons/WebExtensions/Popups)article for more details on
creating and managing popups.

\n

Note that your extension can have only one browser action.

\n

You can change any of the browser action properties programmatically using the
`[browserAction](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction)` API.

\n

## Examples

\n

The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub contains several examples of extensions that uses browser
actions:

\n

\n

  * [bookmark-it](https://github.com/mdn/webextensions-examples/blob/master/bookmark-it/) uses a browser action without a popup.
\n

  * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify) uses a browser action with a popup.
\n

\n]

