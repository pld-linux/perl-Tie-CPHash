#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Tie
%define		pnam	CPHash
Summary:	Tie::CPHash - Case preserving but case insensitive hash table
Summary(pl.UTF-8):	Tie::CPHash - tablica haszująca zachowująca, ale nie rozróżniająca wielkości liter
Name:		perl-Tie-CPHash
Version:	2.000
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tie/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e8c86f8294bd87b56b3c9d7e748ee1ce
URL:		http://search.cpan.org/dist/Tie-CPHash/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::CPHash - provides a hash table that is case preserving but case
insensitive.

%description -l pl.UTF-8
Tie::CPHash - udostępnia tablicę haszującą, która zachowuje wielkość
liter ale ich nie rozróżnia.

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
%doc Changes README
%{perl_vendorlib}/Tie/CPHash.pm
%{_mandir}/man3/*
