GÉNÉRAL:
- Accueil : "Vous êtes (n'êtes pas) connecté comme…" / Login / Signup.
- Page de login : ajouter signup.
- User: Préférences: affichage liste/calendrier.
- Boutons "Annuler" : ajouter une flèche gauche avant le mot "Annuler".
- Everywhere in the site: when create and update, put an "else:" corresponding to the "if request.method == 'POST':" before "form = …".

AGENDA:
- Calendrier.
- Fetcher les retraites et leurs nombres dans la page du P. Savio.

HÔTELLERIE:
- Jours de promenades, retraites.
- Séjour : dans le formulaire, mettre tous les repas avec cases à cocher, pour pouvoir décliquer les repas sautés au cas par cas. (Autre solution : un formset de date + repas ?)
- Un laïc (Personne "non-prêtre") ne devrait pas pouvoir célébrer (case "Prêtre avec Messe" dans la fiche Séjour).

MÉMO:
- Rafraîchir les fichiers de conf. à partir des fichiers actuels, et vérifier qu'ils y sont tous.
- Taskwarrior: + 'verbose=off'.
- Installation :
    - /sda1: point de montage: / ne pas oublier 'bootable'
      /sda2: point de montage: /media/frromain/DATA
      /sda3 (peut être changé après avec GParted?): pas plus de 8Go
    - Gregorio: nécessite le paquet 'cmake'.
    - Mettre à jour l'IP du proxy partout.
    - MySQL : Pour Debian11: '…0.8.22-1_all.deb'
    - Virtual Box: logs:
        root@debian:~# /sbin/vboxconfig 
        vboxdrv.sh: Stopping VirtualBox services.
        vboxdrv.sh: Starting VirtualBox services.
        vboxdrv.sh: Building VirtualBox kernel modules.
        This system is currently not set up to build kernel modules.
        Please install the Linux kernel "header" files matching the current kernel
        for adding new hardware support to the system.
        The distribution packages containing the headers are probably:
            linux-headers-amd64 linux-headers-5.10.0-21-amd64
        This system is currently not set up to build kernel modules.
        Please install the Linux kernel "header" files matching the current kernel
        for adding new hardware support to the system.
        The distribution packages containing the headers are probably:
            linux-headers-amd64 linux-headers-5.10.0-21-amd64

        There were problems setting up VirtualBox.  To re-start the set-up process, run
        /sbin/vboxconfig
        as root.  If your system is using EFI Secure Boot you may need to sign the
        kernel modules (vboxdrv, vboxnetflt, vboxnetadp, vboxpci) before you can load
        them. Please see your Linux system's documentation for more information.
        root@debian:~# aptitude show linux-headers-amd64 
        Package: linux-headers-amd64             
        Version: 5.10.178-3
        State: installed
        Automatically installed: yes
        Priority: optional
        Section: kernel
        Maintainer: Debian Kernel Team <debian-kernel@lists.debian.org>
        Architecture: amd64
        Uncompressed Size: 10.2 k
        Depends: linux-headers-5.10.0-22-amd64 (= 5.10.178-3)
        Provides: linux-headers-generic
        Description: Header files for Linux amd64 configuration (meta-package)
        This package depends on the architecture-specific header files for the latest Linux kernel amd64 configuration.
        Homepage: https://www.kernel.org/


        root@debian:~# aptitude show linux-headers-5.10.0-21-amd64 
        Package: linux-headers-5.10.0-21-amd64   
        Version: 5.10.162-1
        State: not installed
        Priority: optional
        Section: kernel
        Maintainer: Debian Kernel Team <debian-kernel@lists.debian.org>
        Architecture: amd64
        Uncompressed Size: 5,719 k
        Depends: linux-headers-5.10.0-21-common (= 5.10.162-1), linux-kbuild-5.10 (>= 5.10.162-1), linux-compiler-gcc-10-x86
        Description: Header files for Linux 5.10.0-21-amd64
        This package provides the architecture-specific kernel header files for Linux kernel 5.10.0-21-amd64, generally used for building out-of-tree kernel
        modules.  These files are going to be installed into /usr/src/linux-headers-5.10.0-21-amd64, and can be used for building modules that load into the
        kernel provided by the linux-image-5.10.0-21-amd64 package.
        Homepage: https://www.kernel.org/


        root@debian:~# aptitude install linux-headers-5.10.0-21-amd64 
        The following NEW packages will be installed:
        linux-headers-5.10.0-21-amd64 linux-headers-5.10.0-21-common{a} 
        0 packages upgraded, 2 newly installed, 0 to remove and 100 not upgraded.
        Need to get 10.1 MB of archives. After unpacking 59.0 MB will be used.
        Do you want to continue? [Y/n/?] y
        Get: 1 http://security.debian.org/debian-security bullseye-security/main amd64 linux-headers-5.10.0-21-common all 5.10.162-1 [9,060 kB]
        Get: 2 http://security.debian.org/debian-security bullseye-security/main amd64 linux-headers-5.10.0-21-amd64 amd64 5.10.162-1 [1,066 kB]
        Fetched 10.1 MB in 3s (3,205 kB/s)                   
        Selecting previously unselected package linux-headers-5.10.0-21-common.
        (Reading database ... 242006 files and directories currently installed.)
        Preparing to unpack .../linux-headers-5.10.0-21-common_5.10.162-1_all.deb ...
        Unpacking linux-headers-5.10.0-21-common (5.10.162-1) ...
        Selecting previously unselected package linux-headers-5.10.0-21-amd64.
        Preparing to unpack .../linux-headers-5.10.0-21-amd64_5.10.162-1_amd64.deb ...
        Unpacking linux-headers-5.10.0-21-amd64 (5.10.162-1) ...
        Setting up linux-headers-5.10.0-21-common (5.10.162-1) ...
        Setting up linux-headers-5.10.0-21-amd64 (5.10.162-1) ...
                                                
        root@debian:~# /sbin/vboxconfig 
        vboxdrv.sh: Stopping VirtualBox services.
        vboxdrv.sh: Starting VirtualBox services.
        vboxdrv.sh: Building VirtualBox kernel modules.
        root@debian:~# aptitude remove virtualbox-7.0 
        The following packages will be REMOVED:  
        libsdl-ttf2.0-0{u} libsdl1.2debian{u} linux-headers-5.10.0-22-amd64{u} linux-headers-5.10.0-22-common{u} linux-headers-amd64{u} virtualbox-7.0 
        0 packages upgraded, 0 newly installed, 6 to remove and 100 not upgraded.
        Need to get 0 B of archives. After unpacking 276 MB will be freed.
        Do you want to continue? [Y/n/?] y
        (Reading database ... 260536 files and directories currently installed.)
        Removing libsdl-ttf2.0-0:amd64 (2.0.11-6) ...
        Removing libsdl1.2debian:amd64 (1.2.15+dfsg2-6) ...
        Removing linux-headers-amd64 (5.10.178-3) ...
        Removing linux-headers-5.10.0-22-amd64 (5.10.178-3) ...
        Removing linux-headers-5.10.0-22-common (5.10.178-3) ...
        Removing virtualbox-7.0 (7.0.8-156879~Debian~bullseye) ...
        Processing triggers for hicolor-icon-theme (0.17-2) ...
        Processing triggers for gnome-menus (3.36.0-1) ...
        Processing triggers for libc-bin (2.31-13+deb11u5) ...
        Processing triggers for shared-mime-info (2.0-1) ...
        Processing triggers for mailcap (3.69) ...
        Processing triggers for desktop-file-utils (0.26-1) ...
                                                
        root@debian:~# cd /home/frromain/Documents/Informatique/Logiciels/
        root@debian:/home/frromain/Documents/Informatique/Logiciels# ls -al
        total 381536
        drwxr-xr-x  7 frromain frromain     4096 May  2 18:54 .
        drwxr-xr-x 23 frromain frromain     4096 May  2 18:54 ..
        drwxr-xr-x  2 frromain frromain     4096 Mar 19  2019 gimp
        -rw-r--r--  1 frromain frromain 93992344 Apr 24 10:18 google-chrome-stable_current_amd64.deb
        -rw-r--r--  1 frromain frromain  7140398 Apr 24  2020 Grammalecte-fr-v1.8.0.oxt
        -rw-r--r--  1 frromain frromain  8107566 Apr 21 03:29 Grammalecte-fr-v2.1.2.oxt
        drwxr-xr-x  3 frromain frromain     4096 Mar 19  2019 imagemagick
        drwxr-xr-x  2 frromain frromain     4096 Mar 17 16:42 Inkscape
        drwxr-xr-x  3 frromain frromain     4096 Mar 19  2019 scribus
        -rw-r--r--  1 frromain frromain 70836048 Oct 18  2022 teamviewer_15.34.4_amd64.deb
        -rw-r--r--  1 frromain frromain 95692404 May  2 18:53 virtualbox-6.1_6.1.38-153438~Debian~bullseye_amd64.deb
        drwxr-xr-x  2 frromain frromain     4096 Sep  4  2022 VSCode
        -rw-r--r--  1 frromain frromain 52723768 Apr  1  2020 XnViewMP-linux-x64.deb
        -rw-r--r--  1 frromain frromain 62154672 Sep 18  2021 zoom_amd64.deb
        root@debian:/home/frromain/Documents/Informatique/Logiciels# dpkg -i virtualbox-6.1_6.1.38-153438~Debian~bullseye_amd64.deb 
        Selecting previously unselected package virtualbox-6.1.
        (Reading database ... 241254 files and directories currently installed.)
        Preparing to unpack virtualbox-6.1_6.1.38-153438~Debian~bullseye_amd64.deb ...
        Unpacking virtualbox-6.1 (6.1.38-153438~Debian~bullseye) ...
        dpkg: dependency problems prevent configuration of virtualbox-6.1:
        virtualbox-6.1 depends on libsdl1.2debian (>= 1.2.11); however:
        Package libsdl1.2debian is not installed.

        dpkg: error processing package virtualbox-6.1 (--install):
        dependency problems - leaving unconfigured
        Processing triggers for gnome-menus (3.36.0-1) ...
        Processing triggers for desktop-file-utils (0.26-1) ...
        Processing triggers for mailcap (3.69) ...
        Processing triggers for hicolor-icon-theme (0.17-2) ...
        Processing triggers for shared-mime-info (2.0-1) ...
        Errors were encountered while processing:
        virtualbox-6.1
        root@debian:/home/frromain/Documents/Informatique/Logiciels# aptitude install libsdl1.2debian 
        The following NEW packages will be installed:
        libsdl1.2debian 
        0 packages upgraded, 1 newly installed, 0 to remove and 101 not upgraded.
        Need to get 0 B/195 kB of archives. After unpacking 518 kB will be used.
        Selecting previously unselected package libsdl1.2debian:amd64.
        (Reading database ... 242012 files and directories currently installed.)
        Preparing to unpack .../libsdl1.2debian_1.2.15+dfsg2-6_amd64.deb ...
        Unpacking libsdl1.2debian:amd64 (1.2.15+dfsg2-6) ...
        Setting up libsdl1.2debian:amd64 (1.2.15+dfsg2-6) ...
        Setting up virtualbox-6.1 (6.1.38-153438~Debian~bullseye) ...
        addgroup: The group `vboxusers' already exists as a system group. Exiting.
        Processing triggers for libc-bin (2.31-13+deb11u5) ...
                                                
        Current status: 0 (-1) broken.
        root@debian:/home/frromain/Documents/Informatique/Logiciels# dpkg -i virtualbox-6.1_6.1.38-153438~Debian~bullseye_amd64.deb 
        (Reading database ... 242022 files and directories currently installed.)
        Preparing to unpack virtualbox-6.1_6.1.38-153438~Debian~bullseye_amd64.deb ...
        Unpacking virtualbox-6.1 (6.1.38-153438~Debian~bullseye) over (6.1.38-153438~Debian~bullseye) ...
        Setting up virtualbox-6.1 (6.1.38-153438~Debian~bullseye) ...
        addgroup: The group `vboxusers' already exists as a system group. Exiting.
        Processing triggers for gnome-menus (3.36.0-1) ...
        Processing triggers for desktop-file-utils (0.26-1) ...
        Processing triggers for mailcap (3.69) ...
        Processing triggers for hicolor-icon-theme (0.17-2) ...
        Processing triggers for shared-mime-info (2.0-1) ...
        root@debian:/home/frromain/Documents/Informatique/Logiciels# CD ~
        -bash: CD: command not found
        root@debian:/home/frromain/Documents/Informatique/Logiciels# cd ~
        root@debian:~# vim .
        ./             .bash_history  .cache/        .meteor/       .synaptic/     .wget-hsts     
        ../            .bashrc        .dbus/         .profile       .viminfo       
        root@debian:~# vim .bash_history 
        root@debian:~# 

MOINES:
- Models: check dates are consistent (birthday < entry < habit etc.).
- Details: modal.

POLYGLOTTE:
- Table de correspondance des versets.
