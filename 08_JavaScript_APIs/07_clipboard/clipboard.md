The clipboard API enables an extension to copy items to the system clipboard.
Currently the API only supports copying images, but it's intended to support
copying text and HTML in the future.

This WebExtension API exists primarily because the standard web clipboard API
[doesn't support writing images to the clipboard](https://w3c.github.io
/clipboard-apis/#writing-to-clipboard). If and when this capability is added
to the standard web API, this API may be deprecated.

Reading from the clipboard is not supported by this API, because the clipboard
can already be read using the standard web platform APIs. See [Interacting
with the clipboard](/en-US/Add-
ons/WebExtensions/Interact_with_the_clipboard#Reading_from_the_clipboard).

This API is based on Chrome's
`[clipboard](https://developer.chrome.com/apps/clipboard)` API, but that API
is only available for Chrome apps, not extensions.

To use this API you need to have the "clipboardWrite" [permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions).

## Functions

[`clipboard.setImageData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/clipboard/setImageData "Copies an image to the
clipboard. The image is re-encoded before it is written to the clipboard. If
the image is invalid, the clipboard is not modified.")

    Copy an image to the clipboard.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`setImageData`|  No|  No| 57| 57|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`setImageData`|  No support No|  No support No|  Full support 57|  No support
No|  Full support 57  
  
**Acknowledgements**

This API is based on Chromium's
[`chrome.clipboard`](https://developer.chrome.com/apps/clipboard) API.

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
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

