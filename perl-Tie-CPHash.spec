%include	/usr/lib/rpm/macros.perl
Summary:	Tie-CPHash perl module
Summary(pl):	Modu� perla Tie-CPHash
Name:		perl-Tie-CPHash
Version:	1.001
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-CPHash-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-CPHash - provides a hash table that is case preserving but case
insensitive.

%description -l pl
Tie-CPHash - udost�pnia tablic� haszuj�c�, kt�ra zachowuje wielko��
liter ale ich nie rozr�nia.

%prep
%setup -q -n Tie-CPHash-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/CPHash.pm
%{_mandir}/man3/*
