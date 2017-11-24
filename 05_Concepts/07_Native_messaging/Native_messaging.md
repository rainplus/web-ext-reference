[



Native messaging enables an extension to exchange messages with a native
application installed on the user's computer. This enables native applications
to provide a service to extensions without needing to be reachable over the
web. One common example here is password managers: the native application
manages storage and encryption of passwords, and communicates with the
extension to populate web forms. Native messaging also enables extensions to
access resources that are not accessible through WebExtension APIs, such as
some particular piece of hardware.



The native application is not installed or managed by the browser: it's
installed using the underlying operating system's installation machinery.
Along with the native application itself, you'll need to provide a JSON file
called the "host manifest" or "app manifest", and install it in a defined
location on the user's computer. The app manifest file describes how the
browser can connect to the native application.



The extension must request the "nativeMessaging" [permission](/en-
US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions) in its
manifest.json file. Conversely, the native application must grant permission
for the extension by including its ID in the "allowed_extensions" field of the
app manifest.



After that the extension can exchange JSON messages with the native
application using a set of functions in the [`runtime`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime "The documentation about this has not yet
been written; please consider contributing!") API. On the native app side,
messages are received using standard input (stdin) and sent using standard
output (stdout).



![](https://mdn.mozillademos.org/files/13833/native-messaging.png)



Support for native messaging in extensions is mostly compatible with Chrome,
with two main differences:





  * The app manifest lists "allowed_extensions" as an array of app IDs, while Chrome lists "allowed_origins", as an array of "chrome-extension" URLs.


  * The app manifest is stored in a different location, compared to Chrome.




There's a complete example in the ["native-messaging"
directory](https://github.com/mdn/webextensions-examples/tree/master/native-
messaging) of the "webextensions-examples" repository on GitHub. Most of the
sample code in this article is taken directly from that example.



## Setup



### Extension manifest



If you want your extension to communicate with a native application, then:





  * You must set the\xa0"nativeMessaging" [permission](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions) in its [manifest.json](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json) file.


  * You should probably specify your add-on ID explicitly, using the [applications](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications) manifest key (This is because the app's manifest will identify the set of extensions that are allowed to connect to it by listing their IDs).




Here's an example manifest.json file:



    
    
    {  "description": "Native messaging example extension",  "manifest_version": 2,  "name": "Native messaging example",  "version": "1.0",  "icons": {    "48": "icons/message.svg"  },  "applications": {    "gecko": {      "id": "ping_pong@example.org",      "strict_min_version": "50.0"    }  },  "background": {    "scripts": ["background.js"]  },  "browser_action": {    "default_icon": "icons/message.svg"  },   "permissions": ["nativeMessaging"]}



### App manifest



The app manifest describes to the browser how it can connect to the native
application.



The app manifest file must be installed along with the native application.
That is, the browser reads and validates app manifest files but it does not
install or manage them. Thus the security model for when and how these files
are installed and updated is much more like that for native applications than
that for extensions using WebExtension APIs.



For details of native app manifest syntax and location, see [Native manifests
](/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_manifests).



For example, here's a manifest for the "ping_pong" native application:



    
    
    {  "name": "ping_pong",  "description": "Example host for native messaging",  "path": "/path/to/native-messaging/app/ping_pong.py",  "type": "stdio",  "allowed_extensions": [ "ping_pong@example.org" ]}



This allows the extension whose ID is "ping_pong@example.org" to connect, by
passing the name "ping_pong" into the relevant [`runtime`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime "The documentation about this has not yet
been written; please consider contributing!") API function. The application
itself is at "/path/to/native-messaging/app/ping_pong.py".





 **Note for Windows** : in the example above, the native application is a
Python script. It can be difficult to get Windows to run Python scripts
reliably in this way, so an alternative is to provide a .bat file, and link to
that from the manifest:



    
    
    {  "name": "ping_pong",  "description": "Example host for native messaging",  "path": "c:\\\\path\\\\to\\\ative-messaging\\\\app\\\\ping_pong_win.bat",  "type": "stdio",  "allowed_extensions": [ "ping_pong@example.org" ]}



The batch file then invokes the Python script:



    
    
    @echo offpython -u "c:\\\\path\\\\to\\\ative-messaging\\\\app\\\\ping_pong.py"



\xa0









## Exchanging messages



Given the above setup, an extension can exchange JSON messages with a native
application.



### Extension side



If you've used [the messaging APIs to communicate with content scripts](/en-US
/Add-ons/WebExtensions/Content_scripts#Communicating_with_background_scripts),
this should look very familiar. There are two patterns: connection-based
messaging and connectionless messaging.



#### Connection-based messaging



With this pattern you call [`runtime.connectNative()`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime/connectNative "For more information, see
Native messaging."), passing the name of the application (the value of the
"name" property in the app's manifest). This launches the application if it is
not already running and returns a [`runtime.Port`](/en-US/docs/Mozilla/Add-
ons/WebExtensions/API/runtime/Port "The documentation about this has not yet
been written; please consider contributing!") object to the extension.



The native app is passed two arguments when it starts:





  * the complete path to the app manifest


  * (new in Firefox 55) the ID (as given in the [applications](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications) manifest.json key) of the add-on that started it.




The application stays running until the extension calls `Port.disconnect()` or
the page that connected to it is closed.



To send messages using `Port`, call its `postMessage()` function, passing the
JSON message to send. To listen for messages using `Port`, add the listener
using its `onMessage.addListener()` function.



Here's an example background script that establishes a connection with the
"ping_pong" app, listens for messages from it, then sends it a "ping" message
whenever the user clicks the browser action:



    
    
    /*On startup, connect to the "ping_pong" app.*/var port = browser.runtime.connectNative("ping_pong");/*Listen for messages from the app.*/port.onMessage.addListener((response) => {  console.log("Received: " + response);});/*On a click on the browser action, send the app a message.*/browser.browserAction.onClicked.addListener(() => {  console.log("Sending:  ping");  port.postMessage("ping");});



#### Connectionless messaging



With this pattern you call [`runtime.sendNativeMessage()`](/en-US/docs/Mozilla
/Add-ons/WebExtensions/API/runtime/sendNativeMessage "The documentation about
this has not yet been written; please consider contributing!"), passing it:





  * the name of the application


  * the JSON message to send


  * optionally, a callback.




A new instance of the app is created for each message. The app is passed two
arguments when it starts:





  * the complete path to the app manifest


  * (new in Firefox 55) the ID (as given in the [applications](/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/applications) manifest.json key) of the add-on that started it.




The first message sent by the app is treated as a response to the
`sendNativeMessage()` call, and will be passed into the callback.



Here's the example above, rewritten to use `runtime.sendNativeMessage()`:



    
    
    function onResponse(response) {  console.log("Received " + response);}function onError(error) {  console.log(`Error: ${error}`);}/*On a click on the browser action, send the app a message.*/browser.browserAction.onClicked.addListener(() => {  console.log("Sending:  ping");  var sending = browser.runtime.sendNativeMessage(    "ping_pong",    "ping");  sending.then(onResponse, onError);});



### App side



On the application side, you use standard input to receive messages and
standard output to send them.



Each message is serialized using JSON, UTF-8 encoded and is preceded with a
32-bit value containing the message length in native byte order.



The maximum size of a single message from the application is 1 MB. The maximum
size of a message sent to the application is 4 GB.



Here's an example written in Python. It listens for messages from the
extension. If the message is "ping", then it responds with a message "pong":



    
    
    #!/usr/bin/python -u# Note that running python with the `-u` flag is required on Windows,# in order to ensure that stdin and stdout are opened in binary, rather# than text, mode.import jsonimport sysimport struct# Read a message from stdin and decode it.def get_message():    raw_length = sys.stdin.read(4)    if not raw_length:        sys.exit(0)    message_length = struct.unpack('@I', raw_length)[0]    message = sys.stdin.read(message_length)    return json.loads(message)# Encode a message for transmission, given its content.def encode_message(message_content):    encoded_content = json.dumps(message_content)    encoded_length = struct.pack('@I', len(encoded_content))    return {'length': encoded_length, 'content': encoded_content}# Send an encoded message to stdout.def send_message(encoded_message):    sys.stdout.write(encoded_message['length'])    sys.stdout.write(encoded_message['content'])    sys.stdout.flush()while True:    message = get_message()    if message == "ping":        send_message(encode_message("pong"))



## Closing the native app



If you connected to the native application using `runtime.connectNative()`,
then it stays running until the extension calls `Port.disconnect()` or the
page that connected to it is closed. If you started the native application by
sending `runtime.sendNativeMessage()`, then it is closed after it has received
the message and sent a response.



To close the native application:





  * On *nix systems like OS X and Linux, the browser sends SIGTERM to the native application, then SIGKILL after the application has had a chance to exit gracefully. These signals propagate to any subprocesses unless they break away into a new process group.


  * On Windows, the browser puts the native application's process into a [Job object](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684161\(v=vs.85\).aspx), and kills the job. If the native application launches any additional processes and wants them to remain open after the native application itself is killed, then the native application must launch the additional process with the\xa0`[CREATE_BREAKAWAY_FROM_JOB](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684863\(v=vs.85\).aspx)` flag.




## Troubleshooting



If something goes wrong, check the [browser console](/en-US/Add-
ons/WebExtensions/Debugging#Viewing_log_output). If the native application
sends any output to stderr, the browser will redirect it to the browser
console. So if you've got as far as launching the native application, you will
see any error messages it emits.



If you haven't managed to run the application, you should see an error message
giving you a clue about the problem.



    
    
    "No such native application <name>"





  * \xa0Check that the name passed to `runtime.connectNative()` matches the name in the app manifest


  * OS X/Linux: check that name of the app manifest is <name>.json.


  * Windows: check that the registry key is in the correct place, and that its name matches the name in the app manifest.


  * Windows: check that the path given in the registry key points to the app manifest.




    
    
    "Error: Invalid application <name>"





  * Check that the application's name contains no invalid characters.




    
    
    "'python' is not recognized as an internal or external command, ..."





  * Windows: if your application is a Python script, check that you have Python installed and have your path set up for it.




    
    
    "File at path <path> does not exist, or is not executable"





  * If you see this, then the app manifest has been found successfully.


  * Check that the "path" in the app's manifest is correct.


  * Windows: check that you've escaped the path separators ("c:\\\\\\\path\\\\\\\to\\\\\\\file").


  * Check that the app is at the location pointed to by the "path" property in the app's manifest.


  * Check that the app is executable.




    
    
    "This extension does not have permission to use native application <name>"





  * Check that the "allowed_extensions" key in the app manifest contains the add-on's ID.




    
    
    "TypeError: browser.runtime.connectNative is not a function"





  * Check that the extension has the "nativeMessaging" permission




    
    
    "[object Object]       NativeMessaging.jsm:218"





  * There was a problem starting the application.




## Chrome incompatibilities



### Command-line arguments



On Linux and Mac, Chrome passes one argument to the native app, which is the
origin of the extension that started it, in the form: `chrome-
extension://[extensionID]`. This enables the app to identify the extension.



On Windows, Chrome passes two arguments: the first is the origin of the
extension, and the second is a handle to the Chrome native window that started
the app.



### allowed_extensions



In Chrome, the `allowed_extensions` key in the app manifest is called
`allowed_origins` instead.



### App manifest location



Chrome expects to find the app manifest in a different place. See [Native
messaging host
location](https://developer.chrome.com/extensions/nativeMessaging#native-
messaging-host-location) in the Chrome docs.\xa0

]

