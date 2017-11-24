[\n

\n

\xa0

\n

Add-ons allow developers to extend and modify the functionality of Firefox.
They are written using standard Web technologies - JavaScript, HTML, and CSS -
plus some dedicated JavaScript APIs. Among other things, an add-on could:

\n

\n

  * Change the appearance or content of particular websites
\n

  * Modify the Firefox user interface
\n

  * Add new features to Firefox
\n

\n

There are several types of add-ons, but the most common type are extensions.

\n

## Developing extensions

\n

In the past, there were several toolsets for developing Firefox extensions,
but by the end of November 2017, extensions must be built using [WebExtensions
APIs](https://developer.mozilla.org/en-US/Add-ons/WebExtensions). Other
toolsets, such as overlay add-ons, bootstrapped add-ons, and the Add-on SDK,
will be deprecated over the same period of time.

\n

If you are writing a new extension, use [WebExtensions
APIs](https://developer.mozilla.org/en-US/Add-ons/WebExtensions).

\n

Extensions written using WebExtensions APIs for Firefox are designed to be
cross-browser compatible. In most cases it will run in Chrome, Edge, and Opera
with few if any changes. They are also fully compatible with multiprocess
Firefox.  
\n  
\n[See the APIs currently supported in Firefox and other
browsers](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Browser_support_for_JavaScript_APIs). We're continuing to
design and implement new APIs in response to developer needs.  
\n  
\n Most of the WebExtensions APIs are also available on Firefox for Android.

\n

### Migrate an existing extension

\n

If you maintain a legacy extension, such as a XUL overlay, bootstrapped, or
Add-on SDK-based extension, we recommend that you investigate porting it to
use WebExtension APIs. There are some [porting resources on MDN](/en-US/Add-
ons/WebExtensions/Porting_a_legacy_Firefox_add-on).

\n

We've collected [resources](https://wiki.mozilla.org/Add-
ons/developer/communication) on a wiki page to support developers through the
transition. To get started, use the compatibility [Lookup Tool](https
://compatibility-lookup.services.mozilla.com/) to see if your extension will
be affected.

\n

## Publishing add-ons

\n

[Addons.mozilla.org](https://addons.mozilla.org), commonly known as "AMO," is
Mozilla's official site for developers to list add-ons, and for users to
discover them. By uploading your add-on to AMO, you can participate in our
community of users and creators, and find an audience for your add-on.

\n

You are not required to list your add-on on AMO, but your add-on must be
signed by Mozilla or users won't be able to install it.

\n

For an overview of the process of publishing your add-on, see [Signing and
distributing your add-on](https://developer.mozilla.org/en-US/Add-
ons/Distribution).

\n

## Other types of add-ons

\n

In addition to extensions, there are a few other add-on types that allow users
to customize Firefox. Those add-ons include:

\n

\n

  * [Lightweight themes](https://developer.mozilla.org/Add-ons/Themes/Background) are a simple way to provide limited customization for Firefox.
\n

  * [Mobile add-ons](/en-US/Add-ons/Firefox_for_Android) are for\xa0Firefox for Android. Note, though, that we intend to deprecate some of the technology underlying these APIs. In the future, WebExtensions APIs will be fully supported to an extent on Firefox for Android.
\n

  * [Search engine plugins](/en-US/docs/Creating_OpenSearch_plugins_for_Firefox) add new search engines to the browser's search bar.
\n

  * [User dictionaries](/en-US/docs/Mozilla/Creating_a_spell_check_dictionary_add-on) let you spell-check in different languages.
\n

  * [Language packs](https://support.mozilla.org/kb/use-firefox-interface-other-languages-language-pack) let you have more languages available for the user interface of Firefox.
\n

\n

* * *

\n

## Contact us

\n

You can use the links below to get help, keep up to date with news around add-
ons, and give us feedback.

\n

### Add-ons forum

\n

Use the [Add-ons Discourse forum](https://discourse.mozilla.org/c/add-ons) to
discuss all aspects of add-on development and to get help.

\n

### Mailing lists

\n

Use the **dev-addons** list to discuss development of the add-ons ecosystem,
including the development of the WebExtensions system and of AMO:

\n

\n

  * [dev-addons list info](https://mail.mozilla.org/listinfo/dev-addons)
\n

  * [dev-addons archives](https://mail.mozilla.org/pipermail/dev-addons/)
\n

\n

Use the **webextensions-support** list to get help porting or transitioning to
WebExtensions:

\n

\n

  * [webextensions-support list info](https://mail.mozilla.org/listinfo/webextensions-support)
\n

  * [webextensions-support archives](https://mail.mozilla.org/pipermail/webextensions-support/)
\n

\n

### IRC

\n

If you're a fan of IRC, you can get in touch at:

\n

\n

  * [#addons](irc://irc.mozilla.org/addons) (discussion of the add-ons ecosystem)
\n

  * [#extdev](irc://irc.mozilla.org/extdev) (general discussion of add-on development)
\n

  * [#webextensions](irc://irc.mozilla.org/webextensions) (discussion around the WebExtensions API in particular)
\n

\n

### Report problems

\n

#### Security vulnerabilities

\n

If you discover a security vulnerability in an add-on, even if it is not
hosted on a Mozilla site, let us know and we will work with the developer to
correct the issue. Please report them [confidentially
](http://www.mozilla.org/projects/security/security-bugs-policy.html)in
[Bugzilla
](https://bugzilla.mozilla.org/enter_bug.cgi?product=addons.mozilla.org&component
=Add-on%20Security&maketemplate=Add-
on%20Security%20Bug&bit-23=1&rep_platform=All&op_sys=All)or by emailing [amo-
admins@mozilla.org](mailto:amo-admins@mozilla.org).

\n

#### Bugs on addons.mozilla.org (AMO)

\n

If you find a problem with the site, we'd love to fix it. Please [file a bug
report ](https://github.com/mozilla/addons/issues/new)and include as much
detail as possible.

\n]

