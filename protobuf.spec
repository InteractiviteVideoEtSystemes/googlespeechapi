Name:	protobuf
Version: 3.5.1	
Release: 1.ives%{?dist}
Summary: RPC base API for Google Cloud speech services	

Group: Application/Libraries
License: Google
URL: https://cloud.google.com/speech/	
Source: https://github.com/google/protobuf/releases/download/v%{version}/protobuf-all-%{version}.tar.gz

%description
Google protocol buffer libs and utilities

%prep
cd $RPM_SOURCE_DIR
#rm -rf protobuf-*
#wget https://github.com/google/protobuf/releases/download/v%{version}/protobuf-all-%{version}.tar.gz
#tar xzf protobuf-all-%{version}.tar.gz
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
/usr/include/google/protobuf/
/usr/bin/protoc
%{_libdir}/libprotobuf-lite.*
%{_libdir}/libprotobuf.*
%{_libdir}/libprotoc.*
%{_libdir}/pkgconfig/protobuf.pc
%{_libdir}/pkgconfig/protobuf-lite.pc

#
%doc

%clean
#cd $RPM_SOURCE_DIR
#rm -rf protobuf-*

%changelog

