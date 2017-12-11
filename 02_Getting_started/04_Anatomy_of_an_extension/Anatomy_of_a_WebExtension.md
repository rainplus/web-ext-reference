拓展其实本质就是一些文件的集合，用来打包发布后进行安装。这本节中，我们快速解析拓展中的文件。

## manifest.json

这个文件描述并展示一个拓展的全部内部。它包含了元数据，版本，权限，并指向其他文件。

manifest.json会指定如下几种文件类型：

  * [背景页 Background pages](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts): Implement long-running logic.
  * Icons for the extension and any buttons it might define.
  * [边栏，弹出层，选项页 Sidebars, popups, and options pages](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Sidebars_popups_options_pages): HTML documents that provide content for various user interface components.
  * [内容脚本 Content scripts](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Content_scripts): JavaScript included with your extension, that you will inject into web pages.

![](https://mdn.mozillademos.org/files/13669/webextension-anatomy.png)

[点击查询manifest.json更多详情](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)

除了上面的页面，拓展还可以包含 [Extension pages](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Extension_pages)
files.

## 背景脚本 Background scripts

扩展往往需要长期维持的状态 或长期执行操作独立于任何特定的网页浏览器或临时窗口。那背景脚本是什么。

背景脚本（background script）会在拓展被加载的时候加载，直到拓展被卸载或禁用，在背景脚本中，你可以使用任意的[WebExtension APIs](/en-US/Add-ons/WebExtensions/API)，只要你配置了相应的[权限 permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)

### Specifying background scripts

你可以在manifest.json中指定背景脚本的使用：

    "manifest.json":
    // manifest.json
    "background": {
      "scripts": ["background-script.js"]
    }

你可以指定多个背景脚本，它们就像一个web页面加载多个脚本一样。

### Background script environment

#### DOM APIs

背景脚本所运行在的页面就是背景页，拥有一个[window](/en-US/docs/Web/API/Window)全局变量，提供了标准的DOM APIs的对象。

背景页只是一种可选的选择，你的拓展只包含背景脚本的时候，拓展会自己包含一个空白的背景页面

当然你可以特殊地指定一个背景页：

    // manifest.json
    
    "background": {
      "page": "background-page.html"
    }

#### WebExtension APIs

在背景脚本中，你可以使用任意的[WebExtension APIs](/en-US/Add-ons/WebExtensions/API)，只要你配置了相应的[权限 permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions).

#### Cross-origin access

背景脚本拥有跨域权限，通过配置[host permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)进行设置.

#### Web content

背景脚本并不直接访问web页面。它们的作用只是进行加载[内容脚本]((/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts))并通过[消息机制](/en-US/Add-ons/WebExtensions/Content_scripts#Communicating_with_background_scripts)与内容脚本进行交互。

#### 内容安全策略 Content security policy

背景脚本的执行权限太大，会存在一个安全隐患。就像`eval()`操作，更多详情请查阅[Content Security Policy](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy)

## 边栏，弹出层，选项页 Sidebars, popups, options pages

你的拓展可以包含如下几个与用户交互的组件：

  * [边栏 sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars) 是网页内容中左边的面板
  * [弹出层 popup](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) 是点击 [工具栏按钮](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_action) 或 [地址栏按钮](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Page_actions)弹出的面板
  * [选项页面 options page](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) 是显示拓展配置的页面

上面的每种组件，你可以在manifest.json指定一个html页面（可以包含css和js）进行使用。

还有另外的一种页面 [Extension pages](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Extension_pages),它也拥有拓展的全部权限，并可以通过 [`runtime.getBackgroundPage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/getBackgroundPage "Retrieves the Window object
for the background page running inside the current extension.") 返回拓展的window对象.

## Extension pages

您还可以在扩展中包含HTML文档，这些文档未附加到预定义的用户界面组件中。与文件不同，您可能
提供工具条，弹出窗口，或选择的页面，这些没有在manifest.json文件条目。然而，他们也可以获得所有相同的特权。
webextension API作为你的背景脚本。

你通常会加载一个页面使用[ `window.create() ` ](/en-US/docs/Mozilla/Add-ons/WebExtensionsAPI/window/create "创建一个新的窗口。")或[ `tab.create()` ](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/create "Creates a new tab.")
查阅 [Extension pages](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Extension_pages) 获取更多详情.

## Content scripts

内容脚本是作为加载页面的一部分,内容脚本是访问并操作网页页面的主体.

内容脚本的网页中运行,不同于页面自己加载的脚本,内容脚本也使用<script>进行加载,


内容脚本像正常的脚本一样可以操作页面的DOM树的内容

区别于页面正常的脚本,它还可以:

  * 跨域请求.
  * 使用部分[WebExtension APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/API).
  * 通过WebExtension APIs与背景脚本交互消息.

内容脚本不能直接访问正常页面,但可以通过[window.postMessage()](/en-US/docs/Web/API/Window/postMessage) API使用消息机制进行交互.

我们谈论的内容脚本无非就是js,所能我们可以注入css

查阅[内容脚本](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts) 获取更多详情.

## Web accessible resources

我们拓展中的页面,可以包含HTML,CSS,js还有图片,引用资源的方式也是正常的URI模式.

例如,一个内容脚本想要在页面中插入一张图片,可以在内容脚本中创建并添加[img](/en-US/docs/Web/HTML/Element/img)元素并通过引src引用图片的URI.

查阅[web_accessible_resources](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/web_accessible_resources)获取更多详情





