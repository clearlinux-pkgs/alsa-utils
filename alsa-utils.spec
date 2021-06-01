#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-utils
Version  : 1.2.5
Release  : 28
URL      : https://www.alsa-project.org/files/pub/utils/alsa-utils-1.2.5.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/utils/alsa-utils-1.2.5.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/utils/alsa-utils-1.2.5.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: alsa-utils-autostart = %{version}-%{release}
Requires: alsa-utils-bin = %{version}-%{release}
Requires: alsa-utils-config = %{version}-%{release}
Requires: alsa-utils-data = %{version}-%{release}
Requires: alsa-utils-license = %{version}-%{release}
Requires: alsa-utils-locales = %{version}-%{release}
Requires: alsa-utils-man = %{version}-%{release}
Requires: alsa-utils-services = %{version}-%{release}
Requires: dialog
BuildRequires : alsa-lib-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : dialog
BuildRequires : docbook-xml
BuildRequires : docutils
BuildRequires : fftw-dev
BuildRequires : gettext-bin
BuildRequires : glibc-staticdev
BuildRequires : libsamplerate-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(systemd)
BuildRequires : sed
BuildRequires : xmlto
Patch1: mkdir.patch
Patch2: 0001-Disable-the-axfer-tool.patch
Patch3: 0002-alsactl-fix-the-nested-iteration.patch

%description
# alsa-utils
## Advanced Linux Sound Architecture - Utilities
![Build alsa-utils](https://github.com/alsa-project/alsa-utils/workflows/Build%20alsa-utils/badge.svg?branch=master)

%package autostart
Summary: autostart components for the alsa-utils package.
Group: Default

%description autostart
autostart components for the alsa-utils package.


%package bin
Summary: bin components for the alsa-utils package.
Group: Binaries
Requires: alsa-utils-data = %{version}-%{release}
Requires: alsa-utils-config = %{version}-%{release}
Requires: alsa-utils-license = %{version}-%{release}
Requires: alsa-utils-services = %{version}-%{release}

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


%package license
Summary: license components for the alsa-utils package.
Group: Default

%description license
license components for the alsa-utils package.


%package locales
Summary: locales components for the alsa-utils package.
Group: Default

%description locales
locales components for the alsa-utils package.


%package man
Summary: man components for the alsa-utils package.
Group: Default

%description man
man components for the alsa-utils package.


%package services
Summary: services components for the alsa-utils package.
Group: Systemd services

%description services
services components for the alsa-utils package.


%prep
%setup -q -n alsa-utils-1.2.5
cd %{_builddir}/alsa-utils-1.2.5
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622571856
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1622571856
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-utils
cp %{_builddir}/alsa-utils-1.2.5/COPYING %{buildroot}/usr/share/package-licenses/alsa-utils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
%make_install
%find_lang alsa-utils
%find_lang alsaconf

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sound.target.wants/alsa-restore.service
/usr/lib/systemd/system/sound.target.wants/alsa-state.service

%files bin
%defattr(-,root,root,-)
/usr/bin/aconnect
/usr/bin/alsa-info.sh
/usr/bin/alsabat
/usr/bin/alsabat-test.sh
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
/usr/bin/iecset
/usr/bin/speaker-test

%files config
%defattr(-,root,root,-)
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
/usr/share/sounds/alsa/Front_Center.wav
/usr/share/sounds/alsa/Front_Left.wav
/usr/share/sounds/alsa/Front_Right.wav
/usr/share/sounds/alsa/Noise.wav
/usr/share/sounds/alsa/Rear_Center.wav
/usr/share/sounds/alsa/Rear_Left.wav
/usr/share/sounds/alsa/Rear_Right.wav
/usr/share/sounds/alsa/Side_Left.wav
/usr/share/sounds/alsa/Side_Right.wav

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-utils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/fr/man8/alsaconf.8
/usr/share/man/man1/aconnect.1
/usr/share/man/man1/alsa-info.sh.1
/usr/share/man/man1/alsabat.1
/usr/share/man/man1/alsactl.1
/usr/share/man/man1/alsaloop.1
/usr/share/man/man1/alsamixer.1
/usr/share/man/man1/alsatplg.1
/usr/share/man/man1/alsaucm.1
/usr/share/man/man1/amidi.1
/usr/share/man/man1/amixer.1
/usr/share/man/man1/aplay.1
/usr/share/man/man1/aplaymidi.1
/usr/share/man/man1/arecord.1
/usr/share/man/man1/arecordmidi.1
/usr/share/man/man1/aseqdump.1
/usr/share/man/man1/aseqnet.1
/usr/share/man/man1/iecset.1
/usr/share/man/man1/speaker-test.1
/usr/share/man/man7/alsactl_init.7
/usr/share/man/man8/alsaconf.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sound.target.wants/alsa-restore.service
%exclude /usr/lib/systemd/system/sound.target.wants/alsa-state.service
/usr/lib/systemd/system/alsa-restore.service
/usr/lib/systemd/system/alsa-state.service

%files locales -f alsa-utils.lang -f alsaconf.lang
%defattr(-,root,root,-)

