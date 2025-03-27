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


# IMPRIMERIE:
- "Ajouter…" (client, projet etc.) : bouton à mettre en haut.
- Générer devis PDF.
- Générer BL PDF.
- Suivi projet de A à Z.


# LIVRETS:
## Carême:
- *Oratio super populum*.
- Commémoraisons (Stes Perpétue et Félicité etc.)
- Cendres (et autres ?): Prière universelle.
## Pour les livrets "full":
- P. Vianney:
    • Lettrine au début et à chaque division de psaume (si possible) à Tierce
    • Oraison du jour sur une seule page
    • Je mettrai aussi une lettrine au début de chaque oraison
    • Dans les partitions, les accents ne sont pas nécessaire pour les mots de 2 syllabes (si possible)
    • Toujours dans les partitions: i à la place du j
    • Lettrine au début du canon
    • Quand il y a des V/. et R/. la deuxième ligne devrait être en retrait (si possible), cf. p. 2, 18, 20
    • Enlever la rubrique en bas de la page 20.
- P. Louis;
    • Par esprit de contradiction, je n’ai pas de correction importante, mais seulement de détail (ma spécialité est plutôt dans le filtrage du moucheron): on ne met pas deux-points en fin de ligne dans un titre (par ex. « Antienne d’Introït : »). Et pour la lecture et l’évangile, je mettrais plutôt comme dans un missel « Lecture de la lettre de saint Paul Apôtre aux Éphésiens »… Bon, évidemment, vous allez trouver ça compliqué!
    • Dans la partition du « Per ipsum », PER devrait être en capitales.


# MÉMO:
## INSTALL:
### Crontab:
*/20 8-20 * * * /home/frromain/Scripts/server.sh
30 10,16 * * * /home/frromain/Scripts/github.sh
### Vimrc:
colorscheme default
set laststatus=2
set statusline+=%F%r%m%=\ %p%%\ %l:%c
set number
set formatoptions+=w
set textwidth=0
set tabstop=4
set softtabstop=4
set shiftwidth=2
set expandtab
set autoindent
set wrap
set linebreak
set breakindent
set cursorline
:hi CursorLine cterm=bold
:map <CR> $a<Del> <Esc>
:map <C-N> i{}<Esc>hpl%
### _Calibre_ pour lire epubs, GoldenDict.
### Anki :
tar xaf anki-24.11-linux-qt6.tar.zst
cd cd anki-24.11-linux-qt6/
./install.sh
### Ajouter le paquet "rename" pour renommer des fichiers en série.
- Install : Fichier /etc/fstab:
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# systemd generates mount units based on this file, see systemd.mount(5).
# Please run 'systemctl daemon-reload' after making changes here.
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda1 during installation
UUID=b3b077a0-6fac-461d-8dcf-5c51d8f7f542 /               ext4    errors=remount-ro 0       1
# /media/frromain/DATA was on /dev/sda2 during installation
UUID=9cbb4ca5-7d85-4267-b759-4446a8d4a1f4 /media/frromain/DATA ext4    defaults        0       2
# swap was on /dev/sda5 during installation
UUID=43967b17-11a5-47be-bec3-a999ed811195 none            swap    sw              0       0
/dev/sr0        /media/cdrom0   udf,iso9660 user,noauto     0       0
- Commandes : Liste de tous les paquets installés : 'apt list --installed'.
- Python : Ajouter 'WSGIApplicationGroup %{GLOBAL}' dans le virtual host d'Apache.
- Rafraîchir les fichiers de conf. à partir des fichiers actuels, et vérifier qu'ils y sont tous.
- Taskwarrior: + 'verbose=off'.
- Installation :
    - /sda1: point de montage: / ne pas oublier 'bootable'
      /sda2: point de montage: /media/frromain/DATA
      /sda3 (peut être changé après avec GParted?): pas plus de 8Go
    - Gregorio: nécessite le paquet 'cmake'.
    - Mettre à jour l'IP du proxy partout.
    - Virtual Box sur Debian 12:
        + Installation :
        wget -O- -q https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --dearmour -o /usr/share/keyrings/oracle_vbox_2016.gpg
        echo "deb [arch=amd64 signed-by=/usr/share/keyrings/oracle_vbox_2016.gpg] http://download.virtualbox.org/virtualbox/debian bookworm contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
        sudo apt update
        sudo apt install virtualbox-7.1

        + Extensions :
        sudo apt install virtualbox-7.1
        wget https://download.virtualbox.org/virtualbox/7.1.0/Oracle_VirtualBox_Extension_Pack-7.1.0.vbox-extpack
        sudo vboxmanage extpack install Oracle_VirtualBox_Extension_Pack-7.1.0.vbox-extpack

        + Vérification des extensions :
        vboxmanage list extpacks

        + Ajouter User to the vboxusers Group :
        sudo usermod -a -G vboxusers frromain

        + Reboot.

        + Vérifier que User est dans vboxusers :
        groups $USER

        + Uninstall :
        sudo apt purge virtualbox-7.1
        sudo apt autoremove
        sudo rm /etc/apt/sources.list.d/virtualbox.list
    - Virtual Box sur Debian 10:
    Créer le fichier /etc/apt/sources.list.d/virtualbox.list:
    vim /etc/apt/sources.list.d/virtualbox.list
    Écrire la ligne suivante, enregistrer et fermer:
    deb https://download.virtualbox.org/virtualbox/debian buster contrib
    Puis:
    wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | apt-key add -
    wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | apt-key add -
    apt-get update
    apt-get install virtualbox-7.0
    Extensions:
    wget https://download.virtualbox.org/virtualbox/7.0.0/Oracle_VM_VirtualBox_Extension_Pack-7.0.0.vbox-extpack

