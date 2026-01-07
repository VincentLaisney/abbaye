$(document).ready(function () {
  url = new URL(window.location);

  // Lier le datepicker aux input date :
  $(function () {
    var values = {
      dateFormat: "dd/mm/yy",
      minDate: null,
      dayNames: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
      dayNamesMin: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
      monthNames: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
      monthNamesShort: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"],
      onSelect: function () {
        if ($("#id_sejour_au").val() == "") {
          $("#id_sejour_au").val($("#id_sejour_du").val());
        }
        $("#id_sejour_au").datepicker("option", "minDate", $("#id_sejour_du").val());
        fill_repas_table();
        refresh_rooms();
      },
    }
    $("#id_sejour_du").datepicker(values);
    $("#id_sejour_au").datepicker(values);
  });

  if ($('#id_sejour_du').val() != '') {
    $('#id_sejour_au').datepicker('option', 'minDate', $('#id_sejour_du').val());
  }

  // Sejours: has the personne a pere_suiveur?
  // On start (if we are on the right page,
  // elsewhere it raises an error on the server):
  if ($('#id_mail_pere_suiveur').length) {
    check_pere_suiveur();
  }
  // On change personne:
  $('#id_personne').change(function () {
    check_pere_suiveur();
  });

  // repas détaillés
  // on start:
  fill_repas_table();
  set_repas_table();
  
  // Sejours: manage rooms (checkboxes) and selects:
  // On start:
  refresh_rooms();
  // On modif repas (selects):
  $('.sejour_date_row select').on({
    change: function () {
      refresh_rooms();
    },
  });


  // Sejours: repas_au = repas_du if sejour_du = sejour_au:
  $('#id_repas_du').on({
    change: function () {
      if ($('#id_sejour_au').val() == $('#id_sejour_du').val()) {
        $('#id_repas_au').val($('#id_repas_du option:selected').val());
      }
      refresh_rooms();
    },
  });


  // Priests: manage appearence of concerned fields:
  // On start:
  priests_block_appearance();
  // On click on "priest with mass":
  $('#id_dit_messe').change(function () {
    priests_block_appearance();
  });
});

$("#id_repas_du").on("change", function(e) {
  if (e.target.value == "Dîner") {
    if ($("#repas_0_1").is(':checked') == false) {
      $("#repas_0_1").prop('checked',  true).trigger('change');
    }
    if ($("#repas_0_2").is(':checked') == true) {
      $("#repas_0_2").prop('checked',  false).trigger('change');
    }
  } else if (e.target.value == "Déjeuner") {
    if ($("#repas_0_2").is(':checked') == false) {
      $("#repas_0_2").prop('checked',  true).trigger('change');
    }
    if ($("#repas_0_1").is(':checked') == false ) {
      $("#repas_0_1").prop('checked',  true).trigger('change');
    }
  }
});

$("#id_repas_au").on("change", function(e) {
  const nb_days = $("#id_meal_table > tbody").children().length;
  const last = nb_days - 1;
  if (e.target.value == "Dîner") {
    if ($("#repas_" + last + "_1").is(':checked') == true) {
      $("#repas_" + last + "_1").prop('checked',  false).trigger('change');
    }
    if ($("#repas_" + last + "_2").is(':checked') == false) {
      $("#repas_" + last + "_2").prop('checked',  true).trigger('change');
    }
  } else if (e.target.value == "Déjeuner") {
    if ($("#repas_" + last + "_2").is(':checked') == true) {
      $("#repas_" + last + "_2").prop('checked',  false).trigger('change');
    }
    if ($("#repas_" + last + "_1").is(':checked') == true ) {
      $("#repas_" + last + "_1").prop('checked',  false).trigger('change');
    }
  }
});


