Summary: e-smith server and gateway - email module
%define name e-smith-email
Name: %{name}
%define version 4.15.4
%define release 08
Version: %{version}
Release: %{release}
License: GPL
Vendor: Mitel Networks Corporation
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-email-4.15.4-Muttrc.patch
Patch1: e-smith-email-4.15.4-DontRecreatePseudonyms.patch 
Patch2: e-smith-email-4.15.4-useratdomain.patch
Patch3: e-smith-email-4.15.4-hidesections.patch
Patch4: e-smith-email-4.15.4-hidesections.patch2
Patch5: e-smith-email-4.15.4-SMTPAUTHText.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: e-smith-base >= 4.15.0-39
Requires: e-smith-smtpd
Requires: e-smith-mta
Requires: e-smith-pop3
Requires: e-smith-imap
Requires: e-smith-lib >= 1.15.1-19
Requires: perl(Net::Server::Fork)
Requires: perl(Net::SMTP)
Requires: perl(Authen::SASL)
Requires: perl(Net::Server) >= 0.85
Requires: runit
Obsoletes: e-smith-smtp-authentication
Obsoletes: e-smith-securemail
BuildRequires: e-smith-devtools >= 1.13.0-03
BuildArchitectures: noarch
AutoReqProv: no

%description
e-smith server and gateway software - email module.

%changelog
* Fri Jan 27 2006 Gavin Weight <gweight@gmail.com> 4.15.4-08
- Adjusted text to reflect that SSMTP is enabled by default [SME: 419]

* Wed Jan 25 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.4-07
- Made sectionbar its own item so that it is in the right place
  when the sections are hidden [SME: 561]

* Wed Jan 25 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.4-06
- Hide webmail sections if imp isn't installed
- Hide Spam filtering sections if spamassassin isn't installed
- Hide Virus scan sections if clamav isn't installed [SME: 561]

* Fri Jan 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.4-05
- Don't check whether the user exists when creating user@domain
  pseudonyms - i.e. allow support@dom.ain even if support itself
  hasn't been defined. Of course, dom.ain must exist. [SME: 368]

* Fri Jan 6 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.4-04
- Don't attempt to recreate first.last and first_last pseudonyms
  in bootstrap-console-save. We create them when we create the user,
  and if someone deletes them, that's their choice. [SME: 387]

* Wed Jan 4 2006 Gordon Rowell <gordonr@gormand.com.au> 4.15.4-03
- Add 'set hostname=$DomainName' to /etc/Muttrc [SME: 398]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 4.15.4-02
- Bump release number only

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.4-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.3-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.2-41]
- Change French translation of "Weekend" to the more
  universally acceptable "samedi et dimanche" [SF: 1293855]

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.2-40]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.2-39]
- Cleanups to French L10N - Thanks Didier Rambeau [SF: 1293855]

* Sun Sep 25 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.2-38]
- Actually add German L10N to correct package [SF: 1293325]

* Sun Sep 25 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.15.2-37]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Tue Sep 13 2005 Gordon Rowell <gordonr@gormand.com.au>
- [4.15.2-36]
- Add configuration options for ISP SMTP AUTH to Email delivery page
  [SF: 1236748]

* Wed Sep  7 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-35]
- Add requires header for Authen::SASL module, needed by SMTP auth
  proxy. [SF: 1269111]

* Fri Sep  2 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-34]
- Lexicon updates. Still need more French and Spanish translation
  done. [SF: 1280024]

* Fri Sep  2 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-33]
- Add UI toggles for private/public IMAP/IMAPS/POP/POPS. Thanks for
  patch go to Michael Weinberger! [SF: 1280024]

* Wed Aug 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-32]
- Handle upstream disconnect in smtp-auth-proxy. Use more concise
  proxy code, courtesy of the Perl Cookbook. [SF: 1269414]

* Wed Aug 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-31]
- Improve error reporting in smtp-auth-proxy - return 421 status, and
  log config errors and upstream connect errors to stderr. [SF: 1257015]

* Tue Aug 23 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-30]
- Fix typo in fetchmail settings save part of panel code. [SF: 1265400]

* Wed Aug 10 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-29]
- Remove stray symlink from last patch.

* Wed Aug 10 2005 Shad Lords <slords@mail.com>
- [4.15.2-28]
- Remove last qmail stuff [SF: 1255261]
- Break out pop3 into its own package [SF: 1256055]
- Rename popd service to pop3 [SF: 1256055]
- Include imap database stuff [SF: 1256055]

* Tue Aug  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-27]
- Remove "Obsoletes: e-smith-qmail", and split out all qmail specific stuff.
  [SF: 1255261]

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [4.15.2-26]
- Add TCPProxyPort to specify which port to proxy [SF: 1246986]

* Fri Jul 22 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-25]
- Complete the update to current db access APIs - a few esmith::db and
  esmith::config calls were found hiding.  [SF: 1216546, 1242331]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-24]
