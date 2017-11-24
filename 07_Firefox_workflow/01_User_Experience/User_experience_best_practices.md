[\n

\n

The best Firefox extensions provide users with a new feature or capability
that addresses a need. Addressing this need will help users work smarter or
more efficiently, or get more pleasure out of their browsing experience.

\n

You will also want to make sure your users have a great experience using your
extension and as a result give it great feedback and a good rating on
addons.mozilla.org (AMO).

\n

Much has been written about what makes software usable. If you are new to the
subject, a good place to start is Jakob Nielsen\u2019s [Usability
Heuristics](https://en.wikipedia.org/wiki/Heuristic_evaluation#Nielsen). We
recommend, whether you are new to extension development or a seasoned pro,
using Nielsen\u2019s Heuristics as a checklist when testing your user
experience (UX).

\n

So, here we discuss much more specific Firefox and browser extension UX
features, offering advice and suggestions that will help you build an
extension that delights your users.

\n

## Be Firefoxy

\n

Your users have chosen Firefox for a reason, possibly several reasons, so
match your extension\u2019s philosophy, features, and look and feel to that of
Firefox.

\n

### Design values

\n

To best meet the needs of Firefox users, align with the Firefox values.

\n

The [Firefox Design Values](http://design.firefox.com/values/) state that we
respect the user's privacy and sovereignty and do not surprise them. We start
users with smart defaults on the functionality they want to use and enable
them to customize those to their personal preferences so that they are in full
control of their experience. We add humor and whimsy to our design and pay
attention to details, quality, and performance. Local differences in a global
world are important to us, and we help people make sense of the web in clear
language.

\n

### Look and feel

\n

To provide your extensions with the best long term fit to Firefox, align with
the [Firefox Photon Design System](http://design.firefox.com/photon).
Following Photon will ensure that your extension integrates with the Firefox
experience and will make it easier for people to use.

\n

## Keep it focused

\n

An extension is best when it is centered around one main use case, addressing
that use case as well as possible for the target audience. It should add one
function or set of closely related functions to the browser, modify a function
of the browser, or modify web pages. Judge if you have achieved this by asking
whether you can easily communicate the features and purpose of the extension
in three (short) sentences or less.

\n

\n

A short summary description of your extension is also very useful when it
comes to creating its listing on AMO, see [Make sure your summary is just long
enough](/en-US/Add-ons/Listing#Make_sure_your_summary_is_just_long_enough) for
more details.

\n

\n

## Get started right away

\n

Ensure that your extension is ready to be used immediately after installation.
It should be optimized for its main use case, and work as expected for most
users without the need for customization.

\n

Do not expect your users to read detailed instructions, other content, or ask
them to configure the extension to use it. Doing so could mean they never get
started with your extension and, if they do, could result in poor reviews.

\n

## Give users what they need, where they need it

\n

Choosing the right way or combination of ways to make your extension's
functionality available to the user can have a significant impact on
usability. Asking a few simple questions about your extension\u2019s
functionality can quickly guide you to the right choices:

\n

### Does my extension work on most websites and web pages?

\n

If your extension provides the user with features they can use on almost every
website or page, give the user access to it from a [toolbar
button](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/user_interface/Browser_action) using the [browser
action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction). This might include providing access to
your image editor or opening a page from your website.

\n

![](https://mdn.mozillademos.org/files/12966/browser-action.png)

\n

Where you have several features you want to give the user access to, you can
add a [popup](/en-US/Add-ons/WebExtensions/Popups) to the button.

\n

### Does my extension work for only some web sites and pages?

\n

If your extension offers a feature for a type of web page or specific domains,
give the user access to it from an [address bar button](/en-US/docs/Mozilla
/Add-ons/WebExtensions/user_interface/Page_actions) using a [page action](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction). This might include
providing access to your RSS reader on pages with RSS feeds or providing an
extended feature to pages on your website.

\n

![](https://mdn.mozillademos.org/files/12960/page-action.png)

\n

Where you have several features you want to give the user access to, you can
add a [popup](/en-US/Add-ons/WebExtensions/Popups) to the button.

\n

### Does my extension need to show information or offer actions in parallel
with web pages?

\n

If your extension includes information or actions that a user would want
immediate access to while viewing any web page, use a [sidebar](/en-
US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars). This might
include notes the user can make about a page\u2019s content or a feature
offering various font substitutions to improve readability.

\n

\ufeff\ufeff![](https://mdn.mozillademos.org/files/14825/bookmarks-
sidebar.png)

\n

### Does my extension offer functionality specific to page content or other
browser features?

\n

If your extension offers features the user might want to access in context,
add them to an appropriate [context menu](/en-US/Add-
ons/WebExtensions/user_interface/Context_menu_items). This might include
offering access to an image editor on the image context menu or offering
extended copy features on the context menu for selected page content.

\n

![Example of content menu items added by a WebExtension, from the context-
menu-demo
example](https://mdn.mozillademos.org/files/15051/context_menu_example.png)

\n

### Does my extension have settings the user can adjust?

\n

If your extension enables the user to change and save settings that affect the
behavior of the extension, use an [options page](/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Options_pages) to provide a standard
Preferences link to settings from the Add-on Manager.

\n

![Typical preferences button, to access an extension's settings, from the Add-
on Manager](https://mdn.mozillademos.org/files/15271/add-on-manager-
preferences-button.png)

\n

### Does my extension need to gather a lot of information or display content
in addition to the current tabs?

\n

Where your extension needs to gather or display significant amounts of
information (more than is suitable for an [alert](/en-
US/docs/Web/API/Window/alert) or would benefit from additional formatting) use
[bundled web pages](/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Bundled_web_pages) to deliver forms and
similar content.

\n

![Example of a simple bundled page displayed as a detached
panel.](https://mdn.mozillademos.org/files/15073/bundled_page_as_panel.png)

\n

### Does my extension try to help the user find web pages or content?

\n

Where your extension includes a use case to locate web pages or content, for
example, offering a site specific search, use [address bar suggestions](/en-
US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Omnibox) to deliver those
recommendations.

\n

![Example showing the result of the firefox_code_search WebExtension's
customization of the address bar
suggestions.](https://mdn.mozillademos.org/files/15075/omnibox_example_full.png)

\n

### Does my extension offer tools for developers?

\n

Where you are providing tools for developers, add them to the Firefox
developer tools using [developer tools panels](/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/devtools_panels).

\n

## Keep the user informed

\n

Ensuring the user knows what will happen, is happening, and has happened in
your extension is an essential part of building trust and ensuring a happy
user.

\n

### Tell the user what will happen, before it happens

\n

Users should understand what will happen when they click a button. In addition
to a meaningful, descriptive button label, provide tooltips that describe the
action that the button will perform.

\n

\n

Do not put the name of the extension alone in the tooltip, unless it is
descriptive of the action the button will perform.

\n

\n

Also, do not use the tooltip for any other types of information such as
elaborate statistics about your extension. Keep the tooltip content simple and
focused on what will happen when the user clicks the button.

\n

### If it is really important and the user has wandered away, notify them

\n

If your extension has completed a critical, long running background task, when
the task completes use the operating system\u2019s native [notifications](/en-
US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Notifications) to update
the user. This can be useful where the user may not be focusing on the
extension, or the browser, when the process finishes. However, use sparingly.
If it is sufficient for the user to discover that a process has completed when
they return to the browser or extension, do not use notifications.

\n

![](https://mdn.mozillademos.org/files/14043/notify-shadowed.png)

\n

### Use browserAction badges sparingly

\n

You can [add a badge](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setBadgeText) over the toolbar icon of a
browserAction, but do so sparingly to inform users about important events. Do
not use them to provide regular or persistent status updates.

\n

When it comes to [coloring a badge](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/browserAction/setBadgeBackgroundColor), using one of
four colors for notifications of different severity is recommended:

\n

\n

  * Casual: blue
\n

  * Success: green
\n

  * Error: yellow
\n

  * Warning: red
\n

\n

\n

Use of Firefox colors is suggested, for more details see [Firefox
Colors](http://design.firefox.com/photon/visual/color.html). However, for
compatibility with
[Chrome](https://developer.chrome.com/extensions/browserAction#icon) and Opera
free color selection is supported.

\n

\n

## Test, test, and then test again

\n

Testing is a vital part of creating an outstanding UX for your extension.
There are two key aspects of testing your UX:

\n

\n

  1. Test across devices and platforms to ensure your extension works and performs well in as many places as possible. This includes considering factors such as the user\u2019s screen size and resolution\u2014just because your extension looks good and is easy to use on your desktop monitor does not mean it looks as good and works as well on a smaller laptop screen, or, indeed, vice versa.
\n

  2. Test with as many users as possible. Do not assume that you know your audience, as people\u2019s backgrounds and experience can make a huge difference to how they interact with your extension. So, allow for user testing as part of your extension\u2019s development.
\n

\n

Testing tips:

\n

\n

  * In AMO you have the option to [identify your extension as experimental](/en-US/Add-ons/Distribution/Submitting_an_add-on#Listing_on_AMO) or publish a [beta or other non-final release](/en-US/Add-ons/Distribution#Beta_versions). If you flag your extension as experimental it is listed in AMO, so that any user can find it, but with a lower profile. Once you are happy that the extension is ready for a wider audience, you can turn off the experimental flag and your extension will be listed as normal in AMO. If you have a published extension, you can use the Development channel to offer an alpha or beta version for testing. You will need to direct your testers to the Development Channel of your extension\u2019s listing or let your testers know the link to use to install your extension.  
\n![The development channel section of an extension's listing page, offering
access to alpha and beta versions for
testing.](https://mdn.mozillademos.org/files/15273/extensions-development-
channel.png)  
\n Once you are happy with your update, you can publish it as the new release
version of your extension.

\n

  * If you want to distribute your extension to users outside AMO, you can find the instructions for doing so, and the installation instructions you need to provide users, in the article on [Sideloading add-ons](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Alternative_distribution_options/Sideloading_add-ons). Remember that, unlike distribution through AMO, you will need to send users any updated versions of your extension as you make improvements.
\n

  * Use the [Responsive Design Mode](https://developer.mozilla.org/en-US/docs/Tools/Responsive_Design_Mode) to test your extension for its behavior on other screen sizes and device types.
\n

\n]