// ---------------------------------------------------------------------------------
const MS_IN_DAY = (1000 * 60 * 60 * 24)
function fill_repas_table() {
  if ($("#id_sejour_du").val() != $("#id_debut_sejour").val()) {
    // tout effacer 
    $("#id_meal_table > tbody").empty();
    $("#id_debut_sejour").val($("#id_sejour_du").val());
  }

  if ($("#id_sejour_du").val() == '' || $("#id_sejour_au").val() == '') {
    return;
  }
  
  const reg_ex = /(\d\d)\/(\d\d)\/(\d+)/;
  let begin = $("#id_sejour_du").datepicker('getDate');
  if (begin == null) {
    let sejour_begin = $("#id_sejour_du").val();
    if (sejour_begin != '') {
      let parsed = sejour_begin.match(reg_ex);
      begin = new Date(parsed[3], parsed[2] - 1, parsed[1]);
    }
  }
  let end_sejour = $("#id_sejour_au").datepicker('getDate');
  if (end_sejour == null) {
    let sejour_end = $("#id_sejour_au").val();
    if (sejour_end != '') {
      let parsed = sejour_end.match(reg_ex);
      end_sejour = new Date(parsed[3], parsed[2] - 1, parsed[1]);
    }
  }

  const nb_days = ((end_sejour - begin)/ MS_IN_DAY) + 1;
  let repas_detailles = $("#id_repas_detailles").val();
  const old_repas_detailles_ln = repas_detailles.length;
  if (repas_detailles.length != nb_days) {
    if (repas_detailles.length > nb_days) {
      repas_detailles = repas_detailles.slice(0, nb_days);
    } else {
      repas_detailles = repas_detailles + "7".repeat(nb_days - repas_detailles.length);
    }
    $("#id_repas_detailles").val(repas_detailles);
  }


  if (begin != null) {
    const len_days_repas = $("#id_meal_table > tbody").children().length;
    if (len_days_repas > nb_days) {
      for (let i = nb_days; i < len_days_repas; i++) {
        $(`#repas_${i}_1`).parent().parent().parent().remove();
      }
    }
    // on ajoute les lignes manquantes
    for (let i = len_days_repas; i < nb_days; i++) {
      let day = new Date(begin.getTime() + i * MS_IN_DAY);
      let day_formatted = $.datepicker.formatDate("D dd/mm/yy", day, {
        dayNamesShort: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
      });
      let item = $('<tr><th scope="row" >' + day_formatted + "</th>");
      $(`<td><label><input type='checkbox' id ='repas_${i}_2' checked='true' class='repas dej' style='margin: 2px 10px'/>Déjeuner</label></td>`).on(
        "change", null, {jr: `${i}`, rp: 2}, function(event) {
          ch_repas_change(event)
        }
      ).appendTo(item);
      $(`<td><label><input type='checkbox' id ='repas_${i}_1' checked='true' class='repas din' style='margin: 2px 10px'/>Dîner</label></td>`).on(
        "change", null, {jr: `${i}`, rp: 1}, function(event) {
          ch_repas_change(event)
        }
      ).appendTo(item);
      $("</tr>").appendTo(item);
      $("#id_meal_table > tbody").append(item);
    }
  }
}


function set_repas_table() {
  const str_repas_detailles = $("#id_repas_detailles").val();
  for (let jour = 0; jour < str_repas_detailles.length; jour++) {
    let chr = str_repas_detailles[jour];
    if ( (parseInt(chr) & 2) == 2 ) { // déjeuner
      $(`#repas_${jour}_2`).prop('checked', true);
    } else {
      $(`#repas_${jour}_2`).prop('checked', false);
    }
    if ( (parseInt(chr) & 1) == 1 ) { // dîner
      $(`#repas_${jour}_1`).prop('checked', true);
    } else {
      $(`#repas_${jour}_1`).prop('checked', false);
    }
  }
}


function ch_repas_change(event) {
  const jour = +(event.data["jr"]);
  const repas = +(event.data["rp"]);
  const checked = event.target.checked;
  let str_repas_detailles = $("#id_repas_detailles").val();
  let chr = str_repas_detailles[jour];
  if (checked) {
    chr = String( parseInt(chr) | repas ) 
  } else {
    chr = String( parseInt(chr) & (~repas) )
  }
  str_repas_detailles = str_repas_detailles.slice(0, jour) + chr + str_repas_detailles.slice(jour + 1)
  $("#id_repas_detailles").val(str_repas_detailles)
}


