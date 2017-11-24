[

Type| `Object`  
---|---  
Mandatory| No  
Example| 

    
    
    "commands": {  "toggle-feature": {    "suggested_key": {      "default": "Ctrl+Shift+Y",      "linux": "Ctrl+Shift+U"    },    "description": "Send a 'toggle-feature' event"  }}

  


Use the `commands` key to define one or more keyboard shortcuts for your
extension.



Each shortcut is defined with a name, a combination of keys, and a
description. Once you've defined some commands in manifest.json, you can
listen for the associated key combinations using the [`commands`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/commands "Listen for the user
executing commands that you have registered using the commands manifest.json
key.") JavaScript API.



## Syntax



The `commands` key is an object, and each shortcut is a property of it. The
property's name is the name of the shortcut.



Each shortcut is itself an object, which has up to two properties:





  * `suggested_key`: this defines the combination of keys


  * `description`: a string that describes this shortcut




The `suggested_key` property is itself an object, that may have any of the
following properties, which are all strings:





  * `"default"`, `"mac"`, `"linux"`, `"windows"`, `"chromeos"`, `"android"`, `"ios"`




The value of each property is the keyboard shortcut for the command on the
given platform, given as a string containing the keys separated by "+". The
value for `"default"` is used on all platforms that are not explicitly listed.



For example:



    
    
    "commands": {  "toggle-feature": {    "suggested_key": {      "default": "Alt+Shift+U",      "linux": "Ctrl+Shift+U"    },    "description": "Send a 'toggle-feature' event to the extension"  },  "do-another-thing": {    "suggested_key": {      "default": "Ctrl+Shift+Y"    }  }}



This defines two shortcuts:





  * one named "toggle-feature", accessed using Ctrl+Shift+U on Linux, and Alt+Shift+U on all other platforms


  * one named "do-another-thing", accessed using Ctrl+Shift+Y on all platforms.




You could then listen for the first of these commands with code like this:



    
    
    browser.commands.onCommand.addListener(function(command) {  if (command == "toggle-feature") {    console.log("toggling the feature!");  }});



### Special shortcuts



There are three special shortcuts:





  * _execute_browser_action: works like a click on the extension's [browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action).


  * _execute_page_action: works like a click on the extension's [page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions).


  * _execute_sidebar_action: opens the extension's [sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars). Only supported in Firefox, and only from Firefox version 54.




For example, this defines a key combination to click the extension's browser
action:



    
    
    "commands": {  "_execute_browser_action": {    "suggested_key": {      "default": "Ctrl+Shift+Y"    }  }}



## Shortcut values



There are two valid formats for the shortcut keys: as a key combination or as
a media key.



### Key combinations





On Macs, "Ctrl" is interpreted as "Command", so if you actually need "Ctrl",
specify "MacCtrl".





Key combinations must consist of two or three keys:





  *  **modifier** (mandatory, except for function keys). This can be any of: "Ctrl", "Alt", "Command", "MacCtrl".


  *  **secondary modifier** (optional). If supplied, this must be "Shift".


  *  **key** (mandatory). This can be any one of:  
    * the letters A-Z


    * the numbers 0-9


    * the function keys F1-F12


    * Comma, Period, Home, End, PageUp, PageDown, Space, Insert, Delete, Up, Down, Left, Right






### Media keys



Alternatively, the shortcut may be specified as one of the following media
keys:





  * "MediaNextTrack", "MediaPlayPause", "MediaPrevTrack", "MediaStop"




## Example



Define a single shortcut, using only the default:



    
    
    "commands": {  "toggle-feature": {    "suggested_key": {      "default": "Ctrl+Shift+Y"    },    "description": "Send a 'toggle-feature' event"  }}



Define two shortcuts, one with a platform-specific key combination:



    
    
    "commands": {  "toggle-feature": {    "suggested_key": {      "default": "Alt+Shift+U",      "linux": "Ctrl+Shift+U"    },    "description": "Send a 'toggle-feature' event"  },  "do-another-thing": {    "suggested_key": {      "default": "Ctrl+Shift+Y"    }  }}



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 48|  No|  Yes  
`F1-F12`|  Yes|  No| 53|  No|  Yes  
`_execute_sidebar_action`|  No|  No| 54|  No|  No  
`global`|  Yes|  No|  No|  No|  Yes  
`MediaNextTrack`|  Yes|  No|  No|  No|  Yes  
`MediaPlayPause`|  Yes|  No|  No|  No|  Yes  
`MediaPrevTrack`|  Yes|  No|  No|  No|  Yes  
`MediaStop`|  Yes|  No|  No|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes| No support No| Full
support 48| Full support Yes| No support No  
`F1-F12`| Full support Yes| No support No| Full support 53|
Full support Yes| No support No  
`_execute_sidebar_action`| No support No| No support No| Full
support 54| No support No| No support No  
`global`| Full support Yes| No support No| No support No|
Full support Yes| No support No  
`MediaNextTrack`| Full support Yes| No support No| No
support No| Full support Yes| No support No  
`MediaPlayPause`| Full support Yes| No support No| No
support No| Full support Yes| No support No  
`MediaPrevTrack`| Full support Yes| No support No| No
support No| Full support Yes| No support No  
`MediaStop`| Full support Yes| No support No| No support No|
Full support Yes| No support No  
  
]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

