Type | `String`  
---|---  
Mandatory | No  
Example |

    
    
    "short_name": "My Extension"  
  
Short name for the extension. If given, this will be used in contexts where
the [name](/en-US/Add-ons/WebExtensions/manifest.json/name) field is too long.
It's recommended that the short name should not exceed 12 characters. If the
short name field is not included in manifest.json, then name will be used
instead and may be truncated.

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

## Example

    
    
    "short_name": "My Extension"

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
Basic support|  Full support Yes|  Full support Yes|  Full support 48|  Full
support Yes|  Full support 48

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

