[\n

\n

Toolbar buttons are one of the main UI components available to extensions.
Toolbar buttons live in the main browser toolbar and contain an icon. When the
user clicks the icon, one of two things can happen:

\n

\n

  * If you have specified a popup for the icon, the popup is shown. Popups are transient dialogs specified using HTML, CSS, and JavaScript.
\n

  * If you have not specified a popup, a click event is generated, which you can listen for in your code and perform some other kind of action in response to.
\n

\n

With WebExtension APIs, these kinds of buttons are called "browser actions",
and are set up like so:

\n

\n

  * The manifest.json key `[browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)` is used to define the button.
\n

  * The JavaScript API `[browserAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)` is used to listen for clicks and change the button or perform actions via your code.
\n

\n

## A simple button

\n

In this section we'll create an extension that adds a button to the toolbar.
When the user clicks the button, we'll open <https://developer.mozilla.org> in
a new tab.

\n

First, create a new directory, "button", and create a file called
"manifest.json" inside it with the following contents:

\n

    
    
    {\n\n  "description": "Demonstrating toolbar buttons",\n  "manifest_version": 2,\n  "name": "button-demo",\n  "version": "1.0",\n\n  "background": {\n    "scripts": ["background.js"]\n  },\n \n  "browser_action": {\n    "default_icon": {\n      "16": "icons/page-16.png",\n      "32": "icons/page-32.png"\n    }\n  }\n\n}

\n

This specifies that we'll have a [background script](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts) named
"background.js", and a browser action (button) whose icons will live in the
"icons" directory.

\n

\n

These icons are from the
[bitsies!](https://www.iconfinder.com/iconsets/bitsies) iconset created by
Recep K\xfct\xfck.

\n

\n

Next, create the "icons" directory inside the "buttons" directory, and save
the two icons shown below inside it:

\n

\n

  * "page-16.png" (![](https://mdn.mozillademos.org/files/13476/page-16.png))
\n

  * "page-32.png" (![](https://mdn.mozillademos.org/files/13478/page-32.png)).
\n

\n

\xa0

\n

We have two icons so we can use the bigger one in high-density displays. The
browser will take care of selecting the best icon for the current display.

\n

Next, create "background.js" in the extension's root directory, and give it
the following contents:

\n

    
    
    function openPage() {\n  browser.tabs.create({\n    url: "https://developer.mozilla.org"\n  });\n}\n\nbrowser.browserAction.onClicked.addListener(openPage);

\n

This listens for the browser action's click event; when the event fires, the
`openPage()` function is run, which opens the specified page using the `[tabs
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs)` API.

\n

At this point the complete extension should look like this:

\n

    
    
    button/\n    icons/\n        page-16.png\n        page-32.png\n    background.js\n    manifest.json

\n

Now [install the extension](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Temporary_Installation_in_Firefox) and click the button:

\n

\n

## Adding a popup

\n

Let's try adding a popup to the button. Replace manifest.json with this:

\n

    
    
    {\n\n  "description": "Demonstrating toolbar buttons",\n  "manifest_version": 2,\n  "name": "button-demo",\n  "version": "1.0",\n \n  "browser_action": {\n    "browser_style": true,\n    "default_popup": "popup/choose_page.html",\n    "default_icon": {\n      "16": "icons/page-16.png",\n      "32": "icons/page-32.png"\n    }\n  }\n\n}

\n

We've made three changes from the original:

\n

\n

  * We no longer reference "background.js", because now we're going to handle the extension's logic in the popup's script (you are allowed background.js as well as a popup, it's just that we don't need it in this case).
\n

  * We've added `"browser_style": true`, which will help the styling of our popup look more like part of the browser.
\n

  * Finally, we've added `"default_popup": "popup/choose_page.html"`, which is telling the browser that this browser action is now going to display a popup when clicked, the document for which can be found at "popup/choose_page.html".
\n

\n

So now we need to create that popup. Create a directory called "popup" then
create a file called "choose_page.html" inside it. Give it the following
contents:

\n

    
    
    <!DOCTYPE html>\n\n<html>\n  <head>\n    <meta charset="utf-8">\n    <link rel="stylesheet" href="choose_page.css"/>\n  </head>\n\n<body>\n  <div class="page-choice">developer.mozilla.org</div>\n  <div class="page-choice">support.mozilla.org</div>\n  <div class="page-choice">addons.mozilla.org</div>\n  <script src="choose_page.js"></script>\n</body>\n\n</html>

\n

You can see that this is a normal HTML page containing three [`<div>`](/en-
US/docs/Web/HTML/Element/div "The HTML <div> element is the generic container
for flow content and does not inherently represent anything. Use it to group
elements for purposes such as styling \(using the class or id attributes\),
marking a section of a document in a different language \(using the lang
attribute\), and so on.") elements, each with the name of a Mozilla site
inside. It also includes a CSS file and a JavaScript file, which we'll add
next.

\n

Create a file called "choose_page.css" inside the "popup" directory, and give
it these contents:

\n

    
    
    html, body {\n  width: 300px;\n}\n\n.page-choice {\n  width: 100%;\n  padding: 4px;\n  font-size: 1.5em;\n  text-align: center;\n  cursor: pointer;\n}\n\n.page-choice:hover {\n  background-color: #CFF2F2;\n}

\n

This is just a bit of styling for our popup.

\n

Next, create a "choose_page.js" file inside the "popup" directory, and give it
these contents:

\n

    
    
    document.addEventListener("click", function(e) {\n  if (!e.target.classList.contains("page-choice")) {\n    return;\n  }\n\n  var chosenPage = "https://" + e.target.textContent;\n  browser.tabs.create({\n    url: chosenPage\n  });\n\n});

\n

In our JavaScript, we listen for clicks on the popup choices. We first check
to see if the click landed on one of the page-choices; if not, we don't do
anything else. If the click did land on a page-choice, we construct a URL from
it, and open a new tab containing the corresponding page. Note that we can use
WebExtension APIs in popup scripts, just as we can in background scripts.

\n

The extension's final structure should look like this:

\n

    
    
    button/\n    icons/\n        page-16.png\n        page-32.png\n    popup/\n        choose_page.css\n        choose_page.html\n        choose_page.js\n    manifest.json

\n

Now reload the extension, click the button again, and try clicking on the
choices in the popup:

\n

\n

## Page actions

\n

[Page actions](/en-US/docs/Mozilla/Add-ons/WebExtensions/Page_actions) are
just like browser actions, except that they are for actions which are relevant
only for particular pages, rather than the browser as a whole.

\n

While browser actions are always shown, page actions are only shown in tabs
where they are relevant. Page action buttons are displayed in the URL bar,
rather than the browser toolbar.

\n

## Learn more

\n

\n

  * `[browser_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action)` manifest key
\n

  * `[browserAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction)` API
\n

  * Browser action examples:\n \n
    * [beastify](https://github.com/mdn/webextensions-examples/tree/master/beastify)
\n

    * [Bookmark it!](https://github.com/mdn/webextensions-examples/tree/master/bookmark-it)
\n

    * [favourite-colour](https://github.com/mdn/webextensions-examples/tree/master/favourite-colour)
\n

    * [inpage-toolbar-ui](https://github.com/mdn/webextensions-examples/tree/master/inpage-toolbar-ui)
\n

    * [open-my-page-button](https://github.com/mdn/webextensions-examples/tree/master/open-my-page-button)
\n\n

\n

  * `[page_action](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/page_action)` manifest key
\n

  * `[pageAction](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pageAction)` API
\n

  * Page action examples:\n \n
    * [chill-out](https://github.com/mdn/webextensions-examples/tree/master/chill-out)
\n\n

\n

\n]

