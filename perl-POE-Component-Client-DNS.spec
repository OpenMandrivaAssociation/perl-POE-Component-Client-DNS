%define upstream_name	 POE-Component-Client-DNS
%define upstream_version 1.050

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	POE::Component::Client::DNS - non-blocking, concurrent DNS requests
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-POE
BuildRequires:  perl-Net-DNS
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
POE::Component::Client::DNS provides a facility for non-blocking, concurrent
DNS requests. Using POE, it allows other tasks to run while waiting for name
servers to respond.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
