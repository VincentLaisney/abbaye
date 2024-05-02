$(document).ready(function () {
  url = new URL(window.location);

  $("input").change(function () {
    refresh();
  });

  $(".score").keyup(function () {
    var page = $(this).val();
    page = page.replace(".", ",");
    $(this).val(page);
  })
});

// Fonction pour rafraîchir les dates :
function refresh() {
  splitted_date = $('#start_date').val().split('/');
  start_date = [splitted_date[2], splitted_date[1], splitted_date[0]].join('-');
  $.get(
    url['href'] + 'get_dates/' + start_date + '/',
    function (dates) {
      console.log(dates);
      for (i = 0; i < 5; i++) {
        $('#DATE_' + (i + 1).toString()).text(dates[i]);
      }
    },
    'json',
  )
}
