
“选项”页面使您可以定义用户可以更改的扩展的首选项。 用户可以从浏览器的加载项管理器访问扩展的选项页面：

用户访问该页面的方式，以及将其集成到浏览器用户界面的方式因浏览器而异


您可以通过调用[`runtime.openOptionsPage()`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/Runtime/openOptionsPage "If your add-on does not have an options page, or the browser failed to create one for some other reason, runtime.lastError will be set.")以编程方式打开页面.

选项页面有一个内容安全策略，限制它们可以从中加载资源的来源，并且禁止一些不安全的做法，比如使用[eval()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)。 有关更多详细信息，请参阅[内容安全策略](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy)。


## 指定选项页

要创建选项页面，请编写一个定义页面的HTML文件。 这个页面可以包含CSS和JavaScript文件，就像普通的网页一样。 此页面来自[收藏颜色](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)示例，其中包含一个JavaScript文件：


    <!DOCTYPE html>
    
    <html>
      <head>
        <meta charset="utf-8">
      </head>
    
    <body>
      <form>
          <label>Favourite colour</label>
          <input type="text" id="colour" >
          <button type="submit">Save</button>
      </form>
      <script src="options.js"></script>
    </body>
    
    </html>

运行在页面上的JavaScript可以使用附件具有[permissions](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions)的所有[WebExtension APIs](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API)。 特别是，您可以使用[`storage`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/Storage)启用WebExtensions存储和检索数据，API监听存储的项目的变化来保持偏好。

将页面的文件打包到您的扩展中。
您还需要在manifest.json文件中包含[options_ui](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)键， 给它的网页的地址。

    "options_ui": {
      "page": "options.html",
      "browser_style": true
    },

## 示例

在[GitHub](https://github.com/mdn/webextensions-examples)上的仓库，包含几个使用选项页的例子：


  * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour) example extension with options page

