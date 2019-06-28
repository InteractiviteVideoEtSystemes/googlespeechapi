Name:	protobuf
Version: 3.8.0	
Release: 1.ives%{?dist}
Summary: RPC base API for Google Cloud speech services	

Group: Application/Libraries
License: Google
URL: https://github.com/google/protobuf
Source: https://github.com/google/protobuf/releases/download/v%{version}/protobuf-all-%{version}.tar.gz

%description
Google protocol buffer libs and utilities

%package devel
Summary: Static lib and headers
Group: Application/Libraries

%description devel
All headers needed to use Google protobuf lib

%prep
cd $RPM_SOURCE_DIR
rm -rf protobuf-*
wget https://github.com/google/protobuf/releases/download/v%{version}/protobuf-all-%{version}.tar.gz
tar xzf protobuf-all-%{version}.tar.gz
cd protobuf-%{version}
./configure --prefix=/usr --libdir=%{_libdir}


%build
cd $RPM_SOURCE_DIR
cd protobuf-%{version}
make

%install
cd $RPM_SOURCE_DIR
cd protobuf-%{version}
make install DESTDIR=%{buildroot}


%files
/usr/bin/protoc
%{_libdir}/libprotoc.*
%{_libdir}/libprotobuf-lite.so
%{_libdir}/libprotobuf-lite.so.15
%{_libdir}/libprotobuf-lite.so.15.0.1
%{_libdir}/libprotobuf.so
%{_libdir}/libprotobuf.so.15
%{_libdir}/libprotobuf.so.15.0.1
%{_libdir}/pkgconfig/protobuf.pc
%{_libdir}/pkgconfig/protobuf-lite.pc

%files devel
/usr/include/google/protobuf/
%{_libdir}/libprotobuf-lite.a
%{_libdir}/libprotobuf-lite.la
%{_libdir}/libprotobuf.a
%{_libdir}/libprotobuf.la
#
%doc

%clean
cd $RPM_SOURCE_DIR
rm -rf protobuf-*

%changelog

