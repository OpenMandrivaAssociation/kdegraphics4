%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1053190
%endif

Name: kdegraphics4
Summary: K Desktop Environment
Version: 4.3.85
Release: %mkrel 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegraphics-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegraphics-%version.tar.bz2
%endif
Patch0: kdegraphics-4.2.2-workaround-kolorpaintcrash.patch
Buildroot:     %_tmppath/%name-%version-%release-root
BuildRequires: jpeg-devel 
BuildRequires: png-devel 
BuildRequires: imlib2-devel 
BuildRequires: tiff-devel
BuildRequires: zlib-devel 
BuildRequires: bzip2-devel
BuildRequires: gettext texinfo
BuildRequires: kdelibs4-devel >= 2:4.2.98
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
BuildRequires: chmlib-devel
BuildRequires: libgs-devel
BuildRequires: libexiv-devel
BuildRequires: qimageblitz-devel
BuildRequires: ebook-tools-devel
BuildRequires: lcms-devel
BuildRequires: qca2-devel
BuildRequires: shared-desktop-ontologies-devel
Requires: %name-core
Requires: ksnapshot
Requires: kcolorchooser
Requires: okular
Requires: gwenview
Requires: kruler
Requires: kolourpaint
Requires: kgamma
Obsoletes: kde4-kfax < 2:3.93.0-0.714385.1
%if %mdkversion >= 200910
Obsoletes:     kdegraphics < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes:     kdegraphics3 < 1:3.5.10-5
Obsoletes:     kdegraphics3-common < 1:3.5.10-5
%endif

%description
Graphical tools for the K Desktop Environment.
kdegraphics is a collection of graphic oriented applications

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package   core
Summary:   Core files for kdegraphics
Group:     Graphical desktop/KDE	
Requires:  oxygen-icon-theme
Requires:  libgphoto-hotplug
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
%if %mdkversion >= 200910
Obsoletes: kdegraphics-common < 1:3.5.10-3
Obsoletes: kdegraphics-mrmlsearch < 1:3.5.10-3
Obsoletes: kdegraphics-kooka < 1:3.5.10-3
Obsoletes: kdegraphics-kview < 1:3.5.10-3
Obsoletes: kdegraphics-ksvg < 1:3.5.10-3
Obsoletes: kdegraphics-kuickshow < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes: kdegraphics3-common < 1:3.5.10-5
Obsoletes: kdegraphics3-mrmlsearch < 1:3.5.10-5
Obsoletes: kdegraphics3-kooka < 1:3.5.10-5
Obsoletes: kdegraphics3-kview < 1:3.5.10-5
Obsoletes: kdegraphics3-ksvg < 1:3.5.10-5
Obsoletes: kdegraphics3-kuickshow < 1:3.5.10-5
%endif

%description core
Common files for kdegraphics

%files core
%defattr(-,root,root)
%_kde_libdir/kde4/gsthumbnail.so
%_kde_libdir/kde4/svgpart.so
%_kde_appsdir/svgpart
%_kde_datadir/kde4/services/svgpart.desktop
%_kde_libdir/strigi/*
%_kde_libdir/kde4/ksaneplugin.so
%_kde_datadir/kde4/services/ksane_scan_service.desktop
%_kde_datadir/kde4/services/gsthumbnail.desktop
%_kde_iconsdir/hicolor/16x16/actions/black-white.png
%_kde_iconsdir/hicolor/16x16/actions/color.png
%_kde_iconsdir/hicolor/16x16/actions/gray-scale.png

#------------------------------------------------	

%define okularcore_major 1
%define libokularcore %mklibname okularcore %okularcore_major

%package -n %libokularcore
Summary:    KDE 4 core library
Group:      System/Libraries
Obsoletes:  %{_lib}kdegraphics40-okular < 2:3.93.0-0.714385.1
Obsoletes:  %{_lib}kghostviewlib1 < 2:3.95.2-0.734790.2
Obsoletes:  %{_lib}spectreOkular1 < 2:4.0.74-1

%description -n %libokularcore
KDE 4 core library.

%files -n %libokularcore
%defattr(-,root,root)
%_kde_libdir/libokularcore.so.%{okularcore_major}*

#-----------------------------------------------------------------------------

%package -n kgamma
Summary:    kgamma color profiling
Group:      Graphical desktop/KDE
Requires:   %name-core = %epoch:%version
Obsoletes:  kde4-kgamma < 2:4.0.68
Provides:   kde4-kgamma = %epoch:%version

%description -n kgamma
kgamma color profiling

%files -n kgamma
%defattr(-,root,root)
%_kde_datadir/kde4/services/kgamma*
%_kde_appsdir/kgamma
%_kde_libdir/kde4/*_kgamma.*
%_kde_docdir/HTML/*/kcontrol/kgamma
#-----------------------------------------------------------------------------

