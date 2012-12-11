%define upstream_name    Module-Format
%define upstream_version v0.0.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Convert and manipulate stringified versions of Perl modules
License:    MIT
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.xz

BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::More)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Module-Format is a set of Perl modules and the accompanying perlmf command line
utility that can be used to output consistetly formatted named of Perl modules
for input in applications. So one can do:

urpmi --auto $(perlmf as_rpm_c "$@")

to install perl dependencies using urpmi (and many other uses).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_bindir}/perlmf
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.0.3-3mdv2011.0
+ Revision: 657449
- rebuild for updated spec-helper

* Sun Feb 27 2011 Shlomi Fish <shlomif@mandriva.org> 0.0.3-2
+ Revision: 640667
- Bumped rel for the new perl

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.0.3-1mdv2011.0
+ Revision: 606858
- Upgraded to 0.0.3

* Sun Nov 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.0.2-2mdv2011.0
+ Revision: 602592
- Bumped the release number
- Fixed the information
- import perl-Module-Format

