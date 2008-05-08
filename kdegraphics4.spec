Name: kdegraphics4
Summary: K Desktop Environment
Version: 4.0.72
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
BuildRequires: libspectre-devel
BuildRequires: fontconfig-devel
BuildRequires: libpoppler-qt4-devel >= 0.8.0
BuildRequires: mesaglut-devel
BuildRequires: djvulibre-devel
BuildRequires: libchm-devel
BuildRequires: libgs-devel
BuildRequires: libexiv-devel
BuildRequires: qimageblitz-devel
BuildRequires: kde4-libkipi-devel >= 0.2.0
BuildRequires: ebook-tools-devel
Requires: %name-core
Requires: ksnapshot
Obsoletes: kde4-kfax < 2:3.93.0-0.714385.1
Requires: kcolorchooser
Requires: okular
Requires: gwenview
Requires: kruler
Requires: kolourpaint
Requires: kgamma

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

#-----------------------------------------------------------------------------

%package -n kgamma
Summary: kgamma color profiling
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: kde4-kgamma < 2:4.0.68
Provides: kde4-kgamma = %epoch:%version

%description -n kgamma
kgamma color profiling

%files -n kgamma
%defattr(-,root,root)
%_kde_datadir/kde4/services/kgamma*
%_kde_appsdir/kgamma
%_kde_iconsdir/*/*/*/kgamma*
%_kde_libdir/kde4/*_kgamma.*

#-----------------------------------------------------------------------------

%package -n kamera
Summary: kamera ioslave
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kamera < 2:3.93.0-0.714385.1
Obsoletes: kde4-kamera < 2:4.0.68
Provides: kde4-kamera = %epoch:%version

%description -n kamera
Dialog KDE base widgets

%files -n kamera
%defattr(-,root,root)
%dir %_kde_docdir/HTML/en/kamera
%doc %_kde_docdir/HTML/en/kamera/*
%_kde_libdir/kde4/*_kamera.*
%_kde_datadir/kde4/services/camera*
%_kde_datadir/kde4/services/kamera*

#-----------------------------------------------------------------------------

%package -n okular
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-okular < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kpdf < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kdvi < 2:3.93.0-0.714385.1
Obsoletes: kde4-kghostview < 2:3.95.2-0.734790.2
Conflicts: %name-devel < 2:3.95.2-0.734790.2
Obsoletes: kde4-okular < 2:4.0.68
Provides: kde4-okular = %epoch:%version

%description -n okular
Dialog KDE base widgets

%files -n okular
%defattr(-,root,root)
%_kde_bindir/okular
%_kde_bindir/xf86gammacfg
%_kde_libdir/kde4/okularGenerator_*
%_kde_libdir/kde4/okularpart.so
%_kde_libdir/kde4/kio_msits.so
%_kde_datadir/applications/kde4/okular*
%_kde_appsdir/okular
%_kde_datadir/config.kcfg/okular.kcfg
%_kde_datadir/config.kcfg/gssettings.kcfg
%_kde_datadir/config/okular.knsrc
%_kde_datadir/kde4/services/libokularGenerator_*
%_kde_datadir/kde4/services/okular*
%_kde_datadir/kde4/services/msits*
%_kde_datadir/kde4/servicetypes/okularGenerator.desktop
%_kde_docdir/HTML/en/okular

#------------------------------------------------	

%define libgwenviewlib %mklibname gwenviewlib 1

%package -n %libgwenviewlib
Summary:    KDE 4 core library
Group:      System/Libraries
Obsoletes:  %{lib}gwenview1 <= 1.4.2-8 

%description -n %libgwenviewlib
KDE 4 core library.

%post -n %libgwenviewlib -p /sbin/ldconfig
%postun -n %libgwenviewlib -p /sbin/ldconfig

%files -n %libgwenviewlib
%defattr(-,root,root)
%_kde_libdir/libgwenviewlib.so.*

#-----------------------------------------------------------------------------

%package -n gwenview
Summary:    Fast and easy to use image viewer for KDE
Group:      Graphical desktop/KDE
Requires:   %name-core = %epoch:%version
Obsoletes:  %name-gwenview < 2:3.93.0-0.714385.1
Obsoletes:  kde4-gwenview < 2:4.0.68
Provides:   kde4-gwenview = %epoch:%version

%description -n gwenview
Gwenview is a fast and easy to use image viewer/browser for KDE.
All common image formats are supported, such as PNG(including transparency),
JPEG(including EXIF tags and lossless transformations), GIF, XCF (Gimp
image format), BMP, XPM and others. Standard features include slideshow,
fullscreen view, image thumbnails, drag'n'drop, image zoom, full network
transparency using the KIO framework, including basic file operations and
browsing in compressed archives, non-blocking GUI with adjustable views.
Gwenview also provides image and directory KParts components for use e.g. in
Konqueror. Additional features, such as image renaming, comparing,
converting, and batch processing, HTML gallery and others are provided by the
KIPI image framework.

%files -n gwenview
%defattr(-,root,root)
%_kde_bindir/gwenview
%_kde_libdir/kde4/gvpart.so
%_kde_appsdir/gvpart/gvpart.rc
%_kde_appsdir/gwenview
%_kde_datadir/kde4/services/gvpart.desktop
%_kde_datadir/applications/kde4/gwenview.desktop
%_kde_iconsdir/*/*/*/gwenview*
%_kde_docdir/*/*/gwenview

