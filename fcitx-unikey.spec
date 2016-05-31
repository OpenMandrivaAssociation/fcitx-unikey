%define _disable_ld_no_undefined 1

Summary: Unikey (Vietnamese IM) plugin for fcitx
Name: fcitx-unikey
Version: 0.2.5
Release: 1
Source0: http://downloads.fcitx-im.org/fcitx-unikey/%{name}-%{version}.tar.xz
URL: http://www.fcitx-im.org/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(fcitx-qt)

%track
prog %{name} = {
	url = http://downloads.fcitx-im.org/fcitx-unikey
	regex = %name-(__VER__)\.tar\.xz
	version = %{version}
}

%description
Unikey (Vietnamese IM) plugin for fcitx.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %{name}

%files -f %name.lang
%{_libdir}/fcitx/fcitx-unikey.so
%{_libdir}/fcitx/qt/libfcitx-unikey-macro-editor.so
%{_datadir}/fcitx/addon/fcitx-unikey.conf
%{_datadir}/fcitx/configdesc/fcitx-unikey.desc
%{_datadir}/fcitx/imicon/unikey.png
%{_datadir}/fcitx/inputmethod/unikey.conf
%{_datadir}/icons/hicolor/256x256/apps/fcitx-unikey.png
