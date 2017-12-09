如果你阅读过[你的第一个拓展](/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension),你已经对开发一个拓展有了一个全面的认识,在这篇文章中,我们会写一个更加复杂(使用了大量的APIs)的拓展.

本次的拓展，在firefox工具栏上添加了一个新按钮。当用户点击这个按钮，我们会弹出并展示给他们一个选择动物页面。一旦他们选择了一种动物，我们会替换页面上的动物图片。

要实现这些功能,我做如下操作:

  * **定义一个[浏览器行为](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action), 实现了工具栏上添加按钮**.  
针对这个按钮，要提供:
    * 一个图标："beasts-32.png"
    * 按下按钮的弹出层，包含HTML, CSS和JavaScript.
  * **定义拓展的图标** , 名称"beasts-48.png". 会展示在拓展管理中心.
  * **一个内容脚本："beastify.js",会注入到页面中**.  
这里代码会直接修改页面的内容
  * **打包一些用于替换页面的动物图片**.  
使这些动物图片可以被访问

你可以查看这个拓展的架构如下：

![](https://mdn.mozillademos.org/files/13671/Untitled-1.png)

它还是一个简单的拓展，只是使用了更多的WebExtensions API,并展示了更多的基本概念：

  * 在工具栏添加按钮
  * 使用HTML, CSS, 和 JavaScript定义弹出的页面
  * 注入内容脚本
  * 在不同拓展问交互内容脚本
  * 在页面上查阅打包的资源

本拓展示源码[Github](https://github.com/mdn/webextensions-examples/tree/master/beastify).

实现该拓展，请你确认firefox版本>=45
## 写拓展

创建文件夹并进入：

    mkdir beastify
    cd beastify

### manifest.json

创建说明文件 "manifest.json", 并转入如下内容：

    {
    
      "manifest_version": 2,
      "name": "Beastify",
      "version": "1.0",
    
      "description": "Adds a browser action icon to the toolbar. Click the button to choose a beast. The active tab's body content is then replaced with a picture of the chosen beast. See https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Examples#beastify",
      "homepage_url": "https://github.com/mdn/webextensions-examples/tree/master/beastify",
      "icons": {
        "48": "icons/beasts-48.png"
      },
    
      "permissions": [
        "activeTab"
      ],
    
      "browser_action": {
        "default_icon": "icons/beasts-32.png",
        "default_title": "Beastify",
        "default_popup": "popup/choose_beast.html"
      },
    
      "web_accessible_resources": [
        "beasts/frog.jpg",
        "beasts/turtle.jpg",
        "beasts/snake.jpg"
      ]
    
    }
    

  * 前三个键值: [manifest_version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/manifest_version), [name](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/name), 和 [version](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version)是拓展强制的.
  * [description](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/description) and [homepage_url](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/homepage_url) 是可选, 但推荐使用: 它们用来介绍拓展的功能.
  * [icons](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/icons) 是可选, 但推荐使用：它用来标识一个应用，并在拓展管理中心进行展示
  * [permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions) 列出了拓展需要的所有权限. 在上面的例子中我们要了 [`activeTab` permission](/en-US/Add-ons/WebExtensions/manifest.json/permissions#activeTab_permission).
  * [browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action) 指定了工具栏上的按钮. 我们提供了三个信息如下: 
    * `default_icon` 强制的，按钮的图标
    * `default_title` 可选的，展示按钮的名字
    * `default_popup` 点击的时候，弹出显示，这个我们要包含这个值并指向一个HTML 
  * [web_accessible_resources](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/web_accessible_resources) 列出拓展中可以应用的访问的资源列表

提示：所有路径都是相对于manifest.json的相对路径。

### 图标

拓展应用有一个图标,它会展示在拓展管理中心,我们的manifest.json提供一个图标`icons/border-48.png`.

在文件夹下创建一个icons的文件夹,在保存`border-48.png`文件到icons下.你可以使用我们的[样例文件](https://github.com/mdn/webextensions-examples/blob/master/borderify/icons/border-48.png),一个google material 设计风格的图标,使用了协议[Creative Commons Attribution-ShareAlike](https://creativecommons.org/licenses/by-sa/3.0/) 

如果你选择使用自己的图标,应用选择48x48像素,你也可以提供96x96像素,添加如下:
    
    "icons": {
      "48": "icons/border-48.png",
      "96": "icons/border-96.png"
    }
    
### 工具栏按钮

工具栏按钮也应该有一个图标。manifest.json 提供了一个工具栏上的图标icons/beasts-32.png

### 弹出层

弹出层的功能是让我们选择三个动物中的其中一个。

在拓展目录下创建一个pop的文件夹，将弹出层的代码放入pop中保存，我们的例子保存了下面三个文件：

  * **`choose_beast.html`** 定义内容面板
  * **`choose_beast.css`** 内容的样式
  * **`choose_beast.js`** 处理我们的选择


    mkdir popup 
    cd popup
    touch choose_beast.html choose_beast.css choose_beast.js 
    

#### choose_beast.html

HTML页面如下:

    <!DOCTYPE html>
    
    <html>
      <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="choose_beast.css"/>
      </head>
    
    <body>
      <div id="popup-content">
        <div class="button beast">Frog</div>
        <div class="button beast">Turtle</div>
        <div class="button beast">Snake</div>
        <div class="button reset">Reset</div>
      </div>
      <div id="error-content" class="hidden">
        <p>Can't beastify this web page.</p><p>Try a different page.</p>
      </div>
      <script src="choose_beast.js"></script>
    </body>
    
    </html>
    

我们有一个 `[<div>](/en-US/docs/Web/HTML/Element/div)` 元素且它的id为`"popup-content"`,他包含了选择动物的元素. 另外一个`<div>`的id是`"error-content"`并有一个类`"hidden"`. 当出现异常的时候，可以使用这个div进行展示。

提示：我们还包含了CC和Js文件就像一个正常的web页面一样

#### choose_beast.css

CSS文件写定义一popup的大小，确保popup层可以包含全部选择，样式内容如下    
    
    html, body {
      width: 100px;
    }
    
    .hidden {
      display: none;
    }
    
    .button {
      margin: 3% auto;
      padding: 4px;
      text-align: center;
      font-size: 1.5em;
      cursor: pointer;
    }
    
    .beast:hover {
      background-color: #CFF2F2;
    }
    
    .beast {
      background-color: #E5F2F2;
    }
    
    .reset {
      background-color: #FBFBC9;
    }
    
    .reset:hover {
      background-color: #EAEA9D;
    }
    
    

#### choose_beast.js

下面是弹出层的页面Js文件:

    /**
     * CSS to hide everything on the page,
     * except for elements that have the "beastify-image" class.
     */
    const hidePage = `body > :not(.beastify-image) {
                        display: none;
                      }`;
    
    /**
     * Listen for clicks on the buttons, and send the appropriate message to
     * the content script in the page.
     */
    function listenForClicks() {
      document.addEventListener("click", (e) => {
    
        /**
         * Given the name of a beast, get the URL to the corresponding image.
         */
        function beastNameToURL(beastName) {
          switch (beastName) {
            case "Frog":
              return browser.extension.getURL("beasts/frog.jpg");
            case "Snake":
              return browser.extension.getURL("beasts/snake.jpg");
            case "Turtle":
              return browser.extension.getURL("beasts/turtle.jpg");
          }
        }
    
        /**
         * Insert the page-hiding CSS into the active tab,
         * then get the beast URL and
         * send a "beastify" message to the content script in the active tab.
         */
        function beastify(tabs) {
          browser.tabs.insertCSS({code: hidePage}).then(() => {
            let url = beastNameToURL(e.target.textContent);
            browser.tabs.sendMessage(tabs[0].id, {
              command: "beastify",
              beastURL: url
            });
          });
        }
    
        /**
         * Remove the page-hiding CSS from the active tab,
         * send a "reset" message to the content script in the active tab.
         */
        function reset(tabs) {
          browser.tabs.removeCSS({code: hidePage}).then(() => {
            browser.tabs.sendMessage(tabs[0].id, {
              command: "reset",
            });
          });
        }
    
        /**
         * Just log the error to the console.
         */
        function reportError(error) {
          console.error(`Could not beastify: ${error}`);
        }
    
        /**
         * Get the active tab,
         * then call "beastify()" or "reset()" as appropriate.
         */
        if (e.target.classList.contains("beast")) {
          browser.tabs.query({active: true, currentWindow: true})
            .then(beastify)
            .catch(reportError);
        }
        else if (e.target.classList.contains("reset")) {
          browser.tabs.query({active: true, currentWindow: true})
            .then(reset)
            .catch(reportError);
        }
      });
    }
    
    /**
     * There was an error executing the script.
     * Display the popup's error message, and hide the normal UI.
     */
    function reportExecuteScriptError(error) {
      document.querySelector("#popup-content").classList.add("hidden");
      document.querySelector("#error-content").classList.remove("hidden");
      console.error(`Failed to execute beastify content script: ${error.message}`);
    }
    
    /**
     * When the popup loads, inject a content script into the active tab,
     * and add a click handler.
     * If we couldn't inject the script, handle the error.
     */
    browser.tabs.executeScript({file: "/content_scripts/beastify.js"})
    .then(listenForClicks)
    .catch(reportExecuteScriptError);
    
    

开始的地方是96行. 当一个页面被打开的上，弹出层会立刻执行内容脚本，使用的是[browser.tabs.executeScript()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/executeScript) API. 如果执行内容成功, 内容脚本会被加载直到关闭页签或转到其他页签
`browser.tabs.executeScript()`可以会执行失败，例如你不能在浏览器内部的页面执行像about:debug,同步不也能在[addons.mozilla.org](https://addons.mozilla.org/)域名下执行。如果执行失败了，会执行`reportExecuteScriptError()`，隐藏`popup-content` div,显示`"error-content"` `<div>`并在console记录日志.


如果内容脚本执行成功,会调用`listenForClicks()`
它监听了弹出层的点击事件.

  * 如果点击了 `class="beast"` 按钮, 会调用 `beastify()`.
  * 如果点击了 `class="reset"` 按钮, 会调用 `reset()`.

 `beastify()` 函数执行如下三件事情:

  * 映射点击按钮的指向动物图片的URL
  * 隐藏页面内容 [browser.tabs.insertCSS()](/en-US/Add-ons/WebExtensions/API/tabs/insertCSS) API
  * 发送 "beastify" 消息给内容脚本,使用 [browser.tabs.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/sendMessage) API, 请求 beastify 页面展示动物图片.

 `reset()` 函数重置操作:

  *通过 [browser.tabs.removeCSS()](/en-US/Add-ons/WebExtensions/API/tabs/removeCSS) API移除我们添加的CSS,
  * 发送`reset`消息给内容脚本,去请求重置页面

### The content script

创建内容脚本目录`content_scripts`并创建文件beastify.js,并写入如下内容:    
    
    (function() {
      /**
       * Check and set a global guard variable.
       * If this content script is injected into the same page again,
       * it will do nothing next time.
       */
      if (window.hasRun) {
        return;
      }
      window.hasRun = true;
    
      /**
       * Given a URL to a beast image, remove all existing beasts, then
       * create and style an IMG node pointing to
       * that image, then insert the node into the document.
       */
      function insertBeast(beastURL) {
        removeExistingBeasts();
        let beastImage = document.createElement("img");
        beastImage.setAttribute("src", beastURL);
        beastImage.style.height = "100vh";
        beastImage.className = "beastify-image";
        document.body.appendChild(beastImage);
      }
    
      /**
       * Remove every beast from the page.
       */
      function removeExistingBeasts() {
        let existingBeasts = document.querySelectorAll(".beastify-image");
        for (let beast of existingBeasts) {
          beast.remove();
        }
      }
    
      /**
       * Listen for messages from the background script.
       * Call "beastify()" or "reset()".
      */
      browser.runtime.onMessage.addListener((message) => {
        if (message.command === "beastify") {
          insertBeast(message.beastURL);
        } else if (message.command === "reset") {
          removeExistingBeasts();
        }
      });
    
    })();
    
内容脚本第一件事就是检查全局变量`window.hasRun`,如果已经存在则退出,否则设置 `window.hasRun`并继续执行.原因是打开新页签就执行内容脚本,当我们打开多个页签的时候,我们要保证脚本只能在单页签上执行

然后,执行开始在第40行.使用[browser.runtime.onMessage](/en-US/Add-ons/WebExtensions/API/runtime/onMessage) API监听着弹出层发出的消息


  * 如果消息是 "beastify",我们期望他包含着一张动物(野兽)的图片.我们移除之前添加的动物(野兽的图片),并构造一个新的野兽的图片
  * 如果消息是 "reset", 移除我们添加的页面元素.

### The beasts

最后,我们需要动物的图片

创建一个文件夹`beasts,并添加图片,图片可以在[the GitHub repository](https://github.com/mdn/webextensions-examples/tree/master/beastify/beasts)获取


![](https://mdn.mozillademos.org/files/11459/frog.jpg)
![](https://mdn.mozillademos.org/files/11461/snake.jpg)
![](https://mdn.mozillademos.org/files/11463/turtle.jpg)

## 测试

重新检测一下你的文件：
    
    
    beastify/
        beasts/
            frog.jpg
            snake.jpg
            turtle.jpg
        content_scripts/
            beastify.js
        icons/
            beasts-32.png
            beasts-48.png
        popup/
            choose_beast.css
            choose_beast.html
            choose_beast.js
        manifest.json

打开 "about:debugging" 页面, 选中 "调试拓展" 并选中你的文件夹进行加载到浏览器.

这样应用就被安装了,直到你重启了浏览器,否则它会一直存在.

打开一个页面，点击按钮查看一下页面变化

## Developing from the command line

你也可以通过[web-ext](/en-US/Add-ons/WebExtensions/Getting_started_with_web-ext) 工具进行命令执行:

    cd beastify
    web-ext run

