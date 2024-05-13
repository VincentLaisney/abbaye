$(document).ready(function () {
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
    $("#id_birthday").datepicker(values);
    $("#id_entry").datepicker(values);
    $("#id_habit").datepicker(values);
    $("#id_profession_temp").datepicker(values);
    $("#id_profession_perp").datepicker(values);
    $("#id_priest").datepicker(values);
    $("#id_death").datepicker(values);
  });

  $('label:contains("<i>")').each(function () {
    $(this).html(
      $(this).html().replace(/&lt;i&gt;(.*)&lt;\/i&gt;/g, "<i>$1</i > ")
    );
  });
});
