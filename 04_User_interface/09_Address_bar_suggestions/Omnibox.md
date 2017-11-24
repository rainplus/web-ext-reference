[\n

\n

Using the [`omnibox`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox
"Enables extensions to implement customised behavior when the user types into
the browser's address bar.") API, extensions can customize the suggestions
offered in the browser address bar's drop-down when the user enters a keyword.

\n

![Example showing the result of the firefox_code_search WebExtension's
customization of the address bar
suggestions.](https://mdn.mozillademos.org/files/15075/omnibox_example_full.png)

\n

This enables your extension to, for example, search a library of free ebooks
or, as in the example above, a repository of code examples.

\n

## Specifying the omnibox customization

\n

You tell your extension that it is going to customize the address bar
suggestions by including the [omnibox](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox) key and
definition of the trigger keyword in its
[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) file:

\n

    
    
      "omnibox": { "keyword" : "cs" }

\n

In the extension's background JavaScript file,
using\xa0[`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/setDefaultSuggestion "The documentation about
this has not yet been written; please consider contributing!"), you can
optionally define the first suggestion to be displayed in the address bar
drop-down. Use this to provide a hint on how to use the feature:

\n

    
    
    browser.omnibox.setDefaultSuggestion({\n  description: `Search the firefox codebase\n    (e.g. "hello world" | "path:omnibox.js onInputChanged")`\n});

\n\n

You can then add the code to provide the customized content by listening for
[`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputStarted "The documentation about this has
not yet been written; please consider contributing!"), which is dispatched
when the user has typed the keyword and a space, and [`omnibox.onInputChanged
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputChanged "Fired
whenever the user changes their input, after they have started interacting
with your extension by entering its keyword in the address bar and then
pressing the space key."), which is dispatched whenever the user updates the
address bar entry. You can then populate the suggestions, in this case
building a search of https://searchfox.org/mozilla-central using the term
entered by the user:

\n

    
    
    browser.omnibox.onInputChanged.addListener((text, addSuggestions) => {\n  let headers = new Headers({"Accept": "application/json"});\n  let init = {method: 'GET', headers};\n  let url = buildSearchURL(text);\n  let request = new Request(url, init);\n\n  fetch(request)\n    .then(createSuggestionsFromResponse)\n    .then(addSuggestions);\n});

\n

If the extension set a default suggestion using [`omnibox.setDefaultSuggestion
()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/setDefaultSuggestion "The documentation about
this has not yet been written; please consider contributing!"), then this will
appear first in the drop-down.

\n

The extension can then listen for the user clicking one of the suggestions,
using [`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected
one of the suggestions your extension has added to the address bar's drop-down
list."). If the default suggestion is clicked the user's custom term is
returned, otherwise the suggestion's string is returned. Also, information on
the user's browser preferences for handling new links is passed. In the code
below the user's custom term is used to create a search otherwise, the
suggested URL is opened:

\n

    
    
    browser.omnibox.onInputEntered.addListener((text, disposition) => {\n  let url = text;\n  if (!text.startsWith(SOURCE_URL)) {\n    // Update the url if the user clicks on the default suggestion.\n    url = `${SEARCH_URL}?q=${text}`;\n  }\n  switch (disposition) {\n    case "currentTab":\n      browser.tabs.update({url});\n      break;\n    case "newForegroundTab":\n      browser.tabs.create({url});\n      break;\n    case "newBackgroundTab":\n      browser.tabs.create({url, active: false});\n      break;\n  }\n});

\n\xa0\n\n

## Examples

\n

The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use customizes
the omnibox

\n

\n

  * [firefox-code-search](https://github.com/mdn/webextensions-examples/tree/master/firefox-code-search) uses customizes the omnibox.
\n

\n\n, \n

You can then add the code to provide the customized content by listening for
[`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputStarted "The documentation about this has
not yet been written; please consider contributing!"), which is dispatched
when the user has typed the keyword and a space, and [`omnibox.onInputChanged
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputChanged "Fired
whenever the user changes their input, after they have started interacting
with your extension by entering its keyword in the address bar and then
pressing the space key."), which is dispatched whenever the user updates the
address bar entry. You can then populate the suggestions, in this case
building a search of https://searchfox.org/mozilla-central using the term
entered by the user:

\n

    
    
    browser.omnibox.onInputChanged.addListener((text, addSuggestions) => {\n  let headers = new Headers({"Accept": "application/json"});\n  let init = {method: 'GET', headers};\n  let url = buildSearchURL(text);\n  let request = new Request(url, init);\n\n  fetch(request)\n    .then(createSuggestionsFromResponse)\n    .then(addSuggestions);\n});

\n

If the extension set a default suggestion using [`omnibox.setDefaultSuggestion
()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/setDefaultSuggestion "The documentation about
this has not yet been written; please consider contributing!"), then this will
appear first in the drop-down.

\n

The extension can then listen for the user clicking one of the suggestions,
using [`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected
one of the suggestions your extension has added to the address bar's drop-down
list."). If the default suggestion is clicked the user's custom term is
returned, otherwise the suggestion's string is returned. Also, information on
the user's browser preferences for handling new links is passed. In the code
below the user's custom term is used to create a search otherwise, the
suggested URL is opened:

\n

    
    
    browser.omnibox.onInputEntered.addListener((text, disposition) => {\n  let url = text;\n  if (!text.startsWith(SOURCE_URL)) {\n    // Update the url if the user clicks on the default suggestion.\n    url = `${SEARCH_URL}?q=${text}`;\n  }\n  switch (disposition) {\n    case "currentTab":\n      browser.tabs.update({url});\n      break;\n    case "newForegroundTab":\n      browser.tabs.create({url});\n      break;\n    case "newBackgroundTab":\n      browser.tabs.create({url, active: false});\n      break;\n  }\n});

\n\xa0\n\n

## Examples

\n

The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use customizes
the omnibox

\n

\n

  * [firefox-code-search](https://github.com/mdn/webextensions-examples/tree/master/firefox-code-search) uses customizes the omnibox.
\n

\n]

