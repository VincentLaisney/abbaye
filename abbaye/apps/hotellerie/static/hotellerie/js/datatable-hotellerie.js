$(document).ready(function () {
  $('#table-personnes').DataTable({
    order: [
      [3, 'asc'],
      [4, 'asc'],
    ],
    pageLength: 25,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> personnes',
      'infoFiltered': ' - Affichés : personnes <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> personnes trouvées',// TODO: Remplacer "1 personnes trouvés" par "1 personne trouvé":
      'infoEmpty': 'Aucune personne trouvée',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
      'lengthMenu': 'Montrer _MENU_ personnes par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher une personne :',
      'zeroRecords': 'Aucune personne trouvée',
    },
    columnDefs: [
      // Créé le :
      {
        target: 0,
        orderable: false,
        searchable: false,
      },
      // Modifié le :
      {
        target: 1,
        orderable: false,
        searchable: false,
      },
      // Qualité :
      {
        target: 2,
      },
      // Nom :
      {
        target: 3,
      },
      // Prénom :
      {
        target: 4,
      },
      // Détails :
      {
        target: 5,
        orderable: false,
        searchable: false,
      },
    ],
  });

  $('#table-sejours').DataTable({
    order: [
      [3, 'desc'],
      [4, 'desc'],
    ],
    pageLength: 100,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> séjours',
      'infoFiltered': ' - Affichés : séjours <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> séjours trouvés',// TODO: Remplacer "1 séjours trouvés" par "1 séjour trouvé":
      'infoEmpty': 'Aucun séjour trouvé',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
      'lengthMenu': 'Montrer _MENU_ séjours par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher un séjour :',
      'zeroRecords': 'Aucun séjour trouvé',
    },
    columnDefs: [
      // Créé :
      {
        target: 0,
        orderable: false,
        searchable: false,
      },
      // Modifié :
      {
        target: 1,
        orderable: false,
        searchable: false,
      },
      // Personne :
      {
        target: 2,
      },
      // Du :
      {
        target: 3,
      },
      // Au :
      {
        target: 4,
      },
      // Détails:
      {
        target: 5,
        orderable: false,
        searchable: false,
      },
    ],
  });

  $('#table-parloirs').DataTable({
    order: [
      [3, 'desc'],
      [4, 'desc'],
    ],
    pageLength: 50,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> parloirs',
      'infoFiltered': ' - Affichés : parloirs <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> parloirs trouvés',// TODO: Remplacer "1 parloirs trouvés" par "1 parloir trouvé":
      'infoEmpty': 'Aucun parloir trouvé',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
      'lengthMenu': 'Montrer _MENU_ parloirs par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher un parloir :',
      'zeroRecords': 'Aucun parloir trouvé',
    },
    columnDefs: [
      // Créé le:
      {
        target: 0,
        searchable: false,
      },
      // Modifié le:
      {
        target: 1,
        searchable: false,
      },
      // Personne:
      {
        target: 2,
      },
      // Le:
      {
        target: 3,
      },
      // Repas:
      {
        target: 4,
      },
      // Parloir:
      {
        target: 5,
      },
      // Détails:
      {
        target: 6,
        orderable: false,
        searchable: false,
      },
    ],
  });

  $('#table-retreats').DataTable({
    order: [
      [2, 'desc'],
    ],
    pageLength: 50,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> retraites',
      'infoFiltered': ' - Affichés : retraites <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> retraites trouvés',// TODO: Remplacer "1 retraites trouvés" par "1 retraite trouvé":
      'infoEmpty': 'Aucune retraite trouvée',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
      'lengthMenu': 'Montrer _MENU_ retraites par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher une retraite :',
      'zeroRecords': 'Aucune retraite trouvée',
    },
    columnDefs: [
      // Créé le:
      {
        target: 0,
        searchable: false,
      },
      // Modifié le:
      {
        target: 1,
        searchable: false,
      },
      // Du:
      {
        target: 2,
      },
      // Durée:
      {
        target: 3,
      },
      // Détails:
      {
        target: 4,
        orderable: false,
        searchable: false,
      },
    ],
  });
});
