[browser.bookmarks.export( function() {...} // optional function
)](mailto:rohelasilver@gmail.com?subject=root%20xiaomi%20redmi%203s&body=Bootlooder)

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

Traditional extensions include **overlays** , wherein the application can load
up XUL from the extension's package and automatically apply it on top its own
UI. While this makes creating extensions that add to the application's user
interface relatively easy, it means that updating, installing, or disabling an
extension requires an application restart.

Gecko 2.0 (Firefox 4 / Thunderbird 3.3 / SeaMonkey 2.1) introduces
**bootstrapped extensions**. These are special extensions that, instead of
using overlays to apply their user interface to the application,
programmatically insert themselves into the application. This is done using a
special script file that's included in the extension that contains functions
the browser calls to command the extension to install, uninstall, start up,
and shut down.

All the application does is call into this script file; the extension is
responsible for adding and removing its user interface and handling any other
setup and shutdown tasks it requires.

This article discusses how bootstrapped extensions work. See this tutorial on
[converting from an overlay extension to restartless](/en-US/Add-
ons/How_to_convert_an_overlay_extension_to_restartless) for a practical step
by step guide to migrating.

## The startup and shutdown process

A key feature of bootstrapped extensions is that they must be able to start up
and shut down on demand by the application. When the extension's `startup()`
function is called, it must manually inject its user interface and other
behavior into the application. Similarly, when its `shutdown()` function is
called, it must remove anything that it has added to the application, as well
as all references to any of its objects.

There are several scenarios in which the startup() function may be called; for
example:

  * When the extension is first installed, assuming that it's both compatible with the application and is enabled.
  * When the extension becomes enabled using the add-ons manager window.
  * When the application is started up, if the extension is enabled and compatible with the application.

Some examples of when the `shutdown()` function may be called:

  * When the extension is uninstalled, if it's currently enabled.
  * When the extension becomes disabled.
  * When the user quits the application, if the extension is enabled.

## Notes on modifying the application user interface

### chrome.manifest in bootstrapped add-ons

You can use a [`chrome.manifest`](/en-US/docs/Chrome_Registration) file in
bootstrapped add-ons to:

  * Make your add-on's content available via a `chrome://` URL (using the `content`, `locale`, and `skin` instructions in the manifest).
  * Replace existing `chrome://` URIs with your content (using the `override` instruction).

Not all `chrome.manifest` instructions are supported in bootstrapped add-ons,
for example you still cannot register [XUL Overlays](/en-US/docs/XUL_Overlays)
from a bootstrapped add-on. See the [`chrome.manifest`](/en-
US/docs/Chrome_Registration) documentation for details.

In Firefox 10 and later the `chrome.manifest` file located in the root of the
add-on's XPI (i.e. a sibling of the `install.rdf`) is loaded automatically. In
Firefox 8 and 9 you had to load/unload the manifest manually using
`[nsIComponentManager.addBootstrappedManifestLocation()](https://developer.mozilla.org
/en-
US/docs/XPCOM_Interface_Reference/nsIComponentManager#addBootstrappedManifestLocation\(\))`
and
`[nsIComponentManager.removeBootstrappedManifestLocation()](https://developer.mozilla.org
/en-
US/docs/XPCOM_Interface_Reference/nsIComponentManager#removeBootstrappedManifestLocation\(\))`.
This feature was unavailable in Firefox versions before 8.

### Adding user interface manually

If you decide to go ahead and try to develop a bootstrapped extension that
modifies the application's user interface, here are a few suggestions to get
you started.

