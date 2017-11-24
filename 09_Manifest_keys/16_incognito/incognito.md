[\n

\n\n\n\nType\n| `String`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"incognito": "spanning"

\n

    
    
    \n"incognito": "split"

\n

    
    
    \n"incognito": "not_allowed"

\n\n  
\n\n\n

Use the `incognito` key to control how the extension works with private
browsing windows.

\n

This is a string which may take any of the following values:

\n

\n

  * \n

"spanning" (the default): the extension will see events from private and non-
private windows and tabs. Windows and tabs will get an `incognito` property in
the `[Window](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/Window)`
or `[Tab](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/Tab)` that
represents them. This property indicates whether or not the object is private:

\n

    
        browser.windows.getLastFocused().then((windowInfo) => {\n  console.log(`Window is private: ${windowInfo.incognito}`);\n});

\n

\n

  * "split": the extension will be split between private and non-private windows. There are effectively two copies of the extension running: one sees only non-private windows, the other sees only private windows. Each copy has isolated access to Web APIs (so, for example, `[localStorage](/en-US/docs/Web/API/Storage/LocalStorage)` is not shared). However, the WebExtension API `[storage.local](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/local)` is shared.
\n

  * "not_allowed": private tabs and windows are invisible to the extension.
\n

\n

## Example

\n

    
    
    "incognito": "spanning"\n

\n

    
    
    "incognito": "split"\n

\n

    
    
    "incognito": "not_allowed"\n

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 48| 48| \n Yes  
`split`| \n Yes| \n No| \n No| \n No| \n Yes  
`not_allowed`| \n Yes| \n No| \n No| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`split`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`not_allowed`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
  
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

