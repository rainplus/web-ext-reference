The [WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions) [`bookmarks
`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks "The documentation
about this has not yet been written; please consider contributing!") API lets
an extension interact with and manipulate the browser's bookmarking system.
You can use it to bookmark pages, retrieve existing bookmarks, and edit,
remove, and organize bookmarks.

To use this API, an extension must request the "bookmarks"
[permission](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/permissions) in its `[manifest.json](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json)` file.

## Types

[`bookmarks.BookmarkTreeNode`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type
bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each
node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered
by an index within their respective parent folders.")

    Represents a bookmark or folder in the bookmarks tree.
[`bookmarks.BookmarkTreeNodeType`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNodeType "The
bookmarks.BookmarkTreeNodeType type is used to describe whether a node in the
bookmark tree is a bookmark, a folder, or a separator.")

    A [`String`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String "The String global object is a constructor for strings, or a sequence of characters.") enum which describes whether a node in the tree is a bookmark, a folder, or a separator.
[`bookmarks.BookmarkTreeNodeUnmodifiable`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/BookmarkTreeNodeUnmodifiable "The
bookmarks.BookmarkTreeNodeUnmodifiable type is used to indicate the reason
that a node in the bookmark tree \(where each node is either a bookmark or a
bookmark folder\) cannot be changed. This is used as the value of the
bookmarks.BookmarkTreeNode.unmodifiable.unmodifiable field on bookmark
nodes.")

    A [`String`](/en-US/docs/Web/JavaScript/Reference/Global_Objects/String "The String global object is a constructor for strings, or a sequence of characters.") enum which specifies why a bookmark or folder is unmodifiable.
[`bookmarks.CreateDetails`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/CreateDetails "The CreateDetails type is used
to describe the properties of a new, bookmark, bookmark folder, or separator
when calling the bookmarks.create\(\) method.")

    Contains information which is passed to the [`bookmarks.create()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/create "Creates a bookmark or folder as a child of the BookmarkTreeNode with the specified parentId. To create a folder, omit or leave empty the CreateDetails.url parameter.") function when creating a new bookmark.

## Functions

[`bookmarks.create()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/create "Creates a bookmark or folder as a
child of the BookmarkTreeNode with the specified parentId. To create a folder,
omit or leave empty the CreateDetails.url parameter.")

    Creates a bookmark or folder.
[`bookmarks.get()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/get "Given the ID of a
bookmarks.BookmarkTreeNode or an array of such IDs, the bookmarks.get\(\)
method retrieves the matching nodes.")

    Retrieves one or more [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered by an index within their respective parent folders.")s, given a bookmark's ID or an array of bookmark IDs.
[`bookmarks.getChildren()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getChildren "bookmarks.getChildren\(\)
retrieves all the immediate children of a given bookmark folder, identified as
a BookmarkTreeNode ID.")

    Retrieves the children of the specified [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered by an index within their respective parent folders.").
[`bookmarks.getRecent()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getRecent "The documentation about this has
not yet been written; please consider contributing!")

    Retrieves a requested number of recently added bookmarks.
[`bookmarks.getSubTree()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getSubTree "The bookmarks.getSubTree\(\)
method asynchronously retrieves a bookmarks.BookmarkTreeNode, given its ID.")

    Retrieves part of the bookmarks tree, starting at the specified node.
[`bookmarks.getTree()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/getTree "bookmarks.getTree\(\) returns an
array containing the root of the bookmarks tree as a
bookmarks.BookmarkTreeNode object.")

    Retrieves the entire bookmarks tree into an array of [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered by an index within their respective parent folders.") objects.
[`bookmarks.move()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/move "The bookmarks.move\(\) method moves the
specified BookmarkTreeNode to the specified destination within the tree of
bookmarks. This lets you move a bookmark to a new folder and/or position
within the folder.")

    Moves the specified [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered by an index within their respective parent folders.") to a new location in the bookmark tree.
[`bookmarks.remove()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/remove "The bookmarks.remove\(\) method
removes a single bookmark or an empty bookmark folder.")

    Removes a bookmark or an empty bookmark folder, given the node's ID.
[`bookmarks.removeTree()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/removeTree "The documentation about this has
not yet been written; please consider contributing!")

    Recursively removes a bookmark folder; that is, given the ID of a folder node, removes that node and all its descendants.
[`bookmarks.search()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/search "The bookmarks.search\(\) function
searches for bookmarks matching the given query.")

    Searches for [`BookmarkTreeNode`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/BookmarkTreeNode "An object of type bookmarks.BookmarkTreeNode represents a node in the bookmark tree, where each node is a bookmark, a bookmark folder, or a separator. Child nodes are ordered by an index within their respective parent folders.")s matching a specified set of criteria.
[`bookmarks.update()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/update "bookmarks.update\(\) updates the title
and/or URL of a bookmark, or the name of a bookmark folder.")

    Updates the title and/or URL of a bookmark, or the name of a bookmark folder, given the bookmark's ID.

## Events

[`bookmarks.onCreated`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onCreated "Fired when a bookmark item \(a
bookmark or a folder\) is created.")

    Fired when a bookmark or folder is created.
[`bookmarks.onRemoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onRemoved "The documentation about this has
not yet been written; please consider contributing!")

    Fired when a bookmark or folder is removed. When a folder is removed recursively, a single notification is fired for the folder, and none for its contents.
[`bookmarks.onChanged`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onChanged "Fired when there is a change to:")

    Fired when a bookmark or folder changes. Currently, only `title` and `url` changes trigger this.
[`bookmarks.onMoved`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onMoved "Fired when a bookmark or folder is
moved to a different parent folder and/or position within a folder.")

    Fired when a bookmark or folder is moved to a different parent folder or to a new offset within its folder.
[`bookmarks.onChildrenReordered`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onChildrenReordered "Fired when the children
of a folder have changed their order due to the order being sorted in the UI.
This is not called as a result of a call to bookmarks.move\(\) or a drag
operation in the UI.")

    Fired when the user has sorted the children of a folder in the browser's UI. This is not called as a result of a [`move()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/move "The bookmarks.move\(\) method moves the specified BookmarkTreeNode to the specified destination within the tree of bookmarks. This lets you move a bookmark to a new folder and/or position within the folder.").
[`bookmarks.onImportBegan`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onImportBegan "Fired when the browser has
started importing a set of bookmarks.")

    Fired when a bookmark import session is begun. Expensive observers should ignore [`bookmarks.onCreated`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/onCreated "Fired when a bookmark item \(a bookmark or a folder\) is created.") updates until [`bookmarks.onImportEnded`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/bookmarks/onImportEnded "The documentation about this has not yet been written; please consider contributing!") is fired. Observers should still handle other notifications immediately.
[`bookmarks.onImportEnded`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/bookmarks/onImportEnded "The documentation about this
has not yet been written; please consider contributing!")

    Fired when a bookmark import session has finished.

## Browser compatibility

| Chrome| Edge| Firefox| Firefox for Android| Opera  
---|---|---|---|---|---  
`BookmarkTreeNode`|  Yes *|  No| 45 *|  No|  Yes *  
`BookmarkTreeNodeType`|  No|  No| 57|  No|  No  
`BookmarkTreeNodeUnmodifiable`|  Yes|  No| 45|  No|  Yes  
`CreateDetails`|  Yes *|  No| 45 *|  No|  Yes *  
`create`|  Yes| 15| 45|  No|  Yes  
`get`|  Yes|  No| 45|  No|  Yes  
`getChildren`|  Yes|  No| 45|  No|  Yes  
`getRecent`|  Yes|  No| 47|  No|  Yes  
`getSubTree`|  Yes|  No| 45|  No|  Yes  
`getTree`|  Yes| 15| 45|  No|  Yes  
`move`|  Yes| 15| 45|  No|  Yes  
`onChanged`|  Yes|  No| 52|  No|  Yes  
`onChildrenReordered`|  Yes|  No|  No|  No|  Yes  
`onCreated`|  Yes|  No| 52|  No|  Yes  
`onImportBegan`|  Yes|  No|  No|  No|  Yes  
`onImportEnded`|  Yes|  No|  No|  No|  Yes  
`onMoved`|  Yes|  No| 52|  No|  Yes  
`onRemoved`|  Yes|  No| 52|  No|  Yes  
`remove`|  Yes| 15| 45|  No|  Yes  
`removeTree`|  Yes| 15| 47|  No|  Yes  
`search`|  Yes|  No| 47|  No|  Yes  
`update`|  Yes| 15| 45|  No|  Yes  
  
| Desktop __| Mobile __  
---|---|---  
| Chrome __| Edge __| Firefox __| Opera __| Firefox for Android __  
`BookmarkTreeNode`|  Partial support Partial|  No support No|  Partial support
45|  Partial support Partial|  No support No  
`BookmarkTreeNodeType`|  No support No|  No support No|  Full support 57|  No
support No|  No support No  
`BookmarkTreeNodeUnmodifiable`|  Full support Yes|  No support No|  Full
support 45|  Full support Yes|  No support No  
`CreateDetails`|  Partial support Partial|  No support No|  Partial support
45|  Partial support Partial|  No support No  
`create`|  Full support Yes|  Full support 15|  Full support 45|  Full support
Yes|  No support No  
`get`|  Full support Yes|  No support No|  Full support 45|  Full support Yes|
No support No  
`getChildren`|  Full support Yes|  No support No|  Full support 45|  Full
support Yes|  No support No  
`getRecent`|  Full support Yes|  No support No|  Full support 47|  Full
support Yes|  No support No  
`getSubTree`|  Full support Yes|  No support No|  Full support 45|  Full
support Yes|  No support No  
`getTree`|  Full support Yes|  Full support 15|  Full support 45|  Full
support Yes|  No support No  
`move`|  Full support Yes|  Full support 15|  Full support 45|  Full support
Yes|  No support No  
`onChanged`|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`onChildrenReordered`|  Full support Yes|  No support No|  No support No|
Full support Yes|  No support No  
`onCreated`|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`onImportBegan`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`onImportEnded`|  Full support Yes|  No support No|  No support No|  Full
support Yes|  No support No  
`onMoved`|  Full support Yes|  No support No|  Full support 52|  Full support
Yes|  No support No  
`onRemoved`|  Full support Yes|  No support No|  Full support 52|  Full
support Yes|  No support No  
`remove`|  Full support Yes|  Full support 15|  Full support 45|  Full support
Yes|  No support No  
`removeTree`|  Full support Yes|  Full support 15|  Full support 47|  Full
support Yes|  No support No  
`search`|  Full support Yes|  No support No|  Full support 47|  Full support
Yes|  No support No  
`update`|  Full support Yes|  Full support 15|  Full support 45|  Full support
Yes|  No support No  
  
The "Chrome incompatibilities" section is included from [
https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Chrome_incompatibilities](https://developer.mozilla.org/en-
US/Add-ons/WebExtensions/Chrome_incompatibilities) using the
[WebExtChromeCompat](/en-US/docs/Template:WebExtChromeCompat) macro.

If you need to update this content, edit <https://developer.mozilla.org/en-US
/Add-ons/WebExtensions/Chrome_incompatibilities>, then shift-refresh this page
to see your changes.

## Example extensions

  * [bookmark-it](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)

**Acknowledgements**

This API is based on Chromium's
[`chrome.bookmarks`](https://developer.chrome.com/extensions/bookmarks) API.
This documentation is derived from
[`bookmarks.json`](https://chromium.googlesource.com/chromium/src/+/master/chrome/common/extensions/api/bookmarks.json)
in the Chromium code.

Microsoft Edge compatibility data is supplied by Microsoft Corporation and is
included here under the Creative Commons Attribution 3.0 United States
License.

    
    
    // Copyright 2015 The Chromium Authors. All rights reserved.
    //
    // Redistribution and use in source and binary forms, with or without
    // modification, are permitted provided that the following conditions are
    // met:
    //
    //    * Redistributions of source code must retain the above copyright
    // notice, this list of conditions and the following disclaimer.
    //    * Redistributions in binary form must reproduce the above
    // copyright notice, this list of conditions and the following disclaimer
    // in the documentation and/or other materials provided with the
    // distribution.
    //    * Neither the name of Google Inc. nor the names of its
    // contributors may be used to endorse or promote products derived from
    // this software without specific prior written permission.
    //
    // THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    // "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    // LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    // A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    // OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    // SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    // LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    // DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    // THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    // (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    // OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
  *[
Full support

]: Full support

  *[
No support

]: No support

  *[Edge __]: Edge
  *[Opera __]: Opera
  *[Firefox for Android __]: Firefox for Android
  *[Desktop __]: Desktop
  *[
Partial support

]: Partial support

  *[Mobile __]: Mobile
  *[Firefox __]: Firefox
  *[
 Partial support

]: Partial support

  *[Chrome __]: Chrome

