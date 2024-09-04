$(document).ready(function () {
  url = new URL(window.location);

  // Create PDF:
  $('#pdf').click(function () {
    $('#overlay_wait').css({
      'display': 'flex',
      'flex-direction': 'column',
      'align-items': 'center',
      'justify-content': 'center',
    });
    $.get(
      'pdf/' + $('#select_year').val(),
      function (data) {
        if (data['status'] == 'ready') {
          $('#overlay_wait').css('display', 'none');
          $('#overlay_ready').css({
            'display': 'flex',
            'flex-direction': 'column',
            'align-items': 'center',
            'justify-content': 'center',
          });
        }
      },
      'json',
    )
  });

  // View PDF:
  $('#display_pdf').click(function () {
    $('#overlay_ready').css('display', 'none');
    console.log(url['origin'] + '/media/ordomatic/' + $('#select_year').val() + '.pdf')
    window.open(url['origin'] + '/media/ordomatic/' + $('#select_year').val() + '.pdf');
  });
});
