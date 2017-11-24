[

Type| `Array`  
---|---  
Mandatory| No  
Example| 

    
    
    "protocol_handlers": [  {    "protocol": "ircs",    "name": "IRC Mozilla Extension",    "uriTemplate": "https://irccloud.mozilla.com/#!/%s"  }]

  


Use this key to register one or more web-based protocol handlers.



A protocol handler is an application that knows how to handle particular types
of links: for example, a mail client is a protocol handler for "mailto:"
links. When the user clicks a "mailto:" link, the browser opens the
application selected as the handler for the "mailto:" protocol (or offers them
a choice of handlers, depending on their settings).



With this key, you can register a website as a handler for a particular
protocol. The syntax and semantics of this key is very much like the
`[Navigator.registerProtocolHandler()](/en-
US/docs/Web/API/Navigator/registerProtocolHandler)` function, except that with
`registerProtocolHandler()` a website can only register itself as a handler.



Each protocol handler has three properties, all mandatory:



`protocol`

    

A string defining the protocol. This must be either:





  * one of the following: "bitcoin", "geo", "gopher", "im", "irc", "ircs", "magnet", "mailto", "mms", "news", "nntp", "sip", "sms", "smsto", "ssh", "tel", "urn", "webcal", "wtai", "xmpp".


  * a string consisting of a custom name prefixed with "web+" or "ext+". For example: "web+foo" or "ext+foo". The custom name must consist only of lower-case ASCII characters. It's recommended that extensions use the "ext+" form.




`name`

    A string representing the name of the protocol handler. This will be
displayed to the user when they are being asked if they want this handler to
open the link.

`uriTemplate`

    A string representing the URL of the handler. This string must include
"%s" as a placeholder: this will be replaced with the escaped URL of the
document to be handled. This URL might be a true URL, or it could be a phone
number, email address, or so forth. This is a [localizable
property](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Internationalization#Internationalizing_manifest.json).



## Example



    
    
    "protocol_handlers": [\xa0 {\xa0\xa0\xa0 "protocol": "magnet",\xa0\xa0\xa0 "name": "Magnet Extension",\xa0\xa0\xa0 "uriTemplate": "https://example.com/#!/%s"\xa0 }]



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  No|  No| 54| 54|  No  
`gopher`|  No|  No| 56| 56|  No  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  No support No| No support No| Full support
54| No support No| Full support 54  
`gopher`| No support No| No support No| Full support 56|
No support No| Full support 56  
  
]

  *[Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[No support]: No support
  *[ No support]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

