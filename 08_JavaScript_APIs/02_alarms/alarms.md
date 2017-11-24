[\n

\n

Schedule code to run at a specific time in the future. This is like
`[setTimeout()](/en-US/docs/Web/API/WindowTimers/setTimeout)` and
`[setInterval()](/en-US/docs/Web/API/WindowTimers/setInterval)`, except that
those functions don't work with background pages that are loaded on demand.

\n

To use this API you need to have the "alarms" [permission](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/permissions).

\n

## Types

\n

\n[`alarms.Alarm`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms/Alarm
"Information about a single alarm. This object is returned from alarms.get\(\)
and alarms.getAll\(\), and is passed into the alarms.onAlarm listener.")

\n    Information about a particular alarm.

\n\n

## Functions

\n

\n[`alarms.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/create "Creates a new alarm.")

\n    Create a new alarm.

\n[`alarms.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms/get
"Gets an alarm, given its name.")

\n    Retrieves a specific alarm, given its name.

\n[`alarms.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/getAll "Gets all active alarms for the
extension.")

\n    Retrieve all scheduled alarms.

\n[`alarms.clear()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/clear "Cancels an alarm, given its name.")

\n    Clear a specific alarm, given its name.

\n[`alarms.clearAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/clearAll "Cancels all active alarms.")

\n    Clear all scheduled alarms.

\n\n

## Events

\n

\n[`alarms.onAlarm`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/alarms/onAlarm "Fired when any alarm set by the
extension goes off.")

\n    Fired when an alarm goes off.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Alarm`| \n Yes| \n No| 45| 48| \n Yes  
`clear`| \n Yes| \n No| 45| 48| \n Yes  
`clearAll`| \n Yes| \n No| 45| 48| \n Yes  
`create`| \n Yes| \n No| 45| 48| \n Yes  
`get`| \n Yes| \n No| 45| 48| \n Yes  
`getAll`| \n Yes| \n No| 45| 48| \n Yes  
`onAlarm`| \n Yes| \n No| 45| 48| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Alarm`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`clear`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`clearAll`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 48  
`create`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`get`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`getAll`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`onAlarm`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
  
## Example extensions

  * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out)
  * [dynamic-theme](https://github.com/mdn/webextensions-examples/tree/master/dynamic-theme)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.alarms`](https://developer.chrome.com/extensions/alarms) API.

\n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

\n

\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

