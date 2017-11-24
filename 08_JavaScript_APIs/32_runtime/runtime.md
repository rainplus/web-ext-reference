This module provides information about your extension and the environment it's
running in.

It also provides messaging APIs enabling you to:

  * Communicate between different parts of your extension.
  * Communicate with other extensions.
  * Communicate with native applications.

## Types

[`runtime.Port`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port "A
Port object represents one end of a connection between two specific contexts,
which can be used to exchange messages.")

    Represents one end of a connection between two specific contexts, which can be used to exchange messages.
[`runtime.MessageSender`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/MessageSender "An object containing information
about the sender of a message or connection request; this is passed to the
runtime.onMessage\(\) listener.")

    

Contains information about the sender of a message or connection request.

[`runtime.PlatformOs`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/PlatformOs "The operating system the browser is
running on.")

    Identifies the browser's operating system.
[`runtime.PlatformArch`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/PlatformArch "The machine's processor
architecture.")

    Identifies the browser's processor architecture.
[`runtime.PlatformInfo`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/PlatformInfo "An object containing information
about the current platform.")

    Contains information about the platform the browser is running on.
[`runtime.RequestUpdateCheckStatus`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/RequestUpdateCheckStatus "Result of a call to
runtime.requestUpdateCheck\(\).")

    Result of a call to [`runtime.requestUpdateCheck()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/requestUpdateCheck "Checks to see if an update for the extension is available.").
[`runtime.OnInstalledReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/OnInstalledReason "The reason that the
runtime.onInstalled event is being dispatched.")

    The reason that the [`runtime.onInstalled`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onInstalled "Fired when the extension is first installed, when the extension is updated to a new version, and when the browser is updated to a new version.") event is being dispatched.
[`runtime.OnRestartRequiredReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/OnRestartRequiredReason "The reason that the
onRestartRequired event is being dispatched.")

    The reason that the [`runtime.onRestartRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onRestartRequired "Fired when an app or the device that it runs on needs to be restarted. The app should close all its windows at its earliest convenience to let the restart happen. If the app does nothing, a restart will be enforced after a 24-hour grace period has passed. Currently, this event is only fired for Chrome OS kiosk apps.") event is being dispatched.

## Properties

[`runtime.lastError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/lastError "The runtime.lastError property is set
when an asynchronous function has an error condition that it needs to report
to its caller.")

    This value is set when an asynchronous function has an error condition that it needs to report to its caller.
[`runtime.id`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/id "The
ID of the extension.")

    The ID of the extension.

## Functions

[`runtime.getBackgroundPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBackgroundPage "The documentation about this
has not yet been written; please consider contributing!")

    Retrieves the [Window](/en-US/docs/Web/API/Window) object for the background page running inside the current extension.
[`runtime.openOptionsPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/openOptionsPage "This is an asynchronous
function that returns a Promise.")

    

Opens your extension's [options page](/en-US/Add-
ons/WebExtensions/user_interface/Options_pages).

[`runtime.getManifest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getManifest "None.")

    Gets the complete [manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file, serialized as an object.
[`runtime.getURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getURL "string. The fully-qualified URL to the
resource.")

    Given a relative path from the [manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) to a resource packaged with the extension, returns a fully-qualified URL.
[`runtime.setUninstallURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/setUninstallURL "The documentation about this
has not yet been written; please consider contributing!")

    Sets a URL to be visited when the extension is uninstalled.
[`runtime.reload()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/reload "The documentation about this has not yet
been written; please consider contributing!")

    Reloads the extension.
[`runtime.requestUpdateCheck()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/requestUpdateCheck "Checks to see if an update
for the extension is available.")

    Checks for updates to this extension.
[`runtime.connect()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/connect "Make a connection between different
contexts inside the extension.")

    Establishes a connection from a content script to the main extension process, or from one extension to a different extension.
[`runtime.connectNative()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/connectNative "For more information, see Native
messaging.")

    

Connects the extension to a native application on the user's computer.

[`runtime.sendMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendMessage "Sends a single message to event
listeners within your extension or a different extension.")

    Sends a single message to event listeners within your extension or a different extension. Similar to [`runtime.connect`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/connect "Make a connection between different contexts inside the extension.") but only sends a single message, with an optional response.
[`runtime.sendNativeMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendNativeMessage "The documentation about this
has not yet been written; please consider contributing!")

    Sends a single message from an extension to a native application.
[`runtime.getPlatformInfo()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getPlatformInfo "Returns information about the
current platform.")

    Returns information about the current platform.
[`runtime.getBrowserInfo()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getBrowserInfo "Returns information about the
browser in which the extension is installed.")

    Returns information about the browser in which this extension is installed.
[`runtime.getPackageDirectoryEntry()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/getPackageDirectoryEntry "Returns a
DirectoryEntry object representing the package directory.")

    Returns a DirectoryEntry for the package directory.

## Events

[`runtime.onStartup`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onStartup "Fired when a profile that has this
extension installed first starts up. This event is not fired when a private
browsing/incognito profile is started, even if this extension is operating in
'split' incognito mode.")

    Fired when a profile that has this extension installed first starts up. This event is not fired when an incognito profile is started.
[`runtime.onInstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onInstalled "Fired when the extension is first
installed, when the extension is updated to a new version, and when the
browser is updated to a new version.")

    Fired when the extension is first installed, when the extension is updated to a new version, and when the browser is updated to a new version.
[`runtime.onSuspend`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onSuspend "Sent to the event page just before it
is unloaded. This gives the extension an opportunity to do some cleanup. Note
that since the page is unloading, any asynchronous operations started while
handling this event are not guaranteed to complete.")

    Sent to the event page just before the extension is unloaded. This gives the extension an opportunity to do some cleanup.
[`runtime.onSuspendCanceled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onSuspendCanceled "Sent after runtime.onSuspend
to indicate that the app won't be unloaded after all.")

    Sent after [`runtime.onSuspend`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onSuspend "Sent to the event page just before it is unloaded. This gives the extension an opportunity to do some cleanup. Note that since the page is unloading, any asynchronous operations started while handling this event are not guaranteed to complete.") to indicate that the extension won't be unloaded after all.
[`runtime.onUpdateAvailable`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onUpdateAvailable "Fired when an update to the
extension is available. This event enables an extension to delay an update:
for example, because it is in the middle of some operation which should not be
interrupted.")

    Fired when an update is available, but isn't installed immediately because the extension is currently running.
[`runtime.onBrowserUpdateAvailable`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onBrowserUpdateAvailable "Fired when an update
for the browser is available, but it isn't installed immediately because a
browser restart is required.")

    Fired when an update for the browser is available, but isn't installed immediately because a browser restart is required.
[`runtime.onConnect`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onConnect "Fired when a connection is made with
either an extension process or a content script.")

    Fired when a connection is made with either an extension process or a content script.
[`runtime.onConnectExternal`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onConnectExternal "Fired when an extension
receives a connection request from a different extension.")

    Fired when a connection is made with another extension.
[`runtime.onMessage`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onMessage "To send a message which will be
received by the onMessage listener, use runtime.sendMessage\(\) or \(to send a
message to a content script\) tabs.sendMessage\(\).")

    Fired when a message is sent from either an extension process or a content script.
[`runtime.onMessageExternal`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onMessageExternal "This API can't be used in a
content script.")

    Fired when a message is sent from another extension. Cannot be used in a content script.
[`runtime.onRestartRequired`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onRestartRequired "Fired when an app or the
device that it runs on needs to be restarted. The app should close all its
windows at its earliest convenience to let the restart happen. If the app does
nothing, a restart will be enforced after a 24-hour grace period has passed.
Currently, this event is only fired for Chrome OS kiosk apps.")

    Fired when the device needs to be restarted.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`MessageSender`| 26 *|  Yes *| 45 *| 48 *| 15 *  
`OnInstalledReason`|  Yes *|  Yes *| 45| 48|  Yes *  
`OnRestartRequiredReason`|  Yes|  No| 45| 48|  Yes  
`PlatformArch`|  Yes|  No| 45| 48|  Yes  
`PlatformInfo`|  Yes|  No| 45 *| 48 *|  Yes  
`PlatformNaclArch`|  Yes|  No| 45| 48|  Yes  
`PlatformOs`|  Yes|  No| 45| 48|  Yes  
`Port`| 26 *| 15 *| 45 *| 48 *| 15 *  
`RequestUpdateCheckStatus`|  Yes|  No|  No|  No|  Yes  
`connect`| 26|  Yes| 45| 48| 15  
`connectNative`| 29| 15| 50|  No| 16  
`getBackgroundPage`| 22|  Yes| 45 *| 48 *| 15  
`getBrowserInfo`|  No|  No| 51| 51|  No  
`getManifest`| 22|  Yes| 45| 48| 15  
`getPackageDirectoryEntry`| 29|  No|  No|  No| 16  
`getPlatformInfo`| 29|  No| 45| 48| 16  
`getURL`| 22|  Yes| 45| 48| 15  
`id`| 22|  Yes| 45| 48| 15  
`lastError`|  Yes *|  Yes| 47| 48|  Yes *  
`onBrowserUpdateAvailable`| 27|  No|  No|  No| 15  
`onConnect`| 26|  Yes| 45| 48| 15  
`onConnectExternal`| 26|  No| 54| 54| 15  
`onInstalled`| 22|  Yes| 52 *| 52 *| 15  
`onMessage`| 26|  Yes| 45| 48| 15  
`onMessageExternal`| 26|  No| 54| 54| 15  
`onRestartRequired`| 29|  No|  No|  No| 16  
`onStartup`| 23|  No| 52| 52| 15  
`onSuspend`| 22|  No|  No|  No| 15  
`onSuspendCanceled`| 22|  No|  No|  No| 15  
`onUpdateAvailable`| 25|  No| 51| 51| 15  
`openOptionsPage`| 42|  No| 48| 57| 29  
`reload`| 25| 15| 51| 51| 15  
`requestUpdateCheck`| 25|  No|  No|  No| 15  
`sendMessage`| 26|  Yes *| 45| 48| 15  
`sendNativeMessage`| 29| 15| 50|  No| 16  
`setUninstallURL`| 41| 15| 47| 48| 28  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`MessageSender`|  Partial support 26|  Partial support Partial|  Full support
45

Notes __

Full support 45

Notes __

     Notes __Before version 54, 'id' was the add-on's internal UUID, not the add-on ID.
|  Partial support 15|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Before version 54, 'id' was the add-on's internal UUID, not the add-on ID.  
`OnInstalledReason`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Uses 'chrome_update' instead of 'browser_update'.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Only supports 'install' and 'update'.
|  Full support 45|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Uses 'chrome_update' instead of 'browser_update'.
|  Full support 48  
`OnRestartRequiredReason`|  Full support Yes|  No support No|  Full support
45|  Full support Yes|  Full support 48  
`PlatformArch`|  Full support Yes|  No support No|  Full support 45|  Full
support Yes|  Full support 48  
`PlatformInfo`|  Full support Yes|  No support No|  Partial support 45|  Full
support Yes|  Partial support 48  
`PlatformNaclArch`|  Full support Yes|  No support No|  Full support 45|  Full
support Yes|  Full support 48  
`PlatformOs`|  Full support Yes|  No support No|  Full support 45|  Full
support Yes|  Full support 48  
`Port`|  Partial support 26|  Partial support 15|  Partial support 45|
Partial support 15|  Partial support 48  
`RequestUpdateCheckStatus`|  Full support Yes|  No support No|  No support No|
Full support Yes|  No support No  
`connect`|  Full support 26|  Full support Yes|  Full support 45|  Full
support 15|  Full support 48  
`connectNative`|  Full support 29|  Full support 15|  Full support 50|  Full
support 16|  No support No  
`getBackgroundPage`|  Full support 22|  Full support Yes|  Full support 45

Notes __

Full support 45

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then it will always return`null`.
|  Full support 15|  Full support 48

Notes __

Full support 48

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then it will always return`null`.  
`getBrowserInfo`|  No support No|  No support No|  Full support 51|  No
support No|  Full support 51  
`getManifest`|  Full support 22|  Full support Yes|  Full support 45|  Full
support 15|  Full support 48  
`getPackageDirectoryEntry`|  Full support 29|  No support No|  No support No|
Full support 16|  No support No  
`getPlatformInfo`|  Full support 29|  No support No|  Full support 45|  Full
support 16|  Full support 48  
`getURL`|  Full support 22|  Full support Yes|  Full support 45|  Full support
15|  Full support 48  
`id`|  Full support 22|  Full support Yes|  Full support 45|  Full support 15|
Full support 48  
`lastError`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __lastError is not an Error object. Instead, it is a plain Object with the error text as the string value of the 'message' property.
|  Full support Yes|  Full support 47|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __lastError is not an Error object. Instead, it is a plain Object with the error text as the string value of the 'message' property.
|  Full support 48  
`onBrowserUpdateAvailable`

Deprecated __Non-standard __

|  Full support 27|  No support No|  No support No|  Full support 15|  No
support No  
`onConnect`|  Full support 26|  Full support Yes|  Full support 45|  Full
support 15|  Full support 48  
`onConnectExternal`|  Full support 26|  No support No|  Full support 54|  Full
support 15|  Full support 54  
`onInstalled`|  Full support 22|  Full support Yes|  Full support 52

Notes __

Full support 52

Notes __

     Notes __Before version 55, this event is not triggered for temporarily installed add-ons.
|  Full support 15|  Full support 52

Notes __

Full support 52

Notes __

     Notes __Before version 55, this event is not triggered for temporarily installed add-ons.  
`onMessage`|  Full support 26|  Full support Yes|  Full support 45|  Full
support 15|  Full support 48  
`onMessageExternal`|  Full support 26|  No support No|  Full support 54|  Full
support 15|  Full support 54  
`onRestartRequired`|  Full support 29|  No support No|  No support No|  Full
support 16|  No support No  
`onStartup`|  Full support 23|  No support No|  Full support 52|  Full support
15|  Full support 52  
`onSuspend`|  Full support 22|  No support No|  No support No|  Full support
15|  No support No  
`onSuspendCanceled`|  Full support 22|  No support No|  No support No|  Full
support 15|  No support No  
`onUpdateAvailable`|  Full support 25|  No support No|  Full support 51|  Full
support 15|  Full support 51  
`openOptionsPage`|  Full support 42|  No support No|  Full support 48|  Full
support 29|  Full support 57  
`reload`|  Full support 25|  Full support 15|  Full support 51|  Full support
15|  Full support 51  
`requestUpdateCheck`|  Full support 25|  No support No|  No support No|  Full
support 15|  No support No  
`sendMessage`|  Full support 26|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __`runtime.onMessage` listeners in extension views receive the messages they sent.
|  Full support 45|  Full support 15|  Full support 48  
`sendNativeMessage`|  Full support 29|  Full support 15|  Full support 50|
Full support 16|  No support No  
`setUninstallURL`|  Full support 41|  Full support 15|  Full support 47|  Full
support 28|  Full support 48  
  
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

**Acknowledgements**

This API is based on Chromium's
[`chrome.runtime`](https://developer.chrome.com/extensions/runtime) API. This
documentation is derived from
[`runtime.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/runtime.json)
in the Chromium code.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.
    //
    // Redistribution and use in source and binary forms, with or without
    // modification, are permitted provided that the following conditions are
    // met:
    //
    //    * Redistributions of source code must retain the above copyright
    // notice, this list of conditions and the following disclaimer.
    //    * Redistributions in binary form must reproduce the above
    // copyright notice, this list of conditions and the following disclaimer
    // in the documentation and/or other materials provided with the
    // distribution.
    //    * Neither the name of Google Inc. nor the names of its
    // contributors may be used to endorse or promote products derived from
    // this software without specific prior written permission.
    //
    // THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    // "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    // LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    // A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    // OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    // SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    // LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    // DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    // THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    // (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    // OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
  *[
 No support

]: No support

  *[
Full support

]: Full support

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[ Full support
]: Full support

  *[Desktop __]: Desktop
  *[
Partial support

]: Partial support

  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[Notes __]: See implementation notes
  *[
 Partial support

]: Partial support

  *[Deprecated __]: Deprecated. Not for use in new websites.
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

