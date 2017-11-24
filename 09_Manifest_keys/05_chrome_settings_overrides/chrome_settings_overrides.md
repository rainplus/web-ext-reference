Use the `chrome_settings_overrides` key to override certain browser settings.
Two settings are available:

  * `"homepage"`, which enables you to override the browser's home page.
  * `"search_provider"`, which enables you to add a new search engine.

    
    
    "chrome_settings_overrides" : {
      "homepage": "https://developer.mozilla.org/"
    }
    
    
    "chrome_settings_overrides": {
      "search_provider": {
        "name": "Discogs",
        "search_url": "https://www.discogs.com/search/?q={searchTerms}",
        "keyword": "disc",
        "favicon_url": "https://www.discogs.com/favicon.ico"
      }
    }

Manifest key: `chrome_settings_overrides`  
---  
Type | `Object`  
Mandatory | No  
  
## Syntax

The `chrome_settings_overrides` key is an object that may have the following
properties:

Name | Type | Description  
---|---|---  
`homepage` | `String` |

Defines the page to be used as the browser's homepage.

The replacement is given as a URL. The URL may:

  * point to a file bundled with the extension, in which case it is given as a URL relative to the manifest.json file
  * be a remote URL, such as "https://developer.mozilla.org/".

If two or more extensions both set this value, then the setting from the most
recently installed one will take precedence.

To override new tabs, use "[chrome_url_overrides](/en-US/Add-
ons/WebExtensions/manifest.json/chrome_url_overrides)" instead.

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).  
  
`search_provider` | `Object` |

Defines a search provider to add to the browser.

The search provider has a name and a primary search URL. Alternative URLs may
be provided, including URLs for more specialized searches like image search.
In the URL you supply, use "`{searchTerms}`" to interpolate the search term
into the URL, like: `https://www.discogs.com/search/?q={searchTerms}`. You can
also provide POST parameters to be sent along with the search.

The search provider will be presented to the user alongside the built-in
providers. If you include the `is_default` property and set it to `true`, the
new search provider will be the default option. By supplying the `keyword`
property, you enable the user to select your search provider by typing the
keyword into the search/address bar before the search term.

This is an object with the properties listed below. All string properties are
[localizable](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

`name`

    String: The search engine's name, displayed to the user.
`search_url`

    String: URL used by the search engine. This must be an HTTPS URL.
`is_default`

    Boolean: True if the search engine should be the default choice.
`alternate_urls Optional`

    Array of String: An array of alternative URLs that can be used instead of `search_url`.
`encoding Optional`

    String: Encoding of the search term, specified as a [standard character encoding name](https://www.iana.org/assignments/character-sets/character-sets.xhtml), such as "UTF-8".
`favicon_url Optional`

    String: URL pointing to an icon for the search engine. This must be a absolute HTTP or HTTPS URL.
`image_url Optional`

    String: URL used for image search.
`image_url_post_params Optional`

    String: POST parameters to send to `image_url`.
`instant_url Optional`

    String: URL used for instant search.
`instant_url_post_params Optional`

    String: POST parameters to send to `instant_url`.
`keyword Optional`

    String: Address bar keyword for the search engine.
`prepopulated_id Optional`

    The ID of a built-in search engine to use.
`search_url_post_params Optional`

    String: POST parameters to send to `search_url`.
`suggest_url Optional`

    String: URL used for search suggestions.
`suggest_url_post_params Optional`

    String: POST parameters to send to `suggest_url`.  
  
## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 55|  No|  No  
`homepage`|  Yes|  No| 55|  No|  No  
`search_provider`|  Yes|  No| 55|  No|  No  
`search_provider.alternate_urls`|  Yes|  No|  No|  No|  No  
`search_provider.encoding`|  Yes|  No|  No|  No|  No  
`search_provider.favicon_url`|  Yes|  No| 55|  No|  No  
`search_provider.image_url`|  Yes|  No|  No|  No|  No  
`search_provider.image_url_post_params`|  Yes|  No|  No|  No|  No  
`search_provider.instant_url`|  Yes|  No|  No|  No|  No  
`search_provider.instant_url_post_params`|  Yes|  No|  No|  No|  No  
`search_provider.is_default`|  Yes|  No| 571|  No|  No  
`search_provider.keyword`|  Yes|  No| 55|  No|  No  
`search_provider.name`|  Yes|  No| 55|  No|  No  
`search_provider.prepopulated_id`|  Yes|  No|  No|  No|  No  
`search_provider.search_url`|  Yes|  No| 55|  No|  No  
`search_provider.search_url_post_params`|  Yes|  No|  No|  No|  No  
`search_provider.suggest_url`|  Yes|  No|  No|  No|  No  
`search_provider.suggest_url_post_params`|  Yes|  No|  No|  No|  No  
`startup_pages`|  Yes|  No|  No|  No|  No  
  
1\. Only built-in engines can be set as default.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes|  No support No|  Full support 55|  No
support No|  No support No  
`homepage`|  Full support Yes|  No support No|  Full support 55|  No support
No|  No support No  
`search_provider`|  Full support Yes|  No support No|  Partial support 55|  No
support No|  No support No  
`search_provider.alternate_urls`|  Full support Yes|  No support No|  No
support No|  No support No|  No support No  
`search_provider.encoding`|  Full support Yes|  No support No|  No support No|
No support No|  No support No  
`search_provider.favicon_url`|  Full support Yes|  No support No|  Full
support 55|  No support No|  No support No  
`search_provider.image_url`|  Full support Yes|  No support No|  No support
No|  No support No|  No support No  
`search_provider.image_url_post_params`|  Full support Yes|  No support No|
No support No|  No support No|  No support No  
`search_provider.instant_url`|  Full support Yes|  No support No|  No support
No|  No support No|  No support No  
`search_provider.instant_url_post_params`|  Full support Yes|  No support No|
No support No|  No support No|  No support No  
`search_provider.is_default`|  Full support Yes|  No support No|  Full support
57

Notes __

Full support 57

Notes __

     Notes __Only built-in engines can be set as default.
|  No support No|  No support No  
`search_provider.keyword`|  Full support Yes|  No support No|  Full support
55|  No support No|  No support No  
`search_provider.name`|  Full support Yes|  No support No|  Full support 55|
No support No|  No support No  
`search_provider.prepopulated_id`|  Full support Yes|  No support No|  No
support No|  No support No|  No support No  
`search_provider.search_url`|  Full support Yes|  No support No|  Full support
55|  No support No|  No support No  
`search_provider.search_url_post_params`|  Full support Yes|  No support No|
No support No|  No support No|  No support No  
`search_provider.suggest_url`|  Full support Yes|  No support No|  No support
No|  No support No|  No support No  
`search_provider.suggest_url_post_params`|  Full support Yes|  No support No|
No support No|  No support No|  No support No  
`startup_pages`|  Full support Yes|  No support No|  No support No|  No
support No|  No support No

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
  *[
Partial support

]: Partial support

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

