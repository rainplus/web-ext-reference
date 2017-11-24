[



Once you have a first build of your add-on, you'll want to distribute it so
others can give it a try. Whether you are distributing your add-on publicly or
privately, through [addons.mozilla.org](https://addons.mozilla.org/) (AMO) or
elsewhere, you'll want to have your add-on package signed.



## Signing your add-on



Starting with Firefox 43, there are some restrictions in place for add-on
distribution. Most add-ons that support Firefox need to be signed by Mozilla
in order for them to be installable in release and beta versions of Firefox.
Note that this only applies to add-on types 2 and 32; [other add-on types
](/en-US/Add-ons/Install_Manifests#type) like themes and language packs don't
require signing. Add-ons that only support other applications like Thunderbird
and SeaMonkey are also excluded. Unsigned add-ons can still be installed in
[Developer Edition](/en-US/Firefox/Developer_Edition), Nightly, and [ESR](/en-
US/Firefox/Enterprise_deployment) versions of Firefox, after toggling the
_xpinstall.signatures.required_ preference in `about:config`.



Only Mozilla can sign your add-on so that Firefox will install it by default.
Add-ons are signed by [submitting them to
AMO](https://addons.mozilla.org/developers/addon/submit) or using the API and
passing either an automated or manual code review. Note that you are not
required to list or distribute your add-on through AMO. If you are
distributing the add-on on your own, you can choose that option and AMO will
only serve as the way to get your package signed.



### Signing API



If you choose, you can sign your [XPI](/en-US/docs/XPI) files using the
[addons.mozilla.org signing API](http://addons-
server.readthedocs.io/en/latest/topics/api/signing.html). All add-ons uploaded
to AMO which pass review are automatically signed. Signing your add-on prior
to uploading to AMO is not required.



If your add-on is an SDK add-on then use the [jpm](/en-US/Add-
ons/SDK/Tools/jpm) tool, the [jpm sign](/en-US/Add-ons/SDK/Tools/jpm#jpm_sign)
command will work with the API to sign your add-on.



If your extension uses WebExtension APIs then use the [web-ext](/en-
US/docs/Mozilla/Add-ons/WebExtensions/Getting_started_with_web-ext) tool, the
[web-ext sign](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/web-
ext_command_reference#web-ext_sign) command will work with the API to sign
your extension.



## Submitting to AMO



New add-ons are uploaded to AMO through [this submission
form](https://addons.mozilla.org/developers/addon/submit/). The first step is
to read through and accept our [Developer Agreement](/en-US/Add-
ons/AMO/Policy/Agreement). A [tutorial ](/en-US/docs/Mozilla/Add-
ons/Distribution/Submitting_an_add-on_tutorial)is available to guide you
through the submission process.



Next, you'll need to decide if you want to distribute and list your add-on
file through AMO or not. Here are some things you should consider to make this
decision:





  * AMO is a very popular distribution platform, with millions of monthly visitors and installations. It is integrated into the Firefox Add-ons Manager, allowing easy installation of published AMO add-ons directly from the Firefox UI.


  * All add-ons listed on AMO may be subject to code review and testing by a team of employees and volunteers. In some cases, an add-on may require a review before it can be listed. In these cases, review times can range between a few hours to a number of weeks depending on an add-on\u2019s complexity and other factors.


  * Self-distributed add-on files are automatically reviewed and signed. The add-ons review team may, from time to time, perform a manual review of your signed add-ons and give you feedback about them.


  * When you make updates to your add-on to add features or fix bugs, you'll probably want any previously installed versions of the add-on to automatically be updated to the new version. 
    * For versions hosted on AMO, all you have to do is upload the new version: Host applications (e.g. Firefox) default to checking AMO for new versions of add-ons.


    * For versions that aren't hosted on AMO, you need to tell the host application (e.g. Firefox) where it can find new versions. To do this, you need to include a URL in the add-on's manifest: [update_link](/en-US/Add-ons/Updates) for WebExtensions and `[updateURL](/en-US/Add-ons/Install_Manifests#updateURL)` for legacy add-ons. The host application will go there to get information about updates. If you're using the Add-on SDK, see [Supporting updates for self-hosted add-ons](/en-US/Add-ons/SDK/Tools/jpm#Supporting_updates_for_self-hosted_add-ons). Self-distributed add-ons that don't have an update URL defined in their manifest will check AMO for updates, and will be updated to a listed version if available.






### Self-distributed (unlisted) versions



After accepting the Developer Agreement, choose the platforms your add-on
supports and upload your add-on file. The file will be scanned by an automatic
code validator which will show a number of warnings or errors, depending on
what it detects. If no errors are found in your add-on package, your add-on
management page will be created and your file will be immediately signed.
You'll receive an email with instructions on how to download the signed file.



All new versions of your add-ons will also need to be signed. Once your first
version has been submitted, you can upload new versions in the developer page
for your add-on.\xa0 The signing process is the same for all self-distributed
versions.



### Listed versions



After accepting the Developer Agreement, choose the platforms your add-on
supports and upload your add-on file. The file will be scanned by an automatic
code validator which will show a number of warnings or errors depending on
what it detects. Errors only show up for listed add-ons if there's something
wrong in the package that needs to be fixed before it can be accepted.
Warnings can vary in importance and severity; you should read through all of
them carefully and see if there's anything you can fix in your add-on in order
to avoid them showing up. Your add-on does not need to have no warnings
generated by the automatic code validator in order to pass review, but they
are areas of your add-on which you should check and possibly rewrite. You
should not obfuscate your code to bypass validation warnings. That practice
can lead to your add-on being rejected and potentially blacklisted.



Once you finish your listed add-on submission, it may be placed in a review
queue, where a member of our review team will give it a look. This can take
between a couple of hours to a number of weeks, depending on your add-on's
complexity and other factors. Once your add-on passes review, the file is
signed and published on AMO.



#### Beta versions



Beta channels are only available for listed add-ons that aren't marked as
experimental.



To create a beta channel, upload a file with a unique version string that
contains any of the following strings: `a,b,alpha,beta,pre,rc`, with an
optional number at the end. This text must come at the end of the version
string. If you understand [RegEx](/en-
US/docs/Web/JavaScript/Reference/Global_Objects/RegExp) format, here's what we
look for in the version number: `"(a|alpha|b|beta|pre|rc)\\d*$"`.



When a file meeting this version number criteria is uploaded to AMO, it will
automatically be detected as a beta version. Users of your add-on who have
chosen to download beta versions will automatically be served the newest beta
updates. Beta versions are treated like unlisted add-on versions, in that they
will be accepted and signed immediately, if they pass automatic
validation.\xa0 They also cannot be side-loaded, and must not be pushed as
updates to side-loaded versions if you're also using these versions outside of
AMO.



While we call these "Beta versions", you can use this channel for nightlies,
or alphas, or prerelease versions, as you wish. Please note that there is only
one channel for this purpose and all of your users on this channel will
receive the latest add-ons submitted. For instance, if you upload `1.0beta1`
to the release channel and then upload `1.1alpha1`, all users of `1.0beta1`
will be offered an upgrade to `1.1alpha1`. Updates are pushed by submission
date and not version number, so users will always get the most recent channel
update regardless of any kind of alphabetical sorting.



## Ownership



Add-ons can have multiple users with permission to update and manage the
listing. Existing authors of an add-on can transfer ownership and add
additional developers to an add-on's listing through the Developer Tools
provided. No interaction with Mozilla representatives is necessary for a
transfer of ownership.



## Code disputes



Many add-ons allow their source code to be openly viewed. This does not mean
that the source code is open source or available for use in another add-on.
The original author of\xa0an add-on retains copyright of their work unless
otherwise noted in the add-on's license.



In the event that we're notified of a copyright or license infringement, we
will take steps to address the situation per the DMCA, which may include
taking down the add-on listing. Details about this process and how to report
trademark or licensing issues can be [found here](https://www.mozilla.org/en-
US/about/legal/report-abuse/).



If you are unsure of the current copyright status of an add-on's source code,
you must contact the original author and receive explicit permission before
using the source code.

]

