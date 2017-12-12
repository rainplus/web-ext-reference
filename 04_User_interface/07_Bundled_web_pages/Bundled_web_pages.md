您可以在您的扩展程序中包含html页面，以提供表单，帮助或扩展程序所需的任何其他内容。

![Example of a simple bundled page displayed as a detached panel.](https://mdn.mozillademos.org/files/15073/bundled_page_as_panel.png)

这些页面还可以访问可用于您的扩展的后台脚本的特权JavaScript API。

## 指定拓展页面

您可以在扩展中包含HTML文件及其关联的CSS或JavaScript文件。 这些文件可以包含在根目录中，或者组织在有意义的子文件夹中。

    /my-extension
        /manifest.json
        /my-page.html
        /my-page.js

## 展示拓展页面

有两种显示扩展页面的选项：

* [`windows.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/create "Creates a new window.")  
* [`tabs.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/create "Creates a new tab.")


例如，使用windows.create（），你可以打开一个HTML页面到一个分离的面板（一个没有地址栏，书签栏等的普通浏览器UI的窗口）来创建类似对话的用户体验：

    var createData = {
      type: "detached_panel",
      url: "panel.html",
      width: 250,
      height: 100
    };
    var creating = browser.windows.create(createData);

当窗口不再需要的时候，可以通过编程来关闭窗口，例如，在用户点击一个按钮之后，把当前窗口的ID传给[`windows.remove()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/windows/remove)在给定窗口ID的情况下关闭窗口和所有标签。

    document.getElementById("closeme").addEventListener("click", function(){
      var winId = browser.windows.WINDOW_ID_CURRENT;
      var removing = browser.windows.remove(winId);
    }); 

## Extension pages and history

默认情况下，以这种方式打开的页面将存储在用户的历史记录中，就像正常的网页一样。 如果您不希望出现这种情况，请使用[`history.deleteUrl()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/history/deleteUrl) 从浏览器历史记录中删除“）来删除浏览器的记录：
  
    const url = browser.extension.getURL("my-page.html");
    
    browser.tabs.create({url: url}).then(() => {
      // We don't want to sync this URL ever nor clutter the users history
      browser.history.deleteUrl({url: url});
    }).catch((e) => { throw e });

要使用历史记录API，您必须在您的“历史记录”中请求“历史”[权限 permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions)在文件中[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)


## 示例

在[GitHub](https://github.com/mdn/webextensions-examples)上的仓库，包含几个使用绑定页面的例子：

* [window-manipulator](https://github.com/mdn/webextensions-examples/tree/master/window-manipulator)

