%define         crda_version    3.18
%define         regdb_version   2020.04.29

%global         _firmwarepath	/usr/lib/firmware
%global		_udevrulesdir	/usr/lib/udev/rules.d

Name:           crda
Version:        %{crda_version}_%{regdb_version}
Release:        1%{?dist}
Summary:        Regulatory compliance daemon for 802.11 wireless networking
BuildArch:      noarch

Group:          System Environment/Base
License:        ISC
URL:            https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
BuildRoot:      %{_tmppath}/%{name}-%{crda_version}-%{release}-root-%(%{__id_u} -n)

Requires:       udev, iw
Requires:       systemd >= 190
Requires:       kernel >= 4.15

Source0:        http://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-%{regdb_version}.tar.xz
Source1:        setregdomain
Source2:        setregdomain.1
Source3:        85-regulatory.rules

Patch0:         wireless-regdb-install_db.patch

%description
The crda package provideds the regulatory rules database
"wireless-regdb" used by the kernels 802.11 networking stack
in order to comply with radio frequency regulatory rules around
the world.

%prep
%setup -q -c
%patch0 -p0 -b .install_db

%install
cd wireless-regdb-%{regdb_version}
make install_db DESTDIR=%{buildroot} MANDIR=%{_mandir} \
	FIRMWARE_PATH=%{_firmwarepath}

install -D -pm 0755 %SOURCE1 %{buildroot}%{_sbindir}/setregdomain
install -D -pm 0644 %SOURCE2 %{buildroot}%{_mandir}/man1/setregdomain.1
install -D -pm 0644 %SOURCE3 %{buildroot}%{_udevrulesdir}/85-regulatory.rules

%files
%defattr(-,root,root,-)
%{_sbindir}/setregdomain
%{_udevrulesdir}/85-regulatory.rules
%{_firmwarepath}/regulatory.db
%{_firmwarepath}/regulatory.db.p7s
%{_mandir}/man1/setregdomain.1*
%{_mandir}/man5/regulatory.db.5*
%license wireless-regdb-%{regdb_version}/LICENSE
%doc wireless-regdb-%{regdb_version}/README

%changelog
* Mon Nov 09 2020 Jarod Wilson <jarod@redhat.com> - 2020.04.29-1
- Update to wireless-regdb 2020.04.29 release for additional US spectrum
- Resolves: rhbz#1892700

* Mon Apr 01 2019 John W. Linville <linville@redhat.com> -  2018.05.31-4
- Bump NVR to test CI-related build changes
- Correct Release value for preceding changelog entry

* Fri Jul 27 2018 Stanislaw Gruszka <sgruszka@redhat.com> - 2018.05.31-3
- Remove crda package, since kernel 4.15 is sufficient to provide only
  wireless-regdb package

* Tue Jun 26 2018 Stanislaw Gruszka <sgruszka@redhat.com> - 3.18_2018.05.31-2
- Update wireless-regdb to 2018.05.31
- Remove python2 dependency
- Use sforshee signed reulatory.bin (required by modern kernels)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.18_2016.02.08-7
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18_2016.02.08-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.18_2016.02.08-5
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18_2016.02.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18_2016.02.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18_2016.02.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 09 2016 John W. Linville <linville@redhat.com> - 3.18_2016.02.08-1
- Update wireless-regdb to version 2016.02.08
- Do not treat unused-const-variable warnings as errors

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18_2015.10.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov  3 2015 John W. Linville <linville@redhat.com> - 3.18_2015.10.22-1
- Update wireless-regdb to version 2015.10.22
- Fix some whitespace damage in spec file

* Fri Aug 14 2015 Adam Jackson <ajax@redhat.com> 3.18_2015.04.06-3
- Pass rpm's ldflags through to fix hardening

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18_2015.04.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 John W. Linville <linville@redhat.com> - 3.18_2015.04.06-1
- Update wireless-regdb to version 2015.04.06

* Fri Mar 20 2015 John W. Linville <linville@redhat.com> - 3.18_2015.03.13-1
- Update wireless-regdb to version 2015.03.13

