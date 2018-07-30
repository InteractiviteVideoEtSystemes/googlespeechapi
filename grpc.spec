Name:	grpc
Version: 1.11.1	
Release: 1.ives%{?dist}
Summary: RPC base API for Google Cloud speech services	

Group: Development/Library
License: Apache 2.0
URL: https://grpc.io/
Source0: https://github.com/grpc/grpc/archive/v1.11.1.tar.gz


BuildRequires:	c-ares-devel, git, protobuf-devel, gtest-devel, gperftools-devel
Requires: c-ares	

%description
Google speech API compiled with all its dependencies

%package devel


%prep
cd $RPM_SOURCE_DIR
#rm -rf grpc-*
wget https://github.com/grpc/grpc/archive/v%{version}.tar.gz
tar xzf grpc-%{version}.tar.gz

%build
cd $RPM_SOURCE_DIR/grpc-%{version}
make


%install
cd $RPM_SOURCE_DIR/grpc-%{version}
make install DESTDIR=%{buildroot}


%files
%{_libdir}/libgrpc++.so
%{_libdir}/libgrpc++.so.1
%{_libdir}/libgrpc++.so.1.11.1
%{_libdir}/libgrpc++_cronet.so
%{_libdir}/libgrpc++_cronet.so.1
%{_libdir}/libgrpc++_cronet.so.1.11.1
%{_libdir}/libgrpc++_error_details.so
%{_libdir}/libgrpc++_error_details.so.1
%{_libdir}/libgrpc++_error_details.so.1.11.1
%{_libdir}/libgrpc++_reflection.so
%{_libdir}/libgrpc++_reflection.so.1
%{_libdir}/libgrpc++_reflection.so.1.11.1
%{_libdir}/libgrpc++_unsecure.so
%{_libdir}/libgrpc++_unsecure.so.1
%{_libdir}/libgrpc++_unsecure.so.1.11.1



%files devel
%{_libdir}/libgrpc++.a
%{_libdir}/libgrpc++_cronet.a
%{_libdir}/libgrpc++_error_details.a
%{_libdir}/libgrpc++_reflection.a
%{_libdir}/libgrpc++_unsecure.a

%doc

%clean
cd $RPM_SOURCE_DIR
rm -rf grpc*

%changelog

