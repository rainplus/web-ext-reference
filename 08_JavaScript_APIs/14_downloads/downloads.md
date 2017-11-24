[\n

\n

Enables extensions to interact with the browser's download manager. You can
use this API module to download files, cancel, pause, resume downloads, and
show downloaded files in the file manager.

\n

To use this API you need to have the "downloads" [API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions) specified in your
[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) file.

\n

## Types

\n

\n[`downloads.FilenameConflictAction`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/FilenameConflictAction "The
FilenameConflictAction type of the downloads API specifies what to do if the
name of a downloaded file conflicts with an existing file.")

\n    Defines options for what to do if the name of a downloaded file
conflicts with an existing file.

\n[`downloads.InterruptReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/InterruptReason "The InteruptReason type of
the downloads API defines a set of possible reasons why a download was
interrupted.")

\n    Defines a set of possible reasons why a download was interrupted.

\n[`downloads.DangerType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DangerType "The DangerType type of the
downloads API defines a set of possible reasons that a downloadable file might
be considered dangerous.")

\n    Defines a set of common warnings of possible dangers associated with
downloadable files.

\n[`downloads.State`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/State "The State type of the downloads API
defines different states that a current download can be in.")

\n    Defines different states that a current download can be in.

\n[`downloads.DownloadItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadItem "The documentation about this has
not yet been written; please consider contributing!")

\n    Represents a downloaded file.

\n[`downloads.StringDelta`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/StringDelta "The StringDelta type of the
downloads API represents the difference between two strings.")

\n    Represents the difference between two strings.

\n[`downloads.DoubleDelta`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DoubleDelta "The DoubleDelta type of the
downloads API represents the difference between two doubles.")

\n    Represents the difference between two doubles.

\n[`downloads.BooleanDelta`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/BooleanDelta "The BooleanDelta type of the
downloads API represents the difference between two booleans.")

\n    Represents the difference between two booleans.

\n[`downloads.DownloadTime`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadTime "The DownloadTime type of the
downloads API represents the time a download took to complete.")

\n    Represents the time a download took to complete.

\n[`downloads.DownloadQuery`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadQuery "The DownloadQuery type of the
downloads API defines a set of parameters that can be used to search the
downloads manager for a specific set of downloads.")

\n    Defines a set of parameters that can be used to search the downloads
manager for a specific set of downloads.

\n\n

## Functions

\n

\n[`downloads.download()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/download "The download\(\) function of the
downloads API downloads a file, given its URL and other optional
preferences.")

\n    Downloads a file, given its URL and other optional preferences.

\n[`downloads.search()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/search "The search\(\) function of the
downloads API queries the\\xa0DownloadItems available in the browser's
downloads manager, and returns those that match the specified search
criteria.")

\n    Queries the\xa0[`DownloadItems`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadItem "The documentation about this has
not yet been written; please consider contributing!") available in the
browser's downloads manager, and returns those that match the specified search
criteria.

\n[`downloads.pause()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/pause "The pause\(\) function of the downloads
API pauses a download.")

\n    Pauses a download.

\n[`downloads.resume()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/resume "The resume\(\) function of the
downloads API resumes a paused download. If the request was successful, the
download will be unpaused and progress will resume. The resume\(\) call will
fail if the download is not active: for example, because it has finished
downloading.")

\n    Resumes a paused download.

\n[`downloads.cancel()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/cancel "The cancel\(\) function of the
downloads API cancels a download. The call will fail if the download is not
active: for example, because it has completed downloading.")

\n    Cancels a download.

\n[`downloads.getFileIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/getFileIcon "The getFileIcon\(\) function of
the downloads API retrieves an icon for the specified download.")

\n    Retrieves an icon for the specified download.

\n[`downloads.open()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/open "The open\(\) function of the downloads
API opens the downloaded file with its associated application. A
downloads.onChanged event will fire when the item is opened for the first
time.")

\n    Opens the downloaded file with its associated application.

\n[`downloads.show()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/show "The show\(\) function of the downloads
API shows the downloaded file in its containing folder in the underlying
platform's file manager.")

\n    Opens the platform's file manager application to show the downloaded
file in its containing folder.

\n[`downloads.showDefaultFolder()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/showDefaultFolder "The showDefaultFolder\(\)
function of the downloads API opens the default downloads folder in the
platform's file manager.")

\n    Opens the platform's file manager application to show the default
downloads folder.

\n[`downloads.erase()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/erase "The erase\(\) function of the downloads
API erases matching DownloadItems from the browser's download history, without
deleting the downloaded files from disk.")

\n    Erases matching [`DownloadItems`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadItem "The documentation about this has
not yet been written; please consider contributing!") from the browser's
download history, without deleting the downloaded files from disk.

\n[`downloads.removeFile()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/removeFile "The removeFile\(\) function of the
downloads API removes a downloaded file from disk.")

\n    Removes a downloaded file from disk, but not from the browser's download
history.

\n[`downloads.acceptDanger()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/acceptDanger "The acceptDanger\(\) function of
the downloads API prompts the user to either accept or cancel a potentially
dangerous download.")

\n    Prompts the user to accept or cancel a dangerous download.

\n[`downloads.drag()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/drag "The drag\(\) function of the downloads
API initiates dragging the downloaded file to another application.")

\n    Initiates dragging the downloaded file to another application.

\n[`downloads.setShelfEnabled()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/setShelfEnabled "The setShelfEnabled\(\)
function of the downloads API enables or disables the gray shelf at the bottom
of every window associated with the current browser profile. The shelf will be
disabled as long as at least one extension has disabled it.")

\n    Enables or disables the gray shelf at the bottom of every window
associated with the current browser profile. The shelf will be disabled as
long as at least one extension has disabled it.

\n\n

## Events

\n

\n[`downloads.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/onCreated "The onCreated\(\) event of the
downloads API fires when a download begins, i.e. when downloads.download\(\)
is sucessfully invoked.")

\n    Fires with the [`DownloadItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadItem "The DownloadItem type of the
downloads API represents a downloaded file.") object when a download begins.

\n[`downloads.onErased`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/onErased "The onErased\(\) event of the
downloads API fires when a download is erased from the browser history.")

\n    Fires with the `downloadId` when a download is erased from history.

\n[`downloads.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/onChanged "The onChanged\(\) event of the
downloads API is fired when any of a downloads.DownloadItem's properties
changes \(except for bytesReceived\).")

\n    When any of a [`DownloadItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadItem "The DownloadItem type of the
downloads API represents a downloaded file.")'s properties except
`bytesReceived` changes, this event fires with the `downloadId` and an object
containing the properties that changed.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`BooleanDelta`| \n Yes| \n No| 47| 48| \n Yes  
`DangerType`| \n Yes| \n No| 47| 48| \n Yes  
`DoubleDelta`| \n Yes| \n No| 47| 48| \n Yes  
`DownloadQuery`| \n Yes| \n No| 47| 48| \n Yes  
`DownloadTime`| \n Yes| \n No| 47| 48| \n Yes  
`FilenameConflictAction`| \n Yes| \n No| 47 *| 48 *| \n Yes  
`InterruptReason`| \n Yes| \n No| 47| 48| \n Yes  
`State`| \n Yes| \n No| 47| 48| \n Yes  
`StringDelta`| \n Yes| \n No| 47| 48| \n Yes  
`acceptDanger`| \n Yes| \n No| \n No| \n No| \n Yes  
`cancel`| \n Yes| \n No| 48| 48| \n Yes  
`download`| \n Yes *| \n No| 47 *| 48 *| \n Yes *  
`drag`| \n Yes| \n No| \n No| \n No| \n Yes  
`erase`| \n Yes| \n No| 48| 48| \n Yes  
`getFileIcon`| \n Yes| \n No| 48| \n No| \n Yes  
`onChanged`| \n Yes| \n No| 47| 48| \n Yes  
`onCreated`| \n Yes| \n No| 48| 48| \n Yes  
`onErased`| \n Yes| \n No| 48| 48| \n Yes  
`open`| \n Yes| \n No| 48| 48| \n Yes  
`pause`| \n Yes| \n No| 48| 48| \n Yes  
`removeFile`| \n Yes| \n No| 48| 48| \n Yes  
`resume`| \n Yes| \n No| 48| 48| \n Yes  
`search`| \n Yes| \n No| 47| 48| \n Yes  
`setShelfEnabled`| \n Yes| \n No| \n No| \n No| \n Yes  
`show`| \n Yes| \n No| 48| 48| \n Yes  
`showDefaultFolder`| \n Yes| \n No| 48| 48| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`BooleanDelta`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 47| \nFull support\n\n Yes| \nFull support\n\n 48  
`DangerType`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nFull support\n\n 48  
`DoubleDelta`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nFull support\n\n 48  
`DownloadQuery`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 47| \nFull support\n\n Yes| \nFull support\n\n 48  
`DownloadTime`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 47| \nFull support\n\n Yes| \nFull support\n\n 48  
`FilenameConflictAction`| \nFull support\n\n Yes| \nNo support\n\n No|
\nPartial support\n47| \nFull support\n\n Yes| \nPartial support\n48  
`InterruptReason`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 47| \nFull support\n\n Yes| \nFull support\n\n 48  
`State`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 47|
\nFull support\n\n Yes| \nFull support\n\n 48  
`StringDelta`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nFull support\n\n 48  
`acceptDanger`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`cancel`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 48|
\nFull support\n\n Yes| \nFull support\n\n 48  
`download`| \nPartial support\nPartial| \nNo support\n\n No| \nPartial
support\n47| \nPartial support\nPartial| \nPartial support\n48  
`drag`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`erase`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 48|
\nFull support\n\n Yes| \nFull support\n\n 48  
`getFileIcon`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
48| \nFull support\n\n Yes| \nNo support\n\n No  
`onChanged`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nFull support\n\n 48  
`onCreated`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
48| \nFull support\n\n Yes| \nFull support\n\n 48  
`onErased`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
48| \nFull support\n\n Yes| \nFull support\n\n 48  
`open`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 48|
\nFull support\n\n Yes| \nFull support\n\n 48  
`pause`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 48|
\nFull support\n\n Yes| \nFull support\n\n 48  
`removeFile`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
48| \nFull support\n\n Yes| \nFull support\n\n 48  
`resume`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 48|
\nFull support\n\n Yes| \nFull support\n\n 48  
`search`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 47|
\nFull support\n\n Yes| \nFull support\n\n 48  
`setShelfEnabled`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`show`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 48|
\nFull support\n\n Yes| \nFull support\n\n 48  
`showDefaultFolder`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
  
\n

## Example extensions

  * [latest-download](https://github.com/mdn/webextensions-examples/tree/master/latest-download)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.downloads`](https://developer.chrome.com/extensions/downloads) API.

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
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

