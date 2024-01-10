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
  var marge_papier = 1.2;
  var cout_clic_noir = 0.012;
  var cout_clic_cmjn = 0.06;
  var cout_heure = 60;

  // Quantité :
  var quantity = Number.parseInt($('#id_quantity').val());

  // Prix fixe :
  var prix_fixe = Number.parseFloat($('#id_fixed').val());

  // Recto-verso :
  var recto_verso = 1;
  if ($('#id_recto_verso').prop('checked')) {
    recto_verso = 2;
  }

  // Prix du papier :
  var prix_mille = Number.parseFloat(data_paper['price']);
  $('#prix_mille').text(prix_mille.toFixed(2));
  var paper_cut_into = Number.parseInt($('#id_paper_cut_into').val());
  var prix_feuille = prix_mille / 1000 / paper_cut_into;
  $('#prix_feuille').text(prix_feuille.toFixed(3));
  var number_of_pages_doc = Number.parseInt($('#id_number_of_pages_doc').val());
  var prix_papier = (number_of_pages_doc / $('#id_imposition').val() / recto_verso) * prix_feuille * quantity;
  $('#prix_papier').html((prix_papier * marge_papier).toFixed(2) + ' €');

  // Prix des clics :
  var nb_clics = number_of_pages_doc;
  nb_clics /= $('#id_imposition').val();
  nb_clics *= quantity;
  var prix_clics;
  if ($('#id_color').val() == "CMYN") {
    prix_clics = nb_clics * cout_clic_cmjn;
  } else if ($('#id_color').val() == "B&W") {
    prix_clics = nb_clics * cout_clic_noir;
  }
  $('#prix_clics').html(prix_clics.toFixed(2) + ' €');

  // Massicot etc.:
  var prix_massicot = Number.parseInt($('#id_massicot').val());
  var prix_pelliculage = Number.parseInt($('#id_pelliculage').val());
  var prix_rainage = Number.parseInt($('#id_rainage').val());
  var prix_encollage = Number.parseInt($('#id_encollage').val());
  var prix_agrafage = Number.parseInt($('#id_agrafage').val());
  var prix_finition = (prix_massicot + prix_pelliculage + prix_rainage + prix_encollage + prix_agrafage) * cout_heure / 60;
  $('#prix_finition').html(prix_finition.toFixed(2) + ' €');

  // Total :
  $('#prix_total').html(
    (prix_fixe
      + prix_papier
      + prix_clics
      + prix_finition)
      .toFixed(2)
    + ' €'
  );

  // Prix unitaire :
  var total = Number.parseFloat($('#prix_total').text());
  $('#prix_unitaire').html(
    (total / quantity).toFixed(2) + ' €'
  );
}
