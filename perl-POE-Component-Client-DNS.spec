%define upstream_name	 POE-Component-Client-DNS
%define upstream_version 1.053

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	POE::Component::Client::DNS - non-blocking, concurrent DNS requests
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/POE-Component-Client-DNS-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(POE)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch

%description
POE::Component::Client::DNS provides a facility for non-blocking, concurrent
DNS requests. Using POE, it allows other tasks to run while waiting for name
servers to respond.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.51.0-2mdv2011.0
+ Revision: 655153
- rebuild for updated spec-helper

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.51.0-1mdv2011.0
+ Revision: 461344
- update to 1.051

* Sun Aug 30 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 422583
- adding missing buildrequires:
- update to 1.050

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 408774
- update to 1.04

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 407990
- rebuild using %%perl_convert_version

* Thu Feb 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.1
+ Revision: 342825
- update to new version 1.03

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.1
+ Revision: 330193
- update to new version 1.02

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.1
+ Revision: 299403
- update to new version 1.01

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.00-5mdv2009.0
+ Revision: 258269
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.00-4mdv2009.0
+ Revision: 246323
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.00-2mdv2008.1
+ Revision: 151412
- rebuild for perl-5.10.0

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.00-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.00-1mdv2007.0
+ Revision: 106113
- 1.00

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.99-1mdv2007.0
+ Revision: 54022
- 0.99
- Import perl-POE-Component-Client-DNS

* Tue Dec 20 2005 Olivier Thauvin <nanardon@mandriva.org> 0.9803-1mdk
- 0.9803

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9802-3mdk
- Fix BuildRequires

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9802-2mdk
- Buildrequires fix

* Thu Sep 08 2005 Olivier Thauvin <nanardon@mandriva.org> 0.9802-1mdk
- First mandriva package


