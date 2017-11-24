[\n

\n

You may want to send a user your add-on\u2019s XPI file by some means other
than a web download, such as an email distribution of a beta version for user
testing. In this case, there are two practical options for installing the add-
on:

\n

\n

  * Using **Install Add-on From File** in the Add-on manager.
\n

  * Adding the file to one of the standard extension folders.
\n

\n

\n

No automatic updates will be performed for add-ons installed using these
methods. You will have to deliver a new XPI file to your user for each update.
However, automatic compatibility checks are still performed.

\n

\n

## Preparing your add-on

\n

Regardless of the sideloading method used, you must prepare the add-on as
follows:

\n

\n

  1. Ensure the add-on includes an ID, by adding the following to its manifest.json file, replacing _your-add-on-name@your-domain.com_ with a suitable ID for your add-on:\n\n 
    
        "applications": {\n  "gecko": {\n    "id": "your-add-on-name@your-domain.com"\n  }\n}\n

\n An email address style ID is recommended.

\n

  2. Sign the add-on in [addons.mozilla.org](http://addons.mozilla.org) (AMO). Depending on how you want to make your add-on available, you can use either the unlisted (if you are distributing the add-on exclusively) or listed options. For more details, see [Signing and distributing your add-on](/en-US/docs/Mozilla/Add-ons/Distribution).
\n

\n

## Using Install Add-on From File

\n

To use **Install Add-on From File** in Add-on manager, send the user the
signed add-on with the following instructions:

\n

\n

  1. Save the add-on file to a suitable location on your computer.
\n

  2. In Firefox, open the Firefox menu ![Firefox browser menu button](https://mdn.mozillademos.org/files/15199/Firefox_menu.png) and click **Add-ons**.
\n

  3. From the settings cog, open **Install Add-on From File** :  
\n![Add-on Manager utilities cog](https://mdn.mozillademos.org/files/15201
/add-on_manager_cog.png)

\n

  4. Browse to and open the file from the location where it was saved.
\n

  5. When prompted click **Add** :  
\n![Message asking user to confirm the installation of the add-
on](https://mdn.mozillademos.org/files/15203/add_add_on_confirmation.png)

\n

  6. The add-on will now appear in the add-on manager\u2019s list of installed add-ons and be ready to use:  
\n![After installation the add-on is listed in the add-on
manager](https://mdn.mozillademos.org/files/15205/add_on_added.png)

\n

\n

## Installation using the standard extension folders

\n

This method of add-on installation involves copying the add-on into one of the
standard extension folders on the user's computer. Once copied, the next time
Firefox launches the add-on will be installed. By default, the user will be
asked to approve the installation, and if the user approves, the add-on will
be installed and automatically loaded for subsequent launches. If the user has
more than one Firefox profile, the approval and installation will occur on the
next launch of each profile. For details on controlling whether the user is
prompted to approve the installation, see \xa0[Controlling automatic
installation](/en-US/docs/Mozilla/Add-ons/WebExtensions
/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Controlling_automatic_installation).

\n

### Rename your XPI file

\n

To use this method, your XPI file must be named using the add-on or
application ID, as set in [Preparing your add-on](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Alternative_methods_of_installing_add-ons/Sideloading_add-
ons#Preparing_your_add-on). The signed add-on file you downloaded from AMO
will be named something like borderify-1.0-an+fx.xpi (see [Signing and
distributing your add-on](/en-US/docs/Mozilla/Add-ons/Distribution) for more
details), change this to, for example, borderify@example.com.xpi.

\n

\n

If you are developing an add-on for Firefox you can use an[ extension proxy
file](/en-US/docs/Mozilla/Add-
ons/Setting_up_extension_development_environment#Firefox_extension_proxy_file)
to install an add-on without copying the files over to the standard extensions
folders.

\n

\n

### Add the add-on XPI file to a standard extensions folder.

\n

In what follows {ec8030f7-c20a-464f-9b0e-13a3a9e97384} is the application ID
of Firefox. \xa0

\n

The standard installation of Firefox disables the automatic installation of
add-ons from these locations (see [Controlling automatic installation](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Alternative_methods_of_installing_add-
ons/Installing_add-
ons_in_an_enterprise_environment#Controlling_automatic_installation)). As a
result, the process for each of the methods described below is as follows:

\n

\n

  * Copy the renamed XPI file to the extensions folder for Windows, OSX, or Linux as appropriate. Note that, depending on the desktop OS and its settings, the user may need administrator permission to complete this action.
\n

  * Close and restart Firefox.
\n

  * Depending on the OS and version of Firefox one of the the following will happen:\n \n
    * The install will happen silently, and the user will need to open add-on manager and enable the add-on:  
\n![An add-on is installed but disabled
](https://mdn.mozillademos.org/files/15207/add_on_disabled.png)  
\n To enable the add-on, the user will need to click **Enable**.

\n

    * An interstitial message will be displayed:  
\n![An interstitial warning about the installation of the add-
on](https://mdn.mozillademos.org/files/15209/interstitial_windows.png)  
\n To install the add-on, the user will need to check **Allow this
installation** and click **Continue**.

\n\n

\n

  * The add-on is now installed.
\n

\n

For more details on the interstitial and silent installs, see [Controlling
automatic installation](/en-US/docs/Mozilla/Add-ons/WebExtensions
/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Controlling_automatic_installation).

\n

\n

To uninstall the add-on, close Firefox and remove the add-on from the location
where it was added.

\n

\n

#### Windows

\n

To install the add-on for a user of the computer, copy the XPI file to:

\n

    
    
    C:\\Users\\<user name>\\AppData\\Roaming\\Mozilla\\Extensions\\{ec8030f7-c20a-464f-9b0e-13a3a9e97384}\\

\n

If this folder does not exist, create it. You can also identify the current
user\u2019s path with the %appdata% system variable.

\n

\n

Note: To install an add-on for all users of a Windows computer, see
[Installation using the Windows registry](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Installation_using_the_Windows_registry).

\n

\n

#### OSX

\n

To install an add-on for use by all Firefox profiles and all users, copy the
XPI file to the global extension folder located in Library. If this folder
doesn't exist, you will need to create it.

\n

    
    
    /Library/Application Support/Mozilla/Extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/

\n

To install an add-on for a specific user, copy the XPI file to the user's
local Library:

\n

    
    
    ~/Library/Application Support/Mozilla/Extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/

\n

#### Linux

\n

To install an add-on for use by all users, copy the XPI file to:

\n

    
    
    /usr/lib/Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/

\n

Or...

\n

    
    
    /usr/lib64/Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/

\n

Or...

\n

    
    
    /usr/share/Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/

\n

To install an add-on for a specific user, copy the XPI file to:

\n

    
    
    ~/.Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/

\n]

