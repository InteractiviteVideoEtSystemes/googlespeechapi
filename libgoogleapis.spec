# DEC 2019
%define         googleapis_commit_id    192c14029861752a911ed434fd6ee5b850517cd9
%undefine       _disable_source_fetch

Name:	        libgoogleapis
Version:        1.2.3	
Release:        1%{?dist}

Summary:        RPC base API for Google Cloud speech services	

License:        Google
URL:            https://github.com/googleapis/googleapis
Packager:       IVeS

Source0:       	https://github.com/googleapis/googleapis/archive/%{googleapis_commit_id}.zip
Source1:        https://raw.githubusercontent.com/InteractiviteVideoEtSystemes/googlespeechapi/%{version}/Makefile.libgoogleapis

BuildRequires:  grpc-devel = 1.55.0
BuildRequires:  git
BuildRequires:  devtoolset-7

%description
Google API libraries based on gRPC.

%prep
%setup -q -n googleapis-%{googleapis_commit_id}
%{__cp} %{_sourcedir}/Makefile.libgoogleapis %{_builddir}/googleapis-%{googleapis_commit_id}/

%build
cd %{_builddir}/googleapis-%{googleapis_commit_id}/
. /opt/rh/devtoolset-7/enable
make GRPCPLUGIN=/opt/google/bin/grpc_cpp_plugin PROTOINCLUDE=/opt/google/include PROTOC=/opt/google/bin/protoc
make -f Makefile.libgoogleapis GOOGLEAPIS_GENS_PATH=./gens

%install
cd %{_builddir}/googleapis-%{googleapis_commit_id}/
mkdir -p %{buildroot}/opt/google/%{_lib}
cp libgoogleapis.a %{buildroot}/opt/google/%{_lib}
make -f Makefile.libgoogleapis install GOOGLEAPIS_GENS_PATH=./gens DESTDIR=%{buildroot}

%clean
rm -rf %{_builddir}/googleapis-%{googleapis_commit_id}/ %{_sourcedir}/Makefile.libgoogleapis %{_sourcedir}/%{googleapis_commit_id}.zip

%files
/opt/google/%{_lib}/libgoogleapis.a
/opt/google/include/googleapis/
