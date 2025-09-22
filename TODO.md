# GÉNÉRAL:
- Accueil : "Vous êtes (n'êtes pas) connecté comme…" / Login / Signup.
- Page de login : ajouter signup.
- User: Préférences:
  - Affichage liste/calendrier.
  - Recevoir mail fêtes moines ("la veille", "le jour même", "jamais").
- Boutons "Annuler" : ajouter une flèche gauche avant le mot "Annuler".
- Everywhere in the site: when create and update, put an "else:" corresponding to the "if request.method == 'POST':" before "form = …".
- Pagination (datatables trop lourdes et lentes) pour hôtellerie, séjours etc. Inutile pour des petits tableaux.


# AGENDA:
- Calendrier.
- Fetcher les retraites et leurs nombres dans la page du P. Savio.
- Empêcher date_to < date_from.
- On change date_from: date_to = date_from.
- Après validation d'un événement : renvoyer sur la semaine de l'événement (pas la semaine en cours).


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
## Option "3 jours" ne fonctionne pas: parce qu'il attend 5 jours? à cause du formset? (suppr. de 2 forms)
## Vérifier lectures propres pour les Abbés (saint Antoine au moins ne semble pas fait).
## Lectures Ste Famille année C.
## Cendres: antiennes ad lotionem pedum.
## Dimanches, solennités, Cendres etc.: homélie.
## Carême:
- *Oratio super populum*.
- Commémoraisons (Stes Perpétue et Félicité etc.).
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
## Installation:
### Raccourcis clavier:
VirtualBox WindowsXP
virtualbox VirtualBox\ VMs/WindowsXP/WindowsXP.vbox
### Installation avec aptitude hors-proxy:
aptitude -o Acquire::http::proxy=false install […]


## HTML:
Rediriger d'une page html vers une autre:
Dans le <head>:
<meta http-equiv="refresh" content="0; url=http://example.com/" />


# MOINES:
- Models: check dates are consistent (birthday < entry < habit etc.).
- Details: modal.

# POLYGLOTTE:
- Table de correspondance des versets.
