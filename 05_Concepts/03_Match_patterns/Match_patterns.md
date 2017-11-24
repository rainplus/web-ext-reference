[\n

\n

Match patterns are a way to specify groups of URLs: a match pattern matches a
specific set of URLs. They are for extensions using WebExtensions APIs in a
few places, most notably to specify which documents to load [content scripts
](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts) into, and to
specify which URLs to add `[webRequest](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest)` listeners to.

\n

APIs that use match patterns usually accept a list of match patterns, and will
perform the appropriate action if the URL matches any of the patterns. See,
for example, the `[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)` key in manifest.json.

\n

## Match pattern structure

\n

All match patterns are specified as strings. Apart from the special
["<all_urls>"](/en-US/Add-ons/WebExtensions/Match_patterns#%3Call_urls%3E)
pattern, match patterns consist of three parts: _scheme_ , _host_ , and
_path_. The scheme and host are separated by "://".

\n

    
    
    <scheme>://<host><path>

\n

### scheme

\n

The _scheme_ component may take one of two forms:

\n\n\n\nForm\n| Matches\n  
---|---  
\n\n\n\n"*"\n| Only "http" and "https".\n  
\n\nOne of "http", "https", "file", "ftp", "app".\n| Only the given scheme.\n  
\n\n\n

### host

\n

The _host_ component may take one of three forms:

\n\n\n\nForm\n| Matches\n  
---|---  
\n\n\n\n"*"\n| Any host.\n  
\n\n"*." followed by part of the hostname.\n| The given host and any of its
subdomains.\n  
\n\nA complete hostname, without wildcards.\n| Only the given host.\n  
\n\n\n

 _host_ is optional only if the _scheme_ is "file".

\n

Note that the wildcard may only appear at the start.

\n

### path

\n

The path component must begin with a "/".

\n

After that, it may subsequently contain any combination of the "*" wildcard
and any of the characters that are allowed in URL paths. Unlike _host_ , the
_path_ component may contain the "*" wildcard in the middle or at the end, and
the "*" wildcard may appear more than once.

\n

### <all_urls>

\n

The special value "<all_urls>" matches all URLs under any of the supported
schemes: that is, "http", "https", "file", "ftp", "app".

\n

## Examples

\n\n\n\nPattern\n| Example matches\n| Example non-matches\n  
---|---|---  
\n\n\n\n\n

`<all_urls>`

\n

Match all URLs.

\n\n| \n

`http://example.org/`

\n

`ftp://files.somewhere.org/`

\n

`https://a.org/some/path/`

\n\n| \n

`resource://a/b/c/`  
\n (unsupported scheme)

\n\n  
\n\n\n

`*://*.mozilla.org/*`

\n

Match all HTTP and HTTPS URLs that are hosted at "mozilla.org" or one of its
subdomains.

\n\n| \n

`http://mozilla.org/`

\n

`https://mozilla.org/`

\n

`http://a.mozilla.org/`

\n

`http://a.b.mozilla.org/`

\n

`https://b.mozilla.org/path/`

\n\n| \n

`ftp://mozilla.org/`  
\n (unmatched scheme)

\n

`http://mozilla.com/`  
\n (unmatched host)

\n

`http://firefox.org/`  
\n (unmatched host)

\n\n  
\n\n\n

`*://mozilla.org/`

\n

Match all HTTP and HTTPS URLs that are hosted at exactly "mozilla.org/".

\n\n| \n

`http://mozilla.org/`

\n

`https://mozilla.org/`

\n\n| \n

`ftp://mozilla.org/`  
\n (unmatched scheme)

\n

`http://a.mozilla.org/`  
\n (unmatched host)

\n

`http://mozilla.org/a`  
\n (unmatched path)

\n\n  
\n\n\n

`ftp://mozilla.org/`

\n

Match only "ftp://mozilla.org/".

\n\n| `ftp://mozilla.org`\n| \n

`http://mozilla.org/`  
\n (unmatched scheme)

\n

`ftp://sub.mozilla.org/`  
\n (unmatched host)

\n

`ftp://mozilla.org/path`  
\n (unmatched path)

\n\n  
\n\n\n

`https://*/path`

\n

Match HTTPS URLs on any host, whose path is "path".

\n\n| \n

`https://mozilla.org/path`

\n

`https://a.mozilla.org/path`

\n

`https://something.com/path`

\n\n| \n

`http://mozilla.org/path`  
\n (unmatched scheme)

\n

`https://mozilla.org/path/`  
\n (unmatched path)

\n

`https://mozilla.org/a`  
\n (unmatched path)

\n

`https://mozilla.org/`  
\n (unmatched path)

\n\n  
\n\n\n

`https://*/path/`

\n

Match HTTPS URLs on any host, whose path is "path/".

\n\n| \n

`https://mozilla.org/path/`

\n

`https://a.mozilla.org/path/`

\n

`https://something.com/path`/

\n\n| \n

`http://mozilla.org/path/`  
\n (unmatched scheme)

\n

`https://mozilla.org/path`  
\n (unmatched path)

\n

`https://mozilla.org/a`  
\n (unmatched path)

\n

`https://mozilla.org/`  
\n (unmatched path)

\n\n  
\n\n\n

`https://mozilla.org/*`

\n

Match HTTPS URLs only at "mozilla.org", with any path.

\n\n| \n

`https://mozilla.org/`

\n

`https://mozilla.org/path`

\n

`https://mozilla.org/another`

\n

`https://mozilla.org/path/to/doc`

\n\n| \n

`http://mozilla.org/path`  
\n (unmatched scheme)

\n

`https://mozilla.com/path`  
\n (unmatched host)

\n\n  
\n\n\n

`https://mozilla.org/a/b/c/`

\n

Match only this URL.

\n\n| `https://mozilla.org/a/b/c/`\n| Anything else.\n  
\n\n\n

`https://mozilla.org/*/b/*/`

\n

Match HTTPS URLs hosted on "mozilla.org", whose path contains a component "b"
somewhere in the middle.

\n\n| \n

`https://mozilla.org/a/b/c/`

\n

`https://mozilla.org/d/b/f/`

\n

`https://mozilla.org/a/b/c/d/`

\n\n| \n

`https://mozilla.org/b/*/`  
\n (unmatched path)

\n

`https://mozilla.org/a/b/`  
\n (unmatched path)

\n\n  
\n\n\n

`file:///blah/*`

\n

Match any FILE URL whose path begins with "blah".

\n\n| \n

`file:///blah/`

\n

`file:///blah/bleh`

\n\n| `file:///bleh/`  
\n (unmatched path)\n  
\n\n\n

### Invalid match patterns

\n\n\n\nInvalid pattern\n| Reason\n  
---|---  
\n\n\n\n`resource://path/`\n| Unsupported scheme.\n  
\n\n`https://mozilla.org`\n| No path.\n  
\n\n`https://mozilla.*.org/`\n| "*" in host must be at the start.\n  
\n\n`https://*zilla.org/`\n| "*" in host must be the only character or be
followed by ".".\n  
\n\n`http*://mozilla.org/`\n| "*" in scheme must be the only character.\n  
\n\n`file://*`\n| Empty path: this should be "`file:///*`".\n  
\n\n\n

## Testing match patterns

\n

When writing extensions, you don't generally work with match patterns
directly: usually you pass a match pattern string into an API, and the API
constructs a match pattern and uses it to test URLs. However, if you're trying
to work out which match pattern to use, or debugging a problem with one, it
can be useful to be able to create and test match patterns directly. This
section explains how to do this.

\n

First, open the developer tool settings and check the setting marked "Enable
browser chrome and add-on debugging toolboxes":

\n

\n

Next, open the "Browser Console":

\n

\n

This gives you a command line that you can use to execute privileged
JavaScript in Firefox.

\n

\n

Because code running in the Browser Console has system privileges, any time
you use it to run code, you need to understand exactly what the code is doing.
That includes the code samples in this article.

\n

\n

Now paste this code into the command line and press enter:

\n

    
    
    Cu.import("resource://gre/modules/MatchPattern.jsm");\nCu.import("resource://gre/modules/BrowserUtils.jsm");

\n

This does two things:

\n

\n

  * imports "MatchPattern.jsm": this is the system module that implements match patterns. Specifically, the module contains a constructor for `MatchPattern` objects.\xa0`MatchPattern` objects define a function called `matches()`, that takes a URI and returns `true` or `false`.
\n

  * imports "BrowserUtils.jsm": this includes a function `makeURI()`, that converts a string into an `[nsIURI](/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIURI)` object. `nsIURI` is the type that `matches()` expects to receive.
\n

\n

Now you can construct `MatchPattern` objects, construct URIs, and check
whether the URIs match:

\n

    
    
    var match = new MatchPattern("*://mozilla.org/");\n\nvar uri = BrowserUtils.makeURI("https://mozilla.org/");\nmatch.matches(uri); //        < true\n\nuri = BrowserUtils.makeURI("https://mozilla.org/path");\nmatch.matches(uri); //        < false

\n

## Converting Match Patterns to Regular Expressions

\n

All match patterns can be representing by regular expressions. This code
converts a match pattern to a regular expression:

\n

    
    
    /**\n * Transforms a valid match pattern into a regular expression\n * which matches all URLs included by that pattern.\n *\n * @param  {string}  pattern  The pattern to transform.\n * @return {RegExp}           The pattern's equivalent as a RegExp.\n * @throws {TypeError}        If the pattern is not a valid MatchPattern\n */\nfunction matchPatternToRegExp(pattern) {\n    if (pattern === '') {\n        return (/^(?:http|https|file|ftp|app):\\/\\//);\n    }\n\n    const schemeSegment = '(\\\\*|http|https|file|ftp)';\n    const hostSegment = '(\\\\*|(?:\\\\*\\\\.)?(?:[^/*]+))?';\n    const pathSegment = '(.*)';\n    const matchPatternRegExp = new RegExp(\n        `^${schemeSegment}://${hostSegment}/${pathSegment}$`\n    );\n\n    let match = matchPatternRegExp.exec(pattern);\n    if (!match) {\n         throw new TypeError(`"${pattern}" is not a valid MatchPattern`);\n    }\n\n    let [, scheme, host, path] = match;\n    if (!host) {\n        throw new TypeError(`"${pattern}" does not have a valid host`);\n    }\n\n    let regex = '^';\n\n    if (scheme === '*') {\n        regex += '(http|https)';\n    } else {\n        regex += scheme;\n    }\n\n    regex += '://';\n\n    if (host && host === '*') {\n        regex += '[^/]+?';\n    } else if (host) {\n        if (host.match(/^\\*\\./)) {\n            regex += '[^/]*?';\n            host = host.substring(2);\n        }\n        regex += host.replace(/\\./g, '\\\\.');\n    }\n\n    if (path) {\n        if (path === '*') {\n            regex += '(/.*)?';\n        } else if (path.charAt(0) !== '/') {\n            regex += '/';\n            regex += path.replace(/\\./g, '\\\\.').replace(/\\*/g, '.*?');\n            regex += '/?';\n        }\n    }\n\n    regex += '$';\n    return new RegExp(regex);\n}\n

\n]