%package -n kamera
Summary: kamera ioslave
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kamera < 2:3.93.0-0.714385.1
Obsoletes: kde4-kamera < 2:4.0.68
Provides: kde4-kamera = %epoch:%version

%description -n kamera
kamera ioslave

%files -n kamera
%defattr(-,root,root)
%doc %_kde_docdir/HTML/en/kcontrol/kamera
%_kde_libdir/kde4/*_kamera.*
%_kde_datadir/kde4/services/camera*
%_kde_datadir/kde4/services/kamera*
%_kde_appsdir/solid/actions/solid_camera.desktop

#-----------------------------------------------------------------------------

%package -n okular
Summary: A universal document viewer
Group: Graphical desktop/KDE

Requires: %name-core = %epoch:%version

Obsoletes: %name-okular < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kpdf < 2:3.93.0-0.714385.1
Obsoletes: kdegraphics4-kdvi < 2:3.93.0-0.714385.1
Obsoletes: kde4-kghostview < 2:3.95.2-0.734790.2
Obsoletes: kde4-okular < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdegraphics-kdvi < 1:3.5.10-3
Obsoletes: kdegraphics-kghostview < 1:3.5.10-3
Obsoletes: kdegraphics-kpdf < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes: kdegraphics3-kdvi < 1:3.5.10-5
Obsoletes: kdegraphics3-kghostview < 1:3.5.10-5
Obsoletes: kdegraphics3-kpdf < 1:3.5.10-5
%endif
Suggests: poppler-data
Provides: kde4-okular = %epoch:%version
Conflicts: %name-devel < 2:3.95.2-0.734790.2

%description -n okular
Okular is a universal document viewer based on KPDF for KDE 4.

Okular combines the excellent functionalities of KPDF with the versatility
of supporting different kind of documents, like PDF, Postscript, DjVu, CHM,
and others.

The document format handlers page has a chart describing in more detail
the supported formats and the features supported in each of them.

%files -n okular
%defattr(-,root,root)
%_kde_bindir/okular
%_kde_bindir/xf86gammacfg
%_kde_libdir/kde4/okularGenerator_*
%_kde_libdir/kde4/okularpart.so
%_kde_libdir/kde4/kio_msits.so
%_kde_libdir/kde4/mobithumbnail.so
%_kde_libdir/kde4/rawthumbnail.so
%_kde_datadir/applications/kde4/okular*
%_kde_appsdir/okular
%_kde_datadir/config.kcfg/okular.kcfg
%_kde_datadir/config.kcfg/gssettings.kcfg
%_kde_datadir/config/okular.knsrc
%_kde_datadir/kde4/services/libokularGenerator_*
%_kde_datadir/kde4/services/okular*
%_kde_datadir/kde4/services/msits*
%_kde_datadir/kde4/services/mobithumbnail.desktop
%_kde_datadir/kde4/services/rawthumbnail.desktop
%_kde_datadir/kde4/servicetypes/okularGenerator.desktop
%_kde_docdir/HTML/en/okular
%_kde_iconsdir/*/*/*/okular.*

#------------------------------------------------	

%package -n libkdcraw-common
Summary: Non-library files for the kdcraw library
Group: System/Libraries
Obsoletes: kde4-libkdcraw < 0.2.0-0.744910.5

%description -n libkdcraw-common
Common files for the kdcraw library

%files -n libkdcraw-common
%defattr(-,root,root)
%{_kde_appsdir}/libkdcraw
%{_kde_iconsdir}/hicolor/*/apps/kdcraw.png

#------------------------------------------------	

%define	kdcraw_major 8
%define	libkdcraw %mklibname kdcraw %kdcraw_major

%package -n %{libkdcraw}
Summary: %{name} library
Group: System/Libraries
Requires: libkdcraw-common

%description -n %{libkdcraw}
%{name} library.

%files -n %{libkdcraw}
%defattr(0644, root, root, 0755)
%{_kde_libdir}/libkdcraw.so.%{kdcraw_major}*

#------------------------------------------------	

