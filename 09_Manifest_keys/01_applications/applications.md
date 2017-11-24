[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| Usually, no (but see also [When do you need an Add-on
ID](https://developer.mozilla.org/en-US/Add-ons/WebExtensions
/WebExtensions_and_the_Add-on_ID#When_do_you_need_an_Add-
on_ID)[?](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/applications#When_do_I_need_the_applications_key)).
Mandatory before Firefox 48 (desktop) and Firefox for Android.\n  
\n\nExample\n| \n

    
    
    \n"applications": {\n  "gecko": {\n    "id": "addon@example.com",\n    "strict_min_version": "42.0"\n  }\n}

\n\n  
\n\n\n

The `applications` key contains keys that are specific to a particular host
application.

\n

Currently this contains just one key, `gecko`, which may contain four string
attributes:

\n

\n

  * `id` is the [extension ID](https://developer.mozilla.org/en-US/Add-ons/Install_Manifests#id). Optional from Firefox 48, mandatory before Firefox 48. See [Extensions and the Add-on ID](/en-US/docs/Mozilla/Add-ons/WebExtensions/WebExtensions_and_the_Add-on_ID) to see when you need to specify an add-on ID.
\n

  * `strict_min_version`: minimum version of Gecko to support. Versions containing a "*" are not valid in this field. Defaults to "42a1".
\n

  * `strict_max_version`: maximum version of Gecko to support. If the Firefox version on which the extension is being installed or run is above this version, then the extension will be disabled, or not permitted to be installed. Defaults to "*", which disables checking for a maximum version.
\n

  * `update_url` is a link to an [extension update manifest](/en-US/Add-ons/Updates). Note that the link must begin with "https". This key is for managing extension updates yourself (i.e. not through AMO).
\n

\n

See the list of [valid Gecko versions](https://addons.mozilla.org/en-
US/firefox/pages/appversions/).

\n

## Examples

\n

Example with all possible keys. Note that most extensions will omit
`strict_max_version` and `update_url`.

\n

    
    
    "applications": {\n  "gecko": {\n    "id": "addon@example.com",\n    "strict_min_version": "42.0",\n\xa0\xa0\xa0 "strict_max_version": "50.*",\n    "update_url": "https://example.com/updates.json"\n  }\n}

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n No| \n No| 48| 48| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
48| \nNo support\n\n No| \nFull support\n\n 48  
  
\n]

  *[\nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

