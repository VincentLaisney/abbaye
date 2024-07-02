$(document).ready(function () {
  $('#pdf').click(function () {
    $.get(
      'pdf/' + $('#select_year').val(),
      function (data) {
        console.log(data);
      },
      'json',
    )
  });
});
