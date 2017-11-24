[



You will approach the coding of an extension for Firefox for Android in the
same way as you would for a desktop extension using WebExtension APIs; using a
text editor or tool of your choice to write the code. However, when you get to
testing and debugging your extension you need to follow a different process,
this article walks you through that process.



## Set up your computer and Android emulator or device



You first need to complete some one-off setup tasks on your computer and
Android device.



On your development computer:





  * If you want to test on your computer by running Firefox for Android in the Android emulator: 
    * Install [Android Studio](https://developer.android.com/studio/index.html).


    * Use the Android Studio[ SDK Manager](https://developer.android.com/studio/intro/update.html#sdk-manager) or the[ sdkmanager](https://developer.android.com/studio/command-line/sdkmanager.html) command-line tool to install the[ Android Platform Tools](https://developer.android.com/studio/releases/platform-tools.html).




  * If you plan to test in Firefox for Android running on a device only: 
    * Download and extract the [standalone Android SDK Platform-Tools package](https://developer.android.com/studio/releases/platform-tools.html) to a suitable location on your computer.


    * On Windows, Mac, or Linux: Add the location into which you extracted the tools package to your operating system\u2019s PATH environment variable.


    * Alternatively, on Mac or Linux: Link the binary to /usr/local/bin using `sudo ln -s /<extract folder>/platform-tools/adb /usr/local/bin`.






On your device or Android emulator:





  * Install [Firefox for Android](https://play.google.com/store/apps/details?id=org.mozilla.firefox&referrer=utm_source%3Dmozilla%26utm_medium%3DReferral%26utm_campaign%3Dmozilla-org) and, if you wish to test the latest features, [Firefox for Android Beta](https://play.google.com/store/apps/details?id=org.mozilla.firefox_beta) or [Firefox Nightly for Developers](https://play.google.com/store/apps/details?id=org.mozilla.fennec_aurora).


  * Open Firefox for Android and turn off signing by browsing to `about:config` then locating and setting `xpinstall``.signatures.required` to false.  
![Firefox for Android with about:config open, showing
xpinstall.signatures.required set to
false.](https://mdn.mozillademos.org/files/15101/set_xpinstall.png)





If you are using a device:





  * [Enable Android USB debugging on the device](https://developer.android.com/studio/run/device.html). You need to follow step 2 only, but note that you may have to [enable the developer options](https://developer.android.com/studio/debug/dev-options.html) if you do not see them on your device.


  * Attach your device to the development computer using a USB cable and on the device, when prompted, allow USB debugging for the connection.




On your development computer:





  * Open a command shell.


  * Run `adb devices`  
 You should see output similar to:  
`List of devices attached  
 51800F220F01564 device`  
 Where the hex string is your device\u2019s (or emulator\u2019s) code. This
means adb has found your device (or emulator).





## Install and run your extension in Firefox for Android



In your extension ensure that you have included an application ID using the
[applications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/applications) key in the manifest.json:



    
    
     "applications": {    "gecko": {       "id": "[borderify@example.com](mailto:borderify@example.com)"    } },



[Zip the content of your extension into an xpi file](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Publishing_your_WebExtension#1._Zip_up_your_add-
on%27s_files) named to match the application ID, for example,
`borderify@example.com.xpi`.



You now have two options for transferring and running your extension: using
adb or a website.



### Transfer your extension using adb



On your computer, execute `/path/to/adb push /path/to/<extension file
name>.xpi /mnt/sdcard/`, which will transfer the extensions xpi file to your
attached emulator or device.



On your Android device or in the emulator, open Firefox for Android and browse
to `file:///mnt/sdcard`:



![Firefox for Android showing the add-on xpi file located on the memory
card](https://mdn.mozillademos.org/files/15103/xpi%20file%20on%20memory%20card.png)



Tap on `<extension file name>.xpi` to install it. You will get a warning about
the extension being blocked, tap ALLOW:



![Firefox for Android blocked add-on
message](https://mdn.mozillademos.org/files/15105/blocked-add-on-message.png)



An additional warning will tell you the extension is unverified, tap INSTALL:



![Firefox for Android unverified add-on
message](https://mdn.mozillademos.org/files/15107/unverified_add_on_messages.png)



Your extension will start running (in this case a copy of the
[borderify](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Examples#borderify) example extension):



![Borderify shown adding a red border to the www.mozilla.org home
page](https://mdn.mozillademos.org/files/15109/borderify_in_action.png)



### Transfer your extension via a website.



Upload your xpi file to your website and make it accessible over HTTP. Browse
to the file and download it. Follow the installation instructions, which will
be similar to those for an extension transferred using adb.



## Debug your extension



You can debug your extension in WebIDE and view any manifest,json validation
messages using adb logcat. To make use of these features, first set up Firefox
remote debugging [over USB](https://developer.mozilla.org/en-
US/docs/Tools/Remote_Debugging/Debugging_Firefox_for_Android_with_WebIDE#Enable_remote_debugging_in_Firefox_for_Android)
or [Wi-Fi](https://developer.mozilla.org/en-
US/docs/Tools/Remote_Debugging/Debugging_Firefox_for_Android_over_Wifi).



### Using WebIDE to debug your extension



Open WebIDE from the Developer option on the desktop Firefox menu. Once open,
select your connected device from the options in the right-hand sidebar.



![Selecting the Firefox for Android device from the list in
WebIDE](https://mdn.mozillademos.org/files/15111/Select%20Firefox%20on%20Android%20device.png)



Now, ensure you are viewing the Main Process, then load a page in which your
extension will be exercised.





Unlike desktop Firefox, where background scripts output their console messages
and are debugged in the add-on debugger, while content scripts output their
console messages and are debugged in the browser\u2019s developer tools (see
[Debugging content scripts](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Debugging#Debugging_content_scripts)), you can view all
messages and debug all scripts in WebIDE when running extensions in Firefox
for Android.





If you included any console messages in your extension (using
`console.log()`), you can see these the Console tab, and can use the console
filter (highlighted below) to hide other console messages:



![WebIDE showing console with messages filtered for those including
'borderify'](https://mdn.mozillademos.org/files/15113/WebIDE%20console%20messages%20and%20filter.png)



The Debugger tab then enables you to access the background script and any
content scripts:



![The borderify.js script in the WebIDE debugger
tab](https://mdn.mozillademos.org/files/15115/WebIDE%20script%20in%20debugger.png)



You can now apply breakpoints and observe the extension\u2019s behavior.



Also, you can also target the document related to an extension page, for
example, the background page of the borderify example, using the same approach
described for the [Browser Toolbox](https://developer.mozilla.org/en-
US/docs/Tools/Browser_Toolbox#Targeting_a_document):



![Selecting a specific page to examine in the
WebIDE](https://mdn.mozillademos.org/files/15117/WebIDE%20selecting%20page.png)



Once you have switched to an extension page, you can inspect the extension
page\u2019s DOM elements from the Inspector panel (also the "inspect node"
toggle button should work as expected) and execute WebExtension API calls from
the Console panel:



![Using the interactive console to test the effect of JavaScript on the open
page](https://mdn.mozillademos.org/files/15119/WebIDE%20testing%20JavaScript.png)



For more details on using WebIDE, see the [WebIDE
section](https://developer.mozilla.org/en-US/docs/Tools/WebIDE).



### Viewing manifest validation messages using the console



In addition to the console messages output through WebIDE, there may also be
messages relating to the validation of the extension\u2019s manifest.json
files. These messages can be viewed using the adb logcat command. To avoid
receiving other, unrelated messages, you can pipe the output through grep,
filtering by the extension\u2019s ID, for example:



`/path/to/adb logcat | grep borderify@example.com`



`This will give output similar to this:`



``I/Gecko \xa0\xa0(30440): 1496056181889 \xa0\xa0\xa0addons.xpi
\xa0\xa0\xa0WARN \xa0\xa0\xa0Addon with ID borderify@example.com already
installed, older version will be disabled``



`If your add-on fails to run, check these messages as they may provide
information explaining why.`

]

