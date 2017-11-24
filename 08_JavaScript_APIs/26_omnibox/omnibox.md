Enables extensions to implement customised behavior when the user types into
the browser's address bar.

When the user focuses the browser's address bar and starts typing, the browser
displays a drop-down list containing suggested pages, based on what they
typed. This gives the user a quick way to access, for example, pages from
their history or bookmarks.

The omnibox API provides the extension a way to customise the suggestions
displayed in the drop-down, when the user enters a keyword defined by the
extension. It works as follows:

  1. First, the extension must include an "[omnibox](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox)" key in its [manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file, which defines a keyword.
  2. When the user focuses the address bar and types the keyword, followed by a space, the extension will get an [`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputStarted "Fired when the user starts interacting with your extension by entering its keyword in the address bar and then pressing the space key.") event.
  3. Optionally, the extension can call [`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion "Set the default suggestion to appear in the address bar drop-down list when the user starts interacting with your extension.") to define the first suggestion that will be displayed in the address bar drop-down.
  4. As the user continues to type characters after this, the extension will get [`omnibox.onInputChanged`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputChanged "Fired whenever the user changes their input, after they have started interacting with your extension by entering its keyword in the address bar and then pressing the space key.") events. The event listener will be passed the current value the user has typed, and will be able to populate the address bar drop-down with suggestions. If the extension set a default suggestion using [`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion "Set the default suggestion to appear in the address bar drop-down list when the user starts interacting with your extension."), then this will appear first in the drop-down.
  5. If the user accepts a suggestion, the extension will get an [`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected one of the suggestions your extension has added to the address bar's drop-down list.") event. The event listener will be passed the accepted suggestion.
  6. If the user dismisses the drop-down, the extension will get an [`omnibox.onInputCancelled`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputCancelled "Fired when the user has cancelled their interaction with your extension \(for example, by clicking outside the address bar\).") event.

## Types

[`omnibox.OnInputEnteredDisposition`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/OnInputEnteredDisposition "The
omnibox.OnInputEnteredDisposition type describes how the extension should
handle a user selection from the suggestions in the address bar's drop-down
list.")

    Describes the recommended method to handle the selected suggestion: open in the current tab, open in a new foreground tab, or open in a new background tab.
[`omnibox.SuggestResult`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/SuggestResult "The documentation about this has
not yet been written; please consider contributing!")

    Object representing a suggestion to add to the address bar drop-down.

## Functions

[`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/setDefaultSuggestion "Set the default suggestion
to appear in the address bar drop-down list when the user starts interacting
with your extension.")

    Defines the first suggestion that appears in the drop-down when the user enters the keyword for your extension, followed by a space.

## Events

[`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputStarted "Fired when the user starts
interacting with your extension by entering its keyword in the address bar and
then pressing the space key.")

    Fired when a the user focuses the address bar and types your extension's omnibox keyword, followed by a space.
[`omnibox.onInputChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputChanged "Fired whenever the user changes
their input, after they have started interacting with your extension by
entering its keyword in the address bar and then pressing the space key.")

    Fired whenever the user's input changes, after they have focused the address bar and typed your extension's omnibox keyword, followed by a space.
[`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected
one of the suggestions your extension has added to the address bar's drop-down
list.")

    Fired when the user accepts one of your extension's suggestions.
[`omnibox.onInputCancelled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputCancelled "Fired when the user has
cancelled their interaction with your extension \(for example, by clicking
outside the address bar\).")

    Fired when the user dismisses the address bar drop-down, after they have focused the address bar and typed your extension's omnibox keyword.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`OnInputEnteredDisposition`|  Yes|  No| 52|  No|  Yes  
`SuggestResult`|  Yes|  No| 52 *|  No|  Yes  
`onInputCancelled`|  Yes|  No| 52|  No|  Yes  
`onInputChanged`|  Yes|  No| 52|  No|  Yes  
`onInputEntered`|  Yes|  No| 52|  No|  Yes  
`onInputStarted`|  Yes|  No| 52|  No|  Yes  
`setDefaultSuggestion`|  Yes|  No| 52 *|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`OnInputEnteredDisposition`|  Full support Yes|  No support No|  Full support
52|  Full support Yes|  No support No  
`SuggestResult`|  Full support Yes|  No support No|  Full support 52

Notes __

Full support 52

Notes __

     Notes __'description' is interpreted as plain text, and XML markup is not recognised.
|  Full support Yes|  No support No  
`onInputCancelled`|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`onInputChanged`|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`onInputEntered`|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`onInputStarted`|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`setDefaultSuggestion`|  Full support Yes|  No support No|  Full support 52

Notes __

Full support 52

Notes __

     Notes __'description' is interpreted as plain text, and XML markup is not recognised.
|  Full support Yes|  No support No  
  
## Example extensions

  * [firefox-code-search](https://github.com/mdn/webextensions-examples/tree/master/firefox-code-search)

**Acknowledgements**

This API is based on Chromium's
[`chrome.omnibox`](https://developer.chrome.com/extensions/omnibox) API.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

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
  *[Notes __]: See implementation notes
  *[
Full support

]: Full support

  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

