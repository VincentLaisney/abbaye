$(document).ready(function () {
  $('#input_barcode').keyup(function () {
    var barcode = $(this).val();
    if (barcode.length == 13) {
      $('#warning').text('')
      if (check_barcode(barcode)) {
        $.get(
          'create/' + barcode + '/',
          function (data) {
            if (data['status'] == 'ready') {
              $('#image').attr('src', '/statics/barcode/img/archives/' + barcode + '.png');
            }
          },
          'json'
        )
      }
      else {
        $('#warning').text('Code EAN erroné.');
      }
    }
    else {
      $('#image').attr('src', '');
      if (barcode.length > 13) {
        $('#warning').text('Code EAN trop long.');
      }
      else {
        $('#warning').text('');
      }
    }
  });
});

function check_barcode(barcode) {
  var result = 0;
  var i = 1;
  for (var counter = 11; counter >= 0; counter--) {
    result = result + parseInt(barcode.charAt(counter)) * (1 + (2 * (i % 2)));
    i++;
  }
  return ((10 - (result % 10)) % 10) === parseInt(barcode.charAt(12));
}
