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
  $('#id_recto_verso, #id_fibers').click(function () {
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
  $('#frais_fixes').html(prix_fixe.toFixed(2) + ' €');

  // Recto-verso :
  var recto_verso = 1;
  if ($('#id_recto_verso').prop('checked')) {
    recto_verso = 2;
  }

  // Fibres:
  var fibers = true;
  if (!$('#id_fibers').prop('checked')) {
    fibers = false;
  }

  // Prix du papier :
  var prix_mille = Number.parseFloat(data_paper['price']);
  $('#prix_mille').text(prix_mille.toFixed(2));
  var paper_cut_into = Number.parseInt($('#id_paper_cut_into').val());
  var prix_feuille = prix_mille / 1000 / paper_cut_into;
  $('#prix_feuille').text(prix_feuille.toFixed(3));
  var number_of_pages_doc = Number.parseInt($('#id_number_of_pages_doc').val());
  var nb_feuilles_machine = (number_of_pages_doc / $('#id_imposition').val() / recto_verso) * quantity;
  $('#nb_feuilles_machine').html(nb_feuilles_machine);
  var prix_papier = nb_feuilles_machine * prix_feuille * marge_papier;
  $('#prix_papier').html(prix_papier.toFixed(2) + ' €');

  // Meilleure imposition :
  var paper_dim1_machine = Number.parseInt($('#id_paper_dim1_machine').val());
  var paper_dim2_machine = Number.parseInt($('#id_paper_dim2_machine').val());
  var file_width = Number.parseInt($('#id_file_width').val());
  var file_height = Number.parseInt($('#id_file_height').val());
  var margins = Number.parseInt($('#id_margins').val());
  var paper_dim1 = paper_dim1_machine - (margins * 2);
  var paper_dim2 = paper_dim2_machine - (margins * 2);
  var gutters_width = Number.parseInt($('#id_gutters_width').val());
  var gutters_height = Number.parseInt($('#id_gutters_height').val());
  var prop_according_fibers, prop_against_fibers, best_imposition;
  // Proposition dans le sens des fibres:
  var file_width_in_dim1 = Math.floor((paper_dim1 + gutters_width) / (file_width + gutters_width));
  var file_height_in_dim2 = Math.floor((paper_dim2 + gutters_height) / (file_height + gutters_height));
  prop_according_fibers = file_width_in_dim1 * file_height_in_dim2;
  best_imposition = prop_according_fibers;
  if (!fibers) {
    // Proposition contre le sens des fibres:
    var file_width_in_dim2 = Math.floor((paper_dim2 + gutters_width) / (file_width + gutters_width));
    var file_height_in_dim1 = Math.floor((paper_dim1 + gutters_height) / (file_height + gutters_height));
    prop_against_fibers = file_width_in_dim2 * file_height_in_dim1;
    if (prop_against_fibers > prop_according_fibers) {
      best_imposition = prop_against_fibers;
    }
  }
  $('#id_imposition').val(best_imposition);

  // Prix des clics :
  var nb_clics = number_of_pages_doc;
  nb_clics /= $('#id_imposition').val();
  nb_clics *= quantity;
  $('#nb_clics').html(nb_clics);
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
  var total = prix_fixe + prix_papier + prix_clics + prix_finition;
  $('#id_total').val(
    total.toFixed(2)
  );

  // Prix unitaire :
  $('#prix_unitaire').html(
    (total / quantity).toFixed(2) + ' €'
  );
}
