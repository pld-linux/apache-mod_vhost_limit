%define		mod_name	vhost_limit
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module: clients restriction per vhost
Summary(pl.UTF-8):	Moduł Apache'a - ograniczanie klientów dla vhosta
Name:		apache-mod_%{mod_name}
Version:	0.2
Release:	1
License:	Apache
Group:		Networking/Daemons
Source0:	http://apache.ivn.cl/files/source/mod_vhost_limit-%{version}.tgz
# Source0-md5:	7379520e078d26503f8323e7f36302fb
URL:		http://apache.ivn.cl/#vhostlimit
BuildRequires:	apache-apxs >= 2.0
BuildRequires:	apache-devel >= 2.0.0
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	apache(modules-api) = %apache_modules_api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
Restrict the number of simultaneous connections per vhost.

%description -l pl.UTF-8
Moduł ograniczający liczbę jednoczesnych połączeń dla vhosta.

%prep
%setup -q -n mod_vhost_limit-%{version}

%build
%{apxs} -c mod_vhost_limit.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkglibdir}

libtool install mod_vhost_limit.la $RPM_BUILD_ROOT%{_pkglibdir}
rm -f $RPM_BUILD_ROOT%{_pkglibdir}/*.{l,}a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/*.so
