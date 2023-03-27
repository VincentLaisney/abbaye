$(document).ready(function () {
    // Fade out '.fade_out' elements on clik:
    $('.fade_out').click(function () {
        $(this).fadeOut('slow', function () {
            $(this).remove();
        });
    });
});
