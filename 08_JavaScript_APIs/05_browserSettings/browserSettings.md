[\n

\n

Enables an extension to modify certain global browser settings. Each property
of this API is a [`BrowserSetting`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/types/BrowserSetting "A BrowserSetting is an object
representing a browser setting.") object, providing the ability to modify a
particular setting.

\n

\xa0

\n

Because these are global settings, it's possible for extensions to conflict.
See the documentation for `[BrowserSetting.set()](/en-US/Add-
ons/WebExtensions/API/types/BrowserSetting/set)` for details of how conflicts
are handled.

\n

\xa0

\n

\n

To use this API you need to have the "browserSettings"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

\n

\n

## Properties

\n

\n[`browserSettings.allowPopupsForUserEvents`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/allowPopupsForUserEvents "A
BrowserSetting object that can be used to enable or disable the ability of web
pages to open popups in response to user actions.")

\n    Determines whether code running in web pages can display popups in
response to user events.

\n[`browserSettings.cacheEnabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/cacheEnabled "A BrowserSetting object
that can be used to globally enable or disable the browser cache.")

\n    Determines whether the browser cache is enabled or not.

\n[`browserSettings.homepageOverride`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/homepageOverride "A BrowserSetting
object that can be used to get a string representing the URL currently set as
the browser's homepage.")

\n    Read the value of the browser's home page.

\n[`browserSettings.imageAnimationBehavior`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/imageAnimationBehavior "A BrowserSetting
object that can be used to change the way the browser handles animated images,
such as GIFs.")

\n    Determines how the browser treats animated images.

\n[`browserSettings.newTabPageOverride`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/newTabPageOverride "A BrowserSetting
object that can be used to get a string representing the URL for the "new tab"
page: that is, the page that's loaded when the user opens a new empty tab.")

\n    Read the value of the browser's new tab page.

\n[`browserSettings.webNotificationsDisabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/webNotificationsDisabled "A
BrowserSetting object that can be used to prevent websites from showing
notifications using the Notifications Web API.")

\n    Prevents websites from showing notifications using the `[Notification
](/en-US/docs/Web/API/notification)` Web API.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`allowPopupsForUserEvents`| \n No| \n No| 57| 57| \n No  
`cacheEnabled`| \n No| \n No| 56| 56| \n No  
`homepageOverride`| \n No| \n No| 57| 57| \n No  
`imageAnimationBehavior`| \n No| \n No| 57| 57| \n No  
`newTabPageOverride`| \n No| \n No| 57| 57| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`allowPopupsForUserEvents`|  \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nFull support\n\n 57  
`cacheEnabled`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
56| \nNo support\n\n No| \nFull support\n\n 56  
`homepageOverride`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nFull support\n\n 57  
`imageAnimationBehavior`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nFull support\n\n 57  
`newTabPageOverride`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nFull support\n\n 57  
  
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

