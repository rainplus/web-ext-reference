The techniques described here work in Firefox 50 and later. If you need to use
an earlier version of Firefox, please refer to the article on [debugging
extensions using WebExtension APIs before Firefox 50](/en-US/Add-
ons/WebExtensions/Debugging_\(before_Firefox_50\)).

This article explains how you can use the Firefox developer tools to debug
extensions built with WebExtension APIs.

An extension can consist of various different pieces — background scripts,
popups, options pages, content scripts, sidebars — and you'll need to use a
slightly different workflow to debug each piece. So each piece gets a top-
level section in this article, and the intention is that these sections can be
read in isolation. We'll begin by introducing the Add-on Debugger, which
you'll use to debug most of the pieces of your extension.

## The Add-on Debugger

For most of this article we'll use the Add-on Debugger. To open the Add-on
Debugger:

  * open Firefox
  * enter "about:debugging" in the URL bar
  * check the box labelled "Enable add-on debugging"
  * click the "Debug" button next to your extension
  * click "OK" in the warning dialog.

You'll then see a new window open. The main Firefox window will be switched
into the foreground, so you'll have to click on the new window to bring it in
front.

This new window is sometimes called a "toolbox" and contains the debugging
tools we'll use. It has a tabbed interface: the row of tabs along the top lets
you switch between the different tools:

