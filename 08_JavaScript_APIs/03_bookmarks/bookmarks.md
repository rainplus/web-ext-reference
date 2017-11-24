[\n

\n

The [WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions) [`bookmarks
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks "The documentation
about this has not yet been written; please consider contributing!") API lets
an extension interact with and manipulate the browser's bookmarking system.
You can use it to bookmark pages, retrieve existing bookmarks, and edit,
remove, and organize bookmarks.

\n

To use this API, an extension must request the "bookmarks"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) in its `[manifest.json](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)` file.

\n

## Types

\n

\n[`bookmarks.BookmarkTreeNode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type
bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each
node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered
by an index within their respective parent folders.")

\n    Represents a bookmark or folder in the bookmarks tree.

\n[`bookmarks.BookmarkTreeNodeType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNodeType "The
bookmarks.BookmarkTreeNodeType type is used to describe whether a node in the
bookmark tree is a bookmark, a folder, or a separator.")

\n    A [`String`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String
"The String global object is a constructor for strings, or a sequence of
characters.") enum which describes whether a node in the tree is a bookmark, a
folder, or a separator.

\n[`bookmarks.BookmarkTreeNodeUnmodifiable`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNodeUnmodifiable "The
bookmarks.BookmarkTreeNodeUnmodifiable type is used to indicate the reason
that a node in the bookmark tree \(where each node is either a bookmark or a
bookmark folder\) cannot be changed. This is used as the value of the
bookmarks.BookmarkTreeNode.unmodifiable.unmodifiable field on bookmark
nodes.")

\n    A [`String`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String
"The String global object is a constructor for strings, or a sequence of
characters.") enum which specifies why a bookmark or folder is unmodifiable.

\n[`bookmarks.CreateDetails`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/CreateDetails "The CreateDetails type is used
to describe the properties of a new, bookmark, bookmark folder, or separator
when calling the bookmarks.create\(\) method.")

\n    Contains information which is passed to the [`bookmarks.create()`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/create "Creates a bookmark
or folder as a child of the BookmarkTreeNode with the specified parentId. To
create a folder, omit or leave empty the CreateDetails.url parameter.")
function when creating a new bookmark.

\n\n

## Functions

\n

\n[`bookmarks.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/create "Creates a bookmark or folder as a
child of the BookmarkTreeNode with the specified parentId. To create a folder,
omit or leave empty the CreateDetails.url parameter.")

\n    Creates a bookmark or folder.

\n[`bookmarks.get()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/get "Given the ID of a
bookmarks.BookmarkTreeNode or an array of such IDs, the bookmarks.get\(\)
method retrieves the matching nodes.")

\n    Retrieves one or more [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type
bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each
node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered
by an index within their respective parent folders.")s, given a bookmark's ID
or an array of bookmark IDs.

\n[`bookmarks.getChildren()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getChildren "bookmarks.getChildren\(\)
retrieves all the immediate children of a given bookmark folder, identified as
a BookmarkTreeNode ID.")

\n    Retrieves the children of the specified [`BookmarkTreeNode`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An
object of type bookmarks.BookmarkTreeNode represents a node in the bookmark
tree, where each node is a bookmark, a bookmark folder, or a separator. Child
nodes are ordered by an index within their respective parent folders.").

\n[`bookmarks.getRecent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getRecent "The documentation about this has
not yet been written; please consider contributing!")

\n    Retrieves a requested number of recently added bookmarks.

\n[`bookmarks.getSubTree()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getSubTree "The bookmarks.getSubTree\(\)
method asynchronously retrieves a bookmarks.BookmarkTreeNode, given its ID.")

\n    Retrieves part of the bookmarks tree, starting at the specified node.

\n[`bookmarks.getTree()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getTree "bookmarks.getTree\(\) returns an
array containing the root of the bookmarks tree as a
bookmarks.BookmarkTreeNode object.")

\n    Retrieves the entire bookmarks tree into an array of [`BookmarkTreeNode
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/BookmarkTreeNode
"An object of type bookmarks.BookmarkTreeNode represents a node in the
bookmark tree, where each node is a bookmark, a bookmark folder, or a
separator. Child nodes are ordered by an index within their respective parent
folders.") objects.

\n[`bookmarks.move()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/move "The bookmarks.move\(\) method moves the
specified BookmarkTreeNode to the specified destination within the tree of
bookmarks. This lets you move a bookmark to a new folder and/or position
within the folder.")

\n    Moves the specified [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type
bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each
node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered
by an index within their respective parent folders.") to a new location in the
bookmark tree.

\n[`bookmarks.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/remove "The bookmarks.remove\(\) method
removes a single bookmark or an empty bookmark folder.")

\n    Removes a bookmark or an empty bookmark folder, given the node's ID.

\n[`bookmarks.removeTree()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/removeTree "The documentation about this has
not yet been written; please consider contributing!")

\n    Recursively removes a bookmark folder; that is, given the ID of a folder
node, removes that node and all its descendants.

\n[`bookmarks.search()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/search "The bookmarks.search\(\) function
searches for bookmarks matching the given query.")

\n    Searches for [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type
bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each
node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered
by an index within their respective parent folders.")s matching a specified
set of criteria.

\n[`bookmarks.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/update "bookmarks.update\(\) updates the title
and/or URL of a bookmark, or the name of a bookmark folder.")

\n    Updates the title and/or URL of a bookmark, or the name of a bookmark
folder, given the bookmark's ID.

\n\n

## Events

\n

\n[`bookmarks.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onCreated "Fired when a bookmark item \(a
bookmark or a folder\) is created.")

\n    Fired when a bookmark or folder is created.

\n[`bookmarks.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onRemoved "The documentation about this has
not yet been written; please consider contributing!")

\n    Fired when a bookmark or folder is removed. When a folder is removed
recursively, a single notification is fired for the folder, and none for its
contents.

\n[`bookmarks.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onChanged "Fired when there is a change to:")

\n    Fired when a bookmark or folder changes. Currently, only `title` and
`url` changes trigger this.

\n[`bookmarks.onMoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onMoved "Fired when a bookmark or folder is
moved to a different parent folder and/or position within a folder.")

\n    Fired when a bookmark or folder is moved to a different parent folder or
to a new offset within its folder.

\n[`bookmarks.onChildrenReordered`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onChildrenReordered "Fired when the children
of a folder have changed their order due to the order being sorted in the UI.
This is not called as a result of a call to bookmarks.move\(\) or a drag
operation in the UI.")

\n    Fired when the user has sorted the children of a folder in the browser's
UI. This is not called as a result of a [`move()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/move "The bookmarks.move\(\) method moves the
specified BookmarkTreeNode to the specified destination within the tree of
bookmarks. This lets you move a bookmark to a new folder and/or position
within the folder.").

\n[`bookmarks.onImportBegan`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onImportBegan "Fired when the browser has
started importing a set of bookmarks.")

\n    Fired when a bookmark import session is begun. Expensive observers
should ignore [`bookmarks.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onCreated "Fired when a bookmark item \(a
bookmark or a folder\) is created.") updates until [`bookmarks.onImportEnded
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/onImportEnded "The
documentation about this has not yet been written; please consider
contributing!") is fired. Observers should still handle other notifications
immediately.

\n[`bookmarks.onImportEnded`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onImportEnded "The documentation about this
has not yet been written; please consider contributing!")

\n    Fired when a bookmark import session has finished.

\n\n

## Browser compatibility

\n

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`BookmarkTreeNode`| \n Yes *| \n No| 45 *| \n No| \n Yes *  
`BookmarkTreeNodeType`| \n No| \n No| 57| \n No| \n No  
`BookmarkTreeNodeUnmodifiable`| \n Yes| \n No| 45| \n No| \n Yes  
`CreateDetails`| \n Yes *| \n No| 45 *| \n No| \n Yes *  
`create`| \n Yes| 15| 45| \n No| \n Yes  
`get`| \n Yes| \n No| 45| \n No| \n Yes  
`getChildren`| \n Yes| \n No| 45| \n No| \n Yes  
`getRecent`| \n Yes| \n No| 47| \n No| \n Yes  
`getSubTree`| \n Yes| \n No| 45| \n No| \n Yes  
`getTree`| \n Yes| 15| 45| \n No| \n Yes  
`move`| \n Yes| 15| 45| \n No| \n Yes  
`onChanged`| \n Yes| \n No| 52| \n No| \n Yes  
`onChildrenReordered`| \n Yes| \n No| \n No| \n No| \n Yes  
`onCreated`| \n Yes| \n No| 52| \n No| \n Yes  
`onImportBegan`| \n Yes| \n No| \n No| \n No| \n Yes  
`onImportEnded`| \n Yes| \n No| \n No| \n No| \n Yes  
`onMoved`| \n Yes| \n No| 52| \n No| \n Yes  
`onRemoved`| \n Yes| \n No| 52| \n No| \n Yes  
`remove`| \n Yes| 15| 45| \n No| \n Yes  
`removeTree`| \n Yes| 15| 47| \n No| \n Yes  
`search`| \n Yes| \n No| 47| \n No| \n Yes  
`update`| \n Yes| 15| 45| \n No| \n Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`BookmarkTreeNode`|  \nPartial support\nPartial| \nNo support\n\n No|
\nPartial support\n45| \nPartial support\nPartial| \nNo support\n\n No  
`BookmarkTreeNodeType`| \nNo support\n\n No| \nNo support\n\n No| \nFull
support\n\n 57| \nNo support\n\n No| \nNo support\n\n No  
`BookmarkTreeNodeUnmodifiable`| \nFull support\n\n Yes| \nNo support\n\n No|
\nFull support\n\n 45| \nFull support\n\n Yes| \nNo support\n\n No  
`CreateDetails`| \nPartial support\nPartial| \nNo support\n\n No| \nPartial
support\n45| \nPartial support\nPartial| \nNo support\n\n No  
`create`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`get`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 45|
\nFull support\n\n Yes| \nNo support\n\n No  
`getChildren`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`getRecent`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
47| \nFull support\n\n Yes| \nNo support\n\n No  
`getSubTree`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`getTree`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`move`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull support\n\n 45|
\nFull support\n\n Yes| \nNo support\n\n No  
`onChanged`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
52| \nFull support\n\n Yes| \nNo support\n\n No  
`onChildrenReordered`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo
support\n\n No| \nFull support\n\n Yes| \nNo support\n\n No  
`onCreated`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
52| \nFull support\n\n Yes| \nNo support\n\n No  
`onImportBegan`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`onImportEnded`| \nFull support\n\n Yes| \nNo support\n\n No| \nNo support\n\n
No| \nFull support\n\n Yes| \nNo support\n\n No  
`onMoved`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 52|
\nFull support\n\n Yes| \nNo support\n\n No  
`onRemoved`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n
52| \nFull support\n\n Yes| \nNo support\n\n No  
`remove`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
`removeTree`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull
support\n\n 47| \nFull support\n\n Yes| \nNo support\n\n No  
`search`| \nFull support\n\n Yes| \nNo support\n\n No| \nFull support\n\n 47|
\nFull support\n\n Yes| \nNo support\n\n No  
`update`| \nFull support\n\n Yes| \nFull support\n\n 15| \nFull support\n\n
45| \nFull support\n\n Yes| \nNo support\n\n No  
  
\n

\n

The "Chrome incompatibilities" section is included from [
https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Chrome_incompatibilities](https://developer.mozilla.org/en-
US/Add-ons/WebExtensions/Chrome_incompatibilities) using the
[WebExtChromeCompat](/en-US/docs/Template:WebExtChromeCompat) macro.

\n

If you need to update this content, edit <https://developer.mozilla.org/en-US
/Add-ons/WebExtensions/Chrome_incompatibilities>, then shift-refresh this page
to see your changes.

\n

\n

## Example extensions

  * [bookmark-it](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)

\n

 **Acknowledgements** \n

This API is based on Chromium's
[`chrome.bookmarks`](https://developer.chrome.com/extensions/bookmarks) API.
This documentation is derived from
[`bookmarks.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/bookmarks.json)
in the Chromium code.

\n

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

\n

\n

\n

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.\n//\n// Redistribution and use in source and binary forms, with or without\n// modification, are permitted provided that the following conditions are\n// met:\n//\n//    * Redistributions of source code must retain the above copyright\n// notice, this list of conditions and the following disclaimer.\n//    * Redistributions in binary form must reproduce the above\n// copyright notice, this list of conditions and the following disclaimer\n// in the documentation and/or other materials provided with the\n// distribution.\n//    * Neither the name of Google Inc. nor the names of its\n// contributors may be used to endorse or promote products derived from\n// this software without specific prior written permission.\n//\n// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS\n// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT\n// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR\n// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT\n// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT\n// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,\n// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY\n// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\n// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n

\n

\n]

  *[\nFull support\n]: Full support
  *[Edge __]: Edge
  *[Opera __]: Opera
  *[\nNo support\n]: No support
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[\nPartial support\n]: Partial support
  *[Mobile __]: Mobile
  *[ \nPartial support\n]: Partial support
  *[Firefox __]: Firefox
  *[Chrome __]: Chrome

