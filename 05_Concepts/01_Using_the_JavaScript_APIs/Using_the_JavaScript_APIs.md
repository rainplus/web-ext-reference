用于WebExtensions的JavaScript API可以在扩展的[后台脚本 background_scripts](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts) 以及与该扩展捆绑在一起的任何其他文档中使用，包括 [浏览器操作 browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_action)或[页面操作 page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) 弹出窗口，[边栏 sidebar](/en-US/docs/Mozilla/Add-ons/WebExtensions/Sidebars), [首选项页面 options pages](/en-US/docs/Mozilla/Add-ons/WebExtensions/Options_pages)或[ 新标签页面 new tab pages](/en-US/Add-ons/WebExtensions/manifest.json/chrome_url_overrides)。 这些API中的一部分还可以通过扩展的[内容脚本 Content_scripts](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension#Content_scripts)访问请参阅[内容脚本中的列表](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Content_scripts#WebExtension_APIs)


需要使用强大的API你需要在manifest.json中声明[权限](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/permissions)

参过`browser` 对象进行访问API:

    function logTabs(tabs) {
      console.log(tabs);
    }
    
    browser.tabs.query({currentWindow: true}, logTabs);

如果使用的API是一个异步的，将返回[Promise 对象](/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise):

    function logCookie(c) {
      console.log(c);
    }
    
    function logError(e) {
      console.error(e);
    }
    
    var setCookie = browser.cookies.set(
      {url: "https://developer.mozilla.org/"}
    );
    setCookie.then(logCookie, logError);

请注意，这不同于Google Chrome的扩展系统，它使用`chrome`对象而不是`browser`，它使用回调而不是`Promise`而是异步函数。 Mozilla也写了一个polyfill移植工具，让Firefox支持`chrome`和callback能像`browser`和promise一样。 它使得使用`browser`的代码可以在Chrome中保持不变 <https://github.com/mozilla/webextension-polyfill>.

firefox 实现了让chrome的中chrome对象以及callback可以在不进行巨大修改的情况下在firefox中运行

MS Edge 也使用`browser`对象，但还不运行promise的API，仍然使用的是callback程序。

并不是所有的浏览器都支持全部的APs,详情请查看[rowser support for JavaScript APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs).

## 定时器 alarms

安排代码在未来的特定时间运行。 这就像[setTimeout（）](/en-US/docs/Web/API/WindowTimers/setTimeout)和[setInterval（）](/en-US/docs/Web/API/WindowTimers/setInterval)，只是这些函数不适用于按需加载的后台脚本中。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms)

## 书签 bookmarks

The [WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions) [`bookmarks`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks "The documentation about this has not yet been written; please consider contributing!") API lets an extension interact with and manipulate the browser's bookmarking system.You can use it to bookmark pages, retrieve existing bookmarks, and edit,remove, and organize bookmarks.

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks)

## 浏览器操作 browserAction

添加一个工具栏的按钮

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)

## 浏览器设置 browserSettings

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings)

## 浏览数据 browsingData

使用扩展程序可以清除用户正在浏览时累积的数据。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browsingData)

## 剪贴板 clipboard

剪贴板API允许扩展将项目复制到系统剪贴板。目前，API仅支持复制图像，但它会在将来支持复制文本和HTML。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/clipboard)

## 命令 commands

Listen for the user executing commands that you have registered using the [`commands` manifest.json key](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/manifest.json/commands).

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands)

## 上下文标识 contextualIdentities

Work with contextual identities: list, create, remove, and update contextual identities.

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities)

## cookies

与cookies进行交互

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies)

## 开发者工具检视窗口 devtools.inspectedWindow

The `devtools.inspectedWindow` API lets a devtools extension interact with the window that the developer tools are attached to.

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.inspectedWindow)

## 开发者工具网络面板 devtools.network

The `devtools.network` API lets a devtools extension get information about network requests associated with the window that the devtools are attached to (the inspected window).

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.network)

## 开发者工具面板 devtools.panels

The `devtools.panels` API lets a devtools extension define its user interface inside the devtools window.

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.panels)

## 下载 downloads

允许扩展程序与浏览器的下载管理器进行交互。 您可以使用此API模块下载文件，取消，暂停，恢复下载，并在文件管理器中显示下载的文件。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads)

