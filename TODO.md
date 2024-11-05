# GÉNÉRAL:
- Accueil : "Vous êtes (n'êtes pas) connecté comme…" / Login / Signup.
- Page de login : ajouter signup.
- User: Préférences:
  - Affichage liste/calendrier.
  - Recevoir mail fêtes moines ("la veille", "le jour même", "jamais").
- Boutons "Annuler" : ajouter une flèche gauche avant le mot "Annuler".
- Everywhere in the site: when create and update, put an "else:" corresponding to the "if request.method == 'POST':" before "form = …".

# AGENDA:
- Calendrier.
- Fetcher les retraites et leurs nombres dans la page du P. Savio.
- Empêcher date_to < date_from.
- On change date_from: date_to = date_from.

# HÔTELLERIE:
- Jours de promenades, retraites.
- Séjour : dans le formulaire, mettre tous les repas avec cases à cocher, pour pouvoir décliquer les repas sautés au cas par cas. (Autre solution : un formset de date + repas ?)
- Un laïc (Personne "non-prêtre") ne devrait pas pouvoir célébrer (case "Prêtre avec Messe" dans la fiche Séjour).

# MÉMO:
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

- Installation Debian 12:
Pour Django avec MySQL, mettre à jour la commande :
apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config

Au lieu de pip3 install virtualenv:
apt-get install python3-virtualenv 
virtualenv -p python3.11 abbaye

Mysql:
wget https://dev.mysql.com/get/mysql-apt-config_0.8.30-1_all.deb
dpkg -i mysql-apt-config_0.8.30-1_all.deb 
apt update
apt install mysql-server
Pour pouvoir installer libssl:
wget http://snapshot.debian.org/archive/debian/20190501T215844Z/pool/main/g/glibc/multiarch-support_2.28-10_amd64.deb
dpkg -i multiarch-support*.deb
Installer libssl:
wget https://snapshot.debian.org/archive/debian-archive/20240331T102506Z/debian/pool/main/o/openssl/libssl1.1_1.1.1n-0%2Bdeb10u3_amd64.deb
dpkg -i libssl1.1_1.1.1n-0+deb10u3_amd64.deb
apt install mysql-server
Faire:
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<my_password>';
Avant de faire:
mysql_secure_installation
Si problème, faire un killall -9 mysql_secure_installation dans un autre Terminal, puis Alter user, puis de nouveau secure_install.

Apache : redirection de "services.asj.com/" vers "http://python.asj.com:8011/abbaye/" :
<VirtualHost *:80>
    ServerName services.asj.com
    Redirect "/" "http://python.asj.com:8011/abbaye/"
</VirtualHost>

---

MySQL : Mettre à jour le champ "commentaire_listing" de la table abbaye.hotellerie_sejour en récupérant ce même champ dans une ancienne table ("hotellerie.sejours_sejour") et en se basant sur l'ID :
>>> UPDATE abbaye.hotellerie_sejour AS a INNER JOIN hotellerie.sejours_sejour AS h ON a.id = h.id SET a.commentaire_listing = h.commentaire_listing;

---

Python:
I have a list of lists like

[
    [1, 2, 3],
    [4, 5, 6],
    [7],
    [8, 9]
]

How can I flatten it to get [1, 2, 3, 4, 5, 6, 7, 8, 9]?

Answer:
flat_list = [
    x
    for xs in xss
    for x in xs
]

------

HTML:
Rediriger d'une page html vers une autre:
Dans le <head>:
<meta http-equiv="refresh" content="0; url=http://example.com/" />

------

MySQL:
Jointures:

Assuming you're joining on columns with no duplicates, which is a very common case:

    An inner join of A and B gives the result of A intersect B, i.e. the inner part of a Venn diagram intersection.

    An outer join of A and B gives the results of A union B, i.e. the outer parts of a Venn diagram union.

Examples

Suppose you have two tables, with a single column each, and data as follows:

A    B
-    -
1    3
2    4
3    5
4    6

Note that (1,2) are unique to A, (3,4) are common, and (5,6) are unique to B.

Inner join

An inner join using either of the equivalent queries gives the intersection of the two tables, i.e. the two rows they have in common.

