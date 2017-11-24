[\n

\n

\n

This article is a technical comparison of the Add-on SDK and WebExtensions
technology. It's intended to help orient people who have an add-on that uses
the SDK, and who are planning to port it to use WebExtension APIs.

\n

If you're planning to port an [overlay extension](/en-US/Add-
ons/Overlay_Extensions) or a [bootstrapped extension](/en-US/docs/Mozilla/Add-
ons/Bootstrapped_extensions), see [Comparison with XUL/XPCOM extensions](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions).

\n

\n

The basic structure and concepts of the Add-on SDK are shared by
WebExtensions. Both technologies include:

\n

\n

  * [manifest files](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Manifest_files) defining metadata for the extension and some aspects of its behavior.
\n

  * [persistent scripts](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Persistent_scripts) that get access to a set of privileged JavaScript APIs and that stay loaded for as long as the extension itself is enabled.
\n

  * [content scripts](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Content_scripts) that can be injected into web pages, and that can communicate with persistent scripts using an asynchronous messaging API.
\n

  * [the ability to add specific UI elements](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#UI_elements), such as buttons, to the browser. Buttons in turn can have popups that are defined using HTML, JavaScript, and CSS.
\n

  * [a set of privileged JavaScript APIs](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#JavaScript_APIs) for interacting with the web or with the browser.
\n

  * [a command-line tool](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Command-line_tool) that developers can use to test their extensions.
\n

\n

Beyond these broad similarities, there are a lot of differences in the
details, and these are summarised in the following sections.

\n

## Manifest files

\n

In both technologies you have a JSON manifest file in the extension's root
directory. In the SDK this is called "[package.json](/en-US/docs/Mozilla/Add-
ons/SDK/Tools/package_json)", while in WebExtensions it's called
"[manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)".
Both files contain basic metadata such as the extension's name, description,
and icons.

\n

However, "manifest.json" includes many keys that define parts of the
extension's capabilities and behavior, which in the SDK are more often defined
in code. For example:

\n\n\n\nFeature\n| Add-on SDK\n| WebExtensions\n  
---|---|---  
\n\n\n\nContent scripts matching URL patterns\n| `[page-mod](/en-
US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-mod)` API\n|
`[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)` key\n  
\n\nToolbar buttons\n| \xa0`[ui/button/action](/en-US/docs/Mozilla/Add-ons/SDK
/Low-Level_APIs/ui_button_action)` API\n| `[browser_action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)` key\n  
\n\nAccess privileged APIs\n| `require()` function\n| `[permissions](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)` key\n  
\n\n\n

This makes developing extensions with WebExtension APIs more declarative and
less programmatic, compared with SDK add-ons.

\n

With the SDK you'll typically use `[jpm init](/en-US/Add-
ons/SDK/Tools/jpm#jpm_init)` to create a new package.json. The WebExtensions
technolgy doesn't have an equivalent of `jpm init`, so you'll probably write
the manifest from scratch or copy and adapt an existing one.

\n

\n

  * [Learn more about manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)
\n

\n

## Persistent scripts

\n

Both technologies have the concept of persistent scripts that stay loaded for
the extension's lifetime, have access to privileged APIs, and can communicate
with other parts of the extension such as content scripts.

\n

In the SDK this script is by default called "index.js", and it can [load other
scripts using the module loader](/en-US/Add-
ons/SDK/Guides/Module_structure_of_the_SDK#Local_Modules).

\n

With WebExtensions, these scripts are called "[background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts)". You can
define a set of scripts using the `[background](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/background)` manifest key, and they will all
be loaded into the same document, which is a hidden, auto-generated, blank
HTML page. You can also define your own custom document using the `background`
key.

\n

An important difference is that background scripts get a `[window](/en-
US/docs/Web/API/Window)` global, with all the DOM objects you'd expect to be
present on a window. This makes writing extensions more like writing web
pages, with direct access to all the normal Web APIs like [XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest) or [IndexedDB](/en-
US/docs/Web/API/IndexedDB_API).

\n

Also note that by default, extensions have a [Content Security Policy](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy) applied to
them. You can specify your own policy, but the default policy, among other
things, disallows potentially unsafe practices such as the use of `[eval
()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)`.

\n

### Learn more

\n

\n

  * [Background scripts for extensions](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts)
\n

\n

## Content scripts

\n

In both the Add-on SDK and WebExtensions, persistent scripts can't directly
access the content of web pages. Instead, extensions can attach content
scripts to web pages. These scripts:

\n

\n

  * do get direct access to web content
\n

  * don't have access to privileged APIs
\n

  * can communicate with the persistent scripts using a messaging API.
\n

\n

In both technologies, there are two ways to attach scripts: you can
automatically attach a set of scripts to pages whose URL matches a given
pattern, or you can programmatically attach a script to the page hosted by a
given tab. The way to do this is different in each technology, though:

\n\n\n\nOperation\n| Add-on SDK\n| WebExtensions\n  
---|---|---  
\n\n\n\nAttach scripts to pages matching URL pattern\n| `[page-mod](/en-
US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-mod)` API\n|
`[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)` key\n  
\n\nAttach scripts to pages hosted by a tab\n| `[tab.attach()](/en-US/Add-
ons/SDK/High-Level_APIs/tabs#Run_scripts_in_a_tab)`\n| `[tabs.executeScript
()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript)`\n  
\n\n\n

The match patterns used for URLs are different:

\n

\n

  * [SDK match patterns](/en-US/Add-ons/SDK/Low-Level_APIs/util_match-pattern)
\n

  * [WebExtension match patterns](/en-US/Add-ons/WebExtensions/match_patterns)
\n

\n

In both technologies you can pass options to control when the script runs and
whether it will be attached to subframes. WebExtensions don't include an
equivalent of `contentScriptOptions`, though, so to pass configuration options
to a content script in an extension, you would either have to send them in a
message or store them in `[storage.local](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/local)`.

\n

In both technologies, content scripts can communicate with persistent scripts
using an asynchronous messaging API:

\n\n\n\nOperation\n| Add-on SDK\n| WebExtensions\n  
---|---|---  
\n\n\n\nSend message\n| [`port.emit()`](/en-US/Add-
ons/SDK/Guides/Content_Scripts/port#emit\(\))\n| `[runtime.sendMessage()](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage)` /
`[tabs.sendMessage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage)`\n  
\n\nReceive message\n| `[port.on()](/en-US/Add-
ons/SDK/Guides/Content_Scripts/port#on\(\))`\n| `[runtime.onMessage](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`\n  
\n\n\n

\n

  * [Communicating with persistent scripts in the SDK](/en-US/Add-ons/SDK/Guides/Content_Scripts#Communicating_with_the_add-on)
\n

  * [Communicating with persistent scripts in WebExtensions](/en-US/Add-ons/WebExtensions/Content_scripts#Communicating_with_background_scripts)
\n

\n

In both cases, content scripts can communicate with scripts loaded by the page
using `[window.postMessage](/en-US/docs/Web/API/Window/postMessage)` and
`[window.addEventListener](/en-US/docs/Web/API/EventTarget/addEventListener)`.

\n

In both technologies, have access to the page they're injected into, but get
"a clean view of the DOM", meaning that they don't get to see modifications
made to the DOM by scripts loaded by the page.

\n

In the SDK, content scripts can [share objects with page scripts](/en-US/Add-
ons/SDK/Guides/Content_Scripts/Interacting_with_page_scripts#Sharing_objects_with_page_scripts),
using techniques like `unsafeWindow` and `[createObjectIn](/en-
US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.createObjectIn)`.
With WebExtensions, the `unsafeWindow` is available via
`[wrappedJSObject](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Content_scripts#Accessing_page_script_objects_from_content_scripts)`
instead. All the export helper functions are available, too.

\n

### Learn more

\n

\n

  * [Content scripts for WebExtensions](/en-US/Add-ons/WebExtensions/Content_scripts)
\n

\n

## UI elements

\n

Both technologies provide APIs to create a UI for your extension. UI options
for WebExtensions are more limited.

\n\n\n\nUI element\n| Add-on SDK\n| WebExtensions\n  
---|---|---  
\n\n\n\nButton\n| `[ui/button/action](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_action)`\n| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-US/Add-
ons/WebExtensions/manifest.json/page_action)`\n  
\n\nToggle button\n| `[ui/button/toggle](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_toggle)`\n| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-US/Add-
ons/WebExtensions/manifest.json/page_action)`\n  
\n\nToolbar\n| `[ui/toolbar](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_toolbar)`\n| None\n  
\n\nSidebar\n| `[ui/sidebar](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_sidebar)`\n| `sidebar_action`\n  
\n\nPanel\n| `[panel](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/panel)`\n| `browser_action` / `page_action`[ popup](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Popups)\n  
\n\nContext menu\n| `[context-menu](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/context-menu)`\n| `[contextMenus](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextMenus)`\n  
\n\n\n

### Panels and popups

\n

Panels and [popups](/en-US/docs/Mozilla/Add-ons/WebExtensions/Popups) are both
transient dialogs specified using HTML, CSS, and JavaScript.

\n

Unlike panels, popups are always attached to a button (either a browser action
or a page action) and can't be displayed programmatically: they are only shown
when the user clicks the button.

\n

Also unlike panels, popup scripts get access to all the same APIs that
background scripts do. They can even get direct access to the background page,
via `[runtime.getBackgroundPage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBackgroundPage)`.

\n

## Settings

\n

The Add-on SDK and WebExtensions both have some support for settings
(sometimes also called options or preferences).

\n

With the SDK you can define preferences using a `preferences` key in
package.json. The user can see and change these preferences in the extension's
entry in the Add-ons Manager. The extension in turn can listen for changes
using the `[simple-prefs](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs
/simple-prefs)` API.

\n

With WebExtensions, you will have to implement your own UI for presenting
settings, and your own code for persisting them for your extension. You do
this by writing an HTML file that presents the settings UI, which can include
a script for persisting the settings. The script gets access to all the
WebExtensions APIs, and it's generally expected that you should use the
`[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API to
persist settings.

\n

You then assign the HTML file's URL to the `[options_ui](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/options_ui)` key in manifest.json. Your
settings page then appears in the extension's entry in the Add-ons Manager.
The options page can also be programmatically opened with an API call to
`[browser.runtime.openOptionsPage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage)`.

\n

Note that WebExtensions does not provide an equivalent of the SDK's
`[preferences/service](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/preferences_service)` API, which provides general access to browser
settings. However, you can change some browser settings using the `[privacy
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)` and
`[browserSettings](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings)` APIs.

\n

### Learn more

\n

\n

  * [Introduction to options pages](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Options_pages)
\n

  * [An example extension that has an options page](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
\n

\n

## Internationalization

\n

The Add-on SDK and WebExtensions both include tools for localizing user-
visible text. They offer mostly similar functionality:

\n\n\n\nFeature\n| Add-on SDK\n| WebExtensions\n  
---|---|---  
\n\n\n\nStrings in add-on scripts\n| Yes\n| Yes\n  
\n\nStrings in content scripts\n| No\n| Yes\n  
\n\nStrings in HTML\n| Yes\n| No\n  
\n\nStrings in CSS\n| No\n| Yes\n  
\n\nTitle & description\n| Yes\n| Yes\n  
\n\nPlural forms\n| Yes\n| No\n  
\n\nPlaceholders\n| Yes\n| Yes\n  
\n\n\n

In both systems, you supply localized strings as a collection of files, one
for each locale.

\n

To retrieve localized strings in extension code, there's a JavaScript API -
`[l10n](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/l10n)` in the SDK and
`[i18n](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)` in WebExtensions
- that returns a localized string given an ID.

\n

WebExtensions don't have direct support for localizing strings appearing in
HTML, so you have to do this yourself, using JavaScript to retrieve localized
strings and to replace the HTML with the localized version.

\n

### Learn more

\n

\n

  * [Extensions Internationalization guide.](/en-US/Add-ons/WebExtensions/Internationalization)
\n

  * [Example internationalized extension.](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)
\n

  * [Example script for an extension using WebExtensions to translate HTML in the SDK style](https://gist.github.com/freaktechnik/4a72bc0711d9bc82cf3b075bcc292953)
\n

\n

## Command-line tool

\n

The Add-on SDK comes with a command-line tool, [jpm](/en-US/docs/Mozilla/Add-
ons/SDK/Tools/jpm), that you can use for testing and packaging extensions.
There's an equivalent tool for WebExtensions, called [web-ext](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext). web-ext
doesn't yet support all the same commands that jpm does, but it has the
basics: [run](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_run), [build](/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_build), and [sign](https://developer.mozilla.org
/en-US/Add-ons/WebExtensions/web-ext_command_reference#web-ext_sign).

\n

It's also now possible to install (and reload) SDK add-ons and extensions
built with WebExtension APIs in Firefox from their source directory, without
needing to package them as an XPI. See [Temporary Installation in Firefox
](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox).

\n

### Learn more

\n

\n

  * [web-ext tutorial](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)
\n

  * [web-ext reference](/en-US/Add-ons/WebExtensions/web-ext_command_reference)
\n

  * [Temporary installation in Firefox](/en-US/docs/Mozilla/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)
\n

\n

## JavaScript APIs

\n

In both the SDK and WebExtensions, the main power of the extension comes from
a set of dedicated JavaScript APIs. For most of the SDK high-level APIs, there
is a WebExtensions equivalent.

\n

One big limitation of WebExtensions compared with the SDK is that SDK add-ons
can use require("chrome") to get access to the full range of XPCOM APIs in
Firefox. This is not possible with WebExtensions.

\n

To access privileged APIs in the SDK, you use require():

\n

    
    
    var tabs = require("sdk/tabs");\ntabs.open("https://developer.mozilla.org/");

\n

With WebExtensions most APIs are made available already, with no need to
import them:

\n

    
    
    browser.tabs.create({\n  "url": "https://developer.mozilla.org/"\n});

\n

For some WebExtension APIs, you need to ask permission first, using the
`[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)` manifest.json key. In the
example below, the extension will need to ask for the "tabs" permission if
they want access to the tab's URL:

\n

 **manifest.json:**

\n

    
    
    ...\n\n"permissions": [\n    "tabs"\n  ]\n\n...

\n

 **background script:**

\n

    
    
    function logUrl(tabs) {\n console.log(tabs[0].url);\n}\n\nvar querying = browser.tabs.query(\n  {active: true, currentWindow: true}\n);\n\nquerying.then(logUrl);\n

\n

### Add-on SDK => WebExtensions

\n

The tables in this section list every SDK API and describe what the equivalent
WebExtensions API would be, if there is one implemented in the current
Developer Edition.

\n

The first table covers high-level SDK APIs, the second covers low-level APIs.

\n

#### High-level APIs

\n\n\n\nAdd-on SDK\n| WebExtensions\n  
---|---  
\n\n\n\n[addon-page](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/addon-
page)\n| Use `[tabs.create()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/create)` to load pages packaged with your add-on
into normal browser tabs.\n  
\n\n[base64](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/base64)\n|
[`window.atob()` and `btoa()`](https://developer.mozilla.org/en-
US/docs/Web/API/WindowBase64)\n  
\n\n[clipboard](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/clipboard)\n|
`[document.execCommand](/en-US/docs/Web/API/Document/execCommand)` without
using `select()` and similar in the background page.\n  
\n\n[context-menu](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/context-
menu)\n| `[contextMenus](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextMenus)`\n  
\n\n[hotkeys](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/hotkeys)\n|
`[commands](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands)`\n  
\n\n[indexed-db](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/indexed-
db)\n| `[window.indexedDB](/en-US/docs/Web/API/IndexedDB_API)`\n  
\n\n[l10n](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/l10n)\n| `[i18n
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)`\n  
\n\n[notifications](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/notifications)\n| `[notifications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications)`\n  
\n\n[page-mod](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-mod)\n|
`[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)`\n  
\n\n[page-worker](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-
worker)\n| \n

Porting isn't complete and being treated in [Bug
1318532](https://bugzilla.mozilla.org/show_bug.cgi?id=1318532)

\n

Workarounds (that might require webrequestBlocking to access all webpages
[[example](https://stackoverflow.com/questions/15532791/getting-around-x
-frame-options-deny-in-a-chrome-extension)]):

\n

\n

  * Use the background page
\n

  * load remote iframes into the background page
\n

  * make an [ajax](/en-US/docs/AJAX) call to get static information from the page
\n

\n\n  
\n\n[panel](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/panel)\n| See [UI
elements](/en-US/Add-ons/WebExtensions/Porting_from_the_Add-
on_SDK#UI_elements) above.\n  
\n\n[passwords](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/passwords)\n|
[Experimental logins API ](https://github.com/web-ext-experiments/logins)\n  
\n\n[private-browsing](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs
/private-browsing)\n| `[Tab.incognito](/en-US/Add-
ons/WebExtensions/API/Tabs/Tab)` and `[Window.incognito](/en-US/Add-
ons/WebExtensions/API/windows/Window)`.\n  
\n\n[querystring](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/querystring)\n| `[window.URLSearchParams](/en-
US/docs/Web/API/URLSearchParams)`\n  
\n\n[request](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/request)\n|
`[window.fetch](/en-US/docs/Web/API/Fetch_API)` or `[window.XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest)`\n  
\n\n[selection](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/selection)\n|
Use a content script that sends the selection data to the add-on.
Alternatively, if you can use a contextmenu on a selection, the selection is
contained in selectionText (see `[contextMenus.OnClickData](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/contextMenus/OnClickData)`).\n  
\n\n[self](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/self)\n|
`[runtime.getManifest()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getManifest)` and `[extension.getURL()](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/extension/getURL)` for
`data.url()`\n  
\n\n[simple-prefs](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/simple-
prefs)\n| `[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)`
and `[options_ui](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/options_ui)`\n  
\n\n[simple-storage](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/simple-
storage)\n| `[storage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage)`\n  
\n\n[system](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/system)\n| Partly
provided by `[runtime](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime)`.\n  
\n\n[tabs](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/tabs)\n| `[tabs
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)`\n  
\n\n[timers](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/timers)\n|
`[alarms](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms)`\n  
\n\n[ui](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/ui)\n| See [UI
elements](/en-US/Add-ons/WebExtensions/Porting_from_the_Add-
on_SDK#UI_elements) above.\n  
\n\n[url](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/url)\n| `[window.URL
](/en-US/docs/Web/API/Window/URL)`\n  
\n\n[widget](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/widget)\n| None\n  
\n\n[windows](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/windows)\n|
`[windows](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)`\n  
\n\n\n

#### Low-level APIs

\n\n\n\nAdd-on SDK\n| WebExtensions\n  
---|---  
\n\n\n\n[loader](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/_loader)\n|
None\n  
\n\n[chrome](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/chrome)\n| None\n  
\n\n[console/plain-text](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/console_plain-text)\n| None\n  
\n\n[console/traceback](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/console_traceback)\n| None\n  
\n\n[content/content](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_content)\n| None\n  
\n\n[content/loader](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_loader)\n| None\n  
\n\n[content/mod](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_mod)\n| None\n  
\n\n[content/symbiont](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_symbiont)\n| None\n  
\n\n[content/worker](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_worker)\n| None\n  
\n\n[core/heritage](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/core_heritage)\n| None\n  
\n\n[core/namespace](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/core_namespace)\n| None\n  
\n\n[core/promise](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/core_promise)\n| `[Promise](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise)`\n  
\n\n[dev/panel](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/dev_panel)\n|
`[devtools.panels](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/devtools.panels)`\n  
\n\n[event/core](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/event_core)\n|
None\n  
\n\n[event/target](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/event_target)\n| None\n  
\n\n[frame/hidden-frame](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/frame_hidden-frame)\n| None\n  
\n\n[frame/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/frame_utils)\n| None\n  
\n\n[fs/path](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/fs_path)\n|
None\n  
\n\n[io/byte-streams](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/io_byte-
streams)\n| None\n  
\n\n[io/file](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/io_file)\n|
None\n  
\n\n[io/text-streams](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/io_text-
streams)\n| None\n  
\n\n[lang/functional](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/lang_functional)\n| None\n  
\n\n[lang/type](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/lang_type)\n|
None\n  
\n\n[loader/cuddlefish](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/loader_cuddlefish)\n| None\n  
\n\n[loader/sandbox](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/loader_sandbox)\n| None\n  
\n\n[net/url](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/net_url)\n|
None\n  
\n\n[net/xhr](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/net_xhr)\n|
`[window.fetch](/en-US/docs/Web/API/Fetch_API)` or `[window.XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest)`\n  
\n\n[places/bookmarks](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/places_bookmarks)\n| `[bookmarks](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks)`\n  
\n\n[places/favicon](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/places_favicon)\n| None\n  
\n\n[places/history](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/places_history)\n| `[history](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history)`\n  
\n\n[platform/xpcom](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/platform_xpcom)\n| None\n  
\n\n[preferences/event-target](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/preferences_event-target)\n| None\n  
\n\n[preferences/service](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/preferences_service)\n| Limited support via the `[privacy](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)` and `[browserSettings
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings)` APIs.\n  
\n\n[remote/child](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/remote_child)\n| None\n  
\n\n[remote/parent](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/remote_parent)\n| None\n  
\n\n[stylesheet/style](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/stylesheet_style)\n| None\n  
\n\n[stylesheet/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/stylesheet_utils)\n| None\n  
\n\n[system/child_process](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_child_process)\n| `[runtime.connectNative](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/connectNative)`\n  
\n\n[system/environment](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_environment)\n| None\n  
\n\n[system/events](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_events)\n| None\n  
\n\n[system/runtime](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_runtime)\n| Partially provided by `[runtime.getPlatformInfo
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/getPlatformInfo)`\n  
\n\n[system/xul-app](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/system_xul-app)\n| Partially provided by `[runtime.getBrowserInfo](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/getBrowserInfo)`\n  
\n\n[tabs/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/tabs_utils)\n|
None\n  
\n\n[ui/button/action](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_action)\n| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)`\n  
\n\n[ui/button/toggle](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_toggle)\n| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)`\n  
\n\n[ui/frame](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_frame)\n|
None\n  
\n\n[ui/id](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_id)\n| None\n  
\n\n[ui/sidebar](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_sidebar)\n|
`[sidebarAction](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction)`\n  
\n\n[ui/toolbar](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_toolbar)\n|
None\n  
\n\n[util/array](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/util_array)\n|
None\n  
\n\n[util/collection](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/util_collection)\n| None\n  
\n\n[util/deprecate](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/util_deprecate)\n| None\n  
\n\n[util/list](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/util_list)\n|
None\n  
\n\n[util/match-pattern](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/util_match-pattern)\n| None\n  
\n\n[util/object](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/util_object)\n| None\n  
\n\n[util/uuid](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/util_uuid)\n|
None\n  
\n\n[window/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/window_utils)\n| None\n  
\n\n\n]

