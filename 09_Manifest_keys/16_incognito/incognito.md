[

Type| `String`  
---|---  
Mandatory| No  
Example| 

    
    
    "incognito": "spanning"



    
    
    "incognito": "split"



    
    
    "incognito": "not_allowed"

  


Use the `incognito` key to control how the extension works with private
browsing windows.



This is a string which may take any of the following values:





  * 

"spanning" (the default): the extension will see events from private and non-
private windows and tabs. Windows and tabs will get an `incognito` property in
the `[Window](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/Window)`
or `[Tab](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/Tab)` that
represents them. This property indicates whether or not the object is private:



    
        browser.windows.getLastFocused().then((windowInfo) => {  console.log(`Window is private: ${windowInfo.incognito}`);});





  * "split": the extension will be split between private and non-private windows. There are effectively two copies of the extension running: one sees only non-private windows, the other sees only private windows. Each copy has isolated access to Web APIs (so, for example, `[localStorage](/en-US/docs/Web/API/Storage/LocalStorage)` is not shared). However, the WebExtension API `[storage.local](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/local)` is shared.


  * "not_allowed": private tabs and windows are invisible to the extension.




## Example



    
    
    "incognito": "spanning"



    
    
    "incognito": "split"



    
    
    "incognito": "not_allowed"



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 48| 48|  Yes  
`split`|  Yes|  No|  No|  No|  Yes  
`not_allowed`|  Yes|  No|  No|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes| No support No| Full
support 48| Full support Yes| Full support 48  
`split`| Full support Yes| No support No| No support No|
Full support Yes| No support No  
`not_allowed`| Full support Yes| No support No| No support
No| Full support Yes| No support No  
  
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