select * from a INNER JOIN b on a.a = b.b;
select a.*, b.*  from a,b where a.a = b.b;

a | b
--+--
3 | 3
4 | 4

Left outer join

A left outer join will give all rows in A, plus any common rows in B.

select * from a LEFT OUTER JOIN b on a.a = b.b;
select a.*, b.*  from a,b where a.a = b.b(+);

a |  b
--+-----
1 | null
2 | null
3 |    3
4 |    4

Right outer join

A right outer join will give all rows in B, plus any common rows in A.

select * from a RIGHT OUTER JOIN b on a.a = b.b;
select a.*, b.*  from a,b where a.a(+) = b.b;

a    |  b
-----+----
3    |  3
4    |  4
null |  5
null |  6

Full outer join

A full outer join will give you the union of A and B, i.e. all the rows in A and all the rows in B. If something in A doesn't have a corresponding datum in B, then the B portion is null, and vice versa.

select * from a FULL OUTER JOIN b on a.a = b.b;

 a   |  b
-----+-----
   1 | null
   2 | null
   3 |    3
   4 |    4
null |    6
null |    5

------

# MOINES:
- Models: check dates are consistent (birthday < entry < habit etc.).
- Details: modal.

# ORDOMATIC:
- Ordos 2011 et 2038 à voir : pb 3e samedi de juin.
- Ordo 2007 : bug.
- Anniv. professions etc.
- Oraison Ste Famille.
- Vigiles Ste Vierge le samedi, attribution intelligente des numéros, pour éviter 4e = 5e.
- Ste Famille : Bizarre, il semble qu'il y ait eu à une époque (2015 au moins) des lectures entièrement différentes pour chaque année.
- ordo_write.py : commentaire Rogations : Code + propre. Il y a 4 cas : vigile = juste "Ben", festum = rien, mémoires mineures = juste "Magnif", et de ea pas vigiles = les 2. TODO : le cas "les 2" n'a pas été testé (pas d'occurrence en 2014). TODO : 2015 problème : veille de l'Ascension = mémoire mineure.
- Sancto : saint Grégoire de Nysse (10/01) : Tirer au clair cette histoire de report à après le Baptême.
- Saint Benoît dimanche : tester que le bon dimanche s'affiche (per annum, post pentec.).
- Présentation dimanche : tester que le bon dimanche s'affiche pour la forme extraordinaire (Septuagésime, etc.).
- ND Mont-Carmel samedi.
- Transfiguration dimanche : il y a des Ières Vêpres, et de plus on calcule quel dimanche (per annum, post Pentecosten).
- Assomption dimanche : vérifier que bon dimanche (per annum, post Pentecosten, dim. d'août).
- Toussaint dimanche : vérifier que bon dimanche (per annum, post Pentecosten, dim. de nov).
- Vérifier les samedis, avec les lectures mariales aux Vigiles. Attention: si le 16/07 tombe un samedi, ce n'est pas la peine (cf. Sancto à ce jour).
- Féries entre Octave de Noël et Baptême: if new_day_date.day == 7 and new_day_date.weekday() != 6: # TODO: Dans quels cas omet-on les "generalities", et dans quels cas les modifie-t-on ?
- Féries per annum : new_day["generalities"] = ("\n\\newpage\n\\ApplyParBox{1cm}{\\ApplyGenerTitleHuge{Tempus Per annum}}\n\\ApplyGenerSubTitle{in Ofﬁcio :}\n\\ApplyGenerList{\n\\item In feriis : hebdomada I per annum vel I post Epiphaniam.}\n\\ApplyGenerSubTitle{ad mensam :}\n\\ApplyGenerList{\n\\item Benedictio de tempore per annum.}" + lectiones_body + "\n\\ApplyGenerList{\n\\item Præfatio communis I, nisi aliter notetur.}\n\\medskip") if i == 0 and j == 0 else "" # TODO : Body = Vigiles… + "in MC : lectiones feriales" à la 1ère férie libre. Pourquoi pas dans le generalities ?
- Texte spécial pour le 3e samedi de juin, s'il tombe avant la Trinité… :) TODO : Ce cas (rarissime) n'a pas encore été testé. functions/tempo.py-new_day["body"] = "\n\\item Ad Vigilias : lectio sabbato 3 (in supplemento 202).\n\\item In MC : Beatæ Mariæ Virginis, Matris et mediatricis gratiæ (CM 30) ; præfatio I de Beata Maria Virgine."
- Remplacer partout les tabulations par 4 espaces.
- Semailles = 1ère férie libre avant l'Ascension (descendre du lundi au mercredi). Récoltes = semaine avant 3e dim. de Septembre (4 temps de sept.) : mercredi ou vendredi, sinon lundi, mardi ou jeudi.
- Fêtes mobiles de l'année suivante à la fin de l'ordo.
- 1er samedi du mois de janvier : in ML avant in MC (7/1/2017 par ex.).
- Octave de Pentecôte : calculer et modifier toutes les mc_bmv (dans various).
- Saint Boniface : 3 cas : TP, entre Pent. et Trin., après Trinité. 2e cas, ajouter cette mention pour les Vigiles : "Ad Vigilias: post lectionem dicitur Responsorium *Iste sanctus*, e Communi Martyris extra Tempus Paschale post primam lectionem I Nocturni."
- Automatiser le report d'un jour de jeûne au lendemain si festum.
- Page de garde: variante "évidée" de la même police.
- 9 janvier 2021: ajouter «- in ML: Missa de sancta Maria in sabbato.
- Pour les fêtes, il me semblerait plus léger de ne mettre en petites capitales que le nom du saint (e.g. S. Bernardi), en laissant son titre en romain (e.g. abbatis et Ecclesiæ doctoris): comme pour les mémoires majeures, mais en gras.
- Alterner 1 année sur 2 saint Clément et saint Colomban :
    \ApplyHeader{\textbf{23} & Feria III - \textsc{S. Columbani}, abbatis - \textbf{memoria maior} - \textit{Alb.}}
    \ApplyBody{
        \item In Officio~: oratio in supplemento 193*.
        \item Ad Vigilias~: lectio in supplemento 193*.
        \item \textit{in ML~: Missa pro abbate.}
        \item In MC~: collecta in MP~; Commune sanctorum et sanctarum (MR 958)~; præfatio de sanctis virginibus et religiosis.}
- Il faudrait que les abréviations utilisées pour les livres bibliques correspondent avec la table donnée en p. 4 (par exemple Io et non pas Jn).

I. Sanctoral
• 6 août (2022) : la Transfiguration, fête du Seigneur, prime sur le dimanche, donc « Vesperæ festi ».
• 17 septembre (années impaires) : à la ligne du Benedictus, il manque une espace « tono III g »

II. Temporal
• Mettre l’oraison des mercredi et vendredi des Quatre-Temps de l’Avent aussi aux vêpres avant le 17 décembre (comme indiqué dans le bréviaire, p. 62 et 65 : « Oratio Præsta / Excita, quæ dicitur ad omnes Horas, etiam ad Vesperas »).

III. Généralités
• Tons des antiennes : espace insécable entre le mode et la différence (III g)
• Indiquer les commémoraisons à faire (ML) : Avent et Carême
• Bénédiction solennelle pour les solennités : ajouter à MC une rubrique « Missa concluditur benedictione sollemni. »
    ◦ 1 er dimanche de l’Avent
    ◦ Noël (Messe de la nuit + Messe du jour)
    ◦ 1 er janvier
    ◦ Épiphanie
    ◦ Pâques (Vigile + Messe du jour)
    ◦ Ascension
    ◦ Pentecôte
    ◦ 29 juin : saints Pierre et Paul
    ◦ 15 août, 8 décembre : B. V. M.
    ◦ Toussaint
• Insérer deux variantes : Flavigny/Solignac
• Carême (MC) :
    ◦ Mercredi des Cendres et vendredis de carême : Canon à genoux

Le Père Abbé Antoine me signale une petite erreur de référence dans l’Ordo, pour le samedi de la 27ᵉ semaine TO années impaires: Ioel 4, 12-21 au lieu de Ioel 3, 12-21.

Sainte Thérèse 15/10 : simplifier les hymnes: Ad vigilias, Laudes et Vesperas: Hymni proprii. Ensuite il n'y a plus qu'à préciser les ant. de Ben. et Magn.

Pour les commémoraisons en Avent et en Carême, il faudrait trouver une solution… Idem pour le cas où les Quatre-Temps tombent un 23 septembre, par exemple: comme saint Pio est une mémoire obligatoire, la commémoraison est in-dis-pen-sable.

Début novembre : "lectio *de memoria*" à affiner (ça peut être avant les lectures SO, du coup inutile de préciser "de memoria").

Saint Bénigne à refondre.

Après les corrections 2022, il reste encore quelques moucherons :
Page 96 (8 septembre), il manque une espace avant la parenthèse: «II(pro».
Page 85 (24 juillet), c’est la préface I du dimanche (et non pas la VIII) pour le XVIIᵉ dimanche per annum.
    Idem page 98 (18 septembre), préface I pour le XXVᵉ dimanche per annum.
    Idem page 112 (13 novembre), préface I pour le XXXIIIᵉ dimanche per annum.
Page 112 (lundi 14 novembre): MC pour les bienfaiteurs défunts (collision avec les antiennes spéciales Ben. et Magn. ?).

Baptême : refondre.

7/1 : Inverser ML/MC.
2/2 : He (pas Hebr), et Lc en gras.

Pour l’évangile de ce lundi notre ordo indique Jn 8, 12-20.
Or, pour les années C, le lectionnaire dit de lire cet évangile lorsque l’évangile de la femme adultère (Jn 8, 1-11) a été lu le dimanche précédent ; donc, lorsque celui-ci n’a pas été lu le dimanche (ce qui est notre cas puisque on a lu celui de l’année A), il faut le lire le lundi.
En conclusion, l’évangile de ce lundi devrait être Jn 8, 1-11.

2022 : saint Bède : "in Officio et in ML": supprimer.

P. Jean Pouchet : "Pour simplifier, il faudrait distinguer entre Fête-Dieu le 24 (avec Saint-Jean-Baptiste le 25) et Sacré-Cœur le 24 (avec Saint-Jean-Baptiste le 23)…"

3e Messe des défunts (septembre): il semble que la référence de l'Évangile ait changé (Jo).

11 juin (2038) : la Saint-Barnabé tombe pendant le temps pascal…

Vérifier le bon comportement "vigile Pentecôte" et "infra octavam Pentecostes" (y compris "4 Temps", y compris "samedi brevior") des saints suivants:
11/5
13/5
15/5
18/5
19/5
25/5
26/5
27/5
30/5
31/5
1/6
2/6
3/6
5/6
9/6
11/6
13/6
19/6

Antiennes du XXIVe dim. ap. la Pentecôte : jamais avant le Christ-Roi. Comme cela ne se produira pas avant plusieurs années, je surseois !

23 décembre : si vendredi : Ant. Benedictus p. 231 et non 220 (plus naturel), dans la mesure où c'est la même.

Præfatio II de BMV à mettre plus souvent ?

Annonciation reportée (2024) : les Vêpres disparaissent (tant les 1ères que les 2e).

Ste Famille : pourquoi jamais les leçons du IIIe Nocturne ? Si confirmation : ne pas préciser "I et II Noct." lors des années paires.

Commémoraison des saints durant le Carême : préciser dans quel Commun chercher le verset.

St Jérôme Émilien : préciser qu'on prend le Trait au Commun des Confesseurs.

P. Irénée _17_ février.

24 juin : saint Jean-Baptiste : "Vesperæ solemnitatis" ??? (2024)
Préface propre Mater Ecclesiæ?

Lectures propres Pentecôte années B et C?

Visitation (31/05): Ad Vigilias: in supplemento 122; invitatorium proprium in supplemento 58 (seulement quand le 31 mai tombe avant la Trinité)
Supprimer "In ML: Missa in PAL; præfatio de sanctis."

Office de saints Maur et Placide : prendre répons, hymne et verset du commun de plusieurs confesseurs (5 octobre) sauf hymne de saint Maur

Corrections 2024 :
    • * Évangile Vigile pascale année B : Mc 16, 1-7 (corriger dans l’évangéliaire)
    • * 17 février (et non pas le 18) : décès du T.R.P. Irénée Henriot
    • 19 et 21 mars : « année I, saint Joseph les trois premiers psaumes, saint Benoît les trois suivants, et l’inverse l’année II » (dans ce cas, il faudrait appliquer la même logique à toutes les fêtes)
    • * 25 mars : vérifier Salut pour Annonciation
    • * 12 septembre : Saint Nom de Marie, préface propre CM 21
    • * 23 octobre : Notre-Dame de la Sainte-Espérance, préface propre CM 37
    • Quatre-Temps de septembre (IIIe semaine) :
        ◦ * c’est le samedi, et non pas le mercredi, qu’il y a une forma Missæ brevior ;
# FIXME messe du samedi des 4 Temps de septembre (III Septembris) décalée par erreur à la IVe semaine de septembre en 2024.
    • * Va-t-on se décider à mettre plus souvent la Préface II de la Ste Vierge ?

2025 :
Horreur! On a remplacé mes jolies espaces insécables par cet affreux gribouillis: ☒ => Pas trouvé.
Manque une espace p. 106 (2 novembre) « NoctunisI ». Mais, de toute façon, il faudra supprimer ce paragraphe (ut infra). Enfin, ça servira pour les autres années. => Ai remplacé le I par une espace insécable. Par contre je ne comprends pas la ligne de code : « Nocturnes = "psalmi et lectiones sumuntur e I et II Nocturnis." if even_year else "psalmi sumuntur e I et II Nocturnis ; lectiones sumuntur e I et II Nocturnis."». Quelle différence entre années paires et impaires?
Insérer une rubrique pour la répartition des psaumes des vigiles des fêtes et solennités sur année paire ou impaire (p. 7). => Done.
Par voie de conséquence:
    Supprimer la rubrique du jour de Noël « Ad Vigilias : psalmi hebdomadæ I. »
    Sainte Famille: si Noël tombe un dimanche, mettre les psaumes de l’année opposée: « Ad Vigilias: antiphonæ et psalmi anni I / II. »
    Idem, psaumes de l’année opposée pour:
        21 mars, saint Benoît
        => aussi saint Thomas.
        23 juillet, sainte Brigitte
        8 septembre, Nativité de la Sainte Vierge
        13 novembre, saint Bénigne
    Vérifier qu’il ne reste plus nulle part la mention « psalmi hebdomadæ ». => OK, sauf pour les 5 occurrences mentionnées.

Remettre « (forma Missæ brevior) » pour le samedi des Quatre-Temps de septembre (p. 98).
🤫 Un indice pour vous mettre sur la piste: en 2024, si on se retrouvait avec la Messe du samedi des Quatre-Temps en IVᵉ semaine (au lieu de la IIIᵉ), c’est sans doute parce que cette Messe était écrasée par la Saint-Matthieu (samedi 21 septembre).
Mercredi 28 mai: Messe pour les semailles « In MC: Missa In conserendis agris (MR 1127 A - GR 654); præfatio V de dominicis per annum. »
Mercredi 24 septembre: Messe pour les récoltes « In MC: Missa post collectos fructus terræ (MR 1129 - GR 654); præfatio V de dominicis per annum. »
Messes pour les défunts:

    Mardi 4 février: « In MC (Nigr.): Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225); lectiones propriæ: Rom 5, 5-11 / Mt 5, 1-12a; præfatio II de defunctis. »
    Mercredi 4 juin: « In MC (Nigr.): Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225); lectiones propriæ: Rom 8, 14-23 / Lc 12, 35-40; præfatio III de defunctis. »
    Lundi 1ᵉʳ septembre: « In MC (Nigr.): Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225); lectiones propriæ: 1 Io 3, 14-16 / Io 5, 24-29; præfatio IV de defunctis. »
    Mercredi 5 novembre: « In MC (Nigr.): Missa defunctorum pro omnibus benefactoribus nostris defunctis (MR 1225); lectiones propriæ: Ap 20, 11 – 21, 1 / Io 14, 1-6; præfatio V de defunctis. »

P. 52, remonter le bloc « SACRUM TRIDUUM PASCHALE »
Dimanche 2 novembre: office du dimanche, Messes des défunts. Supprimer tout ce qui a trait à l’office des défunts (Gloria Patri, vigiles, complies).

# POLYGLOTTE:
- Table de correspondance des versets.
