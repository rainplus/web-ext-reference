[\n

\n

Enables extensions to request extra permissions at runtime, after they have
been installed.

\n

\xa0

\n

Extensions need permissions to access many of the more powerful WebExtension
APIs. They can ask for permissions at install time by including the
permissions they need in the `[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)` manifest.json key. The main
advantages of asking for permissions at install time are:

\n

\n

  * the user is only asked once, so it's less disruptive for them and a simpler decision
\n

  * the extension can rely on the access to the APIs it needs, because if it's running at all, the permissions have been granted.
\n

\n

With the permissions API, an extension can ask for additional permissions at
runtime. These permissions need to be listed in the `[optional_permissions
](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/optional_permissions)` manifest.json key. Note
that some permissions are not allowed in `optional_permissions`. The main
advantages of this are:

\n

\n

  * the extension can run with a smaller set of permissions except when it actually needs them
\n

  * the extension can handle permission denial in a graceful manner instead of presenting the user with a global "all or nothing" choice at install time. You can still get a lot out of that map extension without giving it access to your location, for example.
\n

  * \n

the extension may need [host permissions](/en-US/Add-
ons/WebExtensions/manifest.json/permissions#Host_permissions), but not know at
install time exactly which host permissions it needs. For example, the list of
hosts may be a user setting. In this scenario, asking for a more specific
range of hosts at runtime can be an alternative to asking for "<all_urls>" at
install time.

\n

\n

\n

To use the permissions API, decide which permissions your extension can
request at runtime, and list them in `[optional_permissions](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/optional_permissions)`.
After this, you can request any permissions that were included in
`optional_permissions`. Requests may only be made in the handler for a user
action (for example, a click handler).

\n

\xa0

\n

## Types

\n

\n[`permissions.Permissions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/Permissions "The documentation about this
has not yet been written; please consider contributing!")

\n    Represents a set of permissions.

\n\n

## Methods

\n

\n[`permissions.contains()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/contains "Check whether the extension has
the permissions listed in the given permissions.Permissions object.")

\n    Find out whether the extension has the given set of permissions.

\n[`permissions.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/getAll "Retrieve a permissions.Permissions
object containing all the permissions currently granted to the extension.")

\n    Get all the permissions this extension currently has.

\n[`permissions.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/remove "The documentation about this has not
yet been written; please consider contributing!")

\n    Give up a set of permissions.

\n[`permissions.request()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/request "Ask for the set of permissions
listed in the given permissions.Permissions object.")

\n    Ask for a set of permissions.

\n\n

## Event handlers

\n

\n[`permissions.onAdded`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/onAdded "Fired when the extension granted
new permissions.")

\n    Fired when a new permission is granted.

\n[`permissions.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/onRemoved "Fired when some permissions are
removed from the extension.")

\n    Fired when a permission is removed.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`contains`| \n Yes| \n No| 55| 55| \n Yes  
`getAll`| \n Yes| \n No| 55| 55| \n Yes  
`onAdded`| \n Yes| \n No| \n No| \n No| \n Yes  
`onRemoved`| \n Yes| \n No| \n No| \n No| \n Yes  
`Permissions`| \n Yes| \n No| 55| 55| \n Yes  
`remove`| \n Yes| \n No| 55| 55| \n Yes  
`request`| \n Yes| \n No| 55 *| 55 *| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`contains`|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
55| \nFull support\n\n Yes| \nFull support\n\n 55  
`getAll`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55|
\nFull support\n\n Yes| \nFull support\n\n 55  
`onAdded`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`onRemoved`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`Permissions`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
55| \nFull support\n\n Yes| \nFull support\n\n 55  
`remove`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55|
\nFull support\n\n Yes| \nFull support\n\n 55  
`request`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 55

Notes __

\nFull support\n\n 55

Notes __

     Notes __The user will be prompted again for permissions that have been previously granted and then removed.
|  \nFull support\n\n Yes| \nFull support\n\n 55

Notes __

\nFull support\n\n 55

Notes __

     Notes __The user will be prompted again for permissions that have been previously granted and then removed.  
  
\n

## Example extensions

  * [permissions](https://github.com/mdn/webextensions-examples/tree/master/permissions)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.permissions`](https://developer.chrome.com/extensions/permissions)
API.

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

