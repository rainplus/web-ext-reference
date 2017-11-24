This page describes the WebExtensions devtools APIs as they exist in Firefox
54. Although the APIs are based on the [Chrome devtools
APIs](https://developer.chrome.com/extensions/devtools), there are still many
features that are not yet implemented in Firefox, and therefore are not
documented here. To see which features are currently missing please see
[Limitations of the devtools APIs](/en-US/Add-
ons/WebExtensions/Using_the_devtools_APIs#Limitations_of_the_devtools_APIs).

The `devtools.network` API lets a devtools extension get information about
network requests associated with the window that the devtools are attached to
(the inspected window).

Like all the `devtools` APIs, this API is only available to code running in
the document defined in the [devtools_page](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/devtools_page) manifest.json key, or in other
devtools documents created by the extension (such as the panel's own
document). See [Extending the developer tools](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Extending_the_developer_tools) for more.

## Events

`[devtools.network.onNavigated](/en-US/Add-
ons/WebExtensions/API/devtools.network/onNavigated)`

    Fired when the user navigates the inspected window to a new page.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`onNavigated`|  Yes|  No| 54|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`onNavigated`|  Full support Yes|  No support No|  Full support 54|  Full
support Yes|  No support No  
  
**Acknowledgements**

This API is based on Chromium's
[`chrome.devtools.network`](https://developer.chrome.com/extensions/devtools_network)
API.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.
    //
    // Redistribution and use in source and binary forms, with or without
    // modification, are permitted provided that the following conditions are
    // met:
    //
    //    * Redistributions of source code must retain the above copyright
    // notice, this list of conditions and the following disclaimer.
    //    * Redistributions in binary form must reproduce the above
    // copyright notice, this list of conditions and the following disclaimer
    // in the documentation and/or other materials provided with the
    // distribution.
    //    * Neither the name of Google Inc. nor the names of its
    // contributors may be used to endorse or promote products derived from
    // this software without specific prior written permission.
    //
    // THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    // "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    // LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    // A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    // OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    // SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    // LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    // DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    // THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    // (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    // OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