- Update all db access APIs to current standards. [SF: 1216546]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-23]
- Fix pop* run scripts to find checkpassword binary via
  PATH search.  [SF: 1239720]
- Various further muttrc configuration changes (from Shad) [SF: 1235454]
  . Fix braces
  . Configure "folder" to use IMAP as well, so we see all IMAP
    folders
  . use URLs instead of PINE style folder names, and use imaps directly

* Thu Jul 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-22]
- Configure /etc/Muttrc to use IMAP
- And expand /etc/Muttrc at same times as /etc/pine.conf
  Patch contributed by Gordon Rowell. [SF: 1235454]

* Tue Jul 12 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-21]
- French L10N Merci - Didier. [ SF:1227389 ] 
- Add some missing Requires: headers. [SF: 1217914]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-20]
- Add Obsoletes headers for a number of email addon packages.
  [SF: 1219069]

* Thu Jun  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-19]
- Four PIF file patterns (AHhUYXgg,AMlIbDk5Lm,AMkgICAg,AHhIYW5k) and
  one more EXE file pattern (TVoAACoAG) - Thanks Hans-Cees Speel

* Fri Jun  3 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-18]
- Another EXE file pattern TVpLRVJOR - Thanks Ray Mitchell
  and Gordon Rowell.

* Tue May 31 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-17]
- Disable all mailpatterns by default [Gordon SF:1202391]
- Change mailpatterns database back to one pattern per entry [Gordon SF:1202391]
- Add two new EXE file patterns - Thanks Ray Mitchell

* Tue May 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-16]
- Make sure that there are empty templates-default files in the
  peers/{o,local} templates directory. Fix up a couple of problems
  in the pop3s run script. [SF: 1206471]

* Wed May 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-15]
- Change db lookup of spamassassin{sortspam} to spamassassin{SortSpam}.
  Expand all users' .qmail files in email-update action. [SF: 1202402]

* Fri May 13 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-14]
- [Patch from Gordon's e-smith-email-4.15.2-13gr02]
- Add missing qmail initscript links [SF:1201092]
- Modify email-update-user to expand ~/.qmail-junkmail
- Add templates for ~/.qmail-junkmail
- This should probably be in e-smith-spamassassin, but that
  would mean another perl invocation for that template

* Thu May  5 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-13]
- Big set of patches from Gordon Rowell.
- Show public pop/public imap/http webmail/smtp auth if they
  are already enabled in that way. Otherwise, only show disabled
  and the pop3s/imaps/https webmail/ssmtp auth version
- Change emailsettings.pm to store most properties in the virtual
  smtpd and ssmtpd records
- Change URL in webmail text to https://
- Various lexicon changes for consistency across the panel
- Use $db->set_prop(thing,prop,value) instead of 
  $db->get(thing)->set_prop(prop,value)
- TODO: The fetchmail settings could easily be done in a loop
- Don't delete DelegateMailServer when empty, just clear the value
- Changed Patterns property to PatternsScan to match VirusScan
- Added lots of defaults for smtpd and ssmtpd:
    smtpd{access}: public
    smtpd{Authentication}: disabled
    smtpd{Instances}: 40
    smtpd{InstancesPerIP}: 5
    smtpd{PatternsScan}: disabled
    smtpd{Proxy}: enabled
    smtpd{status}: enabled
    smtpd{TCPPort}: 25
    smtpd{type}: service
    smtpd{VirusScan}: enabled

    ssmtpd{access}: public
    ssmtpd{Authentication}: enabled
    ssmtpd{Instances}: 10
    ssmtpd{status}: enabled
    ssmtpd{TCPPort}: 465
    ssmtpd{type}: service
- Fix up masq fragment to look at smtpd{Proxy}
- Add migrate frament for smtpfront-qmail properties
- Move mailpatterns defaults to this package
- Delete duplicate Requires: line
- Fix check for smtpd{Authentication} when displaying options

* Mon May  2 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-12]
- Add pseudonyms fragment for virtualdomains template (missed in last
  change).

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-11]
- [All items in this change contributed by Gordon Rowell.]
- Allow separation of mail for bob@domain1 from bob@domain2
- To configure, enter pseudonyms of the form pseudo@domain => user 
  with the following restrictions:
    - pseudo must be a user already configured on the server
    - domain must be a domain alredy configured on the server
    - pseudo may not equal user (since that's the default for all domains)
- Merged in the web interface from Shad Lords' e-smith-spamassassin
  onto the E-mail filtering sub-page
- TODO: We should probably disallow this if only one domain is hosted
  on the server.

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-10]
- [All items in this change contributed by Gordon Rowell.]
- Add e-mail filtering page
- Prepare for migration to qpsmtpd by using $SMTPD and $SSMTPD 
  throughout the panel code
