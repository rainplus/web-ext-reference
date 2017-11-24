[

Type| `String`  
---|---  
Mandatory| No  
Example| 

    
    
    "content_security_policy": "default-src 'self'"

  


Extensions have a content security policy applied to them by default. The
default policy restricts the sources from which they can load[<script>](/en-
US/docs/Web/HTML/Element/script) and [<object>](/en-
US/docs/Web/HTML/Element/object) resources, and disallows potentially unsafe
practices such as the use of `[eval()](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/eval)`. See [Default content
security policy](/en-US/Add-
ons/WebExtensions/Content_Security_Policy#Default_content_security_policy) to
learn more about the implications of this.



You can use the `"content_security_policy"` manifest key to loosen or tighten
the default policy. This key is specified in just the same way as the Content-
Security-Policy HTTP header. See [Using Content Security Policy](/en-
US/docs/Web/HTTP/CSP) for a general description of CSP syntax.



For example, you can use this key to:





  * Allow the extension to load scripts and objects from outside its package, by supplying their URL in the [`script-src`](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src "The HTTP Content-Security-Policy \(CSP\) script-src directive specifies valid sources for sources for JavaScript. This includes not only URLs loaded directly into <script> elements, but also things like inline script event handlers \(onclick\) and XSLT stylesheets which can trigger script execution.") or [`object-src`](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/object-src "The HTTP Content-Security-Policy object-src directive specifies valid sources for the <object>, <embed>, and <applet> elements.") directives.


  * Allow the extension to execute inline scripts, by [supplying the hash of the script in the `"script-src"` directive](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src#Unsafe_inline_script).


  * Allow the extension to use `eval()` and similar features, by including\xa0`'unsafe-eval'` in the\xa0[`script-src`](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src "The HTTP Content-Security-Policy \(CSP\) script-src directive specifies valid sources for sources for JavaScript. This includes not only URLs loaded directly into <script> elements, but also things like inline script event handlers \(onclick\) and XSLT stylesheets which can trigger script execution.") directive.


  * Restrict permitted sources for other types of content, such as images and stylesheets, using the appropriate [policy directive](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy).




There are restrictions on the policy you can specify here:





  * The policy must include at least the\xa0[`script-src`](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src "The HTTP Content-Security-Policy \(CSP\) script-src directive specifies valid sources for sources for JavaScript. This includes not only URLs loaded directly into <script> elements, but also things like inline script event handlers \(onclick\) and XSLT stylesheets which can trigger script execution.") and the\xa0[`object-src`](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/object-src "The HTTP Content-Security-Policy object-src directive specifies valid sources for the <object>, <embed>, and <applet> elements.") directives, and the\xa0[`script-src`](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src "The HTTP Content-Security-Policy \(CSP\) script-src directive specifies valid sources for sources for JavaScript. This includes not only URLs loaded directly into <script> elements, but also things like inline script event handlers \(onclick\) and XSLT stylesheets which can trigger script execution.") directive must contain the keyword `'self'`.


  * Remote sources must use `https:` schemes.


  * Remote sources must not use wildcards for any domains in the [public suffix list](https://publicsuffix.org/list/) (so "*.co.uk" and "*.blogspot.com" are not allowed, although "*.foo.blogspot.com" is allowed).


  * All sources must specify a host.


  * The only permitted schemes for sources are: `blob:`, `filesystem:`, `moz-extension:`, and `https:`.


  * The only permitted [keywords](/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/default-src#Sources) are: `'none'`, `'self'`, and `'unsafe-eval'`.




## Example



### Valid examples



Allow remote scripts from "https://example.com": ( _see note_ 1 )



    
    
    "content_security_policy": "script-src 'self' https://example.com; object-src 'self'"



Allow remote scripts from any subdomain of "jquery.com":



    
    
    "content_security_policy": "script-src 'self' https://*.jquery.com; object-src 'self'"



Allow [`eval()` and friends](/en-US/Add-
ons/WebExtensions/Content_Security_Policy#eval%28%29_and_friends):



    
    
    "content_security_policy": "script-src 'self' 'unsafe-eval'; object-src 'self';"



Allow the inline script: `"<script>alert('Hello, world.');</script>"`:



    
    
    "content_security_policy": "script-src 'self' 'sha256-qznLcsROx4GACP2dm0UCKCzCG+HiZ1guq6ZZDob/Tng='; object-src 'self'"



Keep the rest of the policy, but also require that images should be packaged
with the extension:



    
    
    "content_security_policy": "script-src 'self'; object-src 'self'; img-src 'self'"



Require that all types of content should be packaged with the extension:



    
    
    "content_security_policy": "default-src 'self'"



### Invalid examples



Policy that omits the `"object-src"` directive:



    
    
    "content_security_policy": "script-src 'self' https://*.jquery.com;"



Policy that omits the `"self"` keyword in the `"script-src"` directive:



    
    
    "content_security_policy": "script-src https://*.jquery.com; object-src 'self'"



Scheme for a remote source is not `https`:



    
    
    "content_security_policy": "script-src 'self' http://code.jquery.com; object-src 'self'"



Wildcard is used with a generic domain:



    
    
    "content_security_policy": "script-src 'self' https://*.blogspot.com; object-src 'self'"



Source specifies a scheme but no host:



    
    
    "content_security_policy": "script-src 'self' https:; object-src 'self'"



Directive includes the unsupported keyword `'unsafe-inline'`:



    
    
    "content_security_policy": "script-src 'self' 'unsafe-inline'; object-src 'self'"



1\. _Note: Valid examples display the correct use of keys in CSP. However,
extensions with 'unsafe-eval', 'unsafe-inline', remote script, or remote
sources in their CSP are not allowed for extensions listed on
addons.mozilla.org due to major security issues._



\xa0



## \xa0



## Browser compatibility



The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.



| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes|  Yes1| 482| 482|  Yes  
  
1\. Only the default content security policy is supported: "script-src 'self';
object-src 'self';".

2\. Firefox does not support 'http://127.0.0.1' or 'http://localhost' as
script sources: they must be served over HTTPS.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes| Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Only the default content security policy is supported: "script-src 'self'; object-src 'self';".
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Firefox does not support 'http://127.0.0.1' or 'http://localhost' as script sources: they must be served over HTTPS.
|  Full support Yes| Full support 48

Notes __

Full support 48

Notes __

     Notes __Firefox does not support 'http://127.0.0.1' or 'http://localhost' as script sources: they must be served over HTTPS.  
  
]

  *[Full support]: Full support
  *[ Full support]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

