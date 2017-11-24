[\n

\n

The manifest.json file is a [JSON](/en-US/docs/Glossary/JSON)-formatted file,
and is the only file that every extension using WebExtension APIs must
contain.

\n

Using manifest.json, you specify basic metadata about your extension such as
the name and version, and can also specify aspects of your extension's
functionality, such as background scripts, content scripts, and browser
actions.

\n

manifest.json keys are listed below:

\n

  * [applications](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications)
  * [author](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/author)
  * [background](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/background)
  * [browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)
  * [chrome_settings_overrides](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/chrome_settings_overrides)
  * [chrome_url_overrides](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/chrome_url_overrides)
  * [commands](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands)
  * [content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)
  * [content_security_policy](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_security_policy)
  * [default_locale](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/default_locale)
  * [description](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/description)
  * [developer](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/developer)
  * [devtools_page](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/devtools_page)
  * [homepage_url](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/homepage_url)
  * [icons](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/icons)
  * [incognito](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/incognito)
  * [manifest_version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/manifest_version)
  * [name](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/name)
  * [omnibox](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox)
  * [optional_permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/optional_permissions)
  * [options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)
  * [page_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)
  * [permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)
  * [protocol_handlers](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/protocol_handlers)
  * [short_name](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/short_name)
  * [sidebar_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/sidebar_action)
  * [theme](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme)
  * [version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version)
  * [web_accessible_resources](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/web_accessible_resources)

\n

\xa0

\n

`"manifest_version"`, `"version"`, and `"name"` are the only mandatory keys.
`"default_locale"` must be present if the "_locales" directory is present and
must be absent otherwise. `"applications"` is not supported in Google Chrome,
and is mandatory in Firefox before Firefox 48 and Firefox for Android.

\n

You can access your extension's manifest from the extension's JavaScript using
the [`runtime.getManifest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getManifest "None.") function:

\n

    
    
    browser.runtime.getManifest().version;

\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`applications`| \n No| \n No| 48| 48| \n No  
`author`| \n Yes| \n Yes1| 52| 52| \n Yes  
`background`| \n Yes| \n Yes2| 48| 48| \n Yes  
`browser_action`| \n Yes| \n Yes| 48| 55| \n Yes  
`chrome_settings_overrides`| \n Yes| \n No| 55| \n No| \n No  
`chrome_url_overrides`| \n Yes| \n No| 54| \n No| \n Yes  
`commands`| \n Yes| \n No| 48| \n No| \n Yes  
`content_scripts`| \n Yes3| \n Yes| 484| 484| \n Yes3  
`content_security_policy`| \n Yes| \n Yes5| 486| 486| \n Yes  
`default_locale`| \n Yes| \n Yes| 48| 48| \n Yes  
`description`| \n Yes| \n Yes| 48| 48| \n Yes  
`developer`| \n No| \n No| 52| 52| \n Yes  
`devtools_page`| \n Yes| \n No| 54| \n No| \n Yes  
`homepage_url`| \n Yes| \n No| 48| 48| \n Yes  
`icons`| \n Yes| \n Yes| 48| 48| \n Yes  
`incognito`| \n Yes| \n No| 48| 48| \n Yes  
`manifest_version`| \n Yes| \n Yes| 48| 48| \n Yes  
`name`| \n Yes| \n Yes| 48| 48| \n Yes  
`omnibox`| \n Yes| \n No| 52| \n No| \n Yes  
`optional_permissions`| \n Yes| \n No| 55| 55| \n Yes  
`options_ui`| \n Yes| \n No| 52| \n No| \n Yes  
`page_action`| \n Yes7| \n Yes7 8| 48| \n No| \n Yes  
`permissions`| \n Yes| \n Yes| 48| 48| \n Yes  
`protocol_handlers`| \n No| \n No| 54| 54| \n No  
`short_name`| \n Yes| \n Yes| 48| 48| \n Yes  
`sidebar_action`| \n No| \n No| 54| \n No| \n Yes  
`theme`| \n Yes| \n No| 55| \n No| \n No  
`version`| \n Yes9| \n Yes| 48| 48| \n Yes  
`web_accessible_resources`| \n Yes| \n Yes| 48| 48| \n Yes  
  
1\. This key is mandatory in Microsoft Edge.

2\. The 'persistent' property is mandatory.

3\. Content scripts are not applied to tabs already open when the extension is
loaded.

4\. Content scripts won't be injected into empty iframes at 'document_start'
even if you specify that value in 'run_at'.

5\. Only the default content security policy is supported: "script-src 'self';
object-src 'self';".

6\. Firefox does not support 'http://127.0.0.1' or 'http://localhost' as
script sources: they must be served over HTTPS.

7\. SVG icons are not supported.

8\. 'default_icon' must be an object, with explicit sizes.

9\. Valid Chrome versions are a subset of valid Firefox versions.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`applications`|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
48| \nNo support\n\n No| \nFull support\n\n 48  
`author`| \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __This key is mandatory in Microsoft Edge.
|  \nFull support\n\n 52| \nFull support\n\n Yes| \nFull support\n\n 52  
`background`| \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __The 'persistent' property is mandatory.
|  \nPartial support\n48| \nFull support\n\n Yes| \nPartial support\n48  
`browser_action`| \nPartial support\nPartial| \nPartial support\nPartial|
\nPartial support\n48| \nPartial support\nPartial| \nPartial support\n55  
`chrome_settings_overrides`| \nFull support\n\n Yes| \nNo support\n\n No|
\nPartial support\n55| \nNo support\n\n No| \nNo support\n\n No  
`chrome_url_overrides`| \nPartial support\nPartial| \nNo support\n\n No|
\nPartial support\n54| \nPartial support\nPartial| \nNo support\n\n No  
`commands`| \nPartial support\nPartial| \nNo support\n\n No| \nPartial
support\n48| \nPartial support\nPartial| \nNo support\n\n No  
`content_scripts`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  \nFull support\n\n Yes| \nPartial support\n48

Notes __

\nPartial support\n48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  \nPartial support\n48

Notes __

\nPartial support\n48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.  
`content_security_policy`|  \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Only the default content security policy is supported: "script-src 'self'; object-src 'self';".
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Firefox does not support 'http://127.0.0.1' or 'http://localhost' as script sources: they must be served over HTTPS.
|  \nFull support\n\n Yes| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Firefox does not support 'http://127.0.0.1' or 'http://localhost' as script sources: they must be served over HTTPS.  
`default_locale`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`description`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`developer`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 52|
\nFull support\n\n Yes| \nFull support\n\n 52  
`devtools_page`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n Yes| \nNo support\n\n No  
`homepage_url`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`icons`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
48| \nFull support\n\n Yes| \nFull support\n\n 48  
`incognito`| \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n48| \nFull support\n\n Yes| \nPartial support\n48  
`manifest_version`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`name`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n 48|
\nFull support\n\n Yes| \nFull support\n\n 48  
`omnibox`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 52|
\nFull support\n\n Yes| \nNo support\n\n No  
`optional_permissions`| \nPartial support\nPartial| \nNo support\n\n No|
\nPartial support\n55| \nPartial support\nPartial| \nPartial support\n55  
`options_ui`| \nPartial support\nPartial| \nNo support\n\n No| \nPartial
support\n52| \nPartial support\nPartial| \nNo support\n\n No  
`page_action`| \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __SVG icons are not supported.
|  \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __SVG icons are not supported.
     Notes __'default_icon' must be an object, with explicit sizes.
|  \nFull support\n\n 48| \nPartial support\nPartial| \nNo support\n\n No  
`permissions`| \nFull support\n\n Yes| \nPartial support\nPartial| \nPartial
support\n48| \nFull support\n\n Yes| \nPartial support\n48  
`protocol_handlers`| \nNo support\n\n No| \nNo support\n\n No| \nPartial
support\n54| \nNo support\n\n No| \nPartial support\n54  
`short_name`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`sidebar_action`| \nNo support\n\n No| \nNo support\n\n No| \nPartial
support\n54| \nPartial support\nPartial| \nNo support\n\n No  
`theme`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55|
\nNo support\n\n No| \nNo support\n\n No  
`version`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Valid Chrome versions are a subset of valid Firefox versions.
|  \nFull support\n\n Yes| \nFull support\n\n 48| \nFull support\n\n Yes|
\nFull support\n\n 48  
`web_accessible_resources`| \nFull support\n\n Yes| \nFull support\n\n Yes|
\nFull support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
  
\n

## Example

\n

Quick syntax example for manifest.json:

\n

    
    
    {\n  "applications": {\n    "gecko": {\n      "id": "addon@example.com",\n      "strict_min_version": "42.0"\n    }\n  },\n\n  "background": {\n    "scripts": ["jquery.js", "my-background.js"],\n    "page": "my-background.html"\n  },\n\n  "browser_action": {\n    "default_icon": {\n      "19": "button/geo-19.png",\n      "38": "button/geo-38.png"\n    },\n    "default_title": "Whereami?",\n    "default_popup": "popup/geo.html"\n  },\n\n  "commands": {\n    "toggle-feature": {\n\xa0     "suggested_key": {\n\xa0\xa0\xa0     "default": "Ctrl+Shift+Y",\n\xa0\xa0\xa0     "linux": "Ctrl+Shift+U"\n\xa0     },\n  \xa0\xa0\xa0 "description": "Send a 'toggle-feature' event"\n    }\n  },\n\n  "content_security_policy": "script-src 'self' https://example.com; object-src 'self'",\n\n  "content_scripts": [\n    {\n      "exclude_matches": ["*://developer.mozilla.org/*"],\n      "matches": ["*://*.mozilla.org/*"],\n      "js": ["borderify.js"]\n    }\n  ],\n\n  "default_locale": "en",\n\n  "description": "...",\n\n  "icons": {\n    "48": "icon.png",\n    "96": "icon@2x.png"\n  },\n\n  "manifest_version": 2,\n\n  "name": "...",\n\n  "page_action": {\n    "default_icon": {\n      "19": "button/geo-19.png",\n      "38": "button/geo-38.png"\n    },\n    "default_title": "Whereami?",\n    "default_popup": "popup/geo.html"\n  },\n\n  "permissions": ["webNavigation"],\n\n  "version": "0.1",\n\n  "web_accessible_resources": ["images/my-image.png"]\n}

\n

\xa0

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
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

