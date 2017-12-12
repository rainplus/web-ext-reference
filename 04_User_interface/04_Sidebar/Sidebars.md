侧边栏是一个窗格，显示在浏览器窗口的左侧，位于网页旁边。 浏览器提供了一个用户界面，使用户能够看到当前可用的侧边栏，并选择一个边栏来显示。 例如，Firefox有一个“View> Sidebar”菜单。 每次只能显示一个边栏，该边栏将显示所有选项卡和所有浏览器窗口。

浏览器可能包含一些内置的侧边栏。 例如，Firefox包含一个用于与书签交互的侧栏：

![](https://mdn.mozillademos.org/files/14825/bookmarks-sidebar.png) 

使用`sidebar_action`manifest.json键，拓展展可以将自己的侧边栏添加到浏览器。它将与内置的侧边栏一起列出，用户将能够使用与内置侧边栏相同的机制打开它。

与浏览器操作弹出窗口一样，您可以将边栏的内容指定为HTML文档。 当用户打开边栏时，其文档被加载到每个打开的浏览器窗口中。 每个窗口都有自己的文档实例。 当新窗口打开时，他们也获得自己的边栏文档。

您可以使用[`sidebarAction.setPanel（）`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction/setPanel "Sets the HTML document that defines the content of this sidebar.") 为特定选项卡设置文档.
一个边栏可以找出它属于哪个窗口使用 [`windows.getCurrent()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/getCurrent "The documentation about this has not yet been written; please consider contributing!") API:

    // sidebar.js
    browser.windows.getCurrent({populate: true}).then((windowInfo) => {
      myWindowId = windowInfo.id;
    });

如果边栏想要为不同的窗口显示不同的内容，这很有用。 有关这方面的示例，请参阅[“注释页面”示例](https://github.com/mdn/webextensions-examples/tree/master/annotate-page).

边栏文档可以访问扩展程序的后台和弹出脚本获得的相同特权JavaScript API。 他们可以使用[`runtime.getBackgroundPage（）`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/getBackgroundPage "Retrieves the Window object for the background page running inside the current extension.") 直接访问后台页面（除非侧边栏属于隐身模式窗口）,并且可以使用消息API[`tabs.sendMessage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage "Sends a single message from the extension's background scripts \(or other privileged scripts, such as popup scripts or options page scripts\) to any content scripts that belong to the extension and are running in the specified tab.")和[`runtime.sendNativeMessage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendNativeMessage "Sends a single message from an extension to a native application.")与内容脚本或本机应用程序进行交互

当浏览器窗口关闭或用户关闭边栏时，边栏文档将被关闭。这意味着与背景页面不同，边栏文档不会始终保持加载状态，但与浏览器操作弹出窗口不同，它们在用户与网页交互时保持加载状态。

首次安装定义侧栏的扩展时，其侧栏将自动打开。 这旨在帮助用户了解该扩展程序包含侧边栏。请注意，扩展程序无法以编程方式打开侧边栏：侧边栏只能由用户打开。

## Specifying sidebars

要指定侧边栏，请使用[sidebar_action](/en-US/Add-ons/WebExtensions/manifest.json/sidebar_action)manifest.json键以及默认标题和图标来定义默认文档：

    "sidebar_action": {
      "default_title": "My sidebar",
      "default_panel": "sidebar.html",
      "default_icon": "sidebar_icon.png"
    }

您可以使用[`sidebarAction`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction "Gets and sets properties of an extension's sidebar.") API以编程方式更改标题，面板和图标。。

标题和图标在浏览器提供的任何UI中向用户显示，以列出侧边栏，例如Firefox中的“查看>侧边栏”菜单。

## Example
在[GitHub](https://github.com/mdn/webextensions-examples)上的仓库，包含几个使用侧边栏的扩展的例子：

  * [annotate-page](https://github.com/mdn/webextensions-examples/tree/master/annotate-page) uses a sidebar.

