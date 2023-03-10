$(document).ready(function () {
  $('#table-monks').DataTable({
    order: [[2, 'asc']],
    // info: false,
    paging: 5,
    'language': {
      'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b>',
      'infoFiltered': ' - sur un total de <b>_MAX_</b> moines',
      'lengthMenu': 'Montrer _MENU_ moines par page',
      'paginate': {
        'previous': 'Page précédente',
        'next': 'Page suivante',
      },
      'search': 'Rechercher un moine :',
      'zeroRecords': 'Aucun moine trouvé',
    },
    columnDefs: [
      // Naissance:
      {
        target: 1,
        searchable: false,
      },
      // Entrée:
      {
        target: 2,
        searchable: false,
      },
      // Prise d'habit:
      {
        target: 3,
        orderable: false,
        searchable: false,
      },
      // Prof. temp.:
      {
        target: 4,
        orderable: false,
        searchable: false,
      },
      // Prof. perp.:
      {
        target: 5,
        orderable: false,
        searchable: false,
      },
      // Ordination:
      {
        target: 6,
        searchable: false,
      },
      // Fête:
      {
        target: 7,
        searchable: false,
      },
      // Numéro de linge:
      {
        target: 8,
        searchable: false,
      },
    ],
  });
});