#-----------------------------------------------------------------------------

%package -n kcolorchooser
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: kdegraphics4-kcolorchooser < 2:3.93.0-0.714385.1
Obsoletes: kde4-kcolorchooser < 2:4.0.68
Provides: kde4-kcolorchooser = %epoch:%version

%description -n kcolorchooser
Dialog KDE base widgets

%files -n kcolorchooser
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

%package -n kolourpaint
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kolourpaint < 2:3.93.0-0.714385.1
Obsoletes: kde4-kolourpaint < 2:4.0.68
Provides: kde4-kolourpaint = %epoch:%version

%description -n kolourpaint
Dialog KDE base widgets

%files -n kolourpaint
%defattr(-,root,root)
%_kde_bindir/kolourpaint4
%_kde_datadir/applications/kde4/kolourpaint4.desktop
%_kde_appsdir/kolourpaint4
%_kde_iconsdir/hicolor/*/apps/kolourpaint4.*
%_kde_docdir/HTML/en/kolourpaint4

#-----------------------------------------------------------------------------

%package -n kruler
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kruler < 2:3.93.0-0.714385.1
Obsoletes: kde4-kruler < 2:4.0.68
Provides: kde4-kruler = %epoch:%version

%description -n kruler
Dialog KDE base widgets

%files -n kruler
%defattr(-,root,root)
%_kde_bindir/kruler
%_kde_datadir/applications/kde4/kruler.desktop
%_kde_appsdir/kruler
%_kde_iconsdir/*/*/*/kruler*
%_kde_docdir/*/*/kruler

#-----------------------------------------------------------------------------

%package -n ksnapshot
Summary: Dialog KDE base widgets
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-ksnapshot < 2:3.93.0-0.714385.1
Obsoletes: kde4-ksnapshot < 2:4.0.68
Provides: kde4-ksnapshot = %epoch:%version

%description -n ksnapshot
Dialog KDE base widgets

%files -n ksnapshot
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
Obsoletes: %{_lib}kdegraphics40-ksvg-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kview-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kooka-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kpovmodeler-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-common-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kghostview-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-okular-devel < 2:3.93.0-0.714385.1
Conflicts: kde4-okular < 2:3.95.2-0.734790.2

%description  devel
This package contains header files needed if you wish to build applications
based on kdegraphics.

%files devel
%defattr(-,root,root)
%_kde_libdir/libgwenviewlib.so
%_kde_libdir/libkolourpaint4_lgpl.so
%_kde_libdir/libokularcore.so
%_kde_prefix/include/*
%_kde_appsdir/cmake/*/*

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

