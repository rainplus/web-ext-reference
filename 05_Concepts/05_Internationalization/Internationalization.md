[\n

\n

The [WebExtensions](/en-US/docs/Mozilla/Add-ons/WebExtensions) API has a
rather handy module available for internationalizing extensions \u2014 [i18n
](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n). In this article we'll
explore its features and provide a practical example of how it works. The i18n
system for extensions built using WebExtension APIs is similar to common
JavaScript libraries for i18n such as [i18n.js](http://i18njs.com/).

\n

\n

The example extension featured in this article \u2014 [notify-link-clicks-
i18n](https://github.com/mdn/webextensions-examples/tree/master/notify-link-
clicks-i18n) \u2014 is available on GitHub. Follow along with the source code
as you go through the sections below.

\n

\n

## Anatomy of an internationalized extension

\n

An internationalized extension can contain the same features as any other
extension \u2014 [background scripts](/en-US/Add-
ons/WebExtensions/Anatomy_of_a_WebExtension#Background_scripts), [content
scripts](/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts), etc.
\u2014 but it also has some extra parts to allow it to switch between
different locales. These are summarized in the following directory tree:

\n

\n

  * extension-root-directory/\n \n
    * _locales\n \n
      * en\n \n
        * messages.json\n \n
          * English messages (strings)
\n\n

\n\n

\n

      * de\n \n
        * messages.json\n \n
          * German messages (strings)
\n\n

\n\n

\n

      * etc.
\n\n

\n

    * manifest.json\n \n
      * locale-dependent metadata
\n\n

\n

    * myJavascript.js\n \n
      * JavaScript for retrieving browser locale, locale-specific messages, etc.
\n\n

\n

    * myStyles.css\n \n
      * locale-dependent CSS
\n\n

\n\n

\n

\n

Let's explore each of the new features in turn \u2014 each of the below
sections represents a step to follow when internationalizing your extension.

\n

## Providing localized strings in _locales

\n

\n

You can look up language subtags using the _Find_ tool on the [Language subtag
lookup page](http://r12a.github.io/apps/subtags/). Note that you need to
search for the English name of the language.

\n

\n

Every i18n system requires the provision of strings translated into all the
different locales you want to support. In extensions, these are contained
within a directory called `_locales`, placed inside the extension root. Each
individual locale has its strings (referred to as messages) contained within a
file called `messages.json`, which is placed inside a subdirectory of
`_locales`, named using the language subtag for that locale's language.

\n

Note that if the subtag includes a basic language plus a regional variant,
then the language and variant are conventionally separated using a hyphen: for
example, "en-US". However, in the directories under `_locales`, **the
separator must be an underscore** : "en_US".

\n

So [for example, in our sample app](https://github.com/mdn/webextensions-
examples/tree/master/notify-link-clicks-i18n/_locales) we have directories for
"en" (English), "de" (German), "nl" (Dutch), and "ja" (Japanese). Each one of
these has a `messages.json` file inside it.

\n

Let's now look at the structure of one of these files
([_locales/en/messages.json](https://github.com/mdn/webextensions-
examples/blob/master/notify-link-clicks-i18n/_locales/en/messages.json)):

\n

    
    
    {\n  "extensionName": {\n    "message": "Notify link clicks i18n",\n    "description": "Name of the extension."\n  },\n\n  "extensionDescription": {\n    "message": "Shows a notification when the user clicks on links.",\n    "description": "Description of the extension."\n  },\n\n  "notificationTitle": {\n    "message": "Click notification",\n    "description": "Title of the click notification."\n  },\n\n  "notificationContent": {\n    "message": "You clicked $URL$.",\n    "description": "Tells the user which link they clicked.",\n    "placeholders": {\n\xa0\xa0\xa0\xa0\xa0 "url" : {\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 "content" : "$1",\n\xa0\xa0\xa0\xa0\xa0\xa0\xa0 "example" : "https://developer.mozilla.org"\n\xa0\xa0\xa0\xa0\xa0 }\n\xa0\xa0\xa0 }\n  }\n}

\n

This file is standard JSON \u2014 each one of its members is an object with a
name, which contains a `message` and a `description`. All of these items are
strings; `$URL$` is a placeholder, which is replaced with a substring at the
time the `notificationContent` member is called by the extension. You'll learn
how to do this in the Retrieving message strings from JavaScript section.

\n

\n

 **Note** : You can find much more information about the contents of
`messages.json` files in our [Locale-Specific Message reference](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/Locale-
Specific_Message_reference).

\n

\n

## Internationalizing manifest.json

\n

There are a couple of different tasks to carry out to internationalize your
manifest.json.

\n

### Retrieving localized strings in manifests

\n

Your [manifest.json](https://github.com/mdn/webextensions-examples/blob/master
/notify-link-clicks-i18n/manifest.json) includes strings that are displayed to
the user, such as the extension's name and description. If you
internationalize these strings and put the appropriate translations of them in
messages.json, then the correct translation of the string will be displayed to
the user, based on the current locale, like so.

\n

To internationalize strings, specify them like this:

\n

    
    
    "name": "__MSG_extensionName__",\n"description": "__MSG_extensionDescription__",

\n

Here, we are retrieving message strings dependant on the browser's locale,
rather than just including static strings.

\n

To call a message string like this, you need to specify it like this:

\n

\n

  1. Two underscores, followed by
\n

  2. The string "MSG", followed by
\n

  3. One underscore, followed by
\n

  4. The name of the message you want to call as defined in `messages.json`, followed by
\n

  5. Two underscores
\n

\n

    
    
     **__MSG_** + _messageName_ + **__**

\n

### Specifying a default locale

\n

Another field you should specify in your manifest.json is [default_locale
](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/default_locale):

\n

    
    
    "default_locale": "en"

\n

This specifies a default locale to use if the extension doesn't include a
localized string for the browser's current locale. Any message strings that
are not available in the browser locale are taken from the default locale
instead. There are some more details to be aware of in terms of how the
browser selects strings \u2014 see Localized string selection.

\n

## Locale-dependent CSS

\n

Note that you can also retrieve localized strings from CSS files in the
extension. For example, you might want to construct a locale-dependent CSS
rule, like this:

\n

    
    
    header {\n  background-image: url(../images/__MSG_extensionName__/header.png);\n}

\n

This is useful, although you might be better off handling such a situation
using Predefined messages.

\n

## Retrieving message strings from JavaScript

\n

So, you've got your message strings set up, and your manifest. Now you just
need to start calling your message strings from JavaScript so your extension
can talk the right language as much as possible. The actual [i18n API](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/i18n) is pretty simple, containing
just four main methods:

\n

\n

  * You'll probably use [`i18n.getMessage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getMessage "Gets the localized string for the specified message.") most often \u2014 this is the method you use to retrieve a specific language string, as mentioned above. We'll see specific usage examples of this below.
\n

  * The [`i18n.getAcceptLanguages()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getAcceptLanguages "The documentation about this has not yet been written; please consider contributing!") and [`i18n.getUILanguage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/getUILanguage "The documentation about this has not yet been written; please consider contributing!") methods could be used if you needed to customize the UI depending on the locale \u2014 perhaps you might want to show preferences specific to the users' preferred languages higher up in a prefs list, or display cultural information relevant only to a certain language, or format displayed dates appropriately according to the browser locale.
\n

  * The [`i18n.detectLanguage()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n/detectLanguage "Detects the language of the provided text using the Compact Language Detector \(CLD\).") method could be used to detect the language of user-submitted content, and format it appropriately.
\n

\n

In our [notify-link-clicks-i18n](https://github.com/mdn/webextensions-
examples/tree/master/notify-link-clicks-i18n) example, the[ background
script](https://github.com/mdn/webextensions-examples/blob/master/notify-link-
clicks-i18n/background-script.js) contains the following lines:

\n

    
    
    var title = browser.i18n.getMessage("notificationTitle");\nvar content = browser.i18n.getMessage("notificationContent", message.url);

\n

The first one just retrieves the `notificationTitle message` field from the
available `messages.json` file most appropriate for the browser's current
locale. The second one is similar, but it is being passed a URL as a second
parameter. What gives? This is how you specify the content to replace the
`$URL$` placeholder we see in the\xa0`notificationContent message` field:

\n

    
    
    "notificationContent": {\n  "message": "You clicked $URL$.",\n  "description": "Tells the user which link they clicked.",\n  "placeholders": {\n    "url" : {\n      "content" : "$1",\n      "example" : "https://developer.mozilla.org"\n    }\n  }\n}\n

\n

The `"placeholders"` member defines all the placeholders, and where they are
retrieved from. The `"url"` placeholder specifies that its content is taken
from $1, which is the first value given inside the second parameter of
`getMessage()`. Since the placeholder is called `"url"`, we use `$URL$` to
call it inside the actual message string (so for `"name"` you'd use `$NAME$`,
etc.) If you have multiple placeholders, you can provide them inside an array
that is given to [`i18n.getMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/i18n/getMessage "Gets the localized string for the
specified message.") as the second parameter \u2014 `[a, b, c]` will be
available as `$1`, `$2`, and `$3`, and so on, inside `messages.json`.

\n

Let's run through an example: the original\xa0`notificationContent` message
string in the `en/messages.json` file is

\n

    
    
    You clicked $URL$.

\n

Let's say the link clicked on points to `https://developer.mozilla.org`. After
the [`i18n.getMessage()`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/i18n/getMessage "Gets the localized string for the
specified message.") call, the contents of the second parameter are made
available in messages.json as `$1`, which replaces the `$URL$` placeholder as
defined in the `"url"` placeholder. So the final message string is

\n

    
    
    You clicked https://developer.mozilla.org.

\n

### Direct placeholder usage

\n

It is possible to insert your variables (`$1`, `$2`, `$3`, etc.) directly into
the message strings, for example we could rewrite the above
`"notificationContent"` member like this:

\n

    
    
    "notificationContent": {\n  "message": "You clicked $1.",\n  "description": "Tells the user which link they clicked."\n}

\n

This may seem quicker and less complex, but the other way (using
`"placeholders"`) is seen as best practice. This is because having the
placeholder name (e.g. `"url"`) and example helps you to remember what the
placeholder is for \u2014 a week after you write your code, you'll probably
forget what `$1`\u2013`$8` refer to, but you'll be more likely to know what
your placeholder names refer to.

\n

### Hardcoded substitution

\n

It is also possible to include hardcoded strings in placeholders, so that the
same value is used every time, instead of getting the value from a variable in
your code. For example:

\n

    
    
    "mdn_banner": {\n  "message": "For more information on web technologies, go to $MDN$.",\n  "description": "Tell the user about MDN",\n  "placeholders": {\n    "mdn": {\n      "content": "https://developer.mozilla.org/"\n    }\n  }\n}

\n

In this case we are just hardcoding the placeholder content, rather than
getting it from a variable value like `$1`. This can sometimes be useful when
your message file is very complex, and you want to split up different values
to make the strings more readable in the file, plus then these values could be
accessed programmatically.

\n

In addition, you can use such substitutions to specify parts of the string
that you don't want to be translated, such as person or business names.

\n

## Localized string selection

\n

Locales can be specified using only a language code, like `fr` or `en`, or
they may be further qualified with a region code, like `en_US` or `en_GB`,
which describes a regional variant of the same basic language. When you ask
the i18n system for a string, it will select a string using the following
algorithm:

\n

\n

  1. if there is a `messages.json` file for the exact current locale, and it contains the string, return it.
\n

  2. Otherwise, if the current locale is qualified with a region (e.g. `en_US`) and there is a `messages.json` file for the regionless version of that locale (e.g. `en`), and that file contains the string, return it.
\n

  3. Otherwise, if there is a `messages.json` file for the `default_locale` defined in the `manifest.json`, and it contains the string, return it.
\n

  4. Otherwise return an empty string.
\n

\n

Take the following example:

\n

\n

  * extension-root-directory/\n \n
    * _locales\n \n
      * en_GB\n \n
        * messages.json\n \n
          * `{ "colorLocalised": { "message": "colour", "description": "Color." }, ... }`
\n\n

\n\n en\n\n \n

        * messages.json\n \n
          * `{ "colorLocalised": { "message": "color", "description": "Color." }, ... }`
\n\n

\n\n

\n

      * fr\n \n
        * messages.json\n \n
          * `{ "colorLocalised": { "message": "couleur", "description": "Color." }, ...}`
\n\n

\n\n

\n\n

\n\n

\n

\n

Suppose the `default_locale` is set to `fr`, and the browser's current locale
is `en_GB`:

\n

\n

  * If the extension calls `getMessage("colorLocalised")`, it will return "colour".
\n

  * If "colorLocalised" were not present in `en_GB`, then `getMessage("colorLocalised")`, would return "color", not "couleur".
\n

\n

## Predefined messages

\n

The i18n module provides us with some predefined messages, which we can call
in the same way as we saw earlier in Calling message strings from manifests
and extension CSS. For example:

\n

    
    
    __MSG_extensionName__

\n

Predefined messages use exactly the same syntax, except with `@@` before the
message name, for example

\n

    
    
    __MSG_@@ui_locale__

\n

The following table shows the different available predefined messages:

\n\n\n\nMessage name\n| Description\n  
---|---  
\n\n\n\n`@@extension_id`\n| \n

The extension's internally-generated UUID. You might use this string to
construct URLs for resources inside the extension. Even unlocalized extensions
can use this message.

\n

You can't use this message in a manifest file.

\n

Also note that this ID is _not_ the add-on ID returned by [`runtime.id`](/en-
US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/id "The ID of the
extension."), and that can be set using the [applications](/en-US/docs/Mozilla
/Add-ons/WebExtensions/manifest.json/applications) key in manifest.json. It's
the generated UUID that appears in the add-on's URL. This means that you can't
use this value as the `extensionId` parameter to [`runtime.sendMessage
()`](/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/sendMessage "Sends
a single message to event listeners within your extension or a different
extension."), and can't use it to check against the `id` property of a
[`runtime.MessageSender`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/MessageSender "An object containing information
about the sender of a message or connection request; this is passed to the
runtime.onMessage\(\) listener.") object.

\n\n  
\n\n`@@ui_locale`\n| The current locale; you might use this string to
construct locale-specific URLs.\n  
\n\n`@@bidi_dir`\n| The text direction for the current locale, either "ltr"
for left-to-right languages such as English or "rtl" for right-to-left
languages such as Arabic.\n  
\n\n`@@bidi_reversed_dir`\n| If the `@@bidi_dir` is "ltr", then this is "rtl";
otherwise, it's "ltr".\n  
\n\n`@@bidi_start_edge`\n| If the `@@bidi_dir` is "ltr", then this is "left";
otherwise, it's "right".\n  
\n\n`@@bidi_end_edge`\n| If the `@@bidi_dir` is "ltr", then this is "right";
otherwise, it's "left".\n  
\n\n\n

Going back to our earlier example, it would make more sense to write it like
this:

\n

    
    
    header {\n  background-image: url(../images/__MSG_@@ui_locale__/header.png);\n}

\n

Now we can just store our local specific images in directories that match the
different locales we are supporting \u2014 en, de, etc. \u2014 which makes a
lot more sense.

\n

Let's look at an example of using `@@bidi_*` messages in a CSS file:

\n

    
    
    body {\n  direction: __MSG_@@bidi_dir__;\n}\n      \ndiv#header {\n  margin-bottom: 1.05em;\n  overflow: hidden;\n  padding-bottom: 1.5em;\n  padding-__MSG_@@bidi_start_edge__: 0;\n  padding-__MSG_@@bidi_end_edge__: 1.5em;\n  position: relative;\n}

\n

For left-to-right languages such as English, the CSS declarations involving
the predefined messages above would translate to the following final code
lines:

\n

    
    
    direction: ltr;\npadding-left: 0;\npadding-right: 1.5em;\n

\n

For a right-to-left language like Arabic, you'd get:

\n

    
    
    direction: rtl;\npadding-right: 0;\npadding-left: 1.5em;

\n

## Testing out your extension

\n

Starting in Firefox 45, you can install extensions temporarily from disk
\u2014 see [Loading from disk](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Packaging_and_installation#Loading_from_disk). Do this, and
then try testing out our [notify-link-clicks-i18n](https://github.com/mdn
/webextensions-examples/tree/master/notify-link-clicks-i18n) extension. Go to
one of your favourite websites and click a link to see if a notification
appears reporting the URL of the clicked link.

\n

Next, change Firefox's locale to one supported in the extension that you want
to test.

\n

\n

  1. Open "about:config" in Firefox, and search for the `general.useragent.locale` preference.
\n

  2. Double click on the preference (or press Return/Enter) to select it, enter the language code for the locale you want to test, then click "OK" (or press Return/Enter). For example in our example extension, "en" (English), "de" (German), "nl" (Dutch), and "ja" (Japanese) are supported.
\n

  3. Search for `intl.locale.matchOS` and double click the preference so that it is set to `false`.
\n

  4. Restart your browser to complete the change.
\n

\n

\n

 **Note** : This works to change the browser's locale, even if you haven't got
the [language pack](https://addons.mozilla.org/en-US/firefox/language-tools/)
installed for that language. You'll just get the browser UI in your default
language if this is the case.

\n

\n

\n

\n

Load the extension temporarily from disk again, then test your new locale:

\n

\n

  * Visit "about:addons" again \u2014 you should now see the extension listed, with its icon, plus name and description in the chosen language.
\n

  * Test your extension again. In our example, you'd go to another website and click a link, to see if the notification now appears in the chosen language.
\n

\n

\n]

