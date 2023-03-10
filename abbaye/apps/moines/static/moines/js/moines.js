$(document).ready(function () {
  $('#table-monks').DataTable({
    order: [[2, 'asc']],
    info: false,
    paging: false,
    'language': {
      'search': '<p class="text-center mb-0">Rechercher un moine :</p>',
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
