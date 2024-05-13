$(document).ready(function () {
  // Lier le datepicker à l'input date :
  $(function () {
    var values = {
      dateFormat: "dd/mm/yy",
      minDate: null,
      dayNames: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
      dayNamesMin: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
      monthNames: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
      monthNamesShort: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"]
    }
    $("#id_date_from").datepicker(values);
    $("#id_date_to").datepicker(values);
  });

  // Date formatting:
  $('.date').each(function () {
    // Uppercase first letter:
    const weekdays = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];
    for (const weekday of weekdays) {
      $(this).html($(this).html().replace(
        weekday,
        first_letter_uppercase(weekday)
      ));
    }
    // 1 => 1er.
    $(this).html($(this).html().replace(" 1 ", " 1er "));
  });

  $('#id_date_from').on('change', function () {
    $('#id_date_to').val($('#id_date_from').val());
  });

  $('#days_list')
    // Details: fill modal when clicked on a button "Détails":
    .on(
      'click',
      '.button_details',
      function () {
        const category = $(this).attr('id').split('_')[0];
        const id = $(this).attr('id').split('_')[1];
        if (category == "absence") {
          $.get('/abbaye/absences/' + id, function (data) {
            $('.modal-content').html(data);
          });
        }
        else if (category == "event") {
          $.get('/abbaye/agenda/' + id, function (data) {
            $('.modal-content').html(data);
          });
        }
      }
    );
});
