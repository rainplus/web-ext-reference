[\n

\n

This module provides information about your extension and the environment it's
running in.

\n

It also provides messaging APIs enabling you to:

\n

\n

  * Communicate between different parts of your extension.
\n

  * Communicate with other extensions.
\n

  * Communicate with native applications.
\n

\n

## Types

\n

\n[`runtime.Port`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port
"A Port object represents one end of a connection between two specific
contexts, which can be used to exchange messages.")

\n    Represents one end of a connection between two specific contexts, which
can be used to exchange messages.

\n[`runtime.MessageSender`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/MessageSender "An object containing information
about the sender of a message or connection request; this is passed to the
runtime.onMessage\(\) listener.")

\n    \n

Contains information about the sender of a message or connection request.

\n

\n[`runtime.PlatformOs`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/PlatformOs "The operating system the browser is
running on.")

\n    Identifies the browser's operating system.

\n[`runtime.PlatformArch`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/PlatformArch "The machine's processor
architecture.")

\n    Identifies the browser's processor architecture.

\n[`runtime.PlatformInfo`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/PlatformInfo "An object containing information
about the current platform.")

\n    Contains information about the platform the browser is running on.

\n[`runtime.RequestUpdateCheckStatus`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/RequestUpdateCheckStatus "Result of a call to
runtime.requestUpdateCheck\(\).")

\n    Result of a call to [`runtime.requestUpdateCheck()`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime/requestUpdateCheck "Checks to see if an
update for the extension is available.").

\n[`runtime.OnInstalledReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/OnInstalledReason "The reason that the
runtime.onInstalled event is being dispatched.")

\n    The reason that the [`runtime.onInstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onInstalled "Fired when the extension is first
installed, when the extension is updated to a new version, and when the
browser is updated to a new version.") event is being dispatched.

\n[`runtime.OnRestartRequiredReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/OnRestartRequiredReason "The reason that the
onRestartRequired event is being dispatched.")

\n    The reason that the [`runtime.onRestartRequired`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime/onRestartRequired "Fired when an app or the
device that it runs on needs to be restarted. The app should close all its
windows at its earliest convenience to let the restart happen. If the app does
nothing, a restart will be enforced after a 24-hour grace period has passed.
Currently, this event is only fired for Chrome OS kiosk apps.") event is being
dispatched.

\n\n

## Properties

\n

\n[`runtime.lastError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/lastError "The runtime.lastError property is set
when an asynchronous function has an error condition that it needs to report
to its caller.")

\n    This value is set when an asynchronous function has an error condition
that it needs to report to its caller.

\n[`runtime.id`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/id "The
ID of the extension.")

\n    The ID of the extension.

\n\n

## Functions

\n

\n[`runtime.getBackgroundPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBackgroundPage "The documentation about this
has not yet been written; please consider contributing!")

\n    Retrieves the [Window](/en-US/docs/Web/API/Window) object for the
background page running inside the current extension.

\n[`runtime.openOptionsPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage "This is an asynchronous
function that returns a Promise.")

\n    \n

Opens your extension's [options page](/en-US/Add-
ons/WebExtensions/user_interface/Options_pages).

\n

\n[`runtime.getManifest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getManifest "None.")

\n    Gets the complete [manifest.json](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) file, serialized as an object.

\n[`runtime.getURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getURL "string. The fully-qualified URL to the
resource.")

\n    Given a relative path from the [manifest.json](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) to a resource packaged with the extension,
returns a fully-qualified URL.

\n[`runtime.setUninstallURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/setUninstallURL "The documentation about this
has not yet been written; please consider contributing!")

\n    Sets a URL to be visited when the extension is uninstalled.

\n[`runtime.reload()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/reload "The documentation about this has not yet
been written; please consider contributing!")

\n    Reloads the extension.

\n[`runtime.requestUpdateCheck()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/requestUpdateCheck "Checks to see if an update
for the extension is available.")

\n    Checks for updates to this extension.

\n[`runtime.connect()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/connect "Make a connection between different
contexts inside the extension.")

\n    Establishes a connection from a content script to the main extension
process, or from one extension to a different extension.

\n[`runtime.connectNative()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/connectNative "For more information, see Native
messaging.")

\n    \n

Connects the extension to a native application on the user's computer.

\n

\n[`runtime.sendMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendMessage "Sends a single message to event
listeners within your extension or a different extension.")

\n    Sends a single message to event listeners within your extension or a
different extension. Similar to [`runtime.connect`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/connect "Make a connection between different
contexts inside the extension.") but only sends a single message, with an
optional response.

\n[`runtime.sendNativeMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendNativeMessage "The documentation about this
has not yet been written; please consider contributing!")

\n    Sends a single message from an extension to a native application.

\n[`runtime.getPlatformInfo()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getPlatformInfo "Returns information about the
current platform.")

\n    Returns information about the current platform.

\n[`runtime.getBrowserInfo()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBrowserInfo "Returns information about the
browser in which the extension is installed.")

\n    Returns information about the browser in which this extension is
installed.

\n[`runtime.getPackageDirectoryEntry()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getPackageDirectoryEntry "Returns a
DirectoryEntry object representing the package directory.")

\n    Returns a DirectoryEntry for the package directory.

\n\n

## Events

\n

\n[`runtime.onStartup`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onStartup "Fired when a profile that has this
extension installed first starts up. This event is not fired when a private
browsing/incognito profile is started, even if this extension is operating in
'split' incognito mode.")

\n    Fired when a profile that has this extension installed first starts up.
This event is not fired when an incognito profile is started.

\n[`runtime.onInstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onInstalled "Fired when the extension is first
installed, when the extension is updated to a new version, and when the
browser is updated to a new version.")

\n    Fired when the extension is first installed, when the extension is
updated to a new version, and when the browser is updated to a new version.

\n[`runtime.onSuspend`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onSuspend "Sent to the event page just before it
is unloaded. This gives the extension an opportunity to do some cleanup. Note
that since the page is unloading, any asynchronous operations started while
handling this event are not guaranteed to complete.")

\n    Sent to the event page just before the extension is unloaded. This gives
the extension an opportunity to do some cleanup.

\n[`runtime.onSuspendCanceled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onSuspendCanceled "Sent after runtime.onSuspend
to indicate that the app won't be unloaded after all.")

\n    Sent after [`runtime.onSuspend`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onSuspend "Sent to the event page just before it
is unloaded. This gives the extension an opportunity to do some cleanup. Note
that since the page is unloading, any asynchronous operations started while
handling this event are not guaranteed to complete.") to indicate that the
extension won't be unloaded after all.

\n[`runtime.onUpdateAvailable`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onUpdateAvailable "Fired when an update to the
extension is available. This event enables an extension to delay an update:
for example, because it is in the middle of some operation which should not be
interrupted.")

\n    Fired when an update is available, but isn't installed immediately
because the extension is currently running.

\n[`runtime.onBrowserUpdateAvailable`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onBrowserUpdateAvailable "Fired when an update
for the browser is available, but it isn't installed immediately because a
browser restart is required.")

\n    Fired when an update for the browser is available, but isn't installed
immediately because a browser restart is required.

\n[`runtime.onConnect`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onConnect "Fired when a connection is made with
either an extension process or a content script.")

\n    Fired when a connection is made with either an extension process or a
content script.

\n[`runtime.onConnectExternal`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onConnectExternal "Fired when an extension
receives a connection request from a different extension.")

\n    Fired when a connection is made with another extension.

\n[`runtime.onMessage`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onMessage "To send a message which will be
received by the onMessage listener, use runtime.sendMessage\(\) or \(to send a
message to a content script\) tabs.sendMessage\(\).")

\n    Fired when a message is sent from either an extension process or a
content script.

\n[`runtime.onMessageExternal`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onMessageExternal "This API can't be used in a
content script.")

\n    Fired when a message is sent from another extension. Cannot be used in a
content script.

\n[`runtime.onRestartRequired`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onRestartRequired "Fired when an app or the
device that it runs on needs to be restarted. The app should close all its
windows at its earliest convenience to let the restart happen. If the app does
nothing, a restart will be enforced after a 24-hour grace period has passed.
Currently, this event is only fired for Chrome OS kiosk apps.")

\n    Fired when the device needs to be restarted.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`MessageSender`| 26 *| \n Yes *| 45 *| 48 *| 15 *  
`OnInstalledReason`| \n Yes *| \n Yes *| 45| 48| \n Yes *  
`OnRestartRequiredReason`| \n Yes| \n No| 45| 48| \n Yes  
`PlatformArch`| \n Yes| \n No| 45| 48| \n Yes  
`PlatformInfo`| \n Yes| \n No| 45 *| 48 *| \n Yes  
`PlatformNaclArch`| \n Yes| \n No| 45| 48| \n Yes  
`PlatformOs`| \n Yes| \n No| 45| 48| \n Yes  
`Port`| 26 *| 15 *| 45 *| 48 *| 15 *  
`RequestUpdateCheckStatus`| \n Yes| \n No| \n No| \n No| \n Yes  
`connect`| 26| \n Yes| 45| 48| 15  
`connectNative`| 29| 15| 50| \n No| 16  
`getBackgroundPage`| 22| \n Yes| 45 *| 48 *| 15  
`getBrowserInfo`| \n No| \n No| 51| 51| \n No  
`getManifest`| 22| \n Yes| 45| 48| 15  
`getPackageDirectoryEntry`| 29| \n No| \n No| \n No| 16  
`getPlatformInfo`| 29| \n No| 45| 48| 16  
`getURL`| 22| \n Yes| 45| 48| 15  
`id`| 22| \n Yes| 45| 48| 15  
`lastError`| \n Yes *| \n Yes| 47| 48| \n Yes *  
`onBrowserUpdateAvailable`| 27| \n No| \n No| \n No| 15  
`onConnect`| 26| \n Yes| 45| 48| 15  
`onConnectExternal`| 26| \n No| 54| 54| 15  
`onInstalled`| 22| \n Yes| 52 *| 52 *| 15  
`onMessage`| 26| \n Yes| 45| 48| 15  
`onMessageExternal`| 26| \n No| 54| 54| 15  
`onRestartRequired`| 29| \n No| \n No| \n No| 16  
`onStartup`| 23| \n No| 52| 52| 15  
`onSuspend`| 22| \n No| \n No| \n No| 15  
`onSuspendCanceled`| 22| \n No| \n No| \n No| 15  
`onUpdateAvailable`| 25| \n No| 51| 51| 15  
`openOptionsPage`| 42| \n No| 48| 57| 29  
`reload`| 25| 15| 51| 51| 15  
`requestUpdateCheck`| 25| \n No| \n No| \n No| 15  
`sendMessage`| 26| \n Yes *| 45| 48| 15  
`sendNativeMessage`| 29| 15| 50| \n No| 16  
`setUninstallURL`| 41| 15| 47| 48| 28  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`MessageSender`|  \nPartial support\n26| \nPartial support\nPartial| \nFull
support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Before version 54, 'id' was the add-on's internal UUID, not the add-on ID.
|  \nPartial support\n15| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Before version 54, 'id' was the add-on's internal UUID, not the add-on ID.  
`OnInstalledReason`|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Uses 'chrome_update' instead of 'browser_update'.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Only supports 'install' and 'update'.
|  \nFull support\n\n 45| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Uses 'chrome_update' instead of 'browser_update'.
|  \nFull support\n\n 48  
`OnRestartRequiredReason`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`PlatformArch`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`PlatformInfo`| \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n45| \nFull support\n\n Yes| \nPartial support\n48  
`PlatformNaclArch`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`PlatformOs`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 48  
`Port`| \nPartial support\n26| \nPartial support\n15| \nPartial support\n45|
\nPartial support\n15| \nPartial support\n48  
`RequestUpdateCheckStatus`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`connect`| \nFull support\n\n 26| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n 15| \nFull support\n\n 48  
`connectNative`| \nFull support\n\n 29| \nFull support\n\n 15| \nFull
support\n\n 50| \nFull support\n\n 16| \nNo support\n\n No  
`getBackgroundPage`| \nFull support\n\n 22| \nFull support\n\n Yes| \nFull
support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then it will always return`null`.
|  \nFull support\n\n 15| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then it will always return`null`.  
`getBrowserInfo`|  \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 51| \nNo support\n\n No| \nFull support\n\n 51  
`getManifest`| \nFull support\n\n 22| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n 15| \nFull support\n\n 48  
`getPackageDirectoryEntry`| \nFull support\n\n 29| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n 16| \nNo support\n\n No  
`getPlatformInfo`| \nFull support\n\n 29| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n 16| \nFull support\n\n 48  
`getURL`| \nFull support\n\n 22| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n 15| \nFull support\n\n 48  
`id`| \nFull support\n\n 22| \nFull support\n\n Yes| \nFull support\n\n 45|
\nFull support\n\n 15| \nFull support\n\n 48  
`lastError`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __lastError is not an Error object. Instead, it is a plain Object with the error text as the string value of the 'message' property.
|  \nFull support\n\n Yes| \nFull support\n\n 47| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __lastError is not an Error object. Instead, it is a plain Object with the error text as the string value of the 'message' property.
|  \nFull support\n\n 48  
`onBrowserUpdateAvailable`

Deprecated __Non-standard __

| \n Full support\n\n 27| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 15| \nNo support\n\n No  
`onConnect`| \nFull support\n\n 26| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n 15| \nFull support\n\n 48  
`onConnectExternal`| \nFull support\n\n 26| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n 15| \nFull support\n\n 54  
`onInstalled`| \nFull support\n\n 22| \nFull support\n\n Yes| \nFull
support\n\n 52

Notes __

\nFull support\n\n 52

Notes __

     Notes __Before version 55, this event is not triggered for temporarily installed add-ons.
|  \nFull support\n\n 15| \nFull support\n\n 52

Notes __

\nFull support\n\n 52

Notes __

     Notes __Before version 55, this event is not triggered for temporarily installed add-ons.  
`onMessage`|  \nFull support\n\n 26| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n 15| \nFull support\n\n 48  
`onMessageExternal`| \nFull support\n\n 26| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n 15| \nFull support\n\n 54  
`onRestartRequired`| \nFull support\n\n 29| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n 16| \nNo support\n\n No  
`onStartup`| \nFull support\n\n 23| \nNo support\n\n No| \nFull support\n\n
52| \nFull support\n\n 15| \nFull support\n\n 52  
`onSuspend`| \nFull support\n\n 22| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n 15| \nNo support\n\n No  
`onSuspendCanceled`| \nFull support\n\n 22| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n 15| \nNo support\n\n No  
`onUpdateAvailable`| \nFull support\n\n 25| \nNo support\n\n No| \nFull
support\n\n 51| \nFull support\n\n 15| \nFull support\n\n 51  
`openOptionsPage`| \nFull support\n\n 42| \nNo support\n\n No| \nFull
support\n\n 48| \nFull support\n\n 29| \nFull support\n\n 57  
`reload`| \nFull support\n\n 25| \nFull support\n\n 15| \nFull support\n\n 51|
\nFull support\n\n 15| \nFull support\n\n 51  
`requestUpdateCheck`| \nFull support\n\n 25| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n 15| \nNo support\n\n No  
`sendMessage`| \nFull support\n\n 26| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __`runtime.onMessage` listeners in extension views receive the messages they sent.
|  \nFull support\n\n 45| \nFull support\n\n 15| \nFull support\n\n 48  
`sendNativeMessage`| \nFull support\n\n 29| \nFull support\n\n 15| \nFull
support\n\n 50| \nFull support\n\n 16| \nNo support\n\n No  
`setUninstallURL`| \nFull support\n\n 41| \nFull support\n\n 15| \nFull
support\n\n 47| \nFull support\n\n 28| \nFull support\n\n 48  
  
\n

## Example extensions

  * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
  * [cookie-bg-picker](https://github.com/mdn/webextensions-examples/tree/master/cookie-bg-picker)
  * [devtools-panels](https://github.com/mdn/webextensions-examples/tree/master/devtools-panels)
  * [embedded-webextension-bootstrapped](https://github.com/mdn/webextensions-examples/tree/master/embedded-webextension-bootstrapped)
  * [embedded-webextension-overlay](https://github.com/mdn/webextensions-examples/tree/master/embedded-webextension-overlay)
  * [embedded-webextension-sdk](https://github.com/mdn/webextensions-examples/tree/master/embedded-webextension-sdk)
  * [export-helpers](https://github.com/mdn/webextensions-examples/tree/master/export-helpers)
  * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
  * [find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master/find-across-tabs)
  * [imagify](https://github.com/mdn/webextensions-examples/tree/master/imagify)
  * [menu-demo](https://github.com/mdn/webextensions-examples/tree/master/menu-demo)
  * [mocha-client-tests](https://github.com/mdn/webextensions-examples/tree/master/mocha-client-tests)
  * [native-messaging](https://github.com/mdn/webextensions-examples/tree/master/native-messaging)
  * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)
  * [permissions](https://github.com/mdn/webextensions-examples/tree/master/permissions)
  * [proxy-blocker](https://github.com/mdn/webextensions-examples/tree/master/proxy-blocker)
  * [store-collected-images](https://github.com/mdn/webextensions-examples/tree/master/store-collected-images)
  * [webpack-modules](https://github.com/mdn/webextensions-examples/tree/master/webpack-modules)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.runtime`](https://developer.chrome.com/extensions/runtime) API. This
documentation is derived from
[`runtime.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/runtime.json)
in the Chromium code.

\n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

\n

\n

\n

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.\n//\n// Redistribution and use in source and binary forms, with or without\n// modification, are permitted provided that the following conditions are\n// met:\n//\n//    * Redistributions of source code must retain the above copyright\n// notice, this list of conditions and the following disclaimer.\n//    * Redistributions in binary form must reproduce the above\n// copyright notice, this list of conditions and the following disclaimer\n// in the documentation and/or other materials provided with the\n// distribution.\n//    * Neither the name of Google Inc. nor the names of its\n// contributors may be used to endorse or promote products derived from\n// this software without specific prior written permission.\n//\n// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n

\n

\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[\n Full support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[Notes __]: See implementation notes
  *[Deprecated __]: Deprecated. Not for use in new websites.
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

