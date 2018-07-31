Name:	grpc
Version: 1.11.1	
Release: 1.ives%{?dist}
Summary: Google RPC framework

Group: Development/Library
License: Apache 2.0
URL: https://grpc.io/
Source0: https://github.com/grpc/grpc/archive/v1.11.1.tar.gz
Source1: https://github.com/InteractiviteVideoEtSystemes/googlespeechapi/raw/master/Makefile.grpc

BuildRequires: protobuf-devel, gtest-devel, gperftools-devel


%description
Google speech API compiled with all its dependencies

%package devel
Summary: Header and static lib for GRPC library

%description devel
Google RPC framework headers

%prep
cd $RPM_SOURCE_DIR
rm -rf grpc-* v*
wget https://github.com/grpc/grpc/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
cd $RPM_SOURCE_DIR/grpc-%{version}
wget https://github.com/InteractiviteVideoEtSystemes/googlespeechapi/raw/master/Makefile.grpc
rm -f Makefile
mv Makefile.grpc Makefile

%build
cd $RPM_SOURCE_DIR/grpc-%{version}
make prefix=%{buildroot}/opt/google


%install
cd $RPM_SOURCE_DIR/grpc-%{version}
make install prefix=%{buildroot}/opt/google
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/opt/google/lib/pkgconfig/grpc.pc
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/opt/google/lib/pkgconfig/grpc++.pc
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/opt/google/lib/pkgconfig/grpc_unsecure.pc
sed -i "s|${RPM_BUILD_ROOT}||g" $RPM_BUILD_ROOT/opt/google/lib/pkgconfig/grpc++_unsecure.pc

%files
/opt/google/lib/libgrpc++.so
/opt/google/lib/libgrpc++.so.1.11.1
/opt/google/lib/libgrpc++.so.6
/opt/google/lib/libgrpc_cronet.so
/opt/google/lib/libgrpc_cronet.so.6
/opt/google/lib/libgrpc_cronet.so.6.0.0
/opt/google/lib/libgrpc_unsecure.so
/opt/google/lib/libgrpc_unsecure.so.6
/opt/google/lib/libgrpc_unsecure.so.6.0.0
/opt/google/lib/libgrpc++_cronet.so
/opt/google/lib/libgrpc++_cronet.so.1.11.1
/opt/google/lib/libgrpc++_cronet.so.6
/opt/google/lib/libgrpc++_error_details.so
/opt/google/lib/libgrpc++_error_details.so.1.11.1
/opt/google/lib/libgrpc++_error_details.so.6
/opt/google/lib/libgrpc++_reflection.so
/opt/google/lib/libgrpc++_reflection.so.1.11.1
/opt/google/lib/libgrpc++_reflection.so.6
/opt/google/lib/libgrpc++_unsecure.so
/opt/google/lib/libgrpc++_unsecure.so.1.11.1
/opt/google/lib/libgrpc++_unsecure.so.6
/opt/google/lib/pkgconfig/*.pc
/opt/google/lib/libgpr.so
/opt/google/lib/libgpr.so.6
/opt/google/lib/libgpr.so.6.0.0
/opt/google/lib/libgrpc.so
/opt/google/lib/libgrpc.so.6
/opt/google/lib/libgrpc.so.6.0.0
/opt/google/lib/libaddress_sorting.so
/opt/google/lib/libaddress_sorting.so.6
/opt/google/lib/libaddress_sorting.so.6.0.0
/opt/google/bin/grpc_*
/opt/google/share/grpc/roots.pem

%files devel
/opt/google/lib/libgrpc++.a
/opt/google/lib/libgrpc++_cronet.a
/opt/google/lib/libgrpc++_error_details.a
/opt/google/lib/libgrpc++_reflection.a
/opt/google/lib/libgrpc++_unsecure.a
/opt/google/lib/libgpr.a
/opt/google/lib/libgrpc.a
/opt/google/lib/libaddress_sorting.a
/opt/google/lib/libgrpc_cronet.a
/opt/google/lib/libgrpc_unsecure.a
/opt/google/include/grpc/
/opt/google/include/grpc++/
/opt/google/include/grpcpp/

%doc

%clean
cd $RPM_SOURCE_DIR
rm -rf grpc*
rm -f v%{version}.*

%changelog

