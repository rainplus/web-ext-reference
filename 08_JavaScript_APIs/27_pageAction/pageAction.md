[\n

\n

A [page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) is a
clickable icon inside the browser's address bar.

\n

![](https://mdn.mozillademos.org/files/12960/page-action.png)

\n

You can listen for clicks on the icon, or specify a
[popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/Popups) that will open when the icon is clicked.

\n

If you specify a popup, you can define its contents and behavior using HTML,
CSS, and JavaScript, just like a normal web page. JavaScript running in the
popup gets access to all the same WebExtension APIs as your background
scripts.

\n

You can define most of a page action's properties declaratively using the
[page_action key](/en-US/Add-ons/WebExtensions/manifest.json/page_action) in
your [manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json),
but can also redefine them programmatically using this API.

\n

Page actions are for actions that are only relevant to particular pages. If
your icon should always be available, use a [browser action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Browser_action) instead.

\n

## Types

\n

\n[`pageAction.ImageDataType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/ImageDataType "Pixel data for an image.")

\n    Pixel data for an image.

\n\n

## Functions

\n

\n[`pageAction.show()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/show "Shows the page action for a given tab.
The page action is shown whenever the given tab is the active tab.")

\n    Shows the page action for a given tab.

\n[`pageAction.hide()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/hide "Hides the page action for a given
tab.")

\n    Hides the page action for a given tab.

\n[`pageAction.setTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/setTitle "Sets the title of the page action.
The title is displayed in a tooltip when the user hovers over the page
action.")

\n    Sets the page action's title. This is displayed in a tooltip over the
page action.

\n[`pageAction.getTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/getTitle "Gets the title of the page
action.")

\n    Gets the page action's title.

\n[`pageAction.setIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/setIcon "Sets the icon for the page action.")

\n    Sets the page action's icon.

\n[`pageAction.setPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/setPopup "Sets the HTML document to be opened
as a popup when the user clicks on the page action's icon.")

\n    Sets the URL for the page action's popup.

\n[`pageAction.getPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/getPopup "Gets the URL for the HTML document
set as the popup for this page action.")

\n    Gets the URL for the page action's popup.

\n[`pageAction.openPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/openPopup "None.")

\n    Opens the page action's popup.

\n\n

## Events

\n

\n[`pageAction.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/onClicked "The documentation about this has
not yet been written; please consider contributing!")

\n    Fired when a page action icon is clicked. This event will not fire if
the page action has a popup.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ImageDataType`| \n Yes| \n No| 45| \n No| \n Yes  
`getPopup`| \n Yes| \n Yes| 45| 50 *| \n Yes  
`getTitle`| \n Yes| \n Yes| 45| \n No| \n Yes  
`hide`| \n Yes| \n Yes| 45| 50 *| \n Yes  
`onClicked`| \n Yes| \n Yes| 45| 50| \n Yes  
`openPopup`| \n No| \n No| 57| \n No| \n No  
`setIcon`| \n Yes *| \n Yes *| 45| \n No| 15  
`setPopup`| \n Yes| \n Yes| 45| 50 *| \n Yes  
`setTitle`| \n Yes| \n Yes| 45| \n No| \n Yes  
`show`| \n Yes| \n Yes| 45| 50 *| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ImageDataType`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`getPopup`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 50

Notes __

\nFull support\n\n 50

Notes __

     Notes __The 'tabId' parameter is ignored: the page action popup is the same for all tabs.  
`getTitle`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`hide`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 50

Notes __

\nFull support\n\n 50

Notes __

     Notes __Before version 56, the 'tabId' parameter was ignored, and the page action was hidden for all tabs.  
`onClicked`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 50  
`openPopup`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 57|
\nNo support\n\n No| \nNo support\n\n No  
`setIcon`| \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __Before Chrome 23, `path` couldn't specify multiple icon files, but had to be a string specifying a single icon path.
|  \nPartial support\nPartial| \nFull support\n\n 45| \nFull support\n\n 15|
\nNo support\n\n No  
`setPopup`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 50

Notes __

\nFull support\n\n 50

Notes __

     Notes __The 'tabId' parameter is ignored, and the popup is set for all tabs.  
`setTitle`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`show`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 50

Notes __

\nFull support\n\n 50

Notes __

     Notes __Before version 56, the 'tabId' parameter was ignored, and the page action was shown for all tabs.  
  
\n

## Example extensions

  * [apply-css](https://github.com/mdn/webextensions-examples/tree/master/apply-css)
  * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out)
  * [history-deleter](https://github.com/mdn/webextensions-examples/tree/master/history-deleter)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.pageAction`](https://developer.chrome.com/extensions/pageAction) API.
This documentation is derived from
[`page_action.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/page_action.json)
in the Chromium code.

\n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

\n

\n

\n

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.\n//\n// Redistribution and use in source and binary forms, with or without\n// modification, are permitted provided that the following conditions are\n// met:\n//\n//    * Redistributions of source code must retain the above copyright\n// notice, this list of conditions and the following disclaimer.\n//    * Redistributions in binary form must reproduce the above\n// copyright notice, this list of conditions and the following disclaimer\n// in the documentation and/or other materials provided with the\n// distribution.\n//    * Neither the name of Google Inc. nor the names of its\n// contributors may be used to endorse or promote products derived from\n// this software without specific prior written permission.\n//\n// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n

\n

\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

