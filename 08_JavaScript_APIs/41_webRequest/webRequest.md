[\n

\n

Add event listeners for the various stages of making an HTTP request. The
event listener receives detailed information about the request, and can modify
or cancel the request.

\n

Each event is fired at a particular stage of the request. The typical sequence
of events is like this:

\n

![](https://mdn.mozillademos.org/files/13376/webRequest-flow.png)

\n

[`onErrorOccurred`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onErrorOccurred "Fired when a request could
not be processed due to an error: for example, a lack of Internet
connectivity.") can be fired at any time during the request. Also note that
sometimes the sequence of events may differ from this: for example, in
Firefox, on an [HSTS](/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)
upgrade, the `onBeforeRedirect` event will be triggered immediately after
`onBeforeRequest`.

\n

All the events, except `onErrorOccurred`, can take three arguments to
`addListener()`:

\n

\n

  * the listener itself
\n

  * a [`filter`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/RequestFilter "An object describing filters to apply to webRequest events.") object, so you can only be notified for requests made to particular URLs or for particular types of resource
\n

  * an optional `extraInfoSpec` object. You can use this to pass additional event-specific instructions.
\n

\n

The listener function is passed a `details` object containing information
about the request. This includes a request ID, which is provided to enable an
add-on to correlate events associated with a single request. It is unique
within a browser session and the add-on's context. It stays the same
throughout a request, even across redirections and authentication exchanges.

\n

To use the webRequest API for a given host, you must have the "webRequest"
[API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions) and the [host
permission ](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions)for that host. To
use the "blocking" feature you must also have the "webRequestBlocking" API
permission.

\n

## Modifying requests

\n

On some of these events,\xa0you can modify the request. Specifically, you can:

\n

\n

  * cancel the request in:\n \n
    * [`onBeforeRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when a request is about to be made, and before headers are available. This is a good place to listen if you want to cancel or redirect the request.")
\n

    * [`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered before sending any HTTP data, but after all HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.")
\n

    * [`onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.")
\n\n

\n

  * redirect the request in:\n \n
    * [`onBeforeRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when a request is about to be made, and before headers are available. This is a good place to listen if you want to cancel or redirect the request.")
\n

    * [`onHeadersReceived`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onHeadersReceived "Fired when the HTTP response headers associated with a request have been received. You can use this event to modify HTTP response headers.")
\n\n

\n

  * modify request headers in:\n \n
    * [`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered before sending any HTTP data, but after all HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.")
\n\n

\n

  * modify response headers in:\n \n
    * [`onHeadersReceived`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onHeadersReceived "Fired when the HTTP response headers associated with a request have been received. You can use this event to modify HTTP response headers.")
\n\n

\n

  * supply authentication credentials in:\n \n
    * [`onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.")
\n\n

\n

\n

To do this, you need to pass an option with the value "blocking" in the
`extraInfoSpec` argument to the event's `addListener()`. This makes the
listener synchronous. In the listener, you can then return a
[`BlockingResponse`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/BlockingResponse "An object of this type is
returned by event listeners that have set "blocking" in their extraInfoSpec
argument.") object, which indicates the modification you need to make: for
example, the modified request header you want to send.

\n

## Modifying responses

\n

To modify the HTTP response bodies for a request, call
[`webRequest.filterResponseData`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/filterResponseData "Use this function to
create a webRequest.StreamFilter object for a particular request. You can then
use the stream filter to monitor and modify the response. You'd typically call
this function from a webRequest event listener."), passing it the ID of the
request. This returns a [`webRequest.StreamFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/StreamFilter "A StreamFilter is an object you
can use to monitor and modify HTTP responses.") object that you can use to
examine and modify the data as it is received by the browser.

\n

To do this, you must have the "webRequestBlocking" API permission as well as
the "webRequest" [API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions) and the [host
permission ](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions)for the relevant
host.

\n

## Types

\n

\n[`webRequest.BlockingResponse`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/BlockingResponse "An object of this type is
returned by event listeners that have set "blocking" in their extraInfoSpec
argument.")

\n    \n

An object of this type is returned by event listeners that have set
`"blocking"` in their `extraInfoSpec` argument. By setting particular
properties in `BlockingResponse`, the listener can modify network requests.

\n

\n[`webRequest.HttpHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/HttpHeaders "An array of HTTP headers. Each
header is represented as an object with two properties: name and either value
or binaryValue.")

\n    An array of HTTP headers. Each header is represented as an object with
two properties: `name` and either `value` or `binaryValue`.

\n[`webRequest.RequestFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/RequestFilter "An object describing filters
to apply to webRequest events.")

\n    An object describing filters to apply to webRequest events.

\n[`webRequest.ResourceType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/ResourceType "This type is a string, which
represents the context in which a resource was fetched\\xa0in a web request.")

\n    Represents a particular kind of resource fetched in a web request.

\n[`webRequest.StreamFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/StreamFilter "A StreamFilter is an object you
can use to monitor and modify HTTP responses.")

\n    An object that can be used to monitor and modify HTTP responses while
they are being received.

\n[`webRequest.UploadData`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/UploadData "Contains data uploaded in a URL
request.")

\n    Contains data uploaded in a URL request.

\n\n

## Properties

\n

\n[`webRequest.MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES`](/en-
US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES
"The maximum number of times that handlerBehaviorChanged\(\) can be called in
a 10 minute period.")

\n    The maximum number of times that
`[`handlerBehaviorChanged()`](https://developer.mozilla.org/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/WebRequest/handlerBehaviorChanged "Suppose an add-
on's job is to block web requests against a pattern, and the following
scenario happens:")` can be called in a 10 minute period.

\n\n

## Functions

\n

\n[`webRequest.handlerBehaviorChanged()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/handlerBehaviorChanged "Suppose an
extension's job is to block web requests against a pattern, and the following
scenario happens:")

\n    This function can be used to ensure that event listeners are applied
correctly when pages are in the browser's in-memory cache.

\n[`webRequest.filterResponseData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/filterResponseData "Use this function to
create a webRequest.StreamFilter object for a particular request. You can then
use the stream filter to monitor and modify the response. You'd typically call
this function from a webRequest event listener.")

\n    Returns a [`webRequest.StreamFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/StreamFilter "A StreamFilter is an object you
can use to monitor and modify HTTP responses.") object for a given request.

\n\n

## Events

\n

\n[`webRequest.onBeforeRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when
a request is about to be made, and before headers are available. This is a
good place to listen if you want to cancel or redirect the request.")

\n    Fired when a request is about to be made, and before headers are
available. This is a good place to listen if you want to cancel or redirect
the request.

\n[`webRequest.onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered
before sending any HTTP data, but after all HTTP headers are available. This
is a good place to listen if you want to modify HTTP request headers.")

\n    Fired before sending any HTTP data, but after HTTP headers are
available. This is a good place to listen if you want to modify HTTP request
headers.

\n[`webRequest.onSendHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onSendHeaders "This event is fired just
before sending headers. If your extension or some other extension modified
headers in onBeforeSendHeaders, you'll see the modified version here.")

\n    Fired just before sending headers. If your add-on or some other add-on
modified headers in `[`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered
before sending any HTTP data, but after all HTTP headers are available. This
is a good place to listen if you want to modify HTTP request headers.")`,
you'll see the modified version here.

\n[`webRequest.onHeadersReceived`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onHeadersReceived "Fired when the HTTP
response headers associated with a request have been received. You can use
this event to modify HTTP response headers.")

\n    Fired when the HTTP response headers associated with a request have been
received. You can use this event to modify HTTP response headers.

\n[`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a
401 or 407 status code: that is, when the server is asking the client to
provide authentication credentials such as a username and password.")

\n    Fired when the server asks the client to provide authentication
credentials. The listener can do nothing, cancel the request, or supply
authentication credentials.

\n[`webRequest.onResponseStarted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onResponseStarted "Fired when the first byte
of the response body is received.")

\n    Fired when the first byte of the response body is received. For HTTP
requests, this means that the status line and response headers are available.

\n[`webRequest.onBeforeRedirect`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeRedirect "Fired when a server-
initiated redirect is about to occur.")

\n    Fired when a server-initiated redirect is about to occur.

\n[`webRequest.onCompleted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onCompleted "Fired when a request has
completed.")

\n    Fired when a request is completed.

\n[`webRequest.onErrorOccurred`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onErrorOccurred "Fired when a request could
not be processed due to an error: for example, a lack of Internet
connectivity.")

\n    Fired when an error occurs.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`BlockingResponse`| \n Yes| \n Yes| 45| 48| \n Yes  
`HttpHeaders`| \n Yes| \n Yes| 45| 48| \n Yes  
`MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES`| \n Yes| \n Yes| 45| 48|
\n Yes  
`RequestFilter`| \n Yes| \n Yes| 45 *| 48 *| \n Yes  
`ResourceType`| 44 *| \n No| 45 *| 48 *| 31 *  
`StreamFilter`| \n No| \n No| 57| 57| \n No  
`UploadData`| \n Yes| \n Yes| 45| 48| \n Yes  
`filterResponseData`| \n No| \n No| 57| 57| \n No  
`handlerBehaviorChanged`| \n Yes| \n Yes| 45| 48| \n Yes  
`onAuthRequired`| \n Yes| \n Yes| 54 *| 54 *| \n Yes  
`onBeforeRedirect`| \n Yes| \n Yes| 46| 48| \n Yes  
`onBeforeRequest`| \n Yes *| \n Yes *| 46 *| 48 *| \n Yes *  
`onBeforeSendHeaders`| \n Yes *| \n Yes *| 45 *| 48 *| \n Yes *  
`onCompleted`| \n Yes| \n Yes| 45| 48| \n Yes  
`onErrorOccurred`| \n Yes| \n Yes| 45| 48| \n Yes  
`onHeadersReceived`| \n Yes *| \n Yes *| 45 *| 48 *| \n Yes *  
`onResponseStarted`| \n Yes| \n Yes| 45| 48| \n Yes  
`onSendHeaders`| \n Yes| \n Yes| 45| 48| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`BlockingResponse`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`HttpHeaders`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES`| \nFull support\n\n Yes|
\nFull support\n\n Yes| \nFull support\n\n 45| \nFull support\n\n Yes| \nFull
support\n\n 48  
`RequestFilter`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nPartial
support\n45| \nFull support\n\n Yes| \nPartial support\n48  
`ResourceType`| \nPartial support\n44| \nNo support\n\n No| \nPartial
support\n45| \nPartial support\n31| \nPartial support\n48  
`StreamFilter`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
57| \nNo support\n\n No| \nFull support\n\n 57  
`UploadData`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`filterResponseData`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nFull support\n\n 57  
`handlerBehaviorChanged`| \nFull support\n\n Yes| \nFull support\n\n Yes|
\nFull support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`onAuthRequired`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nPartial
support\n54

Notes __

\nPartial support\n54

Notes __

     Notes __To handle a request asynchronously, return a Promise from the listener.
|  \nFull support\n\n Yes| \nPartial support\n54

Notes __

\nPartial support\n54

Notes __

     Notes __To handle a request asynchronously, return a Promise from the listener.  
`onBeforeRedirect`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 46| \nFull support\n\n Yes| \nFull support\n\n 48  
`onBeforeRequest`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n 46

Notes __

\nFull support\n\n 46

Notes __

     Notes __Asynchronous event listeners are supported from version 52.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Asynchronous event listeners are supported from version 52.  
`onBeforeSendHeaders`|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Asynchronous event listeners are supported from version 52.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Asynchronous event listeners are supported from version 52.  
`onCompleted`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`onErrorOccurred`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`onHeadersReceived`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Modification of the 'Content-Type' header is supported from version 51.
     Notes __Asynchronous event listeners are supported from version 52.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Modification of the 'Content-Type' header is supported from version 51.
     Notes __Asynchronous event listeners are supported from version 52.  
`onResponseStarted`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`onSendHeaders`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
  
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

### Chrome incompatibilities

#### [webRequest](/en-US/Add-ons/WebExtensions/API/webRequest)

\n

\n

  * In Firefox requests can be redirected only if their original URL uses the `http:`\xa0or `https:` scheme.
\n

  * In Firefox, events are not fired for system requests (for example, extension upgrades or searchbar suggestions). From Firefox 57 onwards, Firefox makes an exception for extensions that need to intercept [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.") for proxy authorization. See the documentation for [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.").
\n

## Example extensions

  * [http-response](https://github.com/mdn/webextensions-examples/tree/master/http-response)
  * [stored-credentials](https://github.com/mdn/webextensions-examples/tree/master/stored-credentials)
  * [user-agent-rewriter](https://github.com/mdn/webextensions-examples/tree/master/user-agent-rewriter)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.webRequest`](https://developer.chrome.com/extensions/webRequest) API.
This documentation is derived from
[`web_request.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/web_request.json)
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

