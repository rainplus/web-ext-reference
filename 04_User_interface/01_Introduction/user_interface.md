[



Extensions that use WebExtension APIs are provided with several user interface
options so that their functionality can be made available to the user. A
summary of those options is provided below, with a more detailed introduction
to each user interface option in this section.





For advice on using these UI components to create a great user experience in
your extension, please see the [User experience best practices](/en-
US/docs/Mozilla/Add-ons/WebExtensions/User_experience_best_practices) article.



UI option| Description| Example  
---|---|---  
[Browser toolbar button](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_action)| A
button on the browser toolbar that dispatches an event to the extension when
clicked. By default, the button is visible in all tabs.| ![Example of a
WebExtension toolbar button](https://mdn.mozillademos.org/files/12966/browser-
action.png)  
Browser toolbar button with a [popup](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)| A popup on a
button in the browser toolbar that opens when the button is clicked. The popup
is defined in an HTML document that handles the user interaction.| ![Example
of a WebExtension toolbar button with a
popup](https://mdn.mozillademos.org/files/14039/popup-shadow.png)  
[Address bar button](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Page_actions)| A button on the browser
address bar that dispatches an event to the extension when clicked. By
default, the button is hidden in all tabs.| ![Example showing an address bar
button \(page
action\)](https://mdn.mozillademos.org/files/15047/address_bar_button.png)  
Address bar button with a [popup](https://developer.mozilla.org/en-
US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups)| A popup on a
button in the browser address bar that opens when the button is clicked. The
popup is defined in an HTML document that handles the user interaction.|
![Example of a popup on the address bar
button](https://mdn.mozillademos.org/files/15053/page_action_popup.png)  
[Context menu items](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Context_menu_items)| Menu items,
checkboxes, and radio buttons on one or more of the browser's context menus.
Also, menus can be structured by adding separators. When menu items are
clicked, an event is dispatched to the extension.|
![](https://mdn.mozillademos.org/files/15051/context_menu_example.png)  
[Sidebar](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Sidebars)| 

An HTML document displayed next to a web page, with the option for unique
content per page. The sidebar is opened when the extension is installed, then
obeys the user's sidebar visibility selection. User interaction within the
sidebar is handled by its HTML document.

| ![Example of a WebExtension's
sidebar](https://mdn.mozillademos.org/files/14825/bookmarks-sidebar.png)  
[Options page](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Options_pages)| A page that enables you to
define preferences for your extension that your users can change. The user can
access this page in the from the browser's add-ons manager.| ![Example
showing the options page content added in the favorite colors
example.](https://mdn.mozillademos.org/files/15055/options_page.png)  
[Bundled web pages](/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Bundled_web_pages)| Use web pages included
in your extension to provide forms, help, or any other content required,
within windows or tabs.| ![Example of a simple bundled page displayed as a
detached
panel.](https://mdn.mozillademos.org/files/15063/bundled_page_as_panel_small.png)  
[Notifications](https://developer.mozilla.org/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Notifications)| Transient notifications
displayed to the user through the underlying operating system's notifications
mechanism. Dispatches an event to the extension when the user clicks a
notification, or when a notification closes (either automatically or at the
user's request).| ![Example notification from a
WebExtension](https://mdn.mozillademos.org/files/14043/notify-shadowed.png)  
[Address bar suggestions](/en-US/docs/Mozilla/Add-
ons/WebExtensions/user_interface/Omnibox)| Offer custom address bar
suggestions when the user enters a keyword.| ![Example showing the result of
the firefox_code_search WebExtension's customization of the address bar
suggestions.](https://mdn.mozillademos.org/files/15059/omnibox_example_small.png)  
[Developer tools panels](https://developer.mozilla.org/en-US/docs/Mozilla
/Add-ons/WebExtensions/user_interface/devtools_panels)| A tab with an
associated HTML document that displays in the browser's developer tools.|
![New panel tab in the Developer Tools tab
bar](https://mdn.mozillademos.org/files/15049/developer_panel_tab.png)  


The following how-to guides provide step-by-step guidance to creating some of
these user interface options:





  * [Add a button to the toolbar](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Add_a_button_to_the_toolbar)


  * [Implement a settings page](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Implement_a_settings_page)


  * [Extending the developer tools](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Extending_the_developer_tools)


]

