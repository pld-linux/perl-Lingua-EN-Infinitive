%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Infinitive
Summary:	Lingua::EN::Infinitive perl module
Summary(pl):	Modu³ perla Lingua::EN::Infinitive
Name:		perl-Lingua-EN-Infinitive
Version:	1.00
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
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
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Lingua/EN/Infinitive.pm
%{_mandir}/man3/*
