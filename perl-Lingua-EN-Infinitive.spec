%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-Infinitive perl module
Summary(pl):	Modu³ perla Lingua-EN-Infinitive
Name:		perl-Lingua-EN-Infinitive
Version:	1.00
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Infinitive-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-EN-Infinitive - determines the infinitive form of a conjugated
word.

%description -l pl
Lingua-EN-Infinitive - okre¶la bezokolicznik dla koniugowanego
czasownika w jêzyku angielskim.

%prep
%setup -q -n Lingua-EN-Infinitive-%{version}

%build
perl Makefile.PL
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
