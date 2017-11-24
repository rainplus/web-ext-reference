[



Interact with the browser's tab system.



You can use this API to get a list of opened tabs, filtered by various
criteria, and to open, update, move, reload, and remove tabs. You can't
directly access the content hosted by tabs using this API, but you can insert
JavaScript and CSS into tabs using the [`tabs.executeScript()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript "Injects
JavaScript code into a page.") or [`tabs.insertCSS()`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.") APIs.



You can use most of this API without any special permission. However:





  * to access `Tab.url`, `Tab.title`, and `Tab.favIconUrl`, you need to have the "tabs" [permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions). In Firefox this also means you need "tabs" to [`query`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query "Gets all tabs that have the specified properties, or all tabs if no properties are specified.") by URL.


  * to use [`tabs.executeScript()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript "Injects JavaScript code into a page.") or [`tabs.insertCSS()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.") you must have the [host permission](/en-US/Add-ons/WebExtensions/manifest.json/permissions#Host_permissions) for the tab




Alternatively, you can get these permissions temporarily, only for the
currently active tab and only in response to an explicit user action, by
asking for the ["activeTab" permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#activeTab_permission).



Many tab operations use a Tab ID. Tab IDs are guaranteed to be unique to a
single tab only within a browser session. If the browser is restarted, then it
can and will reuse tab IDs. To associate information with a tab across browser
restarts, use [`sessions.setTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/setTabValue "Stores a key/value pair to
associate with a given tab. You can subsequently retrieve this value using
sessions.getTabValue.").



## Types



[`tabs.MutedInfoReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/MutedInfoReason "Specifies the reason a tab was
muted or unmuted.")

    Specifies the reason a tab was muted or unmuted.

[`tabs.MutedInfo`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/MutedInfo "This object contains a boolean
indicating whether the tab is muted, and the reason for the last state
change.")

    This object contains a boolean indicating whether the tab is muted, and
the reason for the last state change.

[`tabs.PageSettings`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/PageSettings "The type tabs.PageSettings is used to
control how a tab is rendered as a PDF by the tabs.saveAsPDF\(\) method.")

    

Used to control how a tab is rendered as a PDF by the
[`tabs.saveAsPDF()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/saveAsPDF "Saves the current page as a PDF. This
will open a dialog, supplied by the underlying operating system, asking the
user where they want to save the PDF.") method.



[`tabs.Tab`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/Tab "The
type tabs.Tab contains information about a tab. This provides access to
information about what content is in the tab, how large the content is, what
special states or restrictions are in effect, and so forth.")

    This type contains information about a tab.

[`tabs.TabStatus`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/TabStatus "Indicates whether the tab has finished
loading.")

    Indicates whether the tab has finished loading.

[`tabs.WindowType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/WindowType "The type of window that hosts this
tab.")

    The type of window that hosts this tab.

[`tabs.ZoomSettingsMode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsMode "Defines how zoom changes are
handled. Extensions can pass this value into tabs.setZoomSettings\(\) to
control how the browser handles attempts to change zoom settings for a tab.
Defaults to "automatic".")

    Defines whether zoom changes are handled by the browser, by the
extension, or are disabled.

[`tabs.ZoomSettingsScope`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsScope "Defines whether zoom changes
will persist for the page's origin, or only take effect in this tab. This
defaults to per-origin when tabs.zoomSettingsMode is "automatic", and is
always per-tab otherwise.")

    Defines whether zoom changes will persist for the page's origin, or only
take effect in this tab.

[`tabs.ZoomSettings`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettings "Defines zoom settings for a tab:
mode,\\xa0scope, and default zoom factor.")

    Defines zoom settings [`mode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsMode "Defines how zoom changes are
handled. Extensions can pass this value into tabs.setZoomSettings\(\) to
control how the browser handles attempts to change zoom settings for a tab.
Defaults to "automatic"."),\xa0[`scope`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsScope "Defines whether zoom changes
will persist for the page's origin, or only take effect in this tab. This
defaults to per-origin when tabs.zoomSettingsMode is "automatic", and is
always per-tab otherwise."), and default zoom factor.



## Properties



[`tabs.TAB_ID_NONE`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/TAB_ID_NONE "A special ID value given to tabs that
are not browser tabs \(for example, tabs in devtools windows\).")

    A special ID value given to tabs that are not browser tabs (for example,
tabs in devtools windows).



## Functions



[`tabs.captureVisibleTab()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/captureVisibleTab "Creates a data URI encoding an
image of the visible area of the currently active tab in the specified window.
You must have the <all_urls> permission to use this method.")

    Creates a data URI encoding an image of the visible area of the
currently active tab in the specified window.

[`tabs.connect()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/connect "Call this function to set up a connection
between the extension's background scripts \(or other privileged scripts, such
as popup scripts or options page scripts\) and any content scripts that belong
to this extension and are running in the specified tab. This function returns
a runtime.Port object.")

    Sets up a messaging connection between the extension's background
scripts (or other privileged scripts, such as popup scripts or options page
scripts) and any [content scripts](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts) running in the
specified tab.

[`tabs.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/create
"Creates a new tab.")

    Creates a new tab.

[`tabs.detectLanguage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/detectLanguage "The documentation about this has
not yet been written; please consider contributing!")

    Detects the primary language of the content in a tab.

[`tabs.duplicate()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/duplicate "Duplicates a tab, given its ID.")

    Duplicates a tab.

[`tabs.executeScript()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/executeScript "Injects JavaScript code into a
page.")

    Injects JavaScript code into a page.

[`tabs.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/get "Given
a tab ID, get the tab's details as a tabs.Tab object.")

    Retrieves details about the specified tab.

[`tabs.getAllInWindow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getAllInWindow "The documentation about this has
not yet been written; please consider contributing!") __

    Gets details about all tabs in the specified window.

[`tabs.getCurrent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getCurrent "The documentation about this has not
yet been written; please consider contributing!")

    Gets information about the tab that this script is running in, as a
[`tabs.Tab`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/Tabs/Tab "This type contains information about a tab.")
object.

[`tabs.getSelected()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getSelected "Gets the tab that is selected in the
specified window.") __

    Gets the tab that is selected in the specified window.

[`tabs.getZoom()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getZoom "Gets the current zoom factor for the
specified tab.")

    Gets the current zoom factor of the specified tab.

[`tabs.getZoomSettings()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getZoomSettings "The documentation about this has
not yet been written; please consider contributing!")

    Gets the current zoom settings for the specified tab.

[`tabs.highlight()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/highlight "A Promise that will be fulfilled with
a\\xa0windows.Window object containing details about the window whose tabs
were highlighted. If the window could not be found or some other error occurs,
the promise will be rejected with an error message.")

    Highlights one or more tabs.

[`tabs.insertCSS()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.")

    Injects CSS into a page.

[`tabs.move()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/move "The
documentation about this has not yet been written; please consider
contributing!")

    Moves one or more tabs to a new position in the same window or to a
different window.

[`tabs.print()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/print
"The documentation about this has not yet been written; please consider
contributing!")

    Prints the contents of the active tab.

[`tabs.printPreview()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/printPreview "None.")

    

Opens print preview for the active tab.



[`tabs.query()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query
"Gets all tabs that have the specified properties, or all tabs if no
properties are specified.")

    Gets all tabs that have the specified properties, or all tabs if no
properties are specified.

[`tabs.reload()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/reload
"Reload a tab, optionally bypassing the local web cache.")

    Reload a tab, optionally bypassing the local web cache.

[`tabs.remove()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/remove
"Closes one or more tabs.")

    Closes one or more tabs.

[`tabs.removeCSS()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/removeCSS "Removes from a page CSS which was
previously injected by a call to tabs.insertCSS\(\).")

    Removes from a page CSS which was previously injected by calling
[`tabs.insertCSS()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.").

[`tabs.saveAsPDF()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/saveAsPDF "Saves the current page as a PDF file.
This will open a dialog, supplied by the underlying operating system, asking
the user where they want to save the PDF file.")

    Saves the current page as a PDF.

[`tabs.sendMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage "Sends a single message from the
extension's background scripts \(or other privileged scripts, such as popup
scripts or options page scripts\) to any content scripts that belong to the
extension and are running in the specified tab.")

    Sends a single message to the content script(s) in the specified tab.

[`tabs.sendRequest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendRequest "Sends a single request to the content
script\(s\) in the specified tab, with an optional callback to run when a
response is sent back. The extension.onRequest event is fired in each content
script running in the specified tab for the current extension.") __

    Sends a single request to the content script(s) in the specified tab.
**Deprecated** : use [`tabs.sendMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage "Sends a single message from the
extension's background scripts \(or other privileged scripts, such as popup
scripts or options page scripts\) to any content scripts that belong to the
extension and are running in the specified tab.") instead.

[`tabs.setZoom()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/setZoom "Zooms the specified tab.")

    Zooms the specified tab.

[`tabs.setZoomSettings()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/setZoomSettings "Sets zoom settings for the
specified tab. These settings are reset to the default settings upon
navigating the tab.")

    Sets the zoom settings for the specified tab.

[`tabs.toggleReaderMode()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/toggleReaderMode "Toggles Reader Mode for the given
tab.")

    Toggles Reader mode for the specified tab.

[`tabs.update()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/update
"Navigate the tab to a new URL, or modify other properties of the tab.")

    Navigate the tab to a new URL, or modify other properties of the tab.



## Events



[`tabs.onActivated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActivated "The documentation about this has not
yet been written; please consider contributing!")

    Fires when the active tab in a window changes. Note that the tab's URL
may not be set at the time this event fired.

[`tabs.onActiveChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActiveChanged "The documentation about this has
not yet been written; please consider contributing!") __

    Fires when the selected tab in a window changes. **Deprecated:** use
[`tabs.onActivated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActivated "The documentation about this has not
yet been written; please consider contributing!") instead.

[`tabs.onAttached`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onAttached "Fired when a tab is attached to a
window, for example because it was moved between windows.")

    Fired when a tab is attached to a window, for example because it was
moved between windows.

[`tabs.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onCreated "Fired when a tab is created.")

    Fired when a tab is created. Note that the tab's URL may not be set at
the time this event fired.

[`tabs.onDetached`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onDetached "Fired when a tab is detached from a
window, for example because it is being moved between windows.")

    Fired when a tab is detached from a window, for example because it is
being moved between windows.

[`tabs.onHighlightChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onHighlightChanged "Fired when the highlighted or
selected tabs in a window changes.") __

    Fired when the highlighted or selected tabs in a window change.
**Deprecated:** use [`tabs.onHighlighted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onHighlighted "Fired when the set of highlighted
tabs in a window changes.") instead.

[`tabs.onHighlighted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onHighlighted "Fired when the set of highlighted
tabs in a window changes.")

    Fired when the highlighted or selected tabs in a window change.

[`tabs.onMoved`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/onMoved
"Fired when a tab is moved within a window.")

    Fired when a tab is moved within a window.

[`tabs.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onRemoved "Fired when a tab is closed.")

    Fired when a tab is closed.

[`tabs.onReplaced`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onReplaced "Fired when a tab is replaced with
another tab due to prerendering or instant.")

    Fired when a tab is replaced with another tab due to prerendering.

[`tabs.onSelectionChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onSelectionChanged "Fires when the selected tab in
a window changes.") __

    Fires when the selected tab in a window changes. **Deprecated:** use
[`tabs.onActivated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActivated "The documentation about this has not
yet been written; please consider contributing!") instead.

[`tabs.onUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onUpdated "Fired when a tab is updated.")

    Fired when a tab is updated.

[`tabs.onZoomChange`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onZoomChange "Fired when a tab is zoomed.")

    Fired when a tab is zoomed.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`MutedInfo`|  Yes|  No| 47|  No|  Yes  
`MutedInfoReason`|  Yes|  No| 47|  No|  Yes  
`PageSettings`|  No|  No| 56|  No|  No  
`TAB_ID_NONE`|  Yes|  Yes| 45| 54|  Yes  
`TabStatus`|  Yes|  Yes| 45| 54|  Yes  
`WindowType`|  Yes|  Yes| 45| 54|  Yes  
`ZoomSettings`|  Yes|  No| 45|  No|  Yes  
`ZoomSettingsMode`|  Yes|  No| 45|  No|  Yes  
`ZoomSettingsScope`|  Yes|  No| 45|  No|  Yes  
`captureVisibleTab`|  Yes *| 15| 47| 54|  Yes *  
`connect`|  Yes|  No| 45| 54|  Yes  
`create`|  Yes|  Yes| 45| 54|  Yes  
`detectLanguage`|  Yes|  Yes| 45|  No|  Yes  
`duplicate`|  Yes|  No| 47| 54|  Yes  
`executeScript`|  Yes *|  Yes *| 43 *| 54 *|  Yes *  
`get`|  Yes|  Yes| 45| 54|  Yes  
`getAllInWindow`|  Yes|  No| 45| 54|  No  
`getCurrent`|  Yes|  Yes| 45| 54|  Yes  
`getSelected`|  Yes|  No|  No|  No|  No  
`getZoom`|  Yes|  No| 45|  No|  Yes  
`getZoomSettings`|  Yes|  No| 45|  No|  Yes  
`highlight`|  Yes|  No|  No|  No|  No  
`insertCSS`|  Yes *|  Yes *| 47 *| 54 *|  Yes *  
`move`|  Yes|  No| 46|  No|  Yes  
`onActivated`|  Yes|  Yes| 45| 54|  Yes  
`onActiveChanged`|  Yes|  No|  No|  No|  No  
`onAttached`|  Yes| 15| 45| 54|  Yes  
`onCreated`|  Yes|  Yes| 45| 54|  Yes  
`onDetached`|  Yes| 15| 45| 54|  Yes  
`onHighlightChanged`|  Yes|  No|  No|  No|  No  
`onHighlighted`|  Yes|  No| 45| 54|  No  
`onMoved`|  Yes|  No| 45|  No|  Yes  
`onRemoved`|  Yes|  Yes| 45| 54|  Yes  
`onReplaced`|  Yes|  No|  No|  No|  Yes  
`onSelectionChanged`|  Yes|  No|  No|  No|  No  
`onUpdated`|  Yes|  Yes| 45| 54|  Yes  
`onZoomChange`|  Yes|  No| 45|  No|  Yes  
`print`|  No|  No| 56|  No|  No  
`printPreview`|  No|  No| 56|  No|  No  
`query`|  Yes|  Yes *| 45| 54|  Yes  
`reload`|  Yes|  No| 45| 54|  Yes  
`remove`|  Yes|  Yes| 45| 54|  Yes  
`removeCSS`|  No|  No| 49| 54|  No  
`saveAsPDF`|  No|  No| 56 *|  No|  No  
`sendMessage`|  Yes|  Yes *| 45| 54|  Yes  
`sendRequest`|  Yes|  No|  No|  No|  No  
`setZoom`|  Yes|  No| 45|  No|  Yes  
`setZoomSettings`|  Yes|  No| 45|  No|  Yes  
`toggleReaderMode`|  No|  No| 58|  No|  No  
`update`|  Yes|  Yes| 45| 54|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`MutedInfo`|  Full support Yes| No support No| Full support
47| Full support Yes| No support No  
`MutedInfoReason`| Full support Yes| No support No| Full
support 47| Full support Yes| No support No  
`PageSettings`| No support No| No support No| Full support
56| No support No| No support No  
`TAB_ID_NONE`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`TabStatus`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`WindowType`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`ZoomSettings`| Full support Yes| No support No| Full
support 45| Full support Yes| No support No  
`ZoomSettingsMode`| Full support Yes| No support No| Full
support 45| Full support Yes| No support No  
`ZoomSettingsScope`| Full support Yes| No support No| Full
support 45| Full support Yes| No support No  
`captureVisibleTab`| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __The default file format is 'jpeg'.
|  Full support 15| Full support 47| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __The default file format is 'jpeg'.
|  Full support 54  
`connect`| Full support Yes| No support No| Full support 45|
Full support Yes| Full support 54  
`create`| Full support Yes| Full support Yes| Full support
45| Full support Yes| Full support 54  
`detectLanguage`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| No support No  
`duplicate`| Full support Yes| No support No| Full support
47| Full support Yes| Full support 54  
`executeScript`| Partial supportPartial| Partial supportPartial|
Partial support43

Notes __

Partial support43

Notes __

     Notes __Before version 50, Firefox would pass a single result value into its callback rather than an array, unless 'allFrames' had been set.
|  Partial supportPartial| Partial support54  
`get`| Full support Yes| Full support Yes| Full support 45|
Full support Yes| Full support 54  
`getAllInWindow`

Deprecated __Non-standard __

|  Full support Yes| No support No| Full support 45| No
support No| Full support 54  
`getCurrent`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`getSelected`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| No
support No| No support No  
`getZoom`| Full support Yes| No support No| Full support 45|
Full support Yes| No support No  
`getZoomSettings`| Full support Yes| No support No| Full
support 45| Full support Yes| No support No  
`highlight`| Full support Yes| No support No| No support No|
No support No| No support No  
`insertCSS`| Partial supportPartial| Partial supportPartial| Partial
support47| Partial supportPartial| Partial support54  
`move`| Full support Yes| No support No| Full support 46|
Full support Yes| No support No  
`onActivated`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`onActiveChanged`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| No
support No| No support No  
`onAttached`| Full support Yes| Full support 15| Full
support 45| Full support Yes| Full support 54  
`onCreated`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`onDetached`| Full support Yes| Full support 15| Full
support 45| Full support Yes| Full support 54  
`onHighlightChanged`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| No
support No| No support No  
`onHighlighted`| Full support Yes| No support No| Full
support 45| No support No| Full support 54  
`onMoved`| Full support Yes| No support No| Full support 45|
Full support Yes| No support No  
`onRemoved`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`onReplaced`| Full support Yes| No support No| No support
No| Full support Yes| No support No  
`onSelectionChanged`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| No
support No| No support No  
`onUpdated`| Full support Yes| Full support Yes| Full
support 45| Full support Yes| Full support 54  
`onZoomChange`| Full support Yes| No support No| Full
support 45| Full support Yes| No support No  
`print`| No support No| No support No| Full support 56| No
support No| No support No  
`printPreview`| No support No| No support No| Full support
56| No support No| No support No  
`query`| Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __The`panel`, `app`, `devtools` and `popup` values for `WindowType` are not supported.
|  Full support 45| Full support Yes| Full support 54  
`reload`| Full support Yes| No support No| Full support 45|
Full support Yes| Full support 54  
`remove`| Full support Yes| Full support Yes| Full support
45| Full support Yes| Full support 54  
`removeCSS`| No support No| No support No| Full support 49|
No support No| Full support 54  
`saveAsPDF`| No support No| No support No| Full support 56

Notes __

Full support 56

Notes __

     Notes __This function does not work on Mac OS X.
|  No support No| No support No  
`sendMessage`| Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __No response is sent after the receiving tab is refreshed if there is no `runtime.onMessage` listener.
|  Full support 45| Full support Yes| Full support 54  
`sendRequest`

Deprecated __Non-standard __

|  Full support Yes| No support No| No support No| No
support No| No support No  
`setZoom`| Full support Yes| No support No| Full support 45|
Full support Yes| No support No  
`setZoomSettings`| Full support Yes| No support No| Full
support 45| Full support Yes| No support No  
`toggleReaderMode`| No support No| No support No| Full
support 58| No support No| No support No  
`update`| Full support Yes| Full support Yes| Full support
45| Full support Yes| Full support 54  
  


## Example extensions

  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page)
  * [apply-css](https://github.com/mdn/webextensions-examples/tree/master/apply-css)
  * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
  * [bookmark-it](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)
  * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out)
  * [context-menu-copy-link-with-types](https://github.com/mdn/webextensions-examples/tree/master/context-menu-copy-link-with-types)
  * [contextual-identities](https://github.com/mdn/webextensions-examples/tree/master/contextual-identities)
  * [cookie-bg-picker](https://github.com/mdn/webextensions-examples/tree/master/cookie-bg-picker)
  * [devtools-panels](https://github.com/mdn/webextensions-examples/tree/master/devtools-panels)
  * [find-across-tabs](https://github.com/mdn/webextensions-examples/tree/master/find-across-tabs)
  * [firefox-code-search](https://github.com/mdn/webextensions-examples/tree/master/firefox-code-search)
  * [history-deleter](https://github.com/mdn/webextensions-examples/tree/master/history-deleter)
  * [imagify](https://github.com/mdn/webextensions-examples/tree/master/imagify)
  * [list-cookies](https://github.com/mdn/webextensions-examples/tree/master/list-cookies)
  * [menu-demo](https://github.com/mdn/webextensions-examples/tree/master/menu-demo)
  * [open-my-page-button](https://github.com/mdn/webextensions-examples/tree/master/open-my-page-button)
  * [permissions](https://github.com/mdn/webextensions-examples/tree/master/permissions)
  * [react-es6-popup](https://github.com/mdn/webextensions-examples/tree/master/react-es6-popup)
  * [session-state](https://github.com/mdn/webextensions-examples/tree/master/session-state)
  * [store-collected-images](https://github.com/mdn/webextensions-examples/tree/master/store-collected-images)
  * [tabs-tabs-tabs](https://github.com/mdn/webextensions-examples/tree/master/tabs-tabs-tabs)



 **Acknowledgements** 

This API is based on Chromium's
[`chrome.tabs`](https://developer.chrome.com/extensions/tabs) API. This
documentation is derived from
[`tabs.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/tabs.json)
in the Chromium code.



Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.







    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.//// Redistribution and use in source and binary forms, with or without// modification, are permitted provided that the following conditions are// met:////    * Redistributions of source code must retain the above copyright// notice, this list of conditions and the following disclaimer.//    * Redistributions in binary form must reproduce the above// copyright notice, this list of conditions and the following disclaimer// in the documentation and/or other materials provided with the// distribution.//    * Neither the name of Google Inc. nor the names of its// contributors may be used to endorse or promote products derived from// this software without specific prior written permission.//// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Partial support]: Partial support
  *[Mobile __]: Mobile
  *[ Partial support]: Partial support
  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[Notes __]: See implementation notes
  *[Deprecated __]: Deprecated. Not for use in new websites.
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

