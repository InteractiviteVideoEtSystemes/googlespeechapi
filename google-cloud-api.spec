Name:	libgoogleapis
Version: 1.0.0	
Release: 1%{?dist}
Summary: RPC base API for Google Cloud speech services	

Group: Application/Development
License: Google
URL: https://github.com/googleapis/googleapis



%description
Google API libraries based on gRPC

%prep
cd $RPM_SOURCE_DIR
rm -rf googleapis
git clone git@github.com:googleapis/googleapis.git
git checkout 01d7d7d21ab5b8610f351b11552dff2caf0c0a23
cd googleapis
wget https://github.com/InteractiviteVideoEtSystemes/googlespeechapi/raw/master/Makefile.libgoogleapis

%build
cd $RPM_SOURCE_DIR
cd googleapis
make GRPCPLUGIN=/opt/google/bin/grpc_cpp_plugin
make -f Makefile.libgoogleapis GOOGLEAPIS_GENS_PATH=./gens


%install
cd $RPM_SOURCE_DIR
cd googleapis
mkdir -p $RPM_BUILD_ROOT/opt/google/lib
cp libgoogleapis.a $RPM_BUILD_ROOT/opt/google/lib
make -f Makefile.libgoogleapis clean
mkdir -p $RPM_BUILD_ROOT/opt/google/apis
cp -rp gens/* $RPM_BUILD_ROOT/opt/google/apis/

%files
/opt/google/lib/libgoogleapis.a
/opt/google/apis/

%doc

%clean
#cd $RPM_SOURCE_DIR
#rm -rf googleapis

%changelog

