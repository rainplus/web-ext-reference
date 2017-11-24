[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"background": {\n  "scripts": ["background.js"]\n}

\n\n  
\n\n\n

Use the `background` key to include one or more background scripts, and
optionally a background page in your extension.

\n

Background scripts are the place to put code that needs to maintain long-term
state, or perform long-term operations, independently of the lifetime of any
particular web pages or browser windows.

\n

Background scripts are loaded as soon as the extension is loaded and stay
loaded until the extension is disabled or uninstalled. You can use any of the
WebExtension APIs in the script, as long as you have requested the necessary
[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

\n

See the "Background pages" section in [Anatomy of an extension](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_pages) for some more
details.

\n

The `background` key is an object that may have one of the following two
properties, both optional:

\n\n\n\n`"scripts"`\n| \n

An array of strings, each of which is a path to a JavaScript source. The path
is relative to the manifest.json file itself. These are the background scripts
that will be included in the extension.

\n

The scripts share the same `window` global.

\n

The scripts are loaded in the order they appear in the array.

\n

 **Note that there is a bug affecting Firefox versions earlier than 50** :
when the Firefox debugger is open, scripts are not always loaded in the order
given in the array. To work around this bug, you can use the `"page"` property
and include background scripts from the page using `<script>` tags. This bug
is fixed in Firefox 50, and from that point on, scripts are always loaded in
the order given in the array.

\n

\n

 **Note:** If you want to fetch a script from a remote location with the
`<script>` tag (e.g. `<script src =
"https://code.jquery.com/jquery-1.7.1.min.js">`), you will also have to change
the `content_security_policy` key in the manifest.json file of your extension.

\n

\n\n  
---|---  
\n\n`"page"`\n| \n

If you specify `"scripts"`, then an empty page will be created for your
scripts to run in.

\n

If you need some particular content in the page, you can define your own page
using the `"page"` option.

\n

If you use this property, you can no longer specify background scripts using
`"scripts"`, but you can\xa0 include your own scripts from the page, just like
in a normal web page.

\n\n  
\n\n\n

## Example

\n

    
    
    \xa0 "background": {\n\xa0\xa0\xa0 "scripts": ["jquery.js", "my-background.js"]\n\xa0 }

\n

Load two background scripts.

\n

    
    
      "background": {\n    "page": "my-background.html"\n  }

\n

Load a custom background page.

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n Yes1| 48| 48| \n Yes  
`persistent`| \n Yes| \n Yes| \n No| \n No| \n Yes  
  
1\. The 'persistent' property is mandatory.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __The 'persistent' property is mandatory.
|  \nFull support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
`persistent`| \nFull support\n\n Yes| \nFull support\n\n Yes| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
  
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

