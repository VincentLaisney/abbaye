$(document).ready(function () {
  url = new URL(window.location);

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
    $('#start').datepicker(values);
  });

  // Initaliser l'input date à la date du jour:
  $('#start').val(new Date().toISOString().substring(0, 10).split('-').reverse().join('/'));
  refresh()

  // On change input date:
  $('#start').change(function () {
    refresh();
  });

  // On change page, replace "." by ",":
  $('.score').keyup(function () {
    var page = $(this).val();
    page = page.replace(".", ",");
    $(this).val(page);
  })

  // View PDF:
  $('#pdf').click(function () {
    const data = {
      'start': $('#start').val(),
    };
    for (i = 1; i < 6; i++) {
      data['date_' + String(i)] = $('#date_' + String(i)).text();
      data['in_' + String(i)] = $('#in_' + String(i)).val();
      data['gr_' + String(i)] = $('#gr_' + String(i)).val();
      data['al_' + String(i)] = $('#al_' + String(i)).val();
      data['of_' + String(i)] = $('#of_' + String(i)).val();
      data['co_' + String(i)] = $('#co_' + String(i)).val();
      data['ky_' + String(i)] = $('#ky_' + String(i)).val();
      data['gl_' + String(i)] = $('#gl_' + String(i)).val();
      data['sa_' + String(i)] = $('#sa_' + String(i)).val();
      data['cr_' + String(i)] = $('#cr_' + String(i)).val();
    }
    $.get(
      url['href'] + 'pdf/',
      data,
      function (back) {
        console.log(back);
      }
    )
  });
});

// Fonction pour rafraîchir les dates :
function refresh() {
  const start = new Date($('#start').val().split('/')[2], $('#start').val().split('/')[1] - 1, $('#start').val().split('/')[0]);
  for (var i = 0; i < 6; i++) {
    var date = new Date(start.getTime() + (i * 24 * 3600 * 1000));
    $('#date_' + (i + 1)).text(date_to_french_string(date));
  }
}
