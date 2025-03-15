
%define		module	pycurl
Summary:	Free and easy-to-use client-side URL transfer library
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka obsługi URL od strony klienta
Name:		python3-%{module}
Version:	7.45.6
Release:	1
License:	LGPL v2 or MIT-like
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pycurl/%{module}-%{version}.tar.gz
# Source0-md5:	385831ba48aab2e109af838643f2921f
Patch0:		python-pycurl-no-static-libs.patch
URL:		http://pycurl.io/
BuildRequires:	curl-devel >= 7.19
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
# During its initialization, PycURL checks that the actual libcurl version
# is not lower than the one used when PycURL was built.
# Yes, that should be handled by library versioning (which would then get
# automatically reflected by rpm).
# For now, we have to reflect that dependency.
%requires_ge curl-libs
Requires:	python3-libs >= 1:3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycurl is Python interface to curl library - free and easy-to-use
client-side URL transfer library, supporting FTP, FTPS, HTTP, HTTPS,
GOPHER, TELNET, DICT, FILE and LDAP. libcurl supports HTTPS
certificates, HTTP POST, HTTP PUT, FTP uploading, kerberos, HTTP form
based upload, proxies, cookies, user+password authentication, file
transfer resume, HTTP proxy tunneling and more!

%description -l pl.UTF-8
pycurl jest interfejsem języka Python do biblioteki libcurl -
wolnodostępnej i łatwej w użyciu biblioteki operacji na URL-ach od
strony klienta, obsługującej FTP, FTPS, HTTP, HTTPS, GOPHER, TELNET,
DICT, FILE i LDAP. libcurl obsługuje także certyfikaty HTTPS, HTTP
POST, HTTP PUT, uploady FTP, kerberos, upload plików przez HTTP oparty
na formularzach, proxy, ciasteczka, uwierzytelnienie, wznawianie
przesyłania plików, tunelowanie proxy i wiele innych.

%package doc
Summary:	Documentation for pycurl Python module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona pycurl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
This module contains documentation files for pycurl Python module.

%description doc -l pl.UTF-8
Moduł zawierający dokumentację dla modułu Pythona pucurl.

%package examples
Summary:	Examples for pycurl Python module
Summary(pl.UTF-8):	Przykładowe programy do modułu Pythona pycurl
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description examples
This module contains examples for pycurl Python module.

%description examples -l pl.UTF-8
Moduł zawierający przykładowe programy do modułu Pythona pycurl.

%prep
%setup -q -n %{module}-%{version}
%patch -P 0 -p1

%build
%py3_build \
	--debug

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%py3_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/pycurl

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING-MIT ChangeLog README.rst RELEASE-NOTES.rst
%attr(755,root,root) %{py3_sitedir}/pycurl*.so
%dir %{py3_sitedir}/curl
%{py3_sitedir}/curl/__pycache__
%{py3_sitedir}/curl/*.py
%{py3_sitedir}/pycurl-*.egg-info

%files doc
%defattr(644,root,root,755)
# TODO: use rst2html to convert?
#%doc doc/*.html
%doc doc/*.rst

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
