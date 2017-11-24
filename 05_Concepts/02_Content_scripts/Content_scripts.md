[\n

\n

A content script is a part of your extension that runs in the context of a
particular web page (as opposed to background scripts which are part of the
extension, or scripts which are part of the web site itself, such as those
loaded using the [`<script>`](/en-US/docs/Web/HTML/Element/script "The HTML
<script> element is used to embed or reference an executable script.")
element).

\n

[Background scripts](/en-US/Add-ons/WebExtensions/Background_scripts) can
access all the\xa0[WebExtension JavaScript APIs](/en-US/Add-
ons/WebExtensions/API), but they can't directly access the content of web
pages. So if your extension needs to do that, you need content scripts.

\n

Just like the scripts loaded by normal web pages, content scripts can read and
modify the content of their pages using the standard DOM APIs.

\n

Content scripts can only access [a small subset of the WebExtension
APIs](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Content_scripts#WebExtension_APIs), but they can
[communicate with background scripts](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Content_scripts#Communicating_with_background_scripts) using
a messaging system, and thereby indirectly access the WebExtension APIs.

\n

\n

Note that content scripts are currently blocked on addons.mozilla.org and
testpilot.firefox.com. If you try to inject a content script into a page in
these domains, it will fail and the page will log a [CSP](/en-
US/docs/Web/HTTP/CSP) error.

\n

\n

## Loading content scripts

\n

You can load a content script into a web page in one of two ways:

\n

\n

  *  **declaratively** : using the `[content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)` key in your manifest.json, you can ask the browser to load a content script whenever the browser loads a page whose URL [matches a given pattern](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/match_patterns)
\n

  *  **programmatically** : using the `[tabs.executeScript()](/en-US/Add-ons/WebExtensions/API/Tabs/executeScript)` API, you can load a content script into a specific tab whenever you want: for example, in response to the user clicking on a [browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action).
\n

\n

There is only one global scope per frame per extension, so variables from one
content script can directly be accessed by another content script, regardless
of how the content script was loaded.

\n

## Content script environment

\n

### DOM access

\n

Content scripts can access and modify the page's DOM, just like normal page
scripts can. They can also see any changes that were made to the DOM by page
scripts.

\n

However, content scripts get a "clean view of the DOM". This means:

\n

\n

  * content scripts cannot see JavaScript variables defined by page scripts
\n

  * if a page script redefines a built-in DOM property, the content script will see the original version of the property, not the redefined version.
\n

\n

In Gecko, this behavior is called [Xray vision](/en-US/docs/Xray_vision).

\n

For example, consider a web page like this:

\n

    
    
    <!DOCTYPE html>\n<html>\n  <head>\n    <meta http-equiv="content-type" content="text/html; charset=utf-8" />\n  </head>\n\n  <body>\n    <script src="page-scripts/page-script.js"></script>\n  </body>\n</html>

\n

The script "page-script.js" does this:

\n

    
    
    // page-script.js\n\n// add a new element to the DOM\nvar p = document.createElement("p");\np.textContent = "This paragraph was added by a page script.";\np.setAttribute("id", "page-script-para");\ndocument.body.appendChild(p);\n\n// define a new property on the window\nwindow.foo = "This global variable was added by a page script";\n\n// redefine the built-in window.confirm() function\nwindow.confirm = function() {\n  alert("The page script has also redefined 'confirm'");\n}

\n

Now an extension injects a content script into the page:

\n

    
    
    // content-script.js\n\n// can access and modify the DOM\nvar pageScriptPara = document.getElementById("page-script-para");\npageScriptPara.style.backgroundColor = "blue";\n\n// can't see page-script-added properties\nconsole.log(window.foo);  // undefined\n\n// sees the original form of redefined properties\nwindow.confirm("Are you sure?"); // calls the original window.confirm()

\n

The same is true in reverse: page scripts can't see JavaScript properties
added by content scripts.

\n

All this means that the content script can rely on DOM properties behaving
predictably, and doesn't have to worry about variables it defines clashing
with variables defined in the page script.

\n

One practical consequence of this behavior is that a content script won't have
access to any JavaScript libraries loaded by the page. So for example, if the
page includes jQuery, the content script won't be able to see it.

\n

If a content script does want to use a JavaScript library, then the library
itself should be injected as a content script alongside the content script
that wants to use it:

\n

    
    
    "content_scripts": [\n  {\n    "matches": ["*://*.mozilla.org/*"],\n    "js": ["jquery.js", "content-script.js"]\n  }\n]

\n

### WebExtension APIs

\n

In addition to the standard DOM APIs, content scripts can use the following
WebExtension APIs:

\n

From `[extension](/en-US/Add-ons/WebExtensions/API/extension)`:

\n

\n

  * `[getURL()](/en-US/Add-ons/WebExtensions/API/extension#getURL\(\))`
\n

  * `[inIncognitoContext](/en-US/Add-ons/WebExtensions/API/extension#inIncognitoContext)`
\n

\n

From `[runtime](/en-US/Add-ons/WebExtensions/API/runtime)`:

\n

\n

  * `[connect()](/en-US/Add-ons/WebExtensions/API/runtime#connect\(\))`
\n

  * `[getManifest()](/en-US/Add-ons/WebExtensions/API/runtime#getManifest\(\))`
\n

  * `[getURL()](/en-US/Add-ons/WebExtensions/API/runtime#getURL\(\))`
\n

  * `[onConnect](/en-US/Add-ons/WebExtensions/API/runtime#onConnect)`
\n

  * `[onMessage](/en-US/Add-ons/WebExtensions/API/runtime#onMessage)`
\n

  * `[sendMessage()](/en-US/Add-ons/WebExtensions/API/runtime#sendMessage\(\))`
\n

\n

From `[i18n](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)`:

\n

\n

  * `[getMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getMessage)`
\n

  * `[getAcceptLanguages()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getAcceptLanguages)`
\n

  * `[getUILanguage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getUILanguage)`
\n

  * `[detectLanguage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/detectLanguage)`
\n

\n

Everything from `[storage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage)`.

\n

### XHR and Fetch

\n

Content scripts can make requests using the normal `[window.XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest)` and `[window.fetch()](/en-
US/docs/Web/API/Fetch_API)` APIs.

\n

Content scripts get the same cross-domain privileges as the rest of the
extension: so if the extension has requested cross-domain access for a domain
using the `[permissions](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions)` key in manifest.json, then its
content scripts get access that domain as well.

\n

This is accomplished by exposing more privileged XHR and fetch instances in
the content script, which has the side-effect of not setting the `[Origin
](/en-US/docs/Web/HTTP/Headers/Origin)` and `[Referer](/en-
US/docs/Web/HTTP/Headers/Referer)` headers like a request from the page itself
would, this is often preferable to prevent the request from revealing its
cross-orign nature. From version 58 onwards extensions that need to perform
requests that behave as if they were sent by the content itself can use\xa0
`content.XMLHttpRequest` and `content.fetch()` instead. For cross-browser
extensions their presence must be feature-detected.

\n

## Communicating with background scripts

\n

Although content scripts can't directly use most of the WebExtension APIs,
they can communicate with the extension's background scripts using the
messaging APIs, and can therefore indirectly access all the same APIs that the
background scripts can.

\n

There are two basic patterns for communicating between the background scripts
and content scripts: you can send one-off messages, with an optional response,
or you can set up a longer-lived connection between the two sides, and use
that connection to exchange messages.

\n

### One-off messages

\n

To send one-off messages, with an optional response, you can use the following
APIs:

\n\n\n\n\xa0\n| In content script\n| In background script\n  
---|---|---  
\n\n\n\nSend a message\n| `[browser.runtime.sendMessage()](/en-US/Add-
ons/WebExtensions/API/runtime#sendMessage\(\))`\n| `[browser.tabs.sendMessage
()](/en-US/Add-ons/WebExtensions/API/Tabs/sendMessage)`\n  
\n\nReceive a message\n| `[browser.runtime.onMessage](/en-US/Add-
ons/WebExtensions/API/runtime/onMessage)`\n| `[browser.runtime.onMessage](/en-
US/Add-ons/WebExtensions/API/runtime#onMessage)`\n  
\n\n\n

For example, here's a content script which listens for click events in the web
page. If the click was on a link, it messages the background page with the
target URL:

\n

    
    
    // content-script.js\n\nwindow.addEventListener("click", notifyExtension);\n\nfunction notifyExtension(e) {\n  if (e.target.tagName != "A") {\n    return;\n  }\n  browser.runtime.sendMessage({"url": e.target.href});\n}

\n

The background script listens for these messages and displays a notification
using the `[notifications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications)` API:

\n

    
    
    // background-script.js\n\nbrowser.runtime.onMessage.addListener(notify);\n\nfunction notify(message) {\n  browser.notifications.create({\n    "type": "basic",\n    "iconUrl": browser.extension.getURL("link.png"),\n    "title": "You clicked a link!",\n    "message": message.url\n  });\n}\n

\n

This example code is lightly adapted from the [notify-link-clicks-
i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-
clicks-i18n) example on GitHub.

\n

### Connection-based messaging

\n

Sending one-off messages can get cumbersome if you are exchanging a lot of
messages between a background script and a content script. So an alternative
pattern is to establish a longer-lived connection between the two contexts,
and use this connection to exchange messages.

\n

Each side has a `[runtime.Port](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/Port)` object, which they can use to exchange
messages.

\n

To create the connection:

\n

\n

  * one side listens for connections using `[runtime.onConnect](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect)`
\n

  * the other side calls either `[tabs.connect()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/connect)` (if connecting to a content script) or `[runtime.connect()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/connect)` (if connecting to a background script). This returns a `[runtime.Port](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port)` object.
\n

  * the\xa0`[runtime.onConnect](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect)` listener gets passed its own `[runtime.Port](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port)` object.
\n

\n

Once each side has a port, the two sides can exchange messages using
`runtime.Port.postMessage()` to send a message, and `runtime.Port.onMessage`
to receive messages.

\n

For example, as soon as it loads, this content script:

\n

\n

  * connects to the background script, and stores the `Port` in a variable `myPort`
\n

  * listens for messages on `myPort`, and logs them
\n

  * sends messages to the background script, using `myPort`, when the user clicks the document
\n

\n

    
    
    // content-script.js\n\nvar myPort = browser.runtime.connect({name:"port-from-cs"});\nmyPort.postMessage({greeting: "hello from content script"});\n\nmyPort.onMessage.addListener(function(m) {\n  console.log("In content script, received message from background script: ");\n  console.log(m.greeting);\n});\n\ndocument.body.addEventListener("click", function() {\n  myPort.postMessage({greeting: "they clicked the page!"});\n});

\n

The corresponding background script:

\n

\n

  * listens for connection attempts from the content script
\n

  * when it receives a connection attempt:\n \n
    * stores the port in a variable named `portFromCS`
\n

    * sends the content script a message using the port
\n

    * starts listening to messages received on the port, and logs them
\n\n

\n

  * sends messages to the content script, using `portFromCS`, when the user clicks the extension's browser action
\n

\n

    
    
    // background-script.js\n\nvar portFromCS;\n\nfunction connected(p) {\n  portFromCS = p;\n  portFromCS.postMessage({greeting: "hi there content script!"});\n  portFromCS.onMessage.addListener(function(m) {\n    console.log("In background script, received message from content script")\n    console.log(m.greeting);\n  });\n}\n\nbrowser.runtime.onConnect.addListener(connected);\n\nbrowser.browserAction.onClicked.addListener(function() {\n  portFromCS.postMessage({greeting: "they clicked the button!"});\n});\n

\n

\n

\n

## Communicating with the web page

\n

Although content scripts don't by default get access to objects created by
page scripts, they can communicate with page scripts using the DOM
`[window.postMessage](/en-US/docs/Web/API/Window/postMessage)` and
`[window.addEventListener](/en-US/docs/Web/API/EventTarget/addEventListener)`
APIs.

\n

For example:

\n

    
    
    // page-script.js\n\nvar messenger = document.getElementById("from-page-script");\n\nmessenger.addEventListener("click", messageContentScript);\n\nfunction messageContentScript() {\n  window.postMessage({\n    direction: "from-page-script",\n    message: "Message from the page"\n  }, "*");

\n

    
    
    // content-script.js\n\nwindow.addEventListener("message", function(event) {\n  if (event.source == window &&\n      event.data &&\n      event.data.direction == "from-page-script") {\n    alert("Content script received message: \\"" + event.data.message + "\\"");\n  }\n});

\n

For a complete working example of this, [visit the demo page on
GitHub](https://mdn.github.io/webextensions-examples/content-script-page-
script-messaging.html) and follow the instructions.

\n

\n

Note that any time you interact with untrusted web content on this way, you
need to be very careful. Extensions are privileged code which can have
powerful capabilities, and hostile web pages can easily trick them into
accessing those capabilities.

\n

To make a trivial example, suppose the content script code that receives the
message does something like this:

\n

    
    
    // content-script.js\n\nwindow.addEventListener("message", function(event) {\n  if (event.source == window &&\n      event.data.direction &&\n      event.data.direction == "from-page-script") {\n    eval(event.data.message);\n  }\n});

\n

Now the page script can run any code with all the privileges of the content
script.

\n

\n

## Sharing objects with page scripts

\n

\n

The techniques described in this section are only available in Firefox, and
only from Firefox 49 onwards.

\n

\n

\n

As an extension developer you should consider that scripts running in
arbitrary web pages are hostile code whose aim is to steal the user's personal
information, damage their computer, or attack them in some other way.

\n

The isolation between content scripts and scripts loaded by web pages is
intended to make it more difficult for hostile web pages to do this.

\n

Since the techniques described in this section break down that isolation, they
are inherently dangerous and should be used with great care.

\n

\n

We saw in [DOM access](/en-US/Add-
ons/WebExtensions/Content_scripts#DOM_access) that content scripts don't see
changes made to the DOM by scripts loaded by web pages. This means that, for
example, if a web page loads a library like jQuery, content scripts won't be
able to use it, and have to load their own copy. Conversely, scripts loaded by
web pages can't see changes made by content scripts.

\n

However, Firefox provides some APIs that enable content scripts to:

\n

\n

  * access JavaScript objects created by page scripts
\n

  * expose their own JavaScript objects to page scripts.
\n

\n

### Xray vision in Firefox

\n

In Firefox, part of the isolation between content scripts and page scripts is
implemented using a feature called "Xray vision". When a script in a more-
privileged scope accesses an object that's defined in a less-privileged scope
it sees only the "native version" of the object. Any [expando](/en-
US/docs/Glossary/Expando) properties are invisible, and if any properties of
the object have been redefined, it sees the original implementation, not the
redefined version.

\n

The purpose of this feature is to make it harder for the less-privileged
script to confuse the more-privileged script by redefining the native
properties of objects.

\n

So for example, when a content script accesses the page's [window](/en-
US/docs/Web/API/Window), it won't see any properties the page script added to
the window, and if the page script has redefined any existing properties of
the window, the content script will see the original version.

\n

For the full story on Xray vision, see the articles on [Xray vision](/en-
US/docs/Mozilla/Tech/Xray_vision) and [Script security](/en-
US/docs/Mozilla/Gecko/Script_security).

\n

### Accessing page script objects from content scripts

\n

In Firefox, DOM objects in content scripts get an extra
property\xa0`wrappedJSObject`. This is an "unwrapped" version of the object,
which includes any changes made to that object by any page scripts.

\n

Let's take a simple example. Suppose a web page loads a script:

\n

    
    
    <!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="UTF-8">\n  </head>\n  <body>\n    <script type="text/javascript" src="main.js"></script>\n  </body>\n</html>

\n

The script adds an expando property to the global `window`:

\n

    
    
    // main.js\n\nvar foo = "I'm defined in a page script!";

\n

Xray vision means that if a content script tries to access `foo`, it will be
undefined:

\n

    
    
    // content-script.js\n\nconsole.log(window.foo); // undefined

\n

In Firefox, content scripts can use `window.wrappedJSObject` to see the
expando property:

\n

    
    
    // content-script.js\n\nconsole.log(window.wrappedJSObject.foo); // "I'm defined in a page script!"

\n

Note that once you do this, you can no longer rely on any of this object's
properties or functions being, or doing, what you expect. Any of them, even
setters and getters, could have been redefined by untrusted code.

\n

Also note that unwrapping is transitive: when you use `wrappedJSObject`, any
properties of the unwrapped object are themselves unwrapped (and therefore
unreliable). So it's good practice, once you've got the object you need, to
rewrap it, which you can do like this:

\n

    
    
    XPCNativeWrapper(window.wrappedJSObject.foo);

\n

See the document on [Xray vision](/en-US/docs/Mozilla/Tech/Xray_vision) for
much more detail on this.

\n

### Sharing content script objects with page scripts

\n

Firefox also provides APIs enabling content scripts to make objects available
to page scripts. There are two main APIs here:

\n

\n

  * `[exportFunction()](/en-US/Add-ons/WebExtensions/Content_scripts#exportFunction)`: export a function to page scripts.
\n

  * `[cloneInto()](/en-US/Add-ons/WebExtensions/Content_scripts#cloneInto)`: export an object to page scripts.
\n

\n

#### exportFunction

\n

Given a function defined in the content script, `exportFunction()` exports it
to the page script's scope, so the page script can call it.

\n

For example, let's consider an extension which has a background script like
this:

\n

    
    
    /*\nExecute content script in the active tab.\n*/\nfunction loadContentScript() {\n  browser.tabs.executeScript({\n    file: "/content_scripts/export.js"\n  });\n}\n\n/*\nAdd loadContentScript() as a listener to clicks\non the browser action.\n*/\nbrowser.browserAction.onClicked.addListener(loadContentScript);\n\n/*\nShow a notification when we get messages from\nthe content script.\n*/\nbrowser.runtime.onMessage.addListener((message) => {\n  browser.notifications.create({\n    type: "basic",\n    title: "Message from the page",\n    message: message.content\n  });\n});

\n

This does two things:

\n

\n

  * execute a content script in the current tab, when the user clicks a browser action
\n

  * listen for messages from the content script, and display a [notification](/en-US/Add-ons/WebExtensions/API/notifications) when the message arrives.
\n

\n

The content script looks like this:

\n

    
    
    /*\nDefine a function in the content script's scope, then export it\ninto the page script's scope.\n*/\nfunction notify(message) {\n  browser.runtime.sendMessage({content: "Function call: " + message});\n}\n\nexportFunction(notify, window, {defineAs:'notify'});

\n

This defines a function `notify()`, which just sends its argument to the
background script. It then exports the function to the page script's scope.
Now the page script can call this function:

\n

    
    
    window.notify("Message from the page script!");

\n

For the full story, see `[Components.utils.exportFunction](/en-
US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.exportFunction)`.

\n

#### cloneInto

\n

Given an object defined in the content script, this creates a clone of the
object in the page script's scope, thereby making the clone accessible to page
scripts. By default, this uses the [structured clone algorithm](/en-
US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) to clone the
object, meaning that functions in the object are not included in the clone. To
include functions, pass the `cloneFunctions` option.

\n

For example, here's a content script that defines an object that contains a
function, then clones it into the page script's scope:

\n

    
    
    /*\nCreate an object that contains functions in\nthe content script's scope, then clone it\ninto the page script's scope.\n\nBecause the object contains functions,\nthe cloneInto call must include\nthe `cloneFunctions` option.\n*/\nvar messenger = {\n  notify: function(message) {\n    browser.runtime.sendMessage({\n      content: "Object method call: " + message\n    });\n  }\n};\n\nwindow.wrappedJSObject.messenger = cloneInto(\n  messenger,\n  window,\n  {cloneFunctions: true});

\n

Now page scripts will see a new property on the window, `messenger`, which has
a function `notify()`:

\n

    
    
    window.messenger.notify("Message from the page script!");

\n

For the full story, see `[Components.utils.cloneInto](/en-
US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.cloneInto)`.

\n

## Using eval() in content scripts

\n

In Chrome, `[eval()](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/eval)` always runs code in the
context of the content script, not in the context of the page.

\n

In Firefox:

\n

\n

  * if you call `eval()`, it runs code in the context of the content script
\n

  * if you call `window.eval()`, it runs code in the context of the page.
\n

\n

For example, consider a content script like this:

\n

    
    
    // content-script.js\n\nwindow.eval('window.x = 1;');\neval('window.y = 2');\n\nconsole.log(`In content script, window.x: ${window.x}`);\nconsole.log(`In content script, window.y: ${window.y}`);\n\nwindow.postMessage({\n  message: "check"\n}, "*");

\n

This code just creates some variables x and y using `window.eval()` and
`eval()`, then logs their values, then messages the page.

\n

On receiving the message, the page script logs the same variables:

\n

    
    
    window.addEventListener("message", function(event) {\n  if (event.source === window && event.data && event.data.message === "check") {\n    console.log(`In page script, window.x: ${window.x}`);\n    console.log(`In page script, window.y: ${window.y}`);\n  }\n});

\n

In Chrome, this will produce output like this:

\n

    
    
    In content script, window.x: 1\nIn content script, window.y: 2\nIn page script, window.x: undefined\nIn page script, window.y: undefined

\n

In Firefox the following output is produced:

\n

    
    
    In content script, window.x: undefined\nIn content script, window.y: 2\nIn page script, window.x: 1\nIn page script, window.y: undefined

\n

The same applies to `[setTimeout()](/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)`, `[setInterval()](/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)`, and `[Function
()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)`.

\n

When running code in the context of the page, the warning in the "[Sharing
content script objects with page scripts](/en-US/Add-
ons/WebExtensions/Content_scripts#Sharing_objects_with_page_scripts)" section
above applies: the page's environment is controlled by potentially malicious
web pages, which can redefine objects you interact with to behave in
unexpected ways:

\n

    
    
    // page.js redefines console.log\n\nvar original = console.log;\n\nconsole.log = function() {\n\xa0 original(true);\n}\n

\n

    
    
    // content-script.js calls the redefined version\n\nwindow.eval('console.log(false)');\n

\n]

