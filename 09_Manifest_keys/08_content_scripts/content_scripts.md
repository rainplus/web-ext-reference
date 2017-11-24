[\n

\n\n\n\nType\n| `Array`\n  
---|---  
\n\nMandatory\n| No\n  
\n\nExample\n| \n

    
    
    \n"content_scripts": [\n  {\n    "matches": ["*://*.mozilla.org/*"],\n    "js": ["borderify.js"]\n  }\n]

\n\n  
\n\n\n

Instructs the browser to load [content scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Content_scripts) into web pages whose URL matches a given
pattern.

\n

This key is an array. Each item is an object which:

\n

\n

  *  **must** contain a key named **`matches`** , that specifies the URL patterns to be matched in order for the scripts to be loaded
\n

  *  **may** contain keys named **`js`** and **`css`** , which list scripts to be loaded into matching pages
\n

  *  **may** contain a number of other properties that control finer aspects of how and when content scripts are loaded
\n

\n

Details of all the keys you can include are given in the table below.

\n\n\n\nName\n| Type\n| Description\n  
---|---|---  
\n\n\n\n`all_frames`\n| `Boolean`\n| \n

`true`: inject the scripts specified in `js` and `css` into all frames
matching the specified URL requirements, even if the frame is not the topmost
frame in a tab. This does not inject into child frames where only their parent
matches the URL requirements and the child frame does not match the URL
requirements. The URL requirements are checked for each frame independently.

\n

`false`: inject only into frames matching the URL requirements which are the
topmost frame in a tab.

\n

Defaults to `false`.

\n\n  
\n\n`css`\n| `Array`\n| \n

An array of paths, relative to manifest.json, referencing CSS files that will
be injected into matching pages.

\n

Files are injected in the order given, and before the DOM is loaded.

\n\n  
\n\n`exclude_globs`\n| `Array`\n| An array of strings containing wildcards.
See [Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns)
below.\n  
\n\n`exclude_matches`\n| `Array`\n| An array of [match patterns](/en-US/Add-
ons/WebExtensions/match_patterns). See [Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns)
below.\n  
\n\n`include_globs`\n| `Array`\n| An array of strings containing wildcards.
See [Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns)
below.\n  
\n\n`js`\n| `Array`\n| \n

An array of paths, relative to the manifest.json file, referencing JavaScript
files that will be injected into matching pages.

\n

Files are injected in the order given. This means that, for example, if you
include jQuery here followed by another content script, like this:

\n

    
    
    \n"js": ["jquery.js", "my-content-script.js"]

\n

then\xa0`"my-content-script.js"` can use jQuery.

\n

Files are injected at the time specified by `run_at`.

\n\n  
\n\n`match_about_blank`\n| `Boolean`\n| \n

Insert the content scripts into pages whose URL is "about:blank" or
"about:srcdoc", if the URL of the page that opened or created this page
[matches the patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns)
specified in the rest of the `content_scripts` key.

\n

This is especially useful to run scripts in empty iframes , whose URL is
"about:blank". To do this you should also set the `all_frames` key.

\n

For example, suppose you have a `content_scripts` key like this:

\n

    
    
    \n  "content_scripts": [\n    {\n      "js": ["my-script.js"],\n      "matches": ["https://example.org/"],\n      "match_about_blank": true,\n      "all_frames": true\n    }\n  ]

\n

If the user loads https://example.org/, and this page embeds an empty iframe,
then "my-script.js" will be loaded into the iframe.

\n

`match_about_blank` is supported in Firefox from version 52. Note that in
Firefox, content scripts won't be injected into empty iframes at
`"document_start"` even if you specify that value in `[run_at](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#run_at)`.

\n\n  
\n\n`matches`\n| `Array`\n| \n

An array of [match patterns](/en-US/Add-ons/WebExtensions/match_patterns). See
[Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns) below.

\n

This is the only mandatory key.

\n\n  
\n\n`run_at`\n| `String`\n| \n

This option determines when the scripts specified in `js` are injected. You
can supply one of three strings here, each of which identifies a state in the
process of loading a document. The states directly correspond to
[`Document.readyState`](/en-US/docs/Web/API/Document/readyState "The
Document.readyState property of a document describes the loading state of the
document."):

\n

\n

  * "`document_start`": corresponds to `loading`. The DOM is still loading.
\n

  * "`document_end`": corresponds to `interactive`. The DOM has finished loading, but resources such as scripts and images may still be loading.
\n

  * "`document_idle`": corresponds to `complete`. The document and all its resources have finished loading.
\n

\n

The default value is `"document_idle"`.

\n

In all cases, files in `js` are injected after files in `css`.

\n\n  
\n\n\n

## Matching URL patterns

\n

The `"content_scripts"` key attaches content scripts to documents based on URL
matching: if the document's URL matches the specification in the key, then the
script will be attached. There are four properties inside `"content_scripts"`
that you can use for this specification:

\n

\n

  * `matches`: an array of [match patterns](/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns).
\n

  * `exclude_matches:` an array of [match patterns](/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns).
\n

  * `include_globs`: an array of globs.
\n

  * `exclude_globs:` an array of globs.
\n

\n

To match one of these properties, a URL must match at least one of the items
in its array. For example, given a property like:

\n

    
    
    "matches": ["*://*.example.org/*", "*://*.example.com/*"]

\n

Both "http://example.org/" and "http://example.com/" will match.

\n

Since `matches` is the only mandatory key, the other three keys are use to
limit further the URLs that match. To match the key as a whole, a URL must:

\n

\n

  1. match the `matches` property
\n

  2. AND match the `include_globs` property, if present
\n

  3. AND NOT match the `exclude_matches` property, if present
\n

  4. AND NOT match the `exclude_globs` property, if present
\n

\n

### globs

\n

A glob is just a string that may contain wildcards. There are two types of
wildcard, and you can combine them in the same glob:

\n

\n

  * "*" matches zero or more characters
\n

  * "?" matches exactly one character.
\n

\n

For example: `"*na?i"` would match `"illuminati"` and `"annunaki"`, but not
`"sagnarelli"`.

\n

## Example

\n

    
    
    "content_scripts": [\n  {\n    "matches": ["*://*.mozilla.org/*"],\n    "js": ["borderify.js"]\n  }\n]

\n

This injects a single content script "borderify.js" into all pages under
"mozilla.org" or any of its subdomains, whether served over HTTP or HTTPS.

\n

    
    
      "content_scripts": [\n    {\n      "exclude_matches": ["*://developer.mozilla.org/*"],\n      "matches": ["*://*.mozilla.org/*"],\n      "js": ["jquery.js", "borderify.js"]\n    }\n  ]

\n

This injects two content scripts into all pages under "mozilla.org" or any of
its subdomains except "developer.mozilla.org", whether served over HTTP or
HTTPS.

\n

The content scripts see the same view of the DOM and are injected in the order
they appear in the array, so "borderify.js" can see global variables added by
"jquery.js".

\n

## Browser compatibility

\n

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support| \n Yes1| \n Yes| 482| 482| \n Yes1  
`match_about_blank`| \n Yes| \n Yes| 52| 52| \n Yes  
  
1\. Content scripts are not applied to tabs already open when the extension is
loaded.

2\. Content scripts won't be injected into empty iframes at 'document_start'
even if you specify that value in 'run_at'.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  \nFull support\n\n Yes| \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.
|  \nFull support\n\n Yes

Notes __

\nFull support\n\n Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  \nFull support\n\n 48

Notes __

\nFull support\n\n 48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.  
`match_about_blank`|  \nFull support\n\n Yes| \nFull support\n\n Yes| \nFull
support\n\n 52| \nFull support\n\n Yes| \nFull support\n\n 52  
  
\n]

  *[\nFull support\n]: Full support
  *[ \nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

