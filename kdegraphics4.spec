Name: kdegraphics4
Summary: K Desktop Environment
Version: 4.0.1
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 1
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegraphics-%version.tar.bz2
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: jpeg-devel 
BuildRequires: png-devel 
BuildRequires: libimlib-devel 
BuildRequires: libtiff-devel
BuildRequires: zlib-devel 
BuildRequires: bzip2-devel
BuildRequires: gettext texinfo
BuildRequires: kdelibs4-devel
BuildRequires: X11-devel 
BuildRequires: freetype2-devel
BuildRequires: openssl-devel 
BuildRequires: libsane-devel 
BuildRequires: OpenEXR-devel
BuildRequires: libtiff-progs
BuildRequires: gphoto2-devel
BuildRequires: fontconfig-devel
BuildRequires: libpoppler-qt4-devel
BuildRequires: mesaglut-devel
BuildRequires: djvulibre-devel
BuildRequires: libchm-devel
BuildRequires: libgs-devel
BuildRequires: libexiv-devel
BuildRequires: qimageblitz-devel
Requires: %name-core
Requires: kde4-ksnapshot
Obsoletes: kde4-kfax < 2:3.93.0-0.714385.1
Requires: kde4-kcolorchooser
Requires: kde4-okular
Requires: kde4-gwenview
Requires: kde4-kruler
Requires: kde4-kolourpaint
Requires: kde4-kgamma

%description
Graphical tools for the K Desktop Environment.
kdegraphics is a collection of graphic oriented applications

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package core
Summary: Core files for kdegraphics
Group: Graphical desktop/KDE	
Requires: kdelibs4-core
Requires: libgphoto-hotplug
Obsoletes: kdegraphics4-common < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kview < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kiconedit < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kpovmodeler < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-ksvg < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kooka < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-mrmlsearch < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kcoloredit < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kview < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kpovmodeler < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-ksvg < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kooka < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-common < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kscan1 < 2:3.93.0-0.714385.1

%description core
Common files for kdegraphics

%files core
%defattr(-,root,root)
%_kde_libdir/kde4/gsthumbnail.so
%_kde_libdir/kde4/svgpart.so
%_kde_appsdir/svgpart/svgpart.rc
%_kde_datadir/kde4/services/svgpart.desktop
%_kde_libdir/strigi/*
%_kde_datadir/kde4/services/gsthumbnail.desktop
%_kde_libdir/kde4/kscanplugin.so
%_kde_iconsdir/*/*/*/palette_*
%_kde_datadir/kde4/services/scanservice.desktop

#------------------------------------------------	

%define libokularcore %mklibname okularcore 1

%package -n %libokularcore
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdegraphics40-okular < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kghostviewlib1 <  2:3.95.2-0.734790.2

%description -n %libokularcore
KDE 4 core library.

%post -n %libokularcore -p /sbin/ldconfig
%postun -n %libokularcore -p /sbin/ldconfig

%files -n %libokularcore
%defattr(-,root,root)
%_kde_libdir/libokularcore.so.*

#------------------------------------------------

%define libspectreOkular %mklibname spectreOkular 1

%package -n %libspectreOkular
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libspectreOkular
KDE 4 core library.

%post -n %libspectreOkular -p /sbin/ldconfig
%postun -n %libspectreOkular -p /sbin/ldconfig

%files -n %libspectreOkular
%defattr(-,root,root)
%_kde_libdir/libspectreOkular.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kgamma
Summary: kgamma color profiling
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description -n kde4-kgamma
kgamma color profiling

%files -n kde4-kgamma
%defattr(-,root,root)
%_kde_datadir/kde4/services/kgamma*
%_kde_appsdir/kgamma
%_kde_iconsdir/*/*/*/kgamma*
%_kde_libdir/kde4/*_kgamma.*

#-----------------------------------------------------------------------------

%package -n kde4-kamera
Summary: kamera ioslave
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kamera < 2:3.93.0-0.714385.1

%description -n kde4-kamera
Dialog KDE base widgets

%files -n kde4-kamera
%defattr(-,root,root)
%dir %_kde_docdir/HTML/en/kamera
%doc %_kde_docdir/HTML/en/kamera/*
%_kde_libdir/kde4/*_kamera.*
%_kde_datadir/kde4/services/camera*
%_kde_datadir/kde4/services/kamera*

#-----------------------------------------------------------------------------

%package -n kde4-okular
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-okular < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kpdf < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kdvi < 2:3.93.0-0.714385.1
Obsoletes: kde4-kghostview < 2:3.95.2-0.734790.2
Conflicts: %name-devel < 2:3.95.2-0.734790.2

%description -n kde4-okular
Dialog KDE base widgets

%files -n kde4-okular
%defattr(-,root,root)
%_kde_bindir/okular
%_kde_bindir/xf86gammacfg
%_kde_libdir/kde4/okularGenerator_*
%_kde_libdir/kde4/okularpart.so
%_kde_libdir/kde4/kio_msits.so
%_kde_libdir/libspectreOkular.so
%_kde_datadir/applications/kde4/okular*
%_kde_appsdir/okular
%_kde_datadir/config.kcfg/okular.kcfg
%_kde_datadir/config/okular.knsrc
%_kde_datadir/kde4/services/libokularGenerator_*
%_kde_datadir/kde4/services/okular*
%_kde_datadir/kde4/services/msits*
%_kde_datadir/kde4/servicetypes/okularGenerator.desktop
%dir %_kde_docdir/HTML/en/okular
%doc %_kde_docdir/HTML/en/okular/*

#------------------------------------------------	

%define libgwenviewlib %mklibname gwenviewlib 1

%package -n %libgwenviewlib
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libgwenviewlib
KDE 4 core library.

%post -n %libgwenviewlib -p /sbin/ldconfig
%postun -n %libgwenviewlib -p /sbin/ldconfig

%files -n %libgwenviewlib
%defattr(-,root,root)
%_kde_libdir/libgwenviewlib.so.*

#-----------------------------------------------------------------------------

%package -n kde4-gwenview
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-gwenview < 2:3.93.0-0.714385.1

%description -n kde4-gwenview
Dialog KDE base widgets

%files -n kde4-gwenview
%defattr(-,root,root)
%_kde_bindir/gwenview
%_kde_libdir/kde4/gvpart.so
%_kde_appsdir/gvpart/gvpart.rc
%_kde_appsdir/gwenview/gwenviewui.rc
%_kde_datadir/kde4/services/gvpart.desktop
%_kde_datadir/applications/kde4/gwenview.desktop
%_kde_iconsdir/*/*/*/gwenview*
%_kde_docdir/*/*/gwenview

