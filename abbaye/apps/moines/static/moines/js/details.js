// monks/details.js

$(document).ready(function () {
    // Date formatting:
    $('.details_date').each(function () {
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
});
