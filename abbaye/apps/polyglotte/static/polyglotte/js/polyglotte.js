$(document).ready(function () {
    var params_url = new URL(window.location).pathname.split('/');

    $('#select_books').change(function () {
        window.location = '/polyglotte/' + $('#select_books option:selected').val() + '/1';
    });

    $('#select_chapters').change(function () {
        window.location = '/polyglotte/' + $('#select_books option:selected').val() + '/' + $('#select_chapters option:selected').val();
    });

    $('#previous_book').click(function () {
        var index_current_book = $('#select_books option:selected').prop('index');
        var previous_book = $('#select_books option').eq(index_current_book - 1).val();
        window.location = '/polyglotte/' + previous_book + '/1';
    });

    $('#next_book').click(function () {
        var number_of_books = $('#select_books').prop('length');
        var index_current_book = $('#select_books option:selected').prop('index');
        var next_book = $('#select_books option').eq(index_current_book + 1).val();
        if (index_current_book == number_of_books - 1) {
            next_book = 'Gn';
        }
        window.location = '/polyglotte/' + next_book + '/1';
    });

    $('#previous_chapter').click(function () {
        var current_book = params_url[2];
        var current_chapter = params_url[3];
        if (current_chapter != 1) {
            window.location = '/polyglotte/' + current_book + '/' + (parseInt(current_chapter) - 1);
        }
    })

    $('#next_chapter').click(function () {
        var current_book = params_url[2];
        var current_chapter = params_url[3];
        if (current_chapter != $('#select_chapters').children().length) {
            window.location = '/polyglotte/' + current_book + '/' + (parseInt(current_chapter) + 1);
        }
    })
});