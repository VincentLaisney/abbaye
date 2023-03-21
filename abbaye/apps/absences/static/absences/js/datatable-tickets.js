$(document).ready(function () {
    $('#table-tickets').DataTable({
        order: [
            [2, 'desc'],
            [3, 'desc'],
        ],
        paging: 5,
        'language': {
            'info': 'Page <b>_PAGE_</b> sur <b>_PAGES_</b> - Total : <b>_MAX_</b> billets',
            'infoFiltered': ' - Affichés : billets <b>_START_</b> à <b>_END_</b> parmi <b>_TOTAL_</b> billets trouvés',// TODO: Remplacer "1 billets trouvés" par "1 billet trouvé":
            'infoEmpty': 'Aucun billet trouvé',// TODO: Du coup supprimer le bloc 'infoFiltered', ainsi que "Page précédente" et "Page suivante".
            'lengthMenu': 'Montrer _MENU_ billets par page',
            'paginate': {
                'previous': 'Page précédente',
                'next': 'Page suivante',
            },
            'search': 'Rechercher un billet :',
            'zeroRecords': 'Aucun billet trouvé',
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
                orderable: false,
                searchable: false,
            },
            // Départ le:
            {
                target: 2,
                searchable: false,
            },
            // Retour le:
            {
                target: 3,
                searchable: false,
            },
            // Destination:
            {
                target: 4,
            },
            // Moines:
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
});