## Raccourcis clavier:
Vetus Latina:
evince /home/frromain/Documents/Sainte\ Écriture/0\ Bibles/Vetus\ Latina.pdf
Polyglotte de Walton
evince /home/frromain/Documents/Sainte\ Écriture/0\ Bibles/Polyglotte\ Walton/Walton\'s\ Polyglot\ -\ Totum.pdf
Jastrow
evince /home/frromain/Documents/Sainte\ Écriture/Langues\ bibliques/Araméen/Jastrow-AramaicHebrew.pdf
Syriaque
evince /home/frromain/Documents/Sainte\ Écriture/Langues\ bibliques/Syriaque/epdf.pub_a-compendious-syriac-dictionary.pdf
PierreQuiBible
python3 /home/frromain/Documents/Sainte\ Écriture/Divers/PQV/PierreQuiBible/rollingBible.py
Gaffiot
evince /home/frromain/Documents/Langues/Latin/Dictionnaires\ latins/Gaffiot_2016.pdf
Bailly
evince /home/frromain/Documents/Langues/Grec/bailly-2020-hugo-chavez-20200718.pdf
Zorell grec
evince /home/frromain/Documents/Sainte\ Écriture/Langues\ bibliques/Grec/NT/Zorell\ grec.pdf
Zorell hébreu
evince /home/frromain/Documents/Sainte\ Écriture/Langues\ bibliques/Hébreu/Zorell\ hébreu.pdf
Utiles
libreoffice /media/frromain/DATA/Documents/Divers/Utiles.ods


### Installation Debian 12:
#### Pour Django avec MySQL, mettre à jour la commande :
apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config

#### Au lieu de pip3 install virtualenv:
apt-get install python3-virtualenv
virtualenv -p python3.11 abbaye

#### Mysql:
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

#### Apache : redirection de "services.asj.com/" vers "http://python.asj.com:8011/abbaye/" :
<VirtualHost *:80>
    ServerName services.asj.com
    Redirect "/" "http://python.asj.com:8011/abbaye/"
</VirtualHost>

#### Mutt:
~/.msmtprc :
account dev
account default : dev 
user clairval
host <my_host>
port 587
auth plain
password <my_super_password>

---

## Commandes:
- 'free' pour avoir la RAM.

---

## Git:
Pour rapatrier un submodule:
git submodule update --remote

---

## MySQL:
- Mettre à jour le champ "commentaire_listing" de la table abbaye.hotellerie_sejour en récupérant ce même champ dans une ancienne table ("hotellerie.sejours_sejour") et en se basant sur l'ID :
>>> UPDATE abbaye.hotellerie_sejour AS a INNER JOIN hotellerie.sejours_sejour AS h ON a.id = h.id SET a.commentaire_listing = h.commentaire_listing;

- Jointures:
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

---

## Python:
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

## HTML:
Rediriger d'une page html vers une autre:
Dans le <head>:
<meta http-equiv="refresh" content="0; url=http://example.com/" />

