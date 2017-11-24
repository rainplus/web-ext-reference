[\n

\n

Listen for the user executing commands that you have registered using the
[`commands` manifest.json key](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/commands).

\n

## Types

\n

\n[`commands.Command`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/commands/Command "Information about a command. This
contains the information specified for the command in the commands
manifest.json key.")

\n    Object representing a command. This contains the information specified
for the command in the [`commands` manifest.json
key](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/manifest.json/commands).

\n\n

## Functions

\n

\n[`commands.getAll`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/commands/getAll "Gets all commands for the extention
that you have registered using the commands manifest.json key.")

\n    \n

Gets all registered commands for this extension.

\n

\n\n

## Events

\n

\n[`commands.onCommand`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/commands/onCommand "Events have three functions:")

\n    \n

Fired when a command is executed using its associated keyboard shortcut.

\n

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`Command`| \n Yes| \n No| 48| \n No| \n Yes  
`getAll`| \n Yes| \n No| 48| \n No| \n Yes  
`onCommand`| \n Yes| \n No| 48| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`Command`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
48| \nFull support\n\n Yes| \nNo support\n\n No  
`getAll`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 48|
\nFull support\n\n Yes| \nNo support\n\n No  
`onCommand`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
48| \nFull support\n\n Yes| \nNo support\n\n No  
  
## Example extensions

  * [commands](https://github.com/mdn/webextensions-examples/tree/master/commands)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.commands`](https://developer.chrome.com/extensions/commands) API.

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

