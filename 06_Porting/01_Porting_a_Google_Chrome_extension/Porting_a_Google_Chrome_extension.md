Extensions developed with WebExtension APIs are designed for cross-browser
compatibility: to a large extent, the technology is directly code-compatible
with the [extension API](https://developer.chrome.com/extensions) supported by
Google Chrome and Opera. Extensions written for these browsers will, in most
cases, run in Firefox with just a few changes. Almost all of the [extension
APIs](/en-US/docs/Mozilla/Add-ons/WebExtensions/API) are supported using
callback functions under the `chrome` namespace, the same as Chrome. The only
APIs which are not supported in the `chrome` namespace are those which are
intentionally incompatible with Chrome. In those few cases, the API
documentation page will explicitly state that it's only supported in the
`browser` namespace. The process of porting an extension from Chrome or Opera
is like this:

  1. Review your use of manifest.json features and WebExtension APIs against the [Chrome incompatibilities reference](/en-US/Add-ons/WebExtensions/Chrome_incompatibilities). If you're using features or APIs that are not yet supported in Firefox, you may not be able to port your extension yet. Mozilla provides a service that can help to automate this step: <https://www.extensiontest.com/>.
  2. [Install your extension in Firefox](/en-US/Add-ons/WebExtensions/Temporary_Installation_in_Firefox) and test it out.
  3. If you have any problems, contact us on the [dev-addons mailing list](https://mail.mozilla.org/listinfo/dev-addons) or [#webextensions](irc://irc.mozilla.org/webextensions) on [IRC](https://wiki.mozilla.org/IRC).
  4. [Submit your add-on to AMO for signing and distribution](/en-US/Add-ons/WebExtensions/Publishing_your_WebExtension).

If you were relying on Chrome's command line option for loading an unpacked
extension, check out the [web-ext](/en-US/Add-ons/WebExtensions
/Getting_started_with_web-ext) tool which automates temporary installation in
Firefox for development.

