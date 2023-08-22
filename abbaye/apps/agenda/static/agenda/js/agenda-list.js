
$('body')
    .on(
        'click',
        '.day',
        function () {
            console.log($(this).attr('data-value'));
            window.location.replace($(this).attr('data-value').split("/").reverse().join("-"));
        }
    );
