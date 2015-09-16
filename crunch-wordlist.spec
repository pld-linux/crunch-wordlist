# TODO
# - merge/handle crnlib
#   file /usr/bin/crunch from install of crnlib-1.04-2.x86_64 conflicts with file from package crunch-wordlist-3.6-0.2.x86_64
#
Summary:	Wordlist generator
Name:		crunch-wordlist
Version:	3.6
Release:	0.2
License:	GPL v2
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/crunch-wordlist/crunch-%{version}.tgz
# Source0-md5:	1cbab783805d1bd382bd2edf33298108
URL:		http://downloads.sourceforge.net/crunch-wordlist/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A command line program for generating intelligent wordlists.

%prep
%setup -q -n crunch-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CPPFLAGS="%{rpmcppflags}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p crunch $RPM_BUILD_ROOT%{_bindir}/crunch
cp -p unicode_test.lst $RPM_BUILD_ROOT%{_bindir}/unicode_test.lst
cp -p charset.lst $RPM_BUILD_ROOT%{_bindir}/charset.lst
cp -p crunch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/crunch
# FIXME: not the best place
%attr(755,root,root) %{_bindir}/*.lst
%{_mandir}/man1/crunch.1*
