
// Lier le datepicker aux input date :
$(function () {
  var values = {
    dateFormat: "dd/mm/yy",
    minDate: null,
    dayNames: ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"],
    dayNamesMin: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
    monthNames: ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
    monthNamesShort: ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Aoû", "Sep", "Oct", "Nov", "Déc"]
  }
  $("#id_sejour_du").datepicker(values);// Séjours
  $("#id_sejour_au").datepicker(values);// Séjours
  $("#id_date").datepicker(values);// Parloirs
  $("#id_date_from").datepicker(values);// Retraites
});
