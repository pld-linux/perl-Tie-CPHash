#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	CPHash
Summary:	Tie::CPHash perl module
Summary(pl):	Modu³ perla Tie::CPHash
Name:		perl-Tie-CPHash
Version:	1.001
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	70adcbb754fd7102d46653c43057a328
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::CPHash - provides a hash table that is case preserving but case
insensitive.

%description -l pl
Tie::CPHash - udostêpnia tablicê haszuj±c±, która zachowuje wielko¶æ
liter ale ich nie rozró¿nia.

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
