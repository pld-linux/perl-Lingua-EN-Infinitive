%include	/usr/lib/rpm/macros.perl
Summary:	Lingua-EN-Infinitive perl module
Summary(pl):	Modu� perla Lingua-EN-Infinitive
Name:		perl-Lingua-EN-Infinitive
Version:	1.00
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Lingua/Lingua-EN-Infinitive-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua-EN-Infinitive - determines the infinitive form of a conjugated
word.

%description -l pl
Lingua-EN-Infinitive - okre�la bezokolicznik dla koniugowanego
czasownika w j�zyku angielskim.

%prep
%setup -q -n Lingua-EN-Infinitive-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
