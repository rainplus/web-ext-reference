[

Type| `Object`  
---|---  
Mandatory| No  
Example| 

    
    
    "omnibox": {\xa0 "keyword": "mdn"}

  


Use the `omnibox` key to define an omnibox keyword for your extension.



When the user types this keyword into the browser's address bar, followed by a
space, then any subsequent characters will be sent to the extension using the
`[omnibox](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox)` API. The
extension will then be able to populate the address bar's drop-down
suggestions list with its own suggestions.



If two or more extensions define the same keyword, then the extension that was
installed last gets to control the keyword. Any previously installed
extensions that defined the same keyword will no longer be able to use the
`omnibox` API.



## Example



    
    
    "omnibox": {  "keyword": "mdn"}



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 52|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes| No support No| Full
support 52| Full support Yes| No support No  
  
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
  *[Chrome __]: Chrome

