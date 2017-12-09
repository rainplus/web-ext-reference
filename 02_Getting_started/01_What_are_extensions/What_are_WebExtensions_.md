拓展是使用标准web技术（JavaScript，HTML，CSS）对一个浏览器功能增强的一组代码。除了此之外，拓展可以新强加浏览器特性和修改一些站点的展示。

firefox拓展是使用WebExtensions API，它是一个跨浏览器系统的拓展。在很大的程度上WebEXtensions是兼容Google Chrome和Opera还有 [W3C Draft Community Group](https://browserext.github.io/browserext).已经支持Chrome和Opera的拓展，要兼容到Firefox或[MS Edge](https://developer.microsoft.com/en-us/microsoft-edge/platform/documentation/extensions/)要作稍微的[修改](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Porting_from_Google_Chrome).API同时也是兼容[多进程的firefox](https://developer.mozilla.org/en-US/Firefox/Multiprocess_Firefox)

在过去（截止2017年11月），你可以通过[XUL/XPCOM overlays](/en-US/Add-ons/Overlay_Extensions),[bootstrapped extensions](/en-US/docs/Mozilla/Add-ons/Bootstrapped_extensions), or the [Add-on SDK](/en-US/docs/Mozilla/Add-ons/SDK)开发一个firefox拓展。但现在通过 WebExtensions APIs 开发firefox拓展是唯一方式，其他方式将会弃用。

如果你有想法或问题，或者需要帮助迁移传统的拓展到WebExtensions APIs,你可以参考[拓展邮件列表](https://mail.mozilla.org/listinfo/dev-addons)或者[WebExtensions on [IRC](https://wiki.mozilla.org/IRC)](irc://irc.mozilla.org/webextensions)


## 接下来

  * 尝试样例拓展, 可以查看 [Example extensions](/en-US/Add-ons/WebExtensions/Examples).
  * 学习拓展的架构，可以查看 [Anatomy（剖析） of an extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Anatomy_of_a_WebExtension).
  * 通过开发一个简单的拓展, 可以查看 [Your first extension](/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension).

