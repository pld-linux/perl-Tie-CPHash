%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	CPHash
Summary:	Tie-CPHash perl module
Summary(pl):	Modu³ perla Tie-CPHash
Name:		perl-Tie-CPHash
Version:	1.001
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-CPHash - provides a hash table that is case preserving but case
insensitive.

%description -l pl
Tie-CPHash - udostêpnia tablicê haszuj±c±, która zachowuje wielko¶æ
liter ale ich nie rozró¿nia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
