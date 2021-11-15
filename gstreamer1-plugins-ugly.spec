%global         majorminor 1.0

Name:           gstreamer1-plugins-ugly
Version:        1.19.3
Release:        1%{?dist}
Epoch:          1
Summary:        GStreamer streaming media framework "ugly" plugins
License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  a52dec-devel >= 0.7.3
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.17
BuildRequires:  libdvdread-devel
BuildRequires:  libid3tag-devel >= 0.15.0
BuildRequires:  meson >= 0.48.0
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(libcdio) >= 0.76
BuildRequires:  pkgconfig(libmpeg2) >= 0.5.1
BuildRequires:  pkgconfig(mad) >= 0.15
BuildRequires:  pkgconfig(opencore-amrnb) >= 0.1.3
BuildRequires:  pkgconfig(opencore-amrwb) >= 0.1.3
BuildRequires:  pkgconfig(x264) >= 0.120

Obsoletes:      %{name}-free < %{?epoch}:%{version}-%{release}
Provides:       %{name}-free = %{?epoch}:%{version}-%{release}
Provides:       %{name}-free%{?_isa} = %{?epoch}:%{version}-%{release}

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This module contains a set of plugins that have good quality and correct
functionality, but distributing them might pose problems. The license on either
the plugins or the supporting libraries might not be how we'd like. The code
might be widely known to present patent problems. Distributors should check if
they want/can ship these plugins.

%prep
%autosetup -n gst-plugins-ugly-%{version}

%build
%meson \
  -D package-name="Fedora GStreamer-plugins-ugly package" \
  -D package-origin="https://negativo17.org" \
  -D a52dec=enabled \
  -D amrnb=enabled \
  -D amrwbdec=enabled \
  -D asfdemux=enabled \
  -D cdio=enabled \
  -D doc=disabled \
  -D dvdlpcmdec=enabled \
  -D dvdread=enabled \
  -D dvdsub=enabled \
  -D gpl=enabled \
  -D mpeg2dec=enabled \
  -D realmedia=enabled \
  -D sidplay=disabled \
  -D x264=enabled \
  -D xingmux=enabled
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete
%find_lang gst-plugins-ugly-%{majorminor}

%files -f gst-plugins-ugly-%{majorminor}.lang
%license COPYING
%doc AUTHORS README REQUIREMENTS ChangeLog
%{_datadir}/gstreamer-%{majorminor}/presets/*.prs
%{_libdir}/gstreamer-%{majorminor}/libgstasf.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdsub.so
%{_libdir}/gstreamer-%{majorminor}/libgstxingmux.so
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrnb.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrwbdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdio.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdread.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstrealmedia.so
%{_libdir}/gstreamer-%{majorminor}/libgstx264.so

%changelog
* Mon Nov 15 2021 Simone Caronni <negativo17@gmail.com> - 1:1.19.3-1
- Update to 1.19.3.

* Sun Oct 24 2021 Simone Caronni <negativo17@gmail.com> - 1:1.19.2-1
- Update to 1.19.2.

* Wed Sep 22 2021 Fabio Valentini <decathorpe@gmail.com> - 1:1.19.1-1
- Update to 1.19.1.

* Mon Jul 26 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-2
- Rebuild for updated dependencies.

* Mon Apr 12 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.4-1
- Update to 1.18.4.

* Thu Jan 14 2021 Simone Caronni <negativo17@gmail.com> - 1:1.18.2-1
- Update to 1.18.2.

* Tue Dec 15 2020 Simone Caronni <negativo17@gmail.com> - 1:1.18.1-2
- Rebuild for updated dependencies

* Sun Nov 01 2020 Simone Caronni <negativo17@gmail.com> - 1:1.18.1-1
- Update to 1.18.1, rebase on Meson.
- Trim changelog.

* Wed Jul 15 2020 Simone Caronni <negativo17@gmail.com> - 1:1.16.2-2
- Rebuild for updated dependencies.

* Tue Feb 11 2020 Simone Caronni <negativo17@gmail.com> - 1:1.16.2-1
- Update to 1.16.2.

* Sun Jan 19 2020 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-2
- Rebuild for updated dependencies.

* Wed Oct 09 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.1-1
- Update to 1.16.1.

* Mon May 27 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.0-2
- Rebuild for updated dependencies.

* Tue Apr 30 2019 Simone Caronni <negativo17@gmail.com> - 1:1.16.0-1
- Update to 1.16.0.

* Wed Apr 03 2019 Simone Caronni <negativo17@gmail.com> - 1:1.15.2-1
- Update to 1.15.2.
