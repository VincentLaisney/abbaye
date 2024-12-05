$(document).ready(function () {
  // Barcode:
  $('#input_barcode').keyup(function () {
    $('#image_barcode').attr('src', '');
    var barcode = $(this).val();
    if (barcode.length == 13) {
      $('#warning').text('');
      if (check_barcode(barcode)) {
        $.get(
          'create_barcode/' + barcode + '/',
          function (data) {
            if (data['status'] == 'ready') {
              $('#image_barcode').attr('src', '/media/barcode/barcode.png?' + new Date().getTime());
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

  // QR code:
  $('#input_qrcode').keyup(function () {
    var qrcode = $('#input_qrcode').val();
    if (qrcode != '') {
      $.get(
        'create_qrcode/' + qrcode + '/',
        function (data) {
          if (data['status'] == 'ready') {
            $('#image_qrcode').attr('src', '/media/barcode/qrcode.png?' + new Date().getTime());
          }
        },
        'json'
      )
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
