[\n

\n

Use the `chrome_settings_overrides` key to override certain browser settings.
Two settings are available:

\n

\n

  * `"homepage"`, which enables you to override the browser's home page.
\n

  * `"search_provider"`, which enables you to add a new search engine.
\n

\n

    
    
    "chrome_settings_overrides" : {\n  "homepage": "https://developer.mozilla.org/"\n}

\n

    
    
    "chrome_settings_overrides": {\n  "search_provider": {\n    "name": "Discogs",\n    "search_url": "https://www.discogs.com/search/?q={searchTerms}",\n    "keyword": "disc",\n    "favicon_url": "https://www.discogs.com/favicon.ico"\n  }\n}

\n\n\n\nManifest key: `chrome_settings_overrides`\n  
---  
\n\nType\n| `Object`\n  
\n\nMandatory\n| No\n  
\n\n\n

## Syntax

\n

The `chrome_settings_overrides` key is an object that may have the following
properties:

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`homepage`\n| `String`\n| \n

Defines the page to be used as the browser's homepage.

\n

The replacement is given as a URL. The URL may:

\n

\n

  * point to a file bundled with the extension, in which case it is given as a URL relative to the manifest.json file
\n

  * be a remote URL, such as "https://developer.mozilla.org/".
\n

\n

If two or more extensions both set this value, then the setting from the most
recently installed one will take precedence.

\n

To override new tabs, use "[chrome_url_overrides](/en-US/Add-
ons/WebExtensions/manifest.json/chrome_url_overrides)" instead.

\n

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n\n  
\n\n`search_provider`\n| `Object`\n| \n

Defines a search provider to add to the browser.

\n

The search provider has a name and a primary search URL. Alternative URLs may
be provided, including URLs for more specialized searches like image search.
In the URL you supply, use "`{searchTerms}`" to interpolate the search term
into the URL, like: `https://www.discogs.com/search/?q={searchTerms}`. You can
also provide POST parameters to be sent along with the search.

\n

The search provider will be presented to the user alongside the built-in
providers. If you include the `is_default` property and set it to `true`, the
new search provider will be the default option. By supplying the `keyword`
property, you enable the user to select your search provider by typing the
keyword into the search/address bar before the search term.

\n

This is an object with the properties listed below. All string properties are
[localizable](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n

\n`name`

\n    String: The search engine's name, displayed to the user.

\n`search_url`

\n    String: URL used by the search engine. This must be an HTTPS URL.

\n`is_default`

\n    Boolean: True if the search engine should be the default choice.

\n`alternate_urls Optional`

\n    Array of String: An array of alternative URLs that can be used instead
of `search_url`.

\n`encoding Optional`

\n    String: Encoding of the search term, specified as a [standard character
encoding name](https://www.iana.org/assignments/character-sets/character-
sets.xhtml), such as "UTF-8".

\n`favicon_url Optional`

\n    String: URL pointing to an icon for the search engine. This must be a
absolute HTTP or HTTPS URL.

\n`image_url Optional`

\n    String: URL used for image search.

\n`image_url_post_params Optional`

\n    String: POST parameters to send to `image_url`.

\n`instant_url Optional`

\n    String: URL used for instant search.

\n`instant_url_post_params Optional`

\n    String: POST parameters to send to `instant_url`.

\n`keyword Optional`

\n    String: Address bar keyword for the search engine.

\n`prepopulated_id Optional`

\n    The ID of a built-in search engine to use.

\n`search_url_post_params Optional`

\n    String: POST parameters to send to `search_url`.

\n`suggest_url Optional`

\n    String: URL used for search suggestions.

\n`suggest_url_post_params Optional`

\n    String: POST parameters to send to `suggest_url`.

\n\n\n  
\n\n\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 55| \n No| \n No  
`homepage`| \n Yes| \n No| 55| \n No| \n No  
`search_provider`| \n Yes| \n No| 55| \n No| \n No  
`search_provider.alternate_urls`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.encoding`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.favicon_url`| \n Yes| \n No| 55| \n No| \n No  
`search_provider.image_url`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.image_url_post_params`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.instant_url`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.instant_url_post_params`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.is_default`| \n Yes| \n No| 571| \n No| \n No  
`search_provider.keyword`| \n Yes| \n No| 55| \n No| \n No  
`search_provider.name`| \n Yes| \n No| 55| \n No| \n No  
`search_provider.prepopulated_id`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.search_url`| \n Yes| \n No| 55| \n No| \n No  
`search_provider.search_url_post_params`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.suggest_url`| \n Yes| \n No| \n No| \n No| \n No  
`search_provider.suggest_url_post_params`| \n Yes| \n No| \n No| \n No| \n No  
`startup_pages`| \n Yes| \n No| \n No| \n No| \n No  
  
1\. Only built-in engines can be set as default.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`homepage`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
55| \nNo support\n\n No| \nNo support\n\n No  
`search_provider`| \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n55| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.alternate_urls`| \nFull support\n\n Yes| \nNo support\n\n No|
\nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.encoding`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.favicon_url`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.image_url`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.image_url_post_params`| \nFull support\n\n Yes| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.instant_url`| \nFull support\n\n Yes| \nNo support\n\n No|
\nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.instant_url_post_params`| \nFull support\n\n Yes| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.is_default`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __Only built-in engines can be set as default.
|  \nNo support\n\n No| \nNo support\n\n No  
`search_provider.keyword`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.name`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.prepopulated_id`| \nFull support\n\n Yes| \nNo support\n\n
No| \nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.search_url`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.search_url_post_params`| \nFull support\n\n Yes| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.suggest_url`| \nFull support\n\n Yes| \nNo support\n\n No|
\nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`search_provider.suggest_url_post_params`| \nFull support\n\n Yes| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`startup_pages`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nNo support\n\n No| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

