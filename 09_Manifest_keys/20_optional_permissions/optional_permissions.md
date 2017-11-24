Type | `Array`  
---|---  
Mandatory | No  
Example |

    
    
    
    "optional_permissions": [
      "*://developer.mozilla.org/*",
      "webRequest"
    ]  
  
Use the `optional_permissions` key to list permissions which you want to ask
for at runtime, after your extension has been installed.

While the `[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)` key lists permissions which your
extension needs if it is to be installed at all, `optional_permissions` lists
permissions which your extension doesn't need at install time, but which it
might need to ask for at runtime at some point after it has been installed. To
ask for a permission, use the `[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions)` API. Asking for a permission will probably
present the user with a dialog asking them to grant the permission to your
extension.

The key can contain two kinds of permissions: host permissions and API
permissions.

## Host permissions

These are the same as the host permissions you can specify in the
`[permissions](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions)` key.

## API permissions

You can include any of the following here, but not in all browsers: check the
compatibility table for browser-specific details:

  * `activeTab`
  * `background`
  * `bookmarks`
  * `browserSettings`
  * `clipboardRead`
  * `clipboardWrite`
  * `contentSettings`
  * `contextMenus`
  * `cookies`
  * `debugger`
  * `geolocation`
  * `history`
  * `idle`
  * `management`
  * `notifications`
  * `pageCapture`
  * `tabs`
  * `topSites`
  * `webNavigation`
  * `webRequest`
  * `webRequestBlocking`

Note that this is a subset of the API permissions allowed in `[permissions
](/en-US/Add-ons/WebExtensions/manifest.json/permissions#API_permissions)`.

Of this set, the following permissions are granted silently, without a user
prompt: activeTab, cookies, idle, webRequest, webRequestBlocking.

## Example

    
    
     "optional_permissions": ["*://developer.mozilla.org/*"]

Enable the extension to ask for privileged access to pages under
developer.mozilla.org.

    
    
      "optional_permissions": ["tabs"]

Enable the extension to ask for access to the privileged pieces of the `tabs`
API.

    
    
      "optional_permissions": ["*://developer.mozilla.org/*", "tabs"]

Enable the extension to ask for both of the above permissions.

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 55| 55|  Yes  
`bookmarks`|  Yes|  No| 55| 55|  Yes  
`clipboardRead`|  Yes|  No| 55| 55|  Yes  
`clipboardWrite`|  Yes|  No| 55| 55|  Yes  
`cookies`|  Yes|  No| 55| 55|  Yes  
`history`|  Yes|  No| 55| 55|  Yes  
`idle`|  Yes|  No| 55| 55|  Yes  
`notifications`|  Yes|  No| 55| 55|  Yes  
`tabs`|  Yes|  No| 55| 55|  Yes  
`topSites`|  Yes|  No| 55| 55|  Yes  
`webNavigation`|  Yes|  No| 55| 55|  Yes  
`webRequest`|  Yes|  No| 55| 55|  Yes  
`webRequestBlocking`|  Yes|  No| 55| 55|  Yes  
`background`|  Yes|  No|  No|  No|  Yes  
`contentSettings`|  Yes|  No|  No|  No|  Yes  
`contextMenus`|  Yes|  No|  No|  No|  Yes  
`debugger`|  Yes|  No|  No|  No|  Yes  
`management`|  Yes|  No|  No|  No|  Yes  
`pageCapture`|  Yes|  No|  No|  No|  Yes  
`activeTab`|  No|  No| 55| 55|  No  
`geolocation`|  No|  No| 55| 55|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`bookmarks`|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`clipboardRead`|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`clipboardWrite`|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`cookies`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`history`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`idle`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`notifications`|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`tabs`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`topSites`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`webNavigation`|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`webRequest`|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`webRequestBlocking`|  Full support Yes|  No support No|  Full support 55|
Full support Yes|  Full support 55  
`background`|  Full support Yes|  No support No|  No support No|  Full support
Yes|  No support No  
`contentSettings`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`contextMenus`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`debugger`|  Full support Yes|  No support No|  No support No|  Full support
Yes|  No support No  
`management`|  Full support Yes|  No support No|  No support No|  Full support
Yes|  No support No  
`pageCapture`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`activeTab`|  No support No|  No support No|  Full support 55|  No support No|
Full support 55  
`geolocation`|  No support No|  No support No|  Full support 55|  No support
No|  Full support 55

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

