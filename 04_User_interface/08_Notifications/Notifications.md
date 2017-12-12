通知允许您使用底层操作系统的通知服务来传递有关您的扩展或其内容的信息：

![](https://mdn.mozillademos.org/files/14043/notify-shadowed.png)

通知可以包括对用户的调用，并且您的插件可以监听用户单击通知或通知关闭。

## Specifying notifications

使用[`notifications`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications)以编程方式管理通知使用底层操作系统的通知机制向用户显示通知。 操作系统的通知机制，通知显示和行为的细节可能因操作系统和用户的设置而异。“）API。 要使用此API，您必须在您的manifest.json中请求`notifications`权限：

    "permissions": ["notifications"]

然后使用[`notifications.create`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications/create "Creates and displays a notification.")来创建通知。示例[通知链路-点击-I18N：](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n)

    var title = browser.i18n.getMessage("notificationTitle");
    var content = browser.i18n.getMessage("notificationContent", message.url);
    browser.notifications.create({
      "type": "basic",
      "iconUrl": browser.extension.getURL("icons/link-48.png"),
      "title": title,
      "message": content
    });

此代码创建一个带有图标，标题和消息的通知。

如果通知包含一个号召性用语，则可以监听用户单击该通知以调用该函数来处理该操作：

    browser.notifications.onClicked.addListener(handleClick);

如果您正在通过通知发出呼叫，则还需要定义可选通知“id”，以便您可以确定用户选择了哪个呼叫。

## Examples

在[GitHub](https://github.com/mdn/webextensions-examples)上的仓库，包含几个使用提示功能的例子：

  * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n) 使用创建提示。

