扩展中最常见的用例之一是修改网页。 例如，扩展可能希望更改应用于页面的样式，隐藏特定的DOM节点，或向页面中注入额外的DOM节点。

有两种方法可以使用WebExtensions API执行此操作：

  * **Declaratively** : 定义一个模式，而不是匹配一组URL，并将一组脚本加载到URL匹配该模式的页面中。
  * **Programmatically** : 使用JavaScript API，将脚本加载到由特定标签的页面中。.

无论哪种方式实现都会调用 _内容脚本（content scripts）_ , 与构成扩展的其他脚本不同:

  * 他们只能访问WebExtension API的一小部分。
  * 他们可以直接访问他们加载的网页。
  * 他们使用消息传递API与扩展的其余部分进行通信。

在本篇文章中，我们对这两种的实现方式都进行了介绍
## 通过匹配URL模式（类似正则）进行页面的修改

创建拓展目录并写入如下的`manifest.json`
    
    {
      "manifest_version": 2,
      "name": "modify-page",
      "version": "1.0",
      "content_scripts": [
        {
          "matches": ["https://developer.mozilla.org/*"],
          "js": ["page-eater.js"]
        }
      ]
    }

上面的 [content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts) 关键字是将匹配到的脚本文件加载到页面中. 在本案例中, `content_scripts` 加载"page-eater.js" 到 <https://developer.mozilla.org/>的页面中.

js是一个`content_scripts`的一个数据属性，我们可以注入不止一个脚本。

 `content_scripts` 还包含`"css"` 属性，可以让拓展注入CSS样式表。

接下来，我们实现`page-eater.js`的内容如下
  
    document.body.textContent = "";
    
    var header = document.createElement('h1');
    header.textContent = "This page has been eaten";
    document.body.appendChild(header);

现在加载拓展并访问进行测试<https://developer.mozilla.org/>:

## 在拓展中使用API进行加载脚本并修改页面

如果你仍然想修改页面，但只有当用户要求你时呢？ 让我们更新这个例子，以便当用户点击一个上下文菜单项时注入内容脚本。

首先更新`manifest.js`的内容：

    {    
      "manifest_version": 2,
      "name": "modify-page",
      "version": "1.0",
      "permissions": [
        "activeTab",
        "contextMenus"
      ],
      "background": {
        "scripts": ["background.js"]
      }
    
    }

