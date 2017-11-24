[\n

\n\n\n\nType\n| `String`\n  
---|---  
\n\nMandatory\n| Contingent: must be present if the _locales subdirectory is
present, must be absent otherwise.\n  
\n\nExample\n| \n

    
    
    \n"default_locale": "en"

\n\n  
\n\n\n

This key must be present if the extension contains the _locales directory, and
must be absent otherwise. It identifies a subdirectory of _locales, and this
subdirectory will be used to find the default strings for your extension.

\n

See [Internationalization](/en-US/Add-ons/WebExtensions/Internationalization).

\n

## Example

\n

    
    
    "default_locale": "en"

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n Yes| 48| 48| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

