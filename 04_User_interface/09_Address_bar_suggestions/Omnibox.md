使用[`omnibox`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox)当用户输入浏览器的地址栏时，允许扩展实现自定义行为。 当用户输入关键字时，浏览器地址栏下拉菜单中提供的建议。

![Example showing the result of the firefox_code_search WebExtension's customization of the address bar suggestions.](https://mdn.mozillademos.org/files/15075/omnibox_example_full.png)

这使得您的扩展能够搜索免费电子书库，或者像上面的例子那样搜索代码示例的存储库。

## 指定多功能框的自定义

你告诉你的扩展名，它将自定义地址栏的建议，包括[omnibox](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/omnibox)键和在其[manifest.json](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)文件中定义触发的关键字：

      "omnibox": { "keyword" : "cs" }

在扩展的后台JavaScript文件中，使用[`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion)关于此的文档尚未编写;请 考虑贡献！“），您可以选择定义要在地址栏下拉菜单中显示的第一个建议。 使用这个提示如何使用该功能：

    browser.omnibox.setDefaultSuggestion({
      description: `Search the firefox codebase
        (e.g. "hello world" | "path:omnibox.js onInputChanged")`
    });

然后，您可以通过侦听[`omnibox.onInputStarted`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputStarted "The documentation about this has not yet been written; please consider contributing!")当用户更改输入时，通过在地址栏中输入关键字，然后按空格键开始与您的扩展进行交互之后触发。每当用户更新地址栏条目时调度。 然后，您可以填充这些建议，在这种情况下，使用该术语构建 https://searchfox.org/mozilla-central 的搜索

    browser.omnibox.onInputChanged.addListener((text, addSuggestions) => {
      let headers = new Headers({"Accept": "application/json"});
      let init = {method: 'GET', headers};
      let url = buildSearchURL(text);
      let request = new Request(url, init);
    
      fetch(request)
        .then(createSuggestionsFromResponse)
        .then(addSuggestions);
    });

如果扩展名使用[`omnibox.setDefaultSuggestion()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/setDefaultSuggestion "The documentation about this has not yet been written; please consider contributing!")，那么这将首先出现在下拉列表中。

然后，扩展程序可以使用[`omnibox.onInputEntered`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/omnibox/onInputEntered "Fired when the user has selected one of the suggestions your extension has added to the address bar's drop-down list.")来监听用户单击其中一个建议。 您的扩展程序已添加到地址栏的下拉列表中的一个建议“）。 如果单击默认建议，则返回用户的自定义术语，否则返回建议的字符串。 而且，关于处理新链接的用户浏览器偏好的信息被传递。 在下面的代码中，用户的自定义术语用于创建搜索，否则将打开建议的URL：


    
    browser.omnibox.onInputEntered.addListener((text, disposition) => {
      let url = text;
      if (!text.startsWith(SOURCE_URL)) {
        // Update the url if the user clicks on the default suggestion.
        url = `${SEARCH_URL}?q=${text}`;
      }
      switch (disposition) {
        case "currentTab":
          browser.tabs.update({url});
          break;
        case "newForegroundTab":
          browser.tabs.create({url});
          break;
        case "newBackgroundTab":
          browser.tabs.create({url, active: false});
          break;
      }
    });



## 示例
在[GitHub](https://github.com/mdn/webextensions-examples)上的仓库，包含几个使用多功能框的例子：

  * [firefox-code-search](https://github.com/mdn/webextensions-examples/tree/master/firefox-code-search) 自定义多功能框

