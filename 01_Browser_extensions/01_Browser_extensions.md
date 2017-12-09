
拓展可以拓展和修改一个浏览器的功能。firefox拓展是使用WebExtensions API，它是一个跨浏览器系统的拓展。在很大的程度上WebEXtensions是兼容Google Chrome和Opera还有 [W3C Draft Community Group](https://browserext.github.io/browserext).已经支持Chrome和Opera的拓展，要兼容到Firefox或[MS Edge](https://developer.microsoft.com/en-us/microsoft-edge/platform/documentation/extensions/)要作稍微的[修改](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Porting_from_Google_Chrome).API同时也是兼容[多进程的firefox](https://developer.mozilla.org/en-US/Firefox/Multiprocess_Firefox)

如果你有想法或问题，或者需要帮助迁移传统的拓展到WebExtensions APIs,你可以参考[拓展邮件列表](https://mail.mozilla.org/listinfo/dev-addons)或者[WebExtensions on [IRC](https://wiki.mozilla.org/IRC)](irc://irc.mozilla.org/webextensions)

## 开始入门

  * [什么是拓展?](/en-US/Add-ons/WebExtensions/What_are_WebExtensions)
  * [你的第一个拓展](/en-US/Add-ons/WebExtensions/Your_first_WebExtension)
  * [你的第二个拓展](/en-US/Add-ons/WebExtensions/Your_second_WebExtension)
  * [剖析一个拓展](/en-US/Add-ons/WebExtensions/Anatomy_of_a_WebExtension)
  * [拓展样例](/en-US/Add-ons/WebExtensions/Examples)

## 如何操作

  * [拦截HTTP请求](/en-US/docs/Mozilla/Add-ons/WebExtensions/Intercept_HTTP_requests)
  * [修改页面内容](/en-US/docs/Mozilla/Add-ons/WebExtensions/Modify_a_web_page)
  * [工具栏添加按钮](/en-US/docs/Mozilla/Add-ons/WebExtensions/Add_a_button_to_the_toolbar)
  * [实现配置页面](/en-US/docs/Mozilla/Add-ons/WebExtensions/Implement_a_settings_page)
  * [与剪贴板交互](/en-US/docs/Mozilla/Add-ons/WebExtensions/Interact_with_the_clipboard)

## 用户接口

  * [介绍](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface)
  * [工具栏按钮](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_action)
  * [工具栏弹出按钮]](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)
  * [地址栏按钮](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Page_actions)
  * [地址栏弹出按钮](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)
  * [内容菜单项](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Context_menu_items)
  * [侧边栏](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars)
  * [选项页](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages)
  * [绑定页面](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Bundled_web_pages)
  * [提醒](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Notifications)
  * [地址栏建议](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Omnibox)
  * [开发工具面板](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/devtools_panels)

## 概念

  * [JavaScript API 回顾](/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
  * [内容脚本](/en-US/Add-ons/WebExtensions/Content_scripts)
  * [匹配模式](/en-US/Add-ons/WebExtensions/Match_patterns)
  * [使用文件](/en-US/docs/Mozilla/Add-ons/WebExtensions/Working_with_files)
  * [国际化](/en-US/docs/Mozilla/Add-ons/WebExtensions/Internationalization)
  * [内容安全策略](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy)
  * [本地消息](/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging)
  * [使用开发工具APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/Using_the_devtools_APIs)
  * [用户最佳实践](/en-US/Add-ons/WebExtensions/User_experience_best_practices)

## 移植

  * [迁移chrome拓展](/en-US/Add-ons/WebExtensions/Porting_from_Google_Chrome)
  * [迁移传统的firefox拓展](/en-US/docs/Mozilla/Add-ons/WebExtensions/Porting_a_legacy_Firefox_add-on)
  * [开发firefox安卓拓展](/en-US/docs/Mozilla/Add-ons/WebExtensions/Developing_WebExtensions_for_Firefox_for_Android)
  * [嵌入拓展](/en-US/docs/Mozilla/Add-ons/WebExtensions/Embedded_WebExtensions)
  * [C与Add-on SDK精武比较](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_the_Add-on_SDK)
  * [与 XUL/XPCOM 类型比较](/en-US/docs/Mozilla/Add-ons/WebExtensions/Comparison_with_XUL_XPCOM_extensions)
  * [Chrome的不兼容](/en-US/docs/Mozilla/Add-ons/WebExtensions/Chrome_incompatibilities)
  * [桌面和安卓的不同](/en-US/docs/Mozilla/Add-ons/WebExtensions/Differences_between_desktop_and_Android)

## 火狐工作流

  * [用户体验](/en-US/docs/Mozilla/Add-ons/WebExtensions/User_experience_best_practices)
  * [安装](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox)
  * [调试](/en-US/Add-ons/WebExtensions/Debugging)
  * [web拓展入门](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)
  * [web拓展命令参考](/en-US/docs/Mozilla/Add-ons/WebExtensions/web-ext_command_reference)
  * [拓展和插件的ip](/en-US/docs/Mozilla/Add-ons/WebExtensions/WebExtensions_and_the_Add-on_ID)
  * [修改发布设置](/en-US/Add-ons/WebExtensions/Alternative_distribution_options)
  * [发布你的拓展](/en-US/docs/Mozilla/Add-ons/WebExtensions/Publishing_your_WebExtension)

## 参考 

### JavaScript APIs

  * [JavaScript API overview](/en-US/docs/Mozilla/Add-ons/WebExtensions/API)
  * [Browser compatibility tables for JavaScript APIs](/en-US/Add-ons/WebExtensions/Browser_support_for_JavaScript_APIs)

  * [alarms 闹钟](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/alarms)
  * [bookmarks 书签](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks)
  * [browserAction 浏览器行为](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)
  * [browserSettings 浏览器设置](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings)
  * [browsingData 浏览数据](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browsingData)
  * [clipboard 剪贴板](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/clipboard)
  * [commands 命令](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands)
  * [contextualIdentities 内容识别](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities)
  * [cookies ](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies)
  * [devtools.inspectedWindow 开发工具检视窗口](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.inspectedWindow)
  * [devtools.network 开发工具网络窗口](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.network)
  * [devtools.panels 开发工具面板](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.panels)
  * [downloads 下载](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads)
  * [events 事件](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/events)
  * [extension 拓展](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension)
  * [extensionTypes 拓展类型](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes)
  * [find 查询](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/find)
  * [history 历史](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/history)
  * [i18n 国际化](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n)
  * [identity 标识](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity)
  * [idle 系统空闲](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/idle)
  * [management 管理](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management)
  * [menus 菜单](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus)
  * [notifications 提示](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications)
  * [omnibox 多功能框](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox)
  * [pageAction 页面行为](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)
  * [permissions 权限](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions)
  * [pkcs11](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11)
  * [privacy 隐私](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/privacy)
  * [proxy 代理](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/proxy)
  * [runtime 运行时](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime)
  * [sessions 会话](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions)
  * [sidebarAction 侧边栏行为](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sidebarAction)
  * [storage 储存](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage)
  * [tabs 标签](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)
  * [theme 主题](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme)
  * [topSites](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/topSites)
  * [types 类型](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/types)
  * [webNavigation 导航](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation)
  * [webRequest 请求](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest)
  * [windows 窗口](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows)

### Manifest文件键值含意

  * [manifest.json 回顾](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)
  * [manifest.json 浏览器兼容](/en-US/docs/Mozilla/Add-ons/WebExtensions/Browser_compatibility_for_manifest.json)

  * [applications 应用](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications)
  * [author 作者](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/author)
  * [background 背景](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/background)
  * [browser_action 浏览器行为](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)
  * [chrome_settings_overrides 覆写chrome设置](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/chrome_settings_overrides)
  * [chrome_url_overrides 覆写chrome url](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/chrome_url_overrides)
  * [commands 命令](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands)
  * [content_scripts 内容脚本](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_scripts)
  * [content_security_policy 内容安全策略](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_security_policy)
  * [default_locale 本地默认值](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/default_locale)
  * [description 描述](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/description)
  * [developer 开发都](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/developer)
  * [devtools_page 开发工具主页 ](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/devtools_page)
  * [homepage_url 主页url](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/homepage_url)
  * [icons 图样](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/icons)
  * [incognito](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/incognito)
  * [manifest_version manifest 版本](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/manifest_version)
  * [name 名称](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/name)
  * [omnibox  多功能框 ](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox)
  * [optional_permissions 可选权限](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/optional_permissions)
  * [options_ui 可选ui](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/options_ui)
  * [page_action 页面行为](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)
  * [permissions 权限](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)
  * [protocol_handlers 协议处理吕器](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/protocol_handlers)
  * [short_name 短名称](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/short_name)
  * [sidebar_action 侧边栏行为](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/sidebar_action)
  * [theme 主题](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme)
  * [version 版本](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/version)
  * [web_accessible_resources 可访问资源](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/web_accessible_resources)

