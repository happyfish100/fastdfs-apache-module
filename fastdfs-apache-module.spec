Name: fastdfs-apache-module
Version: 1.0.0
Release: 1%{?dist}
Summary: The apache module of fastdfs
License: GPL
Group: Arch/Tech
URL: 	http://perso.orange.fr/sebastien.godard/
Source: http://perso.orange.fr/sebastien.godard/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

#Requires: /sbin/chkconfig
#Requires: sh-utils textutils grep fileutils /etc/cron.d
#BuildRequires: libmcclient-devel
#Requires: %__cp %__mv %__chmod %__grep %__mkdir %__install %__id
Requires: libfdfsclient

%description
This package provides apache module of fastdfs

%prep
%setup -q

%build
# FIXME: I need to fix the upstream Makefile to use LIBDIR et al. properly and
# send the upstream maintainer a patch.
# add DOCDIR to the configure part
cd src
make
%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib64/httpd/modules
cp -f src/.libs/mod_fastdfs.so  %{buildroot}/usr/lib64/httpd/modules/

#make install IGNORE_MAN_GROUP=y DOC_DIR=%{_docdir}/%{name}-%{version} INIT_DIR=%{_initrddir}

#install -m 0644 sysstat.crond %{buildroot}/%{_sysconfdir}/cron.d/sysstat

#%find_lang %{name}

%post

%preun

%postun

%clean
#rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/httpd/modules/*

%changelog
* Mon Jun 23 2014  Zaixue Liao <liaozaixue@yongche.com>
- first RPM release (1.0)
