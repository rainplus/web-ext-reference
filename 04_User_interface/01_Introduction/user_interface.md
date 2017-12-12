使用WebExtension API的扩展提供了几个用户界面选项，使其功能可以提供给用户。 一个下面提供了这些选项的摘要，并有更详细的介绍到本节中的每个用户界面选项。

有关使用这些UI组件来建立良好用户体验的建议您的扩展程序，请参阅[用户体验最佳实践](/en-US/docs/Mozilla/Add-ons/WebExtensions/User_experience_best_practices)文章。

UI选项| 说明| 案例
---|---|---  
| 工具栏按钮 [Browser toolbar button](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_action) |浏览器工具栏上的一个按钮，用于在单击事件时将事件分派给扩展。 默认情况下，该按钮在所有选项卡中都可见。 | ![Example of a WebExtension toolbar button](https://mdn.mozillademos.org/files/12966/browser-action.png)  
| 工具栏按钮带弹出层 Browser toolbar button with a [popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) |浏览器工具栏中按钮上的一个弹出按钮，当点击按钮时打开。 弹出窗口是在处理用户交互的HTML文档中定义的。 | ![Example of a WebExtension toolbar button with a popup](https://mdn.mozillademos.org/files/14039/popup-shadow.png)
|地址栏按钮 [Address bar button](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Page_actions) | 浏览器地址栏上的一个按钮，用于在单击时将事件分派给扩展。 默认情况下，该按钮隐藏在所有选项卡中。 | ![Example showing an address bar button \(page action\)](https://mdn.mozillademos.org/files/15047/address_bar_button.png)  
| 地址栏按钮带弹出层 Address bar button with a [popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) | 点击按钮时打开的浏览器地址栏中的按钮弹出。 弹出窗口是在处理用户交互的HTML文档中定义的。 |![Example of a popup on the address bar button](https://mdn.mozillademos.org/files/15053/page_action_popup.png) 
[ 上下文菜单 Context menu items](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Context_menu_items) | 一个或多个浏览器的上下文菜单上的菜单项，复选框和单选按钮。 另外，菜单可以通过添加分隔符来构造。 当菜单项被点击时，一个事件被分派给拓展。 |![](https://mdn.mozillademos.org/files/15051/context_menu_example.png) 
|边栏 [Sidebar](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars) |显示在网页旁边的HTML文档，每个页面都有独特的内容选项。安装扩展程序后打开边栏，然后服从用户侧栏的可见性选择。 边栏内的用户交互由其HTML文档处理。|![Example of a WebExtension's sidebar](https://mdn.mozillademos.org/files/14825/bookmarks-sidebar.png)  
|选项页 [Options page](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) |一个页面，使您可以定义用户可以更改的扩展的首选项。 用户可以从浏览器的加载项管理器访问此页面。 | ![Example showing the options page content added in the favorite colors example.](https://mdn.mozillademos.org/files/15055/options_page.png)  
| 绑定页面 [Bundled web pages](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Bundled_web_pages) |使用您的扩展程序中包含的网页，在窗口或标签页中提供表单，帮助或其他所需的内容。| ![Example of a simple bundled page displayed as a detached panel.](https://mdn.mozillademos.org/files/15063/bundled_page_as_panel_small.png)  
|通知 [Notifications](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Notifications) | 通过底层操作系统的通知机制向用户显示瞬态通知。 当用户单击通知或通知关闭（自动或根据用户请求）时，将事件指派给拓展。 | ![Example notification from a WebExtension](https://mdn.mozillademos.org/files/14043/notify-shadowed.png)  
|地址栏建议 [Address bar suggestions](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Omnibox) | 当用户输入关键字时提供自定义地址栏建议。| ![Example showing the result of the firefox_code_search WebExtension's customization of the address bar suggestions.](https://mdn.mozillademos.org/files/15059/omnibox_example_small.png)  
|开发工具面板 [Developer tools panels](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/devtools_panels) | 浏览器的开发人员工具中显示的关联HTML文档的选项卡。| ![New panel tab in the Developer Tools tab bar](https://mdn.mozillademos.org/files/15049/developer_panel_tab.png)  
  
下面的提供这些用户界面操作指南指导案例：

  * [添加一个工具栏按钮](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Add_a_button_to_the_toolbar)
  * [实现一个首选项](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Implement_a_settings_page)
  * [拓展开发者工具](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Extending_the_developer_tools)

