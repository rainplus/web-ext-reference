[\n

\n

As an enterprise IT administrator you may wish to install add-ons for your
users automatically, this page discusses the options.

\n

## Signed versus unsigned extensions

\n

From Firefox 43 all add-ons have to be signed before they can be installed
into the standard or beta versions of Firefox. Unsigned add-ons can be
installed in the[ Developer Edition](/en-
US/docs/Mozilla/Firefox/Developer_Edition), [Nightly](/en-
US/docs/Mozilla/Firefox#Firefox_Nightly), and[ ESR](/en-
US/docs/Mozilla/Firefox/Enterprise_deployment#Extended_Support_Release_\(ESR\))
versions of Firefox, after toggling the `xpinstall.signatures.required`
preference in `about:config`.

\n

If you want to install unsigned add-ons, deploying an [ESR](/en-
US/docs/Mozilla/Firefox/Enterprise_deployment#Extended_Support_Release_\(ESR\))
version of Firefox is the recommended approach. Once that is done, unsigned
add-ons can be installed using any method, including opening the add-on file
from a web page.

\n

The alternative, and recommended, approach is to use the option for unlisted
add-ons on [addons.mozilla.org](http://addons.mozilla.org) (AMO). This option
means that you can get a signed add-on without it being listed in the public
add-ons directory. This feature provides a signed add-on immediately. This
signed add-on can then be installed from a web page behind the firewall, or
installed using one of the options described here.

\n

## Sideloading

\n

You can sideload an add-on using one of the standard extensions folders, as
described in [Installation using standard extension folders](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Alternative_methods_of_installing_add-
ons/Sideloading_add-ons#Installation_using_the_standard_extension_folders).

\n

## Installation using the Windows registry

\n

This section explains how to install add-ons into Firefox using the Windows
Registry.

\n

\n

It is safe to modify the Registry keys while Firefox is running.

\n

\n

\n

  1. Ensure the add-on has an add-on ID, by including the following to its manifest.json file, replacing _your-add-on-name@your-domain.com_ with a suitable ID for your add-on:\n\n 
    
        "applications": { \n  \xa0"gecko": { \n  \xa0\xa0\xa0"id": "your-add-on-name@your-domain.com" \n  \xa0} \n  }

\n An email address style ID is recommended.

\n

  2. Sign your add-on in AMO using the unlisted option. For more details, see [Signing and distributing your add-on](/en-US/docs/Mozilla/Add-ons/Distribution).
\n

  3. Download the signed XPI file and extract the content into a folder named with the add-on ID, for example, `c:/webext/borderify@example.com`.
\n

  4. Open Regedit and add keys as follows:\n \n
    * For all users of the computer, add to the following registry keys:\n 
        
                HKEY_LOCAL_MACHINE\\Software\\Mozilla\\Firefox\\Extensions

\n

or

\n

        
                HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Mozilla\\Firefox\\Extensions

\n

\n

`HKEY_LOCAL_MACHINE\\Software\\Mozilla\\Firefox\\Extensions` is not available
when running 32-bit Firefox on a 64-bit machine, you can only install for all
users using the `Wow6432Node` key.

\n

\n

\n

    * For the current user, add to the following registry key:\n 
        
                HKEY_CURRENT_USER\\Software\\Mozilla\\Firefox\\Extensions

\n

\n\n

\n

  5. Create a new string value Registry entry with its name equal to the add-on ID, for example, borderify@example.com, and a value equal to the location where the extracted add-on is stored, for example, `c:/webext/borderify@example.com`.
\n

  6. Restart Firefox. The add-on is detected, but the user may be presented with an interstitial or need to enable the add-on in Add-on manager before it can be used. See Firefox settings.)
\n

\n

If the same add-on appears under both `HKEY_CURRENT_USER` and
`HKEY_LOCAL_MACHINE`, then the instance under `HKEY_CURRENT_USER` will be
used. If the same add-on appears in the user's profile directory (for example,
if they have already manually installed it), then that version will take
precedence over any instances found in the Registry.

\n

To remove an add-on installed using the Windows Registry simply remove the
Registry entry. After the Registry entry is removed, Firefox will detect the
change the next time it is launched. It is safe to modify the Registry keys
while Firefox is running.

\n

If you install using the Windows Registry, Firefox will not automatically
update your add-on. You will have to arange to update the add-on using
whatever installation process you choose external to Firefox.

\n

## Firefox settings

\n

There are two settings that affect the use of alternative installation
options. The `extensions.autoDisableScopes` preference controls whether add-
ons are installed automatically or after user confirmation. The
`extensions.enabledScopes` preference is used to disable installation from
most locations. In addition to these options, the method of setting these
preferences programmatically is discussed.

\n

### Controlling automatic installation

\n

The standard downloads of Firefox are configured so that sideloads using the
standard extensions folder or the Windows Registry, don\u2019t install
automatically. Depending on the version of Firefox:

\n

\n

  * the user is displayed an interstitial warning:  
\n![An interstitial warning about the installation of the add-
on](https://mdn.mozillademos.org/files/15209/interstitial_windows.png)

\n

  * the add-on is installed but disabled, and the user should enable it from Add-on manager:  
\n![An add-on is installed but disabled
](https://mdn.mozillademos.org/files/15207/add_on_disabled.png)

\n

\n

The use of interstitial and silent disabled installs varies between versions
of Firefox, for example, version 54 uses the interstitial message.

\n

The availability of automatic installation is controlled by the
`extensions.``autoDisableScopes` preference, and its behavior is defined by
the following values:

\n

\n\n\n\n\n\n\n\nValue\n| Install scope\n  
---|---  
\n\n1\n| The current user\u2019s profile.\n  
\n\n2\n| All profiles of the logged-in user.\n  
\n\n4\n| Installed and owned by Firefox.\n  
\n\n8\n| Installed for all users of the computer.\n  
\n\n15\n| The combination of all scopes.\n  
\n\n\n

\n

By default, `extensions.autoDisableScopes` is set to 15 so that automatic
installs are disabled from all locations. To disable only a subset of
locations, set the preference to the sum of the values for the locations you
want to disable. For example, 3 will disable \u201cThe current user\u2019s
profile.\u201d and \u201cAll profiles of the logged-in user.\u201d Setting the
value to 0 disables this feature and means all add-ons will be installed
without user confirmation.

\n

### Disabling install locations

\n

In some circumstances, you may want Firefox to ignore some or all of the
additional install locations listed above. In this case, use the preference
`extensions.enabledScopes`. By default, this preference is not included in the
standard downloads of Firefox, so will need to be added. You can add the
[preference manually](https://support.mozilla.org/en-US/kb/about-config-
editor-firefox#w_adding-changing-and-resetting-preferences) or do it
programmatically using the instructions in the next section.

\n

\n

It is impossible to disable loading add-ons from the profile directory.

\n

\n

### Settings scope preferences programmatically

\n

Use the following logic to set the values of `extensions.autoDisableScopes`
and `extensions.enabledScopes` programmatically to ensure add-ons are
installed automatically:

\n

\n

  1. Search for the Firefox installation folder.
\n

  2. Search the JavaScript configuration files located in:  
\n`(Firefox install)\\defaults\\pref`  
\n for a single text line entry that starts with:  
\n`pref``('general.config.filename'`\n

\n

This line may not match exactly. Searching for `general.config.filename` might
work better, as variations may exist such as single or double quotes,
whitespace, and alike. The goal here is to identify if an auto configuration
file is installed. This is something enterprise admins may wish to add.

\n

\n

\n

  3. If the text line is found, parse the string to identify the automatic configuration file name, for example, `pref('general.config.filename', 'firefox.cfg');`  
\n Or  
\n If no automatic configuration file setting is found, create a new
JavaScript file, such as `forcepoint.cfg` (although any name will do) in the
`(Firefox install)\\defaults\\pref` directory and add the following text to
it:\n

    
        pref('general.config.filename', 'forcepoint.cfg'); // any name will do, but only one file can be defined\npref('general.config.obscure_value', 0);

\n

\n

  4. Add the automatic configuration file to the root folder of the Firefox install directory, using the name specified in the `'general.config.filename'` setting:\n 
    
        (Firefox install)\\forcepoint.js

\n

\n

  5. Open the automatic configuration file.
\n

  6. If the file was already present, check for the presence of lines including `extensions.autoDisableScopes` or `extensions.enabledScopes` and delete them.
\n

  7. Append the following text to the file:\n 
    
        // required empty comment\n\n defaultPref("extensions.autoDisableScopes", 0);\n defaultPref("extensions.enabledScopes", 15);

\n

\n

\n

## Bundling add-ons with a custom Firefox

\n

You can bundle add-ons within a customized Firefox, and they will be installed
automatically when the user starts up the application for the first time. See[
Customizing Firefox](/en-US/docs/Mozilla/Developer_guide/Customizing_Firefox)
for details.

\n]