我们移除了内容脚本 `content_scripts` 属性, 并添加了两个键值:

  * [权限  permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions): 为了修改内容，我们要申请对应的权限，[当前页面标签 `activeTab` permission](/en-US/Add-ons/WebExtensions/manifest.json/permissions#activeTab_permission) 是为了获取当前活跃的页面. 我们需要上下文菜单 `contextMenus` 权限，给上下文添加新的项。
  * [后台 background](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/background): 我们使用了后台脚本["background script"](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts)  "background.js"来执行我们javascript APIs.

给background.js写入下面的内容：

    browser.contextMenus.create({
      id: "eat-page",
      title: "Eat this page"
    });
    
    browser.contextMenus.onClicked.addListener(function(info, tab) {
      if (info.menuItemId == "eat-page") {
        browser.tabs.executeScript({
          file: "page-eater.js"
        });
      }
    });
    

在脚本中我们添加了一个菜单项 [菜单项](/en-US/Add-ons/WebExtensions/API/ContextMenus/create), 指定了一个id和一个在上下文菜单中要展示的项. 并且我们给菜单项添加了一个事件监听，当我们点击菜单项时候。会执行 [tabs.executeScript()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript)API在当前标签页，进行加载脚本.这个接口使用标签的id作为参数进行指定某个标签。

脚本的架构文件：

    modify-page/
        background.js
        manifest.json
        page-eater.js

进行加载拓展并进行测试

## Messaging

内容脚本和后台脚本不能直接访问彼此的状态。 但是，他们可以通过发送消息进行通信。 一端设置消息监听器，另一端可以发送消息。 下表总结了每一方涉及的API：

  |内容脚本 content script | 后台脚本 background script  
---|---|---  
发送消息 | [browser.runtime.sendMessage()](/en-US/Add-ons/WebExtensions/API/runtime#sendMessage\(\)) | [browser.tabs.sendMessage()](/en-US/Add-ons/WebExtensions/API/Tabs/sendMessage)  
接收消息 | [browser.runtime.onMessage](/en-US/Add-ons/WebExtensions/API/runtime/onMessage) | [browser.runtime.onMessage](/en-US/Add-ons/WebExtensions/API/runtime#onMessage)  
  
我们使用消息机制修改上面的例子：

变更background.js脚本中的内容：

    browser.contextMenus.create({
      id: "eat-page",
      title: "Eat this page"
    });
    
    function messageTab(tabs) {
      browser.tabs.sendMessage(tabs[0].id, {
        replacement: "Message from the extension!"
      });
    }
    
    function onExecuted(result) {
        var querying = browser.tabs.query({
            active: true,
            currentWindow: true
        });
        querying.then(messageTab);
    }
    
    browser.contextMenus.onClicked.addListener(function(info, tab) {
      if (info.menuItemId == "eat-page") {
        let executing = browser.tabs.executeScript({
          file: "page-eater.js"
        });
        executing.then(onExecuted);
      }
    });
    

我们使用[tabs.query()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/query) 当前活跃的标签, 并使用[tabs.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage) 发送一个消息到内容脚本. 消息内容为： `{replacement:"Message from the extension!"}`.

修改"page-eater.js"的内容:

    function eatPageReceiver(request, sender, sendResponse) {
      document.body.textContent = "";
      var header = document.createElement('h1');
      header.textContent = request.replacement;
      document.body.appendChild(header);
    }
    browser.runtime.onMessage.addListener(eatPageReceiver);
    

现在，内容脚本不是立即修改页面，而是使用[runtime.onMessage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage).来监听消息。 当一个消息到达时，内容脚本基本上运行与以前相同的代码，除了替换文本取自`request.replacement`。

由于[tabs.executeScript()](/en-US/Add-ons/WebExtensions/API/tabs/executeScript) 是一个异步函数，为了确保我们仅在侦听器添加到page-eater.js 我们使用`onExecuted`执行”page-eater.js“调用。

快捷键Ctrl+Shift+J (or Cmd+Shift+J on a Mac)或 `web-ext run --bc` 打开 [Browser Console](/en-US/docs/Tools/Browser_Console)查看`console.log`.或者使用 [Add-on Debugger](/en-US/Add-ons/Add-on_Debugger)  进行断点调试[start Add-on Debugger directly from web-ext](https://github.com/mozilla/web-ext/issues/759).

如果我们要从内容脚本向后台脚本发送数据,要使用 [runtime.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage) 来替换[tabs.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage), 例如:

    browser.runtime.sendMessage({
        title: "from page-eater.js"
    });

插入CSS使用[tabs.insertCSS()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/insertCSS)函数.

## 更多详情

  * [内容脚本 Content scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts) guide
  * [content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts) manifest key
  * [权限 permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions) manifest key
  * [标签页 执行脚本 tabs.executeScript()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript)
  * [标签页 插入CSS tabs.insertCSS()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/insertCSS)
  * [标签页 发送消息 tabs.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage)
  * [运行时 发送消息 runtime.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage)
  * [运行时 接收消息 runtime.onMessage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)
  * `content_scripts` 案例: 
    * [borderify](https://github.com/mdn/webextensions-examples/tree/master/borderify)
    * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)
    * [page-to-extension-messaging](https://github.com/mdn/webextensions-examples/tree/master/page-to-extension-messaging)
  * `tabs.executeScript()` 案例: 
    * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
    * [context-menu-demo](https://github.com/mdn/webextensions-examples/tree/master/context-menu-demo)



