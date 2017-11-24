[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"sidebar_action": {\n  "default_icon": {\n    "16": "button/geo-16.png",\n    "32": "button/geo-32.png"\n  },\n  "default_title": "My sidebar",\n  "default_panel": "sidebar/sidebar.html"\n}

\n\n  
\n\n\n

A [sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars) is a pane that
is displayed at the left-hand side of the browser window, next to the web
page. The browser provides a UI that enables the user to see the currently
available sidebars and to select a sidebar to display.

\n

The sidebar_action key enables you to define the default properties for the
sidebar. You can change these properties at runtime using the [`sidebarAction
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction "Gets and sets
properties of an extension's sidebar.") API.

\n

## Syntax

\n

The `sidebar_action` key is an object that may have any of the properties
listed below. The only mandatory property is `default_panel`.

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`browser_style`\n| `Boolean`\n| \n

Optional, defaulting to `true`.

\n

Use this to include a stylesheet in your popup that will make it look
consistent with the browser's UI and with other extensions that use the
`browser_style` property.

\n\n  
\n\n`default_icon`\n| `Object` or `String`\n| \n

Use this to specify one or more icons for the sidebar. The icon is shown in
the browser's UI for opening and closing sidebars.

\n

Icons are specified as URLs relative to the manifest.json file itself.

\n

You can specify a single icon file by supplying a string here:

\n

    
    
    \n"default_icon": "path/to/geo.svg"

\n

To specify multiple icons in different sizes, specify an object here. The name
of each property is the icon's height in pixels, and must be convertible to an
integer. The value is the URL. For example:

\n

    
    
    \n    "default_icon": {\n      "16": "path/to/geo-16.png",\n      "32": "path/to/geo-32.png"\n    }

\n

See [Choosing icon sizes](/en-US/Add-
ons/WebExtensions/manifest.json/browser_action#Choosing_icon_sizes) for more
guidance on this.

\n

This property is optional: if it is omitted, the sidebar doesn't get an icon.

\n\n  
\n\n`default_panel`\n| `String`\n| \n

The path to an HTML file that specifies the sidebar's contents.

\n

The HTML file may include CSS and JavaScript files using `[<link>](/en-
US/docs/Web/HTML/Element/link)` and `[<script>](/en-
US/docs/Web/HTML/Element/script)` elements, just like a normal web page.

\n

Unlike a normal web page, JavaScript running in the panel can access all the
[WebExtension APIs](/en-US/Add-ons/WebExtensions/API) (subject, of course, to
the extension having the appropriate [permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)).

\n

This property is mandatory.

\n

This is a [localizable property](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n\n  
\n\n`default_title`\n| `String`\n| \n

Title for the sidebar. This is used in the browser UI for listing and opening
sidebars, and is displayed at the top of the sidebar when it is open.

\n

This property is optional: if it is omitted, the sidebar's title is the
extension's `[name](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/name)`.

\n

This is a [localizable property](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n\n  
\n\n\n

## Example

\n

    
    
    "sidebar_action": {\n\xa0 "default_icon": "sidebar.svg",\n\xa0 "default_title": "My sidebar!",\n\xa0 "default_panel": "sidebar.html",\n  "browser_style": true\n}

\n

For a simple example of an extension that uses a sidebar, see [annotate-
page](https://github.com/mdn/webextensions-examples/tree/master/annotate-
page).

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n No| \n No| 54| \n No| \n Yes  
`browser_style`| \n No| \n No| 55| \n No| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
54| \nFull support\n\n Yes| \nNo support\n\n No  
`browser_style`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
55| \nNo support\n\n No| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

