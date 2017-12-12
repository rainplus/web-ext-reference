要拦截HTTP请求，请使用[`webRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest "为各个阶段添加事件侦听器做出一个HTTP请求。 事件监听器接收详细信息关于请求，并且可以修改或者取消请求。")API。这个API使您能够为发出HTTP请求的各个阶段添加监听器。 在监听器中，你可以：

   *获得访问请求标题和正文，和响应头
   *取消并重定向请求
   *修改请求和响应头

在本文中，我们将看看`webRequest`的三种不同用途模块：

   *记录请求URL。
   *请求重定向。
   *修改请求头。

## 记录URL日志

创建一个名为“请求”的新目录。 在该目录中创建一个文件称为“manifest.json”，其具有以下内容：
    
    {
      "description": "Demonstrating webRequests",
      "manifest_version": 2,
      "name": "webRequest-demo",
      "version": "1.0",
    
      "permissions": [
        "webRequest",
        "<all_urls>"
      ],
    
      "background": {
        "scripts": ["background.js"]
      }
    }

接下来，创建一个名为“background.js”的文件，内容如下：
    
    function logURL(requestDetails) {
      console.log("Loading: " + requestDetails.url);
    }
    
    browser.webRequest.onBeforeRequest.addListener(
      logURL,
      {urls: ["<all_urls>"]}
    );
    
    
在这里我们使用[`onBeforeRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "这个事件是在一个请求即将被触发时触发的。 如果你想取消或重定向请求，是一个很好的地方")在启动请求之前调用`logURL（）`函数。 `logURL（）`函数从事件对象获取请求的URL并将其记录到浏览器控制台。 “{url：[<all_urls>”]} [pattern]（/ en-US / Add-ons / WebExtensions / Match_patterns）意味着我们将拦截所有URL的HTTP请求。

要测试它，[先安装拓展](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox), [打开浏览器控制台](/en-US/docs/Tools/Browser_Console)，然后打开一些网页。 在浏览器控制台中，您应该可以看到浏览器请求的任何资源的URL。

## 请求重定向

现在让我们使用`webRequest`重定向HTTP请求。 首先，用下面的内容替换manifest.json：

    {
    
      "description": "Demonstrating webRequests",
      "manifest_version": 2,
      "name": "webRequest-demo",
      "version": "1.0",
    
      "permissions": [
        "webRequest",
        "webRequestBlocking",
        "https://mdn.mozillademos.org"
      ],
     
      "background": {
        "scripts": ["background.js"]
      }
    
    }

唯一修改了的地方是添加了 "webRequestBlocking" [权限](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions). 无论何时我们主动修改请求，我们都需要额外的权限。

接下来，重写"background.js":

    var pattern = "https://mdn.mozillademos.org/*";
    
    function redirect(requestDetails) {
      console.log("Redirecting: " + requestDetails.url);
      return {
        redirectUrl: "https://38.media.tumblr.com/tumblr_ldbj01lZiP1qe0eclo1_500.gif"
      };
    }
    
    browser.webRequest.onBeforeRequest.addListener(
      redirect,
      {urls:[pattern], types:["image"]},
      ["blocking"]
    );

再一次，我们使用了 [`onBeforeRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when a request is about to be made, and before headers are available. This is a good place to listen if you want to cancel or redirect the request.") 监听每一个请求. 函数会在`redirect`中将目标的url替换。

我们并没有监听每一个请求:  `{urls:[pattern],types:["image"]}` 指定了我们进行拦截的请求
    
* 只在"https://mdn.mozillademos.org/" 下面的url请求
* 只针对图片资源.查阅[webRequest.RequestFilter`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/RequestFilter "An object describing filters to apply to webRequest events.") 获得更多详情

我们想修改请求的内容的时候，我们要传输一个参数`blocking`,这让监听器阻塞请求，等待监听器返回结果才能继续执行。
查阅 [`webRequest.onBeforeRequest`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeRequest "This event is triggered when a request is about to be made, and before headers are available. This is a good place to listen if you want to cancel or redirect the request.")获取关于"blocking"更多的信息.

测试这个拓展要重新打开一个mdn上多图处的页面，重新加载拓展，并重新打开MDN的页面。
## 修改请求头
最后我们使用`webRequest` 来修改请求头信息. 在这个案例中我们进行 "User-Agent" 修改成 Opera 12.16, 仅在http://useragentstring.com/的页面下

"manifest.json"保持如上面的例子一致。

替换"background.js" 如下:
    
    var targetPage = "http://useragentstring.com/*";
    
    var ua = "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16";
    
    function rewriteUserAgentHeader(e) {
      for (var header of e.requestHeaders) {
        if (header.name.toLowerCase() == "user-agent") {
          header.value = ua;
        }
      }
      return {requestHeaders: e.requestHeaders};
    }
    
    browser.webRequest.onBeforeSendHeaders.addListener(
      rewriteUserAgentHeader,
      {urls: [targetPage]},
      ["blocking", "requestHeaders"]
    );

我们使用了 [`onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered before sending any HTTP data, but after all HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.") 事件监听来监听请求在发送请求头。

监听匹配了 `targetPage` [pattern](/en-US/Add-ons/WebExtensions/Match_patterns)的请求. 同时我们还发送了`"blocking"` 参数. 
我们还发送了requestHeaders，这意味着监听器将传递一个包含我们期望发送的请求头的数组.查阅[`webRequest.onBeforeSendHeaders`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onBeforeSendHeaders "This event is triggered before sending any HTTP data, but after all HTTP headers are available. This is a good place to listen if you want to modify HTTP request headers.") 来获取更多的信息.

侦听器函数在请求头数组中查找“User-Agent”头，用“ua”变量的值替换其值，并返回修改过的数组。 这个修改过的数组现在将被发送到服务器。

## 了解更多

要了解所有可以使用“webRequest”API执行的操作，请参阅 [reference documentation](/en-US/Add-ons/WebExtensions/API/WebRequest).

