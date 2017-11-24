Enables an extension to modify certain global browser settings. Each property
of this API is a [`BrowserSetting`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/types/BrowserSetting "A BrowserSetting is an object
representing a browser setting.") object, providing the ability to modify a
particular setting.



Because these are global settings, it's possible for extensions to conflict.
See the documentation for `[BrowserSetting.set()](/en-US/Add-
ons/WebExtensions/API/types/BrowserSetting/set)` for details of how conflicts
are handled.



To use this API you need to have the "browserSettings"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

## Properties

[`browserSettings.allowPopupsForUserEvents`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/allowPopupsForUserEvents "A
BrowserSetting object that can be used to enable or disable the ability of web
pages to open popups in response to user actions.")

    Determines whether code running in web pages can display popups in response to user events.
[`browserSettings.cacheEnabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/cacheEnabled "A BrowserSetting object
that can be used to globally enable or disable the browser cache.")

    Determines whether the browser cache is enabled or not.
[`browserSettings.homepageOverride`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/homepageOverride "A BrowserSetting
object that can be used to get a string representing the URL currently set as
the browser's homepage.")

    Read the value of the browser's home page.
[`browserSettings.imageAnimationBehavior`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/imageAnimationBehavior "A BrowserSetting
object that can be used to change the way the browser handles animated images,
such as GIFs.")

    Determines how the browser treats animated images.
[`browserSettings.newTabPageOverride`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/newTabPageOverride "A BrowserSetting
object that can be used to get a string representing the URL for the "new tab"
page: that is, the page that's loaded when the user opens a new empty tab.")

    Read the value of the browser's new tab page.
[`browserSettings.webNotificationsDisabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserSettings/webNotificationsDisabled "A
BrowserSetting object that can be used to prevent websites from showing
notifications using the Notifications Web API.")

    Prevents websites from showing notifications using the `[Notification](/en-US/docs/Web/API/notification)` Web API.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`allowPopupsForUserEvents`|  No|  No| 57| 57|  No  
`cacheEnabled`|  No|  No| 56| 56|  No  
`homepageOverride`|  No|  No| 57| 57|  No  
`imageAnimationBehavior`|  No|  No| 57| 57|  No  
`newTabPageOverride`|  No|  No| 57| 57|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`allowPopupsForUserEvents`|  No support No|  No support No|  Full support 57|
No support No|  Full support 57  
`cacheEnabled`|  No support No|  No support No|  Full support 56|  No support
No|  Full support 56  
`homepageOverride`|  No support No|  No support No|  Full support 57|  No
support No|  Full support 57  
`imageAnimationBehavior`|  No support No|  No support No|  Full support 57|
No support No|  Full support 57  
`newTabPageOverride`|  No support No|  No support No|  Full support 57|  No
support No|  Full support 57

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

