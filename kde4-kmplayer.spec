%define		origname	kmplayer
%define		kdever		4.4.4

Summary:	A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(pl.UTF-8):	Frontend dla programów MPlayer/Xine/ffmpeg/ffserver/VDR pod KDE
Name:		kde4-kmplayer
Version:	0.11.2b
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://kmplayer.kde.org/pkgs/%{origname}-%{version}.tar.bz2
# Source0-md5:	4dcaf4dc7fa2b2e9a2792ae7cd525bd0
Patch0:		%{name}-unistd.patch
URL:		http://kmplayer.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	strigi-devel >= 0.5.10
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	mplayer
Requires:	xorg-lib-libXft
Requires:	xorg-lib-libXpm
Requires:	xorg-lib-libXtst
Obsoletes:	kde4-kmplayer-icons-oxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE MPlayer/Xine/ffmpeg/ffserver/VDR
GUI.

%description -l pl.UTF-8
W pełni zintegrowany z KDE frontend dla programów
MPlayer/Xine/ffmpeg/ffserver/VDR.

%prep
%setup -q -n %{origname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# remove unsupported langs
rm -rf $RPM_BUILD_ROOT/%{_datadir}/locale/x-test

%find_lang %{origname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{origname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/kmplayer
%attr(755,root,root) %{_bindir}/knpplayer
%attr(755,root,root) %{_bindir}/kphononplayer
%attr(755,root,root) %{_libdir}/libkdeinit4_kmplayer.so
%attr(755,root,root) %{_libdir}/libkmplayercommon.so
%attr(755,root,root) %{_libdir}/kde4/libkmplayerpart.so
%{_datadir}/apps/kmplayer
%{_datadir}/config/kmplayerrc
%{_datadir}/kde4/services/kmplayer_part.desktop
%{_desktopdir}/kde4/kmplayer.desktop
%{_iconsdir}/hicolor/*/apps/kmplayer.*
%{_kdedocdir}/en/kmplayer
