[

Type| `Object`  
---|---  
Mandatory| No  
Example| 

    
    
    "browser_action": {  "browser_style": true,  "default_icon": {    "16": "button/geo-16.png",    "32": "button/geo-32.png"  },  "default_title": "Whereami?",  "default_popup": "popup/geo.html",  "theme_icons": [{\xa0\xa0\xa0 "light": "icons/geo-32-light.png",\xa0\xa0\xa0 "dark": "icons/geo-32.png",\xa0\xa0\xa0 "size": 32  }]}

  


A browser action is a button that your extension adds to the browser's
toolbar. The button has an icon, and may optionally have a popup whose content
is specified using HTML, CSS, and JavaScript.



If you supply a popup, then the popup is opened when the user clicks the
button, and your JavaScript running in the popup can handle the user's
interaction with it. If you don't supply a popup, then a click event is
dispatched to your extension's [background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts) when the user
clicks the button.



You can also create and manipulate browser actions programmatically using the
[browserAction API](/en-US/Add-ons/WebExtensions/API/browserAction).



## Syntax



The `browser_action` key is an object that may have any of the following
properties, all optional:

Name| Type| Description  
---|---|---  
`browser_style`| `Boolean`| 

New in Firefox 48



Optional, defaulting to `false`.



Use this to include a stylesheet in your popup that will make it look
consistent with the browser's UI and with other extensions that use the
`browser_style` property. Although this key defaults to `false`, it's
recommended that you include it and set it to `true`.



In Firefox, the stylesheet can be seen at
chrome://browser/content/extension.css, or chrome://browser/content/extension-
mac.css on OS X.



The [Firefox Style Guide](https://firefoxux.github.io/StyleGuide/#/controls)
describes the classes you can apply to elements in the popup in order to get
particular styles.



The [latest-download](https://github.com/mdn/webextensions-
examples/tree/master/latest-download) example extension uses `browser_style`
in its popup.

  
`default_area`| `String`| 

New in Firefox 54



Defines the part of the browser in which the button is initially placed. This
is a string that may take one of four values:





  * "navbar": the button is placed in the main browser toolbar, alongside the URL bar.


  * "menupanel": the button is placed in a popup panel.


  * "tabstrip": the button is placed in the toolbar that contains browser tabs.


  * "personaltoolbar": the button is placed in the bookmarks toolbar.




This property is only supported in Firefox.



This property is optional, and defaults to "navbar".



An extension can't change the location of the button after it has been
installed, but the user may be able to move the button using the browser's
built-in UI customization mechanism.

  
`default_icon`| `Object` or `String`| 

Use this to specify one or more icons for the browser action. The icon is
shown in the browser toolbar by default.



Icons are specified as URLs relative to the manifest.json file itself.



You can specify a single icon file by supplying a string here:



    
    
    "default_icon": "path/to/geo.svg"



To specify multiple icons in different sizes, specify an object here. The name
of each property is the icon's height in pixels, and must be convertible to an
integer. The value is the URL. For example:



    
    
        "default_icon": {      "16": "path/to/geo-16.png",      "32": "path/to/geo-32.png"    }



See [Choosing icon sizes](/en-US/Add-
ons/WebExtensions/manifest.json/browser_action#Choosing_icon_sizes) for more
guidance on this.

  
`default_popup`| `String`| 

The path to an HTML file containing the specification of the popup.



The HTML file may include CSS and JavaScript files using `[<link>](/en-
US/docs/Web/HTML/Element/link)` and `[<script>](/en-
US/docs/Web/HTML/Element/script)` elements, just like a normal web page.



Unlike a normal web page, JavaScript running in the popup can access all the
[WebExtension APIs](/en-US/Add-ons/WebExtensions/API) (subject, of course, to
the extension having the appropriate [permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)).



This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

  
`default_title`| `String`| 

Tooltip for the button, displayed when the user moves their mouse over it. If
the button is added to the browser's menu panel, this is also shown under the
app icon.



This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

  
`theme_icons`| `Array`| 

This property enables you to specify different icons for dark and light
themes.



If this property is present, it's an array containing at least one
`ThemeIcons` object. A `ThemeIcons` object contains three properties, all
mandatory:



`"dark"`

    A URL pointing to an icon. This icon will be selected when themes with
dark text are active (e.g. Firefox's Light theme, and the Default theme if no
default_icon is specified).

`"light"`

    A URL pointing to an icon. This icon will be selected when themes with
light text are active (e.g. Firefox's Dark theme).

`"size"`

    The size of the two icons in pixels.



Icons are specified as URLs relative to the manifest.json file itself.



Providing multiple `ThemeIcons` objects enables you to supply a set of icon
pairs in different sizes.

  


## Choosing icon sizes



The browser action's icon may need to be displayed in different sizes in
different contexts:





  * The icon is displayed by default in the browser toolbar, but the user can move it into the browser's menu panel (the panel that opens when the user clicks the "hamburger" icon). The icon in the toolbar is smaller than the icon in the menu panel.


  * On a high-density display like a Retina screen, icons needs to be twice as big.




If the browser can't find an icon of the right size in a given situation, it
will pick the best match and scale it. Scaling may make the icon appear
blurry, so it's important to choose icon sizes carefully.



There are two main approaches to this. You can supply a single icon as an SVG
file, and it will be scaled correctly:



    
    
    "default_icon": "path/to/geo.svg"



Alternatively, you can supply several icons in different sizes, and the
browser will pick the best match.



In Firefox:





  * The default height and width for icons in the toolbar is 16\xa0* `[window.devicePixelRatio](/en-US/docs/Web/API/Window/devicePixelRatio)`.


  * The default height and width for icons in the menu panel is 32 * `[window.devicePixelRatio](/en-US/docs/Web/API/Window/devicePixelRatio)`.




So you can specify icons that match exactly, on both normal and Retina
displays, by supplying three icon files, and specifying them like this:



    
    
        "default_icon": {      "16": "path/to/geo-16.png",      "32": "path/to/geo-32.png",      "64": "path/to/geo-64.png"    }



If Firefox can't find an exact match for the size it wants, then it will pick
the smallest icon specified that's bigger than the ideal size. If all icons
are smaller than the ideal size, it will pick the biggest icon specified.



## Example



    
    
    "browser_action": {  "default_icon": {    "16": "button/geo-16.png",    "32": "button/geo-32.png"  }}



A browser action with just an icon, specified in 2 different sizes. The
extension's background scripts can receive click events when the user clicks
the icon using code like this:



    
    
     browser.browserAction.onClicked.addListener(handleClick);



    
    
    "browser_action": {  "default_icon": {    "16": "button/geo-16.png",    "32": "button/geo-32.png"  },  "default_title": "Whereami?",  "default_popup": "popup/geo.html"}



A browser action with an icon, a title, and a popup. The popup will be shown
when the user clicks the button.



For a simple, but complete, extension that uses a browser action, see the
[walkthrough tutorial](/en-US/Add-ons/WebExtensions/Your_second_WebExtension).



## Browser compatibility



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  Yes| 48| 55|  Yes  
`browser_style`|  No|  No| 48|  No|  No  
`default_area`|  No|  No| 54|  No|  No  
`default_icon`|  Yes1|  Yes1 2| 48|  No|  Yes  
`default_popup`|  Yes|  Yes| 48| 57|  Yes  
`default_title`|  Yes|  Yes| 48| 553|  Yes  
`theme_icons`|  No|  No| 56|  No|  No  
  
1\. SVG icons are not supported.

2\. 'default_icon' must be an object, with explicit sizes.

3\. Browser actions are presented as menu items, and the title is the menu
item's label.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 55  
`browser_style`| No support No| No support No| Full support
48| No support No| No support No  
`default_area`| No support No| No support No| Full support
54| No support No| No support No  
`default_icon`| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __SVG icons are not supported.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __SVG icons are not supported.
     Notes __'default_icon' must be an object, with explicit sizes.
|  Full support 48| Full support Yes| No support No  
`default_popup`| Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 57  
`default_title`| Full support Yes| Full support Yes| Full
support 48| Full support Yes| Full support 55

Notes __

Full support 55

Notes __

     Notes __Browser actions are presented as menu items, and the title is the menu item's label.  
`theme_icons`|  No support No| No support No| Full support
56| No support No| No support No  
  
]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

