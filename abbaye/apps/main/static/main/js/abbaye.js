$(document).ready(function () {
    // Fade out '.fade_out' elements on clik:
    $('.fade_out').click(function () {
        $(this).fadeOut('slow', function () {
            $(this).remove();
        });
    });
});

function first_letter_uppercase(string) {
    return string.substring(0, 1).toUpperCase() + string.substring(1)
}
