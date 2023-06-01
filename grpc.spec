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
cmake3 --build . -j4


%install
cd $RPM_SOURCE_DIR/grpc
cmake3 --install . --prefix %{buildroot}/usr -DCMAKE_INSTALL_LIBDIR=lib64

sed -i "s|${HOME}||g" $HOME%{_libdir}/pkgconfig/gpr.pc
sed -i "s|${HOME}||g" $HOME%{_libdir}/pkgconfig/grpc.pc
sed -i "s|${HOME}||g" $HOME%{_libdir}/pkgconfig/grpc++.pc
sed -i "s|${HOME}||g" $HOME%{_libdir}/pkgconfig/grpc_unsecure.pc
sed -i "s|${HOME}||g" $HOME%{_libdir}/pkgconfig/grpc++_unsecure.pc
mkdir -p $RPM_BUILD_ROOT/usr/
cp -rp $HOME/usr/* $RPM_BUILD_ROOT/usr/

%files
%{_libdir}/libgrpc++.so
%{_libdir}/libgrpc++.so.*
%{_libdir}/libgrpc_cronet.so
%{_libdir}/libgrpc_cronet.so.*
%{_libdir}/libgrpc_unsecure.so
%{_libdir}/libgrpc_unsecure.so.*
%{_libdir}/libgrpc++_error_details.so
%{_libdir}/libgrpc++_error_details.so.*
%{_libdir}/libgrpc++_reflection.so
%{_libdir}/libgrpc++_reflection.so.*
%{_libdir}/libgrpc++_unsecure.so
%{_libdir}/libgrpc++_unsecure.so.*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgpr.so
%{_libdir}/libgpr.so.*
%{_libdir}/libgrpc.so
%{_libdir}/libgrpc.so.*
%{_libdir}/libaddress_sorting.so
%{_libdir}/libaddress_sorting.so.*
%{_libdir}/libgrpc++_alts.so
%{_libdir}/libgrpc++_alts.so.*
/usr/bin/grpc_*
/usr/share/grpc/roots.pem
%{_libdir}/libgrpcpp_channelz.so
%{_libdir}/libgrpcpp_channelz.so.*
%{_libdir}/libupb.so
%{_libdir}/libupb.so.*

%files devel
%{_libdir}/libupb.a
%{_libdir}/libaddress_sorting.a
%{_libdir}/libgpr.a
%{_libdir}/libgrpc.a
%{_libdir}/libgrpc_unsecure.a
%{_libdir}/libgrpc_cronet.a

/usr/include/grpc/
/usr/include/grpc++/
/usr/include/grpcpp/

%doc

%clean
cd $RPM_SOURCE_DIR
rm -rf grpc*

rm -rf $HOME/usr

%post
#rm -f %{_libdir}/libgrpc++.so.1 %{_libdir}/libgrpc++_reflection.so.1
#ln -s %{_libdir}/libgrpc++.so.%{version} %{_libdir}/libgrpc++.so.1
#ln -s %{_libdir}/libgrpc++_reflection.so.%{version} %{_libdir}/libgrpc++_reflection.so.1

%changelog

