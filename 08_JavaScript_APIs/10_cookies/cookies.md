[\n

\n

Enables extensions to get and set cookies, and be notified when they change.

\n

To use this API, you need to include the "cookies" [API permission](/en-US
/Add-ons/WebExtensions/manifest.json/permissions#API_permissions) in your
[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) file, as well as [host permissions](/en-US
/Add-ons/WebExtensions/manifest.json/permissions#Host_permissions) for the
sites whose cookies you need to access. See [cookie Permissions](/en-US/Add-
ons/WebExtensions/API/cookies#Permissions).

\n

## Types

\n

\n[`cookies.Cookie`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/Cookie "The documentation about this has not yet
been written; please consider contributing!")

\n    Represents information about an HTTP cookie.

\n[`cookies.CookieStore`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/CookieStore "The documentation about this has
not yet been written; please consider contributing!")

\n    Represents a cookie store in the browser.

\n[`cookies.OnChangedCause`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/OnChangedCause "The documentation about this has
not yet been written; please consider contributing!")

\n    Represents the reason a cookie changed.

\n\n

## Methods

\n

\n[`cookies.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies/get
"The get\(\) method of the cookies API retrieves information about a single
cookie, given its name and URL.")

\n    Retrieves information about a single cookie.

\n[`cookies.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/getAll "The getAll\(\) method of the cookies API
retrieves all cookies from a single cookie store that match the given
information.")

\n    Retrieves all cookies that match a given set of filters.

\n[`cookies.set()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies/set
"The set\(\) method of the cookies API sets a cookie containing the specified
cookie data. This method is equivalent to issuing an HTTP Set-Cookie header
during a request to a given URL.")

\n    Sets a cookie with the given cookie data; may overwrite equivalent
cookies if they exist.

\n[`cookies.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/remove "The remove\(\) method of the cookies API
deletes a cookie, given its name and URL.")

\n    Deletes a cookie by name.

\n[`cookies.getAllCookieStores()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/getAllCookieStores "The getAllCookieStores\(\)
method of the cookies API returns a list of all cookie stores.")

\n    Lists all existing cookie stores.

\n\n

## Event handlers

\n

\n[`cookies.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/cookies/onChanged "The onChanged event of
the\\xa0cookies API is fired when a cookie is set or removed.")

\n    Fired when a cookie is set or removed.

\n\n

## Permissions

\n

In order to use this API, an add-on must specify the "cookies" [API permission
](/en-US/Add-ons/WebExtensions/manifest.json/permissions#API_permissions) in
its manifest, along with [host permissions](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions) for any sites
for which it wishes to access cookies. The add-on may read or write any
cookies which could be read or written by a URL matching the host permissions.
For example:

\n

\n`http://*.example.com/`

\n    \n

An add-on with this host permission may:

\n

\n

  * Read a non-secure cookie for `www.example.com`, with any path.
\n

  * Write a secure or non-secure cookie for `www.example.com`, with any path.
\n

\n

It may _not_ :

\n

\n

  * Read a secure cookie for `www.example.com`.
\n

\n

\n`http://www.example.com/`

\n    \n

An add-on with this host permission may:

\n

\n

  * Read a non-secure cookie for `www.example.com`, with any path.
\n

  * Read a non-secure cookie for `.example.com`, with any path.
\n

  * Write a secure or non-secure cookie for `www.example.com` with any path.
\n

  * Write a secure or non-secure cookie for `.example.com` with any path.
\n

\n

It may _not_ :

\n

\n

  * Read or write a cookie for `foo.example.com`.
\n

  * Read or write a cookie for `foo.www.example.com`.
\n

\n

\n`*://*.example.com/`

\n    \n

An add-on with this host permission may:

\n

\n

  * Read or write a secure or non-secure cookie for `www.example.com` with any path.
\n

\n

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Cookie`| \n Yes| \n Yes| 45| 48| \n Yes  
`CookieStore`| \n Yes| \n Yes| 45| 48| \n Yes  
`OnChangedCause`| \n Yes| \n No| 45| 48| \n Yes  
`get`| \n Yes| \n Yes| 45 *| 48| \n Yes  
`getAll`| \n Yes| \n Yes *| 45 *| 48| \n Yes  
`getAllCookieStores`| \n Yes| \n Yes *| 45 *| 48| \n Yes  
`onChanged`| \n Yes| \n No| 45| 48| \n Yes  
`remove`| \n Yes| \n Yes| 45 *| 48 *| \n Yes  
`set`| \n Yes| \n Yes| 45 *| 48 *| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Cookie`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 48  
`CookieStore`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`OnChangedCause`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 48  
`get`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Provides access to cookies from private browsing mode and container tabs since version 52.
|  \nFull support\n\n Yes| \nFull support\n\n 48  
`getAll`| \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If no URL is provided, cookies are retrieved only for URLs in currently opened tabs. In Chrome, this gets all cookies on a user's machine.
|  \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Before version 52, the 'tabIds' list was empty and only cookies from the default cookie store were returned. From version 52 onwards, this has been fixed and the result includes cookies from private browsing mode and container tabs.
|  \nFull support\n\n Yes| \nFull support\n\n 48  
`getAllCookieStores`| \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Always returns the same default cookie store with ID 0. All cookies belong to this store.
|  \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Before version 52, only the default cookie store was visible. From version 52 onwards, the cookie stores for private browsing mode and container tabs are also readable.
|  \nFull support\n\n Yes| \nFull support\n\n 48  
`onChanged`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 48  
`remove`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Before version 56, this function did not remove cookies from private browsing mode. From version 56 onwards this is fixed.
|  \nFull support\n\n Yes| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Before version 56, this function did not remove cookies from private browsing mode. From version 56 onwards this is fixed.  
`set`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n 45

Notes __

\nFull support\n\n 45

Notes __

     Notes __Before version 56, this function did not modify cookies in private browsing mode. From version 56 onwards this is fixed.
|  \nFull support\n\n Yes| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Before version 56, this function did not modify cookies in private browsing mode. From version 56 onwards this is fixed.  
  
\n

## Example extensions

  * [cookie-bg-picker](https://github.com/mdn/webextensions-examples/tree/master/cookie-bg-picker)
  * [list-cookies](https://github.com/mdn/webextensions-examples/tree/master/list-cookies)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.cookies`](https://developer.chrome.com/extensions/cookies) API. This
documentation is derived from
[`cookies.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/cookies.json)
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
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

