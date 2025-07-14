%define		origname	kmplayer
%define		kdever		4.4.4

Summary:	A KDE MPlayer/Xine/ffmpeg/ffserver/VDR frontend
Summary(pl.UTF-8):	Frontend dla programów MPlayer/Xine/ffmpeg/ffserver/VDR pod KDE
Name:		kde4-kmplayer
Version:	0.11.3d
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://kmplayer.kde.org/pkgs/%{origname}-%{version}.tar.bz2
# Source0-md5:	a652d00370e0940e6bd9cf51b32770c4
Patch0:		%{name}-unistd.patch
Patch1:		cmake.patch
URL:		http://kmplayer.kde.org/
BuildRequires:	cmake >= 2.8.0
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	mplayer
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
%patch -P0 -p1
%patch -P1 -p1

%build
install -d build
cd build
%cmake \
				.. \

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

# Remove empty locale
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/sk/LC_MESSAGES/kmplayer.mo

%find_lang %{origname} --all-name --with-kde

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
