#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
Name     : graphite
Version  : 1.3.14
Release  : 27
URL      : https://github.com/silnrsi/graphite/releases/download/1.3.14/graphite2-1.3.14.tgz
Source0  : https://github.com/silnrsi/graphite/releases/download/1.3.14/graphite2-1.3.14.tgz
Summary  : "Interface to SIL's Graphite2 rendering engine"
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0 ICU LGPL-2.1 OFL-1.1
Requires: graphite-bin = %{version}-%{release}
Requires: graphite-data = %{version}-%{release}
Requires: graphite-lib = %{version}-%{release}
Requires: graphite-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : freetype-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pypi(fonttools)
BuildRequires : python3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
*** Linux MonoDevelop build instructions. ***
To run unittests first install the libgraphite2-2.0.0 package and ensure that the fonts Paduak and DejaVuSans are installed.

%package bin
Summary: bin components for the graphite package.
Group: Binaries
Requires: graphite-data = %{version}-%{release}
Requires: graphite-license = %{version}-%{release}

%description bin
bin components for the graphite package.


%package data
Summary: data components for the graphite package.
Group: Data

%description data
data components for the graphite package.


%package dev
Summary: dev components for the graphite package.
Group: Development
Requires: graphite-lib = %{version}-%{release}
Requires: graphite-bin = %{version}-%{release}
Requires: graphite-data = %{version}-%{release}
Provides: graphite-devel = %{version}-%{release}
Requires: graphite = %{version}-%{release}

%description dev
dev components for the graphite package.


%package dev32
Summary: dev32 components for the graphite package.
Group: Default
Requires: graphite-lib32 = %{version}-%{release}
Requires: graphite-bin = %{version}-%{release}
Requires: graphite-data = %{version}-%{release}
Requires: graphite-dev = %{version}-%{release}

%description dev32
dev32 components for the graphite package.


%package lib
Summary: lib components for the graphite package.
Group: Libraries
Requires: graphite-data = %{version}-%{release}
Requires: graphite-license = %{version}-%{release}

%description lib
lib components for the graphite package.


%package lib32
Summary: lib32 components for the graphite package.
Group: Default
Requires: graphite-data = %{version}-%{release}
Requires: graphite-license = %{version}-%{release}

%description lib32
lib32 components for the graphite package.


%package license
Summary: license components for the graphite package.
Group: Default

%description license
license components for the graphite package.


%prep
%setup -q -n graphite2-1.3.14
cd %{_builddir}/graphite2-1.3.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701962934
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build32;
make test || : || :
cd ../clr-build-avx2;
make test || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701962934
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/graphite
cp %{_builddir}/graphite2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/graphite/07903fc8c18ad3ffa9f30a28c3a3947ef7888296 || :
cp %{_builddir}/graphite2-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/graphite/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
cp %{_builddir}/graphite2-%{version}/debian-src/copyright %{buildroot}/usr/share/package-licenses/graphite/c951267758aad7dbdfa3251e5a2680f4889bac4c || :
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gr2fonttest
/usr/bin/gr2fonttest

%files data
%defattr(-,root,root,-)
/usr/share/graphite2/graphite2-relwithdebinfo.cmake
/usr/share/graphite2/graphite2.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/graphite2/Font.h
/usr/include/graphite2/Log.h
/usr/include/graphite2/Segment.h
/usr/include/graphite2/Types.h
/usr/lib64/libgraphite2.so
/usr/lib64/pkgconfig/graphite2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgraphite2.so
/usr/lib32/pkgconfig/32graphite2.pc
/usr/lib32/pkgconfig/graphite2.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgraphite2.so.3.2.1
/usr/lib64/libgraphite2.so.3
/usr/lib64/libgraphite2.so.3.2.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgraphite2.so.3
/usr/lib32/libgraphite2.so.3.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/graphite/07903fc8c18ad3ffa9f30a28c3a3947ef7888296
/usr/share/package-licenses/graphite/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/graphite/c951267758aad7dbdfa3251e5a2680f4889bac4c
