[\n

\n

Adds a button to the browser's toolbar.

\n

A [browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action)
is a button in the browser's toolbar.

\n

You can associate a popup with the button. The popup is specified using HTML,
CSS and JavaScript, just like a normal web page. JavaScript running in the
popup gets access to all the same WebExtension APIs as your background
scripts, but its global context is the popup, not the current page displayed
in the browser. To affect web pages you need to communicate with them via
[messages](/en-US/Add-ons/WebExtensions/Modify_a_web_page#Messaging).

\n

If you specify a popup, it will be shown \u2014 and the content will be loaded
\u2014 when the user clicks the icon. If you do not specify a popup, then when
the user clicks the icon an event is dispatched to your extension.

\n

You can define most of a browser action's properties declaratively using the
`[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` key in the manifest.json.

\n

With the `browserAction` API, you can:

\n

\n

  * use [`browserAction.onClicked`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction/onClicked "The documentation about this has not yet been written; please consider contributing!") to listen for clicks on the icon.
\n

  * get and set the icon's properties \u2014 icon, title, popup, and so on. You can get and set these globally across all tabs, or for a specific tab by passing the tab ID as an additional argument.
\n

\n

## Types

\n

\n[`browserAction.ColorArray`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/ColorArray "An array of four integers in
the range 0-255, defining an RGBA color. The four values specify the following
channels:")

\n    An array of four integers in the range 0-255 defining an RGBA color.

\n[`browserAction.ImageDataType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/ImageDataType "The documentation about
this has not yet been written; please consider contributing!")

\n    Pixel data for an image. Must be an `[ImageData](/en-
US/docs/Web/API/ImageData)` object (for example, from a [`<canvas>`](/en-
US/docs/Web/HTML/Element/canvas "Use the HTML <canvas> element with the canvas
scripting API to draw graphics and animations.") element).

\n\n

## Functions

\n

\n[`browserAction.setTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setTitle "Sets the browser action's title.
The title is displayed in a tooltip over the browser action's icon. You can
pass a tabId in as an optional parameter \\u2014 if you do this then the title
is changed only for the given tab.")

\n    Sets the browser action's title. This will be displayed in a tooltip.

\n[`browserAction.getTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getTitle "Gets the browser action's
title.")

\n    Gets the browser action's title.

\n[`browserAction.setIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setIcon "Sets the icon for the browser
action.")

\n    Sets the browser action's icon.

\n[`browserAction.setPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setPopup "The documentation about this has
not yet been written; please consider contributing!")

\n    Sets the HTML document to be opened as a popup when the user clicks on
the browser action's icon.

\n[`browserAction.getPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getPopup "The documentation about this has
not yet been written; please consider contributing!")

\n    Gets the HTML document set as the browser action's popup.

\n[`browserAction.openPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/openPopup "None.")

\n    Open the browser action's popup.

\n[`browserAction.setBadgeText()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setBadgeText "Sets the badge text for the
browser action. The badge is displayed on top of the icon.")

\n    Sets the browser action's badge text. The badge is displayed on top of
the icon.

\n[`browserAction.getBadgeText()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getBadgeText "Gets the browser action's
badge text.")

\n    Gets the browser action's badge text.

\n[`browserAction.setBadgeBackgroundColor()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setBadgeBackgroundColor "Sets the
background color for the badge.")

\n    Sets the badge's background color.

\n[`browserAction.getBadgeBackgroundColor()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getBadgeBackgroundColor "The documentation
about this has not yet been written; please consider contributing!")

\n    Gets the badge's background color.

\n[`browserAction.enable()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/enable "Enables the browser action for a
tab. By default, browser actions are enabled for all tabs.")

\n    Enables the browser action for a tab. By default, browser actions are
enabled for all tabs.

\n[`browserAction.disable()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/disable "Disables the browser action for a
tab, meaning that it cannot be clicked when that tab is active.")

\n    Disables the browser action for a tab, meaning that it cannot be clicked
when that tab is active.

\n\n

## Events

\n

\n[`browserAction.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/onClicked "The documentation about this
has not yet been written; please consider contributing!")

\n    Fired when a browser action icon is clicked. This event will not fire if
the browser action has a popup.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ColorArray`| \n Yes| \n Yes| 45| \n No| \n Yes  
`ImageDataType`| \n Yes| \n Yes| 45| \n No| \n Yes  
`disable`| \n Yes| \n Yes| 45| \n No| \n Yes  
`enable`| \n Yes| \n Yes| 45| \n No| \n Yes  
`getBadgeBackgroundColor`| \n Yes| \n Yes| 45| \n No| \n Yes  
`getBadgeText`| \n Yes| \n Yes| 45| \n No| \n Yes  
`getPopup`| \n Yes| \n No| 45| 57| \n Yes  
`getTitle`| \n Yes| 15| 45| 55| \n Yes  
`onClicked`| \n Yes| \n Yes| 45| 55| \n Yes  
`openPopup`| \n No| \n No| 57| \n No| \n No  
`setBadgeBackgroundColor`| \n Yes| \n Yes| 45| \n No| \n Yes  
`setBadgeText`| \n Yes| \n Yes| 45 *| \n No| \n Yes  
`setIcon`| \n Yes *| \n Yes *| 45| \n No| 15  
`setPopup`| \n Yes| \n Yes| 45| 57| \n Yes  
`setTitle`| \n Yes| 15| 45| 55| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ColorArray`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`ImageDataType`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`disable`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`enable`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`getBadgeBackgroundColor`| \nFull support\n\n Yes| \nFull support\n\n Yes|
\nFull support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`getBadgeText`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`getPopup`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 57  
`getTitle`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 55  
`onClicked`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 55  
`openPopup`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 57|
\nNo support\n\n No| \nNo support\n\n No  
`setBadgeBackgroundColor`| \nFull support\n\n Yes| \nFull support\n\n Yes|
\nFull support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`setBadgeText`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __On Firefox, the badge text is not cleared on navigation, see[bug 1395074](https://bugzil.la/1395074).
|  \nFull support\n\n Yes| \nNo support\n\n No  
`setIcon`| \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __Before Chrome 23, `path` couldn't specify multiple icon files, but had to be a string specifying a single icon path.
|  \nPartial support\nPartial| \nFull support\n\n 45| \nFull support\n\n 15|
\nNo support\n\n No  
`setPopup`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 57  
`setTitle`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 55  
  
\n

\n

The "Chrome incompatibilities" section is included from [
https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Chrome_incompatibilities](https://developer.mozilla.org/en-
US/Add-ons/WebExtensions/Chrome_incompatibilities) using the
[WebExtChromeCompat](/en-US/docs/Template:WebExtChromeCompat) macro.

\n

If you need to update this content, edit <https://developer.mozilla.org/en-US
/Add-ons/WebExtensions/Chrome_incompatibilities>, then shift-refresh this page
to see your changes.

\n

\n

## Example extensions

  * [bookmark-it](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)
  * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
  * [find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master/find-across-tabs)
  * [forget-it](https://github.com/mdn/webextensions-examples/tree/master/forget-it)
  * [google-userinfo](https://github.com/mdn/webextensions-examples/tree/master/google-userinfo)
  * [native-messaging](https://github.com/mdn/webextensions-examples/tree/master/native-messaging)
  * [open-my-page-button](https://github.com/mdn/webextensions-examples/tree/master/open-my-page-button)
  * [permissions](https://github.com/mdn/webextensions-examples/tree/master/permissions)
  * [store-collected-images](https://github.com/mdn/webextensions-examples/tree/master/store-collected-images)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.browserAction`](https://developer.chrome.com/extensions/browserAction)
API. This documentation is derived from
[`browser_action.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/browser_action.json)
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

