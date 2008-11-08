#
# Conditional build:
#
%define		origname	kmplayer
%define		_rc		rc1
Summary:	A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(pl.UTF-8):	Frontend dla programów MPlayer/Xine/ffmpeg/ffserver/VDR pod KDE
Name:		kde4-kmplayer
Version:	0.11.0
Release:	%{_rc}_1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://kmplayer.kde.org/pkgs/%{origname}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	6ad12e99addaf63e49529ea3f2a9e7f6
Patch0:		%{name}-unistd.patch
URL:		http://kmplayer.kde.org/
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:  QtCore-devel >= %{qt_ver}
BuildRequires:  Qt3Support-devel >= %{qt_ver}
BuildRequires:  QtDBus-devel >= %{qt_ver}
BuildRequires:	bzip2-devel
BuildRequires:  QtSvg-devel >= %{qt_ver}
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:  strigi-devel >= 0.5.10
Requires:	Qt3Support
Requires:	QtCore
Requires:	QtDBus
Requires:	QtSvg
Requires:	xorg-lib-libXft
Requires:	xorg-lib-libXpm
Requires:	xorg-lib-libXtst
Requires:	kde4-kdebase-core >= 4.0.0
Requires:	kde4-kdelibs >= 4.0.0
Requires:	mplayer
BuildRoot:	%{tmpdir}/%{origname}-%{version}-%{_rc}-root-%(id -u -n)

%description
A powerful, fully integrated with KDE MPlayer/Xine/ffmpeg/ffserver/VDR
GUI.

%description -l pl.UTF-8
W pełni zintegrowany z KDE frontend dla programów
MPlayer/Xine/ffmpeg/ffserver/VDR.

%package icons-oxygen
Summary:		Kmplayer Oxygen Icons
Summary(pl.UTF-8):	Ikony kmplayer dla oxygen
Group:			X11/Applications/Multimedia
Requires:		%{name} = %{version}-%{release}
Conflicts:		kde4-icons-oxygen

%description icons-oxygen
Kmplayer Oxygen Icons

%description icons-oxygen -l pl.UTF-8
Ikony kmplayer dla Oxygen

%prep
%setup -q -n %{origname}-%{version}-%{_rc}
%patch0 -p1

%build
install -d build
cd build
%cmake \
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

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/kmplayer
%attr(755,root,root) %{_bindir}/kphononplayer
%attr(755,root,root) %{_libdir}/libkdeinit4_kmplayer.so
%attr(755,root,root) %{_libdir}/libkmplayercommon.so
%attr(755,root,root) %{_libdir}/kde4/libkmplayerpart.so
%{_datadir}/apps/kmplayer
%{_datadir}/kde4/services/kmplayer_part.desktop
%{_datadir}/kde4/services/kmplayer.desktop
%{_iconsdir}/hicolor/*/apps/kmplayer.*
%{_datadir}/apps/kmplayer/kmplayerpartui.rc
%{_datadir}/apps/kmplayer/kmplayerui.rc
%{_datadir}/apps/kmplayer/noise.gif
%{_datadir}/apps/kmplayer/pluginsinfo
%{_docdir}/kde/HTML/en/doc/*

%files icons-oxygen
%{_iconsdir}/oxygen/*/apps/kmplayer.*
