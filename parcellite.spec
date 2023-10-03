Summary:	GTK+ clipboard manager
Summary(pl.UTF-8):	Zarządca schowka stworzony w GTK+
Name:		parcellite
Version:	1.2.6
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	https://github.com/ZaWertun/parcellite/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	3875fd547557a99711da4d3087948b1c
Source1:	%{name}-startup.desktop
URL:		https://parcellite.sourceforge.net/
BuildRequires:	cmake >= 3.1
BuildRequires:	glib2-devel >= 2.14.0
BuildRequires:	gtk+2-devel >= 2.10.0
BuildRequires:	intltool >= 0.23
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
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/xdg/autostart
cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/xdg/autostart
install -D data/%{name}.appdata.xml $RPM_BUILD_ROOT%{_datadir}/metainfo/%{name}.appdata.xml

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# duplicate of pl
rm -fr $RPM_BUILD_ROOT%{_localedir}/pl_PL

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/%{name}
%doc AUTHORS ChangeLog README.md
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/xdg/autostart/parcellite-startup.desktop
%{_desktopdir}/parcellite.desktop
%{_iconsdir}/hicolor/*x*/apps/parcellite.png
%{_iconsdir}/hicolor/scalable/apps/parcellite.svg
%{_datadir}/metainfo/parcellite.appdata.xml
