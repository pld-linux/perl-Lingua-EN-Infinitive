%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Lingua-EN-Infinitive perl module
Summary(pl):	Modu³ perla Lingua-EN-Infinitive
Name:		perl-Lingua-EN-Infinitive
Version:	1.00
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Infinitive-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Lingua-EN-Infinitive - determines the infinitive form of a conjugated word. 

%description -l pl
Lingua-EN-Infinitive - okre¶la bezokolicznik dla koniugowanego czasownika
w jêzyku angielskim.

%prep
%setup -q -n Lingua-EN-Infinitive-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Lingua/EN/Infinitive
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{perl_sitelib}/Lingua/EN/Infinitive.pm
%{perl_sitearch}/auto/Lingua/EN/Infinitive

%{_mandir}/man3/*
