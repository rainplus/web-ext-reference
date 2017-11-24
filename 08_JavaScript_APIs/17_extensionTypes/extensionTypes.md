[\n

\n

Some common types used in other WebExtension APIs.

\n

## Types

\n

\n[`extensionTypes.ImageFormat`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extensionTypes/ImageFormat "The format of an image.")

\n    The format of an image.

\n[`extensionTypes.ImageDetails`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extensionTypes/ImageDetails "Details about the format
and quality of an image.")

\n    Details about the format and quality of an image.

\n[`extensionTypes.RunAt`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extensionTypes/RunAt "The soonest that the JavaScript or
CSS will be injected into the tab.")

\n    The soonest that the JavaScript or CSS will be injected into the tab.

\n`extensionTypes.CSSOrigin`

\n    Indicates whether a CSS stylesheet injected
by\xa0`[tabs.insertCSS](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/API/tabs/insertCSS)` should be treated as an "author" or
"user" stylesheet.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ImageDetails`| \n Yes *| \n Yes *| 45| 48| \n Yes *  
`ImageFormat`| \n Yes *| \n Yes *| 45| 48| \n Yes *  
`RunAt`| 20 *| \n No| 45| 48| 15 *  
`CSSOrigin`| \n No| \n No| 53| 53| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ImageDetails`|  \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nFull support\n\n 45| \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nFull support\n\n 48  
`ImageFormat`| \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nFull support\n\n 45| \nPartial support\nPartial

Notes __

\nPartial support\nPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nFull support\n\n 48  
`RunAt`| \nPartial support\n20

Notes __

\nPartial support\n20

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nNo support\n\n No| \nFull support\n\n 45| \nPartial support\n15

Notes __

\nPartial support\n15

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  \nFull support\n\n 48  
`CSSOrigin`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 53|
\nNo support\n\n No| \nFull support\n\n 53  
  
\n

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.extensionTypes`](https://developer.chrome.com/extensions/extensionTypes)
API. This documentation is derived from
[`extension_types.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/extension_types.json)
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
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

