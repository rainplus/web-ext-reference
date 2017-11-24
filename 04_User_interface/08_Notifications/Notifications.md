[





Notifications allow you to communicate information about your extension or its
content using the underlying operating system's notification service:



![](https://mdn.mozillademos.org/files/14043/notify-shadowed.png)



Notifications can include a call to action for the user, and your add-on can
listen for the user clicking the notification or the notification closing.



## Specifying notifications



You manage notifications programmatically, using the [`notifications`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/notifications "Display notifications
to the user, using the underlying operating system's notification mechanism.
Because this API uses the operating system's notification mechanism, the
details of how notifications appear and behave may differ according to the
operating system and the user's settings.") API. To use this API you must
request the `notifications` permission in your manifest.json:



    
    
    "permissions": ["notifications"]



You then use [`notifications.create`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/notifications/create "Creates and displays a
notification.") to create your notifications, as in this example from [notify-
link-clicks-i18n:](https://github.com/mdn/webextensions-examples/tree/master
/notify-link-clicks-i18n)



    
    
    var title = browser.i18n.getMessage("notificationTitle");var content = browser.i18n.getMessage("notificationContent", message.url);browser.notifications.create({  "type": "basic",  "iconUrl": browser.extension.getURL("icons/link-48.png"),  "title": title,  "message": content});



This code creates a notification with an icon, title, and message.



If the notification includes a call to action, you can listen for the user
clicking the notification to call the function to handle the action:



    
    
    browser.notifications.onClicked.addListener(handleClick);



If you are issuing calls to action through notifications, you will also want
to define the optional notification `id`, so you can figure out which call to
action the user has selected.



## Examples



The [webextensions-examples](https://github.com/mdn/webextensions-examples)
repo on GitHub, contains several examples of extensions that use the creates
notifications:





  * [notify-link-clicks-i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-clicks-i18n) uses the creates notifications.




]

