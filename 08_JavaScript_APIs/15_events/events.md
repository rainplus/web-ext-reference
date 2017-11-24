[\n

\n

Common types used by APIs that dispatch events.

\n

## Types

\n

\n[`events.Rule`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events/Rule
"Description of a declarative rule for handling events.")

\n    Description of a declarative rule for handling events.

\n[`events.Event`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events/Event
"An object which allows the addition and removal of listeners for a browser
event.")

\n    An object which allows the addition and removal of listeners for a
Chrome event.

\n[`events.UrlFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/events/UrlFilter "Describes various criteria for
filtering URLs. If all of the criteria specified in the filter's properties
match the URL, then the filter matches. Filters are often provided to API
methods in an Array of UrlFilters. For example, webNavigation listeners can be
added with a filter which is an object with a single url property that is an
Array of UrlFilters, e.g. {url:\[UrlFilter,UrlFilter,...\]}. If any filter
within the Array of UrlFilters matches, then it is considered a match for the
Array. Effectively, the criteria specified within a single filter are AND'ed
together, while all of the individual filters within an Array are OR'ed.")

\n    Filters URLs for various criteria. If any of the given criteria match,
then the whole filter matches.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Event`| \n Yes| \n Yes| \n No| \n No| \n Yes  
`Rule`| \n Yes| \n Yes| \n No| \n No| \n Yes  
`UrlFilter`| \n Yes| \n Yes| 50| 50| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Event`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`Rule`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`UrlFilter`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 50| \nFull support\n\n Yes| \nFull support\n\n 50  
  
\n

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.events`](https://developer.chrome.com/extensions/events) API. This
documentation is derived from
[`events.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/events.json)
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
  *[Chrome __]: Chrome

