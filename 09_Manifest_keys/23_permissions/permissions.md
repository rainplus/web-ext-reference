[\n

\n\n\n\nType\n| `Array`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"permissions": [\n  "*://developer.mozilla.org/*",\n  "webRequest"\n]

\n\n  
\n\n\n

Use the `permissions` key to request special powers for your extension. This
key is an array of strings, and each string is a request for a permission.

\n

If you request permissions using this key, then the browser may inform the
user at install time that the extension is requesting certain privileges, and
ask them to confirm that they are happy to grant these privileges. The browser
may also allow the user to inspect an extension's privileges after
installation.

\n

The key can contain three kinds of permissions:

\n

\n

  * host permissions
\n

  * API permissions
\n

  * the activeTab permission
\n

\n

## Host permissions

\n

Host permissions are specified as [match
patterns](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/Match_patterns), and each pattern identifies a group of URLs
for which the extension is requesting extra privileges. For example, a host
permission could be `"*://developer.mozilla.org/*"`.

\n

The extra privileges include:

\n

\n

  * [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) and [fetch](/en-US/docs/Web/API/Fetch_API) access to those origins without cross-origin restrictions (even for requests made from content scripts)
\n

  * the ability to inject scripts programmatically (using [tabs.executeScript](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript)) into pages served from those origins
\n

  * the ability to receive events from the [webRequest](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest) API for these hosts
\n

  * the ability to access cookies for that host using the [cookies](/en-US/Add-ons/WebExtensions/API/cookies) API, as long as the "cookies" API permission is also included.
\n

  * bypass tracking protection if the host is a full domain without wildcards. Doesn't work with `<all_urls>`.
\n

\n

In Firefox, from version 56 onwards, extensions automatically get host
permissions for their own origin, which is of the form:

\n

    
    
    moz-extension://60a20a9b-1ad4-af49-9b6c-c64c98c37920/

\n

where `60a20a9b-1ad4-af49-9b6c-c64c98c37920` is the extension's internal ID.
The extension can get this URL programmatically by calling [extension.getURL
()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/getURL):

\n

    
    
    browser.extension.getURL("");\n// moz-extension://60a20a9b-1ad4-af49-9b6c-c64c98c37920/

\n

## API permissions

\n

API permissions are specified as keywords, and each keyword names a
WebExtension API that the extension would like to use.

\n

The following keywords are currently available:

\n

\n

  * `activeTab`
\n

  * `alarms`
\n

  * `bookmarks`
\n

  * `browsingData`
\n

  * `browserSettings`
\n

  * `contextMenus`
\n

  * `contextualIdentities`
\n

  * `cookies`
\n

  * `downloads`
\n

  * `downloads.open`
\n

  * `find`
\n

  * `geolocation`
\n

  * `history`
\n

  * `identity`
\n

  * `idle`
\n

  * `management`
\n

  * `menus`
\n

  * `nativeMessaging`
\n

  * `notifications`
\n

  * `pkcs11`
\n

  * `privacy`
\n

  * `proxy`
\n

  * `sessions`
\n

  * `storage`
\n

  * `tabs`
\n

  * `theme`
\n

  * `topSites`
\n

  * `webNavigation`
\n

  * `webRequest`
\n

  * `webRequestBlocking`
\n

\n

In most cases the permission just grants access to the API, with the following
exceptions:

\n

\n

  * \xa0`tabs` gives you access to [privileged parts of the `tabs` API](/en-US/Add-ons/WebExtensions/API/tabs): `Tab.url`, `Tab.title`, and `Tab.faviconUrl`. In Firefox, you also need `tabs` if you want to include `url` in the `queryInfo` parameter to\xa0 `[tabs.query()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query)`. The rest of the `tabs` API can be used without requesting any permission.
\n

  * `webRequestBlocking` enables you to use the "blocking" argument, so you can [modify and cancel requests](/en-US/Add-ons/WebExtensions/API/WebRequest).
\n

  * `downloads.open` lets you use the [`downloads.open()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads/open "The open\(\) function of the downloads API opens the downloaded file with its associated application. A downloads.onChanged event will fire when the item is opened for the first time.") API.
\n

\n

## activeTab permission

\n

This permission is specified as `"activeTab"`. If an extension has the
`activeTab` permission, then when the user interacts with the extension, the
extension is granted extra privileges for the active tab only.

\n

"User interaction" includes:

\n

\n

  * the user clicks the extension's browser action or page action
\n

  * the user selects its context menu item
\n

  * the user activates a keyboard shortcut defined by the extension
\n

\n

The extra privileges are:

\n

\n

  * the ability to inject JavaScript or CSS into the tab programmatically, using `[browser.tabs.executeScript](/en-US/Add-ons/WebExtensions/API/tabs/executeScript)` and `[browser.tabs.insertCSS](/en-US/Add-ons/WebExtensions/API/tabs/insertCSS)`
\n

  * access to the privileged parts of the tabs API for the current tab: `Tab.url`, `Tab.title`, and `Tab.faviconUrl`.
\n

\n

The intention of this permission is to enable extensions to fulfill a common
use case, without having to give them very powerful permissions. Many
extensions want to "do something to the current page when the user asks". For
example, consider an extension that wants to run a script in the current page
when the user clicks a browser action. If the\xa0 `activeTab` permission did
not exist, the extension would need to ask for the host permission
`<all_urls>`. But this gives the extension more power than it needs: it could
now execute scripts in any tab, any time it likes, instead of just the active
tab and just in response to a user action.

\n

## Clipboard access

\n

There are two permissions which enables the extension to interact with the
clipboard:

\n

\n

  * `clipboardWrite`: write to the clipboard using `document.execCommand("copy")` or `document.execCommand("cut")`
\n

  * `clipboardRead`: read from the clipboard using `document.execCommand("paste")`
\n

\n

See [Interact with the clipboard](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Interact_with_the_clipboard) for all the details on this.

\n

## Unlimited storage

\n

The `unlimitedStorage` permission:

\n

\n

  * enables extensions to exceed any quota imposed by the [`storage.local`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/local "Represents the local storage area. Items in local storage are local to the machine the extension was installed on.") API
\n

  * in Firefox, enables extensions to create a ["persistent" IndexedDB database](/en-US/docs/Web/API/IndexedDB_API/Browser_storage_limits_and_eviction_criteria#Firefox_specifics), without the browser prompting the user for permission at the time the database is created.
\n

\n

## Example

\n

    
    
     "permissions": ["*://developer.mozilla.org/*"]

\n

Request privileged access to pages under developer.mozilla.org.

\n

    
    
      "permissions": ["tabs"]

\n

Request access to the privileged pieces of the `tabs` API.

\n

    
    
      "permissions": ["*://developer.mozilla.org/*", "tabs"]

\n

Request both of the above permissions.

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n Yes| 48| 48| \n Yes  
`background`| \n Yes| \n No| \n No| \n No| \n Yes  
`unlimitedStorage`| \n Yes| \n Yes| 56| 56| \n Yes  
`geolocation`| \n Yes| \n Yes| 54| 54| \n Yes  
`activeTab`| \n Yes| \n No| 48| 48| \n Yes  
`clipboardRead`| \n Yes| \n No| 54| 54| \n Yes  
`clipboardWrite`| \n Yes| \n No| 51| 51| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`background`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`unlimitedStorage`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 56| \nFull support\n\n Yes| \nFull support\n\n 56  
`geolocation`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 54| \nFull support\n\n Yes| \nFull support\n\n 54  
`activeTab`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
48| \nFull support\n\n Yes| \nFull support\n\n 48  
`clipboardRead`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n Yes| \nFull support\n\n 54  
`clipboardWrite`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 51| \nFull support\n\n Yes| \nFull support\n\n 51  
  
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

