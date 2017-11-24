[\n

\n

Finds text in a web page, and highlights matches.

\n

To use this API you need to have the "find" [permission](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/permissions).

\n

## Functions

\n

\n[`find.find()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/find/find
"Searches for text in a tab.")

\n    Find text in a web page.

\n[`find.highlightResults()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/find/highlightResults "Highlights the results of a
previous call to find.find\(\).")

\n    Highlight the last set of matches found.

\n[`find.removeHighlighting()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/find/removeHighlighting "Remove any highlighting of a
previous search that was applied by a previous call to highlightResults\(\),
or by the browser's native UI.")

\n    Remove any highlighting.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`find`| \n No| \n No| 57| \n No| \n No  
`highlightResults`| \n No| \n No| 57| \n No| \n No  
`removeHighlighting`| \n No| \n No| 57| \n No| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`find`|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 57| \nNo
support\n\n No| \nNo support\n\n No  
`highlightResults`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
`removeHighlighting`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
  
## Example extensions

  * [find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master/find-across-tabs)

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

