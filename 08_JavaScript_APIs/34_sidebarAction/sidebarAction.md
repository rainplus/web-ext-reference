[\n

\n

Gets and sets properties of an extension's sidebar.

\n

A [sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars) is a pane that
is displayed at the left-hand or right-hand side of the browser window, next
to the web page. The browser provides a UI that enables the user to see the
currently available sidebars and to select a sidebar to display. Using the
`[sidebar_action](/en-US/Add-ons/WebExtensions/manifest.json/sidebar_action)`
manifest.json key, an extension can define its own sidebar. Using the
`sidebarAction` API described here, an extension can get and set the sidebar's
properties.

\n

The `sidebarAction` API is closely modeled on the [`browserAction`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction "Adds a button to the
browser's toolbar.") API.

\n

The sidebarAction API is based on Opera's [sidebarAction
API](https://dev.opera.com/extensions/sidebar-action-api/). However, note that
the following are not yet supported: `setBadgeText()`, `getBadgeText()`,
`setBadgeBackgroundColor()`, `getBadgeBackgroundColor()`, `onFocus`, `onBlur`.

\n

## Types

\n

\n[`sidebarAction.ImageDataType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/ImageDataType "Pixel data for an image.
Must be an ImageData object \(for example, from a <canvas> element\).")

\n    Pixel data for an image. Must be an `[ImageData](/en-
US/docs/Web/API/ImageData)` object (for example, from a [`<canvas>`](/en-
US/docs/Web/HTML/Element/canvas "Use the HTML <canvas> element with the canvas
scripting API to draw graphics and animations.") element).

\n\n

## Functions

\n

\n[`sidebarAction.setPanel()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/setPanel "Sets the HTML document that
defines the content of this sidebar.")

\n    Sets the sidebar's panel.

\n[`sidebarAction.getPanel()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/getPanel "Gets a URL to the HTML document
that defines the sidebar's contents.")

\n    Gets the sidebar's panel.

\n[`sidebarAction.setTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/setTitle "Sets the sidebar's title. The
title is displayed anywhere the browser lists available sidebars. For example,
Firefox will show it in the "View > Sidebar" menu. It's also shown at the top
o the sidebar when the sidebar is open.")

\n    Sets the sidebar's title. This will be displayed in any UI provided by
the browser to list sidebars, such as a menu.

\n[`sidebarAction.getTitle()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/getTitle "Gets the sidebar's title.")

\n    Gets the sidebar's title.

\n[`sidebarAction.setIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/setIcon "Sets the icon for the sidebar.")

\n    Sets the sidebar's icon.

\n[`sidebarAction.open()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/open "None.")

\n    Opens the sidebar.

\n[`sidebarAction.close()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction/close "Closes the sidebar in the active
window, if it is the extension's own sidebar.")

\n    Closes the sidebar.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ImageDataType`| \n No| \n No| 54| \n No| \n Yes  
`close`| \n No| \n No| 57| \n No| \n No  
`getPanel`| \n No| \n No| 54| \n No| \n Yes  
`getTitle`| \n No| \n No| 54| \n No| \n Yes  
`open`| \n No| \n No| 57| \n No| \n No  
`setIcon`| \n No| \n No| 54| \n No| \n Yes  
`setPanel`| \n No| \n No| 54| \n No| \n Yes  
`setTitle`| \n No| \n No| 54| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ImageDataType`|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
54| \nFull support\n\n Yes| \nNo support\n\n No  
`close`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 57| \nNo
support\n\n No| \nNo support\n\n No  
`getPanel`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 54|
\nFull support\n\n Yes| \nNo support\n\n No  
`getTitle`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 54|
\nFull support\n\n Yes| \nNo support\n\n No  
`open`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 57| \nNo
support\n\n No| \nNo support\n\n No  
`setIcon`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 54|
\nFull support\n\n Yes| \nNo support\n\n No  
`setPanel`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 54|
\nFull support\n\n Yes| \nNo support\n\n No  
`setTitle`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 54|
\nFull support\n\n Yes| \nNo support\n\n No  
  
\n

## Example add-ons

\n

\n

  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page)
\n

\n

 **Acknowledgements** \n

This API is based on Opera's
[`chrome.sidebarAction`](https://dev.opera.com/extensions/sidebar-action-api/)
API.

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
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

