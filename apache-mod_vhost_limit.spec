%define		mod_name	vhost_limit
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module: clients restriction per vhost
Name:		apache-mod_%{mod_name}
Version:	0.1
Release:	1
License:	Apache
Group:		Networking/Daemons
Source0:	http://apache.ivn.cl/files/source/mod_vhost_limit-%{version}.tgz
# Source0-md5:	58e86dfe8f3813f693652ee6740c1c1b
URL:		http://apache.ivn.cl/#vhostlimit
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.0.0
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	apache(modules-api) = %apache_modules_api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
Restrict the number of simultaneous connections per vhost.

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