%package -n kipi-common
Summary: Non-library files for the kipi library
Group: System/Libraries
Obsoletes: libkipi < 1:0.3
Obsoletes: kde4-libkipi < 1:0.3

%description -n kipi-common
Common files for the kipi library

%files -n kipi-common
%defattr(-,root,root)
%{_kde_appsdir}/kipi
%{_kde_iconsdir}/*/*/*/kipi.*
%{_kde_servicetypes}/kipiplugin.desktop

#------------------------------------------------	

%define	kipi_major 7
%define	libkipi %mklibname kipi %kipi_major

%package -n %{libkipi}
Summary: %{name} library
Group: System/Libraries
Requires: kipi-common

%description -n %{libkipi}
%{name} library.

%files -n %{libkipi}
%defattr(0644, root, root, 0755)
%{_kde_libdir}/libkipi.so.%{kipi_major}*

#------------------------------------------------	

%define kexiv2_major 8
%define	libkexiv2 %mklibname kexiv2_ %kexiv2_major

%package -n %{libkexiv2}
Summary: %{name} library
Group: System/Libraries
Obsoletes: %mklibname kexiv 6

%description -n %{libkexiv2}
%{name} library.

%files -n %{libkexiv2}
%defattr(0644, root, root, 0755)
%{_kde_libdir}/libkexiv2.so.%{kexiv2_major}*
%_kde_appsdir/libkexiv2/data/topicset.iptc-subjectcode.xml

#------------------------------------------------	

%define gwenviewlib_major 4
%define libgwenviewlib %mklibname gwenviewlib %gwenviewlib_major

%package -n %libgwenviewlib
Summary:    KDE 4 core library
Group:      System/Libraries
Obsoletes:  %{_lib}gwenview1 < 1.4.2-9
# (Anssi 06/2008) Package had wrong major:
Obsoletes:  %{_lib}gwenviewlib1 < 2:4.0.82-3 

%description -n %libgwenviewlib
KDE 4 core library.

%files -n %libgwenviewlib
%defattr(-,root,root)
%_kde_libdir/libgwenviewlib.so.%{gwenviewlib_major}*

#------------------------------------------------

%define ksane_major 0
%define libksane %mklibname ksane %ksane_major

%package -n %libksane
Summary:    KDE 4 core library
Group:      System/Libraries

%description -n %libksane
KDE 4 core library.

%files -n %libksane
%defattr(-,root,root)
%_kde_libdir/libksane.so.%{ksane_major}*

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
%_kde_bindir/gwenview_importer
%_kde_libdir/kde4/gvpart.so
%_kde_appsdir/gvpart
%_kde_appsdir/gwenview
%_kde_datadir/kde4/services/gvpart.desktop
%_kde_datadir/kde4/services/ServiceMenus/slideshow.desktop
%_kde_datadir/applications/kde4/gwenview.desktop
%_kde_appsdir/solid/actions/gwenview_importer.desktop
%_kde_iconsdir/*/*/*/gwenview*
%_kde_docdir/*/*/gwenview

#-----------------------------------------------------------------------------

%package -n kcolorchooser
Summary:   KDE Color Chooser
Group:     Graphical desktop/KDE
Requires:  %name-core = %epoch:%version
Obsoletes: kdegraphics4-kcolorchooser < 2:3.93.0-0.714385.1
Obsoletes: kde4-kcolorchooser < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdegraphics-kcolorchooser < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes: kdegraphics3-kcolorchooser < 1:3.5.10-5
%endif
Provides:  kde4-kcolorchooser = %epoch:%version

%description -n kcolorchooser
KDE Color Chooser

%files -n kcolorchooser
%defattr(-,root,root)
%_kde_bindir/kcolorchooser
%_kde_datadir/applications/kde4/kcolorchooser.desktop
%_kde_iconsdir/*/*/*/kcolorchooser*

#-----------------------------------------------------------------------------

%define kolourpaint_lgpl_major 4
%define libkolourpaint_lgpl %mklibname kolourpaint_lgpl %kolourpaint_lgpl_major

%package -n %libkolourpaint_lgpl
Summary: KDE 4 core library
Group: System/Libraries
Obsoletes: %{_lib}kdegraphics40-kghostview < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kolourpaint4_lgpl4 < 2:3.94.0
Obsoletes: %{_lib}kolourpaint4_lgpl < 2:4.0.74-1
Obsoletes: %{_lib}kolourpaint_lgpl4 < 2:3.94.0

%description -n %libkolourpaint_lgpl
KDE 4 core library.

