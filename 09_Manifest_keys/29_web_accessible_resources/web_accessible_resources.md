[\n

\n\n\n\nType\n| `Array`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"web_accessible_resources": [\n  "images/my-image.png"\n]

\n\n  
\n\n\n

Sometimes you will want to package some resources - for example, images, HTML,
CSS, or JavaScript - with your extension, and make them available to web
pages.

\n

For example, the "beastify" example extension used in the [walkthrough
tutorial](/en-US/Add-ons/WebExtensions/Walkthrough) replaces images in a web
page with images of some beasts, by setting the `src` attribute of any `[<img
>](/en-US/docs/Web/HTML/Element/img)` elements. The images are packaged with
the extension, and for the web page to be able to load them, they must be made
web accessible.

\n

The `web_accessible_resources` key lists all packaged resources that you want
to make available to web pages in this way. You specify them as paths relative
to the manifest.json file.

\n

The files will then be available using a URL like: "moz-extension://<random-
UUID>/<path/to/resource>".

\n

\n

This UUID is randomly generated for every browser instance and is **not** your
extension's ID. This prevents websites from fingerprinting the extensions a
user has installed.

\n

\n

For example, consider an entry like this:

\n

    
    
      "web_accessible_resources": ["images/my-image.png"]

\n

If the random UUID is `944cfddf-7a95-3c47-bd9a-663b3ce8d699`, then this
resource will be available at the following URL:

\n

moz-extension://944cfddf-7a95-3c47-bd9a-663b3ce8d699/images/my-image.png

\n

Entries can contain wildcards, for example:

\n

    
    
      "web_accessible_resources": ["images/*.png"]

\n

Will also work.

\n

The easiest way to get this URL is to use the `[browser.extension.getURL](/en-
US/Add-ons/WebExtensions/API/extension#getURL)` API, and give it the path
relative to manifest.json:

\n

    
    
    browser.extension.getURL("images/my-image.png");

\n

Note that content scripts don't need to be listed as web accessible resources.

\n

## Example

\n

    
    
    "web_accessible_resources": ["images/my-image.png"]

\n

Make the file at "images/my-image.png" web accessible.

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n Yes| 48| 48| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 48| \nFull support\n\n Yes| \nFull support\n\n 48  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

