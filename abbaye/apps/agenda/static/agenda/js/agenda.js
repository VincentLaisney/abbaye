// agenda/agenda.js

$(document).ready(function () {
    // Date formatting:
    $('.date').each(function () {
        // Uppercase first letter:
        const weekdays = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];
        for (const weekday of weekdays) {
            $(this).html($(this).html().replace(
                weekday,
                first_letter_uppercase(weekday)
            ));
        }
        // 1 => 1er.
        $(this).html($(this).html().replace(" 1 ", " 1er "));
    });


    $('#days_list')
        // Details: fill modal when clicked on a button "Détails":
        .on(
            'click',
            '.button_details',
            function () {
                const category = $(this).attr('id').split('_')[0];
                const id = $(this).attr('id').split('_')[1];
                if (category == "absence") {
                    $.get('/abbaye/absences/' + id, function (data) {
                        $('.modal-content').html(data);
                    });
                }
                else if (category == "event") {
                    $.get('/abbaye/agenda/' + id, function (data) {
                        $('.modal-content').html(data);
                    });
                }
            }
        );
});
