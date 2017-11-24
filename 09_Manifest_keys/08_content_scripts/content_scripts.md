Type | `Array`  
---|---  
Mandatory | No  
Example |

    
    
    "content_scripts": [
      {
        "matches": ["*://*.mozilla.org/*"],
        "js": ["borderify.js"]
      }
    ]  
  
Instructs the browser to load [content scripts](/en-US/docs/Mozilla/Add-
ons/WebExtensions/Content_scripts) into web pages whose URL matches a given
pattern.

This key is an array. Each item is an object which:

  * **must** contain a key named **`matches`** , that specifies the URL patterns to be matched in order for the scripts to be loaded
  * **may** contain keys named **`js`** and **`css`** , which list scripts to be loaded into matching pages
  * **may** contain a number of other properties that control finer aspects of how and when content scripts are loaded

Details of all the keys you can include are given in the table below.

Name | Type | Description  
---|---|---  
`all_frames` | `Boolean` |

`true`: inject the scripts specified in `js` and `css` into all frames
matching the specified URL requirements, even if the frame is not the topmost
frame in a tab. This does not inject into child frames where only their parent
matches the URL requirements and the child frame does not match the URL
requirements. The URL requirements are checked for each frame independently.

`false`: inject only into frames matching the URL requirements which are the
topmost frame in a tab.

Defaults to `false`.  
  
`css` | `Array` |

An array of paths, relative to manifest.json, referencing CSS files that will
be injected into matching pages.

Files are injected in the order given, and before the DOM is loaded.  
  
`exclude_globs` | `Array` | An array of strings containing wildcards. See
[Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns) below.  
`exclude_matches` | `Array` | An array of [match patterns](/en-US/Add-
ons/WebExtensions/match_patterns). See [Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns) below.  
`include_globs` | `Array` | An array of strings containing wildcards. See
[Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns) below.  
`js` | `Array` |

An array of paths, relative to the manifest.json file, referencing JavaScript
files that will be injected into matching pages.

Files are injected in the order given. This means that, for example, if you
include jQuery here followed by another content script, like this:

    
    
    "js": ["jquery.js", "my-content-script.js"]

then `"my-content-script.js"` can use jQuery.

Files are injected at the time specified by `run_at`.  
  
`match_about_blank` | `Boolean` |

Insert the content scripts into pages whose URL is "about:blank" or
"about:srcdoc", if the URL of the page that opened or created this page
[matches the patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns)
specified in the rest of the `content_scripts` key.

This is especially useful to run scripts in empty iframes , whose URL is
"about:blank". To do this you should also set the `all_frames` key.

For example, suppose you have a `content_scripts` key like this:

    
    
      "content_scripts": [
        {
          "js": ["my-script.js"],
          "matches": ["https://example.org/"],
          "match_about_blank": true,
          "all_frames": true
        }
      ]

If the user loads https://example.org/, and this page embeds an empty iframe,
then "my-script.js" will be loaded into the iframe.

`match_about_blank` is supported in Firefox from version 52. Note that in
Firefox, content scripts won't be injected into empty iframes at
`"document_start"` even if you specify that value in `[run_at](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#run_at)`.  
  
`matches` | `Array` |

An array of [match patterns](/en-US/Add-ons/WebExtensions/match_patterns). See
[Matching URL patterns](/en-US/Add-
ons/WebExtensions/manifest.json/content_scripts#Matching_URL_patterns) below.

This is the only mandatory key.  
  
`run_at` | `String` |

This option determines when the scripts specified in `js` are injected. You
can supply one of three strings here, each of which identifies a state in the
process of loading a document. The states directly correspond to
[`Document.readyState`](/en-US/docs/Web/API/Document/readyState "The
Document.readyState property of a document describes the loading state of the
document."):

  * "`document_start`": corresponds to `loading`. The DOM is still loading.
  * "`document_end`": corresponds to `interactive`. The DOM has finished loading, but resources such as scripts and images may still be loading.
  * "`document_idle`": corresponds to `complete`. The document and all its resources have finished loading.

The default value is `"document_idle"`.

In all cases, files in `js` are injected after files in `css`.  
  
## Matching URL patterns

The `"content_scripts"` key attaches content scripts to documents based on URL
matching: if the document's URL matches the specification in the key, then the
script will be attached. There are four properties inside `"content_scripts"`
that you can use for this specification:

  * `matches`: an array of [match patterns](/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns).
  * `exclude_matches:` an array of [match patterns](/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns).
  * `include_globs`: an array of globs.
  * `exclude_globs:` an array of globs.

To match one of these properties, a URL must match at least one of the items
in its array. For example, given a property like:

    
    
    "matches": ["*://*.example.org/*", "*://*.example.com/*"]

Both "http://example.org/" and "http://example.com/" will match.

Since `matches` is the only mandatory key, the other three keys are use to
limit further the URLs that match. To match the key as a whole, a URL must:

  1. match the `matches` property
  2. AND match the `include_globs` property, if present
  3. AND NOT match the `exclude_matches` property, if present
  4. AND NOT match the `exclude_globs` property, if present

### globs

A glob is just a string that may contain wildcards. There are two types of
wildcard, and you can combine them in the same glob:

  * "*" matches zero or more characters
  * "?" matches exactly one character.

For example: `"*na?i"` would match `"illuminati"` and `"annunaki"`, but not
`"sagnarelli"`.

## Example

    
    
    "content_scripts": [
      {
        "matches": ["*://*.mozilla.org/*"],
        "js": ["borderify.js"]
      }
    ]

This injects a single content script "borderify.js" into all pages under
"mozilla.org" or any of its subdomains, whether served over HTTP or HTTPS.

    
    
      "content_scripts": [
        {
          "exclude_matches": ["*://developer.mozilla.org/*"],
          "matches": ["*://*.mozilla.org/*"],
          "js": ["jquery.js", "borderify.js"]
        }
      ]

This injects two content scripts into all pages under "mozilla.org" or any of
its subdomains except "developer.mozilla.org", whether served over HTTP or
HTTPS.

The content scripts see the same view of the DOM and are injected in the order
they appear in the array, so "borderify.js" can see global variables added by
"jquery.js".

## Browser compatibility

The compatibility table in this page is generated from structured data. If
you'd like to contribute to the data, please check out <https://github.com/mdn
/browser-compat-data> and send us a pull request.

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
Basic support|  Yes1|  Yes| 482| 482|  Yes1  
`match_about_blank`|  Yes|  Yes| 52| 52|  Yes  
  
1\. Content scripts are not applied to tabs already open when the extension is
loaded.

2\. Content scripts won't be injected into empty iframes at 'document_start'
even if you specify that value in 'run_at'.

| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
Basic support|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  Full support Yes|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.
|  Full support Yes

Notes __

Full support Yes

Notes __

     Notes __Content scripts are not applied to tabs already open when the extension is loaded.
|  Full support 48

Notes __

Full support 48

Notes __

     Notes __Content scripts won't be injected into empty iframes at 'document_start' even if you specify that value in 'run_at'.  
`match_about_blank`|  Full support Yes|  Full support Yes|  Full support 52|
Full support Yes|  Full support 52

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[Mobile __]: Mobile
  *[
 Full support

]: Full support

  *[Firefox __]: Firefox
  *[Notes __]: See implementation notes
  *[
Full support

]: Full support

  *[ Notes __]: See implementation notes
  *[Chrome __]: Chrome

