%define _requires_exceptions devel\(linux-gate\)

%define launchers /etc/dynamic/launchers/scanner

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070418

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig kdegraphics4
%define lib_major 0
%define lib_name %mklibname kdegraphics4 %lib_major

Name:		kdegraphics4
Version:    	3.80.3
Release:    	%mkrel  0.%branch_date.3
Epoch:		1
Group:		Graphical desktop/KDE
Summary:	K Desktop Environment - Graphics
License:	GPL
URL:		http://www.kde.org/
Packager: Mandriva Linux KDE Team <kde@mandriva.com>
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegraphics-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegraphics-%version.tar.bz2
%endif
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: jpeg-devel 
BuildRequires: png-devel 
BuildRequires: libimlib-devel libtiff-devel
BuildRequires: zlib-devel 
BuildRequires: bzip2-devel
BuildRequires: gettext texinfo
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires: X11-devel 
BuildRequires: freetype2-devel
BuildRequires: openssl-devel 
BuildRequires: libsane-devel 
BuildRequires: OpenEXR-devel
BuildRequires: libtiff-progs
BuildRequires: gphoto2-devel
BuildRequires: fontconfig-devel
#Disable it for the moment okular use svn poppler version
#BuildRequires: libpoppler-qt4-devel
# necessary for displaying info into konqueror pdfinfo
BuildRequires:	xpdf
BuildRequires: 	mesaglut-devel
BuildRequires:	libdjvulibre-devel
BuildRequires:	chmlib-devel

Requires: %name-ksnapshot = %epoch:%version-%release
Requires: %name-common = %epoch:%version-%release
Requires: %name-kuickshow = %epoch:%version-%release
Requires: %name-kdvi = %epoch:%version-%release
Requires: %name-kfax = %epoch:%version-%release
Requires: %name-kghostview = %epoch:%version-%release   
Requires: %name-kiconedit = %epoch:%version-%release   
Requires: %name-kcolorchooser = %epoch:%version-%release   
Requires: %name-kcoloredit = %epoch:%version-%release   
Requires: %name-kpovmodeler = %epoch:%version-%release    
Requires: %name-kruler = %epoch:%version-%release    
Requires: %name-mrmlsearch = %epoch:%version-%release    
Requires: %name-kview = %epoch:%version-%release    
Requires: %name-okular = %epoch:%version-%release

%description
Graphical tools for the K Desktop Environment.
kdegraphics is a collection of graphic oriented applications:

	- kamera: digital camera io_slave for Konqueror. Together gPhoto this 
			allows you to access your camera's picture with the URL kamera:/
	- kcoloredit: contains two programs: a color value editor and also 
			a color picker
	- kdvi: program (and embeddable KPart) to display *.DVI files from TeX
	- kfax: a program to display raw and tiffed fax images (g3, g3-2d, g4)
	- kfaxview: an embeddable KPart to display tiffed fax images
	- kfile-plugins: provide meta information for graphic files
	- kghostview: program (and embeddable KPart) to display *.PDF and *.PS
	- kiconedit: an icon editor
	- kooka: a raster image scan program, based on SANE and libkscan
	- kruler: a ruler in inch, centimeter and pixel to check distances 
	 		  on the screen
	- ksnapshot: make snapshots of the screen contents
	- kuickshow: fast and comfortable imageviewer
	- kview: picture viewer, provided as standalone program and embeddable KPart
	- kviewshell: generic framework for viewer applications

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package common
Summary:	Common files for kdegraphics
Group:		Graphical desktop/KDE	
Requires:   kdelibs4
Requires:   libgphoto-hotplug


%description common
Common files for kdegraphics


%files common
%defattr(-,root,root)
%_libdir/kde4/kio_kamera.*
%_libdir/kde4/kcm_kamera.*
%_datadir/kde4/services/kamera.desktop
%_iconsdir/*/*/devices/*
%_iconsdir/*/*/apps/camera*
%_datadir/kde4/services/kfile_*
%_datadir/kde4/services/scanservice.desktop
%_datadir/kde4/services/camera.protocol
%_iconsdir/crystalsvg/22x22/places/camera.png
%_iconsdir/crystalsvg/32x32/places/camera.png