![](https://mdn.mozillademos.org/files/13861/toolbox-tabs.png)

In this article we'll use three debugging tools:

  * [The Console](/en-US/docs/Tools/Web_Console): this displays messages logged by the extension as well as error messages logged by the browser as it runs the extension. It also provides a command line enabling you to execute JavaScript in the extension's context.
  * [The Debugger](/en-US/docs/Tools/Debugger): this enables you to set breakpoints and watchpoints in your extension's JavaScript, and examine and modify its internal state.
  * [The Inspector](/en-US/docs/Tools/Page_Inspector): this enables you to examine and modify the HTML and CSS used to build your extension's pages.

## Debugging background scripts

The examples in this section use the "notify-link-clicks-l10n" example
extension. If you'd like to play along, you can find this example in the
[webextensions-examples](https://github.com/mdn/webextensions-examples)
repository.

[Background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts) stay loaded
for the lifetime of the extension. They're loaded inside an invisible
"background page": by default this is an empty HTML document, but you can
specify your own HTML content using the ["background" key in "manifest.json
"](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/background).

You can debug background scripts using the [Add-on Debugger](/en-US/Add-
ons/WebExtensions/Debugging_\(Firefox_50_onwards\)#The_Add-on_Debugger).

In the Add-on Debugger's Console you'll see logged output, including calls to
`[console.log()](/en-US/docs/Web/API/Console/log)` from your own background
scripts and any errors the browser raises as it executes them. Note that at
the moment, the console shows all errors raised by the browser, not just
errors related to your extensions code.

For example, the [notify-link-clicks-i18n](https://github.com/mdn
/webextensions-examples/tree/master/notify-link-clicks-i18n) example extension
logs a message from its background script when it receives a message from one
of its content scripts:

Using the Console's command line, you can access and modify the objects
created by your background scripts.

For example, here we call the `notify()` function defined in the extension's
background script:

If you switch to the Debugger, you'll see all your extension's background
scripts. You can set breakpoints, step through code, and do [everything else
you'd expect to be able to do in a debugger](https://developer.mozilla.org/en-
US/docs/Tools/Debugger).

If you press the Escape key while you're in the Debugger, the toolbox will be
split, with the bottom half now occupied by the Console. While you're at a
breakpoint, you can now modify the program's state using the console. See
[Split console](/en-US/docs/Tools/Web_Console/Split_console) for more on this.

## Debugging options pages

[Options pages](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Options_pages) are HTML pages that
the extension developer can supply, that contain options for the extension.
They are typically displayed in an iframe in the Add-ons Manager (to see the
Add-ons Manager, visit the "about:addons" page).

To debug options pages:

  * open the [Add-on Debugger](/en-US/Add-ons/WebExtensions/Debugging_\(Firefox_50_onwards\)#The_Add-on_Debugger) for your extension
  * open your extension's option page.

Any JavaScript sources it includes are then listed in the Debugger:

This video uses the [favourite-colour](https://github.com/mdn/webextensions-
examples/tree/master/favourite-colourbeastify) example extension.

You'll also see any messages logged by your code in the Add-on Debugger's
Console.

You can also use the Add-on Debugger to debug the page's HTML and CSS. First,
though, you need to point the tools at the iframe that hosts the options page.
To do this: open the options page, click the icon highlighted in the
screenshot below, and select the options page from the drop-down list:

![](https://mdn.mozillademos.org/files/13863/toolbox-iframe.png)Now switch to
the Inspector tab, and you'll be able to examine and edit HTML and CSS for the
page:

## Debugging popups

[Popups](/en-US/docs/Mozilla/Add-ons/WebExtensions/Popups) are dialogs that
are attached to browser actions or page actions. They are specified using an
HTML document that can include CSS and JavaScript sources for styling and
behavior. Whenever the popup is visible, you can use the [Add-on Debugger
](/en-US/Add-ons/WebExtensions/Debugging_\(Firefox_50_onwards\)#The_Add-
on_Debugger) to debug its code.

One problem with popups is that if a popup is open and you click outside the
popup, the popup is closed and its code is unloaded. This obviously makes them
impossible to debug. To suppress this behavior, click the button in the Add-on
Debugger that we've highlighted in the screenshot below:

![](https://mdn.mozillademos.org/files/13877/toolbox-popup.png)Now, when you
open a popup it will stay open until you press Escape.

Note that this change applies to built-in browser popups, like the Hamburger
menu (![](https://mdn.mozillademos.org/files/12712/hamburger.png)), as well as
extension popups.

Also note that the change is persistent, even across browser restarts. This
was fixed starting with Firefox 57 in [bug
1251658](https://bugzilla.mozilla.org/show_bug.cgi?id=1251658), in previous
versions you may prefer to re-enable autohide by clicking the button again
before you close the Browser Toolbox.

Internally, this button just toggles the `ui.popup.disable_autohide`
preference, which you can toggle manually using about:config.

When the popup is open, its JavaScript sources will be listed in the Debugger.
You can set breakpoints and modify the program's internal state:

This video uses the [beastify](https://github.com/mdn/webextensions-
examples/tree/master/beastify) example extension.

You can also use the Add-on Debugger to debug the popup's HTML and CSS. First,
though, you need to point the tools at the popup's document. To do this: open
the popup, then click the icon highlighted in the screenshot below and select
the popup's page from the drop-down
list:![](https://mdn.mozillademos.org/files/13863/toolbox-iframe.png)

Now switch to the Inspector, and you'll be able to examine and edit the
popup's HTML and CSS:

## Debugging content scripts

You can use the Add-on Debugger to debug background pages, options pages, and
popups. However, you can't use it to debug content scripts. This is because,
in [multiprocess Firefox](/en-US/docs/Mozilla/Firefox/Multiprocess_Firefox),
content scripts run in a different process from the other parts of your
extension.

To debug content scripts attached to a web page, use the normal web developer
tools for that page:

  * either select "Toggle Tools" from the Web Developer submenu in the Firefox Menu (or Tools menu if you display the menu bar or are on Mac OS X)
  * or press the CtrlShiftI (CommandOptionI on OS X) keyboard shortcut.

By default, the tools are shown attached to the bottom of browser tab, to
reflect the fact that they are attached to this tab. You'll see any output
from `[console.log()](/en-US/docs/Web/API/Console/log)` statements in your
content scripts. You will also see your content scripts listed in the
Debugger, where you'll be able to set breakpoints, step through the code, and
so on.

This video uses the [notify-link-clicks-i18n](https://github.com/mdn
/webextensions-examples/tree/master/notify-link-clicks-i18n) example
extension.

If the developer tools tab was not already open when the content script was
injected, sometimes the content script is not listed in the debugger panel. If
you experience this, reloading the page with the developer tools tab open
should fix the problem.

## Debugging sidebars

[Sidebars](/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Sidebars)
are HTML pages opened as a sidebar in the browser UI that the extension
developer can supply.

To debug sidebars:

  * open the [Add-on Debugger](/en-US/Add-ons/WebExtensions/Debugging_\(Firefox_50_onwards\)#The_Add-on_Debugger) for your extension
  * open your extension's sidebar.

Any JavaScript sources it includes are then listed in the Debugger.

You'll also see any messages logged by your code in the Add-on Debugger's
Console.

You can also use the Add-on Debugger to debug the page's HTML and CSS. First,
though, you need to point the tools at the iframe that hosts the options page.
To do this: open the sidebar, click the icon highlighted in the screenshot
below, and select the sidebar from the drop-down list:

![](https://mdn.mozillademos.org/files/13863/toolbox-iframe.png)

## Debugging developer tools pages & panels

[Developer tools](/en-US/Add-ons/WebExtensions/Extending_the_developer_tools)
are extended by loading a hidden HTML page when devtools are opened and
[developer tools panels](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/devtools.panels/create) are HTML pages displayed as a
developer tool in the browser UI that the extension developer can supply.

To debug the developer tools page:

  * open the [Add-on Debugger](/en-US/Add-ons/WebExtensions/Debugging_\(Firefox_50_onwards\)#The_Add-on_Debugger) for your extension
  * open the Web Developer Tools

To debug developer tools panels:

  * Follow the steps for the developer tools page above
  * Select your developer tools panel

Any JavaScript sources it includes are then listed in the Debugger.

You'll also see any messages logged by your code in the Add-on Debugger's
Console.

You can also use the Add-on Debugger to debug the page's HTML and CSS. First,
though, you need to point the tools at the iframe that hosts the options page.
To do this: open the sidebar, click the icon highlighted in the screenshot
below, and select the sidebar from the drop-down list:

![](https://mdn.mozillademos.org/files/13863/toolbox-iframe.png)

## Debugging Browser Restarts

If your extension is active in ways that might be affected by the browser
restarting, such as a session being restored, then you may want to do extra
testing to ensure your code works as expected in those conditions.

You can test your extension across browser restarts by following these steps:

  1. Create a new browser profile. This is optional, but recommended as you'll be disabling extension signing, which opens you up to malicious code installation, and also because your extension could affect your default profile in unexpected ways.
  2. Open your new browser profile in Firefox Developer Edition or Firefox Nightly. Those are the only two channels of Firefox that allow disabling extension signing. Unfortunately this means you cannot test your extension across restarts in a release version of Firefox.
  3. Type about:config into the location bar, hit Enter, and then use the search box on that page to find the "xpinstall.signatures.required" preference, and change it to "false".
  4. In your manifest.json file, add a new top-level key called "applications" with an object value containing a key called "gecko" with an object value that contains a key called "id", with a value of "a@b". It should look like: applications": {"gecko": {"id": "a@b"}}. You can change the values of "a" and "b" to whatever you like. Remember to remove the "applications" key from your manifest.json file once you're finished testing restarts.
  5. Package your extension with "web-ext build" and change the result file's extension to ".xpi"
  6. Open the .xpi file with Firefox with the File->Open menu. Your extension should now be installed, and you can restart the browser and it will still be there.

