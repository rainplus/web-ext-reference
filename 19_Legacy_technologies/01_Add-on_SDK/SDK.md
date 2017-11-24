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



Using the Add-on SDK, you can create Firefox add-ons. You can use
various\xa0standard Web technologies: JavaScript, HTML, and CSS, to create the
add-ons. The SDK includes JavaScript APIs, which you can use to create add-
ons\xa0and tools for creating, running, testing, and packaging add-ons.



* * *



### [Tutorials](/en-US/Add-ons/SDK/Tutorials)







[Getting started](/en-US/Add-ons/SDK/Tutorials#getting-started)

    How to [install the SDK](/en-US/Add-ons/SDK/Tutorials/Installation) and
[use the jpm tool](/en-US/Add-ons/SDK/Tutorials/Getting_Started_\(jpm\)) to
develop, test, and package add-ons.

[Interact with the browser](/en-US/Add-ons/SDK/Tutorials#interact-with-the-
browser)

    [Open web pages](/en-US/Add-ons/SDK/Tutorials/Open_a_Web_Page), [listen
for pages loading](/en-US/Add-ons/SDK/Tutorials/Listen_For_Page_Load)\xa0and
[list open pages](/en-US/Add-ons/SDK/Tutorials/List_Open_Tabs).

[Development techniques](/en-US/Add-ons/SDK/Tutorials#development-
techniques)

    Learn about common development techniques, such as [unit testing](/en-US
/Add-ons/SDK/Tutorials/Unit_testing), [logging](/en-US/Add-
ons/SDK/Tutorials/Logging), [creating reusable modules](/en-US/Add-
ons/SDK/Tutorials/Creating_Reusable_Modules), [localization](/en-US/Add-
ons/SDK/Tutorials/l10n), and [mobile development](/en-US/Add-
ons/SDK/Tutorials/Mobile_development).







[Create user interface components](/en-US/Add-ons/SDK/Tutorials#create-user-
interfaces)

    Create user interface components such as [toolbar buttons](/en-US/Add-
ons/SDK/Tutorials/Adding_a_Button_to_the_Toolbar), [context menus](/en-US/Add-
ons/SDK/Tutorials/Add_a_Context_Menu_Item), [menu items](/en-US/Add-
ons/SDK/Tutorials/Add_a_Menu_Item_to_Firefox), and [dialogs](/en-US/Add-
ons/SDK/Tutorials/Display_a_Popup).

[Modify web pages](/en-US/Add-ons/SDK/Tutorials#modify-web-pages)

    Modify pages [matching a URL pattern](/en-US/Add-
ons/SDK/Tutorials/Modifying_Web_Pages_Based_on_URL) or dynamically [modify a
particular tab](/en-US/Add-
ons/SDK/Tutorials/Modifying_the_Page_Hosted_by_a_Tab).

[Putting it together](/en-US/Add-ons/SDK/Tutorials/Annotator)

    Walkthrough of the Annotator example add-on.







* * *



### Guides







[Contributor's guide](/en-US/Add-ons/SDK/Guides#contributors-guide)

    Learn [how to start contributing](/en-US/Add-
ons/SDK/Guides/Getting_Started) to the SDK\xa0and about the most important
idioms used in the SDK code\xa0such as [modules](/en-US/Add-
ons/SDK/Guides/Modules), [classes and inheritance](/en-US/Add-
ons/SDK/Guides/Classes_and_Inheritance), [private properties](/en-US/Add-
ons/SDK/Guides/Private_Properties), and [content processes](/en-US/Add-
ons/SDK/Guides/Content_Processes).

[SDK infrastructure](/en-US/Add-ons/SDK/Guides#sdk-infrastructure)

    Aspects of the SDK's underlying technology: [modules](/en-US/Add-
ons/SDK/Guides/Module_structure_of_the_SDK), the [Program ID](/en-US/Add-
ons/SDK/Guides/Program_ID)\xa0and the rules defining [Firefox compatibility
](/en-US/Add-ons/SDK/Guides/Firefox_Compatibility).

[Content scripts](/en-US/Add-ons/SDK/Guides/Content_Scripts)

    A detailed guide to working\xa0with content scripts.







[SDK idioms](/en-US/Add-ons/SDK/Guides#sdk-idioms)

    The SDK's [event framework](/en-US/Add-
ons/SDK/Guides/Working_with_Events) and the [distinction between add-on
scripts and content scripts](/en-US/Add-ons/SDK/Guides/Two_Types_of_Scripts).

[XUL migration](/en-US/Add-ons/SDK/Guides/XUL_Migration_Guide)

    A guide to [porting XUL add-ons to the SDK](/en-US/Add-
ons/SDK/Guides/XUL_Migration_Guide). This guide includes a [comparison of the
two toolsets](/en-US/Add-ons/SDK/Guides/XUL_vs_SDK) and a [working example
](/en-US/Add-ons/SDK/Guides/Porting_the_Library_Detector) of porting a XUL
add-on.

[Multiprocess Firefox and the SDK](/en-US/Add-
ons/SDK/Guides/Multiprocess_Firefox_and_the_SDK)

    How to check whether your add-on is compatible with multiprocess Firefox
or not and fix it accordingly.







* * *



### Reference







[High-Level APIs](/en-US/Add-ons/SDK/High-Level_APIs)

    Reference documentation for the high-level SDK APIs.

[Tools reference](/en-US/Add-ons/SDK/Tools)

    Reference documentation for the [jpm tool](/en-US/Add-ons/SDK/Tools/jpm)
used to develop, test\xa0and package add-ons, the [console](/en-US/Add-
ons/SDK/Tools/console) global used for logging, and the [package.json](/en-US
/Add-ons/SDK/Tools/package_json) file.







[Low-Level APIs](/en-US/Add-ons/SDK/Low-Level_APIs)

    Reference documentation for the low-level SDK APIs.







\xa0



* * *







## Join the Add-on SDK community





Choose your preferred method for joining the discussion:





  * [Mailing list](https://mail.mozilla.org/listinfo/dev-addons)


  * [ Twitter](https://twitter.com/mozillajetpack)


  * [ Stack Overflow](http://stackoverflow.com/questions/tagged/firefox-addon-sdk)


  * [Newsgroup](http://groups.google.com/group/https://groups.google.com/forum/?fromgroups#!forum/mozilla-labs-jetpack)


  * [RSS feed](http://groups.google.com/group/https://groups.google.com/forum/?fromgroups#!forum/mozilla-labs-jetpack/feeds)








  *  **IRC:**[#jetpack](irc://irc.mozilla.org/jetpack) ([learn more](https://wiki.mozilla.org/IRC))
  *  **Team info:**[Jetpack Wiki](https://wiki.mozilla.org/Jetpack "Designs and plans for the SDK tools")







]

