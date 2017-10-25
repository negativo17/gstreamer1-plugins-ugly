%global         majorminor 1.0

Name:           gstreamer1-plugins-ugly
Version:        1.10.4
Release:        2%{?dist}
Epoch:          1
Summary:        GStreamer streaming media framework "ugly" plugins
License:        LGPLv2+ and LGPLv2
URL:            http://gstreamer.freedesktop.org/

Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz

BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}

BuildRequires:  a52dec-devel >= 0.7.3
BuildRequires:  gettext-devel >= 0.17
BuildRequires:  gtk-doc >= 1.12
BuildRequires:  lame-devel >= 3.89
BuildRequires:  libdvdread-devel
BuildRequires:  libid3tag-devel >= 0.15.0
#BuildRequires:  libsidplay-devel < 2.0.0
BuildRequires:  orc-devel >= 0.4.16
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(libcdio) >= 0.76
BuildRequires:  pkgconfig(libmpeg2) >= 0.5.1
BuildRequires:  pkgconfig(libmpg123) >= 1.13
BuildRequires:  pkgconfig(mad) >= 0.15
BuildRequires:  pkgconfig(opencore-amrnb) >= 0.1.3
BuildRequires:  pkgconfig(opencore-amrwb) >= 0.1.3
BuildRequires:  pkgconfig(twolame) >= 0.3.10
BuildRequires:  pkgconfig(x264) >= 0.120

Obsoletes:      gstreamer1-plugin-mpg123 < %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-mpg123 = %{?epoch}:%{version}-%{release}
Provides:       gstreamer1-plugin-mpg123%{?_isa} = %{?epoch}:%{version}-%{release}
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
%setup -q -n gst-plugins-ugly-%{version}

%build
%configure \
    --disable-rpath \
    --disable-silent-rules \
    --disable-fatal-warnings \
    --enable-gtk-doc \
    --enable-experimental \
    --with-package-name="Fedora GStreamer-plugins-ugly package" \
    --with-package-origin="http://negativo17.org"
make %{?_smp_mflags}


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
%{_libdir}/gstreamer-%{majorminor}/libgstrmdemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstxingmux.so
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrnb.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrwbdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdio.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdread.so
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpg123.so
%{_libdir}/gstreamer-%{majorminor}/libgsttwolame.so
%{_libdir}/gstreamer-%{majorminor}/libgstx264.so

%files devel-docs
%doc %{_datadir}/gtk-doc/html/*

%changelog
* Wed Oct 25 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-2
- Rebuild for x264 and mpg123 updates.

* Wed Aug 16 2017 Simone Caronni <negativo17@gmail.com> - 1:1.10.4-1
- Update to 1.10.4.

* Tue Nov 15 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-2
- Obsolete/provide gstreamer1-plugin-mpg123.

* Wed Aug 17 2016 Simone Caronni <negativo17@gmail.com> - 1:1.4.5-1
- Initial import.
