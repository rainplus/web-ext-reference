[\n

\n

\n

Although the APIs are based on the [Chrome devtools
APIs](https://developer.chrome.com/extensions/devtools), there are still many
features that are not yet implemented in Firefox, and therefore are not
documented here. To see which features are currently missing please see
[Limitations of the devtools APIs](/en-US/Add-
ons/WebExtensions/Using_the_devtools_APIs#Limitations_of_the_devtools_APIs).

\n

\n

The `devtools.panels` API lets a devtools extension define its user interface
inside the devtools window.

\n

The devtools window hosts a number of separate tools - the JavaScript
Debugger, Network Monitor, and so on. A row of tabs across the top lets the
user switch between the different tools. The window hosting each tool's user
interface is called a "panel".

\n

With the `devtools.panels` API you can create new panels in the devtools
window.

\n

Like all the `devtools` APIs, this API is only available to code running in
the document defined in the [devtools_page](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/devtools_page) manifest.json key, or in other
devtools documents created by the extension (such as the panel's own
document). See [Extending the developer tools](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Extending_the_developer_tools) for more.

\n

## Types

\n

\n`[devtools.panels.ElementsPanel](/en-US/Add-
ons/WebExtensions/API/devtools.panels/ElementsPanel)`

\n    Represents the HTML/CSS inspector in the browser's devtools.

\n`[devtools.panels.ExtensionPanel](/en-US/Add-
ons/WebExtensions/API/devtools.panels/ExtensionPanel)`

\n    Represents a devtools panel created by the extension.

\n`[devtools.panels.ExtensionSidebarPane](/en-US/Add-
ons/WebExtensions/API/devtools.panels/ExtensionSidebarPane)`

\n    Represents a pane that an extension has added to the\xa0HTML/CSS
inspector in the browser's devtools.

\n\n

## Properties

\n

\n`[devtools.panels.elements](/en-US/Add-
ons/WebExtensions/API/devtools.panels/elements)`

\n    A reference to an `[ElementsPanel](/en-US/Add-
ons/WebExtensions/API/devtools.panels/ElementsPanel)` object.

\n`[devtools.panels.themeName](/en-US/Add-
ons/WebExtensions/API/devtools.panels/themeName)`

\n    The name of the current devtools theme.

\n\n

## Functions

\n

\n`[devtools.panels.create()](/en-US/Add-
ons/WebExtensions/API/devtools.panels/create)`

\n    Creates a new devtools panel.

\n\n

## Events

\n

\n`[devtools.panels.onThemeChanged](/en-US/Add-
ons/WebExtensions/API/devtools.panels/onThemeChanged)`

\n    Fired when the devtools theme changes.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`ElementsPanel.createSidebarPane`| \n Yes| \n No| 57| \n No| \n Yes  
`ElementsPanel.onSelectionChanged`| \n Yes| \n No| 56| \n No| \n Yes  
`ExtensionPanel.onHidden`| \n Yes| \n No| 54| \n No| \n Yes  
`ExtensionPanel.onSearch`| \n Yes| \n No| \n No| \n No| \n Yes  
`ExtensionPanel.onShown`| \n Yes| \n No| 54| \n No| \n Yes  
`ExtensionSidebarPane.onHidden`| \n Yes| \n No| 571| \n No| \n Yes  
`ExtensionSidebarPane.onShown`| \n Yes| \n No| 571| \n No| \n Yes  
`ExtensionSidebarPane.setExpression`| \n Yes2| \n No| 573| \n No| \n Yes  
`ExtensionSidebarPane.setObject`| \n Yes4| \n No| 575| \n No| \n Yes  
`create`| \n Yes| \n No| 54| \n No| \n Yes  
`elements`| \n Yes| \n No| 56| \n No| \n Yes  
`onThemeChanged`| \n No| \n No| 55| \n No| \n No  
`themeName`| 54| \n No| 55| \n No| 41  
  
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
`ElementsPanel.createSidebarPane`|  \nFull support\n\n Yes| \nNo support\n\n
No| \nFull support\n\n 57| \nFull support\n\n Yes| \nNo support\n\n No  
`ElementsPanel.onSelectionChanged`| \nFull support\n\n Yes| \nNo support\n\n
No| \nFull support\n\n 56| \nFull support\n\n Yes| \nNo support\n\n No  
`ExtensionPanel.onHidden`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n Yes| \nNo support\n\n No  
`ExtensionPanel.onSearch`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`ExtensionPanel.onShown`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull
support\n\n 54| \nFull support\n\n Yes| \nNo support\n\n No  
`ExtensionSidebarPane.onHidden`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __This event is only fired when the user switches between sidebar panes, not when the user switches between devtools panels. See[bug 1412317](https://bugzil.la/1412317).
|  \nFull support\n\n Yes| \nNo support\n\n No  
`ExtensionSidebarPane.onShown`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __This event is only fired when the user switches between sidebar panes, not when the user switches between devtools panels. See[bug 1412317](https://bugzil.la/1412317).
|  \nFull support\n\n Yes| \nNo support\n\n No  
`ExtensionSidebarPane.setExpression`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __The expression must evaluate to a JavaScript object or a DOM node, or nothing is shown in the sidebar.
|  \nNo support\n\n No| \nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __The expression must evaluate to an object that can be serialized to JSON, or nothing is shown in the sidebar. In particular, JavaScript cyclic objects and DOM nodes are not supported. See[bug 1403130](https://bugzil.la/1403130).
|  \nFull support\n\n Yes| \nNo support\n\n No  
`ExtensionSidebarPane.setObject`| \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __If the`jsonObject` parameter is a string, it is not displayed.
|  \nNo support\n\n No| \nFull support\n\n 57

Notes __

\nFull support\n\n 57

Notes __

     Notes __If the`jsonObject` is a string, then `rootTitle` must also be given, or `jsonObject` will not be displayed. See [bug 1412310](https://bugzil.la/1412310).
|  \nFull support\n\n Yes| \nNo support\n\n No  
`create`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 54|
\nFull support\n\n Yes| \nNo support\n\n No  
`elements`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
56| \nFull support\n\n Yes| \nNo support\n\n No  
`onThemeChanged`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
55| \nNo support\n\n No| \nNo support\n\n No  
`themeName`| \nFull support\n\n 54| \nNo support\n\n No| \nFull support\n\n
55| \nFull support\n\n 41| \nNo support\n\n No  
  
\n

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.devtools.panels`](https://developer.chrome.com/extensions/devtools_panels)
API.

\n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

\n

\n

\n

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.\n//\n// Redistribution and use in source and binary forms, with or without\n// modification, are permitted provided that the following conditions are\n// met:\n//\n//    * Redistributions of source code must retain the above copyright\n// notice, this list of conditions and the following disclaimer.\n//    * Redistributions in binary form must reproduce the above\n// copyright notice, this list of conditions and the following disclaimer\n// in the documentation and/or other materials provided with the\n// distribution.\n//    * Neither the name of Google Inc. nor the names of its\n// contributors may be used to endorse or promote products derived from\n// this software without specific prior written permission.\n//\n// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n

\n

\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

