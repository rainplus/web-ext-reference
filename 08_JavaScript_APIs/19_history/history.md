[



Use the `history` API to interact with the browser history.





Note that downloads are treated as
[`HistoryItem`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/HistoryItem "A HistoryItem object provides
information about a page in the browser history.") objects. Therefore, events
such as [`history.onVisited`](https://developer.mozilla.org/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/history/onVisited "Fired each time the user visits
a page. A history.HistoryItem object is passed to the listener. This event
fires before the page has loaded.") will also fire for downloads.





Browser history is a chronological record of pages the user has visited. The
history API enables you to:





  * [search for pages that appear in the browser history](/en-US/Add-ons/WebExtensions/API/history/search)


  * [remove individual pages from the browser history](/en-US/Add-ons/WebExtensions/API/history/deleteUrl)


  * [add pages to the browser history](/en-US/Add-ons/WebExtensions/API/history/addUrl)


  * [remove all pages from the browser history](/en-US/Add-ons/WebExtensions/API/history/deleteAll).




However, the user may have visited a single page multiple times, so the API
also has the concept of "visits". So you can also use this API to:





  * [retrieve the complete set of visits the user made to a particular page](/en-US/Add-ons/WebExtensions/API/history/getVisits)


  * [remove visits to any pages made during a given time period](/en-US/Add-ons/WebExtensions/API/history/deleteRange).




To use this API, an extension must request the "history"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) in its
`[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json)` file.



## Types



[`history.TransitionType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/TransitionType "This describes how the browser
navigated to a particular page. For example, "link" means that the browser
navigated to the page because the user clicked a link.")

    Describes how the browser navigated to a particular page.

[`history.HistoryItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/HistoryItem "A HistoryItem object provides
information about a page in the browser history.")

    

Provides information about a particular page in the browser history.



[`history.VisitItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/VisitItem "An object describing a single visit
to a page.")

    

Describes a single visit to a page.





## Functions



[`history.search()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/search "Searches the browser's history for
history.HistoryItem objects matching the given criteria.")

    Searches the browser history for
[`history.HistoryItem`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/History/HistoryItem "A HistoryItem object provides
information about one result from a history query.") objects matching the
given criteria.

[`history.getVisits()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/getVisits "Retrieves information about all
visits to the given URL.")

    Retrieves information about visits to a given page.

[`history.addUrl()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/addUrl "Adds a record to the browser's history
of a visit to the given URL. The visit's time is recorded as the time of the
call, and the TransitionType is recorded as "link".")

    Adds a record to the browser history of a visit to the given page.

[`history.deleteUrl()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/deleteUrl "Removes all visits to the given URL
from the browser history.")

    Removes all visits to the given URL from the browser history.

[`history.deleteRange()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/deleteRange "Removes all visits to pages that
the user made during the given time range. If this removes all visits made to
a given page, then the page will be no longer appear in the browser history
and history.onVisitRemoved will fire for it.")

    Removes all visits to pages that the user made during the given time
range.

[`history.deleteAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/deleteAll "Deletes all visits from the browser's
history.")

    Removes all visits from the browser history.



## Events



[`history.onTitleChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/onTitleChanged "Events have three functions:")

    

Fired when the title of a page visited by the user is recorded.



[`history.onVisited`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/onVisited "Fired each time the user visits a
page. A history.HistoryItem object is passed to the listener. This event fires
before the page has loaded.")

    Fired each time the user visits a page, providing the
[`history.HistoryItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/HistoryItem "A HistoryItem object provides
information about a page in the browser history.") data for that page.

[`history.onVisitRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/onVisitRemoved "Fired when a page is removed
completely from the browser history.")

    

Fired when a URL is removed completely from the browser history.





## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`HistoryItem`|  Yes|  No| 49 *|  No|  Yes  
`TransitionType`|  Yes|  No| 50|  No|  Yes  
`VisitItem`|  Yes|  No| 50|  No|  Yes  
`addUrl`|  Yes *|  No| 49|  No|  Yes *  
`deleteAll`|  Yes|  No| 49|  No|  Yes  
`deleteRange`|  Yes|  No| 49|  No|  Yes  
`deleteUrl`|  Yes|  No| 49|  No|  Yes  
`getVisits`|  Yes|  No| 50|  No|  Yes  
`onTitleChanged`|  No|  No| 55|  No|  No  
`onVisitRemoved`|  Yes|  No| 50|  No|  Yes  
`onVisited`|  Yes|  No| 50 *|  No|  Yes  
`search`|  Yes|  No| 49|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`HistoryItem`|  Full support Yes| No support No| Partial
support49| Full support Yes| No support No  
`TransitionType`| Full support Yes| No support No| Full
support 50| Full support Yes| No support No  
`VisitItem`| Full support Yes| No support No| Full support
50| Full support Yes| No support No  
`addUrl`| Partial supportPartial| No support No| Full support
49| Partial supportPartial| No support No  
`deleteAll`| Full support Yes| No support No| Full support
49| Full support Yes| No support No  
`deleteRange`| Full support Yes| No support No| Full support
49| Full support Yes| No support No  
`deleteUrl`| Full support Yes| No support No| Full support
49| Full support Yes| No support No  
`getVisits`| Full support Yes| No support No| Full support
50| Full support Yes| No support No  
`onTitleChanged`| No support No| No support No| Full support
55| No support No| No support No  
`onVisitRemoved`| Full support Yes| No support No| Full
support 50| Full support Yes| No support No  
`onVisited`| Full support Yes| No support No| Full support
50

Notes __

Full support 50

Notes __

     Notes __Before version 56, the result object's 'title' was always an empty string. From version 56 onwards, it is set to the last known title, if that is available, or an empty string otherwise.
|  Full support Yes| No support No  
`search`| Full support Yes| No support No| Full support 49|
Full support Yes| No support No  
  


## Example extensions

  * [history-deleter](https://github.com/mdn/webextensions-examples/tree/master/history-deleter)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.history`](https://developer.chrome.com/extensions/history) API. This
documentation is derived from
[`history.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/history.json)
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
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

