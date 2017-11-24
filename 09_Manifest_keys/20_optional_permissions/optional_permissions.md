[\n

\n\n\n\nType\n| `Array`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n\n"optional_permissions": [\n  "*://developer.mozilla.org/*",\n  "webRequest"\n]

\n\n  
\n\n\n

Use the `optional_permissions` key to list permissions which you want to ask
for at runtime, after your extension has been installed.

\n

While the `[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)` key lists permissions which your
extension needs if it is to be installed at all, `optional_permissions` lists
permissions which your extension doesn't need at install time, but which it
might need to ask for at runtime at some point after it has been installed. To
ask for a permission, use the `[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions)` API. Asking for a permission will probably
present the user with a dialog asking them to grant the permission to your
extension.

\n

The key can contain two kinds of permissions: host permissions and API
permissions.

\n

## Host permissions

\n

These are the same as the host permissions you can specify in the
`[permissions](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions)` key.

\n

## API permissions

\n

You can include any of the following here, but not in all browsers: check the
compatibility table for browser-specific details:

\n

\n

  * `activeTab`
\n

  * `background`
\n

  * `bookmarks`
\n

  * `browserSettings`
\n

  * `clipboardRead`
\n

  * `clipboardWrite`
\n

  * `contentSettings`
\n

  * `contextMenus`
\n

  * `cookies`
\n

  * `debugger`
\n

  * `geolocation`
\n

  * `history`
\n

  * `idle`
\n

  * `management`
\n

  * `notifications`
\n

  * `pageCapture`
\n

  * `tabs`
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

Note that this is a subset of the API permissions allowed in `[permissions
](/en-US/Add-ons/WebExtensions/manifest.json/permissions#API_permissions)`.

\n

Of this set, the following permissions are granted silently, without a user
prompt: activeTab, cookies, idle, webRequest, webRequestBlocking.

\n

## Example

\n

    
    
     "optional_permissions": ["*://developer.mozilla.org/*"]

\n

Enable the extension to ask for privileged access to pages under
developer.mozilla.org.

\n

    
    
      "optional_permissions": ["tabs"]

\n

Enable the extension to ask for access to the privileged pieces of the `tabs`
API.

\n

    
    
      "optional_permissions": ["*://developer.mozilla.org/*", "tabs"]

\n

Enable the extension to ask for both of the above permissions.

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 55| 55| \n Yes  
`bookmarks`| \n Yes| \n No| 55| 55| \n Yes  
`clipboardRead`| \n Yes| \n No| 55| 55| \n Yes  
`clipboardWrite`| \n Yes| \n No| 55| 55| \n Yes  
`cookies`| \n Yes| \n No| 55| 55| \n Yes  
`history`| \n Yes| \n No| 55| 55| \n Yes  
`idle`| \n Yes| \n No| 55| 55| \n Yes  
`notifications`| \n Yes| \n No| 55| 55| \n Yes  
`tabs`| \n Yes| \n No| 55| 55| \n Yes  
`topSites`| \n Yes| \n No| 55| 55| \n Yes  
`webNavigation`| \n Yes| \n No| 55| 55| \n Yes  
`webRequest`| \n Yes| \n No| 55| 55| \n Yes  
`webRequestBlocking`| \n Yes| \n No| 55| 55| \n Yes  
`background`| \n Yes| \n No| \n No| \n No| \n Yes  
`contentSettings`| \n Yes| \n No| \n No| \n No| \n Yes  
`contextMenus`| \n Yes| \n No| \n No| \n No| \n Yes  
`debugger`| \n Yes| \n No| \n No| \n No| \n Yes  
`management`| \n Yes| \n No| \n No| \n No| \n Yes  
`pageCapture`| \n Yes| \n No| \n No| \n No| \n Yes  
`activeTab`| \n No| \n No| 55| 55| \n No  
`geolocation`| \n No| \n No| 55| 55| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nFull support\n\n Yes| \nFull support\n\n 55  
`bookmarks`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
55| \nFull support\n\n Yes| \nFull support\n\n 55  
`clipboardRead`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nFull support\n\n Yes| \nFull support\n\n 55  
`clipboardWrite`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nFull support\n\n Yes| \nFull support\n\n 55  
`cookies`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55|
\nFull support\n\n Yes| \nFull support\n\n 55  
`history`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55|
\nFull support\n\n Yes| \nFull support\n\n 55  
`idle`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55|
\nFull support\n\n Yes| \nFull support\n\n 55  
`notifications`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nFull support\n\n Yes| \nFull support\n\n 55  
`tabs`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55|
\nFull support\n\n Yes| \nFull support\n\n 55  
`topSites`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
55| \nFull support\n\n Yes| \nFull support\n\n 55  
`webNavigation`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nFull support\n\n Yes| \nFull support\n\n 55  
`webRequest`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
55| \nFull support\n\n Yes| \nFull support\n\n 55  
`webRequestBlocking`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nFull support\n\n Yes| \nFull support\n\n 55  
`background`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`contentSettings`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`contextMenus`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`debugger`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`management`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`pageCapture`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`activeTab`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 55|
\nNo support\n\n No| \nFull support\n\n 55  
`geolocation`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
55| \nNo support\n\n No| \nFull support\n\n 55  
  
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

