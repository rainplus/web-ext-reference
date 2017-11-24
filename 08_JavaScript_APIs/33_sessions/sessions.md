[\n

\n

Use the sessions API to list, and restore, tabs and windows that have been
closed while the browser has been running.

\n

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

\n

You can then restore a window or tab using the [`sessions.restore()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/sessions/restore "Restores a closed
tab or window. Restoring doesn't just reopen the tab or window: it also
restores the tab's navigation history so the back/forward buttons will work.
Restoring a window will restore all the tabs that the window contained when it
was closed.") function. Restoring doesn't just reopen the tab: it also
restores the tab's navigation history so the back/forward buttons will work.

\n

This API also provides a group of functions that enable an extension to store
additional state associated with a tab or a window. Then, if the tab or window
is closed and subsequently restored, the extension can retrieve the state. For
example, a tab grouping extension might use this to remember which group a tab
is in, so as to restore it into the right group if the user restores the tab.

\n

To use the sessions API you must have the "sessions" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).

\n

## Types

\n

\n[`sessions.Filter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/Filter "The Filter object enables you to
restrict the number of Session objects returned by a call to
sessions.getRecentlyClosed\(\).")

\n    Enables you to restrict the number of [`Session`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/sessions/Session "The Session object represents a
tab or window that the user has closed in the current browsing session.")
objects returned by a call to [`sessions.getRecentlyClosed()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/sessions/getRecentlyClosed "Returns
an array of Session objects, representing windows and tabs that were closed in
the current browsing session \(that is: the time since the browser was
started\).").

\n[`sessions.Session`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/Session "The Session object represents a tab or
window that the user has closed in the current browsing session.")

\n    \n

Represents a tab or window that the user has closed in the current browsing
session.

\n

\n\n

## Properties

\n

\n[`sessions.MAX_SESSION_RESULTS`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/MAX_SESSION_RESULTS "This value represents the
maximum number of sessions that will be returned by a call to
sessions.getRecentlyClosed\(\). It is read-only for WebExtension code, and is
set to 25.")

\n    The maximum number of sessions that will be returned by a call to
[`sessions.getRecentlyClosed()`](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/sessions/getRecentlyClosed "Returns
an array Session objects, representing windows and tabs that were closed in
the current browsing session \(that is: the time since the browser was
started\).").

\n\n

## Functions

\n

\n[`sessions.forgetClosedTab()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/forgetClosedTab "This is an asynchronous
function that returns a Promise.")

\n    Removes a closed tab from the browser's list of recently closed tabs.

\n[`sessions.forgetClosedWindow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/forgetClosedWindow "This is an asynchronous
function that returns a Promise.")

\n    Removes a closed window from the browser's list of recently closed
windows.

\n[`sessions.getRecentlyClosed()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/getRecentlyClosed "Returns an array of Session
objects, representing windows and tabs that were closed in the current
browsing session \(that is: the time since the browser was started\).")

\n    Returns an array of [`Session`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/Session "The Session object represents a tab or
window that the user has closed in the current browsing session.") objects,
representing windows and tabs that were closed in the current browsing session
(that is: the time since the browser was started).

\n[`sessions.restore()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/restore "Restores a closed tab or window.
Restoring doesn't just reopen the tab or window: it also restores the tab's
navigation history so the back/forward buttons will work. Restoring a window
will restore all the tabs that the window contained when it was closed.")

\n    \n

Restores a closed tab or window.

\n

\n[`sessions.setTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/setTabValue "Stores a key/value pair to
associate with a given tab. You can subsequently retrieve this value using
sessions.getTabValue.")

\n    \n

Store a key/value pair associated with a given tab.

\n

\n[`sessions.getTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/getTabValue "Retrieves a value previously
stored by a call to sessions.setTabValue.")

\n    \n

Retrieve a previously stored value for a given tab, given its key.

\n

\n[`sessions.removeTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/removeTabValue "Removes a value previously
stored by a call to sessions.setTabValue.")

\n    \n

Remove a key/value pair from a given tab.

\n

\n[`sessions.setWindowValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/setWindowValue "Stores a key/value pair to
associate with a given window. You can subsequently retrieve this value using
sessions.getWindowValue.")

\n    \n

Store a key/value pair associated with a given window.

\n

\n[`sessions.getWindowValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/getWindowValue "Retrieves a value previously
stored by a call to sessions.setWindowValue.")

\n    \n

Retrieve a previously stored value for a given window, given its key.

\n

\n[`sessions.removeWindowValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/removeWindowValue "Removes a value previously
stored by a call to sessions.setWindowValue.")

\n    \n

Remove a key/value pair from a given window.

\n

\n\n

## Events

\n

\n[`sessions.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/onChanged "Fired whenever the list of closed
tabs or windows changes.")

\n    \n

Fired when a tab or window is closed.

\n

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Filter`| \n Yes| \n No| 52| \n No| \n Yes  
`MAX_SESSION_RESULTS`| \n Yes| \n No| 52| \n No| \n Yes  
`Session`| \n Yes| \n No| 52 *| \n No| \n Yes  
`forgetClosedTab`| \n No| \n No| 55| \n No| \n No  
`forgetClosedWindow`| \n No| \n No| 55| \n No| \n No  
`getRecentlyClosed`| \n Yes| \n No| 52| \n No| \n Yes  
`getTabValue`| \n No| \n No| 57| \n No| \n No  
`getWindowValue`| \n No| \n No| 57| \n No| \n No  
`onChanged`| \n Yes| \n No| 53| \n No| \n Yes  
`removeTabValue`| \n No| \n No| 57| \n No| \n No  
`removeWindowValue`| \n No| \n No| 57| \n No| \n No  
`restore`| \n Yes| \n No| 52| \n No| \n Yes  
`setTabValue`| \n No| \n No| 57| \n No| \n No  
`setWindowValue`| \n No| \n No| 57| \n No| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Filter`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 52|
\nFull support\n\n Yes| \nNo support\n\n No  
`MAX_SESSION_RESULTS`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`Session`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 52

Notes __

\nFull support\n\n 52

Notes __

     Notes __'Tab' objects in Sessions don't contain the 'url', 'title', or 'favIconUrl' properties.
|  \nFull support\n\n Yes| \nNo support\n\n No  
`forgetClosedTab`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`forgetClosedWindow`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`getRecentlyClosed`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`getTabValue`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
57| \nNo support\n\n No| \nNo support\n\n No  
`getWindowValue`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
57| \nNo support\n\n No| \nNo support\n\n No  
`onChanged`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
53| \nFull support\n\n Yes| \nNo support\n\n No  
`removeTabValue`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
57| \nNo support\n\n No| \nNo support\n\n No  
`removeWindowValue`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
`restore`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 52|
\nFull support\n\n Yes| \nNo support\n\n No  
`setTabValue`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
57| \nNo support\n\n No| \nNo support\n\n No  
`setWindowValue`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
57| \nNo support\n\n No| \nNo support\n\n No  
  
\n

## Example extensions

  * [session-state](https://github.com/mdn/webextensions-examples/tree/master/session-state)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.sessions`](https://developer.chrome.com/extensions/sessions) API.

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
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

