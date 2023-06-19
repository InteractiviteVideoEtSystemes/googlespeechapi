%define         github_name grpc

Name:	        grpc-devel
Version:        1.55.0
Release:        2.ives%{?dist}

Summary:        Google RPC framework

License:        Apache 2.0
URL:            https://grpc.io
Packager:       IVeS

BuildRequires:  cmake3
BuildRequires:  devtoolset-7
BuildRequires:  git
BuildRequires:  gperftools-devel
BuildRequires:  gtest-devel
BuildRequires:  zlib-devel

%description
Static GRPC library from Google and complication headers. Packages dependencies such as ABSEIL, C-ARES and prototol buffer.

%prep
%{__rm} --recursive --force %{_builddir}/%{github_name}-%{version}
# GitHub does not include submodules in assets, we have to use git here instead of source tar.gz
git clone --single-branch --branch=v%{version} https://github.com/%{github_name}/%{github_name}.git %{_builddir}/%{github_name}-%{version}
cd %{_builddir}/%{github_name}-%{version}/
git submodule update --init --recursive third_party/abseil-cpp
git submodule update --init --recursive third_party/boringssl-with-bazel
git submodule update --init --recursive third_party/cares
git submodule update --init --recursive third_party/protobuf
git submodule update --init --recursive third_party/re2
. /opt/rh/devtoolset-7/enable
cmake3 . -DCMAKE_CXX_STANDARD=14 -DCMAKE_INSTALL_LIBDIR=%{_lib} -DCMAKE_INSTALL_PREFIX=%{_prefix} -DgRPC_INSTALL_LIBDIR=%{_lib} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF

%build
cd %{_builddir}/%{github_name}-%{version}/
. /opt/rh/devtoolset-7/enable
cmake3 --build . -j 2

%install
cd %{_builddir}/%{github_name}-%{version}/
. /opt/rh/devtoolset-7/enable
cmake3 --install . --prefix %{buildroot}/opt/google

%clean
%{__rm} --recursive --force %{_builddir}/%{github_name}-%{version}/

%files
/opt/google/%{_lib}/pkgconfig/*.pc
/opt/google/%{_lib}/lib*.a
/opt/google/%{_lib}/cmake/protobuf/
/opt/google/%{_lib}/cmake/utf8_range/
/opt/google/%{_lib}/cmake/re2/
/opt/google/%{_lib}/cmake/c-ares/
/opt/google/%{_lib}/cmake/absl/
/opt/google/lib/cmake/grpc/
/opt/google/lib/cmake/grpc/modules/

# Do not package ARES bins
%exclude /opt/google/bin/acountry
%exclude /opt/google/bin/adig
%exclude /opt/google/bin/ahost

# GRPC plugin
/opt/google/bin/grpc_*

# Protobuf compilers
/opt/google/bin/protoc
/opt/google/bin/protoc-23.1.0
/opt/google/share/grpc/roots.pem

# Headers
/opt/google/include/absl/
/opt/google/include/grpc/
/opt/google/include/grpc++/
/opt/google/include/grpcpp/
/opt/google/include/re2/
/opt/google/include/google/
/opt/google/include/ares.h
/opt/google/include/ares_build.h
/opt/google/include/ares_dns.h
/opt/google/include/ares_rules.h
/opt/google/include/ares_version.h
/opt/google/include/utf8_range.h
/opt/google/include/utf8_validity.h

%doc
# Do not package ARES doc
%exclude /opt/google/share/man/man1/acountry.1
%exclude /opt/google/share/man/man1/adig.1
%exclude /opt/google/share/man/man1/ahost.1
/opt/google/share/man/man3/ares_*
