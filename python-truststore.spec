Name:		python-truststore
Version:	0.10.4
Release:	1
Summary:	Verify certificates using native system trust stores
License:	MIT
Group:		Development/Python
URL:		https://github.com/sethmlarson/truststore
Source0:	https://files.pythonhosted.org/packages/source/t/truststore/truststore-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)

%description
truststore exposes the operating system's certificate store through
an ssl.SSLContext-like API, so HTTPS clients can verify peers with
the system trust store.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/truststore
%{py_sitedir}/truststore-*.*-info
