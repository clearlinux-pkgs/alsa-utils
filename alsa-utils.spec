#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v24
# autospec commit: a88ffdc
#
# Source0 file verified with key 0x8380596DA6E59C91 (release@alsa-project.org)
#
Name     : alsa-utils
Version  : 1.2.14
Release  : 46
URL      : https://www.alsa-project.org/files/pub/utils/alsa-utils-1.2.14.tar.bz2
Source0  : https://www.alsa-project.org/files/pub/utils/alsa-utils-1.2.14.tar.bz2
Source1  : https://www.alsa-project.org/files/pub/utils/alsa-utils-1.2.14.tar.bz2.sig
Source2  : 8380596DA6E59C91.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: alsa-utils-autostart = %{version}-%{release}
Requires: alsa-utils-bin = %{version}-%{release}
Requires: alsa-utils-config = %{version}-%{release}
Requires: alsa-utils-data = %{version}-%{release}
Requires: alsa-utils-lib = %{version}-%{release}
Requires: alsa-utils-license = %{version}-%{release}
Requires: alsa-utils-locales = %{version}-%{release}
Requires: alsa-utils-man = %{version}-%{release}
Requires: alsa-utils-services = %{version}-%{release}
Requires: alsa-plugins
Requires: dialog
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : fftw-dev
BuildRequires : file
BuildRequires : gnupg
BuildRequires : libsamplerate-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(systemd)
BuildRequires : pypi-docutils
BuildRequires : sed
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: mkdir.patch
Patch2: 0001-Disable-the-axfer-tool.patch

%description
# alsa-utils
## Advanced Linux Sound Architecture - Utilities
[![Build alsa-utils](https://github.com/alsa-project/alsa-utils/workflows/Build%20alsa-utils/badge.svg?branch=master)](https://github.com/alsa-project/alsa-utils/actions/workflows/build.yml?query=branch%3Amaster++)

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


%package lib
Summary: lib components for the alsa-utils package.
Group: Libraries
Requires: alsa-utils-data = %{version}-%{release}
Requires: alsa-utils-license = %{version}-%{release}

%description lib
lib components for the alsa-utils package.


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
Requires: systemd

%description services
services components for the alsa-utils package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 8380596DA6E59C91' gpg.status
%setup -q -n alsa-utils-1.2.14
cd %{_builddir}/alsa-utils-1.2.14
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a alsa-utils-1.2.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744671731
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744671731
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/alsa-utils
cp %{_builddir}/alsa-utils-%{version}/COPYING %{buildroot}/usr/share/package-licenses/alsa-utils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang alsa-utils
%find_lang alsaconf
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sound.target.wants/alsa-restore.service
/usr/lib/systemd/system/sound.target.wants/alsa-state.service

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aconnect
/V3/usr/bin/alsabat
/V3/usr/bin/alsactl
/V3/usr/bin/alsaloop
/V3/usr/bin/alsamixer
/V3/usr/bin/alsatplg
/V3/usr/bin/alsaucm
/V3/usr/bin/amidi
/V3/usr/bin/amixer
/V3/usr/bin/aplay
/V3/usr/bin/aplaymidi
/V3/usr/bin/aplaymidi2
/V3/usr/bin/arecordmidi
/V3/usr/bin/arecordmidi2
/V3/usr/bin/aseqdump
/V3/usr/bin/aseqnet
/V3/usr/bin/aseqsend
/V3/usr/bin/iecset
/V3/usr/bin/nhlt-dmic-info
/V3/usr/bin/speaker-test
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
/usr/bin/aplaymidi2
/usr/bin/arecord
/usr/bin/arecordmidi
/usr/bin/arecordmidi2
/usr/bin/aseqdump
/usr/bin/aseqnet
/usr/bin/aseqsend
/usr/bin/iecset
/usr/bin/nhlt-dmic-info
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
/usr/share/sounds/alsa/Front_Center.wav
/usr/share/sounds/alsa/Front_Left.wav
/usr/share/sounds/alsa/Front_Right.wav
/usr/share/sounds/alsa/Noise.wav
/usr/share/sounds/alsa/Rear_Center.wav
/usr/share/sounds/alsa/Rear_Left.wav
/usr/share/sounds/alsa/Rear_Right.wav
/usr/share/sounds/alsa/Side_Left.wav
/usr/share/sounds/alsa/Side_Right.wav

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/alsa-topology/libalsatplg_module_nhlt.so
/usr/lib64/alsa-topology/libalsatplg_module_nhlt.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/alsa-utils/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/fr/man8/alsaconf.8
/usr/share/man/man1/aconnect.1
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
/usr/share/man/man1/aplaymidi2.1
/usr/share/man/man1/arecord.1
/usr/share/man/man1/arecordmidi.1
/usr/share/man/man1/arecordmidi2.1
/usr/share/man/man1/aseqdump.1
/usr/share/man/man1/aseqnet.1
/usr/share/man/man1/aseqsend.1
/usr/share/man/man1/iecset.1
/usr/share/man/man1/nhlt-dmic-info.1
/usr/share/man/man1/speaker-test.1
/usr/share/man/man7/alsactl_init.7
/usr/share/man/man8/alsa-info.sh.8
/usr/share/man/man8/alsaconf.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sound.target.wants/alsa-restore.service
%exclude /usr/lib/systemd/system/sound.target.wants/alsa-state.service
/usr/lib/systemd/system/alsa-restore.service
/usr/lib/systemd/system/alsa-state.service

%files locales -f alsa-utils.lang -f alsaconf.lang
%defattr(-,root,root,-)