## 事件 events

调度事件的API使用的常见类型。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events)

## 拓展 extension

Utilities related to your extension. Get URLs to resources packages with your extension, get the `[Window](/en-US/docs/Web/API/Window)` object for your extension's pages, get the values for various settings. Note that the messaging APIs in this module are deprecated in favor of the equivalent APIs in the `[runtime](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)` module.

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension)

## 拓展类型 extensionTypes

其他WebExtension API中使用的一些常见类型。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes)

## 查找 find

在当前页面为查找内容，并高亮显示

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/find)

## 历史 history

使用history对象与

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/history)

## 国际化 i18n

将您的扩展程序国际化的功能。 您可以使用这些API从您的扩展打包的语言环境文件中获取本地化的字符串，找出浏览器的当前语言，并找出其值 [Accept-Language header](/en-US/docs/Web/HTTP/Content_negotiation#The_Accept-Language_header).

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)

## 标识 identity

使用身份API获取[OAuth2](https://oauth.net/2/)授权码或访问令牌，然后扩展可以使用该令牌访问来自支持OAuth2访问的服务的用户数据（例如Google 或Facebook帐户）。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity)

## 空闲 idle

找出当前用户系统资源的空闲，锁和运行状态
Find out when the user's system is idle, locked, or active.

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/idle)

## 管理 management

获取有关已安装的拓展信息。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management)

## 菜单 menus

将项目添加到浏览器的菜单系统。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus)

## 提示 notifications

使用底层操作系统的通知机制向用户显示通知。 由于此API使用操作系统的通知机制，因此根据操作系统和用户的设置，通知的显示方式和行为方式可能有所不同。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications)

## 多功能框 omnibox

当用户输入浏览器的地址栏时，允许扩展实现自定义行为。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox)

## 页面操作 pageAction

 [page action](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) 是浏览器地址栏的一个图标

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)

## 权限 permissions

扩展需要访问许多功能更强大的WebExtension API的权限。 他们可以在安装时通过在manifest.json键中包含他们需要的权限[permissions](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)。 在安装时询问权限的主要优点参考[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions)

## pkcs11

pkcs11 API允许扩展枚举[PKCS＃11](https://en.wikipedia.org/wiki/PKCS_11)安全模块，并使浏览器可以将其作为密钥和证书来源访问。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11)

## 隐私 privacy

访问和修改各种隐私相关的浏览器设置。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)

## 代理 proxy

使用代理API来注册一个扩展的[代理自动配置 Proxy Auto-Configuration (PAC) file](/en-US/Add-ons/WebExtensions/API/proxy#PAC_file_specification)，实现代理Web请求的策略。这种实现与标准的PAC设计有若干差异，因为事实上PAC文件规范自1995年初始实施以来并没有改变。没有任何标准维护规范。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/proxy)

## 运行时 runtime

此模块提供有关您的扩展程序及其运行环境的信息。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)

## 会话 sessions

使用会话API列出并恢复在浏览器运行时已关闭的选项卡和窗口。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions)

## 边样操作 sidebarAction

获取并设置扩展的边栏的属性。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction)

## 存储 storage

使扩展程序能够存储和检索数据，并侦听对存储项目的更改。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)

## 标签 tabs

与浏览器的选项卡系统进行交互。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)

## 主题 theme

使浏览器扩展程序能够更新浏览器主题

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme)

## topSites

使用topSites API获取包含浏览器“新标签”页面中列出的所有网站的数组。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/topSites)

## 类型 types

定义用于表示浏览器设置的BrowserSetting类型。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/types)

## 页面导航 webNavigation

为导航的各个阶段添加事件侦听器。导航由浏览器中的一个框架构成，从一个URL转换到另一个URL，通常（但不总是）响应用户的操作，如点击链接或在地址栏中输入URL。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation)

## web请求 webRequest

为发出HTTP请求的各个阶段添加事件侦听器。 事件监听器接收关于请求的详细信息，并且可以修改或取消请求。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest)

## 窗口 windows

与浏览器窗口进行交互。 您可以使用此API获取有关打开的窗口以及打开，修改和关闭窗口的信息。 您还可以侦听窗口打开，关闭和激活事件。

[API 参考文档](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)

