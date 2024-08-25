# Please keep this package in sync with FC

# -*- rpm-spec -*-

Group:   System/Libraries
Summary: Osinfo database files
Name: osinfo-db
Version:	20240701
Release:	1
License: LGPLv2+
Source0: https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
Source1: https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz.asc
URL: http://libosinfo.org/
BuildRequires: intltool
BuildRequires: osinfo-db-tools
BuildArch: noarch
Requires: hwdata

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%install
osinfo-db-import  --root %{buildroot} --dir %{_datadir}/osinfo %{SOURCE0}

%files
%dir %{_datadir}/osinfo/
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema
