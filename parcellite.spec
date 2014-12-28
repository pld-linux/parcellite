Summary:	GTK+ clipboard manager
Summary(pl.UTF-8):	zarządca schowska stworzony w GTK+
######		/home/users/caleb/rpm/packages/../rpm-build-tools/rpm.groups: no such file
Name:		parcellite
Version:	1.1.6
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/parcellite/parcellite-%{version}.tar.gz
# Source0-md5:	4b0a89aeb885a2f7d2ace3e4ea7e153e
URL:		http://parcellite.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
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
