#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Infinitive
Summary:	Lingua::EN::Infinitive perl module
Summary(pl):	Modu³ perla Lingua::EN::Infinitive
Name:		perl-Lingua-EN-Infinitive
Version:	1.00
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1525c36e9dcda4de19e1f640b516766b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Infinitive - determines the infinitive form of a conjugated
word.

%description -l pl
Lingua::EN::Infinitive - okre¶la bezokolicznik dla koniugowanego
czasownika w jêzyku angielskim.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Lingua/EN/Infinitive.pm
%{_mandir}/man3/*