- Changed Requires: from e-smith-mailfront to e-smith-smtpd (which
  is provided by e-smith-qpsmtpd and could be by e-smith-mailfront).
- Add skeleton virus and spam scan toggles. Note that these set
  options in the $SMTPD services and each virus or spam scanner can
  use those as defaults and add additional options as required. For
  example, if $SMTPD{VirusScan} == 'disabled', no virus scanners should
  configure themselves to look at the mail.
- Make patterns status depend on any being selected, which removes a
  redundant toggle

* Thu Apr 28 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-09]
- Drop e-smith-mailfront dependency, to allow switch to qpsmtpd
  if desired.

* Tue Apr 26 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-08]
- Add update of PatternsStatus (patch from Gordon), and fix a few typos.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-07]
- Add missing /var/service/qmail/down file.

* Sun Apr 10 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-06]
- [Patch from Gordon]
- Complete L10N of front page of emailsettings
- Move many panel option hashes into subroutines for re-use on status page
- Move executable content blocking section from subroutine to FM XML
- Open AccountsDB read-only since that's all we need
- Actually fix the evil and unsafe part of the webmail settings code
- Dormant prototype of optional display of multidrop settings regions
- Removed percent from (percent)prep in 4.9.0-01 changelog entry
  to stop mezzanine/rpmbuild failures due to multiple (percent)prep 
  sections (sigh)

* Thu Mar 31 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-05]
- Add template expansion of pop service peers files to email-update,
  as private/public may have changed.

* Tue Mar 29 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-04]
- Fix configuration of ACLs and users-assign files during bootstrap-console-save.

* Sat Mar 26 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-03]
- Ensure that /var/service/qmail/control/1 is executable.

* Thu Mar 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-02]
- Integrate Gordon's changes to break form up into subforms.
  TODO - non-en localisations.

* Thu Mar 24 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.2-01]
- Roll new development stream - 4.15.2

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-30]
- Avoid warning from email panel if patterns are not enabled.
- Avoid crash in panel if DelegateMailServer is being set.

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-29]
- Don't expand /var/qmail/users/assign in generic_template_expand,
  as users/groups may not yet be created. Instead, combine with
  qmail-newu in qmail service control/1 script.

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-28]
- Add missing templates for popd/pop3s peers files.
- Change port specification in popd run file from "pop3" to
  "pop" - tcpsvd doesn't grok "pop3".

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-27]
- Use tcpsvd instead of tcpserver for popd and pop3d. Use sslio
  instead of stunnel for pop3d. TODO - configurable concurrency
  limits.

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-26]
- Remove now obsolete email-assign action.
- Add "Requires: runit"

* Fri Mar 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-25]
- Add missing templates.metadata file for qmail/users/assign.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-24]
- More fixes of path for qmail service directory.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-23]
- Fix paths for qmail service directory in filelist.

* Thu Mar 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-22]
- Move post-upgrade actions to bootstrap-console-save. 

* Wed Mar 16 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-21]
- Include all content from e-smith-qmail (arguably lots of this
  content should move to e-smith-qmail, but this is easier).
- Obsolete email-assign action.

* Mon Mar 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-20]
- Fix dangling symlink.
- Add missing exports in FormMagick::Panel::emailsettings
- Add missing templates for pop3s tcpserver cdb file.

* Fri Mar 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-19]
- Fix dangling symlinks, and add tcpserver cdb support for
  popd and pop3s.

* Fri Mar 11 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-18]
- Fix warning from EmailUnknownUser migrate fragment.

* Thu Mar 10 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-17]
- Fix path to skeletal junkmail Maildir.
- Up memory limits for popd and pop3s run files.
- Add missing /var/log/pop3s directory.

* Wed Mar  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-16]
- Fix some missing checkins from previous version.

* Wed Mar  9 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-15]
- Fold in most of Shad's panel changes, with support for
  imaps and pop3s.
- Add supervised pop3s service.
- Allow pseudonums of pseudonyms.
- Obsolete email-update-shared and email-conf actions.
- Add junkmail maildir to skeletal user dir
- Remove db entry creation code from panel code - now done
  via default fragments.
- Add TCPPort property of popd (and pop3s).

* Wed Feb 23 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-14]
- Remove bogus dependency on sortspam.

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-13]
- Remove obsolete email-startup-links action. [MN00065651]
- Obsolete email-sighup and smtp-auth-proxy-restart by using generic
  services-adjust action. Remove unused email-restart action. 
  Update e-smith-lib dependency. [MN00065576]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-12]
- Remove conf-fetchmail action - done by default fragments. [MN00064329]
- Include ~alias/.qmail-default symlink in rpm. [MN00064230]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]

* Mon Jan  3 2005 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-11]
- Add default "abuse" pseudonym. [MN00062658]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-10]
- Remove no longer needed conf-migrate-* actions. [charlieb MN00062545]
- Fix "Visisble" typo in default "everyone" pseudonym. [charlieb MN00046951]
- Don't restart auth proxy in bootstrap-console-save [charlieb MN00062549]

