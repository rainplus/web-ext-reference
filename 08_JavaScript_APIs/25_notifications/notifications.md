[



Display notifications to the user, using the underlying operating system's
notification mechanism. Because this API uses the operating system's
notification mechanism, the details of how notifications appear and behave may
differ according to the operating system and the user's settings.



To use this API you need to have the "notifications" [permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions).



## Types



[`notifications.NotificationOptions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/NotificationOptions "The documentation
about this has not yet been written; please consider contributing!")

    Defines the content of a notification.

[`notifications.TemplateType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/TemplateType "This is a string, and
represents the type of notification to create. There are four types of
notification: "basic", "image", "list", "progress".")

    The type of notification. For example, this defines whether the
notification can contain an image.



## Functions



[`notifications.clear()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/clear "Clears a notification, given its
ID.")

    Clear a specific notification, given its ID.

[`notifications.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/create "Creates and displays a
notification.")

    Create and display a new notification.

[`notifications.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/getAll "Gets all currently active
notifications created by the extension.")

    Get all notifications.

[`notifications.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/update "Updates a notification, given its
ID.")

    Update a notification.



## Events



[`notifications.onButtonClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onButtonClicked "Fired when the user
clicks one of the notification's buttons.")

    Fired when the user clicked a button in the notification.

[`notifications.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onClicked "The documentation about this
has not yet been written; please consider contributing!")

    Fired when the user clicked the notification, but not on a button.

[`notifications.onClosed`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onClosed "Fired when a notification is
closed, either by the system or by the user.")

    Fired when a notification closed, either by the system or because the
user dismissed it.

[`notifications.onShown`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/onShown "Fired immediately after a
notification has been shown.")

    Fired immediately after a notification has been shown.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`NotificationOptions`|  Yes|  No| 45 *| 48 *|  Yes  
`TemplateType`|  Yes|  No| 45 *| 48 *|  Yes *  
`clear`|  Yes|  No| 45| 48|  Yes  
`create`|  Yes|  No| 45| 48|  Yes  
`getAll`|  Yes|  No| 45| 48|  Yes  
`onButtonClicked`|  Yes|  No|  No|  No|  Yes  
`onClicked`|  Yes|  No| 47| 48|  Yes  
`onClosed`|  Yes|  No| 45 *| 48 *|  Yes  
`onShown`|  No|  No| 56| 56|  No  
`update`|  Yes|  No|  No|  No|  Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`NotificationOptions`|  Full support Yes| No support No| Full
support 45

Notes __

Full support 45

Notes __

     Notes __Only 'type', 'iconUrl', 'title', and 'message' are supported.
|  Full support Yes| Full support 48

Notes __

Full support 48

Notes __

     Notes __Only 'type', 'iconUrl', 'title', and 'message' are supported.  
`TemplateType`|  Full support Yes| No support No| Full
support 45

Notes __

Full support 45

Notes __

     Notes __Only the 'basic' type is supported.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Only the 'basic' type is supported.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Only the 'basic' type is supported.  
`clear`|  Full support Yes| No support No| Full support 45|
Full support Yes| Full support 48  
`create`| Full support Yes| No support No| Full support 45|
Full support Yes| Full support 48  
`getAll`| Full support Yes| No support No| Full support 45|
Full support Yes| Full support 48  
`onButtonClicked`| Full support Yes| No support No| No
support No| Full support Yes| No support No  
`onClicked`| Full support Yes| No support No| Full support
47| Full support Yes| Full support 48  
`onClosed`| Full support Yes| No support No| Partial
support45| Full support Yes| Partial support48  
`onShown`| No support No| No support No| Full support 56|
No support No| Full support 56  
`update`| Full support Yes| No support No| No support No|
Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Not supported on Macs.
|  No support No  
  


## Example extensions

  * [embedded-webextension-sdk](https://github.com/mdn/webextensions-examples/tree/master/embedded-webextension-sdk)
  * [export-helpers](https://github.com/mdn/webextensions-examples/tree/master/export-helpers)
  * [forget-it](https://github.com/mdn/webextensions-examples/tree/master/forget-it)
  * [google-userinfo](https://github.com/mdn/webextensions-examples/tree/master/google-userinfo)
  * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.notifications`](https://developer.chrome.com/extensions/notifications)
API.



]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

