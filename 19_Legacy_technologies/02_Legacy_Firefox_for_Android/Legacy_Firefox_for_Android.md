[\n

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

\n

\n

This page, and its subpages, describe how to develop Firefox for Android add-
ons using legacy techniques. These techniques will stop working in Firefox 57.
You will still be able to use [WebExtensions](/en-US/docs/Mozilla/Add-
ons/WebExtensions) to develop add-ons for Firefox for Android.

\n

\n

Add-ons that work with desktop Firefox **do not** automatically work in
Firefox for Android:

\n

\n

  * There is no visible XUL in the UI, so you can't use an overlay to create the UI.
\n

  * Internal code and objects, like `gBrowser`, do not exist. Look at the Firefox on Android [`browser.js`](https://dxr.mozilla.org/mozilla-central/source/mobile/android/chrome/content/browser.js "http://mxr.mozilla.org/mozilla-central/source/mobile/android/chrome/content/browser.js") file to learn about the internals. Much of the same fundamental functionality exists.
\n

  * Services like `nsIPromptService` and `nsIAlertsService` are implemented to use native Android UI.
\n

  * There is a simple JavaScript object, called [`NativeWindow`](https://developer.mozilla.org/en/Extensions/Mobile/API/NativeWindow "en/Extensions/Mobile/NativeWindow"), that allows you to manipulate parts of the native Android UI.
\n

\n

The following articles provide help with developing extensions for Firefox on
Android. In addition, please refer to the [general extension documentation
](/en-US/Add-ons "En/Extensions") that applies to all Mozilla applications.

\n

\n

\n

### Tutorials

\n

\n[Prerequisites](/en-US/Add-ons/Firefox_for_Android/Prerequisites)

\n    Setting up your desktop to write addons and push them to device, and how
to test snippets from Desktop straight on your connected device.

\n[Debugging Firefox for Android with WebIDE](/en-
US/docs/Tools/Remote_Debugging/Debugging_Firefox_for_Android_with_WebIDE)

\n    Article from the Prerequisites tutorial, add-on debugging and snippet
testing is not possible without the WebIDE.

\n[Walkthrough](/en-US/Add-ons/Firefox_for_Android/Walkthrough)

\n    Developing, packaging and installing a simple add-on for Firefox for
Android.

\n[Firefox Hub Walkthrough](/en-US/Add-
ons/Firefox_for_Android/Firefox_Hub_Walkthrough)

\n    How to develop a Firefox Hub add-on to add content to the Firefox for
Android home page.

\n[Add-on SDK](/en-US/Add-ons/SDK/Tutorials/Mobile_development)

\n    How to develop Firefox for Android add-ons using the Add-on SDK.

\n\n

### Sample code

\n

\n[Code Snippets](/en-US/Add-ons/Firefox_for_Android/Code_snippets)

\n    Code samples for common tasks.

\n[Initialization and Cleanup](/en-US/Add-
ons/Firefox_for_Android/Initialization_and_Cleanup)

\n    How to initialize your add-on when it is started and clean up when it is
shut down.

\n[Firefox for Android Add-ons Github Repo](https://github.com/mozilla
/firefox-for-android-addons)

\n    A collection of JS modules, sample code, and boilerplate repos to help
you build add-ons for Firefox for Android.

\n\n

\n

\n

### API reference

\n

\n[NativeWindow](/en-US/Add-ons/Firefox_for_Android/API/NativeWindow)

\n    Create native Android UI widgets.

\n[BrowserApp](/en-US/Add-ons/Firefox_for_Android/API/BrowserApp)

\n    Access browser tabs and the web content they host.

\n[Prompt.jsm](/en-US/Add-ons/Firefox_for_Android/API/Prompt.jsm)

\n    Show native Android dialogs.

\n[HelperApps.jsm](/en-US/Add-ons/Firefox_for_Android/API/HelperApps.jsm)

\n    Query and launch native apps installed on the system.

\n[Notifications.jsm](/en-US/Add-
ons/Firefox_for_Android/API/Notifications.jsm)

\n    Use extended properties for Android system notifications.

\n[Home.jsm](/en-US/Add-ons/Firefox_for_Android/API/Home.jsm)

\n    Customize the home page.

\n[HomeProvider.jsm](/en-US/Add-ons/Firefox_for_Android/API/HomeProvider.jsm)

\n    Store data to display on the home page.

\n[PageActions.jsm](/en-US/Add-ons/Firefox_for_Android/API/PageActions.jsm)

\n    Display page-specific actions in the URL bar.

\n[JNI.jsm](/en-US/docs/Mozilla/JavaScript_code_modules/JNI.jsm)

\n    Tap into the native Java Android API from addons.

\n[Sound.jsm](/en-US/docs/Mozilla/Add-ons/Firefox_for_Android/API/Sound.jsm)

\n    Play sounds in the browser simply.

\n\n

\n

\n

\xa0

\n]

