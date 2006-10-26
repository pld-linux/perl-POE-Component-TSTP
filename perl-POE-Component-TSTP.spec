#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-TSTP
Summary:	POE::Component::TSTP - a POE component to handle Ctrl-Z
Summary(pl):	POE::Component::TSTP - komponent POE obs³uguj±cy Ctrl-Z
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

%description -l pl
Komponent POE obs³uguj±cy SIGTSTP, czyli zwykle Ctrl-Z. Domy¶lnie
aplikacje POE nie reaguj± na Ctrl-Z ze wzglêdu na nieco dziwn±
semantykê obs³ugi sygna³ów. Ten modu³ poprawia to.

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
