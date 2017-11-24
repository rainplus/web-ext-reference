Schedule code to run at a specific time in the future. This is like
`[setTimeout()](/en-US/docs/Web/API/WindowTimers/setTimeout)` and
`[setInterval()](/en-US/docs/Web/API/WindowTimers/setInterval)`, except that
those functions don't work with background pages that are loaded on demand.

To use this API you need to have the "alarms" [permission](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/permissions).

## Types

[`alarms.Alarm`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms/Alarm
"Information about a single alarm. This object is returned from alarms.get\(\)
and alarms.getAll\(\), and is passed into the alarms.onAlarm listener.")

    Information about a particular alarm.

## Functions

[`alarms.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/create "Creates a new alarm.")

    Create a new alarm.
[`alarms.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms/get
"Gets an alarm, given its name.")

    Retrieves a specific alarm, given its name.
[`alarms.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/getAll "Gets all active alarms for the
extension.")

    Retrieve all scheduled alarms.
[`alarms.clear()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms/clear
"Cancels an alarm, given its name.")

    Clear a specific alarm, given its name.
[`alarms.clearAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/clearAll "Cancels all active alarms.")

    Clear all scheduled alarms.

## Events

[`alarms.onAlarm`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/onAlarm "Fired when any alarm set by the
extension goes off.")

    Fired when an alarm goes off.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Alarm`|  Yes|  No| 45| 48|  Yes  
`clear`|  Yes|  No| 45| 48|  Yes  
`clearAll`|  Yes|  No| 45| 48|  Yes  
`create`|  Yes|  No| 45| 48|  Yes  
`get`|  Yes|  No| 45| 48|  Yes  
`getAll`|  Yes|  No| 45| 48|  Yes  
`onAlarm`|  Yes|  No| 45| 48|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Alarm`|  Full support Yes|  No support No|  Full support 45|  Full support
Yes|  Full support 48  
`clear`|  Full support Yes|  No support No|  Full support 45|  Full support
Yes|  Full support 48  
`clearAll`|  Full support Yes|  No support No|  Full support 45|  Full support
Yes|  Full support 48  
`create`|  Full support Yes|  No support No|  Full support 45|  Full support
Yes|  Full support 48  
`get`|  Full support Yes|  No support No|  Full support 45|  Full support Yes|
Full support 48  
`getAll`|  Full support Yes|  No support No|  Full support 45|  Full support
Yes|  Full support 48  
`onAlarm`|  Full support Yes|  No support No|  Full support 45|  Full support
Yes|  Full support 48  
  
## Example extensions

  * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out)
  * [dynamic-theme](https://github.com/mdn/webextensions-examples/tree/master/dynamic-theme)

**Acknowledgements**

This API is based on Chromium's
[`chrome.alarms`](https://developer.chrome.com/extensions/alarms) API.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

