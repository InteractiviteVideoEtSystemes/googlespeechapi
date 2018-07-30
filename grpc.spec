Name:	grpc
Version: 1.11.1	
Release: 1.ives%{?dist}
Summary: Google RPC framework

Group: Development/Library
License: Apache 2.0
URL: https://grpc.io/
Source0: https://github.com/grpc/grpc/archive/v1.11.1.tar.gz


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

%build
cd $RPM_SOURCE_DIR/grpc-%{version}
make prefix=%{buildroot}/usr libdir=%{buildroot}/%{_libdir}


%install
cd $RPM_SOURCE_DIR/grpc-%{version}
make install prefix=%{buildroot}/usr libdir=%{buildroot}/%{_libdir}


%files
%{_libdir}/libgrpc++.so
%{_libdir}/libgrpc++.so.1
%{_libdir}/libgrpc++.so.1.11.1
%{_libdir}/libgrpc++.so.6
%{_libdir}/libgrpc++_cronet.so
%{_libdir}/libgrpc++_cronet.so.1
%{_libdir}/libgrpc++_cronet.so.1.11.1
%{_libdir}/libgrpc++_cronet.so.6
%{_libdir}/libgrpc++_error_details.so
%{_libdir}/libgrpc++_error_details.so.1
%{_libdir}/libgrpc++_error_details.so.1.11.1
%{_libdir}/libgrpc++_error_details.so.6
%{_libdir}/libgrpc++_error_details.so.6.0.0
%{_libdir}/libgrpc++_reflection.so
%{_libdir}/libgrpc++_reflection.so.1
%{_libdir}/libgrpc++_reflection.so.1.11.1
%{_libdir}/libgrpc++_reflection.so.6
%{_libdir}/libgrpc++_reflection.so.6.0.0
%{_libdir}/libgrpc++_unsecure.so
%{_libdir}/libgrpc++_unsecure.so.1
%{_libdir}/libgrpc++_unsecure.so.1.11.1
%{_libdir}/libgrpc++_unsecure.so.6
%{_libdir}/libgrpc++_unsecure.so.6.0.0
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgpr.so
%{_libdir}/libgpr.so.6
%{_libdir}/libgpr.so.6.0.0
%{_libdir}/libgprc.so
%{_libdir}/libgprc.so.6
%{_libdir}/libgprc.so.6.0.0



%files devel
%{_libdir}/libgrpc++.a
%{_libdir}/libgrpc++_cronet.a
%{_libdir}/libgrpc++_error_details.a
%{_libdir}/libgrpc++_reflection.a
%{_libdir}/libgrpc++_unsecure.a
%{_libdir}/libgpr.a
%{_libdir}/libgprc.a
/usr/include/grpc/
/usr/include/grpc++/


%doc

%clean
#cd $RPM_SOURCE_DIR
#rm -rf grpc*
#rm -f v%{version}.*

%changelog

