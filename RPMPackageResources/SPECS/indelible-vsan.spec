Name:	indelible-vsan	
Version:	@REVISION@
Release:	1%{?dist}
Summary:	Indelible Virtual SAN
Group:		System Environment/Daemons
License:	Apache
URL:		http://www.indeliblefs.com
Source:		%{name}-%{version}.tar.gz

BuildRequires:	java-1.6.0-openjdk, ant >= 1.8, avahi-devel
Requires:	avahi, avahi-tools, avahi-libs, java-1.6.0-openjdk

%description
Indelible Virtual SAN provides an iSCSI target with local caching and disk images
backed by Indelible FS
%prep
%setup

%build
cd %{_builddir}/%{name}-%{version}/IndelibleVirtualSAN-Linux
ant buildDist

%install
echo %{buildroot}
cd %{_builddir}/%{name}-%{version}/IndelibleVirtualSAN-Linux
ant -DrpmInstallDir='%{buildroot}' install-rh

%files
/etc/init/
/usr/bin/
/usr/lib/igeek/indelible-vsan/
/usr/share/igeek/indelible-vsan/

%changelog

%clean
echo "Not cleaning"
