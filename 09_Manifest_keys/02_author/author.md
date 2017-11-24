Type | `String`  
---|---  
Mandatory | No  
Example |

    
    
    "author": "Walt Whitman"  
  
The extension's author, intended for display in the browser's user interface.
If the [developer](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/developer) key is supplied and it contains the
"name" property, it will override the author key. There's no way to specify
multiple authors.

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

## Example

    
    
    "author": "Walt Whitman"

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  Yes1| 52| 52|  Yes  
  
1\. This key is mandatory in Microsoft Edge.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __This key is mandatory in Microsoft Edge.
|  Full support 52|  Full support Yes|  Full support 52

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[
Full support

]: Full support

  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

