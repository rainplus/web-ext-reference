[\n

\n

Access and modify various privacy-related browser settings.

\n

To use the privacy API, you must have the "privacy" [API permission](/en-US
/Add-ons/WebExtensions/manifest.json/permissions#API_permissions).

\n

## Properties

\n

\n[`privacy.network`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/privacy/network "Set the webRTCIPHandlingPolicy
property:")

\n    Access and modify privacy settings relating to the network.

\n[`privacy.services`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/privacy/services "The documentation about this has not
yet been written; please consider contributing!")

\n    Access and modify privacy settings relating to the services provided by
the browser or third parties.

\n[`privacy.websites`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/privacy/websites "Set the hyperlinkAuditingEnabled
property.")

\n    Access and modify privacy settings relating to the behavior of websites.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`network.networkPredictionEnabled`| \n Yes| \n No| 54| 54| \n Yes  
`network.peerConnectionEnabled`| \n No| \n No| 55| 55| \n No  
`network.webRTCIPHandlingPolicy`| \n Yes| \n No| 54| 54| \n Yes  
`services.passwordSavingEnabled`| \n Yes| \n No| 56| 56| \n Yes  
`websites.firstPartyIsolate`| \n No| \n No| 58| 58| \n No  
`websites.hyperlinkAuditingEnabled`| \n Yes| \n No| 54| 54| \n Yes  
`websites.protectedContentEnabled`| \n Yes| \n No| \n No| \n No| \n Yes  
`websites.referrersEnabled`| \n Yes| \n No| 56| 56| \n Yes  
`websites.resistFingerprinting`| \n No| \n No| 58| 58| \n No  
`websites.thirdPartyCookiesAllowed`| \n Yes| \n No| \n No| \n No| \n Yes  
`websites.trackingProtectionMode`| \n No| \n No| 57| 57| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`network.networkPredictionEnabled`|  \nFull support\n\n Yes| \nNo support\n\n
No| \nFull support\n\n 54| \nFull support\n\n Yes| \nFull support\n\n 54  
`network.peerConnectionEnabled`| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n 55| \nNo support\n\n No| \nFull support\n\n 55  
`network.webRTCIPHandlingPolicy`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 54| \nFull support\n\n Yes| \nFull support\n\n 54  
`services.passwordSavingEnabled`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 56| \nFull support\n\n Yes| \nFull support\n\n 56  
`websites.firstPartyIsolate`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 58| \nNo support\n\n No| \nFull support\n\n 58  
`websites.hyperlinkAuditingEnabled`| \nFull support\n\n Yes| \nNo support\n\n
No| \nFull support\n\n 54| \nFull support\n\n Yes| \nFull support\n\n 54  
`websites.protectedContentEnabled`| \nFull support\n\n Yes| \nNo support\n\n
No| \nNo support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`websites.referrersEnabled`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 56| \nFull support\n\n Yes| \nFull support\n\n 56  
`websites.resistFingerprinting`| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n 58| \nNo support\n\n No| \nFull support\n\n 58  
`websites.thirdPartyCookiesAllowed`| \nFull support\n\n Yes| \nNo support\n\n
No| \nNo support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`websites.trackingProtectionMode`| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n 57| \nNo support\n\n No| \nFull support\n\n 57  
  
\n

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.privacy`](https://developer.chrome.com/extensions/privacy) API.

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

