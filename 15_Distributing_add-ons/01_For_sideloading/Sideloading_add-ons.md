[



You may want to send a user your add-on\u2019s XPI file by some means other
than a web download, such as an email distribution of a beta version for user
testing. In this case, there are two practical options for installing the add-
on:





  * Using **Install Add-on From File** in the Add-on manager.


  * Adding the file to one of the standard extension folders.






No automatic updates will be performed for add-ons installed using these
methods. You will have to deliver a new XPI file to your user for each update.
However, automatic compatibility checks are still performed.





## Preparing your add-on



Regardless of the sideloading method used, you must prepare the add-on as
follows:





  1. Ensure the add-on includes an ID, by adding the following to its manifest.json file, replacing _your-add-on-name@your-domain.com_ with a suitable ID for your add-on: 
    
        "applications": {  "gecko": {    "id": "your-add-on-name@your-domain.com"  }}

 An email address style ID is recommended.



  2. Sign the add-on in [addons.mozilla.org](http://addons.mozilla.org) (AMO). Depending on how you want to make your add-on available, you can use either the unlisted (if you are distributing the add-on exclusively) or listed options. For more details, see [Signing and distributing your add-on](/en-US/docs/Mozilla/Add-ons/Distribution).




## Using Install Add-on From File



To use **Install Add-on From File** in Add-on manager, send the user the
signed add-on with the following instructions:





  1. Save the add-on file to a suitable location on your computer.


  2. In Firefox, open the Firefox menu ![Firefox browser menu button](https://mdn.mozillademos.org/files/15199/Firefox_menu.png) and click **Add-ons**.


  3. From the settings cog, open **Install Add-on From File** :  
![Add-on Manager utilities cog](https://mdn.mozillademos.org/files/15201
/add-on_manager_cog.png)



  4. Browse to and open the file from the location where it was saved.


  5. When prompted click **Add** :  
![Message asking user to confirm the installation of the add-
on](https://mdn.mozillademos.org/files/15203/add_add_on_confirmation.png)



  6. The add-on will now appear in the add-on manager\u2019s list of installed add-ons and be ready to use:  
![After installation the add-on is listed in the add-on
manager](https://mdn.mozillademos.org/files/15205/add_on_added.png)





## Installation using the standard extension folders



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



### Rename your XPI file



To use this method, your XPI file must be named using the add-on or
application ID, as set in [Preparing your add-on](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Alternative_methods_of_installing_add-ons/Sideloading_add-
ons#Preparing_your_add-on). The signed add-on file you downloaded from AMO
will be named something like borderify-1.0-an+fx.xpi (see [Signing and
distributing your add-on](/en-US/docs/Mozilla/Add-ons/Distribution) for more
details), change this to, for example, borderify@example.com.xpi.





If you are developing an add-on for Firefox you can use an[ extension proxy
file](/en-US/docs/Mozilla/Add-
ons/Setting_up_extension_development_environment#Firefox_extension_proxy_file)
to install an add-on without copying the files over to the standard extensions
folders.





### Add the add-on XPI file to a standard extensions folder.



In what follows {ec8030f7-c20a-464f-9b0e-13a3a9e97384} is the application ID
of Firefox. \xa0



The standard installation of Firefox disables the automatic installation of
add-ons from these locations (see [Controlling automatic installation](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Alternative_methods_of_installing_add-
ons/Installing_add-
ons_in_an_enterprise_environment#Controlling_automatic_installation)). As a
result, the process for each of the methods described below is as follows:





  * Copy the renamed XPI file to the extensions folder for Windows, OSX, or Linux as appropriate. Note that, depending on the desktop OS and its settings, the user may need administrator permission to complete this action.


  * Close and restart Firefox.


  * Depending on the OS and version of Firefox one of the the following will happen: 
    * The install will happen silently, and the user will need to open add-on manager and enable the add-on:  
![An add-on is installed but disabled
](https://mdn.mozillademos.org/files/15207/add_on_disabled.png)  
 To enable the add-on, the user will need to click **Enable**.



    * An interstitial message will be displayed:  
![An interstitial warning about the installation of the add-
on](https://mdn.mozillademos.org/files/15209/interstitial_windows.png)  
 To install the add-on, the user will need to check **Allow this
installation** and click **Continue**.





  * The add-on is now installed.




For more details on the interstitial and silent installs, see [Controlling
automatic installation](/en-US/docs/Mozilla/Add-ons/WebExtensions
/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Controlling_automatic_installation).





To uninstall the add-on, close Firefox and remove the add-on from the location
where it was added.





#### Windows



To install the add-on for a user of the computer, copy the XPI file to:



    
    
    C:\\Users\\<user name>\\AppData\\Roaming\\Mozilla\\Extensions\\{ec8030f7-c20a-464f-9b0e-13a3a9e97384}\\



If this folder does not exist, create it. You can also identify the current
user\u2019s path with the %appdata% system variable.





Note: To install an add-on for all users of a Windows computer, see
[Installation using the Windows registry](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Alternative_methods_of_installing_add-ons/Installing_add-
ons_in_an_enterprise_environment#Installation_using_the_Windows_registry).





#### OSX



To install an add-on for use by all Firefox profiles and all users, copy the
XPI file to the global extension folder located in Library. If this folder
doesn't exist, you will need to create it.



    
    
    /Library/Application Support/Mozilla/Extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/



To install an add-on for a specific user, copy the XPI file to the user's
local Library:



    
    
    ~/Library/Application Support/Mozilla/Extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/



#### Linux



To install an add-on for use by all users, copy the XPI file to:



    
    
    /usr/lib/Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/



Or...



    
    
    /usr/lib64/Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/



Or...



    
    
    /usr/share/Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/



To install an add-on for a specific user, copy the XPI file to:



    
    
    ~/.Mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/

]

