// absences/form.js

$(document).ready(function () {
  // Type:
  // Si aucun des 2 boutons radio n'est cliqué (création de billet),
  // cocher l'option "Départ":
  if (!$('#id_type_0').prop('checked') && !$('#id_type_1').prop('checked')) {
    $('#id_type_0').prop('checked', true);
  }
  // Lors du clic sur un des boutons radio, refresh too:
  // $('#id_type').click(function () {
  //   refresh_type();
  // });

  // Lier le datepicker aux inputs date :
  $(function () {
    var values = {
      dateFormat: "dd/mm/yy",
      minDate: null,
      dayNames: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
      dayNamesMin: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
      monthNames: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
      monthNamesShort: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"]
    }
    $("#id_go_date").datepicker(values);
    $("#id_back_date").datepicker(values);
  });

  // Voiture/train: on change, display or hide group_train:
  $("#id_go_by").change(function () {
    if ($("#id_go_by option:selected").text() == "Train") {
      $("#group_train_go").attr("class", "d-flex");
    } else {
      $("#id_go_station").val(null);
      $("#id_go_hour").val(null);
      $("#group_train_go").attr("class", "d-none");
    }
  }).trigger('change');
  $("#id_back_by").change(function () {
    if ($("#id_back_by option:selected").text() == "Train") {
      $("#group_train_back").attr("class", "d-flex");
    } else {
      $("#id_back_station").val(null);
      $("#id_back_hour").val(null);
      $("#group_train_back").attr("class", "d-none");
    }
  }).trigger('change');

  // Checkbox all additional recipients:
  $('#checkbox_all_additional_recipients').click(function () {
    if ($(this).prop('checked')) {
      $('#id_additional_recipients').find(':checkbox').each(function () {
        $(this).prop('checked', true);
      });
    }
    else {
      $('#id_additional_recipients').find(':checkbox').each(function () {
        $(this).prop('checked', false);
      });
    }
  });

  // Additional recipients: set name in bold:
  $('[id^=id_additional_recipients_]').each(function (element) {
    $(this).parent().html($(this).parent().html().replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>'));
  });

  // On document ready, fill summary:
  refresh_type();
  refresh_summary();

  // On change: refresh summary:
  $("input, select, .form-control").on(
    'change keyup', function () {
      refresh_type();
      refresh_summary();
    }
  );

  // Refresh DOM according to type (in or out):
  function refresh_type() {
    // Si c'est un départ :
    if ($('#id_type_0').prop('checked')) {
      $('#label_check_monks').text('Sélectionnez le(s) moine(s) qui part(ent)')
      $('#go_block h2').text('DÉPART');
      $('#back_block h2').text('RETOUR');
      if ($('#id_destination').val() == "FLAVIGNY") {
        $('#id_label_destination').text('Destination (facultatif) :')
        $('#id_destination').val('');
        $('#id_destination').attr('hidden', false);
        $('#id_destination').css('color', 'rgb(33,37,41');
      }
      $('#group_servants_picnic').attr('hidden', 'false');
      $('#group_keep_hot').attr('hidden', 'false');
      $('#id_summary_label_go').text('Départ :');
      $('#id_summary_label_back').text('Retour :');
    }
    // Si c'est un retour:
    if ($('#id_type_1').prop('checked')) {
      $('#label_check_monks').text('Sélectionnez le(s) moine(s) qui arrive(nt)')
      $('#go_block h2').text('ARRIVÉE');
      $('#back_block h2').text('DÉPART');
      $('#id_destination').val('FLAVIGNY');
      $('#id_label_destination').text('Destination : Flavigny')
      $('#id_destination').attr('hidden', true);
      $('#id_destination').css('color', 'grey');
      $('#group_servants_picnic').attr('hidden', 'true');
      $('#group_keep_hot').attr('hidden', 'true');
      $('#id_summary_label_go').text('Arrivée :');
      $('#id_summary_label_back').text('Départ :');
    }
  }

  // Refresh summary:
  function refresh_summary() {
    // Monks:
    let monks = "";
    $("input[id^='id_monks']:checked").each(function (i, monk) {
      i != 0 ? monks += ', ' : '';
      monks += $(this).parent().text();
    });
    $('#monks').html(monks);

    // Destination:
    $('#destination').html($("#id_destination").val());

    // Go:
    let go = "";
    let go_date = "";
    if ($("#id_go_date").val()) {
      go_date = date_to_french_string(
        string_to_date_object($("#id_go_date").val())
      );
    }
    let go_moment = '';
    if ($("#id_go_moment").val() != '') {
      go_moment = ' (' + $("#id_go_moment").val().toLowerCase() + ')';
    }
    let go_by = '';
    if ($("#id_go_by").val() != '') {
      go_by = '</br> En ' + $("#id_go_by").val().toLowerCase();
    }
    let go_train = '';
    if ($("#id_go_by").val() == 'Train') {
      const go_station = $("#id_go_station").val() == '' ? '' : ' : ' + $("#id_go_station").val();
      const go_hour = $("#id_go_hour").val() == '' ? '' : ' à ' + $("#id_go_hour").val();
      go_train = go_station + go_hour;
    }
    const go_servants = $("#id_servants").is(':checked') ? '</br>Repas avec les serveurs' : '';
    const go_picnic = $("#id_picnic").is(':checked') ? '</br>Casse-croûte' : '';
    go = go_date + go_moment + go_by + go_train + go_servants + go_picnic;
    $('#go').html(go);

    // Back:
    let back = "";
    let back_date = "";
    if ($("#id_back_date").val()) {
      back_date = date_to_french_string(
        string_to_date_object($("#id_back_date").val())
      );
    }
    let back_moment = '';
    if ($("#id_back_moment").val() != '') {
      back_moment = ' (' + $("#id_back_moment").val().toLowerCase() + ')';
    }
    let back_by = '';
    if ($("#id_back_by").val() != '') {
      back_by = '</br> En ' + $("#id_back_by").val().toLowerCase();
    }
    let back_train = '';
    if ($("#id_back_by").val() == 'Train') {
      const back_station = $("#id_back_station").val() == '' ? '' : ' : ' + $("#id_back_station").val();
      const back_hour = $("#id_back_hour").val() == '' ? '' : ' à ' + $("#id_back_hour").val();
      back_train = back_station + back_hour;
    }
    const back_keep_hot = $("#id_keep_hot").is(':checked') ? '</br>Garder du chaud' : '';
    back = back_date + back_moment + back_by + back_train + back_keep_hot;
    $('#back').html(back);

    // Forme ordinaire:
    $('#ordinary').html(
      $("#id_ordinary_form").is(':checked')
        .toString()
        .replace('true', 'Oui').replace('false', 'Non')
    );

    // Commentaire:
    $('#comment').html($("#id_commentary").val().replace(/\n/g, '</br>'));

    // Destinataires obligatoires:
    $('#mandatory').html($(".recipients").html().replace(/<b>/g, '').replace(/<\/b>/g, ''));

    // Destinataires supplémentaires:
    let additionals = "";
    $("input[id^='id_additional_recipients']:checked").each(function (i, additional) {
      additionals += $(this).parent().text().replace(/\n /, '') + '</br>';
    });
    $('#additional').html(additionals);
  }
});
