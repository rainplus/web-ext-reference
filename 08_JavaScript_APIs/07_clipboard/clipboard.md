[\n

\n

The clipboard API enables an extension to copy items to the system clipboard.
Currently the API only supports copying images, but it's intended to support
copying text and HTML in the future.

\n

This WebExtension API exists primarily because the standard web clipboard API
[doesn't support writing images to the clipboard](https://w3c.github.io
/clipboard-apis/#writing-to-clipboard). If and when this capability is added
to the standard web API, this API may be deprecated.

\n

Reading from the clipboard is not supported by this API, because the clipboard
can already be read using the standard web platform APIs. See [Interacting
with the clipboard](/en-US/Add-
ons/WebExtensions/Interact_with_the_clipboard#Reading_from_the_clipboard).

\n

This API is based on Chrome's
`[clipboard](https://developer.chrome.com/apps/clipboard)` API, but that API
is only available for Chrome apps, not extensions.

\n

To use this API you need to have the "clipboardWrite" [permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions).

\n

## Functions

\n

\n[`clipboard.setImageData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/clipboard/setImageData "Copies an image to the
clipboard. The image is re-encoded before it is written to the clipboard. If
the image is invalid, the clipboard is not modified.")

\n    Copy an image to the clipboard.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`setImageData`| \n No| \n No| 57| 57| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`setImageData`|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
57| \nNo support\n\n No| \nFull support\n\n 57  
  
\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.clipboard`](https://developer.chrome.com/apps/clipboard) API.

\n

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