function check_pere_suiveur() {
  const green = $('#id_personne').parent().find('label').css('color');
  personne = $('#id_personne option:selected').val();
  if (personne == '') {
    $('#id_mail_pere_suiveur').prop('disabled', true);
    $('#id_mail_pere_suiveur').parent().find('label').css('color', 'rgb(150, 150, 150)');
  }
  else {
    $.get(
      '/abbaye/hotellerie/personnes/get_pere_suiveur/',
      { 'personne': personne },
      function (back) {
        $('#id_mail_pere_suiveur').prop('disabled', !(back['pere_suiveur'] && back['has_mail']));
        $('#id_mail_pere_suiveur').parent().find('label').css('color', (back['pere_suiveur'] && back['has_mail']) ? green : 'rgb(150, 150, 150)');
        if (back['pere_suiveur'] && back['has_mail']) {
          $('#id_mail_pere_suiveur').prop('checked', true);
        }
        else {
          $('#id_mail_pere_suiveur').prop('checked', false);
        }
      },
      'json',
    );
  }
}


function refresh_rooms() {
  const param_sejour = url['pathname'].split('/')[4];
  const id_sejour = param_sejour != 'create' ? param_sejour : 0;
  const sejour_du = $('#id_sejour_du').val();
  const sejour_au = $('#id_sejour_au').val();
  const repas_du = $('#id_repas_du').val();
  const repas_au = $('#id_repas_au').val();
  const green = $('#id_chambre').parent().parent().find('label').css('color');
  if (sejour_du && sejour_au) {
    $.get(
      '/abbaye/hotellerie/sejours/rooms/', {
      'id_sejour': id_sejour,
      'start': sejour_du,
      'end': sejour_au,
      'repas_start': repas_du,
      'repas_end': repas_au,
    },
      function (back) {
        for (i in back) {
          room = back[i];
          const checkbox = $(`#id_chambre input[type=checkbox][value="${i}"]`);
          if (room['occupied']) {
            checkbox.parent().css({ 'color': 'red' });
            checkbox.parent().attr('title', room['title']);
          }
          else {
            checkbox.parent().css({ 'color': green });
            checkbox.parent().attr('title', '');
          }
        }
      },
      'json',
    );
  }
}

function priests_block_appearance() {
  const green = $('#id_personne').parent().find('label').css('color');
  if ($('#id_dit_messe').prop('checked')) {
    $('#id_mail_sacristie').prop('checked', true);
  }
  else {
    $('#id_messe_premier_jour').prop('checked', false);
    $('#id_tour_messe').val('---------');
    $('#id_servant').prop('checked', false);
    $('#id_oratoire').val('---------');
    $('#id_mail_sacristie').prop('checked', false);
    $('#pretres').find('label').css('color', 'rgb(150, 150, 150)');
    $('#id_dit_messe').parent().find('label').css('color', green);
  }
  $('#id_messe_premier_jour').prop('disabled', !$('#id_dit_messe').prop('checked'));
  $('#id_tour_messe').prop('disabled', !$('#id_dit_messe').prop('checked'));
  $('#id_servant').prop('disabled', !$('#id_dit_messe').prop('checked'));
  $('#id_oratoire').prop('disabled', !$('#id_dit_messe').prop('checked'));
  $('#pretres').find('label').css('color', $('#id_dit_messe').prop('checked') ? green : 'rgb(150, 150, 150)');
  $('#id_dit_messe').parent().find('label').css('color', green);
  $('#id_mail_sacristie').prop('disabled', !$('#id_dit_messe').prop('checked'));
  $('#id_mail_sacristie').parent().find('label').css('color', $('#id_dit_messe').prop('checked') ? green : 'rgb(150, 150, 150)');
}