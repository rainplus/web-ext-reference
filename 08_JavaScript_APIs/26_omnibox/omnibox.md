[\n

\n

Enables extensions to implement customised behavior when the user types into
the browser's address bar.

\n

When the user focuses the browser's address bar and starts typing, the browser
displays a drop-down list containing suggested pages, based on what they
typed. This gives the user a quick way to access, for example, pages from
their history or bookmarks.

\n

The omnibox API provides the extension a way to customise the suggestions
displayed in the drop-down, when the user enters a keyword defined by the
extension. It works as follows:

\n

\n

  1. First, the extension must include an "[omnibox](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox)" key in its [manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file, which defines a keyword.
\n

  2. When the user focuses the address bar and types the keyword, followed by a space, the extension will get an [`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputStarted "Fired when the user starts interacting with your extension by entering its keyword in the address bar and then pressing the space key.") event.
\n

  3. Optionally, the extension can call [`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion "Set the default suggestion to appear in the address bar drop-down list when the user starts interacting with your extension.") to define the first suggestion that will be displayed in the address bar drop-down.
\n

  4. As the user continues to type characters after this, the extension will get [`omnibox.onInputChanged`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputChanged "Fired whenever the user changes their input, after they have started interacting with your extension by entering its keyword in the address bar and then pressing the space key.") events. The event listener will be passed the current value the user has typed, and will be able to populate the address bar drop-down with suggestions. If the extension set a default suggestion using [`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion "Set the default suggestion to appear in the address bar drop-down list when the user starts interacting with your extension."), then this will appear first in the drop-down.
\n

  5. If the user accepts a suggestion, the extension will get an [`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected one of the suggestions your extension has added to the address bar's drop-down list.") event. The event listener will be passed the accepted suggestion.
\n

  6. If the user dismisses the drop-down, the extension will get an [`omnibox.onInputCancelled`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputCancelled "Fired when the user has cancelled their interaction with your extension \(for example, by clicking outside the address bar\).") event.
\n

\n

## Types

\n

\n[`omnibox.OnInputEnteredDisposition`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/OnInputEnteredDisposition "The
omnibox.OnInputEnteredDisposition type describes how the extension should
handle a user selection from the suggestions in the address bar's drop-down
list.")

\n    Describes the recommended method to handle the selected suggestion: open
in the current tab, open in a new foreground tab, or open in a new background
tab.

\n[`omnibox.SuggestResult`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/SuggestResult "The documentation about this has
not yet been written; please consider contributing!")

\n    Object representing a suggestion to add to the address bar drop-down.

\n\n

## Functions

\n

\n[`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/setDefaultSuggestion "Set the default suggestion
to appear in the address bar drop-down list when the user starts interacting
with your extension.")

\n    Defines the first suggestion that appears in the drop-down when the user
enters the keyword for your extension, followed by a space.

\n\n

## Events

\n

\n[`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputStarted "Fired when the user starts
interacting with your extension by entering its keyword in the address bar and
then pressing the space key.")

\n    Fired when a the user focuses the address bar and types your extension's
omnibox keyword, followed by a space.

\n[`omnibox.onInputChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputChanged "Fired whenever the user changes
their input, after they have started interacting with your extension by
entering its keyword in the address bar and then pressing the space key.")

\n    Fired whenever the user's input changes, after they have focused the
address bar and typed your extension's omnibox keyword, followed by a space.

\n[`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected
one of the suggestions your extension has added to the address bar's drop-down
list.")

\n    Fired when the user accepts one of your extension's suggestions.

\n[`omnibox.onInputCancelled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputCancelled "Fired when the user has
cancelled their interaction with your extension \(for example, by clicking
outside the address bar\).")

\n    Fired when the user dismisses the address bar drop-down, after they have
focused the address bar and typed your extension's omnibox keyword.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`OnInputEnteredDisposition`| \n Yes| \n No| 52| \n No| \n Yes  
`SuggestResult`| \n Yes| \n No| 52 *| \n No| \n Yes  
`onInputCancelled`| \n Yes| \n No| 52| \n No| \n Yes  
`onInputChanged`| \n Yes| \n No| 52| \n No| \n Yes  
`onInputEntered`| \n Yes| \n No| 52| \n No| \n Yes  
`onInputStarted`| \n Yes| \n No| 52| \n No| \n Yes  
`setDefaultSuggestion`| \n Yes| \n No| 52 *| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`OnInputEnteredDisposition`|  \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`SuggestResult`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52

Notes __

\nFull support\n\n 52

Notes __

     Notes __'description' is interpreted as plain text, and XML markup is not recognised.
|  \nFull support\n\n Yes| \nNo support\n\n No  
`onInputCancelled`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`onInputChanged`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`onInputEntered`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`onInputStarted`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52| \nFull support\n\n Yes| \nNo support\n\n No  
`setDefaultSuggestion`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 52

Notes __

\nFull support\n\n 52

Notes __

     Notes __'description' is interpreted as plain text, and XML markup is not recognised.
|  \nFull support\n\n Yes| \nNo support\n\n No  
  
\n

## Example extensions

  * [firefox-code-search](https://github.com/mdn/webextensions-examples/tree/master/firefox-code-search)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.omnibox`](https://developer.chrome.com/extensions/omnibox) API.

\n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

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
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

