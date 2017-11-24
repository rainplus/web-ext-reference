[\n

\n

\n

This page describes the WebExtensions devtools APIs as they exist in Firefox
54. Although the APIs are based on the [Chrome devtools
APIs](https://developer.chrome.com/extensions/devtools), there are still many
features that are not yet implemented in Firefox, and therefore are not
documented here. To see which features are currently missing please see
[Limitations of the devtools APIs](/en-US/Add-
ons/WebExtensions/Using_the_devtools_APIs#Limitations_of_the_devtools_APIs).

\n

\n

The `devtools.network` API lets a devtools extension get information about
network requests associated with the window that the devtools are attached to
(the inspected window).

\n

Like all the `devtools` APIs, this API is only available to code running in
the document defined in the [devtools_page](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/devtools_page) manifest.json key, or in other
devtools documents created by the extension (such as the panel's own
document). See [Extending the developer tools](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Extending_the_developer_tools) for more.

\n

## Events

\n

\n`[devtools.network.onNavigated](/en-US/Add-
ons/WebExtensions/API/devtools.network/onNavigated)`

\n    Fired when the user navigates the inspected window to a new page.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`onNavigated`| \n Yes| \n No| 54| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`onNavigated`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n Yes| \nNo support\n\n No  
  
\n

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.devtools.network`](https://developer.chrome.com/extensions/devtools_network)
API.

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

