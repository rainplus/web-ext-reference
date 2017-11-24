[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"page_action": {\n  "browser_style": true,\n  "default_icon": {\n    "19": "button/geo-19.png",\n    "38": "button/geo-38.png"\n  },\n  "default_title": "Whereami?",\n  "default_popup": "popup/geo.html"\n}

\n\n  
\n\n\n

A page action is an icon that your extension adds inside the browser's URL
bar.

\n

Your extension may optionally also supply an associated popup whose content is
specified using HTML, CSS, and JavaScript.

\n

If you supply a popup, then the popup is opened when the user clicks the icon,
and your JavaScript running in the popup can handle the user's interaction
with it. If you don't supply a popup, then a click event is dispatched to your
extension's [background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_pages) when the user
clicks the icon.

\n

You can also create and manipulate page actions programmatically using the
[pageAction API](/en-US/Add-ons/WebExtensions/API/pageAction).

\n

Page actions are like browser actions, except that they are associated with
particular web pages rather than with the browser as a whole. If an action is
only relevant on certain pages, then you should use a page action and display
it only on relevant pages. If an action is relevant to all pages or to the
browser itself, use a browser action.

\n

While browser actions are displayed by default, page actions are hidden by
default. They can be shown for a particular tab by calling `[pageAction.show
()](/en-US/Add-ons/WebExtensions/API/pageAction/show)`, passing in the tab's
ID.

\n

## Syntax

\n

The `page_action` key is an object that may have any of three properties, all
optional:

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`browser_style`\n| `Boolean`\n| \n

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
\n\n`default_icon`\n| `Object` or `String`\n| \n

Use this to specify an icon for the action.

\n

It's recommended that you supply two icons here, one 19x19 pixels, and one
38x38 pixels, and specify them in an object with properties named "19" and
"38", like this:

\n

    
    
    \n    "default_icon": {\n      "19": "geo-19.png",\n      "38": "geo-38.png"\n    }

\n

If you do this, then the browser will pick the right size icon for the
screen's pixel density.

\n

You can just supply a string here:

\n

    
    
    \n"default_icon": "geo.png"

\n

If you do this, then the icon will be scaled to fit the toolbar, and may
appear blurry.

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

Tooltip for the icon, displayed when the user moves their mouse over it.

\n

This is a [localizable property](/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n\n  
\n\n\n

## Example

\n

    
    
    "page_action": {\n  "default_icon": {\n    "19": "button/geo-19.png",\n    "38": "button/geo-38.png"\n  }\n}

\n

A page action with just an icon, specified in 2 different sizes. The
extension's background scripts can receive click events when the user clicks
the icon using code like this:

\n

    
    
     browser.pageAction.onClicked.addListener(handleClick);

\n

    
    
    "page_action": {\n  "default_icon": {\n    "19": "button/geo-19.png",\n    "38": "button/geo-38.png"\n  },\n  "default_title": "Whereami?",\n  "default_popup": "popup/geo.html"\n}

\n

A page action with an icon, a title, and a popup. The popup will be shown when
the user clicks the icon.

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes1| \n Yes1 2| 48| \n No| \n Yes  
`browser_style`| \n No| \n No| 48| \n No| \n No  
  
1\. SVG icons are not supported.

2\. 'default_icon' must be an object, with explicit sizes.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes

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
`browser_style`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
48| \nNo support\n\n No| \nNo support\n\n No  
  
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
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

