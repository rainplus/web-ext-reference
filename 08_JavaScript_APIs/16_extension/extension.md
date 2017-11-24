[\n

\n

Utilities related to your extension. Get URLs to resources packages with your
extension, get the `[Window](/en-US/docs/Web/API/Window)` object for your
extension's pages, get the values for various settings. Note that the
messaging APIs in this module are deprecated in favor of the equivalent APIs
in the `[runtime](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)`
module.

\n

## Types

\n

\n[`extension.ViewType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/ViewType "The type of extension view.")

\n    The type of extension view.

\n\n

## Properties

\n

\n[`extension.lastError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/lastError "An alias for runtime.lastError.")

\n    Set for the lifetime of a callback if an ansychronous extension api has
resulted in an error. If no error has occured lastError will be undefined.

\n[`extension.inIncognitoContext`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/inIncognitoContext "Boolean value, true for
content scripts running inside private browsing tabs and for extension pages
running inside a private browsing process.")

\n    True for content scripts running inside incognito tabs, and for
extension pages running inside an incognito process. The latter only applies
to extensions with 'split' incognito_behavior.

\n\n

## Functions

\n

\n[`extension.getURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getURL "Converts a relative path within an
extension's install directory to a fully-qualified URL.")

\n    Converts a relative path within an extension install directory to a
fully-qualified URL.

\n[`extension.getViews()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getViews "Returns an array of the Window
objects for each of the pages running inside the current extension. This
includes, for example:")

\n    Returns an array of the `[Window](/en-US/docs/Web/API/Window)` objects
for each of the pages running inside the current extension.

\n[`extension.getBackgroundPage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/getBackgroundPage "Alias for
runtime.getBackgroundPage\(\).")

\n    Returns the `[Window](/en-US/docs/Web/API/Window)` object for the
background page running inside the current extension. Returns null if the
extension has no background page.

\n[`extension.isAllowedIncognitoAccess()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/isAllowedIncognitoAccess "Check whether the
extension is allowed access to tabs opened in "private browsing" mode.")

\n    Retrieves the state of the extension's access to Incognito-mode (as
determined by the user-controlled 'Allowed in Incognito' checkbox).

\n[`extension.isAllowedFileSchemeAccess()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/isAllowedFileSchemeAccess "None.")

\n    Retrieves the state of the extension's access to the 'file://' scheme
(as determined by the user-controlled 'Allow access to File URLs' checkbox).

\n[`extension.setUpdateUrlData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/setUpdateUrlData "Sets parameters for the
extension's update URL. This value is ignored for extensions that are hosted
in the browser vendor's store.")

\n    Sets the value of the ap CGI parameter used in the extension's update
URL. This value is ignored for extensions that are hosted in the browser
vendor's store.

\n\n

## Events

\n

\n[`extension.onRequest`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/onRequest "Fired when a request is sent from
either an extension process or a content script.")

\n    Fired when a request is sent from either an extension process or a
content script.

\n[`extension.onRequestExternal`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extension/onRequestExternal "Fired when a request is
sent from another extension.")

\n    Fired when a request is sent from another extension.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ViewType`| \n Yes| \n No| 45| 48| \n Yes  
`getBackgroundPage`| \n Yes| \n Yes| 45| 48| \n Yes  
`getExtensionTabs`| \n Yes| \n No| \n No| \n No| \n No  
`getURL`| \n Yes| \n Yes| 45| 48| \n Yes  
`getViews`| \n Yes| \n Yes| 45 *| 48 *| \n Yes  
`inIncognitoContext`| \n Yes| \n No| 45| 48| \n Yes  
`isAllowedFileSchemeAccess`| \n Yes| \n No| 48| 48| \n Yes  
`isAllowedIncognitoAccess`| \n Yes| \n No| 48| 48| \n Yes  
`lastError`| \n Yes| \n No| 47| 48| \n Yes  
`onRequest`| \n Yes| \n No| \n No| \n No| \n Yes  
`onRequestExternal`| \n Yes| \n No| \n No| \n No| \n Yes  
`sendRequest`| \n Yes| \n No| \n No| \n No| \n No  
`setUpdateUrlData`| \n Yes| \n No| \n No| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ViewType`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 48  
`getBackgroundPage`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`getExtensionTabs`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No  
`getURL`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 48  
`getViews`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45

Notes __

\nFull support\n\n 45

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then its return value will not include the extension's background page.
|  \nFull support\n\n Yes| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then its return value will not include the extension's background page.  
`inIncognitoContext`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`isAllowedFileSchemeAccess`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`isAllowedIncognitoAccess`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`lastError`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nFull support\n\n 48  
`onRequest`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n Yes| \nNo support\n\n No  
`onRequestExternal`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n Yes| \nNo support\n\n No  
`sendRequest`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No  
`setUpdateUrlData`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
  
\n

## Example extensions

  * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
  * [cookie-bg-picker](https://github.com/mdn/webextensions-examples/tree/master/cookie-bg-picker)
  * [find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master/find-across-tabs)
  * [imagify](https://github.com/mdn/webextensions-examples/tree/master/imagify)
  * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)
  * [proxy-blocker](https://github.com/mdn/webextensions-examples/tree/master/proxy-blocker)
  * [user-agent-rewriter](https://github.com/mdn/webextensions-examples/tree/master/user-agent-rewriter)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.extension`](https://developer.chrome.com/extensions/extension) API.
This documentation is derived from
[`extension.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/extension.json)
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
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Notes __]: See implementation notes
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[\n Full support\n]: Full support
  *[ Notes __]: See implementation notes
  *[Deprecated __]: Deprecated. Not for use in new websites.
  *[Chrome __]: Chrome

