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
      'in_1': '235',
      'ky_1': 'XVI',
      'in_2': '397',
      'ky_2': 'X',
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
