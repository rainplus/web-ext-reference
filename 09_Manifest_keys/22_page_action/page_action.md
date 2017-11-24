[

Type| `Object`  
---|---  
Mandatory| No  
Example| 

    
    
    "page_action": {  "browser_style": true,  "default_icon": {    "19": "button/geo-19.png",    "38": "button/geo-38.png"  },  "default_title": "Whereami?",  "default_popup": "popup/geo.html"}

  


A page action is an icon that your extension adds inside the browser's URL
bar.



Your extension may optionally also supply an associated popup whose content is
specified using HTML, CSS, and JavaScript.



If you supply a popup, then the popup is opened when the user clicks the icon,
and your JavaScript running in the popup can handle the user's interaction
with it. If you don't supply a popup, then a click event is dispatched to your
extension's [background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_pages) when the user
clicks the icon.



You can also create and manipulate page actions programmatically using the
[pageAction API](/en-US/Add-ons/WebExtensions/API/pageAction).



Page actions are like browser actions, except that they are associated with
particular web pages rather than with the browser as a whole. If an action is
only relevant on certain pages, then you should use a page action and display
it only on relevant pages. If an action is relevant to all pages or to the
browser itself, use a browser action.



While browser actions are displayed by default, page actions are hidden by
default. They can be shown for a particular tab by calling `[pageAction.show
()](/en-US/Add-ons/WebExtensions/API/pageAction/show)`, passing in the tab's
ID.



## Syntax



The `page_action` key is an object that may have any of three properties, all
optional:

Name| Type| Description  
---|---|---  
`browser_style`| `Boolean`| 

Optional, defaulting to `false`.



Use this to include a stylesheet in your popup that will make it look
consistent with the browser's UI and with other extensions that use the
`browser_style` property. Although this key defaults to `false`, it's
recommended that you include it and set it to `true`.



In Firefox, the stylesheet can be seen at
chrome://browser/content/extension.css, or chrome://browser/content/extension-
mac.css on OS X.



The [Firefox Style Guide](https://firefoxux.github.io/StyleGuide/#/controls)
describes the classes you can apply to elements in the popup in order to get
particular styles.



The [latest-download](https://github.com/mdn/webextensions-
examples/tree/master/latest-download) example extension uses `browser_style`
in its popup.

  
`default_icon`| `Object` or `String`| 

Use this to specify an icon for the action.



It's recommended that you supply two icons here, one 19x19 pixels, and one
38x38 pixels, and specify them in an object with properties named "19" and
"38", like this:



    
    
        "default_icon": {      "19": "geo-19.png",      "38": "geo-38.png"    }



If you do this, then the browser will pick the right size icon for the
screen's pixel density.



You can just supply a string here:



    
    
    "default_icon": "geo.png"



If you do this, then the icon will be scaled to fit the toolbar, and may
appear blurry.

  
`default_popup`| `String`| 

The path to an HTML file containing the specification of the popup.



The HTML file may include CSS and JavaScript files using `[<link>](/en-
US/docs/Web/HTML/Element/link)` and `[<script>](/en-
US/docs/Web/HTML/Element/script)` elements, just like a normal web page.



Unlike a normal web page, JavaScript running in the popup can access all the
[WebExtension APIs](/en-US/Add-ons/WebExtensions/API) (subject, of course, to
the extension having the appropriate [permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)).



This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

  
`default_title`| `String`| 

Tooltip for the icon, displayed when the user moves their mouse over it.



This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

  


## Example



    
    
    "page_action": {  "default_icon": {    "19": "button/geo-19.png",    "38": "button/geo-38.png"  }}



A page action with just an icon, specified in 2 different sizes. The
extension's background scripts can receive click events when the user clicks
the icon using code like this:



    
    
     browser.pageAction.onClicked.addListener(handleClick);



    
    
    "page_action": {  "default_icon": {    "19": "button/geo-19.png",    "38": "button/geo-38.png"  },  "default_title": "Whereami?",  "default_popup": "popup/geo.html"}



A page action with an icon, a title, and a popup. The popup will be shown when
the user clicks the icon.



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes1|  Yes1 2| 48|  No|  Yes  
`browser_style`|  No|  No| 48|  No|  No  
  
1\. SVG icons are not supported.

2\. 'default_icon' must be an object, with explicit sizes.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __SVG icons are not supported.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __SVG icons are not supported.
     Notes __'default_icon' must be an object, with explicit sizes.
|  Full support 48| Full support Yes| No support No  
`browser_style`| No support No| No support No| Full support
48| No support No| No support No  
  
]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

