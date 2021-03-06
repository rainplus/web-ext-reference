Once you've finished writing and testing your extension, you'll probably want
to share it with other people. Mozilla operates a website:
[addons.mozilla.org](https://addons.mozilla.org) (commonly abbreviated to
AMO), where developers can publish add-ons and users can find them. By
publishing your extension on AMO, you can participate in our community of
users and creators, and find an audience for your extension.

You don't have to publish your extension on AMO. However, even if you are not
intending to publish your extension on AMO, you do have to submit it to AMO so
it can be reviewed and signed. Release versions of Firefox will refuse to
install extensions that are not signed by AMO.

So the process for publishing an extension is, in outline:

  1. zip up your extension's files
  2. create an account on AMO
  3. upload your zip to AMO for signing and review, and select listing option
  4. fix any problems that are found in review
  5. if you chose not to publish on AMO, retrieve the signed extension, and publish it yourself

When you're ready to release a new version of your extension, you can update
it by visiting the extension's page on
[addons.mozilla.org](https://addons.mozilla.org), and uploading the new
version there. Note that you must update it on the extension's page, so AMO
recognizes it as an update to an existing extension, and not a brand-new one.

If you chose to publish your extension on AMO, then Firefox will automatically
check for updates. If you chose to publish it yourself, you'll need to include
the `[applications](/en-US/docs/Mozilla/Add-
ons/WebExtensions/manifest.json/applications)` key in your manifest.json, with
the `update_url` attribute set to point to an [update manifest file](/en-US
/Add-ons/Updates).

Packaged extensions in Firefox are called "XPI files", which are just ZIP
files with a different extension.

You don't have to use the XPI extension when uploading to AMO.

## 1\. Zip up your extension's files

At this point your extension will consist of a directory containing a
manifest.json and any other files it needs - scripts, icons, HTML documents,
and so on. You'll need to zip these into a single file for uploading to AMO.

One trick is that **the ZIP file must be a ZIP of the extension's files
themselves, not of the containing directory**.

### Windows

  1. Open the folder with your extension's files.
  2. Select all of the files.
  3. Right click and choose Send to → Compressed (zipped) Folder.

![](https://mdn.mozillademos.org/files/11949/install-windows.png)

### Mac OS X

  1. Open the folder with your extension's files.
  2. Select all of the files.
  3. Right click and choose Compress _n_ Items.

![](https://mdn.mozillademos.org/files/11951/install-osx.png)

See <http://www.info-zip.org/mans/zip.html>.

### Linux / Mac OS X Terminal

  1. `cd path/to/my-extension/`
  2. `zip -r -FS ../my-extension.zip *`



## 2\. Create an account on addons.mozilla.org

Visit <https://addons.mozilla.org/>. If you already have a [Firefox
Account](https://support.mozilla.org/en-US/kb/access-mozilla-services-firefox-
accounts), you can use that to log in. Otherwise, click "Register" and you'll
be asked to create a Firefox account.

## 3\. Upload your zip

Next, upload the zipped extension to AMO for signing and review, and choose
whether to publish it on AMO or not. A [tutorial ](/en-US/docs/Mozilla/Add-
ons/Distribution/Submitting_an_add-on_tutorial)is available to guide you
through the submission process. You may also see [Submitting to AMO](/en-US
/Add-ons/Distribution#Submitting_to_AMO) for submission details.

Note that once you have uploaded your extension to AMO, you can't then update
the extension to use the Add-on SDK or legacy XUL/XPCOM techniques. If you do
switch to one of these platforms, you must submit it as a completely new
extension.

That is: porting from legacy extension systems to use WebExtension APIs is a
one-way street.

Before uploading, double-check that the ZIP contains exactly the contents you
want to submit, with no extra redundant files.

## 4\. Fix review problems

As soon as you upload the extension, the AMO server will run some basic checks
and immediately notify you about any problems. Problems are presented in two
categories: "errors" and "warnings". If you have errors, you must fix them and
resubmit. If you only have warnings, it's advisable to address them, but not
mandatory: you can continue with the submission.

If the automated checker doesn't report any errors, the extension will go for
a more detailed review. You'll be contacted with the review results and will
need to fix any problems and resubmit.

If you have chosen to have the extension hosted on AMO, this is the end of the
publication process. AMO will sign the extension and publish it, and users
will then be able to download and install it.

## 5\. Publish your extension

If you chose not to publish on AMO, retrieve the signed extension, and publish
it yourself.



