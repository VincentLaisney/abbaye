const ids = [
    'id_birthday',
    'id_entry',
    'id_habit',
    'id_profession_temp',
    'id_profession_perp',
    'id_priest',
    'id_death',
]

ids.forEach(function (id) {
    new tempusDominus.TempusDominus(document.getElementById(id), calendar);
});
