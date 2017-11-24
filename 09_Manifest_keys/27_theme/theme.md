[\n

\n\n\n\nType\n| `Object`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"theme": {\n  "images": {\n    "headerURL": "images/sun.jpg"\n  },\n  "colors": {\n    "accentcolor": "#CF723F",\n    "textcolor": "#000"\n  }\n}

\n\n  
\n\n\n

Use the theme key to define a static theme to apply to Firefox.

\n

\n

If your manifest.json file includes the theme key, the extension is assumed to
be a theme and any other WebExtension keys are ignored. If you want to include
a theme with an extension, please see the [`theme`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/theme "Enables browser extensions to update the browser
theme.") API.

\n

\n

## Image formats

\n

The following image formats are supported in all theme image properties:

\n

\n

  * JPEG
\n

  * PNG
\n

  * APNG
\n

  * SVG
\n

  * GIF (animated GIF isn\u2019t supported)
\n

\n

## Syntax

\n

The theme key is an object that takes the following properties:

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`images`\n| `Object`\n| \n

Mandatory.

\n

Has the following properties:

\n

\n

  * `"headerURL":` or (optionally, for Chrome compatibility) `"theme_frame":` the URL of a foreground image to be added to the header area and anchored to the upper right corner of the header area.  
\n Mandatory.

\n

  * `"additional_backgrounds":` an array of URLs for additional background images to be added to the header area and displayed behind the `"headerURL":` image. These images layer the first image in the array on top, the last image in the array at the bottom.  
\n By default all images are anchored to the upper right corner of the header
area, but their alignment and repeat behavior can be controlled by properties
of `"properties":`.  
\n Optional.

\n

\n

\n

All URLs are relative to the manifest.json file and cannot reference an
external URL.

\n

\n

\n

Images should be 200 pixels high to ensure they always fill the header space
vertically.

\n

\n\n  
\n\n`colors`\n| `Object`\n| \n

Mandatory.

\n

Has the following properties, all optional except `"accentcolor"` and
`"textcolor"`.

\n

\n

  * `"accentcolor"`: the color of the header area background, displayed in the part of the header not covered or visible through the images specified in `"headerURL"` and `"additional_backgrounds"`.
\n

  * `"frame"`: the same as `"accentcolor"`, provided for Chrome compatibility.
\n

  * `"textcolor"`: the color of the text displayed in the header area.
\n

  * `"tab_text"`: From Firefox 59, it represents the color of the selected tab. From Firefox 55 to 58, it is the same as `"textcolor"`, provided for Chrome compatibility.
\n

  * `"background_tab_text"`: it is the same as `"textcolor"`, provided for Chrome compatibility.
\n

  * `"toolbar"`: the background color for the navigation bar, the bookmarks bar, and the selected tab.
\n

  * `"toolbar_text"`: the color of toolbar text.
\n

  * `"bookmark_text"`: the same as `"toolbar_text"`, provided for Chrome compatibility. If this property and `"toolbar_text"` are both given, then the value for `"toolbar_text"` will be used.
\n

  * `"toolbar_field"`: the background color for fields in the toolbar, such as the URL bar.
\n

  * `"toolbar_field_text"`: the color of text in fields in the toolbar, such as the URL bar.
\n

  * `"toolbar_top_separator"`: the color of the line separating the top of the toolbar from the region above.
\n

  * `"toolbar_bottom_separator"`: the color of the line separating the bottom of the toolbar from the region below.
\n

  * `"toolbar_vertical_separator"`: the color of vertical separators in the toolbar.
\n

\n

See the example screenshot below to understand the parts of the browser UI
that are affected by these properties.

\n

\n

All these colors can be specified with any valid [CSS color code](/en-
US/docs/Web/CSS/color_value), except `"frame"` and `"tab_text"`, which are
specified using an RGB array, such as `"tab_text": [ 107 , 99 , 23 ]`.

\n

\n\n  
\n\n`properties`\n| `Object`\n| \n

Optional

\n

This object has two properties that affect how the `"additional_backgrounds":`
images are displayed:

\n

\n

  * `"additional_backgrounds_alignment":` an array of enumeration values defining the alignment of the corresponding `"additional_backgrounds":` array item.  
\n The alignment options include: `"bottom"`, `"center"`, `"left"`, `"right"`,
`"top"`, `"center bottom"`, `"center center"`, `"center top"`, `"left
bottom"`, `"left center"`, `"left top"`, `"right bottom"`, `"right center"`,
and `"right top"`. If not specified, defaults to `"left top"`.  
\n Optional

\n

  * `"additional_backgrounds_tiling":` an array of enumeration values defining how the corresponding `"additional_backgrounds":` array item repeats, with support for `"no-repeat"`, `"repeat"`, `"repeat-x"`, and `"repeat-y"`. If not specified, defaults to `"no-repeat"`.  
\n Optional

\n

\n\n  
\n\n\n

## Examples

\n

A basic theme must define an image to add to the header, the accent color to
use in the header, and the color of text used in the header:

\n

    
    
     "theme": {\n   "images": {\n     "headerURL": "images/sun.jpg"\n   },\n   "colors": {\n     "accentcolor": "#CF723F",\n     "textcolor": "#000"\n   }\n }

\n

Multiple images can be used to fill the header, using a blank/transparent
header image to gain control over the placement of each visible image:

\n

    
    
     "theme": {\n   "images": {\n     "headerURL": "images/blank.png",\n     "additional_backgrounds": [ "images/left.png" , "images/middle.png", "images/right.png"]\n   },\n   "properties": {\n     "additional_backgrounds_alignment": [ "left top" , "top", "right top"]\n   },\n   "colors": {\n     "accentcolor": "blue",\n     "textcolor": "#ffffff"\n   }\n }

\n

You can also fill the header with a repeating image, or images, in this case a
single image anchored in the middle top of the header and repeated across the
rest of the header:

\n

    
    
     "theme": {\n   "images": {\n     "headerURL": "images/blank.png",\n     "additional_backgrounds": [ "images/logo.png"]\n   },\n   "properties": {\n     "additional_backgrounds_alignment": [ "top" ],\n     "additional_backgrounds_tiling": [ "repeat"  ]\n   },\n   "colors": {\n     "accentcolor": "green",\n     "textcolor": "#000"\n   }\n }

\n

The following example uses all the different values for `theme.colors`:

\n

    
    
    \xa0 "theme": {\n\xa0\xa0\xa0 "images": {\n\xa0\xa0\xa0\xa0\xa0 "headerURL": "weta.png"\n\xa0\xa0\xa0 },\n\xa0\xa0\xa0\xa0 \xa0\n\xa0\xa0\xa0 "colors": {\n\xa0\xa0\xa0\xa0\xa0\xa0 "accentcolor": "darkgreen",\n\xa0\xa0\xa0\xa0\xa0\xa0 "textcolor": "white",\n\xa0\xa0\xa0\xa0\xa0\xa0 "toolbar": "blue",\n\xa0\xa0\xa0\xa0\xa0\xa0 "toolbar_text": "cyan",\n\xa0\xa0\xa0\xa0\xa0\xa0 "toolbar_field": "orange",\n\xa0\xa0\xa0\xa0\xa0\xa0 "toolbar_field_text": "green",\n\xa0\xa0\xa0\xa0\xa0\xa0 "toolbar_top_separator": "red",\n\xa0\xa0\xa0\xa0\xa0\xa0 "toolbar_bottom_separator": "white",\n\xa0\xa0\xa0\xa0\xa0\xa0 "toolbar_vertical_separator": "white"\n\xa0\xa0\xa0 }\n\xa0 }

\n

It will give you a browser that looks something like this:

\n

![](https://mdn.mozillademos.org/files/15642/theme-example.png)

\n

In this screenshot, `"toolbar_vertical_separator"` is the white vertical line
in the URL bar dividing the Reader Mode icon from the other icons.

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes| \n No| 55| \n No| \n No  
`colors.accentcolor`| \n No| \n No| 55| \n No| \n No  
`colors.background_tab_text`| \n Yes| \n No| 55| \n No| \n No  
`colors.bookmark_text`| \n Yes| \n No| \n No| \n No| \n No  
`colors.frame`| \n Yes| \n No| 55| \n No| \n No  
`colors.frame_inactive`| \n Yes| \n No| \n No| \n No| \n No  
`colors.frame_incognito`| \n Yes| \n No| \n No| \n No| \n No  
`colors.frame_incognito_inactive`| \n Yes| \n No| \n No| \n No| \n No  
`colors.ntp_background`| \n Yes| \n No| \n No| \n No| \n No  
`colors.ntp_header`| \n Yes| \n No| \n No| \n No| \n No  
`colors.ntp_link`| \n Yes| \n No| \n No| \n No| \n No  
`colors.ntp_text`| \n Yes| \n No| \n No| \n No| \n No  
`colors.tab_text`| \n Yes| \n No| 55| \n No| \n No  
`colors.textcolor`| \n No| \n No| 55| \n No| \n No  
`colors.toolbar`| \n Yes| \n No| 57| \n No| \n No  
`colors.toolbar_field`| \n No| \n No| 57| \n No| \n No  
`colors.toolbar_field_text`| \n No| \n No| 57| \n No| \n No  
`colors.toolbar_text`| \n No| \n No| 57| \n No| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`colors.accentcolor`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`colors.background_tab_text`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`colors.bookmark_text`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.frame`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`colors.frame_inactive`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.frame_incognito`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.frame_incognito_inactive`| \nFull support\n\n Yes| \nNo support\n\n
No| \nNo support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.ntp_background`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.ntp_header`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.ntp_link`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.ntp_text`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nNo support\n\n No| \nNo support\n\n No  
`colors.tab_text`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`colors.textcolor`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 55| \nNo support\n\n No| \nNo support\n\n No  
`colors.toolbar`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
`colors.toolbar_field`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
`colors.toolbar_field_text`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
`colors.toolbar_text`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
  
\n

### Chrome compatibility

\n\n\n\nFirefox property\n| Chrome property\n  
---|---  
\n\n\n\n`images/headerURL`\n| \n

`images/theme_frame`

\n

In Chrome, the image is anchored to the top left of the header and tiled if it
doesn\u2019t fill the header area.

\n\n  
\n\n`images/additional_backgrounds`\n| Not supported\n  
\n\n`colors/accentcolor`\n| `colors/frame`\n  
\n\n`colors/textcolor`\n| Incorrectly implemented as `colors/tab_text` from
Firefox 55 to 58, fixed as `colors/background_tab_text` from Firefox 59
onward\n  
\n\n`colors/toolbar_text`\n| `colors/bookmark_text`\n  
\n\n`properties/additional_backgrounds_alignment`\n| Not supported\n  
\n\n`properties/additional_backgrounds_tiling`\n| Not supported\n  
\n\n\n

In Chrome, all colors must be specified as an array of RGB values, like this:

\n

    
    
    "theme": {\n\xa0 "colors": {\n\xa0\xa0\xa0\xa0 "frame": [255, 0, 0],\n\xa0\xa0\xa0\xa0 "background_tab_text": [0, 255, 0],\n\xa0\xa0\xa0\xa0 "bookmark_text": [0, 0, 255]\n\xa0 }\n}

\n

From Firefox 59 onward, both the array form and the CSS color form are
accepted for all properties. Before that, `colors/frame` and `colors/tab_text`
required the array form, while other properties required the CSS color form.

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

