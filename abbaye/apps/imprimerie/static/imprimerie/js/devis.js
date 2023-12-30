// imprimerie/devis.js

$(document).ready(function () {
  get_paper_and_refresh();
  $('select').change(function () {
    get_paper_and_refresh();
  });
  $('.number').on(
    'click keyup',
    function () {
      get_paper_and_refresh();
    }
  );
  $('#id_recto_verso').click(function () {
    get_paper_and_refresh();
  });
});

function get_paper_and_refresh() {
  var id_paper = $('#id_paper').val();
  $.get(
    '/abbaye/imprimerie/papers/fetch_paper_data/' + id_paper + '/',
    function (data) {
      var data_paper = JSON.parse(data)[0]['fields'];
      refresh(data_paper);
    },
    'json',
  );
}

function refresh(data_paper) {
  // Quantité :
  var quantity = Number.parseInt($('#id_quantity').val());

  // Prix fixe :
  var prix_fixe = Number.parseFloat($('#id_fixed').val());

  // Price of paper :
  var prix_mille = Number.parseFloat(data_paper['price']);
  $('#prix_mille').text(prix_mille.toFixed(2));
  var paper_cut_into = Number.parseInt($('#id_paper_cut_into').val());
  var prix_feuille = prix_mille / 1000 / paper_cut_into;
  $('#prix_feuille').text(prix_feuille.toFixed(3));
  var number_of_sheets_doc = Number.parseInt($('#id_number_of_sheets_doc').val());
  var prix_papier = number_of_sheets_doc * prix_feuille * quantity;

  // Massicot etc.:
  var prix_massicot = Number.parseInt($('#id_massicot').val());
  var prix_pelliculage = Number.parseInt($('#id_pelliculage').val());
  var prix_rainage = Number.parseInt($('#id_rainage').val());
  var prix_encollage = Number.parseInt($('#id_encollage').val());
  var prix_agrafage = Number.parseInt($('#id_agrafage').val());
  // On compte 1€ la minute :
  var prix_finition = prix_massicot + prix_pelliculage + prix_rainage + prix_encollage + prix_agrafage;

  // Total :
  $('#total span').html(
    (prix_fixe
      + prix_papier
      + prix_finition)
      .toFixed(2)
  );
}