%files -n %libkolourpaint_lgpl
%defattr(-,root,root)
%_kde_libdir/libkolourpaint_lgpl.so.%{kolourpaint_lgpl_major}*

#-----------------------------------------------------------------------------

%package -n kolourpaint
Summary: A free, easy-to-use paint program for KDE
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kolourpaint < 2:3.93.0-0.714385.1
Obsoletes: kde4-kolourpaint < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdegraphics-kolourpaint < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes: kdegraphics3-kolourpaint < 1:3.5.10-5
%endif

Provides: kde4-kolourpaint = %epoch:%version

%description -n kolourpaint
KolourPaint is a free, easy-to-use paint program for KDE.

It aims to be conceptually simple to understand; providing a level of
functionality targeted towards the average user.  It's designed for daily
tasks like:

* Painting - drawing diagrams and "finger painting"
* Image Manipulation - editing screenshots and photos; applying effects
* Icon Editing - drawing clipart and logos with transparency

%files -n kolourpaint
%defattr(-,root,root)
%_kde_bindir/kolourpaint
%_kde_datadir/applications/kde4/kolourpaint.desktop
%_kde_appsdir/kolourpaint
%_kde_iconsdir/hicolor/*/apps/kolourpaint.*
%_kde_docdir/HTML/en/kolourpaint

#-----------------------------------------------------------------------------

%package -n kruler
Summary: KDE Screen Ruler
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

Obsoletes: %name-kruler < 2:3.93.0-0.714385.1
Obsoletes: kde4-kruler < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdegraphics-kruler < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes: kdegraphics3-kruler < 1:3.5.10-5
%endif
Provides: kde4-kruler = %epoch:%version

%description -n kruler
A screen ruler for the K Desktop Environment

%files -n kruler
%defattr(-,root,root)
%_kde_bindir/kruler
%_kde_datadir/applications/kde4/kruler.desktop
%_kde_appsdir/kruler
%_kde_iconsdir/*/*/*/kruler*
%_kde_docdir/*/*/kruler

#-----------------------------------------------------------------------------

%package -n ksnapshot
Summary: KDE Screenshot Utility
Group: Graphical desktop/KDE

Requires:  %name-core = %epoch:%version

Obsoletes: %name-ksnapshot < 2:3.93.0-0.714385.1
Obsoletes: kde4-ksnapshot < 2:4.0.68
%if %mdkversion >= 200910
Obsoletes: kdegraphics-ksnapshot < 1:3.5.10-3
%endif
%if %mdkversion >= 200100
Obsoletes: kdegraphics3-ksnapshot < 1:3.5.10-5
%endif
Provides:  kde4-ksnapshot = %epoch:%version

%description -n ksnapshot
KDE Screenshot Utility

%files -n ksnapshot
%defattr(-,root,root)
%_kde_bindir/kbackgroundsnapshot
%_kde_bindir/ksnapshot
%_kde_datadir/applications/kde4/ksnapshot.desktop
%_kde_iconsdir/*/*/*/ksnapshot*
%_kde_docdir/*/*/ksnapshot

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for kdegraphics
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:4.2.98
Requires: %libokularcore = %epoch:%version-%release
Requires: %libgwenviewlib = %epoch:%version-%release
Requires: %libksane  = %epoch:%version-%release
Requires: %libkipi  = %epoch:%version-%release
Requires: %libkdcraw  = %epoch:%version-%release
Requires: %libkexiv2  = %epoch:%version-%release
Obsoletes: %{_lib}kdegraphics40-ksvg-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kview-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kooka-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kpovmodeler-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-common-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-kghostview-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kdegraphics40-okular-devel < 2:3.93.0-0.714385.1
Obsoletes: %{_lib}kexiv-devel
Obsoletes: %{_lib}kdcraw-devel
Obsoletes: %{_lib}kipi-devel
Conflicts: kde4-okular < 2:3.95.2-0.734790.2
Provides: libkexiv-devel = %epoch:%version-%release
Provides: libkdcraw-devel = %epoch:%version-%release
Provides: libkipi-devel = %epoch:%version-%release

%description  devel
This package contains header files needed if you wish to build applications
based on kdegraphics.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_libdir/pkgconfig/*.pc
%_kde_includedir/*
%_kde_appsdir/cmake/*/*
%_kde_datadir/dbus-1/interfaces/org.kde.ksnapshot.xml

#----------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdegraphics-%version%kde_snapshot
%else
%setup -q -n kdegraphics-%version
%endif
%patch0 -p1

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

