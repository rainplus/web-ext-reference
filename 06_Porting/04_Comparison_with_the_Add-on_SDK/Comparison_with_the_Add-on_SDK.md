[





This article is a technical comparison of the Add-on SDK and WebExtensions
technology. It's intended to help orient people who have an add-on that uses
the SDK, and who are planning to port it to use WebExtension APIs.



If you're planning to port an [overlay extension](/en-US/Add-
ons/Overlay_Extensions) or a [bootstrapped extension](/en-US/docs/Mozilla/Add-
ons/Bootstrapped_extensions), see [Comparison with XUL/XPCOM extensions](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions).





The basic structure and concepts of the Add-on SDK are shared by
WebExtensions. Both technologies include:





  * [manifest files](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Manifest_files) defining metadata for the extension and some aspects of its behavior.


  * [persistent scripts](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Persistent_scripts) that get access to a set of privileged JavaScript APIs and that stay loaded for as long as the extension itself is enabled.


  * [content scripts](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Content_scripts) that can be injected into web pages, and that can communicate with persistent scripts using an asynchronous messaging API.


  * [the ability to add specific UI elements](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#UI_elements), such as buttons, to the browser. Buttons in turn can have popups that are defined using HTML, JavaScript, and CSS.


  * [a set of privileged JavaScript APIs](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#JavaScript_APIs) for interacting with the web or with the browser.


  * [a command-line tool](/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK#Command-line_tool) that developers can use to test their extensions.




Beyond these broad similarities, there are a lot of differences in the
details, and these are summarised in the following sections.



## Manifest files



In both technologies you have a JSON manifest file in the extension's root
directory. In the SDK this is called "[package.json](/en-US/docs/Mozilla/Add-
ons/SDK/Tools/package_json)", while in WebExtensions it's called
"[manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)".
Both files contain basic metadata such as the extension's name, description,
and icons.



However, "manifest.json" includes many keys that define parts of the
extension's capabilities and behavior, which in the SDK are more often defined
in code. For example:

Feature| Add-on SDK| WebExtensions  
---|---|---  
Content scripts matching URL patterns| `[page-mod](/en-
US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-mod)` API|
`[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)` key  
Toolbar buttons| \xa0`[ui/button/action](/en-US/docs/Mozilla/Add-ons/SDK
/Low-Level_APIs/ui_button_action)` API| `[browser_action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)` key  
Access privileged APIs| `require()` function| `[permissions](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)` key  


This makes developing extensions with WebExtension APIs more declarative and
less programmatic, compared with SDK add-ons.



With the SDK you'll typically use `[jpm init](/en-US/Add-
ons/SDK/Tools/jpm#jpm_init)` to create a new package.json. The WebExtensions
technolgy doesn't have an equivalent of `jpm init`, so you'll probably write
the manifest from scratch or copy and adapt an existing one.





  * [Learn more about manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)




## Persistent scripts



Both technologies have the concept of persistent scripts that stay loaded for
the extension's lifetime, have access to privileged APIs, and can communicate
with other parts of the extension such as content scripts.



In the SDK this script is by default called "index.js", and it can [load other
scripts using the module loader](/en-US/Add-
ons/SDK/Guides/Module_structure_of_the_SDK#Local_Modules).



With WebExtensions, these scripts are called "[background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts)". You can
define a set of scripts using the `[background](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/background)` manifest key, and they will all
be loaded into the same document, which is a hidden, auto-generated, blank
HTML page. You can also define your own custom document using the `background`
key.



An important difference is that background scripts get a `[window](/en-
US/docs/Web/API/Window)` global, with all the DOM objects you'd expect to be
present on a window. This makes writing extensions more like writing web
pages, with direct access to all the normal Web APIs like [XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest) or [IndexedDB](/en-
US/docs/Web/API/IndexedDB_API).



Also note that by default, extensions have a [Content Security Policy](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy) applied to
them. You can specify your own policy, but the default policy, among other
things, disallows potentially unsafe practices such as the use of `[eval
()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)`.



### Learn more





  * [Background scripts for extensions](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts)




## Content scripts



In both the Add-on SDK and WebExtensions, persistent scripts can't directly
access the content of web pages. Instead, extensions can attach content
scripts to web pages. These scripts:





  * do get direct access to web content


  * don't have access to privileged APIs


  * can communicate with the persistent scripts using a messaging API.




In both technologies, there are two ways to attach scripts: you can
automatically attach a set of scripts to pages whose URL matches a given
pattern, or you can programmatically attach a script to the page hosted by a
given tab. The way to do this is different in each technology, though:

Operation| Add-on SDK| WebExtensions  
---|---|---  
Attach scripts to pages matching URL pattern| `[page-mod](/en-
US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-mod)` API|
`[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)` key  
Attach scripts to pages hosted by a tab| `[tab.attach()](/en-US/Add-
ons/SDK/High-Level_APIs/tabs#Run_scripts_in_a_tab)`| `[tabs.executeScript
()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript)`  


The match patterns used for URLs are different:





  * [SDK match patterns](/en-US/Add-ons/SDK/Low-Level_APIs/util_match-pattern)


  * [WebExtension match patterns](/en-US/Add-ons/WebExtensions/match_patterns)




In both technologies you can pass options to control when the script runs and
whether it will be attached to subframes. WebExtensions don't include an
equivalent of `contentScriptOptions`, though, so to pass configuration options
to a content script in an extension, you would either have to send them in a
message or store them in `[storage.local](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/local)`.



In both technologies, content scripts can communicate with persistent scripts
using an asynchronous messaging API:

Operation| Add-on SDK| WebExtensions  
---|---|---  
Send message| [`port.emit()`](/en-US/Add-
ons/SDK/Guides/Content_Scripts/port#emit\(\))| `[runtime.sendMessage()](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage)` /
`[tabs.sendMessage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage)`  
Receive message| `[port.on()](/en-US/Add-
ons/SDK/Guides/Content_Scripts/port#on\(\))`| `[runtime.onMessage](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`  




  * [Communicating with persistent scripts in the SDK](/en-US/Add-ons/SDK/Guides/Content_Scripts#Communicating_with_the_add-on)


  * [Communicating with persistent scripts in WebExtensions](/en-US/Add-ons/WebExtensions/Content_scripts#Communicating_with_background_scripts)




In both cases, content scripts can communicate with scripts loaded by the page
using `[window.postMessage](/en-US/docs/Web/API/Window/postMessage)` and
`[window.addEventListener](/en-US/docs/Web/API/EventTarget/addEventListener)`.



In both technologies, have access to the page they're injected into, but get
"a clean view of the DOM", meaning that they don't get to see modifications
made to the DOM by scripts loaded by the page.



In the SDK, content scripts can [share objects with page scripts](/en-US/Add-
ons/SDK/Guides/Content_Scripts/Interacting_with_page_scripts#Sharing_objects_with_page_scripts),
using techniques like `unsafeWindow` and `[createObjectIn](/en-
US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.createObjectIn)`.
With WebExtensions, the `unsafeWindow` is available via
`[wrappedJSObject](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Content_scripts#Accessing_page_script_objects_from_content_scripts)`
instead. All the export helper functions are available, too.



### Learn more





  * [Content scripts for WebExtensions](/en-US/Add-ons/WebExtensions/Content_scripts)




## UI elements



Both technologies provide APIs to create a UI for your extension. UI options
for WebExtensions are more limited.

UI element| Add-on SDK| WebExtensions  
---|---|---  
Button| `[ui/button/action](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_action)`| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-US/Add-
ons/WebExtensions/manifest.json/page_action)`  
Toggle button| `[ui/button/toggle](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_toggle)`| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-US/Add-
ons/WebExtensions/manifest.json/page_action)`  
Toolbar| `[ui/toolbar](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_toolbar)`| None  
Sidebar| `[ui/sidebar](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_sidebar)`| `sidebar_action`  
Panel| `[panel](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/panel)`| `browser_action` / `page_action`[ popup](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Popups)  
Context menu| `[context-menu](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/context-menu)`| `[contextMenus](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextMenus)`  


### Panels and popups



Panels and [popups](/en-US/docs/Mozilla/Add-ons/WebExtensions/Popups) are both
transient dialogs specified using HTML, CSS, and JavaScript.



Unlike panels, popups are always attached to a button (either a browser action
or a page action) and can't be displayed programmatically: they are only shown
when the user clicks the button.



Also unlike panels, popup scripts get access to all the same APIs that
background scripts do. They can even get direct access to the background page,
via `[runtime.getBackgroundPage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBackgroundPage)`.



## Settings



The Add-on SDK and WebExtensions both have some support for settings
(sometimes also called options or preferences).



With the SDK you can define preferences using a `preferences` key in
package.json. The user can see and change these preferences in the extension's
entry in the Add-ons Manager. The extension in turn can listen for changes
using the `[simple-prefs](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs
/simple-prefs)` API.



With WebExtensions, you will have to implement your own UI for presenting
settings, and your own code for persisting them for your extension. You do
this by writing an HTML file that presents the settings UI, which can include
a script for persisting the settings. The script gets access to all the
WebExtensions APIs, and it's generally expected that you should use the
`[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)` API to
persist settings.



You then assign the HTML file's URL to the `[options_ui](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/options_ui)` key in manifest.json. Your
settings page then appears in the extension's entry in the Add-ons Manager.
The options page can also be programmatically opened with an API call to
`[browser.runtime.openOptionsPage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage)`.



Note that WebExtensions does not provide an equivalent of the SDK's
`[preferences/service](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/preferences_service)` API, which provides general access to browser
settings. However, you can change some browser settings using the `[privacy
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)` and
`[browserSettings](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings)` APIs.



### Learn more





  * [Introduction to options pages](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Options_pages)


  * [An example extension that has an options page](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)




## Internationalization



The Add-on SDK and WebExtensions both include tools for localizing user-
visible text. They offer mostly similar functionality:

Feature| Add-on SDK| WebExtensions  
---|---|---  
Strings in add-on scripts| Yes| Yes  
Strings in content scripts| No| Yes  
Strings in HTML| Yes| No  
Strings in CSS| No| Yes  
Title & description| Yes| Yes  
Plural forms| Yes| No  
Placeholders| Yes| Yes  


In both systems, you supply localized strings as a collection of files, one
for each locale.



To retrieve localized strings in extension code, there's a JavaScript API -
`[l10n](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/l10n)` in the SDK and
`[i18n](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)` in WebExtensions
- that returns a localized string given an ID.



WebExtensions don't have direct support for localizing strings appearing in
HTML, so you have to do this yourself, using JavaScript to retrieve localized
strings and to replace the HTML with the localized version.



### Learn more





  * [Extensions Internationalization guide.](/en-US/Add-ons/WebExtensions/Internationalization)


  * [Example internationalized extension.](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)


  * [Example script for an extension using WebExtensions to translate HTML in the SDK style](https://gist.github.com/freaktechnik/4a72bc0711d9bc82cf3b075bcc292953)




## Command-line tool



The Add-on SDK comes with a command-line tool, [jpm](/en-US/docs/Mozilla/Add-
ons/SDK/Tools/jpm), that you can use for testing and packaging extensions.
There's an equivalent tool for WebExtensions, called [web-ext](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext). web-ext
doesn't yet support all the same commands that jpm does, but it has the
basics: [run](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_run), [build](/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_build), and [sign](https://developer.mozilla.org
/en-US/Add-ons/WebExtensions/web-ext_command_reference#web-ext_sign).



It's also now possible to install (and reload) SDK add-ons and extensions
built with WebExtension APIs in Firefox from their source directory, without
needing to package them as an XPI. See [Temporary Installation in Firefox
](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox).



### Learn more





  * [web-ext tutorial](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)


  * [web-ext reference](/en-US/Add-ons/WebExtensions/web-ext_command_reference)


  * [Temporary installation in Firefox](/en-US/docs/Mozilla/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)




## JavaScript APIs



In both the SDK and WebExtensions, the main power of the extension comes from
a set of dedicated JavaScript APIs. For most of the SDK high-level APIs, there
is a WebExtensions equivalent.



One big limitation of WebExtensions compared with the SDK is that SDK add-ons
can use require("chrome") to get access to the full range of XPCOM APIs in
Firefox. This is not possible with WebExtensions.



To access privileged APIs in the SDK, you use require():



    
    
    var tabs = require("sdk/tabs");tabs.open("https://developer.mozilla.org/");



With WebExtensions most APIs are made available already, with no need to
import them:



    
    
    browser.tabs.create({  "url": "https://developer.mozilla.org/"});



For some WebExtension APIs, you need to ask permission first, using the
`[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)` manifest.json key. In the
example below, the extension will need to ask for the "tabs" permission if
they want access to the tab's URL:



 **manifest.json:**



    
    
    ..."permissions": [    "tabs"  ]...



 **background script:**



    
    
    function logUrl(tabs) { console.log(tabs[0].url);}var querying = browser.tabs.query(  {active: true, currentWindow: true});querying.then(logUrl);



### Add-on SDK => WebExtensions



The tables in this section list every SDK API and describe what the equivalent
WebExtensions API would be, if there is one implemented in the current
Developer Edition.



The first table covers high-level SDK APIs, the second covers low-level APIs.



#### High-level APIs

Add-on SDK| WebExtensions  
---|---  
[addon-page](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/addon-
page)| Use `[tabs.create()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/create)` to load pages packaged with your add-on
into normal browser tabs.  
[base64](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/base64)|
[`window.atob()` and `btoa()`](https://developer.mozilla.org/en-
US/docs/Web/API/WindowBase64)  
[clipboard](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/clipboard)|
`[document.execCommand](/en-US/docs/Web/API/Document/execCommand)` without
using `select()` and similar in the background page.  
[context-menu](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/context-
menu)| `[contextMenus](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextMenus)`  
[hotkeys](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/hotkeys)|
`[commands](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands)`  
[indexed-db](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/indexed-
db)| `[window.indexedDB](/en-US/docs/Web/API/IndexedDB_API)`  
[l10n](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/l10n)| `[i18n
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)`  
[notifications](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/notifications)| `[notifications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications)`  
[page-mod](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-mod)|
`[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)`  
[page-worker](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/page-
worker)| 

Porting isn't complete and being treated in [Bug
1318532](https://bugzilla.mozilla.org/show_bug.cgi?id=1318532)



Workarounds (that might require webrequestBlocking to access all webpages
[[example](https://stackoverflow.com/questions/15532791/getting-around-x
-frame-options-deny-in-a-chrome-extension)]):





  * Use the background page


  * load remote iframes into the background page


  * make an [ajax](/en-US/docs/AJAX) call to get static information from the page


  
[panel](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/panel)| See [UI
elements](/en-US/Add-ons/WebExtensions/Porting_from_the_Add-
on_SDK#UI_elements) above.  
[passwords](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/passwords)|
[Experimental logins API ](https://github.com/web-ext-experiments/logins)  
[private-browsing](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs
/private-browsing)| `[Tab.incognito](/en-US/Add-
ons/WebExtensions/API/Tabs/Tab)` and `[Window.incognito](/en-US/Add-
ons/WebExtensions/API/windows/Window)`.  
[querystring](/en-US/docs/Mozilla/Add-ons/SDK/High-
Level_APIs/querystring)| `[window.URLSearchParams](/en-
US/docs/Web/API/URLSearchParams)`  
[request](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/request)|
`[window.fetch](/en-US/docs/Web/API/Fetch_API)` or `[window.XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest)`  
[selection](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/selection)|
Use a content script that sends the selection data to the add-on.
Alternatively, if you can use a contextmenu on a selection, the selection is
contained in selectionText (see `[contextMenus.OnClickData](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/contextMenus/OnClickData)`).  
[self](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/self)|
`[runtime.getManifest()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getManifest)` and `[extension.getURL()](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/extension/getURL)` for
`data.url()`  
[simple-prefs](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/simple-
prefs)| `[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)`
and `[options_ui](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/options_ui)`  
[simple-storage](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/simple-
storage)| `[storage](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage)`  
[system](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/system)| Partly
provided by `[runtime](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime)`.  
[tabs](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/tabs)| `[tabs
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)`  
[timers](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/timers)|
`[alarms](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms)`  
[ui](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/ui)| See [UI
elements](/en-US/Add-ons/WebExtensions/Porting_from_the_Add-
on_SDK#UI_elements) above.  
[url](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/url)| `[window.URL
](/en-US/docs/Web/API/Window/URL)`  
[widget](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/widget)| None  
[windows](/en-US/docs/Mozilla/Add-ons/SDK/High-Level_APIs/windows)|
`[windows](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)`  


#### Low-level APIs

Add-on SDK| WebExtensions  
---|---  
[loader](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/_loader)|
None  
[chrome](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/chrome)| None  
[console/plain-text](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/console_plain-text)| None  
[console/traceback](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/console_traceback)| None  
[content/content](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_content)| None  
[content/loader](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_loader)| None  
[content/mod](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_mod)| None  
[content/symbiont](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_symbiont)| None  
[content/worker](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/content_worker)| None  
[core/heritage](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/core_heritage)| None  
[core/namespace](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/core_namespace)| None  
[core/promise](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/core_promise)| `[Promise](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/Promise)`  
[dev/panel](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/dev_panel)|
`[devtools.panels](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/devtools.panels)`  
[event/core](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/event_core)|
None  
[event/target](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/event_target)| None  
[frame/hidden-frame](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/frame_hidden-frame)| None  
[frame/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/frame_utils)| None  
[fs/path](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/fs_path)|
None  
[io/byte-streams](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/io_byte-
streams)| None  
[io/file](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/io_file)|
None  
[io/text-streams](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/io_text-
streams)| None  
[lang/functional](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/lang_functional)| None  
[lang/type](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/lang_type)|
None  
[loader/cuddlefish](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/loader_cuddlefish)| None  
[loader/sandbox](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/loader_sandbox)| None  
[net/url](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/net_url)|
None  
[net/xhr](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/net_xhr)|
`[window.fetch](/en-US/docs/Web/API/Fetch_API)` or `[window.XMLHttpRequest
](/en-US/docs/Web/API/XMLHttpRequest)`  
[places/bookmarks](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/places_bookmarks)| `[bookmarks](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks)`  
[places/favicon](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/places_favicon)| None  
[places/history](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/places_history)| `[history](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history)`  
[platform/xpcom](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/platform_xpcom)| None  
[preferences/event-target](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/preferences_event-target)| None  
[preferences/service](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/preferences_service)| Limited support via the `[privacy](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)` and `[browserSettings
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings)` APIs.  
[remote/child](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/remote_child)| None  
[remote/parent](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/remote_parent)| None  
[stylesheet/style](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/stylesheet_style)| None  
[stylesheet/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/stylesheet_utils)| None  
[system/child_process](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_child_process)| `[runtime.connectNative](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/connectNative)`  
[system/environment](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_environment)| None  
[system/events](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_events)| None  
[system/runtime](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/system_runtime)| Partially provided by `[runtime.getPlatformInfo
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/getPlatformInfo)`  
[system/xul-app](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/system_xul-app)| Partially provided by `[runtime.getBrowserInfo](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/getBrowserInfo)`  
[tabs/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/tabs_utils)|
None  
[ui/button/action](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_action)| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)`  
[ui/button/toggle](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/ui_button_toggle)| `[browser_action](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/browser_action)` / `[page_action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)`  
[ui/frame](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_frame)|
None  
[ui/id](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_id)| None  
[ui/sidebar](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_sidebar)|
`[sidebarAction](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sidebarAction)`  
[ui/toolbar](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/ui_toolbar)|
None  
[util/array](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/util_array)|
None  
[util/collection](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/util_collection)| None  
[util/deprecate](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/util_deprecate)| None  
[util/list](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/util_list)|
None  
[util/match-pattern](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs
/util_match-pattern)| None  
[util/object](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/util_object)| None  
[util/uuid](/en-US/docs/Mozilla/Add-ons/SDK/Low-Level_APIs/util_uuid)|
None  
[window/utils](/en-US/docs/Mozilla/Add-ons/SDK/Low-
Level_APIs/window_utils)| None  
]

