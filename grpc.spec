%define version_tag 1.33.2

Name:	grpc
Version: 1.33.2
Release: 1.ives%{?dist}
Summary: Google RPC framework

Group: Development/Library
License: Apache 2.0
URL: https://grpc.io/
Source0: https://github.com/grpc/grpc/archive/v1.33.2.tar.gz
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
rm -rf grpc-* v*
wget https://github.com/grpc/grpc/archive/v%{version_tag}.tar.gz
tar xzf v%{version_tag}.tar.gz
cd $RPM_SOURCE_DIR/grpc-%{version_tag}
wget https://github.com/InteractiviteVideoEtSystemes/googlespeechapi/raw/master/gprc-makefile.patch
patch -p0 < gprc-makefile.patch
#rm -f Makefile
#mv Makefile.grpc Makefile

%build
cd $RPM_SOURCE_DIR/grpc-%{version_tag}
make prefix=%{buildroot}/usr/local


%install
cd $RPM_SOURCE_DIR/grpc-%{version_tag}
make install prefix=%{buildroot}/usr/local
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/usr/local/lib/pkgconfig/gpr.pc
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/usr/local/lib/pkgconfig/grpc.pc
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/usr/local/lib/pkgconfig/grpc++.pc
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/usr/local/lib/pkgconfig/grpc_unsecure.pc
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/usr/local/lib/pkgconfig/grpc++_unsecure.pc

%files
/usr/local/lib/libgrpc++.so
/usr/local/lib/libgrpc++.so.*
/usr/local/lib/libgrpc_cronet.so
/usr/local/lib/libgrpc_cronet.so.*
/usr/local/lib/libgrpc_unsecure.so
/usr/local/lib/libgrpc_unsecure.so.*
/usr/local/lib/libgrpc++_cronet.so
/usr/local/lib/libgrpc++_cronet.so.*
/usr/local/lib/libgrpc++_error_details.so
/usr/local/lib/libgrpc++_error_details.so.*
/usr/local/lib/libgrpc++_reflection.so
/usr/local/lib/libgrpc++_reflection.so.*
/usr/local/lib/libgrpc++_unsecure.so
/usr/local/lib/libgrpc++_unsecure.so.*
/usr/local/lib/pkgconfig/*.pc
/usr/local/lib/libgpr.so
/usr/local/lib/libgpr.so.*
/usr/local/lib/libgrpc.so
/usr/local/lib/libgrpc.so.*
/usr/local/lib/libaddress_sorting.so
/usr/local/lib/libaddress_sorting.so.*
/usr/local/bin/grpc_*
/usr/local/share/grpc/roots.pem
/usr/local/lib/libgrpcpp_channelz.so
/usr/local/lib/libgrpcpp_channelz.so.*

%files devel
/usr/local/lib/libgrpc++.a
/usr/local/lib/libgrpc++_cronet.a
/usr/local/lib/libgrpc++_error_details.a
/usr/local/lib/libgrpc++_reflection.a
/usr/local/lib/libgrpc++_unsecure.a
/usr/local/lib/libgpr.a
/usr/local/lib/libgrpc.a
/usr/local/lib/libaddress_sorting.a
/usr/local/lib/libgrpc_cronet.a
/usr/local/lib/libgrpc_unsecure.a
/usr/local/lib/libgrpcpp_channelz.a
/usr/local/include/grpc/
/usr/local/include/grpc++/
/usr/local/include/grpcpp/

%doc

%clean
cd $RPM_SOURCE_DIR
rm -rf grpc*
rm -f v%{version}.*

%post
rm -f /usr/local/lib/libgrpc++.so.1 /usr/local/lib/libgrpc++_reflection.so.1
ln -s /usr/local/lib/libgrpc++.so.%{version} /usr/local/lib/libgrpc++.so.1
ln -s /usr/local/lib/libgrpc++_reflection.so.%{version} /usr/local/lib/libgrpc++_reflection.so.1

%changelog

