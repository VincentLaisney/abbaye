$(document).ready(function () {
    $('#table-clients').DataTable({
        order: [
            [2, 'desc'],
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
            // Créé le:
            {
                target: 0,
                orderable: false,
                searchable: false,
            },
            // Modifié le:
            {
                target: 1,
                orderable: false,
                searchable: false,
            },
            // Client:
            {
                target: 2,
                searchable: true,
            },
        ],
    });

    $('#table-tickets')
        // Details: fill modal when clicked on a button "Détails":
        .on(
            'click',
            '.button_details',
            function () {
                const id = $(this).attr('id').split('_')[1];
                $.get('/abbaye/absences/' + id, function (data) {
                    $('.modal-content').html(data);
                });
            }
        );
});
