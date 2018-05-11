%define xmrvariant nvidia 
%define xmrbuildflags -DCUDA_ENABLE=ON -DOpenCL_ENABLE=OFF -DCONF_NO_CPU=ON

%include xmr-stak-common.spec