* Mon Dec 27 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-09]
- Untaint pseudonym before using in system(). [charlieb MN00050161]

* Thu Nov 11 2004 Charlie Brady <charlieb@e-smith.com>
- [4.15.1-08]
- Fix ownership and permissions of ~alias [charlieb MN00057000]

* Tue Sep 28 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-07]
- Updated requires with new perl dependencies. [msoulier MN00040240]

* Mon Jun 21 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-06]
- Updated requires. 

* Tue May 11 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-05]
- Added validation to the AdminEmail field. [msoulier MN00023812]

* Mon May 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-04]
- Made filtering via SA the default preprocessing action for all email.
  [msoulier MN00027881]

* Tue May  4 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-03]
- Added defaults fragments for all smtp-auth-proxy properties.
  [msoulier 4728]

* Tue May  4 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-02]
- Updating dependencies.

* Tue May  4 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.1-01]
- Rolling as-source to collect patches.

* Tue May  4 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-07]
- Patches run script to provide FQDN in POP3 login. [msoulier dpar-27887]

* Wed Feb 18 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-06]
- Updated template for admin's .qmail file. [msoulier dpar-20868]

* Tue Feb 17 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-05]
- Updated template for home directory .qmail files to support change in
  sortspam to allow .qmail files more control over mail delivery. 
  [msoulier dpar-20868]

* Thu Feb 12 2004 Mark Knox <markk@e-smith.com>
- [4.15.0-04]
- Fwd port of 10064: fixed expansion of /etc/fetchmail in email-update event
  [markk 11026]

* Mon Feb  9 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-03]
- Updated the Requires list and fixed a couple of minor problems.
  [msoulier 4728]

* Mon Feb  9 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-02]
- Adding Charlie's smtp-auth-proxy, and putting it under supervision.
  [msoulier 4728]

* Mon Jan 26 2004 Michael Soulier <msoulier@e-smith.com>
- [4.15.0-01]
- rolling to dev - 4.15.0

* Sun Sep 21 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-08]
- Remove duplicate primary domain name in multidrop fetchmail template
  [charlieb 10064]

* Wed Aug 27 2003 Michael Soulier <msoulier@e-smith.com>
- [4.14.0-07]
- Added K* init symlinks to runlevels 0, 1 and 6 for popd. [msoulier 9761]

* Fri Aug 22 2003 Michael Soulier <msoulier@e-smith.com>
- [4.14.0-06]
- Removed the conditional around the SMTPProxy creation code. [msoulier 9572]
- Changed the trigger property for the SMTPProxy to "Proxy", in
  smtpfront-qmail. [msoulier 9572]

* Tue Aug 19 2003 Michael Soulier <msoulier@e-smith.com>
- [4.14.0-05]
- Added an smtp-proxy db record to permit enabling/disabling of the smtp
  proxy. [msoulier 9572]

* Wed Jul 16 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-04]
- Add junkmail maildir to skel home directory. [charlieb 9475]

* Thu Jul  3 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-03]
- Use qmail delivery properties to determine local delivery instructions for
  admin user. [charlieb 9198, 9255]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-02]
- Ensure that admin has a .qmail file.
  [charlieb 9198]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [4.14.0-01]
- Changing version to stable stream number - 4.14.0

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-63]
- Spanish nav bar [gordonr 9153]

* Tue Jun 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-62]
- Added pseudonym for anonymous [gordonr 9127]

* Thu Jun 19 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-61]
- Fix bug with format of ETRN fetchmail invocation. [charlieb 9077]

* Thu Jun 19 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-60]
- Add some defaults for fetchmail, including Method|standard
  [gordonr 8921]

* Wed Jun 11 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-59]
- Add log/run script which was missing from last checkin. [charlieb 8903]

* Wed Jun 11 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-58]
- Use tcpserver/supervise rather than xinetd to handle POP connections. Need new
  genfilelist to handle the permissions under /var/service. [charlieb 8903]

* Wed Jun  4 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-57]
- Fix devnull pre-defined alias definition. Use defaults mechanism to reserve
  devnull alias. Use same mechanism for postmaster, mailer-daemon, and everyone
  pseudonyms. [charlieb 6460]

* Tue Jun  3 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-56]
- Change default status for fetchmail to "disabled". [charlieb 8921]

* Fri May 30 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-55]
- Removed dangling symlink to email-startup. [msoulier 8808]

* Tue May 20 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-54]
- Fixed expectation of email-update-group so that it can handle user-deleted
  and group-deleted. [msoulier 6414]

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-53]
- Add Spanish lexicon for emailsettings and pseudonyms [lijied 3793]

* Tue Apr 29 2003 Tony Clayton <apc@e-smith.com>
- [4.13.0-52]
- Add default db fragments for qmail/popd/fetchmail services [tonyc 8537]
- Remove dead email-startup action [tonyc 8537]

