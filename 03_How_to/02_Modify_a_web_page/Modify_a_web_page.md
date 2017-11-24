[\n

\n

One of the most common use cases for an extension is to modify a web page. For
example, an extension might want to change the style applied to a page, hide
particular DOM nodes, or inject extra DOM nodes into the page.

\n

There are two ways to do this with WebExtensions APIs:

\n

\n

  *  **Declaratively** : Define a pattern than matches a set of URLs, and load a set of scripts into pages whose URL matches that pattern.
\n

  *  **Programmatically** : Using a JavaScript API, load a script into the page hosted by a particular tab.
\n

\n

Either way, these scripts are called _content scripts_ , and are different
from the other scripts that make up an extension:

\n

\n

  * They only get access to a small subset of the WebExtension APIs.
\n

  * They get direct access to the web page in which they are loaded.
\n

  * They communicate with the rest of the extension using a messaging API.
\n

\n

In this article we'll look at both methods of loading a script.

\n

## Modifying pages that match a URL pattern

\n

First of all, create a new directory called "modify-page". In that directory,
create a file called "manifest.json", with the following contents:

\n

    
    
    {\n\n  "manifest_version": 2,\n  "name": "modify-page",\n  "version": "1.0",\n\n  "content_scripts": [\n    {\n      "matches": ["https://developer.mozilla.org/*"],\n      "js": ["page-eater.js"]\n    }\n  ]\n\n}

\n

The `[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)` key is how you load scripts
into pages that match URL patterns. In this case, `content_scripts` instructs
the browser to load a script called "page-eater.js" into all pages under
<https://developer.mozilla.org/>.

\n

\n

Since the `"js"` property of `content_scripts` is an array, you can use it to
inject more than one script into matching pages. If you do this the pages
share the same scope, just like multiple scripts loaded by a page, and they
are loaded in the order that they are listed in the array.

\n

\n

\n

The `content_scripts` key also has a `"css"` property that you can use to
inject CSS stylesheets.

\n

\n

Next, create a file called "page-eater.js" inside the "modify-page" directory,
and give it the following contents:

\n

    
    
    document.body.textContent = "";\n\nvar header = document.createElement('h1');\nheader.textContent = "This page has been eaten";\ndocument.body.appendChild(header);

\n

Now [install the extension](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox), and visit
<https://developer.mozilla.org/>:

\n

\n

\n

Note that although this video shows the content script working in
[addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/), content
scripts are currently blocked for this site.

\n

\n

## Modifying pages programmatically

\n

What if you still want to eat pages, but only when the user asks you to? Let's
update this example so we inject the content script when the user clicks a
context menu item.

\n

First, update "manifest.json" so it has the following contents:

\n

    
    
    {\n\n  "manifest_version": 2,\n  "name": "modify-page",\n  "version": "1.0",\n\n  "permissions": [\n    "activeTab",\n    "contextMenus"\n  ],\n\n  "background": {\n    "scripts": ["background.js"]\n  }\n\n}

\n

Here, we've removed the `content_scripts` key, and added two new keys:

\n

\n

  * `[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)`: To inject scripts into pages we need permissions for the page we're modifying. The [`activeTab` permission](/en-US/Add-ons/WebExtensions/manifest.json/permissions#activeTab_permission) is a way to get this temporarily for the currently active tab. We also need the `contextMenus` permission to be able to add context menu items.
\n

  * `[background](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/background)`: We're using this to load a persistent ["background script"](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts) called "background.js", in which we'll set up the context menu and inject the content script.
\n

\n

Let's create this file. Create a new file called "background.js" in the
"modify-page" directory, and give it the following contents:

\n

    
    
    browser.contextMenus.create({\n  id: "eat-page",\n  title: "Eat this page"\n});\n\nbrowser.contextMenus.onClicked.addListener(function(info, tab) {\n  if (info.menuItemId == "eat-page") {\n    browser.tabs.executeScript({\n      file: "page-eater.js"\n    });\n  }\n});\n

\n

In this script we're creating a [context menu item](/en-US/Add-
ons/WebExtensions/API/ContextMenus/create), giving it a specific id and title
(the text to be displayed in the context menu). Then we set up an event
listener so that when the user clicks a context menu item, we check to see if
it is our `eat-page` item. If it is, we inject "page-eater.js" into the
current tab using the `[tabs.executeScript()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/executeScript)` API. This API optionally takes a
tab ID as an argument: we've omitted the tab ID, which means that the script
is injected into the currently active tab.

\n

At this point the extension should look like this:

\n

    
    
    modify-page/\n    background.js\n    manifest.json\n    page-eater.js

\n

Now [reload the extension](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox#Reloading_a_temporary_add-
on), open a page (any page, this time) activate the context menu, and select
"Eat this page":

\n

\n

\n

Note that although this video shows the content script working in
[addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/), content
scripts are currently blocked for this site.

