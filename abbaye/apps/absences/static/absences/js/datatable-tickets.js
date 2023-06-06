$(document).ready(function () {
    function formatted_date(data) {
        // Break line after first-letter-uppercased weekday:
        const weekdays = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];
        for (const weekday of weekdays) {
            data = data.replace(
                weekday,
                first_letter_uppercase(weekday) + '</br>'
            );
        }
        return data;
    };

    $('#table-tickets').DataTable({
        order: [
            [2, 'desc'],
            [3, 'desc'],
        ],
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
                render: function (data) {
                    return formatted_date(data);
                }
            },
            // Retour le:
            {
                target: 3,
                searchable: false,
                render: function (data) {
                    return formatted_date(data);
                }
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
