%define		kdeplasmaver	5.11.0
%define		qtver		5.3.2
%define		kpname		oxygen
Summary:	Plasma and Qt widget style and window decorations for Plasma 5 and KDE 4
Name:		kp5-%{kpname}
Version:	5.11.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	e346d3d92b2a9e75f484724fe8754928
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-frameworkintegration-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plasma and Qt widget style and window decorations for Plasma 5 and KDE
4 A plugin-based library to create window decorations.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oxygen-demo5
%attr(755,root,root) %{_bindir}/oxygen-settings5
%attr(755,root,root) %{_libdir}/liboxygenstyle5.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liboxygenstyle5.so.5
%attr(755,root,root) %{_libdir}/liboxygenstyleconfig5.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liboxygenstyleconfig5.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/kstyle_oxygen_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kdecoration2/oxygendecoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/styles/oxygen.so
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_iconsdir}/KDE_Classic
%{_datadir}/kservices5/oxygenstyleconfig.desktop
%{_datadir}/kservices5/oxygendecorationconfig.desktop
%{_datadir}/kstyle/themes/oxygen.themerc
%{_datadir}/sounds/Oxygen*.ogg
%{_iconsdir}/hicolor/256x256/apps/oxygen-settings.png
%{_iconsdir}/Oxygen*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboxygenstyle5.so
%attr(755,root,root) %{_libdir}/liboxygenstyleconfig5.so
