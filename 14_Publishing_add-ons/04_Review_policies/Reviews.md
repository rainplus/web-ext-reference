[



In order to protect the safety and sovereignty of Firefox users, Mozilla
requires all add-ons to comply with a set of policies on acceptable practices.
The exact set of applicable policies varies depending on a number of
circumstances, the most important being whether the add-on is hosted on
[addons.mozilla.org](https://addons.mozilla.org/) (hereafter AMO), and how the
add-on is distributed in the wild.



This document outlines the policies which different classes of add-ons are
expected to follow. Regardless of the class of add-on, these policies are
enforced via a review process facilitated by AMO, and a mandatory code
signature check, enforced by Firefox.



## Add-on Review Tracks



### Listed on AMO



Add-ons listed on AMO may be subject to review. When awaiting review, an add-
on is accessible to users who have a direct link to its listing page.\xa0It
does not appear in category pages, collections, or search results. Once
approved, these add-ons have a public listing page that includes screenshots,
descriptions, and user reviews; the listing may also appear in search results,
collections, and occasional promotions. Existing users automatically receive
updates to new versions published to AMO. Listed add-ons may be subject to
full code review, as well as functional testing. These add-ons are held to a
high quality bar.



### Unlisted



Unlisted add-ons must be uploaded to AMO prior to distribution, but are
otherwise not accessible to the public via the site. These add-ons must be
distributed elsewhere by their publishers. Depending on the manner of
distribution, unlisted add-ons undergo a fully-automated review, with possible
post-signing code reviews.



While these add-ons are automatically signed, they are held to very similar
standards to those of listed add-ons. The primary difference is that these
add-ons must manage their own updates.



## Policies



The following table outlines the primary policies which apply to each add-on
review track. The policies are explained in further detail below. The symbols
below each review class specify how the requirement applies to those add-ons
as follows:

\xa0| The requirement does not apply to this review track.  
---|---  
\u2718| Add-ons in this review track are prohibited from engaging in
this behavior.  
\u2714| Add-ons in this review track _must_ follow this behavior.   
\xa0| Listed| Unlisted  
---|---|---  
Security| \xa0  
Cause harm to users' data, systems, or online identities| \u2718|
\u2718  
Create or expose security vulnerabilities| \u2718| \u2718  
Tamper with the application/add-on update or blocklist systems|
\u2718| \u2718  
Execute remote code\xb9| \u2718| \xa0  
Degrade the security of HTTPS sites| \u2718| \u2718  
Install additional add-ons or system applications without user consent|
\u2718| \xa0  
Include their own update mechanism| \u2718| \xa0  
Privacy and User Consent| \xa0  
Make unexpected changes to the browser or web content| \u2718|
\u2718  
Prevent users from reverting changes made by the add-on| \u2718|
\u2718  
Prevent the add-on from appearing in the Add-on Manager| \u2718|
\u2718  
Prevent the user from disabling or uninstalling the add-on\u2076|
\u2718| \u2718  
Send sensitive information to remote servers unprotected| \u2718|
\u2718  
Store browsing data from private browsing windows| \u2718| \xa0  
Leak identity information to web content in private browsing windows|
\u2718| \xa0  
Change Firefox preferences without user consent| \u2718| \xa0  
Clearly disclose all user data handling in a Privacy Policy| \u2714|
\xa0  
User Experience| \xa0  
Break or disable core application features| \u2718| \u2718  
Make any changes which persist after the add-on is disabled or
uninstalled| \u2718| \u2718  
Be easy to use and provide a consistent user experience| \u2714|
\xa0  
Require payment to use core add-on features (upfront or after trial)|
\u2718| \xa0  
Content| \xa0  
Violate the Mozilla [Conditions of Use](https://www.mozilla.org/en-
US/about/legal/acceptable-use/)| \u2718| \xa0  
Is intended for internal corporate use, testing, or personal use|
\u2718| \xa0  
Technical| \xa0  
Provide reviewers with full source code\u2075| \u2714| \u2714\xb2  
Use unvetted third-party code libraries or frameworks| \u2718| \xa0  
Contain obvious coding errors| \u2718| \xa0  
Conflict with other well-behaved add-ons\xb3| \u2718| \xa0  
Use APIs known to cause performance or stability problems\u2074|
\u2718| \xa0  


\xb9 Remote code may be executed in documents with the same origin as the code
being executed, or, under limited circumstances, in carefully constructed
sandboxes. Remote code may never be executed in privileged contexts.



\xb2 Unlisted add-ons must provide sources upon request. Failure to provide
sources for an automatically signed add-on upon explicit request may lead to
the add-on being blocked.



\xb3 It may not be possible for all add-ons to entirely avoid conflict with
all other add-ons. Add-ons which, by nature, cannot operate side-by-side may
be allowed to conflict. Conflicts due to poor technical practices will not be
tolerated.



\u2074 APIs which have been deprecated for performance or stability reasons,
including DOM mutation event listeners, synchronous XMLHttpRequests and
Storage API calls, and code which re-enters the main event loop, should not be
used in add-ons. They may be allowed under limited circumstances, where
alternatives are impractical, or be granted a reimplementation grace period,
but such exceptions are rare, and in general the APIs should be avoided as a
mater of course.



\u2075 Separate submission of full source code is required for add-ons which
use obfuscation, minification, or transcompilation to generate JavaScript
source code, or which include executable binary files, including system
executables or libraries. Instructions and tools necessary to reproduce
obfuscation may also be required. Add-ons which include only human-readable
JavaScript are not required to submit separate source code.



\u2076 Users must be able to disable and install the add-on via the Add-on
Manager interface. Providing secondary methods of uninstall, such as a system-
level uninstaller, while preventing it via the Add-on Manager interface, _does
not_ satisfy this requirement.



## Security



Because add-ons run in an environment with elevated privileges relative to
ordinary web pages, they present a very serious set of security
considerations. They have the potential to open security holes not only in the
add-ons themselves, but also in the browser, in web pages, and in particularly
worrying cases, the entire system the browser is running on. As a result, we
take our security policies very seriously, and apply most of them to all add-
ons, whether hosted on AMO or not. We expect all add-ons to be secure, not
only in their handling of their own data, and of user data, but also in all of
their interaction with the web, the browser, and the operating system.



## Privacy and User Consent



We take user sovereignty and privacy extremely seriously. Whether hosted on
AMO or not, we require all add-ons to respect users choices and their
reasonable expectations of privacy. In particular, this means that add-ons may
not limit users control of their browsers, by making it impossible to
permanently change settings (such as the homepage or search engine),
preventing users from uninstalling them, hiding their presence from users, or
installing toolbar buttons or other UI elements which cannot be permanently
removed via the UI customization process.



Features like advertising or certain forms of user activity tracking may be
required to be opt-in, or at least opt-out, depending on the privacy and
security impact, and whether the feature is necessary for the add-on to
function or not. Since these are usually additional monetization features that
are unrelated to what the add-on is meant to do, they generally require an
opt-in for listed add-ons and an opt-out for unlisted ones. Some forms of
tracking, like gathering all visited URLs, are generally forbidden even for
unlisted add-ons. The decision to activate or deactivate these features and
its implications must be clearly presented to the user.



## User Experience



We expect all add-ons to work without significantly degrading users'
experience with the browser. In particular, add-ons may not adversely affect
browser performance, break built-in features, or damage the user interface.
For add-ons listed on AMO, we likewise expect a consistent generally positive
user experience for any functionality provided by the add-on.



## Content



While we have no interest in controlling the types of functionality provided
by add-ons in the wild, there are certain types of content that
`addons.mozilla.org` cannot host. In particular, all content hosted on the
site must conform to the laws of the United States, and comply with the
Mozilla [Conditions of Use](https://www.mozilla.org/en-US/about/legal
/acceptable-use/).



## Technical



We try, as much as possible, not to restrict the freedom of developers to
maintain their add-ons as they choose. However, for reasons of security and
our ability to effectively review code, we do have certain technical
requirements. In particular, potentially dangerous APIs, such as those which
evaluate HTML or JavaScript, may only be used in ways which are provably safe,
and code which we cannot verify to behave safely and correctly may need to be
refactored.



## Source Code Submission



Listed and unlisted add-ons may contain binary, obfuscated and minified source
code, but Mozilla must be allowed to review a copy of the human-readable
source code upon request. In such cases, the author will receive a message
\xa0from Mozilla asking for their assistance in the review. The submitted
source code will be reviewed by an administrator and will not be redistributed
in any way. The code will only be used for the purpose of reviewing the add-
on.



Instructions for reproducing obfuscation are also required, please read [the
details of this guideline](/en-US/docs/Mozilla/Add-ons/Source_Code_Submission)
to ensure a swift review.



If your add-on contains code that you don't own or can't get the source code
for, you may [contact us](https://developer.mozilla.org/en-US/Add-
ons/AMO/Policy/Contact) for information on how to proceed.



## Reviewers



Add-ons are reviewed by the [AMO Reviewer Team](https://wiki.mozilla.org/Add-
ons/Reviewers), a group of experienced add-on developers that volunteer to
help the Mozilla project by reviewing add-ons to ensure a stable and safe
experience for users. The [Reviewer
Guide](https://wiki.mozilla.org/AMO/Reviewers/Guide) details how reviewers
evaluate add-ons submitted for review. It is an expanded version of the table
shown above. Developers will receive an email with any updates throughout the
review process. Review times can fluctuate depending on reviewer availability
and the complexity of the add-on being reviewed. Regular updates of review
queue status are posted in the [Add-ons
Blog](https://blog.mozilla.org/addons/).



## Blocklisting



Add-ons that don't meet the bar for Unlisted may qualify for blocklisting,
depending on the extent of their problems. The Add-ons Team will do their best
to contact the add-on's developers and provide a reasonable time frame for the
problems to be corrected before a block is deployed. If an add-on is
considered malicious or its developers have proven unreachable or
unresponsive, or in case of repeat violations, blocklisting may be immediate.



Guideline violations should be [reported via
Bugzilla](https://bugzilla.mozilla.org/enter_bug.cgi?product=Tech%20Evangelism&component
=Add-ons), under Tech Evangelism > Add-ons. Questions can be posted in the
[#addons IRC channel](irc://irc.mozilla.org/addons).

]

  *[AMO]: addons.mozilla.org