* Wed Feb  4 2015 John W. Linville <linville@redhat.com> - 3.18_2015.01.30-3
- Use %%license instead of %%doc for file containing license information
- Add %%license entry for wireless-regdb
- Correct NVR info at end of previous changelog entry

* Mon Feb  2 2015 John W. Linville <linville@redhat.com> - 3.18_2015.01.30-2
- Update crda to version 3.18
- Update wireless-regdb to version 2015.01.30
- Drop patch to add DESTDIR in install rules for libreg in crda Makefile

* Tue Nov 25 2014 John W. Linville <linville@redhat.com> - 3.13_2014.11.18-1
- Update wireless-regdb to version 2014.11.18

* Mon Oct 27 2014 John W. Linville <linville@redhat.com> - 3.13_2014.10.07-1
- Update wireless-regdb to version 2014.10.07
- Update copyright dates in setregdomain

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13_2014.06.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 John W. Linville <linville@redhat.com> - 3.13_2014.06.13-1
- Update wireless-regdb to version 2014.06.13

* Fri Jun  6 2014 John W. Linville <linville@redhat.com> - 3.13_2014.06.02-1
- Add logger commands to setregdomain to make it more communicative
- Update wireless-regdb to version 2014.06.02

* Fri Feb 28 2014 John W. Linville <linville@redhat.com> - 3.13_2013.11.27-2
- Accomodate relative pathnames in the symlink for /etc/localtime

* Fri Feb 14 2014 John W. Linville <linville@redhat.com> - 3.13_2013.11.27-1
- Update crda to version 3.13
- Remove obsolete patch for regdbdump to display DFS region
- Add patch to use DESTDIR rule for crda libreg installation
- Add patch to avoid calling ldconfig from crda Makefile
- Remove PREFIX='' lines from make commands
- Use SBINDIR and LIBDIR definitions in make commands

* Thu Jan 23 2014 John W. Linville <linville@redhat.com> - 1.1.3_2013.11.27-3
- Correct a typo in setregdomain

* Fri Jan 17 2014 John W. Linville <linville@redhat.com> - 1.1.3_2013.11.27-2
- Add patch for regdbdump to display DFS region

* Mon Dec  2 2013 John W. Linville <linville@redhat.com> - 1.1.3_2013.11.27-1
- Update wireless-regdb to version 2013.11.27

* Fri Nov 22 2013 Xose Vazquez Perez <xose.vazquez@gmail.com> - 1.1.3_2013.02.13-5
- fixed wrong dates
- link with libnl3
- new home for sources

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3_2013.02.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr  3 2013 John W. Linville <linville@redhat.com> - 1.1.3_2013.02.13-3
- setregdomain: remove sed and awk calls
- setregdomain: reimplement COUNTRY assignment with shell function

* Fri Mar  1 2013 John W. Linville <linville@redhat.com> - 1.1.3_2013.02.13-2
- Bump release to prevent upgrade issues from F17...oops!

* Wed Feb 13 2013 John W. Linville <linville@redhat.com> - 1.1.3_2013.02.13-1
- Update wireless-regdb to version 2013.02.13

* Tue Feb 12 2013 John W. Linville <linville@redhat.com> - 1.1.3_2013.02.12-1
- Update wireless-regdb to version 2013.02.12

* Fri Jan 25 2013 John W. Linville <linville@redhat.com> - 1.1.3_2013.01.11-2
- Update setregdomain to determine timezone info from /etc/timezone

* Fri Jan 25 2013 John W. Linville <linville@redhat.com> - 1.1.3_2013.01.11-1
- Update crda to version 1.1.3
- Update wireless-regdb to version 2013.01.11

* Fri Aug 10 2012 John W. Linville <linville@redhat.com>
- Add BuildRequires for openssl

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2_2011.04.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2_2011.04.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 John W. Linville <linville@redhat.com> 1.1.2_2011.04.28-1
- Update crda to version 1.1.2
- Update wireless-regdb to version 2011.04.28 
- Fix mis-numbered version comment in changelog for Nov 23 2010

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1_2010.11.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 23 2010 John W. Linville <linville@redhat.com> 1.1.1_2010.11.22-1
- Update wireless-regdb to version 2010.11.22 

