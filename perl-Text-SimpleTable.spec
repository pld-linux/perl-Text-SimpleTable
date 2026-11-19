#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Text
%define	pnam	SimpleTable
Summary:	Text::SimpleTable - Simple Eyecandy ASCII Tables
Summary(pl.UTF-8):	Text::SimpleTable - proste, ładne tabele ASCII
Name:		perl-Text-SimpleTable
Version:	2.07
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	206d21f8f1ea526704657d169c2be1ec
URL:		http://search.cpan.org/dist/Text-SimpleTable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple eyecandy ASCII tables, as seen in Catalyst.

%description -l pl.UTF-8
Proste, ładne tabele ASCII, takie jakie można zobaczyć w Catalyście.

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Text/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
