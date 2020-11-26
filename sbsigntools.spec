#define gitver 20191108
Name:		sbsigntools
Version:	0.9.4
Release:	1
Summary:	Tool for signing secure-boot efi binaries
Group:		System
License:	GPLv2+
URL:		https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
# (tpg) this source is broken, please use sbsigntools-mktarball.sh
#Source0:	https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/snapshot/sbsigntools-%{version}.tar.gz
Source0:	sbsigntools-%{version}.tar.xz
Patch0:		sbsigntools-no-git.patch
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
%{_mandir}/man1/sbattach.1.*
%{_mandir}/man1/sbsiglist.1.*
%{_mandir}/man1/sbsign.1.*
%{_mandir}/man1/sbvarsign.1.*
%{_mandir}/man1/sbverify.1.*
%{_mandir}/man1/sbkeysync.1.*