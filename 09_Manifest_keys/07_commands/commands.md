[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"commands": {\n  "toggle-feature": {\n    "suggested_key": {\n      "default": "Ctrl+Shift+Y",\n      "linux": "Ctrl+Shift+U"\n    },\n    "description": "Send a 'toggle-feature' event"\n  }\n}

\n\n  
\n\n\n

Use the `commands` key to define one or more keyboard shortcuts for your
extension.

\n

Each shortcut is defined with a name, a combination of keys, and a
description. Once you've defined some commands in manifest.json, you can
listen for the associated key combinations using the [`commands`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/commands "Listen for the user
executing commands that you have registered using the commands manifest.json
key.") JavaScript API.

\n

## Syntax

\n

The `commands` key is an object, and each shortcut is a property of it. The
property's name is the name of the shortcut.

\n

Each shortcut is itself an object, which has up to two properties:

\n

\n

  * `suggested_key`: this defines the combination of keys
\n

  * `description`: a string that describes this shortcut
\n

\n

The `suggested_key` property is itself an object, that may have any of the
following properties, which are all strings:

\n

\n

  * `"default"`, `"mac"`, `"linux"`, `"windows"`, `"chromeos"`, `"android"`, `"ios"`
\n

\n

The value of each property is the keyboard shortcut for the command on the
given platform, given as a string containing the keys separated by "+". The
value for `"default"` is used on all platforms that are not explicitly listed.

\n

For example:

\n

    
    
    "commands": {\n  "toggle-feature": {\n    "suggested_key": {\n      "default": "Alt+Shift+U",\n      "linux": "Ctrl+Shift+U"\n    },\n    "description": "Send a 'toggle-feature' event to the extension"\n  },\n  "do-another-thing": {\n    "suggested_key": {\n      "default": "Ctrl+Shift+Y"\n    }\n  }\n}

\n

This defines two shortcuts:

\n

\n

  * one named "toggle-feature", accessed using Ctrl+Shift+U on Linux, and Alt+Shift+U on all other platforms
\n

  * one named "do-another-thing", accessed using Ctrl+Shift+Y on all platforms.
\n

\n

You could then listen for the first of these commands with code like this:

\n

    
    
    browser.commands.onCommand.addListener(function(command) {\n  if (command == "toggle-feature") {\n    console.log("toggling the feature!");\n  }\n});

\n

### Special shortcuts

\n

There are three special shortcuts:

\n

\n

  * _execute_browser_action: works like a click on the extension's [browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action).
\n

  * _execute_page_action: works like a click on the extension's [page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions).
\n

  * _execute_sidebar_action: opens the extension's [sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars). Only supported in Firefox, and only from Firefox version 54.
\n

\n

For example, this defines a key combination to click the extension's browser
action:

\n

    
    
    "commands": {\n  "_execute_browser_action": {\n    "suggested_key": {\n      "default": "Ctrl+Shift+Y"\n    }\n  }\n}

\n

## Shortcut values

\n

There are two valid formats for the shortcut keys: as a key combination or as
a media key.

\n

### Key combinations

\n

\n

On Macs, "Ctrl" is interpreted as "Command", so if you actually need "Ctrl",
specify "MacCtrl".

\n

\n

Key combinations must consist of two or three keys:

\n

\n

  *  **modifier** (mandatory, except for function keys). This can be any of: "Ctrl", "Alt", "Command", "MacCtrl".
\n

  *  **secondary modifier** (optional). If supplied, this must be "Shift".
\n

  *  **key** (mandatory). This can be any one of:\n  \n
    * the letters A-Z
\n

    * the numbers 0-9
\n

    * the function keys F1-F12
\n

    * Comma, Period, Home, End, PageUp, PageDown, Space, Insert, Delete, Up, Down, Left, Right
\n\n

\n

\n

### Media keys

\n

Alternatively, the shortcut may be specified as one of the following media
keys:

\n

\n

  * "MediaNextTrack", "MediaPlayPause", "MediaPrevTrack", "MediaStop"
\n

\n

## Example

\n

Define a single shortcut, using only the default:

\n

    
    
    "commands": {\n  "toggle-feature": {\n    "suggested_key": {\n      "default": "Ctrl+Shift+Y"\n    },\n    "description": "Send a 'toggle-feature' event"\n  }\n}

\n

Define two shortcuts, one with a platform-specific key combination:

\n

    
    
    "commands": {\n  "toggle-feature": {\n    "suggested_key": {\n      "default": "Alt+Shift+U",\n      "linux": "Ctrl+Shift+U"\n    },\n    "description": "Send a 'toggle-feature' event"\n  },\n  "do-another-thing": {\n    "suggested_key": {\n      "default": "Ctrl+Shift+Y"\n    }\n  }\n}

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 48| \n No| \n Yes  
`F1-F12`| \n Yes| \n No| 53| \n No| \n Yes  
`_execute_sidebar_action`| \n No| \n No| 54| \n No| \n No  
`global`| \n Yes| \n No| \n No| \n No| \n Yes  
`MediaNextTrack`| \n Yes| \n No| \n No| \n No| \n Yes  
`MediaPlayPause`| \n Yes| \n No| \n No| \n No| \n Yes  
`MediaPrevTrack`| \n Yes| \n No| \n No| \n No| \n Yes  
`MediaStop`| \n Yes| \n No| \n No| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 48| \nFull support\n\n Yes| \nNo support\n\n No  
`F1-F12`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 53|
\nFull support\n\n Yes| \nNo support\n\n No  
`_execute_sidebar_action`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 54| \nNo support\n\n No| \nNo support\n\n No  
`global`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
`MediaNextTrack`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`MediaPlayPause`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`MediaPrevTrack`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`MediaStop`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n No|
\nFull support\n\n Yes| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

