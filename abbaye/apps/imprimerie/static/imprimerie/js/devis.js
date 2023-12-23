// imprimerie/devis.js

$(document).ready(function () {
    refresh_calculations();
    $('#id_paper').change(function () {
        refresh_calculations();
    });
    $('#id_paper_cut_into').change(function () {
        refresh_calculations();
    });
});

function refresh_calculations() {
    var id_paper = $('#id_paper').val();
    $.get(
        '/abbaye/imprimerie/papers/fetch_paper_data/' + id_paper + '/',
        function (data) {
            data = JSON.parse(data)[0]['fields'];
            console.log(data);
            var prix_mille = data['price'];
            $('#prix_mille').text(prix_mille);
            $('#prix_feuille').text((prix_mille / 1000 / $('#id_paper_cut_into').val()).toFixed(3));
        },
        'json',
    )
}
