内容脚本（content scripts）是您的扩展的一部分，它运行在特定网页的上下文中（而不是作为扩展的一部分的后台脚本(background)或作为网站本身一部分的脚本，例如使用[`<script>`](/en-US/docs/Web/HTML/Element/script "The HTML <script> element is used to embed or reference an executable script.") 加载的脚本.

[后台脚本 background scripts](/en-US/Add-ons/WebExtensions/Background_scripts)可以访问所有的[WebExtension JavaScript API](/en-US/Add- ons/WebExtensions/API)，但是它们不能直接访问网页内容。 所以如果你的扩展需要这样做，你需要内容脚本(content scripts)。

就像普通网页加载的脚本一样，内容脚本(content scripts)可以使用标准的DOM API来读取和修改他们页面的内容。

内容脚本可以直接访问一小部分的[WebExtension APIs](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Content_scripts#WebExtension_APIs), 但是它们可以通过消息机制与[后台脚本background scripts](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Content_scripts#Communicating_with_background_scripts)进行交互

请注意，内容脚本目前被阻止在addons.mozilla.org和testpilot.firefox.com上运行。 如果您尝试将内容脚本插入这些域中的页面，则该脚本将失败，并且该页面将记录[CSP](/en-US/docs/Web/HTTP/CSP) 错误.

## 加载内容脚本（content scripts）

你可以使用两种方式进行加载内容脚本：

  * **显示声明** : 在manifest.json中显示声明[content_scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts) 进行引用一个内容脚本，并使用模式匹配要加载该内容脚本的链接 [匹配模式](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/match_patterns)
  * **编程调用** : 使用[tabs.executeScript()](/en-US/Add-ons/WebExtensions/API/Tabs/executeScript) API, 你可以在你指定的页答进行加载内容脚本，例如可以在点击一个[browser action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action)的时候进行加载.

每个扩展每个frame只有一个全局范围，所以不管内容脚本如何加载，来自不同内容脚本的变量都可以直接被另一个内容脚本访问。

## 内容脚本（Content script）的环境变量

### DOM 权限

内容脚本可以访问和修改页面的DOM，就像普通的页面脚本一样。 他们还可以看到页面脚本对DOM所做的任何更改。

内容脚本会获得“清晰的DOM视图”。 意即：

  * 内容脚本对网页内的js变量不可见。
  * 如果网页内的js修改了dom，内容脚本也不见最新的dom

在 Gecko中, 这个行为叫做 [Xray vision](/en-US/docs/Xray_vision).

举例如下：

    <!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
      </head>
    
      <body>
        <script src="page-scripts/page-script.js"></script>
      </body>
    </html>

网页脚本 "page-script.js" 做了如下的变更:

    // page-script.js
    
    // add a new element to the DOM
    var p = document.createElement("p");
    p.textContent = "This paragraph was added by a page script.";
    p.setAttribute("id", "page-script-para");
    document.body.appendChild(p);
    
    // define a new property on the window
    window.foo = "This global variable was added by a page script";
    
    // redefine the built-in window.confirm() function
    window.confirm = function() {
      alert("The page script has also redefined 'confirm'");
    }

拓展注入了一个内容脚本如下：
    
    
    // content-script.js
    
    // can access and modify the DOM
    var pageScriptPara = document.getElementById("page-script-para");
    pageScriptPara.style.backgroundColor = "blue";
    
    // can't see page-script-added properties
    console.log(window.foo);  // undefined
    
    // sees the original form of redefined properties
    window.confirm("Are you sure?"); // calls the original window.confirm()

这个问题，反过来也是成立的，即：内容脚本修改的内容，网页的脚本也是看不到的

所有这一切意味着内容脚本可以依靠DOM属性进行预测，而不必担心变量定义与页面脚本中定义的变量冲突。

这种行为的一个实际结果是内容脚本将无法访问由该页面加载的任何JavaScript库。 因此，例如，如果页面包含jQuery，内容脚本将无法看到它。

如果内容脚本确实想要使用JavaScript库，则应该将库本身作为内容脚本注入，并与要使用它的内容脚本一起使用：
        
    "content_scripts": [
      {
        "matches": ["*://*.mozilla.org/*"],
        "js": ["jquery.js", "content-script.js"]
      }
    ]

### 拓展接口 WebExtension APIs

除了标准的DOM API之外，内容脚本还可以使用以下WebExtension API：

来自 [extension](/en-US/Add-ons/WebExtensions/API/extension):

  * [getURL()](/en-US/Add-ons/WebExtensions/API/extension#getURL\(\))
  * [inIncognitoContext](/en-US/Add-ons/WebExtensions/API/extension#inIncognitoContext)

来自 [runtime](/en-US/Add-ons/WebExtensions/API/runtime):

  * [connect()](/en-US/Add-ons/WebExtensions/API/runtime#connect\(\))
  * [getManifest()](/en-US/Add-ons/WebExtensions/API/runtime#getManifest\(\))
  * [getURL()](/en-US/Add-ons/WebExtensions/API/runtime#getURL\(\))
  * [onConnect](/en-US/Add-ons/WebExtensions/API/runtime#onConnect)
  * [onMessage](/en-US/Add-ons/WebExtensions/API/runtime#onMessage)
  * [sendMessage()](/en-US/Add-ons/WebExtensions/API/runtime#sendMessage\(\))

来自 [i18n](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n):

  * [getMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getMessage)
  * [getAcceptLanguages()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getAcceptLanguages)
  * [getUILanguage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getUILanguage)
  * [detectLanguage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/detectLanguage)

来自[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)API的全部.

### 获取请求和获取 XHR and Fetch

内容脚本可以使用 [window.XMLHttpRequest](/en-US/docs/Web/API/XMLHttpRequest) and [window.fetch()](/en-US/docs/Web/API/Fetch_API) APIs进行发送请求.

内容脚本拥有拓展的权限，当拓展在manifest.json中定义了[permissions](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/permissions)有了跨域权限的时候，内容脚本也会拥有相应的权限。

这是通过在内容脚本中暴露更多特权的XHR和获取实例来实现的，其具有不设置[Origin](/en-US/docs/Web/HTTP/Headers/Origin)和[[Referer](/en-US/docs/Web/HTTP/Headers/Referer)请求头一致的效果，就像来自页面本身的请求一样，这通常是最好的，以防止请求显示其交叉性质。从版本58开始，需要执行内容本身发送的请求的扩展可以使用“content.XMLHttpRequest”和“content.fetch（）”。 对于跨浏览器扩展，他们的存在必须是功能检测。

## 与后台脚本交互

尽管内容脚本不能直接使用大多数WebExtension API，但它们可以使用消息传递API与扩展的后台脚本进行通信，因此可以间接访问所有与后台脚本相同的API。

在后台脚本和内容脚本之间进行通信有两种基本模式：您可以发送一次性消息和一个可选响应，也可以在双方之间建立一个长期连接，并使用该连接交换消息。


### 一次性消息

要发送一次性消息和一个可选的响应，您可以使用以下API：

  | 内容脚本 | 后台脚本  
---|---|---  
发送消息| [browser.runtime.sendMessage()](/en-US/Add-ons/WebExtensions/API/runtime#sendMessage\(\)) | browser.tabs.sendMessage()](/en-US/Add-ons/WebExtensions/API/Tabs/sendMessage)  
接收消息 | [browser.runtime.onMessage](/en-US/Add-ons/WebExtensions/API/runtime/onMessage) | [browser.runtime.onMessage](/en-US/Add-ons/WebExtensions/API/runtime#onMessage)  
  
例如，下面是一个内容脚本，用于监听网页中的点击事件。 如果点击位于链接上，则会通过目标网址向后台页面发送消息：  
    // content-script.js
    
    window.addEventListener("click", notifyExtension);
    
    function notifyExtension(e) {
      if (e.target.tagName != "A") {
        return;
      }
      browser.runtime.sendMessage({"url": e.target.href});
    }

后台脚本会监听这些消息，并使用 [notifications](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications) API对消息进行显示通知:

    // background-script.js
    
    browser.runtime.onMessage.addListener(notify);
    
    function notify(message) {
      browser.notifications.create({
        "type": "basic",
        "iconUrl": browser.extension.getURL("link.png"),
        "title": "You clicked a link!",
        "message": message.url
      });
    }
    

是这案例是在 [GitHub notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n) 上

### 基于连接的消息传递

如果您在后台脚本和内容脚本之间交换大量消息，则发送一次性消息可能会非常麻烦。所以另一种模式是在两个上下文之间建立一个更长的连接，并使用这个连接来交换消息。

每一端都有[runtime.Port](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port) 对象, 它们用来交互消息：

创建连接:

  * 一端使用[runtime.onConnect](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect)监听连接
  * 另一端使用[tabs.connect()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/connect) 发起请求(内容脚本使用) 或 [runtime.connect()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/connect) (后台脚本使用). 会返回一个 [runtime.Port](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port) 对象.
  * 然后[runtime.onConnect](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect) 也会得到一个[runtime.Port](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port) 对象.

每一端都有一个port对象, 两端可以通过使用`runtime.Port.postMessage()` 发送消息并使用 `runtime.Port.onMessage` 接收消息。

举个例子, 内容脚本 content script:

  * 连接到后台脚本，并保存一个Port对象到全局变量myPort
  * 在myPort上进行监听消息
  * 点击文档的的时候向后台发送消息
    
    // content-script.js
    
    var myPort = browser.runtime.connect({name:"port-from-cs"});
    myPort.postMessage({greeting: "hello from content script"});
    
    myPort.onMessage.addListener(function(m) {
      console.log("In content script, received message from background script: ");
      console.log(m.greeting);
    });
    
    document.body.addEventListener("click", function() {
      myPort.postMessage({greeting: "they clicked the page!"});
    });

相应的后台脚本 background script:

  * 监听连接
  * 当一个连接到达的时候: 
    * 保存成本地变量`portFromCS`
    * 使用port向内容脚本发送一个消息
    * 使用 port进行监听，并记录
  * 进行浏览器操作的时候使用`portFromCS`向内容脚本发送消息

    // background-script.js
    
    var portFromCS;
    
    function connected(p) {
      portFromCS = p;
      portFromCS.postMessage({greeting: "hi there content script!"});
      portFromCS.onMessage.addListener(function(m) {
        console.log("In background script, received message from content script")
        console.log(m.greeting);
      });
    }
    
    browser.runtime.onConnect.addListener(connected);
    
    browser.browserAction.onClicked.addListener(function() {
      portFromCS.postMessage({greeting: "they clicked the button!"});
    });
    

## 与网页进行交互

即使内容脚本不能获取页面脚本创建的脚本，但是它们可与页面脚本进行交互，使用[window.postMessage](/en-US/docs/Web/API/Window/postMessage) and[window.addEventListener](/en-US/docs/Web/API/EventTarget/addEventListener) APIs.

示例:
    
    // page-script.js
    
    var messenger = document.getElementById("from-page-script");
    
    messenger.addEventListener("click", messageContentScript);
    
    function messageContentScript() {
      window.postMessage({
        direction: "from-page-script",
        message: "Message from the page"
      }, "*");
    
    
    // content-script.js
    
    window.addEventListener("message", function(event) {
      if (event.source == window &&
          event.data &&
          event.data.direction == "from-page-script") {
        alert("Content script received message: \"" + event.data.message + "\"");
      }
    });

这是一个完成的安全，请在[GitHub](https://mdn.github.io/webextensions-examples/content-script-page-script-messaging.html)上进行查阅


请注意，只要您通过这种方式与不受信任的网络内容进行互动，就需要非常小心。 扩展是具有强大功能的特权代码，恶意网页可以轻易诱骗他们访问这些功能。

为了做一个简单的例子，假设收到消息的内容脚本代码是这样的：

    
    
    // content-script.js
    
    window.addEventListener("message", function(event) {
      if (event.source == window &&
          event.data.direction &&
          event.data.direction == "from-page-script") {
        eval(event.data.message);
      }
    });

现在，页面脚本可以运行具有内容脚本的所有特权的任何代码。

## 与页面脚本分享对象

本部分介绍的技术仅适用于Firefox，仅适用于Firefox 49以上版本。

作为一个扩展开发者，你应该考虑在任意网页上运行的脚本是恶意代码，其目的是窃取用户的个人信息，损害他们的计算机，或以其他方式攻击他们。

内容脚本与网页加载的脚本之间的隔离旨在使恶意网页更难以执行此操作。

由于本节描述的技术打破了这种隔离，所以它们本质上是危险的，应该小心使用。

我们知道了内容脚本的[DOM access](/en-US/Add-ons/WebExtensions/Content_scripts#DOM_access)并不能知道页面脚本修改后的内容。
这意味着如果页面上加载了Jquery库，内容脚本并不能使用它们，内容脚本必须进行加载JQuery库，相应地，页面脚本也不能看到内容脚本做出的修改。

然后，firefox提交一些API进行如下的操作

  * 访问页面脚本创建的js对象
  * 暴露内容脚本中的js对象给页面脚本

### Firefox的X光检视

在Firefox中，内容脚本和页面脚本之间的一部分隔离是使用称为“Xray视觉”的功能实现的。当特权更高的作用域中的脚本访问在低权限范围内定义的对象时，它只会看到该对象的“本地版本”。 任何[expando](/en-US/docs/Glossary/Expando)属性都是不可见的，如果对象的任何属性已被重新定义，则会看到原始实现，而不是重新定义的版本。

此功能的目的是通过重新定义对象的本机属性，使得权限较低的脚本难以混淆具有较多特权的脚本。

例如，当内容脚本访问页面的[window](/en-US/docs/Web/API/Window)时，它将不会看到页面脚本添加到窗口的任何属性，并且如果页面脚本具有 重新定义窗口的任何现有属性，内容脚本将只看到原始版本。


更多内容请查查看[Xray vision](/en-US/docs/Mozilla/Tech/Xray_vision) and [Script security](/en-US/docs/Mozilla/Gecko/Script_security).

### 从内容脚本访问页面脚本对象

在Firefox中, 内容脚本的DOM Object 会有一个额外的属性`wrappedJSObject`. 这是由页面脚本修改后的对象的包装

举个例子，如下页面    
    
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
      </head>
      <body>
        <script type="text/javascript" src="main.js"></script>
      </body>
    </html>

页面脚本可以定义对象
    
    
    // main.js
    
    var foo = "I'm defined in a page script!";

X视觉功能会隔离内容脚本，所有内容脚本无法获取数据
    
    
    // content-script.js
    
    console.log(window.foo); // undefined

在Firefox中，内容脚本可以使用`window.wrappedJSObject` 查看这个属性:

    // content-script.js
    
    console.log(window.wrappedJSObject.foo); // "I'm defined in a page script!"
请注意，一旦你这样做，你就不能再依赖这个对象的任何属性或函数，或者正在做你期望的事情。它们中的任何一个，甚至是setter和getter，都可能被不可信的代码重新定义。

还要注意，展开是传递性的：当你使用`wrappedJSObject`时，展开对象的任何属性本身都是解包的（因此不可靠）。所以这是一个很好的做法，一旦你得到了你需要的对象，重新包装它，你可以这样做：

    
    
    XPCNativeWrapper(window.wrappedJSObject.foo);

更多信息请查阅 [Xray vision](/en-US/docs/Mozilla/Tech/Xray_vision) .

### 页面脚本访问内容脚本中的对象

Firefox 也让页面脚本可以访问内容脚本的对象，如下面的两个脚本:

  * [exportFunction()](/en-US/Add-ons/WebExtensions/Content_scripts#exportFunction): export a function to page scripts.
  * [cloneInto()](/en-US/Add-ons/WebExtensions/Content_scripts#cloneInto): export an object to page scripts.

#### exportFunction

导出内容脚本的函数到页面脚本的作用域，使页面脚本可以进行调用：

示例, 使后台脚本如下:
    
    /*
    Execute content script in the active tab.
    */
    function loadContentScript() {
      browser.tabs.executeScript({
        file: "/content_scripts/export.js"
      });
    }
    
    /*
    Add loadContentScript() as a listener to clicks
    on the browser action.
    */
    browser.browserAction.onClicked.addListener(loadContentScript);
    
    /*
    Show a notification when we get messages from
    the content script.
    */
    browser.runtime.onMessage.addListener((message) => {
      browser.notifications.create({
        type: "basic",
        title: "Message from the page",
        message: message.content
      });
    });

这个后台脚本做了如下的两件事情:

  * 当用户点击浏览器操作的时候，加载一个内容脚本
  * 监听内容脚本，并在获取一个消息之后，使用 [notification](/en-US/Add-ons/WebExtensions/API/notifications) 进行展示.

执行的内容脚本如下:

    
    
    /*
    Define a function in the content script's scope, then export it
    into the page script's scope.
    */
    function notify(message) {
      browser.runtime.sendMessage({content: "Function call: " + message});
    }
    
    exportFunction(notify, window, {defineAs:'notify'});

定义`notify()`向后台脚本发送了消息. 并导出了这个方法到页面脚本作用域，现在让我们在页面脚本上进行调用：

    window.notify("Message from the page script!");

查阅完整的信息[Components.utils.exportFunction](/en-US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.exportFunction).

#### 克隆

在内容脚本上定义一个对象，可以克隆这个对象到页面脚本作用域。默认地，这个使用的是[structured clone algorithm](/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)，意味着克隆对象并没有复制这个对象的函数。要使函数也一直复制，可以使用`cloneFunctions`

示例,这时在内容脚本定义了一个对象包含了函数，将它克隆到页面脚本中

    
    
    /*
    Create an object that contains functions in
    the content script's scope, then clone it
    into the page script's scope.
    
    Because the object contains functions,
    the cloneInto call must include
    the `cloneFunctions` option.
    */
    var messenger = {
      notify: function(message) {
        browser.runtime.sendMessage({
          content: "Object method call: " + message
        });
      }
    };
    
    window.wrappedJSObject.messenger = cloneInto(
      messenger,
      window,
      {cloneFunctions: true});

页面脚本会在window对象中新增一个属性 `messenger`, 并拥有函数 `notify()`:

  
    window.messenger.notify("Message from the page script!");

更多详情请查阅[Components.utils.cloneInto](/en-US/docs/Mozilla/Tech/XPCOM/Language_Bindings/Components.utils.cloneInto).

## 在内容脚本中执行 eval() 

在Chrome中，[eval()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)始终在内容脚本的上下文中运行代码，而不是在页面上下文中运行代码。

在Firefox中:

  *  `eval()`运行在后台脚本中
  *  `window.eval()`运行在页面脚本中

示例, 如下面的脚本:

    
    
    // content-script.js
    
    window.eval('window.x = 1;');
    eval('window.y = 2');
    
    console.log(`In content script, window.x: ${window.x}`);
    console.log(`In content script, window.y: ${window.y}`);
    
    window.postMessage({
      message: "check"
    }, "*");

这段代码仅仅使用`window.eval()`和`eval()`,并记录在日志中，然后发送消息给页面。

一旦页面脚本接收到了消息，也会在日志中进行记录：
    
    
    window.addEventListener("message", function(event) {
      if (event.source === window && event.data && event.data.message === "check") {
        console.log(`In page script, window.x: ${window.x}`);
        console.log(`In page script, window.y: ${window.y}`);
      }
    });

在chrome会产生如下输出：
    
    In content script, window.x: 1
    In content script, window.y: 2
    In page script, window.x: undefined
    In page script, window.y: undefined

在firefox会产生如下输出：
    
    In content script, window.x: undefined
    In content script, window.y: 2
    In page script, window.x: 1
    In page script, window.y: undefined


[setTimeout()](/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)，[setInterval()](/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval)和[Function()](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function).也同此原理。

当在页面上下文中运行代码时，“上面的”[与页面脚本共享内容脚本对象](/en-US/Add-ons/WebExtensions/Content_scripts#Sharing_objects_with_page_scripts)部分中的警告适用于：页面环境受到控制通过潜在的恶意网页，它可以重新定义你与之交互的对象的行为意外的方法

    // page.js redefines console.log
    
    var original = console.log;
    
    console.log = function() {
      original(true);
    }
    
    
    
    // content-script.js calls the redefined version
    
    window.eval('console.log(false)');
    

