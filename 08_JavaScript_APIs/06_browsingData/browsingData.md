Enables extensions to clear the data that is accumulated while the user is
browsing.

In the `browsingData` API, browsing data is divided into types:

  * browser cache
  * cookies
  * downloads
  * history
  * local storage
  * plugin data
  * saved form data
  * saved passwords

You can use the [`browsingData.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/remove "Removes the specified browsing
data.") function to remove any combination of these types. There are also
dedicated functions to remove each particular type of data, such as
[`removePasswords()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removePasswords "The documentation about
this has not yet been written; please consider contributing!"),
[`removeHistory()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeHistory "The documentation about this
has not yet been written; please consider contributing!") and so on.

All the `browsingData.remove[X]()` functions take a
[`browsingData.RemovalOptions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/RemovalOptions "The
browsingData.RemovalOptions type contains options to control certain aspects
of browsing data removal.") object, which you can use to control two further
aspects of data removal:

  * how far back in time to remove data
  * whether to remove data only from normal web pages, or also from hosted web apps and add-ons. Note that this option is not yet supported in Firefox.

Finally, this API gives you a [`browsingData.settings()`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/browsingData/settings "Browsers have a built-in
"Clear History" feature, which enables the user to clear various types of
browsing data. This has a UI that enables the user to select what type of data
to remove \(e.g. history, downloads, ...\) and how far back in time to remove
data.") function that gives you the current value of the settings for the
browser's built-in "Clear History" feature.

To use this API you must have the "browsingData" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).

## Types

[`browsingData.DataTypeSet`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/DataTypeSet "The browsingData.DataTypeSet
type describes a set of data types.")

    Object used to specify the type of data to remove: for example, history, downloads, passwords, and so on.
[`browsingData.RemovalOptions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/RemovalOptions "The
browsingData.RemovalOptions type contains options to control certain aspects
of browsing data removal.")

    Object used to specify how far back in time to remove data, and whether to remove data added through normal web browsing, by hosted apps, or by add-ons.

## Methods

[`browsingData.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/remove "Removes the specified browsing
data.")

    Removes browsing data for the data types specified.
[`browsingData.removeCache()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeCache "Clears the browser's cache.")

    Clears the browser's cache.
[`browsingData.removeCookies()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeCookies "The documentation about this
has not yet been written; please consider contributing!")

    Removes cookies.
[`browsingData.removeDownloads()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeDownloads "Clears the browser's
download history. Note that this does not delete the downloaded objects
themselves, only records of downloads in the browser's history.")

    Removes the list of downloaded files.
[`browsingData.removeFormData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeFormData "The documentation about
this has not yet been written; please consider contributing!")

    Clears saved form data.
[`browsingData.removeHistory()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeHistory "The documentation about this
has not yet been written; please consider contributing!")

    Clears the browser's history.
[`browsingData.removeLocalStorage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeLocalStorage "The documentation about
this has not yet been written; please consider contributing!")

    Clears any [local storage](/en-US/docs/Web/API/Window/localStorage) created by websites.
[`browsingData.removePasswords()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removePasswords "The documentation about
this has not yet been written; please consider contributing!")

    Clears saved passwords.
[`browsingData.removePluginData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removePluginData "Clears data stored by
browser plugins.")

    Clears data associated with plugins.
[`browsingData.settings()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/settings "Browsers have a built-in "Clear
History" feature, which enables the user to clear various types of browsing
data. This has a UI that enables the user to select what type of data to
remove \(e.g. history, downloads, ...\) and how far back in time to remove
data.")

    Gets the current value of settings in the browser's "Clear History" feature.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`remove`|  Yes|  No| 53 *| 57 *|  Yes  
`removeCache`|  Yes|  No| 53 *| 57 *|  Yes  
`removeCookies`|  Yes|  No| 53| 56|  Yes  
`removeDownloads`|  Yes|  No| 53| 57|  Yes  
`removeFormData`|  Yes|  No| 53| 57|  Yes  
`removeHistory`|  Yes|  No| 53 *|  No|  Yes  
`removeLocalStorage`|  Yes|  No| 57 *| 57 *|  Yes  
`removePasswords`|  Yes|  No| 53|  No|  Yes  
`removePluginData`|  Yes|  No| 53|  No|  Yes  
`settings`|  Yes|  No| 53| 56|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`remove`|  Full support Yes|  No support No|  Full support 53

Notes __

Full support 53

Notes __

     Notes __Specifying`dataTypes.history` will also remove download history and service workers.
|  Full support Yes|  Full support 57

Notes __

Full support 57

Notes __

     Notes __Specifying`dataTypes.history` will also remove download history and service workers.  
`removeCache`|  Full support Yes|  No support No|  Full support 53

Notes __

Full support 53

Notes __

     Notes __`removalOptions.since` is not supported.
|  Full support Yes|  Full support 57

Notes __

Full support 57

Notes __

     Notes __`removalOptions.since` is not supported.  
`removeCookies`|  Full support Yes|  No support No|  Full support 53|  Full
support Yes|  Full support 56  
`removeDownloads`|  Full support Yes|  No support No|  Full support 53|  Full
support Yes|  Full support 57  
`removeFormData`|  Full support Yes|  No support No|  Full support 53|  Full
support Yes|  Full support 57  
`removeHistory`|  Full support Yes|  No support No|  Full support 53

Notes __

Full support 53

Notes __

     Notes __This function also removes download history and service workers.
|  Full support Yes|  No support No  
`removeLocalStorage`|  Full support Yes|  No support No|  Full support 57

Notes __

Full support 57

Notes __

     Notes __`removalOptions.since` is not supported.
|  Full support Yes|  Full support 57

Notes __

Full support 57

Notes __

     Notes __`removalOptions.since` is not supported.  
`removePasswords`|  Full support Yes|  No support No|  Full support 53|  Full
support Yes|  No support No  
`removePluginData`|  Full support Yes|  No support No|  Full support 53|  Full
support Yes|  No support No  
`settings`|  Full support Yes|  No support No|  Full support 53|  Full support
Yes|  Full support 56  
  
The "Chrome incompatibilities" section is included from [
https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Chrome_incompatibilities](https://developer.mozilla.org/en-
US/Add-ons/WebExtensions/Chrome_incompatibilities) using the
[WebExtChromeCompat](/en-US/docs/Template:WebExtChromeCompat) macro.

If you need to update this content, edit <https://developer.mozilla.org/en-US
/Add-ons/WebExtensions/Chrome_incompatibilities>, then shift-refresh this page
to see your changes.

## Example extensions

  * [forget-it](https://github.com/mdn/webextensions-examples/tree/master/forget-it)

**Acknowledgements**

This API is based on Chromium's
[`chrome.browsingData`](https://developer.chrome.com/extensions/browsingData)
API.

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

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[
Full support

]: Full support

  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

