$(document).ready(function () {
  url = new URL(window.location);

  // On change "mode":
  $('#mode_mg').click(function () {
    $('#number_of_days').removeAttr('disabled');
  });
  $('#mode_full').click(function () {
    $('#number_of_days').attr('disabled', 'true');
    $('#number_of_days').val('1');
    refresh();
  });

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

  // On change number of days:
  $('#number_of_days').click(function () {
    refresh();
  });

  // On change input date:
  $('#start').change(function () {
    refresh();
  });

  // On change page, replace "." by "_":
  $('.score').keyup(function () {
    var page = $(this).val();
    page = page.replace(".", "_");
    $(this).val(page);
  });

  // Check score exists:
  $('.score').focusout(function () {
    var input = $(this);
    var type = $(this).attr('id').toUpperCase().substring(0, 2);
    var score = $(this).val();
    if (['IN', 'GR', 'AL', 'OF', 'CO'].indexOf(type) != -1 && score != '') {
      $.get(
        url['href'] + 'score/',
        {
          'type': type,
          'score': score,
        },
        function (back) {
          input.css('color', back['color']);
          input.attr('title', back['title']);
        }
      )
    }
  });

  // Create PDF:
  $('#pdf').click(function () {
    $('#overlay_wait').css({
      'display': 'flex',
      'flex-direction': 'column',
      'align-items': 'center',
      'justify-content': 'center',
    });
    const data = {
      'mode': $('#mode input[type=radio]:checked').attr('id'),
      'start': $('#start').val(),
      'number_of_days': $('#number_of_days').val(),
    };
    for (i = 1; i <= Number($('#number_of_days').val()); i++) {
      data['date_' + String(i)] = $('#date_' + String(i)).text();
      data['special_' + String(i)] = $('#special_' + String(i) + ' option:selected').val();
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
        if (back['back'] == "OK") {
          $('#overlay_wait').css('display', 'none');
          $('#overlay_ready').css({
            'display': 'flex',
            'flex-direction': 'column',
            'align-items': 'center',
            'justify-content': 'center',
          });
        }
      }
    )
  });

  // View PDF:
  $('#display_pdf').click(function () {
    $('#overlay_ready').css('display', 'none');
    window.open(url['origin'] + '/media/livrets/livret.pdf');
  });
});

// Refresh the grid:
function refresh() {
  // Hide/show rows:
  for (var i = Number($('#number_of_days').val()); i < 8; i++) {
    $('#row_' + (i + 1)).hide();
  }
  for (var i = 1; i <= Number($('#number_of_days').val()); i++) {
    $('#row_' + i).show();
  }

  // Display dates:
  const start = new Date($('#start').val().split('/')[2], $('#start').val().split('/')[1] - 1, $('#start').val().split('/')[0]);
  for (var i = 0; i < Number($('#number_of_days').val()); i++) {
    var date = new Date(start.getTime() + (i * 24 * 3600 * 1000));
    $('#date_' + (i + 1)).text(date_to_french_string(date));
  }
}
