Use the identity API to get an [OAuth2](https://oauth.net/2/) authorization
code or access token, which an extension can then use to access user data from
a service which supports OAuth2 access (such as a Google or a Facebook
account).

Details of how the OAuth2 flow works differ from one service provider to
another, so to use this API with a particular service provider, you'll need to
consult their documentation. For example:

  * <https://developers.google.com/identity/protocols/OAuth2UserAgent>
  * <https://developer.github.com/v3/oauth/>

The identity API provides the [`identity.launchWebAuthFlow()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/identity/launchWebAuthFlow "Performs
the first part of an OAuth2 flow, including user authentication and client
authorization.") function. This authenticates the user with the service, if
necessary, and asks the user to authorize the extension to access data, if
necessary. The function completes with an access token or authorization code,
depending on the provider.

The extension then completes the OAuth2 flow to get a validated access token,
and can then use this in HTTP requests to access the user's data according to
the authorization the user gave.

To use this API, you must have the "identity" [API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions).

## Setup

There's some setup you must do before publishing your extension.

### Getting the redirect URL

The [redirect URL](https://www.oauth.com/oauth2-servers/redirect-uris/)
represents the end point of [`identity.launchWebAuthFlow()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/identity/launchWebAuthFlow "Performs
the first part of an OAuth2 flow, including user authentication and client
authorization."), in which the access token or authorization code is delivered
to the extension.

You can get a redirect URL by calling [`identity.getRedirectURL()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/identity/getRedirectURL "Generates a
URL that you can use as a redirect URL."). This function derives a redirect
URL from the add-on's ID, so if you want to use it, you should probably set
your add-on's ID explicitly using the `[applications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/applications)` key (otherwise, each time you
[temporarily install the add-on](/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox), you'll get a different
redirect URL).

You don't have to use the redirect URL returned by
`identity.getRedirectURL()`: you can supply your own, and it can be anything
that the service will redirect to. However, it should use a domain that you
control.

You'll use the redirect URL in two places:

  * supply it when registering your extension as an OAuth2 client
  * pass it into `identity.launchWebAuthFlow()`, as a URL parameter added to that function's `url` argument.

### Registering your extension

Before you can use OAuth2 with a service provider, you must register the
extension with the provider as an OAuth2 client.

This will tend to be specific to the service provider, but in general it means
creating an entry for your extension on the provider's website. In this
process you will supply your redirect URL, and receive a client ID (and
sometimes also a secret). You'll need to pass both of these into
[`identity.launchWebAuthFlow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/identity/launchWebAuthFlow "Performs the first part of
an OAuth2 flow, including user authentication and client authorization.").

## Functions

[`identity.getRedirectURL()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/identity/getRedirectURL "Generates a URL that you can
use as a redirect URL.")

    Gets the redirect URL.
[`identity.launchWebAuthFlow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/identity/launchWebAuthFlow "Performs the first part of
an OAuth2 flow, including user authentication and client authorization.")

    Launches WAF.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`getRedirectURL`|  Yes|  No| 53| 53|  No  
`launchWebAuthFlow`|  Yes|  No| 53| 53|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`getRedirectURL`|  Full support Yes|  No support No|  Full support 53|  No
support No|  Full support 53  
`launchWebAuthFlow`|  Full support Yes|  No support No|  Full support 53|
Full support Yes|  Full support 53  
  
## Example extensions

  * [google-userinfo](https://github.com/mdn/webextensions-examples/tree/master/google-userinfo)

**Acknowledgements**

This API is based on Chromium's
[`chrome.identity`](https://developer.chrome.com/extensions/identity) API.

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

