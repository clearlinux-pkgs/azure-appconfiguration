#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-appconfiguration
Version  : 1.1.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/21/0a/1b24d1b3c1477b849d48aa29dcde3141c1524fab293042493f3432b672c2/azure-appconfiguration-1.1.1.zip
Source0  : https://files.pythonhosted.org/packages/21/0a/1b24d1b3c1477b849d48aa29dcde3141c1524fab293042493f3432b672c2/azure-appconfiguration-1.1.1.zip
Summary  : Microsoft App Configuration Data Library for Python
Group    : Development/Tools
License  : MIT
Requires: azure-appconfiguration-python = %{version}-%{release}
Requires: azure-appconfiguration-python3 = %{version}-%{release}
Requires: aiodns
Requires: aiohttp
Requires: azure-core
Requires: azure-nspkg
Requires: msrest
BuildRequires : aiodns
BuildRequires : aiohttp
BuildRequires : azure-core
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : msrest

%description
Azure App Configuration is a managed service that helps developers centralize their application configurations simply and securely.
        
        Modern programs, especially programs running in a cloud, generally have many components that are distributed in nature. Spreading configuration settings across these components can lead to hard-to-troubleshoot errors during an application deployment. Use App Configuration to securely store all the settings for your application in one place.
        
        Use the client library for App Configuration to create and manage application configuration settings.

%package python
Summary: python components for the azure-appconfiguration package.
Group: Default
Requires: azure-appconfiguration-python3 = %{version}-%{release}

%description python
python components for the azure-appconfiguration package.


%package python3
Summary: python3 components for the azure-appconfiguration package.
Group: Default
Requires: python3-core
Provides: pypi(azure_appconfiguration)
Requires: pypi(azure_core)
Requires: pypi(msrest)

%description python3
python3 components for the azure-appconfiguration package.


%prep
%setup -q -n azure-appconfiguration-1.1.1
cd %{_builddir}/azure-appconfiguration-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607991660
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
