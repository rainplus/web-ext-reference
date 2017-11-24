[



Adds a button to the browser's toolbar.



A [browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action)
is a button in the browser's toolbar.



You can associate a popup with the button. The popup is specified using HTML,
CSS and JavaScript, just like a normal web page. JavaScript running in the
popup gets access to all the same WebExtension APIs as your background
scripts, but its global context is the popup, not the current page displayed
in the browser. To affect web pages you need to communicate with them via
[messages](/en-US/Add-ons/WebExtensions/Modify_a_web_page#Messaging).



If you specify a popup, it will be shown \u2014 and the content will be loaded
\u2014 when the user clicks the icon. If you do not specify a popup, then when
the user clicks the icon an event is dispatched to your extension.



You can define most of a browser action's properties declaratively using the
`[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` key in the manifest.json.



With the `browserAction` API, you can:





  * use [`browserAction.onClicked`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction/onClicked "The documentation about this has not yet been written; please consider contributing!") to listen for clicks on the icon.


  * get and set the icon's properties \u2014 icon, title, popup, and so on. You can get and set these globally across all tabs, or for a specific tab by passing the tab ID as an additional argument.




## Types



[`browserAction.ColorArray`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/ColorArray "An array of four integers in
the range 0-255, defining an RGBA color. The four values specify the following
channels:")

    An array of four integers in the range 0-255 defining an RGBA color.

[`browserAction.ImageDataType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/ImageDataType "The documentation about
this has not yet been written; please consider contributing!")

    Pixel data for an image. Must be an `[ImageData](/en-
US/docs/Web/API/ImageData)` object (for example, from a [`<canvas>`](/en-
US/docs/Web/HTML/Element/canvas "Use the HTML <canvas> element with the canvas
scripting API to draw graphics and animations.") element).



## Functions



[`browserAction.setTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setTitle "Sets the browser action's title.
The title is displayed in a tooltip over the browser action's icon. You can
pass a tabId in as an optional parameter \\u2014 if you do this then the title
is changed only for the given tab.")

    Sets the browser action's title. This will be displayed in a tooltip.

[`browserAction.getTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getTitle "Gets the browser action's
title.")

    Gets the browser action's title.

[`browserAction.setIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setIcon "Sets the icon for the browser
action.")

    Sets the browser action's icon.

[`browserAction.setPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setPopup "The documentation about this has
not yet been written; please consider contributing!")

    Sets the HTML document to be opened as a popup when the user clicks on
the browser action's icon.

[`browserAction.getPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getPopup "The documentation about this has
not yet been written; please consider contributing!")

    Gets the HTML document set as the browser action's popup.

[`browserAction.openPopup()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/openPopup "None.")

    Open the browser action's popup.

[`browserAction.setBadgeText()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setBadgeText "Sets the badge text for the
browser action. The badge is displayed on top of the icon.")

    Sets the browser action's badge text. The badge is displayed on top of
the icon.

[`browserAction.getBadgeText()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getBadgeText "Gets the browser action's
badge text.")

    Gets the browser action's badge text.

[`browserAction.setBadgeBackgroundColor()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setBadgeBackgroundColor "Sets the
background color for the badge.")

    Sets the badge's background color.

[`browserAction.getBadgeBackgroundColor()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/getBadgeBackgroundColor "The documentation
about this has not yet been written; please consider contributing!")

    Gets the badge's background color.

[`browserAction.enable()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/enable "Enables the browser action for a
tab. By default, browser actions are enabled for all tabs.")

    Enables the browser action for a tab. By default, browser actions are
enabled for all tabs.

[`browserAction.disable()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/disable "Disables the browser action for a
tab, meaning that it cannot be clicked when that tab is active.")

    Disables the browser action for a tab, meaning that it cannot be clicked
when that tab is active.



## Events



[`browserAction.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/onClicked "The documentation about this
has not yet been written; please consider contributing!")

    Fired when a browser action icon is clicked. This event will not fire if
the browser action has a popup.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ColorArray`|  Yes|  Yes| 45|  No|  Yes  
`ImageDataType`|  Yes|  Yes| 45|  No|  Yes  
`disable`|  Yes|  Yes| 45|  No|  Yes  
`enable`|  Yes|  Yes| 45|  No|  Yes  
`getBadgeBackgroundColor`|  Yes|  Yes| 45|  No|  Yes  
`getBadgeText`|  Yes|  Yes| 45|  No|  Yes  
`getPopup`|  Yes|  No| 45| 57|  Yes  
`getTitle`|  Yes| 15| 45| 55|  Yes  
`onClicked`|  Yes|  Yes| 45| 55|  Yes  
`openPopup`|  No|  No| 57|  No|  No  
`setBadgeBackgroundColor`|  Yes|  Yes| 45|  No|  Yes  
`setBadgeText`|  Yes|  Yes| 45 *|  No|  Yes  
`setIcon`|  Yes *|  Yes *| 45|  No| 15  
`setPopup`|  Yes|  Yes| 45| 57|  Yes  
`setTitle`|  Yes| 15| 45| 55|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ColorArray`|  Full support Yes| Full support Yes| Full
support 45| Full support Yes| No support No  
`ImageDataType`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| No support No  
`disable`| Full support Yes| Full support Yes| Full support
45| Full support Yes| No support No  
`enable`| Full support Yes| Full support Yes| Full support
45| Full support Yes| No support No  
`getBadgeBackgroundColor`| Full support Yes| Full support Yes|
Full support 45| Full support Yes| No support No  
`getBadgeText`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| No support No  
`getPopup`| Full support Yes| No support No| Full support
45| Full support Yes| Full support 57  
`getTitle`| Full support Yes| Full support 15| Full support
45| Full support Yes| Full support 55  
`onClicked`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 55  
`openPopup`| No support No| No support No| Full support 57|
No support No| No support No  
`setBadgeBackgroundColor`| Full support Yes| Full support Yes|
Full support 45| Full support Yes| No support No  
`setBadgeText`| Full support Yes| Full support Yes| Full
support 45

Notes __

Full support 45

Notes __

     Notes __On Firefox, the badge text is not cleared on navigation, see[bug 1395074](https://bugzil.la/1395074).
|  Full support Yes| No support No  
`setIcon`| Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __Before Chrome 23, `path` couldn't specify multiple icon files, but had to be a string specifying a single icon path.
|  Partial supportPartial| Full support 45| Full support 15|
No support No  
`setPopup`| Full support Yes| Full support Yes| Full support
45| Full support Yes| Full support 57  
`setTitle`| Full support Yes| Full support 15| Full support
45| Full support Yes| Full support 55  
  




The "Chrome incompatibilities" section is included from [
https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Chrome_incompatibilities](https://developer.mozilla.org/en-
US/Add-ons/WebExtensions/Chrome_incompatibilities) using the
[WebExtChromeCompat](/en-US/docs/Template:WebExtChromeCompat) macro.



If you need to update this content, edit <https://developer.mozilla.org/en-US
/Add-ons/WebExtensions/Chrome_incompatibilities>, then shift-refresh this page
to see your changes.





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



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.browserAction`](https://developer.chrome.com/extensions/browserAction)
API. This documentation is derived from
[`browser_action.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/browser_action.json)
in the Chromium code.



Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.







    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.//// Redistribution and use in source and binary forms, with or without// modification, are permitted provided that the following conditions are// met:////    * Redistributions of source code must retain the above copyright// notice, this list of conditions and the following disclaimer.//    * Redistributions in binary form must reproduce the above// copyright notice, this list of conditions and the following disclaimer// in the documentation and/or other materials provided with the// distribution.//    * Neither the name of Google Inc. nor the names of its// contributors may be used to endorse or promote products derived from// this software without specific prior written permission.//// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[ Partial support]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

