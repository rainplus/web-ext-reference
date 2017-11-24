[\n

\n

web-ext is a command line tool designed to speed up various parts of the
extension development process, making development faster and easier. This
article explains how to install and use web-ext.

\n

## Installation

\n

web-ext is a node-based application that you can install with the
[nodejs/npm](https://nodejs.org/) tool. Install web-ext using the following
command:

\n

    
    
    npm install --global web-ext

\n

web-ext requires the current [LTS](https://github.com/nodejs/LTS) (long term
support) version of [NodeJS](https://nodejs.org/).

\n

You can test whether your installation worked by running the following
command, which lists the installed web-ext version number:

\n

    
    
    web-ext --version

\n

## Using web-ext

\n

Once you've installed it, you can test web-ext out. At this point, it is a
good idea to have a sample extension to try it out on \u2014 if you don't have
one of your own, you can clone our [webextensions-
examples](https://github.com/mdn/webextensions-examples) repo.

\n

### Testing out an extension

\n

You can test an extension in Firefox by `cd`'ing into your extension's root
directory and entering the following command:

\n

    
    
    web-ext run

\n

This will start up Firefox and load the extension temporarily in the browser,
just like you could on the [about:debugging page](/en-
US/docs/Tools/about:debugging#Add-ons).

\n

See the [run reference guide](/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_run) to learn about all available options.

\n

### Automatic extension reloading

\n

The `run` command will watch your source files and tell Firefox to reload the
extension after you edit and save a file. For example, if you changed the
`name` property in your `manifest.json` file, Firefox would display the new
name. This makes it easy to try out new features and see them immediately. The
automatic reloading feature is active by default so you can use it like this:

\n

    
    
    web-ext run

\n

You can also press the `r` key from the `web-ext` terminal to trigger an
extension reload manually.

\n

If you experience unexpected behavior with the reloading feature, please [file
a bug](https://github.com/mozilla/web-ext/issues). You can also disable
reloading like this:

\n

    
    
    web-ext run --no-reload

\n

\n

Extension reloading is only supported in Firefox 49 or higher.

\n

\n

### Testing in different versions of Firefox

\n

To run your extension in a version of Firefox other than the default, use the
`--firefox` option to specify a full path to the binary file. Here is an
example on Mac OS:

\n

    
    
    web-ext run --firefox=/Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin

\n

On Windows, the path needs to include the `firefox.exe` part, for example:

\n

    
    
    web-ext run --firefox="C:\\Program Files\\Mozilla Firefox\\firefox.exe"

\n

### Testing in Firefox 48

\n

Firefox 48 was the first stable version to use the WebExtension platform but
it doesn't allow `web-ext` to install an extension remotely. You need to run
your extension in Firefox 48 with a different installation option:

\n

    
    
    web-ext run --pre-install

\n

### Testing unsigned extensions

\n

When you execute [web-ext run](/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_run), the extension gets installed temporarily
until you close Firefox. This does not violate any signing restrictions. If
instead you create a zip file with [web-ext build](/en-US/Add-
ons/WebExtensions/web-ext_command_reference#web-ext_build) and try to install
it into Firefox, you will see an error telling you that the add-on is not
signed. You will need to use an [unbranded
build](https://wiki.mozilla.org/Addons/Extension_Signing#Unbranded_Builds) or
use a [development build](https://www.mozilla.org/en-US/firefox/developer/) to
install unsigned extensions.

\n

### Using a custom profile

\n

By default, the `run` command will create a temporary Firefox profile. You can
run your extension with a specific profile using the `--firefox-profile`
option, like this:

\n

    
    
    web-ext run --firefox-profile=your-custom-profile

\n

This option accepts a string containing the name of your profile or an
absolute path to the profile directory. This may be helpful if you want to
manually configure some settings that will always available to the `run`
command.

\n

### Keeping profile changes

\n

The `run` command will not save any changes made to the custom profile
specified by `--firefox-profile`. To keep changes, add this option:

\n

    
    
    web-ext run --keep-profile-changes --firefox-profile=your-custom-profile

\n

This may be helpful if your extension has many different run states.

\n

\n

This option makes the profile specified by `--firefox-profile` completely
insecure for daily usage. It turns off auto-updates and allows silent remote
connections, among other things. Specifically, it will make destructive
changes to the profile that are required for `web-ext` to operate.

\n

\n

### Packaging your extension

\n

Once you've tested your extension and verified that it's working, you can turn
it into a package for submitting to
[addons.mozilla.org](https://addons.mozilla.org) using the following command:

\n

    
    
    web-ext build

\n

This will output a full path to the generated `.zip` file that can be loaded
into a browser.

\n

\n

The generated `.zip` file doesn't work on Firefox without signing it, or
adding `[applications](/en-US/Add-
ons/WebExtensions/manifest.json/applications).gecko.id` key into
`[manifest.json](/en-US/Add-ons/WebExtensions/manifest.json)`.\xa0 For more
information, please refer [WebExtensions and the Add-on
ID](https://developer.mozilla.org/en-US/Add-ons/WebExtensions
/WebExtensions_and_the_Add-on_ID) page.

\n

\n

`web-ext build` is designed to automatically ignore files that are commonly
unwanted in packages, such as `.git`, `node_modules`, and other artifacts.

\n

See the [build reference guide](/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_build) to learn more.

\n

### Signing your extension for distribution

\n

As an alternative to publishing your extension on
[addons.mozilla.org](https://addons.mozilla.org/), you can self-host your
package file but it needs to be [signed by
Mozilla](https://developer.mozilla.org/Add-ons/Distribution) first. The
following command packages and signs a ZIP file, then returns it as a signed
XPI file for distribution:

\n

    
    
    web-ext sign --api-key=$AMO_JWT_ISSUER --api-secret=$AMO_JWT_SECRET 

\n

The API options are required to specify your [addons.mozilla.org
credentials](https://addons.mozilla.org/en-US/developers/addon/api/key/).

\n

\n

  * `--api-key`: the API key (JWT issuer) from `addons.mozilla.org` needed to sign the extension. This should always be a string.
\n

  * `--api-secret`: the API secret (JWT secret) from `addons.mozilla.org` needed to sign the extension. This should always be a string.
\n

\n

See the [sign reference guide](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/web-ext_command_reference#web-ext_sign) to learn about all
available options.

\n

### Signing extensions without an explicit ID

\n

`web-ext` fully supports signing extensions that do not declare the
[applications.gecko.id](/en-US/Add-
ons/WebExtensions/manifest.json/applications) property in their manifest. The
first time you sign an extension without an explicit ID,
[addons.mozilla.org](https://addons.mozilla.org/) will auto-generate an ID and
`web-ext` will save it to `.web-extension-id` in the current working
directory. You should save the ID file so that you can sign future versions of
the same extension. If you lose the ID file, you will have to add back the
`applications.gecko.id` property or use the `--id` option when signing future
versions, for example:

\n

    
    
    web-ext sign --api-key=... --api-secret=... --id="{c23c69a7-f889-447c-9d6b-7694be8035bc}"

\n

### Signing in a restricted environment

\n

If you are working in an environment that restricts access to certain domains,
you can try using a proxy when signing:

\n

    
    
    web-ext sign --api-key=... --api-secret=... --api-proxy=https://yourproxy:6000

\n

See the [\--api-proxy](/en-US/Add-ons/WebExtensions/web-ext_command_reference
#--api-proxy) to learn more.

\n

If you simply need to allow the domains used for signing and downloading
files, allow these:

\n

\n

  * addons.mozilla.org
\n

  * addons.cdn.mozilla.net
\n

\n

### Checking for code "lint"

\n

Before trying out your extension with the [run](/en-US/Add-ons/WebExtensions
/web-ext_command_reference#web-ext_run) command or submitting your package to
[addons.mozilla.org](https://addons.mozilla.org/en-US/firefox/), you can use
the `lint` command to make sure your [manifest](/en-US/Add-
ons/WebExtensions/manifest.json) and other source files do not contain any
errors. Example:

\n

    
    
    web-ext lint

\n

This uses the [addons-linter](https://github.com/mozilla/addons-linter)
library to walk through your source code directory and report any errors, such
as the declaration of an unknown permission.

\n

See the [lint reference guide](/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_lint) to learn about all available options.

\n

### Specifying different source and destination directories

\n

The above commands all use default directories for the extension source and
artifact creation (e.g. built `.zip` files). The defaults are:

\n

\n

  * Source: The directory you are currently inside.
\n

  * Artifacts: A directory called `./web-ext-artifacts`, created inside the current directory.
\n

\n

You can specify different source and destination directories using the
`--source-dir` (or `-s` alias) and `--artifacts-dir` (or `-a` alias) options
when running your commands. Their values can be relative or absolute paths,
but must always be specified as strings. Here is an example of specifying both
options at the same time when\xa0 building an extension:

\n

    
    
    web-ext build --source-dir=webextension-examples/notify-link-clicks-i18n --artifacts-dir=zips

\n

### Outputting verbose messages

\n

If you want to see exactly what web-ext is doing when you run a command, you
can include the `--verbose` option (or the `-v` alias). For example:

\n

    
    
    web-ext build --verbose

\n

### Viewing all commands and options

\n

You can list all commands and options like this:

\n

    
    
    web-ext --help

\n

\n

 **Note** : You can also use the `-h` alias.

\n

\n

You can list options for a specific command by adding it as an argument:

\n

    
    
    web-ext --help run

\n

### Detecting temporary installation

\n

Your extension can detect whether it was installed using "web-ext run" rather
than as a built and signed extension downloaded from addons.mozilla.org.
Listen for the [`runtime.onInstalled`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/onInstalled "Fired when the extension is first
installed, when the extension is updated to a new version, and when the
browser is updated to a new version.") event, and check the value of
`details.temporary`.

\n

## See also

\n

\n

  * [web-ext repo](https://github.com/mozilla/web-ext)
\n

  * \n

[web-ext command reference](/en-US/docs/Mozilla/Add-ons/WebExtensions/web-
ext_command_reference)

\n

\n

\n]

