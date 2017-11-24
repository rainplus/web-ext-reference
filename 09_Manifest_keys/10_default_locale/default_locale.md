[

Type| `String`  
---|---  
Mandatory| Contingent: must be present if the _locales subdirectory is
present, must be absent otherwise.  
Example| 

    
    
    "default_locale": "en"

  


This key must be present if the extension contains the _locales directory, and
must be absent otherwise. It identifies a subdirectory of _locales, and this
subdirectory will be used to find the default strings for your extension.



See [Internationalization](/en-US/Add-ons/WebExtensions/Internationalization).



## Example



    
    
    "default_locale": "en"



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  Yes| 48| 48|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 48  
  
]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

