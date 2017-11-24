[\n

\n\n\n\nType\n| `Array`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"protocol_handlers": [\n  {\n    "protocol": "ircs",\n    "name": "IRC Mozilla Extension",\n    "uriTemplate": "https://irccloud.mozilla.com/#!/%s"\n  }\n]

\n\n  
\n\n\n

Use this key to register one or more web-based protocol handlers.

\n

A protocol handler is an application that knows how to handle particular types
of links: for example, a mail client is a protocol handler for "mailto:"
links. When the user clicks a "mailto:" link, the browser opens the
application selected as the handler for the "mailto:" protocol (or offers them
a choice of handlers, depending on their settings).

\n

With this key, you can register a website as a handler for a particular
protocol. The syntax and semantics of this key is very much like the
`[Navigator.registerProtocolHandler()](/en-
US/docs/Web/API/Navigator/registerProtocolHandler)` function, except that with
`registerProtocolHandler()` a website can only register itself as a handler.

\n

Each protocol handler has three properties, all mandatory:

\n

\n`protocol`

\n    \n

A string defining the protocol. This must be either:

\n

\n

  * one of the following: "bitcoin", "geo", "gopher", "im", "irc", "ircs", "magnet", "mailto", "mms", "news", "nntp", "sip", "sms", "smsto", "ssh", "tel", "urn", "webcal", "wtai", "xmpp".
\n

  * a string consisting of a custom name prefixed with "web+" or "ext+". For example: "web+foo" or "ext+foo". The custom name must consist only of lower-case ASCII characters. It's recommended that extensions use the "ext+" form.
\n

\n

\n`name`

\n    A string representing the name of the protocol handler. This will be
displayed to the user when they are being asked if they want this handler to
open the link.

\n`uriTemplate`

\n    A string representing the URL of the handler. This string must include
"%s" as a placeholder: this will be replaced with the escaped URL of the
document to be handled. This URL might be a true URL, or it could be a phone
number, email address, or so forth. This is a [localizable
property](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).

\n\n

## Example

\n

    
    
    "protocol_handlers": [\n\xa0 {\n\xa0\xa0\xa0 "protocol": "magnet",\n\xa0\xa0\xa0 "name": "Magnet Extension",\n\xa0\xa0\xa0 "uriTemplate": "https://example.com/#!/%s"\n\xa0 }\n]

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n No| \n No| 54| 54| \n No  
`gopher`| \n No| \n No| 56| 56| \n No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n
54| \nNo support\n\n No| \nFull support\n\n 54  
`gopher`| \nNo support\n\n No| \nNo support\n\n No| \nFull support\n\n 56|
\nNo support\n\n No| \nFull support\n\n 56  
  
\n]

  *[\nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[ \nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

