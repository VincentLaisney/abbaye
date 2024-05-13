$(document).ready(function () {
  url = new URL(window.location);

  // Lier le datepicker à l'input date:
  $(function () {
    var values = {
      dateFormat: "dd/mm/yy",
      minDate: null,
      dayNames: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
      dayNamesMin: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
      monthNames: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
      monthNamesShort: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"],
      onSelect: function () {
        window.location.href = '/abbaye/hotellerie/calendar/' + $(this).val();
      },
    }
    $("#datepicker").datepicker(values);
  });


  // Set lines height to bars height:
  // SetTimeout(200) is required to be sure the js is fired after the css.
  // TODO: setTimeout(200) is a very dirty solution…
  let bars_height;
  setTimeout(function () {
    $('#calendar_retreats .calendar_bars').ready(function () {
      bars_height = $('#calendar_retreats .calendar_bars').css('height');
      $('#calendar_retreats .vertical_line').each(function () {
        $(this).css('height', bars_height);
      });
    });
  }, 200);
  setTimeout(function () {
    $('#calendar_sejours .calendar_bars').ready(function () {
      bars_height = $('#calendar_sejours .calendar_bars').css('height');
      $('#calendar_sejours .vertical_line').each(function () {
        $(this).css('height', bars_height);
      });
    });
  }, 200);
  setTimeout(function () {
    $('#calendar_parloirs .calendar_bars').ready(function () {
      bars_height = $('#calendar_parloirs .calendar_bars').css('height');
      $('#calendar_parloirs .vertical_line').each(function () {
        $(this).css('height', bars_height);
      });
    });
  }, 200);


  // Click on 'previous week':
  $('body').on('click', '#previous_week', function () {
    const regex = /([^\/]*)\/(\d{2})\/(\d{2})\/(\d{4})/;
    const result = regex.exec(url);
    const date = new Date(parseInt(result[4]), parseInt(result[3]) - 1, parseInt(result[2]));
    const previous_date = new Date(date.getTime() - (7 * 24 * 3600 * 1000));

    let previous_day = previous_date.getDate();
    previous_day = previous_day < 10 ? '0' + previous_day : previous_day;

    let previous_month = previous_date.getMonth() + 1;
    previous_month = previous_month < 10 ? '0' + previous_month : previous_month;

    const previous_year = previous_date.getYear() + 1900;

    window.location.href = '/abbaye/hotellerie/calendar/' + previous_day + '/' + previous_month + '/' + previous_year;
  });


  // Click on 'next week':
  $('body').on('click', '#next_week', function () {
    const regex = /([^\/]*)\/(\d{2})\/(\d{2})\/(\d{4})/;
    const result = regex.exec(url);
    const date = new Date(parseInt(result[4]), parseInt(result[3]) - 1, parseInt(result[2]));
    const next_date = new Date(date.getTime() + (7 * 24 * 3600 * 1000));

    let next_day = next_date.getDate();
    next_day = next_day < 10 ? '0' + next_day : next_day;

    let next_month = next_date.getMonth() + 1;
    next_month = next_month < 10 ? '0' + next_month : next_month;

    next_year = next_date.getYear() + 1900;

    window.location.href = '/abbaye/hotellerie/calendar/' + next_day + '/' + next_month + '/' + next_year;
  });


  // Datepicker:
  // TODO: ':not(.new)' = not days in grey in the datepicker. Elsewhere bug! (displays an aberrant date).
  // $('body').on('click', '.day:not(.new)', function (e) {
  //   date = e.target.dataset.value.split('-');
  //   day = date[2];
  //   month = date[1];
  //   year = date[0];
  //   window.location.href = '/abbaye/hotellerie/calendar/' + day + '/' + month + '/' + year;
  // });
});
