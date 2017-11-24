Use the proxy API to register an extended [Proxy Auto-Configuration (PAC) file
](/en-US/Add-ons/WebExtensions/API/proxy#PAC_file_specification), which
implements a policy for proxying web requests. This implementation deviates
from standard PAC design in several ways because the de-facto specification
for PAC files hasn't changed since its initial implementation circa 1995.
There is no standards body maintaining the specification.

Note that Google Chrome provides [an extension API also called
"proxy"](https://developer.chrome.com/extensions/proxy) which is functionally
similar to this API, in that extensions can use it to implement a proxying
policy. However, the design of the Chrome API is completely different to this
API. With Chrome's API an extension can register a PAC file, but can also
define explicit proxying rules. Since this is also possible using the extended
PAC files, this API only supports the PAC file approach. Because this API is
incompatible with the Chrome `proxy` API, this API is only available through
the `browser` namespace.

To use this API you need to have the "proxy"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

## Communicating with PAC files

You can exchange messages between the PAC file and your extension's background
page (or any other privileged pages, like popup pages) using
`[runtime.sendMessage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendMessage)` and `[runtime.onMessage](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`.

To send a message to the PAC file, you must set the `toProxyScript` option:

    
    
    // background.js
    
    // Log any messages from the proxy.
    browser.runtime.onMessage.addListener((message, sender) => {
      if (sender.url === browser.extension.getURL(proxyScriptURL)) {
        console.log(message);
      }
    });
    
    let messageToProxy = {
      enabled: true,
      foo: "A string",
      bar: 1234
    };
    
    browser.runtime.sendMessage(messageToProxy, {toProxyScript: true});
    
    
    // pac.js
    
    browser.runtime.onMessage.addListener((message) => {
      if (message.enabled) {
        browser.runtime.sendMessage("I'm enabled!");
      }
    });

## PAC file specification

The basic PAC file syntax is described in the [PAC documentation](/en-
US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_\(PAC\)_file), but the implementation used by the proxy API
differs from standard PAC design in several ways, which are described in this
section.

### FindProxyForURL() return value

The standard `FindProxyForURL()` [returns a
string](https://developer.mozilla.org/en-
US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_%28PAC%29_file#Return_value_format). In Firefox 55 and 56, the
PAC file used with the proxy API also returns a string. In Firefox 55 _only_ ,
you must pass an argument to the "DIRECT" return value, even though it doesn't
need an argument.

From Firefox 57 onwards, `FindProxyForURL()` may still return a string, but
may alternatively (and preferably) return an array of objects. Each object has
the following properties:

`type`

    String. This must be one of: "http"|"https|"socks4"|"socks"|"direct". "socks" refers to the SOCKS5 protocol.
`host`

    String. Hostname for the proxy to use.
`port`

    String. Port for the proxy.
`username` Optional

    String. Username for the proxy. This is usable with "socks". For HTTP proxy authorizations, use [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.").
`password` Optional

    String. Password for the proxy. This is usable with "socks". For HTTP proxy authorizations, use [`webRequest.onAuthRequired`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server sends a 401 or 407 status code: that is, when the server is asking the client to provide authentication credentials such as a username and password.").
`proxyDNS` Optional

    Boolean. If true, the proxy server is used to resolve certain DNS queries (only usable with "socks4" and "socks"). Defaults to `false`.
`failoverTimeout` Optional

    Integer. Number of seconds before timing out and trying the next proxy in the array. Defaults to 1.

For example:

    
    
    const proxySpecification = [
      {
        type: "socks",
        host: "foo.com",
        port: 1080,
        proxyDNS: true,
        failoverTimeout: 5
      },
      {
        type: "socks",
        host: "bar.com",
        port: 1060,
      }
    ];

The first proxy in the array will be tried first. If it does not respond in
`failoverTimeout` seconds, the next will be tried, until the end of the array
is reached.

### PAC file environment

The global helper functions usually available for PAC files (`[isPlainHostName
()](/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_\(PAC\)_file#isPlainHostName\(\)_2)`, `[dnsDomainIs()](/en-
US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_\(PAC\)_file#dnsDomainIs\(\))`, and so on) are not available.

Code running in the PAC file does not get access to:

  * any DOM functions (for example, [window](/en-US/docs/Web/API/Window) or any of its properties)
  * any WebExtension APIs except `[runtime.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage)` and `[runtime.onMessage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`
  * the [console API](/en-US/docs/Web/API/Console) \- to log messages from a PAC, send a message to the background script:

    
    
    //  pac.js
    
    // send the log message to the background script
    browser.runtime.sendMessage(`Proxy-blocker: blocked ${url}`);
    
    
    // background-script.js
    
    function handleMessage(message, sender) {
      // only handle messages from the proxy script
      if (sender.url != browser.extension.getURL(proxyScriptURL)) {
        return;
      }
      console.log(message);
    }
    
    browser.runtime.onMessage.addListener(handleMessage);

## Functions

[`proxy.register()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/proxy/register "Registers a Proxy Auto-Configuration
\(PAC\) file. The file is executed immediately, and its FindProxyForURL\(\)
function will be called for any HTTP, HTTPS, or FTP requests.")

    Registers the given proxy script.
[`proxy.unregister()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/proxy/unregister "Unregisters a Proxy Auto-Configuration
\(PAC\) file. that was registered by an earlier call to proxy.register\(\).")

    Unregisters the proxy script.

## Events

[`proxy.onProxyError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/proxy/onProxyError "Fired when there is an error
evaluating the PAC file.")

    Fired when the system encounters an error running the proxy script.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`onProxyError`|  No|  No| 55| 55|  No  
`register`|  No|  No|

56

55 *

| 55|  No  
`unregister`|  No|  No| 56| 56|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`onProxyError`|  No support No|  No support No|  Full support 55|  No support
No|  Full support 55  
`register`|  No support No|  No support No|  Full support 56

Full support 56

    
Full support 55

Alternate Name __

     Alternate Name __Uses the non-standard name:`registerProxyScript`
|  No support No|  Full support 55  
`unregister`|  No support No|  No support No|  Full support 56|  No support
No|  Full support 56  
  
## Example extensions

  * [proxy-blocker](https://github.com/mdn/webextensions-examples/tree/master/proxy-blocker)

**Acknowledgements**

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

  *[
 No support

]: No support

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[ Alternate Name __]: Uses the non-standard name: <code>registerProxyScript</code>
  *[Alternate Name __]: Uses the non-standard name: <code>registerProxyScript</code>
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[
Full support

]: Full support

  *[Chrome __]: Chrome

