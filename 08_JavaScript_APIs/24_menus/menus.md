[\n

\n

Add items to the browser's menu system.

\n

This API is modeled on Chrome's
["contextMenus"](https://developer.chrome.com/extensions/contextMenus) API,
which enables Chrome extensions to add items to the browser's context menu.
The `browser.menus` API adds a few features to Chrome's API, most notably the
ability to add items to the browser's "Tools" menu as well as the context
menu.

\n

Before Firefox 55 this API was also originally named `contextMenus`, and that
name has been retained as an alias, so you can use `contextMenus` to write
code that works in Firefox and also in other browsers.

\n

To use this API you need to have the "menus"\xa0
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) (or "contextMenus" for the
alias).

\n

## Creating menu items

\n

To create a menu item call the [`menus.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/create "Creates a new menu item, given an options
object defining properties for the item.") method. You pass this method an
object containing options for the item, including the item ID, item type, and
the contexts in which it should be shown.

\n

Listen for clicks on your menu item by adding a listener to the
[`menus.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/onClicked "Fired when a menu item is clicked.")
event. This listener will be passed a [`menus.OnClickData`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/menus/OnClickData "Information sent
when a menu item is clicked.") object containing the event's details.

\n

You can create four different types of menu item, based on the value of the
`type` property you supply in the options to `create()`:

\n

\n

  * "normal": a menu item that just displays a label
\n

  * "checkbox": a menu item that represents a binary state. It displays a checkmark next to the label. Clicking the item toggles the checkmark. The click listener will be passed two extra properties: "checked", indicating whether the item is checked now, and "wasChecked", indicating whether the item was checked before the click event.
\n

  * "radio": a menu item that represents one of a group of choices. Just like a checkbox, this also displays a checkmark next to the label, and its click listener is passed "checked" and "wasChecked". However, if you create more than one radio item, then the items function as a group of radio items: only one item in the group can be checked, and clicking an item makes it the checked item.
\n

  * "separator": a line separating a group of items.
\n

\n

If you have created more than one context menu item or more than one tools
menu item, then the items will be placed in a submenu. The submenu's parent
will be labeled with the name of the extension. For example, here's an
extension called "Menu demo" that's added two context menu items:

\n

![](https://mdn.mozillademos.org/files/15431/menus-1.png)

\n

## Icons

\n

If you've specified icons for your extension using the ["icons" manifest key
](/en-US/Add-ons/WebExtensions/manifest.json/icons), your menu item will
display the specified icon next to its label. The browser will try to choose a
16x16 pixel icon for a normal display or a 32x32 pixel icon for a high-density
display:

\n

![](https://mdn.mozillademos.org/files/15433/menus-2.png)

\n

Only for items in a submenu, you can specify custom icons by passing the
`icons` option to [`menus.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/create "Creates a new menu item, given an options
object defining properties for the item."):

\n

![](https://mdn.mozillademos.org/files/15435/menus-3.png)

\n

## Example

\n

Here's a context menu containing 4 items: a normal item, two radio items with
separators on each side, and a checkbox. The radio items are given custom
icons.

\n

![](https://mdn.mozillademos.org/files/15437/menus-4.png)You could create a
submenu like this using code like:

\n

    
    
    browser.menus.create({\n  id: "remove-me",\n  title: browser.i18n.getMessage("menuItemRemoveMe"),\n  contexts: ["all"]\n}, onCreated);\n\nbrowser.menus.create({\n  id: "separator-1",\n  type: "separator",\n  contexts: ["all"]\n}, onCreated);\n\nbrowser.menus.create({\n  id: "greenify",\n  type: "radio",\n  title: browser.i18n.getMessage("menuItemGreenify"),\n  contexts: ["all"],\n  checked: true,\n  icons: {\n    "16": "icons/paint-green-16.png",\n    "32": "icons/paint-green-32.png"\n  }\n}, onCreated);\n\nbrowser.menus.create({\n  id: "bluify",\n  type: "radio",\n  title: browser.i18n.getMessage("menuItemBluify"),\n  contexts: ["all"],\n  checked: false,\n  icons: {\n    "16": "icons/paint-blue-16.png",\n    "32": "icons/paint-blue-32.png"\n  }\n}, onCreated);\n\nbrowser.menus.create({\n  id: "separator-2",\n  type: "separator",\n  contexts: ["all"]\n}, onCreated);\n\nvar checkedState = true;\n\nbrowser.menus.create({\n  id: "check-uncheck",\n  type: "checkbox",\n  title: browser.i18n.getMessage("menuItemUncheckMe"),\n  contexts: ["all"],\n  checked: checkedState\n}, onCreated);

\n

## Types

\n

\n[`menus.ContextType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/ContextType "The different contexts a menu item
can appear in.")

\n    The different contexts a menu can appear in.

\n[`menus.ItemType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/ItemType "The type of menu item.")

\n    The type of menu item: "normal", "checkbox", "radio", "separator".

\n[`menus.OnClickData`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/OnClickData "Information sent when a menu item is
clicked.")

\n    Information sent when a menu item is clicked.

\n\n

## Properties

\n

\n[`menus.ACTION_MENU_TOP_LEVEL_LIMIT`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/ACTION_MENU_TOP_LEVEL_LIMIT "The maximum number of
top level extension items that can be added to a menu item whose ContextType
is "browser_action" or "page_action". Any items beyond this limit will be
ignored.")

\n    The maximum number of top level extension items that can be added to a
menu item whose ContextType is "browser_action" or "page_action".

\n\n

## Functions

\n

\n[`menus.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/create "Creates a new menu item, given an options
object defining properties for the item.")

\n    Creates a new menu item.

\n[`menus.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/update "Updates a previously created menu item.")

\n    Updates a previously created menu item.

\n[`menus.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/remove "Removes a menu item.")

\n    Removes a menu item.

\n[`menus.removeAll()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/removeAll "Removes all menu items added by the
extension.")

\n    Removes all menu items added by this extension.

\n\n

## Events

\n

\n[`menus.onClicked`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/menus/onClicked "Fired when a menu item is clicked.")

\n    Fired when a menu item is clicked.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ACTION_MENU_TOP_LEVEL_LIMIT`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
`ContextType`| \n Yes *| \n Yes *|

55 *

48 *

| \n No| \n Yes *  
`ItemType`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
`OnClickData`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
`create`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
`onClicked`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
`remove`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
`removeAll`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
`update`| \n Yes *| \n Yes *|

55

48 *

| \n No| \n Yes *  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ACTION_MENU_TOP_LEVEL_LIMIT`|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ACTION_MENU_TOP_LEVEL_LIMIT`
|  \nNo support\n\n No  
`ContextType`| \nPartial support\nPartial

Alternate Name __

\nPartial support\nPartial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  \nPartial support\nPartial

Alternate Name __

\nPartial support\nPartial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  \nFull support\n\n 55

\nFull support\n\n 55

Notes __

     Notes __'The 'editable' context does not include password fields. Use the 'password' context for this.
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  \nPartial support\nPartial

Alternate Name __

\nPartial support\nPartial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ContextType`
|  \nNo support\n\n No  
`ItemType`| \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.ItemType`
|  \nNo support\n\n No  
`OnClickData`| \nPartial support\nPartial

Alternate Name __

\nPartial support\nPartial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  \nPartial support\nPartial

Alternate Name __

\nPartial support\nPartial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  \nPartial support\nPartial

Alternate Name __

\nPartial support\nPartial

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.OnClickData`
|  \nNo support\n\n No  
`create`| \nPartial support\nPartial

Notes __ Alternate Name __

\nPartial support\nPartial

Notes __ Alternate Name __

     Notes __Items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  \nPartial support\nPartial

Notes __ Alternate Name __

\nPartial support\nPartial

Notes __ Alternate Name __

     Notes __Items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Notes __ Alternate Name __

     Notes __Before version 53, items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  \nPartial support\nPartial

Notes __ Alternate Name __

\nPartial support\nPartial

Notes __ Alternate Name __

     Notes __Items that don't specify 'contexts' do not inherit contexts from their parents.
     Alternate Name __Uses the non-standard name:`contextMenus.create`
|  \nNo support\n\n No  
`onClicked`| \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.onClicked`
|  \nNo support\n\n No  
`remove`| \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.remove`
|  \nNo support\n\n No  
`removeAll`| \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.removeAll`
|  \nNo support\n\n No  
`update`| \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  \nFull support\n\n 55

\nFull support\n\n 55

    
\nFull support\n\n 48

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  \nFull support\n\n Yes

Alternate Name __

\nFull support\n\n Yes

Alternate Name __

     Alternate Name __Uses the non-standard name:`contextMenus.update`
|  \nNo support\n\n No  
  
\n

## Example extensions

  * [menu-demo](https://github.com/mdn/webextensions-examples/tree/master/menu-demo)
  * [session-state](https://github.com/mdn/webextensions-examples/tree/master/session-state)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.contextMenus`](https://developer.chrome.com/extensions/contextMenus)
API. This documentation is derived from
[`context_menus.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/context_menus.json)
in the Chromium code.

\n

\n

\n

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.\n//\n// Redistribution and use in source and binary forms, with or without\n// modification, are permitted provided that the following conditions are\n// met:\n//\n//    * Redistributions of source code must retain the above copyright\n// notice, this list of conditions and the following disclaimer.\n//    * Redistributions in binary form must reproduce the above\n// copyright notice, this list of conditions and the following disclaimer\n// in the documentation and/or other materials provided with the\n// distribution.\n//    * Neither the name of Google Inc. nor the names of its\n// contributors may be used to endorse or promote products derived from\n// this software without specific prior written permission.\n//\n// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n

\n

\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[\nPartial support\n]: Partial support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[ Alternate Name __]: Uses the non-standard name: <code>contextMenus.update</code>
  *[Alternate Name __]: Uses the non-standard name: <code>contextMenus.update</code>
  *[Mobile __]: Mobile
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

