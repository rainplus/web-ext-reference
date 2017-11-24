[

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



This page contains links to documentation for the approach to developing
extensions for Gecko-based applications which uses:





  * XUL overlays to specify the interface


  * APIs available to privileged code, such as [`tabbrowser`](/en-US/docs/XUL/tabbrowser) and [JavaScript modules](/en-US/docs/Mozilla/JavaScript_code_modules), to interact with the application and content.




Prior to Firefox 4, and the Gecko 2 engine that powers it, this was the only
way to develop extensions. This methodology has largely been superseded by
[restartless extensions](/en-US/docs/Extensions/Bootstrapped_extensions), and
the [Add-on SDK](/en-US/Add-ons/SDK), which is built on top of them. The
privileged JavaScript APIs described here can still be used in these newer
types of add-ons.



## XUL School



[XUL School](/en-US/Add-ons/Overlay_Extensions/XUL_School) is a comprehensive
add-on development tutorial, focusing on Firefox extension development but
mostly applicable to other Gecko-based applications.



## More resources







[Setting up your environment](/en-US/Mozilla/Add-
ons/Setting_up_extension_development_environment)

    Setting up the application for extension development.

[XUL](/en-US/docs/XUL)

    Tutorials and reference for the user interface language used by XUL
extensions.

[Code snippets](/en-US/Mozilla/Add-ons/Code_snippets)

    Sample code for many of the things you'll want to do.

[Installing extensions](/en-US/Mozilla/Add-ons/Installing_extensions)

    How to install an extension by copying the extension files into the
application's install directory.

[Firefox add-ons developer guide](/en-US/Add-
ons/Overlay_extensions/Firefox_addons_developer_guide)

    A guide to developing overlay extensions.







[JavaScript code modules](/en-US/docs/Mozilla/JavaScript_code_modules)

    JavaScript modules available to extension developers.

[Extension preferences](/en-US/Mozilla/Add-ons/Inline_Options)

    How to specify the preferences for your extension that will appear in
the Add-ons Manager.

[Extension packaging](/en-US/Mozilla/Add-ons/Extension_Packaging)

    How extensions are packaged and installed.

[Binary Firefox extensions](/en-US/Mozilla/Add-
ons/Creating_Custom_Firefox_Extensions_with_the_Mozilla_Build_System)

    Creating binary extensions for Firefox.







\xa0

]