------

## Bash scripts:
### Substring Removal
${string#substring}
Deletes shortest match of $substring from front of $string.
${string##substring}
Deletes longest match of $substring from front of $string.
${string%substring}
Deletes shortest match of $substring from back of $string.
${string%%substring}
Deletes longest match of $substring from back of $string.
Exemple :
url="http://clairval.com"
echo ${url#*/}
>>> /clairval.com
echo ${url##*/}
>>> clairval.com
echo ${url%/*}
>>> http:/
echo ${url%%/*}
>>> http:
url="http://clairval.com/"
echo ${url#*/}
>>> /clairval.com/
echo ${url##*/}
>>>
echo ${url%/*}
>>> http://clairval.com
echo ${url%%/*}
>>> http:

### Cut:
$ s='one_two_three_four_five'
$ A="$(cut -d'_' -f2 <<<"$s")"
$ echo "$A"
two
$ B="$(cut -d'_' -f4 <<<"$s")"
$ echo "$B"
four
La même chose avec awk:
A=$(awk -F_ '{print $2}' <<< 'one_two_three_four_five')
B=$(awk -F_ '{print $4}' <<< 'one_two_three_four_five')  

### Save the output of a command to a file:
          || visible in terminal ||   visible in file   || existing
  Syntax  ||  StdOut  |  StdErr  ||  StdOut  |  StdErr  ||   file   
==========++==========+==========++==========+==========++===========
    >     ||    no    |   yes    ||   yes    |    no    || overwrite
    >>    ||    no    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
   2>     ||   yes    |    no    ||    no    |   yes    || overwrite
   2>>    ||   yes    |    no    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
   &>     ||    no    |    no    ||   yes    |   yes    || overwrite
   &>>    ||    no    |    no    ||   yes    |   yes    ||  append
          ||          |          ||          |          ||
 | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite
 | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    || overwrite
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
|& tee    ||   yes    |   yes    ||   yes    |   yes    || overwrite
|& tee -a ||   yes    |   yes    ||   yes    |   yes    ||  append

List:
    command > output.txt
    The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

    command >> output.txt
    The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

    command 2> output.txt
    The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

    command 2>> output.txt
    The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

    command &> output.txt
    Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, it gets overwritten.

    command &>> output.txt
    Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, the new data will get appended to the end of the file..

    command | tee output.txt
    The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, it gets overwritten.

    command | tee -a output.txt
    The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

    (*)
    Bash has no shorthand syntax that allows piping only StdErr to a second command, which would be needed here in combination with tee again to complete the table. If you really need something like that, please look at "How to pipe stderr, and not stdout?" on Stack Overflow for some ways how this can be done e.g. by swapping streams or using process substitution.

    command |& tee output.txt
    Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, it gets overwritten.

    command |& tee -a output.txt
    Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

### Durée d'exécution d'un script:
time my_script.sh
Retourne:
real    2m5.034s # <-- Actual time taken from start to finish.
user    0m0.000s # <-- CPU time user-space.
sys     0m0.003s # <-- CPU time kernel-space.

------

## Commandes:
### Rename files with find:
find . -name 'file_*' -exec rename 's/file_/mywish_/' {} \;

### Rename files with find: replace spaces with underscores:
find -name '* *' -exec bash -c 'mv "$1" "${1// /_}"' -- {} \;

### Remove files of a dir, except 'file.txt':
find . ! -name 'file.txt' -type f -exec rm -f {} +

### Taille d'un dossier:
du -h --max-depth=2 . | sort -hr
-h : human-readable
--max-depth=2 : taille des sous-dossiers avec une profondeur de 2.
-hr : trier ('sort') par le champ 'human-readable' ('h') en sens inverse ('r', les plus lourds d'abord)


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

2024: Messe du samedi des 4 Temps de septembre (III Septembris) décalée par erreur à la IVe semaine de septembre en 2024 (dû à saint Matthieu ?).

Faire la chasse aux ant. de Benedictus et Magnificat inutilement indiquées car tirées du Commun.

Annonciation : le report à Pâques + 8 ne fonctionne pas (2027).

Césures : pas moins de 2 lettres.

Problème du "Quatuor": enlever la queue. Ou changer de police ?


# POLYGLOTTE:
- Table de correspondance des versets.