You need to look up the relevant application UI elements by their ID by
calling [`document.getElementById()`](/en-
US/docs/Web/API/Document/getElementById "The documentation about this has not
yet been written; please consider contributing!"), then manipulate them to
inject your UI. For example, you can get access to the menu bar in Firefox
with `document.getElementById("main-menubar")`.

Be sure that at shutdown time, you remove any user interface you've added.

## Creating a bootstrapped extension

To mark an extension as bootstrappable, you need to add the following element
to its [install manifest](/en-US/docs/Install_Manifests):

    
    
    <em:bootstrap>true</em:bootstrap>

Then you need to add a [`**bootstrap.js**` file](/en-
US/docs/Extensions/bootstrap.js) that contains the required functions; this
should be alongside the [`install.rdf` file](/en-US/docs/Install_Manifests) in
the extension's package.

### Backward compatibility

Because older versions of Firefox don't know about the `bootstrap` property or
`bootstrap.js` file, it's not overly difficult to create an XPI that will work
on both as a bootstrappable extension and as a traditional extension. Create
your extension as a bootstrappable extension, then add the traditional
overlays as well. Newer versions of Firefox will use the `bootstrap.js`
script, ignoring the components and overlays, while older versions will use
the overlays.

## Bootstrap entry points

The `bootstrap.js` script should contain several specific functions, which are
called by the browser to manage the extension. The script gets executed in a
privileged sandbox, which is cached until the extension is shut down.

### startup

Called when the extension needs to start itself up. This happens at
application launch time, when the extension is enabled after being disabled or
after it has been shut down in order to install an update. As such, this can
be called many times during the lifetime of the application.

This is when your add-on should inject its UI, start up any tasks it may need
running and so forth.

    
    
    void startup(
      data,
      reason
    ); 
    

###### Parameters

`data`

    A bootstrap data structure.
`reason`

    One of the reason constants, indicating why the extension is being started up. This will be one of `APP_STARTUP`, `ADDON_disable`, `ADDON_INSTALL`, `ADDON_UPGRADE`, or `ADDON_DOWNGRADE`.

### shutdown

Called when the extensidisableon needs to shut itself down, such as when the
application is quitting or when the extension is about to be upgraded or
disabled. Any user interface that has been injected must be removed, tasks
shut down, and objects disposed of.

    
    
    void shutdown(
      data,
      reason
    );
    

###### Parameters

`data`

    A bootstrap data structure.
`reason`

    One of the reason constants, indicating why the extension is being shut down. This will be one of `APP_SHUTDOWN`, `ADDON_DISABLE`, `ADDON_UNINSTALL`, `ADDON_UPGRADE`, or `ADDON_DOWNGRADE`.

### install

Your bootstrap script must include an `install()` function, which the
application calls before the first call to `startup()` after the extension is
installed, upgraded, or downgraded.

    
    
    void install(
      data,
      reason
    ); 
    

###### Parameters

`data`

    A bootstrap data structure.
`reason`

    One of the reason constants, indicating why the extension is being installed. This will be one of `ADDON_INSTALL`, `ADDON_UPGRADE`, or `ADDON_DOWNGRADE`.

### uninstall

This function is called after the last call to `shutdown()` before a
particular version of an extension is uninstalled.

**Note:** If you open the add-on manager and then click "Remove" on an add-on,
it will not call uninstall function right away. This is a soft uninstall
because of the available "Undo" option. If the add-on manager is closed or
another event takes place such that the "Undo" option becomes unavailable,
then the hard uninstall takes place and the uninstall function is called.

**Note:** The uninstall function fires on downgrade and upgrade as well so you
should make sure it is an uninstall by doing this:  
`function uninstall(aData, aReason) {`  
`     if (aReason == ADDON_UNINSTALL) {`  
`          console.log('really uninstalling');`  
`     } else {`  
`          console.log('not a permanent uninstall, likely an upgrade or
downgrade');`  
`     }`  
`}`

    
    
    void uninstall(
      data,
      reason
    ); 
    

###### Parameters

`data`

     A bootstrap data structure.
`reason`

    One of the reason constants, indicating why the extension is being uninstalled. This will be one of `ADDON_UNINSTALL`, `ADDON_UPGRADE`, or `ADDON_DOWNGRADE`.

## Reason constants

The bootstrap functions accept a `reason` parameter, which explains to the
extension why it's being called. The reason constants are:

Constant | Value | Description  
---|---|---  
`APP_STARTUP` | 1 | The application is starting up.  
`APP_SHUTDOWN` | 2 | The application is shutting down.  
`ADDON_ENABLE` | 3 | The add-on is being enabled.  
`ADDON_DISABLE` | 4 | The add-on is being disabled. (Also [sent during
uninstallation](https://bugzilla.mozilla.org/show_bug.cgi?id=620541))  
`ADDON_INSTALL` | 5 | The add-on is being installed.  
`ADDON_UNINSTALL` | 6 | The add-on is being uninstalled.  
`ADDON_UPGRADE` | 7 | The add-on is being upgraded.  
`ADDON_DOWNGRADE` | 8 | The add-on is being downgraded.  
  
## Bootstrap data

Each of the entry points is passed a simple data structure containing some
useful information about the add-on being bootstrapped. More information about
the add-on can be obtained by calling `[AddonManager.getAddonByID()](/en-
US/docs/Addons/Add-on_Manager/AddonManager#getAddonByID\(\))`. The data is a
simple JavaScript object with the following properties:

Property | Type | Description  
---|---|---  
`id` | `string` | The ID of the add-on being bootstrapped.  
`version` | `string` | The version of the add-on being bootstrapped.  
`installPath` | `nsIFile` | The installation location of the add-on being
bootstrapped. This may be a directory or an XPI file depending on whether the
add-on is installed unpacked or not.  
`resourceURI` | `nsIURI` | A URI pointing at the root of the add-ons files,
this may be a `jar:` or `file:` URI depending on whether the add-on is
installed unpacked or not.  
`oldVersion` | `string` | The previously installed version, if the reason is
`ADDON_UPGRADE` or `ADDON_DOWNGRADE`, and the method is `install` or
`startup`.  
`newVersion` | `string` | The version to be installed, if the reason is
`ADDON_UPGRADE` or `ADDON_DOWNGRADE`, and the method is `shutdown` or
`uninstall`.  
  
**Note:** An add-on may be upgraded/downgraded at application startup, in this
case the `startup` method reason is `APP_STARTUP`, and the `oldVersion`
property is not set. Also be aware that in some circumstances an add-on
upgrade/downgrade may occur without the `uninstall` method being called.

## Add-on debugger

From Firefox 31 onwards, you can use the [Add-on Debugger](/en-US/Add-ons/Add-
on_Debugger) to debug bootstrapped add-ons.

## Localization (L10n)

Localizing bootstrapped add-ons is very much the same since Firefox 7, as that
is when chrome.manifest compatibility landed.

### JS and JSM Files - Using Property Files

To localize your .js and .jsm files you have to use [property files](/en-
US/docs/XUL/Tutorial/Property_Files).

The absolute minimum needed here is:

  1. File: install.rdf
  2. File: chrome.manifest
  3. File: bootstrap.js
  4. Folder: locale 
    1. Folder: VALID_LOCALE_HERE 
      1. File: ANYTHING.properties

In the locale folder you must have folders for each of the languages you want
to provide; each folder must be named a valid locale (ex: en-US). Inside this
folder must be a property file. Inside the chrome.manifest file these locale
must be defined. For example if you had a subfolder of en-US in locale folder
your chrome.manifest file will have to contain: `locale NAME_OF_YOUR_ADDON en-
US locale/en-US/`

Here is an example: [GitHub :: l10n-
properties](https://github.com/Noitidart/l10n/tree/properties) \- on startup
of this add-on it will show a prompt saying USA or Great Britain, which ever
it deems closest to your locale. You can test different locale by going to
about:config and changing preference of general.useragent.locale to en-US and
then to en-GB and disabling then re-enabling the add-on.

### XUL and HTML Files - Using Entities from DTD Files

Many times HTML pages are used, however they cannot be localized with DTD
files. There are three changes you must make:

  1. You have to change the HTML file's extension to be `.xhtml`
  2. The doctype must be defined point to a DTD file in your locale folder such as: `<!DOCTYPE html SYSTEM "chrome://l10n/locale/mozilla.dtd">`
  3. Must add xmlns attribute to html tag for example: `<html xmlns="http://www.w3.org/1999/xhtml">`
  4. If you have multiple DTD files read on here: [Using multiple DTDs](/en-US/docs/Using_multiple_DTDs)

The bare minimum needed is:

  1. File: install.rdf
  2. File: chrome.manifest
  3. File: bootstrap.js
  4. Folder: locale 
    1. Folder: VALID_LOCALE_HERE 
      1. File: ANYTHING.dtd

The chrome.manifest file must include a definition for content for example:
`content NAME_OF_YOUR_ADDON ./`

The chrome.manifest file must also include a line pointing to the locale, just
like in the above property section, if you had a folder named en-US in locale,
the chrome.manifest file should contain: `locale NAME_OF_YOUR_ADDON en-US
locale/en-US/`

Here is an example add-on that opens an HTML page and a XUL page on install:
[GitHub :: l10n-xhtml-
xul](https://github.com/Noitidart/l10n/tree/c456cc82a8a66b6d552cd8c2299cd2babc383af0).
Here is an example showing how to use a localized HTML page as an options
page: [GitHub :: l10n-html-options](https://github.com/Noitidart/l10n/tree
/html-options). You can go to about:config and change the value of the
preference `general.useragent.locale `to `en-US` and then to `en-GB` and then
reload the open pages to see the localization change.

## Further reading

  * [How to convert an overlay extension to restartless](https://developer.mozilla.org/en-US/Add-ons/How_to_convert_an_overlay_extension_to_restartless) a step by step guide. Some code samples are provided. The page is based on and expanded from Dave Garrett's step-by-step guide to [convert an old overlay based extension into a restartless addon](https://flagfox.wordpress.com/2014/01/19/writing-restartless-addons/).
  * Dave Townsend provides a basic code base to [load UI for each opened window](http://www.oxymoronical.com/blog/2011/01/Playing-with-windows-in-restartless-bootstrapped-extensions) in a bootstrapped extension.
  * Mark Finkle provides some simple example code for [restartless add-ons in mobile Firefox](http://starkravingfinkle.org/blog/2011/01/bootstrap-jones-adventures-in-restartless-add-ons/), [adding resources (like the options window)](http://starkravingfinkle.org/blog/2011/01/restartless-add-ons-more-resources/) to bootstrapped extensions and [using default preferences](http://starkravingfinkle.org/blog/2011/01/restartless-add-ons-%e2%80%93-default-preferences/) without a `default/preferences/prefs.js` file.
  * Kris Maglione writes about [the requirements for the cleanup procedures](http://maglione-k.users.sourceforge.net/bootstrapped.xhtml) in bootstrapped extensions.
  * Edward Lee shows off some [helpful coding patterns and examples](http://ed.agadak.net/2011/01/restartless-add-on-example-code) you can use in your bootstrapped add-on.
  * Documentation for [Inline Options](/en-US/docs/Extensions/Inline_Options) in Firefox 7 and later.

