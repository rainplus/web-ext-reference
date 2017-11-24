Type | `Object`  
---|---  
Mandatory | Usually, no (but see also [When do you need an Add-on
ID](https://developer.mozilla.org/en-US/Add-ons/WebExtensions
/WebExtensions_and_the_Add-on_ID#When_do_you_need_an_Add-
on_ID)[?](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/applications#When_do_I_need_the_applications_key)).
Mandatory before Firefox 48 (desktop) and Firefox for Android.  
Example |

    
    
    "applications": {
      "gecko": {
        "id": "addon@example.com",
        "strict_min_version": "42.0"
      }
    }  
  
The `applications` key contains keys that are specific to a particular host
application.

Currently this contains just one key, `gecko`, which may contain four string
attributes:

  * `id` is the [extension ID](https://developer.mozilla.org/en-US/Add-ons/Install_Manifests#id). Optional from Firefox 48, mandatory before Firefox 48. See [Extensions and the Add-on ID](/en-US/docs/Mozilla/Add-ons/WebExtensions/WebExtensions_and_the_Add-on_ID) to see when you need to specify an add-on ID.
  * `strict_min_version`: minimum version of Gecko to support. Versions containing a "*" are not valid in this field. Defaults to "42a1".
  * `strict_max_version`: maximum version of Gecko to support. If the Firefox version on which the extension is being installed or run is above this version, then the extension will be disabled, or not permitted to be installed. Defaults to "*", which disables checking for a maximum version.
  * `update_url` is a link to an [extension update manifest](/en-US/Add-ons/Updates). Note that the link must begin with "https". This key is for managing extension updates yourself (i.e. not through AMO).

See the list of [valid Gecko versions](https://addons.mozilla.org/en-
US/firefox/pages/appversions/).

## Examples

Example with all possible keys. Note that most extensions will omit
`strict_max_version` and `update_url`.

    
    
    "applications": {
      "gecko": {
        "id": "addon@example.com",
        "strict_min_version": "42.0",
        "strict_max_version": "50.*",
        "update_url": "https://example.com/updates.json"
      }
    }

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  No|  No| 48| 48|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  No support No|  No support No|  Full support 48|  No support
No|  Full support 48

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

