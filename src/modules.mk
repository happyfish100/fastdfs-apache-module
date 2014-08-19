mod_fastdfs.la: mod_fastdfs.slo
	$(SH_LINK) -rpath $(libexecdir) -module -avoid-version  mod_fastdfs.lo
DISTCLEAN_TARGETS = modules.mk
shared =  mod_fastdfs.la
