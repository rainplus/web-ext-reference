[



The manifest.json file is a [JSON](/en-US/docs/Glossary/JSON)-formatted file,
and is the only file that every extension using WebExtension APIs must
contain.



Using manifest.json, you specify basic metadata about your extension such as
the name and version, and can also specify aspects of your extension's
functionality, such as background scripts, content scripts, and browser
actions.



manifest.json keys are listed below:



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



\xa0



`"manifest_version"`, `"version"`, and `"name"` are the only mandatory keys.
`"default_locale"` must be present if the "_locales" directory is present and
must be absent otherwise. `"applications"` is not supported in Google Chrome,
and is mandatory in Firefox before Firefox 48 and Firefox for Android.



You can access your extension's manifest from the extension's JavaScript using
the [`runtime.getManifest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getManifest "None.") function:



    
    
    browser.runtime.getManifest().version;



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`applications`|  No|  No| 48| 48|  No  
`author`|  Yes|  Yes1| 52| 52|  Yes  
`background`|  Yes|  Yes2| 48| 48|  Yes  
`browser_action`|  Yes|  Yes| 48| 55|  Yes  
`chrome_settings_overrides`|  Yes|  No| 55|  No|  No  
`chrome_url_overrides`|  Yes|  No| 54|  No|  Yes  
`commands`|  Yes|  No| 48|  No|  Yes  
`content_scripts`|  Yes3|  Yes| 484| 484|  Yes3  
`content_security_policy`|  Yes|  Yes5| 486| 486|  Yes  
`default_locale`|  Yes|  Yes| 48| 48|  Yes  
`description`|  Yes|  Yes| 48| 48|  Yes  
`developer`|  No|  No| 52| 52|  Yes  
`devtools_page`|  Yes|  No| 54|  No|  Yes  
`homepage_url`|  Yes|  No| 48| 48|  Yes  
`icons`|  Yes|  Yes| 48| 48|  Yes  
`incognito`|  Yes|  No| 48| 48|  Yes  
`manifest_version`|  Yes|  Yes| 48| 48|  Yes  
`name`|  Yes|  Yes| 48| 48|  Yes  
`omnibox`|  Yes|  No| 52|  No|  Yes  
`optional_permissions`|  Yes|  No| 55| 55|  Yes  
`options_ui`|  Yes|  No| 52|  No|  Yes  
`page_action`|  Yes7|  Yes7 8| 48|  No|  Yes  
`permissions`|  Yes|  Yes| 48| 48|  Yes  
`protocol_handlers`|  No|  No| 54| 54|  No  
`short_name`|  Yes|  Yes| 48| 48|  Yes  
`sidebar_action`|  No|  No| 54|  No|  Yes  
`theme`|  Yes|  No| 55|  No|  No  
`version`|  Yes9|  Yes| 48| 48|  Yes  
`web_accessible_resources`|  Yes|  Yes| 48| 48|  Yes  
  
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
`applications`|  No support No| No support No| Full support
48| No support No| Full support 48  
`author`| Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __This key is mandatory in Microsoft Edge.
|  Full support 52| Full support Yes| Full support 52  
`background`| Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __The 'persistent' property is mandatory.
|  Partial support48| Full support Yes| Partial support48  
`browser_action`| Partial supportPartial| Partial supportPartial|
Partial support48| Partial supportPartial| Partial support55  
`chrome_settings_overrides`| Full support Yes| No support No|
Partial support55| No support No| No support No  
`chrome_url_overrides`| Partial supportPartial| No support No|
Partial support54| Partial supportPartial| No support No  
`commands`| Partial supportPartial| No support No| Partial
support48| Partial supportPartial| No support No  
`content_scripts`| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  Full support Yes| Partial support48

Notes __

Partial support48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  Partial support48

Notes __

Partial support48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.  
`content_security_policy`|  Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Only the default content security policy is supported: "script-src 'self'; object-src 'self';".
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Firefox does not support 'http://127.0.0.1' or 'http://localhost' as script sources: they must be served over HTTPS.
|  Full support Yes| Full support 48

Notes __

Full support 48

Notes __

     Notes __Firefox does not support 'http://127.0.0.1' or 'http://localhost' as script sources: they must be served over HTTPS.  
`default_locale`|  Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 48  
`description`| Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 48  
`developer`| No support No| No support No| Full support 52|
Full support Yes| Full support 52  
`devtools_page`| Full support Yes| No support No| Full
support 54| Full support Yes| No support No  
`homepage_url`| Full support Yes| No support No| Full
support 48| Full support Yes| Full support 48  
`icons`| Full support Yes| Full support Yes| Full support
48| Full support Yes| Full support 48  
`incognito`| Full support Yes| No support No| Partial
support48| Full support Yes| Partial support48  
`manifest_version`| Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 48  
`name`| Full support Yes| Full support Yes| Full support 48|
Full support Yes| Full support 48  
`omnibox`| Full support Yes| No support No| Full support 52|
Full support Yes| No support No  
`optional_permissions`| Partial supportPartial| No support No|
Partial support55| Partial supportPartial| Partial support55  
`options_ui`| Partial supportPartial| No support No| Partial
support52| Partial supportPartial| No support No  
`page_action`| Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __SVG icons are not supported.
|  Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __SVG icons are not supported.
     Notes __'default_icon' must be an object, with explicit sizes.
|  Full support 48| Partial supportPartial| No support No  
`permissions`| Full support Yes| Partial supportPartial| Partial
support48| Full support Yes| Partial support48  
`protocol_handlers`| No support No| No support No| Partial
support54| No support No| Partial support54  
`short_name`| Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 48  
`sidebar_action`| No support No| No support No| Partial
support54| Partial supportPartial| No support No  
`theme`| Full support Yes| No support No| Full support 55|
No support No| No support No  
`version`| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Valid Chrome versions are a subset of valid Firefox versions.
|  Full support Yes| Full support 48| Full support Yes|
Full support 48  
`web_accessible_resources`| Full support Yes| Full support Yes|
Full support 48| Full support Yes| Full support 48  
  


## Example



Quick syntax example for manifest.json:



    
    
    {  "applications": {    "gecko": {      "id": "addon@example.com",      "strict_min_version": "42.0"    }  },  "background": {    "scripts": ["jquery.js", "my-background.js"],    "page": "my-background.html"  },  "browser_action": {    "default_icon": {      "19": "button/geo-19.png",      "38": "button/geo-38.png"    },    "default_title": "Whereami?",    "default_popup": "popup/geo.html"  },  "commands": {    "toggle-feature": {\xa0     "suggested_key": {\xa0\xa0\xa0     "default": "Ctrl+Shift+Y",\xa0\xa0\xa0     "linux": "Ctrl+Shift+U"\xa0     },  \xa0\xa0\xa0 "description": "Send a 'toggle-feature' event"    }  },  "content_security_policy": "script-src 'self' https://example.com; object-src 'self'",  "content_scripts": [    {      "exclude_matches": ["*://developer.mozilla.org/*"],      "matches": ["*://*.mozilla.org/*"],      "js": ["borderify.js"]    }  ],  "default_locale": "en",  "description": "...",  "icons": {    "48": "icon.png",    "96": "icon@2x.png"  },  "manifest_version": 2,  "name": "...",  "page_action": {    "default_icon": {      "19": "button/geo-19.png",      "38": "button/geo-38.png"    },    "default_title": "Whereami?",    "default_popup": "popup/geo.html"  },  "permissions": ["webNavigation"],  "version": "0.1",  "web_accessible_resources": ["images/my-image.png"]}



\xa0

]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[ Partial support]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

