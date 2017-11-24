[



Interact with browser windows. You can use this API to get information about
open windows and to open, modify, and close windows. You can also listen for
window open, close, and activate events.



## Types



[`windows.WindowType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WindowType "The documentation about this has not
yet been written; please consider contributing!")

    The type of browser window this is.

[`windows.WindowState`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WindowState "The state of this browser window.")

    The state of this browser window.

[`windows.Window`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/Window "Information about a browser window.")

    Contains information about a browser window.

[`windows.CreateType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/CreateType "Specifies the type of browser window
to create.")

    Specifies the type of browser window to create.



## Properties



[`windows.WINDOW_ID_NONE`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WINDOW_ID_NONE "The windowId value that
represents the absence of a browser window.")

    The `windowId` value that represents the absence of a browser window.

[`windows.WINDOW_ID_CURRENT`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/WINDOW_ID_CURRENT "The windowId value for the
current window.")

    The `windowId` value that represents the current window.



## Functions



[`windows.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/get
"Gets details about a window, given its ID. The details are passed into a
callback.")

    Gets details about a window, given its ID.

[`windows.getCurrent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/getCurrent "Gets the current browser window,
passing its details into a callback.")

    Gets the current window.

[`windows.getLastFocused()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/getLastFocused "Gets the window that was most
recently focused \\u2014 typically the window 'on top'.")

    Gets the window that was most recently focused \u2014 typically the
window 'on top'.

[`windows.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/getAll "Gets information about all open windows,
passing them into a callback.")

    Gets all windows.

[`windows.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/create "The documentation about this has not yet
been written; please consider contributing!")

    

Creates a new window.



[`windows.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/update "Updates the properties of a window. Use
this to move, resize, and \(un\)focus a window, etc.")

    Updates the properties of a window. Use this to move, resize, and
(un)focus a window, etc.

[`windows.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/remove "Closes a window and all the tabs inside
it, given the window's ID.")

    Closes a window, and all its tabs.



## Events



[`windows.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/onCreated "Fired when a window is created.")

    Fired when a window is created.

[`windows.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/onRemoved "Fired when a window is closed.")

    Fired when a window is closed.

[`windows.onFocusChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/onFocusChanged "Fired when the currently focused
window changes. Will be windows.WINDOW_ID_NONE if all browser windows have
lost focus.")

    Fired when the currently focused window changes.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`CreateType`|  Yes *|  Yes *| 45|  No|  Yes *  
`WINDOW_ID_CURRENT`| 18|  Yes| 45|  No| 15  
`WINDOW_ID_NONE`|  Yes|  Yes| 45|  No|  Yes  
`Window`|  Yes *|  Yes *| 45 *|  No|  Yes *  
`WindowState`|  Yes|  Yes *| 45 *|  No|  Yes  
`WindowType`|  Yes|  Yes *| 45|  No|  Yes  
`create`|  Yes|  Yes| 45 *|  No|  Yes  
`get`|  Yes *|  Yes| 45|  No|  Yes *  
`getAll`|  Yes *|  Yes *| 45|  No|  Yes *  
`getCurrent`|  Yes *|  Yes| 45|  No|  Yes *  
`getLastFocused`|  Yes *|  Yes| 45|  No|  Yes *  
`onCreated`|  Yes|  Yes| 45|  No|  Yes  
`onFocusChanged`|  Yes|  Yes| 45|  No|  Yes  
`onRemoved`|  Yes|  No| 45|  No|  Yes  
`remove`|  Yes|  No| 45|  No|  Yes  
`update`|  Yes *|  Yes *| 45 *|  No|  Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`CreateType`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __`detached_panel` is not supported.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __`panel` and `detached_panel` are not supported.
|  Full support 45| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __`detached_panel` is not supported.
|  No support No  
`WINDOW_ID_CURRENT`| Full support 18| Full support Yes| Full
support 45| Full support 15| No support No  
`WINDOW_ID_NONE`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| No support No  
`Window`| Partial supportPartial| Partial supportPartial| Partial
support45| Partial supportPartial| No support No  
`WindowState`| Full support Yes| Partial supportPartial| Partial
support45| Full support Yes| No support No  
`WindowType`| Full support Yes| Partial supportPartial| Full
support 45| Full support Yes| No support No  
`create`| Full support Yes| Full support Yes| Full support
45

Notes __

Full support 45

Notes __

     Notes __'url' and 'tabId options can't both be set together.
     Notes __The returned 'Window' object contains the 'tabs' property only from version 52 onwards.
|  Full support Yes| No support No  
`get`| Partial supportPartial| Full support Yes| Full support
45| Partial supportPartial| No support No  
`getAll`| Partial supportPartial| Partial supportPartial| Full
support 45| Partial supportPartial| No support No  
`getCurrent`| Partial supportPartial| Full support Yes| Full
support 45| Partial supportPartial| No support No  
`getLastFocused`| Partial supportPartial| Full support Yes| Full
support 45| Partial supportPartial| No support No  
`onCreated`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| No support No  
`onFocusChanged`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| No support No  
`onRemoved`| Full support Yes| No support No| Full support
45| Full support Yes| No support No  
`remove`| Full support Yes| No support No| Full support 45|
Full support Yes| No support No  
`update`| Partial supportPartial| Partial supportPartial| Partial
support45| Partial supportPartial| No support No  
  


## Example extensions

  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page)
  * [bookmark-it](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)
  * [store-collected-images](https://github.com/mdn/webextensions-examples/tree/master/store-collected-images)
  * [window-manipulator](https://github.com/mdn/webextensions-examples/tree/master/window-manipulator)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.windows`](https://developer.chrome.com/extensions/windows) API. This
documentation is derived from
[`windows.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/windows.json)
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
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

