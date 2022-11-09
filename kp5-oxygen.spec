#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.26.3
%define		qtver		5.15.2
%define		kpname		oxygen
Summary:	Plasma and Qt widget style and window decorations for Plasma 5 and KDE 4
Name:		kp5-%{kpname}
Version:	5.26.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	abe708f80b03f75463668c12110f5582
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
BuildRequires:	ninja
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
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%ghost %{_libdir}/liboxygenstyle5.so.5
%attr(755,root,root) %{_libdir}/liboxygenstyleconfig5.so.*.*
%ghost %{_libdir}/liboxygenstyleconfig5.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/kstyle_oxygen_config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/org.kde.kdecoration2/oxygendecoration.so
%attr(755,root,root) %{_libdir}/qt5/plugins/styles/oxygen.so
%{_datadir}/plasma/look-and-feel/org.kde.oxygen
%{_iconsdir}/KDE_Classic
%{_datadir}/kservices5/oxygenstyleconfig.desktop
%{_datadir}/kservices5/oxygendecorationconfig.desktop
%{_datadir}/kstyle/themes/oxygen.themerc
%{_iconsdir}/hicolor/256x256/apps/oxygen-settings.png
%{_iconsdir}/Oxygen*
%{_datadir}/color-schemes/Oxygen.colors
%{_datadir}/color-schemes/OxygenCold.colors
