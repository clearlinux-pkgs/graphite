#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : graphite
Version  : 1.3.13
Release  : 5
URL      : https://github.com/silnrsi/graphite/releases/download/1.3.13/graphite2-1.3.13.tgz
Source0  : https://github.com/silnrsi/graphite/releases/download/1.3.13/graphite2-1.3.13.tgz
Summary  : "Interface to SIL's Graphite2 rendering engine"
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0 ICU LGPL-2.1 OFL-1.1
Requires: graphite-bin = %{version}-%{release}
Requires: graphite-data = %{version}-%{release}
Requires: graphite-lib = %{version}-%{release}
Requires: graphite-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : freetype-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : python3

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
%setup -q -n graphite2-1.3.13
pushd ..
cp -a graphite2-1.3.13 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545315707
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="$ASFLAGS --32"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DLIB_SUFFIX=32 ..
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build32;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1545315707
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/graphite
cp COPYING %{buildroot}/usr/share/package-licenses/graphite/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/graphite/LICENSE
cp debian-src/copyright %{buildroot}/usr/share/package-licenses/graphite/debian-src_copyright
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/lib64/libgraphite2.so.3
/usr/lib64/libgraphite2.so.3.2.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgraphite2.so.3
/usr/lib32/libgraphite2.so.3.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/graphite/COPYING
/usr/share/package-licenses/graphite/LICENSE
/usr/share/package-licenses/graphite/debian-src_copyright
