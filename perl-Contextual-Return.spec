#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : perl-Contextual-Return
Version  : 0.004014
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Contextual-Return-0.004014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Contextual-Return-0.004014.tar.gz
Summary  : 'Create context-sensitive return values'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Contextual-Return-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Want)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Contextual::Return version 0.004014
This module provides a collection of named blocks that allow a return
statement to return different values depending on the context in which it's
called. For example:

%package dev
Summary: dev components for the perl-Contextual-Return package.
Group: Development
Provides: perl-Contextual-Return-devel = %{version}-%{release}
Requires: perl-Contextual-Return = %{version}-%{release}

%description dev
dev components for the perl-Contextual-Return package.


%package perl
Summary: perl components for the perl-Contextual-Return package.
Group: Default
Requires: perl-Contextual-Return = %{version}-%{release}

%description perl
perl components for the perl-Contextual-Return package.


%prep
%setup -q -n Contextual-Return-0.004014
cd %{_builddir}/Contextual-Return-0.004014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Contextual::Return.3
/usr/share/man/man3/Contextual::Return::Failure.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
