[\n

\n

Use the `history` API to interact with the browser history.

\n

\n

Note that downloads are treated as
[`HistoryItem`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/HistoryItem "A HistoryItem object provides
information about a page in the browser history.") objects. Therefore, events
such as [`history.onVisited`](https://developer.mozilla.org/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/history/onVisited "Fired each time the user visits
a page. A history.HistoryItem object is passed to the listener. This event
fires before the page has loaded.") will also fire for downloads.

\n

\n

Browser history is a chronological record of pages the user has visited. The
history API enables you to:

\n

\n

  * [search for pages that appear in the browser history](/en-US/Add-ons/WebExtensions/API/history/search)
\n

  * [remove individual pages from the browser history](/en-US/Add-ons/WebExtensions/API/history/deleteUrl)
\n

  * [add pages to the browser history](/en-US/Add-ons/WebExtensions/API/history/addUrl)
\n

  * [remove all pages from the browser history](/en-US/Add-ons/WebExtensions/API/history/deleteAll).
\n

\n

However, the user may have visited a single page multiple times, so the API
also has the concept of "visits". So you can also use this API to:

\n

\n

  * [retrieve the complete set of visits the user made to a particular page](/en-US/Add-ons/WebExtensions/API/history/getVisits)
\n

  * [remove visits to any pages made during a given time period](/en-US/Add-ons/WebExtensions/API/history/deleteRange).
\n

\n

To use this API, an extension must request the "history"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) in its
`[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json)` file.

\n

## Types

\n

\n[`history.TransitionType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/TransitionType "This describes how the browser
navigated to a particular page. For example, "link" means that the browser
navigated to the page because the user clicked a link.")

\n    Describes how the browser navigated to a particular page.

\n[`history.HistoryItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/HistoryItem "A HistoryItem object provides
information about a page in the browser history.")

\n    \n

Provides information about a particular page in the browser history.

\n

\n[`history.VisitItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/VisitItem "An object describing a single visit
to a page.")

\n    \n

Describes a single visit to a page.

\n

\n\n

## Functions

\n

\n[`history.search()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/search "Searches the browser's history for
history.HistoryItem objects matching the given criteria.")

\n    Searches the browser history for
[`history.HistoryItem`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/History/HistoryItem "A HistoryItem object provides
information about one result from a history query.") objects matching the
given criteria.

\n[`history.getVisits()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/getVisits "Retrieves information about all
visits to the given URL.")

\n    Retrieves information about visits to a given page.

\n[`history.addUrl()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/addUrl "Adds a record to the browser's history
of a visit to the given URL. The visit's time is recorded as the time of the
call, and the TransitionType is recorded as "link".")

\n    Adds a record to the browser history of a visit to the given page.

\n[`history.deleteUrl()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/deleteUrl "Removes all visits to the given URL
from the browser history.")

\n    Removes all visits to the given URL from the browser history.

\n[`history.deleteRange()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/deleteRange "Removes all visits to pages that
the user made during the given time range. If this removes all visits made to
a given page, then the page will be no longer appear in the browser history
and history.onVisitRemoved will fire for it.")

\n    Removes all visits to pages that the user made during the given time
range.

\n[`history.deleteAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/deleteAll "Deletes all visits from the browser's
history.")

\n    Removes all visits from the browser history.

\n\n

## Events

\n

\n[`history.onTitleChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/onTitleChanged "Events have three functions:")

\n    \n

Fired when the title of a page visited by the user is recorded.

\n

\n[`history.onVisited`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/onVisited "Fired each time the user visits a
page. A history.HistoryItem object is passed to the listener. This event fires
before the page has loaded.")

\n    Fired each time the user visits a page, providing the
[`history.HistoryItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/HistoryItem "A HistoryItem object provides
information about a page in the browser history.") data for that page.

\n[`history.onVisitRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/history/onVisitRemoved "Fired when a page is removed
completely from the browser history.")

\n    \n

Fired when a URL is removed completely from the browser history.

\n

\n\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`HistoryItem`| \n Yes| \n No| 49 *| \n No| \n Yes  
`TransitionType`| \n Yes| \n No| 50| \n No| \n Yes  
`VisitItem`| \n Yes| \n No| 50| \n No| \n Yes  
`addUrl`| \n Yes *| \n No| 49| \n No| \n Yes *  
`deleteAll`| \n Yes| \n No| 49| \n No| \n Yes  
`deleteRange`| \n Yes| \n No| 49| \n No| \n Yes  
`deleteUrl`| \n Yes| \n No| 49| \n No| \n Yes  
`getVisits`| \n Yes| \n No| 50| \n No| \n Yes  
`onTitleChanged`| \n No| \n No| 55| \n No| \n No  
`onVisitRemoved`| \n Yes| \n No| 50| \n No| \n Yes  
`onVisited`| \n Yes| \n No| 50 *| \n No| \n Yes  
`search`| \n Yes| \n No| 49| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`HistoryItem`|  \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n49| \nFull support\n\n Yes| \nNo support\n\n No  
`TransitionType`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 50| \nFull support\n\n Yes| \nNo support\n\n No  
`VisitItem`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
50| \nFull support\n\n Yes| \nNo support\n\n No  
`addUrl`| \nPartial support\nPartial| \nNo support\n\n No| \nFull support\n\n
49| \nPartial support\nPartial| \nNo support\n\n No  
`deleteAll`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
49| \nFull support\n\n Yes| \nNo support\n\n No  
`deleteRange`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
49| \nFull support\n\n Yes| \nNo support\n\n No  
`deleteUrl`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
49| \nFull support\n\n Yes| \nNo support\n\n No  
`getVisits`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
50| \nFull support\n\n Yes| \nNo support\n\n No  
`onTitleChanged`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
55| \nNo support\n\n No| \nNo support\n\n No  
`onVisitRemoved`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 50| \nFull support\n\n Yes| \nNo support\n\n No  
`onVisited`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
50

Notes __

\nFull support\n\n 50

Notes __

     Notes __Before version 56, the result object's 'title' was always an empty string. From version 56 onwards, it is set to the last known title, if that is available, or an empty string otherwise.
|  \nFull support\n\n Yes| \nNo support\n\n No  
`search`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 49|
\nFull support\n\n Yes| \nNo support\n\n No  
  
\n

## Example extensions

  * [history-deleter](https://github.com/mdn/webextensions-examples/tree/master/history-deleter)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.history`](https://developer.chrome.com/extensions/history) API. This
documentation is derived from
[`history.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/history.json)
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
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

