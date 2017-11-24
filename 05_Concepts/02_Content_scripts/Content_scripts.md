A content script is a part of your extension that runs in the context of a
particular web page (as opposed to background scripts which are part of the
extension, or scripts which are part of the web site itself, such as those
loaded using the [`<script>`](/en-US/docs/Web/HTML/Element/script "The HTML
<script> element is used to embed or reference an executable script.")
element).

[Background scripts](/en-US/Add-ons/WebExtensions/Background_scripts) can
access all the [WebExtension JavaScript APIs](/en-US/Add-
ons/WebExtensions/API), but they can't directly access the content of web
pages. So if your extension needs to do that, you need content scripts.

Just like the scripts loaded by normal web pages, content scripts can read and
modify the content of their pages using the standard DOM APIs.

Content scripts can only access [a small subset of the WebExtension
APIs](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Content_scripts#WebExtension_APIs), but they can
[communicate with background scripts](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Content_scripts#Communicating_with_background_scripts) using
a messaging system, and thereby indirectly access the WebExtension APIs.

Note that content scripts are currently blocked on addons.mozilla.org and
testpilot.firefox.com. If you try to inject a content script into a page in
these domains, it will fail and the page will log a [CSP](/en-
US/docs/Web/HTTP/CSP) error.

## Loading content scripts

You can load a content script into a web page in one of two ways:

  * **declaratively** : using the `[content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)` key in your manifest.json, you can ask the browser to load a content script whenever the browser loads a page whose URL [matches a given pattern](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/match_patterns)
  * **programmatically** : using the `[tabs.executeScript()](/en-US/Add-ons/WebExtensions/API/Tabs/executeScript)` API, you can load a content script into a specific tab whenever you want: for example, in response to the user clicking on a [browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action).

There is only one global scope per frame per extension, so variables from one
content script can directly be accessed by another content script, regardless
of how the content script was loaded.

## Content script environment

### DOM access

Content scripts can access and modify the page's DOM, just like normal page
scripts can. They can also see any changes that were made to the DOM by page
scripts.

However, content scripts get a "clean view of the DOM". This means:

  * content scripts cannot see JavaScript variables defined by page scripts
  * if a page script redefines a built-in DOM property, the content script will see the original version of the property, not the redefined version.

In Gecko, this behavior is called [Xray vision](/en-US/docs/Xray_vision).

For example, consider a web page like this:

    
    
    <!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
      </head>
    
      <body>
        <script src="page-scripts/page-script.js"></script>
      </body>
    </html>

The script "page-script.js" does this:

    
    
    // page-script.js
    
    // add a new element to the DOM
    var p = document.createElement("p");
    p.textContent = "This paragraph was added by a page script.";
    p.setAttribute("id", "page-script-para");
    document.body.appendChild(p);
    
    // define a new property on the window
    window.foo = "This global variable was added by a page script";
    
    // redefine the built-in window.confirm() function
    window.confirm = function() {
      alert("The page script has also redefined 'confirm'");
    }

Now an extension injects a content script into the page:

    
    
    // content-script.js
    
    // can access and modify the DOM
    var pageScriptPara = document.getElementById("page-script-para");
    pageScriptPara.style.backgroundColor = "blue";
    
    // can't see page-script-added properties
    console.log(window.foo);  // undefined
    
    // sees the original form of redefined properties
    window.confirm("Are you sure?"); // calls the original window.confirm()

The same is true in reverse: page scripts can't see JavaScript properties
added by content scripts.

All this means that the content script can rely on DOM properties behaving
predictably, and doesn't have to worry about variables it defines clashing
with variables defined in the page script.

One practical consequence of this behavior is that a content script won't have
access to any JavaScript libraries loaded by the page. So for example, if the
page includes jQuery, the content script won't be able to see it.

If a content script does want to use a JavaScript library, then the library
itself should be injected as a content script alongside the content script
that wants to use it:

    
    
    "content_scripts": [
      {
        "matches": ["*://*.mozilla.org/*"],
        "js": ["jquery.js", "content-script.js"]
      }
    ]

### WebExtension APIs

In addition to the standard DOM APIs, content scripts can use the following
WebExtension APIs:

From `[extension](/en-US/Add-ons/WebExtensions/API/extension)`:

  * `[getURL()](/en-US/Add-ons/WebExtensions/API/extension#getURL\(\))`
  * `[inIncognitoContext](/en-US/Add-ons/WebExtensions/API/extension#inIncognitoContext)`

From `[runtime](/en-US/Add-ons/WebExtensions/API/runtime)`:

  * `[connect()](/en-US/Add-ons/WebExtensions/API/runtime#connect\(\))`
  * `[getManifest()](/en-US/Add-ons/WebExtensions/API/runtime#getManifest\(\))`
  * `[getURL()](/en-US/Add-ons/WebExtensions/API/runtime#getURL\(\))`
  * `[onConnect](/en-US/Add-ons/WebExtensions/API/runtime#onConnect)`
  * `[onMessage](/en-US/Add-ons/WebExtensions/API/runtime#onMessage)`
  * `[sendMessage()](/en-US/Add-ons/WebExtensions/API/runtime#sendMessage\(\))`

From `[i18n](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)`:

  * `[getMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getMessage)`
  * `[getAcceptLanguages()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getAcceptLanguages)`
  * `[getUILanguage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getUILanguage)`
  * `[detectLanguage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/detectLanguage)`

Everything from `[storage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage)`.

### XHR and Fetch

Content scripts can make requests using the normal `[window.XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest)` and `[window.fetch()](/en-
US/docs/Web/API/Fetch_API)` APIs.

Content scripts get the same cross-domain privileges as the rest of the
extension: so if the extension has requested cross-domain access for a domain
using the `[permissions](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions)` key in manifest.json, then its
content scripts get access that domain as well.

This is accomplished by exposing more privileged XHR and fetch instances in
the content script, which has the side-effect of not setting the `[Origin
](/en-US/docs/Web/HTTP/Headers/Origin)` and `[Referer](/en-
US/docs/Web/HTTP/Headers/Referer)` headers like a request from the page itself
would, this is often preferable to prevent the request from revealing its
cross-orign nature. From version 58 onwards extensions that need to perform
requests that behave as if they were sent by the content itself can use
`content.XMLHttpRequest` and `content.fetch()` instead. For cross-browser
extensions their presence must be feature-detected.

## Communicating with background scripts

Although content scripts can't directly use most of the WebExtension APIs,
they can communicate with the extension's background scripts using the
messaging APIs, and can therefore indirectly access all the same APIs that the
background scripts can.

There are two basic patterns for communicating between the background scripts
and content scripts: you can send one-off messages, with an optional response,
or you can set up a longer-lived connection between the two sides, and use
that connection to exchange messages.

### One-off messages

To send one-off messages, with an optional response, you can use the following
APIs:

  | In content script | In background script  
---|---|---  
Send a message | `[browser.runtime.sendMessage()](/en-US/Add-
ons/WebExtensions/API/runtime#sendMessage\(\))` | `[browser.tabs.sendMessage
()](/en-US/Add-ons/WebExtensions/API/Tabs/sendMessage)`  
Receive a message | `[browser.runtime.onMessage](/en-US/Add-
ons/WebExtensions/API/runtime/onMessage)` | `[browser.runtime.onMessage](/en-
US/Add-ons/WebExtensions/API/runtime#onMessage)`  
  
For example, here's a content script which listens for click events in the web
page. If the click was on a link, it messages the background page with the
target URL:

    
    
    // content-script.js
    
    window.addEventListener("click", notifyExtension);
    
    function notifyExtension(e) {
      if (e.target.tagName != "A") {
        return;
      }
      browser.runtime.sendMessage({"url": e.target.href});
    }

The background script listens for these messages and displays a notification
using the `[notifications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications)` API:

    
    
    // background-script.js
    
    browser.runtime.onMessage.addListener(notify);
    
    function notify(message) {
      browser.notifications.create({
        "type": "basic",
        "iconUrl": browser.extension.getURL("link.png"),
        "title": "You clicked a link!",
        "message": message.url
      });
    }
    

This example code is lightly adapted from the [notify-link-clicks-
i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-
clicks-i18n) example on GitHub.

### Connection-based messaging

Sending one-off messages can get cumbersome if you are exchanging a lot of
messages between a background script and a content script. So an alternative
pattern is to establish a longer-lived connection between the two contexts,
and use this connection to exchange messages.

Each side has a `[runtime.Port](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/Port)` object, which they can use to exchange
messages.

To create the connection:

  * one side listens for connections using `[runtime.onConnect](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect)`
  * the other side calls either `[tabs.connect()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/connect)` (if connecting to a content script) or `[runtime.connect()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/connect)` (if connecting to a background script). This returns a `[runtime.Port](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port)` object.
  * the `[runtime.onConnect](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect)` listener gets passed its own `[runtime.Port](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port)` object.

Once each side has a port, the two sides can exchange messages using
`runtime.Port.postMessage()` to send a message, and `runtime.Port.onMessage`
to receive messages.

For example, as soon as it loads, this content script:

  * connects to the background script, and stores the `Port` in a variable `myPort`
  * listens for messages on `myPort`, and logs them
  * sends messages to the background script, using `myPort`, when the user clicks the document

    
    
    // content-script.js
    
    var myPort = browser.runtime.connect({name:"port-from-cs"});
    myPort.postMessage({greeting: "hello from content script"});
    
    myPort.onMessage.addListener(function(m) {
      console.log("In content script, received message from background script: ");
      console.log(m.greeting);
    });
    
    document.body.addEventListener("click", function() {
      myPort.postMessage({greeting: "they clicked the page!"});
    });

The corresponding background script:

  * listens for connection attempts from the content script
  * when it receives a connection attempt: 
    * stores the port in a variable named `portFromCS`
    * sends the content script a message using the port
    * starts listening to messages received on the port, and logs them
  * sends messages to the content script, using `portFromCS`, when the user clicks the extension's browser action

    
    
    // background-script.js
    
    var portFromCS;
    
    function connected(p) {
      portFromCS = p;
      portFromCS.postMessage({greeting: "hi there content script!"});
      portFromCS.onMessage.addListener(function(m) {
        console.log("In background script, received message from content script")
        console.log(m.greeting);
      });
    }
    
    browser.runtime.onConnect.addListener(connected);
    
    browser.browserAction.onClicked.addListener(function() {
      portFromCS.postMessage({greeting: "they clicked the button!"});
    });
    

## Communicating with the web page

Although content scripts don't by default get access to objects created by
page scripts, they can communicate with page scripts using the DOM
`[window.postMessage](/en-US/docs/Web/API/Window/postMessage)` and
`[window.addEventListener](/en-US/docs/Web/API/EventTarget/addEventListener)`
APIs.

For example:

    
    
    // page-script.js
    
    var messenger = document.getElementById("from-page-script");
    
    messenger.addEventListener("click", messageContentScript);
    
    function messageContentScript() {
      window.postMessage({
        direction: "from-page-script",
        message: "Message from the page"
      }, "*");
    
    
    // content-script.js
    
    window.addEventListener("message", function(event) {
      if (event.source == window &&
          event.data &&
          event.data.direction == "from-page-script") {
        alert("Content script received message: \"" + event.data.message + "\"");
      }
    });

For a complete working example of this, [visit the demo page on
GitHub](https://mdn.github.io/webextensions-examples/content-script-page-
script-messaging.html) and follow the instructions.

Note that any time you interact with untrusted web content on this way, you
need to be very careful. Extensions are privileged code which can have
powerful capabilities, and hostile web pages can easily trick them into
accessing those capabilities.

To make a trivial example, suppose the content script code that receives the
message does something like this:

    
    
    // content-script.js
    
    window.addEventListener("message", function(event) {
      if (event.source == window &&
          event.data.direction &&
          event.data.direction == "from-page-script") {
        eval(event.data.message);
      }
    });

Now the page script can run any code with all the privileges of the content
script.

## Sharing objects with page scripts

The techniques described in this section are only available in Firefox, and
only from Firefox 49 onwards.

As an extension developer you should consider that scripts running in
arbitrary web pages are hostile code whose aim is to steal the user's personal
information, damage their computer, or attack them in some other way.

The isolation between content scripts and scripts loaded by web pages is
intended to make it more difficult for hostile web pages to do this.

Since the techniques described in this section break down that isolation, they
are inherently dangerous and should be used with great care.

We saw in [DOM access](/en-US/Add-
ons/WebExtensions/Content_scripts#DOM_access) that content scripts don't see
changes made to the DOM by scripts loaded by web pages. This means that, for
example, if a web page loads a library like jQuery, content scripts won't be
able to use it, and have to load their own copy. Conversely, scripts loaded by
web pages can't see changes made by content scripts.

However, Firefox provides some APIs that enable content scripts to:

  * access JavaScript objects created by page scripts
  * expose their own JavaScript objects to page scripts.

### Xray vision in Firefox

In Firefox, part of the isolation between content scripts and page scripts is
implemented using a feature called "Xray vision". When a script in a more-
privileged scope accesses an object that's defined in a less-privileged scope
it sees only the "native version" of the object. Any [expando](/en-
US/docs/Glossary/Expando) properties are invisible, and if any properties of
the object have been redefined, it sees the original implementation, not the
redefined version.

The purpose of this feature is to make it harder for the less-privileged
script to confuse the more-privileged script by redefining the native
properties of objects.

So for example, when a content script accesses the page's [window](/en-
US/docs/Web/API/Window), it won't see any properties the page script added to
the window, and if the page script has redefined any existing properties of
the window, the content script will see the original version.

For the full story on Xray vision, see the articles on [Xray vision](/en-
US/docs/Mozilla/Tech/Xray_vision) and [Script security](/en-
US/docs/Mozilla/Gecko/Script_security).

### Accessing page script objects from content scripts

In Firefox, DOM objects in content scripts get an extra property
`wrappedJSObject`. This is an "unwrapped" version of the object, which
includes any changes made to that object by any page scripts.

Let's take a simple example. Suppose a web page loads a script:

    
    
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
      </head>
      <body>
        <script type="text/javascript" src="main.js"></script>
      </body>
    </html>

The script adds an expando property to the global `window`:

    
    
    // main.js
    
    var foo = "I'm defined in a page script!";

Xray vision means that if a content script tries to access `foo`, it will be
undefined:

    
    
    // content-script.js
    
    console.log(window.foo); // undefined

In Firefox, content scripts can use `window.wrappedJSObject` to see the
expando property:

    
    
    // content-script.js
    
    console.log(window.wrappedJSObject.foo); // "I'm defined in a page script!"

Note that once you do this, you can no longer rely on any of this object's
properties or functions being, or doing, what you expect. Any of them, even
setters and getters, could have been redefined by untrusted code.

Also note that unwrapping is transitive: when you use `wrappedJSObject`, any
properties of the unwrapped object are themselves unwrapped (and therefore
unreliable). So it's good practice, once you've got the object you need, to
rewrap it, which you can do like this:

    
    
    XPCNativeWrapper(window.wrappedJSObject.foo);

See the document on [Xray vision](/en-US/docs/Mozilla/Tech/Xray_vision) for
much more detail on this.

### Sharing content script objects with page scripts

Firefox also provides APIs enabling content scripts to make objects available
to page scripts. There are two main APIs here:

  * `[exportFunction()](/en-US/Add-ons/WebExtensions/Content_scripts#exportFunction)`: export a function to page scripts.
  * `[cloneInto()](/en-US/Add-ons/WebExtensions/Content_scripts#cloneInto)`: export an object to page scripts.

#### exportFunction

Given a function defined in the content script, `exportFunction()` exports it
to the page script's scope, so the page script can call it.

For example, let's consider an extension which has a background script like
this:

    
    
    /*
    Execute content script in the active tab.
    */
    function loadContentScript() {
      browser.tabs.executeScript({
        file: "/content_scripts/export.js"
      });
    }
    
    /*
    Add loadContentScript() as a listener to clicks
    on the browser action.
    */
    browser.browserAction.onClicked.addListener(loadContentScript);
    
    /*
    Show a notification when we get messages from
    the content script.
    */
    browser.runtime.onMessage.addListener((message) => {
      browser.notifications.create({
        type: "basic",
        title: "Message from the page",
        message: message.content
      });
    });

This does two things:

  * execute a content script in the current tab, when the user clicks a browser action
  * listen for messages from the content script, and display a [notification](/en-US/Add-ons/WebExtensions/API/notifications) when the message arrives.

The content script looks like this:

    
    
    /*
    Define a function in the content script's scope, then export it
    into the page script's scope.
    */
    function notify(message) {
      browser.runtime.sendMessage({content: "Function call: " + message});
    }
    
    exportFunction(notify, window, {defineAs:'notify'});

This defines a function `notify()`, which just sends its argument to the
background script. It then exports the function to the page script's scope.
Now the page script can call this function:

    
    
    window.notify("Message from the page script!");

For the full story, see `[Components.utils.exportFunction](/en-
US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.exportFunction)`.

#### cloneInto

Given an object defined in the content script, this creates a clone of the
object in the page script's scope, thereby making the clone accessible to page
scripts. By default, this uses the [structured clone algorithm](/en-
US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) to clone the
object, meaning that functions in the object are not included in the clone. To
include functions, pass the `cloneFunctions` option.

For example, here's a content script that defines an object that contains a
function, then clones it into the page script's scope:

    
    
    /*
    Create an object that contains functions in
    the content script's scope, then clone it
    into the page script's scope.
    
    Because the object contains functions,
    the cloneInto call must include
    the `cloneFunctions` option.
    */
    var messenger = {
      notify: function(message) {
        browser.runtime.sendMessage({
          content: "Object method call: " + message
        });
      }
    };
    
    window.wrappedJSObject.messenger = cloneInto(
      messenger,
      window,
      {cloneFunctions: true});

Now page scripts will see a new property on the window, `messenger`, which has
a function `notify()`:

    
    
    window.messenger.notify("Message from the page script!");

For the full story, see `[Components.utils.cloneInto](/en-
US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.cloneInto)`.

## Using eval() in content scripts

In Chrome, `[eval()](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/eval)` always runs code in the
context of the content script, not in the context of the page.

In Firefox:

  * if you call `eval()`, it runs code in the context of the content script
  * if you call `window.eval()`, it runs code in the context of the page.

For example, consider a content script like this:

    
    
    // content-script.js
    
    window.eval('window.x = 1;');
    eval('window.y = 2');
    
    console.log(`In content script, window.x: ${window.x}`);
    console.log(`In content script, window.y: ${window.y}`);
    
    window.postMessage({
      message: "check"
    }, "*");

This code just creates some variables x and y using `window.eval()` and
`eval()`, then logs their values, then messages the page.

On receiving the message, the page script logs the same variables:

    
    
    window.addEventListener("message", function(event) {
      if (event.source === window && event.data && event.data.message === "check") {
        console.log(`In page script, window.x: ${window.x}`);
        console.log(`In page script, window.y: ${window.y}`);
      }
    });

In Chrome, this will produce output like this:

    
    
    In content script, window.x: 1
    In content script, window.y: 2
    In page script, window.x: undefined
    In page script, window.y: undefined

In Firefox the following output is produced:

    
    
    In content script, window.x: undefined
    In content script, window.y: 2
    In page script, window.x: 1
    In page script, window.y: undefined

The same applies to `[setTimeout()](/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)`, `[setInterval()](/en-
US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)`, and `[Function
()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)`.

When running code in the context of the page, the warning in the "[Sharing
content script objects with page scripts](/en-US/Add-
ons/WebExtensions/Content_scripts#Sharing_objects_with_page_scripts)" section
above applies: the page's environment is controlled by potentially malicious
web pages, which can redefine objects you interact with to behave in
unexpected ways:

    
    
    // page.js redefines console.log
    
    var original = console.log;
    
    console.log = function() {
      original(true);
    }
    
    
    
    // content-script.js calls the redefined version
    
    window.eval('console.log(false)');
    

