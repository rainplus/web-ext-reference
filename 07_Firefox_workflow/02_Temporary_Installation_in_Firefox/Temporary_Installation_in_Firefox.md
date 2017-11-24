[





This article describes how an add-on developer can temporarily install an
extension in Firefox for testing and debugging. The extension will stay
installed until you restart Firefox. You can use this method with any kind of
restartless extension, including [bootstrapped extensions](/en-US/docs/Mozilla
/Add-ons/Bootstrapped_extensions) and [Add-on SDK add-ons](/en-US/docs/Mozilla
/Add-ons/SDK).



Note that this is _not_ how end users should install add-ons in Firefox. End
users will install add-ons by downloading and opening packaged add-ons that
have been signed by Mozilla. To learn how an extension developer can get an
add-on packaged and signed, see [Publishing your extension](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Publishing_your_WebExtension).





To install an extension temporarily:





  * open Firefox


  * enter "about:debugging" in the URL bar


  * click "Load Temporary Add-on"


  * open the extension's directory and select any file inside the extension.




The extension will be installed, and will stay installed until you restart
Firefox.





## Reloading a temporary extension



Starting in Firefox 48, there's a new button labeled "Reload" next to the
extension's entry in about:debugging:



![](https://mdn.mozillademos.org/files/13462/reload.png)This does what it
says:





  * reloading any persistent scripts, such as [background scripts](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts)


  * parsing the manifest.json file again, so changes to `[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)`, `[content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)`, `[browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)` or any other keys will take effect.








Note that in Firefox 48 only, "Reload" does not update the extension's name
and description that are displayed in about:debugging and about:addons. This
is fixed in Firefox 49.





## Using the command line



If you are already using the command line for development, check out the [web-
ext](/en-US/Add-ons/WebExtensions/Getting_started_with_web-ext) tool. It
automates the temporary installation step and automatically reloads your
extension when its source code changes.



## Detecting temporary installation



Your extension can detect whether it was installed from about:debugging rather
than as a built and signed extension downloaded from addons.mozilla.org.
Listen for the [`runtime.onInstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onInstalled "Fired when the extension is first
installed, when the extension is updated to a new version, and when the
browser is updated to a new version.") event, and check the value of
`details.temporary`.

]

