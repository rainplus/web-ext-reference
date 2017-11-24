Although the APIs are based on the [Chrome devtools
APIs](https://developer.chrome.com/extensions/devtools), there are still many
features that are not yet implemented in Firefox, and therefore are not
documented here. To see which features are currently missing please see
[Limitations of the devtools APIs](/en-US/Add-
ons/WebExtensions/Using_the_devtools_APIs#Limitations_of_the_devtools_APIs).

The `devtools.panels` API lets a devtools extension define its user interface
inside the devtools window.

The devtools window hosts a number of separate tools - the JavaScript
Debugger, Network Monitor, and so on. A row of tabs across the top lets the
user switch between the different tools. The window hosting each tool's user
interface is called a "panel".

With the `devtools.panels` API you can create new panels in the devtools
window.

Like all the `devtools` APIs, this API is only available to code running in
the document defined in the [devtools_page](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/devtools_page) manifest.json key, or in other
devtools documents created by the extension (such as the panel's own
document). See [Extending the developer tools](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Extending_the_developer_tools) for more.

## Types

`[devtools.panels.ElementsPanel](/en-US/Add-
ons/WebExtensions/API/devtools.panels/ElementsPanel)`

    Represents the HTML/CSS inspector in the browser's devtools.
`[devtools.panels.ExtensionPanel](/en-US/Add-
ons/WebExtensions/API/devtools.panels/ExtensionPanel)`

    Represents a devtools panel created by the extension.
`[devtools.panels.ExtensionSidebarPane](/en-US/Add-
ons/WebExtensions/API/devtools.panels/ExtensionSidebarPane)`

    Represents a pane that an extension has added to the HTML/CSS inspector in the browser's devtools.

## Properties

`[devtools.panels.elements](/en-US/Add-
ons/WebExtensions/API/devtools.panels/elements)`

    A reference to an `[ElementsPanel](/en-US/Add-ons/WebExtensions/API/devtools.panels/ElementsPanel)` object.
`[devtools.panels.themeName](/en-US/Add-
ons/WebExtensions/API/devtools.panels/themeName)`

    The name of the current devtools theme.

## Functions

`[devtools.panels.create()](/en-US/Add-
ons/WebExtensions/API/devtools.panels/create)`

    Creates a new devtools panel.

## Events

`[devtools.panels.onThemeChanged](/en-US/Add-
ons/WebExtensions/API/devtools.panels/onThemeChanged)`

    Fired when the devtools theme changes.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ElementsPanel.createSidebarPane`|  Yes|  No| 57|  No|  Yes  
`ElementsPanel.onSelectionChanged`|  Yes|  No| 56|  No|  Yes  
`ExtensionPanel.onHidden`|  Yes|  No| 54|  No|  Yes  
`ExtensionPanel.onSearch`|  Yes|  No|  No|  No|  Yes  
`ExtensionPanel.onShown`|  Yes|  No| 54|  No|  Yes  
`ExtensionSidebarPane.onHidden`|  Yes|  No| 571|  No|  Yes  
`ExtensionSidebarPane.onShown`|  Yes|  No| 571|  No|  Yes  
`ExtensionSidebarPane.setExpression`|  Yes2|  No| 573|  No|  Yes  
`ExtensionSidebarPane.setObject`|  Yes4|  No| 575|  No|  Yes  
`create`|  Yes|  No| 54|  No|  Yes  
`elements`|  Yes|  No| 56|  No|  Yes  
`onThemeChanged`|  No|  No| 55|  No|  No  
`themeName`| 54|  No| 55|  No| 41  
  
1\. This event is only fired when the user switches between sidebar panes, not
when the user switches between devtools panels. See [bug
1412317](https://bugzil.la/1412317).

2\. The expression must evaluate to a JavaScript object or a DOM node, or
nothing is shown in the sidebar.

3\. The expression must evaluate to an object that can be serialized to JSON,
or nothing is shown in the sidebar. In particular, JavaScript cyclic objects
and DOM nodes are not supported. See [bug 1403130](https://bugzil.la/1403130).

4\. If the `jsonObject` parameter is a string, it is not displayed.

5\. If the `jsonObject` is a string, then `rootTitle` must also be given, or
`jsonObject` will not be displayed. See [bug
1412310](https://bugzil.la/1412310).

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`ElementsPanel.createSidebarPane`|  Full support Yes|  No support No|  Full
support 57|  Full support Yes|  No support No  
`ElementsPanel.onSelectionChanged`|  Full support Yes|  No support No|  Full
support 56|  Full support Yes|  No support No  
`ExtensionPanel.onHidden`|  Full support Yes|  No support No|  Full support
54|  Full support Yes|  No support No  
`ExtensionPanel.onSearch`|  Full support Yes|  No support No|  No support No|
Full support Yes|  No support No  
`ExtensionPanel.onShown`|  Full support Yes|  No support No|  Full support 54|
Full support Yes|  No support No  
`ExtensionSidebarPane.onHidden`|  Full support Yes|  No support No|  Full
support 57

Notes __

Full support 57

Notes __

     Notes __This event is only fired when the user switches between sidebar panes, not when the user switches between devtools panels. See[bug 1412317](https://bugzil.la/1412317).
|  Full support Yes|  No support No  
`ExtensionSidebarPane.onShown`|  Full support Yes|  No support No|  Full
support 57

Notes __

Full support 57

Notes __

     Notes __This event is only fired when the user switches between sidebar panes, not when the user switches between devtools panels. See[bug 1412317](https://bugzil.la/1412317).
|  Full support Yes|  No support No  
`ExtensionSidebarPane.setExpression`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __The expression must evaluate to a JavaScript object or a DOM node, or nothing is shown in the sidebar.
|  No support No|  Full support 57

Notes __

Full support 57

Notes __

     Notes __The expression must evaluate to an object that can be serialized to JSON, or nothing is shown in the sidebar. In particular, JavaScript cyclic objects and DOM nodes are not supported. See[bug 1403130](https://bugzil.la/1403130).
|  Full support Yes|  No support No  
`ExtensionSidebarPane.setObject`|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __If the`jsonObject` parameter is a string, it is not displayed.
|  No support No|  Full support 57

Notes __

Full support 57

Notes __

     Notes __If the`jsonObject` is a string, then `rootTitle` must also be given, or `jsonObject` will not be displayed. See [bug 1412310](https://bugzil.la/1412310).
|  Full support Yes|  No support No  
`create`|  Full support Yes|  No support No|  Full support 54|  Full support
Yes|  No support No  
`elements`|  Full support Yes|  No support No|  Full support 56|  Full support
Yes|  No support No  
`onThemeChanged`|  No support No|  No support No|  Full support 55|  No
support No|  No support No  
`themeName`|  Full support 54|  No support No|  Full support 55|  Full support
41|  No support No  
  
**Acknowledgements**

This API is based on Chromium's
[`chrome.devtools.panels`](https://developer.chrome.com/extensions/devtools_panels)
API.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

    
    
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