* Mon Apr 14 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-51]
- Changed the interface to email-update-group to accept either no second
  argument, or a group or user. [msoulier 8103]

* Mon Apr 14 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-50]
- Removed email-update-all-groups and modified email-update-group to handle
  its functionality. [msoulier 8103]

* Mon Apr 14 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-49]
- Remove email-relocate-maildirs action - it's moving to e-smith-imap.
  [charlieb 8273]

* Fri Apr 11 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-48]
- Modified French button name [lijied 7921]

* Fri Apr 11 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-47]
- Modified button name [lijied 7921]

* Thu Apr 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-46]
- Using the createlinks script for symlink creation for consistency.
  [msoulier 6414]

* Thu Apr 10 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-45]
- Fixed lack of & in front of addresses generated by email-update-all-groups.
  [msoulier 6414]
- Fixed lack of use of processTemplate in email-update-group. [msoulier 6414]
- Added a symlink to email-update-all-groups in user-delete. [msoulier 6414]

* Wed Apr  9 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-44]
- Add creation of ~admin/.qmail-default symlink. Move email-update-user
  action from post-upgrade to bootstrap-console-save, so it is run
  at post-install as well. [charlieb 7660]

* Tue Apr  8 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-43]
- Modified pseudonym button name [lijied 7921]

* Tue Apr  8 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-42]
- Fixed fr nav bar [gordonr 7926]

* Mon Apr  7 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-41]
- Change email-update-user action to loop through all users if
  username not given. Link into post-upgrade action. Create
  .qmail-default symlink if it doesn't already exist.
  [charlieb 7609]

* Fri Apr  4 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-40]
- Changed $q->table to $q->start_table where necessary [lijied 8034]

* Thu Apr  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-39]
- Missing english L10N in emailsettings [gordonr 1950]

* Wed Apr  2 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-38]
- Removed 'Mitel Networks SME Server' branding on emailsetting
  and pseudonyms [lijied 8016]
- Changed Copyright header to License. [charlieb]
- Add local delivery options in .qmail template - use
  DeliveryType and DeliveryInstruction properties of qmail.
  [charlieb 2600]

* Wed Apr  2 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-37]
- Modify email-relocate-maildirs to ensure that Mail/junkmail
  folder exists for all users. [charlieb 2600]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-36]
- Redirect outbound port 25 through our SMTP server [gordonr 6349]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-35]
- Changed to ~alias/.qmail-devnull-default [gordonr 6460]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-34]
- Added ~alias/.qmail-devnull [gordonr 6460]

* Tue Apr  1 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-33]
- Modified emailsetting en-us 'standard' trans text [lijied 7949]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-32]
- Fixed fr nav bar entry [gordonr 7926]

* Mon Mar 31 2003 Mike Dickson <miked@e-smith.com>
- [4.13.0-31]
- fixed the "Action" column to be several columns instead of one [miked 7761]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-30]
- Make use of sectionbar hr CSS class [gordonr 7911]

* Mon Mar 31 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-29]
- And make section bars only 80% of the width to its obvious there's one
  Save button for the page [gordonr 7911]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-28]
- Lighten section bars a little [gordonr 7911]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-27]
- Strengthen section headings to show blocks [gordonr 1950]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-26]
- Deleted dangling panel links after panel merge [gordonr 1950]

* Fri Mar 28 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-25]
- Adding French L10Ns [gordonr 1950]

* Thu Mar 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-24]
- Rearranged panel order slightly to group like items [gordonr 1950]
- Adjusted titles of the two delegate mail server (upstream/downstream)
  items [gordonr 1950]
- TODO: Some missing French L10Ns (tagged in lexicon) [gordonr 1950]

* Thu Mar 27 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-23]
- Deleted emailretrieval/otheremail - now merged into emailsettings 
  [gordonr 1950]
- Made emailsettings panel loop back to start and display 
  success/failure message [gordonr 1950]

* Thu Mar 27 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-22]
- Modified emailretrieval and emailsettings en-us text [lijied 4937]
- Modified emailretrieval and emailsettings fr-ca text [lijied 4937]
  and modified the lexicons to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Tue Mar 25 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-21]
- Modified emailsettings access text [lijied 4081]

* Tue Mar 25 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-20]
- And add panel link [gordonr 1950]
- Change page title to "E-mail settings' and nav bar to 'e-mail'
  in English and French [gordonr 1950]
- Modified otheremail POP and IMAP server access text [lijied 4081]

* Mon Mar 24 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-19]
- Merge emailretrieval/othermail -> emailsettings [gordonr 1950]

* Tue Mar 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-18]
- Added [$ExternalIP] to "locals" [gordonr 6900]

* Tue Mar 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-17]
- Deleted ./etc/{fetchmail, startmail}/template-begin,
  and modified %build [lijied 3295]
