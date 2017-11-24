Themes developed using the [WebExtensions API](/en-US/Add-ons/WebExtensions)
in Firefox enable you to change the look of the browser by adding images to
the header area of the Firefox browser; this is the area behind the menu bar,
toolbars, address bar, search bar, and tab strip.

These theme options can be implemented as static themes (although the theme
images themselves may be animated) or as dynamic themes created in a browser
extension.

If you have a [lightweight theme](/en-US/docs/Mozilla/Add-
ons/Themes/Lightweight_themes) it will be converted to this new theme format
automatically before lightweight themes are deprecated. You do not need to
port your theme. However, please feel free to update your themes to use any of
the new features described here.

## Static themes

Static themes are specified using the same resources as a browser extension: a
[manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file
to define the theme components with those components stored in the same folder
as the manifest.json file or a sub folder. These resources are then packed in
a zip for publication on [addons.mozilla.org](https://addons.mozilla.org)
(AMO).

A theme and browser extension functionality cannot be defined in one package,
such as including a theme to complement an extension. You can, however,
programmatically include a theme in an extension using the Theme API. See
Dynamic themes.

### Defining a theme

To create a theme (in this example a simple, single image theme):

  * Create a folder in a suitable location on your computer.
  * Add the theme image file to the folder: 
    
        <mytheme>
     <your_header_image>.<type>

  * Create a file called manifest.json in the folder and edit its content as follows: 
    
         "theme": {
       "images": {
         "headerURL": "<your_header_image>.<type>"
            },
       "colors": {
         "accentcolor": "#FFFFFF",
         "textcolor": "#000"
       }
     }
    

Where:

    * `"accentcolor":` is the heading area background color for your theme.
    * `"``textcolor``":` the color of the text in the heading area.
  * Package your theme and submit it to AMO, [following these instructions](/en-US/Add-ons/WebExtensions/Publishing_your_WebExtension).

### Static theme approaches

There are two approaches you can take to theming the header area of Firefox:
using a single image or using multiple images. You could combine the two, but
it’s easier to treat them separately.

#### Single image themes

This is the basic or minimal theming option, where you define:

  * a single image, which is anchored to the top right of the header area.
  * A color for the text in the header.

The area your header image needs to fill is a maximum of 200 pixels high. The
maximum image width is determined by the resolution of the monitor Firefox is
displaying on and how much of the monitor Firefox is using. Practically, this
means you would need to allow for a width of up to 5120 pixels wide (for the
next generation of 5k monitors). However, rather than creating a very wide
image, a better approach is to use a narrower image with a transparent left
edge so that it fades to the background color. For example, we could use this
image  
![An image of a weta \(the common name for a group of about 70 insect species
in the families Anostostomatidae and Rhaphidophoridae, endemic to New
Zealand\) with the left edge fading to total
transparency.](https://mdn.mozillademos.org/files/15215/weta.png)  
combined with a complementary background color, to create this effect in the
header  
![A single image theme using the weta.png
image](https://mdn.mozillademos.org/files/15217/basic_theme.png)

See details about this theme in the [themes](https://github.com/mdn
/webextensions-examples/tree/master/themes) example
[weta_fade](https://github.com/mdn/webextensions-
examples/tree/master/themes/weta_fade).

Obviously, you can still provide a single wide image if you prefer.

#### Multiple image themes

As an alternative to creating a single image theme, you have the option to use
multiple images. These images can be individually anchored to locations within
the header, with the option to apply tiling to each image.

Depending on the effect you want to create you may need to suppress the
mandatory `"``headerURL``":` image with an empty or transparent image. You
would use an empty or transparent image if, for example, you wanted to tile a
centrally justified image, such as  
![An image of a weta \(the common name for a group of about 70 insect species
in the families Anostostomatidae and Rhaphidophoridae, endemic to New
Zealand\) with the left and right edges fading to total
transparency.](https://mdn.mozillademos.org/files/15219/weta_for_tiling.png)  
to create this effect  
![A single image theme using the additional images option to align an image to
the center of the heading and tile it.
](https://mdn.mozillademos.org/files/15221/tiled_theme.png)  
Here you specify the weta image like this:

    
    
        "images": {
          "headerURL": "empty.png",
          "additional_backgrounds": [ "weta_for_tiling.png"]
        },

and the images tiling with:

    
    
        "properties": {
          "additional_backgrounds_alignment": [ "top" ],
          "additional_backgrounds_tiling": [ "repeat"  ]
         },

Full details of how to setup this theme can be found in the
[themes](https://github.com/mdn/webextensions-examples/tree/master/themes)
example [weta_tiled](https://github.com/mdn/webextensions-
examples/tree/master/themes/weta_tiled). Full detais of the alignment and
tiling options can be found in the ["theme" key description](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme).

Alternatively, you can use multiple images, say combining the original weta
image with this one anchored to the left of the header  
![An image of a weta \(the common name for a group of about 70 insect species
in the families Anostostomatidae and Rhaphidophoridae, endemic to New
Zealand\) with the right edge fading to total
transparency.](https://mdn.mozillademos.org/files/15223/weta-left.png)  
to create this effect  
![A theme using the additional images option to place two mirrored image to
the left and right of the browser
header.](https://mdn.mozillademos.org/files/15225/multi_image_theme.png)

Where the images are specified with:

    
    
      "images": {
       "headerURL": "empty.png",
       "additional_backgrounds": [ "weta.png", "weta-left.png"]
       },

and their alignment by:

    
    
      "properties": {
        "additional_backgrounds_alignment": [ "right top" , "left top" ]
        },

Full details of how to setup this theme can be found in the
[themes](https://github.com/mdn/webextensions-examples/tree/master/themes)
example [weta_mirror](https://github.com/mdn/webextensions-
examples/tree/master/themes/weta_mirror). Full detais of the alignment options
can be found in the ["theme" key description](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/theme).

### Static animated themes

It is possible to create an animated theme using an APNG format image, as in
the [themes](https://github.com/mdn/webextensions-examples/tree/master/themes)
example [animated](https://github.com/mdn/webextensions-
examples/tree/master/themes/animated). However, remember that rapid
animations, such as the one in the example might be too distracting for a
practical theme.

You can also animate themes programmatically, which we discuss in Dynamic
themes.

## Dynamic themes

As an alternative to defining a static theme, you can use the [`theme`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/theme "Enables browser extensions to
update the browser theme.") API to control the theme used in Firefox from
within a browser extension. There are a couple of use cases for this option:

  * To bundle a theme with a browser extension, as an added extra.
  * Create a dynamic theme that changes under programmatic control.

And, obviously, you can combine the two and bundle a programmatically
controlled theme with your extension.

Using the [`theme`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme
"Enables browser extensions to update the browser theme.") API is
straightforward. First, request "theme"[ permission](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) in the extension's[ manifest.json
](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file. Next, you
build a JSON object containing the same information you would use in a static
theme’s manifest.json, Finally, pass the JSON object in a [`theme.update
()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme/update "Updates the
browser theme according to the content of given Theme object.") call.

For example, the following code, from the [dynamic theme
example](https://github.com/mdn/webextensions-examples/tree/master/dynamic-
theme) defines the content for the day and night elements of the dynamic
theme:

    
    
    const themes = {
      'day': {
        images: {
         headerURL: 'sun.jpg',
        },
        colors: {
         accentcolor: '#CF723F',
         textcolor: '#111',
        }
      },
      'night': {
        images: {
         headerURL: 'moon.jpg',
        },
        colors: {
         accentcolor: '#000',
         textcolor: '#fff',
        }
      }
    };

The theme.Theme object is then passed to [`theme.update()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/theme/update "Updates the browser
theme according to the content of given Theme object.") to change the header
theme, as in this code snippet from the same example:

    
    
    function setTheme(theme) {
      if (currentTheme === theme) {
        // No point in changing the theme if it has already been set.
        return;
      }
      currentTheme = theme;
      browser.theme.update(themes[theme]);
     }

If you have not built a browser extension before, check out [Your first
extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension)
for a step-by-step guide.

## Cross browser compatibility

There is currently limited compatibility between themes in the major browsers.
Opera takes an entirely different approach, and Microsoft Edge themes are not
yet open to developers.

There is some compatibility between Firefox static themes and Chrome themes,
providing the ability to port a single header image theme from Firefox to
Chrome. This would be done by amending the manifest.json keys as follows:

  * `"headerURL":` to `"theme_frame":`
  * `"accentcolor":` to `"frame":`
  * `"textcolor":` to `"tab_text":`

Noting that "frame": and "tab_text": support RGB color definition only.

So, in the single image theme example (weta_fade) could be supported in Chrome
using the following manifest.json file:

    
    
     "theme": {
        "images": {
          "theme_frame": "weta.png"
        },
        "colors": {
           "frame": [ 173 , 176 , 159 ],
           "tab_text": [ 0 , 0 , 0 ]
        }
     }

However, there will be a couple of differences:

  * Chrome tiles the `“theme_frame”:` image from the left of the header area.
  * `"tab_text":` only affects the text on the highlighted/active tab.

![The basic theme example using the Chrome compatible manifest.json keys,
showing the differences in how those keys are
implemented.](https://mdn.mozillademos.org/files/15227/basic_in_chrome.png)

For more information, see the notes on [Chrome compatibility](/en-US/Add-
ons/WebExtensions/manifest.json/theme#Chrome_compatibility).

