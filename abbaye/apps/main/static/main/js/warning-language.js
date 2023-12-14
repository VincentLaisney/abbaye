// main/warning-language.js

$(document).ready(function () {
    // If browser is not set in French: display a warning, because of the datepickers:
    if (!navigator.language.includes('fr')) {
        $('#browser_language').text(navigator.language);
        $('#warning_language').attr('hidden', false);
    }
});