\n

\n

## Messaging

\n

Content scripts and background scripts can't directly access each other's
state. However, they can communicate by sending messages. One end sets up a
message listener, and the other end can then send it a message. The following
table summarises the APIs involved on each side:

\n\n\n\n\xa0\n| In content script\n| In background script\n  
---|---|---  
\n\nSend a message\n| `[browser.runtime.sendMessage()](/en-US/Add-
ons/WebExtensions/API/runtime#sendMessage\(\))`\n| `[browser.tabs.sendMessage
()](/en-US/Add-ons/WebExtensions/API/Tabs/sendMessage)`\n  
\n\nReceive a message\n| `[browser.runtime.onMessage](/en-US/Add-
ons/WebExtensions/API/runtime/onMessage)`\n| `[browser.runtime.onMessage](/en-
US/Add-ons/WebExtensions/API/runtime#onMessage)`\n  
\n\n\n

Let's update our example to show how to send a message from the background
script.

\n

First, edit "background.js" so that it has these contents:

\n

    
    
    browser.contextMenus.create({\n  id: "eat-page",\n  title: "Eat this page"\n});\n\nfunction messageTab(tabs) {\n  browser.tabs.sendMessage(tabs[0].id, {\n    replacement: "Message from the extension!"\n  });\n}\n\nfunction onExecuted(result) {\n\xa0\xa0\xa0 var querying = browser.tabs.query({\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 active: true,\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 currentWindow: true\n\xa0\xa0\xa0 });\n\xa0\xa0\xa0 querying.then(messageTab);\n}\n\nbrowser.contextMenus.onClicked.addListener(function(info, tab) {\n  if (info.menuItemId == "eat-page") {\n    let executing = browser.tabs.executeScript({\n      file: "page-eater.js"\n    });\n    executing.then(onExecuted);\n  }\n});\n

\n

Now, after injecting "page-eater.js", we use `[tabs.query()](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query)` to get the currently
active tab, and then use `[tabs.sendMessage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage)` to send a message to the content
scripts loaded into that tab. The message has the payload `{replacement:
"Message from the extension!"}`.

\n

Next, update "page-eater.js" like this:

\n

    
    
    function eatPageReceiver(request, sender, sendResponse) {\n  document.body.textContent = "";\n  var header = document.createElement('h1');\n  header.textContent = request.replacement;\n  document.body.appendChild(header);\n}\nbrowser.runtime.onMessage.addListener(eatPageReceiver);\n

\n

Now instead of just eating the page right away, the content script listens for
a message using `[runtime.onMessage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onMessage)`. When a message arrives, the content
script runs essentially the same code as before, except that the replacement
text is taken from `request.replacement`.

\n

Since `[tabs.executeScript()](/en-US/Add-
ons/WebExtensions/API/tabs/executeScript)` is an asynchronous function, and to
ensure we send message only after listener has been added in "page-eater.js",
we use `onExecuted` which will be called after "page-eater.js" executed.

\n

\n

Press Ctrl+Shift+J (or Cmd+Shift+J on a Mac) OR `web-ext run --bc` to open
[Browser Console](/en-US/docs/Tools/Browser_Console) to view `console.log` in
background script. Alternatively use [Add-on Debugger](/en-US/Add-ons/Add-
on_Debugger)\xa0 which allows you set breakpoint. There is currently no way to
[start Add-on Debugger directly from web-ext](https://github.com/mozilla/web-
ext/issues/759).

\n

\n

If we want send messages back from the content script to the background
page,\xa0 we would use `[runtime.sendMessage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendMessage)` instead of `[tabs.sendMessage
()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage)`, e.g.:

\n

    
    
    browser.runtime.sendMessage({\n    title: "from page-eater.js"\n});

\n

\n

These examples all inject JavaScript; you can also inject CSS programmatically
using the `[tabs.insertCSS()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/insertCSS)` function.

\n

\n

## Learn more

\n

\n

  * [Content scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts) guide
\n

  * `[content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)` manifest key
\n

  * `[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)` manifest key
\n

  * `[tabs.executeScript()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript)`
\n

  * `[tabs.insertCSS()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/insertCSS)`
\n

  * `[tabs.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage)`
\n

  * `[runtime.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage)`
\n

  * `[runtime.onMessage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`
\n

  * Examples using `content_scripts`:\n \n
    * [borderify](https://github.com/mdn/webextensions-examples/tree/master/borderify)
\n

    * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)
\n

    * [page-to-extension-messaging](https://github.com/mdn/webextensions-examples/tree/master/page-to-extension-messaging)
\n\n

\n

  * Examples using `tabs.executeScript()`:\n \n
    * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
\n

    * [context-menu-demo](https://github.com/mdn/webextensions-examples/tree/master/context-menu-demo)
\n\n

\n

\n

\xa0

\n]

