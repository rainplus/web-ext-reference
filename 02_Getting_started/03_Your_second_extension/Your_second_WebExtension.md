[\n

\n

If you've been through the [Your first extension](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Your_first_WebExtension) article, you've already got an idea
of how to write a extension. In this article we'll write a slightly more
complex extension that demonstrates a few more of the APIs.

\n

The extension adds a new button to the Firefox toolbar. When the user clicks
the button, we display a popup enabling them to choose an animal. Once they
choose an animal, we'll replace the current page's content with a picture of
the chosen animal.

\n

To implement this, we will:

\n

\n

  *  **define a[browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action), which is a button attached to the Firefox toolbar**.  
\n For the button we'll supply:\n \n

    * an icon, called "beasts-32.png"
\n

    * a popup to open when the button is pressed. The popup will include HTML, CSS, and JavaScript.
\n\n

\n

  *  **define an icon for the extension** , called "beasts-48.png". This will be shown in the Add-ons Manager.
\n

  *  **write a content script, "beastify.js" that will be injected into web pages**.  
\n This is the code that will actually modify the pages.

\n

  *  **package some images of the animals, to replace images in the web page**.  
\n We'll make the images "web accessible resources" so the web page can refer
to them.

\n

\n

You could visualise the overall structure of the extension like this:

\n

![](https://mdn.mozillademos.org/files/13671/Untitled-1.png)

\n

It's a simple extension, but shows many of the basic concepts of the
WebExtensions API:

\n

\n

  * adding a button to the toolbar
\n

  * defining a popup panel using HTML, CSS, and JavaScript
\n

  * injecting content scripts into web pages
\n

  * communicating between content scripts and the rest of the extension
\n

  * packaging resources with your extension that can be used by web pages
\n

\n

You can find [complete source code for the extension on
GitHub](https://github.com/mdn/webextensions-examples/tree/master/beastify).

\n

To write this extension, you'll need Firefox 45 or newer.

\n

## Writing the extension

\n

Create a new directory and navigate to it:

\n

    
    
    mkdir beastify\ncd beastify

\n

### manifest.json

\n

Now create a new file called "manifest.json", and give it the following
contents:

\n

    
    
    {\n\n  "manifest_version": 2,\n  "name": "Beastify",\n  "version": "1.0",\n\n  "description": "Adds a browser action icon to the toolbar. Click the button to choose a beast. The active tab's body content is then replaced with a picture of the chosen beast. See https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Examples#beastify",\n  "homepage_url": "https://github.com/mdn/webextensions-examples/tree/master/beastify",\n  "icons": {\n    "48": "icons/beasts-48.png"\n  },\n\n  "permissions": [\n    "activeTab"\n  ],\n\n  "browser_action": {\n    "default_icon": "icons/beasts-32.png",\n    "default_title": "Beastify",\n    "default_popup": "popup/choose_beast.html"\n  },\n\n  "web_accessible_resources": [\n    "beasts/frog.jpg",\n    "beasts/turtle.jpg",\n    "beasts/snake.jpg"\n  ]\n\n}\n

\n

\n

  * The first three keys: `[manifest_version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/manifest_version)`, `[name](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/name)`, and `[version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version)`, are mandatory and contain basic metadata for the extension.
\n

  * `[description](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/description)` and `[homepage_url](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/homepage_url)` are optional, but recommended: they provide useful information about the extension.
\n

  * `[icons](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/icons)` is optional, but recommended: it allows you to specify an icon for the extension, that will be shown in the Add-ons Manager.
\n

  * `[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)` lists permissions the extension needs. We're just asking for the [`activeTab` permission](/en-US/Add-ons/WebExtensions/manifest.json/permissions#activeTab_permission) here.
\n

  * `[browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)` specifies the toolbar button. We're supplying three pieces of information here:\n \n
    * `default_icon` is mandatory, and points to the icon for the button
\n

    * `default_title` is optional, and will be shown in a tooltip
\n

    * `default_popup` is used if you want a popup to be shown when the user clicks the button. We do, so we've included this key and made it point to an HTML file included with the extension.
\n\n

\n

  * `[web_accessible_resources](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/web_accessible_resources)` lists files that we want to make accessible to web pages. Since the extension replaces the content in the page with images we've packaged with the extension, we need to make these images accessible to the page.
\n

\n

Note that all paths given are relative to manifest.json itself.

\n

### The icon

\n

The extension should have an icon. This will be shown next to the extension's
listing in the Add-ons Manager (you can open this by visiting the URL
"about:addons"). Our manifest.json promised that we would have an icon for the
toolbar at "icons/beasts-48.png".

\n

Create the "icons" directory and save an icon there named "beasts-48.png".\xa0
You could use [the one from our example](https://github.com/mdn/webextensions-
examples/blob/master/beastify/icons/beasts-48.png), which is taken from
the\xa0[Aha-Soft\u2019s Free Retina
iconset](https://www.iconfinder.com/iconsets/free-retina-icon-set), and used
under the terms of its [license](http://www.aha-soft.com/free-icons/free-
retina-icon-set/).

\n

If you choose to supply your own icon, It should be 48x48 pixels. You could
also supply a 96x96 pixel icon, for high-resolution displays, and if you do
this it will be specified as the `96` property of the `icons` object in
manifest.json:

\n

    
    
    "icons": {\n  "48": "icons/beasts-48.png",\n  "96": "icons/beasts-96.png"\n}

\n

### The toolbar button

\n

The toolbar button also needs an icon, and our manifest.json promised that we
would have an icon for the toolbar at "icons/beasts-32.png".

\n

Save an icon named "beasts-32.png" in the "icons" directory. You could use
[the one from our example](https://github.com/mdn/webextensions-
examples/blob/master/beastify/icons/beasts-32.png), which is taken from the
[IconBeast Lite icon set](http://www.iconbeast.com/free) and used under the
terms of its [license](http://www.iconbeast.com/faq/).

\n

If you don't supply a popup, then a click event is dispatched to your
extension when the user clicks the button. If you do supply a popup, the click
event is not dispatched, but instead, the popup is opened. We want a popup, so
let's create that next.

\n

### The popup

\n

The function of the popup is to enable the user to choose one of three beasts.

\n

Create a new directory called "popup" under the extension root. This is where
we'll keep the code for the popup. The popup will consist of three files:

\n

\n

  *  **`choose_beast.html`** defines the content of the panel
\n

  *  **`choose_beast.css`** styles the content
\n

  *  **`choose_beast.js`** handles the user's choice by running a content script in the active tab
\n

\n

    
    
    mkdir popup \ncd popup\ntouch choose_beast.html choose_beast.css choose_beast.js \n

\n

#### choose_beast.html

\n

The HTML file looks like this:

\n

    
    
    <!DOCTYPE html>\n\n<html>\n  <head>\n    <meta charset="utf-8">\n    <link rel="stylesheet" href="choose_beast.css"/>\n  </head>\n\n<body>\n  <div id="popup-content">\n    <div class="button beast">Frog</div>\n    <div class="button beast">Turtle</div>\n    <div class="button beast">Snake</div>\n    <div class="button reset">Reset</div>\n  </div>\n  <div id="error-content" class="hidden">\n    <p>Can't beastify this web page.</p><p>Try a different page.</p>\n  </div>\n  <script src="choose_beast.js"></script>\n</body>\n\n</html>\n

\n

We have a `[<div>](/en-US/docs/Web/HTML/Element/div)` element with an ID of
`"popup-content"` that contains an element for each animal choice. We have
another `<div>` with an ID of `"error-content"` and a class `"hidden"`. We'll
use that in case there's a problem initializing the popup.

\n

Note that we include the CSS and JS files from this file, just like a web
page.

\n

#### choose_beast.css

\n

The CSS fixes the size of the popup, ensures that the three choices fill the
space, and gives them some basic styling. It also hides elements with
`class="hidden"`: this means that our `"error-content"` `<div>` will be hidden
by default.

\n

    
    
    html, body {\n  width: 100px;\n}\n\n.hidden {\n  display: none;\n}\n\n.button {\n  margin: 3% auto;\n  padding: 4px;\n  text-align: center;\n  font-size: 1.5em;\n  cursor: pointer;\n}\n\n.beast:hover {\n  background-color: #CFF2F2;\n}\n\n.beast {\n  background-color: #E5F2F2;\n}\n\n.reset {\n  background-color: #FBFBC9;\n}\n\n.reset:hover {\n  background-color: #EAEA9D;\n}\n\n

\n

#### choose_beast.js

\n

Here's the JavaScript for the popup:

\n

    
    
    /**\n * CSS to hide everything on the page,\n * except for elements that have the "beastify-image" class.\n */\nconst hidePage = `body > :not(.beastify-image) {\n                    display: none;\n                  }`;\n\n/**\n * Listen for clicks on the buttons, and send the appropriate message to\n * the content script in the page.\n */\nfunction listenForClicks() {\n  document.addEventListener("click", (e) => {\n\n    /**\n     * Given the name of a beast, get the URL to the corresponding image.\n     */\n    function beastNameToURL(beastName) {\n      switch (beastName) {\n        case "Frog":\n          return browser.extension.getURL("beasts/frog.jpg");\n        case "Snake":\n          return browser.extension.getURL("beasts/snake.jpg");\n        case "Turtle":\n          return browser.extension.getURL("beasts/turtle.jpg");\n      }\n    }\n\n    /**\n     * Insert the page-hiding CSS into the active tab,\n     * then get the beast URL and\n     * send a "beastify" message to the content script in the active tab.\n     */\n    function beastify(tabs) {\n      browser.tabs.insertCSS({code: hidePage}).then(() => {\n        let url = beastNameToURL(e.target.textContent);\n        browser.tabs.sendMessage(tabs[0].id, {\n          command: "beastify",\n          beastURL: url\n        });\n      });\n    }\n\n    /**\n     * Remove the page-hiding CSS from the active tab,\n     * send a "reset" message to the content script in the active tab.\n     */\n    function reset(tabs) {\n      browser.tabs.removeCSS({code: hidePage}).then(() => {\n        browser.tabs.sendMessage(tabs[0].id, {\n          command: "reset",\n        });\n      });\n    }\n\n    /**\n     * Just log the error to the console.\n     */\n    function reportError(error) {\n      console.error(`Could not beastify: ${error}`);\n    }\n\n    /**\n     * Get the active tab,\n     * then call "beastify()" or "reset()" as appropriate.\n     */\n    if (e.target.classList.contains("beast")) {\n      browser.tabs.query({active: true, currentWindow: true})\n        .then(beastify)\n        .catch(reportError);\n    }\n    else if (e.target.classList.contains("reset")) {\n      browser.tabs.query({active: true, currentWindow: true})\n        .then(reset)\n        .catch(reportError);\n    }\n  });\n}\n\n/**\n * There was an error executing the script.\n * Display the popup's error message, and hide the normal UI.\n */\nfunction reportExecuteScriptError(error) {\n  document.querySelector("#popup-content").classList.add("hidden");\n  document.querySelector("#error-content").classList.remove("hidden");\n  console.error(`Failed to execute beastify content script: ${error.message}`);\n}\n\n/**\n * When the popup loads, inject a content script into the active tab,\n * and add a click handler.\n * If we couldn't inject the script, handle the error.\n */\nbrowser.tabs.executeScript({file: "/content_scripts/beastify.js"})\n.then(listenForClicks)\n.catch(reportExecuteScriptError);\n\n

\n

The place to start here is line 96. The popup script executes a content script
in the active tab as soon as the popup is loaded, using the
`[browser.tabs.executeScript()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/executeScript)` API. If executing the content
script is successful, then the content script will stay loaded in the page
until the tab is closed or the user navigates to a different page.

\n

A common reason the `browser.tabs.executeScript()` call might fail is that you
can't execute content scripts in all pages. For example, you can't execute
them in privileged browser pages like about:debugging, and you can't execute
them on pages in the [addons.mozilla.org](https://addons.mozilla.org/) domain.
If it does fail, `reportExecuteScriptError()` will hide the `"popup-content"`
`<div>`, show the `"error-content"` `<div>`, and log an error to the [console
](/en-US/Add-ons/WebExtensions/Debugging).

\n

If executing the content script is successful, we call `listenForClicks()`.
This listens for clicks on the popup.

\n

\n

  * If the click was on a button with `class="beast"`, then we call `beastify()`.
\n

  * If the click was on a button with `class="reset"`, then we call `reset()`.
\n

\n

The `beastify()` function does three things:

\n

\n

  * map the button clicked to a URL pointing to an image of a particular beast
\n

  * hide the page's whole content by injecting some CSS, using the\xa0`[browser.tabs.insertCSS()](/en-US/Add-ons/WebExtensions/API/tabs/insertCSS)` API
\n

  * send a "beastify" message to the content script using the `[browser.tabs.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage)` API, asking it to beastify the page, and passing it the URL to the beast image.
\n

\n

The `reset()` function essentially undoes a beastify:

\n

\n

  * remove the CSS we added, using the\xa0`[browser.tabs.removeCSS()](/en-US/Add-ons/WebExtensions/API/tabs/removeCSS)` API
\n

  * send a "reset" message to the content script asking it to reset the page.
\n

\n

### The content script

\n

Create a new directory, under the extension root, called "content_scripts" and
create a new file in it called "beastify.js", with the following contents:

\n

    
    
    (function() {\n  /**\n   * Check and set a global guard variable.\n   * If this content script is injected into the same page again,\n   * it will do nothing next time.\n   */\n  if (window.hasRun) {\n    return;\n  }\n  window.hasRun = true;\n\n  /**\n   * Given a URL to a beast image, remove all existing beasts, then\n   * create and style an IMG node pointing to\n   * that image, then insert the node into the document.\n   */\n  function insertBeast(beastURL) {\n    removeExistingBeasts();\n    let beastImage = document.createElement("img");\n    beastImage.setAttribute("src", beastURL);\n    beastImage.style.height = "100vh";\n    beastImage.className = "beastify-image";\n    document.body.appendChild(beastImage);\n  }\n\n  /**\n   * Remove every beast from the page.\n   */\n  function removeExistingBeasts() {\n    let existingBeasts = document.querySelectorAll(".beastify-image");\n    for (let beast of existingBeasts) {\n      beast.remove();\n    }\n  }\n\n  /**\n   * Listen for messages from the background script.\n   * Call "beastify()" or "reset()".\n  */\n  browser.runtime.onMessage.addListener((message) => {\n    if (message.command === "beastify") {\n      insertBeast(message.beastURL);\n    } else if (message.command === "reset") {\n      removeExistingBeasts();\n    }\n  });\n\n})();\n

\n

The first thing the content script does is to check for a global variable
`window.hasRun`: if it's set the script returns early, otherwise it sets
`window.hasRun` and continues. The reason we do this is that every time the
user opens the popup, the popup executes a content script in the active tab,
so we could have multiple instances of the script running in a single tab. If
this happens, we need to make sure that only the first instance is actually
going to do anything.

\n

After that, the place to start is line 40, where the content script listens
for messages from the popup, using the `[browser.runtime.onMessage](/en-US
/Add-ons/WebExtensions/API/runtime/onMessage)` API. We saw above that the
popup script can send two different sorts of messages: "beastify" and "reset".

\n

\n

  * if the message is "beastify", we expect it to contain a URL pointing to a beast image. We remove any beasts that might have been added by previous "beastify" calls, then construct and append an `[<img>](/en-US/docs/Web/HTML/Element/img)` element whose `src` attribute is set to the beast URL.
\n

  * if the message is "reset", we just remove any beasts that might have been added.
\n

\n

### The beasts

\n

Finally, we need to include the images of the beasts.

\n

Create a new directory called "beasts", and add the three images in that
directory, with the appropriate names. You can get the images from [the GitHub
repository](https://github.com/mdn/webextensions-
examples/tree/master/beastify/beasts), or from here:

\n

![](https://mdn.mozillademos.org/files/11459/frog.jpg)![](https://mdn.mozillademos.org/files/11461/snake.jpg)![](https://mdn.mozillademos.org/files/11463/turtle.jpg)

\n

## Testing it out

\n

First, double check that you have the right files in the right places:

\n

    
    
    beastify/\n\n    beasts/\n        frog.jpg\n        snake.jpg\n        turtle.jpg\n\n    content_scripts/\n        beastify.js\n\n    icons/\n        beasts-32.png\n        beasts-48.png\n\n    popup/\n        choose_beast.css\n        choose_beast.html\n        choose_beast.js\n\n    manifest.json

\n

Starting in Firefox 45, you can install extensions temporarily from disk.

\n

Open "about:debugging" in Firefox, click "Load Temporary Add-on", and select
your manifest.json file. You should then see the extension's icon appear in
the Firefox toolbar:

\n

\n

Open a web page, then click the icon, select a beast, and see the web page
change:

\n

\n

## Developing from the command line

\n

You can automate the temporary installation step by using the [web-ext](/en-US
/Add-ons/WebExtensions/Getting_started_with_web-ext) tool. Try this:

\n

    
    
    cd beastify\nweb-ext run

\n

\n]