- Reconfigure/reload /var/qmail/control/locals on ip-change [gordonr 6900]

* Tue Mar 18 2003 Gordon Rowell <gordonr@e-smith.com>
- [4.13.0-16]
- Broken rebuild - missing mkdir in %build

* Fri Mar  7 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-15]
- Modified panel order for emailretrieval,otheremail 
  and pseudonyms
- Modified en-us and fr-ca pseudonyms panel title [lijied 7356] 

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-14]
- Split en-us lexicon from emailretrieval panel
  split en-us lexicon from otheremail panel
  split en-us lexicon from pseudonyms panel  [lijied 4030]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-13]
- RebuildRPM for otheremail and pseudonyms [lijied 5003]

* Mon Mar  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.13.0-12]
- RebuildRPM for emailretrival, commit missed last time [lijied 5003]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-11]
- Added French lexicon for emailretrieval, otheremail
  and pseudonyms. [lijied 5003]
- Re-do hosts.allow template to use esmith::ConfigDB::hosts_allow_spec.
  Add dependency on up-to-date e-smith-lib. [charlieb 5650]
- Remove bogus mailfront dependency.

* Tue Feb 25 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-10]
- Convert virtualdomains template to use esmith::{Hosts,Domains}DB.
  [charlieb 2670]
- Remove duplicate DomainName setting from virtualdomains template,
  now that the primary domain is added to the domains db. [charlieb 2670]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-09]
- Removed use of LocalDomainPrefix. [msoulier 4812]

* Sat Jan 25 2003 Mike Dickson <miked@e-smith.com>
- [4.13.0-08]
- added ACTION to the lexicon [miked 6363]

* Wed Jan 15 2003 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-07]
- Change pattern match for ppp device in /etc/startmail, so that
  mail collection is triggered on a PCI ISDN dialup link [charlieb 5399]
- Remove standard template-{begin,end} fragments where possible. The
  default ones will be used in their place [charlieb 3295]

* Thu Jan  9 2003 Michael Soulier <msoulier@e-smith.com>
- [4.13.0-06]
- Fixed incorrect page flow behaviour. Panel now returns to start page on
  completion, with a status message prefixed. [msoulier 6470]

* Fri Dec 27 2002 Mike Dickson <miked@e-smith.com>
- [4.13.0-05]
- minor UI updates [miked 5494]

* Mon Dec 16 2002 Mike Dickson <miked@e-smith.com>
- [4.13.0-04]
- UI Update, part of the tweaking for the new UI [miked 5494]

* Mon Dec  2 2002 Mike Dickson <miked@e-smith.com>
- [4.13.0-03]
- ui update  [miked 5494]

* Thu Nov 21 2002 Mike Dickson <miked@e-smith.com>
- [4.13.0-02]
- update to new UI system [miked 5494]

* Wed Nov  6 2002 Charlie Brady <charlieb@e-smith.com>
- [4.13.0-01]
- Rolling development stream version to 4.13.0

* Tue Oct 15 2002 Charlie Brady <charlieb@e-smith.com>
- [4.12.1-01]
- Roll new version to fix tagging problem

* Tue Oct 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.12.0-02]
- If the user had a maildir called Mail/, rename it so it gets 
  relocated into the new directory Mail/. Attempt to relocate as
  many directories as possible - only warn when directories can't
  be renamed rather than calling die(). [gordonr 4767]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [4.12.0-01]
- Roll to maintained version number to 4.12.0

* Tue Oct  8 2002 Mark Knox <markk@e-smith.com>
- [4.11.8-05]
- Removed stray description tag [markk 5135]

* Tue Sep 24 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.8-04]
- Re-add "use esmith::util" to email-update-group - it was lost in the
  esmith::AccountsDB rewrite. [charlieb 4932]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.8-03]
- Fix creation of list of groups from groupname in last change [charlieb 4932]

* Fri Sep 20 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.8-02]
- Modify email-update-group to iterate over all groups during post-upgrade
  event [charlieb 4932]

* Mon Sep  9 2002 Mark Knox <markk@e-smith.com>
- [4.11.8-01]
- Rolling to new version to fix patching problem

* Mon Sep  9 2002 Mark Knox <markk@e-smith.com>
- [4.11.7-06]
- Display only multidrop retrieval in private s&g mode [markk 4780]

* Mon Sep  9 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.7-05]
- Use localhost for all fetchmail local delivery [charlieb 4742]

* Thu Sep  5 2002 Mark Knox <markk@e-smith.com>
- [4.11.7-04]
- Remove empty description and lexicon entry [markk 4764]

* Wed Sep  4 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.7-03]
- Relocate maildirs for all users and admin to Mail/ subdirectory
  in post-upgrade event. Directories which didn't exist in Mail/ 
  preserve their name. Directories which conflict with an existing
  directory in Mail/ become {name}.relocated and if that conflicts,
  we try {name}.relocated-time(). If that conflicts, we generate a
  warning to the log and give up. [gordonr 4767]

