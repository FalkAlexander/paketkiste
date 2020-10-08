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
qmake-qt5 "DEFINES+=APP_GOOGLE_API_KEY=AIzaSyBs1wuIgc-QDnk5u7OavF1loJVO0r89B4Y" PREFIX=$RPM_BUILD_ROOT/usr
%make_build %{?_smp_mflags}

%install
make install prefix=%{_prefix} INSTALL="%{__install} -p" \
DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f | xargs sed -i "s|$RPM_BUILD_ROOT||g"

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/minitube
/usr/share/minitube/locale/ar.qm
/usr/share/minitube/locale/ast.qm
/usr/share/minitube/locale/be.qm
/usr/share/minitube/locale/bg_BG.qm
/usr/share/minitube/locale/ca.qm
/usr/share/minitube/locale/ca_ES.qm
/usr/share/minitube/locale/cs_CZ.qm
/usr/share/minitube/locale/da.qm
/usr/share/minitube/locale/de_DE.qm
/usr/share/minitube/locale/el.qm
/usr/share/minitube/locale/en.qm
/usr/share/minitube/locale/en_GB.qm
/usr/share/minitube/locale/es.qm
/usr/share/minitube/locale/es_AR.qm
/usr/share/minitube/locale/es_ES.qm
/usr/share/minitube/locale/es_MX.qm
/usr/share/minitube/locale/fi.qm
/usr/share/minitube/locale/fi_FI.qm
/usr/share/minitube/locale/fr.qm
/usr/share/minitube/locale/gl.qm
/usr/share/minitube/locale/he_IL.qm
/usr/share/minitube/locale/hr.qm
/usr/share/minitube/locale/hu.qm
/usr/share/minitube/locale/id.qm
/usr/share/minitube/locale/it.qm
/usr/share/minitube/locale/ja_JP.qm
/usr/share/minitube/locale/ko_KR.qm
/usr/share/minitube/locale/ky.qm
/usr/share/minitube/locale/ms_MY.qm
/usr/share/minitube/locale/nb.qm
/usr/share/minitube/locale/nl.qm
/usr/share/minitube/locale/nn.qm
/usr/share/minitube/locale/pl.qm
/usr/share/minitube/locale/pl_PL.qm
/usr/share/minitube/locale/pt.qm
/usr/share/minitube/locale/pt_BR.qm
/usr/share/minitube/locale/pt_PT.qm
/usr/share/minitube/locale/ro.qm
/usr/share/minitube/locale/ru.qm
/usr/share/minitube/locale/sk.qm
/usr/share/minitube/locale/sl.qm
/usr/share/minitube/locale/sq.qm
/usr/share/minitube/locale/sr.qm
/usr/share/minitube/locale/sv_SE.qm
/usr/share/minitube/locale/th.qm
/usr/share/minitube/locale/tr.qm
/usr/share/minitube/locale/uk.qm
/usr/share/minitube/locale/uk_UA.qm
/usr/share/minitube/locale/vi.qm
/usr/share/minitube/locale/zh_CN.qm
/usr/share/minitube/locale/zh_TW.qm
/usr/share/minitube/sounds/snapshot.wav
/usr/share/applications/minitube.desktop
/usr/share/metainfo/org.tordini.flavio.minitube.metainfo.xml
/usr/share/icons/hicolor/scalable/apps/minitube.svg
/usr/share/icons/hicolor/16x16/apps/minitube.png
/usr/share/icons/hicolor/22x22/apps/minitube.png
/usr/share/icons/hicolor/32x32/apps/minitube.png
/usr/share/icons/hicolor/48x48/apps/minitube.png
/usr/share/icons/hicolor/64x64/apps/minitube.png
/usr/share/icons/hicolor/128x128/apps/minitube.png
/usr/share/icons/hicolor/256x256/apps/minitube.png
/usr/share/icons/hicolor/512x512/apps/minitube.png
