[





Firefox add-ons contain a unique ID which is used to distinguish this add-on
from any other Firefox add-on.



This article describes how add-on IDs are handled for extensions that are
built with WebExtensions APIs.





Firefox add-ons contain a unique identifier which is used both inside Firefox
itself and on the [addons.mozilla.org](https://addons.mozilla.org/) (AMO)
website. For example, it's used by Firefox to check for updates to installed
add-ons and to identify which objects (such as data stores) are controlled by
this add-on.



With older types of Firefox add-on, the add-on developer must set the add-on
ID explicitly. XUL/XPCOM add-ons set the ID in the [install manifest](/en-
US/docs/Mozilla/Add-ons/Install_Manifests), while SDK add-ons set it in the
[package.json](/en-US/docs/Mozilla/Add-ons/SDK/Tools/package_json).



However, from Firefox 48 you can develop, debug, publish, and update
extensions without needing to set an explicit ID at all.





Note that the ability to develop and debug WebExtensions that don't include an
ID is new in Firefox 48. If you need to use an earlier version of Firefox,
then you must use the `[applications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/applications)` key to set an ID explicitly.





## Basic workflow with no add-on ID



Extensions can explicitly set the add-on ID using the `[applications](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications)` key in
manifest.json. However, this key is usually optional. If you don't set it,
then you can usually develop, debug, publish, and update your extension
without ever having to deal with an ID. One advantage of this is that Google
Chrome does not recognize the `applications` key and will show a warning if
you include it.



Note, though, that some WebExtension APIs use the add-on ID and expect it to
be the same from one browser session to the next. If you use these APIs in
Firefox, then you must set the ID explicitly using the `[applications](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications)` key. See
[When do you need an Add-on ID?](/en-US/Add-ons/WebExtensions
/WebExtensions_and_the_Add-on_ID#When_do_you_need_an_add-on_ID).



### Developing and debugging



Starting in Firefox 48, if your manifest.json does not contain an ID then the
extension will be assigned a randomly-generated temporary ID when you [install
it in Firefox](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)
through about:debugging. If you then reload the extension using the "Reload"
button, the same ID will be used. If you then restart Firefox and load the
add-on again, it will get a new ID.



If you turn the extension into an .xpi or .zip and install it through
about:addons, it will not work. To have it work in this scenario, you will
need to add in the `[applications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/applications)` key in manifest.json



### Publishing



Once you have finished developing the extension, you can [package it and
submit it to AMO for review and signing](/en-US/Add-
ons/WebExtensions/Publishing_your_WebExtension). If the packaged extension you
upload does not contain an ID, AMO will generate one for you. It's only at
this point that the add-on will be assigned a permanent ID, which will be
embedded in the signed packaged extension.



Note that once an extension has been given a permanent ID, you can't then
update it to use the Add-on SDK or legacy XUL/XPCOM techniques. If you do
switch to one of these platforms, you must submit it as a distinct new add-on,
with a new ID.



### Updating



Even after this point, though, you don't generally have to deal with the ID at
all. You can continue to develop the add-on without an ID, and when you want
to update, upload the new version by visiting the add-on's AMO page. Because
you are uploading the add-on through that page, AMO knows that this is an
update to this particular add-on, even though it doesn't contain an ID.





It's essential with this workflow that you update the add-on _manually using
its page on AMO_ , otherwise AMO will not understand that the submission is an
update to an existing add-on, and will treat the update as a brand-new add-on.





You can do the same thing if you are updating from an older add-on type, such
as a XUL/XPCOM add-on, to use WebExtensions APIs. Just visit the old add-on's
page on AMO, upload the new extension there, and it will be treated as an
update to the old version.



## When do you need an add-on ID?





  * If you are loading the add-on from it's XPI file, are not loading it temporarily using about:debugging and it is not signed.


  * If you use [AMO's API](https://addons-server.readthedocs.io/en/latest/topics/api/signing.html) for uploading your add-on, rather than uploading it manually on its page, then you need to include the add-on's ID in the request.


  * Some WebExtension APIs use the add-on ID and expect it to be the same from one browser session to the next. If you use these APIs, then you must set the ID explicitly using the `[applications](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications)` key. This applies to the following APIs: 
    * [`storage.managed`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/managed "A storage.StorageArea object that represents the managed storage area. Items in managed storage are set by the domain administrator or other native applications installed on user's computer, and are read-only for the extension. Trying to modify this storage area results in an error.")


    * [`storage.sync`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/sync "Represents the sync storage area. Items in sync storage are synced by the browser, and are available across all instances of that browser that the user is logged into \(e.g. via Firefox sync, or a Google account\), across different devices.")


    * [`identity.getRedirectURL`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity/getRedirectURL "Generates a URL that you can use as a redirect URL.")


    * [Native messaging](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_messaging)




  * Using Firefox for Android. See [applications in manifest.json](/en-US/Add-ons/WebExtensions/manifest.json/applications).




\xa0



\xa0



\xa0

]

