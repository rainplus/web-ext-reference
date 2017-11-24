[





An Options page enables you to define preferences for your extension that your
users can change. Users can access the options page for an extension from the
browser's add-ons manager:





The way users access the page, and the way it's integrated into the browser's
user interface, will vary from one browser to another.







You can open the page programmatically by calling
[`runtime.openOptionsPage()`](https://developer.mozilla.org/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/Runtime/openOptionsPage "If your add-on does not
have an options page, or the browser failed to create one for some other
reason, runtime.lastError will be set.").



Options pages have a Content Security Policy that restricts the sources from
which they can load resources, and disallows some unsafe practices such as the
use of `[eval()](https://developer.mozilla.org/en-
US/docs/Web/JavaScript/Reference/Global_Objects/eval)`. See [Content Security
Policy](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/Content_Security_Policy) for more details.



## Specifying the options page



To create an options page, write an HTML file defining the page. This page can
include CSS and JavaScript files, like a normal web page. This page, from the
[favourite-colour](https://github.com/mdn/webextensions-examples/tree/master
/favourite-colour) example, includes a JavaScript file:



    
    
    <!DOCTYPE html><html>  <head>    <meta charset="utf-8">  </head><body>  <form>      <label>Favourite colour</label>      <input type="text" id="colour" >      <button type="submit">Save</button>  </form>  <script src="options.js"></script></body></html>



JavaScript running in the page can use all the [WebExtension
APIs](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API) that the
add-on has [permissions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) for. In particular, you can use
the [`storage`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/Storage "Enables WebExtensions to store and retrieve
data, and listen for changes to stored items.") API to persist preferences.



Package the page's files in your extension.



You also need to include the `[options_ui](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)` key in your
manifest.json file, giving it the URL to the page.



    
    
    "options_ui": {  "page": "options.html",  "browser_style": true},



## Examples



The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use an options
page:





  * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour) example extension with options page




]

