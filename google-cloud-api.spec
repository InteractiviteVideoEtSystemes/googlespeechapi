Name:	libgoogleapis
Version: 1.2.2	
Release: 2%{?dist}
Summary: RPC base API for Google Cloud speech services	

Group: Application/Development
License: Google
URL: https://github.com/googleapis/googleapis
BuildRequires: grpc = 1.55.0


%description
Google API libraries based on gRPC

%prep
cd $RPM_SOURCE_DIR
rm -rf googleapis
# git clone git@github.com:googleapis/googleapis.git
git clone https://github.com/googleapis/googleapis.git
cd googleapis
# DEc 2019
git checkout 192c14029861752a911ed434fd6ee5b850517cd9
wget --no-check-certificate https://github.com/InteractiviteVideoEtSystemes/googlespeechapi/raw/master/Makefile.libgoogleapis

%build
cd $RPM_SOURCE_DIR
cd googleapis
make GRPCPLUGIN=/usr/bin/grpc_cpp_plugin PROTOINCLUDE=/usr/include
make -f Makefile.libgoogleapis GOOGLEAPIS_GENS_PATH=./gens


%install
cd $RPM_SOURCE_DIR
cd googleapis
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
cp libgoogleapis.a $RPM_BUILD_ROOT/%{_libdir}
make -f Makefile.libgoogleapis clean GOOGLEAPIS_GENS_PATH=./gens
mkdir -p $RPM_BUILD_ROOT/usr/google/apis
cp -rp gens/* $RPM_BUILD_ROOT/usr/google/apis/

%files
%{_libdir}/libgoogleapis.a
/usr/google/apis/

%doc

%clean
cd $RPM_SOURCE_DIR
rm -rf googleapis

%changelog

