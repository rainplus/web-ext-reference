[



Enables extensions to get and set cookies, and be notified when they change.



To use this API, you need to include the "cookies" [API permission](/en-US
/Add-ons/WebExtensions/manifest.json/permissions#API_permissions) in your
[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) file, as well as [host permissions](/en-US
/Add-ons/WebExtensions/manifest.json/permissions#Host_permissions) for the
sites whose cookies you need to access. See [cookie Permissions](/en-US/Add-
ons/WebExtensions/API/cookies#Permissions).



## Types



[`cookies.Cookie`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/Cookie "The documentation about this has not yet
been written; please consider contributing!")

    Represents information about an HTTP cookie.

[`cookies.CookieStore`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/CookieStore "The documentation about this has
not yet been written; please consider contributing!")

    Represents a cookie store in the browser.

[`cookies.OnChangedCause`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/OnChangedCause "The documentation about this has
not yet been written; please consider contributing!")

    Represents the reason a cookie changed.



## Methods



[`cookies.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies/get
"The get\(\) method of the cookies API retrieves information about a single
cookie, given its name and URL.")

    Retrieves information about a single cookie.

[`cookies.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/getAll "The getAll\(\) method of the cookies API
retrieves all cookies from a single cookie store that match the given
information.")

    Retrieves all cookies that match a given set of filters.

[`cookies.set()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies/set
"The set\(\) method of the cookies API sets a cookie containing the specified
cookie data. This method is equivalent to issuing an HTTP Set-Cookie header
during a request to a given URL.")

    Sets a cookie with the given cookie data; may overwrite equivalent
cookies if they exist.

[`cookies.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/remove "The remove\(\) method of the cookies API
deletes a cookie, given its name and URL.")

    Deletes a cookie by name.

[`cookies.getAllCookieStores()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/getAllCookieStores "The getAllCookieStores\(\)
method of the cookies API returns a list of all cookie stores.")

    Lists all existing cookie stores.



## Event handlers



[`cookies.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/onChanged "The onChanged event of
the\\xa0cookies API is fired when a cookie is set or removed.")

    Fired when a cookie is set or removed.



## Permissions



In order to use this API, an add-on must specify the "cookies" [API permission
](/en-US/Add-ons/WebExtensions/manifest.json/permissions#API_permissions) in
its manifest, along with [host permissions](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions) for any sites
for which it wishes to access cookies. The add-on may read or write any
cookies which could be read or written by a URL matching the host permissions.
For example:



`http://*.example.com/`

    

An add-on with this host permission may:





  * Read a non-secure cookie for `www.example.com`, with any path.


  * Write a secure or non-secure cookie for `www.example.com`, with any path.




It may _not_ :





  * Read a secure cookie for `www.example.com`.




`http://www.example.com/`

    

An add-on with this host permission may:





  * Read a non-secure cookie for `www.example.com`, with any path.


  * Read a non-secure cookie for `.example.com`, with any path.


  * Write a secure or non-secure cookie for `www.example.com` with any path.


  * Write a secure or non-secure cookie for `.example.com` with any path.




It may _not_ :





  * Read or write a cookie for `foo.example.com`.


  * Read or write a cookie for `foo.www.example.com`.




`*://*.example.com/`

    

An add-on with this host permission may:





  * Read or write a secure or non-secure cookie for `www.example.com` with any path.






## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Cookie`|  Yes|  Yes| 45| 48|  Yes  
`CookieStore`|  Yes|  Yes| 45| 48|  Yes  
`OnChangedCause`|  Yes|  No| 45| 48|  Yes  
`get`|  Yes|  Yes| 45 *| 48|  Yes  
`getAll`|  Yes|  Yes *| 45 *| 48|  Yes  
`getAllCookieStores`|  Yes|  Yes *| 45 *| 48|  Yes  
`onChanged`|  Yes|  No| 45| 48|  Yes  
`remove`|  Yes|  Yes| 45 *| 48 *|  Yes  
`set`|  Yes|  Yes| 45 *| 48 *|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Cookie`|  Full support Yes| Full support Yes| Full support
45| Full support Yes| Full support 48  
`CookieStore`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 48  
`OnChangedCause`| Full support Yes| No support No| Full
support 45| Full support Yes| Full support 48  
`get`| Full support Yes| Full support Yes| Full support 45

Notes __

Full support 45

Notes __

     Notes __Provides access to cookies from private browsing mode and container tabs since version 52.
|  Full support Yes| Full support 48  
`getAll`| Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If no URL is provided, cookies are retrieved only for URLs in currently opened tabs. In Chrome, this gets all cookies on a user's machine.
|  Full support 45

Notes __

Full support 45

Notes __

     Notes __Before version 52, the 'tabIds' list was empty and only cookies from the default cookie store were returned. From version 52 onwards, this has been fixed and the result includes cookies from private browsing mode and container tabs.
|  Full support Yes| Full support 48  
`getAllCookieStores`| Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Always returns the same default cookie store with ID 0. All cookies belong to this store.
|  Full support 45

Notes __

Full support 45

Notes __

     Notes __Before version 52, only the default cookie store was visible. From version 52 onwards, the cookie stores for private browsing mode and container tabs are also readable.
|  Full support Yes| Full support 48  
`onChanged`| Full support Yes| No support No| Full support
45| Full support Yes| Full support 48  
`remove`| Full support Yes| Full support Yes| Full support
45

Notes __

Full support 45

Notes __

     Notes __Before version 56, this function did not remove cookies from private browsing mode. From version 56 onwards this is fixed.
|  Full support Yes| Full support 48

Notes __

Full support 48

Notes __

     Notes __Before version 56, this function did not remove cookies from private browsing mode. From version 56 onwards this is fixed.  
`set`|  Full support Yes| Full support Yes| Full support 45

Notes __

Full support 45

Notes __

     Notes __Before version 56, this function did not modify cookies in private browsing mode. From version 56 onwards this is fixed.
|  Full support Yes| Full support 48

Notes __

Full support 48

Notes __

     Notes __Before version 56, this function did not modify cookies in private browsing mode. From version 56 onwards this is fixed.  
  


## Example extensions

  * [cookie-bg-picker](https://github.com/mdn/webextensions-examples/tree/master/cookie-bg-picker)
  * [list-cookies](https://github.com/mdn/webextensions-examples/tree/master/list-cookies)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.cookies`](https://developer.chrome.com/extensions/cookies) API. This
documentation is derived from
[`cookies.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/cookies.json)
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
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

