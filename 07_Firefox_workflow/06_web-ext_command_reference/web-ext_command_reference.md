[\n

\n

This page lists all the commands and options available under the [web-
ext](https://github.com/mozilla/web-ext) command line tool.

\n

## Commands

\n

web-ext has the following commands available; options specific to these
commands are included as subsections.

\n

### web-ext build

\n

Packages an extension into a `.zip` file, ignoring files that are commonly
unwanted in packages, such as `.git` and other artifacts. The name of the
`.zip` file is taken from the [name](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/name) field in the extension [manifest](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json).

\n

#### \--as-needed

\n

Re-build the extension anytime you edit and save a source file. This allows
you to continuously create a package with the most up to date source code.

\n

Environment variable: `$WEB_EXT_AS_NEEDED=true`

\n

### web-ext docs

\n

Opens the [web-ext documentation](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Getting_started_with_web-ext) in the user's default browser.

\n

### web-ext lint

\n

Reports errors in the extension [manifest](/en-US/Add-
ons/WebExtensions/manifest.json) or other source code files. See the [addons-
linter](https://github.com/mozilla/addons-linter) project for more information
about what kind of rules are used to validate extension source.

\n

#### \--output, -o

\n

The type of output to generate when reporting on errors. Choices: `json` or
`text`.

\n

Environment variable: `$WEB_EXT_OUTPUT`

\n

#### \--metadata

\n

Output only metadata about the extension in JSON.

\n

Environment variable: `$WEB_EXT_METADATA=true`

\n

#### \--pretty

\n

Format the JSON output so that it's easier to read. This only applies when
`--output` is set to `json`.

\n

Environment variable: `$WEB_EXT_PRETTY=true`

\n

#### \--self-hosted

\n

Declares that your extension will be self-hosted.\xa0This disables messages
related to hosting on [addons.mozilla.org](https://addons.mozilla.org/).

\n

Environment variable: `$WEB_EXT_SELF_HOSTED=true`

\n

#### \--boring

\n

Disables colorful shell characters so that the output only contains plain
text.

\n

Environment variable: `$WEB_EXT_BORING=true`

\n

#### \--warnings-as-errors, -w

\n

Treat warnings as errors by exiting non-zero for warnings.

\n

Environment variable: `$WEB_EXT_WARNINGS_AS_ERRORS=true`

\n

### web-ext run

\n

Builds and then temporarily installs an extension on Firefox so it can be
tested. By default, this will also watch all extension source files and reload
the extension in Firefox as files change.

\n

#### \--firefox, -f

\n

Allows you to specify a particular version of Firefox to run the extension in.
The value can be an absolute path to the Firefox executable or it can be an
alias string. If this is not specified, it will attempt to run the extension
inside the default installation of Firefox on the system.

\n

Here is an example of specifying a full path to a Firefox executable on
Windows:

\n

    
    
    --firefox="C:\\Program Files\\Mozilla Firefox\\firefox.exe"

\n

Here is an example of specifying an executable path on Mac OS:

\n

    
    
    --firefox=/Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin

\n

You can also use aliases, like this:

\n

    
    
    --firefox=beta

\n

Here are all available aliases and the executables they map to:

\n\n\n\nAlias\n| Firefox executable\n  
---|---  
\n\n\n\n`firefox`\n| The [release](https://www.mozilla.org/en-US/firefox/new/)
build of Firefox\n  
\n\n`beta`\n| The [beta](https://www.mozilla.org/en-
US/firefox/channel/desktop/) build of Firefox\n  
\n\n`nightly`\n| The [nightly](https://www.mozilla.org/en-
US/firefox/channel/desktop/) build of Firefox\n  
\n\n`firefoxdeveloperedition`\n| The [developer](https://www.mozilla.org/en-
US/firefox/channel/desktop/) build of Firefox\n  
\n\n\n

Environment variable: `$WEB_EXT_FIREFOX`

\n

#### \--firefox-profile, -p

\n

Allows you to specify a base Firefox profile to run the extension in. This is
specified as a string containing your profile name or an absolute path to its
directory. The profile you specify is copied into a new temporary profile and
some settings are added that are required for `web-ext` to function.

\n

If a profile is not specified, it will run the extension using a new temporary
profile.

\n

Environment variable: `$WEB_EXT_FIREFOX_PROFILE`

\n

#### \--keep-profile-changes

\n

With this option, any changes made to the profile directory (specified by
`--firefox-profile`) will be saved. Without this option, profile changes will
not be saved.

\n

\n

This option makes the profile specified by `--firefox-profile` completely
insecure for daily usage. It turns off auto-updates and allows silent remote
connections, among other things. Specifically, it will make destructive
changes to the profile that are required for `web-ext` to operate.

\n

\n

Environment variable: `$WEB_EXT_KEEP_PROFILE_CHANGES=true`

\n

#### \--no-reload

\n

Do not automatically reload the extension in the browser as you edit and save
source files.

\n

Environment variable: `$WEB_EXT_NO_RELOAD=true`

\n

#### \--pre-install

\n

Pre-install the extension into the profile before starting the browser. This
is a way to support Firefox versions less than 49 since they do not support
remote installation. Specifying this option implies `--no-reload`.

\n

Environment variable: `$WEB_EXT_PRE_INSTALL=true`

\n

#### \--pref

\n

Customize any Firefox preference without creating or\xa0modifying the profile.
Use the equal sign to set values, for example:

\n

    
    
    --pref general.useragent.locale=fr-FR

\n

You can specify this option multiple times to set more than one preference.

\n

Environment variable: `$WEB_EXT_PREF`

\n

#### \--browser-console, -bc

\n

This automatically opens a [Browser Console](/en-
US/docs/Tools/Browser_Console) on startup so you can see log messages for your
extension. Example:

\n

    
    
    web-ext run --browser-console

\n

Environment variable: `$WEB_EXT_BROWSER_CONSOLE=true`

\n

#### \--start-url

\n

This will automatically open a tab at the specified URL when the browser
starts up. Example:

\n

    
    
    web-ext run --start-url www.mozilla.com

\n

You can declare this option multiple times to open multiple tabs. Example:

\n

    
    
    web-ext run --start-url www.mozilla.com --start-url developer.mozilla.org

\n

Environment variable: `$WEB_EXT_START_URL`

\n

### web-ext sign

\n

Packages an extension and signs it so it can be self-hosted. This will create
a signed `.xpi` file instead of a `.zip` file. You will need to create [API
access credentials](http://addons-
server.readthedocs.org/en/latest/topics/api/auth.html#access-credentials) to
run this command.

\n

#### \--api-key

\n

Your API key ([JWT issuer](http://addons-
server.readthedocs.org/en/latest/topics/api/auth.html#create-a-jwt-for-each-
request/)) for accessing the [addons.mozilla.org API](http://addons-
server.readthedocs.org/en/latest/topics/api/index.html). This should always be
a string.

\n

Environment variable: `$WEB_EXT_API_KEY`

\n

#### \--api-secret

\n

Your API secret ([JWT secret](http://addons-
server.readthedocs.org/en/latest/topics/api/auth.html#create-a-jwt-for-each-
request)) from [addons.mozilla.org API](http://addons-
server.readthedocs.org/en/latest/topics/api/index.html). This should always be
a string.

\n

Environment variable: `$WEB_EXT_API_SECRET`

\n

#### \--api-url-prefix

\n

The signing API URL prefix. This should always be a string. If not specified,
this will default to\xa0`https://addons.mozilla.org/api/v3` which is the
production API.

\n

Environment variable: `$WEB_EXT_API_URL_PREFIX`

\n

#### \--api-proxy

\n

A proxy host to use for all API connections. Example: `https://yourproxy:6000.
`Read more about [how proxy requests
work](https://github.com/request/request#proxies). There is a separate section
about [signing in a restricted environment](/en-US/Add-ons/WebExtensions
/Getting_started_with_web-ext#Signing_in_a_restricted_environment) if the
proxy approach doesn't work for you.

\n

Environment variable: `$WEB_EXT_API_PROXY`

\n

#### \--timeout

\n

Number of milleseconds to wait before giving up on a\xa0response from
Mozilla's web service. This should always be a number.

\n

Environment variable: `$WEB_EXT_TIMEOUT`

\n

#### \--id

\n

A custom identifier string for the extension. This has no effect if the
extension already declares an identifier in its manifest. This option may be
useful for signing versions of an exisiting extension that you own.

\n

Environment variable: `$WEB_EXT_ID`

\n

## Global options

\n

web-ext has the following global options that may apply to multiple commands.

\n

### \--artifacts-dir, -a

\n

Specifies a particular directory to save artifacts in, e.g the `.zip` file,
once you've built an extension. This can be specified as a relative or
absolute path, and should always be a string.

\n

\n

 **Note** : If this is not specified, the default is the relative path `./web-
ext-artifacts`.

\n

\n

Environment variable: `$WEB_EXT_ARTIFACTS_DIR`

\n

### \--ignore-files, -i

\n

A list of [glob patterns](https://github.com/isaacs/node-glob#glob-primer) to
define which files should be ignored by `build`, `run`, `lint` and other
commands. If you specify relative paths, they will be relative to your
`--source-dir`.

\n

Here is an example of ignoring any file within your `--source-dir` (or its
subdirectories) that ends in the suffix `.api-key`:

\n

    
    
    web-ext build --ignore-files "**/*.api-key"

\n

You can specify multiple patterns by separating them with spaces:

\n

    
    
    web-ext build --ignore-files path/to/first.js path/to/second.js

\n

By default, without the use of `--ignore-files`, the following rules are
applied:

\n

\n

  * Any file ending in `.xpi` or `.zip` is ignored
\n

  * Any hidden file (one that starts with a dot) is ignored
\n

  * Any directory named `node_modules` is ignored
\n

\n

When you specify custom patterns using `--ignore-files`, they are applied _in
addition to_ the default patterns.

\n

\n

 **Note** : Order is important: you must specify the web-ext command before
specifying the --ignore-files option.

\n

\n

Environment variable: `$WEB_EXT_IGNORE_FILES`

\n

### \--help, -h

\n

Lists all the available commands and options available for the web-ext tool.

\n

\n

 **Note** : You can list the options available for a specific command by
including the command name as you request help, for example\xa0`web-ext --help
run`.

\n

\n

### \--source-dir, -s

\n

Specifies the directory of the extension's source code, e.g. when building or
running an extension. This can be specified as a relative or absolute path,
and should always be a string.

\n

\n

 **Note** : If this is not specified, the default is the directory you are
currently inside in your terminal.

\n

\n

Environment variable: `$WEB_EXT_SOURCE_DIR`

\n

### \--verbose, -v

\n

Shows verbose output when commands are run.

\n

Environment variable: `$WEB_EXT_VERBOSE=true`

\n

### \--version

\n

Shows the version number of the installed web-ext tool.

\n

## Setting option environment variables

\n

Environment variables can be set for any option. You:

\n

\n

  1. Take the option name.
\n

  2. Remove the two dashes at the start.
\n

  3. Convert the remaining dashes to underscores.
\n

  4. Capitalize the letters.
\n

  5. Prefix the result with `$WEB_EXT_`.
\n

\n

So, for example, instead of specifying the following source option every time
you wish to run the extension:

\n

    
    
    web-ext run --source-dir=/path/to/my/extension

\n

You could set the source directory as an environment variable like this:

\n

    
    
    WEB_EXT_SOURCE_DIR=/path/to/my/extension

\n

Then you can just specify the run command without options:

\n

    
    
    web-ext run

\n

A command line option will always override the environment variable. For
example, this ignores the environment variable:

\n

    
    
    web-ext run --source-dir=/another/path/to/source

\n

To define a `true` / `false` flag option (which does not have a value on the
command line), set it to a literal string value of either `true` or `false`.
Example:

\n

    
    
    WEB_EXT_VERBOSE=true

\n

## See also

\n

\n

  * [web-ext repo](https://github.com/mozilla/web-ext)
\n

  * [Getting started with web-ext](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)
\n

\n]

