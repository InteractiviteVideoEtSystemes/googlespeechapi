%define version_tag 1.55.0

Name:	grpc
Version: 1.55.0
Release: 1.ives%{?dist}
Summary: Google RPC framework

Group: Development/Library
License: Apache 2.0
URL: https://grpc.io/
Source0: https://github.com/grpc/grpc/archive/v1.28.2.tar.gz
Source1: https://github.com/InteractiviteVideoEtSystemes/googlespeechapi/raw/master/Makefile.grpc

BuildRequires: protobuf-devel, gtest-devel, gperftools-devel


%description
Google speech API compiled with all its dependencies

%package devel
Summary: Header and static lib for GRPC library
Requires: %{name}

%description devel
Google RPC framework headers

%prep
cd $RPM_SOURCE_DIR
rm -rf grpc $HOME/usr/*
git clone https://github.com/grpc/grpc.git --branch=v%{version}
cd grpc
git submodule update --init --recursive third_party/protobuf
git submodule update --init --recursive third_party/abseil-cpp
git submodule update --init --recursive third_party/cares
git submodule update --init --recursive third_party/re2
git submodule update --init --recursive third_party/boringssl-with-bazel
cmake3 . -DCMAKE_CXX_STANDARD=14 -DCMAKE_INSTALL_LIBDIR=lib64 -DCMAKE_INSTALL_PREFIX=/usr -DgRPC_INSTALL_LIBDIR=lib64

#patch -p0 < $RPM_SOURCE_DIR/grpc-makefile.patch

%build
cd $RPM_SOURCE_DIR/grpc
cmake3 --build .


%install
cd $RPM_SOURCE_DIR/grpc
cmake3 --install . --prefix %{buildroot}/usr -DCMAKE_INSTALL_LIBDIR=lib64

%files
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.a
%{_libdir}/cmake/

#Do not package ARES bins
%exclude /usr/bin/acountry
%exclude /usr/bin/adig
%exclude /usr/bin/ahost

# GRPC plugin
/usr/bin/grpc_*

# Protobuf compilers

/usr/bin/protoc
/usr/bin/protoc-23.1.0
/usr/share/grpc/roots.pem

# Headers
/usr/include/absl/
/usr/include/grpc/
/usr/include/grpc++/
/usr/include/grpcpp/
/usr/include/re2/
/usr/include/google/
/usr/include/ares.h
/usr/include/ares_build.h
/usr/include/ares_dns.h
/usr/include/ares_rules.h
/usr/include/ares_version.h
/usr/include/utf8_range.h
/usr/include/utf8_validity.h

%doc /usr/share/man/

%clean
cd $RPM_SOURCE_DIR
rm -rf grpc

%changelog

