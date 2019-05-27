%global         majorminor 1.0

Name:           gstreamer1-plugins-ugly
Version:        1.14.4
Release:        2%{?dist}
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
BuildRequires:  gtk-doc >= 1.12
BuildRequires:  libdvdread-devel
BuildRequires:  libid3tag-devel >= 0.15.0
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

%package        devel-docs
Summary:        Development files for the GStreamer "ugly" plug-ins
Requires:       %{name}%{?isa} = %{?epoch}:%{version}-%{release}
BuildArch:      noarch

%description    devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This module contains a set of plugins that have good quality and correct
functionality, but distributing them might pose problems. The license on either
the plugins or the supporting libraries might not be how we'd like. The code
might be widely known to present patent problems. Distributors should check if
they want/can ship these plugins.

This package contains the development documentation.

%prep
%autosetup -n gst-plugins-ugly-%{version}

%build
%configure \
    --disable-rpath \
    --disable-silent-rules \
    --disable-fatal-warnings \
    --enable-a52dec \
    --enable-amrnb \
    --enable-amrwb \
    --enable-cdio \
    --enable-dvdread \
    --enable-experimental \
    --enable-gtk-doc \
    --enable-mpeg2dec \
    --enable-x264 \
    --disable-sidplay \
    --with-package-name="Fedora GStreamer-plugins-ugly package" \
    --with-package-origin="http://negativo17.org"
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
%find_lang gst-plugins-ugly-%{majorminor}

%files -f gst-plugins-ugly-%{majorminor}.lang
%license COPYING
%doc AUTHORS README REQUIREMENTS
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

%files devel-docs
%doc %{_datadir}/gtk-doc/html/*

%changelog
* Mon May 27 2019 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-2
- Rebuild for updated dependencies.

* Sat Oct 20 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.4-1
- Update to 1.14.4.

* Wed Sep 26 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.3-1
- Update to 1.14.3.

* Tue Aug 28 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.2-1
- Update to 1.14.2.

* Thu Jun 14 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.1-1
- Update to 1.14.1.

* Wed May 02 2018 Simone Caronni <negativo17@gmail.com> - 1:1.14.0-1
- Update to 1.14.0.
- Update SPEC file.

* Tue May 01 2018 Simone Caronni <negativo17@gmail.com> - 1:1.12.4-2
- Rebuild for updated dependencies.

* Tue Jan 09 2018 Simone Caronni <negativo17@gmail.com> - 1:1.12.4-1
- Update to 1.12.4.

* Wed Oct 25 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-2
- Rebuild for x264 and mpg123 updates.

* Mon Oct 23 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.3-1
- Update to 1.12.3.

* Thu Jul 20 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.2-1
- Update to 1.12.2.

* Sat Jun 24 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.1-1
- Update to 1.12.1.

* Thu May 18 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.0-2
- Also obsolete/provide gstreamer-plugins-ugly-free.

* Sat May 13 2017 Simone Caronni <negativo17@gmail.com> - 1:1.12.0-1
- Update to 1.12.0.

* Wed Apr 19 2017 Simone Caronni <negativo17@gmail.com> - 1:1.11.90-1
- Update to 1.11.90.

* Mon Dec 05 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.2-1
- Update to 1.10.2.

* Mon Nov 28 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.1-1
- Update to 1.10.1.

* Tue Nov 15 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.0-2
- Obsolete/provide gstreamer1-plugin-mpg123.

* Thu Nov 10 2016 Simone Caronni <negativo17@gmail.com> - 1:1.10.0-1
- Update to 1.10.0.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.2-2
- Rebuild for mpg123 update.

* Thu Nov 03 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.2-1
- Update to 1.9.2.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.9.1-1
- Update to 1.9.1.

* Mon Jul 25 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-2
- Rename devel subpackage to devel-docs.

* Sun Jun 19 2016 Simone Caronni <negativo17@gmail.com> - 1:1.8.2-1
- First build.
