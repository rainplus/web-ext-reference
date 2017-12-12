工具栏按钮是扩展可用的主要UI组件之一。
工具栏按钮位于主浏览器工具栏中，并包含一个图标。 当用户点击图标的时候，可能会发生以下两件事之一：

   * 如果您为图标指定了弹出窗口，则弹出窗口会显示。 弹出窗口是使用HTML，CSS和JavaScript指定的瞬态对话框。
   * 如果您没有指定弹出窗口，则会生成一个点击事件，您可以在代码中侦听，并执行其他一些响应操作。
   
使用WebExtension API时，这些按钮被称为“浏览器操作（行为）”，并设置如下：

  *在manifest.json的主键[browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)是用来定义按钮的
  *JavaScript API `[browserAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)` 监听点击事件并作出响应
  
## 一个简单的按钮

在本节中，我们将创建一个向工具栏添加按钮的扩展。当用户单击按钮时，我们将在新选项卡中打开<https://developer.mozilla.org>。

创建manifest.js:    
    
    {
    
      "description": "Demonstrating toolbar buttons",
      "manifest_version": 2,
      "name": "button-demo",
      "version": "1.0",
    
      "background": {
        "scripts": ["background.js"]
      },
     
      "browser_action": {
        "default_icon": {
          "16": "icons/page-16.png",
          "32": "icons/page-32.png"
        }
      }
    
    }

特别说明：我们使用了"background.js"作为后台脚本,一个浏览器操作按钮的图标。


存在多个图标的情况下，浏览器会选择高清那个进行显示。

接下来创建background.js的内容    
    
    function openPage() {
      browser.tabs.create({
        url: "https://developer.mozilla.org"
      });
    }
    
    browser.browserAction.onClicked.addListener(openPage);

监听浏览器行为的点击事件，当触发时，打开一个新标签，页面url是https://developer.mozilla.org

完整的拓展内容如下：
    
    button/
        icons/
            page-16.png
            page-32.png
        background.js
        manifest.json

安装拓展并进行测试

## 添加一个弹出窗口

我们尝试一下点击按钮弹出一个弹出层。我们替换manifest.json如下：
    
    {
    
      "description": "Demonstrating toolbar buttons",
      "manifest_version": 2,
      "name": "button-demo",
      "version": "1.0",
     
      "browser_action": {
        "browser_style": true,
        "default_popup": "popup/choose_page.html",
        "default_icon": {
          "16": "icons/page-16.png",
          "32": "icons/page-32.png"
        }
      }
    
    }

我们做了如下变更:

  * 我们不再引用后台脚本"background.js", 因为我们要做的业务逻辑放在了弹出层中。
  * 我们添加了`"browser_style": true`, 让弹出层的风格更加像浏览器风格。
  * 最后我们添加了 `"default_popup": "popup/choose_page.html"`页面作为弹出层显示的页面。
  
我们傅的弹层页面的代码如下：
    
    <!DOCTYPE html>
    
    <html>
      <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="choose_page.css"/>
      </head>
    
    <body>
      <div class="page-choice">developer.mozilla.org</div>
      <div class="page-choice">support.mozilla.org</div>
      <div class="page-choice">addons.mozilla.org</div>
      <script src="choose_page.js"></script>
    </body>
    
    </html>

您可以看到，这是一个普通的HTML页面，包含三个[`<div>`](/en-US/docs/Web/HTML/Element/div) HTML <div>元素是流内容的通用容器，不是固有地表示任何东西，用它来为元素分组，例如样式\（使用class或id attributes \），以不同的语言标记文档的一部分\（使用lang属性\），等等。 ）元素，每个元素内都有一个Mozilla网站的名称。 它还包括一个CSS文件和一个JavaScript文件，我们将在下面添加。

添加它的css文件：
    
    html, body {
      width: 300px;
    }
    
    .page-choice {
      width: 100%;
      padding: 4px;
      font-size: 1.5em;
      text-align: center;
      cursor: pointer;
    }
    
    .page-choice:hover {
      background-color: #CFF2F2;
    }

创建choose_page.js的内容：
    
    
    document.addEventListener("click", function(e) {
      if (!e.target.classList.contains("page-choice")) {
        return;
      }
    
      var chosenPage = "https://" + e.target.textContent;
      browser.tabs.create({
        url: chosenPage
      });
    
    });

在我们的JavaScript中，我们倾听点击弹出选择。 我们首先检查点击是否落在其中一个页面选项上; 如果没有，我们什么都不做。 如果点击确实落在了一个页面选项上，我们就从它构建一个URL，并打开一个包含相应页面的新标签。 请注意，我们可以在弹出脚本中使用WebExtension API，就像在后台脚本中一样。

本拓展的最后架构如下：
    
    button/
        icons/
            page-16.png
            page-32.png
        popup/
            choose_page.css
            choose_page.html
            choose_page.js
        manifest.json

进行加载并测试

## 页面操作

[Page actions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) 页面操作就像浏览器操作一样，除了它们是针对仅针对特定页面的操作，而不是作为整体的浏览器。

尽管始终显示浏览器操作，但页面操作仅显示在与其相关的标签中。 页面操作按钮显示在URL栏中，而不是浏览器工具栏中。

## 了解更多

  * [浏览器操作 browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action) manifest key
  * [JavaScript APIs browserAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction) API
  * 浏览器操作样例: 
    * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
    * [Bookmark it!](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)
    * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
    * [inpage-toolbar-ui](https://github.com/mdn/webextensions-examples/tree/master/inpage-toolbar-ui)
    * [open-my-page-button](https://github.com/mdn/webextensions-examples/tree/master/open-my-page-button)
  * [page_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action) manifest key
  * [pageAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction) API
  * 页面操作样例: 
    * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out)

