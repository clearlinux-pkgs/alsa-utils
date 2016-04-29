#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : alsa-utils
Version  : 1.1.0
Release  : 4
URL      : ftp://ftp.alsa-project.org/pub/utils/alsa-utils-1.1.0.tar.bz2
Source0  : ftp://ftp.alsa-project.org/pub/utils/alsa-utils-1.1.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: alsa-utils-bin
Requires: alsa-utils-config
Requires: alsa-utils-data
Requires: alsa-utils-locales
Requires: alsa-utils-doc
BuildRequires : alsa-lib-dev
BuildRequires : docbook-xml
BuildRequires : fftw-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(udev)
BuildRequires : sed
BuildRequires : systemd-dev
BuildRequires : util-linux
BuildRequires : xmlto

%description
Advanced Linux Sound Architecture - Utilities
=============================================

%package bin
Summary: bin components for the alsa-utils package.
Group: Binaries
Requires: alsa-utils-data
Requires: alsa-utils-config

%description bin
bin components for the alsa-utils package.


%package config
Summary: config components for the alsa-utils package.
Group: Default

%description config
config components for the alsa-utils package.


%package data
Summary: data components for the alsa-utils package.
Group: Data

%description data
data components for the alsa-utils package.


%package doc
Summary: doc components for the alsa-utils package.
Group: Documentation

%description doc
doc components for the alsa-utils package.


%package locales
Summary: locales components for the alsa-utils package.
Group: Default

%description locales
locales components for the alsa-utils package.


%prep
%setup -q -n alsa-utils-1.1.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang alsa-utils
%find_lang alsaconf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/aconnect
/usr/bin/alsa-info.sh
/usr/bin/alsaconf
/usr/bin/alsactl
/usr/bin/alsaloop
/usr/bin/alsamixer
/usr/bin/alsatplg
/usr/bin/alsaucm
/usr/bin/amidi
/usr/bin/amixer
/usr/bin/aplay
/usr/bin/aplaymidi
/usr/bin/arecord
/usr/bin/arecordmidi
/usr/bin/aseqdump
/usr/bin/aseqnet
/usr/bin/bat
/usr/bin/iecset
/usr/bin/speaker-test

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/alsa-restore.service
/usr/lib/systemd/system/alsa-state.service
/usr/lib/systemd/system/basic.target.wants/alsa-restore.service
/usr/lib/systemd/system/basic.target.wants/alsa-state.service
/usr/lib/udev/rules.d/90-alsa-restore.rules

%files data
%defattr(-,root,root,-)
/usr/share/alsa/init/00main
/usr/share/alsa/init/ca0106
/usr/share/alsa/init/default
/usr/share/alsa/init/hda
/usr/share/alsa/init/help
/usr/share/alsa/init/info
/usr/share/alsa/init/test
/usr/share/alsa/speaker-test/sample_map.csv
/usr/share/man/fr/man8/alsaconf.8
/usr/share/sounds/alsa/Front_Center.wav
/usr/share/sounds/alsa/Front_Left.wav
/usr/share/sounds/alsa/Front_Right.wav
/usr/share/sounds/alsa/Noise.wav
/usr/share/sounds/alsa/Rear_Center.wav
/usr/share/sounds/alsa/Rear_Left.wav
/usr/share/sounds/alsa/Rear_Right.wav
/usr/share/sounds/alsa/Side_Left.wav
/usr/share/sounds/alsa/Side_Right.wav

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files locales -f alsa-utils.lang -f alsaconf.lang 
%defattr(-,root,root,-)

