Name:          evolution-on
Version:       3.24.2
Release:       1
Summary:       Plugin to put evolution in system tray.

License:       GPLv2
URL:           https://github.com/acidrain42/evolution-on
Source0:       https://github.com/acidrain42/evolution-on/archive/master.tar.gz

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gnome-common
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: GConf2-devel
BuildRequires: evolution-devel

Requires: evolution
Requires: libnotify
Requires: GConf2

%description
Plugin to put evolution in system tray.

%prep
%autosetup -n %{name}-master
NOCONFIGURE=1 ./autogen.sh

%build
./configure --prefix=/usr
make

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/GConf/gsettings/evolution-on.convert
/usr/share/glib-2.0/schemas/org.gnome.evolution.plugin.evolution-on.gschema.xml
/usr/lib64/evolution/plugins/org-gnome-evolution-on.eplug
/usr/lib64/evolution/plugins/liborg-gnome-evolution-on.so
/usr/lib64/evolution/plugins/liborg-gnome-evolution-on.la

%changelog
