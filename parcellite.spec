Summary:	GTK+ clipboard manager
Summary(pl.UTF-8):	zarządca schowska stworzony w GTK+
Name:		parcellite
Version:	1.1.9
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/parcellite/%{name}-%{version}.tar.gz
# Source0-md5:	6c3b70165c2dee9341a81a2a8481e446
URL:		http://parcellite.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2.10.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
Suggests:	xdotool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parcellite is a lightweight GTK+ clipboard manager.

%description -l pl.UTF-8
Parcellite to lekki zarządca schowka stworzony w GTK+.

%prep
%setup -q

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

# duplicate of pl
rm -fr $RPM_BUILD_ROOT%{_localedir}/pl_PL

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/%{name}
%doc AUTHORS ChangeLog COPYING README NEWS TODO
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/xdg/autostart/parcellite-startup.desktop
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}.xpm
%{_pixmapsdir}/%{name}.svg
