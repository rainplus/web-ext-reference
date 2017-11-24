Type | `Object`  
---|---  
Mandatory | No  
Example |

    
    
    "developer": {
      "name": "Walt Whitman",
      "url": "https://en.wikipedia.org/wiki/Walt_Whitman"
    }  
  
The name of the extension's developer and their homepage URL, intended for
display in the browser's user interface.

The object, and both of its properties, are optional. The "name" and "url"
properties, if present, will override the  [author](/en-US/Add-
ons/WebExtensions/manifest.json/author) and [homepage_url](/en-US/Add-
ons/WebExtensions/manifest.json/homepage_url) keys, respectively. This object
only allows for a single developer name and URL to be specified.

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

## Example

    
    
    "developer": {
      "name": "Walt Whitman",
      "url": "https://en.wikipedia.org/wiki/Walt_Whitman"
    }

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  No|  No| 52| 52|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  No support No|  No support No|  Full support 52|  Full support
Yes|  Full support 52

  *[
 No support

]: No support

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

