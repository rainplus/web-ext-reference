[\n

\n

Use the proxy API to register an extended [Proxy Auto-Configuration (PAC) file
](/en-US/Add-ons/WebExtensions/API/proxy#PAC_file_specification), which
implements a policy for proxying web requests. This implementation deviates
from standard PAC design in several ways because the de-facto specification
for PAC files hasn't changed since its initial implementation circa 1995.
There is no standards body maintaining the specification.

\n

Note that Google Chrome provides [an extension API also called
"proxy"](https://developer.chrome.com/extensions/proxy) which is functionally
similar to this API, in that extensions can use it to implement a proxying
policy. However, the design of the Chrome API is completely different to this
API. With Chrome's API an extension can register a PAC file, but can also
define explicit proxying rules. Since this is also possible using the extended
PAC files, this API only supports the PAC file approach. Because this API is
incompatible with the Chrome `proxy` API, this API is only available through
the `browser` namespace.

\n

To use this API you need to have the "proxy"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions).

\n

## Communicating with PAC files

\n

You can exchange messages between the PAC file and your extension's background
page (or any other privileged pages, like popup pages) using
`[runtime.sendMessage()](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/sendMessage)` and `[runtime.onMessage](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`.

\n

To send a message to the PAC file, you must set the `toProxyScript` option:

\n

    
    
    // background.js\n\n// Log any messages from the proxy.\nbrowser.runtime.onMessage.addListener((message, sender) => {\n\xa0 if (sender.url === browser.extension.getURL(proxyScriptURL)) {\n\xa0\xa0\xa0 console.log(message);\n\xa0 }\n});\n\nlet messageToProxy = {\n  enabled: true,\n  foo: "A string",\n  bar: 1234\n};\n\nbrowser.runtime.sendMessage(messageToProxy, {toProxyScript: true});

\n

    
    
    // pac.js\n\nbrowser.runtime.onMessage.addListener((message) => {\n  if (message.enabled) {\n    browser.runtime.sendMessage("I'm enabled!");\n  }\n});

\n

## PAC file specification

\n

The basic PAC file syntax is described in the [PAC documentation](/en-
US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_\(PAC\)_file), but the implementation used by the proxy API
differs from standard PAC design in several ways, which are described in this
section.

\n

### FindProxyForURL() return value

\n

The standard `FindProxyForURL()` [returns a
string](https://developer.mozilla.org/en-
US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_%28PAC%29_file#Return_value_format). In Firefox 55 and 56, the
PAC file used with the proxy API also returns a string. In Firefox 55 _only_ ,
you must pass an argument to the "DIRECT" return value, even though it doesn't
need an argument.

\n

From Firefox 57 onwards,\xa0`FindProxyForURL()` may still return a string, but
may alternatively (and preferably) return an array of objects. Each object has
the following properties:

\n

\n`type`

\n    String. This must be one of: "http"|"https|"socks4"|"socks"|"direct".
"socks" refers to the SOCKS5 protocol.

\n`host`

\n    String. Hostname for the proxy to use.

\n`port`

\n    String. Port for the proxy.

\n`username` Optional

\n    String. Username for the proxy. This is usable with "socks". For HTTP
proxy authorizations, use [`webRequest.onAuthRequired`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server
sends a 401 or 407 status code: that is, when the server is asking the client
to provide authentication credentials such as a username and password.").

\n`password` Optional

\n    String. Password for the proxy. This is usable with "socks". For HTTP
proxy authorizations, use [`webRequest.onAuthRequired`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/webRequest/onAuthRequired "Fired when the server
sends a 401 or 407 status code: that is, when the server is asking the client
to provide authentication credentials such as a username and password.").

\n`proxyDNS` Optional

\n    Boolean. If true, the proxy server is used to resolve certain DNS
queries (only usable with "socks4" and "socks"). Defaults to `false`.

\n`failoverTimeout` Optional

\n    Integer. Number of seconds before timing out and trying the next proxy
in the array. Defaults to 1.

\n\n

For example:

\n

    
    
    const proxySpecification = [\n  {\n    type: "socks",\n    host: "foo.com",\n    port: 1080,\n    proxyDNS: true,\n    failoverTimeout: 5\n  },\n  {\n    type: "socks",\n    host: "bar.com",\n    port: 1060,\n  }\n];

\n

The first proxy in the array will be tried first. If it does not respond in
`failoverTimeout` seconds, the next will be tried, until the end of the array
is reached.

\n

### PAC file environment

\n

The global helper functions usually available for PAC files (`[isPlainHostName
()](/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_\(PAC\)_file#isPlainHostName\(\)_2)`, `[dnsDomainIs()](/en-
US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-
Configuration_\(PAC\)_file#dnsDomainIs\(\))`, and so on) are not available.

\n

Code running in the PAC file does not get access to:

\n

\n

  * any DOM functions (for example, [window](/en-US/docs/Web/API/Window) or any of its properties)
\n

  * any WebExtension APIs except `[runtime.sendMessage()](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage)` and `[runtime.onMessage](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage)`
\n

  * the [console API](/en-US/docs/Web/API/Console) \- to log messages from a PAC, send a message to the background script:
\n

\n

    
    
    //  pac.js\n\n// send the log message to the background script\nbrowser.runtime.sendMessage(`Proxy-blocker: blocked ${url}`);

\n

    
    
    // background-script.js\n\nfunction handleMessage(message, sender) {\n  // only handle messages from the proxy script\n  if (sender.url != browser.extension.getURL(proxyScriptURL)) {\n    return;\n  }\n  console.log(message);\n}\n\nbrowser.runtime.onMessage.addListener(handleMessage);

\n

## Functions

\n

\n[`proxy.register()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/proxy/register "Registers a Proxy Auto-Configuration
\(PAC\) file. The file is executed immediately, and its FindProxyForURL\(\)
function will be called for any HTTP, HTTPS, or FTP requests.")

\n    Registers the given proxy script.

\n[`proxy.unregister()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/proxy/unregister "Unregisters a Proxy Auto-Configuration
\(PAC\) file. that was registered by an earlier call to proxy.register\(\).")

\n    Unregisters the\xa0proxy script.

\n\n

## Events

\n

\n[`proxy.onProxyError`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/proxy/onProxyError "Fired when there is an error
evaluating the PAC file.")

\n    Fired when the system encounters an error running the proxy script.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`onProxyError`| \n No| \n No| 55| 55| \n No  
`register`| \n No| \n No|

56

55 *

| 55| \n No  
`unregister`| \n No| \n No| 56| 56| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`onProxyError`|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
55| \nNo support\n\n No| \nFull support\n\n 55  
`register`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 56

\nFull support\n\n 56

    
\nFull support\n\n 55

Alternate Name __

     Alternate Name __Uses the non-standard name:`registerProxyScript`
|  \nNo support\n\n No| \nFull support\n\n 55  
`unregister`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 56|
\nNo support\n\n No| \nFull support\n\n 56  
  
\n

## Example extensions

  * [proxy-blocker](https://github.com/mdn/webextensions-examples/tree/master/proxy-blocker)

\n

 **Acknowledgements** \n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

\n

\n]

  *[\nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[ Alternate Name __]: Uses the non-standard name: <code>registerProxyScript</code>
  *[Alternate Name __]: Uses the non-standard name: <code>registerProxyScript</code>
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

