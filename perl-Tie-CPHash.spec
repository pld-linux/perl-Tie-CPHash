%include	/usr/lib/rpm/macros.perl
Summary:	Tie-CPHash perl module
Summary(pl):	Modu� perla Tie-CPHash
Name:		perl-Tie-CPHash
Version:	1.001
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-CPHash-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tie/CPHash
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Tie/CPHash.pm
%{perl_sitearch}/auto/Tie/CPHash

%{_mandir}/man3/*
