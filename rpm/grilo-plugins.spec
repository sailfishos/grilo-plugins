Name:       grilo-plugins
Summary:    Grilo plugins
Version:    0.3.11
Release:    1
License:    LGPLv2.1
URL:        https://live.gnome.org/Grilo
Source0:    http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/0.3/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(grilo-net-0.3)
BuildRequires:  pkgconfig(tracker-sparql-2.0)
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libquvi)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  lua
BuildRequires:  gettext

Patch1: 0001-Disable-building-help-files.patch

%description
Grilo is a framework focused on making media discovery and browsing
easy for application developers.
More precisely, Grilo provides:
* A single, high-level API that abstracts the differences among
  various media content providers, allowing application developers
  to integrate content from various services and sources easily.
* A collection of plugins for accessing content from various media
  providers. Developers can share efforts and code by writing
  plugins for the framework that are application agnostic.
* A flexible API that allows plugin developers to write plugins of
  various kinds.
This package contains the set of plugins officially distributed with
Grilo.

%package    -n grilo-plugin-youtube
Summary:    Grilo plugin - youtube

%description -n grilo-plugin-youtube
Grilo plugin - youtube


%package    -n grilo-plugin-filesystem
Summary:    Grilo plugin - filesystem

%description -n grilo-plugin-filesystem
Grilo plugin - filesystem

%package    -n grilo-plugin-jamendo
Summary:    Grilo plugin - jamendo
#
%description -n grilo-plugin-jamendo
Grilo plugin - jamendo


%package    -n grilo-plugin-lastfm-albumart
Summary:    Grilo plugin - lastfm-albumart (obsolete)

%description -n grilo-plugin-lastfm-albumart
Grilo plugin - lastfm-albumart. Obsolete and non-functional.


%package    -n grilo-plugin-flickr
Summary:    Grilo plugin - flickr

%description -n grilo-plugin-flickr
Grilo plugin - flickr


%package    -n grilo-plugin-podcasts
Summary:    Grilo plugin - podcasts

%description -n grilo-plugin-podcasts
Grilo plugin - podcasts

# disabled due to missing gom packaging
%package    -n grilo-plugin-bookmarks
Summary:    Grilo plugin - bookmarks. Obsolete.

%description -n grilo-plugin-bookmarks
Grilo plugin - bookmarks. Non-functional.


%package    -n grilo-plugin-shoutcast
Summary:    Grilo plugin - shoutcast

%description -n grilo-plugin-shoutcast
Grilo plugin - shoutcast


%package    -n grilo-plugin-apple-trailers
Summary:    Grilo plugin - apple-trailers (obsolete)

%description -n grilo-plugin-apple-trailers
Grilo plugin - apple-trailers. Obsolete and non-functional.


%package    -n grilo-plugin-metadata-store
Summary:    Grilo plugin - metadata-store

%description -n grilo-plugin-metadata-store
Grilo plugin - metadata-store


%package    -n grilo-plugin-vimeo
Summary:    Grilo plugin - vimeo

%description -n grilo-plugin-vimeo
Grilo plugin - vimeo


%package    -n grilo-plugin-gravatar
Summary:    Grilo plugin - gravatar

%description -n grilo-plugin-gravatar
Grilo plugin - gravatar


%package    -n grilo-plugin-tracker
Summary:    Grilo plugin - tracker

%description -n grilo-plugin-tracker
Grilo plugin - tracker


%package    -n grilo-plugin-bliptv
Summary:    Grilo plugin - bliptv (obsolete)

%description -n grilo-plugin-bliptv
Grilo plugin - bliptv. Obsolete and non-functional.


%package    -n grilo-plugin-localmetadata
Summary:    Grilo plugin - localmetadata

%description -n grilo-plugin-localmetadata
Grilo plugin - localmetadata


%package    -n grilo-plugin-raitv
Summary:    Grilo plugin - Rai.tv

%description -n grilo-plugin-raitv
Grilo plugin - Rai.tv


%package    -n grilo-plugin-magnatune
Summary:    Grilo plugin - Magnatune

%description -n grilo-plugin-magnatune
Grilo plugin - Magnatune

%package    -n grilo-plugin-dleyna
Summary:    Grilo plugin - dLeyna

%description -n grilo-plugin-dleyna
A Grilo plugin for browsing DLNA servers

%package    -n grilo-plugin-opensubtitles
Summary:    Grilo plugin - OpenSubtitles Provider

%description -n grilo-plugin-opensubtitles
A Grilo plugin that gets a list of subtitles for a video


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build

%meson -Denable-bookmarks=no -Denable-optical-media=no \
       -Denable-lua-factory=no -Denable-chromaprint=no

%install
rm -rf %{buildroot}
%meson_install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gnome/help/
rm -rf $RPM_BUILD_ROOT/%{_datadir}/locale
# don't think we have any use for .pc file containing only the version
rm -rf $RPM_BUILD_ROOT/usr/lib/pkgconfig/grilo-plugins-0.3.pc

%files -n grilo-plugin-youtube
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlyoutube.so

%files -n grilo-plugin-filesystem
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlfilesystem.so

%files -n grilo-plugin-jamendo
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrljamendo.so

%files -n grilo-plugin-flickr
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlflickr.so

%files -n grilo-plugin-podcasts
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlpodcasts.so

#%files -n grilo-plugin-bookmarks
#%defattr(-,root,root,-)
#%{_libdir}/grilo-0.3/libgrlbookmarks.so

%files -n grilo-plugin-shoutcast
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlshoutcast.so

%files -n grilo-plugin-metadata-store
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlmetadatastore.so

%files -n grilo-plugin-vimeo
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlvimeo.so

%files -n grilo-plugin-gravatar
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlgravatar.so

%files -n grilo-plugin-tracker
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrltracker.so

%files -n grilo-plugin-localmetadata
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrllocalmetadata.so

%files -n grilo-plugin-raitv
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlraitv.so

%files -n grilo-plugin-magnatune
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlmagnatune.so

%files -n grilo-plugin-dleyna
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrldleyna.so

%files -n grilo-plugin-opensubtitles
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlopensubtitles.so
