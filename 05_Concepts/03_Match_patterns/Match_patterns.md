Match patterns are a way to specify groups of URLs: a match pattern matches a
specific set of URLs. They are for extensions using WebExtensions APIs in a
few places, most notably to specify which documents to load [content scripts
](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts) into, and to
specify which URLs to add `[webRequest](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/webRequest)` listeners to.

APIs that use match patterns usually accept a list of match patterns, and will
perform the appropriate action if the URL matches any of the patterns. See,
for example, the `[content_scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/content_scripts)` key in manifest.json.

## Match pattern structure

All match patterns are specified as strings. Apart from the special
["<all_urls>"](/en-US/Add-ons/WebExtensions/Match_patterns#%3Call_urls%3E)
pattern, match patterns consist of three parts: _scheme_ , _host_ , and
_path_. The scheme and host are separated by "://".

    
    
    <scheme>://<host><path>

### scheme

The _scheme_ component may take one of two forms:

Form | Matches  
---|---  
"*" | Only "http" and "https".  
One of "http", "https", "file", "ftp", "app". | Only the given scheme.  
  
### host

The _host_ component may take one of three forms:

Form | Matches  
---|---  
"*" | Any host.  
"*." followed by part of the hostname. | The given host and any of its
subdomains.  
A complete hostname, without wildcards. | Only the given host.  
  
_host_ is optional only if the _scheme_ is "file".

Note that the wildcard may only appear at the start.

### path

The path component must begin with a "/".

After that, it may subsequently contain any combination of the "*" wildcard
and any of the characters that are allowed in URL paths. Unlike _host_ , the
_path_ component may contain the "*" wildcard in the middle or at the end, and
the "*" wildcard may appear more than once.

### <all_urls>

The special value "<all_urls>" matches all URLs under any of the supported
schemes: that is, "http", "https", "file", "ftp", "app".

## Examples

Pattern | Example matches | Example non-matches  
---|---|---  
  
`<all_urls>`

Match all URLs.

|

`http://example.org/`

`ftp://files.somewhere.org/`

`https://a.org/some/path/`

|

`resource://a/b/c/`  
(unsupported scheme)  
  
`*://*.mozilla.org/*`

Match all HTTP and HTTPS URLs that are hosted at "mozilla.org" or one of its
subdomains.

|

`http://mozilla.org/`

`https://mozilla.org/`

`http://a.mozilla.org/`

`http://a.b.mozilla.org/`

`https://b.mozilla.org/path/`

|

`ftp://mozilla.org/`  
(unmatched scheme)

`http://mozilla.com/`  
(unmatched host)

`http://firefox.org/`  
(unmatched host)  
  
`*://mozilla.org/`

Match all HTTP and HTTPS URLs that are hosted at exactly "mozilla.org/".

|

`http://mozilla.org/`

`https://mozilla.org/`

|

`ftp://mozilla.org/`  
(unmatched scheme)

`http://a.mozilla.org/`  
(unmatched host)

`http://mozilla.org/a`  
(unmatched path)  
  
`ftp://mozilla.org/`

Match only "ftp://mozilla.org/".

| `ftp://mozilla.org` |

`http://mozilla.org/`  
(unmatched scheme)

`ftp://sub.mozilla.org/`  
(unmatched host)

`ftp://mozilla.org/path`  
(unmatched path)  
  
`https://*/path`

Match HTTPS URLs on any host, whose path is "path".

|

`https://mozilla.org/path`

`https://a.mozilla.org/path`

`https://something.com/path`

|

`http://mozilla.org/path`  
(unmatched scheme)

`https://mozilla.org/path/`  
(unmatched path)

`https://mozilla.org/a`  
(unmatched path)

`https://mozilla.org/`  
(unmatched path)  
  
`https://*/path/`

Match HTTPS URLs on any host, whose path is "path/".

|

`https://mozilla.org/path/`

`https://a.mozilla.org/path/`

`https://something.com/path`/

|

`http://mozilla.org/path/`  
(unmatched scheme)

`https://mozilla.org/path`  
(unmatched path)

`https://mozilla.org/a`  
(unmatched path)

`https://mozilla.org/`  
(unmatched path)  
  
`https://mozilla.org/*`

Match HTTPS URLs only at "mozilla.org", with any path.

|

`https://mozilla.org/`

`https://mozilla.org/path`

`https://mozilla.org/another`

`https://mozilla.org/path/to/doc`

|

`http://mozilla.org/path`  
(unmatched scheme)

`https://mozilla.com/path`  
(unmatched host)  
  
`https://mozilla.org/a/b/c/`

Match only this URL.

| `https://mozilla.org/a/b/c/` | Anything else.  
  
`https://mozilla.org/*/b/*/`

Match HTTPS URLs hosted on "mozilla.org", whose path contains a component "b"
somewhere in the middle.

|

`https://mozilla.org/a/b/c/`

`https://mozilla.org/d/b/f/`

`https://mozilla.org/a/b/c/d/`

|

`https://mozilla.org/b/*/`  
(unmatched path)

`https://mozilla.org/a/b/`  
(unmatched path)  
  
`file:///blah/*`

Match any FILE URL whose path begins with "blah".

|

`file:///blah/`

`file:///blah/bleh`

| `file:///bleh/`  
(unmatched path)  
  
### Invalid match patterns

Invalid pattern | Reason  
---|---  
`resource://path/` | Unsupported scheme.  
`https://mozilla.org` | No path.  
`https://mozilla.*.org/` | "*" in host must be at the start.  
`https://*zilla.org/` | "*" in host must be the only character or be followed
by ".".  
`http*://mozilla.org/` | "*" in scheme must be the only character.  
`file://*` | Empty path: this should be "`file:///*`".  
  
## Testing match patterns

When writing extensions, you don't generally work with match patterns
directly: usually you pass a match pattern string into an API, and the API
constructs a match pattern and uses it to test URLs. However, if you're trying
to work out which match pattern to use, or debugging a problem with one, it
can be useful to be able to create and test match patterns directly. This
section explains how to do this.

First, open the developer tool settings and check the setting marked "Enable
browser chrome and add-on debugging toolboxes":

Next, open the "Browser Console":

This gives you a command line that you can use to execute privileged
JavaScript in Firefox.

Because code running in the Browser Console has system privileges, any time
you use it to run code, you need to understand exactly what the code is doing.
That includes the code samples in this article.

Now paste this code into the command line and press enter:

    
    
    Cu.import("resource://gre/modules/MatchPattern.jsm");
    Cu.import("resource://gre/modules/BrowserUtils.jsm");

This does two things:

  * imports "MatchPattern.jsm": this is the system module that implements match patterns. Specifically, the module contains a constructor for `MatchPattern` objects. `MatchPattern` objects define a function called `matches()`, that takes a URI and returns `true` or `false`.
  * imports "BrowserUtils.jsm": this includes a function `makeURI()`, that converts a string into an `[nsIURI](/en-US/docs/Mozilla/Tech/XPCOM/Reference/Interface/nsIURI)` object. `nsIURI` is the type that `matches()` expects to receive.

Now you can construct `MatchPattern` objects, construct URIs, and check
whether the URIs match:

    
    
    var match = new MatchPattern("*://mozilla.org/");
    
    var uri = BrowserUtils.makeURI("https://mozilla.org/");
    match.matches(uri); //        < true
    
    uri = BrowserUtils.makeURI("https://mozilla.org/path");
    match.matches(uri); //        < false

## Converting Match Patterns to Regular Expressions

All match patterns can be representing by regular expressions. This code
converts a match pattern to a regular expression:

    
    
    /**
     * Transforms a valid match pattern into a regular expression
     * which matches all URLs included by that pattern.
     *
     * @param  {string}  pattern  The pattern to transform.
     * @return {RegExp}           The pattern's equivalent as a RegExp.
     * @throws {TypeError}        If the pattern is not a valid MatchPattern
     */
    function matchPatternToRegExp(pattern) {
        if (pattern === '') {
            return (/^(?:http|https|file|ftp|app):\/\//);
        }
    
        const schemeSegment = '(\\*|http|https|file|ftp)';
        const hostSegment = '(\\*|(?:\\*\\.)?(?:[^/*]+))?';
        const pathSegment = '(.*)';
        const matchPatternRegExp = new RegExp(
            `^${schemeSegment}://${hostSegment}/${pathSegment}$`
        );
    
        let match = matchPatternRegExp.exec(pattern);
        if (!match) {
             throw new TypeError(`"${pattern}" is not a valid MatchPattern`);
        }
    
        let [, scheme, host, path] = match;
        if (!host) {
            throw new TypeError(`"${pattern}" does not have a valid host`);
        }
    
        let regex = '^';
    
        if (scheme === '*') {
            regex += '(http|https)';
        } else {
            regex += scheme;
        }
    
        regex += '://';
    
        if (host && host === '*') {
            regex += '[^/]+?';
        } else if (host) {
            if (host.match(/^\*\./)) {
                regex += '[^/]*?';
                host = host.substring(2);
            }
            regex += host.replace(/\./g, '\\.');
        }
    
        if (path) {
            if (path === '*') {
                regex += '(/.*)?';
            } else if (path.charAt(0) !== '/') {
                regex += '/';
                regex += path.replace(/\./g, '\\.').replace(/\*/g, '.*?');
                regex += '/?';
            }
        }
    
        regex += '$';
        return new RegExp(regex);
    }
    

