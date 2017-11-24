[\n

\n

Find out when the user's system is idle, locked, or active.

\n

To use this API you need to have the "idle"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

\n

## Types

\n

\n[`idle.IdleState`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/idle/IdleState "String describing the device's idle
state.")

\n    \n

String describing the device's idle state.

\n

\n\n

## Functions

\n

\n[`idle.queryState()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/idle/queryState "Returns "locked" if the system is
locked, "idle" if the user has not generated any input for a specified number
of seconds, or "active" otherwise.")

\n    Returns `"locked"` if the system is locked, `"idle"` if the user has not
generated any input for a specified number of seconds, or `"active"`
otherwise.

\n[`idle.setDetectionInterval()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/idle/setDetectionInterval "Sets the interval, in
seconds, used to determine when the system is in an idle state for
idle.onStateChanged events. The default interval is 60 seconds.")

\n    Sets the interval used to determine when the system is in an idle state
for [`idle.onStateChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/idle/onStateChanged "Fired when the system changes to an
active, idle or locked state. The event listener is passed a string that has
one of three values:") events.

\n\n

## Events

\n

\n[`idle.onStateChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/idle/onStateChanged "Fired when the system changes to an
active, idle or locked state. The event listener is passed a string that has
one of three values:")

\n    Fired when the system changes state.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`IdleState`| \n Yes| \n No| 45| 48| \n Yes  
`onStateChanged`| \n Yes| \n No| 51 *| 51 *| \n Yes  
`queryState`| \n Yes| 15 *| 45 *| 48 *| \n Yes  
`setDetectionInterval`| \n Yes| 15| 51| 51| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`IdleState`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 48  
`onStateChanged`| \nFull support\n\n Yes| \nNo support\n\n No| \nPartial
support\n51| \nFull support\n\n Yes| \nPartial support\n51  
`queryState`| \nFull support\n\n Yes| \nPartial support\n15| \nPartial
support\n45

Notes __

\nPartial support\n45

Notes __

     Notes __Before version 51, Firefox always reports 'active'. After version 51, Firefox reports 'active' or 'idle' as appropriate.
|  \nFull support\n\n Yes| \nPartial support\n48

Notes __

\nPartial support\n48

Notes __

     Notes __Before version 51, Firefox always reports 'active'. After version 51, Firefox reports 'active' or 'idle' as appropriate.  
`setDetectionInterval`|  \nFull support\n\n Yes| \nFull support\n\n 15| \nFull
support\n\n 51| \nFull support\n\n Yes| \nFull support\n\n 51  
  
\n

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.idle`](https://developer.chrome.com/extensions/idle) API. This
documentation is derived from
[`idle.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/idle.json)
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
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

