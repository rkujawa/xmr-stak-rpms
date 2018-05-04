%define xmrversion 2.4.3
%define xmrdonation 2.0

Name:		xmr-stak-%{xmrvariant}
Version:	%{xmrversion}	
Release:	1%{?dist}
Summary:	Unified All-in-one Monero miner.

Group:		System Environment/Base	
License:	GPLv3
URL:		https://github.com/fireice-uk/xmr-stak
Source0:	xmr-stak-%{xmrversion}.tar.gz

# note this requires source scl_source enable devtoolset-7 before running rpmbuild
BuildRequires:	cmake3 devtoolset-7-gcc-c++ devtoolset-7-libstdc++-devel libmicrohttpd-devel openssl hwloc
Requires:	devtoolset-7-runtime libmicrohttpd openssl-devel hwloc-devel

%description
Unified All-in-one Monero miner.

%prep
%setup -q -n xmr-stak-%{xmrversion}
sed -i "s/fDevDonationLevel = 2.0/fDevDonationLevel = %{xmrdonation}/" xmrstak/donate-level.hpp

%build
cmake3 %{xmrbuildflags} .
make

%install
make install
mkdir -p %{buildroot}/usr/bin/
install -m 755 bin/xmr-stak %{buildroot}/usr/bin/xmr-stak-%{xmrvariant}

%files
/usr/bin/xmr-stak-%{xmrvariant}

%changelog

