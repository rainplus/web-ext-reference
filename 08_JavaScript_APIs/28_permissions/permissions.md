Enables extensions to request extra permissions at runtime, after they have
been installed.



Extensions need permissions to access many of the more powerful WebExtension
APIs. They can ask for permissions at install time by including the
permissions they need in the `[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)` manifest.json key. The main
advantages of asking for permissions at install time are:

  * the user is only asked once, so it's less disruptive for them and a simpler decision
  * the extension can rely on the access to the APIs it needs, because if it's running at all, the permissions have been granted.

With the permissions API, an extension can ask for additional permissions at
runtime. These permissions need to be listed in the `[optional_permissions
](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/optional_permissions)` manifest.json key. Note
that some permissions are not allowed in `optional_permissions`. The main
advantages of this are:

  * the extension can run with a smaller set of permissions except when it actually needs them
  * the extension can handle permission denial in a graceful manner instead of presenting the user with a global "all or nothing" choice at install time. You can still get a lot out of that map extension without giving it access to your location, for example.
  * the extension may need [host permissions](/en-US/Add-ons/WebExtensions/manifest.json/permissions#Host_permissions), but not know at install time exactly which host permissions it needs. For example, the list of hosts may be a user setting. In this scenario, asking for a more specific range of hosts at runtime can be an alternative to asking for "<all_urls>" at install time.

To use the permissions API, decide which permissions your extension can
request at runtime, and list them in `[optional_permissions](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/optional_permissions)`.
After this, you can request any permissions that were included in
`optional_permissions`. Requests may only be made in the handler for a user
action (for example, a click handler).



## Types

[`permissions.Permissions`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/Permissions "The documentation about this
has not yet been written; please consider contributing!")

    Represents a set of permissions.

## Methods

[`permissions.contains()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/contains "Check whether the extension has
the permissions listed in the given permissions.Permissions object.")

    Find out whether the extension has the given set of permissions.
[`permissions.getAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/getAll "Retrieve a permissions.Permissions
object containing all the permissions currently granted to the extension.")

    Get all the permissions this extension currently has.
[`permissions.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/remove "The documentation about this has not
yet been written; please consider contributing!")

    Give up a set of permissions.
[`permissions.request()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/request "Ask for the set of permissions
listed in the given permissions.Permissions object.")

    Ask for a set of permissions.

## Event handlers

[`permissions.onAdded`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/onAdded "Fired when the extension granted
new permissions.")

    Fired when a new permission is granted.
[`permissions.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/permissions/onRemoved "Fired when some permissions are
removed from the extension.")

    Fired when a permission is removed.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`contains`|  Yes|  No| 55| 55|  Yes  
`getAll`|  Yes|  No| 55| 55|  Yes  
`onAdded`|  Yes|  No|  No|  No|  Yes  
`onRemoved`|  Yes|  No|  No|  No|  Yes  
`Permissions`|  Yes|  No| 55| 55|  Yes  
`remove`|  Yes|  No| 55| 55|  Yes  
`request`|  Yes|  No| 55 *| 55 *|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`contains`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`getAll`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`onAdded`|  Full support Yes|  No support No|  No support No|  Full support
Yes|  No support No  
`onRemoved`|  Full support Yes|  No support No|  No support No|  Full support
Yes|  No support No  
`Permissions`|  Full support Yes|  No support No|  Full support 55|  Full
support Yes|  Full support 55  
`remove`|  Full support Yes|  No support No|  Full support 55|  Full support
Yes|  Full support 55  
`request`|  Full support Yes|  No support No|  Full support 55

Notes __

Full support 55

Notes __

     Notes __The user will be prompted again for permissions that have been previously granted and then removed.
|  Full support Yes|  Full support 55

Notes __

Full support 55

Notes __

     Notes __The user will be prompted again for permissions that have been previously granted and then removed.  
  
## Example extensions

  * [permissions](https://github.com/mdn/webextensions-examples/tree/master/permissions)

**Acknowledgements**

This API is based on Chromium's
[`chrome.permissions`](https://developer.chrome.com/extensions/permissions)
API.

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

