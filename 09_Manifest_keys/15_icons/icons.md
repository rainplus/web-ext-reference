[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"icons": {\n  "48": "icon.png",\n  "96": "icon@2x.png"\n}

\n\n  
\n\n\n

The `icons` key specifies icons for your extension. Those icons will be used
to represent the extension in components such as the Add-ons Manager.

\n

It consists of key-value pairs of image size in px and image path relative to
the root directory of the extension.

\n

If `icons` is not supplied, a standard extension icon will be used by default.

\n

You should supply at least a main extension icon, ideally 48x48 px in size.
This is the default icon that will be used in the Add-ons Manager. You may,
however, supply icons of any size and Firefox will attempt to find the best
icon to display in different components.

\n

Firefox will consider the screen resolution when choosing an icon. To deliver
the best visual experience to users with high-resolution displays, such as
Retina displays, provide double-sized versions of all your icons.

\n

## Example

\n

The keys in the `icons` object specify the icon size in px, values specify the
relative icon path. This example contains a 48px extension icon and a larger
version for high-resolution displays.

\n

    
    
    "icons": {\n  "48": "icon.png",\n  "96": "icon@2x.png"\n}

\n

## SVG

\n

You can use SVG and the browser will scale your icon appropriately. There are
currently two caveats though:

\n

\n

  1. You need to specify a viewBox in the image. E.g.:\n 
    
        <svg viewBox="0 0 48 48" width="48" height="48" ...

\n

\n

  2. Even though you can use one file, you still need to specify various size of the icon in your manifest. E.g.:\n 
    
        "icons": {\n  "48": "icon.svg",\n  "96": "icon.svg"\n}

\n

\n

\n

\n

If you are using a program like Inkscape for creating SVG, you might want to
save it as a "plain SVG". Firefox might be confused by various special
namespaces and not display your icon.

\n

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

