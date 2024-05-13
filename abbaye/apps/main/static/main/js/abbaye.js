$(document).ready(function () {
    // Fade out all the '.fade_out' elements on click.
    $('.fade_out').click(function () {
        $(this).fadeOut('slow', function () {
            $(this).remove();
        });
    });
});

function first_letter_uppercase(string) {
    // Uppercase first letter of a string.
    return string.substring(0, 1).toUpperCase() + string.substring(1)
}

function string_to_date_object(string) {
    // Return a date object from a 'dd/mm/yyyy' string.
    return new Date(string.replace(/(\d{2})\/(\d{2})\/(\d{4})/, "$2/$1/$3"))
}

function date_to_french_string(date) {
    // Return a french-formatted date from a date object.
    return (
        first_letter_uppercase(
            new Intl.DateTimeFormat(
                "fr-FR",
                {
                    dateStyle: 'full',
                }
            ).format(date)
        ).replace(' 1 ', ' 1er ')
    );
}