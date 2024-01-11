$(document).ready(function () {
  $('#table-clients').DataTable({
    order: [
      [2, 'asc'],
    ],
    pageLength: 25,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> clients',
      'infoFiltered': ' - Affichés : clients <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> clients trouvés',// TODO: Remplacer "1 clients trouvés" par "1 client trouvé":
      'infoEmpty': 'Aucun client trouvé',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
      'lengthMenu': 'Montrer _MENU_ clients par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher un client :',
      'zeroRecords': 'Aucun client trouvé',
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
      // Nom :
      {
        target: 2,
      },
      // Notes :
      {
        target: 3,
      },
      // Détails :
      {
        target: 4,
        orderable: false,
        searchable: false,
      },
    ],
  });

  $('#table-papers').DataTable({
    order: [
      [0, 'asc'],
      [1, 'asc'],
      [2, 'asc'],
      [3, 'asc'],
    ],
    pageLength: 100,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> papiers',
      'infoFiltered': ' - Affichés : papiers <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> papiers trouvés',// TODO: Remplacer "1 papiers trouvés" par "1 papier trouvé":
      'infoEmpty': 'Aucun papier trouvé',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
      'lengthMenu': 'Montrer _MENU_ papiers par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher un papier :',
      'zeroRecords': 'Aucun papier trouvé',
    },
    columnDefs: [
      // Nom :
      {
        target: 0,
      },
      // Grammage :
      {
        target: 1,
      },
      // Dimension 1 :
      {
        target: 2,
      },
      // Dimension 2 :
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

  $('#table-projects').DataTable({
    order: [
      [1, 'desc'],
    ],
    pageLength: 50,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> projets',
      'infoFiltered': ' - Affichés : projets <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> projets trouvés',// TODO: Remplacer "1 projets trouvés" par "1 projet trouvé":
      'infoEmpty': 'Aucun projet trouvé',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
      'lengthMenu': 'Montrer _MENU_ projets par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher un projet :',
      'zeroRecords': 'Aucun projet trouvé',
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
      // Nom:
      {
        target: 2,
      },
      // Client:
      {
        target: 3,
      },
      // Notes:
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
});
