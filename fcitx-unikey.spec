%define beta %{nil}
%define scmrev %{nil}
%define _disable_ld_no_undefined 1

Name: fcitx-unikey
Version: 0.2.3
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 3
Source0: http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: Unikey (Vietnamese IM) plugin for fcitx
URL: http://fcitx.googlecode.com/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(fcitx-qt)
BuildRequires: fcitx-qt4

%track
prog %{name} = {
	url = http://code.google.com/p/fcitx/downloads/list
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
Unikey (Vietnamese IM) plugin for fcitx

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %name

%files -f %name.lang
%_libdir/fcitx/fcitx-unikey.so
%_libdir/fcitx/qt/libfcitx-unikey-macro-editor.so
%_datadir/fcitx/addon/fcitx-unikey.conf
%_datadir/fcitx/configdesc/fcitx-unikey.desc
%_datadir/fcitx/imicon/unikey.png
%_datadir/fcitx/inputmethod/unikey.conf
%_datadir/icons/hicolor/256x256/apps/fcitx-unikey.png
