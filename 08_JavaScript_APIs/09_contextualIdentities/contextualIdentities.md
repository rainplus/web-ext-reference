[



Work with contextual identities: list, create, remove, and update contextual
identities.



"Contextual identities", also known as "containers", are a browser feature
which addresses the idea that users assume multiple identities when browsing
the web, and wish to maintain some separation between these identities. For
example, a user might consider their "work identity" separate from their
"personal identity", and not want to share cookies between these two contexts.



With the contextual identities feature, each\xa0contextual identity has a
name, a color, and an icon. New tabs can be assigned to an identity, and the
name, icon, and color will appear in the address bar. Internally, each
identity gets its own cookie store which is not shared with other tabs.



![](https://mdn.mozillademos.org/files/14719/containers.png)Contextual
identities are an experimental feature in Firefox and are only enabled by
default in Firefox Nightly. To enable them in other versions of Firefox, set
the `privacy.userContext.enabled` preference to true. Note that although
contextual identities are available in Firefox for Android, there's no UI to
work with them in this version of the browser.



Before Firefox 57, the `contextualIdentities` API is only available if the
contextual identities feature is itself enabled. If an extension tried to use
the `contextualIdentities` API without the feature being enabled, then method
calls would resolve their promises with `false`.



From Firefox 57 onwards, if an extension that uses the `contextualIdentities`
API is installed, then the contextual identities feature will be enabled
automatically. Note though that it's still possible for the user to disable
the feature using the "privacy.userContext.enabled" preference. If this
happens, then\xa0`contextualIdentities` method calls will reject their
promises with an error message.



For more information about contextual identities in Firefox, see [this
guide](https://wiki.mozilla.org/Security/Contextual_Identity_Project/Containers).



Contextual identities are not currently supported in any other browsers.



To use this API you need to include the "contextualIdentities"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) in your
[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json) file.



## Types



[`contextualIdentities.ContextualIdentity`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/ContextualIdentity "The
contextualIdentities.ContextualIdentity type describes a single contextual
identity.")

    Contains information about a contextual identity.



## Functions



[`contextualIdentities.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/create "Creates a new contextual
identity. Once created, the user will be able to create new tabs belonging to
this contextual identity, just as they can with the built-in identities.")

    Creates a new contextual identity.

[`contextualIdentities.get()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/get "Gets information about a
contextual identity, given its cookie store ID.")

    Retrieves a single contextual identity, given its cookie store ID.

[`contextualIdentities.query()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/query "Gets information about all
contextual identities, or about those contextual identities that match a given
filter argument.")

    Retrieves all contextual identities, or all contextual identities with a
particular name.

[`contextualIdentities.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/update "Updates properties of a
contextual identity, given its cookie store ID.")

    Updates properties of an existing contextual identity.

[`contextualIdentities.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/remove "Removes a contextual
identity, given its cookie store ID.")

    Deletes a contextual identity.



## Events



[`contextualIdentities.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/onCreated "Fired when a new
contextual identity is created. Contextual identities may be created by
extensions using the contextualIdentities API, or directly by the user, using
the browser's user interface.")

    Fired when a contextual identity is created.

[`contextualIdentities.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/onRemoved "Fired when a new
contextual identity is removed. Contextual identities may be removed by
extensions using the contextualIdentities API, or directly by the user, using
the browser's user interface.")

    Fired when a contextual identity is removed.

[`contextualIdentities.onUpdated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/contextualIdentities/onUpdated "Fired when the
properties of a contextual identity, such as its name, icon, or color, are
changed. Contextual identities may be updated by extensions using the
contextualIdentities API, or directly by the user, using the browser's user
interface.")

    Fired when one or more properties of a contextual identity is updated.



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`create`|  No|  No| 53 *| 53 *|  No  
`get`|  No|  No| 53 *| 53 *|  No  
`onCreated`|  No|  No| 57| 57|  No  
`onRemoved`|  No|  No| 57| 57|  No  
`onUpdated`|  No|  No| 57| 57|  No  
`query`|  No|  No| 53 *| 53 *|  No  
`remove`|  No|  No| 53 *| 53 *|  No  
`update`|  No|  No| 53 *| 53 *|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`create`|  No support No| No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
|  No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.  
`get`|  No support No| No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
     Notes __Before version 57, this method resolves its promise with`null` if the given identity was not found.
|  No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
     Notes __Before version 57, this method resolves its promise with`null` if the given identity was not found.  
`onCreated`|  No support No| No support No| Full support 57|
No support No| Full support 57  
`onRemoved`| No support No| No support No| Full support 57|
No support No| Full support 57  
`onUpdated`| No support No| No support No| Full support 57|
No support No| Full support 57  
`query`| No support No| No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
|  No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.  
`remove`|  No support No| No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
     Notes __Before version 57, this method resolves its promise with`null` if the given identity was not found.
|  No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
     Notes __Before version 57, this method resolves its promise with`null` if the given identity was not found.  
`update`|  No support No| No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
     Notes __Before version 57, this method resolves its promise with`null` if the given identity was not found.
|  No support No| Full support 53

Notes __

Full support 53

Notes __

     Notes __Before version 57, this method resolves its promise with`false` if the contextual identities feature is disabled.
     Notes __Before version 57, this method resolves its promise with`null` if the given identity was not found.  
  
## Example extensions

  * [contextual-identities](https://github.com/mdn/webextensions-examples/tree/master/contextual-identities)

]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

