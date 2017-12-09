在这篇文章中我们通过从头到尾进行创建一个firefox拓展。拓展只是装简单地给mozilla.org及子域名的页面添加红色的边框。

本章节源代码: [Github](https://github.com/mdn/webextensions-examples/tree/master/borderify)

首先，请确认你的firefox浏览器版本>=45

## 写拓展

创建一个文件夹并进入:

    mkdir borderify
    cd borderify

### manifest.json

在文件夹下创建 manifest.json文件，并添加如下内容：

    {    
      "manifest_version": 2,
      "name": "Borderify",
      "version": "1.0",
      "description": "Adds a red border to all webpages matching mozilla.org.",
      "icons": {
        "48": "icons/border-48.png"
      },
      "content_scripts": [
        {
          "matches": ["*://*.mozilla.org/*"],
          "js": ["borderify.js"]
        }
      ]
    }

  * 前三个键值: [manifest_version](/en-US/Add-ons/WebExtensions/manifest.json/manifest_version), [name](/en-US/Add-ons/WebExtensions/manifest.json/name), 和 [version](/en-US/Add-ons/WebExtensions/manifest.json/version)是拓展强制的基本元数据。
  * [description](/en-US/Add-ons/WebExtensions/manifest.json/description)是可选的, 但建议加上: 它可以简单描述拓展的功能.
  * [icons](/en-US/Add-ons/WebExtensions/manifest.json/icons)是可选的, 但建议加上: 它可以标识你的拓展，并在拓展中心进行展示.

最有趣的键值是`[content_scripts](/en-US/Add-ons/WebExtensions/manifest.json/content_scripts)`, 它告诉浏览器在页面上加载这些匹配了模式的脚本. 在上面的例子中,我们在`*://*.mozilla.org/*`下加载了`borderify.js`.

  * [了解内容脚本](/en-US/Add-ons/WebExtensions/Content_scripts)
  * [了解匹配模式(正则)](/en-US/Add-ons/WebExtensions/Match_patterns).

[在特殊的情况下你需要添加ID标高你的拓展](/en-US/Add-ons/WebExtensions/WebExtensions_and_the_Add-on_ID#When_do_you_need_an_Add-on_ID). 如果需要指定一个ID,要添加`[applications](/en-US/Add-ons/WebExtensions/manifest.json/applications)` 键值,并设置gecko.id,如下:

    "applications": {
      "gecko": {
        "id": "borderify@example.com"
      }
    }

### 图标 icons/border-48.png

拓展应用有一个图标,它会展示在拓展管理中心,我们的manifest.json提供一个图标`icons/border-48.png`.

在文件夹下创建一个icons的文件夹,在保存`border-48.png`文件到icons下.你可以使用我们的[样例文件](https://github.com/mdn/webextensions-examples/blob/master/borderify/icons/border-48.png),一个google material 设计风格的图标,使用了协议[Creative Commons Attribution-ShareAlike](https://creativecommons.org/licenses/by-sa/3.0/) 

如果你选择使用自己的图标,应用选择48x48像素,你也可以提供96x96像素,添加如下:
    
    "icons": {
      "48": "icons/border-48.png",
      "96": "icons/border-96.png"
    }

可选的,你可以提供SVG矢量图,通过计算的方式指定大小和位置.

  * [关于使用图样的更多说明.](/en-US/Add-ons/WebExtensions/manifest.json/icons)

### borderify.js
最后添加`borderify.js`文件,并写入如下的内容

    document.body.style.border = "5px solid red";

这个文件会被`content_scripts`中的模式匹配到到加载到到相关页面下

  * [深入学习内容脚本](/en-US/Add-ons/WebExtensions/Content_scripts)

## 尝试使用

重新检查一下你的拓展文件

    borderify/
        icons/
            border-48.png
        borderify.js
        manifest.json

### 安装

打开 "about:debugging" 页面, 选中 "调试拓展" 并选中你的文件夹进行加载到浏览器.

这样应用就被安装了,直到你重启了浏览器,否则它会一直存在.

可选的你使用使用命令行进行操作,参考[web-ext](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)

### 测试

现在访问mozilla.org的页面,你会发现页面被包裹了一层红边框:

不要尝试访问addons.mozilla.org,它目前是禁止的.

尝试不同的体验,修改内容脚本,改变边框的颜色,并重新加载拓展

  * [重新加载拓展](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)

## 打包和发布

为了人们可以使用你的拓展,你需要打包和提交给Mozilla进行签名.

  * [发布你的拓展](/en-US/docs/Mozilla/Add-ons/WebExtensions/Publishing_your_WebExtension).

## 接下来

Now you've got an idea of the process of developing a WebExtension for
Firefox, try:

  * [剖析一个应用](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension)
  * [写一个复杂的应用](/en-US/Add-ons/WebExtensions/Your_second_WebExtension)
  * [查阅extensions可用的JavaScripts APIs](/en-US/Add-ons/WebExtensions/API)

