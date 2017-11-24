[



Enables extensions to store and retrieve data, and listen for changes to
stored items.



The storage system is based on the [Web Storage API](/en-
US/docs/Web/API/Web_Storage_API), with a few differences. Among other
differences, these include:





  * It's asynchronous.


  * Values are scoped to the extension, not to a specific domain (i.e. the same set of key/value pairs are available to all scripts in the background context and content scripts).


  * The values stored can be any JSON-ifiable value, not just `[String](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)`. Among other things, this includes: `[Array](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)` and `[Object](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)`, but only when their contents can can be represented as JSON, which does not include DOM nodes. You don't need to convert your values to JSON `Strings` prior to storing them, but they are represented as JSON internally, thus the requirement that they be JSON-ifiable.


  * Multiple key/value pairs can be set or retrieved in the same API call.




To use this API you need to include the "storage"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) in your [manifest.json](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file.



Each extension has its own storage area, which can be split into different
types of storage.



Although this API is similar to\xa0[`Window.localStorage`](/en-
US/docs/Web/API/Window/localStorage "The read-only localStorage property
allows you to access a Storage object for the Document's origin; the stored
data is saved across browser sessions.") it is recommended that you don't use
`Window.localStorage` in the extension code to store extension-related data.
Firefox will clear data stored by extensions using the localStorage API in
various scenarios where users clear their browsing history and data for
privacy reasons, while data saved using the `[storage.local](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/storage/local)` API will be
correctly persisted in these scenarios.



## Types



[`storage.StorageArea`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/StorageArea "The documentation about this has
not yet been written; please consider contributing!")

    An object representing a storage area.

[`storage.StorageChange`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/StorageChange "StorageChange objects contain the
following properties:")

    An object representing a change to a storage area.



## Properties



`storage` has three properties, which represent the different types of
available storage area.



[`storage.sync`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/sync
"Represents the sync storage area. Items in sync storage are synced by the
browser, and are available across all instances of that browser that the user
is logged into \(e.g. via Firefox sync, or a Google account\), across
different devices.")

    Represents the `sync` storage area. Items in `sync` storage are synced
by the browser, and are available across all instances of that browser that
the user is logged into, across different devices.

[`storage.local`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/local "Represents the local storage area. Items
in local storage are local to the machine the extension was installed on.")

    Represents the `local` storage area. Items in `local` storage are local
to the machine the extension was installed on.

[`storage.managed`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/managed "A storage.StorageArea object that
represents the managed storage area. Items in managed storage are set by the
domain administrator or other native applications installed on user's
computer, and are read-only for the extension. Trying to modify this storage
area results in an error.")

    Represents the `managed` storage area. Items in `managed` storage are
set by the domain administrator and are read-only for the extension. Trying to
modify this namespace results in an error.



## Events



[`storage.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/storage/onChanged "Fired when one or more items
change.")

    Fired when one or more items change in a storage area.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`StorageArea`|  Yes|  Yes *| 45 *| 48 *|  Yes *  
`StorageChange`|  Yes|  Yes| 45| 48|  Yes  
`local`|  Yes|  Yes| 45 *| 48|  Yes  
`managed`|  Yes|  No| 57 *|  No|  No  
`onChanged`|  Yes|  Yes| 45| 48|  Yes  
`sync`|  Yes| 15| 53|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`StorageArea`|  Full support Yes| Partial supportPartial| Partial
support45| Partial supportPartial| Partial support48  
`StorageChange`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 48  
`local`| Full support Yes| Full support Yes| Full support 45

Notes __

Full support 45

Notes __

     Notes __The storage API is supported in content scripts from version 48.
|  Full support Yes| Full support 48  
`managed`| Full support Yes| No support No| Full support 57

Notes __

Full support 57

Notes __

     Notes __Platform-specific storage backends, such as Windows registry keys, are not supported.
     Notes __Enforcement of extension-provided storage schemas is not supported.
     Notes __The`onChanged` event is not supported.
|  No support No| No support No  
`onChanged`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 48  
`sync`| Full support Yes| Full support 15| Full support 53|
No support No| No support No  
  


## Example extensions

  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page)
  * [embedded-webextension-bootstrapped](https://github.com/mdn/webextensions-examples/tree/master/embedded-webextension-bootstrapped)
  * [embedded-webextension-sdk](https://github.com/mdn/webextensions-examples/tree/master/embedded-webextension-sdk)
  * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
  * [forget-it](https://github.com/mdn/webextensions-examples/tree/master/forget-it)
  * [navigation-stats](https://github.com/mdn/webextensions-examples/tree/master/navigation-stats)
  * [proxy-blocker](https://github.com/mdn/webextensions-examples/tree/master/proxy-blocker)
  * [quicknote](https://github.com/mdn/webextensions-examples/tree/master/quicknote)
  * [stored-credentials](https://github.com/mdn/webextensions-examples/tree/master/stored-credentials)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.storage`](https://developer.chrome.com/extensions/storage) API. This
documentation is derived from
[`storage.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/storage.json)
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
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

