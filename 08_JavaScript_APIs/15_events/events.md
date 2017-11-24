[



Common types used by APIs that dispatch events.



## Types



[`events.Rule`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events/Rule
"Description of a declarative rule for handling events.")

    Description of a declarative rule for handling events.

[`events.Event`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events/Event
"An object which allows the addition and removal of listeners for a browser
event.")

    An object which allows the addition and removal of listeners for a
Chrome event.

[`events.UrlFilter`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/events/UrlFilter "Describes various criteria for
filtering URLs. If all of the criteria specified in the filter's properties
match the URL, then the filter matches. Filters are often provided to API
methods in an Array of UrlFilters. For example, webNavigation listeners can be
added with a filter which is an object with a single url property that is an
Array of UrlFilters, e.g. {url:\[UrlFilter,UrlFilter,...\]}. If any filter
within the Array of UrlFilters matches, then it is considered a match for the
Array. Effectively, the criteria specified within a single filter are AND'ed
together, while all of the individual filters within an Array are OR'ed.")

    Filters URLs for various criteria. If any of the given criteria match,
then the whole filter matches.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Event`|  Yes|  Yes|  No|  No|  Yes  
`Rule`|  Yes|  Yes|  No|  No|  Yes  
`UrlFilter`|  Yes|  Yes| 50| 50|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Event`|  Full support Yes| Full support Yes| No support No|
Full support Yes| No support No  
`Rule`| Full support Yes| Full support Yes| No support No|
Full support Yes| No support No  
`UrlFilter`| Full support Yes| Full support Yes| Full
support 50| Full support Yes| Full support 50  
  




 **Acknowledgements** 

This API is based on Chromium's
[`chrome.events`](https://developer.chrome.com/extensions/events) API. This
documentation is derived from
[`events.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/events.json)
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
  *[Chrome __]: Chrome

