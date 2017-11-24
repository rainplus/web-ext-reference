[\n

\n

Enables extensions to clear the data that is accumulated while the user is
browsing.

\n

In the `browsingData` API, browsing data is divided into types:

\n

\n

  * browser cache
\n

  * cookies
\n

  * downloads
\n

  * history
\n

  * local storage
\n

  * plugin data
\n

  * saved form data
\n

  * saved passwords
\n

\n

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

\n

All the `browsingData.remove[X]()` functions take a
[`browsingData.RemovalOptions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/RemovalOptions "The
browsingData.RemovalOptions type contains options to control certain aspects
of browsing data removal.") object, which you can use to control two further
aspects of data removal:

\n

\n

  * how far back in time to remove data
\n

  * whether to remove data only from normal web pages, or also from hosted web apps and add-ons. Note that this option is not yet supported in Firefox.
\n

\n

Finally, this API gives you a\xa0[`browsingData.settings()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/browsingData/settings "Browsers have
a built-in "Clear History" feature, which enables the user to clear various
types of browsing data. This has a UI that enables the user to select what
type of data to remove \(e.g. history, downloads, ...\) and how far back in
time to remove data.") function that gives you the current value of the
settings for the browser's built-in "Clear History" feature.

\n

To use this API you must have the "browsingData" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).

\n

## Types

\n

\n[`browsingData.DataTypeSet`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/DataTypeSet "The browsingData.DataTypeSet
type describes a set of data types.")

\n    Object used to specify the type of data to remove: for example, history,
downloads, passwords, and so on.

\n[`browsingData.RemovalOptions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/RemovalOptions "The
browsingData.RemovalOptions type contains options to control certain aspects
of browsing data removal.")

\n    Object used to specify how far back in time to remove data, and whether
to remove data added through normal web browsing, by hosted apps, or by add-
ons.

\n\n

## Methods

\n

\n[`browsingData.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/remove "Removes the specified browsing
data.")

\n    Removes browsing data for the data types specified.

\n[`browsingData.removeCache()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeCache "Clears the browser's cache.")

\n    Clears the browser's cache.

\n[`browsingData.removeCookies()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeCookies "The documentation about this
has not yet been written; please consider contributing!")

\n    Removes cookies.

\n[`browsingData.removeDownloads()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeDownloads "Clears the browser's
download history. Note that this does not delete the downloaded objects
themselves, only records of downloads in the browser's history.")

\n    Removes the list of downloaded files.

\n[`browsingData.removeFormData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeFormData "The documentation about
this has not yet been written; please consider contributing!")

\n    Clears saved form data.

\n[`browsingData.removeHistory()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeHistory "The documentation about this
has not yet been written; please consider contributing!")

\n    Clears the browser's history.

\n[`browsingData.removeLocalStorage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removeLocalStorage "The documentation about
this has not yet been written; please consider contributing!")

\n    Clears any [local storage](/en-US/docs/Web/API/Window/localStorage)
created by websites.

\n[`browsingData.removePasswords()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removePasswords "The documentation about
this has not yet been written; please consider contributing!")

\n    Clears saved passwords.

\n[`browsingData.removePluginData()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/removePluginData "Clears data stored by
browser plugins.")

\n    Clears data associated with plugins.

\n[`browsingData.settings()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browsingData/settings "Browsers have a built-in "Clear
History" feature, which enables the user to clear various types of browsing
data. This has a UI that enables the user to select what type of data to
remove \(e.g. history, downloads, ...\) and how far back in time to remove
data.")

\n    Gets the current value of settings in the browser's "Clear History"
feature.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`remove`| \n Yes| \n No| 53 *| 57 *| \n Yes  
`removeCache`| \n Yes| \n No| 53 *| 57 *| \n Yes  
`removeCookies`| \n Yes| \n No| 53| 56| \n Yes  
`removeDownloads`| \n Yes| \n No| 53| 57| \n Yes  
`removeFormData`| \n Yes| \n No| 53| 57| \n Yes  
`removeHistory`| \n Yes| \n No| 53 *| \n No| \n Yes  
`removeLocalStorage`| \n Yes| \n No| 57 *| 57 *| \n Yes  
`removePasswords`| \n Yes| \n No| 53| \n No| \n Yes  
`removePluginData`| \n Yes| \n No| 53| \n No| \n Yes  
`settings`| \n Yes| \n No| 53| 56| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`remove`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 53

Notes __

\nFull support\n\n 53

Notes __

     Notes __Specifying`dataTypes.history` will also remove download history and service workers.
|  \nFull support\n\n Yes| \nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __Specifying`dataTypes.history` will also remove download history and service workers.  
`removeCache`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53

Notes __

\nFull support\n\n 53

Notes __

     Notes __`removalOptions.since` is not supported.
|  \nFull support\n\n Yes| \nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __`removalOptions.since` is not supported.  
`removeCookies`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53| \nFull support\n\n Yes| \nFull support\n\n 56  
`removeDownloads`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53| \nFull support\n\n Yes| \nFull support\n\n 57  
`removeFormData`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53| \nFull support\n\n Yes| \nFull support\n\n 57  
`removeHistory`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53

Notes __

\nFull support\n\n 53

Notes __

     Notes __This function also removes download history and service workers.
|  \nFull support\n\n Yes| \nNo support\n\n No  
`removeLocalStorage`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __`removalOptions.since` is not supported.
|  \nFull support\n\n Yes| \nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __`removalOptions.since` is not supported.  
`removePasswords`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53| \nFull support\n\n Yes| \nNo support\n\n No  
`removePluginData`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53| \nFull support\n\n Yes| \nNo support\n\n No  
`settings`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
53| \nFull support\n\n Yes| \nFull support\n\n 56  
  
\n

\n

The "Chrome incompatibilities" section is included from [
https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Chrome_incompatibilities](https://developer.mozilla.org/en-
US/Add-ons/WebExtensions/Chrome_incompatibilities) using the
[WebExtChromeCompat](/en-US/docs/Template:WebExtChromeCompat) macro.

\n

If you need to update this content, edit <https://developer.mozilla.org/en-US
/Add-ons/WebExtensions/Chrome_incompatibilities>, then shift-refresh this page
to see your changes.

\n

\n

## Example extensions

  * [forget-it](https://github.com/mdn/webextensions-examples/tree/master/forget-it)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.browsingData`](https://developer.chrome.com/extensions/browsingData)
API.

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
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

