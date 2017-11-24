[\n

\n

Interact with the browser's tab system.

\n

You can use this API to get a list of opened tabs, filtered by various
criteria, and to open, update, move, reload, and remove tabs. You can't
directly access the content hosted by tabs using this API, but you can insert
JavaScript and CSS into tabs using the [`tabs.executeScript()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript "Injects
JavaScript code into a page.") or [`tabs.insertCSS()`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.") APIs.

\n

You can use most of this API without any special permission. However:

\n

\n

  * to access `Tab.url`, `Tab.title`, and `Tab.favIconUrl`, you need to have the "tabs" [permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions). In Firefox this also means you need "tabs" to [`query`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query "Gets all tabs that have the specified properties, or all tabs if no properties are specified.") by URL.
\n

  * to use [`tabs.executeScript()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript "Injects JavaScript code into a page.") or [`tabs.insertCSS()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.") you must have the [host permission](/en-US/Add-ons/WebExtensions/manifest.json/permissions#Host_permissions) for the tab
\n

\n

Alternatively, you can get these permissions temporarily, only for the
currently active tab and only in response to an explicit user action, by
asking for the ["activeTab" permission](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#activeTab_permission).

\n

Many tab operations use a Tab ID. Tab IDs are guaranteed to be unique to a
single tab only within a browser session. If the browser is restarted, then it
can and will reuse tab IDs. To associate information with a tab across browser
restarts, use [`sessions.setTabValue()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/sessions/setTabValue "Stores a key/value pair to
associate with a given tab. You can subsequently retrieve this value using
sessions.getTabValue.").

\n

## Types

\n

\n[`tabs.MutedInfoReason`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/MutedInfoReason "Specifies the reason a tab was
muted or unmuted.")

\n    Specifies the reason a tab was muted or unmuted.

\n[`tabs.MutedInfo`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/MutedInfo "This object contains a boolean
indicating whether the tab is muted, and the reason for the last state
change.")

\n    This object contains a boolean indicating whether the tab is muted, and
the reason for the last state change.

\n[`tabs.PageSettings`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/PageSettings "The type tabs.PageSettings is used to
control how a tab is rendered as a PDF by the tabs.saveAsPDF\(\) method.")

\n    \n

Used to control how a tab is rendered as a PDF by the
[`tabs.saveAsPDF()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/saveAsPDF "Saves the current page as a PDF. This
will open a dialog, supplied by the underlying operating system, asking the
user where they want to save the PDF.") method.

\n

\n[`tabs.Tab`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/Tab "The
type tabs.Tab contains information about a tab. This provides access to
information about what content is in the tab, how large the content is, what
special states or restrictions are in effect, and so forth.")

\n    This type contains information about a tab.

\n[`tabs.TabStatus`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/TabStatus "Indicates whether the tab has finished
loading.")

\n    Indicates whether the tab has finished loading.

\n[`tabs.WindowType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/WindowType "The type of window that hosts this
tab.")

\n    The type of window that hosts this tab.

\n[`tabs.ZoomSettingsMode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsMode "Defines how zoom changes are
handled. Extensions can pass this value into tabs.setZoomSettings\(\) to
control how the browser handles attempts to change zoom settings for a tab.
Defaults to "automatic".")

\n    Defines whether zoom changes are handled by the browser, by the
extension, or are disabled.

\n[`tabs.ZoomSettingsScope`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsScope "Defines whether zoom changes
will persist for the page's origin, or only take effect in this tab. This
defaults to per-origin when tabs.zoomSettingsMode is "automatic", and is
always per-tab otherwise.")

\n    Defines whether zoom changes will persist for the page's origin, or only
take effect in this tab.

\n[`tabs.ZoomSettings`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettings "Defines zoom settings for a tab:
mode,\\xa0scope, and default zoom factor.")

\n    Defines zoom settings [`mode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsMode "Defines how zoom changes are
handled. Extensions can pass this value into tabs.setZoomSettings\(\) to
control how the browser handles attempts to change zoom settings for a tab.
Defaults to "automatic"."),\xa0[`scope`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/ZoomSettingsScope "Defines whether zoom changes
will persist for the page's origin, or only take effect in this tab. This
defaults to per-origin when tabs.zoomSettingsMode is "automatic", and is
always per-tab otherwise."), and default zoom factor.

\n\n

## Properties

\n

\n[`tabs.TAB_ID_NONE`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/TAB_ID_NONE "A special ID value given to tabs that
are not browser tabs \(for example, tabs in devtools windows\).")

\n    A special ID value given to tabs that are not browser tabs (for example,
tabs in devtools windows).

\n\n

## Functions

\n

\n[`tabs.captureVisibleTab()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/captureVisibleTab "Creates a data URI encoding an
image of the visible area of the currently active tab in the specified window.
You must have the <all_urls> permission to use this method.")

\n    Creates a data URI encoding an image of the visible area of the
currently active tab in the specified window.

\n[`tabs.connect()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/connect "Call this function to set up a connection
between the extension's background scripts \(or other privileged scripts, such
as popup scripts or options page scripts\) and any content scripts that belong
to this extension and are running in the specified tab. This function returns
a runtime.Port object.")

\n    Sets up a messaging connection between the extension's background
scripts (or other privileged scripts, such as popup scripts or options page
scripts) and any [content scripts](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts) running in the
specified tab.

\n[`tabs.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/create
"Creates a new tab.")

\n    Creates a new tab.

\n[`tabs.detectLanguage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/detectLanguage "The documentation about this has
not yet been written; please consider contributing!")

\n    Detects the primary language of the content in a tab.

\n[`tabs.duplicate()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/duplicate "Duplicates a tab, given its ID.")

\n    Duplicates a tab.

\n[`tabs.executeScript()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/executeScript "Injects JavaScript code into a
page.")

\n    Injects JavaScript code into a page.

\n[`tabs.get()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/get "Given
a tab ID, get the tab's details as a tabs.Tab object.")

\n    Retrieves details about the specified tab.

\n[`tabs.getAllInWindow()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getAllInWindow "The documentation about this has
not yet been written; please consider contributing!") __

\n    Gets details about all tabs in the specified window.

\n[`tabs.getCurrent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getCurrent "The documentation about this has not
yet been written; please consider contributing!")

\n    Gets information about the tab that this script is running in, as a
[`tabs.Tab`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/Tabs/Tab "This type contains information about a tab.")
object.

\n[`tabs.getSelected()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getSelected "Gets the tab that is selected in the
specified window.") __

\n    Gets the tab that is selected in the specified window.

\n[`tabs.getZoom()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getZoom "Gets the current zoom factor for the
specified tab.")

\n    Gets the current zoom factor of the specified tab.

\n[`tabs.getZoomSettings()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/getZoomSettings "The documentation about this has
not yet been written; please consider contributing!")

\n    Gets the current zoom settings for the specified tab.

\n[`tabs.highlight()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/highlight "A Promise that will be fulfilled with
a\\xa0windows.Window object containing details about the window whose tabs
were highlighted. If the window could not be found or some other error occurs,
the promise will be rejected with an error message.")

\n    Highlights one or more tabs.

\n[`tabs.insertCSS()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.")

\n    Injects CSS into a page.

\n[`tabs.move()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/move "The
documentation about this has not yet been written; please consider
contributing!")

\n    Moves one or more tabs to a new position in the same window or to a
different window.

\n[`tabs.print()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/print
"The documentation about this has not yet been written; please consider
contributing!")

\n    Prints the contents of the active tab.

\n[`tabs.printPreview()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/printPreview "None.")

\n    \n

Opens print preview for the active tab.

\n

\n[`tabs.query()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query
"Gets all tabs that have the specified properties, or all tabs if no
properties are specified.")

\n    Gets all tabs that have the specified properties, or all tabs if no
properties are specified.

\n[`tabs.reload()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/reload
"Reload a tab, optionally bypassing the local web cache.")

\n    Reload a tab, optionally bypassing the local web cache.

\n[`tabs.remove()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/remove
"Closes one or more tabs.")

\n    Closes one or more tabs.

\n[`tabs.removeCSS()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/removeCSS "Removes from a page CSS which was
previously injected by a call to tabs.insertCSS\(\).")

\n    Removes from a page CSS which was previously injected by calling
[`tabs.insertCSS()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/insertCSS "Injects CSS into a page.").

\n[`tabs.saveAsPDF()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/saveAsPDF "Saves the current page as a PDF file.
This will open a dialog, supplied by the underlying operating system, asking
the user where they want to save the PDF file.")

\n    Saves the current page as a PDF.

\n[`tabs.sendMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage "Sends a single message from the
extension's background scripts \(or other privileged scripts, such as popup
scripts or options page scripts\) to any content scripts that belong to the
extension and are running in the specified tab.")

\n    Sends a single message to the content script(s) in the specified tab.

\n[`tabs.sendRequest()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendRequest "Sends a single request to the content
script\(s\) in the specified tab, with an optional callback to run when a
response is sent back. The extension.onRequest event is fired in each content
script running in the specified tab for the current extension.") __

\n    Sends a single request to the content script(s) in the specified tab.
**Deprecated** : use [`tabs.sendMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/sendMessage "Sends a single message from the
extension's background scripts \(or other privileged scripts, such as popup
scripts or options page scripts\) to any content scripts that belong to the
extension and are running in the specified tab.") instead.

\n[`tabs.setZoom()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/setZoom "Zooms the specified tab.")

\n    Zooms the specified tab.

\n[`tabs.setZoomSettings()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/setZoomSettings "Sets zoom settings for the
specified tab. These settings are reset to the default settings upon
navigating the tab.")

\n    Sets the zoom settings for the specified tab.

\n[`tabs.toggleReaderMode()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/toggleReaderMode "Toggles Reader Mode for the given
tab.")

\n    Toggles Reader mode for the specified tab.

\n[`tabs.update()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/update
"Navigate the tab to a new URL, or modify other properties of the tab.")

\n    Navigate the tab to a new URL, or modify other properties of the tab.

\n\n

## Events

\n

\n[`tabs.onActivated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActivated "The documentation about this has not
yet been written; please consider contributing!")

\n    Fires when the active tab in a window changes. Note that the tab's URL
may not be set at the time this event fired.

\n[`tabs.onActiveChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActiveChanged "The documentation about this has
not yet been written; please consider contributing!") __

\n    Fires when the selected tab in a window changes. **Deprecated:** use
[`tabs.onActivated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActivated "The documentation about this has not
yet been written; please consider contributing!") instead.

\n[`tabs.onAttached`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onAttached "Fired when a tab is attached to a
window, for example because it was moved between windows.")

\n    Fired when a tab is attached to a window, for example because it was
moved between windows.

\n[`tabs.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onCreated "Fired when a tab is created.")

\n    Fired when a tab is created. Note that the tab's URL may not be set at
the time this event fired.

\n[`tabs.onDetached`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onDetached "Fired when a tab is detached from a
window, for example because it is being moved between windows.")

\n    Fired when a tab is detached from a window, for example because it is
being moved between windows.

\n[`tabs.onHighlightChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onHighlightChanged "Fired when the highlighted or
selected tabs in a window changes.") __

\n    Fired when the highlighted or selected tabs in a window change.
**Deprecated:** use [`tabs.onHighlighted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onHighlighted "Fired when the set of highlighted
tabs in a window changes.") instead.

\n[`tabs.onHighlighted`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onHighlighted "Fired when the set of highlighted
tabs in a window changes.")

\n    Fired when the highlighted or selected tabs in a window change.

\n[`tabs.onMoved`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/onMoved
"Fired when a tab is moved within a window.")

\n    Fired when a tab is moved within a window.

\n[`tabs.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onRemoved "Fired when a tab is closed.")

\n    Fired when a tab is closed.

\n[`tabs.onReplaced`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onReplaced "Fired when a tab is replaced with
another tab due to prerendering or instant.")

\n    Fired when a tab is replaced with another tab due to prerendering.

\n[`tabs.onSelectionChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onSelectionChanged "Fires when the selected tab in
a window changes.") __

\n    Fires when the selected tab in a window changes. **Deprecated:** use
[`tabs.onActivated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onActivated "The documentation about this has not
yet been written; please consider contributing!") instead.

\n[`tabs.onUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onUpdated "Fired when a tab is updated.")

\n    Fired when a tab is updated.

\n[`tabs.onZoomChange`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/tabs/onZoomChange "Fired when a tab is zoomed.")

\n    Fired when a tab is zoomed.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`MutedInfo`| \n Yes| \n No| 47| \n No| \n Yes  
`MutedInfoReason`| \n Yes| \n No| 47| \n No| \n Yes  
`PageSettings`| \n No| \n No| 56| \n No| \n No  
`TAB_ID_NONE`| \n Yes| \n Yes| 45| 54| \n Yes  
`TabStatus`| \n Yes| \n Yes| 45| 54| \n Yes  
`WindowType`| \n Yes| \n Yes| 45| 54| \n Yes  
`ZoomSettings`| \n Yes| \n No| 45| \n No| \n Yes  
`ZoomSettingsMode`| \n Yes| \n No| 45| \n No| \n Yes  
`ZoomSettingsScope`| \n Yes| \n No| 45| \n No| \n Yes  
`captureVisibleTab`| \n Yes *| 15| 47| 54| \n Yes *  
`connect`| \n Yes| \n No| 45| 54| \n Yes  
`create`| \n Yes| \n Yes| 45| 54| \n Yes  
`detectLanguage`| \n Yes| \n Yes| 45| \n No| \n Yes  
`duplicate`| \n Yes| \n No| 47| 54| \n Yes  
`executeScript`| \n Yes *| \n Yes *| 43 *| 54 *| \n Yes *  
`get`| \n Yes| \n Yes| 45| 54| \n Yes  
`getAllInWindow`| \n Yes| \n No| 45| 54| \n No  
`getCurrent`| \n Yes| \n Yes| 45| 54| \n Yes  
`getSelected`| \n Yes| \n No| \n No| \n No| \n No  
`getZoom`| \n Yes| \n No| 45| \n No| \n Yes  
`getZoomSettings`| \n Yes| \n No| 45| \n No| \n Yes  
`highlight`| \n Yes| \n No| \n No| \n No| \n No  
`insertCSS`| \n Yes *| \n Yes *| 47 *| 54 *| \n Yes *  
`move`| \n Yes| \n No| 46| \n No| \n Yes  
`onActivated`| \n Yes| \n Yes| 45| 54| \n Yes  
`onActiveChanged`| \n Yes| \n No| \n No| \n No| \n No  
`onAttached`| \n Yes| 15| 45| 54| \n Yes  
`onCreated`| \n Yes| \n Yes| 45| 54| \n Yes  
`onDetached`| \n Yes| 15| 45| 54| \n Yes  
`onHighlightChanged`| \n Yes| \n No| \n No| \n No| \n No  
`onHighlighted`| \n Yes| \n No| 45| 54| \n No  
`onMoved`| \n Yes| \n No| 45| \n No| \n Yes  
`onRemoved`| \n Yes| \n Yes| 45| 54| \n Yes  
`onReplaced`| \n Yes| \n No| \n No| \n No| \n Yes  
`onSelectionChanged`| \n Yes| \n No| \n No| \n No| \n No  
`onUpdated`| \n Yes| \n Yes| 45| 54| \n Yes  
`onZoomChange`| \n Yes| \n No| 45| \n No| \n Yes  
`print`| \n No| \n No| 56| \n No| \n No  
`printPreview`| \n No| \n No| 56| \n No| \n No  
`query`| \n Yes| \n Yes *| 45| 54| \n Yes  
`reload`| \n Yes| \n No| 45| 54| \n Yes  
`remove`| \n Yes| \n Yes| 45| 54| \n Yes  
`removeCSS`| \n No| \n No| 49| 54| \n No  
`saveAsPDF`| \n No| \n No| 56 *| \n No| \n No  
`sendMessage`| \n Yes| \n Yes *| 45| 54| \n Yes  
`sendRequest`| \n Yes| \n No| \n No| \n No| \n No  
`setZoom`| \n Yes| \n No| 45| \n No| \n Yes  
`setZoomSettings`| \n Yes| \n No| 45| \n No| \n Yes  
`toggleReaderMode`| \n No| \n No| 58| \n No| \n No  
`update`| \n Yes| \n Yes| 45| 54| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`MutedInfo`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nNo support\n\n No  
`MutedInfoReason`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 47| \nFull support\n\n Yes| \nNo support\n\n No  
`PageSettings`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
56| \nNo support\n\n No| \nNo support\n\n No  
`TAB_ID_NONE`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`TabStatus`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`WindowType`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`ZoomSettings`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`ZoomSettingsMode`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`ZoomSettingsScope`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`captureVisibleTab`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __The default file format is 'jpeg'.
|  \nFull support\n\n 15| \nFull support\n\n 47| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __The default file format is 'jpeg'.
|  \nFull support\n\n 54  
`connect`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 54  
`create`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 54  
`detectLanguage`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`duplicate`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nFull support\n\n 54  
`executeScript`| \nPartial support\nPartial| \nPartial support\nPartial|
\nPartial support\n43

Notes __

\nPartial support\n43

Notes __

     Notes __Before version 50, Firefox would pass a single result value into its callback rather than an array, unless 'allFrames' had been set.
|  \nPartial support\nPartial| \nPartial support\n54  
`get`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 54  
`getAllInWindow`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45| \nNo
support\n\n No| \nFull support\n\n 54  
`getCurrent`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`getSelected`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No  
`getZoom`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nNo support\n\n No  
`getZoomSettings`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`highlight`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nNo support\n\n No| \nNo support\n\n No  
`insertCSS`| \nPartial support\nPartial| \nPartial support\nPartial| \nPartial
support\n47| \nPartial support\nPartial| \nPartial support\n54  
`move`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 46|
\nFull support\n\n Yes| \nNo support\n\n No  
`onActivated`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`onActiveChanged`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No  
`onAttached`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`onCreated`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`onDetached`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`onHighlightChanged`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No  
`onHighlighted`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nNo support\n\n No| \nFull support\n\n 54  
`onMoved`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nNo support\n\n No  
`onRemoved`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`onReplaced`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`onSelectionChanged`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No  
`onUpdated`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`onZoomChange`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`print`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 56| \nNo
support\n\n No| \nNo support\n\n No  
`printPreview`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
56| \nNo support\n\n No| \nNo support\n\n No  
`query`| \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __The`panel`, `app`, `devtools` and `popup` values for `WindowType` are not supported.
|  \nFull support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`reload`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nFull support\n\n 54  
`remove`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 54  
`removeCSS`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 49|
\nNo support\n\n No| \nFull support\n\n 54  
`saveAsPDF`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 56

Notes __

\nFull support\n\n 56

Notes __

     Notes __This function does not work on Mac OS X.
|  \nNo support\n\n No| \nNo support\n\n No  
`sendMessage`| \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __No response is sent after the receiving tab is refreshed if there is no `runtime.onMessage` listener.
|  \nFull support\n\n 45| \nFull support\n\n Yes| \nFull support\n\n 54  
`sendRequest`

Deprecated __Non-standard __

| \n Full support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No  
`setZoom`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nNo support\n\n No  
`setZoomSettings`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`toggleReaderMode`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 58| \nNo support\n\n No| \nNo support\n\n No  
`update`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull support\n\n
45| \nFull support\n\n Yes| \nFull support\n\n 54  
  
\n

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

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.tabs`](https://developer.chrome.com/extensions/tabs) API. This
documentation is derived from
[`tabs.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/tabs.json)
in the Chromium code.

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
  *[\n Full support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Non-standard __]: Non-standard. Expect poor cross-browser support.
  *[Notes __]: See implementation notes
  *[Deprecated __]: Deprecated. Not for use in new websites.
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

