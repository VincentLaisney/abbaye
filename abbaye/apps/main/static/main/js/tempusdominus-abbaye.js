const calendar = {
    display: {
        components: {
            decades: true,
            year: true,
            month: true,
            date: true,
            hours: false,
            minutes: false,
            seconds: false
        },
        theme: 'light',
        viewMode: 'calendar',
    },
    localization: {
        today: "Aujourd'hui",
        clear: 'Effacer la sélection',
        close: 'Fermer',
        selectMonth: 'Sélectionner le mois',
        previousMonth: 'Mois précédent',
        nextMonth: 'Mois suivant',
        selectYear: "Sélectionner l'année",
        previousYear: 'Année précédente',
        nextYear: 'Année suivante',
        selectDecade: 'Sélectionner la décennie',
        previousDecade: 'Décennie précédente',
        nextDecade: 'Décennie suivante',
        previousCentury: 'Siècle précédente',
        nextCentury: 'Siècle suivante',
        selectDate: 'Sélectionner une date',
        dayViewHeaderFormat: { month: 'long', year: 'numeric' },
        locale: 'fr',
        startOfTheWeek: 0,
        dateFormats: {
            L: 'dd/MM/yyyy',
        },
        format: 'L',
    },
};

const clock = {
    display: {
        components: {
            decades: false,
            year: false,
            month: false,
            date: false,
            hours: true,
            minutes: true,
            seconds: false
        },
        theme: 'light',
        viewMode: 'clock',
    },
    localization: {
        pickHour: "Sélectionner l'heure",
        incrementHour: "Incrémenter l'heure",
        decrementHour: "Diminuer l'heure",
        pickMinute: 'Sélectionner les minutes',
        incrementMinute: 'Incrémenter les minutes',
        decrementMinute: 'Diminuer les minutes',
        pickSecond: 'Sélectionner les secondes',
        incrementSecond: 'Incrémenter les secondes',
        decrementSecond: 'Diminuer les secondes',
        toggleMeridiem: 'Basculer AM-PM',
        selectTime: "Sélectionner l'heure",
        locale: 'fr',
        dateFormats: {
            LT: 'HH:mm',
        },
        format: 'LT',
    },
};
