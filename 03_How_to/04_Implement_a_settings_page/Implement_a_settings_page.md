A settings page gives users a way to see and change settings (sometimes also
called "preferences" or "options") for the extension.

With WebExtension APIs, settings are generally stored using the `[storage
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API. Implementing a
settings page is a three-step process:

  * Write an HTML file that displays settings and lets the user change them.
  * Write a script, included from the HTML file, that populates the settings page from storage and updates stored settings when the user changes them.
  * Set the path to the HTML file as the `[options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)` key in manifest.json. By doing this, the HTML document will be shown in the browser's add-on manager, alongside the extension's name and description.

You can also open this page programmatically using the
`[runtime.openOptionsPage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage)` function.

## A simple extension

First, we'll write an extension that adds a blue border to every page the user
visits.

Create a new directory called "settings", then create a file called
"manifest.json" inside it with the following contents:

    
    
    {
    
      "manifest_version": 2,
      "name": "Settings example",
      "version": "1.0",
    
      "content_scripts": [
        {
          "matches": ["<all_urls>"],
          "js": ["borderify.js"]
        }
      ]
    
    }

This extension instructs the browser to load a content script called
"borderify.js" into all web pages the user visits.

Next, create a file called "borderify.js" inside the "settings" directory, and
give it these contents:

    
    
    document.body.style.border = "10px solid blue";

This just adds a blue border to the page.

Now [install the extension](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox) and test it — open up any
web page you like:

## Adding settings

Now let's create a settings page to allow the user to set the color of the
border.

First, update "manifest.json" so it has these contents:

    
    
    {
    
      "manifest_version": 2,
      "name": "Settings example",
      "version": "1.0",
    
      "content_scripts": [
        {
          "matches": ["<all_urls>"],
          "js": ["borderify.js"]
        }
      ],
    
      "options_ui": {
        "page": "options.html"
      },
    
      "permissions": ["storage"]
    
    }
    

We've added two new manifest keys:

  * `[options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)`: This sets an HTML document to be the settings page (also called options page) for this extension.
  * `[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)`: We'll use the `[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API to store the settings, and we need to ask permission to use this API.

Next, because we've promised to provide "options.html", let's create it.
Create a file with that name inside the "settings" directory, and give it the
following contents:

    
    
    <!DOCTYPE html>
    
    <html>
      <head>
        <meta charset="utf-8">
      </head>
    
      <body>
    
        <form>
            <label>Border color<input type="text" id="color" ></label>
            <button type="submit">Save</button>
        </form>
    
        <script src="options.js"></script>
    
      </body>
    
    </html>
    

This defines a [`<form>`](/en-US/docs/Web/HTML/Element/form "The HTML <form>
element represents a document section that contains interactive controls to
submit information to a web server.") with a labeled text [`<input>`](/en-
US/docs/Web/HTML/Element/input "The HTML <input> element is used to create
interactive controls for web-based forms in order to accept data from the
user.") and a submit [`<button>`](/en-US/docs/Web/HTML/Element/button "The
HTML <button> element represents a clickable button."). It also includes a
script called "options.js".

Create "options.js", again in the "settings" directory, and give it the
following contents:

    
    
    function saveOptions(e) {
      e.preventDefault();
      browser.storage.local.set({
        color: document.querySelector("#color").value
      });
    }
    
    function restoreOptions() {
    
      function setCurrentChoice(result) {
        document.querySelector("#color").value = result.color || "blue";
      }
    
      function onError(error) {
        console.log(`Error: ${error}`);
      }
    
      var getting = browser.storage.local.get("color");
      getting.then(setCurrentChoice, onError);
    }
    
    document.addEventListener("DOMContentLoaded", restoreOptions);
    document.querySelector("form").addEventListener("submit", saveOptions);
    

This does two things:

  * When the document has loaded, it fetches the value of "color" from storage using `[storage.local.get()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/StorageArea/get)`. If the value isn't set, it uses the default "blue".
  * When the user submits the form by clicking "Save", it stores the value of the textbox using `[storage.local.set()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/StorageArea/set)`.

Finally, update "borderify.js" to read the border color from storage:

Due to a bug in [browser.storage.local.get()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/StorageArea/get) in Firefox versions prior to
52, the following code will not function. To make it function in Firefox
versions below 52, the two occurrences of `item.color` in `onGot()` must be
changed to `item[0].color`.

    
    
     function onError(error) {
      console.log(`Error: ${error}`);
    }
    
    function onGot(item) {
      var color = "blue";
      if (item.color) {
        color = item.color;
      }
      document.body.style.border = "10px solid " + color;
    }
    
    var getting = browser.storage.local.get("color");
    getting.then(onGot, onError);
    

At this point, the complete extension should look like this:

    
    
    settings/
        borderify.js
        manifest.json
        options.html
        options.js

Now:

  * [reload the extension](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox#Reloading_a_temporary_add-on)
  * load a web page
  * open the settings page and change the border color
  * reload the web page to see the difference.

In Firefox you can access the settings page by visiting about:addons and
clicking the "Preferences" button next to the extension's entry.

## Learn more

  * `[options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)` manifest key reference documentation
  * `[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API reference documentation
  * open the settings page directly from your extension using the `[runtime.openOptionsPage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/openOptionsPage)` API
  * Settings page example: 
    * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)

