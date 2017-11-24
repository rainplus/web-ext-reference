[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"omnibox": {\n\xa0 "keyword": "mdn"\n}

\n\n  
\n\n\n

Use the `omnibox` key to define an omnibox keyword for your extension.

\n

When the user types this keyword into the browser's address bar, followed by a
space, then any subsequent characters will be sent to the extension using the
`[omnibox](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox)` API. The
extension will then be able to populate the address bar's drop-down
suggestions list with its own suggestions.

\n

If two or more extensions define the same keyword, then the extension that was
installed last gets to control the keyword. Any previously installed
extensions that defined the same keyword will no longer be able to use the
`omnibox` API.

\n

## Example

\n

    
    
    "omnibox": {\n  "keyword": "mdn"\n}

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 52| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

