%define _disable_ld_no_undefined 1

Summary: Unikey (Vietnamese IM) plugin for fcitx
Name: fcitx-unikey
Version: 0.2.7
Release: 1
Source0: https://github.com/fcitx/fcitx-unikey/archive/%{version}.tar.gz
URL: http://www.fcitx-im.org/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)

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
