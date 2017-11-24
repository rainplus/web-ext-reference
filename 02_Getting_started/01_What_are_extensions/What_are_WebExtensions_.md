[



Extensions are bits of code that modify the functionality of a web browser.
They are written using standard web technologies - JavaScript, HTML, and CSS -
plus some dedicated JavaScript APIs. Among other things, extensions can add
new features to the browser or change the appearance or content of particular
websites.



Extensions for Firefox are built using WebExtensions APIs, a cross-browser
system for developing extensions. To a large extent the API is compatible with
the [extension API](https://developer.chrome.com/extensions) supported by
Google Chrome and Opera. Extensions written for these browsers will in most
cases run in Firefox or Microsoft Edge with [just a few changes](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Porting_a_Google_Chrome_extension). The
API is also fully compatible with [multiprocess Firefox](/en-
US/Firefox/Multiprocess_Firefox).



In the past, you could develop Firefox extensions using one of three different
systems: [XUL/XPCOM overlays](/en-US/Add-ons/Overlay_Extensions),
[bootstrapped extensions](/en-US/docs/Mozilla/Add-
ons/Bootstrapped_extensions), or the [Add-on SDK](/en-US/docs/Mozilla/Add-
ons/SDK). By the end of November 2017, WebExtensions APIs will be the only way
to develop Firefox extensions, and the other systems will be deprecated.



If you have ideas or questions, or need help migrating a legacy add-on to
WebExtensions APIs, you can reach us on the [dev-addons mailing
list](https://mail.mozilla.org/listinfo/dev-addons) or in
[#extdev](irc://irc.mozilla.org/extdev) on
[IRC](https://wiki.mozilla.org/IRC).



## What's next?





  * To try out some example extensions, see [Example extensions](/en-US/Add-ons/WebExtensions/Examples).


  * To learn about the structure of an extension, see [Anatomy of an extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Anatomy_of_a_WebExtension).


  * To walk through the development of a simple extension, see [Your first extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension).


]

