[



Utilities related to your extension. Get URLs to resources packages with your
extension, get the `[Window](/en-US/docs/Web/API/Window)` object for your
extension's pages, get the values for various settings. Note that the
messaging APIs in this module are deprecated in favor of the equivalent APIs
in the `[runtime](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)`
module.



## Types



[`extension.ViewType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/ViewType "The type of extension view.")

    The type of extension view.



## Properties



[`extension.lastError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/lastError "An alias for runtime.lastError.")

    Set for the lifetime of a callback if an ansychronous extension api has
resulted in an error. If no error has occured lastError will be undefined.

[`extension.inIncognitoContext`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/inIncognitoContext "Boolean value, true for
content scripts running inside private browsing tabs and for extension pages
running inside a private browsing process.")

    True for content scripts running inside incognito tabs, and for
extension pages running inside an incognito process. The latter only applies
to extensions with 'split' incognito_behavior.



## Functions



[`extension.getURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getURL "Converts a relative path within an
extension's install directory to a fully-qualified URL.")

    Converts a relative path within an extension install directory to a
fully-qualified URL.

[`extension.getViews()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getViews "Returns an array of the Window
objects for each of the pages running inside the current extension. This
includes, for example:")

    Returns an array of the `[Window](/en-US/docs/Web/API/Window)` objects
for each of the pages running inside the current extension.

[`extension.getBackgroundPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getBackgroundPage "Alias for
runtime.getBackgroundPage\(\).")

    Returns the `[Window](/en-US/docs/Web/API/Window)` object for the
background page running inside the current extension. Returns null if the
extension has no background page.

[`extension.isAllowedIncognitoAccess()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/isAllowedIncognitoAccess "Check whether the
extension is allowed access to tabs opened in "private browsing" mode.")

    Retrieves the state of the extension's access to Incognito-mode (as
determined by the user-controlled 'Allowed in Incognito' checkbox).

[`extension.isAllowedFileSchemeAccess()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/isAllowedFileSchemeAccess "None.")

    Retrieves the state of the extension's access to the 'file://' scheme
(as determined by the user-controlled 'Allow access to File URLs' checkbox).

[`extension.setUpdateUrlData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/setUpdateUrlData "Sets parameters for the
extension's update URL. This value is ignored for extensions that are hosted
in the browser vendor's store.")

    Sets the value of the ap CGI parameter used in the extension's update
URL. This value is ignored for extensions that are hosted in the browser
vendor's store.



## Events



[`extension.onRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/onRequest "Fired when a request is sent from
either an extension process or a content script.")

    Fired when a request is sent from either an extension process or a
content script.

[`extension.onRequestExternal`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/onRequestExternal "Fired when a request is
sent from another extension.")

    Fired when a request is sent from another extension.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ViewType`|  Yes|  No| 45| 48|  Yes  
`getBackgroundPage`|  Yes|  Yes| 45| 48|  Yes  
`getExtensionTabs`|  Yes|  No|  No|  No|  No  
`getURL`|  Yes|  Yes| 45| 48|  Yes  
`getViews`|  Yes|  Yes| 45 *| 48 *|  Yes  
`inIncognitoContext`|  Yes|  No| 45| 48|  Yes  
`isAllowedFileSchemeAccess`|  Yes|  No| 48| 48|  Yes  
`isAllowedIncognitoAccess`|  Yes|  No| 48| 48|  Yes  
`lastError`|  Yes|  No| 47| 48|  Yes  
`onRequest`|  Yes|  No|  No|  No|  Yes  
`onRequestExternal`|  Yes|  No|  No|  No|  Yes  
`sendRequest`|  Yes|  No|  No|  No|  No  
`setUpdateUrlData`|  Yes|  No|  No|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ViewType`|  Full support Yes| No support No| Full support
45| Full support Yes| Full support 48  
`getBackgroundPage`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 48  
`getExtensionTabs`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| No
support No| No support No  
`getURL`

Deprecated __Non-standard __

|  Full support Yes| Full support Yes| Full support 45|
Full support Yes| Full support 48  
`getViews`| Full support Yes| Full support Yes| Full support
45

Notes __

Full support 45

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then its return value will not include the extension's background page.
|  Full support Yes| Full support 48

Notes __

Full support 48

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then its return value will not include the extension's background page.  
`inIncognitoContext`|  Full support Yes| No support No| Full
support 45| Full support Yes| Full support 48  
`isAllowedFileSchemeAccess`| Full support Yes| No support No|
Full support 48| Full support Yes| Full support 48  
`isAllowedIncognitoAccess`| Full support Yes| No support No|
Full support 48| Full support Yes| Full support 48  
`lastError`| Full support Yes| No support No| Full support
47| Full support Yes| Full support 48  
`onRequest`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| Full
support Yes| No support No  
`onRequestExternal`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| Full
support Yes| No support No  
`sendRequest`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| No
support No| No support No  
`setUpdateUrlData`| Full support Yes| No support No| No
support No| Full support Yes| No support No  
  


## Example extensions

  * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
  * [cookie-bg-picker](https://github.com/mdn/webextensions-examples/tree/master/cookie-bg-picker)
  * [find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master/find-across-tabs)
  * [imagify](https://github.com/mdn/webextensions-examples/tree/master/imagify)
  * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)
  * [proxy-blocker](https://github.com/mdn/webextensions-examples/tree/master/proxy-blocker)
  * [user-agent-rewriter](https://github.com/mdn/webextensions-examples/tree/master/user-agent-rewriter)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.extension`](https://developer.chrome.com/extensions/extension) API.
This documentation is derived from
[`extension.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/extension.json)
in the Chromium code.



Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.







    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.//// Redistribution and use in source and binary forms, with or without// modification, are permitted provided that the following conditions are// met:////    * Redistributions of source code must retain the above copyright// notice, this list of conditions and the following disclaimer.//    * Redistributions in binary form must reproduce the above// copyright notice, this list of conditions and the following disclaimer// in the documentation and/or other materials provided with the// distribution.//    * Neither the name of Google Inc. nor the names of its// contributors may be used to endorse or promote products derived from// this software without specific prior written permission.//// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[Notes __]: See implementation notes
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[ Full support]: Full support
  *[ Notes __]: See implementation notes
  *[Deprecated __]: Deprecated. Not for use in new websites.
  *[Chrome __]: Chrome

