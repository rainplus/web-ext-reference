A [page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) is a
clickable icon inside the browser's address bar.

![](https://mdn.mozillademos.org/files/12960/page-action.png)

You can listen for clicks on the icon, or specify a
[popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/Popups) that will open when the icon is clicked.

If you specify a popup, you can define its contents and behavior using HTML,
CSS, and JavaScript, just like a normal web page. JavaScript running in the
popup gets access to all the same WebExtension APIs as your background
scripts.

You can define most of a page action's properties declaratively using the
[page_action key](/en-US/Add-ons/WebExtensions/manifest.json/page_action) in
your [manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json),
but can also redefine them programmatically using this API.

Page actions are for actions that are only relevant to particular pages. If
your icon should always be available, use a [browser action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Browser_action) instead.

## Types

[`pageAction.ImageDataType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/ImageDataType "Pixel data for an image.")

    Pixel data for an image.

## Functions

[`pageAction.show()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/show "Shows the page action for a given tab.
The page action is shown whenever the given tab is the active tab.")

    Shows the page action for a given tab.
[`pageAction.hide()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/hide "Hides the page action for a given
tab.")

    Hides the page action for a given tab.
[`pageAction.setTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/setTitle "Sets the title of the page action.
The title is displayed in a tooltip when the user hovers over the page
action.")

    Sets the page action's title. This is displayed in a tooltip over the page action.
[`pageAction.getTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/getTitle "Gets the title of the page
action.")

    Gets the page action's title.
[`pageAction.setIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/setIcon "Sets the icon for the page action.")

    Sets the page action's icon.
[`pageAction.setPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/setPopup "Sets the HTML document to be opened
as a popup when the user clicks on the page action's icon.")

    Sets the URL for the page action's popup.
[`pageAction.getPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/getPopup "Gets the URL for the HTML document
set as the popup for this page action.")

    Gets the URL for the page action's popup.
[`pageAction.openPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/openPopup "None.")

    Opens the page action's popup.

## Events

[`pageAction.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/pageAction/onClicked "The documentation about this has
not yet been written; please consider contributing!")

    Fired when a page action icon is clicked. This event will not fire if the page action has a popup.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ImageDataType`|  Yes|  No| 45|  No|  Yes  
`getPopup`|  Yes|  Yes| 45| 50 *|  Yes  
`getTitle`|  Yes|  Yes| 45|  No|  Yes  
`hide`|  Yes|  Yes| 45| 50 *|  Yes  
`onClicked`|  Yes|  Yes| 45| 50|  Yes  
`openPopup`|  No|  No| 57|  No|  No  
`setIcon`|  Yes *|  Yes *| 45|  No| 15  
`setPopup`|  Yes|  Yes| 45| 50 *|  Yes  
`setTitle`|  Yes|  Yes| 45|  No|  Yes  
`show`|  Yes|  Yes| 45| 50 *|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ImageDataType`|  Full support Yes|  No support No|  Full support 45|  Full
support Yes|  No support No  
`getPopup`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  Full support 50

Notes __

Full support 50

Notes __

     Notes __The 'tabId' parameter is ignored: the page action popup is the same for all tabs.  
`getTitle`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  No support No  
`hide`|  Full support Yes|  Full support Yes|  Full support 45|  Full support
Yes|  Full support 50

Notes __

Full support 50

Notes __

     Notes __Before version 56, the 'tabId' parameter was ignored, and the page action was hidden for all tabs.  
`onClicked`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  Full support 50  
`openPopup`|  No support No|  No support No|  Full support 57|  No support No|
No support No  
`setIcon`|  Partial support Partial

Notes __

Partial support Partial

Notes __

     Notes __Before Chrome 23, `path` couldn't specify multiple icon files, but had to be a string specifying a single icon path.
|  Partial support Partial|  Full support 45|  Full support 15|  No support No  
`setPopup`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  Full support 50

Notes __

Full support 50

Notes __

     Notes __The 'tabId' parameter is ignored, and the popup is set for all tabs.  
`setTitle`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  No support No  
`show`|  Full support Yes|  Full support Yes|  Full support 45|  Full support
Yes|  Full support 50

Notes __

Full support 50

Notes __

     Notes __Before version 56, the 'tabId' parameter was ignored, and the page action was shown for all tabs.  
  
## Example extensions

  * [apply-css](https://github.com/mdn/webextensions-examples/tree/master/apply-css)
  * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out)
  * [history-deleter](https://github.com/mdn/webextensions-examples/tree/master/history-deleter)

**Acknowledgements**

This API is based on Chromium's
[`chrome.pageAction`](https://developer.chrome.com/extensions/pageAction) API.
This documentation is derived from
[`page_action.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/page_action.json)
in the Chromium code.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.
    //
    // Redistribution and use in source and binary forms, with or without
    // modification, are permitted provided that the following conditions are
    // met:
    //
    //    * Redistributions of source code must retain the above copyright
    // notice, this list of conditions and the following disclaimer.
    //    * Redistributions in binary form must reproduce the above
    // copyright notice, this list of conditions and the following disclaimer
    // in the documentation and/or other materials provided with the
    // distribution.
    //    * Neither the name of Google Inc. nor the names of its
    // contributors may be used to endorse or promote products derived from
    // this software without specific prior written permission.
    //
    // THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    // "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    // LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    // A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    // OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    // SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    // LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    // DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    // THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    // (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    // OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
  *[
No support

]: No support

  *[
 Partial support

]: Partial support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[
Partial support

]: Partial support

  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[
Full support

]: Full support

  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

