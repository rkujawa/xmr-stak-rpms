%define xmrvariant nvidia 
%define xmrbuildflags -DCUDA_ENABLE=ON -DOpenCL_ENABLE=OFF -DCONF_NO_CPU=ON

%define xmrvariantreqs cuda

%if 0%{?fedora}
%define xmrvariantbuildreqs cuda-devel cuda-gcc-c++ cuda-gcc
%endif

%if 0%{?rhel}
%define xmrvariantbuildreqs cuda-devel
%endif

%include xmr-stak-common.spec

