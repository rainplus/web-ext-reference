[



This page lists all the commands and options available under the [web-
ext](https://github.com/mozilla/web-ext) command line tool.



## Commands



web-ext has the following commands available; options specific to these
commands are included as subsections.



### web-ext build



Packages an extension into a `.zip` file, ignoring files that are commonly
unwanted in packages, such as `.git` and other artifacts. The name of the
`.zip` file is taken from the [name](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/name) field in the extension [manifest](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json).



#### \--as-needed



Re-build the extension anytime you edit and save a source file. This allows
you to continuously create a package with the most up to date source code.



Environment variable: `$WEB_EXT_AS_NEEDED=true`



### web-ext docs



Opens the [web-ext documentation](https://developer.mozilla.org/en-US/Add-
ons/WebExtensions/Getting_started_with_web-ext) in the user's default browser.



### web-ext lint



Reports errors in the extension [manifest](/en-US/Add-
ons/WebExtensions/manifest.json) or other source code files. See the [addons-
linter](https://github.com/mozilla/addons-linter) project for more information
about what kind of rules are used to validate extension source.



#### \--output, -o



The type of output to generate when reporting on errors. Choices: `json` or
`text`.



Environment variable: `$WEB_EXT_OUTPUT`



#### \--metadata



Output only metadata about the extension in JSON.



Environment variable: `$WEB_EXT_METADATA=true`



#### \--pretty



Format the JSON output so that it's easier to read. This only applies when
`--output` is set to `json`.



Environment variable: `$WEB_EXT_PRETTY=true`



#### \--self-hosted



Declares that your extension will be self-hosted.\xa0This disables messages
related to hosting on [addons.mozilla.org](https://addons.mozilla.org/).



Environment variable: `$WEB_EXT_SELF_HOSTED=true`



#### \--boring



Disables colorful shell characters so that the output only contains plain
text.



Environment variable: `$WEB_EXT_BORING=true`



#### \--warnings-as-errors, -w



Treat warnings as errors by exiting non-zero for warnings.



Environment variable: `$WEB_EXT_WARNINGS_AS_ERRORS=true`



### web-ext run



Builds and then temporarily installs an extension on Firefox so it can be
tested. By default, this will also watch all extension source files and reload
the extension in Firefox as files change.



#### \--firefox, -f



Allows you to specify a particular version of Firefox to run the extension in.
The value can be an absolute path to the Firefox executable or it can be an
alias string. If this is not specified, it will attempt to run the extension
inside the default installation of Firefox on the system.



Here is an example of specifying a full path to a Firefox executable on
Windows:



    
    
    --firefox="C:\\Program Files\\Mozilla Firefox\\firefox.exe"



Here is an example of specifying an executable path on Mac OS:



    
    
    --firefox=/Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin



You can also use aliases, like this:



    
    
    --firefox=beta



Here are all available aliases and the executables they map to:

Alias| Firefox executable  
---|---  
`firefox`| The [release](https://www.mozilla.org/en-US/firefox/new/)
build of Firefox  
`beta`| The [beta](https://www.mozilla.org/en-
US/firefox/channel/desktop/) build of Firefox  
`nightly`| The [nightly](https://www.mozilla.org/en-
US/firefox/channel/desktop/) build of Firefox  
`firefoxdeveloperedition`| The [developer](https://www.mozilla.org/en-
US/firefox/channel/desktop/) build of Firefox  


Environment variable: `$WEB_EXT_FIREFOX`



#### \--firefox-profile, -p



Allows you to specify a base Firefox profile to run the extension in. This is
specified as a string containing your profile name or an absolute path to its
directory. The profile you specify is copied into a new temporary profile and
some settings are added that are required for `web-ext` to function.



If a profile is not specified, it will run the extension using a new temporary
profile.



Environment variable: `$WEB_EXT_FIREFOX_PROFILE`



#### \--keep-profile-changes



With this option, any changes made to the profile directory (specified by
`--firefox-profile`) will be saved. Without this option, profile changes will
not be saved.





This option makes the profile specified by `--firefox-profile` completely
insecure for daily usage. It turns off auto-updates and allows silent remote
connections, among other things. Specifically, it will make destructive
changes to the profile that are required for `web-ext` to operate.





Environment variable: `$WEB_EXT_KEEP_PROFILE_CHANGES=true`



#### \--no-reload



Do not automatically reload the extension in the browser as you edit and save
source files.



Environment variable: `$WEB_EXT_NO_RELOAD=true`



#### \--pre-install



Pre-install the extension into the profile before starting the browser. This
is a way to support Firefox versions less than 49 since they do not support
remote installation. Specifying this option implies `--no-reload`.



Environment variable: `$WEB_EXT_PRE_INSTALL=true`



#### \--pref



Customize any Firefox preference without creating or\xa0modifying the profile.
Use the equal sign to set values, for example:



    
    
    --pref general.useragent.locale=fr-FR



You can specify this option multiple times to set more than one preference.



Environment variable: `$WEB_EXT_PREF`



#### \--browser-console, -bc



This automatically opens a [Browser Console](/en-
US/docs/Tools/Browser_Console) on startup so you can see log messages for your
extension. Example:



    
    
    web-ext run --browser-console



Environment variable: `$WEB_EXT_BROWSER_CONSOLE=true`



#### \--start-url



This will automatically open a tab at the specified URL when the browser
starts up. Example:



    
    
    web-ext run --start-url www.mozilla.com



You can declare this option multiple times to open multiple tabs. Example:



    
    
    web-ext run --start-url www.mozilla.com --start-url developer.mozilla.org



Environment variable: `$WEB_EXT_START_URL`



### web-ext sign



Packages an extension and signs it so it can be self-hosted. This will create
a signed `.xpi` file instead of a `.zip` file. You will need to create [API
access credentials](http://addons-
server.readthedocs.org/en/latest/topics/api/auth.html#access-credentials) to
run this command.



#### \--api-key



Your API key ([JWT issuer](http://addons-
server.readthedocs.org/en/latest/topics/api/auth.html#create-a-jwt-for-each-
request/)) for accessing the [addons.mozilla.org API](http://addons-
server.readthedocs.org/en/latest/topics/api/index.html). This should always be
a string.



Environment variable: `$WEB_EXT_API_KEY`



#### \--api-secret



Your API secret ([JWT secret](http://addons-
server.readthedocs.org/en/latest/topics/api/auth.html#create-a-jwt-for-each-
request)) from [addons.mozilla.org API](http://addons-
server.readthedocs.org/en/latest/topics/api/index.html). This should always be
a string.



Environment variable: `$WEB_EXT_API_SECRET`



#### \--api-url-prefix



The signing API URL prefix. This should always be a string. If not specified,
this will default to\xa0`https://addons.mozilla.org/api/v3` which is the
production API.



Environment variable: `$WEB_EXT_API_URL_PREFIX`



#### \--api-proxy



A proxy host to use for all API connections. Example: `https://yourproxy:6000.
`Read more about [how proxy requests
work](https://github.com/request/request#proxies). There is a separate section
about [signing in a restricted environment](/en-US/Add-ons/WebExtensions
/Getting_started_with_web-ext#Signing_in_a_restricted_environment) if the
proxy approach doesn't work for you.



Environment variable: `$WEB_EXT_API_PROXY`



#### \--timeout



Number of milleseconds to wait before giving up on a\xa0response from
Mozilla's web service. This should always be a number.



Environment variable: `$WEB_EXT_TIMEOUT`



#### \--id



A custom identifier string for the extension. This has no effect if the
extension already declares an identifier in its manifest. This option may be
useful for signing versions of an exisiting extension that you own.



Environment variable: `$WEB_EXT_ID`



## Global options



web-ext has the following global options that may apply to multiple commands.



### \--artifacts-dir, -a



Specifies a particular directory to save artifacts in, e.g the `.zip` file,
once you've built an extension. This can be specified as a relative or
absolute path, and should always be a string.





 **Note** : If this is not specified, the default is the relative path `./web-
ext-artifacts`.





Environment variable: `$WEB_EXT_ARTIFACTS_DIR`



### \--ignore-files, -i



A list of [glob patterns](https://github.com/isaacs/node-glob#glob-primer) to
define which files should be ignored by `build`, `run`, `lint` and other
commands. If you specify relative paths, they will be relative to your
`--source-dir`.



Here is an example of ignoring any file within your `--source-dir` (or its
subdirectories) that ends in the suffix `.api-key`:



    
    
    web-ext build --ignore-files "**/*.api-key"



You can specify multiple patterns by separating them with spaces:



    
    
    web-ext build --ignore-files path/to/first.js path/to/second.js



By default, without the use of `--ignore-files`, the following rules are
applied:





  * Any file ending in `.xpi` or `.zip` is ignored


  * Any hidden file (one that starts with a dot) is ignored


  * Any directory named `node_modules` is ignored




When you specify custom patterns using `--ignore-files`, they are applied _in
addition to_ the default patterns.





 **Note** : Order is important: you must specify the web-ext command before
specifying the --ignore-files option.





Environment variable: `$WEB_EXT_IGNORE_FILES`



### \--help, -h



Lists all the available commands and options available for the web-ext tool.





 **Note** : You can list the options available for a specific command by
including the command name as you request help, for example\xa0`web-ext --help
run`.





### \--source-dir, -s



Specifies the directory of the extension's source code, e.g. when building or
running an extension. This can be specified as a relative or absolute path,
and should always be a string.





 **Note** : If this is not specified, the default is the directory you are
currently inside in your terminal.





Environment variable: `$WEB_EXT_SOURCE_DIR`



### \--verbose, -v



Shows verbose output when commands are run.



Environment variable: `$WEB_EXT_VERBOSE=true`



### \--version



Shows the version number of the installed web-ext tool.



## Setting option environment variables



Environment variables can be set for any option. You:





  1. Take the option name.


  2. Remove the two dashes at the start.


  3. Convert the remaining dashes to underscores.


  4. Capitalize the letters.


  5. Prefix the result with `$WEB_EXT_`.




So, for example, instead of specifying the following source option every time
you wish to run the extension:



    
    
    web-ext run --source-dir=/path/to/my/extension



You could set the source directory as an environment variable like this:



    
    
    WEB_EXT_SOURCE_DIR=/path/to/my/extension



Then you can just specify the run command without options:



    
    
    web-ext run



A command line option will always override the environment variable. For
example, this ignores the environment variable:



    
    
    web-ext run --source-dir=/another/path/to/source



To define a `true` / `false` flag option (which does not have a value on the
command line), set it to a literal string value of either `true` or `false`.
Example:



    
    
    WEB_EXT_VERBOSE=true



## See also





  * [web-ext repo](https://github.com/mozilla/web-ext)


  * [Getting started with web-ext](/en-US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext)


]

