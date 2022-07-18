#define gitver 20191108
Name:		sbsigntools
Version:	0.9.4
Release:	2
Summary:	Tool for signing secure-boot efi binaries
Group:		System
License:	GPLv2+
URL:		https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
# (tpg) this source is broken, please use sbsigntools-mktarball.sh
#Source0:	https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/snapshot/sbsigntools-%{version}.tar.gz
Source0:	sbsigntools-%{version}.tar.xz
# don't fetch ccan or run git from autogen.sh, already done by mktarball.sh
Patch0:		%{name}-no-git.patch
# add Fedora gnu-efi path and link statically against libefi.a/libgnuefi.a
# do not enable this Patch1:		%{name}-gnuefi.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1955828
Patch2:		https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/patch/?id=f12484869c9590682ac3253d583bf59b890bb826#/f12484869c9590682ac3253d583bf59b890bb826.patch
# https://groups.io/g/sbsigntools/message/54
Patch3:		%{name}-openssl3.patch
BuildRequires:	binutils-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	gnu-efi
BuildRequires:	help2man

%description
Tools for signing secure-boot efi binaries.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build "CFLAGS=$CFLAGS -Wno-error"

%install
%make_install

%files
%doc COPYING README
%{_bindir}/*
%doc %{_mandir}/man1/*.1.*
