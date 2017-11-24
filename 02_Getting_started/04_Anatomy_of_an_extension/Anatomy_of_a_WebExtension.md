[



An extension consists of a collection of files, packaged\xa0for distribution
and installation. In this article, we will quickly go through the files that
might be present in an extension.



## manifest.json



This is the only file that must be present in every extension. It contains
basic metadata such as its name, version\xa0and the permissions it requires.
It also provides pointers to other files in the extension.



This manifest can also contain pointers to several other types of files:





  * [Background pages](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts): Implement long-running logic.


  * Icons for the extension and any buttons it might define.


  * [Sidebars, popups, and options pages](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Sidebars_popups_options_pages): HTML documents that provide content for various user interface components.


  * [Content scripts](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Content_scripts): JavaScript included with your extension, that you will inject into web pages.




![](https://mdn.mozillademos.org/files/13669/webextension-anatomy.png)



See the [manifest.json](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) reference page for all the details.



Other than those referenced from the manifest, an extension can include
additional [Extension pages](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Extension_pages) with supporting
files.



## Background scripts



Extensions often need to maintain long-term state\xa0or perform long-term
operations\xa0independently of the lifetime of any particular web page\xa0or
browser window. That is\xa0what background scripts are for.



Background scripts are loaded as soon as the extension is loaded and stay
loaded until the extension is disabled or uninstalled. You can use any of the
[WebExtension APIs](/en-US/Add-ons/WebExtensions/API) in the script, as long
as you have requested the necessary [permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).



### Specifying background scripts



You can include a background script using the `background` key in
"manifest.json":



    
    
    // manifest.json"background": {  "scripts": ["background-script.js"]}



You can specify multiple background scripts: if you do, they run in the same
context, just like multiple scripts that are loaded into a single web page.



### Background script environment



#### DOM APIs



Background scripts run in the context of special pages called background
pages. This gives them a `[window](/en-US/docs/Web/API/Window)` global, along
with all the standard DOM APIs provided by that object.



You do not have to supply your background page. If you include a background
script, an empty background page will be created for you.



However, you can choose to supply your background page as a separate HTML
file:



    
    
    // manifest.json"background": {  "page": "background-page.html"}



#### WebExtension APIs



Background scripts can use any of the [WebExtension APIs](/en-US/Add-
ons/WebExtensions/API) in the script, as long as their extension has the
necessary [permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).



#### Cross-origin access



Background scripts can make XHR requests to any hosts for which they have
[host permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).



#### Web content



Background scripts do not get direct access to web pages. However, they can
load [content scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Content_scripts) into web pages\xa0and can [communicate with
these content scripts using a message-passing API](/en-US/Add-
ons/WebExtensions/Content_scripts#Communicating_with_background_scripts).



#### Content security policy



Background scripts are restricted from certain potentially dangerous
operations, like the use of `[eval()](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/eval)`, through a Content
Security Policy. See [Content Security Policy](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Content_Security_Policy) for more details on this.



## Sidebars, popups, options pages



Your extension can include various user interface components whose content is
defined using an HTML document:





  * a [sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars) is a pane that is displayed at the left-hand side of the browser window, next to the web page


  * a [popup](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) is a dialog that you can display when the user clicks on a [toolbar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_action) or [address bar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Page_actions)


  * an [options page](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) is a page that's shown when the user accesses your add-on's preferences in the browser's native add-ons manager.




For each of these components, you create an HTML file and point to it using a
specific property in [manifest.json](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json). The HTML file can include CSS and JavaScript
files, just like a normal web page.



All of these are a type of [Extension pages](/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Extension_pages), and unlike a normal web
page, your JavaScript can use all the same privileged WebExtension APIs as
your background script. They can even directly access variables in the
background page using [`runtime.getBackgroundPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBackgroundPage "Retrieves the Window object
for the background page running inside the current extension.").



## Extension pages



You can also include HTML documents in your extension which are not attached
to some predefined user interface component. Unlike the documents you might
provide for sidebars, popups, or options pages, these don't have an entry in
manifest.json. However, they do also get access to all the same privileged
WebExtension APIs as your background script.



You'd typically load a page like this using [`windows.create()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/windows/create "Creates a new
window.") or [`tabs.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/create "Creates a new tab.").



See [Extension pages](/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Extension_pages) to learn more.



## Content scripts



Use content scripts to access and manipulate web pages. Content scripts are
loaded into web pages and run in the context of that particular page.



Content scripts are extension-provided scripts which run in the context of a
web page; this differs from scripts which are loaded by the page itself,
including those which are provided in [`<script>`](/en-
US/docs/Web/HTML/Element/script "The HTML <script> element is used to embed or
reference an executable script.") elements within the page.



Content scripts can see and manipulate the page's DOM, just like normal
scripts loaded by the page.



Unlike normal page scripts, they can:





  * Make cross-domain XHR requests.


  * Use a small subset of the [WebExtension APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/API).


  * Exchange messages with their background scripts\xa0and can in this way indirectly access all the WebExtension APIs.




Content scripts cannot directly access normal page scripts but can exchange
messages with them using the standard `[window.postMessage()](/en-
US/docs/Web/API/Window/postMessage)` API.



Usually, when we talk about content scripts, we are referring to JavaScript,
but you can inject CSS into web pages using the same mechanism.



See the [content scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Content_scripts) article to learn more.



## Web accessible resources



Web accessible resources are resources such as images, HTML, CSS, and
JavaScript\xa0that you include in the extension and want to make accessible to
content scripts and page scripts. Resources which are made web-accessible can
be referenced by page scripts and content scripts using a special URI scheme.



For example, if a content script wants to insert some images into web pages,
you could include them in the extension and make them web accessible. Then the
content script could create and append `[img](/en-
US/docs/Web/HTML/Element/img)` tags which reference the images via the `src`
attribute.



To learn more, see the documentation for the [web_accessible_resources](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/web_accessible_resources)
manifest.json key.



\xa0



\xa0

]

