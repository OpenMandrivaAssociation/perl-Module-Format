%define upstream_name    Module-Format
%define upstream_version v0.0.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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


