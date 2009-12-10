Summary:	GTK+ clipboard manager
Summary(pl.UTF-8):	zarządca schowska stworzony w GTK+
Name:		parcellite
Version:	0.9.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/project/parcellite/parcellite/%{name}-%{version}/parcellite-0.9.1.tar.gz
# Source0-md5:	099d1ccc9fa1e59d3e3b19b77a90a8fb
Patch0:		%{name}-desktop.patch
URL:		http://parcellite.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2.10.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parcellite is a lightweight GTK+ clipboard manager.

%description -l pl.UTF-8
Parcellite to lekki zarządca schowka stworzony w GTK+.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/%{name}
%doc AUTHORS ChangeLog COPYING README NEWS TODO
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/xdg/autostart/parcellite-startup.desktop
%{_desktopdir}/%{name}.desktop
