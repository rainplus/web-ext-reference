[



Get information about installed add-ons.



With the `management` API you can:





  * get information about installed add-ons


  * enable/disable add-ons


  * uninstall add-ons


  * find out which permission warnings are given for particular add-ons or manifests


  * get notifications of add-ons being installed, uninstalled, enabled, or disabled.




Most of these operations require the "management" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions). Operations that don't provide
access to other add-ons don't require this permission.



## Types



[`management.ExtensionInfo`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/ExtensionInfo "An ExtensionInfo object
contains information about an add-on.")

    An object that contains information about an installed add-on.



## Functions



[`management.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getAll "Retrieves an array of ExtensionInfo
objects, one for each installed add-on.")

    Returns information about all installed add-ons.

[`management.get()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/get "Retrieves an ExtensionInfo object
containing information about the specified add-on.")

    Returns information about a particular add-on, given its ID.

[`management.getSelf()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getSelf "Retrieves an ExtensionInfo object
containing information about the calling add-on.")

    Returns information about the calling add-on.

[`management.uninstall()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/uninstall "Uninstalls an add-on, given its
ID.")

    Uninstalls a particular add-on, given its ID.

[`management.uninstallSelf()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/uninstallSelf "The documentation about this
has not yet been written; please consider contributing!")

    Uninstalls the calling add-on.

[`management.getPermissionWarningsById()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getPermissionWarningsById "Given the ID of an
add-on, this function returns the permission warnings for it as an array of
strings.")

    Get the set of permission warnings for a particular add-on, given its
ID.

[`management.getPermissionWarningsByManifest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/getPermissionWarningsByManifest "Given the
text of a manifest.json file, this function returns the permission warnings
that would be given for the resulting add-on, as an array of strings.")

    Get the set of permission warnings that would be displayed for the given
manifest string.

[`management.setEnabled()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/setEnabled "The documentation about this has
not yet been written; please consider contributing!")

    Enable/disable a particular add-on, given its ID.



## Events



[`management.onInstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onInstalled "Fired when an add-on is
installed.")

    Fired when an add-on is installed.

[`management.onUninstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onUninstalled "The documentation about this
has not yet been written; please consider contributing!")

    Fired when an add-on is uninstalled.

[`management.onEnabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onEnabled "Fired when an add-on is enabled.")

    Fired when an add-on is enabled.

[`management.onDisabled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/management/onDisabled "Fired when an add-on is
disabled.")

    Fired when an add-on is disabled.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ExtensionInfo`|  Yes|  No| 51 *| 51 *|  Yes  
`get`|  Yes|  No| 56| 56|  Yes  
`getAll`|  Yes|  No| 55 *| 55 *|  Yes  
`getPermissionWarningsById`|  Yes|  No|  No|  No|  Yes  
`getPermissionWarningsByManifest`|  Yes|  No|  No|  No|  Yes  
`getSelf`|  Yes|  No| 51| 51|  No  
`onDisabled`|  Yes|  No|  No|  No|  Yes  
`onEnabled`|  Yes|  No|  No|  No|  Yes  
`onInstalled`|  Yes|  No|  No|  No|  Yes  
`onUninstalled`|  Yes|  No|  No|  No|  Yes  
`setEnabled`|  Yes|  No| 55 *| 55 *|  Yes  
`uninstall`|  Yes|  No|  No|  No|  Yes  
`uninstallSelf`|  Yes *|  No| 51| 51|  Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ExtensionInfo`|  Full support Yes| No support No| Partial
support51| Full support Yes| Partial support51  
`get`| Full support Yes| No support No| Full support 56|
Full support Yes| Full support 56  
`getAll`| Full support Yes| No support No| Full support 55

Notes __

Full support 55

Notes __

     Notes __Before version 56, only extensions whose 'type' is 'theme' are returned.
|  Full support Yes| Full support 55

Notes __

Full support 55

Notes __

     Notes __Before version 56, only extensions whose 'type' is 'theme' are returned.  
`getPermissionWarningsById`|  Full support Yes| No support No|
No support No| Full support Yes| No support No  
`getPermissionWarningsByManifest`| Full support Yes| No support
No| No support No| Full support Yes| No support No  
`getSelf`| Full support Yes| No support No| Full support 51|
No support No| Full support 51  
`onDisabled`| Full support Yes| No support No| No support
No| Full support Yes| No support No  
`onEnabled`| Full support Yes| No support No| No support No|
Full support Yes| No support No  
`onInstalled`| Full support Yes| No support No| No support
No| Full support Yes| No support No  
`onUninstalled`| Full support Yes| No support No| No support
No| Full support Yes| No support No  
`setEnabled`| Full support Yes| No support No| Full support
55

Notes __

Full support 55

Notes __

     Notes __Only extensions whose 'type' is 'theme' can be enabled and disabled.
|  Full support Yes| Full support 55

Notes __

Full support 55

Notes __

     Notes __Only extensions whose 'type' is 'theme' can be enabled and disabled.  
`uninstall`|  Full support Yes| No support No| No support
No| Full support Yes| No support No  
`uninstallSelf`| Partial supportPartial| No support No| Full
support 51| Partial supportPartial| Full support 51  
  


## Example extensions

  * [theme-switcher](https://github.com/mdn/webextensions-examples/tree/master/theme-switcher)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.management`](https://developer.chrome.com/extensions/management) API.
This documentation is derived from
[`management.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/management.json)
in the Chromium code.



Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.







    
    
    // Copyright 2012 The Chromium Authors. All rights reserved.//// Redistribution and use in source and binary forms, with or without// modification, are permitted provided that the following conditions are// met:////    * Redistributions of source code must retain the above copyright// notice, this list of conditions and the following disclaimer.//    * Redistributions in binary form must reproduce the above// copyright notice, this list of conditions and the following disclaimer// in the documentation and/or other materials provided with the// distribution.//    * Neither the name of Google Inc. nor the names of its// contributors may be used to endorse or promote products derived from// this software without specific prior written permission.//// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

