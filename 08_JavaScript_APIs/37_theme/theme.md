Enables browser extensions to update the browser theme.

To use this API, an extension must request the "theme" [permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions) in its[
manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file.

## Types

[`theme.Theme`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme/Theme "A
Theme object represents the specification of a theme.")

    Represents the content of a theme.

## Functions

[`theme.getCurrent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/theme/getCurrent "Gets the currently used theme as a
Theme object.")

    Gets the current browser theme.
[`theme.update()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme/update
"Updates the browser theme according to the content of given Theme object.")

    Updates the browser’s theme.
[`theme.reset()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme/reset
"Resets any theme that was applied using the theme.update\(\) method.")

    Removes any theme updates made in a call to [`theme.update()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme/update "Updates the browser theme according to the content of given Theme object.").

## Events

[`theme.onUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/theme/onUpdated "Fires when a theme supplied as a
browser extension is applied or removed. Specifically:")

    Fired when the browser theme has been changed.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Theme`|  No|  No| 55|  No|  No  
`getCurrent`|  No|  No| 58|  No|  No  
`onUpdated`|  No|  No| 58|  No|  No  
`reset`|  No|  No| 56 *|  No|  No  
`update`|  No|  No| 55 *|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Theme`|  No support No|  No support No|  Full support 55|  No support No|  No
support No  
`getCurrent`|  No support No|  No support No|  Full support 58|  No support
No|  No support No  
`onUpdated`|  No support No|  No support No|  Full support 58|  No support No|
No support No  
`reset`|  No support No|  No support No|  Partial support 56|  No support No|
No support No  
`update`|  No support No|  No support No|  Partial support 55|  No support No|
No support No  
  
## Example extensions

  * [dynamic-theme](https://github.com/mdn/webextensions-examples/tree/master/dynamic-theme)

  *[
 No support

]: No support

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[
Partial support

]: Partial support

  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

