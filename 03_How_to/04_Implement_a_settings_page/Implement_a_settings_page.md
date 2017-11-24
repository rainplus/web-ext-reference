[\n

\n

A settings page gives users a way to see and change settings (sometimes also
called "preferences" or "options") for the extension.

\n

With WebExtension APIs, settings are generally stored using the `[storage
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API. Implementing a
settings page is a three-step process:

\n

\n

  * Write an HTML file that displays settings and lets the user change them.
\n

  * Write a script, included from the HTML file, that populates the settings page from storage and updates stored settings when the user changes them.
\n

  * Set the path to the HTML file as the `[options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)` key in manifest.json. By doing this, the HTML document will be shown in the browser's add-on manager, alongside the extension's name and description.
\n

\n

\n

You can also open this page programmatically using the
`[runtime.openOptionsPage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage)` function.

\n

\n

## A simple extension

\n

First, we'll write an extension that adds a blue border to every page the user
visits.

\n

Create a new directory called "settings", then create a file called
"manifest.json" inside it with the following contents:

\n

    
    
    {\n\n  "manifest_version": 2,\n  "name": "Settings example",\n  "version": "1.0",\n\n  "content_scripts": [\n    {\n      "matches": ["<all_urls>"],\n      "js": ["borderify.js"]\n    }\n  ]\n\n}

\n

This extension instructs the browser to load a content script called
"borderify.js" into all web pages the user visits.

\n

Next, create a file called "borderify.js" inside the "settings" directory, and
give it these contents:

\n

    
    
    document.body.style.border = "10px solid blue";

\n

This just adds a blue border to the page.

\n

Now [install the extension](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox) and test it \u2014 open
up any web page you like:

\n

\n

## Adding settings

\n

Now let's create a settings page to allow the user to set the color of the
border.

\n

First, update "manifest.json" so it has these contents:

\n

    
    
    {\n\n  "manifest_version": 2,\n  "name": "Settings example",\n  "version": "1.0",\n\n  "content_scripts": [\n    {\n      "matches": ["<all_urls>"],\n      "js": ["borderify.js"]\n    }\n  ],\n\n  "options_ui": {\n    "page": "options.html"\n  },\n\n  "permissions": ["storage"]\n\n}\n

\n

We've added two new manifest keys:

\n

\n

  * `[options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)`: This sets an HTML document to be the settings page (also called options page) for this extension.
\n

  * `[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)`: We'll use the `[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API to store the settings, and we need to ask permission to use this API.
\n

\n

Next, because we've promised to provide "options.html", let's create it.
Create a file with that name inside the "settings" directory, and give it the
following contents:

\n

    
    
    <!DOCTYPE html>\n\n<html>\n  <head>\n    <meta charset="utf-8">\n  </head>\n\n  <body>\n\n    <form>\n        <label>Border color<input type="text" id="color" ></label>\n        <button type="submit">Save</button>\n    </form>\n\n    <script src="options.js"></script>\n\n  </body>\n\n</html>\n

\n

This defines a [`<form>`](/en-US/docs/Web/HTML/Element/form "The HTML <form>
element represents a document section that contains interactive controls to
submit information to a web server.") with a labeled text [`<input>`](/en-
US/docs/Web/HTML/Element/input "The HTML <input> element is used to create
interactive controls for web-based forms in order to accept data from the
user.") and a submit [`<button>`](/en-US/docs/Web/HTML/Element/button "The
HTML <button> element represents a clickable button."). It also includes a
script called "options.js".

\n

Create "options.js", again in the "settings" directory, and give it the
following contents:

\n

    
    
    function saveOptions(e) {\n  e.preventDefault();\n  browser.storage.local.set({\n    color: document.querySelector("#color").value\n  });\n}\n\nfunction restoreOptions() {\n\n  function setCurrentChoice(result) {\n    document.querySelector("#color").value = result.color || "blue";\n  }\n\n  function onError(error) {\n    console.log(`Error: ${error}`);\n  }\n\n  var getting = browser.storage.local.get("color");\n  getting.then(setCurrentChoice, onError);\n}\n\ndocument.addEventListener("DOMContentLoaded", restoreOptions);\ndocument.querySelector("form").addEventListener("submit", saveOptions);\n

\n

This does two things:

\n

\n

  * When the document has loaded, it fetches the value of "color" from storage using `[storage.local.get()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/StorageArea/get)`. If the value isn't set, it uses the default "blue".
\n

  * When the user submits the form by clicking "Save", it stores the value of the textbox using `[storage.local.set()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/StorageArea/set)`.
\n

\n

Finally, update "borderify.js" to read the border color from storage:

\n

\n

Due to a bug in [browser.storage.local.get()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/StorageArea/get) in Firefox versions prior to
52, the following code will not function. To make it function in Firefox
versions below 52, the two occurrences of `item.color` in `onGot()` must be
changed to `item[0].color`.

\n

\n

    
    
     function onError(error) {\n  console.log(`Error: ${error}`);\n}\n\nfunction onGot(item) {\n  var color = "blue";\n  if (item.color) {\n    color = item.color;\n  }\n  document.body.style.border = "10px solid " + color;\n}\n\nvar getting = browser.storage.local.get("color");\ngetting.then(onGot, onError);\n

\n

At this point, the complete extension should look like this:

\n

    
    
    settings/\n    borderify.js\n    manifest.json\n    options.html\n    options.js

\n

Now:

\n

\n

  * [reload the extension](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox#Reloading_a_temporary_add-on)
\n

  * load a web page
\n

  * open the settings page and change the border color
\n

  * reload the web page to see the difference.
\n

\n

In Firefox you can access the settings page by visiting about:addons and
clicking the "Preferences" button next to the extension's entry.

\n

\n

## Learn more

\n

\n

  * `[options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)` manifest key reference documentation
\n

  * `[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API reference documentation
\n

  * open the settings page directly from your extension using the `[runtime.openOptionsPage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/openOptionsPage)` API
\n

  * Settings page example:\n \n
    * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
\n\n

\n

\n]