* Thu Feb 25 2010 John W. Linville <linville@redhat.com> 1.1.1_2009.11.25-3
- Correct license tag from BSD to ISC
- Comment purpose of regulatory-rules-setregdomain.patch
- Add copyright and license statement to setregdomain
- Add comment for why /lib is hardcoded in files section
- Reformat Dec 21 2009 changelog entry so rpmlint stops complaining

* Tue Jan 26 2010 John W. Linville <linville@redhat.com> 1.1.1_2009.11.25-2
- Change RPM_OPT_FLAGS to optflags
- Leave man page compression to rpmbuild
- Correct date in previous changelog entry

* Tue Jan 26 2010 John W. Linville <linville@redhat.com> 1.1.1_2009.11.25-1
- Update for crda version 1.1.1

* Mon Dec 21 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.11.25-5
- Remove unnecessary explicit Requries for libgcrypt and libnl -- oops!

* Mon Dec 21 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.11.25-4
- Add libgcrypt and libnl to Requires

* Mon Dec 21 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.11.25-3
- Add man page for setregdomain (from Andrew Hecox <ahecox@redhat.com>)
- Change $RPM_BUILD_ROOT to buildroot

* Fri Dec 18 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.11.25-2
- Specify path to iw in setregdomain

* Wed Dec  2 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.11.25-1
- Update wireless-regdb to version 2009.11.25 

* Wed Nov 11 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.11.10-1
- Update wireless-regdb to version 2009.11.10 

* Thu Oct  1 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.09.08-3
- Move regdb to /lib/crda to facilitate /usr mounted over wireless network

* Wed Sep  9 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.09.08-2
- Use kernel-headers instead of kernel-devel

* Wed Sep  9 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.09.08-1
- Update wireless-regdb to version 2009.09.08 
- Start resetting release number with version updates

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0_2009.04.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 13 2009 John W. Linville <linville@redhat.com> 1.1.0_2009.04.17-11
- Update crda version to version 1.1.0
- Update wireless-regdb to version 2009.04.17 

* Fri Apr 17 2009 John W. Linville <linville@redhat.com> 1.0.1_2009.04.16-10
- Update wireless-regdb version to pick-up recent updates and fixes (#496392)

* Tue Mar 31 2009 John W. Linville <linville@redhat.com> 1.0.1_2009.03.09-9
- Add Requires line for iw package (#492762)
- Update setregdomain script to correctly check if COUNTRY is set

* Thu Mar 19 2009 John W. Linville <linville@redhat.com> 1.0.1_2009.03.09-8
- Add setregdomain script to set regulatory domain based on timezone
- Expand 85-regulatory.rules to invoke setregdomain script on device add

* Tue Mar 10 2009 John W. Linville <linville@redhat.com> 1.0.1_2009.03.09-7
- Update wireless-regdb version to pick-up recent updates and fixes (#489560)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1_2009.01.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 John W. Linville <linville@redhat.com> 1.0.1_2009.01.30-5
- Recognize regulatory.bin files signed with the upstream key (#484982)

* Tue Feb 03 2009 John W. Linville <linville@redhat.com> 1.0.1_2009.01.30-4
- Change version to reflect new wireless-regdb upstream release practices
- Update wireless-regdb version to pick-up recent updates and fixes (#483816)

* Tue Jan 27 2009 John W. Linville <linville@redhat.com> 1.0.1_2009_01_15-3
- Update for CRDA verion 1.0.1
- Account for lack of "v" in upstream release tarball naming
- Add patch to let wireless-regdb install w/o being root

* Thu Jan 22 2009 John W. Linville <linville@redhat.com> v0.9.5_2009_01_15-2
- Revamp based on package review comments

* Tue Jan 20 2009 John W. Linville <linville@redhat.com> v0.9.5_2009_01_15-1
- Initial build
