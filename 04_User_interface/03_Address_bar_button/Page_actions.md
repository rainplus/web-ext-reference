地址栏的按钮的用户界面选项通常被称为[page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)，它是一个添加到浏览器地址栏的按钮。 用户点击按钮与您的拓展交互。

![](https://mdn.mozillademos.org/files/12960/page-action.png)

当某个功能仅与某些网页相关时，请使用此按钮。 默认情况下，地址栏按钮隐藏在所有浏览器选项卡中，然后您可以调用 [`pageAction.show()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/PageAction/show "Shows the page action for a given tab.The page action is shown whenever the given tab is the active tab.") 和 [`pageAction.hide()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/PageAction/hide "Hides the page action for a given tab.") 在定定标签中显示或隐藏它。



与[工具栏按钮toolbar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action)相比，它提供了类似的行为，但用于扩展功能几乎适用于所有情况

## 指定页面操作

您可以使用[page_action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)在manifest.json中的键：

    "page_action": {
      "browser_style": true,
      "default_icon": {
        "19": "button/geo-19.png",
        "38": "button/geo-38.png"
      },
      "default_title": "Whereami?"
    }

强制的属性键是`default_icon`.

有两种方法可以指定页面操作：带或不带[弹出窗口 popup](/en-US/Add-ons/WebExtensions/Popups). 如果你没有指定一个弹出窗口，当用户点击该按钮时，一个事件被分派到该拓展上的监听使用[`pageAction.onClicked`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction/onClicked "Fired when a browser action icon is clicked. This event will not fire if the browser action has a popup.") 单击浏览器动作图标时触发此事件不会触发浏览器动作弹出窗口：

    browser.pageAction.onClicked.addListener(handleClick);

如果指定一个弹出窗口，则不会分发点击事件：相反，当用户单击按钮时会显示弹出窗口。 用户能够与弹出窗口进行交互，并在用户点击外部时自动关闭。 有关创建和管理弹出窗口的更多详细信息，请参见[Popup ](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Popups)。

请注意，您的扩展只能有一个页面操作。

您可以使用[pageAction](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)API以编程方式更改任何页面操作属性。

## 示例

在[GitHub](https://github.com/mdn/webextensions-examples)上的仓库，包含几个使用地址栏按钮的拓展的例子：

  * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out) uses a page action without a popup.

