$(document).ready(function () {
    $('label:contains("<i>")').each(function () {
        $(this).html(
            $(this).html().replace(/&lt;i&gt;(.*)&lt;\/i&gt;/g, "<i>$1</i > ")
        );
    });
});
