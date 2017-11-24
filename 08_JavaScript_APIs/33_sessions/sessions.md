[



Use the sessions API to list, and restore, tabs and windows that have been
closed while the browser has been running.



The [`sessions.getRecentlyClosed()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/getRecentlyClosed "Returns an array of Session
objects, representing windows and tabs that were closed in the current
browsing session \(that is: the time since the browser was started\).")
function returns an array of\xa0[`tabs.Tab`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/Tab "The type tabs.Tab contains information about a
tab. This provides access to information about what content is in the tab, how
large the content is, what special states or restrictions are in effect, and
so forth.") and [`windows.Window`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/windows/Window "Information about a browser window.")
objects, representing tabs and windows that have been closed since the browser
was running, up to the maximum defined in [`sessions.MAX_SESSION_RESULTS
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions/MAX_SESSION_RESULTS
"This value represents the maximum number of sessions that will be returned by
a call to sessions.getRecentlyClosed\(\). It is read-only for WebExtension
code, and is set to 25.").



You can then restore a window or tab using the [`sessions.restore()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/sessions/restore "Restores a closed
tab or window. Restoring doesn't just reopen the tab or window: it also
restores the tab's navigation history so the back/forward buttons will work.
Restoring a window will restore all the tabs that the window contained when it
was closed.") function. Restoring doesn't just reopen the tab: it also
restores the tab's navigation history so the back/forward buttons will work.



This API also provides a group of functions that enable an extension to store
additional state associated with a tab or a window. Then, if the tab or window
is closed and subsequently restored, the extension can retrieve the state. For
example, a tab grouping extension might use this to remember which group a tab
is in, so as to restore it into the right group if the user restores the tab.



To use the sessions API you must have the "sessions" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).



## Types



[`sessions.Filter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/Filter "The Filter object enables you to
restrict the number of Session objects returned by a call to
sessions.getRecentlyClosed\(\).")

    Enables you to restrict the number of [`Session`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/sessions/Session "The Session object represents a
tab or window that the user has closed in the current browsing session.")
objects returned by a call to [`sessions.getRecentlyClosed()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/sessions/getRecentlyClosed "Returns
an array of Session objects, representing windows and tabs that were closed in
the current browsing session \(that is: the time since the browser was
started\).").

[`sessions.Session`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/Session "The Session object represents a tab or
window that the user has closed in the current browsing session.")

    

Represents a tab or window that the user has closed in the current browsing
session.





## Properties



[`sessions.MAX_SESSION_RESULTS`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/MAX_SESSION_RESULTS "This value represents the
maximum number of sessions that will be returned by a call to
sessions.getRecentlyClosed\(\). It is read-only for WebExtension code, and is
set to 25.")

    The maximum number of sessions that will be returned by a call to
[`sessions.getRecentlyClosed()`](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/sessions/getRecentlyClosed "Returns
an array Session objects, representing windows and tabs that were closed in
the current browsing session \(that is: the time since the browser was
started\).").



## Functions



[`sessions.forgetClosedTab()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/forgetClosedTab "This is an asynchronous
function that returns a Promise.")

    Removes a closed tab from the browser's list of recently closed tabs.

[`sessions.forgetClosedWindow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/forgetClosedWindow "This is an asynchronous
function that returns a Promise.")

    Removes a closed window from the browser's list of recently closed
windows.

[`sessions.getRecentlyClosed()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/getRecentlyClosed "Returns an array of Session
objects, representing windows and tabs that were closed in the current
browsing session \(that is: the time since the browser was started\).")

    Returns an array of [`Session`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/Session "The Session object represents a tab or
window that the user has closed in the current browsing session.") objects,
representing windows and tabs that were closed in the current browsing session
(that is: the time since the browser was started).

[`sessions.restore()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/restore "Restores a closed tab or window.
Restoring doesn't just reopen the tab or window: it also restores the tab's
navigation history so the back/forward buttons will work. Restoring a window
will restore all the tabs that the window contained when it was closed.")

    

Restores a closed tab or window.



[`sessions.setTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/setTabValue "Stores a key/value pair to
associate with a given tab. You can subsequently retrieve this value using
sessions.getTabValue.")

    

Store a key/value pair associated with a given tab.



[`sessions.getTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/getTabValue "Retrieves a value previously
stored by a call to sessions.setTabValue.")

    

Retrieve a previously stored value for a given tab, given its key.



[`sessions.removeTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/removeTabValue "Removes a value previously
stored by a call to sessions.setTabValue.")

    

Remove a key/value pair from a given tab.



[`sessions.setWindowValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/setWindowValue "Stores a key/value pair to
associate with a given window. You can subsequently retrieve this value using
sessions.getWindowValue.")

    

Store a key/value pair associated with a given window.



[`sessions.getWindowValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/getWindowValue "Retrieves a value previously
stored by a call to sessions.setWindowValue.")

    

Retrieve a previously stored value for a given window, given its key.



[`sessions.removeWindowValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/removeWindowValue "Removes a value previously
stored by a call to sessions.setWindowValue.")

    

Remove a key/value pair from a given window.





## Events



[`sessions.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/onChanged "Fired whenever the list of closed
tabs or windows changes.")

    

Fired when a tab or window is closed.





## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Filter`|  Yes|  No| 52|  No|  Yes  
`MAX_SESSION_RESULTS`|  Yes|  No| 52|  No|  Yes  
`Session`|  Yes|  No| 52 *|  No|  Yes  
`forgetClosedTab`|  No|  No| 55|  No|  No  
`forgetClosedWindow`|  No|  No| 55|  No|  No  
`getRecentlyClosed`|  Yes|  No| 52|  No|  Yes  
`getTabValue`|  No|  No| 57|  No|  No  
`getWindowValue`|  No|  No| 57|  No|  No  
`onChanged`|  Yes|  No| 53|  No|  Yes  
`removeTabValue`|  No|  No| 57|  No|  No  
`removeWindowValue`|  No|  No| 57|  No|  No  
`restore`|  Yes|  No| 52|  No|  Yes  
`setTabValue`|  No|  No| 57|  No|  No  
`setWindowValue`|  No|  No| 57|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Filter`|  Full support Yes| No support No| Full support 52|
Full support Yes| No support No  
`MAX_SESSION_RESULTS`| Full support Yes| No support No| Full
support 52| Full support Yes| No support No  
`Session`| Full support Yes| No support No| Full support 52

Notes __

Full support 52

Notes __

     Notes __'Tab' objects in Sessions don't contain the 'url', 'title', or 'favIconUrl' properties.
|  Full support Yes| No support No  
`forgetClosedTab`| No support No| No support No| Full
support 55| No support No| No support No  
`forgetClosedWindow`| No support No| No support No| Full
support 55| No support No| No support No  
`getRecentlyClosed`| Full support Yes| No support No| Full
support 52| Full support Yes| No support No  
`getTabValue`| No support No| No support No| Full support
57| No support No| No support No  
`getWindowValue`| No support No| No support No| Full support
57| No support No| No support No  
`onChanged`| Full support Yes| No support No| Full support
53| Full support Yes| No support No  
`removeTabValue`| No support No| No support No| Full support
57| No support No| No support No  
`removeWindowValue`| No support No| No support No| Full
support 57| No support No| No support No  
`restore`| Full support Yes| No support No| Full support 52|
Full support Yes| No support No  
`setTabValue`| No support No| No support No| Full support
57| No support No| No support No  
`setWindowValue`| No support No| No support No| Full support
57| No support No| No support No  
  


## Example extensions

  * [session-state](https://github.com/mdn/webextensions-examples/tree/master/session-state)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.sessions`](https://developer.chrome.com/extensions/sessions) API.



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
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

