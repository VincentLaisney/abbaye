const ids_calendars = [
    'id_go_date',
    'id_back_date',
];

const ids_clocks = [
    'id_go_hour',
    'id_back_hour',
];

ids_calendars.forEach(function (id) {
    new tempusDominus.TempusDominus(document.getElementById(id), calendar);
});

ids_clocks.forEach(function (id) {
    new tempusDominus.TempusDominus(document.getElementById(id), clock);
});
