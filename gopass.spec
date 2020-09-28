%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

Name:           gopass
Version:        1.10.1
Release:        1
Summary:        The slightly more awesome standard unix password manager for teams

License:        MIT
URL:            https://github.com/gopasspw/gopass
Source0:        https://github.com/gopasspw/gopass/archive/master.tar.gz

BuildRequires:  git
BuildRequires:  tar
BuildRequires:  gzip
BuildRequires:  golang

%description
The slightly more awesome standard unix password manager for teams

%prep
%autosetup -n %{name}-master

%build
make

%install
%make_install PREFIX="/usr"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%exclude /usr/share/zsh/site-functions/_gopass
/usr/share/bash-completion/completions/gopass
%exclude /usr/share/fish/vendor_completions.d/gopass.fish
/usr/bin/gopass
/usr/bin/gopass-git-credentials
/usr/bin/gopass-hibp
/usr/bin/gopass-jsonapi
/usr/bin/gopass-summon-provider