* Fri Aug 30 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.7-02]
- Update default pine configuration to deal with TLS capable imapd,
  and to support a few more features.  [charlieb 3669]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.7-01]
- Use new adjust-masq action script to adjust packet filter, rather than
  restart-masq. [charlieb 4501]

* Fri Jul 26 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.6-01]
- Return exit status from /etc/startmail if it is called, 0 otherwise.
  [charlieb 4487]

* Fri Jul 26 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.5-01]
- Add missing space after --authentication option. [charlieb 3050]

* Fri Jul 26 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.4-01]
- Call /etc/startmail from email-ipup, rather than /etc/fetchmail, so that
  $SMTP is set. [charlieb 4483]

* Wed Jul 24 2002 Mark Knox <markk@e-smith.com>
- [4.11.3-01]
- Fixed faulty display of multidrop params [markk 4453]
- Added fetch of POP password [markk 4453]

* Wed Jul 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.2-01]
- Added optional property fetchmail|AuthenticationMethod, defaulting to
  "password" so that people with working CRAM-MD5 or similar can still
  choose that (or indeed "any" if it works for them) [gordonr 3050]

* Wed Jul 24 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.11.1-01]
- Added --auth password to fetchmail call to force password
  authentication [gordonr 3050]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [4.11.0-01]
- Changing version to maintained stream number to 4.11.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [4.10.0-01]
- Changing version to maintained stream number to 4.10.0

* Tue May 28 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.25-01]
- Fix multi-drop sort. 'on' and 'off' were confused in "select sort
  method" in the panel. [charlieb 3682]

* Tue May 28 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.24-01]
- Fix forward unknonw email to admin, which was broken in the FormMagick
  conversion. [charlieb 3683]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.23-01]
- RPM rebuild forced by cvsroot2rpm

* Wed May 22 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.22-01]
- Set smtp-server=localhost in pine.conf [gordonr 3567]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [4.9.21-01]
- Fixed heading on panel [markk 3516]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [4.9.20-01]
- Bold table headings [markk 3503]

* Thu May 16 2002 Kirrily Robert <skud@e-smith.com>
- [4.9.19-01]
- Added border to pseudonyms table [skud 3491]

* Thu May 16 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.18-01]
- Remove migration of smtpfwdd properties and init of smtpfront-qmail
  service - moved to e-smith-mailfront. [charlieb 3442]
- Fix fetchmail delivery - we need to use smtphost, not smtpaddress.
- Append @$DomainName to "postmaster" for postmaster address - 
  fetchmail otherwise uses postmaster@a.b.c.d [charlieb 3469]
- Remove commented out SMTP address lookup in /etc/fetchmail script -
  it's now passed in from /etc/startmail (and we have CVS for version
  control) [ charlieb 3469].

* Fri May 10 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.17-01]
- Handle concurrencyremote setting of zero [gordonr 2920]

* Mon May  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.16-01]
- Localise SAVE button [gordonr 3222]

* Mon May  6 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.15-01]
- Removed CVS detritus from changelog.
- Changed references to smtpd db entries to smtpfront-qmail. [charlieb 2604]
- Added blank or IP validator. Changed ip_number to new validation in
  emailretrieval [markk 3317]

* Fri May  3 2002 Mark Knox <markk@e-smith.com>
- [4.9.14-01]
- Changed lexicon en -> en-us [markk 3320]
- Removed unused "TITLE" on first page [markk 3320]
- Added status message display on first page [markk 3320]
- Cleaned up display in IE [markk 3320]
- Localised "Everyone" [markk 3320]
- Cleaned up die calls in module for better error handling [markk 3320]

* Thu May  2 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.13-01]
- Enable smtpd service by default. Migrate status and filter properties
  from smtpfwdd to smtpd service, if found. [charlieb 2604]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.12-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Tue Apr 30 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.11-01]
- Quote fetchmail username and password [gordonr 3296]

* Fri Apr 26 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.10-01]
- Removed /var/qmail/control/rcpthosts/template-{begin,end} [gordonr 2604]

* Thu Apr 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.9-01]
- Added head/foot to pseudonyms [gordonr 3223]
- Nav bar entries to all panels [gordonr 3155]

* Mon Apr 22 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.8-01]
- Removed bogus hard quotes on call to serviceControl [gordonr 2920]
- Changed navigation for email retrieval to "E-mail" as per
  glossary [gordonr 3155]

* Fri Apr 19 2002 Mark Knox <markk@e-smith.com>
- [4.9.7-01]
- Changed some db->get()s to check their return values. Was causing breakage
  in otheremail panel on fresh install. [markk]

* Fri Apr 19 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.6-01]
- Allow optional qmail|ConcurrencyRemote setting which overrides the
  memory sized based heuristic [gordonr 2920]

