#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-TSTP
Summary:	POE::Component::TSTP - a POE component to handle Ctrl-Z
Summary(pl.UTF-8):	POE::Component::TSTP - komponent POE obsługujący Ctrl-Z
Name:		perl-POE-Component-TSTP
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ac0dafa63a99b3e305e073e30bb9f22
URL:		http://poe.perl.org/
BuildRequires:	perl-POE
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE component handling SIGTSTP, Ctrl-Z usually. By default, POE
applications do not respond to Ctrl-Z due to slightly strange signal
handling semantics. This module fixes that.

%description -l pl.UTF-8
Komponent POE obsługujący SIGTSTP, czyli zwykle Ctrl-Z. Domyślnie
aplikacje POE nie reagują na Ctrl-Z ze względu na nieco dziwną
semantykę obsługi sygnałów. Ten moduł poprawia to.

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
%{perl_vendorlib}/POE/Component/TSTP.pm
%{_mandir}/man3/*
