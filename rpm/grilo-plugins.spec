Name:       grilo-plugins
Summary:    Plugins for the Grilo framework
Version:    0.3.14
Release:    1
License:    LGPLv2+
URL:        https://wiki.gnome.org/Projects/Grilo
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  meson >= 0.37.0
BuildRequires:  lua >= 5.3.0
BuildRequires:  gettext
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.8
BuildRequires:  pkgconfig(grilo-net-0.3) >= 0.3.0
BuildRequires:  pkgconfig(grilo-pls-0.3) >= 0.3.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libmediaart-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libgdata) >= 0.9.1
BuildRequires:  pkgconfig(totem-plparser) >= 3.4.1
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(oauth)

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

%package -n grilo-plugin-youtube
Summary:  Grilo plugin - YouTube
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-youtube
A Grilo plugin for YouTube.

%package -n grilo-plugin-filesystem
Summary:  Grilo plugin - filesystem
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-filesystem
Grilo plugin - filesystem.

%package -n grilo-plugin-flickr
Summary:  Grilo plugin - Flickr
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-flickr
A Grilo plugin for Flickr.

%package -n grilo-plugin-podcasts
Summary:  Grilo plugin - podcasts
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-podcasts
A Grilo plugin for podcasts.

%package -n grilo-plugin-shoutcast
Summary:  Grilo plugin - Shoutcast
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-shoutcast
A Grilo plugin for Shoutcast.

%package -n grilo-plugin-metadata-store
Summary:  Grilo plugin - metadata store
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-metadata-store
A Grilo plugin for metadata store.

%package -n grilo-plugin-gravatar
Summary:  Grilo plugin - Gravatar
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-gravatar
A Grilo plugin for Gravatar.

%package -n grilo-plugin-tracker
Summary:  Grilo plugin - Tracker
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-tracker
A Grilo plugin for Tracker.

%package -n grilo-plugin-localmetadata
Summary:  Grilo plugin - local metadata
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-localmetadata
A Grilo plugin for local metadata.

%package -n grilo-plugin-raitv
Summary:  Grilo plugin - Rai.tv
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-raitv
Grilo plugin - Rai.tv.

%package -n grilo-plugin-magnatune
Summary:  Grilo plugin - Magnatune
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-magnatune
Grilo plugin - Magnatune.

%package -n grilo-plugin-dleyna
Summary:  Grilo plugin - dLeyna
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-dleyna
A Grilo plugin for browsing UPnP/DLNA servers.

%package -n grilo-plugin-opensubtitles
Summary:  Grilo plugin - OpenSubtitles Provider
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-opensubtitles
A Grilo plugin that gets a list of subtitles for a video.

%package -n grilo-plugin-tmdb
Summary:  Grilo plugin - TMDb
Requires: %{name} = %{version}-%{release}

%description -n grilo-plugin-tmdb
A Grilo plugin that retrieves information about movies from the TMDb online
service.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%meson \
  -Dhelp=no \
  -Denable-bookmarks=no \
  -Denable-optical-media=no \
  -Denable-lua-factory=no \
  -Denable-chromaprint=no \
  -Dgoa=disabled

%meson_build

%install
%meson_install
# don't think we have any use for .pc file containing only the version
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/grilo-plugins-0.3.pc

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING

%files -n grilo-plugin-youtube
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlyoutube.so

%files -n grilo-plugin-filesystem
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlfilesystem.so

%files -n grilo-plugin-flickr
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlflickr.so

%files -n grilo-plugin-podcasts
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlpodcasts.so

%files -n grilo-plugin-shoutcast
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlshoutcast.so

%files -n grilo-plugin-metadata-store
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlmetadatastore.so

%files -n grilo-plugin-gravatar
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrlgravatar.so

%files -n grilo-plugin-tracker
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrltracker3.so

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

%files -n grilo-plugin-tmdb
%defattr(-,root,root,-)
%{_libdir}/grilo-0.3/libgrltmdb.so
