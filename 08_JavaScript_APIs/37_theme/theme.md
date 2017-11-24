[\n

\n

Enables browser extensions to update the browser theme.

\n

To use this API, an extension must request the "theme" [permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions) in its[
manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file.

\n

## Types

\n

\n[`theme.Theme`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme/Theme "A
Theme object represents the specification of a theme.")

\n    Represents the content of a theme.

\n\n

## Functions

\n

\n[`theme.getCurrent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/theme/getCurrent "Gets the currently used theme as a
Theme object.")

\n    Gets the current browser theme.

\n[`theme.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/theme/update "Updates the browser theme according to the
content of given Theme object.")

\n    Updates the browser\u2019s theme.

\n[`theme.reset()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme/reset
"Resets any theme that was applied using the theme.update\(\) method.")

\n    Removes any theme updates made in a call to [`theme.update()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/theme/update "Updates the browser
theme according to the content of given Theme object.").

\n\n

## Events

\n

\n[`theme.onUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/theme/onUpdated "Fires when a theme supplied as a
browser extension is applied or removed. Specifically:")

\n    Fired when the browser theme has been changed.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Theme`| \n No| \n No| 55| \n No| \n No  
`getCurrent`| \n No| \n No| 58| \n No| \n No  
`onUpdated`| \n No| \n No| 58| \n No| \n No  
`reset`| \n No| \n No| 56 *| \n No| \n No  
`update`| \n No| \n No| 55 *| \n No| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Theme`|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 55|
\nNo support\n\n No| \nNo support\n\n No  
`getCurrent`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 58|
\nNo support\n\n No| \nNo support\n\n No  
`onUpdated`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 58|
\nNo support\n\n No| \nNo support\n\n No  
`reset`| \nNo support\n\n No| \nNo support\n\n No| \nPartial support\n56| \nNo
support\n\n No| \nNo support\n\n No  
`update`| \nNo support\n\n No| \nNo support\n\n No| \nPartial support\n55|
\nNo support\n\n No| \nNo support\n\n No  
  
\n

## Example extensions

  * [dynamic-theme](https://github.com/mdn/webextensions-examples/tree/master/dynamic-theme)

\n]

  *[\nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

