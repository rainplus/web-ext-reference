[\n

\n

To intercept HTTP requests, use the [`webRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest "Add event listeners for the various stages
of making an HTTP request. The event listener receives detailed information
about the request, and can modify or cancel the request.") API. This API
enables you to add listeners for various stages of making an HTTP request. In
the listeners, you can:

\n

\n

  * get access to request headers and bodies, and response headers
\n

  * cancel and redirect requests
\n

  * modify request and response headers
\n

\n

In this article we'll look at three different uses for the `webRequest`
module:

\n

\n

  * Logging request URLs as they are made.
\n

  * Redirecting requests.
\n

  * Modifying request headers.
\n

\n

## Logging request URLs

\n

Create a new directory called "requests". In that directory, create a file
called "manifest.json" which has the following contents:

\n

    
    
    {\n  "description": "Demonstrating webRequests",\n  "manifest_version": 2,\n  "name": "webRequest-demo",\n  "version": "1.0",\n\n  "permissions": [\n    "webRequest",\n    "<all_urls>"\n  ],\n\n  "background": {\n    "scripts": ["background.js"]\n  }\n}

\n

Next, create a file called "background.js" with the following contents:

\n

    
    
    function logURL(requestDetails) {\n  console.log("Loading: " + requestDetails.url);\n}\n\nbrowser.webRequest.onBeforeRequest.addListener(\n  logURL,\n  {urls: ["<all_urls>"]}\n);\n\n

\n

Here we use [`onBeforeRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when
a request is about to be made, and before headers are available. This is a
good place to listen if you want to cancel or redirect the request.") to call
the `logURL()` function just before starting the request. The `logURL()`
function grabs the URL of the request from the event object and logs it to the
browser console. The `{urls: ["<all_urls>"]}` [pattern](/en-US/Add-
ons/WebExtensions/Match_patterns) means we will intercept HTTP requests to all
URLs.

\n

To test it out, [install the extension](/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox), [open the Browser
Console](/en-US/docs/Tools/Browser_Console), and open some Web pages. In the
Browser Console, you should see the URLs for any resources that the browser
requests:

\n

\n

## Redirecting requests

\n

Now let's use `webRequest` to redirect HTTP requests. First, replace
manifest.json with this:

\n

    
    
    {\n\n  "description": "Demonstrating webRequests",\n  "manifest_version": 2,\n  "name": "webRequest-demo",\n  "version": "1.0",\n\n  "permissions": [\n    "webRequest",\n    "webRequestBlocking",\n    "https://mdn.mozillademos.org"\n  ],\n \n  "background": {\n    "scripts": ["background.js"]\n  }\n\n}

\n

The only change here is to add the `"webRequestBlocking"` `[permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)`. We need to
ask for this extra permission whenever we are actively modifying a request.

\n

Next, replace "background.js" with this:

\n

    
    
    var pattern = "https://mdn.mozillademos.org/*";\n\nfunction redirect(requestDetails) {\n  console.log("Redirecting: " + requestDetails.url);\n  return {\n    redirectUrl: "https://38.media.tumblr.com/tumblr_ldbj01lZiP1qe0eclo1_500.gif"\n  };\n}\n\nbrowser.webRequest.onBeforeRequest.addListener(\n  redirect,\n  {urls:[pattern], types:["image"]},\n  ["blocking"]\n);

\n

Again, we use the\xa0[`onBeforeRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when
a request is about to be made, and before headers are available. This is a
good place to listen if you want to cancel or redirect the request.") event
listener to run a function just before each request is made. This function
will replace the target URL with the `redirectUrl` specified in the function.

\n

This time we are not intercepting every request: the `{urls:[pattern],
types:["image"]}` option specifies that we should only intercept requests (1)
to URLs residing under "https://mdn.mozillademos.org/" (2) for image
resources. See [`webRequest.RequestFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/RequestFilter "An object describing filters
to apply to webRequest events.") for more on this.

\n

Also note that we're passing an option called `"blocking"`: we need to pass
this whenever we want to modify the request. It makes the listener function
block the network request, so the browser waits for the listener to return
before continuing. See the [`webRequest.onBeforeRequest`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered
when a request is about to be made, and before headers are available. This is
a good place to listen if you want to cancel or redirect the request.")
documentation for more on `"blocking"`.

\n

To test it out, open a page on MDN that contains a lot of images (for example
<https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor>), [reload the
extension](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox
#Reloading_a_temporary_add-on), and then reload the MDN page:

\n

\n

## Modifying request headers

\n

Finally we'll use `webRequest` to modify request headers. In this example
we'll modify the "User-Agent" header so the browser identifies itself as Opera
12.16, but only when visiting pages under http://useragentstring.com/".

\n

The "manifest.json" can stay the same as in the previous example.

\n

Replace "background.js" with code like this:

\n

    
    
    var targetPage = "http://useragentstring.com/*";\n\nvar ua = "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16";\n\nfunction rewriteUserAgentHeader(e) {\n  for (var header of e.requestHeaders) {\n    if (header.name.toLowerCase() == "user-agent") {\n      header.value = ua;\n    }\n  }\n  return {requestHeaders: e.requestHeaders};\n}\n\nbrowser.webRequest.onBeforeSendHeaders.addListener(\n  rewriteUserAgentHeader,\n  {urls: [targetPage]},\n  ["blocking", "requestHeaders"]\n);

\n

Here we use the\xa0[`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered
before sending any HTTP data, but after all HTTP headers are available. This
is a good place to listen if you want to modify HTTP request headers.") event
listener to run a function just before the request headers are sent.

\n

The listener function will be called only for requests to URLs matching the
`targetPage` [pattern](/en-US/Add-ons/WebExtensions/Match_patterns). Also note
that we've again passed `"blocking"` as an option. We've also passed
`"requestHeaders"`, which means that the listener will be passed an array
containing the request headers that we expect to send. See
[`webRequest.onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered
before sending any HTTP data, but after all HTTP headers are available. This
is a good place to listen if you want to modify HTTP request headers.") for
more information on these options.

\n

The\xa0listener function looks for the "User-Agent" header in the array of
request headers, replaces its value with the value of the `ua` variable, and
returns the modified array. This modified array will now be sent to the
server.

\n

To test it out, open [useragentstring.com](http://useragentstring.com/) and
check that it identifies the browser as Firefox. Then reload the extension,
reload [useragentstring.com](http://useragentstring.com/), and check that
Firefox is now identified as Opera:

\n

\n

## Learn more

\n

To learn about all the things you can do with the `webRequest` API, see its
[reference documentation](/en-US/Add-ons/WebExtensions/API/WebRequest).

\n]

