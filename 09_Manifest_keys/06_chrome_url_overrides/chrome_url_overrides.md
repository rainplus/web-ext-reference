[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n\xa0 "chrome_url_overrides" : {\n\xa0\xa0\xa0 "newtab": "my-new-tab.html"\n\xa0 }

\n\n  
\n\n\n

Use the `chrome_url_overrides` key to provide a custom replacement for the
documents loaded into various special pages usually provided by the browser
itself.

\n

## Syntax

\n

The `chrome_url_overrides` key is an object that may have the following
properties:

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`bookmark`\n| `String`\n| \n

Provide a replacement for the page that shows the bookmarks.\xa0

\n\n  
\n\n`history`\n| `String`\n| \n

Provide a replacement for the page that shows the browsing history.\xa0

\n\n  
\n\n`newtab`\n| `String`\n| \n

Provide a replacement for the document that's shown in the "new tab" page.
This is the page that's shown when the user has opened a new tab but has not
loaded any document into it: for example, by using the Ctrl/Command+T keyboard
shortcut.

\n

The replacement is given as a URL to an HTML file. The file must be bundled
with the extension: you can't specify a remote URL here. You can specify it
relative to the extension's root folder, like: "path/to/newtab.html".

\n

The document can load CSS and JavaScript, just like a normal web page.
JavaScript running in the page gets access to the same [privileged "browser.*"
APIs](/en-US/Add-ons/WebExtensions/API) as the extension's background script.

\n

It's very good practice to include a [<title>](/en-
US/docs/Web/HTML/Element/title) for the page, or the tab's title will be the
"moz-extension://..." URL.

\n

A common use case is to let the user define a new tab page: to do this,
provide a custom new tab page that navigates to the page the user defined.

\n

If two or more extensions both define custom new tab pages, then the last one
to be installed or enabled gets to use its value.

\n

To override the browser's homepage, use "[chrome_settings_overrides](/en-
US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/chrome_settings_overrides)" instead.

\n\n  
\n\n\n

All properties are [localizable](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n

## Example

\n

    
    
    "chrome_url_overrides" : {\n  "newtab": "my-new-tab.html"\n}

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 54| \n No| \n Yes  
`newtab`| \n Yes1| \n No| 541| \n No| \n Yes1  
`bookmarks`| \n Yes| \n No| \n No| \n No| \n Yes  
`history`| \n Yes| \n No| \n No| \n No| \n Yes  
  
1\. If two or more extensions both define a custom new tab page, then in
Firefox the first extension to run wins. In Chrome and Opera, the last
extension wins.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n Yes| \nNo support\n\n No  
`newtab`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If two or more extensions both define a custom new tab page, then in Firefox the first extension to run wins. In Chrome and Opera, the last extension wins.
|  \nNo support\n\n No| \nFull support\n\n 54

Notes __

\nFull support\n\n 54

Notes __

     Notes __If two or more extensions both define a custom new tab page, then in Firefox the first extension to run wins. In Chrome and Opera, the last extension wins.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If two or more extensions both define a custom new tab page, then in Firefox the first extension to run wins. In Chrome and Opera, the last extension wins.
|  \nNo support\n\n No  
`bookmarks`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`history`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

