[\n

\n

Interact with browser windows. You can use this API to get information about
open windows and to open, modify, and close windows. You can also listen for
window open, close, and activate events.

\n

## Types

\n

\n[`windows.WindowType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WindowType "The documentation about this has not
yet been written; please consider contributing!")

\n    The type of browser window this is.

\n[`windows.WindowState`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WindowState "The state of this browser window.")

\n    The state of this browser window.

\n[`windows.Window`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/Window "Information about a browser window.")

\n    Contains information about a browser window.

\n[`windows.CreateType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/CreateType "Specifies the type of browser window
to create.")

\n    Specifies the type of browser window to create.

\n\n

## Properties

\n

\n[`windows.WINDOW_ID_NONE`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WINDOW_ID_NONE "The windowId value that
represents the absence of a browser window.")

\n    The `windowId` value that represents the absence of a browser window.

\n[`windows.WINDOW_ID_CURRENT`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WINDOW_ID_CURRENT "The windowId value for the
current window.")

\n    The `windowId` value that represents the current window.

\n\n

## Functions

\n

\n[`windows.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/get
"Gets details about a window, given its ID. The details are passed into a
callback.")

\n    Gets details about a window, given its ID.

\n[`windows.getCurrent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/getCurrent "Gets the current browser window,
passing its details into a callback.")

\n    Gets the current window.

\n[`windows.getLastFocused()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/getLastFocused "Gets the window that was most
recently focused \\u2014 typically the window 'on top'.")

\n    Gets the window that was most recently focused \u2014 typically the
window 'on top'.

\n[`windows.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/getAll "Gets information about all open windows,
passing them into a callback.")

\n    Gets all windows.

\n[`windows.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/create "The documentation about this has not yet
been written; please consider contributing!")

\n    \n

Creates a new window.

\n

\n[`windows.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/update "Updates the properties of a window. Use
this to move, resize, and \(un\)focus a window, etc.")

\n    Updates the properties of a window. Use this to move, resize, and
(un)focus a window, etc.

\n[`windows.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/remove "Closes a window and all the tabs inside
it, given the window's ID.")

\n    Closes a window, and all its tabs.

\n\n

## Events

\n

\n[`windows.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/onCreated "Fired when a window is created.")

\n    Fired when a window is created.

\n[`windows.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/onRemoved "Fired when a window is closed.")

\n    Fired when a window is closed.

\n[`windows.onFocusChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/onFocusChanged "Fired when the currently focused
window changes. Will be windows.WINDOW_ID_NONE if all browser windows have
lost focus.")

\n    Fired when the currently focused window changes.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`CreateType`| \n Yes *| \n Yes *| 45| \n No| \n Yes *  
`WINDOW_ID_CURRENT`| 18| \n Yes| 45| \n No| 15  
`WINDOW_ID_NONE`| \n Yes| \n Yes| 45| \n No| \n Yes  
`Window`| \n Yes *| \n Yes *| 45 *| \n No| \n Yes *  
`WindowState`| \n Yes| \n Yes *| 45 *| \n No| \n Yes  
`WindowType`| \n Yes| \n Yes *| 45| \n No| \n Yes  
`create`| \n Yes| \n Yes| 45 *| \n No| \n Yes  
`get`| \n Yes *| \n Yes| 45| \n No| \n Yes *  
`getAll`| \n Yes *| \n Yes *| 45| \n No| \n Yes *  
`getCurrent`| \n Yes *| \n Yes| 45| \n No| \n Yes *  
`getLastFocused`| \n Yes *| \n Yes| 45| \n No| \n Yes *  
`onCreated`| \n Yes| \n Yes| 45| \n No| \n Yes  
`onFocusChanged`| \n Yes| \n Yes| 45| \n No| \n Yes  
`onRemoved`| \n Yes| \n No| 45| \n No| \n Yes  
`remove`| \n Yes| \n No| 45| \n No| \n Yes  
`update`| \n Yes *| \n Yes *| 45 *| \n No| \n Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`CreateType`|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __`detached_panel` is not supported.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __`panel` and `detached_panel` are not supported.
|  \nFull support\n\n 45| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __`detached_panel` is not supported.
|  \nNo support\n\n No  
`WINDOW_ID_CURRENT`| \nFull support\n\n 18| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n 15| \nNo support\n\n No  
`WINDOW_ID_NONE`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`Window`| \nPartial support\nPartial| \nPartial support\nPartial| \nPartial
support\n45| \nPartial support\nPartial| \nNo support\n\n No  
`WindowState`| \nFull support\n\n Yes| \nPartial support\nPartial| \nPartial
support\n45| \nFull support\n\n Yes| \nNo support\n\n No  
`WindowType`| \nFull support\n\n Yes| \nPartial support\nPartial| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`create`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45

Notes __

\nFull support\n\n 45

Notes __

     Notes __'url' and 'tabId options can't both be set together.
     Notes __The returned 'Window' object contains the 'tabs' property only from version 52 onwards.
|  \nFull support\n\n Yes| \nNo support\n\n No  
`get`| \nPartial support\nPartial| \nFull support\n\n Yes| \nFull support\n\n
45| \nPartial support\nPartial| \nNo support\n\n No  
`getAll`| \nPartial support\nPartial| \nPartial support\nPartial| \nFull
support\n\n 45| \nPartial support\nPartial| \nNo support\n\n No  
`getCurrent`| \nPartial support\nPartial| \nFull support\n\n Yes| \nFull
support\n\n 45| \nPartial support\nPartial| \nNo support\n\n No  
`getLastFocused`| \nPartial support\nPartial| \nFull support\n\n Yes| \nFull
support\n\n 45| \nPartial support\nPartial| \nNo support\n\n No  
`onCreated`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`onFocusChanged`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`onRemoved`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`remove`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nNo support\n\n No  
`update`| \nPartial support\nPartial| \nPartial support\nPartial| \nPartial
support\n45| \nPartial support\nPartial| \nNo support\n\n No  
  
\n

## Example extensions

  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page)
  * [bookmark-it](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)
  * [store-collected-images](https://github.com/mdn/webextensions-examples/tree/master/store-collected-images)
  * [window-manipulator](https://github.com/mdn/webextensions-examples/tree/master/window-manipulator)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.windows`](https://developer.chrome.com/extensions/windows) API. This
documentation is derived from
[`windows.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/windows.json)
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
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

