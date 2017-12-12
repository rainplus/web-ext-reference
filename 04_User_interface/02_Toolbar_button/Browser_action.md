这个用户界面选项是一个添加到浏览器工具栏的按钮，通常被称为[browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)。 用户点击按钮与您的拓展进行交互。
![](https://mdn.mozillademos.org/files/12966/browser-action.png)

当您的拓展功能适用于几乎所有的网页时，请使用此按钮。 工具栏按钮在所有浏览器选项卡中都可见。

与[address bar button](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions)相比，它提供了类似的行为，但只在需要在特定页面上访问拓展的情况下使用。

## 指定浏览器操作


191/5000
您可以使用manifest.json中的[browser_action](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)键来定义浏览器操作的属性：    
    
    "browser_action": {
      "default_icon": {
        "19": "button/geo-19.png",
        "38": "button/geo-38.png"
      },
      "default_title": "Whereami?"
    }

强制要求的属性只有`default_icon`.

有两种方法来指定浏览器操作：带或不带[ 弹出窗口 popup](/en-US/Add-ons/WebExtensions/Popups)。 如果你没有指定弹出窗口，当用户点击按钮时，一个事件被分配给扩展，扩展侦听使用[`browserAction.onClicked`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/BrowserAction/onClicked "Fired when a browser action icon is clicked. This event will not fire if the browser action has a popup.")点击浏览器动作图标时触发，如果浏览器动作弹出，此事件不会触发。

    browser.browserAction.onClicked.addListener(handleClick);

如果指定一个弹出窗口，则不会分派点击事件：相反，当用户单击按钮时会显示弹出窗口。 用户能够与弹出窗口进行交互，并在用户点击外部时自动关闭。 有关创建和管理弹出窗口的更多详细信息，请参阅[`Popup`](/en-US/Add-ons/WebExtensions/Popups)

请注意，您的扩展程序只能有一个浏览器操作。

您可以使用编程方式更改任何浏览器操作属性[browserAction](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction) API.


## 案例

[拓展案例](https://github.com/mdn/webextensions-examples)中包含了几个关于浏览器行为的案例：
  * [bookmark-it](https://github.com/mdn/webextensions-examples/blob/master/bookmark-it/)没有使用popup
  * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify) 使用了popup
