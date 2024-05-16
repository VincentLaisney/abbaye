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
    $('#id_date').datepicker(values);
  });

  // Initaliser l'input date à la date du jour:
  $('#id_date').val(new Date().toISOString().substring(0, 10).split('-').reverse().join('/'));
  refresh()

  // On change input date:
  $('input').change(function () {
    refresh();
  });

  // On change page, replace "." by ",":
  $('.score').keyup(function () {
    var page = $(this).val();
    page = page.replace(".", ",");
    $(this).val(page);
  })
});


// Fonction pour rafraîchir les dates :
function refresh() {
  const start = new Date($('#id_date').val().split('/')[2], $('#id_date').val().split('/')[1] - 1, $('#id_date').val().split('/')[0]);
  for (var i = 0; i < 6; i++) {
    var date = new Date(start.getTime() + (i * 24 * 3600 * 1000));
    $('#date_' + (i + 1)).text(date_to_french_string(date));
  }
}
