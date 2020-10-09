%global debug_package %{nil}

Name:           minitube
Version:        3.6.2
Release:        1
Summary:        Minitube is a YouTube desktop application. It is written in C++ using the Qt framework.

License:        GPLv3
URL:            https://github.com/flaviotordini/minitube
Source0:        https://github.com/flaviotordini/minitube/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  mpv-libs-devel

Requires:       libgcc
Requires:       glibc
Requires:       qt5-qtbase
Requires:       qt5-qtdeclarative
Requires:       qt5-qtx11extras

%description
Minitube is a YouTube desktop application. It is written in C++ using the Qt framework.

%prep
%autosetup -n %{name}-%{version}

%build
%qmake_qt5 PREFIX=%{_prefix} DEFINES+=APP_GOOGLE_API_KEY=AIzaSyBs1wuIgc-QDnk5u7OavF1loJVO0r89B4Y
%make_build %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc TODO CHANGES AUTHORS
%{_bindir}/minitube
%{_datadir}/minitube/
%{_datadir}/applications/minitube.desktop
/usr/share/icons/hicolor/*/apps/minitube.*
/usr/share/metainfo/org.tordini.flavio.minitube.metainfo.xml
