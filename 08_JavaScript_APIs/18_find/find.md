[



Finds text in a web page, and highlights matches.



To use this API you need to have the "find" [permission](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/permissions).



## Functions



[`find.find()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/find/find
"Searches for text in a tab.")

    Find text in a web page.

[`find.highlightResults()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/find/highlightResults "Highlights the results of a
previous call to find.find\(\).")

    Highlight the last set of matches found.

[`find.removeHighlighting()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/find/removeHighlighting "Remove any highlighting of a
previous search that was applied by a previous call to highlightResults\(\),
or by the browser's native UI.")

    Remove any highlighting.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`find`|  No|  No| 57|  No|  No  
`highlightResults`|  No|  No| 57|  No|  No  
`removeHighlighting`|  No|  No| 57|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`find`|  No support No| No support No| Full support 57| No
support No| No support No  
`highlightResults`| No support No| No support No| Full
support 57| No support No| No support No  
`removeHighlighting`| No support No| No support No| Full
support 57| No support No| No support No  
  
## Example extensions

  * [find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master/find-across-tabs)

]

  *[Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

