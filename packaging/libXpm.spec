Name:           libXpm
Version:        3.5.10
Release:        1
License:        MIT
Summary:        XPM format pixmap library
Url:            http://www.x.org
Group:          Graphics/X Window System

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
Summary:        XPM format pixmap library
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxpm-devel

%description devel
X.Org X11 libXpm development package

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXpm.so.4
%{_libdir}/libXpm.so.4.11.0

%files devel
%defattr(-,root,root,-)
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
