$(document).ready(function () {
  $('#body').keyup(function () {
    var body = $(this).val();
    if (body.length == 13) {
      body = Number(body.substring(0, 13));
      var key = 97 - (body % 97);
      body = String(body);
      if (key < 10) {
        key = "0" + String(key);
      }
      else {
        key = String(key);
      }
      $('#message').text(String(body).concat(String(key)));
    }
    else {
      $('#message').text("Veuillez entrer un code à 13 chiffres.");
    }
  })
});
