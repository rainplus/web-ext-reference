Commonly referred to as a [page action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction), this user interface option is a button
added to the browser address bar. Users click the button to interact with your
extension.

![](https://mdn.mozillademos.org/files/12960/page-action.png)

Use this button when a feature is only relevant for some web pages. By
default, the address bar button is hidden in all browser tabs, and you call
[`pageAction.show()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/PageAction/show "Shows the page action for a given tab.
The page action is shown whenever the given tab is the active tab.") and
[`pageAction.hide()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/PageAction/hide "Hides the page action for a given
tab.") to show or hide it in specific tabs.

Compare to the [toolbar button](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Browser_action), which offers similar behavior but is used
in situations where the extension's features are applicable to almost every
web page.

## Specifying the page action

You define the page action's properties using the
`[page_action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/page_action)` key in manifest.json:

    
    
    "page_action": {
      "browser_style": true,
      "default_icon": {
        "19": "button/geo-19.png",
        "38": "button/geo-38.png"
      },
      "default_title": "Whereami?"
    }

The only mandatory key is `default_icon`.

There are two ways to specify a page action: with or without a [popup](/en-US
/Add-ons/WebExtensions/Popups). If you don't specify a popup, when the user
clicks the button an event is dispatched to the extension, which the extension
listens for using [`pageAction.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/onClicked "Fired when a browser action icon
is clicked. This event will not fire if the browser action has a popup."):

    
    
    browser.pageAction.onClicked.addListener(handleClick);

If you specify a popup, the click event is not dispatched: instead, the popup
is shown when the user clicks the button. The user is able to interact with
the popup and it closes automatically when the user clicks outside it. See the
[Popup ](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Popups)article for more details on creating and managing
popups.

Note that your extension can have one page action only.

You can change any of the page action properties programmatically using the
`[pageAction](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction)` API.

## Examples

The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use page action:

  * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out) uses a page action without a popup.

