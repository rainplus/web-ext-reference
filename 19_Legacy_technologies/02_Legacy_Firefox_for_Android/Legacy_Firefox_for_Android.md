Add-ons using the techniques described in this document are considered a
legacy technology in Firefox. Don't use these techniques to develop new add-
ons. Use [WebExtensions](/en-US/Add-ons/WebExtensions) instead. If you
maintain an add-on which uses the techniques described here, consider
migrating it to use WebExtensions.

 **Starting from[Firefox 53](https://wiki.mozilla.org/RapidRelease/Calendar),
no new legacy add-ons will be accepted on addons.mozilla.org (AMO) for desktop
Firefox and Firefox for Android.**

 **Starting from[Firefox 57](https://wiki.mozilla.org/RapidRelease/Calendar),
only extensions developed using WebExtensions APIs will be supported on
Desktop Firefox and Firefox for Android. **

Even before Firefox 57, changes coming up in the Firefox platform will break
many legacy extensions. These changes include multiprocess Firefox (e10s),
sandboxing, and multiple content processes. Legacy extensions that are
affected by these changes should migrate to use WebExtensions APIs if they
can. See the ["Compatibility Milestones"
document](https://blog.mozilla.org/addons/2017/02/16/the-road-to-firefox-57
-compatibility-milestones/) for more information.

A wiki page containing [resources, migration paths, office hours, and
more](https://wiki.mozilla.org/Add-ons/developer/communication), is available
to help developers transition to the new technologies.

This page, and its subpages, describe how to develop Firefox for Android add-
ons using legacy techniques. These techniques will stop working in Firefox 57.
You will still be able to use [WebExtensions](/en-US/docs/Mozilla/Add-
ons/WebExtensions) to develop add-ons for Firefox for Android.

Add-ons that work with desktop Firefox **do not** automatically work in
Firefox for Android:

  * There is no visible XUL in the UI, so you can't use an overlay to create the UI.
  * Internal code and objects, like `gBrowser`, do not exist. Look at the Firefox on Android [`browser.js`](https://dxr.mozilla.org/mozilla-central/source/mobile/android/chrome/content/browser.js "http://mxr.mozilla.org/mozilla-central/source/mobile/android/chrome/content/browser.js") file to learn about the internals. Much of the same fundamental functionality exists.
  * Services like `nsIPromptService` and `nsIAlertsService` are implemented to use native Android UI.
  * There is a simple JavaScript object, called [`NativeWindow`](https://developer.mozilla.org/en/Extensions/Mobile/API/NativeWindow "en/Extensions/Mobile/NativeWindow"), that allows you to manipulate parts of the native Android UI.

The following articles provide help with developing extensions for Firefox on
Android. In addition, please refer to the [general extension documentation
](/en-US/Add-ons "En/Extensions") that applies to all Mozilla applications.

### Tutorials

[Prerequisites](/en-US/Add-ons/Firefox_for_Android/Prerequisites)

    Setting up your desktop to write addons and push them to device, and how to test snippets from Desktop straight on your connected device.
[Debugging Firefox for Android with WebIDE](/en-
US/docs/Tools/Remote_Debugging/Debugging_Firefox_for_Android_with_WebIDE)

    Article from the Prerequisites tutorial, add-on debugging and snippet testing is not possible without the WebIDE.
[Walkthrough](/en-US/Add-ons/Firefox_for_Android/Walkthrough)

    Developing, packaging and installing a simple add-on for Firefox for Android.
[Firefox Hub Walkthrough](/en-US/Add-
ons/Firefox_for_Android/Firefox_Hub_Walkthrough)

    How to develop a Firefox Hub add-on to add content to the Firefox for Android home page.
[Add-on SDK](/en-US/Add-ons/SDK/Tutorials/Mobile_development)

    How to develop Firefox for Android add-ons using the Add-on SDK.

### Sample code

[Code Snippets](/en-US/Add-ons/Firefox_for_Android/Code_snippets)

    Code samples for common tasks.
[Initialization and Cleanup](/en-US/Add-
ons/Firefox_for_Android/Initialization_and_Cleanup)

    How to initialize your add-on when it is started and clean up when it is shut down.
[Firefox for Android Add-ons Github Repo](https://github.com/mozilla/firefox-
for-android-addons)

    A collection of JS modules, sample code, and boilerplate repos to help you build add-ons for Firefox for Android.

### API reference

[NativeWindow](/en-US/Add-ons/Firefox_for_Android/API/NativeWindow)

    Create native Android UI widgets.
[BrowserApp](/en-US/Add-ons/Firefox_for_Android/API/BrowserApp)

    Access browser tabs and the web content they host.
[Prompt.jsm](/en-US/Add-ons/Firefox_for_Android/API/Prompt.jsm)

    Show native Android dialogs.
[HelperApps.jsm](/en-US/Add-ons/Firefox_for_Android/API/HelperApps.jsm)

    Query and launch native apps installed on the system.
[Notifications.jsm](/en-US/Add-ons/Firefox_for_Android/API/Notifications.jsm)

    Use extended properties for Android system notifications.
[Home.jsm](/en-US/Add-ons/Firefox_for_Android/API/Home.jsm)

    Customize the home page.
[HomeProvider.jsm](/en-US/Add-ons/Firefox_for_Android/API/HomeProvider.jsm)

    Store data to display on the home page.
[PageActions.jsm](/en-US/Add-ons/Firefox_for_Android/API/PageActions.jsm)

    Display page-specific actions in the URL bar.
[JNI.jsm](/en-US/docs/Mozilla/JavaScript_code_modules/JNI.jsm)

    Tap into the native Java Android API from addons.
[Sound.jsm](/en-US/docs/Mozilla/Add-ons/Firefox_for_Android/API/Sound.jsm)

    Play sounds in the browser simply.



