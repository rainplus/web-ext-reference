Enables extensions to interact with the browser's download manager. You can
use this API module to download files, cancel, pause, resume downloads, and
show downloaded files in the file manager.

To use this API you need to have the "downloads" [API permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#API_permissions) specified in your
[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) file.

## Types

[`downloads.FilenameConflictAction`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/FilenameConflictAction "The
FilenameConflictAction type of the downloads API specifies what to do if the
name of a downloaded file conflicts with an existing file.")

    Defines options for what to do if the name of a downloaded file conflicts with an existing file.
[`downloads.InterruptReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/InterruptReason "The InteruptReason type of
the downloads API defines a set of possible reasons why a download was
interrupted.")

    Defines a set of possible reasons why a download was interrupted.
[`downloads.DangerType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DangerType "The DangerType type of the
downloads API defines a set of possible reasons that a downloadable file might
be considered dangerous.")

    Defines a set of common warnings of possible dangers associated with downloadable files.
[`downloads.State`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/State "The State type of the downloads API
defines different states that a current download can be in.")

    Defines different states that a current download can be in.
[`downloads.DownloadItem`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadItem "The documentation about this has
not yet been written; please consider contributing!")

    Represents a downloaded file.
[`downloads.StringDelta`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/StringDelta "The StringDelta type of the
downloads API represents the difference between two strings.")

    Represents the difference between two strings.
[`downloads.DoubleDelta`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DoubleDelta "The DoubleDelta type of the
downloads API represents the difference between two doubles.")

    Represents the difference between two doubles.
[`downloads.BooleanDelta`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/BooleanDelta "The BooleanDelta type of the
downloads API represents the difference between two booleans.")

    Represents the difference between two booleans.
[`downloads.DownloadTime`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadTime "The DownloadTime type of the
downloads API represents the time a download took to complete.")

    Represents the time a download took to complete.
[`downloads.DownloadQuery`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/DownloadQuery "The DownloadQuery type of the
downloads API defines a set of parameters that can be used to search the
downloads manager for a specific set of downloads.")

    Defines a set of parameters that can be used to search the downloads manager for a specific set of downloads.

## Functions

[`downloads.download()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/download "The download\(\) function of the
downloads API downloads a file, given its URL and other optional
preferences.")

    Downloads a file, given its URL and other optional preferences.
[`downloads.search()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/search "The search\(\) function of the
downloads API queries the DownloadItems available in the browser's downloads
manager, and returns those that match the specified search criteria.")

    Queries the [`DownloadItems`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads/DownloadItem "The documentation about this has not yet been written; please consider contributing!") available in the browser's downloads manager, and returns those that match the specified search criteria.
[`downloads.pause()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/pause "The pause\(\) function of the downloads
API pauses a download.")

    Pauses a download.
[`downloads.resume()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/resume "The resume\(\) function of the
downloads API resumes a paused download. If the request was successful, the
download will be unpaused and progress will resume. The resume\(\) call will
fail if the download is not active: for example, because it has finished
downloading.")

    Resumes a paused download.
[`downloads.cancel()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/cancel "The cancel\(\) function of the
downloads API cancels a download. The call will fail if the download is not
active: for example, because it has completed downloading.")

    Cancels a download.
[`downloads.getFileIcon()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/getFileIcon "The getFileIcon\(\) function of
the downloads API retrieves an icon for the specified download.")

    Retrieves an icon for the specified download.
[`downloads.open()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/open "The open\(\) function of the downloads
API opens the downloaded file with its associated application. A
downloads.onChanged event will fire when the item is opened for the first
time.")

    Opens the downloaded file with its associated application.
[`downloads.show()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/show "The show\(\) function of the downloads
API shows the downloaded file in its containing folder in the underlying
platform's file manager.")

    Opens the platform's file manager application to show the downloaded file in its containing folder.
[`downloads.showDefaultFolder()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/showDefaultFolder "The showDefaultFolder\(\)
function of the downloads API opens the default downloads folder in the
platform's file manager.")

    Opens the platform's file manager application to show the default downloads folder.
[`downloads.erase()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/erase "The erase\(\) function of the downloads
API erases matching DownloadItems from the browser's download history, without
deleting the downloaded files from disk.")

    Erases matching [`DownloadItems`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads/DownloadItem "The documentation about this has not yet been written; please consider contributing!") from the browser's download history, without deleting the downloaded files from disk.
[`downloads.removeFile()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/removeFile "The removeFile\(\) function of the
downloads API removes a downloaded file from disk.")

    Removes a downloaded file from disk, but not from the browser's download history.
[`downloads.acceptDanger()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/acceptDanger "The acceptDanger\(\) function of
the downloads API prompts the user to either accept or cancel a potentially
dangerous download.")

    Prompts the user to accept or cancel a dangerous download.
[`downloads.drag()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/drag "The drag\(\) function of the downloads
API initiates dragging the downloaded file to another application.")

    Initiates dragging the downloaded file to another application.
[`downloads.setShelfEnabled()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/setShelfEnabled "The setShelfEnabled\(\)
function of the downloads API enables or disables the gray shelf at the bottom
of every window associated with the current browser profile. The shelf will be
disabled as long as at least one extension has disabled it.")

    Enables or disables the gray shelf at the bottom of every window associated with the current browser profile. The shelf will be disabled as long as at least one extension has disabled it.

## Events

[`downloads.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/onCreated "The onCreated\(\) event of the
downloads API fires when a download begins, i.e. when downloads.download\(\)
is sucessfully invoked.")

    Fires with the [`DownloadItem`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads/DownloadItem "The DownloadItem type of the downloads API represents a downloaded file.") object when a download begins.
[`downloads.onErased`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/onErased "The onErased\(\) event of the
downloads API fires when a download is erased from the browser history.")

    Fires with the `downloadId` when a download is erased from history.
[`downloads.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/downloads/onChanged "The onChanged\(\) event of the
downloads API is fired when any of a downloads.DownloadItem's properties
changes \(except for bytesReceived\).")

    When any of a [`DownloadItem`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads/DownloadItem "The DownloadItem type of the downloads API represents a downloaded file.")'s properties except `bytesReceived` changes, this event fires with the `downloadId` and an object containing the properties that changed.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`BooleanDelta`|  Yes|  No| 47| 48|  Yes  
`DangerType`|  Yes|  No| 47| 48|  Yes  
`DoubleDelta`|  Yes|  No| 47| 48|  Yes  
`DownloadQuery`|  Yes|  No| 47| 48|  Yes  
`DownloadTime`|  Yes|  No| 47| 48|  Yes  
`FilenameConflictAction`|  Yes|  No| 47 *| 48 *|  Yes  
`InterruptReason`|  Yes|  No| 47| 48|  Yes  
`State`|  Yes|  No| 47| 48|  Yes  
`StringDelta`|  Yes|  No| 47| 48|  Yes  
`acceptDanger`|  Yes|  No|  No|  No|  Yes  
`cancel`|  Yes|  No| 48| 48|  Yes  
`download`|  Yes *|  No| 47 *| 48 *|  Yes *  
`drag`|  Yes|  No|  No|  No|  Yes  
`erase`|  Yes|  No| 48| 48|  Yes  
`getFileIcon`|  Yes|  No| 48|  No|  Yes  
`onChanged`|  Yes|  No| 47| 48|  Yes  
`onCreated`|  Yes|  No| 48| 48|  Yes  
`onErased`|  Yes|  No| 48| 48|  Yes  
`open`|  Yes|  No| 48| 48|  Yes  
`pause`|  Yes|  No| 48| 48|  Yes  
`removeFile`|  Yes|  No| 48| 48|  Yes  
`resume`|  Yes|  No| 48| 48|  Yes  
`search`|  Yes|  No| 47| 48|  Yes  
`setShelfEnabled`|  Yes|  No|  No|  No|  Yes  
`show`|  Yes|  No| 48| 48|  Yes  
`showDefaultFolder`|  Yes|  No| 48| 48|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`BooleanDelta`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`DangerType`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`DoubleDelta`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`DownloadQuery`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`DownloadTime`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`FilenameConflictAction`|  Full support Yes|  No support No|  Partial support
47|  Full support Yes|  Partial support 48  
`InterruptReason`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`State`|  Full support Yes|  No support No|  Full support 47|  Full support
Yes|  Full support 48  
`StringDelta`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`acceptDanger`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`cancel`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  Full support 48  
`download`|  Partial support Partial|  No support No|  Partial support 47|
Partial support Partial|  Partial support 48  
`drag`|  Full support Yes|  No support No|  No support No|  Full support Yes|
No support No  
`erase`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  Full support 48  
`getFileIcon`|  Full support Yes|  No support No|  Full support 48|  Full
support Yes|  No support No  
`onChanged`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  Full support 48  
`onCreated`|  Full support Yes|  No support No|  Full support 48|  Full
support Yes|  Full support 48  
`onErased`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  Full support 48  
`open`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  Full support 48  
`pause`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  Full support 48  
`removeFile`|  Full support Yes|  No support No|  Full support 48|  Full
support Yes|  Full support 48  
`resume`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  Full support 48  
`search`|  Full support Yes|  No support No|  Full support 47|  Full support
Yes|  Full support 48  
`setShelfEnabled`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`show`|  Full support Yes|  No support No|  Full support 48|  Full support
Yes|  Full support 48  
`showDefaultFolder`|  Full support Yes|  No support No|  Full support 48|
Full support Yes|  Full support 48  
  
## Example extensions

  * [latest-download](https://github.com/mdn/webextensions-examples/tree/master/latest-download)

**Acknowledgements**

This API is based on Chromium's
[`chrome.downloads`](https://developer.chrome.com/extensions/downloads) API.

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
  *[
Partial support

]: Partial support

  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

