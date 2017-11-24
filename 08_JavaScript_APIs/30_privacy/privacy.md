[



Access and modify various privacy-related browser settings.



To use the privacy API, you must have the "privacy" [API permission](/en-US
/Add-ons/WebExtensions/manifest.json/permissions#API_permissions).



## Properties



[`privacy.network`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/privacy/network "Set the webRTCIPHandlingPolicy
property:")

    Access and modify privacy settings relating to the network.

[`privacy.services`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/privacy/services "The documentation about this has not
yet been written; please consider contributing!")

    Access and modify privacy settings relating to the services provided by
the browser or third parties.

[`privacy.websites`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/privacy/websites "Set the hyperlinkAuditingEnabled
property.")

    Access and modify privacy settings relating to the behavior of websites.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`network.networkPredictionEnabled`|  Yes|  No| 54| 54|  Yes  
`network.peerConnectionEnabled`|  No|  No| 55| 55|  No  
`network.webRTCIPHandlingPolicy`|  Yes|  No| 54| 54|  Yes  
`services.passwordSavingEnabled`|  Yes|  No| 56| 56|  Yes  
`websites.firstPartyIsolate`|  No|  No| 58| 58|  No  
`websites.hyperlinkAuditingEnabled`|  Yes|  No| 54| 54|  Yes  
`websites.protectedContentEnabled`|  Yes|  No|  No|  No|  Yes  
`websites.referrersEnabled`|  Yes|  No| 56| 56|  Yes  
`websites.resistFingerprinting`|  No|  No| 58| 58|  No  
`websites.thirdPartyCookiesAllowed`|  Yes|  No|  No|  No|  Yes  
`websites.trackingProtectionMode`|  No|  No| 57| 57|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`network.networkPredictionEnabled`|  Full support Yes| No support
No| Full support 54| Full support Yes| Full support 54  
`network.peerConnectionEnabled`| No support No| No support No|
Full support 55| No support No| Full support 55  
`network.webRTCIPHandlingPolicy`| Full support Yes| No support No|
Full support 54| Full support Yes| Full support 54  
`services.passwordSavingEnabled`| Full support Yes| No support No|
Full support 56| Full support Yes| Full support 56  
`websites.firstPartyIsolate`| No support No| No support No| Full
support 58| No support No| Full support 58  
`websites.hyperlinkAuditingEnabled`| Full support Yes| No support
No| Full support 54| Full support Yes| Full support 54  
`websites.protectedContentEnabled`| Full support Yes| No support
No| No support No| Full support Yes| No support No  
`websites.referrersEnabled`| Full support Yes| No support No|
Full support 56| Full support Yes| Full support 56  
`websites.resistFingerprinting`| No support No| No support No|
Full support 58| No support No| Full support 58  
`websites.thirdPartyCookiesAllowed`| Full support Yes| No support
No| No support No| Full support Yes| No support No  
`websites.trackingProtectionMode`| No support No| No support No|
Full support 57| No support No| Full support 57  
  




 **Acknowledgements** 

This API is based on Chromium's
[`chrome.privacy`](https://developer.chrome.com/extensions/privacy) API.







    
    
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