#-----------------------------------------------------------------------------

%package -n kde4-kcolorchooser
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: kdegraphics4-kcolorchooser < 2:3.93.0-0.714385.1

%description -n kde4-kcolorchooser
Dialog KDE base widgets

%files -n kde4-kcolorchooser
%defattr(-,root,root)
%_kde_bindir/kcolorchooser
%_kde_datadir/applications/kde4/kcolorchooser.desktop
%_kde_iconsdir/*/*/*/kcolorchooser*

#-----------------------------------------------------------------------------

%define libkolourpaint4_lgpl %mklibname kolourpaint4_lgpl 4

%package -n %libkolourpaint4_lgpl
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdegraphics40-kghostview < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kolourpaint4_lgpl4 < 2:3.94.0
Obsoletes: %{_lib}kolourpaint_lgpl4 < 2:3.94.0

%description -n %libkolourpaint4_lgpl
KDE 4 core library.

%post -n %libkolourpaint4_lgpl -p /sbin/ldconfig
%postun -n %libkolourpaint4_lgpl -p /sbin/ldconfig

%files -n %libkolourpaint4_lgpl
%defattr(-,root,root)
%_kde_libdir/libkolourpaint4_lgpl.so.*

#-----------------------------------------------------------------------------

%package -n kde4-kolourpaint
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kolourpaint < 2:3.93.0-0.714385.1

%description -n kde4-kolourpaint
Dialog KDE base widgets

%files -n kde4-kolourpaint
%defattr(-,root,root)
%_kde_bindir/kolourpaint4
%_kde_datadir/applications/kde4/kolourpaint4.desktop
%_kde_appsdir/kolourpaint4
%_kde_iconsdir/hicolor/*/apps/kolourpaint4.*

%dir %_kde_docdir/HTML/en/kolourpaint4
%doc %_kde_docdir/HTML/en/kolourpaint4/*

#-----------------------------------------------------------------------------

%package -n kde4-kruler
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kruler < 2:3.93.0-0.714385.1

%description -n kde4-kruler
Dialog KDE base widgets

%files -n kde4-kruler
%defattr(-,root,root)
%_kde_bindir/kruler
%_kde_datadir/applications/kde4/kruler.desktop
%_kde_appsdir/kruler
%_kde_iconsdir/*/*/*/kruler*
%_kde_docdir/*/*/kruler

#-----------------------------------------------------------------------------

%package -n kde4-ksnapshot
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-ksnapshot < 2:3.93.0-0.714385.1

%description -n kde4-ksnapshot
Dialog KDE base widgets

%files -n kde4-ksnapshot
%defattr(-,root,root)
%_kde_bindir/kbackgroundsnapshot
%_kde_bindir/ksnapshot
%_kde_datadir/applications/kde4/ksnapshot.desktop
%_kde_iconsdir/*/*/*/ksnapshot*
%_datadir/dbus-1/interfaces/org.kde.ksnapshot.xml
%_kde_docdir/*/*/ksnapshot

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdegraphics
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libokularcore = %epoch:%version-%release
Requires: %libgwenviewlib = %epoch:%version-%release
Requires: %libspectreOkular = %epoch:%version-%release
Obsoletes: %{_lib}kdegraphics40-ksvg-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kview-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kooka-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kpovmodeler-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-common-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kghostview-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-okular-devel < 2:3.93.0-0.714385.1
Conflicts: kde4-okular < 2:3.95.2-0.734790.2

%description  devel
This package contains header files needed if you wish to build applications based on kdegraphics.

%files devel
%defattr(-,root,root)
%_kde_libdir/libgwenviewlib.so
%_kde_libdir/libkolourpaint4_lgpl.so
%_kde_libdir/libokularcore.so
%_kde_prefix/include/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdegraphics-%version

%build
%cmake_kde4

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

