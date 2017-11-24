[\n

\n

Get information about installed add-ons.

\n

With the `management` API you can:

\n

\n

  * get information about installed add-ons
\n

  * enable/disable add-ons
\n

  * uninstall add-ons
\n

  * find out which permission warnings are given for particular add-ons or manifests
\n

  * get notifications of add-ons being installed, uninstalled, enabled, or disabled.
\n

\n

Most of these operations require the "management" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions). Operations that don't provide
access to other add-ons don't require this permission.

\n

## Types

\n

\n[`management.ExtensionInfo`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/ExtensionInfo "An ExtensionInfo object
contains information about an add-on.")

\n    An object that contains information about an installed add-on.

\n\n

## Functions

\n

\n[`management.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getAll "Retrieves an array of ExtensionInfo
objects, one for each installed add-on.")

\n    Returns information about all installed add-ons.

\n[`management.get()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/get "Retrieves an ExtensionInfo object
containing information about the specified add-on.")

\n    Returns information about a particular add-on, given its ID.

\n[`management.getSelf()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getSelf "Retrieves an ExtensionInfo object
containing information about the calling add-on.")

\n    Returns information about the calling add-on.

\n[`management.uninstall()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/uninstall "Uninstalls an add-on, given its
ID.")

\n    Uninstalls a particular add-on, given its ID.

\n[`management.uninstallSelf()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/uninstallSelf "The documentation about this
has not yet been written; please consider contributing!")

\n    Uninstalls the calling add-on.

\n[`management.getPermissionWarningsById()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getPermissionWarningsById "Given the ID of an
add-on, this function returns the permission warnings for it as an array of
strings.")

\n    Get the set of permission warnings for a particular add-on, given its
ID.

\n[`management.getPermissionWarningsByManifest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getPermissionWarningsByManifest "Given the
text of a manifest.json file, this function returns the permission warnings
that would be given for the resulting add-on, as an array of strings.")

\n    Get the set of permission warnings that would be displayed for the given
manifest string.

\n[`management.setEnabled()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/setEnabled "The documentation about this has
not yet been written; please consider contributing!")

\n    Enable/disable a particular add-on, given its ID.

\n\n

## Events

\n

\n[`management.onInstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onInstalled "Fired when an add-on is
installed.")

\n    Fired when an add-on is installed.

\n[`management.onUninstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onUninstalled "The documentation about this
has not yet been written; please consider contributing!")

\n    Fired when an add-on is uninstalled.

\n[`management.onEnabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onEnabled "Fired when an add-on is enabled.")

\n    Fired when an add-on is enabled.

\n[`management.onDisabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onDisabled "Fired when an add-on is
disabled.")

\n    Fired when an add-on is disabled.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ExtensionInfo`| \n Yes| \n No| 51 *| 51 *| \n Yes  
`get`| \n Yes| \n No| 56| 56| \n Yes  
`getAll`| \n Yes| \n No| 55 *| 55 *| \n Yes  
`getPermissionWarningsById`| \n Yes| \n No| \n No| \n No| \n Yes  
`getPermissionWarningsByManifest`| \n Yes| \n No| \n No| \n No| \n Yes  
`getSelf`| \n Yes| \n No| 51| 51| \n No  
`onDisabled`| \n Yes| \n No| \n No| \n No| \n Yes  
`onEnabled`| \n Yes| \n No| \n No| \n No| \n Yes  
`onInstalled`| \n Yes| \n No| \n No| \n No| \n Yes  
`onUninstalled`| \n Yes| \n No| \n No| \n No| \n Yes  
`setEnabled`| \n Yes| \n No| 55 *| 55 *| \n Yes  
`uninstall`| \n Yes| \n No| \n No| \n No| \n Yes  
`uninstallSelf`| \n Yes *| \n No| 51| 51| \n Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ExtensionInfo`|  \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n51| \nFull support\n\n Yes| \nPartial support\n51  
`get`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 56|
\nFull support\n\n Yes| \nFull support\n\n 56  
`getAll`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55

Notes __

\nFull support\n\n 55

Notes __

     Notes __Before version 56, only extensions whose 'type' is 'theme' are returned.
|  \nFull support\n\n Yes| \nFull support\n\n 55

Notes __

\nFull support\n\n 55

Notes __

     Notes __Before version 56, only extensions whose 'type' is 'theme' are returned.  
`getPermissionWarningsById`|  \nFull support\n\n Yes| \nNo support\n\n No|
\nNo support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`getPermissionWarningsByManifest`| \nFull support\n\n Yes| \nNo support\n\n
No| \nNo support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`getSelf`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 51|
\nNo support\n\n No| \nFull support\n\n 51  
`onDisabled`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`onEnabled`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`onInstalled`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`onUninstalled`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`setEnabled`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
55

Notes __

\nFull support\n\n 55

Notes __

     Notes __Only extensions whose 'type' is 'theme' can be enabled and disabled.
|  \nFull support\n\n Yes| \nFull support\n\n 55

Notes __

\nFull support\n\n 55

Notes __

     Notes __Only extensions whose 'type' is 'theme' can be enabled and disabled.  
`uninstall`|  \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`uninstallSelf`| \nPartial support\nPartial| \nNo support\n\n No| \nFull
support\n\n 51| \nPartial support\nPartial| \nFull support\n\n 51  
  
\n

## Example extensions

  * [theme-switcher](https://github.com/mdn/webextensions-examples/tree/master/theme-switcher)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.management`](https://developer.chrome.com/extensions/management) API.
This documentation is derived from
[`management.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/management.json)
in the Chromium code.

\n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

\n

\n

\n

    
    
    // Copyright 2012 The Chromium Authors. All rights reserved.\n//\n// Redistribution and use in source and binary forms, with or without\n// modification, are permitted provided that the following conditions are\n// met:\n//\n//    * Redistributions of source code must retain the above copyright\n// notice, this list of conditions and the following disclaimer.\n//    * Redistributions in binary form must reproduce the above\n// copyright notice, this list of conditions and the following disclaimer\n// in the documentation and/or other materials provided with the\n// distribution.\n//    * Neither the name of Google Inc. nor the names of its\n// contributors may be used to endorse or promote products derived from\n// this software without specific prior written permission.\n//\n// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n

\n

\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

