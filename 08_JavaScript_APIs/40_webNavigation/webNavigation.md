[



Add event listeners for the various stages of a navigation. A navigation
consists of a frame in the browser transitioning from one URL to another,
usually (but not always) in response to a user action like clicking a link or
entering a URL in the location bar.



Compared with the [`webRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest "Add event listeners for the various stages
of making an HTTP request. The event listener receives detailed information
about the request, and can modify or cancel the request.") API: navigations
usually result in the browser making web requests, but the webRequest API is
concerned with the lower-level view from the HTTP layer, while the
webNavigation API is more concerned with the view from the browser UI itself.



Each event corresponds to a particular stage in the navigation. The sequence
of events is like this:



![](https://mdn.mozillademos.org/files/13374/we-flow.png)





  * The primary flow is: 
    * `[`onBeforeNavigate`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onBeforeNavigate "Fired when the browser is about to start a navigation event.")`


    * `[`onCommitted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onCommitted "Fired when a navigation is committed. At least part of the new document has been received from the server and the browser has decided to switch to the new document.")`


    * `[`onDOMContentLoaded`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onDOMContentLoaded "Fired when the DOMContentLoaded event is fired in the page. At this point the document is loaded and parsed, and the DOM is fully constructed, but linked resources such as images, stylesheets and subframes may not yet be loaded.")`


    * `[`onCompleted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onCompleted "Fired when a document, including the resources it refers to, is completely loaded and initialized. This is equivalent to the DOM load event.")`.




  * Additionally: 
    * `[`onCreatedNavigationTarget`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onCreatedNavigationTarget "Fired when a new window, or a new tab in an existing window, is created to host the target of a navigation. For example, this event is sent when:")` is fired before `onBeforeNavigate` if the browser needed to create a new tab or window for the navigation (for example, because the user opened a link in a new tab).


    * [`onHistoryStateUpdated`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onHistoryStateUpdated "Fired when the page used the history API to update the URL displayed in the browser's location bar. All future events for this frame will use the updated URL.") is fired if a page uses the [history API](http://diveintohtml5.info/history.html) to update the URL displayed in the browser's location bar.


    * [`onReferenceFragmentUpdated`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onReferenceFragmentUpdated "Events have three functions:") is fired if the [fragment identifier](https://en.wikipedia.org/wiki/Fragment_identifier) for a page is changed.


    * [`onErrorOccurred`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation/onErrorOccurred "Fired when an error occurs and the navigation is aborted. This can happen if either a network error occurred, or the user aborted the navigation.") can be fired at any point.






Each navigation is a URL transition in a particular browser frame. The browser
frame is identified by a tab ID and a frame ID. The frame may be the top-level
browsing context in the tab, or may be a nested browsing context implemented
as an [iframe](/en-US/docs/Web/HTML/Element/iframe).



Each event's `addListener()` call accepts an optional filter parameter. The
filter will specify one or more URL patterns, and the event will then only be
fired for navigations in which the target URL matches one of the patterns.



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



To use this API you need to have the "webNavigation"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).



## Types



[`webNavigation.TransitionType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/TransitionType "Cause of the navigation:
for example, the user clicked a link, or typed an address, or clicked a
bookmark.")

    Cause of the navigation: for example, the user clicked a link, or typed
an address, or clicked a bookmark.

[`webNavigation.TransitionQualifier`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/TransitionQualifier "Values of this type
are strings. Possible values are:")

    

Extra information about a transition.





## Functions



[`webNavigation.getFrame()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/getFrame "Retrieves information about a
particular frame. A frame may be the top-level frame in a tab or a nested
iframe, and is uniquely identified by a tab ID and a frame ID.")

    Retrieves information about a particular frame. A frame may be the top-
level frame in a tab or a nested [iframe](https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/iframe), and is uniquely identified by a tab ID and a
frame ID.

[`webNavigation.getAllFrames()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/getAllFrames "Given a tab ID, retrieves
information about all the frames it contains.")

    

Given a tab ID, retrieves information about all the frames it contains.





## Events



[`webNavigation.onBeforeNavigate`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onBeforeNavigate "Fired when the browser
is about to start a navigation event.")

    

Fired when the browser is about to start a navigation event.



[`webNavigation.onCommitted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onCommitted "Fired when a navigation is
committed. At least part of the new document has been received from the server
and the browser has decided to switch to the new document.")

    Fired when a navigation is committed. At least part of the new document
has been received from the server and the browser has decided to switch to the
new document.

[`webNavigation.onDOMContentLoaded`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onDOMContentLoaded "Fired when the
DOMContentLoaded event is fired in the page. At this point the document is
loaded and parsed, and the DOM is fully constructed, but linked resources such
as images, stylesheets and subframes may not yet be loaded.")

    Fired when the [DOMContentLoaded](https://developer.mozilla.org/en-
US/docs/Web/Events/DOMContentLoaded) event is fired in the page.

[`webNavigation.onCompleted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onCompleted "Fired when a document,
including the resources it refers to, is completely loaded and initialized.
This is equivalent to the DOM load event.")

    Fired when a document, including the resources it refers to, is
completely loaded and initialized. This is equivalent to the DOM
`[load](https://developer.mozilla.org/en-US/docs/Web/Events/load)` event.

[`webNavigation.onErrorOccurred`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onErrorOccurred "Fired when an error
occurs and the navigation is aborted. This can happen if either a network
error occurred, or the user aborted the navigation.")

    Fired when an error occurs and the navigation is aborted. This can
happen if either a network error occurred, or the user aborted the navigation.

[`webNavigation.onCreatedNavigationTarget`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onCreatedNavigationTarget "Fired when a
new window, or a new tab in an existing window, is created to host the target
of a navigation. For example, this event is sent when:")

    Fired when a new window, or a new tab in an existing window, is created
to host a navigation: for example, if the user opens a link in a new tab.

[`webNavigation.onReferenceFragmentUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onReferenceFragmentUpdated "The
documentation about this has not yet been written; please consider
contributing!")

    Fired if the [fragment
identifier](https://en.wikipedia.org/wiki/Fragment_identifier) for a page is
changed.

[`webNavigation.onTabReplaced`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onTabReplaced "Fired when the contents of
the tab is replaced by a different \(usually previously pre-rendered\) tab.")

    

Fired when the contents of the tab is replaced by a different (usually
previously pre-rendered) tab.



[`webNavigation.onHistoryStateUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webNavigation/onHistoryStateUpdated "Fired when the page
used the history API to update the URL displayed in the browser's location
bar. All future events for this frame will use the updated URL.")

    Fired when the page used the [history
API](http://diveintohtml5.info/history.html) to update the URL displayed in
the browser's location bar.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`TransitionQualifier`|  Yes|  No| 48 *| 48 *| 17  
`TransitionType`|  Yes|  No| 48 *| 48 *| 17  
`getAllFrames`|  Yes|  Yes| 47| 48| 17  
`getFrame`|  Yes|  Yes| 47| 48| 17  
`onBeforeNavigate`|  Yes *|  Yes *| 45 *| 48 *| 17 *  
`onCommitted`|  Yes *|  Yes *| 45 *| 48 *| 17 *  
`onCompleted`|  Yes *|  Yes *| 45 *| 48 *| 17 *  
`onCreatedNavigationTarget`|  Yes *|  Yes| 54 *| 54 *| 17 *  
`onDOMContentLoaded`|  Yes *|  Yes *| 45 *| 48 *| 17 *  
`onErrorOccurred`|  Yes *|  Yes *| 45 *| 48 *| 17 *  
`onHistoryStateUpdated`|  Yes|  Yes *| 47 *| 48| 17  
`onReferenceFragmentUpdated`|  Yes *|  Yes *| 45 *| 48 *| 17 *  
`onTabReplaced`|  Yes|  Yes| 45 *| 48 *| 17  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`TransitionQualifier`|  Full support Yes| No support No| Partial
support48

Notes __

Partial support48

Notes __

     Notes __'server_redirect' is limited to top-level frames and 'client_redirect' is not supplied when redirections are created by JavaScript.
|  Full support 17| Partial support48

Notes __

Partial support48

Notes __

     Notes __'server_redirect' is limited to top-level frames and 'client_redirect' is not supplied when redirections are created by JavaScript.  
`TransitionType`|  Full support Yes| No support No| Full
support 48

Notes __

Full support 48

Notes __

     Notes __'link' and 'auto_subframe' are partially supported as the default transition type for top-level frames and subframes respectively. 'reload' and 'form_submit' are supported. All other properties are unsupported.
|  Full support 17| Full support 48

Notes __

Full support 48

Notes __

     Notes __'link' and 'auto_subframe' are partially supported as the default transition type for top-level frames and subframes respectively. 'reload' and 'form_submit' are supported. All other properties are unsupported.  
`getAllFrames`|  Full support Yes| Full support Yes| Full
support 47| Full support 17| Full support 48  
`getFrame`| Full support Yes| Full support Yes| Full support
47| Full support 17| Full support 48  
`onBeforeNavigate`| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Filtering is not supported.
|  Full support 45

Notes __

Full support 45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  Full support 17

Notes __

Full support 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onCommitted`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __Filtering is not supported.
|  Partial support45

Notes __

Partial support45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  Full support 17

Notes __

Full support 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onCompleted`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Filtering is not supported.
|  Full support 45

Notes __

Full support 45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  Full support 17

Notes __

Full support 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onCreatedNavigationTarget`|  Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __If a blocked popup is unblocked by the user, the event is still not sent.
|  Full support Yes| Partial support54

Notes __

Partial support54

Notes __

     Notes __If the filter parameter is empty, Firefox raises an exception.
     Notes __If a blocked popup is unblocked by the user, the event is then sent.
|  Full support 17

Notes __

Full support 17

Notes __

     Notes __If a blocked popup is unblocked by the user, the event is still not sent.
|  Partial support54

Notes __

Partial support54

Notes __

     Notes __If the filter parameter is empty, Firefox raises an exception.
     Notes __If a blocked popup is unblocked by the user, the event is then sent.
     Notes __This event is only sent in the 'window.open()' case.  
`onDOMContentLoaded`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Filtering is not supported.
|  Full support 45

Notes __

Full support 45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  Full support 17

Notes __

Full support 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onErrorOccurred`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Filtering is not supported
|  Partial support45

Notes __

Partial support45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  Full support 17

Notes __

Full support 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  Partial support48

Notes __

Partial support48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onHistoryStateUpdated`|  Full support Yes| Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __Filtering is not supported.
|  Partial support47| Full support 17| Full support 48  
`onReferenceFragmentUpdated`| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If the filter parameter is empty, Chrome matches all URLs.
|  Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __Filtering is not supported.
|  Partial support45

Notes __

Partial support45

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.
|  Full support 17

Notes __

Full support 17

Notes __

     Notes __If the filter parameter is empty, Opera matches all URLs.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Filtering is supported from version 50.
     Notes __If the filter parameter is empty, Firefox raises an exception.  
`onTabReplaced`|  Full support Yes| Full support Yes| Full
support 45

Notes __

Full support 45

Notes __

     Notes __Although you can add listeners for this event, it will never fire because the underlying functionality is not supported.
|  Full support 17| Full support 48

Notes __

Full support 48

Notes __

     Notes __Although you can add listeners for this event, it will never fire because the underlying functionality is not supported.  
  


## Example extensions

  * [navigation-stats](https://github.com/mdn/webextensions-examples/tree/master/navigation-stats)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.webNavigation`](https://developer.chrome.com/extensions/webNavigation)
API. This documentation is derived from
[`web_navigation.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/web_navigation.json)
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

