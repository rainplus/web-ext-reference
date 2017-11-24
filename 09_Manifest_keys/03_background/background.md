Type | `Object`  
---|---  
Mandatory | No  
Example |

    
    
    "background": {
      "scripts": ["background.js"]
    }  
  
Use the `background` key to include one or more background scripts, and
optionally a background page in your extension.

Background scripts are the place to put code that needs to maintain long-term
state, or perform long-term operations, independently of the lifetime of any
particular web pages or browser windows.

Background scripts are loaded as soon as the extension is loaded and stay
loaded until the extension is disabled or uninstalled. You can use any of the
WebExtension APIs in the script, as long as you have requested the necessary
[permissions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

See the "Background pages" section in [Anatomy of an extension](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_pages) for some more
details.

The `background` key is an object that may have one of the following two
properties, both optional:

`"scripts"` |

An array of strings, each of which is a path to a JavaScript source. The path
is relative to the manifest.json file itself. These are the background scripts
that will be included in the extension.

The scripts share the same `window` global.

The scripts are loaded in the order they appear in the array.

**Note that there is a bug affecting Firefox versions earlier than 50** : when
the Firefox debugger is open, scripts are not always loaded in the order given
in the array. To work around this bug, you can use the `"page"` property and
include background scripts from the page using `<script>` tags. This bug is
fixed in Firefox 50, and from that point on, scripts are always loaded in the
order given in the array.

**Note:** If you want to fetch a script from a remote location with the
`<script>` tag (e.g. `<script src =
"https://code.jquery.com/jquery-1.7.1.min.js">`), you will also have to change
the `content_security_policy` key in the manifest.json file of your extension.  
  
---|---  
`"page"` |

If you specify `"scripts"`, then an empty page will be created for your
scripts to run in.

If you need some particular content in the page, you can define your own page
using the `"page"` option.

If you use this property, you can no longer specify background scripts using
`"scripts"`, but you can  include your own scripts from the page, just like in
a normal web page.  
  
## Example

    
    
      "background": {
        "scripts": ["jquery.js", "my-background.js"]
      }

Load two background scripts.

    
    
      "background": {
        "page": "my-background.html"
      }

Load a custom background page.

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  Yes1| 48| 48|  Yes  
`persistent`|  Yes|  Yes|  No|  No|  Yes  
  
1\. The 'persistent' property is mandatory.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __The 'persistent' property is mandatory.
|  Full support 48|  Full support Yes|  Full support 48  
`persistent`|  Full support Yes|  Full support Yes|  No support No|  Full
support Yes|  No support No

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[
Full support

]: Full support

  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

