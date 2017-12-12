此功能自Firefox 54起可用。

当扩展提供对开发人员有用的工具时，可以为浏览器的开发人员工具添加一个UI作为新的面板。

![Simple example showing the addition of "My panel" to the Developer Tools tabs.](https://mdn.mozillademos.org/files/15035/devtools_panel_example.png)

## 指定一个开发人员工具面板

开发人员工具面板是使用[devtools.panels][devtools.panels](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.panels) 添加的，而这又需要 从一个特殊的devtools页面运行。

通过在扩展的[manifest.json]中包含[devtools_page](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/devtools_page)键来添加devtools页面。并在拓展中提供页面HTML文件的位置：

    "devtools_page": "devtools-page.html"

在devtools页面中，调用将添加devtools面板的脚本：

    <body>
      <script src="devtools.js"></script>
    </body>

在脚本中，通过指定提供面板内容的面板标题，图标和HTML文件来创建devtools面板：

    function handleShown() {
      console.log("panel is being shown");
    }
    
    function handleHidden() {
      console.log("panel is being hidden");
    }
    
    browser.devtools.panels.create(
      "My Panel",           // title
      "icons/star.png",           // icon
      "devtools/panel/panel.html"          // content
    ).then((newPanel) => {
      newPanel.onShown.addListener(handleShown);
      newPanel.onHidden.addListener(handleHidden);
    });

该扩展现在可以使用[`devtools`.inspectedWindow.eval()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/devtools.inspectedWindow/eval)在检查窗口中运行代码 通过传递消息通过后台脚本注入脚本脚本。 您可以在[扩展开发人员工具](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Extending_the_developer_tools)中找到更多详细信息


## 示例

在[GitHub](https://github.com/mdn/webextensions-examples)上的仓库，包含几个使用开发工具面板的例子：

  * [devtools-panels](https://github.com/mdn/webextensions-examples/blob/master/devtools-panels/)

