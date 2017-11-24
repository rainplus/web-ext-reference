[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"developer": {\n  "name": "Walt Whitman",\n  "url": "https://en.wikipedia.org/wiki/Walt_Whitman"\n}

\n\n  
\n\n\n

The name of the extension's developer and their homepage URL, intended for
display in the browser's user interface.

\n

The object, and both of its properties, are optional. The "name" and "url"
properties, if present, will override the\xa0 [author](/en-US/Add-
ons/WebExtensions/manifest.json/author) and [homepage_url](/en-US/Add-
ons/WebExtensions/manifest.json/homepage_url) keys, respectively. This object
only allows for a single developer name and URL to be specified.

\n

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n

## Example

\n

    
    
    "developer": {\n  "name": "Walt Whitman",\n  "url": "https://en.wikipedia.org/wiki/Walt_Whitman"\n}

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n No| \n No| 52| 52| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
52| \nFull support\n\n Yes| \nFull support\n\n 52  
  
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

