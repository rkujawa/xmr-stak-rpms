%define xmrversion 2.10.7
%define xmrdonation 2.0

Name:		xmr-stak-%{xmrvariant}
Version:	%{xmrversion}	
Release:	2%{?dist}
Summary:	Unified All-in-one Monero miner.

Group:		System Environment/Base	
License:	GPLv3
URL:		https://github.com/fireice-uk/xmr-stak
Source0:	xmr-stak-%{xmrversion}.tar.gz

# in theory it would be best to add -g to gcc, to generate debuginfo packages later, however fuck CMake
%define debug_package %{nil}

%if 0%{?rhel}
# note this requires source scl_source enable devtoolset-7 before running rpmbuild
BuildRequires:	cmake3 devtoolset-7-gcc-c++ devtoolset-7-libstdc++-devel libmicrohttpd-devel openssl-devel hwloc-devel %{?xmrvariantbuildreqs}
Requires:	libmicrohttpd openssl hwloc %{?xmrvariantreqs}
%endif

%if 0%{?fedora}
BuildRequires:	cmake3 gcc-c++ libstdc++-devel libmicrohttpd-devel openssl-devel hwloc-devel %{?xmrvariantbuildreqs}
Requires:	libmicrohttpd openssl hwloc %{?xmrvariantreqs}
%endif

%description
Unified All-in-one Monero miner.

%prep
%setup -q -n xmr-stak-%{xmrversion}
sed -i "s/fDevDonationLevel = 2.0/fDevDonationLevel = %{xmrdonation}/" xmrstak/donate-level.hpp

%build
%if 0%{?fedora} && "%{xmrvariant}" == "nvidia"
CC=cuda-gcc
CXX=cuda-g++
export CC CXX
%endif

cmake3 %{xmrbuildflags} .
make

%install
make install
mkdir -p %{buildroot}/usr/bin/
install -m 755 bin/xmr-stak %{buildroot}/usr/bin/xmr-stak-%{xmrvariant}

%files
/usr/bin/xmr-stak-%{xmrvariant}

%changelog

