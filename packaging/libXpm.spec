#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           libXpm
Version:        3.5.10
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System Environment/Libraries

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)

%description
X.Org X11 libXpm runtime library

%package devel
Summary:        X
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxpm-devel

%description devel
X.Org X11 libXpm development package

%prep
%setup -q

%build
%reconfigure --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXpm.so.4
%{_libdir}/libXpm.so.4.11.0

%files devel
%defattr(-,root,root,-)
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
