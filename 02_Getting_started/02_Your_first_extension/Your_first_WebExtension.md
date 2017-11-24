[



In this article we'll walk through creating an extension for Firefox, from
start to finish. The extension just adds a red border to any pages loaded from
"mozilla.org" or any of its subdomains.



The source code for this example is on GitHub: <https://github.com/mdn
/webextensions-examples/tree/master/borderify>.



First, you'll need Firefox version 45 or later.



## Writing the extension



Create a new directory and navigate to it:



    
    
    mkdir borderifycd borderify



### manifest.json



Now create a new file called "manifest.json" directly under the "borderify"
directory. Give it the following contents:



    
    
    {  "manifest_version": 2,  "name": "Borderify",  "version": "1.0",  "description": "Adds a red border to all webpages matching mozilla.org.",  "icons": {    "48": "icons/border-48.png"  },  "content_scripts": [    {      "matches": ["*://*.mozilla.org/*"],      "js": ["borderify.js"]    }  ]}





  * The first three keys: `[manifest_version](/en-US/Add-ons/WebExtensions/manifest.json/manifest_version)`, `[name](/en-US/Add-ons/WebExtensions/manifest.json/name)`, and `[version](/en-US/Add-ons/WebExtensions/manifest.json/version)`, are mandatory and contain basic metadata for the extension.


  * `[description](/en-US/Add-ons/WebExtensions/manifest.json/description)` is optional, but recommended: it's displayed in the Add-ons Manager.


  * `[icons](/en-US/Add-ons/WebExtensions/manifest.json/icons)` is optional, but recommended: it allows you to specify an icon for the extension, that will be shown in the Add-ons Manager.




The most interesting key here is `[content_scripts](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts)`, which tells Firefox to load
a script into Web pages whose URL matches a specific pattern. In this case,
we're asking Firefox to load a script called "borderify.js" into all HTTP or
HTTPS pages served from "mozilla.org" or any of its subdomains.





  * [Learn more about content scripts.](/en-US/Add-ons/WebExtensions/Content_scripts)


  * [Learn more about match patterns](/en-US/Add-ons/WebExtensions/Match_patterns).






[In some situations you need to specify an ID for your extension](/en-US/Add-
ons/WebExtensions/WebExtensions_and_the_Add-on_ID#When_do_you_need_an_Add-
on_ID). If you do need to specify an add-on ID, include the\xa0 `[applications
](/en-US/Add-ons/WebExtensions/manifest.json/applications)` key in
`manifest.json` and set its `gecko.id` property:



    
    
    "applications": {  "gecko": {    "id": "borderify@example.com"  }}





### icons/border-48.png



The extension should have an icon. This will be shown next to the extension's
listing in the Add-ons Manager. Our manifest.json promised that we would have
an icon at "icons/border-48.png".



Create the "icons" directory directly under the "borderify" directory. Save an
icon there named "border-48.png".\xa0 You could use [the one from our
example](https://github.com/mdn/webextensions-
examples/blob/master/borderify/icons/border-48.png), which is taken from the
Google Material Design iconset, and is used under the terms of the [Creative
Commons Attribution-ShareAlike](https://creativecommons.org/licenses/by-
sa/3.0/) license.



If you choose to supply your own icon, It should be 48x48 pixels. You could
also supply a 96x96 pixel icon, for high-resolution displays, and if you do
this it will be specified as the `96` property of the `icons` object in
manifest.json:



    
    
    "icons": {  "48": "icons/border-48.png",  "96": "icons/border-96.png"}



Alternatively, you could supply an SVG file here, and it will be scaled
correctly. (Though: if you're using SVG and your icon includes text, you may
want to use your SVG editor's "convert to path" tool to flatten the text, so
that it scales with a consistent size/position.)





  * [Learn more about specifying icons.](/en-US/Add-ons/WebExtensions/manifest.json/icons)




### borderify.js



Finally, create a file called "borderify.js" directly under the "borderify"
directory. Give it this content:



    
    
    document.body.style.border = "5px solid red";



This script will be loaded into the pages that match the pattern given in the
`content_scripts` manifest.json key. The script has direct access to the
document, just like scripts loaded by the page itself.





  * [Learn more about content scripts.](/en-US/Add-ons/WebExtensions/Content_scripts)




## Trying it out



First, double check that you have the right files in the right places:



    
    
    borderify/    icons/        border-48.png    borderify.js    manifest.json



### Installing



Open "about:debugging" in Firefox, click "Load Temporary Add-on" and select
any file in your extension's directory:





The extension will now be installed, and will stay until you restart Firefox.



Alternatively, you can run the extension from the command line using the [web-
ext](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)
tool.



### Testing



Now try visiting a page under "mozilla.org", and you should see the red border
round the page:







Don't try it on addons.mozilla.org, though! Content scripts are currently
blocked on that domain.





Try experimenting a bit. Edit the content script to change the color of the
border, or do something else to the page content. Save the content script,
then reload the extensions's files by clicking the "Reload" button in
about:debugging. You can see the changes right away:







  * [Learn more about loading extensions](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)




## Packaging and publishing



For other people to use your extension, you need to package it and submit it
to Mozilla for signing. To learn more about that, see ["Publishing your
extension"](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Publishing_your_WebExtension).



## What's next?



Now you've got an idea of the process of developing a WebExtension for
Firefox, try:





  * [reading more about the anatomy of an extension](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension)


  * [writing a more complex extension](/en-US/Add-ons/WebExtensions/Your_second_WebExtension)


  * [reading about the JavaScript APIs available for extensions.](/en-US/Add-ons/WebExtensions/API)


]

