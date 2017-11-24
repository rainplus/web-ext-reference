Add items to the browser's menu system.

This API is modeled on Chrome's
["contextMenus"](https://developer.chrome.com/extensions/contextMenus) API,
which enables Chrome extensions to add items to the browser's context menu.
The `browser.menus` API adds a few features to Chrome's API, most notably the
ability to add items to the browser's "Tools" menu as well as the context
menu.

Before Firefox 55 this API was also originally named `contextMenus`, and that
name has been retained as an alias, so you can use `contextMenus` to write
code that works in Firefox and also in other browsers.

To use this API you need to have the "menus"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) (or "contextMenus" for the
alias).

## Creating menu items

To create a menu item call the [`menus.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/create "Creates a new menu item, given an options
object defining properties for the item.") method. You pass this method an
object containing options for the item, including the item ID, item type, and
the contexts in which it should be shown.

Listen for clicks on your menu item by adding a listener to the
[`menus.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/onClicked "Fired when a menu item is clicked.")
event. This listener will be passed a [`menus.OnClickData`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/menus/OnClickData "Information sent
when a menu item is clicked.") object containing the event's details.

You can create four different types of menu item, based on the value of the
`type` property you supply in the options to `create()`:

  * "normal": a menu item that just displays a label
  * "checkbox": a menu item that represents a binary state. It displays a checkmark next to the label. Clicking the item toggles the checkmark. The click listener will be passed two extra properties: "checked", indicating whether the item is checked now, and "wasChecked", indicating whether the item was checked before the click event.
  * "radio": a menu item that represents one of a group of choices. Just like a checkbox, this also displays a checkmark next to the label, and its click listener is passed "checked" and "wasChecked". However, if you create more than one radio item, then the items function as a group of radio items: only one item in the group can be checked, and clicking an item makes it the checked item.
  * "separator": a line separating a group of items.

If you have created more than one context menu item or more than one tools
menu item, then the items will be placed in a submenu. The submenu's parent
will be labeled with the name of the extension. For example, here's an
extension called "Menu demo" that's added two context menu items:

![](https://mdn.mozillademos.org/files/15431/menus-1.png)

## Icons

If you've specified icons for your extension using the ["icons" manifest key
](/en-US/Add-ons/WebExtensions/manifest.json/icons), your menu item will
display the specified icon next to its label. The browser will try to choose a
16x16 pixel icon for a normal display or a 32x32 pixel icon for a high-density
display:

![](https://mdn.mozillademos.org/files/15433/menus-2.png)

Only for items in a submenu, you can specify custom icons by passing the
`icons` option to [`menus.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/create "Creates a new menu item, given an options
object defining properties for the item."):

![](https://mdn.mozillademos.org/files/15435/menus-3.png)

## Example

Here's a context menu containing 4 items: a normal item, two radio items with
separators on each side, and a checkbox. The radio items are given custom
icons.

![](https://mdn.mozillademos.org/files/15437/menus-4.png)You could create a
submenu like this using code like:

    
    
    browser.menus.create({
      id: "remove-me",
      title: browser.i18n.getMessage("menuItemRemoveMe"),
      contexts: ["all"]
    }, onCreated);
    
    browser.menus.create({
      id: "separator-1",
      type: "separator",
      contexts: ["all"]
    }, onCreated);
    
    browser.menus.create({
      id: "greenify",
      type: "radio",
      title: browser.i18n.getMessage("menuItemGreenify"),
      contexts: ["all"],
      checked: true,
      icons: {
        "16": "icons/paint-green-16.png",
        "32": "icons/paint-green-32.png"
      }
    }, onCreated);
    
    browser.menus.create({
      id: "bluify",
      type: "radio",
      title: browser.i18n.getMessage("menuItemBluify"),
      contexts: ["all"],
      checked: false,
      icons: {
        "16": "icons/paint-blue-16.png",
        "32": "icons/paint-blue-32.png"
      }
    }, onCreated);
    
    browser.menus.create({
      id: "separator-2",
      type: "separator",
      contexts: ["all"]
    }, onCreated);
    
    var checkedState = true;
    
    browser.menus.create({
      id: "check-uncheck",
      type: "checkbox",
      title: browser.i18n.getMessage("menuItemUncheckMe"),
      contexts: ["all"],
      checked: checkedState
    }, onCreated);

## Types

[`menus.ContextType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/ContextType "The different contexts a menu item
can appear in.")

    The different contexts a menu can appear in.
[`menus.ItemType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/ItemType "The type of menu item.")

    The type of menu item: "normal", "checkbox", "radio", "separator".
[`menus.OnClickData`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/OnClickData "Information sent when a menu item is
clicked.")

    Information sent when a menu item is clicked.

## Properties

[`menus.ACTION_MENU_TOP_LEVEL_LIMIT`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/ACTION_MENU_TOP_LEVEL_LIMIT "The maximum number of
top level extension items that can be added to a menu item whose ContextType
is "browser_action" or "page_action". Any items beyond this limit will be
ignored.")

    The maximum number of top level extension items that can be added to a menu item whose ContextType is "browser_action" or "page_action".

## Functions

[`menus.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus/create
"Creates a new menu item, given an options object defining properties for the
item.")

    Creates a new menu item.
[`menus.update()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus/update
"Updates a previously created menu item.")

    Updates a previously created menu item.
[`menus.remove()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus/remove
"Removes a menu item.")

    Removes a menu item.
[`menus.removeAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/removeAll "Removes all menu items added by the
extension.")

    Removes all menu items added by this extension.

## Events

[`menus.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/onClicked "Fired when a menu item is clicked.")

    Fired when a menu item is clicked.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ACTION_MENU_TOP_LEVEL_LIMIT`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
`ContextType`|  Yes *|  Yes *|

55 *

48 *

|  No|  Yes *  
`ItemType`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
`OnClickData`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
`create`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
`onClicked`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
`remove`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
`removeAll`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
`update`|  Yes *|  Yes *|

55

48 *

|  No|  Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ACTION_MENU_TOP_LEVEL_LIMIT`|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  Full support 55

Full support 55

    
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  No support No  
`ContextType`|  Partial support Partial

Alternate Name __

Partial support Partial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  Partial support Partial

Alternate Name __

Partial support Partial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  Full support 55

Full support 55

Notes __

     Notes __'The 'editable' context does not include password fields. Use the 'password' context for this.
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  Partial support Partial

Alternate Name __

Partial support Partial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  No support No  
`ItemType`|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  Full support 55

Full support 55

    
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  No support No  
`OnClickData`|  Partial support Partial

Alternate Name __

Partial support Partial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  Partial support Partial

Alternate Name __

Partial support Partial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  Full support 55

Full support 55

    
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  Partial support Partial

Alternate Name __

Partial support Partial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  No support No  
`create`|  Partial support Partial

Notes __ Alternate Name __

Partial support Partial

Notes __ Alternate Name __

     Notes __Items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  Partial support Partial

Notes __ Alternate Name __

Partial support Partial

Notes __ Alternate Name __

     Notes __Items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  Full support 55

Full support 55

    
Full support 48

Notes __ Alternate Name __

     Notes __Before version 53, items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  Partial support Partial

Notes __ Alternate Name __

Partial support Partial

Notes __ Alternate Name __

     Notes __Items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  No support No  
`onClicked`|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  Full support 55

Full support 55

    
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  No support No  
`remove`|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  Full support 55

Full support 55

    
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  No support No  
`removeAll`|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  Full support 55

Full support 55

    
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  No support No  
`update`|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  Full support 55

Full support 55

    
Full support 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  Full support Yes

Alternate Name __

Full support Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  No support No  
  
## Example extensions

  * [menu-demo](https://github.com/mdn/webextensions-examples/tree/master/menu-demo)
  * [session-state](https://github.com/mdn/webextensions-examples/tree/master/session-state)

**Acknowledgements**

This API is based on Chromium's
[`chrome.contextMenus`](https://developer.chrome.com/extensions/contextMenus)
API. This documentation is derived from
[`context_menus.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/context_menus.json)
in the Chromium code.

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.
    //
    // Redistribution and use in source and binary forms, with or without
    // modification, are permitted provided that the following conditions are
    // met:
    //
    //    * Redistributions of source code must retain the above copyright
    // notice, this list of conditions and the following disclaimer.
    //    * Redistributions in binary form must reproduce the above
    // copyright notice, this list of conditions and the following disclaimer
    // in the documentation and/or other materials provided with the
    // distribution.
    //    * Neither the name of Google Inc. nor the names of its
    // contributors may be used to endorse or promote products derived from
    // this software without specific prior written permission.
    //
    // THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    // "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    // LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    // A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    // OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    // SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    // LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    // DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    // THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    // (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    // OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
  *[
 No support

]: No support

  *[
 Partial support

]: Partial support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[ Alternate Name __]: Uses the non-standard name: <code>contextMenus.update</code>
  *[Alternate Name __]: Uses the non-standard name: <code>contextMenus.update</code>
  *[
Partial support

]: Partial support

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

