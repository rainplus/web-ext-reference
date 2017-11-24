Type | `Object`  
---|---  
Mandatory | No  
Example |

    
    
    "theme": {
      "images": {
        "headerURL": "images/sun.jpg"
      },
      "colors": {
        "accentcolor": "#CF723F",
        "textcolor": "#000"
      }
    }  
  
Use the theme key to define a static theme to apply to Firefox.

If your manifest.json file includes the theme key, the extension is assumed to
be a theme and any other WebExtension keys are ignored. If you want to include
a theme with an extension, please see the [`theme`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/theme "Enables browser extensions to update the browser
theme.") API.

## Image formats

The following image formats are supported in all theme image properties:

  * JPEG
  * PNG
  * APNG
  * SVG
  * GIF (animated GIF isn’t supported)

## Syntax

The theme key is an object that takes the following properties:

Name | Type | Description  
---|---|---  
`images` | `Object` |

Mandatory.

Has the following properties:

  * `"headerURL":` or (optionally, for Chrome compatibility) `"theme_frame":` the URL of a foreground image to be added to the header area and anchored to the upper right corner of the header area.  
Mandatory.

  * `"additional_backgrounds":` an array of URLs for additional background images to be added to the header area and displayed behind the `"headerURL":` image. These images layer the first image in the array on top, the last image in the array at the bottom.  
By default all images are anchored to the upper right corner of the header
area, but their alignment and repeat behavior can be controlled by properties
of `"properties":`.  
Optional.

All URLs are relative to the manifest.json file and cannot reference an
external URL.

Images should be 200 pixels high to ensure they always fill the header space
vertically.  
  
`colors` | `Object` |

Mandatory.

Has the following properties, all optional except `"accentcolor"` and
`"textcolor"`.

  * `"accentcolor"`: the color of the header area background, displayed in the part of the header not covered or visible through the images specified in `"headerURL"` and `"additional_backgrounds"`.
  * `"frame"`: the same as `"accentcolor"`, provided for Chrome compatibility.
  * `"textcolor"`: the color of the text displayed in the header area.
  * `"tab_text"`: From Firefox 59, it represents the color of the selected tab. From Firefox 55 to 58, it is the same as `"textcolor"`, provided for Chrome compatibility.
  * `"background_tab_text"`: it is the same as `"textcolor"`, provided for Chrome compatibility.
  * `"toolbar"`: the background color for the navigation bar, the bookmarks bar, and the selected tab.
  * `"toolbar_text"`: the color of toolbar text.
  * `"bookmark_text"`: the same as `"toolbar_text"`, provided for Chrome compatibility. If this property and `"toolbar_text"` are both given, then the value for `"toolbar_text"` will be used.
  * `"toolbar_field"`: the background color for fields in the toolbar, such as the URL bar.
  * `"toolbar_field_text"`: the color of text in fields in the toolbar, such as the URL bar.
  * `"toolbar_top_separator"`: the color of the line separating the top of the toolbar from the region above.
  * `"toolbar_bottom_separator"`: the color of the line separating the bottom of the toolbar from the region below.
  * `"toolbar_vertical_separator"`: the color of vertical separators in the toolbar.

See the example screenshot below to understand the parts of the browser UI
that are affected by these properties.

All these colors can be specified with any valid [CSS color code](/en-
US/docs/Web/CSS/color_value), except `"frame"` and `"tab_text"`, which are
specified using an RGB array, such as `"tab_text": [ 107 , 99 , 23 ]`.  
  
`properties` | `Object` |

Optional

This object has two properties that affect how the `"additional_backgrounds":`
images are displayed:

  * `"additional_backgrounds_alignment":` an array of enumeration values defining the alignment of the corresponding `"additional_backgrounds":` array item.  
The alignment options include: `"bottom"`, `"center"`, `"left"`, `"right"`,
`"top"`, `"center bottom"`, `"center center"`, `"center top"`, `"left
bottom"`, `"left center"`, `"left top"`, `"right bottom"`, `"right center"`,
and `"right top"`. If not specified, defaults to `"left top"`.  
Optional

  * `"additional_backgrounds_tiling":` an array of enumeration values defining how the corresponding `"additional_backgrounds":` array item repeats, with support for `"no-repeat"`, `"repeat"`, `"repeat-x"`, and `"repeat-y"`. If not specified, defaults to `"no-repeat"`.  
Optional

  
  
## Examples

A basic theme must define an image to add to the header, the accent color to
use in the header, and the color of text used in the header:

    
    
     "theme": {
       "images": {
         "headerURL": "images/sun.jpg"
       },
       "colors": {
         "accentcolor": "#CF723F",
         "textcolor": "#000"
       }
     }

Multiple images can be used to fill the header, using a blank/transparent
header image to gain control over the placement of each visible image:

    
    
     "theme": {
       "images": {
         "headerURL": "images/blank.png",
         "additional_backgrounds": [ "images/left.png" , "images/middle.png", "images/right.png"]
       },
       "properties": {
         "additional_backgrounds_alignment": [ "left top" , "top", "right top"]
       },
       "colors": {
         "accentcolor": "blue",
         "textcolor": "#ffffff"
       }
     }

You can also fill the header with a repeating image, or images, in this case a
single image anchored in the middle top of the header and repeated across the
rest of the header:

    
    
     "theme": {
       "images": {
         "headerURL": "images/blank.png",
         "additional_backgrounds": [ "images/logo.png"]
       },
       "properties": {
         "additional_backgrounds_alignment": [ "top" ],
         "additional_backgrounds_tiling": [ "repeat"  ]
       },
       "colors": {
         "accentcolor": "green",
         "textcolor": "#000"
       }
     }

The following example uses all the different values for `theme.colors`:

    
    
      "theme": {
        "images": {
          "headerURL": "weta.png"
        },
          
        "colors": {
           "accentcolor": "darkgreen",
           "textcolor": "white",
           "toolbar": "blue",
           "toolbar_text": "cyan",
           "toolbar_field": "orange",
           "toolbar_field_text": "green",
           "toolbar_top_separator": "red",
           "toolbar_bottom_separator": "white",
           "toolbar_vertical_separator": "white"
        }
      }

It will give you a browser that looks something like this:

![](https://mdn.mozillademos.org/files/15642/theme-example.png)

In this screenshot, `"toolbar_vertical_separator"` is the white vertical line
in the URL bar dividing the Reader Mode icon from the other icons.

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  No| 55|  No|  No  
`colors.accentcolor`|  No|  No| 55|  No|  No  
`colors.background_tab_text`|  Yes|  No| 55|  No|  No  
`colors.bookmark_text`|  Yes|  No|  No|  No|  No  
`colors.frame`|  Yes|  No| 55|  No|  No  
`colors.frame_inactive`|  Yes|  No|  No|  No|  No  
`colors.frame_incognito`|  Yes|  No|  No|  No|  No  
`colors.frame_incognito_inactive`|  Yes|  No|  No|  No|  No  
`colors.ntp_background`|  Yes|  No|  No|  No|  No  
`colors.ntp_header`|  Yes|  No|  No|  No|  No  
`colors.ntp_link`|  Yes|  No|  No|  No|  No  
`colors.ntp_text`|  Yes|  No|  No|  No|  No  
`colors.tab_text`|  Yes|  No| 55|  No|  No  
`colors.textcolor`|  No|  No| 55|  No|  No  
`colors.toolbar`|  Yes|  No| 57|  No|  No  
`colors.toolbar_field`|  No|  No| 57|  No|  No  
`colors.toolbar_field_text`|  No|  No| 57|  No|  No  
`colors.toolbar_text`|  No|  No| 57|  No|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes|  No support No|  Full support 55|  No
support No|  No support No  
`colors.accentcolor`|  No support No|  No support No|  Full support 55|  No
support No|  No support No  
`colors.background_tab_text`|  Full support Yes|  No support No|  Full support
55|  No support No|  No support No  
`colors.bookmark_text`|  Full support Yes|  No support No|  No support No|  No
support No|  No support No  
`colors.frame`|  Full support Yes|  No support No|  Full support 55|  No
support No|  No support No  
`colors.frame_inactive`|  Full support Yes|  No support No|  No support No|
No support No|  No support No  
`colors.frame_incognito`|  Full support Yes|  No support No|  No support No|
No support No|  No support No  
`colors.frame_incognito_inactive`|  Full support Yes|  No support No|  No
support No|  No support No|  No support No  
`colors.ntp_background`|  Full support Yes|  No support No|  No support No|
No support No|  No support No  
`colors.ntp_header`|  Full support Yes|  No support No|  No support No|  No
support No|  No support No  
`colors.ntp_link`|  Full support Yes|  No support No|  No support No|  No
support No|  No support No  
`colors.ntp_text`|  Full support Yes|  No support No|  No support No|  No
support No|  No support No  
`colors.tab_text`|  Full support Yes|  No support No|  Full support 55|  No
support No|  No support No  
`colors.textcolor`|  No support No|  No support No|  Full support 55|  No
support No|  No support No  
`colors.toolbar`|  Full support Yes|  No support No|  Full support 57|  No
support No|  No support No  
`colors.toolbar_field`|  No support No|  No support No|  Full support 57|  No
support No|  No support No  
`colors.toolbar_field_text`|  No support No|  No support No|  Full support 57|
No support No|  No support No  
`colors.toolbar_text`|  No support No|  No support No|  Full support 57|  No
support No|  No support No  
  
### Chrome compatibility

Firefox property | Chrome property  
---|---  
`images/headerURL` |

`images/theme_frame`

In Chrome, the image is anchored to the top left of the header and tiled if it
doesn’t fill the header area.  
  
`images/additional_backgrounds` | Not supported  
`colors/accentcolor` | `colors/frame`  
`colors/textcolor` | Incorrectly implemented as `colors/tab_text` from Firefox
55 to 58, fixed as `colors/background_tab_text` from Firefox 59 onward  
`colors/toolbar_text` | `colors/bookmark_text`  
`properties/additional_backgrounds_alignment` | Not supported  
`properties/additional_backgrounds_tiling` | Not supported  
  
In Chrome, all colors must be specified as an array of RGB values, like this:

    
    
    "theme": {
      "colors": {
         "frame": [255, 0, 0],
         "background_tab_text": [0, 255, 0],
         "bookmark_text": [0, 0, 255]
      }
    }

From Firefox 59 onward, both the array form and the CSS color form are
accepted for all properties. Before that, `colors/frame` and `colors/tab_text`
required the array form, while other properties required the CSS color form.

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
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

