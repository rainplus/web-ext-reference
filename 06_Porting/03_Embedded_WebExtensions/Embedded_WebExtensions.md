Firefox 57 drops support for legacy add-on types, including legacy add-ons
that embed WebExtensions. From Firefox 57 onwards, Firefox will not load add-
ons of the type described in this document.

Starting in Firefox 51, you can embed a WebExtension in a classic
[bootstrapped extension](/en-US/docs/Mozilla/Add-ons/Bootstrapped_extensions)
or an [Add-on SDK](/en-US/docs/Mozilla/Add-ons/SDK) add-on.

The embedded WebExtension's files are packaged inside the legacy add-on. The
embedded WebExtension doesn't directly share its scope with the embedding
legacy add-on, but they can exchange messages using the messaging functions
defined in the [`runtime`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime "This module provides information about your
extension and the environment it's running in.") API.

![](https://mdn.mozillademos.org/files/13895/embedded-we.png)

This means you can migrate a legacy add-on to WebExtensions one piece at a
time, and have a fully functioning add-on at every step. In particular, it
enables you to [migrate stored data](/en-US/Add-
ons/WebExtensions/Embedded_WebExtensions#Migrating_data_from_legacy_add-ons)
from a legacy add-on to a WebExtension, by writing an intermediate hybrid add-
on that reads the data using the legacy APIs (for example, [simple-prefs](/en-
US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/simple-prefs) or the preferences
[service](/en-US/docs/Mozilla/JavaScript_code_modules/Services.jsm)) and
writes it using the WebExtension APIs (for example, [`storage`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/storage "Enables extensions to store
and retrieve data, and listen for changes to stored items.")).

Together with this guide, we've written two examples showing how to use
embedded WebExtensions to help migrate from a legacy add-on type. One shows
[how to port from a bootstrapped add-on](https://github.com/mdn/webextensions-
examples/tree/master/embedded-webextension-bootstrapped), and the other shows
[how to port from an SDK add-on](https://github.com/mdn/webextensions-
examples/tree/master/embedded-webextension-sdk).

To embed a WebExtension you'll need Firefox 51 or later. To embed a
WebExtension in an SDK add-on, you'll also need [jpm
1.2.0](https://www.npmjs.com/package/jpm).

Firefox 57 drops support for legacy add-on types. If you are currently
maintaining an add-on in the legacy add-on format and want to migrate data,
publish an update containing an embedded WebExtension as early as possible. If
the update is published close to the [release date of Firefox
57](https://wiki.mozilla.org/RapidRelease/Calendar), the data stored in your
add-on will be lost if the user updates Firefox before receiving your add-on
update.

## Embedding the WebExtension

If the legacy add-on is a bootstrapped extension with an [install.rdf](/en-US
/Add-ons/Install_Manifests), include the property "hasEmbeddedWebExtension" in
the RDF, containing the value "true":

    
    
    <em:hasEmbeddedWebExtension>true</em:hasEmbeddedWebExtension>

If the legacy add-on is an SDK add-on, include the key
"hasEmbeddedWebExtension" in the package.json, set to `true`:



    
    
    "hasEmbeddedWebExtension": true
    

The WebExtension itself lives in a top-level directory called "webextension"
inside the add-on. For example:



    
    
    my-boostrapped-addon/
        chrome/
        webextension/
            manifest.json
            background.js
            ...
        bootstrap.js
        chrome.manifest
        install.rdf



    
    
    my-sdk-addon/
        index.js
        package.json
        webextension/
            manifest.json
            background.js
            ...

Note that the embedded WebExtension must be directly inside the
`webextension/` directory. It can't be in a subdirectory. This also means that
you can't embed more than one WebExtension.

Firefox does not treat the embedded WebExtension as an independent add-on. For
this reason you shouldn't specify an [add-on ID](/en-US/docs/Mozilla/Add-
ons/WebExtensions/WebExtensions_and_the_Add-on_ID) for it. If you do it will
just be ignored.

However, when you've finished migrating the add-on and removed the legacy
embedding code, you must include an [applications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/applications) key setting the ID to be the
same as the original legacy add-on's ID. In this way
[addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/) will recognize
that the WebExtension is an update of the legacy add-on.

## Starting the WebExtension

The embedded WebExtension must be explicitly started by the embedding add-on.

If the embedding add-on is a bootstrapped add-on, then the `data` argument
passed to the bootstrap's `[startup()](/en-US/Add-
ons/Bootstrapped_extensions#startup)` function will get an extra property
`webExtension`:

    
    
    // bootstrapped add-on
    
    function startup({webExtension}) {
    
    ...

If the embedding add-on is an SDK add-on, it will be able to access a
WebExtension object using the `sdk/webextension` module:

    
    
    // SDK add-on
    
    const webExtension = require("sdk/webextension");

Either way, this object has a single function, `startup()`, that returns a
`[Promise](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)`. The
promise resolves to an object with a single property `browser`: this contains
the [`runtime`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime "This
module provides information about your extension and the environment it's
running in.") APIs that the embedding add-on can use to exchange messages with
the embedded WebExtension:

  * [`runtime.onConnect`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect "Fired when a connection is made with either an extension process or a content script.")
  * [`runtime.onMessage`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage "To send a message which will be received by the onMessage listener, use runtime.sendMessage\(\) or \(to send a message to a content script\) tabs.sendMessage\(\).")

For example:

    
    
    // bootstrapped add-on
    
    function startup({webExtension}) {
      webExtension.startup().then(api => {
        const {browser} = api;
        browser.runtime.onMessage.addListener(handleMessage);
      });
    }
    
    
    // SDK add-on
    
    const webExtension = require("sdk/webextension");
    
    webExtension.startup().then(api => {
      const {browser} = api;
      browser.runtime.onMessage.addListener(handleMessage);
    });
    

Note that the embedding legacy add-on can't initiate communications: it can
receive (and optionally respond to) one-off messages, using `onMessage`, and
can accept connection requests using `onConnect`.

The promise is rejected if the embedded WebExtension is missing a manifest or
if the manifest is invalid. In this case you'll see more details in the
[Browser Toolbox Console](/en-US/Add-
ons/WebExtensions/Debugging_\(before_Firefox_50\)#Viewing_log_output).

## Exchanging messages

Once the embedded WebExtension is running, it can exchange messages with the
legacy add-on using a subset of the [`runtime`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime "This module provides information about your
extension and the environment it's running in.") APIs:

  * It can send one-off messages using [`runtime.sendMessage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage "Sends a single message to event listeners within your extension or a different extension.").
  * It can set up a connection using [`runtime.connect()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/connect "Make a connection between different contexts inside the extension.").

### Connectionless messaging

To send a single message, the WebExtension can use [`runtime.sendMessage
()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage "Sends
a single message to event listeners within your extension or a different
extension."). You can omit the `extensionId` argument, because the browser
considers the embedded WebExtension to be part of the embedding add-on:

    
    
    browser.runtime.sendMessage("message-from-webextension").then(reply => {
      if (reply) {
        console.log("response from legacy add-on: " + reply.content);
      }
    });

The embedding add-on can receive (and optionally respond to) this message
using the [`runtime.onMessage`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onMessage "To send a message which will be
received by the onMessage listener, use runtime.sendMessage\(\) or \(to send a
message to a content script\) tabs.sendMessage\(\).") object:

    
    
    // bootstrapped add-on
    
    function startup({webExtension}) {
      // Start the embedded webextension.
      webExtension.startup().then(api => {
        const {browser} = api;
        browser.runtime.onMessage.addListener((msg, sender, sendReply) => {
          if (msg == "message-from-webextension") {
            sendReply({
              content: "reply from legacy add-on"
            });
          }
        });
      });
    }

### Connection-oriented messaging

To set up a longer-lived connection between the WebExtension and the legacy
add-on, the WebExtension can use [`runtime.connect()`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime/connect "Make a connection between
different contexts inside the extension.").

    
    
    var port = browser.runtime.connect({name: "connection-to-legacy"});
    
    port.onMessage.addListener(function(message) {
      console.log("Message from legacy add-on: " + message.content);
    });
    

The legacy add-on can listen for connection attempts using [`runtime.onConnect
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect "Fired when
a connection is made with either an extension process or a content script."),
and both sides can then use the resulting [`runtime.Port`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime/Port "A Port object represents one end of a
connection between two specific contexts, which can be used to exchange
messages.") to exchange messages:

    
    
    function startup({webExtension}) {
      // Start the embedded webextension.
      webExtension.startup().then(api => {
        const {browser} = api;
        browser.runtime.onConnect.addListener((port) => {
          port.postMessage({
            content: "content from legacy add-on"
          });
        });
      });
    }

## Migrating data from legacy add-ons

One major use for embedded WebExtensions is to migrate an add-on's stored
data.

Stored data is a problem for people trying to migrate from legacy add-on
types, because the legacy add-ons can't use the WebExtension storage APIs,
while WebExtensions can't use the legacy storage APIs. For example, if an SDK
add-on uses the SDK's [simple-prefs](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/simple-prefs) API to store preferences, the WebExtension version
won't be able to access that data.

With embedded WebExtensions, you can migrate data by creating an intermediate
version of the add-on that embeds a WebExtension. This intermediate version
reads the stored data using the legacy APIs, and writes the data using the
WebExtension APIs.

  * In the initial version, an SDK-based add-on reads and writes add-on preferences using the [simple-prefs](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/simple-prefs) API.
  * In the intermediate version, the SDK add-on starts the embedded WebExtension. The WebExtension then asks the SDK add-on to retrieve the stored data from simple-prefs. The WebExtension then stores the data using the [`storage`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage "Enables extensions to store and retrieve data, and listen for changes to stored items.") API.

  * In the final version, the add-on is just a WebExtension, and uses only the storage API.

We've provided two examples illustrating this pattern: ["embedded-
webextension-bootstrapped"](https://github.com/mdn/webextensions-
examples/tree/master/embedded-webextension-bootstrapped) shows migration from
a bootstrapped add-on, while ["embedded-webextension-
sdk"](https://github.com/mdn/webextensions-examples/tree/master/embedded-
webextension-sdk) shows migration from an SDK add-on.

### Preferences

An extension that contains an embedded WebExtension can define preferences
either in the _embedding_ legacy extension (using, for example, [simple-prefs
](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/simple-prefs) or the
preferences [service](/en-
US/docs/Mozilla/JavaScript_code_modules/Services.jsm)) or in the _embedded_
WebExtension (using [options_ui](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/options_ui)).

If both parts define preferences, then the embedded WebExtension's preferences
will override the legacy ones.

If the embedded WebExtension defines preferences, then they will only be
initialized after the embedded WebExtension has been [started](/en-US/Add-
ons/WebExtensions/Embedded_WebExtensions#Starting_the_WebExtension). Until
then, the "Preferences" button in "about:addons" will not be shown for the
add-on, and the browser will log an error to the [Browser Console](/en-
US/docs/Tools/Browser_Console) when "about:addons" is opened.

For this reason, it's important for the embedding extension to start the
embedded WebExtension immediately on startup. For a bootstrapped extension,
this means you should call `webExtension.startup()` in the [bootstrap startup
](/en-US/Add-ons/Bootstrapped_extensions#startup). For an add-on SDK
extension, this means you should call `webExtension.startup()` in the add-on's
entry point (by default, index.js).

If the "about:addons" page is already opened in a tab when the embedded
WebExtension is started, the Preferences button will not be visible until the
next reload of the "about:addons" page.

## Limitations

### Debugging

If you have a legacy add-on that embeds a WebExtension, you can't use the new
Add-on Debugger to debug the WebExtension. You'll need to use the [old
debugging workflow](/en-US/Add-
ons/WebExtensions/Debugging_\(before_Firefox_50\)), based around the Browser
Toolbox.

