[\n

\n

If you have developed an add-on to complement a desktop application, there are
several ways you can install the add-on:

\n

\n

  * Direct the user to install from [addons.mozilla.org](http://addons.mozilla.org) (AMO) by offering a link.
\n

  * Sideloading.
\n

  * Using the Windows registry.
\n

\n

Of these options, directing the user to install from AMO by offering a link is
recommended. The reasons for recommending this option are:

\n

\n

  * It avoids any issues with the installation process; the user will not get an interstitial messages during the installation of the add-on, find the add-on installed but disabled, or find that the add-on was not installed.
\n

  * If you update the add-on, the new version will be automatically installed, once you have uploaded it to AMO.
\n

\n

By contrast, sideloading using the [standard extension folders](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Alternative_methods_of_installing_add-
ons/Sideloading_add-ons#Installation_using_the_standard_extension_folders) or
[Windows registry](/en-US/docs/Mozilla/Add-ons/WebExtensions
/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Installation_using_the_Windows_registry) will
require your desktop app to install any update to the add-on. Also, based on
the default Firefox settings, the installation process will present the user
with warnings (an interstitial message) or silently install the add-on but
disable it. The worst case is that the installation will fail silently if
Firefox is setup to [disable automatic installation](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Controlling_automatic_installation). You can
update the [Firefox configuration](/en-US/docs/Mozilla/Add-ons/WebExtensions
/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Settings_scope_preferences_programmatically)
to avoid these issues, but that is not recommended.

\n]

