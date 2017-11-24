[



Some common types used in other WebExtension APIs.



## Types



[`extensionTypes.ImageFormat`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extensionTypes/ImageFormat "The format of an image.")

    The format of an image.

[`extensionTypes.ImageDetails`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extensionTypes/ImageDetails "Details about the format
and quality of an image.")

    Details about the format and quality of an image.

[`extensionTypes.RunAt`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/extensionTypes/RunAt "The soonest that the JavaScript or
CSS will be injected into the tab.")

    The soonest that the JavaScript or CSS will be injected into the tab.

`extensionTypes.CSSOrigin`

    Indicates whether a CSS stylesheet injected
by\xa0`[tabs.insertCSS](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/API/tabs/insertCSS)` should be treated as an "author" or
"user" stylesheet.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ImageDetails`|  Yes *|  Yes *| 45| 48|  Yes *  
`ImageFormat`|  Yes *|  Yes *| 45| 48|  Yes *  
`RunAt`| 20 *|  No| 45| 48| 15 *  
`CSSOrigin`|  No|  No| 53| 53|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ImageDetails`|  Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  Full support 45| Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  Full support 48  
`ImageFormat`| Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  Full support 45| Partial supportPartial

Notes __

Partial supportPartial

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  Full support 48  
`RunAt`| Partial support20

Notes __

Partial support20

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  No support No| Full support 45| Partial support15

Notes __

Partial support15

Notes __

     Notes __This feature is supported but not exposed through the 'extensionTypes' object.
|  Full support 48  
`CSSOrigin`| No support No| No support No| Full support 53|
No support No| Full support 53  
  




 **Acknowledgements** 

This API is based on Chromium's
[`chrome.extensionTypes`](https://developer.chrome.com/extensions/extensionTypes)
API. This documentation is derived from
[`extension_types.json`](https://chromium.googlesource.com/chromium/src/+/master/extensions/common/api/extension_types.json)
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
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[ Partial support]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

