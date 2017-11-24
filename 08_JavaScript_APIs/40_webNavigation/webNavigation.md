[\n

\n

Add event listeners for the various stages of a navigation. A navigation
consists of a frame in the browser transitioning from one URL to another,
usually (but not always) in response to a user action like clicking a link or
entering a URL in the location bar.

\n

Compared with the [`webRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest "Add event listeners for the various stages
of making an HTTP request. The event listener receives detailed information
about the request, and can modify or cancel the request.") API: navigations
usually result in the browser making web requests, but the webRequest API is
concerned with the lower-level view from the HTTP layer, while the
webNavigation API is more concerned with the view from the browser UI itself.

\n

Each event corresponds to a particular stage in the navigation. The sequence
of events is like this:

\n

![](https://mdn.mozillademos.org/files/13374/we-flow.png)

\n

\n

  * The primary flow is:\n \n
    * `[`onBeforeNavigate`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onBeforeNavigate "Fired when the browser is about to start a navigation event.")`
\n

    * `[`onCommitted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onCommitted "Fired when a navigation is committed. At least part of the new document has been received from the server and the browser has decided to switch to the new document.")`
\n

    * `[`onDOMContentLoaded`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onDOMContentLoaded "Fired when the DOMContentLoaded event is fired in the page. At this point the document is loaded and parsed, and the DOM is fully constructed, but linked resources such as images, stylesheets and subframes may not yet be loaded.")`
\n

    * `[`onCompleted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onCompleted "Fired when a document, including the resources it refers to, is completely loaded and initialized. This is equivalent to the DOM load event.")`.
\n\n

\n

  * Additionally:\n \n
    * `[`onCreatedNavigationTarget`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onCreatedNavigationTarget "Fired when a new window, or a new tab in an existing window, is created to host the target of a navigation. For example, this event is sent when:")` is fired before `onBeforeNavigate` if the browser needed to create a new tab or window for the navigation (for example, because the user opened a link in a new tab).
\n

    * [`onHistoryStateUpdated`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onHistoryStateUpdated "Fired when the page used the history API to update the URL displayed in the browser's location bar. All future events for this frame will use the updated URL.") is fired if a page uses the [history API](http://diveintohtml5.info/history.html) to update the URL displayed in the browser's location bar.
\n

    * [`onReferenceFragmentUpdated`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onReferenceFragmentUpdated "Events have three functions:") is fired if the [fragment identifier](https://en.wikipedia.org/wiki/Fragment_identifier) for a page is changed.
\n

    * [`onErrorOccurred`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onErrorOccurred "Fired when an error occurs and the navigation is aborted. This can happen if either a network error occurred, or the user aborted the navigation.") can be fired at any point.
\n\n

\n

\n

Each navigation is a URL transition in a particular browser frame. The browser
frame is identified by a tab ID and a frame ID. The frame may be the top-level
browsing context in the tab, or may be a nested browsing context implemented
as an [iframe](/en-US/docs/Web/HTML/Element/iframe).

\n

Each event's `addListener()` call accepts an optional filter parameter. The
filter will specify one or more URL patterns, and the event will then only be
fired for navigations in which the target URL matches one of the patterns.

\n

The `onCommitted` event listener is passed two additional properties: a
[`TransitionType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/TransitionType "Cause of the navigation:
for example, the user clicked a link, or typed an address, or clicked a
bookmark.") indicating the cause of the navigation (for example, because the
user clicked a link, or because the user selected a bookmark), and a
[`TransitionQualifier`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/TransitionQualifier "Values of this type
are strings. Possible values are:") providing further information about the
navigation.

\n

To use this API you need to have the "webNavigation"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

\n

## Types

\n

\n[`webNavigation.TransitionType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/TransitionType "Cause of the navigation:
for example, the user clicked a link, or typed an address, or clicked a
bookmark.")

\n    Cause of the navigation: for example, the user clicked a link, or typed
an address, or clicked a bookmark.

\n[`webNavigation.TransitionQualifier`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/TransitionQualifier "Values of this type
are strings. Possible values are:")

\n    \n

Extra information about a transition.

\n

\n\n

## Functions

\n

\n[`webNavigation.getFrame()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/getFrame "Retrieves information about a
particular frame. A frame may be the top-level frame in a tab or a nested
iframe, and is uniquely identified by a tab ID and a frame ID.")

\n    Retrieves information about a particular frame. A frame may be the top-
level frame in a tab or a nested [iframe](https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/iframe), and is uniquely identified by a tab ID and a
frame ID.

\n[`webNavigation.getAllFrames()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/getAllFrames "Given a tab ID, retrieves
information about all the frames it contains.")

\n    \n

Given a tab ID, retrieves information about all the frames it contains.

\n

\n\n

## Events

\n

\n[`webNavigation.onBeforeNavigate`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onBeforeNavigate "Fired when the browser
is about to start a navigation event.")

\n    \n

Fired when the browser is about to start a navigation event.

\n

\n[`webNavigation.onCommitted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onCommitted "Fired when a navigation is
committed. At least part of the new document has been received from the server
and the browser has decided to switch to the new document.")

\n    Fired when a navigation is committed. At least part of the new document
has been received from the server and the browser has decided to switch to the
new document.

\n[`webNavigation.onDOMContentLoaded`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onDOMContentLoaded "Fired when the
DOMContentLoaded event is fired in the page. At this point the document is
loaded and parsed, and the DOM is fully constructed, but linked resources such
as images, stylesheets and subframes may not yet be loaded.")

\n    Fired when the [DOMContentLoaded](https://developer.mozilla.org/en-
US/docs/Web/Events/DOMContentLoaded) event is fired in the page.

\n[`webNavigation.onCompleted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onCompleted "Fired when a document,
including the resources it refers to, is completely loaded and initialized.
This is equivalent to the DOM load event.")

\n    Fired when a document, including the resources it refers to, is
completely loaded and initialized. This is equivalent to the DOM
`[load](https://developer.mozilla.org/en-US/docs/Web/Events/load)` event.

\n[`webNavigation.onErrorOccurred`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onErrorOccurred "Fired when an error
occurs and the navigation is aborted. This can happen if either a network
error occurred, or the user aborted the navigation.")

\n    Fired when an error occurs and the navigation is aborted. This can
happen if either a network error occurred, or the user aborted the navigation.

\n[`webNavigation.onCreatedNavigationTarget`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onCreatedNavigationTarget "Fired when a
new window, or a new tab in an existing window, is created to host the target
of a navigation. For example, this event is sent when:")

\n    Fired when a new window, or a new tab in an existing window, is created
to host a navigation: for example, if the user opens a link in a new tab.

\n[`webNavigation.onReferenceFragmentUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onReferenceFragmentUpdated "The
documentation about this has not yet been written; please consider
contributing!")

\n    Fired if the [fragment
identifier](https://en.wikipedia.org/wiki/Fragment_identifier) for a page is
changed.

\n[`webNavigation.onTabReplaced`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onTabReplaced "Fired when the contents of
the tab is replaced by a different \(usually previously pre-rendered\) tab.")

\n    \n

Fired when the contents of the tab is replaced by a different (usually
previously pre-rendered) tab.

\n

\n[`webNavigation.onHistoryStateUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onHistoryStateUpdated "Fired when the page
used the history API to update the URL displayed in the browser's location
bar. All future events for this frame will use the updated URL.")

\n    Fired when the page used the [history
API](http://diveintohtml5.info/history.html) to update the URL displayed in
the browser's location bar.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`TransitionQualifier`| \n Yes| \n No| 48 *| 48 *| 17  
`TransitionType`| \n Yes| \n No| 48 *| 48 *| 17  
`getAllFrames`| \n Yes| \n Yes| 47| 48| 17  
`getFrame`| \n Yes| \n Yes| 47| 48| 17  
`onBeforeNavigate`| \n Yes *| \n Yes *| 45 *| 48 *| 17 *  
`onCommitted`| \n Yes *| \n Yes *| 45 *| 48 *| 17 *  
`onCompleted`| \n Yes *| \n Yes *| 45 *| 48 *| 17 *  
`onCreatedNavigationTarget`| \n Yes *| \n Yes| 54 *| 54 *| 17 *  
`onDOMContentLoaded`| \n Yes *| \n Yes *| 45 *| 48 *| 17 *  
`onErrorOccurred`| \n Yes *| \n Yes *| 45 *| 48 *| 17 *  
`onHistoryStateUpdated`| \n Yes| \n Yes *| 47 *| 48| 17  
`onReferenceFragmentUpdated`| \n Yes *| \n Yes *| 45 *| 48 *| 17 *  
`onTabReplaced`| \n Yes| \n Yes| 45 *| 48 *| 17  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`TransitionQualifier`|  \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n48

Notes __

\nPartial support\n48

Notes __

     Notes __'server_redirect' is limited to top-level frames and 'client_redirect' is not supplied when redirections are created by JavaScript.
|  \nFull support\n\n 17| \nPartial support\n48

Notes __

\nPartial support\n48

Notes __

     Notes __'server_redirect' is limited to top-level frames and 'client_redirect' is not supplied when redirections are created by JavaScript.  
`TransitionType`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __'link' and 'auto_subframe' are partially supported as the default transition type for top-level frames and subframes respectively. 'reload' and 'form_submit' are supported. All other properties are unsupported.
|  \nFull support\n\n 17| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __'link' and 'auto_subframe' are partially supported as the default transition type for top-level frames and subframes respectively. 'reload' and 'form_submit' are supported. All other properties are unsupported.  
`getAllFrames`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 47| \nFull support\n\n 17| \nFull support\n\n 48  
`getFrame`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
47| \nFull support\n\n 17| \nFull support\n\n 48  
`onBeforeNavigate`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Filtering is not supported.
|  \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  \nFull support\n\n 17

Notes __

\nFull support\n\n 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onCommitted`|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __Filtering is not supported.
|  \nPartial support\n45

Notes __

\nPartial support\n45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  \nFull support\n\n 17

Notes __

\nFull support\n\n 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onCompleted`|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Filtering is not supported.
|  \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  \nFull support\n\n 17

Notes __

\nFull support\n\n 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onCreatedNavigationTarget`|  \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __If a blocked popup is unblocked by the user, the event is still not sent.
|  \nFull support\n\n Yes| \nPartial support\n54

Notes __

\nPartial support\n54

Notes __

     Notes __If the filter parameter is empty, Firefox raises an exception.
     Notes __If a blocked popup is unblocked by the user, the event is then sent.
|  \nFull support\n\n 17

Notes __

\nFull support\n\n 17

Notes __

     Notes __If a blocked popup is unblocked by the user, the event is still not sent.
|  \nPartial support\n54

Notes __

\nPartial support\n54

Notes __

     Notes __If the filter parameter is empty, Firefox raises an exception.
     Notes __If a blocked popup is unblocked by the user, the event is then sent.
     Notes __This event is only sent in the 'window.open()' case.  
`onDOMContentLoaded`|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Filtering is not supported.
|  \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  \nFull support\n\n 17

Notes __

\nFull support\n\n 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onErrorOccurred`|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Filtering is not supported
|  \nPartial support\n45

Notes __

\nPartial support\n45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  \nFull support\n\n 17

Notes __

\nFull support\n\n 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  \nPartial support\n48

Notes __

\nPartial support\n48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onHistoryStateUpdated`|  \nFull support\n\n Yes| \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __Filtering is not supported.
|  \nPartial support\n47| \nFull support\n\n 17| \nFull support\n\n 48  
`onReferenceFragmentUpdated`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __Filtering is not supported.
|  \nPartial support\n45

Notes __

\nPartial support\n45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  \nFull support\n\n 17

Notes __

\nFull support\n\n 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onTabReplaced`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Although you can add listeners for this event, it will never fire because the underlying functionality is not supported.
|  \nFull support\n\n 17| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Although you can add listeners for this event, it will never fire because the underlying functionality is not supported.  
  
\n

## Example extensions

  * [navigation-stats](https://github.com/mdn/webextensions-examples/tree/master/navigation-stats)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.webNavigation`](https://developer.chrome.com/extensions/webNavigation)
API. This documentation is derived from
[`web_navigation.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/web_navigation.json)
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

