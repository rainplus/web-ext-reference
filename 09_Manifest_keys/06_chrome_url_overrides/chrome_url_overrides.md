[

Type| `Object`  
---|---  
Mandatory| No  
Example| 

    
    
    \xa0 "chrome_url_overrides" : {\xa0\xa0\xa0 "newtab": "my-new-tab.html"\xa0 }

  


Use the `chrome_url_overrides` key to provide a custom replacement for the
documents loaded into various special pages usually provided by the browser
itself.



## Syntax



The `chrome_url_overrides` key is an object that may have the following
properties:

Name| Type| Description  
---|---|---  
`bookmark`| `String`| 

Provide a replacement for the page that shows the bookmarks.\xa0

  
`history`| `String`| 

Provide a replacement for the page that shows the browsing history.\xa0

  
`newtab`| `String`| 

Provide a replacement for the document that's shown in the "new tab" page.
This is the page that's shown when the user has opened a new tab but has not
loaded any document into it: for example, by using the Ctrl/Command+T keyboard
shortcut.



The replacement is given as a URL to an HTML file. The file must be bundled
with the extension: you can't specify a remote URL here. You can specify it
relative to the extension's root folder, like: "path/to/newtab.html".



The document can load CSS and JavaScript, just like a normal web page.
JavaScript running in the page gets access to the same [privileged "browser.*"
APIs](/en-US/Add-ons/WebExtensions/API) as the extension's background script.



It's very good practice to include a [<title>](/en-
US/docs/Web/HTML/Element/title) for the page, or the tab's title will be the
"moz-extension://..." URL.



A common use case is to let the user define a new tab page: to do this,
provide a custom new tab page that navigates to the page the user defined.



If two or more extensions both define custom new tab pages, then the last one
to be installed or enabled gets to use its value.



To override the browser's homepage, use "[chrome_settings_overrides](/en-
US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/chrome_settings_overrides)" instead.

  


All properties are [localizable](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).



## Example



    
    
    "chrome_url_overrides" : {  "newtab": "my-new-tab.html"}



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 54|  No|  Yes  
`newtab`|  Yes1|  No| 541|  No|  Yes1  
`bookmarks`|  Yes|  No|  No|  No|  Yes  
`history`|  Yes|  No|  No|  No|  Yes  
  
1\. If two or more extensions both define a custom new tab page, then in
Firefox the first extension to run wins. In Chrome and Opera, the last
extension wins.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes| No support No| Full
support 54| Full support Yes| No support No  
`newtab`| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If two or more extensions both define a custom new tab page, then in Firefox the first extension to run wins. In Chrome and Opera, the last extension wins.
|  No support No| Full support 54

Notes __

Full support 54

Notes __

     Notes __If two or more extensions both define a custom new tab page, then in Firefox the first extension to run wins. In Chrome and Opera, the last extension wins.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If two or more extensions both define a custom new tab page, then in Firefox the first extension to run wins. In Chrome and Opera, the last extension wins.
|  No support No  
`bookmarks`| Full support Yes| No support No| No support No|
Full support Yes| No support No  
`history`| Full support Yes| No support No| No support No|
Full support Yes| No support No  
  
]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

