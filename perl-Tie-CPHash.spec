%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	CPHash
Summary:	Tie::CPHash perl module
Summary(pl):	Modu� perla Tie::CPHash
Name:		perl-Tie-CPHash
Version:	1.001
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::CPHash - provides a hash table that is case preserving but case
insensitive.

%description -l pl
Tie::CPHash - udost�pnia tablic� haszuj�c�, kt�ra zachowuje wielko��
liter ale ich nie rozr�nia.

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
%doc Changes README
%{perl_sitelib}/Tie/CPHash.pm
%{_mandir}/man3/*
