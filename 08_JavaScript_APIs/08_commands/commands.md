Listen for the user executing commands that you have registered using the
[`commands` manifest.json key](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/commands).

## Types

[`commands.Command`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/commands/Command "Information about a command. This
contains the information specified for the command in the commands
manifest.json key.")

    Object representing a command. This contains the information specified for the command in the [`commands` manifest.json key](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/commands).

## Functions

[`commands.getAll`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/commands/getAll "Gets all commands for the extention
that you have registered using the commands manifest.json key.")

    

Gets all registered commands for this extension.

## Events

[`commands.onCommand`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/commands/onCommand "Events have three functions:")

    

Fired when a command is executed using its associated keyboard shortcut.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Command`|  Yes|  No| 48|  No|  Yes  
`getAll`|  Yes|  No| 48|  No|  Yes  
`onCommand`|  Yes|  No| 48|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Command`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  No support No  
`getAll`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  No support No  
`onCommand`|  Full support Yes|  No support No|  Full support 48|  Full
support Yes|  No support No  
  
## Example extensions

  * [commands](https://github.com/mdn/webextensions-examples/tree/master/commands)

**Acknowledgements**

This API is based on Chromium's
[`chrome.commands`](https://developer.chrome.com/extensions/commands) API.

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

