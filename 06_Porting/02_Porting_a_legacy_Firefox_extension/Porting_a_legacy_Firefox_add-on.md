[



If you have developed a Firefox extension using XUL/XPCOM or the Add-on SDK,
this page will help you migrate your extension to use WebExtensions APIs. The
standard to build extensions for Firefox is to
use[WebExtensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions)
APIs. It will be the only type of extension supported in Firefox by the end of
November 2017 with the release of [Firefox
57](https://wiki.mozilla.org/RapidRelease/Calendar).



## Quick start





  1. Get an idea of the main things you'll have to change in your extension: 
    * Familiarize yourself with the [WebExtension format and structure](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension), and [build a basic example](/en-US/Add-ons/WebExtensions/Your_first_WebExtension).


    * If your extension is based on XUL and XPCOM, whether it's an [overlay extension](https://developer.mozilla.org/en-US/Add-ons/Overlay_Extensions) or a [bootstrapped extension](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/Bootstrapped_extensions), see [Comparison with XUL/XPCOM extensions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions) to find out how WebExtensions can correspond with the legacy APIs you're using.


    * If your extension is based on the Add-on SDK, see [Comparison with the Add-on SDK](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK) to find out how WebExtensions can correspond with the legacy SDK APIs you're using.




  2. Rewrite your extension code. See below for migration paths for different types of extensions. From Firefox 51 onwards, you can embed an extension built using WebExtension APIs in a bootstrapped extension or an SDK add-on, and can thus port a legacy extension a piece at a time, and have a working extension at each step. See [Embedded WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Embedded_WebExtensions) for more information.


  3. When you're ready to submit the WebExtension version of your extension to AMO... wait a minute... are you truly ready? Because of the extensions permissions model, you cannot revert from WebExtensions back to using a legacy extension format. So test _thoroughly_ , because this is a permanent one-way trip. Also, see the hybrid example below. If you're not ready, you can embed your WebExtension in a legacy extension container, which allows you to test your extension migration but still go back if needed in an emergency.


  4. When you're _really_ ready to submit the WebExtension version of your extension to AMO, first port your old add-on ID to the new WebExtension manifest.json file. Your extension must have the same ID as previous versions. Copy the value in the "id" field from your package.json file into the id field in the [applications](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications) section of the WebExtension manifest.json file. Then you can submit your extension update to AMO as your normally would.






Note that this is a one-way conversion: You **cannot** update an extension
using WebExtensions to use a legacy technology. This means that you must be
sure that you are ready to commit to using WebExtension APIs before you submit
the updated add-on to AMO.





## Migration paths



###  
 SDK Extensions



Here is the comparison chart showing [SDK APIs and their WebExtensions format
counterparts](https://developer.mozilla.org/en-US/Add-ons/WebExtensions
/Comparison_with_the_Add-on_SDK). If you don't see the APIs you need to port
to use WebExtensions APIs, look below to learn how to request APIs and also
how to implement them.



### XUL/XPCOM Extensions



Here is the comparison chart showing [XUL/XPCOM APIs and their WebExtensions
format counterparts](/en-US/Add-
ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions). If you don't see the
APIs you need to port to use WebExtension APIs, look below to learn how to
request APIs and also how to implement them.



### Partial migration



An [Embedded WebExtension](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Embedded_WebExtensions) is an extension that combines two
types of extensions in one, by incorporating a WebExtension inside of a
bootstrapped or SDK extension. If you have a legacy extension that writes data
to the filesystem, and you\u2019re planning to port it to WebExtensions,
[Embedded WebExtensions](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Embedded_WebExtensions) are available to help you
transition. Embedded WebExtensions can be used to transfer the stored data of
your add-on to a format that can be used by WebExtensions. This is essential
because it lets you to convert your users without the need for them to take
any actions.



It\u2019s important to emphasize that Embedded WebExtensions are intended to
be a transition tool, and will not be supported past Firefox 57. They should
not be used for add-ons that are not expected to transition to WebExtensions.



## Don't see the WebExtensions APIs you need?



 **Develop WebExtension APIs for Firefox** \- If you're experienced with
Mozilla infrastructure and would like to develop WebExtensions APIs directly
for Firefox, here is a list of [approved APIs](https://mzl.la/2dVs5Ys) that
you can start contributing to.



 **Experiment with new WebExtension APIs** \- If you want to prototype and
tinker with WebExtensions APIs without having to build Firefox, [WebExtensions
Experiments](http://webextensions-
experiments.readthedocs.io/en/latest/index.html) is for you!



 **Request a new WebExtensions API** \- If you want to request a new
WebExtensions API, please read [this
page](https://wiki.mozilla.org/WebExtensions/NewAPIs).



## Tools





  * [web-ext](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext) is a command line tool designed to speed up various parts of the extension development process, making development faster and easier.


  * [Lookup tool](https://compatibility-lookup.services.mozilla.com/) to check your add-on type and get porting resource recommendations


  * [WebExtensions Helper](https://github.com/mi-g/weh) speeds up browser extension development by providing utilities for WebExtensions-based (Firefox, Chrome, Opera and Edge) extensions


  * [Chrome Extension generator ](https://github.com/yeoman/generator-chrome-extension)creates everything you need to get started with extension development. You can choose Browser UI(Browser,Page Action, Omnibox) type and select permissions you need.


  * [Extensionizr](http://extensionizr.com/) is a wizard that helps you create a basic extension


  * [Chrome Boilerplate](https://github.com/mahemoff/chrome-boilerplate) is boilerplate code for Chrome WebExtension.


  * [Skeleton Chrome Extension](https://github.com/sitepoint/ChromeSkel_a) is an extension bootstrap and template




## Documentation





  * [WebExtensions Project Page](https://wiki.mozilla.org/Add-ons/developer/communication) on the Mozilla Wiki


  * [How-to guides](https://developer.mozilla.org/en-US/Add-ons/WebExtensions) covering common extension developer cases, like [intercepting web requests](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Intercept_HTTP_requests) and [adding a button to the toolbar](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Add_a_button_to_the_toolbar)


  * [Comparison with the Add-on SDK](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK)


  * [Comparison with XUL/XPCOM extensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions)


  * [Browser compatibility table](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs) for all WebExtensions APIs


  * [Examples of extensions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Examples)




## Contact





  * 

You can use the links [here](https://developer.mozilla.org/en-US/Add-
ons#Contact_us) to get help, keep up to date with news around add-ons, and
give us feedback.





]

