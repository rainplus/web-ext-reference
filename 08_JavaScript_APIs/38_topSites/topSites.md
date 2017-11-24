[\n

\n

Use the topSites API to get an array containing all the sites listed in the
browser's "New Tab" page.

\n

The "New Tab" page is the page that opens when the user opens a new tab
without immediately loading a page into it: for example, using the "Open a new
tab" button. The browser generally fills this list with sites the user visits
most often.

\n

To use the topSites API you must have the "topSites" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).

\n

## Types

\n

\n[`topSites.MostVisitedURL`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/topSites/MostVisitedURL "The MostVisitedURL type
contains two properties: the title of a page and its URL.")

\n    An object containing the title and URL of a website.

\n\n

## Functions

\n

\n[`topSites.get()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/topSites/get "Gets an array containing all the sites
listed in the browser's "New Tab" page.")

\n    Gets an array containing all the sites listed in the browser's "New Tab"
page. Note that the number of sites returned here is browser-specific, and the
particular sites returned will probably be specific to the user, based on
their browsing history.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`MostVisitedURL`| \n Yes| \n No| 52| 52| \n Yes  
`get`| \n Yes| \n No| 52| 52| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`MostVisitedURL`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nFull support\n\n 52  
`get`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 52|
\nFull support\n\n Yes| \nFull support\n\n 52  
  
\n

## Example extensions

  * [top-sites](https://github.com/mdn/webextensions-examples/tree/master/top-sites)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.topSites`](https://developer.chrome.com/extensions/topSites) API.

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
  *[Chrome __]: Chrome

