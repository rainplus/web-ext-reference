[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"browser_action": {\n  "browser_style": true,\n  "default_icon": {\n    "16": "button/geo-16.png",\n    "32": "button/geo-32.png"\n  },\n  "default_title": "Whereami?",\n  "default_popup": "popup/geo.html",\n  "theme_icons": [{\n\xa0\xa0\xa0 "light": "icons/geo-32-light.png",\n\xa0\xa0\xa0 "dark": "icons/geo-32.png",\n\xa0\xa0\xa0 "size": 32\n  }]\n}

\n\n  
\n\n\n

A browser action is a button that your extension adds to the browser's
toolbar. The button has an icon, and may optionally have a popup whose content
is specified using HTML, CSS, and JavaScript.

\n

If you supply a popup, then the popup is opened when the user clicks the
button, and your JavaScript running in the popup can handle the user's
interaction with it. If you don't supply a popup, then a click event is
dispatched to your extension's [background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts) when the user
clicks the button.

\n

You can also create and manipulate browser actions programmatically using the
[browserAction API](/en-US/Add-ons/WebExtensions/API/browserAction).

\n

## Syntax

\n

The `browser_action` key is an object that may have any of the following
properties, all optional:

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`browser_style`\n| `Boolean`\n| \n

New in Firefox 48

\n

Optional, defaulting to `false`.

\n

Use this to include a stylesheet in your popup that will make it look
consistent with the browser's UI and with other extensions that use the
`browser_style` property. Although this key defaults to `false`, it's
recommended that you include it and set it to `true`.

\n

In Firefox, the stylesheet can be seen at
chrome://browser/content/extension.css, or chrome://browser/content/extension-
mac.css on OS X.

\n

The [Firefox Style Guide](https://firefoxux.github.io/StyleGuide/#/controls)
describes the classes you can apply to elements in the popup in order to get
particular styles.

\n

The [latest-download](https://github.com/mdn/webextensions-
examples/tree/master/latest-download) example extension uses `browser_style`
in its popup.

\n\n  
\n\n`default_area`\n| `String`\n| \n

New in Firefox 54

\n

Defines the part of the browser in which the button is initially placed. This
is a string that may take one of four values:

\n

\n

  * "navbar": the button is placed in the main browser toolbar, alongside the URL bar.
\n

  * "menupanel": the button is placed in a popup panel.
\n

  * "tabstrip": the button is placed in the toolbar that contains browser tabs.
\n

  * "personaltoolbar": the button is placed in the bookmarks toolbar.
\n

\n

This property is only supported in Firefox.

\n

This property is optional, and defaults to "navbar".

\n

An extension can't change the location of the button after it has been
installed, but the user may be able to move the button using the browser's
built-in UI customization mechanism.

\n\n  
\n\n`default_icon`\n| `Object` or `String`\n| \n

Use this to specify one or more icons for the browser action. The icon is
shown in the browser toolbar by default.

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

\n\n  
\n\n`default_popup`\n| `String`\n| \n

The path to an HTML file containing the specification of the popup.

\n

The HTML file may include CSS and JavaScript files using `[<link>](/en-
US/docs/Web/HTML/Element/link)` and `[<script>](/en-
US/docs/Web/HTML/Element/script)` elements, just like a normal web page.

\n

Unlike a normal web page, JavaScript running in the popup can access all the
[WebExtension APIs](/en-US/Add-ons/WebExtensions/API) (subject, of course, to
the extension having the appropriate [permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)).

\n

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n\n  
\n\n`default_title`\n| `String`\n| \n

Tooltip for the button, displayed when the user moves their mouse over it. If
the button is added to the browser's menu panel, this is also shown under the
app icon.

\n

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n\n  
\n\n`theme_icons`\n| `Array`\n| \n

This property enables you to specify different icons for dark and light
themes.

\n

If this property is present, it's an array containing at least one
`ThemeIcons` object. A `ThemeIcons` object contains three properties, all
mandatory:

\n

\n`"dark"`

\n    A URL pointing to an icon. This icon will be selected when themes with
dark text are active (e.g. Firefox's Light theme, and the Default theme if no
default_icon is specified).

\n`"light"`

\n    A URL pointing to an icon. This icon will be selected when themes with
light text are active (e.g. Firefox's Dark theme).

\n`"size"`

\n    The size of the two icons in pixels.

\n\n

Icons are specified as URLs relative to the manifest.json file itself.

\n

Providing multiple `ThemeIcons` objects enables you to supply a set of icon
pairs in different sizes.

\n\n  
\n\n\n

## Choosing icon sizes

\n

The browser action's icon may need to be displayed in different sizes in
different contexts:

\n

\n

  * The icon is displayed by default in the browser toolbar, but the user can move it into the browser's menu panel (the panel that opens when the user clicks the "hamburger" icon). The icon in the toolbar is smaller than the icon in the menu panel.
\n

  * On a high-density display like a Retina screen, icons needs to be twice as big.
\n

\n

If the browser can't find an icon of the right size in a given situation, it
will pick the best match and scale it. Scaling may make the icon appear
blurry, so it's important to choose icon sizes carefully.

\n

There are two main approaches to this. You can supply a single icon as an SVG
file, and it will be scaled correctly:

\n

    
    
    "default_icon": "path/to/geo.svg"

\n

Alternatively, you can supply several icons in different sizes, and the
browser will pick the best match.

\n

In Firefox:

\n

\n

  * The default height and width for icons in the toolbar is 16\xa0* `[window.devicePixelRatio](/en-US/docs/Web/API/Window/devicePixelRatio)`.
\n

  * The default height and width for icons in the menu panel is 32 * `[window.devicePixelRatio](/en-US/docs/Web/API/Window/devicePixelRatio)`.
\n

\n

So you can specify icons that match exactly, on both normal and Retina
displays, by supplying three icon files, and specifying them like this:

\n

    
    
        "default_icon": {\n      "16": "path/to/geo-16.png",\n      "32": "path/to/geo-32.png",\n      "64": "path/to/geo-64.png"\n    }

\n

If Firefox can't find an exact match for the size it wants, then it will pick
the smallest icon specified that's bigger than the ideal size. If all icons
are smaller than the ideal size, it will pick the biggest icon specified.

\n

## Example

\n

    
    
    "browser_action": {\n  "default_icon": {\n    "16": "button/geo-16.png",\n    "32": "button/geo-32.png"\n  }\n}

\n

A browser action with just an icon, specified in 2 different sizes. The
extension's background scripts can receive click events when the user clicks
the icon using code like this:

\n

    
    
     browser.browserAction.onClicked.addListener(handleClick);

\n

    
    
    "browser_action": {\n  "default_icon": {\n    "16": "button/geo-16.png",\n    "32": "button/geo-32.png"\n  },\n  "default_title": "Whereami?",\n  "default_popup": "popup/geo.html"\n}

\n

A browser action with an icon, a title, and a popup. The popup will be shown
when the user clicks the button.

\n

For a simple, but complete, extension that uses a browser action, see the
[walkthrough tutorial](/en-US/Add-ons/WebExtensions/Your_second_WebExtension).

\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n Yes| 48| 55| \n Yes  
`browser_style`| \n No| \n No| 48| \n No| \n No  
`default_area`| \n No| \n No| 54| \n No| \n No  
`default_icon`| \n Yes1| \n Yes1 2| 48| \n No| \n Yes  
`default_popup`| \n Yes| \n Yes| 48| 57| \n Yes  
`default_title`| \n Yes| \n Yes| 48| 553| \n Yes  
`theme_icons`| \n No| \n No| 56| \n No| \n No  
  
1\. SVG icons are not supported.

2\. 'default_icon' must be an object, with explicit sizes.

3\. Browser actions are presented as menu items, and the title is the menu
item's label.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 55  
`browser_style`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
48| \nNo support\n\n No| \nNo support\n\n No  
`default_area`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
54| \nNo support\n\n No| \nNo support\n\n No  
`default_icon`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __SVG icons are not supported.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __SVG icons are not supported.
     Notes __'default_icon' must be an object, with explicit sizes.
|  \nFull support\n\n 48| \nFull support\n\n Yes| \nNo support\n\n No  
`default_popup`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 57  
`default_title`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 55

Notes __

\nFull support\n\n 55

Notes __

     Notes __Browser actions are presented as menu items, and the title is the menu item's label.  
`theme_icons`|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
56| \nNo support\n\n No| \nNo support\n\n No  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