%dir %_docdir/HTML/en/kgamma/
%doc %_docdir/HTML/en/kgamma/*.bz2
%doc %_docdir/HTML/en/kgamma/*.docbook
%dir %_docdir/HTML/en/kamera/
%doc %_docdir/HTML/en/kamera/*.bz2
%doc %_docdir/HTML/en/kamera/*.docbook

%_iconsdir/crystalsvg/16x16/actions/camera_test.png
%_iconsdir/crystalsvg/16x16/actions/palette_color.png
%_iconsdir/crystalsvg/16x16/actions/palette_gray.png
%_iconsdir/crystalsvg/16x16/actions/palette_halftone.png
%_iconsdir/crystalsvg/16x16/actions/palette_lineart.png

%_datadir/kde4/services/kfilewrite_jpeg.desktop

%_datadir/kde4/services/msits.protocol

#----------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Libraries files for kdegraphics
Group:		Graphical desktop/KDE

%description -n %lib_name-common
Libraries files for kdegraphics

%post -n %lib_name-common -p /sbin/ldconfig
%postun -n %lib_name-common -p /sbin/ldconfig

%files -n %lib_name-common
%defattr(-,root,root)
%_datadir/dbus-1/interfaces/org.kde.kpovmodeler.xml
%_datadir/dbus-1/interfaces/org.kde.ksnapshot.xml
%_datadir/dbus-1/interfaces/org.kde.ligature.MultiPage.xml

%_libdir/strigi/strigiea_jpeg.so
%_libdir/strigi/strigiea_ps.so
%_libdir/strigi/strigita_dvi.so
%_libdir/strigi/strigita_ico.so
%_libdir/kde4/kfilewrite_jpeg.so
%_libdir/kde4/kio_msits.so

#----------------------------------------------------------------------

%package kolourpaint
Summary:    Free and easy-to-use paint program for KDE
Group:      Graphical desktop/KDE

%description kolourpaint
KolourPaint is a free, easy-to-use paint program for KDE.
It aims to be conceptually simple to understand; providing a level of
functionality targeted towards the average user. It's designed for daily
tasks like:
  Painting - drawing diagrams and "finger painting" 
  Image Manipulation - editing screenshots and photos; applying effects 
  Icon Editing - drawing clipart and logos with transparency 
It's not an unusable and monolithic program where simple tasks like drawing 
lines become near impossible. Nor is it so simple that it lacks essential 
features like Undo/Redo. KolourPaint is opensource software written in C++
using the Qt and KDE libraries

%post kolourpaint
%{update_desktop_database}
%update_icon_cache hicolor

%postun kolourpaint
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kolourpaint
%defattr(-,root,root)
%_bindir/kolourpaint
%_datadir/applications/kde4/kolourpaint.desktop
%dir %_datadir/apps/kolourpaint
%_datadir/apps/kolourpaint/*
%dir %_docdir/HTML/en/kolourpaint/
%doc %_docdir/HTML/en/kolourpaint/*.png
%doc %_docdir/HTML/en/kolourpaint/*.docbook
%doc %_docdir/HTML/en/kolourpaint/*.bz2


#----------------------------------------------------------------------

%package mrmlsearch
Summary:	MRML is short for Multimedia Retrieval Markup Language.
Group:		Graphical desktop/KDE
Provides: mrmlsearch4

%description mrmlsearch
MRML is short for Multimedia Retrieval Markup Language,
which defines a protocol for querying a server for images
based on their content. See http://www.mrml.net about MRML
and the GNU Image Finding Tool (GIFT), an MRML server.

This package consists of an mrml kio-slave that handles
the communication with the MRML server and a KPart to
be embedded e.g. into Konqueror.

With those, you can search for images by giving an example
image and let the server look up similar images. The query
result can be refined by giving positive/negative feedback.

%post mrmlsearch
%{update_desktop_database}

%postun mrmlsearch
%{clean_desktop_database}

%files mrmlsearch
%defattr(-,root,root)

#----------------------------------------------------------------------

%package -n %lib_name-common-devel
Summary:	Include files for kdegraphics
Group:		Development/KDE and Qt
Requires:   %{lib_name}-common = %epoch:%version-%release
Provides:	%name-devel = %epoch:%version-%release
Provides:	%lib_name-devel = %epoch:%version-%release
Provides:	%{lib_name_orig}-common-devel = %epoch:%version-%release

%description -n %lib_name-common-devel
This package contains include files needed to build applications 
based on kdegraphic.

%post -n %lib_name-common-devel -p /sbin/ldconfig
%postun -n %lib_name-common-devel -p /sbin/ldconfig

%files -n %lib_name-common-devel
%defattr(-,root,root)
%_includedir/*.h

#----------------------------------------------------------------------


%package kooka
Summary:    Kooka is a raster image scan program for the KDE system.
Group:      Graphical desktop/KDE
Requires:	kdelibs4
Requires:	gocr, sane
Requires:	%lib_name-kooka = %epoch:%version-%release
Provides:	kooka4
#Laurent readd it
#Provides:	scanner-gui

%description kooka
This package contains a raster image scan program, based on SANE and libkscan.

%files kooka
%defattr(-,root,root)
%config(noreplace) %launchers/%name.desktop
#----------------------------------------------------------------------

%package kdvi
Summary:    Kdvi is a DVI Viewer.
Group:      Graphical desktop/KDE
Provides:	kdvi
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	%name-common = %epoch:%version-%release
Requires:	tetex

%description kdvi
Kdvi package

%post kdvi
%{update_desktop_database}
%update_icon_cache hicolor

%postun kdvi
%{clean_desktop_database}
%clean_icon_cache hicolor


%files kdvi
%defattr(-,root,root)
%_datadir/icons/hicolor/16x16/apps/kdvi.png
%_datadir/icons/hicolor/22x22/apps/kdvi.png
%_datadir/icons/hicolor/32x32/apps/kdvi.png
%_datadir/icons/hicolor/48x48/apps/kdvi.png
%_datadir/icons/hicolor/scalable/apps/kdvi.svgz
%_datadir/config.kcfg/kdvi.kcfg
%_datadir/apps/kdvi_part.rc
#----------------------------------------------------------------------

%package kfax
Summary:    Kfax package
Group:      Graphical desktop/KDE
Provides:	kfax4
Requires:   %lib_name-common = %epoch:%version-%release
Requires:   %name-kview 

%description kfax
A program to display raw and tiffed fax images (g3, g3-2d, g4).

%post kfax
%{update_desktop_database}
%update_icon_cache hicolor

%postun kfax
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kfax
%defattr(-,root,root)
%_datadir/config.kcfg/djvumultipage.kcfg
%_datadir/kde4/services/djvumultipage.desktop
%_bindir/kfax        
%_datadir/applications/kde4/kfax.desktop           
%dir %_datadir/apps/kfax/
%_datadir/apps/kfax/*
%_iconsdir/*/*/*/kfax*
# This is a module, not library. We will not change buildsystem
# on kde 3 and the install should be fixed on kde4

#----------------------------------------------------------------------

%package kruler
Summary:    Kruler package
Group:      Graphical desktop/KDE
Provides:	kruler4

%description kruler
A ruler in inch, centimeter and pixel to check distances on the screen

%post kruler
%update_icon_cache hicolor

%postun kruler
%clean_icon_cache hicolor

%files kruler
%defattr(-,root,root)
%_bindir/kruler  
%_iconsdir/*/*/*/kruler*
%_datadir/applications/kde4/kruler.desktop           
%dir %_datadir/apps/kruler/
%_datadir/apps/kruler/*
%dir %_docdir/HTML/en/kruler/
%doc %_docdir/HTML/en/kruler/*.bz2
%doc %_docdir/HTML/en/kruler/*.docbook

#----------------------------------------------------------------------

%package kghostview
Summary:    Kghostview package
Group:      Graphical desktop/KDE
Provides:	kghostview4
Requires:	ghostscript, ghostscript-module-X

%description kghostview
A program (and embeddable KPart) to display *.PDF and *.PS

%post kghostview
%{update_desktop_database}
%update_icon_cache hicolor

%postun kghostview
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kghostview
%defattr(-,root,root)
%_iconsdir/*/*/*/kghostview.*
%_datadir/apps/kconf_update/kghostview.upd
%dir %_datadir/config.kcfg/
%_datadir/config.kcfg/kghostview.kcfg
%_bindir/kghostview  
%_datadir/applications/kde4/kghostview.desktop   
%_datadir/kde4/services/kghostview_part.desktop
%dir %_datadir/apps/kghostview/
%_libdir/kde4/gsthumbnail.*
%_datadir/kde4/services/gsthumbnail.desktop
%_datadir/apps/kghostview/kgv_part.rc
%_datadir/apps/kghostview/pdf_sec.ps
%_datadir/apps/kconf_update/update-to-xt-names.pl
%_datadir/apps/kghostview/kghostviewui.rc
%dir %_docdir/HTML/en/kghostview/
%doc %_docdir/HTML/en/kghostview/*.bz2
%doc %_docdir/HTML/en/kghostview/*.docbook
#----------------------------------------------------------------------

%package -n %lib_name-kghostview
Summary:    Library for kghostview 
Group:      Development/KDE and Qt
Provides:	kghostview4-lib

%description -n %lib_name-kghostview
Library for kghostview

%post -n  %lib_name-kghostview -p /sbin/ldconfig
%postun -n  %lib_name-kghostview -p /sbin/ldconfig

%files -n %lib_name-kghostview
%defattr(-,root,root)
%_libdir/libkghostviewlib.so.*
%_libdir/kde4/libkghostviewpart.so

#----------------------------------------------------------------------

%package -n %lib_name-kghostview-devel
Summary:    Devel for kghostview 
Group:      Development/KDE and Qt
Requires:	%lib_name-kghostview = %epoch:%version-%release

%description -n %lib_name-kghostview-devel
Library for kghostview

%files -n %lib_name-kghostview-devel
%defattr(-,root,root)
%_libdir/libkghostviewlib.so

#----------------------------------------------------------------------

%package ksnapshot
Summary:    Ksnaphot package
Group:      Graphical desktop/KDE
Provides:	ksnapshot4

%description ksnapshot
KSnapshot is intended to be an easy to use program for making
screenshots. I can be bound to the Print Screen key, as the program
takes a snapshot of the desktop on startup (before it displays it
window), so it's a simple way of of making snapshots.

%post ksnapshot
%update_icon_cache hicolor

%postun ksnapshot
%clean_icon_cache hicolor


%files ksnapshot
%defattr(-,root,root)
%_bindir/ksnapshot  
%_datadir/applications/kde4/ksnapshot.desktop
%_iconsdir/*/*/*/ksnapshot*
%dir %_docdir/HTML/en/ksnapshot/
%doc %_docdir/HTML/en/ksnapshot/*.bz2
%doc %_docdir/HTML/en/ksnapshot/*.docbook
%doc %_docdir/HTML/en/ksnapshot/*.png

#----------------------------------------------------------------------

%package okular
Summary:    Okular package
Group:      Graphical desktop/KDE
Provides:       okular
Requires:       %lib_name-okular = %epoch:%version-%release

%description okular
Okular

%post okular
%{update_desktop_database}
%update_icon_cache hicolor

%postun okular
%{clean_desktop_database}
%clean_icon_cache hicolor

%files okular
%defattr(-,root,root)
%_bindir/okular
%_datadir/kde4/services/okularChm.desktop
%_datadir/kde4/services/okularComicbook.desktop
%_datadir/kde4/services/okularDjvu.desktop
%_datadir/kde4/services/okularDvi.desktop
%_datadir/kde4/services/okularFb.desktop
%_datadir/kde4/services/okularKimgio.desktop
%_datadir/kde4/services/okularOoo.desktop
%_datadir/kde4/services/okularPlucker.desktop
%_datadir/kde4/services/okularTiff.desktop
%_datadir/kde4/services/okularXps.desktop
%_datadir/kde4/services/okular_part.desktop

%_datadir/kde4/servicetypes/okularGenerator.desktop
%_datadir/applications/kde4/okular.desktop
%_datadir/applications/kde4/okularApplication_*.desktop

%_datadir/apps/okular/pics/*.png
%_datadir/apps/okular/shell.rc
%_datadir/apps/okular/tools.xml
%_datadir/apps/okularpart/part.rc
%_datadir/config.kcfg/okular.kcfg
%doc %_docdir/HTML/en/okular/*.png
%doc %_docdir/HTML/en/okular/*.bz2
%doc %_docdir/HTML/en/okular/*.docbook

%_iconsdir/hicolor/128x128/apps/okular.png
%_iconsdir/hicolor/16x16/apps/okular.png
%_iconsdir/hicolor/22x22/apps/okular.png
%_iconsdir/hicolor/32x32/apps/okular.png
%_iconsdir/hicolor/48x48/apps/okular.png
%_iconsdir/hicolor/64x64/apps/okular.png
%_iconsdir/hicolor/scalable/apps/okular.svgz

%_datadir/kde4/services/libokularGenerator_*.desktop

%package -n %lib_name-okular
Summary:    Library for okular package
Group:      Graphical desktop/KDE

%description -n %lib_name-okular
Library for okular.

%post -n %lib_name-okular -p /sbin/ldconfig
%postun -n %lib_name-okular -p /sbin/ldconfig

%files -n %lib_name-okular
%defattr(-,root,root)
%_libdir/kde4/libokularGenerator_chmlib.so
%_libdir/kde4/libokularGenerator_comicbook.so
%_libdir/kde4/libokularGenerator_djvu.so
%_libdir/kde4/libokularGenerator_dvi.so
%_libdir/kde4/libokularGenerator_fb.so
%_libdir/kde4/libokularGenerator_kimgio.so
%_libdir/kde4/libokularGenerator_ooo.so
%_libdir/kde4/libokularGenerator_plucker.so
%_libdir/kde4/libokularGenerator_tiff.so
%_libdir/kde4/libokularGenerator_xps.so
%_libdir/kde4/libokularpart.so

%package -n %lib_name-okular-devel
Summary:    Devel for okular package
Group:      Development/KDE and Qt
Requires:       %lib_name-okular = %epoch:%version-%release

%description -n %lib_name-okular-devel
Devel for okular.

%files -n %lib_name-okular-devel
%defattr(-,root,root)
%dir %_includedir/okular/core/
%_includedir/okular/core/*.h
%dir %_includedir/okular/interfaces/
%_includedir/okular/interfaces/*.h

%_libdir/libokularcore.so
#----------------------------------------------------------------------

%package kpovmodeler
Summary:    Kpovmodeler package
Group:      Graphical desktop/KDE
Provides:	kpovmodeler4
Requires:	%lib_name-kpovmodeler = %epoch:%version-%release

%description kpovmodeler
Program to enter scenes for the 3D rendering engine PovRay.

%post kpovmodeler
%{update_desktop_database}
%update_icon_cache hicolor

%postun kpovmodeler
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kpovmodeler
%defattr(-,root,root)
%_bindir/kpovmodeler  
%_libdir/kde4/libkpovmodelerpart.*
%_iconsdir/*/*/*/kpovmodeler*
%dir %_datadir/apps/kpovmodeler/
%_datadir/apps/kpovmodeler/*
%_datadir/applications/kde4/kpovmodeler.desktop
%dir %_docdir/HTML/en/kpovmodeler/
%doc %_docdir/HTML/en/kpovmodeler/*.bz2
%doc %_docdir/HTML/en/kpovmodeler/*.docbook
%doc %_docdir/HTML/en/kpovmodeler/*.png

#----------------------------------------------------------------------

%package -n %lib_name-kpovmodeler
Summary:    Library for kpovmodeler package
Group:      Graphical desktop/KDE

%description -n %lib_name-kpovmodeler
Library for kpovmodeler.

%post -n %lib_name-kpovmodeler -p /sbin/ldconfig
%postun -n %lib_name-kpovmodeler -p /sbin/ldconfig

%files -n %lib_name-kpovmodeler
%defattr(-,root,root)
%_libdir/liblkpovmodeler.so.*
#----------------------------------------------------------------------

%package -n %lib_name-kpovmodeler-devel
Summary:    Devel for kpovmodeler package
Group:      Development/KDE and Qt
Requires:	%lib_name-kpovmodeler = %epoch:%version-%release

%description -n %lib_name-kpovmodeler-devel
Devel for kpovmodeler.

%files -n %lib_name-kpovmodeler-devel
%defattr(-,root,root)
%_libdir/liblkpovmodeler.so
#----------------------------------------------------------------------

%package kiconedit
Summary:    Kiconedit package
Group:      Graphical desktop/KDE
Provides:	kiconedit4

%description kiconedit
An icon editor.

%post kiconedit
%{update_desktop_database}
%update_icon_cache hicolor

%postun kiconedit
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kiconedit
%defattr(-,root,root)
%_datadir/applications/kde4/kiconedit.desktop    
%dir %_datadir/apps/kiconedit
%_datadir/apps/kiconedit/*
%_iconsdir/*/*/*/kiconedit*
%_bindir/kiconedit   
%dir %_docdir/HTML/en/kiconedit/
%doc %_docdir/HTML/en/kiconedit/*.bz2
%doc %_docdir/HTML/en/kiconedit/*.docbook
%doc %_docdir/HTML/en/kiconedit/*.png

#----------------------------------------------------------------------

%package kview
Summary:    Kview package
Group:      Graphical desktop/KDE
Provides:	kview4
Requires:	%lib_name-kview = %epoch:%version-%release

%description kview
Kview is a  picture viewer, provided as standalone program and embeddable KPart

%post kview
%{update_desktop_database}
%update_icon_cache hicolor
%update_icon_cache crystalsvg

%postun kview
%{clean_desktop_database}
%clean_icon_cache hicolor
%clean_icon_cache crystalsvg

%files kview
%defattr(-,root,root)
%_datadir/apps/kviewerpart/icons/hicolor/16x16/actions/measuretool.png
%_datadir/apps/kviewerpart/icons/hicolor/16x16/actions/movetool.png
%_datadir/apps/kviewerpart/icons/hicolor/16x16/actions/selectiontool.png
%_datadir/apps/kviewerpart/icons/hicolor/22x22/actions/measuretool.png
%_datadir/apps/kviewerpart/icons/hicolor/22x22/actions/movetool.png
%_datadir/apps/kviewerpart/icons/hicolor/22x22/actions/selectiontool.png
%_datadir/apps/kviewerpart/icons/hicolor/32x32/actions/movetool.png
%_datadir/apps/kviewerpart/icons/hicolor/48x48/actions/movetool.png
%_datadir/apps/psMultipage.rc
%_datadir/apps/ligature/ligature.rc
%_datadir/apps/ligature/tips
%_datadir/apps/ligaturepart/ligaturepart.rc
%_datadir/config.kcfg/ligature.kcfg
%_datadir/icons/crystalsvg/16x16/apps/kviewshell.png
%_datadir/icons/crystalsvg/32x32/apps/kviewshell.png
%_datadir/icons/crystalsvg/48x48/apps/kviewshell.png
%_datadir/kde4/services/kdvimultipage.desktop
%_datadir/kde4/services/kfaxmultipage.desktop
%_datadir/kde4/servicetypes/ligaturePluginGUI.desktop
%_datadir/kde4/services/kvs_djvu_part.desktop
%_datadir/kde4/services/kvs_dvi_part.desktop
%_datadir/kde4/services/kvs_fax_part.desktop
%_datadir/kde4/services/kvs_ps_part.desktop
%_datadir/kde4/services/psMultipage.desktop
%_bindir/ligature
%_datadir/applications/kde4/ligature.desktop
%_datadir/apps/djvumultipage.rc
#----------------------------------------------------------------------

%package -n %lib_name-kview
Summary:    Librarie for Kview package
Group:      Graphical desktop/KDE

%description -n %lib_name-kview
Libraries for Kview package

%post -n %lib_name-kview -p /sbin/ldconfig
%postun -n %lib_name-kview -p /sbin/ldconfig

%files -n %lib_name-kview
%defattr(-,root,root)
%_libdir/kde4/ligaturePlugin_DJVU.so
%_libdir/kde4/ligaturePlugin_DVI.so
%_libdir/kde4/ligaturePlugin_PS.so
%_libdir/kde4/ligaturePlugin_TIFF.so
%_libdir/kde4/ligaturepart.so
%_libdir/libligaturePluginGUI.so.*
%_libdir/libligaturecore.so.*
%_libdir/libdjvu.so.*
#----------------------------------------------------------------------

%package -n %lib_name-kview-devel
Summary:    Devel file for Kview package
Group:      Development/KDE and Qt
Requires:	%lib_name-kview = %epoch:%version-%release
Provides:	%{lib_name_orig}-kview-devel = %epoch:%version-%release

%description -n %lib_name-kview-devel
Devel files for Kview package

%files -n %lib_name-kview-devel
%defattr(-,root,root)
%_libdir/libligaturePluginGUI.so
%_libdir/libligaturecore.so
%_libdir/libdjvu.so
#----------------------------------------------------------------------

%package kuickshow
Summary:    Kuickshow package
Group:      Graphical desktop/KDE
Provides:	kuickshow4
Obsoletes:	%lib_name-kuickshow

%description kuickshow
A fast and comfortable imageviewer.

%post kuickshow

%{update_desktop_database}
%update_icon_cache hicolor

%postun kuickshow

%{clean_desktop_database}
%clean_icon_cache hicolor


%files kuickshow
%defattr(-,root,root)
%_bindir/kuickshow  
%_iconsdir/*/*/*/kuickshow*
%_datadir/applications/kde4/kuickshow.desktop
%dir %_datadir/apps/kuickshow/
%_datadir/apps/kuickshow/*
%_libdir/libkdeinit_kuickshow.*
%dir %_docdir/HTML/en/kuickshow/
%doc %_docdir/HTML/en/kuickshow/*.bz2
%doc %_docdir/HTML/en/kuickshow/*.docbook
%doc %_docdir/HTML/en/kuickshow/*.png
#----------------------------------------------------------------------

%package kcoloredit
Summary:    kcoloredit package
Group:      Graphical desktop/KDE
Provides:	kcoloredit4

%description kcoloredit
A fast and comfortable imageviewer.

%post kcoloredit

%{update_desktop_database}
%update_icon_cache hicolor

%postun kcoloredit
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kcoloredit
%defattr(-,root,root)
%dir %_datadir/apps/kcoloredit
%_datadir/applications/kde4/kcoloredit.desktop     
%_datadir/apps/kcoloredit/*
%_bindir/kcoloredit     
%_iconsdir/*/*/*/kcoloredit*
%dir %_docdir/HTML/en/kcoloredit/
%doc %_docdir/HTML/en/kcoloredit/*.bz2
%doc %_docdir/HTML/en/kcoloredit/*.docbook

#----------------------------------------------------------------------

%package kcolorchooser
Summary:    kcolorchooser package
Group:      Graphical desktop/KDE
Provides:	kcolorchooser4

%description kcolorchooser
A fast and comfortable imageviewer.

%post kcolorchooser
%{update_desktop_database}
%update_icon_cache hicolor

%postun kcolorchooser
%{clean_desktop_database}
%clean_icon_cache hicolor


%files kcolorchooser
%defattr(-,root,root)
%_bindir/kcolorchooser  
%_datadir/applications/kde4/kcolorchooser.desktop  
%_iconsdir/*/*/*/kcolorchooser*

#----------------------------------------------------------------------

%package -n %lib_name-kooka
Summary:    Library for Kooka 
Group:      Graphical desktop/KDE
Requires:	kdelibs4

%description  -n %lib_name-kooka
Library for Kooka 

%post kooka

update-alternatives --install %{launchers}/kde.desktop scanner.kde.dynamic %launchers/%name.desktop 31
update-alternatives --install %{launchers}/gnome.desktop scanner.gnome.dynamic %launchers/%name.desktop 29

%postun kooka

if [ $1 = 0 ]; then
  update-alternatives --remove scanner.kde.dynamic %launchers/%name.desktop
  update-alternatives --remove scanner.gnome.dynamic %launchers/%name.desktop
fi

%files -n %lib_name-kooka
%defattr(-,root,root)
%_libdir/libkscan.so.*

#----------------------------------------------------------------------

%package -n %lib_name-kooka-devel
Summary:    Devel files for Kooka 
Group:      Development/KDE and Qt
Requires:	kdelibs4
Requires:	%lib_name-kooka = %epoch:%version-%release
Provides:	%{lib_name_orig}-kooka-devel = %epoch:%version-%release

%description  -n %lib_name-kooka-devel
Devel files for Kooka 

%post -n %lib_name-kooka -p /sbin/ldconfig
%postun -n %lib_name-kooka -p /sbin/ldconfig

%files -n %lib_name-kooka-devel
%defattr(-,root,root)
%_libdir/libkscan.so

#----------------------------------------------------------------------


%prep
%setup -q -nkdegraphics-%version-%branch_date

%build

cd $RPM_BUILD_DIR/kdegraphics-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -fr %buildroot

cd $RPM_BUILD_DIR/kdegraphics-%version-%branch_date
cd build

make DESTDIR=%buildroot install


# Create LMDK menu entries
export PATH=%_bindir:$PATH



#mandriva-add-xdg-categories.pl kdegraphics-kdvi Office/Publishing %buildroot/%_datadir/applications/kde4/kdvi.desktop %buildroot/%_menudir/kdegraphics-kdvi
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kfax.desktop "Office/Communications/Fax" 

#mandriva-add-xdg-categories.pl kdegraphics-kfax "Office/Communications/Fax" %buildroot/%_datadir/applications/kde/kfaxview.desktop %buildroot/%_menudir/kdegraphics-kfaxview

mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kghostview.desktop Office/Publishing 
#mandriva-add-xdg-categories.pl kdegraphics-kview Multimedia/Graphics %buildroot/%_datadir/applications/kde/kview.desktop %buildroot/%_menudir/kdegraphics-kview
#mandriva-add-xdg-categories.pl kdegraphics-kooka Multimedia/Graphics %buildroot/%_datadir/applications/kde/kooka.desktop %buildroot/%_menudir/kdegraphics-kooka
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kpovmodeler.desktop Multimedia/Graphics 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kuickshow.desktop Multimedia/Graphics 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcolorchooser.desktop Multimedia/Graphics 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kcoloredit.desktop Multimedia/Graphics 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kiconedit.desktop Multimedia/Graphics 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kruler.desktop Multimedia/Graphics 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/ksnapshot.desktop Multimedia/Graphics 
mandriva-add-xdg-categories.pl %buildroot/%_datadir/applications/kde4/kolourpaint.desktop Multimedia/Graphics 
#mandriva-add-xdg-categories.pl kdegraphics-common System/Configuration/KDE/Peripherals %buildroot/%_datadir/applications/kde/kamera.desktop %buildroot/%_menudir/kdegraphics-kamera kde
#mandriva-add-xdg-categories.pl kdegraphics-common System/Configuration/KDE/Peripherals %buildroot/%_datadir/applications/kde/kgamma.desktop %buildroot/%_menudir/kdegraphics-kgamma kde
#mandriva-add-xdg-categories.pl kdegraphics-kmrml System/Configuration/KDE/System %buildroot/%_datadir/applications/kde/kcmkmrml.desktop %buildroot/%_menudir/kdegraphics-kcmkmrml kde

# David - 2.1-1mdk - kghostview title is "PS/PDF viewer". "PS/" create a new
#                    and non needed submenu. Foolowing command fix that.
#perl -pi -e "s|PS/PDF|PS and PDF|" %buildroot/%_menudir/kdegraphics-kghostview

mkdir -p $RPM_BUILD_ROOT%launchers
cat > $RPM_BUILD_ROOT%launchers/%name.desktop << EOF
[Desktop Entry]
Name=Kooka \$devicename
Comment=Kooka
Exec=%_bindir/kooka
Terminal=false
Icon=scanner.png
Type=Application
EOF

%clean
rm -fr %buildroot


