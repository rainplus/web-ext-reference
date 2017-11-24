[



Use the topSites API to get an array containing all the sites listed in the
browser's "New Tab" page.



The "New Tab" page is the page that opens when the user opens a new tab
without immediately loading a page into it: for example, using the "Open a new
tab" button. The browser generally fills this list with sites the user visits
most often.



To use the topSites API you must have the "topSites" [API
permission](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).



## Types



[`topSites.MostVisitedURL`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/topSites/MostVisitedURL "The MostVisitedURL type
contains two properties: the title of a page and its URL.")

    An object containing the title and URL of a website.



## Functions



[`topSites.get()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/topSites/get "Gets an array containing all the sites
listed in the browser's "New Tab" page.")

    Gets an array containing all the sites listed in the browser's "New Tab"
page. Note that the number of sites returned here is browser-specific, and the
particular sites returned will probably be specific to the user, based on
their browsing history.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`MostVisitedURL`|  Yes|  No| 52| 52|  Yes  
`get`|  Yes|  No| 52| 52|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`MostVisitedURL`|  Full support Yes| No support No| Full
support 52| Full support Yes| Full support 52  
`get`| Full support Yes| No support No| Full support 52|
Full support Yes| Full support 52  
  


## Example extensions

  * [top-sites](https://github.com/mdn/webextensions-examples/tree/master/top-sites)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.topSites`](https://developer.chrome.com/extensions/topSites) API.



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
  *[Chrome __]: Chrome

