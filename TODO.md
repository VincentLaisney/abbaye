GÉNÉRAL:
- Accueil : "Vous êtes (n'êtes pas) connecté comme…" / Login / Signup.
- Page de login : ajouter signup.
- User: Préférences: affichage liste/calendrier.
- Boutons "Annuler" : ajouter une flèche gauche avant le mot "Annuler".
- Everywhere in the site: when create and update, put an "else:" corresponding to the "if request.method == 'POST':" before "form = …".

ABSENCES:
- Faire une page "details" (en plus du modal), cf. monks.

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
- Installation : MySQL : Pour Debian11: '…0.8.22-1_all.deb'

MOINES:
- Models: check dates are consistent (birthday < entry < habit etc.).

POLYGLOTTE:
- Table de correspondance des versets.
