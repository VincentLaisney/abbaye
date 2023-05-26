$(document).ready(function () {
    $('#table-monks').DataTable({
        order: [[2, 'asc']],
        pageLength: 100,
        'language': {
            'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> moines',
            'infoFiltered': ' - Affichés : moines <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> moines trouvés',// TODO: Remplacer "1 moines trouvés" par "1 moine trouvé":
            'infoEmpty': 'Aucun moine trouvé',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
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

    $('#table-monks')
        // Details: fill modal when clicked on a monk:
        .on(
            'click',
            '.button_details',
            function () {
                const id = $(this).attr('id').split('_')[1];
                $.get('/abbaye/moines/' + id + '/modal/', function (data) {
                    $('.modal-content').html(data);
                });
            }
        );
});
