Using the [`omnibox`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox "Enables extensions to implement customised behavior when the user types into the browser's address bar.") API, extensions can customize the suggestions offered in the browser address bar's drop-down when the user enters a keyword.

![Example showing the result of the firefox_code_search WebExtension's customization of the address bar suggestions.](https://mdn.mozillademos.org/files/15075/omnibox_example_full.png)

This enables your extension to, for example, search a library of free ebooks or, as in the example above, a repository of code examples.

## Specifying the omnibox customization

You tell your extension that it is going to customize the address bar suggestions by including the [omnibox](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox) key and definition of the trigger keyword in its [manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file:

      "omnibox": { "keyword" : "cs" }

In the extension's background JavaScript file, using[`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion "The documentation about this has not yet been written; please consider contributing!"), you can optionally define the first suggestion to be displayed in the address bar drop-down. Use this to provide a hint on how to use the feature:

    browser.omnibox.setDefaultSuggestion({
      description: `Search the firefox codebase
        (e.g. "hello world" | "path:omnibox.js onInputChanged")`
    });

You can then add the code to provide the customized content by listening for [`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputStarted "The documentation about this has not yet been written; please consider contributing!"), which is dispatched when the user has typed the keyword and a space, and [`omnibox.onInputChanged`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputChanged "Fired whenever the user changes their input, after they have started interacting with your extension by entering its keyword in the address bar and then pressing the space key."), which is dispatched whenever the user updates the address bar entry. You can then populate the suggestions, in this case building a search of https://searchfox.org/mozilla-central using the term
entered by the user:

    browser.omnibox.onInputChanged.addListener((text, addSuggestions) => {
      let headers = new Headers({"Accept": "application/json"});
      let init = {method: 'GET', headers};
      let url = buildSearchURL(text);
      let request = new Request(url, init);
    
      fetch(request)
        .then(createSuggestionsFromResponse)
        .then(addSuggestions);
    });

If the extension set a default suggestion using [`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion "The documentation about this has not yet been written; please consider contributing!"), then this will appear first in the drop-down.

The extension can then listen for the user clicking one of the suggestions, using [`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected one of the suggestions your extension has added to the address bar's drop-down list."). If the default suggestion is clicked the user's custom term is returned, otherwise the suggestion's string is returned. Also, information on the user's browser preferences for handling new links is passed. In the code below the user's custom term is used to create a search otherwise, the suggested URL is opened:
    
    browser.omnibox.onInputEntered.addListener((text, disposition) => {
      let url = text;
      if (!text.startsWith(SOURCE_URL)) {
        // Update the url if the user clicks on the default suggestion.
        url = `${SEARCH_URL}?q=${text}`;
      }
      switch (disposition) {
        case "currentTab":
          browser.tabs.update({url});
          break;
        case "newForegroundTab":
          browser.tabs.create({url});
          break;
        case "newBackgroundTab":
          browser.tabs.create({url, active: false});
          break;
      }
    });



## Examples

The [webextensions-examples](https://github.com/mdn/webextensions-examples) repo on GitHub, contains several examples of extensions that use customizes the omnibox

  * [firefox-code-search](https://github.com/mdn/webextensions-examples/tree/master/firefox-code-search) uses customizes the omnibox.

