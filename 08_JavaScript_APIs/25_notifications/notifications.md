[\n

\n

Display notifications to the user, using the underlying operating system's
notification mechanism. Because this API uses the operating system's
notification mechanism, the details of how notifications appear and behave may
differ according to the operating system and the user's settings.

\n

To use this API you need to have the "notifications" [permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions).

\n

## Types

\n

\n[`notifications.NotificationOptions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/NotificationOptions "The documentation
about this has not yet been written; please consider contributing!")

\n    Defines the content of a notification.

\n[`notifications.TemplateType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/TemplateType "This is a string, and
represents the type of notification to create. There are four types of
notification: "basic", "image", "list", "progress".")

\n    The type of notification. For example, this defines whether the
notification can contain an image.

\n\n

## Functions

\n

\n[`notifications.clear()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/clear "Clears a notification, given its
ID.")

\n    Clear a specific notification, given its ID.

\n[`notifications.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/create "Creates and displays a
notification.")

\n    Create and display a new notification.

\n[`notifications.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/getAll "Gets all currently active
notifications created by the extension.")

\n    Get all notifications.

\n[`notifications.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/update "Updates a notification, given its
ID.")

\n    Update a notification.

\n\n

## Events

\n

\n[`notifications.onButtonClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onButtonClicked "Fired when the user
clicks one of the notification's buttons.")

\n    Fired when the user clicked a button in the notification.

\n[`notifications.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onClicked "The documentation about this
has not yet been written; please consider contributing!")

\n    Fired when the user clicked the notification, but not on a button.

\n[`notifications.onClosed`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onClosed "Fired when a notification is
closed, either by the system or by the user.")

\n    Fired when a notification closed, either by the system or because the
user dismissed it.

\n[`notifications.onShown`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onShown "Fired immediately after a
notification has been shown.")

\n    Fired immediately after a notification has been shown.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`NotificationOptions`| \n Yes| \n No| 45 *| 48 *| \n Yes  
`TemplateType`| \n Yes| \n No| 45 *| 48 *| \n Yes *  
`clear`| \n Yes| \n No| 45| 48| \n Yes  
`create`| \n Yes| \n No| 45| 48| \n Yes  
`getAll`| \n Yes| \n No| 45| 48| \n Yes  
`onButtonClicked`| \n Yes| \n No| \n No| \n No| \n Yes  
`onClicked`| \n Yes| \n No| 47| 48| \n Yes  
`onClosed`| \n Yes| \n No| 45 *| 48 *| \n Yes  
`onShown`| \n No| \n No| 56| 56| \n No  
`update`| \n Yes| \n No| \n No| \n No| \n Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`NotificationOptions`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Only 'type', 'iconUrl', 'title', and 'message' are supported.
|  \nFull support\n\n Yes| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Only 'type', 'iconUrl', 'title', and 'message' are supported.  
`TemplateType`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Only the 'basic' type is supported.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Only the 'basic' type is supported.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Only the 'basic' type is supported.  
`clear`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`create`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`getAll`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`onButtonClicked`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`onClicked`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nFull support\n\n 48  
`onClosed`| \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n45| \nFull support\n\n Yes| \nPartial support\n48  
`onShown`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 56|
\nNo support\n\n No| \nFull support\n\n 56  
`update`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Not supported on Macs.
|  \nNo support\n\n No  
  
\n

## Example extensions

  * [embedded-webextension-sdk](https://github.com/mdn/webextensions-examples/tree/master/embedded-webextension-sdk)
  * [export-helpers](https://github.com/mdn/webextensions-examples/tree/master/export-helpers)
  * [forget-it](https://github.com/mdn/webextensions-examples/tree/master/forget-it)
  * [google-userinfo](https://github.com/mdn/webextensions-examples/tree/master/google-userinfo)
  * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.notifications`](https://developer.chrome.com/extensions/notifications)
API.

\n

\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

