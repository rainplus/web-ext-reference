[

Type| `Object`  
---|---  
Mandatory| No  
Example| 

    
    
    "sidebar_action": {  "default_icon": {    "16": "button/geo-16.png",    "32": "button/geo-32.png"  },  "default_title": "My sidebar",  "default_panel": "sidebar/sidebar.html"}

  


A [sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars) is a pane that
is displayed at the left-hand side of the browser window, next to the web
page. The browser provides a UI that enables the user to see the currently
available sidebars and to select a sidebar to display.



The sidebar_action key enables you to define the default properties for the
sidebar. You can change these properties at runtime using the [`sidebarAction
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction "Gets and sets
properties of an extension's sidebar.") API.



## Syntax



The `sidebar_action` key is an object that may have any of the properties
listed below. The only mandatory property is `default_panel`.

Name| Type| Description  
---|---|---  
`browser_style`| `Boolean`| 

Optional, defaulting to `true`.



Use this to include a stylesheet in your popup that will make it look
consistent with the browser's UI and with other extensions that use the
`browser_style` property.

  
`default_icon`| `Object` or `String`| 

Use this to specify one or more icons for the sidebar. The icon is shown in
the browser's UI for opening and closing sidebars.



Icons are specified as URLs relative to the manifest.json file itself.



You can specify a single icon file by supplying a string here:



    
    
    "default_icon": "path/to/geo.svg"



To specify multiple icons in different sizes, specify an object here. The name
of each property is the icon's height in pixels, and must be convertible to an
integer. The value is the URL. For example:



    
    
        "default_icon": {      "16": "path/to/geo-16.png",      "32": "path/to/geo-32.png"    }



See [Choosing icon sizes](/en-US/Add-
ons/WebExtensions/manifest.json/browser_action#Choosing_icon_sizes) for more
guidance on this.



This property is optional: if it is omitted, the sidebar doesn't get an icon.

  
`default_panel`| `String`| 

The path to an HTML file that specifies the sidebar's contents.



The HTML file may include CSS and JavaScript files using `[<link>](/en-
US/docs/Web/HTML/Element/link)` and `[<script>](/en-
US/docs/Web/HTML/Element/script)` elements, just like a normal web page.



Unlike a normal web page, JavaScript running in the panel can access all the
[WebExtension APIs](/en-US/Add-ons/WebExtensions/API) (subject, of course, to
the extension having the appropriate [permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)).



This property is mandatory.



This is a [localizable property](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

  
`default_title`| `String`| 

Title for the sidebar. This is used in the browser UI for listing and opening
sidebars, and is displayed at the top of the sidebar when it is open.



This property is optional: if it is omitted, the sidebar's title is the
extension's `[name](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/name)`.



This is a [localizable property](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

  


## Example



    
    
    "sidebar_action": {\xa0 "default_icon": "sidebar.svg",\xa0 "default_title": "My sidebar!",\xa0 "default_panel": "sidebar.html",  "browser_style": true}



For a simple example of an extension that uses a sidebar, see [annotate-
page](https://github.com/mdn/webextensions-examples/tree/master/annotate-
page).



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  No|  No| 54|  No|  Yes  
`browser_style`|  No|  No| 55|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  No support No| No support No| Full support
54| Full support Yes| No support No  
`browser_style`| No support No| No support No| Full support
55| No support No| No support No  
  
]

  *[Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

