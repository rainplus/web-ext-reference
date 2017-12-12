设置页面使用户能够查看和更改扩展的设置（有时也称为“首选项”或“选项”）。

使用WebExtension API时，设置通常使用[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)API存储。 实现设置页面有三个步骤：

   * 编写一个显示设置的HTML文件，让用户改变它们。
   * 编写一个包含在HTML文件中的脚本，用于填充存储设置页面，并在用户更改存储设置时更新存储的设置。
   * 在manifest.json中设置HTML文件的路径为`[options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json options_ui)`。 通过这样做，HTML文档将显示在浏览器的插件管理器中，以及扩展名和描述。

您还可以使用`[runtime.openOptionsPage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/openOptionsPage)`功能以编程方式打开此页面。

## 一个简单的拓展

首先，我们将编写一个扩展，为用户访问的每个页面添加蓝色边框。

创建一个名为“settings”的新目录，然后在其中创建一个名为“manifest.json”的文件，其内容如下：

    {
      "manifest_version": 2,
      "name": "Settings example",
      "version": "1.0",
    
      "content_scripts": [
        {
          "matches": ["<all_urls>"],
          "js": ["borderify.js"]
        }
      ]
    }

该扩展指示浏览器在用户访问的所有网页中加载名为“borderify.js”的内容脚本。

接下来，在“settings”目录下创建一个名为“borderify.js”的文件，并给它们这些内容：

    document.body.style.border = "10px solid blue";

This just adds a blue border to the page.

安装和测试

## Adding settings

现在让我们创建一个设置页面，让用户设置边框的颜色。

首先，更新“manifest.json”，使其具有以下内容：

    {
      "manifest_version": 2,
      "name": "Settings example",
      "version": "1.0",
      "content_scripts": [
        {
          "matches": ["<all_urls>"],
          "js": ["borderify.js"]
        }
      ],
      "options_ui": {
        "page": "options.html"
      },
      "permissions": ["storage"]
    }
    
我们添加了两个新的清单键：

   * [options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)这将HTML文档设置为此扩展的设置页面（也称为选项页面）。
   * [permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)：我们将使用[storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage) API来存储设置，我们需要请求使用这个API的权限。

接下来，因为我们已经承诺提供“options.html”，所以我们来创建它。在“settings”目录下创建一个具有这个名字的文件，并给它以下内容：

    <!DOCTYPE html>
    
    <html>
      <head>
        <meta charset="utf-8">
      </head>
    
      <body>
    
        <form>
            <label>Border color<input type="text" id="color" ></label>
            <button type="submit">Save</button>
        </form>
    
        <script src="options.js"></script>
    
      </body>
    
    </html>



这定义了一个[<form>](/en-US/docs/Web/HTML/Element/form) HTML 元素表示一个文档部分，其中包含交互式控件以向Web服务器提交信息。 与一个带标签的文本[<input>](/en- US/docs/Web/HTML/Element/input) HTML <input>元素用于为基于Web的表单创建交互式控件， <button>元素代表一个可点击的按钮。 它还包含一个名为“options.js”的脚本。


再次在“settings”目录中创建“options.js”，并给它以下内容：
    
    function saveOptions(e) {
      e.preventDefault();
      browser.storage.local.set({
        color: document.querySelector("#color").value
      });
    }
    
    function restoreOptions() {
    
      function setCurrentChoice(result) {
        document.querySelector("#color").value = result.color || "blue";
      }
    
      function onError(error) {
        console.log(`Error: ${error}`);
      }
    
      var getting = browser.storage.local.get("color");
      getting.then(setCurrentChoice, onError);
    }
    
    document.addEventListener("DOMContentLoaded", restoreOptions);
    document.querySelector("form").addEventListener("submit", saveOptions);
    
他做了如下两点：

   *当文档已经加载时，它使用[storage.local.get()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/StorageArea/get)。 如果该值未设置，则使用默认的“蓝色”。
   *当用户通过点击“保存”提交表单时，它使用[storage.local.set()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/StorageArea/set)。

最后，更新“borderify.js”以从存储中读取边框颜色：

由于52版之前的Firefox版本中存在[storage.local.get()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage/StorageArea/get)中的错误，下面的代码将不起作用。 为了使它在52以下的Firefox版本中起作用，必须将`onGot（）`中两个`item.color`改为`item [0] .color`。

     function onError(error) {
      console.log(`Error: ${error}`);
    }
    
    function onGot(item) {
      var color = "blue";
      if (item.color) {
        color = item.color;
      }
      document.body.style.border = "10px solid " + color;
    }
    
    var getting = browser.storage.local.get("color");
    getting.then(onGot, onError);
    

再次检查拓展的文件：

    settings/
        borderify.js
        manifest.json
        options.html
        options.js

加载拓展并进行测试

## 了解更多

  * [options_ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui) manifest key 参考文档
  * [storage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage) API 参考文档
  * 直接使用API打开首选页 [runtime.openOptionsPage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/openOptionsPage) API
  * 设置页面案例: 
    * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)

