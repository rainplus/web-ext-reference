[\n

\n

Use the identity API to get an [OAuth2](https://oauth.net/2/) authorization
code or access token, which an extension can then use to access user data from
a service which supports OAuth2 access (such as a Google or a Facebook
account).

\n

Details of how the OAuth2 flow works differ from one service provider to
another, so to use this API with a particular service provider, you'll need to
consult their documentation. For example:

\n

\n

  * <https://developers.google.com/identity/protocols/OAuth2UserAgent>
\n

  * <https://developer.github.com/v3/oauth/>
\n

\n

The identity API provides the [`identity.launchWebAuthFlow()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/identity/launchWebAuthFlow "Performs
the first part of an OAuth2 flow, including user authentication and client
authorization.") function. This authenticates the user with the service, if
necessary, and asks the user to authorize the extension to access data, if
necessary. The function completes with an access token or authorization code,
depending on the provider.

\n

The extension then completes the OAuth2 flow to get a validated access token,
and can then use this in HTTP requests to access the user's data according to
the authorization the user gave.

\n

To use this API, you must have the "identity" [API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).

\n

## Setup

\n

There's some setup you must do before publishing your extension.

\n

### Getting the redirect URL

\n

The [redirect URL](https://www.oauth.com/oauth2-servers/redirect-uris/)
represents the end point of [`identity.launchWebAuthFlow()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/identity/launchWebAuthFlow "Performs
the first part of an OAuth2 flow, including user authentication and client
authorization."), in which the access token or authorization code is delivered
to the extension.

\n

You can get a redirect URL by calling [`identity.getRedirectURL()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/identity/getRedirectURL "Generates a
URL that you can use as a redirect URL."). This function derives a redirect
URL from the add-on's ID, so if you want to use it, you should probably set
your add-on's ID explicitly using the `[applications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/applications)` key (otherwise, each time you
[temporarily install the add-on](/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox), you'll get a different
redirect URL).

\n

You don't have to use the redirect URL returned by
`identity.getRedirectURL()`: you can supply your own, and it can be anything
that the service will redirect to. However, it should use a domain that you
control.

\n

You'll use the redirect URL in two places:

\n

\n

  * supply it when registering your extension as an OAuth2 client
\n

  * pass it into `identity.launchWebAuthFlow()`, as a URL parameter added to that function's `url` argument.
\n

\n

### Registering your extension

\n

Before you can use OAuth2 with a service provider, you must register the
extension with the provider as an OAuth2 client.

\n

This will tend to be specific to the service provider, but in general it means
creating an entry for your extension on the provider's website. In this
process you will\xa0supply your redirect URL, and receive a client ID (and
sometimes also a secret). You'll need to pass both of these into
[`identity.launchWebAuthFlow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/identity/launchWebAuthFlow "Performs the first part of
an OAuth2 flow, including user authentication and client authorization.").

\n

## Functions

\n

\n[`identity.getRedirectURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/identity/getRedirectURL "Generates a URL that you can
use as a redirect URL.")

\n    Gets the redirect URL.

\n[`identity.launchWebAuthFlow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/identity/launchWebAuthFlow "Performs the first part of
an OAuth2 flow, including user authentication and client authorization.")

\n    Launches WAF.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`getRedirectURL`| \n Yes| \n No| 53| 53| \n No  
`launchWebAuthFlow`| \n Yes| \n No| 53| 53| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`getRedirectURL`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53| \nNo support\n\n No| \nFull support\n\n 53  
`launchWebAuthFlow`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 53| \nFull support\n\n Yes| \nFull support\n\n 53  
  
\n

## Example extensions

  * [google-userinfo](https://github.com/mdn/webextensions-examples/tree/master/google-userinfo)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.identity`](https://developer.chrome.com/extensions/identity) API.

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

