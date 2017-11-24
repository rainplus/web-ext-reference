Type | `Array`  
---|---  
Mandatory | No  
Example |

    
    
    "permissions": [
      "*://developer.mozilla.org/*",
      "webRequest"
    ]  
  
Use the `permissions` key to request special powers for your extension. This
key is an array of strings, and each string is a request for a permission.

If you request permissions using this key, then the browser may inform the
user at install time that the extension is requesting certain privileges, and
ask them to confirm that they are happy to grant these privileges. The browser
may also allow the user to inspect an extension's privileges after
installation.

The key can contain three kinds of permissions:

  * host permissions
  * API permissions
  * the activeTab permission

## Host permissions

Host permissions are specified as [match
patterns](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/Match_patterns), and each pattern identifies a group of URLs
for which the extension is requesting extra privileges. For example, a host
permission could be `"*://developer.mozilla.org/*"`.

The extra privileges include:

  * [XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) and [fetch](/en-US/docs/Web/API/Fetch_API) access to those origins without cross-origin restrictions (even for requests made from content scripts)
  * the ability to inject scripts programmatically (using [tabs.executeScript](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript)) into pages served from those origins
  * the ability to receive events from the [webRequest](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest) API for these hosts
  * the ability to access cookies for that host using the [cookies](/en-US/Add-ons/WebExtensions/API/cookies) API, as long as the "cookies" API permission is also included.
  * bypass tracking protection if the host is a full domain without wildcards. Doesn't work with `<all_urls>`.

In Firefox, from version 56 onwards, extensions automatically get host
permissions for their own origin, which is of the form:

    
    
    moz-extension://60a20a9b-1ad4-af49-9b6c-c64c98c37920/

where `60a20a9b-1ad4-af49-9b6c-c64c98c37920` is the extension's internal ID.
The extension can get this URL programmatically by calling [extension.getURL
()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/getURL):

    
    
    browser.extension.getURL("");
    // moz-extension://60a20a9b-1ad4-af49-9b6c-c64c98c37920/

## API permissions

API permissions are specified as keywords, and each keyword names a
WebExtension API that the extension would like to use.

The following keywords are currently available:

  * `activeTab`
  * `alarms`
  * `bookmarks`
  * `browsingData`
  * `browserSettings`
  * `contextMenus`
  * `contextualIdentities`
  * `cookies`
  * `downloads`
  * `downloads.open`
  * `find`
  * `geolocation`
  * `history`
  * `identity`
  * `idle`
  * `management`
  * `menus`
  * `nativeMessaging`
  * `notifications`
  * `pkcs11`
  * `privacy`
  * `proxy`
  * `sessions`
  * `storage`
  * `tabs`
  * `theme`
  * `topSites`
  * `webNavigation`
  * `webRequest`
  * `webRequestBlocking`

In most cases the permission just grants access to the API, with the following
exceptions:

  *  `tabs` gives you access to [privileged parts of the `tabs` API](/en-US/Add-ons/WebExtensions/API/tabs): `Tab.url`, `Tab.title`, and `Tab.faviconUrl`. In Firefox, you also need `tabs` if you want to include `url` in the `queryInfo` parameter to  `[tabs.query()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query)`. The rest of the `tabs` API can be used without requesting any permission.
  * `webRequestBlocking` enables you to use the "blocking" argument, so you can [modify and cancel requests](/en-US/Add-ons/WebExtensions/API/WebRequest).
  * `downloads.open` lets you use the [`downloads.open()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads/open "The open\(\) function of the downloads API opens the downloaded file with its associated application. A downloads.onChanged event will fire when the item is opened for the first time.") API.

## activeTab permission

This permission is specified as `"activeTab"`. If an extension has the
`activeTab` permission, then when the user interacts with the extension, the
extension is granted extra privileges for the active tab only.

"User interaction" includes:

  * the user clicks the extension's browser action or page action
  * the user selects its context menu item
  * the user activates a keyboard shortcut defined by the extension

The extra privileges are:

  * the ability to inject JavaScript or CSS into the tab programmatically, using `[browser.tabs.executeScript](/en-US/Add-ons/WebExtensions/API/tabs/executeScript)` and `[browser.tabs.insertCSS](/en-US/Add-ons/WebExtensions/API/tabs/insertCSS)`
  * access to the privileged parts of the tabs API for the current tab: `Tab.url`, `Tab.title`, and `Tab.faviconUrl`.

The intention of this permission is to enable extensions to fulfill a common
use case, without having to give them very powerful permissions. Many
extensions want to "do something to the current page when the user asks". For
example, consider an extension that wants to run a script in the current page
when the user clicks a browser action. If the  `activeTab` permission did not
exist, the extension would need to ask for the host permission `<all_urls>`.
But this gives the extension more power than it needs: it could now execute
scripts in any tab, any time it likes, instead of just the active tab and just
in response to a user action.

## Clipboard access

There are two permissions which enables the extension to interact with the
clipboard:

  * `clipboardWrite`: write to the clipboard using `document.execCommand("copy")` or `document.execCommand("cut")`
  * `clipboardRead`: read from the clipboard using `document.execCommand("paste")`

See [Interact with the clipboard](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Interact_with_the_clipboard) for all the details on this.

## Unlimited storage

The `unlimitedStorage` permission:

  * enables extensions to exceed any quota imposed by the [`storage.local`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/local "Represents the local storage area. Items in local storage are local to the machine the extension was installed on.") API
  * in Firefox, enables extensions to create a ["persistent" IndexedDB database](/en-US/docs/Web/API/IndexedDB_API/Browser_storage_limits_and_eviction_criteria#Firefox_specifics), without the browser prompting the user for permission at the time the database is created.

## Example

    
    
     "permissions": ["*://developer.mozilla.org/*"]

Request privileged access to pages under developer.mozilla.org.

    
    
      "permissions": ["tabs"]

Request access to the privileged pieces of the `tabs` API.

    
    
      "permissions": ["*://developer.mozilla.org/*", "tabs"]

Request both of the above permissions.

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  Yes| 48| 48|  Yes  
`background`|  Yes|  No|  No|  No|  Yes  
`unlimitedStorage`|  Yes|  Yes| 56| 56|  Yes  
`geolocation`|  Yes|  Yes| 54| 54|  Yes  
`activeTab`|  Yes|  No| 48| 48|  Yes  
`clipboardRead`|  Yes|  No| 54| 54|  Yes  
`clipboardWrite`|  Yes|  No| 51| 51|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes|  Full support Yes|  Full support 48|  Full
support Yes|  Full support 48  
`background`|  Full support Yes|  No support No|  No support No|  Full support
Yes|  No support No  
`unlimitedStorage`|  Full support Yes|  Full support Yes|  Full support 56|
Full support Yes|  Full support 56  
`geolocation`|  Full support Yes|  Full support Yes|  Full support 54|  Full
support Yes|  Full support 54  
`activeTab`|  Full support Yes|  No support No|  Full support 48|  Full
support Yes|  Full support 48  
`clipboardRead`|  Full support Yes|  No support No|  Full support 54|  Full
support Yes|  Full support 54  
`clipboardWrite`|  Full support Yes|  No support No|  Full support 51|  Full
support Yes|  Full support 51

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
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