* Fri Apr 19 2002 Mark Knox <markk@e-smith.com>
- [4.9.5-01]
- Removed hardcoded server name and replaced with lookup of FQDN [markk 3196]

* Thu Apr 18 2002 Mark Knox <markk@e-smith.com>
- [4.9.4-01]
- Pass SMTP on the command line as the env is cleared [markk 3161]
- Pass LocalIP if ExternalIP doesn't exist [markk 3161]

* Thu Apr 18 2002 Mark Knox <markk@e-smith.com>
- [4.9.3-01]
- Extract ExternalIP in /etc/startmail and export as ENV{SMTP} to 
  /etc/fetchmail to avoid calling privileged commands as user qmailr 
  [markk 3161]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.9.2-01]
- Language en->en-us

* Mon Apr  8 2002 Michael Schwern <schwern@e-smith.com>
- [4.9.1-01]
- Added i18n'd versions of emailretrieval and otheremail panels [skud 3032]

* Fri Mar 15 2002 Charlie Brady <charlieb@e-smith.com>
- [4.9.0-01]
- rollRPM: Rolled version number to 4.9.0-01. Includes patches up to 4.8.0-07.
- Removed empty directories from tarball and add code to make them in prep
  section, prior to CVS import.

* Thu Feb 14 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-07]
- Remove the current qmail rcpthosts template and replace it with a
  template directory containing zero length template-begin and template-end
  files. The current template containing "not used" comments is moved
  into the e-smith-obtuse-smtpd RPM.

* Mon Jan 28 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-06]
- Re-instate 4.8.0-02 patch. See #2677.

* Fri Jan 18 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-05]
- Use external IP as SMTP address when using multidrop mail, so that
  external network smtpd rules are applied to address matches. We have to
  fall back to LocalIP in serveronly mode, unfortunately, because we have
  no other option.

* Fri Dec 21 2001 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-04]
- Temporarily back out 4.8.0-02 patch, pending further verification.

* Fri Dec 21 2001 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-03]
- Fix typo "smptroutes" => "smtproutes" in email-conf.

* Wed Dec 12 2001 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-02]
- Fix a few problems with email-ipup script which lead to warnings being
  logged.
- Trucate the changelog, which is getting very large. For earlier changelog,
  see an earlier version of the package.

* Tue Dec 11 2001 Adrian Chung <mac@e-smith.com>
- [4.8.0-01]
- rollRPM: Rolled version number to 4.8.0-01. Includes patches up to 4.7.0-12.

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.6.1-01]
- Rolled version number to 4.6.1-01. Includes patches upto 4.6.0-06.

* Tue Aug 21 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.6.0-02..06]
- Final branding changes

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-01]
- Rolled version number to 4.6.0-01. Includes patches upto 4.5.0-20.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
mkdir -p root/var/lock/fetchmail
mkdir -p root//etc/e-smith/skel/user/Maildir/.junkmail/{tmp,new,cur}

%build
perl createlinks

mkdir -p root/etc/e-smith/templates/etc/fetchmail
ln -s /etc/e-smith/templates-default/template-begin-shell \
      root/etc/e-smith/templates/etc/fetchmail/template-begin

mkdir -p root/etc/e-smith/templates/etc/startmail
ln -s /etc/e-smith/templates-default/template-begin-shell \
      root/etc/e-smith/templates/etc/startmail/template-begin

mkdir -p root/service

# smtp-auth-proxy supervision
mkdir -p root/var/service/smtp-auth-proxy
ln -s ../var/service/smtp-auth-proxy root/service/smtp-auth-proxy
mkdir -p root/var/service/smtp-auth-proxy/supervise
mkdir -p root/var/service/smtp-auth-proxy/log/supervise
mkdir -p root/var/log/smtp-auth-proxy

rm -rf root/etc/e-smith/templates/var

%postun

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT	\
    --dir /var/lock/fetchmail 'attr(755,qmailr,qmail)' \
    --dir '/var/service/smtp-auth-proxy' 'attr(1755,root,root)' \
    --file '/var/service/smtp-auth-proxy/down' 'attr(0644,root,root)' \
    --file '/var/service/smtp-auth-proxy/run' 'attr(0755,root,root)' \
    --dir '/var/service/smtp-auth-proxy/supervise' 'attr(0700,root,root)' \
    --dir '/var/service/smtp-auth-proxy/log' 'attr(0755,root,root)' \
    --file '/var/service/smtp-auth-proxy/log/run' 'attr(0755,root,root)' \
    --file '/var/service/smtp-auth-proxy/log/supervise' 'attr(0700,root,root)' \
    --dir '/var/log/smtp-auth-proxy' 'attr(2750,smelog,nofiles)' \
    --file '/usr/local/sbin/smtp-auth-proxy.pl' 'attr(0755,root,root)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
