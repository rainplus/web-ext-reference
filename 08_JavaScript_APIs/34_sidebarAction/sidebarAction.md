[



Gets and sets properties of an extension's sidebar.



A [sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars) is a pane that
is displayed at the left-hand or right-hand side of the browser window, next
to the web page. The browser provides a UI that enables the user to see the
currently available sidebars and to select a sidebar to display. Using the
`[sidebar_action](/en-US/Add-ons/WebExtensions/manifest.json/sidebar_action)`
manifest.json key, an extension can define its own sidebar. Using the
`sidebarAction` API described here, an extension can get and set the sidebar's
properties.



The `sidebarAction` API is closely modeled on the [`browserAction`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction "Adds a button to the
browser's toolbar.") API.



The sidebarAction API is based on Opera's [sidebarAction
API](https://dev.opera.com/extensions/sidebar-action-api/). However, note that
the following are not yet supported: `setBadgeText()`, `getBadgeText()`,
`setBadgeBackgroundColor()`, `getBadgeBackgroundColor()`, `onFocus`, `onBlur`.



## Types



[`sidebarAction.ImageDataType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/ImageDataType "Pixel data for an image.
Must be an ImageData object \(for example, from a <canvas> element\).")

    Pixel data for an image. Must be an `[ImageData](/en-
US/docs/Web/API/ImageData)` object (for example, from a [`<canvas>`](/en-
US/docs/Web/HTML/Element/canvas "Use the HTML <canvas> element with the canvas
scripting API to draw graphics and animations.") element).



## Functions



[`sidebarAction.setPanel()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/setPanel "Sets the HTML document that
defines the content of this sidebar.")

    Sets the sidebar's panel.

[`sidebarAction.getPanel()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/getPanel "Gets a URL to the HTML document
that defines the sidebar's contents.")

    Gets the sidebar's panel.

[`sidebarAction.setTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/setTitle "Sets the sidebar's title. The
title is displayed anywhere the browser lists available sidebars. For example,
Firefox will show it in the "View > Sidebar" menu. It's also shown at the top
o the sidebar when the sidebar is open.")

    Sets the sidebar's title. This will be displayed in any UI provided by
the browser to list sidebars, such as a menu.

[`sidebarAction.getTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/getTitle "Gets the sidebar's title.")

    Gets the sidebar's title.

[`sidebarAction.setIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/setIcon "Sets the icon for the sidebar.")

    Sets the sidebar's icon.

[`sidebarAction.open()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/open "None.")

    Opens the sidebar.

[`sidebarAction.close()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/close "Closes the sidebar in the active
window, if it is the extension's own sidebar.")

    Closes the sidebar.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ImageDataType`|  No|  No| 54|  No|  Yes  
`close`|  No|  No| 57|  No|  No  
`getPanel`|  No|  No| 54|  No|  Yes  
`getTitle`|  No|  No| 54|  No|  Yes  
`open`|  No|  No| 57|  No|  No  
`setIcon`|  No|  No| 54|  No|  Yes  
`setPanel`|  No|  No| 54|  No|  Yes  
`setTitle`|  No|  No| 54|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ImageDataType`|  No support No| No support No| Full support
54| Full support Yes| No support No  
`close`| No support No| No support No| Full support 57| No
support No| No support No  
`getPanel`| No support No| No support No| Full support 54|
Full support Yes| No support No  
`getTitle`| No support No| No support No| Full support 54|
Full support Yes| No support No  
`open`| No support No| No support No| Full support 57| No
support No| No support No  
`setIcon`| No support No| No support No| Full support 54|
Full support Yes| No support No  
`setPanel`| No support No| No support No| Full support 54|
Full support Yes| No support No  
`setTitle`| No support No| No support No| Full support 54|
Full support Yes| No support No  
  


## Example add-ons





  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page)




 **Acknowledgements** 

This API is based on Opera's
[`chrome.sidebarAction`](https://dev.opera.com/extensions/sidebar-action-api/)
API.



Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.







    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.//// Redistribution and use in source and binary forms, with or without// modification, are permitted provided that the following conditions are// met:////    * Redistributions of source code must retain the above copyright// notice, this list of conditions and the following disclaimer.//    * Redistributions in binary form must reproduce the above// copyright notice, this list of conditions and the following disclaimer// in the documentation and/or other materials provided with the// distribution.//    * Neither the name of Google Inc. nor the names of its// contributors may be used to endorse or promote products derived from// this software without specific prior written permission.//// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



]

  *[Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

