Add event listeners for the various stages of making an HTTP request. The
event listener receives detailed information about the request, and can modify
or cancel the request.

Each event is fired at a particular stage of the request. The typical sequence
of events is like this:

![](https://mdn.mozillademos.org/files/13376/webRequest-flow.png)

[`onErrorOccurred`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onErrorOccurred "Fired when a request could
not be processed due to an error: for example, a lack of Internet
connectivity.") can be fired at any time during the request. Also note that
sometimes the sequence of events may differ from this: for example, in
Firefox, on an [HSTS](/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)
upgrade, the `onBeforeRedirect` event will be triggered immediately after
`onBeforeRequest`.

All the events, except `onErrorOccurred`, can take three arguments to
`addListener()`:

  * the listener itself
  * a [`filter`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/RequestFilter "An object describing filters to apply to webRequest events.") object, so you can only be notified for requests made to particular URLs or for particular types of resource
  * an optional `extraInfoSpec` object. You can use this to pass additional event-specific instructions.

The listener function is passed a `details` object containing information
about the request. This includes a request ID, which is provided to enable an
add-on to correlate events associated with a single request. It is unique
within a browser session and the add-on's context. It stays the same
throughout a request, even across redirections and authentication exchanges.

To use the webRequest API for a given host, you must have the "webRequest"
[API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions) and the [host
permission ](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions)for that host. To
use the "blocking" feature you must also have the "webRequestBlocking" API
permission.

## Modifying requests

On some of these events, you can modify the request. Specifically, you can:

  * cancel the request in: 
    * [`onBeforeRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when a request is about to be made, and before headers are available. This is a good place to listen if you want to cancel or redirect the request.")
    * [`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered before sending any HTTP data, but after all HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.")
    * [`onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.")
  * redirect the request in: 
    * [`onBeforeRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when a request is about to be made, and before headers are available. This is a good place to listen if you want to cancel or redirect the request.")
    * [`onHeadersReceived`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onHeadersReceived "Fired when the HTTP response headers associated with a request have been received. You can use this event to modify HTTP response headers.")
  * modify request headers in: 
    * [`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered before sending any HTTP data, but after all HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.")
  * modify response headers in: 
    * [`onHeadersReceived`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onHeadersReceived "Fired when the HTTP response headers associated with a request have been received. You can use this event to modify HTTP response headers.")
  * supply authentication credentials in: 
    * [`onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.")

To do this, you need to pass an option with the value "blocking" in the
`extraInfoSpec` argument to the event's `addListener()`. This makes the
listener synchronous. In the listener, you can then return a
[`BlockingResponse`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/BlockingResponse "An object of this type is
returned by event listeners that have set "blocking" in their extraInfoSpec
argument.") object, which indicates the modification you need to make: for
example, the modified request header you want to send.

## Modifying responses

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

To do this, you must have the "webRequestBlocking" API permission as well as
the "webRequest" [API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions) and the [host
permission ](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions)for the relevant
host.

## Types

[`webRequest.BlockingResponse`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/BlockingResponse "An object of this type is
returned by event listeners that have set "blocking" in their extraInfoSpec
argument.")

    

An object of this type is returned by event listeners that have set
`"blocking"` in their `extraInfoSpec` argument. By setting particular
properties in `BlockingResponse`, the listener can modify network requests.

[`webRequest.HttpHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/HttpHeaders "An array of HTTP headers. Each
header is represented as an object with two properties: name and either value
or binaryValue.")

    An array of HTTP headers. Each header is represented as an object with two properties: `name` and either `value` or `binaryValue`.
[`webRequest.RequestFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/RequestFilter "An object describing filters
to apply to webRequest events.")

    An object describing filters to apply to webRequest events.
[`webRequest.ResourceType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/ResourceType "This type is a string, which
represents the context in which a resource was fetched in a web request.")

    Represents a particular kind of resource fetched in a web request.
[`webRequest.StreamFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/StreamFilter "A StreamFilter is an object you
can use to monitor and modify HTTP responses.")

    An object that can be used to monitor and modify HTTP responses while they are being received.
[`webRequest.UploadData`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/UploadData "Contains data uploaded in a URL
request.")

    Contains data uploaded in a URL request.

## Properties

[`webRequest.MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES`](/en-
US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES
"The maximum number of times that handlerBehaviorChanged\(\) can be called in
a 10 minute period.")

    The maximum number of times that `[`handlerBehaviorChanged()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/WebRequest/handlerBehaviorChanged "Suppose an add-on's job is to block web requests against a pattern, and the following scenario happens:")` can be called in a 10 minute period.

## Functions

[`webRequest.handlerBehaviorChanged()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/handlerBehaviorChanged "Suppose an
extension's job is to block web requests against a pattern, and the following
scenario happens:")

    This function can be used to ensure that event listeners are applied correctly when pages are in the browser's in-memory cache.
[`webRequest.filterResponseData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/filterResponseData "Use this function to
create a webRequest.StreamFilter object for a particular request. You can then
use the stream filter to monitor and modify the response. You'd typically call
this function from a webRequest event listener.")

    Returns a [`webRequest.StreamFilter`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/StreamFilter "A StreamFilter is an object you can use to monitor and modify HTTP responses.") object for a given request.

## Events

[`webRequest.onBeforeRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when
a request is about to be made, and before headers are available. This is a
good place to listen if you want to cancel or redirect the request.")

    Fired when a request is about to be made, and before headers are available. This is a good place to listen if you want to cancel or redirect the request.
[`webRequest.onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered
before sending any HTTP data, but after all HTTP headers are available. This
is a good place to listen if you want to modify HTTP request headers.")

    Fired before sending any HTTP data, but after HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.
[`webRequest.onSendHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onSendHeaders "This event is fired just
before sending headers. If your extension or some other extension modified
headers in onBeforeSendHeaders, you'll see the modified version here.")

    Fired just before sending headers. If your add-on or some other add-on modified headers in `[`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered before sending any HTTP data, but after all HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.")`, you'll see the modified version here.
[`webRequest.onHeadersReceived`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onHeadersReceived "Fired when the HTTP
response headers associated with a request have been received. You can use
this event to modify HTTP response headers.")

    Fired when the HTTP response headers associated with a request have been received. You can use this event to modify HTTP response headers.
[`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a
401 or 407 status code: that is, when the server is asking the client to
provide authentication credentials such as a username and password.")

    Fired when the server asks the client to provide authentication credentials. The listener can do nothing, cancel the request, or supply authentication credentials.
[`webRequest.onResponseStarted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onResponseStarted "Fired when the first byte
of the response body is received.")

    Fired when the first byte of the response body is received. For HTTP requests, this means that the status line and response headers are available.
[`webRequest.onBeforeRedirect`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeRedirect "Fired when a server-
initiated redirect is about to occur.")

    Fired when a server-initiated redirect is about to occur.
[`webRequest.onCompleted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onCompleted "Fired when a request has
completed.")

    Fired when a request is completed.
[`webRequest.onErrorOccurred`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onErrorOccurred "Fired when a request could
not be processed due to an error: for example, a lack of Internet
connectivity.")

    Fired when an error occurs.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`BlockingResponse`|  Yes|  Yes| 45| 48|  Yes  
`HttpHeaders`|  Yes|  Yes| 45| 48|  Yes  
`MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES`|  Yes|  Yes| 45| 48|  Yes  
`RequestFilter`|  Yes|  Yes| 45 *| 48 *|  Yes  
`ResourceType`| 44 *|  No| 45 *| 48 *| 31 *  
`StreamFilter`|  No|  No| 57| 57|  No  
`UploadData`|  Yes|  Yes| 45| 48|  Yes  
`filterResponseData`|  No|  No| 57| 57|  No  
`handlerBehaviorChanged`|  Yes|  Yes| 45| 48|  Yes  
`onAuthRequired`|  Yes|  Yes| 54 *| 54 *|  Yes  
`onBeforeRedirect`|  Yes|  Yes| 46| 48|  Yes  
`onBeforeRequest`|  Yes *|  Yes *| 46 *| 48 *|  Yes *  
`onBeforeSendHeaders`|  Yes *|  Yes *| 45 *| 48 *|  Yes *  
`onCompleted`|  Yes|  Yes| 45| 48|  Yes  
`onErrorOccurred`|  Yes|  Yes| 45| 48|  Yes  
`onHeadersReceived`|  Yes *|  Yes *| 45 *| 48 *|  Yes *  
`onResponseStarted`|  Yes|  Yes| 45| 48|  Yes  
`onSendHeaders`|  Yes|  Yes| 45| 48|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`BlockingResponse`|  Full support Yes|  Full support Yes|  Full support 45|
Full support Yes|  Full support 48  
`HttpHeaders`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  Full support 48  
`MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES`|  Full support Yes|  Full
support Yes|  Full support 45|  Full support Yes|  Full support 48  
`RequestFilter`|  Full support Yes|  Full support Yes|  Partial support 45|
Full support Yes|  Partial support 48  
`ResourceType`|  Partial support 44|  No support No|  Partial support 45|
Partial support 31|  Partial support 48  
`StreamFilter`|  No support No|  No support No|  Full support 57|  No support
No|  Full support 57  
`UploadData`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  Full support 48  
`filterResponseData`|  No support No|  No support No|  Full support 57|  No
support No|  Full support 57  
`handlerBehaviorChanged`|  Full support Yes|  Full support Yes|  Full support
45|  Full support Yes|  Full support 48  
`onAuthRequired`|  Full support Yes|  Full support Yes|  Partial support 54

Notes __

Partial support 54

Notes __

     Notes __To handle a request asynchronously, return a Promise from the listener.
|  Full support Yes|  Partial support 54

Notes __

Partial support 54

Notes __

     Notes __To handle a request asynchronously, return a Promise from the listener.  
`onBeforeRedirect`|  Full support Yes|  Full support Yes|  Full support 46|
Full support Yes|  Full support 48  
`onBeforeRequest`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support 46

Notes __

Full support 46

Notes __

     Notes __Asynchronous event listeners are supported from version 52.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Asynchronous event listeners are supported from version 52.  
`onBeforeSendHeaders`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support 45

Notes __

Full support 45

Notes __

     Notes __Asynchronous event listeners are supported from version 52.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Asynchronous event listeners are supported from version 52.  
`onCompleted`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  Full support 48  
`onErrorOccurred`|  Full support Yes|  Full support Yes|  Full support 45|
Full support Yes|  Full support 48  
`onHeadersReceived`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support 45

Notes __

Full support 45

Notes __

     Notes __Modification of the 'Content-Type' header is supported from version 51.
     Notes __Asynchronous event listeners are supported from version 52.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Asynchronous event listeners are not supported.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Modification of the 'Content-Type' header is supported from version 51.
     Notes __Asynchronous event listeners are supported from version 52.  
`onResponseStarted`|  Full support Yes|  Full support Yes|  Full support 45|
Full support Yes|  Full support 48  
`onSendHeaders`|  Full support Yes|  Full support Yes|  Full support 45|  Full
support Yes|  Full support 48  
  
The "Chrome incompatibilities" section is included from [
https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Chrome_incompatibilities](https://developer.mozilla.org/en-
US/Add-ons/WebExtensions/Chrome_incompatibilities) using the
[WebExtChromeCompat](/en-US/docs/Template:WebExtChromeCompat) macro.

If you need to update this content, edit <https://developer.mozilla.org/en-US
/Add-ons/WebExtensions/Chrome_incompatibilities>, then shift-refresh this page
to see your changes.

### Chrome incompatibilities

#### [webRequest](/en-US/Add-ons/WebExtensions/API/webRequest)

  * In Firefox requests can be redirected only if their original URL uses the `http:` or `https:` scheme.
  * In Firefox, events are not fired for system requests (for example, extension upgrades or searchbar suggestions). From Firefox 57 onwards, Firefox makes an exception for extensions that need to intercept [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.") for proxy authorization. See the documentation for [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.").

## Example extensions

  * [http-response](https://github.com/mdn/webextensions-examples/tree/master/http-response)
  * [stored-credentials](https://github.com/mdn/webextensions-examples/tree/master/stored-credentials)
  * [user-agent-rewriter](https://github.com/mdn/webextensions-examples/tree/master/user-agent-rewriter)

**Acknowledgements**

This API is based on Chromium's
[`chrome.webRequest`](https://developer.chrome.com/extensions/webRequest) API.
This documentation is derived from
[`web_request.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/web_request.json)
in the Chromium code.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.
    //
    // Redistribution and use in source and binary forms, with or without
    // modification, are permitted provided that the following conditions are
    // met:
    //
    //    * Redistributions of source code must retain the above copyright
    // notice, this list of conditions and the following disclaimer.
    //    * Redistributions in binary form must reproduce the above
    // copyright notice, this list of conditions and the following disclaimer
    // in the documentation and/or other materials provided with the
    // distribution.
    //    * Neither the name of Google Inc. nor the names of its
    // contributors may be used to endorse or promote products derived from
    // this software without specific prior written permission.
    //
    // THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    // "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    // LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    // A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    // OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    // SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    // LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    // DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    // THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    // (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    // OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
  *[
No support

]: No support

  *[
 Partial support

]: Partial support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[
Partial support

]: Partial support

  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[
Full support

]: Full support

  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

