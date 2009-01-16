%define real_name	POE-Component-Client-DNS
%define name		perl-%{real_name}
%define version		1.02
%define release		%mkrel 1

Summary:	POE::Component::Client::DNS - non-blocking, concurrent DNS requests
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
BuildRequires:	perl-devel
BuildRequires:  perl-POE
BuildRequires:  perl-Net-DNS
Buildroot:	%{_tmppath}/%{name}-root
URL:		http://search.cpan.org/dist/%{real_name}
Source:		%{real_name}-%{version}.tar.bz2
BuildArch:	noarch

%description
POE::Component::Client::DNS provides a facility for non-blocking, concurrent
DNS requests. Using POE, it allows other tasks to run while waiting for name
servers to respond.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/*
%_mandir/*/*



